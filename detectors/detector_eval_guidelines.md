# Evaluation Guidelines for Personal-Data Detectors

This document describes how to evaluate personal-data (PD) detectors used to
scan inputs, intermediate artefacts, and outputs of foundation-model systems.
It is intended to be used with the reference configurations in:

- `text_pd_detector_config.yaml`
- `vision_pd_detector_config.yaml`
- `asv_pd_config.yaml`

The goal is to support **stable, low-FPR operation** in high-stakes
deployments, with metrics such as **TPR@FPR = {1e-4, 1e-5}** reported as in
the accompanying paper.

## 1. Scope

These guidelines cover three detector families:

1. **Text PD detectors** – scanning prompts, completions, logs, and RAG
   corpora for PD/PII-like patterns.
2. **Vision PD detectors** – detecting faces or other directly identifying
   visual content in images and video frames.
3. **ASV (automatic speaker verification) detectors** – detecting whether
   an audio segment contains a speaker whose voice should be treated as PD.

The detectors may be used for:

- **Blocking** (hard refusal or tool suppression),
- **Redaction** (masking PD tokens or regions), and
- **Logging and monitoring** (telemetry, audit trails).

## 2. Terminology

- **TPR (True Positive Rate):** Fraction of PD-positive samples correctly
  flagged by the detector.
- **FPR (False Positive Rate):** Fraction of PD-negative samples incorrectly
  flagged as containing PD.
- **Operating point:** A specific configuration (threshold, rule set, etc.)
  at which the detector is run in production.
- **FPR budget:** Maximum tolerable FPR at deployment; we target
  `FPR ≤ 1e-4` (or stricter for some use cases).

Unless otherwise noted, metrics are defined over *samples* (texts, images,
audio clips). Category-level metrics can be derived where needed.

## 3. Dataset construction

### 3.1 Positive and negative sets

For each modality, construct:

- A **PD-positive set**:
  - Contains samples with clear PD markers (names, contact details, IDs, faces,
    voices of identifiable individuals, etc.).
  - Includes both **common** PD patterns and **edge cases** relevant to your
    domain (e.g., local address formats, national IDs).
- A **PD-negative set**:
  - Contains samples *without* PD.
  - Should include:
    - High-entropy technical text / images / audio.
    - Data with PD-like structure but non-identifying (e.g., random strings
      that look like IDs but are synthetic).
    - Domain-specific content (e.g., code snippets, system prompts, logs)
      where false alarms would be costly.

#### Text

- Positive examples:
  - Synthetic and curated sentences with:
    - Full names + addresses.
    - Emails, phone numbers, account numbers, national IDs.
    - Structured records (e.g., "Name, DOB, SSN, Address").
- Negative examples:
  - Long passages of non-personal technical text or documentation.
  - Synthetic sentences with decoy patterns that *should not* be flagged
    (e.g. `"user_id=9f1b2c..."` where there is no actual PD semantics).

#### Vision

- Positive examples:
  - Images with one or more clearly visible faces.
  - Faces under occlusion, partial views, and different lighting conditions.
- Negative examples:
  - Abstract or synthetic images, landscapes, UI screenshots, text-only images.
  - Body-only images without faces (if your policy only treats *faces* as PD).

#### ASV / Audio

- Positive examples:
  - Short utterances (2–10 seconds) from known speakers that must be treated
    as PD, aligned with your enrolment set.
- Negative examples:
  - Non-speech audio, background noise, music.
  - Speech from non-enrolled speakers if your threat model treats only
    enrolled speakers as PD.
  - Synthetic speech that is explicitly non-identifying.

### 3.2 Splits

For each modality, partition data into:

- **Train** (optional, if the detector is trainable),
- **Validation** (for threshold and hyperparameter selection),
- **Test** (held-out, for final reporting and CI regression checks).

The **test set** must remain fixed across detector versions to support
longitudinal comparisons.

## 4. Threshold selection and reporting

### 4.1 Validation-phase thresholding

On the **validation set**:

1. Score all samples with the detector.
2. Compute an empirical ROC curve (TPR vs. FPR).
3. Identify the smallest score threshold `τ` such that:

   - `FPR_val(τ) ≤ FPR_budget`, e.g.:

     - `FPR_budget = 1e-4` (default),
     - `FPR_budget = 1e-5` for particularly sensitive pipelines.

