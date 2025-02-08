# Creador de plantillas de proyecto en Python | Template Creator for Projects in Python

## Resumen
Este proyecto busca estandarizar la distribución de carpetas y archivos en cualquier tipo de proyecto. No se basa en un estándar conocido, sino que proporciona una forma estructurada para organizar archivos de manera eficiente.

## Abstract
The **Project Template Creator** is a Python application that allows users to generate a predefined folder structure for their projects. It includes a graphical interface (Tkinter) for ease of use, and it automatically creates essential files such as `README.md`, `STRUCTURE.md`, `.gitignore`, and `LICENSE`. The application also initializes a Git repository in the project directory.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/felipewoo/project-template-creator.git
   ```
2. Navigate to the project directory:
   ```sh
   cd project-template-creator
   ```
3. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python main.py
   ```

## Usage
1. Open the **Project Template Creator**.
2. Enter the **Project Title (Spanish & English)**, **Folder Name**, and **Project Location**.
3. Click **Create Project**.
4. The folder structure and necessary files will be generated automatically.
5. The project will be initialized as a Git repository.

## Features
- **GUI-based** project creation using Tkinter.
- **Predefined folder structure** for any type of project.
- **Automatic file generation** (`README.md`, `STRUCTURE.md`, `.gitignore`, `LICENSE`).
- **Supports external templates** (`README_TEMPLATE.txt`, `STRUCTURE_TEMPLATE.txt`).
- **Git initialization** for version control.

## Justification
This project was developed to facilitate the cataloging of projects. Having a structured list of projects with a brief description allows for better decision-making and improves efficiency in project management.

## Contribution
If you wish to contribute, follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-new`).
3. Make your changes and commit them (`git commit -m "Description of changes"`).
4. Submit a **pull request**.

## Keywords
TEMPLATE | PROJECT | AUTOMATION | ORGANIZATION | PYTHON

## License
This project is under the MIT license.