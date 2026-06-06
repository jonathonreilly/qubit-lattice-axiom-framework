# Handoff

## Summary

This branch repairs the J-hunt round-2 packet by preserving the closed
algebraic no-go and removing unsupported downstream readout claims.

## Files

- `docs/FLAVOR_FIND_J_ROUND2_POWER_NOT_COUNT_2026-06-02.md`
- `scripts/flavor_find_J_round2_power_not_count_2026_06_02.py`
- `logs/runner-cache/flavor_find_J_round2_power_not_count_2026_06_02.txt`

## Science

The packet now says:

- Berezin/fermionic determinant power is not generation-doublet mode count.
- Berezin gives a determinant product, not a Frobenius block-total selector.
- `C3` covariance preserves both `I` and `J=C-C^2`.

Therefore the route from fermionic determinant power to a forced `J` pairing is
pruned.

## What Review Should Check

- The note does not promote `det_R/Q=1`, `det_C -> r=1/2 -> Q=2/3`, or a
  Dirac-vs-Majorana wall.
- The runner's R2-4 guard correctly enforces that source boundary.
- No `docs/audit/**` files are changed.

## Next Science

Likely follow-up targets are round-1 static `J_cs` measure-neutrality and the
`Q1` default packet if they still carry broad readout/default language.
