# Handoff

This branch repairs the audited-conditional W8a statistics-product row by
changing the source theorem from a potentially overbroad "product form on the
retained surface" reading to a bounded theorem under a supplied product-form
joint instance.

Changed source files:

- `docs/STATISTICS_ATOM_REDUCES_TO_PRODUCT_FORM_ON_RETAINED_GLEASON_SURFACE_BOUNDED_NOTE_2026-06-12.md`
- `scripts/frontier_statistics_atom_reduces_to_product_form_2026_06_12.py`
- `logs/runner-cache/frontier_statistics_atom_reduces_to_product_form_2026_06_12.txt`

What closes:

- The old conditional blocker asked for either a retained derivation or an
  accepted bounded premise for repeated registrations being carried by
  `sigma tensor sigma`. The note now makes that premise explicit and row-local.
- Local pipeline evidence: the row becomes `effective_status: unaudited`,
  `ready: true`, with no old conditional blocker text. Generated audit outputs
  were restored and are not part of this branch.

What remains open:

- Physical derivation of product-form repeated registrations.
- Any R-D adoption, occupancy-cell selection, durability-to-weight coupling, or
  iid/typicality claim.

Verification performed:

- `PYTHONPATH=scripts python3 scripts/frontier_statistics_atom_reduces_to_product_form_2026_06_12.py` -> `TOTAL: PASS=26 FAIL=0`
- `python3 -m py_compile scripts/frontier_statistics_atom_reduces_to_product_form_2026_06_12.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only`
- `git diff --check`

`python3 scripts/vocab_lint.py --report-only docs/` reports existing baseline
human-review vocabulary drift outside this branch; no touched file is reported.
