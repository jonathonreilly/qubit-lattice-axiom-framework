# Source-Resolved Exact Green Self-Consistent Pocket

**Date:** 2026-04-05  
**Type:** bounded_theorem

**Status:** bounded self-consistent refinement-positive on the compact exact
lattice with explicit assertion wrapper

## Source boundary (2026-06-12)

**Boundary:** numerical-match / bounded calibrated pocket only. Effective
status is audit-derived; this source records only the claim boundary.

The frozen table depends on the selected compact lattice, selected source
cluster, selected Green-like kernel, calibrated gain input, and a single
self-consistency update. This note may be cited only for the bounded
runner-backed pocket on that declared surface. It may not be cited as a
derivation of the gain, field normalization, source geometry, fully converged
self-consistent dynamics, continuum transfer, or physical amplitude.

Promotion beyond numerical-match support requires deriving the calibration
gain and field normalization from retained dynamics, and replacing the single
update pocket with a theorem-grade self-consistent dynamics result.

## Artifact chain

- [`scripts/source_resolved_exact_green_self_consistent.py`](../scripts/source_resolved_exact_green_self_consistent.py)
- [`logs/runner-cache/source_resolved_exact_green_self_consistent.txt`](../logs/runner-cache/source_resolved_exact_green_self_consistent.txt)
- [`outputs/source_resolved_exact_green_self_consistent_assertions_2026-07-11.txt`](../outputs/source_resolved_exact_green_self_consistent_assertions_2026-07-11.txt)

## Question

Does the exact-lattice Green pocket survive a minimal self-consistency update,
where the source-cluster weights are reweighted from the propagated wave once,
while preserving the weak-field gravity lane?

This note is intentionally narrow:

- one compact exact lattice family at `h = 0.25`
- one source-resolved Green-like kernel
- one self-consistency update from source-cluster amplitudes
- one comparison against the instantaneous `1/r` field
- one reduction check: zero source must recover free propagation exactly

## Frozen result

The frozen pocket uses:

- exact lattice with `h = 0.25`, `W = 3`, `L = 6`
- fixed cross5 source cluster clipped at the boundary, leaving 4 in-bounds source nodes
- source strengths `s = 0.001, 0.002, 0.004, 0.008`
- kernel `exp(-mu rho) / rho`, where `rho = distance + eps`, with
  `mu = 0.08`, `eps = 0.5`
- calibration gain input `1.757890330808e+00`
- one self-consistency update from the propagated source-cluster amplitudes

The calibration gain is part of the frozen setup.  It is chosen to set the
base-field cap at the strongest source row and is not evidence of an
independently derived physical amplitude.

## Closed finite-run assertion contract

For the four in-bounds source nodes at positions \(x_a\), normalized source
weights \(w_a\), and declared kernel parameters, the runner evaluates

\[
f_s(x)=g_{\rm cal}s\sum_{a=1}^{4}w_a
\frac{e^{-\mu \rho_a(x)}}{\rho_a(x)},\qquad
\rho_a(x)=|x-x_a|+\epsilon .
\]

It propagates once with uniform \(w_a=1/4\), replaces the weights by the
normalized propagated source-node powers, and propagates once more.  Thus the
reported result is exactly one specified reweighting update.  At \(s=0\),
\(f_0=0\) term by term independently of the weights, so the dynamic and free
propagations receive identical zero fields.  The runner checks that the field
is elementwise zero and that the full propagated complex state is elementwise
identical to the free state, then retains the centroid check at `1e-12` as a
readout-level guard.

The executable contract separately asserts:

1. the frozen scalar/geometry manifest owned by this runner (`h`, `W`, `L`,
   helper propagation constants, exact clipped source positions,
   source-strength ladder, both softenings, `mu`, the calibrated gain/target
   pair, and assertion tolerances);
