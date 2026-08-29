from fastapi import FastAPI
from pathlib import Path
from collections import Counter

app = FastAPI(
    title="Repolens AI",
    description="An autonomous repository intelligence platform for engineering teams.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Repolens AI"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/analyze/stats")
def analyze_stats():
    project_root = Path(__file__).resolve().parents[2]

    total_files = 0
    extensions = Counter()

    ignored_dirs = {".venv", ".git", "__pycache__", "node_modules"}

    for item in project_root.rglob("*"):
        if any(part in ignored_dirs for part in item.parts):
            continue

        if item.is_file():
            total_files += 1

            extension = item.suffix or "no_extension"
            extensions[extension] += 1

    return {
        "repository_name": project_root.name,
        "total_files": total_files,
        "file_types": dict(extensions)
    }
@app.get("/analyze/structure")
def analyze_structure():
    project_root = Path(__file__).resolve().parents[2]

    ignored_dirs = {".venv", ".git", "__pycache__", "node_modules"}

    directories = []
    python_files = []
    documentation_files = []
    config_files = []

    for item in project_root.rglob("*"):
        if any(part in ignored_dirs for part in item.parts):
            continue

        if item.is_dir():
            relative_path = item.relative_to(project_root)
            directories.append(str(relative_path))

        elif item.is_file():
            relative_path = str(item.relative_to(project_root))

            if item.suffix == ".py":
                python_files.append(relative_path)

            elif item.suffix.lower() in {".md", ".txt"}:
                documentation_files.append(relative_path)

            elif item.name.startswith(".") or item.suffix in {".json", ".yaml", ".yml", ".toml"}:
                config_files.append(relative_path)

    return {
        "repository_name": project_root.name,
        "total_directories": len(directories),
        "total_python_files": len(python_files),
        "total_documentation_files": len(documentation_files),
        "total_configuration_files": len(config_files),
        "directories": directories,
        "python_files": python_files,
        "documentation_files": documentation_files,
        "configuration_files": config_files
    }