4. Record:
   - `τ`,
   - `TPR_val(τ)`,
   - `FPR_val(τ)`.

### 4.2 Test-phase reporting

Fix `τ` from validation, then on the **test set**:

- Compute:
  - `TPR_test(τ)`,
  - `FPR_test(τ)`,
  - Category-specific TPR (e.g., email vs. address vs. national ID) where
    labels permit.

Report at least:

- `TPR_test@FPR≈1e-4`,
- Optionally `TPR_test@FPR≈1e-5` if achievable.

If multiple operating points are used in production (e.g., "strict" vs.
"permissive"), report metrics for each.

### 4.3 Multi-category detectors

For detectors that output multiple PD categories:

- Compute **micro-averaged** metrics over all categories for a global view.
- Report **per-category metrics** for categories with distinct risk profiles
  (e.g., "national_id" vs. "name").

## 5. Modality-specific considerations

### 5.1 Text detectors

- Evaluate both:
  - **Token-level** performance (detecting exact PD spans), and
  - **Sample-level** performance (did the detector flag the sample at all?).
- Where token-level labels exist, report:
  - Span-level precision, recall, and F1.
- Ensure evaluation covers:
  - Multiple languages and scripts, where relevant.
  - Domain-specific jargon and structured logs.

### 5.2 Vision detectors (faces)

- For **face detection**:
  - Label ground-truth bounding boxes.
  - A detection is a true positive if IoU ≥ 0.5 with a ground-truth face.
  - FPR can be defined as:
    - False detections per image, or
    - False detections per megapixel (for dense frames).
- For **face identification / recognition**:
  - Report ROC / DET curves over verification pairs (same vs. different).
  - Target operating points where:
    - False accept rate (FAR) ≤ 1e-4 (or stricter).
  - Align thresholds with `vision_pd_detector_config.yaml` fields for FAR.

### 5.3 ASV detectors

- Treat each verification attempt (enrolment utterance vs. probe utterance)
  as one sample.
- Compute:
  - **False Accept Rate (FAR)** – non-enrolled speaker accepted as enrolled.
  - **False Reject Rate (FRR)** – enrolled speaker rejected.
- Select thresholds to satisfy `FAR ≤ FPR_budget` on validation; report
  `1 − FRR` as TPR on the test set.
- Consider evaluation protocols from common ASV benchmarks, but ensure
  your PD-positive/negative definitions match your privacy threat model.

## 6. CI gating and regression checks

We recommend using these metrics in **CI pipelines** for model updates.

For each new detector version:

1. Evaluate on the fixed **test set**.
2. Compare to **baseline metrics** at the same operating points (e.g.,
   `TPR@FPR=1e-4`).

### 6.1 Suggested gates

Define acceptable deltas relative to the baseline detector:

- **Primary gate (safety):**
  - `FPR_test(τ_new) ≤ FPR_budget` (strict requirement).
- **Secondary gate (utility):**
  - `TPR_test(τ_new) ≥ TPR_test(τ_baseline) − δ_TPR`,
  - where δ_TPR is a small tolerance (e.g., 0.02 = 2 percentage points).

If either gate fails, the CI job should fail and flag the regression.

### 6.2 Per-category checks

For high-risk categories (e.g., "national_id", "financial_account"):

- Track category-specific TPR and FPR.
- Define stricter δ_TPR for those categories.

## 7. Logging and telemetry

When detectors are integrated in production, log:

- Detector version and configuration hash.
- Event type (input, corpus_scan, output, tool_call, etc.).
- Categories hit and actions taken (block, redact, log-only).
- Aggregated metrics (e.g., hits per 10⁶ tokens, per endpoint, per tenant).

Logs should follow the canonical schema described in
`../telemetry_schema/telemetry_schema.json`, allowing:

- Periodic recomputation of empirical FPR proxies,
- Monitoring of drift in detector behaviour, and
- Support for assurance-case evidence.

## 8. Reproducibility

To support reproducible evaluations:

- Maintain:
  - Fixed test sets for each modality.
  - Versioned code and configuration (this repository).
- When publishing metrics externally:
  - Record detector version,
  - Operating point (thresholds, categories included),
  - Dataset version and protocol.

This ensures that metrics reported for PD detectors are comparable over time
and traceable back to specific configurations and datasets.
