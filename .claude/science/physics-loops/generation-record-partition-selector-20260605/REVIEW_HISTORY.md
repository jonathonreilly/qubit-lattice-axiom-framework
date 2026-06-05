# Review History

## 2026-06-05 self-review

- Replayed partition-selector runner: PASS=25 FAIL=0.
- Replayed existing two-sector readout runner: PASS=32 FAIL=0.
- Checked claim boundary: partition selected, weights/dynamics not selected.
- Checked no-laundering boundary around K/CPT context: fixed K/CPT remains a
  supplied readout-context input, not a new derivation.

## Required review

Independent audit should verify:

- exact central idempotent enumeration;
- K/CPT orbit interpretation;
- K-odd status of the doublet-splitting operator;
- no promotion from partition selection to value selection.
