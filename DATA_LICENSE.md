# Data and Configuration Licensing

This repository contains several different kinds of material:

1. **Configuration and policy artifacts**  
   - Example: detector configurations, RAG reference profiles, DPIA checklists, assurance-case skeletons, telemetry schemas, unlearning test specifications.

2. **Prompt and evaluation artifacts**  
   - Example: sanitised red-team prompt sets, seed probe templates, evaluation scenario descriptions.

3. **Code and scripts (optional helpers)**  
   - Example: small validation or helper scripts in `ci_examples/` or similar.

4. **Documentation and prose**  
   - Example: README files, explanatory notes, and guidance text.

Because these categories have different reuse expectations, this document clarifies the licensing for each.

---

## 1. Configuration and policy artifacts

**Scope.** This section applies to non-code, machine-readable configuration and policy files, including for example:

- Detector configs (e.g., `detectors/*.yaml`)
- RAG / agent reference profiles and evaluation scenarios (e.g., `rag_policy_evals/*`)
- Telemetry schemas (e.g., `telemetry_schema/*.json`)
- DPIA checklists and templates (where provided as text or structured files)
- Assurance-case skeletons and risk/control matrices
- Unlearning / editing test specifications

**License.**  
These configuration and policy artifacts are licensed under the:

> **Creative Commons Attribution 4.0 International (CC BY 4.0) license**

You are free to:

- Share: copy and redistribute the material in any medium or format.  
- Adapt: remix, transform, and build upon the material for any purpose, including commercial use.

Under the following conditions:

- Attribution: you must give appropriate credit, provide a link to the license, and indicate if changes were made.  
  - A practical way to do this is to cite the associated ACM paper and this repository in documentation or release notes.

A plain-language summary and the full legal code are available at:  
https://creativecommons.org/licenses/by/4.0/

**Recommended attribution form:**

> “Configuration templates and policy artifacts adapted from:  
>  Keivan Navaie, *Personal Data in Foundation Model Systems: Lifecycle Risks, Measurement, and Governance*,  
>  and associated artifact repository (Lancaster University). Licensed under CC BY 4.0.”

You may tailor the wording to your context, provided the required attribution is preserved.

---

## 2. Prompt and evaluation artifacts

**Scope.** This section applies to:

- Sanitised red-team prompt sets (e.g., `red_team_prompts/*.yaml`)
- Example evaluation prompts and scenarios
- Synthetic canary or probe descriptions provided as text

**License.**  
All such **sanitised prompts and evaluation artifacts** are also licensed under:

> **Creative Commons Attribution 4.0 International (CC BY 4.0)**

The same freedoms and obligations as in Section 1 apply. In particular:

- You may reuse, adapt, and extend these prompts and scenarios for internal testing, academic work, and production deployments.
- You must attribute the source (paper + repository) when you redistribute or publish derivative artifacts.

When adapting prompts, please ensure that any new content remains compliant with local laws and does not incorporate real personal data without an appropriate lawful basis.

---

## 3. Code and scripts

**Scope.** This section applies to any code in this repository, for example:

- Helper scripts in `ci_examples/` (e.g., `validate_artifacts.py`)
- Other optional utilities, if present

**License.**  
Code is **not** covered by CC BY 4.0. It is instead licensed under the software license in the top-level `LICENSE` file (for example, MIT or BSD-3-Clause).

Please consult `LICENSE` for the precise terms that apply to code.

---

## 4. Documentation and prose

Short snippets of documentation and prose (such as `README.md` and directory-level guidance) should generally be treated as supporting material for the configurations and prompts.

Unless explicitly stated otherwise in a given file, you may treat these text artifacts as licensed under **CC BY 4.0** when reusing or adapting them in your own documentation, provided that:

- You give appropriate attribution to the original author(s) and this repository.
- You clearly separate your own commentary from quoted or adapted material.

Where a different license is required for a specific document, this will be indicated at the top of that file.

---

## 5. Third-party material

This repository may refer to external tools, libraries, or datasets developed and licensed by third parties. Such third-party components are **not** covered by this license.

- Always check the original source for the license terms applicable to any external tool, library, or dataset.
- When in doubt, assume that external resources are subject to their own licensing and must be obtained separately.

---

## 6. No warranty

All materials in this repository are provided **“as is”**, without warranty of any kind, express or implied. They are intended as evidence-informed **starting points** that must be adapted and validated for your own systems, threat models, and legal obligations.

It is your responsibility, as a controller or deployer, to ensure that any use of these materials is compliant with applicable data-protection, security, and sector-specific regulations.
