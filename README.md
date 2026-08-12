# Physician-Scientist Impact Dashboard

A Streamlit dashboard presenting the MIT Physician Scientist Research Group's
four-tier, twelve-dimension scoring framework, applied to a cohort of
physician-scientists. This README covers project structure, setup, and
navigation for developers working on or extending the app.

## Project Structure

This is a native Streamlit multipage app. Streamlit automatically builds the
sidebar navigation from the file/folder layout below — there is no manual
routing code.

```
.
├── Home.py                          # Entry point / landing page
├── pages/
│   ├── 1_Methodology.py             # Scoring, normalization, and weighting methodology
│   ├── 2_Framework.py               # 4-tier / 12-dimension framework description
│   ├── 3_Distributions.py           # Score distribution histograms
│   ├── 4_Impact_Scores.py           # Interactive per-physician-scientist score viewer
│   ├── dimension_score_breakdown.csv
│   ├── final_score-3.csv
│   └── Framework.jpeg
├── requirements.txt
└── README.md
```

Note that all data tables and images consumed by the app live directly in
the `pages/` folder alongside the page scripts, rather than in a separate
`data/` folder:

- `dimension_score_breakdown.csv` — per-dimension scores for each
  physician-scientist
- `final_score-3.csv` — final composite tier and overall scores
- `Framework.jpeg` — the framework diagram displayed on the Framework page

The numeric prefixes on files in `pages/` control the order they appear in
the sidebar; Streamlit strips the prefix and underscores when rendering the
page name. Renaming or reordering files in `pages/` will change both the
sidebar order and the URL slug for that page, so update any hardcoded links
(e.g. `st.page_link`) if you rename a page.

## Prerequisites

- Python 3.10+ (matches the version used in development; check with
  `python --version`)
- pip (or another package manager of your choice — conda/uv/poetry all work
  fine with `requirements.txt`)

## Installation

Clone the repo, then set up a virtual environment and install dependencies:

```bash
git clone <repo-url>
cd <repo-directory>

python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

pip install -r requirements.txt
```

Core dependencies include `streamlit` and `pandas`; check `requirements.txt`
for the full, pinned list.

## Running the App

From the project root, launch the app via `Home.py`, the entry point for the
multipage app:

```bash
streamlit run Home.py
```

By default this serves the app at `http://localhost:8501`. Streamlit will
hot-reload on file changes — if it doesn't pick up an edit automatically,
use the "Rerun" option in the top-right menu or press `R` in the browser
window.

To run on a different port or make it accessible on your local network:

```bash
streamlit run Home.py --server.port 8502 --server.address 0.0.0.0
```

## Navigation and Page Overview

Once the app is running, the sidebar (expand it via the `>` arrow in the
top-left if collapsed) lists all five pages:

| Page | File | Description |
|---|---|---|
| **Home** | `Home.py` | Landing page: background on the research group, the Data Output subgroup, and general navigation guidance |
| **Methodology** | `pages/1_Methodology.py` | Summary of the scoring methodology — normalization approach (linear vs. logarithmic, max normalization), data sourcing, weighting decisions, and composite scoring equations |
| **Framework** | `pages/2_Framework.py` | Description of the 4 tiers and 12 dimensions used to represent the physician-scientist pipeline |
| **Distributions** | `pages/3_Distributions.py` | Histograms showing the distribution and frequency of scores across all dimensions and tiers for the full cohort |
| **Impact Scores** | `pages/4_Impact_Scores.py` | Interactive tool to look up and visualize an individual physician-scientist's scores across all dimensions |

Streamlit preserves widget state within a session as you move between pages,
but each page runs its own script top-to-bottom on load/rerun, so any
page-local computation (filtering, aggregation, etc.) will re-execute each
time that page is visited.

## Data

The dashboard currently reflects a scored cohort of 74 physician-scientists
across the 12-dimension framework. As noted above, `dimension_score_breakdown.csv`,
`final_score-3.csv`, and `Framework.jpeg` are stored inside `pages/` rather
than a separate `data/` folder. When loading these files, use paths relative
to the page script itself (e.g. via `os.path.dirname(__file__)`) rather than
absolute local paths, so the app runs correctly on other machines.
