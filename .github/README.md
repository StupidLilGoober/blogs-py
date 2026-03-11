# blogs.py

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/StupidLilGoober/blogs-py?style=social)](https://github.com/StupidLilGoober/blogs-py/stargazers)
[![Forks](https://img.shields.io/github/forks/StupidLilGoober/blogs-py?style=social)](https://github.com/StupidLilGoober/blogs-py/network/members)
[![Issues](https://img.shields.io/github/issues/StupidLilGoober/blogs-py)](https://github.com/StupidLilGoober/blogs-py/issues)

`blogs.py` is a Python script for generating static blogs from Markdown files.

## Features

- Convert Markdown posts to HTML
- Minimal dependencies (Python + `markdown`)
- Simple CLI interface

| Command | Description |
|---------|-------------|
| `new`   | Create a new blog folder |
| `blog`  | Create a new blog post folder |
| `build` | Convert Markdown posts to HTML |

## Installation

```bash
git clone https://github.com/StupidLilGoober/blogs-py.git
cd blogs-py
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install markdown
```
