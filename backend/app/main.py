from fastapi import FastAPI
from collections import Counter

app = FastAPI(
    title="RepoLens AI",
    description="Repository Intelligence Platform for analyzing software repositories.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to RepoLens AI",
        "status": "Backend is running successfully"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

from fastapi import FastAPI
from pathlib import Path

app = FastAPI(
    title="RepoLens AI",
    description="Repository Intelligence Platform for analyzing software repositories.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to RepoLens AI",
        "status": "Backend is running successfully"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/analyze")
def analyze_repository():
    project_root = Path(__file__).resolve().parents[2]

    folders = []
    files = []

    for item in project_root.iterdir():
        if item.is_dir():
            folders.append(item.name)
        elif item.is_file():
            files.append(item.name)

    return {
        "repository_name": project_root.name,
        "folders": folders,
        "files": files,
        "total_folders": len(folders),
        "total_files": len(files)
    }
@app.get("/analyze/details")
def analyze_details():
    project_root = Path(__file__).resolve().parents[2]

    structure = []

    for item in project_root.iterdir():
        structure.append({
            "name": item.name,
            "type": "directory" if item.is_dir() else "file"
        })

    return {
        "repository_name": project_root.name,
        "items": structure
    }
@app.get("/analyze/stats")
def analyze_stats():
    project_root = Path(__file__).resolve().parents[2]

    extensions = Counter()
    total_files = 0

    excluded_dirs = {".venv", ".git", "__pycache__"}

    for item in project_root.rglob("*"):
        if any(part in excluded_dirs for part in item.parts):
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
  