# DPIA Checklist for LLM / RAG / Agent Systems

**Scope.**  
This checklist is designed for Data Protection Impact Assessments (DPIAs) covering:

- Pre-training and fine-tuning,
- Deployment (including RAG indices and agent/tool stacks),
- Ongoing operations and monitoring,

for systems that process personal data (PD) with foundation models (LLMs/LMMs), in line with GDPR Art. 35 and relevant supervisory DPIA guidance.   

Use it as a **content checklist**: every item should either be *completed* or explicitly marked *not applicable* with a clear justification.

For each checkbox, you can optionally capture:

- **Status:** e.g., Done / In progress / N.A. (with reason)  
- **Evidence / links:** pointers to documents, tickets, or dashboards  
- **Owner:** accountable person/role  

---

## A. Roles & Processing Context

**A1. Controllers, processors, and processing activities**

- [ ] Identify and record controller and processor roles, including all vendors and subprocessors.  
- [ ] Map the processing activities for this system across the lifecycle (data collection/ingest, training, fine-tuning, deployment, monitoring/analytics).   

**Notes / Evidence / Owner:**  

---

**A2. System scope and deployment footprint**

- [ ] Describe model types and versions (e.g., base FM, fine-tuned variants, RAG/agent configurations) in scope.  
- [ ] Enumerate endpoints and interfaces (APIs, UIs, tools), tenants, and user populations.  
- [ ] Specify jurisdictions and data flows, including any cross-border transfers and hosting locations. :contentReference[oaicite:2]{index=2}  

**Notes / Evidence / Owner:**  

---

## B. Purposes, Lawful Bases, and Minimization

**B1. Purposes and lawful bases per lifecycle stage**

- [ ] Document purposes for each relevant stage: pre-training, fine-tuning, evaluation, deployment, and monitoring.  
- [ ] For each dataset/source, record lawful basis (consent, contract, legitimate interests with LIA, legal obligation, etc.) and link to records of processing.   

**Notes / Evidence / Owner:**  

---

**B2. Data categories, sources, and minimization**

- [ ] List categories of PD processed (e.g., identifiers, contact details, behavioural logs) and their sources (web, enterprise systems, user prompts, third parties).  
- [ ] Describe how special-category data (e.g., health, ethnicity, biometrics) is identified, excluded, or handled with enhanced safeguards where in scope.  
- [ ] Explain minimization measures: curation, filtering, deduplication, sampling, or aggregation applied at each stage, and justify any residual PD.   

**Notes / Evidence / Owner:**  

---

## C. Training-Data Provenance and Documentation

**C1. Provenance and curation pipelines**

- [ ] For each dataset, record provenance: licences/terms, accessibility (public vs. restricted), collection/ingest dates, and domain.   
- [ ] Describe source allow/deny lists, dataset inclusion/exclusion rules, and PD filtering/deduplication pipelines.  
- [ ] Provide metrics on filter/dedup effectiveness (e.g., PII recall, residual PD estimates) where available.   

**Notes / Evidence / Owner:**  

---

**C2. Documentation and accounting**

- [ ] Link to dataset documentation artifacts (datasheets/data cards) for major training/fine-tuning sets. :contentReference[oaicite:7]{index=7}  
- [ ] Reference pre-training/fine-tuning logs that show pipeline steps, configurations, and notable changes.  
- [ ] If differential privacy is applied, attach DP accounting outputs (ε, δ, composition assumptions) and any privacy–utility analyses.   

**Notes / Evidence / Owner:**  

---

## D. Prompts, Logs, and Secondary Use

**D1. Policy on prompts/outputs and reuse**

- [ ] State whether user prompts and outputs are used for further training, evaluation, or debugging.  
- [ ] Provide the legal basis and necessity/proportionality rationale for any such reuse.  
- [ ] Describe transparency mechanisms (notices, in-product explanations) and user controls (opt-out, toggles, separate consent flows).   

**Notes / Evidence / Owner:**  

---

**D2. Telemetry, logging, and retention**

