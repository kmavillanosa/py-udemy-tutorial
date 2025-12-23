# Python Udemy Tutorial

I wrote this note for learning purposes only.

## Documentation

This project uses [MkDocs](https://www.mkdocs.org/) with the [Material theme](https://squidfunk.github.io/mkdocs-material/) for documentation.

### Setup

Install the documentation dependencies:

```bash
pip install -r requirements-docs.txt
```

### View Documentation Locally

Start the development server:

```bash
mkdocs serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

### Build Documentation

Generate static HTML files:

```bash
mkdocs build
```

The generated site will be in the `site/` directory.

## Project Structure

- `section-one/` - Python fundamentals tutorial files
- `docs/` - MkDocs documentation source files
- `mkdocs.yml` - MkDocs configuration file