import os
import re
from datetime import datetime, timedelta

def sanitize_filename(name: str) -> str:
    """
    Makes problem name safe for the filesystem.
    """
    clean = re.sub(r"[^a-zA-Z0-9\-\s]", "", name)
    clean = re.sub(r"[\s\-]+", "_", clean)
    return clean.strip("_")

def generate_frontmatter(created_date: str):
    """
    Generates YAML frontmatter with revision dates (D+2, D+7, D+15, D+30).
    """
    base_date = datetime.strptime(created_date, "%Y-%m-%d")
    revisions = [
        (base_date + timedelta(days=2)).strftime("%Y-%m-%d"),
        (base_date + timedelta(days=7)).strftime("%Y-%m-%d"),
        (base_date + timedelta(days=15)).strftime("%Y-%m-%d"),
        (base_date + timedelta(days=30)).strftime("%Y-%m-%d")
    ]
    
    frontmatter = "---\n"
    frontmatter += f"created: {created_date}\n"
    frontmatter += "revisions:\n"
    for rev in revisions:
        frontmatter += f"  - {rev}\n"
    frontmatter += "---\n\n"
    return frontmatter

def generate_revision_checklist(created_date: str):
    """
    Generates a revision checklist for the bottom of the note.
    """
    base_date = datetime.strptime(created_date, "%Y-%m-%d")
    intervals = [2, 7, 15, 30]
    
    checklist = "\n\n---\n### 🔄 Revision Checklist\n"
    for days in intervals:
        rev_date = (base_date + timedelta(days=days)).strftime("%Y-%m-%d")
        checklist += f"- [ ] Day {days} Revision ({rev_date})\n"
    return checklist

def save_note(vault_root: str, folder: str, problem_name: str, content: str) -> str:
    """
    Saves the note in {vault_root}/{folder}/{problem_name}.md with metadata.
    """
    folder_path = os.path.join(vault_root, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)

    filename = f"{sanitize_filename(problem_name)}.md"
    file_path = os.path.join(folder_path, filename)
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Obsidian frontmatter MUST be at the very top
    frontmatter = generate_frontmatter(today)
    
    # Combined checklist at the bottom
    checklist = generate_revision_checklist(today)
    
    final_content = frontmatter + content + checklist
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(final_content)
        return file_path
    except IOError as e:
        print(f"Failed to write file {file_path}: {e}")
        raise
