# Handoff

## Summary

This branch repairs `FLAVOR_CARRIER_NOT_DERIVED_TWO_INPUTS_2026-05-31` by
preserving the finite no-go while removing the stronger input-count standing.

## Files

- `docs/FLAVOR_CARRIER_NOT_DERIVED_TWO_INPUTS_2026-05-31.md`
- `scripts/flavor_carrier_not_derived_two_inputs_2026_05_31.py`
- `logs/runner-cache/flavor_carrier_not_derived_two_inputs_2026_05_31.txt`

## Science

- Bare `C_3` characters are `1`, `-1`, and `0`, not `2/9`.
- `L_3(1,2)=2/9` comes from the doublet determinant denominator.
- `C_3` equivariance leaves `r=|b|^2/a^2` free.
- `Q(r)` checks both `r=1/2` and `r=1`; it does not select the physical basepoint.

## What Review Should Check

- The source no longer claims that exactly two independent irreducible inputs are proved.
- The source does not derive the physical carrier or basepoint.
- The runner guard enforces the bounded-support status and source boundary.
- No `docs/audit/**` files are changed.
