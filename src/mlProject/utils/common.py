import json
from pathlib import Path
from typing import Any

import joblib
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError

from mlProject.logging import logger


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a YAML file and return its content as a ConfigBox."""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

            # ConfigBox lets you access dictionary keys with dot notation.
            logger.info(f"YAML file loaded successfully from: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


def create_directories(path_to_directories: list, verbose: bool = True):
    """Create directories from a list of paths."""
    for path in path_to_directories:
        Path(path).mkdir(parents=True, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


def save_json(path: Path, data: dict):
    """Save dictionary data into a JSON file."""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")


def load_json(path: Path) -> ConfigBox:
    """Load JSON file data and return it as a ConfigBox."""
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


def save_bin(data: Any, path: Path):
    """Save Python object as a binary file."""
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


def load_bin(path: Path) -> Any:
    """Load data from a binary file."""
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


def get_size(path: Path) -> str:
    """Return file size in kilobytes."""
    size_in_kb = round(path.stat().st_size / 1024)
    return f"~ {size_in_kb} KB"
