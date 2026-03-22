import os
import re

def sanitize_filename(name: str) -> str:
    """
    Makes problem name safe for the filesystem.
    Converts 'Two Sum' -> 'Two_Sum', '3Sum' -> '3Sum'.
    Removes special characters but keeps spaces (initially) or replaces with underscores.
    """
    # Replace non-alphanumeric (except space/dash) with empty
    clean = re.sub(r"[^a-zA-Z0-9\-\s]", "", name)
    # Replace multiple spaces/dashes with single underscore
    clean = re.sub(r"[\s\-]+", "_", clean)
    return clean.strip("_")

def save_note(vault_root: str, folder: str, problem_name: str, content: str) -> str:
    """
    Saves the note in {vault_root}/{folder}/{problem_name}.md
    """
    # Use vault_root directly as it is already the DSA folder
    folder_path = os.path.join(vault_root, folder)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)

    filename = f"{sanitize_filename(problem_name)}.md"
    file_path = os.path.join(folder_path, filename)
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return file_path
    except IOError as e:
        print(f"Failed to write file {file_path}: {e}")
        raise
