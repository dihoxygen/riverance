# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Status

This repository is in its initial setup phase. Update this file as the project is built out.

## Expected Stack

Based on the `.gitignore`, this is a Python project anticipated to use:
- **Linting/formatting**: Ruff
- **Testing**: pytest (with optional tox/nox for multi-environment runs)
- **Type checking**: mypy
- **Package management**: UV or poetry (check for `pyproject.toml` or `uv.lock`)
- **Frameworks**: potentially Django, Flask, Scrapy, or Abstra (AI process automation)

## Commands

> Update these once project files are added.

Once a `pyproject.toml` / `uv.lock` is present:

```bash
# Install dependencies
uv sync          # or: poetry install

# Run tests
pytest
pytest path/to/test_file.py::test_name   # single test

# Lint and format
ruff check .
ruff format .

# Type check
mypy .
```
