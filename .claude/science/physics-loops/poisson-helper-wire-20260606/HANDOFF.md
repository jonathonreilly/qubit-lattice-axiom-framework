# Handoff

Branch: `physics-loop/poisson-helper-wire-20260606`

Primary movement:

- Changes primary runner import to
  `import scripts.backreaction_poisson as bp`, which
  `scripts/audit_packet_script_deps.py` detects.
- Updates the source-packet verifier marker to that static import form.
- Refreshes:
  - `logs/runner-cache/backreaction_poisson_live_threshold_check.txt`
  - `logs/runner-cache/backreaction_poisson_live_threshold_source_packet_manifest_2026_06_04.txt`
  - `outputs/backreaction_poisson_live_threshold_source_packet_manifest_2026_06_04.json`

Science boundary:

- The live finite packet remains bounded support only.
- The old `G_crit ~= 0.011` threshold remains rejected by this packet; first
  sub-unit escape in the declared grid is `G=0.050`.
- No continuum horizon or Schrodinger-Newton closure claim is added.

Audit/result surfaces:

- `docs/audit/**` was not edited.

Next exact action:

- Reviewer/auditor can re-audit after packet build includes
  `scripts/backreaction_poisson.py` via `helper_runner_paths`.

