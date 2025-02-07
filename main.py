import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

# Plantilla para README.md
README_TEMPLATE = """# {title_es} | {title_en}

## Resumen
{summary_es}

## Abstract
{abstract}

## Installation
{installation}

## Usage
{usage}

## Contribution
{contribution}

## License
{license}
"""

# Plantilla para STRUCTURE.md
STRUCTURE_TEMPLATE = """
# 📂 Proyecto: {title_en}

## 📌 Estructura del Proyecto

```
📂 {project_folder}/
│── 📂 src/                  # Archivos fuente (código, diseños, modelos, etc.)
│── 📂 docs/                 # Documentación (manuales, reportes, especificaciones)
│── 📂 assets/               # Recursos gráficos, imágenes, videos, íconos, modelos 3D, etc.
│── 📂 data/                 # Archivos de datos, bases de datos, hojas de cálculo
│── 📂 exports/              # Archivos generados (PDFs, compilaciones, entregables)
│── 📂 config/               # Configuraciones y variables del proyecto
│── 📂 tests/                # Pruebas (código, calidad, validaciones)
│── 📂 logs/                 # Archivos de registro (errores, eventos, cambios)
│── 📂 backups/              # Copias de seguridad de datos y configuraciones
│── 📂 references/           # Documentos de referencia, papers, estándares, normas
│── 📂 templates/            # Plantillas reutilizables para documentos, código, diseño
│── 📂 scripts/              # Automatizaciones y utilidades
│── README.md                # Descripción general del proyecto
│── LICENSE                  # Tipo de licencia del proyecto
│── .gitignore               # Archivos y carpetas a ignorar en Git
│── Makefile                 # Automatización de tareas (opcional)
```
"""

def create_project_structure(project_path, project_name, title_es, title_en):
    # Definir las carpetas
    folders = [
        "src", "docs", "assets", "data", "exports", "config", "tests", "logs",
        "backups", "references", "templates", "scripts"
    ]
    
    # Crear directorio base del proyecto
    project_root = os.path.join(project_path, project_name)
    os.makedirs(project_root, exist_ok=True)
    
    # Crear subcarpetas
    for folder in folders:
        os.makedirs(os.path.join(project_root, folder), exist_ok=True)
    
    # Crear archivos README.md y STRUCTURE.md
    readme_content = README_TEMPLATE.format(
        title_es=title_es,
        title_en=title_en,
        summary_es="Resumen del proyecto...",
        abstract="Descripción detallada...",
        installation="Instrucciones de instalación...",
        usage="Ejemplo de uso...",
        contribution="Cómo contribuir...",
        license="Tipo de licencia..."
    )
    structure_content = STRUCTURE_TEMPLATE.format(title_en=title_en, project_folder=project_name)
    
    with open(os.path.join(project_root, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)
    with open(os.path.join(project_root, "STRUCTURE.md"), "w", encoding="utf-8") as f:
        f.write(structure_content)
    
    # Crear archivos adicionales
    open(os.path.join(project_root, "LICENSE"), "w").close()
    open(os.path.join(project_root, ".gitignore"), "w").close()
    
    # Inicializar Git
    subprocess.run(["git", "init"], cwd=project_root)
    messagebox.showinfo("Éxito", f"Proyecto '{title_es}' creado con éxito en {project_root}")

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
        messagebox.showwarning("Error", "Todos los campos son obligatorios")
        return
    
    create_project_structure(project_location, project_name, title_es, title_en)

def build_gui():
    global entry_title_es, entry_title_en, entry_name, entry_location
    root = tk.Tk()
    root.title("Generador de Proyectos")
    root.geometry("400x300")
    
    tk.Label(root, text="Título del Proyecto (Español)").pack(pady=5)
    entry_title_es = tk.Entry(root, width=50)
    entry_title_es.pack()
    
    tk.Label(root, text="Título del Proyecto (Inglés)").pack(pady=5)
    entry_title_en = tk.Entry(root, width=50)
    entry_title_en.pack()
    
    tk.Label(root, text="Nombre de la Carpeta").pack(pady=5)
    entry_name = tk.Entry(root, width=50)
    entry_name.pack()
    
    tk.Label(root, text="Ubicación").pack(pady=5)
    frame = tk.Frame(root)
    frame.pack()
    entry_location = tk.Entry(frame, width=40)
    entry_location.pack(side=tk.LEFT)
    tk.Button(frame, text="...", command=browse_directory).pack(side=tk.LEFT)
    
    tk.Button(root, text="Crear Proyecto", command=create_project).pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    build_gui()
