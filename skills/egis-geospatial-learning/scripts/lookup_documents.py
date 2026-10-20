#!/usr/bin/env python3
"""Query *optionally installed, author-approved* EGIS PDFs (PyMuPDF only when needed).

    python lookup_documents.py list
    python lookup_documents.py check
    python lookup_documents.py check --require-all
    python lookup_documents.py search --query "accuracy assessment" --scope lesson --limit 5

The public Skill contains no PDFs. Obtain course files via the repository README.
All paths are resolved relative to this installed Skill folder.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "lookup" / "knowledge-index.json"


def read_manifest():
    return json.loads(INDEX.read_text(encoding="utf-8"))["files"]


def select_files(files, scope):
    return [f for f in files if scope == "all" or f.get("kind") == scope]


def pdf_module():
    try:
        import fitz  # type: ignore
    except ImportError:
        raise SystemExit("PDF reading requires PyMuPDF. Install with: python -m pip install pymupdf")
    return fitz


def list_files(files):
    found = 0
    for f in files:
        present = (ROOT / f["path"]).is_file()
        found += int(present)
        state = "INSTALLED" if present else "NOT INSTALLED"
        print(f'{state:13} {f.get("kind", "?"):10} {f["name"]} ({f.get("pages", "?")} pages)')
    print(f"Installed {found}/{len(files)} course PDFs. To request them, see the repository README.")


def check(files, require_all=False):
    existing = [f for f in files if (ROOT / f["path"]).is_file()]
    missing = len(files) - len(existing)
    if not existing:
        print(f"No course PDFs installed ({missing} listed). This is expected in the public Skill. See README to request access.")
        return 1 if require_all else 0
    fitz = pdf_module()
    errors = 0
    for f in existing:
        path = ROOT / f["path"]
        try:
            with fitz.open(path) as doc:
                if len(doc) != f.get("pages"):
                    raise ValueError(f'page count {len(doc)} vs index {f.get("pages")}')
            print("OK", f["name"])
        except Exception as e:
            errors += 1
            print("ERROR", f["name"], str(e), file=sys.stderr)
    print(f"Checked {len(existing)}/{len(files)} installed PDFs; missing: {missing}; invalid: {errors}.")
    if missing:
        print("Not all approved course PDFs are installed; see the repository README.")
    return 1 if errors or (require_all and missing) else 0


def search(files, query, limit, context_chars):
    needle = " ".join(query.split()).casefold()
    if not needle:
        print("Error: non-empty --query is required", file=sys.stderr)
        return 2
    existing = [f for f in files if (ROOT / f["path"]).is_file()]
    if not existing:
        print("No course PDFs are installed. The public Skill contains only a document catalog. Request PDFs via the README or use general geospatial guidance.")
        return 0
    fitz = pdf_module()
    seen = 0
    for f in existing:
        path = ROOT / f["path"]
        try:
            with fitz.open(path) as doc:
                for i, page in enumerate(doc):
                    txt = " ".join(page.get_text(sort=True).split())
                    pos = txt.casefold().find(needle)
                    if pos < 0:
                        continue
                    start = max(0, pos - context_chars)
                    end = min(len(txt), pos + len(needle) + context_chars)
                    print(f"{f['name']} | PDF page {i+1} | {txt[start:end]}")
                    seen += 1
                    if seen >= limit:
                        return 0
        except Exception as e:
            print(f"ERROR {path}: {e}", file=sys.stderr)
    if seen == 0:
        print("No local matches; this does not establish that the topic is absent from figures or missing PDFs.")
    if len(existing) < len(files):
        print(f"Notice: only {len(existing)}/{len(files)} course PDFs installed; results may be incomplete.")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for op in ("list", "check", "search"):
        p = sub.add_parser(op)
        p.add_argument("--scope", choices=("all", "lesson", "practical"), default="all")
        if op == "check":
            p.add_argument("--require-all", action="store_true", help="Fail if any PDF from the catalog is missing")
        if op == "search":
            p.add_argument("--query", required=True)
            p.add_argument("--limit", type=int, default=10)
            p.add_argument("--context-chars", type=int, default=90)
    args = parser.parse_args()
    files = select_files(read_manifest(), args.scope)
    if args.command == "list":
        list_files(files)
        return 0
    if args.command == "check":
        return check(files, args.require_all)
    return search(files, args.query, max(1, args.limit), max(0, args.context_chars))


if __name__ == "__main__":
    raise SystemExit(main())
