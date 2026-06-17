# Commensuration General Lemma Period-Parity Bounded Theorem Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit audit-owned registry,
ledger, queue, or publication-status surfaces.
**Primary runner:** [`scripts/frontier_commensuration_general_lemma_2026_06_12.py`](../scripts/frontier_commensuration_general_lemma_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/frontier_commensuration_general_lemma_2026_06_12.txt`](../logs/runner-cache/frontier_commensuration_general_lemma_2026_06_12.txt)

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane owns status.

## Claim

For the d=3 step-2 chart family with K-periods `(L/2, L, L/2)` and even `L >= 8`,
the minimal-vector `d^2 mod 2` parity agrees with chart parity exactly when
`L = 0 mod 4`.

Equivalently, the next checkerboard is protected exactly when all K-periods are
even. Since the K-periods are `(L/2, L, L/2)`, this is exactly the `L = 0 mod 4`
subfamily.

## Residue-Class Derivation

For one period `p`, the minimal representative of a residue difference `r` is
`r` on the low half and `r - p` on the high half. Since `n^2 mod 2 = n mod 2`,
the minimal-vector `d^2` parity is just the parity sum of those minimal
representatives.

If `p` is even, subtracting `p` does not change parity. If `p` is odd,
subtracting `p` flips parity on the high half of that coordinate.

For `L = 4q`, the K-periods are `(2q, 4q, 2q)`, all even, so every residue class
preserves parity and `d^2 mod 2` equals chart parity.

For `L = 4q + 2`, the K-periods are `(2q + 1, 4q + 2, 2q + 1)`. The first and
third periods are odd. The symbolic table reduces to

```text
d2_mod2 = chart_mod2 + high_x + high_z  (mod 2)
```

Thus the odd-axis parity-flip branch (which includes low negative wraps, not only high-half displacements) forces a mismatch.
For example, at `L=10` the coset from `(0,0,0)` to `(0,0,3)` has minimal vector
`(0,0,-2)`, giving `d^2 mod 2 = 0` while the chart parity changes by `1`.

## Verification

The runner gates:

- landed Hamiltonian anchors at `L=8` and `L=10`, reproducing the protected and
  failing `H_kd_after` dichotomy against frozen parent constants;
- the SymPy residue-class case split for `L = 0 mod 4` and `L = 2 mod 4`;
- the extended combinatorial grid `L in {8,10,...,28,30}`, with every `L`
  gated against the fixed criterion `L = 0 mod 4`;
- an anti-fabrication failing coset at `L=10`, including its nonzero minimal
  vector and parity mismatch.

## Scope

This note proves the combinatorial correspondence on the stated extended grid
and records the symbolic residue-class case split. The direct Hamiltonian tie is
verified only at the landed anchors `L=8` and `L=10`. It does not assert a new
`H_kd_after` equivalence for `L=20,22,24,26,28,30`, a continuum statement, a
generic chart-family theorem beyond this stated chart-period family, or an
audit result.

No new axiom, primitive, measure, weighting, normalization, probability rule,
or value of `r` is introduced.

## Dependencies

- [`D3_TRUNCATION_COMMENSURATION_CRITERION_BOUNDED_THEOREM_NOTE_2026-06-12.md`](D3_TRUNCATION_COMMENSURATION_CRITERION_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the d=3 step-2 chart family and the finite Hamiltonian
  commensuration context that this note does not extend beyond the stated
  anchors.

The audit lane grades.
