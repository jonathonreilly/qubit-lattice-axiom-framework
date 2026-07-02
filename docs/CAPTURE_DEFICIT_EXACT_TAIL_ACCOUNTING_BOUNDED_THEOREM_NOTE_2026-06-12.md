# Capture Deficit Exact Tail Accounting: Bounded L=3 Realized-State Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit audit-owned registry,
ledger, queue, or publication-status surfaces.
**Primary runner:** [`scripts/frontier_capture_tail_exact_law_2026_06_12.py`](../scripts/frontier_capture_tail_exact_law_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/frontier_capture_tail_exact_law_2026_06_12.txt`](../logs/runner-cache/frontier_capture_tail_exact_law_2026_06_12.txt)

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane owns status.

## Scope

This note is an exact finite-dimensional statement for the landed `L=3` gauge-link
system and the four realized fillings used by the determinant-phase machinery:

- `K=3`, seed `391`
- `K=4`, seed `99`
- `K=5`, seed `99`
- `K=6`, seed `466`

It does not claim an asymptotic law, a generic-seed theorem, or a larger-Fock-space
statement.

## Anchors

The runner mirrors the landed trajectory: color-diagonal nearest-neighbor hopping
on the `L=3` ring, `tau=0.35`, centered determinant-polar phase increments over
`T=256`, and the landed Hankel capture definition at window `64`.

| state | capture@order4, window 64 | landed coupled gaps above `1e-8` | landed eigenpair gaps with no floor |
| --- | ---: | ---: | ---: |
| K=3 | 0.898130088565 | 3 | 3 |
| K=4 | 0.777619557343 | 3 | 3 |
| K=5 | 0.899155545493 | 3 | 3 |
| K=6 | 0.994936516891 | 3 | 3 |

Removing only the landed eigenpair coupling floor does not create additional
coupled eigenpair gaps in this finite `L=3` model: the rounded eigenpair inventory is
still `-3, 0, +3`. The full object tested here is therefore the sampled
determinant-phase trajectory spectrum itself, with all `256` Fourier bins retained.
After centering, the zero-frequency coefficient vanishes numerically, leaving `255`
active bins at the fixed `1e-13` zero-detection tolerance for every realized state.

## Reconstruction Identity

For each state, the full sampled tone sum is

`x_t = sum_n c_n exp(2 pi i n t / 256)`,

where `c_n` is the finite Fourier coefficient of the centered phase-increment
trajectory. No amplitude floor is applied in the reconstruction. The runner gates
the maximum reconstruction error over the full `T=256` trajectory below `1e-12`.

## Capture Definition and Tail Law

Let `H_64(x)` be the landed Hankel matrix built from the centered increment
trajectory with window `64`, and let `sigma_j` be its singular values in descending
order. The landed order-4 capture is the Frobenius singular-energy fraction

`C_4 = (sum_{j=1}^4 sigma_j^2) / (sum_j sigma_j^2)`.

Therefore the capture deficit equals the order-4 Hankel-Frobenius complement —
an algebraic identity of the shared singular-value decomposition (capture is the
top-4 Frobenius fraction; the deficit is its complement), verified numerically at
`1e-12` on every state:

`1 - C_4 = (sum_{j>4} sigma_j^2) / (sum_j sigma_j^2)
         = ||H_64 - H_64^(4)||_F^2 / ||H_64||_F^2`,

where `H_64^(4)` is the best rank-4 truncated-SVD object in the same norm. This is
the exact norm relevant to the landed capture definition; it is not the raw
Fourier top-four energy fraction.

| state | capture deficit | Hankel-Frobenius tail fraction |
| --- | ---: | ---: |
| K=3 | 0.101869911435 | 0.101869911435 |
| K=4 | 0.222380442657 | 0.222380442657 |
| K=5 | 0.100844454507 | 0.100844454507 |
| K=6 | 0.005063483109 | 0.005063483109 |

## Depth Ordering as Tail Arithmetic

The landed capture order is

`K=6 -> K=5 -> K=3 -> K=4`.

The exact Hankel tail masses have the reverse arithmetic interpretation: smaller
tail means larger order-4 capture. Their ascending order is the same state order,

`K=6 -> K=5 -> K=3 -> K=4`.

Thus, on this exact finite realized-state surface, the capture deficit is exact tail
accounting in the landed Hankel norm, and the depth ordering is tail arithmetic.
Any broader causal, asymptotic, or generic-state interpretation remains outside
this runner.

## Dependencies

- [`HARMONIC_DEPTH_WEIGHT_DISTRIBUTION_MECHANISM_BOUNDED_THEOREM_NOTE_2026-06-12.md`](HARMONIC_DEPTH_WEIGHT_DISTRIBUTION_MECHANISM_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the landed realized-state family, capture ordering, and
  weight-distribution context.
- [`HARMONIC_DEPTH_HANKEL_RANK_MECHANISM_BOUNDED_THEOREM_NOTE_2026-06-12.md`](HARMONIC_DEPTH_HANKEL_RANK_MECHANISM_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the Hankel capture/rank machinery and equal coupled-gap inventory
  context.
- [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
  supplies pointwise evaluation on the supplied law-admissible realized states
  only; it supplies no state-selection, typicality, weighting, or averaging
  rule.

The audit lane grades.
