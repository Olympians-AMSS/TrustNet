#!/usr/bin/env python3
"""Genereaza SINTEZA.md din fragmentele marcate in dosar/*.md.

Utilizare (din orice director): python3 scripts/generate_sinteza.py
Nu necesita pachete externe.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
DOSAR = ROOT / "dosar"
OUTPUT = ROOT / "SINTEZA.md"
START = "<!-- SINTEZA:START -->"
END = "<!-- SINTEZA:END -->"

# Ordinea dosarului este stabila, indiferent de ordinea fisierelor din Git.
ORDER = [
    "specificatii.md",
    "modelare-domeniu.md",
    "contracte-invarianti.md",
    "stari-comportament.md",
    "validare-arhitectura.md",
]

# Sabloanele nu reprezinta contributii.
SKIP = {"SABLON_CONTRIBUTIE.md", "sablon_contributie.md", "template.md"}


def get_metadata(source: str, label: str) -> str | None:
    match = re.search(rf"^\*\*{re.escape(label)}:\*\*\s*(.+?)\s*$", source, re.M | re.I)
    return match.group(1).strip() if match else None


def get_title(source: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", source, re.M)
    return match.group(1).strip() if match else fallback


def get_excerpt(source: str, path: Path) -> str:
    if source.count(START) != 1 or source.count(END) != 1:
        raise ValueError(f"{path.name}: trebuie sa existe exact o pereche de marcaje SINTEZA")
    before, rest = source.split(START, 1)
    excerpt, after = rest.split(END, 1)
    if END in before or START in excerpt or START in after:
        raise ValueError(f"{path.name}: marcaje SINTEZA in ordine incorecta")
    excerpt = excerpt.strip()
    if not excerpt:
        raise ValueError(f"{path.name}: fragmentul pentru sinteza este gol")
    return excerpt


def contribution_files() -> list[Path]:
    if not DOSAR.is_dir():
        return []
    paths = [p for p in DOSAR.glob("*.md") if p.is_file() and p.name not in SKIP]
    priority = {name: i for i, name in enumerate(ORDER)}
    return sorted(paths, key=lambda p: (priority.get(p.name, len(ORDER)), p.name.casefold()))


def make_summary() -> str:
    sections = [
        "# TrustNet — Sinteza dosarului de proiectare",
        "",
        "> Acest document este generat automat din fragmentele marcate în fișierele din `dosar/`.",
        "> Pentru detalii, justificări și verificări, accesați contribuțiile complete.",
        "",
    ]
    files = contribution_files()
    if not files:
        sections += [
            "*Nu există încă contribuții în `dosar/`. Adăugați fișiere `.md` pe baza șablonului.*",
            "",
        ]
        return "\n".join(sections)

    # Citim si validam TOATE contributiile inainte de a suprascrie sinteza.
    entries = []
    for path in files:
        raw = path.read_text(encoding="utf-8")
        title = get_title(raw, path.stem.replace("-", " ").capitalize())
        author = get_metadata(raw, "Autor") or "Nespecificat"
        discussion = get_metadata(raw, "Discuție")
        status = get_metadata(raw, "Status")
        excerpt = get_excerpt(raw, path)
        link = "dosar/" + quote(path.name)
        entries.append((title, author, discussion, status, excerpt, link))

    sections += ["## Cuprins", ""]
    for i, (title, _, _, _, _, link) in enumerate(entries, start=1):
        sections.append(f"{i}. [{title}]({link})")
    sections.append("")

    for i, (title, author, discussion, status, excerpt, link) in enumerate(entries, start=1):
        sections += [f"## {i}. {title}", "", f"**Autor:** {author}  "]
        if status:
            sections.append(f"**Status:** {status}  ")
        if discussion:
            sections.append(f"**Discuție:** {discussion}  ")
        sections += [f"**Contribuție completă:** [Deschide documentul]({link})", "", excerpt, ""]

    return "\n".join(sections).rstrip() + "\n"


def main() -> int:
    try:
        content = make_summary()
        old = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else None
        if old == content:
            print("SINTEZA.md este deja actualizata.")
        else:
            OUTPUT.write_text(content, encoding="utf-8")
            print(f"Actualizat: {OUTPUT.relative_to(ROOT)}")
        print(f"Contributii incluse: {len(contribution_files())}")
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"EROARE: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
