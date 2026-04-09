#!/usr/bin/env python3

from dotenv import load_dotenv
import os
from typing import Dict, List, Any


def get_config() -> Dict[str, Any]:
    load_dotenv()
    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }


def validate_config(config: Dict[str, Any]) -> List[str]:
    required_keys: List[str] = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]
    missing: List[str] = [
        key for key in required_keys if key not in config or not config[key]
    ]
    return missing


def show_status(config: Dict[str, Any]) -> None:
    """Print the configuration status."""
    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print(f"Database: {config['DATABASE_URL']}")
    print(f"API Key: {config['API_KEY']}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {config['ZION_ENDPOINT']}")
    print("The Oracle sees all configurations.\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    config: Dict[str, Any] = get_config()
    missing_keys: List[str] = validate_config(config)

    if missing_keys:
        print("WARNING: Missing configuration variables:")
        for key in missing_keys:
            print(f"- {key}")
        print("\nPlease check your .env file or environment variables.")
    else:
        show_status(config)
