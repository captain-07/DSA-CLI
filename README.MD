# DSA-CLI 🚀

A production-ready CLI tool to convert a single-line input into structured Data Structures and Algorithms (DSA) notes and save them into an Obsidian vault.

DSA-CLI simplifies the process of creating comprehensive, well-formatted notes for coding problems. By providing just a problem name and optional notes, the tool leverages Google's Gemini AI to generate detailed explanations, solutions, and revision checklists, automatically organizing them in your Obsidian knowledge base.

## 🛠 Features
- **Fast Input:** Just `python -m dsa.main "Problem Name | My Mistake"`
- **AI-Powered:** Defaults to `auto` (resolves to the most powerful Gemini model available).
- **Robust Fallbacks:** Automatically tries fallback models if the primary model is unavailable.
- **Smart Routing:** Automatically maps problems to folders (Arrays, DP, Graph, etc.).
- **Obsidian Ready:** Saves in Markdown with tags and revision checklists in your specified vault.

## 📋 Prerequisites
- Python 3.10 or higher
- [Google Gemini CLI](https://github.com/google/gemini-cli) installed and authenticated
- An Obsidian vault for storing notes

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dsa-cli.git
   cd dsa-cli
   ```

2. Install the package:
   ```bash
   pip install .
   ```

3. Ensure you have the `gemini` CLI installed and authenticated:
   ```bash
   gemini --help  # Verify installation
   ```

4. Update `config.json` with your Obsidian vault path.

## ⚙️ Configuration (`config.json`)
```json
{
  "vault_path": "C:\\Users\\USER\\Desktop\\Obsidian\\DSA",
  "model": "auto",
  "fallback_models": ["gemini-3-flash-preview", "gemini-3-flash-preview", "gemini-2.0-flash", "auto"]
}
```

## 🚀 Usage
Basic usage:
```bash
dsa "Two Sum | Forgot the hash map approach"
```

Or with module:
```bash
python -m dsa.main "Two Sum | Forgot the hash map approach"
```

Override model:
```bash
dsa --model gemini-2.0-flash "Binary Search | Edge cases with empty array"
```

## 🔧 How It Works
1. **Input Parsing:** Splits the input into problem name and optional notes.
2. **AI Generation:** Uses Gemini AI with your configured model to generate structured notes.
3. **Formatting:** Cleans and formats the output into Markdown.
4. **Routing:** Detects the appropriate folder based on problem type (e.g., Arrays, Dynamic Programming).
5. **Saving:** Stores the note in your Obsidian vault with proper naming and tags.

## 📂 Project Structure
- `dsa/`: Core logic modules (main.py, generator.py, etc.).
- `templates/`: AI prompt templates.
- `config.json`: Configuration file.
- `GEMINI.md`: Project mandates for AI assistants.
- `pyproject.toml`: Package configuration.

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License
This project is licensed under the MIT License.
