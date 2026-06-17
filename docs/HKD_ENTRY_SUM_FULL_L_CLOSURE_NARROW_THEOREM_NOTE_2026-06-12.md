# HKD Entry-Support Full-L Period-Parity Criterion for the d=3 Step-2 Chart Family

Draft date: 2026-06-12

Claim type: bounded_theorem

Runner: [`scripts/frontier_hkd_entry_sum_full_l_closure_2026_06_12.py`](../scripts/frontier_hkd_entry_sum_full_l_closure_2026_06_12.py)

## Claim

For the d=3 step-2 chart family with

```text
K_periods = (L/2, L, L/2)
```

and every even `L >= 8` in this scope, the combinatorial kept-decimated
support criterion is

```text
no surviving misaligned kept-decimated support entries  <=>  L = 0 mod 4.
```

The full-`L` step is combinatorial: the surviving kept-decimated cell after
even-`d2` truncation is determined by chart parity and minimal-vector parity,
not by a dense Hamiltonian computation.  Dense Hamiltonians are used only as
anchors for `L = {8,10,12,14,16,18}`.

On those dense anchors, the directly computed real Schur `H_kd_after` vanishes
exactly when the support criterion has no surviving misaligned entry.  This note
does not claim a dense-Hamiltonian or Schur-magnitude theorem beyond the anchor
grid.

## Mechanism

On the dense anchor grid, the runner computes the finite Schur block and
measures

```text
H_kd_after = max over surviving kept-decimated entry magnitudes,
```

after the even-`d2` truncation.  This is the bounded dense-anchor bridge; the
full-`L` part below is the support/parity criterion.

In this block the survivor parity cell is

```text
left_chart_parity = 0
right_chart_parity = 1
d2_parity = 0.
```

Thus `chart_pair_parity = 1` while `d2_parity = 0`, so every nonzero survivor
in that cell is misaligned.

The unconditional period-parity lemma
[`COMMENSURATION_UNCONDITIONAL_PERIOD_PARITY_LEMMA_NARROW_THEOREM_NOTE_2026-06-12.md`](COMMENSURATION_UNCONDITIONAL_PERIOD_PARITY_LEMMA_NARROW_THEOREM_NOTE_2026-06-12.md)
supplies the full-`L` support criterion.  For one axis with period `q`, the
centered representative is

```text
delta = a - q*k
```

with the centered tie convention.  If `q` is even, `delta` preserves parity
for every residue.  If `q` is odd and `q >= 3`, the witness
`a = (q + 1)/2` has `k = 1` and flips parity.  Since
`d2 = sum_i delta_i^2 = sum_i delta_i (mod 2)`, a misaligned survivor exists
exactly when some chart period is odd.  For `(L/2,L,L/2)` with even `L`, this
is exactly `L != 0 mod 4`.

## Verification

The runner gates the anchored Hamiltonian values first:

```text
L=8  H_kd_after = 0
L=10 H_kd_after = 0.748324978630193
L=12 H_kd_after = 0
L=14 H_kd_after = 0.747321492221640
L=16 H_kd_after = 0
L=18 H_kd_after = 0.747285892436525
```

It also gates `H_kd_before` nonzero on every anchor, and checks the `L=8`
step-1 dense Schur anchor remains exact.

The combinatorial predictor then reproduces the anchored Hamiltonian
misaligned-survivor counts exactly:

```text
L=8  -> 0
L=10 -> 5700
L=12 -> 0
L=14 -> 43512
L=16 -> 0
L=18 -> 197640
```

Finally, the runner checks the support criterion for every even `L` from `8`
through `40`:

```text
misaligned support survivors exist  <=>  L != 0 mod 4  <=>  some K-period is odd.
```

The `L=22` witness is combinatorial only, with no dense Hamiltonian:

```text
left=(0,0,0), right=(0,1,6), delta=(0,1,-5)
```

Here `6 = (11+1)/2` is the odd-axis witness for period `11`; the additional
`1` on the even axis puts the right coset in the decimated chart-parity class
and makes `d2` even.  Hence `d2_parity=0` and `chart_pair_parity=1`.

## Scope

This is a bounded theorem for the chart family `(L/2,L,L/2)`.  It upgrades the
support/parity side to the full even-`L` criterion for this family by combining
self-contained dense anchors with the unconditional per-axis period-parity
lemma.  It does not claim other chart families, an all-`L` dense Hamiltonian or
Schur-magnitude theorem, a continuum limit, or an audit result.

The audit lane grades.
