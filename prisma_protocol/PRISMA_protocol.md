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
