import os
import re
from datetime import datetime
import yaml

def check_revisions(vault_path):
    """
    Scans all markdown files in the vault and finds notes due today or overdue.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    due_notes = []

    for root, _, files in os.walk(vault_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except Exception:
                    continue

                # Parse frontmatter
                match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL | re.MULTILINE)
                if not match:
                    continue
                
                try:
                    metadata = yaml.safe_load(match.group(1))
                except Exception:
                    continue

                if metadata and 'revisions' in metadata:
                    revisions = metadata['revisions']
                    if isinstance(revisions, list):
                        # Find all pending dates <= today
                        for rev_date in revisions:
                            rev_date_str = str(rev_date)
                            if rev_date_str <= today:
                                # Check if this specific revision is marked as [x] (done)
                                done_pattern = rf"- \[x\] .*?\({rev_date_str}\)"
                                if not re.search(done_pattern, content):
                                    rel_path = os.path.relpath(file_path, vault_path)
                                    
                                    # Try to find which day label it is (e.g., Day 2)
                                    label_match = re.search(rf"- \[ \] (Day \d+) Revision \({rev_date_str}\)", content)
                                    label = label_match.group(1) if label_match else "Revision"
                                    
                                    due_notes.append(f"{rel_path} ({label} - {rev_date_str})")
                                    break # Only add a file once even if multiple revisions are due
    
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
