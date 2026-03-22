import os
import re
from datetime import datetime
import yaml

def parse_metadata(file_path):
    """
    Parses the YAML frontmatter of a markdown file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Use search instead of match to handle potential leading newlines
            match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL | re.MULTILINE)
            if match:
                return yaml.safe_load(match.group(1))
    except Exception as e:
        # print(f"⚠️ Error parsing {file_path}: {e}")
        pass
    return None

def check_revisions(vault_path):
    """
    Scans all markdown files in the vault and finds notes due today.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    due_notes = []

    for root, _, files in os.walk(vault_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                metadata = parse_metadata(file_path)
                
                if metadata and 'revisions' in metadata:
                    revisions = metadata['revisions']
                    if isinstance(revisions, list):
                        # Some dates might be stored as datetime objects by yaml.safe_load
                        # so we convert them to strings
                        revisions_str = [str(r) for r in revisions]
                        if today in revisions_str:
                            rel_path = os.path.relpath(file_path, vault_path)
                            due_notes.append(rel_path)
    
    return due_notes

def show_due_notes(vault_path):
    """
    Prints a list of due notes.
    """
    print("\n--- 📚 REVISION SYSTEM ---")
    print(f"Checking for notes due on {datetime.now().strftime('%Y-%m-%d')}...")
    
    due_notes = check_revisions(vault_path)
    
    if not due_notes:
        print("✅ No notes due for revision today! Keep grinding! 💪")
    else:
        print(f"🔔 You have {len(due_notes)} note(s) to revise today:")
        for note in due_notes:
            print(f"  - {note}")
        print("\n📝 Make sure to review the logic, implementation, and dry-run table.")
