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

        for current_model in models_to_try:
            print(f"🤖 Attempting generation with model: {current_model}")
            
            # 3 Retries for quality validation per model
            for attempt in range(1, 4):
                try:
                    # Use shell=True for Windows command resolution (.cmd)
                    # We pass the command as a single string when shell=True for best compatibility
                    full_cmd = f'{cmd} --model {current_model}'
                    
                    result = subprocess.run(
                        full_cmd,
                        input=prompt,
                        capture_output=True,
                        text=True,
                        check=True,
                        encoding="utf-8",
                        shell=True
                    )
                    
                    raw_output = result.stdout.strip()
                    if not raw_output:
                        continue
                    
                    # Validate the output
                    is_valid, message = NoteValidator.validate(raw_output)
                    if is_valid:
                        print(f"✅ Attempt {attempt}: Quality validation passed.")
                        return raw_output
                    else:
                        print(f"⚠️ Attempt {attempt}: Validation failed ({message})")
                        best_attempt = raw_output
                
                except subprocess.CalledProcessError as e:
                    # If the command itself fails (e.g. model not found), 
                    # don't retry validation for this model
                    print(f"❌ Model {current_model} failed or not available.")
                    break 
                except Exception as e:
                    print(f"❌ Unexpected error with {current_model}: {e}")
                    break

        if best_attempt:
            print("⚠️ Returning best available attempt (failed strict validation).")
            return best_attempt
            
        return None
    except Exception as e:
        print(f"❌ Critical error in generation: {e}")
        return None
