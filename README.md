# Python Udemy Tutorial

I wrote this note for learning purposes only.

## Live Documentation

You can access the documentation on GitHub Pages:

**https://kmavillanosa.github.io/py-udemy-tutorial/**

## Documentation

This project uses [MkDocs](https://www.mkdocs.org/) with the [Material theme](https://squidfunk.github.io/mkdocs-material/) for documentation.

### Running Locally

Follow these steps to run the documentation on your local machine:

1. **Install dependencies**:
   ```bash
   pip install -r requirements-docs.txt
   ```
   
   Or if you prefer using a virtual environment (recommended):
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements-docs.txt
   ```

2. **Start the development server**:
   
   **Option A: Using MkDocs directly** (built-in auto-reload):
   ```bash
   mkdocs serve
   ```
   
   **Option B: Using nodemon** (enhanced auto-reload, watches Python files too):
   ```bash
   # Install Node.js dependencies (one-time setup)
   npm install
   
   # Start with nodemon (auto-restarts on any file changes)
   npm run docs:dev
   ```
   
   The nodemon approach provides:
   - Automatic restart on changes to `.md`, `.yml`, `.yaml`, and `.py` files
   - Watches both `docs/` and `section-one/` directories
   - More reliable file watching (similar to nodemon for Node.js projects)

3. **Open in your browser**:
   - The documentation will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - The server will automatically reload when you make changes to the documentation files

4. **Stop the server**:
   - Press `Ctrl+C` in the terminal to stop the development server

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
- `package.json` - Node.js configuration for nodemon (optional)
- `nodemon.json` - Nodemon configuration for enhanced auto-reload