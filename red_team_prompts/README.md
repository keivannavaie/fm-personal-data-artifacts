# Red-Team Prompt Sets for Personal-Data (PD) Leakage

This folder contains *seed* prompt sets for probing personal-data (PD) leakage and unsafe PD handling in
foundation-model (FM) systems, including:

- standalone FMs / LLMs,
- RAG pipelines, and
- tool-augmented / agentic stacks.

The prompts are designed to instantiate the deployment-oriented red-teaming concepts described in the paper:

> K. Navaie, *Personal Data in Foundation Model Systems: Lifecycle Risks, Measurement, and Governance*, ACM, 2025.  

They are **illustrative and non-normative**: starting points for internal testing and assurance, not a coverage-complete
benchmark or certification scheme.

## Files

- `pd_leakage_prompts.yaml`  
  Machine-readable prompt sets grouped by category (e.g., canary extraction, generic PD leakage, RAG exfiltration,
  policy-bypass attempts). Each category includes:
  - a short goal description, and
  - example prompts with light templating (e.g., `{{CANARY_TOKEN}}`).

Additional prompt files can be added with similar structure (e.g., per-domain or per-language variants).

## Intended Use

These prompts are intended for **internal red-teaming and evaluation** by:

- privacy / security engineers,
- red-team and safety leads,
- ML and platform engineers responsible for FM, RAG, and agent deployments.

Typical use cases:

1. **Canary and PD-leakage checks**  
   - Seed models or retrieval corpora with synthetic canaries or synthetic PD-like records.  
   - Run prompt sets under controlled conditions to assess:
     - memorization / extraction behaviour,
     - PD-regurgitation channels through RAG and tools, and
     - the effectiveness of PD filters / guardrails.

2. **Guardrail / policy validation**  
   - Exercise refusal policies, PII/PD detectors, and RAG access-control rules using “policy-bypass” prompts.
   - Confirm that:
     - disallowed outputs are consistently blocked or redacted, and
     - telemetry correctly records blocked events.

3. **CI / regression testing**  
   - Integrate a stable subset of prompts into CI to detect regressions in:
     - leakage behaviour, and
     - guardrail effectiveness (e.g., new model versions, new tools, or new retrieval sources).

These prompts are *not* designed for benchmarking research systems in isolation; they are meant to be adapted to and
run against concrete deployments.

## Safety, Ethics, and Legal Considerations

Use of these prompts **must** comply with applicable law, internal policy, and contractual obligations.

- **Authorized targets only.**  
  Run these prompts only against systems and data for which you have explicit authorization and a clear legal basis
  (e.g., internal staging / test environments, or production systems under a controlled testing program).

- **No real personal data required.**  
  The default configurations assume *synthetic* canaries and PD-like records, not real individuals’ data. If you test
  with real PD, ensure that the lawful basis, DPIA, and safeguards are explicitly documented.

- **Respect access controls.**  
  Do not attempt to defeat organizational access controls (e.g., tenant isolation, role-based restrictions) outside a
  sanctioned security assessment.

- **Logging and retention.**  
  Treat any outputs containing PD (or synthetic PD that is difficult to distinguish from real) as PD for logging and
  retention purposes. Align logging with the telemetry schema in `../telemetry_schema/`.

These prompt sets are provided “as-is” with no guarantee of completeness; they do *not* enumerate all possible attack
vectors.

## Adapting and Extending

You are expected to **adapt** these prompts to your environment:

- Add domain-specific variants (e.g., healthcare, finance, HR) with *synthetic* entities and attributes.
- Localize to additional languages and scripts, ensuring that PD / PII categories are appropriate for the jurisdiction.
- Tune prompts to match emerging model behaviours or new tools (e.g., new APIs, new RAG indices).

When extending:

- Preserve the YAML structure (categories, goals, prompt lists).
- Document any high-risk or invasive probes clearly in comments.
- Keep a clear separation between:
  - *canary-based* prompts (using synthetic seeds), and
  - general policy-bypass / exfiltration prompts.

## Relationship to the Paper

This folder corresponds to the **“Red-team prompt sets for PD leakage”** artifact described in:

- Section 5 (Direct red teaming and prompt-based probing),
- Table 3 (Summary of accompanying artifacts), and
- Appendix A (artifact and reproducibility notes).

For reproducibility and traceability, cite the paper when using or adapting these prompts in publications or internal
reports.
