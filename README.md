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

### Trigger pipeline for building distribution artifacts

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