#!/usr/bin/env python3
"""
Generate inventory/survey_corpus.csv from a BibTeX file.

Usage (from repo root):

    pip install bibtexparser
    python inventory/gen_survey_inventory_from_bib.py references.bib inventory/survey_corpus.csv

- Input:  a .bib file containing all the studies and guidance you included.
- Output: CSV with bibliographic fields filled; PD-specific fields left empty
  for manual annotation.
"""

import argparse
import csv
import sys
from pathlib import Path

import bibtexparser


HEADER = [
    "id",
    "bibkey",
    "title",
    "authors",
    "year",
    "venue",
    "type",
    "doi_or_url",
    "task_domain",
    "model_class",
    "model_size",
    "data_regime",
    "threat_type",
    "mitigation",
    "measurement_metric",
    "governance_hooks",
    "fm_surface_training_data",
    "fm_surface_parameters",
    "fm_surface_prompts_outputs",
    "fm_surface_rag_indices",
    "fm_surface_agents_tools",
    "fm_surface_logs_telemetry",
    "threat_model",
    "mechanism",
    "evaluation_datasets",
    "evaluation_scale",
    "lifecycle_phase",
    "quality_signals",
    "limitations",
    "novelty_vs_closest_prior",
    "notes",
]


def guess_venue(entry: dict) -> str:
    """Pick a reasonable venue string from BibTeX fields."""
    for key in ("journal", "booktitle", "institution", "organization", "howpublished"):
        if key in entry and entry[key].strip():
            return entry[key].strip()
    return ""


def guess_type(entry: dict) -> str:
    """
    Heuristic classification:
    - 'standard_guidance' for standards / regulator / official guidance.
    - 'study' otherwise.

    You can always edit this column manually later.
    """
    entry_type = entry.get("ENTRYTYPE", "").lower()
    venue = (guess_venue(entry) or "").lower()
    publisher = entry.get("publisher", "").lower()
    org = entry.get("organization", "").lower()

    text = " ".join([entry_type, venue, publisher, org])

    keywords_for_guidance = [
        "iso",
        "iec",
        "nist",
        "ico",
        "information commissioner's office",
        "european data protection board",
        "edpb",
        "european commission",
        "data protection authority",
        "regulation",
        "standard",
        "technical specification",
    ]

    if any(k in text for k in keywords_for_guidance):
        return "standard_guidance"

    # You might later refine: e.g. treat 'phdthesis' differently if you want.
    return "study"


def get_doi_or_url(entry: dict) -> str:
    doi = entry.get("doi", "").strip()
    if doi:
        # Allow either raw DOI or full URL; here we normalise to URL form
        if doi.lower().startswith("10."):
            return f"https://doi.org/{doi}"
        return doi
    url = entry.get("url", "").strip()
    return url


def parse_args(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("bib_path", type=Path, help="Input BibTeX file (e.g. references.bib)")
    parser.add_argument(
        "csv_path", type=Path, help="Output CSV path (e.g. inventory/survey_corpus.csv)"
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    if not args.bib_path.exists():
        raise SystemExit(f"BibTeX file not found: {args.bib_path}")

    with args.bib_path.open("r", encoding="utf-8") as f:
        db = bibtexparser.load(f)

    entries = db.entries

    # Ensure output directory exists
    args.csv_path.parent.mkdir(parents=True, exist_ok=True)

    with args.csv_path.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=HEADER)
        writer.writeheader()

        for i, entry in enumerate(entries, start=1):
            row = {h: "" for h in HEADER}
            row["id"] = i
            row["bibkey"] = entry.get("ID", "")
            row["title"] = entry.get("title", "").replace("\n", " ").strip()
            row["authors"] = entry.get("author", "").replace("\n", " ").strip()
            row["year"] = entry.get("year", "")
            row["venue"] = guess_venue(entry)
            row["type"] = guess_type(entry)
            row["doi_or_url"] = get_doi_or_url(entry)

            # All other fields left blank for manual annotation:
            # task_domain, model_class, model_size, data_regime, threat_type,
            # mitigation, measurement_metric, governance_hooks, fm_surface_*,
            # threat_model, mechanism, evaluation_datasets, evaluation_scale,
            # lifecycle_phase, quality_signals, limitations, novelty_vs_closest_prior, notes

            writer.writerow(row)

    print(f"Wrote {len(entries)} rows to {args.csv_path}")


if __name__ == "__main__":
    main(sys.argv[1:])
