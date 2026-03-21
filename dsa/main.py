import argparse
import sys
import os
from .config import load_config
from .parser import parse_input
from .generator import generate_notes
from .formatter import clean_output
from .router import detect_folder
from .saver import save_note

def main():
    """Main CLI execution flow."""
    parser = argparse.ArgumentParser(description="🚀 DSA Note Generator - Structured & Obsidian Ready")
    parser.add_argument("input", help='Problem: "Problem Name | Optional Note"')
    parser.add_argument("--model", help="Gemini model override (default from config.json)")
    
    args = parser.parse_args()
    
    print("\n--- 🚀 DSA-CLI: Initializing ---")
    
    # 1. Load config
    config = load_config()
    vault_path = config.get("vault_path", "./vault")
    model = args.model or config.get("model", "gemini-2.0-flash")
    
    if not os.path.exists(vault_path):
        print(f"⚠️ Warning: Vault path '{vault_path}' not found. Creating it...")
        os.makedirs(vault_path, exist_ok=True)
    
    # 2. Parse input
    try:
        problem_name, mistake = parse_input(args.input)
        print(f"🧠 Parsing Input: '{problem_name}'")
    except Exception as e:
        print(f"❌ Error parsing input: {e}")
        sys.exit(1)
    
    # 3. Generate content via AI
    print(f"🤖 Calling AI ({model})... (Be patient, quality takes time)")
    raw_output = generate_notes(problem_name, mistake, model=model)
    
    if not raw_output:
        print("❌ Error: Failed to generate notes from AI.")
        sys.exit(1)
        
    # 4. Format/clean
    print("🧹 Cleaning and formatting note...")
    formatted_content = clean_output(raw_output)
    
    # 5. Route to correct folder
    folder = detect_folder(formatted_content)
    print(f"📁 Target Folder: DSA/{folder}")
    
    # 6. Save note
    try:
        final_path = os.path.abspath(save_note(vault_path, folder, problem_name, formatted_content))
        print(f"\n✅ SUCCESS! Your note is ready.")
        print(f"📍 Location: {final_path}")
    except Exception as e:
        print(f"❌ Error saving note: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
