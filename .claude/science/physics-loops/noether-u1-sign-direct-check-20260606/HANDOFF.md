# Handoff

## What Changed

- Added a 2026-06-06 repair note to
  `docs/AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md`.
- Added runner exhibit `E5b` to
  `scripts/axiom_first_lattice_noether_check.py`.
- Refreshed `logs/runner-cache/axiom_first_lattice_noether_check.txt`.

## Science Content

`E5b` samples arbitrary complex finite fields `chi`, `chibar` and a real
local envelope `alpha_x`. It computes the direct local U(1) variation

```text
delta S = (-i alpha chibar) M chi + chibar M (i alpha chi)
```

and compares it to the bilateral plus-sign expression in equation (7c).
The plus-sign residual is roundoff scale; the old minus-sign expression has
an order-one residual on the same fields.

## Verification

```text
python3 -m py_compile scripts/axiom_first_lattice_noether_check.py
python3 scripts/axiom_first_lattice_noether_check.py
python3 scripts/precompute_audit_runners.py --runners scripts/axiom_first_lattice_noether_check.py --force --allow-non-main --push-mode none
git diff -- docs/audit --exit-code
```

## Remaining Boundary

This closes the U(1) sign-directness blocker only. The note remains bounded
on the admitted staggered/Grassmann carrier and does not promote any audit
verdict.

