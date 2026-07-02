# H_kd Vanishing Is Equivalent to Zero Misaligned Survivor Entries for the d=3 Step-2 Chart Family on L = {8,10,12,14,16,18} (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note sets source
claim metadata only; it does not set, predict, or edit any audit outcome.
**Primary runner:** [`scripts/frontier_hkd_correspondence_equivalence_2026_06_12.py`](../scripts/frontier_hkd_correspondence_equivalence_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/frontier_hkd_correspondence_equivalence_2026_06_12.txt`](../logs/runner-cache/frontier_hkd_correspondence_equivalence_2026_06_12.txt)
**No-promotion statement:** This source note creates no promotion, no registry
edit, no audit verdict, and no downstream status change; status remains owned
by the independent audit lane.

## Claim

For the synthetic d=3 step-2 chart family with

```text
K_periods = (L/2, L, L/2),
```

on the fixed grid `L = {8, 10, 12, 14, 16, 18}`, the runner verifies the
structural equivalence

```text
H_kd_after < 1e-14
  <=> zero nonzero misaligned survivor entries after even-d2 truncation
  <=> every K-chart period is even.
```

Here `H_kd_after` is the next-checkerboard kept-decimated block after applying
the even-`d2` truncation.  The entry decomposition scans every nonzero
post-truncation kept-decimated survivor, computes its minimal-vector `d2`
parity and its chart-pair parity, and counts survivors where those parities are
misaligned.

## Mechanism

The self-contained anchor gates establish the numerical dichotomy:

- `L = 8, 12, 16`: protected at `1e-14`.
- `L = 10, 14, 18`: unprotected, with `H_kd_after` about `0.747`.

This runner upgrades the anchored tie by showing the entry-level reason on the
same grid.  When all K-chart periods are even, the per-axis correspondence
forces the nonzero kept-decimated couplings to have chart parity matching their
minimal-vector `d2` parity, so the even-`d2` truncation leaves no nonzero
misaligned kept-decimated survivor.  When a K-period is odd, nonzero
post-truncation misaligned survivor entries remain and `H_kd_after` is nonzero.

At `L = 10`, the runner prints a concrete surviving misaligned entry with its
coset pair, minimal vector, `d2` parity, chart-pair parity, and nonzero
magnitude.  The witness magnitude is gated above `1e-6`.

## Gates

The runner opens with frozen anchor gates before the new equivalence gates:

- `L = 8`: `H_kd_after = 0` against the frozen protected anchor.
- `L = 10`: `H_kd_after = 0.748324978630193` against the frozen unprotected anchor.
- `L = 12`: `H_kd_after = 0` against the frozen protected anchor.
- `L = 14`: `H_kd_after = 0.74732149222164` against the frozen unprotected anchor.
- Anti-fabrication: `H_kd_before` is nonzero at every grid value before truncation.
- Self-contained step-1 dense Schur anchor at `L = 8` still matches the
  closed form.

The structural gates then check, on the full grid, that zero misaligned survivor
entries is equivalent both to `H_kd_after < 1e-14` and to all K-chart periods
being even.  The `L = 16` out-of-sample protected case is gated explicitly:
zero misaligned survivors and `H_kd_after < 1e-14`.

## Scope

This is a grid-verified structural equivalence plus per-entry mechanism for this
chart family only.  It does not claim full-`L` closure of the entry-sum identity,
other chart families, a continuum theorem, or an audit result.  Full-`L` closure
of the entry-sum identity is the named follow-on.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  (the current axiom surface; scope reference only).
