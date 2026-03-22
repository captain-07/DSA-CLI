import subprocess
import os
import sys

PROMPT_TEMPLATE = "templates/prompt.txt"

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
        
        for current_model in models_to_try:
            try:
                print(f"🤖 Calling AI ({current_model})...")
                result = subprocess.run(
                    ["gemini", "--model", current_model],
                    input=prompt,
                    capture_output=True,
                    text=True,
                    check=True,
                    encoding="utf-8",
                    shell=True
                )
                if result.stdout.strip():
                    return result.stdout.strip()
                print(f"⚠️ Model {current_model} returned empty response.")
            except subprocess.CalledProcessError as e:
                print(f"⚠️ Error calling {current_model}: {e}")
                continue
            except Exception as e:
                print(f"⚠️ Unexpected error with {current_model}: {e}")
                continue
        
        return None
    except Exception as e:
        print(f"❌ Critical error in generation: {e}")
        return None