2. zero-source reduction at the field, propagated-state, and centroid levels;
3. the cap arithmetic for the declared frozen role of `g_cal`, without
   treating either comparator amplitude as a physical prediction;
4. positive (`TOWARD`) self-consistent deflection in all four rows;
5. both fitted source-strength exponents within `5e-3` of one; and
6. reproduction of the frozen table within the declared absolute and relative
   tolerances.

Every assertion prints an explicit `[PASS]` or `[FAIL]`; any failure makes the
runner exit nonzero.  This closes only the bounded finite-run statement.

The imported propagation implementation is also a frozen code-level
condition: it starts from the unit point source at `(0,0,0)` and uses its
declared `w/L^2` transition normalization with phase action `K L (1-f)`.
These implementation choices are not derived physical normalizations.

Reduction check:

- zero-source dynamic shift: `+0.000000e+00`

Frozen readout:

| `s` | instantaneous deflection | self-consistent deflection | ratio | max `|f|` |
| --- | ---: | ---: | ---: | ---: |
| `0.0010` | `+1.410541e-03` | `+1.873799e-03` | `1.328` | `2.500245e-03` |
| `0.0020` | `+2.821591e-03` | `+3.749686e-03` | `1.329` | `5.000223e-03` |
| `0.0040` | `+5.645274e-03` | `+7.507807e-03` | `1.330` | `9.999374e-03` |
| `0.0080` | `+1.129975e-02` | `+1.505023e-02` | `1.332` | `1.999447e-02` |

Fitted exponents:

- instantaneous `F~M`: `1.00`
- self-consistent Green `F~M`: `1.00`

Note: `max |f|` scales linearly with source strength `s` (target cap of
`2.0e-02` reached at `s = 0.008`); previous frozen readout misreported
this column as fixed and rounded the deflections.

Assertion replay artifacts are linked in the artifact chain above.

```text
PASSED: 7/7
SOURCE_RESOLVED_EXACT_GREEN_SELF_CONSISTENT_ASSERTIONS=TRUE
CALIBRATED_GAIN_IS_INPUT=TRUE
CALIBRATED_GAIN_DECLARED_ROLE=frozen_input_not_independent_amplitude_prediction
COMPARATOR_AMPLITUDE_IS_INDEPENDENT_PREDICTION=FALSE
SOURCE_RESOLVED_GREEN_FULL_SELF_CONSISTENT_FIELD_THEORY=FALSE
RESIDUAL_SCOPE=fully_converged_self_consistent_field_theory_and_uncalibrated_amplitude
```

## Safe read

The strongest bounded statement is:

- exact zero-source reduction survives
- the self-consistent Green field keeps the weak-field `TOWARD` sign on the
  compact `h = 0.25` family
- the mass-scaling class stays essentially linear
- the dynamic field remains nontrivial relative to the chosen instantaneous
  comparator, with mean `|green/inst| = 1.330`
- the runner now asserts zero-source exactness, the calibrated gain boundary,
  `TOWARD` sign, exponent tolerances, and frozen table reproduction

## Honest limitation

This is a refinement-positive pocket, not yet a full self-consistent field
theory.

- the exact lattice is intentionally compact
- the architecture still uses a single self-consistency update, not a fully
  converged dynamical field evolution
- the source pattern is boundary-clipped rather than fully symmetric, so this
  is a bounded refinement update rather than a symmetry-clean family proof
- the `|green/inst|` amplitude ratio is comparator- and calibration-dependent,
  so it should not be promoted as a standalone physical observable
- the calibrated gain is a declared frozen setup input rather than derived from
  retained dynamics
- still, it is the smallest exact-lattice refinement of the Green pocket that
  preserves the hard gates cleanly

## Bounded numerical read

Treat this as a bounded calibrated pocket only:

- exact zero-source reduction survives
- weak-field sign survives
- `F~M` stays at `1.00`
- the pocket survives a self-consistency update on the exact refinement family
- this is the best current exact-lattice propagating-field refinement lead
