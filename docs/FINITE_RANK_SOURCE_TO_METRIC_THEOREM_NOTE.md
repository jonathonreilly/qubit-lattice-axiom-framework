# Finite-Rank Source-to-Metric Self-Contained Finite-Lattice Certificate

**Date:** 2026-04-14; self-contained repair 2026-05-26
**Script:** `scripts/frontier_finite_rank_source_to_metric_theorem.py`
**Claim type:** bounded_theorem
**Status:** bounded finite-lattice certificate. This is not a full nonlinear
GR theorem and not a tensorial `3+1` matching theorem.

## Purpose

The earlier row mixed a valid finite-rank source-to-exterior computation with
module-import authority edges for the finite-rank operator, the coarse-grained
radial residual map, and the Schur boundary action. This repair removes those
helper-wrapper imports from the runner. The current packet contains the finite
construction directly:

- the Dirichlet-box negative lattice Laplacian;
- the seven-site finite-rank support and support projector;
- the Woodbury/Dyson compressed-source solve;
- the exterior shell trace and Schur Dirichlet-to-Neumann matrix;
- the shell-averaged radial harmonic projection `phi_eff(r) = a/r`;
- the finite-difference static isotropic Einstein-residual diagnostic.

The row therefore stands as a self-contained finite-lattice certificate, not
as a claim that the accepted axiom already implies a full continuum gravity
map.

## Bounded Claim

On the fixed `15^3` Dirichlet lattice, with the seven-site support and
finite-rank matrix defined in the runner:

1. The finite-rank column identity
   `G_W P = G_0 P (I - W G_S)^-1` is verified to machine precision.
2. The compressed effective source
   `q_eff = (I - W G_S)^-1 m` reproduces the exact finite-rank field.
3. The resulting exterior field is harmonic away from the support.
4. The exact finite-rank shell trace is stationary for the Schur
   boundary action on the `R = 4` exterior shell.
5. Shell averaging and the radial harmonic projection give a bounded
   static isotropic residual reduction on the same finite lattice.

The runner reports the numerical certificate:

```text
finite-rank column identity max column error            3.886e-16
finite-rank compressed source max field error           9.992e-16
finite-rank exterior harmonicity max residual           1.277e-15
boundary reconstruction error                           6.939e-17
Schur flux error / stationary gradient                  4.163e-16 / 4.163e-16
best radial projection                                  R_match=5.0
direct same-source residual                             1.039e-02
coarse radial-harmonic residual                         7.028e-06
improvement                                             1477.6x
```

## What Changed

The runner no longer delegates the load-bearing construction to the previous
frontier helper modules. It defines the finite-rank source family, the
coarse-grained metric residual evaluator, and the Schur boundary-action
calculation locally in the runner. The output is therefore inspectable as one
restricted packet.

This clears the prior audit blocker that the scalar-to-metric reduction relied
on helper-wrapper imports rather than on an attached construction.

## Boundary

This row does not claim:

- a tensorial `3+1` matching law;
- full nonlinear GR;
- a continuum-limit theorem;
- a universal source-to-metric theorem beyond the fixed finite lattice;
- derivation of the finite-rank support choice from a new or accepted axiom;
- any new axiom or audit verdict.

The direct same-source metric still carries a nonzero residual on the finite
grid. The result is a bounded source-to-exterior plus scalar/static isotropic
certificate, with the tensorial completion principle left open.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_finite_rank_source_to_metric_theorem.py
```

Expected summary:

```text
PASS=17 FAIL=0
```
