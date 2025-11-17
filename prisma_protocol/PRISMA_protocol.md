# PRISMA 2020 Protocol – Personal Data in Foundation Model Systems

This document records the systematic-review protocol used in:

> Keivan Navaie, *Personal Data in Foundation Model Systems: Lifecycle Risks, Measurement, and Governance* (evidence current to 2025-10-01).

The protocol follows PRISMA 2020 guidance and corresponds to Appendix A (“Systematic Review Protocol & Reproducibility (PRISMA 2020)”) in the manuscript. It governs only the **systematically synthesized evidence base** used to support empirical findings, measurement recipes, mitigation results, and governance expectations.

- **Scope of PRISMA synthesis**:  
  The PRISMA pipeline applies to the subset of records systematically identified and synthesized to support:
  - Section 5 (Measurement and Evaluation),
  - Section 6 (Mitigations),
  - Sections 7.2–7.4 (Supervisory expectations, DPIAs, assurance evidence),
  - and the repair guidance in Section 8.
- **Out of PRISMA scope**:  
  Background/definitional material (Sections 1–3) and design patterns (Section 9) are based on engineering synthesis and domain practice and were not subjected to PRISMA screening.
- **Multi-version records**:  
  When preprint and archival versions coexist (e.g., arXiv → conference/journal), the archival version is retained; multi-version records are counted once.
- **Machine-readable inventory**:  
  The “Included” count in the PRISMA flow diagram matches the rows of the machine-readable inventory (`inventory/survey_corpus.csv`) distributed with the artifact pack.

---

## 1. Objectives and Review Questions

### 1.1 Objectives

To systematically identify, characterize, and synthesize work on **personal data (PD)** in **foundation model systems**, including:

- Large language models (LLMs) and large multimodal models (LMMs),
- Retrieval-augmented generation (RAG) pipelines,
- Multi-tool / agentic systems and logging/telemetry layers,

with a focus on:

- Risks (memorization, extraction, inversion, membership inference, RAG/agent exfiltration, logging/telemetry leakage),
- Measurement protocols and metrics (e.g., low-FPR leakage evaluation, MIAs, exposure, RAG leak tests),
- Mitigations with operational results (data-centric controls, DP, unlearning, runtime mediation),
- Governance and assurance artifacts (DPIAs, assurance cases, standards/guidance).

### 1.2 Review questions (informal)

Examples of guiding questions:

1. **Risk and surface**  
   - How and where does PD appear in FM/RAG/agent systems (training data, parameters, prompts/outputs, RAG indices, tools, logs)?
2. **Measurement**  
   - Which metrics and protocols are used to measure PD risk (e.g., canary exposure, MIAs, extraction at low FPR), and at what operating points?
3. **Mitigations**  
   - What technical controls (data filters, DP, unlearning, runtime detectors) are proposed or evaluated, and how effective are they?
4. **Governance and assurance**  
   - How do regulatory/standards sources and internal governance work map to concrete controls, evidence artifacts, and KPIs?

---

## 2. Protocol and Registration

- The protocol (objectives, eligibility criteria, sources, search strings, selection, and data-extraction plan) was specified **a priori**.
- Because the review is engineering-focused and includes technical standards/regulator guidance (non-clinical, non-healthcare scope), it was **not preregistered on PROSPERO**.
- This document reproduces the protocol to support transparency and reproducibility.

---

## 3. Eligibility Criteria

### 3.1 Inclusion criteria

Records are included if they:

1. **Topic**  
   - Address **personal information/personal data** in:
     - Foundation models (LLMs/LMMs and closely related FM architectures), or
     - Derived systems: RAG pipelines, agents/toolchains, or logging/telemetry for FM systems.

2. **Operational content**  
   - Provide *operational* detail, such as:
     - Metrics and evaluation protocols,
     - Algorithms or mechanisms (e.g., DP-SGD, unlearning procedures, detectors),
     - Guarantees (e.g., differential privacy statements),
     - Controls (filters, policies, architectures),
     - Governance/assurance artifacts or patterns (DPIAs, assurance cases, audit frameworks).

3. **Venue / type**  
   - Peer-reviewed venues in:
     - ML/NLP/Systems/Security (e.g., NeurIPS, ICML, ICLR, ACL, IEEE S&P, CCS, USENIX Security, NDSS, PETS),
     - Journals and reputable conferences in these domains.
   - **Standards and regulator guidance** from recognised bodies (e.g., UK ICO, NIST, EU/EDPB, ISO/IEC, other DP authorities).

