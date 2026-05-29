# Handoff

This branch repairs the audited-conditional
`rp_p2_gauge_extension_and_realization_residual_note_2026-05-28` row by
narrowing it to the standalone science the audit already accepted:

- fixed-background staggered two-step transfer positivity in temporal gauge;
- determinant / spectrum / trace relabeling invariance for a selected
  `hw = 1` triplet.

It removes the stronger source-note claim that this row tightens the downstream
P2 / `AC_phi_lambda` realization residual. Those downstream claims now remain
explicitly outside scope.

Verification:

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

No new axioms, observed targets, external comparators, or audit-status claims
are introduced.
