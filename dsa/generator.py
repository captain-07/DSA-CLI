import subprocess
import os
import sys
from pathlib import Path
from .validator import NoteValidator

PROMPT_TEMPLATE = Path(__file__).parent.parent / "templates" / "prompt.txt"

def get_gemini_command():
    """Returns the correct command to call Gemini CLI based on OS."""
    if os.name == "nt":
        # On Windows, 'gemini.cmd' is the most reliable shim for npm packages.
        # Avoid .ps1 as it often opens in Notepad.
        return "gemini.cmd"
    return "gemini"

def generate_notes(problem_name, mistake, model="auto", fallback_models=None):
    """
    Calls the Gemini CLI and implements a quality validation retry mechanism.
    """
    if not os.path.exists(PROMPT_TEMPLATE):
        raise FileNotFoundError(f"Prompt template not found at {PROMPT_TEMPLATE}")

    try:
        with open(PROMPT_TEMPLATE, "r", encoding="utf-8") as f:
            template = f.read()

        prompt = template.format(problem_name=problem_name, mistake=mistake)
        
        models_to_try = [model]
        if fallback_models:
            # Avoid duplicates while preserving order
            for m in fallback_models:
                if m not in models_to_try:
                    models_to_try.append(m)
        
        cmd = get_gemini_command()
        best_attempt = None
        attempts_made = 0

        for current_model in models_to_try:
            attempts_made += 1
            print(f"🤖 Attempting generation with model: {current_model} (Attempt {attempts_made})")
            
            try:
                # Use shell=True for Windows command resolution (.cmd)
                full_cmd = f'{cmd} --model {current_model}'
                
                result = subprocess.run(
                    full_cmd,
                    input=prompt,
                    capture_output=True,
                    text=True,
                    check=True,
                    encoding="utf-8",
                    shell=True,
                    timeout=90 # 90 second timeout for each model call
                )
                
                raw_output = result.stdout.strip()
                if not raw_output:
                    print(f"⚠️ Model {current_model} returned empty output.")
                    continue
                
                # Validate the output
                is_valid, message = NoteValidator.validate(raw_output)
                if is_valid:
                    print(f"✅ Quality validation passed with {current_model}.")
                    return raw_output
                else:
                    print(f"⚠️ Validation failed for {current_model}: {message}")
                    # Keep the first reasonable attempt if we don't have one yet
                    if best_attempt is None:
                        best_attempt = raw_output
                    
                    # If we've already tried two models (primary + 1 fallback), stop wasting requests
                    if attempts_made >= 2:
                        print("🛑 Stopping after 2 attempts to save requests. Using best attempt.")
                        break
            
            except subprocess.TimeoutExpired:
                 print(f"❌ Model {current_model} timed out after 90s.")
                 if attempts_made >= 3: # Allow more models if they are just timing out/failing
                     break
                 continue
            except subprocess.CalledProcessError as e:
                print(f"❌ Model {current_model} failed (Exit code: {e.returncode}).")
                continue
            except Exception as e:
                print(f"❌ Unexpected error with {current_model}: {e}")
                continue

        if best_attempt:
            print("⚠️ Returning best available attempt (failed strict validation).")
            return best_attempt
            
        return None
    except Exception as e:
        print(f"❌ Critical error in generation: {e}")
        return None
