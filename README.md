# RepoLens AI

An autonomous repository intelligence platform that helps engineering teams understand unfamiliar codebases through repository analysis and agent-based investigation.

## Overview

RepoLens AI analyzes a software repository in two stages:

1. Basic Baseline Analysis — Provides basic repository statistics.
2. Repository Investigation Agent — Performs deeper repository inspection and generates evidence-based findings.

The project also includes an evaluation workflow that compares the baseline approach with the agent-based approach.

---

## Problem

Understanding an unfamiliar repository can take significant time.

Basic repository analysis can provide useful statistics such as:

- Total files
- Total directories
- Python files

However, statistics alone do not explain:

- What documentation exists
- What dependencies are configured
- What potential risks exist
- What strengths the repository has
- What evidence supports the findings

RepoLens AI addresses this by using an investigation agent to perform deeper repository analysis.

---

## Solution

### 1. Basic Baseline Analysis

The baseline analysis provides repository-level statistics including:

- Repository name
- Total files
- Total directories
- Python files
- Analysis type

Endpoint:

```text
GET /analyze/baseline
```

Example response:

```json
{
  "repository": "example-repo",
  "total_files": 245,
  "total_directories": 38,
  "python_files": 62,
  "analysis_type": "baseline"
}
```

### 2. Repository Investigation Agent

The investigation agent performs a deeper analysis of the repository and produces evidence-backed findings. It inspects the repository structure and content to answer questions such as:

- What is the project about?
- Which documentation artifacts exist?
- What dependencies are declared?
- Does the repo show signs of maintainability or risk?
- What evidence supports each conclusion?

This is designed to help teams quickly understand an unfamiliar codebase without manually reading every file.

---

## Evaluation Workflow

RepoLens AI includes an evaluation process to compare:

- Baseline analysis performance
- Agent-based investigation performance

The objective is to measure how much more useful and informative the deeper analysis is when compared to simple statistical summaries.

This workflow can be used to validate:

- Coverage of repository understanding
- Quality of generated findings
- Relevance of evidence
- Practical usefulness for engineering teams

---

## Typical Use Cases

- Onboarding to a new repository
- Quick codebase assessment before a migration
- Security and risk review
- Architecture discovery
- Evaluating repo health and documentation quality

---

## Architecture Summary

RepoLens AI combines a lightweight baseline analyzer with a repository investigation layer:

- Crawl the repository structure
- Extract relevant metadata
- Inspect files and project configuration
- Synthesize findings from evidence
- Return actionable insights

This creates a structured bridge between raw repository data and human-understandable intelligence.

---

## Example Workflow

1. Submit a repository for analysis.
2. Run the baseline endpoint to collect repository stats.
3. Trigger the investigation agent for deeper review.
4. Review findings and supporting evidence.
5. Compare the results against the baseline for decision-making.

---

## Notes

RepoLens AI is designed to accelerate repository comprehension by combining statistics, evidence gathering, and agent-driven reasoning.

It is especially useful when the goal is not just to know how large a repository is, but also to understand what it contains, how it is structured, and what risks or strengths can be inferred from it.
