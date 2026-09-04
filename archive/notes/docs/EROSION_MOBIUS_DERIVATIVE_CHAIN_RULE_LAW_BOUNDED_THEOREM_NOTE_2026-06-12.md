# Erosion Moebius Derivative Chain-Rule Law Bounded Theorem Note

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit audit-owned registry,
ledger, queue, or publication-status surfaces.
**Primary runner:** `scripts/frontier_erosion_mobius_derivative_law_2026_06_12.py`
**Runner cache:** `logs/runner-cache/frontier_erosion_mobius_derivative_law_2026_06_12.txt`

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane owns status.

## Claim

For the erosion recurrence supplied by
[`EROSION_EXACT_RECURRENCE_PATH_PRODUCT_THRESHOLD_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-06-12.md`](EROSION_EXACT_RECURRENCE_PATH_PRODUCT_THRESHOLD_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-06-12.md),

```text
p_j = (p_{j-1} + s_j eps) / (1 + s_j eps p_{j-1})
c_j = c_{j-1} (1 - eps^2) / (1 + s_j eps p_{j-1})^2,
```

the one-step erosion factor is exactly the derivative of the Moebius step map

```text
f_s(p) = (p + s eps) / (1 + s eps p).
```

Therefore, for a fixed sign word `s_1,...,s_n`, the chain-rule identity gives

```text
c_n / c_0 = (f_{s_n} o ... o f_{s_1})'(p_0).
```

The matrix form is the projective action of

```text
M_s = [[1, s eps], [s eps, 1]],
```

so a periodic word `w` of length `T` has product matrix `M_w`. On hyperbolic
periodic words, the per-period erosion rate is

```text
det(M_w) / lambda_max(M_w)^2 = (1 - eps^2)^T / lambda_max(M_w)^2,
```

where `lambda_max` is the larger absolute eigenvalue of `M_w`.

## What The Runner Gates

The runner first anchors against the landed closed-form machinery:

- uniform rate at `eps=0.2` equals the frozen value `0.6666666666666666`
  within `1e-10`;
- alternating two-step c-product equals `1` within `1e-14`;
- the uniform-word `lambda_max` is strictly larger than `1`, an
  anti-fabrication gate that must be nontrivial if the matrix machinery ran.

It then verifies:

- the pointwise SymPy identity between the c-factor and `f_s'(p)` for both
  signs;
- the numeric chain rule on fixed words and fixed eps values;
- the symbolic `n=3` chain rule for all eight fixed sign triples;
- the periodic-word matrix rate law on fixed words
  `++`, `+-`, `++-`, `+--`, `+++-`, `++--`, and `+-++-+` at
  `eps in {0.1, 0.2, 0.3, 0.4}`;
- the special cases: uniform `T=1` recovers `(1-eps)/(1+eps)`, while
  `M_- M_+ = (1-eps^2) I` exactly, explaining alternating protection.

## Scope

Scope is the landed recurrence model, `0 < eps < 1`, and hyperbolic periodic
words for the asymptotic rate law. The fixed set also contains scalar-identity
edge cases (`+-` and `++--` at the tested eps values), where the matrix product
has a single eigenvalue and the rate is exactly `1` rather than a contracting
hyperbolic multiplier.

This note does not claim a law for non-periodic sign words, the nonlinear
threshold-count envelope, finite-lattice scaling, continuum behavior, or a new
physical measurement derivation. It introduces no new axiom, primitive,
measure, weighting, normalization, probability rule, or value of `r`.

## Dependencies

- [`EROSION_EXACT_RECURRENCE_PATH_PRODUCT_THRESHOLD_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-06-12.md`](EROSION_EXACT_RECURRENCE_PATH_PRODUCT_THRESHOLD_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the exact recurrence and path-product model.
- [`EROSION_GEOMETRIC_RATE_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-12.md`](EROSION_GEOMETRIC_RATE_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  supplies the uniform-sign special case recovered here as a gate, not as a new
  status claim.

The audit lane grades.
