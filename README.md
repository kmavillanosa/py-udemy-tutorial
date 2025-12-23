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

### GitHub Pages Deployment

The documentation is automatically deployed to GitHub Pages when you push to the `main` or `master` branch.

#### Initial Setup

1. **Enable GitHub Pages** in your repository settings:
   - Go to Settings → Pages
   - Under "Source", select "GitHub Actions"

2. **Push to GitHub** - The workflow will automatically:
   - Build the documentation
   - Deploy it to the `gh-pages` branch
   - Make it available at [https://kmavillanosa.github.io/py-udemy-tutorial/](https://kmavillanosa.github.io/py-udemy-tutorial/)

The documentation will be automatically updated whenever you push changes to the main branch.

## Project Structure

- `section-one/` - Python fundamentals tutorial files
- `docs/` - MkDocs documentation source files
- `mkdocs.yml` - MkDocs configuration file