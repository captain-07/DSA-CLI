import subprocess
import os

def sync_to_git(vault_path: str, problem_name: str):
    """
    Performs git add, commit, and push in the vault directory.
    """
    try:
        print(f"🔄 Syncing to GitHub: '{problem_name}'")
        
        # 1. git add .
        subprocess.run(["git", "add", "."], cwd=vault_path, check=True, capture_output=True, text=True)
        
        # 2. git commit -m "problem name"
        commit_message = f"Note: {problem_name}"
        subprocess.run(["git", "commit", "-m", commit_message], cwd=vault_path, check=True, capture_output=True, text=True)
        
        # 3. git push
        subprocess.run(["git", "push"], cwd=vault_path, check=True, capture_output=True, text=True)
        
        print("🚀 Successfully pushed to GitHub!")
        
    except subprocess.CalledProcessError as e:
        if "nothing to commit" in e.stdout or "nothing to commit" in e.stderr:
            print("ℹ️  No changes to commit.")
        else:
            print(f"❌ Git error: {e.stderr or e.stdout}")
    except Exception as e:
        print(f"❌ Unexpected error during git sync: {e}")
