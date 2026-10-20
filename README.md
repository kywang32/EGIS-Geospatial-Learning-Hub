# EGIS Geospatial Learning Hub

[![Skill & code: MIT](https://img.shields.io/badge/Skill%20%26%20code-MIT-blue.svg)](LICENSE)
[![Course PDFs: access on request](https://img.shields.io/badge/14%20course%20PDFs-access%20on%20request-orange.svg)](COURSE-MATERIALS-ACCESS.md)

**A multilingual AI learning assistant for Earth Geospatial Information Science (EGIS), covering cartography, GIS, remote sensing, GNSS, integrated 3S, QGIS, and spatial analysis.**

Developed and maintained by **Kunyang Wang** using original teaching materials for Hiroshima University courses. This is an **independent educational project**, not an official Hiroshima University product or service.

> **Open Skill; controlled-access course library.** All plugin/Skill instructions, manifests, scripts, and metadata in this repository are public under MIT. **The 14 course PDFs (397 pages) are not included in this repository or its public releases.** Request access to the PDFs separately; the Skill is usable without them, but cannot claim to have read or cite course pages unless those files are actually available.

## Who can use it?

Students, researchers and instructors interested in geospatial science. The assistant uses English by default and can respond in Chinese, Japanese or another language. Its focus is understanding spatial concepts, interpreting results and building sound workflows—not automated coursework or examination preparation.

## Features

- Clarifies geospatial principles across GIS, remote sensing (RS), GNSS and integrated 3S.
- Offers conceptual support for mapping, projections, data models, image classification and spatial statistics.
- Explains QGIS-centered practical approaches, with ArcGIS guidance when applicable.
- **Optional course-grounded mode:** given approved PDF copies accessible to the AI host, draws on the 8 lesson PDFs for theory and 6 practical manuals for software workflows; distinguishes their content from general explanations.
- Includes a course catalog and optional PDF keyword-search script with exact filename and 1-based PDF page references.
- Explicitly reports when source files cannot be accessed. A JSON catalog is **not** an embedded vector store or automatic indexing service.

## Public vs. requested materials

| Component | Provided publicly in this repository? | Terms |
|---|---|---|
| `SKILL.md`, `plugin.json`, `agents/openai.yaml` | Yes | MIT |
| `lookup/knowledge-index.json` (filenames/topics/page counts) | Yes | MIT |
| `scripts/lookup_documents.py` | Yes | MIT |
| Project icon and public documentation | Yes | See [LICENSE](LICENSE) and third-party notices, if any |
| **8 lecture PDFs + 6 practical PDF manuals** | **No; access by author approval** | **Not covered by MIT; no general redistribution license** |

### Requesting the 14 course PDFs

The complete teaching-material package is distributed separately at the author's discretion to researchers, educators and students.

**📚 [Request Access to EGIS Course Materials](https://drive.google.com/file/d/1NjzFnw_eet3YHiuKZITbOl8nxNwieNbd/view)**

The 14 original EGIS teaching materials are available upon request for academic and educational purposes. Researchers, educators, and students may request access through Google Drive. All requests are reviewed and approved by the author, Kunyang Wang.

When requesting access, briefly describe your affiliation (if any), intended educational/research use and an email address through the restricted provider's own access-request form. Do **not** post personal details in a public GitHub issue.

Approval is **not automatic**. Please do not publish the private download link as if it were a publicly downloadable file. Recipients must respect the [course-material access and use terms](COURSE-MATERIALS-ACCESS.md). Permission to receive a copy is **not** permission to redistribute it or include the PDFs in public forks/releases.

### Course catalog (files distributed separately)

**Lessons (8 PDFs)**

| PDF filename | Topic | Pages |
|---|---|---:|
| `I-1 Begining + Cartography 1 4 print.pdf` | Introduction and cartography I | 44 |
| `I-2 Cartography 2 4 print.pdf` | Cartography II | 38 |
| `I-3 GIS Concepts I 4 print.pdf` | GIS concepts I | 52 |
| `I-4 GIS Concepts II 4 print.pdf` | GIS concepts II | 40 |
| `I-5 Remote Sensing Concepts I 4 print.pdf` | Remote sensing concepts I | 40 |
| `I-6 Remote Sensing Concepts II 4 print.pdf` | Remote sensing concepts II | 47 |
| `I-7 3S Perspectives 4 print.pdf` | GIS–RS–GNSS integration and emerging technology | 27 |
| `II-5 Remote Sensing Images Classification & Assessment 4 print.pdf` | Image classification and accuracy assessment | 30 |

**Practical manuals (6 PDFs)**

| PDF filename | Topic | Pages |
|---|---|---:|
| `EGIS II Practical Manual - Basic Operations Supplement.pdf` | QGIS basics supplement | 3 |
| `EGIS II Practical Manual - Landsat & Urban Heat.pdf` | Landsat and urban surface temperature | 20 |
| `EGIS II Practical Manual - Raster Analysis.pdf` | Raster and terrain analysis | 15 |
| `EGIS II Practical Manual - Spatial Equity - 2SFCA.pdf` | Spatial accessibility (2SFCA) | 15 |
| `EGIS II Practical Manual - Spatial Pattern Discovery.pdf` | Spatial patterns and exploratory spatial statistics | 10 |
| `EGIS II Practical Manual - Vector Analysis with QGIS.pdf` | Buffers, overlays and vector analysis | 16 |

The two former PPTX lessons (I-7 and II-5) are distributed as **PDF only**. The `knowledge-index.json` lists their filenames and expected page counts.

## Installation

### Plugin (host that supports Agent Plugins)

1. Download this public GitHub repository or its public ZIP release.
2. Keep `plugin.json`, `assets/` and `skills/` together at the plugin root.
3. Install using your platform's own Agent Plugins import workflow. Host features and install methods vary.
4. Start with ordinary GIS questions. The Skill works without the restricted PDFs, using general geospatial knowledge and verified sources where appropriate.

### Standalone Agent Skill

Download the **public Skill-only ZIP** release and import its `egis-geospatial-learning/` folder into a compatible Agent Skills host. The Skill ZIP contains no course PDFs and no plugin manifest.

### Optional: add approved PDFs locally

After receiving permission and downloading the **private course-material ZIP**:

1. Unzip the private package; inside is a `references/` directory containing the 14 PDFs.
2. Copy its **contents** into the installed Skill's `references/` directory (next to `SKILL.md`, `lookup/`, and `scripts/`), retaining the original filenames exactly.
3. Keep these files in your **local/private installation only**. Do not upload to public GitHub branches, forks, PRs, logs, or releases.
4. Confirm file availability with:

```bash
python skills/egis-geospatial-learning/scripts/lookup_documents.py list
python skills/egis-geospatial-learning/scripts/lookup_documents.py check --require-all
```

The script can also be run from the Skill root as `python scripts/lookup_documents.py ...`. `check` uses PyMuPDF when files are present; to install it in a local Python environment use `python -m pip install pymupdf`. PDF access in an AI host depends on its available reading/shell tools; local installation does not guarantee automatic indexing.

### Optional keyword lookup

```bash
python skills/egis-geospatial-learning/scripts/lookup_documents.py search --query "land surface temperature" --limit 5
python skills/egis-geospatial-learning/scripts/lookup_documents.py search --scope practical --query "buffer" --limit 5
```

If no reference PDFs have been installed, the script reports that they are not available and points to the request instructions. Text-only lookup can miss diagrams or screenshots.

## Example prompts

Without course PDFs:

- *Explain the distinction between GIS, remote sensing and GNSS.*
- *Why do coordinate reference systems matter for spatial analysis?*
- *How does supervised classification differ from unsupervised classification?*
- *Outline a reproducible QGIS buffer/overlay workflow and its quality checks.*

With approved local PDFs available to the host:

- *Explain classification accuracy assessment using the EGIS II-5 lesson, with PDF page citations.*
- *Follow the EGIS Practical Manual for Landsat and Urban Heat; note any steps that require exercise datasets.*

## Repository structure

```text
EGIS-Geospatial-Learning-Hub/
├── README.md
├── LICENSE                         # MIT: public Skill and code
├── COURSE-MATERIALS-ACCESS.md      # Policy and access instructions
├── PUBLICATION_CHECKLIST.md
├── .gitignore                      # Excludes private PDF references
├── plugin.json
├── assets/gpt-icon.png
└── skills/
    └── egis-geospatial-learning/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── lookup/knowledge-index.json
        ├── scripts/lookup_documents.py
        └── references/README.md   # Empty of course PDFs in public repository
```

## Limitations and responsible use

- The public repository **does not** bundle teaching slides, figures or exercise datasets. Its default answers must not be presented as extracted from the restricted PDFs.
- Exercise data (Landsat scenes, population rasters, etc.) are not included in either the public repository or the restricted PDF bundle unless separately supplied.
- QGIS/ArcGIS interfaces and methods evolve: verify version-dependent advice against official sources.
- Treat AI responses, citations, maps and calculations as needing independent scientific review.
- The GitHub repository is public; GitHub cannot require approval to download its public files. **Only the separate PDF package has approval-based access.**

## Copyright and contributions

© 2026 Kunyang Wang. The public Skill, plugin manifest and original code are covered by the [MIT License](LICENSE). **The 14 separately supplied PDFs are excluded from that license and are not offered under CC BY 4.0**; see [COURSE-MATERIALS-ACCESS.md](COURSE-MATERIALS-ACCESS.md). Some course figures or maps may involve third-party rights. Use of the Hiroshima University name identifies a teaching context and does not imply institutional endorsement.

Open a GitHub Issue for bugs, suggestions and improvements to the **public Skill or script** (not for personal access credentials or private materials). Pull requests should never include the course PDFs.
