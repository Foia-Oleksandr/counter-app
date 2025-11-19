# counter-app

Standalone app for counting

## 🧩 Prerequisites

- Python **≥3.11**
- [Poetry](https://python-poetry.org/docs/#installation) installed globally:

### For linux like platform
```bash
  curl -sSL https://install.python-poetry.org | python3 -
```
Or via platform package manager. For example:
```shell
sudo apt install python3-poetry
```

### For windows platform
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Build

Clone and install dependencies
```shell
git clone https://github.com/.../counter_app.git
cd counter_app
poetry install
```

## Run the application

```shell
poetry run counter-app
```

or drop into the virtual environment shell and run there:

```shell
poetry shell
counter-app
```

##  Run Tests

Run all tests	
```shell
poetry run pytest
```

Run one test	
```shell
poetry run pytest -k <test name>
```

##  Build a standalone executable for distribution

```shell
poe clean
poe build
```

Observe a binary file at the `dist` folder

## 📦 Poe Tasks Overview

The project defines several automation tasks using **Poe the Poet**, enabling easy execution of common development and build operations.

### 🔧 Asset & UI Compilation
- **`poe compile-qrc`** — Compile Qt resource collections into Python modules.
- **`poe compile-ui`** — Convert `.ui` files into Python UI classes.
- **`poe compile-web-assets`** — Build the web viewer (npm) and pack assets via `pyside6-rcc`.
- **`poe compile-assets`** — Run all of the above in sequence.

### 🧹 Cleaning and Building
- **`poe clean`** — Run the custom cleanup script.
- **`poe installer-build`** — Build a PyInstaller standalone binary.
- **`poe build`** — Generate version + build installer.
- **`poe clean-build`** — Clean, compile assets, then build.

### 👣 Development Helpers
- **`poe run`** — Run the Python app directly.
- **`poe open-designer`** — Open Qt Designer.
- **`poe lint`** — Run ruff linter.
- **`poe lint_fix`** — Auto-fix lint issues + format code.
- **`poe format`** — Apply formatting only.

### 🚀 Release Pipeline
- **`poe generate-version`** — Embed version information.
- **`poe release`** — Create a Git tag for release.
  - After running, push the tag manually to trigger CI/CD.

## Trigger pipeline for building distribution artifacts

- Validate that you bumped a release version in the `pyproject.toml` file.
- Then run poe `release` goal for creating git tag.
```shell
poe release
```
- Push a newly created git tag to the remote repository
- Validate that pipeline complete successfully and created new distribution artifact in the releases section.

## Configuring IDE

If your IDE doesn't automatically detect a path to an interpreter managed by a poetry tool, then set it manually.
Define a path to the interpreter via command:

```shell
poetry env info --path
```

Then set the proper value in your IDE settings. For example, for PyCharm:

In PyCharm → Settings → Python → Python Interpreter

 - Click Add Interpreter → Add Local Interpreter
   - At opened `Add Interpreter dialog`:
     - choose select exising
     - set `Type` to `poetry`
     - (optional) if IDE not automatically detect a path to `poetry env use` than browse to that path to interpreter and select:
       - On Linux/macOS → bin/python
       - On Windows → Scripts/python.exe

## Dependency management with Poetry
Add package
```shell
poetry add numpy
```

Remove package
```shell
poetry remove numpy
```

Add dev tool
```shell
poetry add --group dev ruff
```

Update package to the latest version
```shell
poetry update numpy
```

Downgrade/Upgrade to a specified package version
```shell
poetry add numpy@1.26.4
```

List of available versions
```shell
poetry search numpy
```

