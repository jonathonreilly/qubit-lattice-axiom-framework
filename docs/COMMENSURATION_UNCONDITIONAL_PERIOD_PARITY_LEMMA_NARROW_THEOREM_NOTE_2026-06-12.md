# Commensuration Unconditional Period-Parity Lemma Narrow Theorem Note

Draft date: 2026-06-12

Claim type: positive_theorem

Runner: [`scripts/frontier_commensuration_unconditional_lemma_2026_06_12.py`](../scripts/frontier_commensuration_unconditional_lemma_2026_06_12.py)

## Claim

For any chart periods `(q1, q2, q3)` with each `q_i >= 2`, the minimal-vector
`d^2 mod 2` parity agrees with chart parity for all chart cosets iff every
period `q_i` is even.

(The degenerate `q_i = 1` axis carries a single trivial coset with `delta == 0`,
so its parity is vacuously preserved despite `1` being odd; the "odd period
flips parity" branch needs a non-trivial residue and hence `q_i >= 3`. The
criterion is stated for `q_i >= 2`. The chart family `(L/2, L, L/2)` with even
`L >= 4` always has periods `>= 2`, so this edge never arises in scope.)

For the step-2 commensuration chart family `(L/2, L, L/2)` with even `L`,
this criterion is exactly `L = 0 mod 4`.

## Three-Line Argument

1. For each axis, under the centered representative convention `delta_i = a_i - q_i k_i`; hence `delta_i = a_i + q_i k_i (mod 2)`, and if `q_i` is even the axis preserves parity for every residue.
2. If `q_i` is odd, parity flips exactly when `k_i` is odd; for every odd `q_i >= 3`, the residue `a_i = (q_i + 1)/2` has centered round `k_i = 1`, so that axis supplies a parity-flip witness.
3. Since `delta_i^2 = delta_i (mod 2)`, `d^2 = sum_i delta_i (mod 2)`; therefore chart parity `sum_i a_i` is preserved for all cosets iff every `q_i` is even, and for `(L/2, L, L/2)` with even `L` this is exactly `L = 0 mod 4`.

## Verification

The runner first recomputes selected full-coset mismatch counts and gates them
against frozen copies:

```text
L=8  -> 0
L=10 -> 5700
L=12 -> 0
L=16 -> 0
L=18 -> 197640
L=26 -> 1802892
```

The anti-fabrication gate exhibits the frozen `L=10` parity-flip witness:
`(0,0,0) -> (0,0,3)` has centered minimal vector `(0,0,-2)`, so
`d^2 mod 2 = 0` while the chart parity changes by `1`.

After those anchors, the runner verifies the elementary per-axis steps:

- SymPy checks the even-period residue table has no parity-flip row.
- SymPy checks the odd-period residue table flips exactly on odd `k`.
- SymPy checks the odd witness `a=(q+1)/2` has centered round margin `1`,
  centered representative `-m` for `q=2m+1`, and parity flip `1`.
- Exhaustive integer sweeps cover all even `q` from `2` through `100` and all
  odd `q` from `3` through `99`, using the centered `minimal_delta` tie
  convention.

Finally, the selected full 3-D checks are compared to the per-axis iff
prediction. The selected all-even-period cases have zero mismatches, and the
selected odd-period cases have nonempty failure sets.

## Scope

This note upgrades the period-parity correspondence for this chart family to
an unconditional elementary lemma. It does not upgrade any `H_kd` Hamiltonian
or Schur-complement statement beyond separate finite-computation results.

The audit lane grades.
