import tomllib
from pathlib import Path

def embed_version(version: str = None):
    """Write a version string into _version.py for runtime use."""
    if not version:
        version = read_poetry_version()

    target = Path("src/counter_app/_version.py")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(f'__version__ = "{version}"\n')
    print(f"Embedded version {version} into {target}")

def read_poetry_version(path="pyproject.toml"):
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError("pyproject.toml not found.")

    data = tomllib.loads(p.read_text())
    return data.get("tool", {}).get("poetry", {}).get("version")

if __name__ == "__main__":
    embed_version()