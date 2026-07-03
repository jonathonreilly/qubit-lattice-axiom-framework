# Handoff

This block targets the audited-conditional alpha_s narrow theorem.

Changed source packet:

- `docs/ALPHA_S_DERIVED_NARROW_THEOREM_NOTE_2026-05-10.md` now states that
  the powers `(1,1)` counterfactual has difference
  `alpha_bare^2*(1 - u_0)/u_0^2`, with equality only at the special boundary
  `u_0 = 1`.
- `scripts/audit_companion_alpha_s_tadpole_power_identity.py` now checks the
  source note for that formula and rejects the stale `alpha_bare = u_0`
  wording.
- `logs/runner-cache/audit_companion_alpha_s_tadpole_power_identity.txt` is
  refreshed through the repo cache utility and reports `TOTAL: PASS=18, FAIL=0`.

Reviewer focus:

- Confirm that this is only a formula-inventory/source-runner drift repair.
- Confirm that no `u_0` value, plaquette evaluation, running bridge, or
  observed `alpha_s` is imported.
- Confirm that no generated audit data or ledger verdict file is included.

Remaining status:

Independent audit owns any effective status change.
