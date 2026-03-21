import subprocess
import os
import sys

PROMPT_TEMPLATE = "templates/prompt.txt"

def generate_notes(problem_name, mistake, model="gemini-2.0-flash"):
    """
    Calls the Gemini CLI with the prompt template via stdin for robustness.
    """
    if not os.path.exists(PROMPT_TEMPLATE):
        raise FileNotFoundError(f"Prompt template not found at {PROMPT_TEMPLATE}")

    try:
        with open(PROMPT_TEMPLATE, "r", encoding="utf-8") as f:
            template = f.read()

        # Fill in placeholders
        prompt = template.format(problem_name=problem_name, mistake=mistake)
        
        # Use stdin to avoid command-line length limits (especially on Windows)
        # gemini --model model_name
        result = subprocess.run(
            ["gemini", "--model", model],
            input=prompt,
            capture_output=True,
            text=True,
            check=True,
            encoding="utf-8"
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Error calling Gemini CLI: {e}")
        if e.stdout:
            print(f"Stdout: {e.stdout}")
        if e.stderr:
            print(f"Stderr: {e.stderr}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error in generation: {e}")
        return None
