# Gemini Project Mandates

This file contains foundational instructions and mandates for Gemini CLI while working on the DSA-CLI project. These instructions take precedence over general workflows.

## 🎯 Project Goals
- Automate the creation of high-quality DSA notes from simple inputs.
- Ensure notes are formatted for Obsidian and stored in the specified vault path.
- Use the most powerful Gemini models available with robust fallback mechanisms.

## 🛠 Model Strategy
- **Primary Model:** `auto` (Resolves to the best available model, usually Gemini 3).
- **Fallback Chain:** If the primary model fails, try `gemini-3-flash-preview`, `gemini-2.5-pro`, `gemini-2.5-flash`, and finally `auto`.
- **Logic:** The `dsa/generator.py` script is responsible for iterating through this chain until a valid response is received.

## 📁 Storage Mandate
- All generated notes MUST be saved in the directory defined in `config.json`'s `vault_path`.
- **User Default:** `C:\Users\USER\Desktop\Obsidian\DSA`
- Notes should be organized by topic (e.g., Arrays, DP, Graph) as determined by `dsa/router.py`.

## 🧪 Development & Quality Mandates
- **Continuous Testing:** Before completing any implementation task, run a test generation using `python -m dsa.main "Test Problem | Test Mistake"`.
- **Iterative Improvement:** Analyze the output of the generation. If the formatting or quality is lacking, improve `templates/prompt.txt` or `dsa/formatter.py`.
- **Validation:** Always verify that the file was correctly saved to the Obsidian path after execution.

## 📝 Coding Standards
- Maintain clean, modular, begginer friendly Python code.
- Ensure all subprocess calls to `gemini` CLI use stdin to avoid shell escaping issues on Windows.
- Configuration should be loaded centrally via `dsa/config.py`.
