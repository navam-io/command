# Copyright 2024 and beyond, Command. All Rights Reserved.
# https://www.command.ai/
# This code is Apache-2.0 licensed. Please see the LICENSE file in our repository for the full license text.
# You may use this code under the terms of the Apache-2.0 license.
# This code is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

"""Environment variable loader with support for .env.local files."""

import os
from pathlib import Path
from dotenv import load_dotenv


def load_environment():
    """
    Load environment variables from .env.local file if it exists.

    Priority order:
    1. System environment variables (highest priority)
    2. .env.local file in current directory
    3. .env.local file in user home directory

    Returns:
        bool: True if at least one .env.local file was loaded
    """
    loaded = False

    # Try to load from current directory first
    current_env = Path.cwd() / '.env.local'
    if current_env.exists():
        load_dotenv(dotenv_path=current_env, override=False)
        loaded = True

    # Also try home directory as fallback
    home_env = Path.home() / '.env.local'
    if home_env.exists():
        load_dotenv(dotenv_path=home_env, override=False)
        loaded = True

    return loaded


def get_api_key(key_name, env_var_name=None):
    """
    Get API key from environment variables.

    Args:
        key_name: The name of the key (e.g., 'anthropic', 'openai')
        env_var_name: Optional custom environment variable name.
                     If not provided, will be generated from key_name.

    Returns:
        str or None: The API key if found, None otherwise
    """
    # Ensure environment is loaded
    load_environment()

    # Generate env var name if not provided
    if env_var_name is None:
        env_var_name = f"{key_name.upper()}_API_KEY"

    return os.getenv(env_var_name)


# Auto-load on module import
load_environment()
