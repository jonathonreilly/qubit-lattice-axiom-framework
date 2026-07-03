# Cubic-Quartic Ward Synthesis Diagnostic for the Conserved Coupling

**Date:** 2026-06-08
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/frontier_universal_gr_einstein_hilbert_closure_synthesis.py`](../scripts/frontier_universal_gr_einstein_hilbert_closure_synthesis.py)
**Runner cache:** [`logs/runner-cache/frontier_universal_gr_einstein_hilbert_closure_synthesis.txt`](../logs/runner-cache/frontier_universal_gr_einstein_hilbert_closure_synthesis.txt)

## Statement

This is a runner-supported synthesis diagnostic for the existing universal-GR
Ward lane. It consolidates the cubic and quartic finite-lattice diagnostics in
one script and checks that the same supplied conserved coupling
`D(P_eff) + sqrt(g)` beats the naive non-conserved control at both orders.

It does **not** identify the W-native induced graviton with the full
Einstein-Hilbert action. It does **not** prove all-order nonlinear
diffeomorphism invariance, an exact continuum coefficient, or the physical
`G_Newton` magnitude.

## Runner-Verified Content

The runner recomputes, in a single memory-safe finite-lattice script:

- **T0 - elliptic pin.** The native elliptic `iD` determinant
  `m^2 + |sin q|^2` is positive over the tested Brillouin-zone grid, while the
  bare Hermitian `sigma . sin` comparator is sign-indefinite.
- **T1 - cubic diagnostic.** For the runner-defined cubic Ward cross term, the
  conserved coupling's normalized residual decreases from `L=6` to `L=8`.
- **T2 - quartic diagnostic.** For the runner-defined quartic Ward cross term,
  the conserved coupling's normalized residual decreases from `L=6` to `L=8`.
- **T3 - conserved-vs-naive contrast.** At both cubic and quartic order, the
  conserved coupling has a smaller normalized residual at `L=8` and improves
  faster over `L=6 -> L=8` than the naive non-conserved control.

The diagnostic uses the same n-point Ward construction as the landed cubic and
quartic notes: the `(n-1)`-fold cross term of `dW/deps` under a
lattice-consistent diffeomorphism variation, with non-collinear TT gravitons
and a closing gauge momentum.

## Relation to Landed Rows

- Cubic finite-lattice scaling support:
  [`UNIVERSAL_GR_CUBIC_DIFFEO_WARD_FINITE_LATTICE_SCALING_SUPPORT_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_CUBIC_DIFFEO_WARD_FINITE_LATTICE_SCALING_SUPPORT_BOUNDED_THEOREM_NOTE_2026-06-08.md).
- Quartic finite-lattice continuum-trend diagnostic:
  [`UNIVERSAL_GR_QUARTIC_DIFFEO_WARD_CONTINUUM_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_QUARTIC_DIFFEO_WARD_CONTINUUM_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-08.md).
- Conserved-coupling/operator context:
  [`UNIVERSAL_GR_METRIC_REPARAMETRIZED_VERTEX_OPERATOR_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_METRIC_REPARAMETRIZED_VERTEX_OPERATOR_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  and
  [`UNIVERSAL_GR_CUBIC_DIFFEO_WARD_OPERATOR_TELESCOPE_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_CUBIC_DIFFEO_WARD_OPERATOR_TELESCOPE_BOUNDED_THEOREM_NOTE_2026-06-08.md).

This synthesis does not strengthen those parent rows beyond their audited
boundary. It only confirms that one runner can reproduce the shared
conserved-vs-naive pattern at cubic and quartic order on `L=6,8`.

## Boundaries

- The tested lattices are `L=6,8` in three spatial dimensions, with the
  runner's fixed mass, amplitude, finite-difference step, and non-collinear
  TT-graviton configurations.
- The result is a finite-lattice diagnostic, not a proof of the exact
  `k -> 0` limit or an `O(a^2)` coefficient.
- The quartic trend remains softer than the cubic trend, matching the landed
  quartic note's caution.
- The runner does not include the landed quintic diagnostic.
- The `sqrt(g)` measure and `D(P_eff)` coupling are supplied structures for
  this diagnostic; this note does not derive them uniquely from the framework
  primitives.

## What Is Not Claimed

- no full Einstein-Hilbert action identification;
- no all-order nonlinear diffeomorphism-invariance theorem;
- no exact finite-lattice diffeomorphism invariance;
- no continuum-renormalized finite part;
- no `G_Newton` magnitude, registered scale, or observed gravitational
  coupling;
- no new primitive, axiom, or Tier-A admission.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/frontier_universal_gr_einstein_hilbert_closure_synthesis.py
```
