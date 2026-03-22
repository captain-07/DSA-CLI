# DSA-CLI 🚀

A production-ready CLI tool to convert a single-line input into structured DSA notes and save them into an Obsidian vault.

## 🛠 Features
- **Fast Input:** Just `python -m dsa.main "Problem Name | My Mistake"`
- **AI-Powered:** Defaults to `auto` (resolves to the most powerful Gemini model available).
- **Robust Fallbacks:** Automatically tries fallback models if the primary model is unavailable.
- **Smart Routing:** Automatically maps problems to folders (Arrays, DP, Graph, etc.).
- **Obsidian Ready:** Saves in Markdown with tags and revision checklists in your specified vault.

## 📦 Installation
1. Clone the repository.
2. Ensure you have the `gemini` CLI installed and authenticated.
3. Update `config.json` with your Obsidian vault path.

## ⚙️ Configuration (`config.json`)
```json
{
  "vault_path": "C:\\Users\\USER\\OneDrive\\Documents\\Desktop\\Obsidian\\DSA",
  "model": "auto",
  "fallback_models": ["gemini-3-flash-preview", "gemini-2.5-pro", "gemini-2.0-flash", "auto"]
}
```

## 🚀 Usage
```bash
python -m dsa.main "Two Sum | Forgot the hash map approach"
```

## 📂 Project Structure
- `dsa/`: Core logic modules.
- `templates/`: AI prompt templates.
- `config.json`: Configuration.
- `GEMINI.md`: Project mandates for AI assistants.
