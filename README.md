# Flowprint 🐍

**Flowprint** is a lightweight Python automation utility designed to analyze source files and "inject" specific print statements under recognized built-in patterns like function definitions and imports.

## ✨ The Concept (The Lore)
The current version of Flowprint serves as a "Proof of Concept." Its primary goal is to demonstrate how a tool can automatically traverse Python code, identify specific structural markers (`def` and `import`), and insert debugging or logging statements while strictly maintaining the original code's indentation.

> **Note:** This is the initial "lore" or the foundation of the idea. While simple now, the architecture is built to be expanded into a more sophisticated code-manipulation engine.

## 🚀 Current Capabilities
* **Pattern Recognition:** Detects `def` and `import` statements automatically.
* **Indentation Awareness:** Injected code matches the indentation of the line above it to ensure the code remains runnable.
* **Non-Destructive:** Generates a new file with a randomized name in the `results/` folder, keeping your source files safe.
* **Interactive CLI:** A simple terminal-based interface for selecting files and triggering the injection.

## 📂 Project Structure
* `main.py`: The core logic and command-line interface.
* `lib/`: Homemade library for file handling, searching, and randomization.
* `patterns.py`: Defines the code snippets to be injected.
* `files/`: Your source directory for `.py` files.
* `results/`: Where the transformed files are stored.

## 🛠️ Getting Started
1. **Clone & Setup:**
   ```bash
   git clone git@github.com:xkm9/flowprint.git
   cd flowprint
   pip install rich
   p -m main
