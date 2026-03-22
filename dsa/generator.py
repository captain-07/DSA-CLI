import subprocess
import os
import sys

from pathlib import Path

PROMPT_TEMPLATE = Path(__file__).parent.parent / "templates" / "prompt.txt"

def generate_notes(problem_name, mistake, model="auto", fallback_models=None):
    """
    Calls the Gemini CLI with the prompt template via stdin.
    Tries fallback models if the primary model fails.
    """
    if not os.path.exists(PROMPT_TEMPLATE):
        raise FileNotFoundError(f"Prompt template not found at {PROMPT_TEMPLATE}")

    try:
        with open(PROMPT_TEMPLATE, "r", encoding="utf-8") as f:
            template = f.read()

        prompt = template.format(problem_name=problem_name, mistake=mistake)
        
        models_to_try = [model]
        if fallback_models:
            models_to_try.extend(fallback_models)
        
        # Determine the gemini executable to use. 
        # On Windows, try 'gemini', then 'gemini.cmd', then 'gemini.ps1'.
        # On Unix, 'gemini' should suffice.
        gemini_execs = ["gemini"]
        if os.name == "nt":
            gemini_execs.extend(["gemini.cmd", "gemini.ps1"])

        for current_model in models_to_try:
            for exec_name in gemini_execs:
                try:
                    print(f"🤖 Calling AI ({current_model}) using {exec_name}...")
                    result = subprocess.run(
                        [exec_name, "--model", current_model],
                        input=prompt,
                        capture_output=True,
                        text=True,
                        check=True,
                        encoding="utf-8",
                        shell=True
                    )
                    if result.stdout.strip():
                        return result.stdout.strip()
                    print(f"⚠️ Model {current_model} with {exec_name} returned empty response.")
                except subprocess.CalledProcessError as e:
                    # If this executable failed, try the next one or model.
                    continue
                except Exception as e:
                    # Catch other errors, like WinError 2.
                    continue
        
        return None
    except Exception as e:
        print(f"❌ Critical error in generation: {e}")
        return None
