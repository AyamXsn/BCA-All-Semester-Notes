#!/usr/bin/env python3
"""Structural checks for BCA-All-Semester-Notes (Python standard library only)."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SEMESTERS = [f"Semester-{n:02d}" for n in range(1, 9)]
SOURCE_SUFFIXES = {".c", ".cpp", ".java", ".py", ".js", ".sql"}

def markdown_link_errors(path: Path):
    errors = []
    content = path.read_text(encoding="utf-8", errors="replace")
    for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', content):
        target = target.strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0].split()[0].strip("<>")
        if not target:
            continue
        if not (path.parent / target).resolve().exists():
            errors.append(f"{path.relative_to(ROOT)}: broken relative link: {target}")
    return errors

def main():
    errors = []
    for semester in SEMESTERS:
        directory = ROOT / semester
        if not directory.is_dir():
            errors.append(f"Missing semester directory: {semester}")
            continue
        if not (directory / "README.md").is_file():
            errors.append(f"Missing semester README: {semester}/README.md")
        for subject in (p for p in directory.iterdir() if p.is_dir()):
            if not (subject / "README.md").is_file():
                errors.append(f"Missing subject README: {subject.relative_to(ROOT)}/README.md")

    markdown = list(ROOT.rglob("*.md"))
    for path in markdown:
        if not path.read_text(encoding="utf-8", errors="replace").strip():
            errors.append(f"Empty Markdown file: {path.relative_to(ROOT)}")
        errors.extend(markdown_link_errors(path))

    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in SOURCE_SUFFIXES and path.stat().st_size == 0:
            errors.append(f"Empty source file: {path.relative_to(ROOT)}")

    required = [
        "README.md", "CONTRIBUTING.md", "LICENSE",
        "Resources/Syllabus-Verification.md", "Tools/README.md",
    ]
    for rel in required:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required file: {rel}")

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(" -", error)
        return 1

    print("VALIDATION PASSED")
    print(f"Markdown files checked: {len(markdown)}")
    print("Semester README files: 8/8")
    print("Relative Markdown links: no broken links found")
    print("Note: academic correctness and all language runtimes are not verified by this tool.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
