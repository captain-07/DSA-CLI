# DSA-CLI 🚀

A production-ready CLI tool to convert a single-line input into structured DSA notes and save them into an Obsidian vault.

## 🛠 Features
- **Fast Input:** Just `dsa "Problem Name | My Mistake"`
- **AI-Powered:** Uses Gemini CLI to generate high-quality notes.
- **Smart Routing:** Automatically maps problems to folders (Arrays, DP, Graph, etc.).
- **Obsidian Ready:** Saves in Markdown with tags and revision checklists.

## 📦 Installation
1. Clone the repository.
2. Ensure you have the `gemini` CLI installed and authenticated.
3. Update `config.json` with your Obsidian vault path.

## 🚀 Usage
```bash
python -m dsa.main "Two Sum | Forgot the hash map approach"
```

## 📂 Project Structure
- `dsa/`: Core logic modules.
- `templates/`: AI prompt templates.
- `config.json`: Configuration.
