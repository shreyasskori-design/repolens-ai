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
@app.get("/analyze/summary")
def analyze_summary():
    project_root = Path(__file__).resolve().parents[2]

    ignored_dirs = {".venv", ".git", "__pycache__", "node_modules"}

    total_files = 0
    total_directories = 0
    python_files = 0
    has_documentation = False
    has_tests = False

    for item in project_root.rglob("*"):
        if any(part in ignored_dirs for part in item.parts):
            continue

        if item.is_dir():
            total_directories += 1

            if item.name.lower() in {"tests", "test"}:
                has_tests = True

        elif item.is_file():
            total_files += 1

            if item.suffix == ".py":
                python_files += 1

            if item.suffix.lower() in {".md", ".txt"}:
                has_documentation = True

    primary_language = "Python" if python_files > 0 else "Unknown"

    return {
        "repository_name": project_root.name,
        "total_files": total_files,
        "total_directories": total_directories,
        "primary_language": primary_language,
        "has_documentation": has_documentation,
        "has_tests": has_tests
    }
@app.get("/analyze/quality")
def analyze_quality():
    project_root = Path(__file__).resolve().parents[2]

    total_files = 0
    python_files = 0
    has_readme = False
    has_tests = False
    has_requirements = False
    has_gitignore = False

    ignored_dirs = {".venv", ".git", "__pycache__", "node_modules"}

    for item in project_root.rglob("*"):
        if any(part in ignored_dirs for part in item.parts):
            continue

        if item.is_file():
            total_files += 1

            if item.suffix == ".py":
                python_files += 1

            if item.name.lower() == "readme.md":
                has_readme = True

            if item.name.lower() == "requirements.txt":
                has_requirements = True

            if item.name.lower() == ".gitignore":
                has_gitignore = True

        if item.is_dir() and item.name.lower() in {"tests", "test"}:
            has_tests = True

    quality_score = 0
    strengths = []
    risks = []

    if has_readme:
        quality_score += 20
        strengths.append("Repository documentation is available")
    else:
        risks.append("README documentation is missing")

    if has_tests:
        quality_score += 20
        strengths.append("Test structure is available")
    else:
        risks.append("No dedicated test directory found")

    if has_requirements:
        quality_score += 15
        strengths.append("Dependency configuration is available")
    else:
        risks.append("Dependency configuration is missing")

    if has_gitignore:
        quality_score += 10
        strengths.append("Git ignore configuration is available")
    else:
        risks.append(".gitignore file is missing")

    if python_files > 0:
        quality_score += 20
        strengths.append(f"Repository contains {python_files} Python source files")
    else:
        risks.append("No Python source files found")

    if total_files >= 5:
        quality_score += 15
        strengths.append("Repository has a meaningful project structure")
    else:
        risks.append("Repository contains very few files")

    if quality_score >= 80:
        grade = "A"
    elif quality_score >= 60:
        grade = "B"
    elif quality_score >= 40:
        grade = "C"
    else:
        grade = "D"

    return {
        "repository_name": project_root.name,
        "quality_score": quality_score,
        "grade": grade,
        "strengths": strengths,
        "risks": risks,
        "evidence": {
            "total_files": total_files,
            "python_files": python_files,
            "has_readme": has_readme,
            "has_tests": has_tests,
            "has_requirements": has_requirements,
            "has_gitignore": has_gitignore
        }
    }