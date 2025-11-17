#!/usr/bin/env python3
"""
Release automation script:
 - Reads a version from pyproject.toml
 - Checks if Git tag exists
 - Creates and pushes a new tag
"""

import subprocess
import sys
import tomllib
from pathlib import Path


def embed_version(version: str):
    """Write a version string into _version.py for runtime use."""
    target = Path("src/atomistic_transformations/_version.py")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(f'__version__ = "{version}"\n')
    print(f"📝 Embedded version {version} into {target}")

def main():
    pyproject_path = Path("pyproject.toml")

    if not pyproject_path.exists():
        print("❌ pyproject.toml not found.")
        sys.exit(1)

    # Read version
    with open(pyproject_path, "rb") as f:
        data = tomllib.load(f)
    version = data["project"]["version"]
    tag = f"v{version}"

    # Embed version before tagging
    embed_version(version)

    # Check existing tags
    result = subprocess.run(["git", "tag"], capture_output=True, text=True)
    tags = result.stdout.splitlines()

    if tag in tags:
        print(f"❌ Tag {tag} already exists. Please bump version in pyproject.toml.")
        sys.exit(1)

    # Create and push tag
    subprocess.run(["git", "tag", tag], check=True)
    subprocess.run(["git", "push", "origin", tag], check=True)
    print(f"✅ Created and pushed {tag}")


if __name__ == "__main__":
    main()
