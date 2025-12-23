// Pyodide Runner for MkDocs
// Adds "Run Code" buttons to Python code blocks

let pyodide = null;

async function loadPyodide() {
    if (!pyodide) {
        pyodide = await loadPyodide({
            indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.24.1/full/'
        });
    }
    return pyodide;
}

// Wait for page to be fully loaded
function initPyodideRunner() {
    console.log('Pyodide Runner: Initializing...');
    // Find all Python code blocks - try multiple selectors for Material theme
    const selectors = [
        'pre code.language-python',
        'pre code.lang-python',
        'code[class*="python"]',
        'pre[class*="python"] code',
        '.highlight.python code',
        '.highlightcode.language-python'
    ];
    
    let codeBlocks = [];
    selectors.forEach(selector => {
        const blocks = document.querySelectorAll(selector);
        blocks.forEach(block => {
            if (!codeBlocks.includes(block)) {
                codeBlocks.push(block);
            }
        });
    });
    
    // If no blocks found, try a more general approach
    if (codeBlocks.length === 0) {
        const allCodeBlocks = document.querySelectorAll('pre code, code.highlight');
        allCodeBlocks.forEach(block => {
            const text = block.textContent || '';
            // Check if it looks like Python code (has print, def, class, import, etc.)
            if (text.match(/\b(print|def |class |import |from |if |for |while |= |#)/)) {
                codeBlocks.push(block);
            }
        });
    }
    
    console.log(`Pyodide Runner: Found ${codeBlocks.length} Python code blocks`);
    
    codeBlocks.forEach((codeBlock, index) => {
        // Find the pre element (parent)
        let pre = codeBlock.parentElement;
        while (pre && pre.tagName !== 'PRE') {
            pre = pre.parentElement;
        }
        
        if (!pre) return;
        
        // Skip if already processed
        if (pre.nextElementSibling && pre.nextElementSibling.classList.contains('pyodide-runner-container')) {
            return;
        }
        
        // Create container
        const container = document.createElement('div');
        container.className = 'pyodide-runner-container';
        container.style.marginTop = '10px';
        container.style.marginBottom = '20px';
        
        // Create button container
        const buttonContainer = document.createElement('div');
        buttonContainer.style.marginBottom = '10px';
        
        // Create run button
        const runButton = document.createElement('button');
        runButton.textContent = '▶ Run Code';
        runButton.className = 'md-button md-button--primary';
        runButton.style.marginRight = '10px';
        runButton.style.cursor = 'pointer';
        runButton.style.padding = '8px 16px';
        runButton.style.fontSize = '14px';
        runButton.style.borderRadius = '4px';
        runButton.style.border = 'none';
        
        // Create clear button
        const clearButton = document.createElement('button');
        clearButton.textContent = 'Clear Output';
        clearButton.className = 'md-button';
        clearButton.style.cursor = 'pointer';
        clearButton.style.padding = '8px 16px';
        clearButton.style.fontSize = '14px';
        clearButton.style.borderRadius = '4px';
        clearButton.style.border = '1px solid rgba(0,0,0,0.12)';
        
        // Create output div
        const outputDiv = document.createElement('div');
        outputDiv.className = 'pyodide-output';
        outputDiv.id = `pyodide-output-${index}`;
        outputDiv.style.backgroundColor = '#1e1e1e';
        outputDiv.style.color = '#d4d4d4';
        outputDiv.style.padding = '15px';
        outputDiv.style.borderRadius = '4px';
        outputDiv.style.minHeight = '20px';
        outputDiv.style.display = 'none';
        outputDiv.style.fontFamily = 'Consolas, "Courier New", monospace';
        outputDiv.style.fontSize = '14px';
        outputDiv.style.whiteSpace = 'pre-wrap';
        outputDiv.style.overflowX = 'auto';
        outputDiv.style.border = '1px solid #3e3e3e';
        
        // Get code content
        const code = codeBlock.textContent;
        
        // Run button handler
        runButton.addEventListener('click', async function() {
            runButton.disabled = true;
            runButton.textContent = 'Running...';
            outputDiv.style.display = 'block';
            outputDiv.textContent = 'Loading Pyodide...';
            
            try {
                const pyodideInstance = await loadPyodide();
                
                // Set up output capture
                pyodideInstance.runPython(`
import sys
from io import StringIO

_stdout_capture = StringIO()
_stderr_capture = StringIO()
_original_stdout = sys.stdout
_original_stderr = sys.stderr
sys.stdout = _stdout_capture
sys.stderr = _stderr_capture
`);
                
                outputDiv.textContent = 'Executing code...';
                
                // Run user code
                let output = '';
                try {
                    pyodideInstance.runPython(code);
                    const stdout = pyodideInstance.runPython('_stdout_capture.getvalue()');
                    const stderr = pyodideInstance.runPython('_stderr_capture.getvalue()');
                    output = stdout || stderr || '';
                } catch (error) {
                    output = `Error: ${error}`;
                }
                
                // Restore stdout/stderr
                pyodideInstance.runPython(`
sys.stdout = _original_stdout
sys.stderr = _original_stderr
`);
                
                // Display output
                if (output.trim()) {
                    outputDiv.textContent = output;
                } else {
                    outputDiv.textContent = 'Code executed successfully (no output)';
                    outputDiv.style.color = '#4ec9b0';
                }
            } catch (error) {
                outputDiv.textContent = `Error loading Pyodide: ${error.message}`;
                outputDiv.style.color = '#f48771';
            } finally {
                runButton.disabled = false;
                runButton.textContent = '▶ Run Code';
            }
        });
        
        // Clear button handler
        clearButton.addEventListener('click', function() {
            outputDiv.style.display = 'none';
            outputDiv.textContent = '';
            outputDiv.style.color = '#d4d4d4';
        });
        
        // Append elements
        buttonContainer.appendChild(runButton);
        buttonContainer.appendChild(clearButton);
        container.appendChild(buttonContainer);
        container.appendChild(outputDiv);
        
        // Insert after the pre element
        if (pre.parentNode) {
            pre.parentNode.insertBefore(container, pre.nextSibling);
        } else {
            pre.after(container);
        }
    });
}

// Try multiple times to ensure it runs after page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPyodideRunner);
} else {
    initPyodideRunner();
}

// Also try after a short delay in case Material theme loads code blocks dynamically
setTimeout(initPyodideRunner, 500);
setTimeout(initPyodideRunner, 1000);

