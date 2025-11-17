#!/usr/bin/env python3
"""
Release automation script:
 - Reads a version from pyproject.toml
 - Checks if Git tag exists
 - Creates and pushes a new tag
"""

import subprocess
import sys

from tasks.generate_version import read_poetry_version, embed_version

def ensure_clean_working_tree():
    if subprocess.run(["git", "diff", "--quiet"]).returncode != 0:
        print("❌ Uncommitted changes found. Commit them before tagging.")
        sys.exit(1)

    if subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode != 0:
        print("❌ You have staged changes that are not committed. Commit them first.")
        sys.exit(1)

    print("✔ Working tree is clean.")

def ensure_head_pushed():
    subprocess.run(["git", "fetch", "origin"], check=True)

    status = subprocess.run(
        ["git", "status", "-sb"],
        capture_output=True,
        text=True
    ).stdout

    if "[ahead " in status or "[ahead]" in status:
        print("❌ Local HEAD contains commits not pushed to origin. Push first.")
        sys.exit(1)

    if "[behind " in status or "[behind]" in status:
        print("❌ Local branch is behind origin. Pull or rebase before tagging.")
        sys.exit(1)

    print("✔ HEAD is pushed to origin.")

def main():
    ensure_clean_working_tree()
    ensure_head_pushed()

    version = read_poetry_version()
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
