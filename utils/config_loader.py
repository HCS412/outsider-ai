# utils/config_loader.py

import os
import yaml

class ConfigError(Exception):
    pass

def load_config(path: str = "config.yaml") -> dict:
    try:
        with open(path, "r") as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        raise ConfigError("❌ Configuration file 'config.yaml' not found.")
    except yaml.YAMLError as e:
        raise ConfigError(f"❌ Error parsing YAML: {e}")

    api_key = os.getenv(config["openai"]["api_key_env"])
    if not api_key or not api_key.startswith("sk-"):
        raise ConfigError("❌ OPENAI_API_KEY is not set or invalid. Set it as an environment variable.")
    
    config["openai"]["api_key"] = api_key
    return config
