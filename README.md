# Artifacts for "Personal Data in Foundation Model Systems: Lifecycle Risks, Measurement, and Governance"

This repository contains the reproducibility and deployment-oriented artifacts
promised in:

> K. Navaie, "Personal Data in Foundation Model Systems: Lifecycle Risks,
> Measurement, and Governance", ACM, 2025.

The artifact pack is aligned with ACM's Artifact Review and Badging policy
("Artifacts Available" and "Artifacts Evaluated – Functional"). It provides:

- Machine-readable **inventory and PRISMA protocol** for the systematically
  synthesized evidence base (Appendix A).
- **Red-team prompt sets** and **canary/extraction/MIA recipes** for
  evaluating personal-data leakage (Sections 5, 6, 7).
- **Detector configurations and operating-point guidance** for PD/PII scanning
  and related detectors (Tables 5, 6, 28).
- **RAG and agentic-stack privacy reference profiles** and evaluation scenarios
  (Tables 19–21).
- **Governance artifacts**: DPIA checklist, privacy assurance-case skeleton,
  telemetry schema, and control-substitution pack (Section 7, Appendix B).
- **Unlearning / editing test-suite specification** for PD-focused erasure
  workflows (Section 6.4).
- A **Practitioner Quick Start (one pager)** mapped to the paper’s reference
  profiles and metrics (Appendix A, Table 28).

All thresholds, profiles, and checklists are *illustrative and non-normative*.
They are intended as evidence-informed starting points that must be calibrated
to local threat models, architectures, and regulatory obligations.

## Repository layout

- `prisma_protocol/` – PRISMA 2020 protocol and search/selection artifacts.
- `inventory/` – `survey_corpus.csv` with coded fields for the included
  studies and guidance.
- `red_team_prompts/` – prompt sets for PD leakage, extraction, and policy
  violation probing.
- `detectors/` – reference configurations for text, vision, and ASV PD detectors.
- `dp_recipes/` – example DP-SGD and user-level DP recipes and accounting
  notebook.
- `rag_policy_evals/` – RAG and agent reference profiles and evaluation
  scenarios.
- `dpiA_template/` – DPIA checklist and template for FM/RAG/agent systems.
- `assurance_case/` – privacy assurance-case skeleton (claims, arguments,
  evidence).
- `telemetry_schema/` – canonical schema for PD-relevant telemetry and events.
- `unlearning_tests/` – reference tests for unlearning/edits and snapshot
  regression gates.
- `quick_start/` – 1-page practitioner quick start.
- `ci_examples/` – examples of CI integration for leakage tests.

## How to use this artifact pack

There are three primary use cases:

1. **Reproducing the systematic review inventory**

   - See `prisma_protocol/PRISMA_protocol.md` and `prisma_protocol/regenerate_inventory.py`.
   - Running the script regenerates `inventory/survey_corpus.csv` from the
     recorded queries and selection decisions, up to availability of the
     original sources.

2. **Instantiating evaluation recipes**

   - Use `red_team_prompts/pd_leakage_prompts.yaml` and
     `rag_policy_evals/rag_eval_scenarios.md` to seed extraction and policy
     violation probes against your own FM / RAG stack.
   - Detector configs in `detectors/` plus the operating-point guidance in
     `detectors/detector_eval_guidelines.md` support low-FPR evaluation
     (TPR@FPR in {1e-4, 1e-5}) for PD detectors.

3. **Building governance and assurance artifacts**

   - The DPIA checklist (`dpiA_template/dpiA_llm_checklist.md`) and assurance
     case skeleton (`assurance_case/privacy_assurance_case_skeleton.yaml`)
     map the risk×evidence×control matrix to concrete documentation and
     metrics.
   - `telemetry_schema/telemetry_schema.json` provides a minimal telemetry
     schema for PD-relevant events (RAG retrieval, tool egress, PD scans,
     deletion signals).

## Environment

The optional Python utilities (for PRISMA scripts and synthetic evaluations)
depend on:

- Python ≥ 3.10
- See `environment/requirements.txt` or `environment/environment.yml`.

These utilities are not required to use the checklists or templates, but they
support regenerating the machine-readable inventory and running example tests.

## Contact and support

For questions or suggestions, please contact:

- Keivan Navaie – k.navaie@lancaster.ac.uk