4. **Language and time**  
   - Language: **English**.  
   - Time window: works made publicly available from **January 2012** up to **2025-10-01**, with particular emphasis on **2022–2025** (frontier FM era).

5. **Jurisdiction/standards focus**  
   - Standards/regulator sources are limited to **EU/UK/US** (European Commission/EDPB, UK ICO, NIST, ISO/IEC, and relevant national DPAs) for depth and consistency.

### 3.2 Exclusion criteria

Records are excluded if they are:

- Purely philosophical or opinion pieces **without operational guidance**,
- Duplicates / superseded versions (earlier preprint replaced by archival version),
- Works on privacy **not related** to FMs/RAG/agents (e.g., classic DBMS security with no FM linkage),
- Non-English or not retrievable (e.g., broken links, inaccessible reports),
- General cybersecurity/AI-risk work without a **personal data + FM** angle.

---

## 4. Information Sources

The following sources were queried:

- **Digital libraries and indices**
  - ACM Digital Library
  - IEEE Xplore
  - ACL Anthology
  - arXiv (where no archival version exists)
  - SpringerLink
  - USENIX
  - NDSS
  - IEEE S&P
  - CCS
  - PETS
  - NeurIPS, ICML, ICLR, EMNLP, NAACL, TACL, JMLR, TMLR

- **Broad discovery**
  - Google Scholar
  - Bing (for supplementary discovery and citation chaining)

- **Standards/regulators**
  - UK ICO
  - NIST
  - EU (European Commission, EDPB)
  - ISO/IEC
  - Selected national data-protection authorities (DPAs) where relevant to FM/privacy guidance.

- **Search cut-off**
  - Final manual search date for electronic sources: **2025-09-01**.

---

## 5. Search Strategy (Databases and Targeted Sites)

### 5.1 Concept groups (synonyms)

Search terms were organised into concept groups and combined with Boolean operators, adapted to each portal’s syntax.

- **A — Models**
  - “frontier AI”, “foundation model*”, “large language model*”, LLM, “large multimodal model*”, transformer*, “generative AI”, specific model names (e.g., GPT, BERT).

- **B — Personal data and risks**
  - “personal information”, “personal data”, PII, “data protection”, “privacy leak*”, memorization, “training data extraction”, “model inversion”, “membership inference”, “prompt injection”, “RAG leakage”, “retrieval leakage”, “data exfiltration”.

- **C — Mitigations**
  - “differential privacy”, “DP-SGD”, unlearning, “machine unlearning”, “selective forgetting”, redaction, “PII detection”, “data deduplication”, PETs, FL, HE, MPC, TEE, “access control”, “policy engine”.

- **D — Governance / assurance**
  - audit, assurance, “assurance case”, conformance, compliance, “risk management”, DPIA, certification, standards.

- **E — Operational surfaces**
  - “retrieval-augmented generation”, RAG, agent*, “tool use”, plugin*, “long context”, logging, telemetry, “data lineage”, provenance.

- **F — Evaluation**
  - benchmark, metric, measurement, exposure, canary, probing, “red team*”.

- **G — Regulation / standards**
  - GDPR, “UK GDPR”, “NIST AI RMF”, “ISO/IEC 23894”, “ISO/IEC 42001”, “ISO/IEC 27701”, “ISO/IEC 29100”.

### 5.2 Boolean seed queries (examples)

Database-friendly cores (adapted per portal, e.g. ACM DL, IEEE Xplore, Scholar):

1. `(("foundation model" OR "large language model" OR LLM) AND (memorization OR "data extraction" OR "model inversion" OR "membership inference") AND ("personal data" OR "personal information" OR PII))`

2. `(("retrieval-augmented generation" OR RAG OR agent* OR "tool use" OR "long context") AND ("privacy leak*" OR "retrieval leakage" OR "prompt injection" OR "data exfiltration") AND ("personal data" OR PII))`

3. `((logging OR telemetry OR "usage data" OR monitoring) AND ("personal data" OR PII) AND (LLM OR "foundation model"))`

4. `(("differential privacy" OR "DP-SGD") AND (LLM OR "foundation model") AND ("personal data" OR PII OR "privacy guarantee"))`

5. `(unlearning OR "machine unlearning" OR "selective forgetting" OR redaction) AND (LLM OR "foundation model" OR RAG) AND ("personal data" OR PII OR memorization)`

6. `(("PII detection" OR "privacy filtering" OR "data deduplication" OR "dataset curation") AND (LLM OR "pretraining corpus" OR "foundation model"))`

