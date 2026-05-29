## Summary

Repairs the critical audited-conditional RP/P2 gauge-extension row by narrowing
it to the standalone transfer and invariance theorem the audit said could pass:

- fixed-background two-step transfer positivity in temporal gauge;
- `det(M_KS+mI)`, `spec(H_hat)`, and `Z` permutation invariance.

The previous source text also claimed a downstream P2 / `AC_phi_lambda`
residual tightening. This branch removes that claim from scope instead of
adding unaudited dependencies.

## Science Boundary

- no new axioms
- no observed target values
- no fitted selectors
- no external comparator
- no P2 residual tightening claim
- no `AC_phi_lambda` closure or irrelevance claim
- no author-applied audit promotion

## Verification

```text
python3 -m py_compile scripts/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py
python3 scripts/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

Key runner readout:

```text
SCORECARD: PASS=7 FAIL=0
sampled SU(3) positivity failures: 0/200
sampled U(1) positivity failures: 0/200
determinant invariance: PASS
spectrum invariance: PASS
trace invariance: PASS
```

Audit queue readout after pipeline regeneration:

```text
rp_p2_gauge_extension_and_realization_residual_note_2026-05-28
rank: 1
ready: true
queue_reason: unaudited
criticality: critical
deps:
  - staggered_only_det_positivity_case_a_note_2026-05-17
  - reflection_positivity_gauge_half_cauchy_schwarz_narrow_theorem_note_2026-05-10
runner classification: C=17
```

## Target Row

`rp_p2_gauge_extension_and_realization_residual_note_2026-05-28`

The branch is intended to reset this row for independent re-audit. It does not
retag the ledger as retained.
