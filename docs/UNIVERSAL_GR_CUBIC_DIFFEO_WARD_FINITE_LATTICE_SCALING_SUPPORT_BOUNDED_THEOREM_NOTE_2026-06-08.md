# Cubic Diffeomorphism Ward Finite-Lattice Scaling Support for the Conserved GR Coupling

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Scope:** finite-lattice scaling support for the supplied conserved coupling
`D(P_eff)` plus the `sqrt(g)` / densitized-inverse-vielbein measure. This is
not a proof of the continuum limit, an Einstein-Hilbert normalization, or full
nonlinear diffeomorphism invariance.
**Primary runner:**
[`scripts/frontier_universal_gr_cubic_diffeo_ward_finite_lattice_scaling_support_2026_06_08.py`](../scripts/frontier_universal_gr_cubic_diffeo_ward_finite_lattice_scaling_support_2026_06_08.py)
**Runner cache:**
[`logs/runner-cache/frontier_universal_gr_cubic_diffeo_ward_finite_lattice_scaling_support_2026_06_08.txt`](../logs/runner-cache/frontier_universal_gr_cubic_diffeo_ward_finite_lattice_scaling_support_2026_06_08.txt)

## Summary

The runner tests the cubic diffeomorphism-Ward residual for a supplied lattice
conserved coupling, using a genuine two-momentum transverse-traceless cubic
configuration. The finite-lattice result is useful and should land:

- with the conserved `D(P_eff)` coupling plus `sqrt(g)` measure, the normalized
  residual decreases over `L=6,8,10`;
- with the naive non-conserved C1 coupling, the same diagnostic does not show
  that decrease over the tested range;
- the conserved/naive separation widens as the lattice momentum decreases.

That is finite-lattice evidence for the conserved-coupling continuum-closure
route. It is not itself a retained continuum theorem: three accessible lattice
sizes and a fitted positive power do not prove the `k -> 0` limit.

## Tested Operator And Diagnostic

The supplied lattice coupling is the momentum-reparametrized conserved operator
from
[`UNIVERSAL_GR_METRIC_REPARAMETRIZED_VERTEX_OPERATOR_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_METRIC_REPARAMETRIZED_VERTEX_OPERATOR_LIFT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-06-08.md),
with the measure ansatz

```text
D[h] = i sigma_a[ Lm_a + Ch_a o d_a - 1/2 Lm_a o d_a^2 - 1/6 Ch_a o d_a^3 ] + m sqrt(g),
d_a = sum_b (W_dens - I)_ab o Lm_b,
W_dens = det(e) e^{-1},  e = sqrt(I+h).
```

The cubic test is the `a2*a3` cross term of the gauge variation `dW/deps`,
`W=log|det D[h]|`, under a lattice-consistent diffeomorphism with two distinct
non-collinear transverse-traceless gravitons. This uses the operator-telescoping
backbone from
[`UNIVERSAL_GR_CUBIC_DIFFEO_WARD_OPERATOR_TELESCOPE_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_CUBIC_DIFFEO_WARD_OPERATOR_TELESCOPE_BOUNDED_THEOREM_NOTE_2026-06-08.md)
as context for why the cubic channel must be tested at loop level rather than
as a clean finite operator identity.

## Finite-Lattice Result

The runner reports `TOTAL: PASS=3 FAIL=0`.

- **T1 conserved coupling:** `resid/amplitude` decreases monotonically over the
  tested range:
  `0.0315@k=1.05 > 0.0234@k=0.79 > 0.0167@k=0.63`, with a fitted power
  `~k^+1.24`.
- **T2 naive C1 control:** the non-conserved control does not show the same
  decreasing trend over the tested range:
  `0.0494@k=1.05 -> 0.0540@k=0.79`, with fitted power `~k^-0.31`.
- **T3 separation:** the naive/conserved ratio widens from `1.57` to `2.31` as
  `k` decreases from `1.05` to `0.79`.

The decisive reviewed claim is the finite-lattice contrast: the conserved
coupling has the right decreasing trend in this cubic diagnostic, while the
naive coupling does not.

## Boundaries

- The tested lattices are `L=6,8,10` in three spatial dimensions, with the
  runner's fixed mass, amplitude, finite-difference step, and non-collinear
  TT-graviton configuration.
- The fitted positive power is support for the `O(a^2)` lattice-floor story,
  not a proof of the asymptotic coefficient or the exact continuum limit.
- The note does not prove the quartic vertex, all-order nonlinear
  diffeomorphism invariance, a continuum-renormalized finite part, the
  Einstein-Hilbert action, or `G_Newton`.
- The `sqrt(g)` measure and `D(P_eff)` coupling are supplied structures for
  this finite-lattice test; this note does not derive them as unique from the
  framework primitives.

## Relation To Existing GR Rows

This note narrows and extends the landed GR support chain without overwriting
its boundaries. The operator-telescoping note says the finite operator backbone
does not by itself prove the full cubic diffeomorphism Ward identity. The
metric-reparametrized operator note supplies the conserved-coupling route and
keeps the continuum-removal question open. This note adds a finite-lattice
scaling diagnostic in favor of that route; it does not close the continuum
theorem by prose.

## Forbidden-Imports Check

No observed gravitational coupling, fitted empirical value, Planck-scale input,
or continuum Einstein-Hilbert normalization is used. The numbers in the theorem
are produced by the runner from the stated finite lattice operator.
