# Handoff

Target row: `uv_gauge_to_yukawa_bridge_sc_vs_pert_note`.

Repair summary:

- The old row overclaimed that the canonical tadpole-improved surface selects
  the perturbative coefficient.
- This branch preserves the exact finite coefficient algebra and moves the
  expansion-domain selector out of scope.
- A dedicated runner has a source-note firewall for the repaired scope. The
  shared Ward runner is intentionally untouched to avoid invalidating its
  retained row.

Verification before PR:

- `python3 -m py_compile scripts/uv_gauge_to_yukawa_bridge_sc_vs_pert_scope_check.py`
- `python3 scripts/uv_gauge_to_yukawa_bridge_sc_vs_pert_scope_check.py`
- `bash docs/audit/scripts/run_pipeline.sh`

Pipeline result:

- Target row reset to `unaudited`.
- Audit queue rank: 3.
- Ready queue count: 60.
- Effective status counts after regeneration: `audited_conditional=14`,
  `unaudited=1195`.
- Stale audit invalidations: 0.
- `git diff --check` passed.

Reviewer should extract the science and let the audit lane assign effective
status.
