# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.


## Project Overview
This is a project to create a data pipeline with data from the USGS (via the dataretrieval python lib), and potentially other sources to extract, transform and load to an application to view in real-time the conditions for certain river activiites (i.e., fishing, boating, rafting, etc..).

`This is a project for learning` about SDLC, data engineering, and other technial skills. 

## Project Stages
Envision this a multi-stage project as outlined below:
- Stage 1:
-- create pipeline: script for data extraction, transformation, and load
-- host data in a postgreSQL database (if needed)
-- create a dashboard with geographical features; historical, live and forecasted data.
- Stage 2:
-- create an application (web and phone) for viewing maps and data


## Project Status

This repository is in its initial setup phase.

## Expected Stack

`.gitignore` was used as a template from github to get that initial gitignore file created. Just because an item is listed there, does not mean it will be used in the project. You may updated this file as requirements are discovered.

For now, focus on stage 1: creating the pipeline and dashboards. I know we are using (for now):
- dataretrieval (USGS Water API)
- pandas, numpy, requests, json, geopandas, dotenv, folium, map classify, dateutils, ipython

## Architecture
Will be filled in once built


## Coding Conventions
filled in later

## Safety Rules
filled in later

## Educational Guidance
- Provide context on code written to explain the technical use of a line of code to less technical user
- ask operator for their input on what needs to be done. If operator doesn't know, code it and explain it as if you were a teacher

## Commands
filled in later
<!-- > Update these once project files are added.

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
mypy . -->
```
