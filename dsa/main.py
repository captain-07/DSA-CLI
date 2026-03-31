import argparse
import sys
import os
import glob
from .config import load_config
from .parser import parse_input
from .generator import generate_notes
from .formatter import clean_output
from .router import detect_folder
from .saver import save_note, sanitize_filename
from .sync import sync_to_git
from .reviser import show_due_notes

def check_existing_note(vault_path, problem_name):
    """
    Checks if a note with the same name already exists in the vault (any folder).
    Returns the path if found, else None.
    """
    safe_name = sanitize_filename(problem_name)
    # Search recursively for safe_name.md
    search_pattern = os.path.join(vault_path, "**", f"{safe_name}.md")
    matches = glob.glob(search_pattern, recursive=True)
    return matches[0] if matches else None

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
        
        # 1. Parse input
        try:
            problem_name, mistake = parse_input(args.input)
            print(f"🧠 Parsing Input: '{problem_name}'")
        except Exception as e:
            print(f"❌ Error parsing input: {e}")
            sys.exit(1)

        # 2. Check for existing note
        existing_path = check_existing_note(vault_path, problem_name)
        if existing_path:
            print(f"⚠️  Note already exists: '{os.path.relpath(existing_path, vault_path)}'")
            print("💡 This will overwrite the existing file with updated content.")
        
        # 3. Generate content via AI
        model = args.model or config.get("model", "auto")
        fallback_models = config.get("fallback_models", [])
        
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
            
            # 7. Sync to Git
            sync_to_git(vault_path, problem_name)
            
        except Exception as e:
            print(f"❌ Error saving note: {e}")
            sys.exit(1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
