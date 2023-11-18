# Python Package Template
 A very customizable template for a Python package OR a package-ified Python app.

## Prerequisites
- [Cookiecutter](https://www.cookiecutter.io/)
- [Poetry](https://python-poetry.org)
- [Git](https://git-scm.com)
- [w64devkit](https://github.com/skeeto/w64devkit) (On windows)

## Usage
1. Make sure you have installed all the prerequisites.
2. Run the cookiecutter command:
```bash
cookiecutter gh:tinkering-townsperson/python_package_template
```
The rest of the process is interactive- you'll be asked for a project name and about which features you want enabled, after which the project will be setup.

## Core Functionality

- Development Management using [Makefiles](https://www.gnu.org/software/make/manual/html_node/Introduction.html).
- Testing with [pytest](https://docs.pytest.org/en/7.2.x/).
- CI/CD using [Github Actions](https://docs.github.com/en/actions).
- Multiple license options.
- Modern `pyproject.toml` with [poetry](https://python-poetry.org) without any legacy files.


## Thanks
Many thanks to [Robert Hafner](https://github.com/tedivm) for the original template. It provided a lot of inspiration, especially in this README!
