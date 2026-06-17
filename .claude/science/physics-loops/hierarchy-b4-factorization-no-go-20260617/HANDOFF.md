# Handoff

## What This PR Does

Adds an exact no-go boundary for the determinant-only B4 route in the
hierarchy lane. It proves that the checked determinant factor `u_0^16` cannot,
by finite determinant products, powers, or quotients, become
`alpha_LM^16 = alpha_bare^16 u_0^(-16)`.

## What It Does Not Do

- Does not close B4.
- Does not prove the hierarchy formula.
- Does not identify the electroweak VEV.
- Does not change audit status.
- Does not add an axiom.

## Reviewer Extraction Path

If accepted, wire this as a route-pruning boundary for
`hierarchy_formula_honest_status_note_2026-05-10` and the B4 delta-zero
gate. The positive follow-up remains the attachment-observable theorem
supplying `alpha_s` per taste decoupling, or an equivalent non-determinant
transport rule.

## Verification

```bash
python3 scripts/frontier_hierarchy_b4_determinant_only_factor_signature_no_go_2026_06_17.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_hierarchy_b4_determinant_only_factor_signature_no_go_2026_06_17.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_hierarchy_b4_determinant_only_factor_signature_no_go_2026_06_17.py
python3 -m py_compile scripts/frontier_hierarchy_b4_determinant_only_factor_signature_no_go_2026_06_17.py
git diff --cached --check
```
