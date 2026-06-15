# [physics-loop] g2 RGE scale bridge bounded-support

## What this PR does

This is a source-side audit unlock, not an audit verdict update. It addresses
the `g_2_v_bounded_interval_narrow_theorem_note_2026-05-17` blocker:

> missing_bridge_theorem: add retained or Tier-A admitted bridge rows for X1 u_0(SU(2)), X6 ln(M_Pl/v), and X7 the one-loop RGE form, or explicitly register them as accepted bounded-tier admissions before re-auditing for clean bounded retention.

The branch repairs X6/X7 only:

- Adds a framework-local bridge deriving the integrated one-loop inverse-alpha
  equation by calculus from the one-loop coefficient convention.
- Computes `ln(M_Pl/v_cand) = 38.442224515...` from the scale-reference
  primitive and hierarchy candidate map, with `38.44` treated as a rounded
  runner surrogate.
- Rewires the existing `g_2` bounded interval note and runner to cite the
  bridge and preserve X1 as the remaining open literature import.

No audit ledger, queue, effective-status, publication, or front-door generated
outputs are committed.

## Files

- `docs/SU2_WEAK_ONE_LOOP_INVERSE_ALPHA_SCALE_LOG_BRIDGE_NARROW_THEOREM_NOTE_2026-06-15.md`
- `scripts/audit_companion_su2_weak_one_loop_inverse_alpha_scale_log_bridge_2026_06_15.py`
- `docs/G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM_NOTE_2026-05-17.md`
- `scripts/audit_companion_g2_v_bounded_interval_narrow_exact_2026_05_17.py`
- `.claude/science/physics-loops/g2-rge-scale-bridge-20260615/`

## Honest status

Actual current-surface status: `bounded-support` source proposal. Independent
audit remains required. Bare retained status is not claimed.

Remaining blocker: X1 `u_0(SU(2)) in [0.96, 0.98]`.

## Validation

```bash
python3 scripts/audit_companion_su2_weak_one_loop_inverse_alpha_scale_log_bridge_2026_06_15.py
# TOTAL: PASS=19 FAIL=0

python3 scripts/audit_companion_g2_v_bounded_interval_narrow_exact_2026_05_17.py
# PASS=24 FAIL=0

python3 -m py_compile scripts/audit_companion_su2_weak_one_loop_inverse_alpha_scale_log_bridge_2026_06_15.py scripts/audit_companion_g2_v_bounded_interval_narrow_exact_2026_05_17.py

git diff --check
```

Diagnostic pipeline policy: if run locally, restore generated audit outputs
before commit.

Diagnostic pipeline was run locally and generated outputs were restored before
commit:

```text
cycles: 0
ready queue entries: 50
audit_lint: OK, no errors
g_2 row: unaudited after source hash change
new bridge row: seeded unaudited
```
