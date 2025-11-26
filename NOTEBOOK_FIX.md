# VS Code Notebook Service Worker Error - Solutions

This error occurs when VS Code's Service Worker fails to initialize. The notebooks are **completely valid** - this is a VS Code bug, not a notebook issue.

## Solution 1: Clear VS Code Service Worker Cache (Recommended)

1. **Close VS Code completely**
2. Run this command in terminal:
   ```bash
   rm -rf ~/.config/Code/Service\ Worker/
   ```
3. **Reopen VS Code**
4. Try opening the notebooks again

## Solution 2: Use Jupyter Notebook in Browser

Since you have Jupyter installed, you can run the notebooks in your browser:

```bash
cd /home/karanos/kiam/week1
jupyter notebook
```

This will open Jupyter in your browser where you can run all the notebooks without any issues.

## Solution 3: Use Jupyter Lab (Modern Interface)

```bash
cd /home/karanos/kiam/week1
jupyter lab
```

## Verification

All notebooks are valid and contain code:
- `01-EDA.ipynb`: 10 cells ✓
- `02-Indicators.ipynb`: 5 cells ✓  
- `03-Sentiment-Correlation.ipynb`: 7 cells ✓

The issue is purely with VS Code's webview, not the files themselves.