7. `((audit OR assurance OR "assurance case" OR conformance OR compliance) AND (LLM OR "foundation model") AND (privacy OR "personal data"))`

### 5.3 Regulator/standards site-specific filters

- `site:ico.org.uk` with queries such as:
  - (“generative AI” OR “foundation model” OR LLM) AND “personal data”
- `site:nist.gov` with:
  - (AI AND privacy AND (audit OR risk OR assurance))
- `site:edpb.europa.eu` OR `site:europa.eu` with:
  - (“foundation model” OR LLM) AND “personal data”
- `site:iso.org` with:
  - (AI AND privacy AND risk)

### 5.4 Time window and updates

- We **prioritised 2022–2025-09-01**, which aligns with the deployment of large FM systems and associated guidance.
- Seminal pre-2022 work (especially on differential privacy, memorization, and unlearning) was included where relevant.
- All systematic searches were **last executed on 2025-09-01**.
- The evidence snapshot in the paper reflects the state of the literature and guidance as of **2025-10-01**.

---

## 6. Selection Process

A multi-stage selection process was used.

1. **Deduplication**
   - Primary merge key: DOI,
   - Fallback: arXiv identifier (when no DOI),
   - Next: exact Title + Year,
   - Finally: fuzzy title match (normalised Levenshtein ≥ 0.9).
   - When both arXiv and archival versions exist, the **archival version** is retained.

2. **Title/abstract screening**
   - Two reviewers independently apply the eligibility criteria.
   - Borderline items (e.g., ambiguous or incomplete abstracts) are passed to full-text review.

3. **Full-text assessment**
   - Inclusion/exclusion criteria applied with reasons recorded using a small taxonomy, e.g.:
     - “taxonomy mismatch” (not FM/RAG/agents or not about PD),
     - “no operational content” (conceptual essay without metrics/controls),
     - “superseded/duplicate”,
     - “out of scope”,
     - “non-English/non-retrievable”.
   - Disagreements resolved via discussion, with a **tie-break rule favouring inclusion** when operational content seems plausible.

The counts at each stage are reported in the PRISMA 2020 flow diagram (Fig. 11 in the manuscript) and reproduced in summary in Section 13 below.

---

## 7. Data Collection and Data Items

For each **included record**, we extracted:

- **Bibliographic metadata**
  - Authors, year, venue, DOI or other stable identifier.

- **Artifact type**
  - Paper, standard/guidance, report, or similar.

- **FM privacy surface coverage**
  - Training data,
  - Parameters/memorization,
  - Prompts/outputs,
  - RAG indices/embeddings,
  - Agents/tools,
  - Logs/telemetry.

- **Threat model**
  - Attackers and capabilities (e.g., extraction, MIAs, inversion, exfiltration through tools).

- **Mechanism / guarantee**
  - Techniques (e.g., DP-SGD, unlearning, filters, detectors, cryptographic protections), and any formal or informal guarantees.

- **Evaluation setup**
  - Metrics (e.g., TPR@FPR, exposure, precision@k),
  - Datasets and domains,
  - Scale (tokens, model size, number of models, number of tasks).

- **Governance hooks**
  - Evidence outputs relevant to assurance:
    - Tests and metrics,
    - Logs and telemetry,
    - Lineage/provenance artifacts,
    - Assurance case assets.

- **Limitations**
  - Stated or inferred limitations of the study or guidance.

- **Lifecycle phase**
  - Assessment, repair, design (and, where relevant, deployment/monitoring).

- **Novelty vs. closest prior**
  - How the work relates to prior art in methodology, metrics, or governance framing.

Extraction is recorded in a **structured schema**; a machine-readable CSV/JSON version is provided as part of the artifact pack (`inventory/survey_corpus.csv` and associated schema).

**Reference management**: a single BibTeX database is maintained, citing archival versions (with DOIs) where possible. Regulatory/standards documents are cited by document number and official URL.

---

## 8. Quality and Bias Assessment (Fit-for-Purpose)

Classical clinical risk-of-bias tools are not applicable to this heterogeneous, technical evidence base. Instead, we record and use **quality signals** to contextualise findings, including:

1. **Code/data availability**
   - Whether implementations and/or datasets are released.

2. **Reproducible metrics**
   - Presence of well-defined metrics (e.g., TPR@FPR with confidence intervals, exposure measures).

3. **Scale and coverage**
   - Token counts, number and type of models evaluated, number of domains/tasks.

