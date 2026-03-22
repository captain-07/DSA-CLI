import argparse
import sys
import os
from .config import load_config
from .parser import parse_input
from .generator import generate_notes
from .formatter import clean_output
from .router import detect_folder
from .saver import save_note
from .reviser import show_due_notes

def main():
    """Main CLI execution flow."""
    parser = argparse.ArgumentParser(description="🚀 DSA Note Generator - Structured & Obsidian Ready")
    
    # Use subparsers for 'revise' command
    subparsers = parser.add_subparsers(dest="command")
    
    # 'generate' command (default-like behavior)
    gen_parser = subparsers.add_parser("generate", help="Generate a new DSA note")
    gen_parser.add_argument("input", help='Problem: "Problem Name | Optional Note"')
    gen_parser.add_argument("--model", help="Gemini model override")

    # 'revise' command
    subparsers.add_parser("revise", help="Check for notes due for revision today")

    # Compatibility: if no command is given but an argument exists, assume 'generate'
    if len(sys.argv) > 1 and sys.argv[1] not in ["generate", "revise", "-h", "--help"]:
        # Prepend 'generate' to sys.argv for backward compatibility
        sys.argv.insert(1, "generate")

    args = parser.parse_args()
    
    config = load_config()
    vault_path = config.get("vault_path", "./vault")
    
    if not os.path.exists(vault_path):
        os.makedirs(vault_path, exist_ok=True)

    if args.command == "revise":
        show_due_notes(vault_path)
        return

    # Default to generate
    if args.command == "generate":
        print("\n--- 🚀 DSA-CLI: Initializing ---")
        
        model = args.model or config.get("model", "auto")
        fallback_models = config.get("fallback_models", [])
        
        # Parse input
        try:
            problem_name, mistake = parse_input(args.input)
            print(f"🧠 Parsing Input: '{problem_name}'")
        except Exception as e:
            print(f"❌ Error parsing input: {e}")
            sys.exit(1)
        
        # 3. Generate content via AI
        raw_output = generate_notes(problem_name, mistake, model=model, fallback_models=fallback_models)
        
        if not raw_output:
            print("❌ Error: Failed to generate notes from AI.")
            sys.exit(1)
            
        # 4. Format/clean
        print("🧹 Cleaning and formatting note...")
        formatted_content = clean_output(raw_output)
        
        # 5. Route to correct folder
        folder = detect_folder(formatted_content)
        print(f"📁 Target Folder: {folder}")
        
        # 6. Save note
        try:
            final_path = os.path.abspath(save_note(vault_path, folder, problem_name, formatted_content))
            print(f"\n✅ SUCCESS! Your note is ready.")
            print(f"📍 Location: {final_path}")
        except Exception as e:
            print(f"❌ Error saving note: {e}")
            sys.exit(1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
