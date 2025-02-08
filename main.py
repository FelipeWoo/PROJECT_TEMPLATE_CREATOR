import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

# README.md Template
README_TEMPLATE = """# {title_es} | {title_en}

## Resumen
Este proyecto...

## Abstract
This repository contains the source code and resources necessary for...

## Installation
1. Clone the repository:  
   ```sh
   git clone https://github.com/user/project.git
   ```
2. Navigate to the project directory:
   ```sh
   cd project
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the following command to start the project:
```sh
python main.py
```

## Contribution
If you wish to contribute, follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-new`).
3. Make changes and commit them (`git commit -m "Description of changes"`).
4. Submit a **pull request**.

## Keywords
key|words|project|related

## License
This project is under the MIT license.
"""

# STRUCTURE.md Template
STRUCTURE_TEMPLATE = """
# Project: {title_en}

## Project Structure

### src/
Contains the project's source files, such as code, designs, 3D models, or any other necessary resources.

### docs/
Stores project documentation, including manuals, technical reports, specifications, and diagrams.

### assets/
Includes graphical and multimedia resources, such as images, videos, icons, 3D models, and design files.

### data/
Contains data files, databases, spreadsheets, or any other structured information storage.

### exports/
Used to store generated or compiled files, such as PDFs, reports, deliverables, and binaries.

### config/
Includes project configuration files, such as environment variables and custom settings.

### tests/
Contains automated project tests, including unit and integration tests.

### logs/
Stores activity logs, error logs, and system events to facilitate debugging and project monitoring.

### backups/
Backup copies of data, configurations, or critical files to prevent information loss.

### references/
Contains reference documents, standards, norms, or papers related to the project.

### templates/
Reusable templates for code, design, or documentation.

### scripts/
Automation tools and auxiliary scripts for project management.

### README.md
A file with the general project description, including installation and usage instructions.

### LICENSE
Specifies the type of license used in the project.

### .gitignore
A list of files and folders that should not be tracked by Git.

### Makefile
An optional file for automating project tasks and commands.
"""

def create_project_structure(project_path, project_name, title_es, title_en):
    # Convert to uppercase and replace spaces with underscores
    project_name = project_name.upper().replace(" ", "_")
    title_es = title_es.upper().replace(" ", "_")
    title_en = title_en.upper().replace(" ", "_")
    
    # Define folders
    folders = [
        "src", "docs", "assets", "data", "exports", "config", "tests", "logs",
        "backups", "references", "templates", "scripts"
    ]
    
    # Create project root directory
    project_root = os.path.join(project_path, project_name)
    os.makedirs(project_root, exist_ok=True)
    
    # Create subdirectories
    for folder in folders:
        os.makedirs(os.path.join(project_root, folder), exist_ok=True)
    
    # Create README.md and STRUCTURE.md files
    readme_content = README_TEMPLATE.format(
        title_es=title_es,
        title_en=title_en
    )
    structure_content = STRUCTURE_TEMPLATE.format(
      title_en=title_en, 
      project_folder=project_name
    )
    
    with open(os.path.join(project_root, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)
    with open(os.path.join(project_root, "STRUCTURE.md"), "w", encoding="utf-8") as f:
        f.write(structure_content)
    
    # Create additional files
    open(os.path.join(project_root, "LICENSE"), "w").close()
    open(os.path.join(project_root, ".gitignore"), "w").close()
    
    # Initialize Git
    subprocess.run(["git", "init"], cwd=project_root)
    messagebox.showinfo("Success", f"Project '{title_es}' successfully created in {project_root}")

def browse_directory():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_location.delete(0, tk.END)
        entry_location.insert(0, folder_selected)

def create_project():
    title_es = entry_title_es.get().strip()
    title_en = entry_title_en.get().strip()
    project_name = entry_name.get().strip()
    project_location = entry_location.get().strip()
    
    if not title_es or not title_en or not project_name or not project_location:
        messagebox.showwarning("Error", "All fields are required")
        return
    
    create_project_structure(project_location, project_name, title_es, title_en)

if __name__ == "__main__":
    build_gui()