- [ ] Enumerate telemetry and log fields collected for this system (inputs, outputs, RAG events, tool usage, detector hits, etc.), aligned with data minimization.   
- [ ] Define retention schedules per log class, including pseudonymization or aggregation strategies where feasible.  
- [ ] Describe access controls (roles, RBAC/ABAC) on logs and dashboards, and any use of encryption or secure enclaves.   

**Notes / Evidence / Owner:**  

---

## E. RAG / Agents and Access Control

**E1. RAG corpus and retrieval controls**

- [ ] Define the scope of any RAG or external knowledge corpora (tenant documents, web data, third-party sources).   
- [ ] Describe indexing policies: PD redaction/replacement, deduplication, partitioning per tenant or sensitivity level.  
- [ ] Specify retrieval-time access controls: ACL/ABAC rules, policy-check components, and how violations are detected and logged.   

**Notes / Evidence / Owner:**  

---

**E2. Tools, plugins, and egress control**

- [ ] Inventory all tools/plugins/agents (e.g., email, calendar, search, DB, browser, file store) that the model or agent can call.   
- [ ] Document scopes and least-privilege permissions per tool (data access, network egress, write operations).  
- [ ] Describe egress control mechanisms: domain allow-lists, payload size limits, structured schemas for tool outputs, and post-tool content checks (e.g., PII scanning).   

**Notes / Evidence / Owner:**  

---

## F. Risk Assessment (Threats and Tests)

**F1. Threat identification**

- [ ] Identify privacy-relevant threats for this system, including (as applicable):  
  - Training-data extraction/memorization,  
  - Inversion and reconstruction,  
  - Membership inference (record- or user-level),  
  - RAG corpus exfiltration and cross-tenant retrieval,  
  - Insider misuse or abuse of elevated access,  
  - Logging/telemetry leakage, cache bleed, and monitoring misuse.   
- [ ] Record which threats are in-scope vs. out-of-scope and justify any exclusions.

**Notes / Evidence / Owner:**  

---

**F2. Tests, metrics, and acceptance criteria**

- [ ] Describe the privacy evaluation suite used (where applicable):  
  - Canary insertion and exposure metrics,  
  - Membership inference (including TPR@FPR in {10⁻⁴, 10⁻⁵}),  
  - Targeted extraction/red-team probes,  
  - Output and corpus PII/PD scanning,  
  - RAG/agent policy-violation probes (retrieval and tool egress).   
- [ ] Document acceptance criteria and thresholds (e.g., canary-exposure ceilings, detector TPR/FPR targets, allowed slip-rate, RAG violation FN/FP budgets).   
- [ ] Link to evaluation reports and CI/regression dashboards.

**Notes / Evidence / Owner:**  

---

## G. Rights Handling and Unlearning

**G1. Data subject rights workflows**

- [ ] Describe workflows and channels for data subject rights: access, rectification, erasure, restriction, objection, and portability as applicable.   
- [ ] Explain how records in training sets, RAG corpora, and logs can be located or approximated (search and tracing strategy, limitations, and fallback approaches).  
- [ ] Describe communication templates and timelines (SLA) for responses.

**Notes / Evidence / Owner:**  

---

**G2. Erasure, unlearning, and repair**

- [ ] Describe the erasure plan for this system, covering:  
  - Corpus-level and index-level purges,  
  - RAG de-indexing and cache invalidation,  
  - Model-level unlearning or targeted edits where applicable.   
- [ ] Define how cross-snapshot leakage is controlled: pre/post tests, exposure comparisons, and regression gates.  
- [ ] Link to the unlearning/repair SOP and evidence of effect (e.g., Table 13 outputs, snapshot-delta results).   

**Notes / Evidence / Owner:**  

---

## H. Monitoring, Incidents, and Governance

**H1. Monitoring plan and KPIs**

- [ ] Specify monitoring cadence (e.g., continuous, daily, weekly) for privacy-relevant metrics such as:  
  - Exposure / canary metrics,  
  - MIA metrics at low FPR,  
  - Detector block/deny rates and slip-rate,  
  - RAG/agent policy-violation events,  
  - Tool egress anomalies and cross-tenant retrieval hits.   
