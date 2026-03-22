import json
import os
import sys

from pathlib import Path
CONFIG_FILE = Path(__file__).parent.parent / "config.json"

DEFAULT_CONFIG = {
    "vault_path": "./vault",
    "model": "auto",
    "fallback_models": ["gemini-3-flash-preview", "gemini-2.5-pro", "gemini-2.0-flash", "auto"]
}

def load_config():
    """Loads configuration from config.json with error handling and defaults."""
    if not os.path.exists(CONFIG_FILE):
        return DEFAULT_CONFIG
    
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            # Ensure all default keys are present
            for key, value in DEFAULT_CONFIG.items():
                if key not in config:
                    config[key] = value
            return config
    except json.JSONDecodeError as e:
        print(f"Error decoding {CONFIG_FILE}: {e}")
        print("Using default configuration instead.")
        return DEFAULT_CONFIG
    except Exception as e:
        print(f"Unexpected error loading config: {e}")
        return DEFAULT_CONFIG