4. **Comparative baselines**
   - Inclusion of baselines (e.g., non-private or non-unlearning versions, simple heuristics).
   - For MIAs and extraction, inclusion of blind/duplication/control-prompt baselines where available.

5. **Standards provenance (for guidance)**
   - Whether guidance is from official/regulator/standards bodies vs. non-binding interpretations.

Archival publications are prioritised where possible. Empirical claims (e.g., memorization and extraction rates) are triangulated across multiple sources when available, and non-archival preprints are flagged in text/tables.

Regulatory/standards sources are restricted to **official domains** and the latest available versions at the time of search.

---

## 9. Synthesis Methods

Given heterogeneity of tasks, models, metrics, and deployment contexts, **quantitative meta-analysis is not appropriate**.

We use:

- **Narrative synthesis**:
  - Organised around the FM privacy surface and attack surfaces.
- **Structured matrices**:
  - By surface / risk / mechanism (e.g., training-data memorization vs. DP-SGD mitigation),
  - Governance crosswalk mapping technical findings to regulatory/standards expectations and assurance artifacts.

We present:

- Trend counts (e.g., adoption of DP-SGD at FM scale; prevalence of RAG leakage evaluations),
- Qualitative characterization of gaps and limitations.

---

## 10. Reporting-Bias Considerations

To mitigate publication bias, venue skew, and “success-only” reporting:

1. **Inclusion of standards/regulator guidance**
   - Brings in non-academic but authoritative sources that may surface risks and mitigations underreported in research venues.

2. **Retention of influential preprints**
   - Where no archival version yet exists, impactful preprints are retained and clearly labelled as such.

3. **Explicit recording of superseded duplicates**
   - Earlier versions (e.g., arXiv v1) that are superseded by archival publications are recorded but not double-counted.

These choices are reflected in the machine-readable inventory and in the narrative synthesis.

---

## 11. Deviations from Protocol

- Any deviations from the initial protocol (e.g., expanded regulator list, additional concept terms, minor changes to search filters) are recorded in the **artifact changelog** accompanying the GitHub repository.
- No deviations materially changed the core inclusion logic (population, intervention, comparators, outcomes, or study designs of interest).

---

## 12. Update Policy

- The area is considered **fast-moving**, especially for:
  - Frontier FM deployments,
  - PD leakage techniques and defenses,
  - Regulator and standards guidance.
- The artifact pack includes scripts to re-run searches and refresh the machine-readable inventory.
- Periodic updates are anticipated; the manuscript represents the state of the evidence as of **2025-10-01**.

---

## 13. PRISMA 2020 Flow Diagram and Counts

The PRISMA 2020 flow diagram summarises the selection pipeline:

- Records identified via databases: **n = 1326**
- Records identified via websites/other sources (standards, regulators): **n = 118**
- Records after duplicates removed: **n = 1048**
- Records screened (title/abstract): **n = 1048**
- Records excluded at title/abstract: **n = 782**
- Reports sought for retrieval / full-text assessed: **n = 266**
- Reports not retrieved: **n = 9**
- Full-text reports excluded, with reasons: **n = 121**

**Included in review**:

- **Studies**: n = 104  
- **Standards/Guidance**: n = 32  

These counts correspond to the rows in `inventory/survey_corpus.csv` and to the subset of studies and standards/guidance used to support Sections 5–6 and 7.2–7.4 of the manuscript.

Exclusion reasons at full-text are categorised using the taxonomy:

- Out of scope (not FM/RAG/agents or not about PD),
- No operational content,
- Superseded/duplicate,
- Non-English or not retrievable,
- Irrelevant domain (e.g., general cybersecurity without PD/FM angle).

---

## 14. Relation to Artifact Pack

This protocol is implemented and made reproducible via the artifact pack:

- `inventory/survey_corpus.csv`  
  – machine-readable inventory of included records (task/domain, model class/size, data regime, threat type, mitigation, metrics, governance hooks).

- `inventory/` schema  
  – documentation of data fields and coding choices.

- `prisma_protocol/regenerate_inventory.*` (optional helpers)  
  – scripts and templates for re-running searches or rebuilding the inventory, where APIs and terms of use permit.

Users can:

- Inspect or extend the search strategy (concept groups, Boolean seeds, site filters),
- Replicate the selection process on new snapshots of the literature,
- Adapt the schema to related domains (e.g., non-personal privacy risks, broader AI assurance).

This completes the PRISMA 2020 protocol for the systematically synthesized evidence base in *Personal Data in Foundation Model Systems: Lifecycle Risks, Measurement, and Governance*.
