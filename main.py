import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from datetime import datetime

def load_template(file_path):
    """Load template content from a file."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    return ""

def create_project_structure(project_path, project_name, title_es, title_en, author):
    # Convert to uppercase and replace spaces with underscores
    project_name = project_name.upper().replace(" ", "_")
    title_es = title_es.lower().title()
    title_en = title_en.lower().title()
    author = author.lower().title()
    
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
    
    # Load README and STRUCTURE templates
    readme_template = load_template("README_TEMPLATE.txt")
    structure_template = load_template("STRUCTURE_TEMPLATE.txt")
    license_template = load_template("MIT_LICENSE_TEMPLATE.txt")
    
    # Format templates with project information
    readme_content = readme_template.format(
        title_es=title_es,
        title_en=title_en
    )
    structure_content = structure_template.format(
        title_en=title_en,
        project_folder=project_name
    )
    license_content = license_template.format(
        year=datetime.now().year,
        author=author
    )

    
    # Write Files with content
    with open(os.path.join(project_root, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)
    with open(os.path.join(project_root, "STRUCTURE.md"), "w", encoding="utf-8") as f:
        f.write(structure_content)
    with open(os.path.join(project_root, "LICENSE"), "w", encoding="utf-8") as f:
        f.write(license_content)
    
    # Create additional files
    open(os.path.join(project_root, ".gitignore"), "w").close()
    today = datetime.now().strftime("%Y_%m_%d")
    open(os.path.join(project_root, today), "w").close()

    
    
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
    author = entry_author.get().strip()
    
    if not title_es or not title_en or not project_name or not project_location or not author:
        messagebox.showwarning("Error", "All fields are required")
        return
    
    create_project_structure(project_location, project_name, title_es, title_en, author)

def build_gui():
    global entry_title_es, entry_title_en, entry_name, entry_location, entry_author
    root = tk.Tk()
    root.title("Project Generator")
    root.geometry("400x380")

    tk.Label(root, text="Author").pack(pady=5)
    entry_author = tk.Entry(root, width=40)
    entry_author.pack()
    
    tk.Label(root, text="Project Title (Spanish)").pack(pady=5)
    entry_title_es = tk.Entry(root, width=40)
    entry_title_es.pack()
    
    tk.Label(root, text="Project Title (English)").pack(pady=5)
    entry_title_en = tk.Entry(root, width=40)
    entry_title_en.pack()
    
    tk.Label(root, text="Folder Name").pack(pady=5)
    entry_name = tk.Entry(root, width=40)
    entry_name.pack()
    
    tk.Label(root, text="Location").pack(pady=5)
    frame = tk.Frame(root)
    frame.pack()
    entry_location = tk.Entry(frame, width=35)
    entry_location.pack(side=tk.LEFT)
    tk.Button(frame, text="...", command=browse_directory).pack(side=tk.LEFT)
    
    tk.Button(root, text="Create Project", command=create_project).pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    build_gui()