- [ ] Define change-control triggers (e.g., new model version, major corpus changes, new tools, threshold adjustments).  

**Notes / Evidence / Owner:**  

---

**H2. Incident response and escalation**

- [ ] Outline the incident response process for privacy incidents, including:  
  - Containment steps (e.g., disabling endpoints, tightening filters/ACLs),  
  - Forensic investigation and root-cause analysis,  
  - Communication and notification obligations (supervisory authorities, affected data subjects) where criteria are met.   
- [ ] Define roles and responsibilities (e.g., DPO, product owner, SRE/on-call) and escalation paths.  
- [ ] Specify how DPIA and assurance-case artifacts are updated post-incident.

**Notes / Evidence / Owner:**  

---

## I. Residual Risk and Decisions

**I1. Residual risk statement**

- [ ] Summarize residual risks to data subjects after mitigations (including technical, organizational, and legal safeguards) are applied.  
- [ ] Explicitly note mitigations **not adopted**, with rationale (e.g., disproportionate burden, technical infeasibility, conflicts with other obligations).   

**Notes / Evidence / Owner:**  

---

**I2. Decision, sign-off, and review cadence**

- [ ] Record the decision outcome of the DPIA (e.g., proceed with controls, proceed with additional safeguards, do not proceed).  
- [ ] Capture accountable sign-off (roles and names) and any conditions attached (e.g., milestones for additional controls).  
- [ ] Specify re-evaluation schedule (e.g., annually, on major changes, post-incident) and link to assurance case, risk register, and model/data cards.   

**Notes / Evidence / Owner:**  

---

## J. Threat Modelling and LINDDUN Artifacts

**J1. System DFD and threat analysis**

- [ ] Attach a system data-flow diagram (DFD) covering training pipelines, inference endpoints, RAG indices, tools/agents, logs, and telemetry.   
- [ ] Include a privacy threat table (e.g., LINDDUN/GO or equivalent) enumerating threats, mitigations, and residual risks across components.   
- [ ] Link identified threats and mitigations back to DPIA items (A–I) and to assurance-case claims.

**Notes / Evidence / Owner:**  

---

## K. Control Substitution (If Deviating from Defaults)

Use this section if you adopt alternative controls or operating points relative to default reference profiles (e.g., detection thresholds, RAG profiles, telemetry defaults).

**K1. Substitution summary and equivalence claim**

- [ ] Describe the scope of substitution: which control(s) are being replaced or altered (e.g., different PD detector, alternative RAG index architecture, new threshold rule).   
- [ ] Provide rationale for the change (technical, legal, product constraints) and compare risks vs. the default profile.  
- [ ] State the **outcome-equivalence claim**: which KPIs and targets you commit to match or exceed (e.g., TPR@FPR=10⁻⁴, non-allow-listed egress=0, retention limits).   

**Notes / Evidence / Owner:**  

---

**K2. Operating point, harm budget, and re-evaluation**

- [ ] Document the new operating point(s): thresholds/policies (τ) selected using the rule in Section 5.3.2 (base rate π, cost ratio C_FN/C_FP, FPR budget α).   
- [ ] Update the harm budget (e.g., maximum allowable PD events per 100k interactions) and monitoring cadence.  
- [ ] Attach re-evaluation results:  
  - ROC/DET or PR curves with 95% CIs,  
  - Low-FPR metrics (e.g., TPR@FPR∈{10⁻⁴,10⁻⁵}),  
  - Canary exposure counts, RAG violation FN/FP, tool-egress statistics.  
- [ ] Describe regression gates used to approve the change and any rollback plan / drift triggers; record approvals (e.g., DPO, risk committee).   

**Notes / Evidence / Owner:**  

---

**Usage note.**  
This checklist is deliberately **implementation-agnostic**: it aligns to the DPIA structure in Section 7 and Table 16 of the paper but can be instantiated with your own templates, tools, and governance frameworks. For each item, either provide concrete evidence or explicitly justify why it is out of scope for the system under assessment.
