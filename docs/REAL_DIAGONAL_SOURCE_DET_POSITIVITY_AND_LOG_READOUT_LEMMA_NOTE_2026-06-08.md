# Real-Diagonal Source Determinant Positivity (Self-Contained Lemma)

**Date:** 2026-06-08; scope repaired 2026-07-16
**Claim type:** bounded_theorem
**Author-proposed claim boundary:** **L1/L2 determinant positivity only.**
**Status authority:** independent audit lane only. No audit verdict is asserted.
**Stable claim ID/path:** the legacy filename and claim ID retain
`and_log_readout` so existing citations do not break; those words do not make
the open L3 bridge part of this theorem.
**Primary runner:**
[`scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py`](../scripts/audit_companion_real_diagonal_source_det_positivity_lemma_2026_06_08.py)
(expected `SCORECARD PASS=7 FAIL=0`).

## Why this lemma exists

The observable-principle parent
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` needs a finite-dimensional fact for
its phase-free source surface: the source-dressed determinant is a strictly
positive real number. An earlier citation routed that fact through a fuller
application note that depended back on the parent. This note extracts only the
self-contained linear algebra needed to break that cycle.

The extracted theorem does **not** supply a determinant-only scalar readout or
a source-block-to-disjoint-record composition law. Those are separate bridge
premises, discussed below only to make the claim boundary explicit.

## Theorem statement: determinant positivity only

Let `D` be a finite real antisymmetric matrix (`D^T = -D`).

- **(L1) Positive-diagonal cone.** If `S` is real positive diagonal, then
  `det(S + D) > 0`. Indeed,

  ```text
  S + D = S^(1/2) (I + B) S^(1/2),
  B = S^(-1/2) D S^(-1/2),
  ```

  and `B` is real antisymmetric. Its nonzero eigenvalues occur in pairs
  `+i lambda_k, -i lambda_k`, so

  ```text
  det(S + D) = det(S) det(I + B)
             = det(S) product_k (1 + lambda_k^2) > 0.
  ```

  Thus the determinant is a strictly positive real number with no phase.

- **(L2) Sign-constant local derivative patch.** For invertible real antisymmetric D
  and real diagonal J, suppose a submultiplicative operator
  norm satisfies `||D^(-1) J|| < 1`. For every `t in [0,1]`,
  `||t D^(-1) J|| < 1`, so `I + t D^(-1)J` and hence `D + tJ` are invertible
  by the Neumann series. The real continuous function `det(D+tJ)` cannot
  change sign on this path. An invertible real antisymmetric matrix has paired
  eigenvalues `+i lambda_k, -i lambda_k`, hence
  `det D = product_k lambda_k^2 > 0`. Therefore `det(D+J) > 0` throughout the
  stated local patch.

These two conclusions are the complete bounded-theorem target of this note.

## Open L3 boundary: conditional readout classification, not a theorem claim

Determinant multiplicativity by itself gives
`det(A direct_sum B) = det(A) det(B)`. It does not establish either of the two
bridges needed to turn finite additivity of already-supplied records into a
functional equation for a source readout:

1. a **determinant-only readout bridge**, saying the scalar readout factors as
   `W(A) = f(det A)`; and
2. a **source-block-to-disjoint-record bridge**, saying independent direct-sum
   source blocks register as disjoint records to which finite additivity
   applies.

Continuity does not supply either bridge. On positive diagonal blocks,

```text
W_epsilon(S) = log det(S) + epsilon Tr(S)
```

is continuous and direct-sum additive. Yet `diag(4,1)` and `diag(2,2)` have the
same determinant and different traces, so this family is not determinant-only
when `epsilon != 0`. This countermodel is checked by the runner.

Only **if a separate future premise or theorem supplies both bridges** does the
continuous Cauchy classification apply: a continuous `f: R_{>0} -> R` with
`f(xy) = f(x) + f(y)` has the form `f(x) = c log x`. Choosing `c = 1` is a
further normalization convention. This conditional mathematical observation
is not L3 theorem content of the present claim and is not licensed by L1/L2.

## Downstream license and exclusions

Consumers may cite this claim for exactly the following facts:

- positive-diagonal real sources added to finite real antisymmetric blocks have
  strictly positive real determinant; and
- the stated Neumann neighborhood of an invertible real antisymmetric block
  preserves that positive determinant sign.

Consumers must **not** cite this claim as supplying a determinant-only readout,
a source-block-to-disjoint-record correspondence, a Record-to-source
composition law, `c log det` as a physical readout, or the `c = 1`
normalization. The note also does not derive the observable principle,
source-response physics, species/flavor content, or any numerical value.

## Load-bearing inputs

L1 and L2 use only the stated finite-matrix hypotheses and elementary linear
algebra: positive diagonal square roots, the spectrum of a real antisymmetric
matrix, the Neumann invertibility criterion, and continuity of the real
determinant. No framework axiom, empirical comparator, fitted value, or
literature numerical input is consumed.
