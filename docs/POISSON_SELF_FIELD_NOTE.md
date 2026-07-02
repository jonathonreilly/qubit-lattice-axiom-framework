# Poisson Self-Field: Transverse Profile from a Local Equation

**Date:** 2026-04-06
**Status:** bounded support / open PDE-origin gate — transverse profile is
computed by solving a supplied 2D Poisson equation; longitudinal falloff is
still imposed; F~M=0.9997 and Born<1.5e-15 on the supplied Poisson branch.

## Source boundary (2026-06-12)

**Boundary:** bounded support for a supplied Poisson branch, not a retained
derivation of the field law. Effective status is audit-derived; this source
records only the claim boundary.

The note solves and tests a manually specified transverse Poisson equation,
while the PDE, source, boundary condition, normalization, physical gravity
readout, and longitudinal law remain supplied or imposed.

This note may be cited for the numerical behavior of the supplied Poisson
branch and its exact-null/Born-cancellation checks. It may not be cited as a
retained derivation of gravity, a derived transverse field law from framework
axioms, or a full 3D field equation.

## Supplied-branch core split (2026-06-18)

[`POISSON_SELF_FIELD_SUPPLIED_BRANCH_CORE_BOUNDED_NOTE_2026-06-18.md`](POISSON_SELF_FIELD_SUPPLIED_BRANCH_CORE_BOUNDED_NOTE_2026-06-18.md)
extracts the finite supplied-branch theorem from this parent note. That split
does not promote this parent to a retained gravity derivation. It certifies only
that, once the 2D PDE, point source, zero boundary, strength normalization,
gravity readout, and longitudinal `1/(dx+0.1)` factor are supplied, the runner
computes the stated finite consequences on the declared lattice branch:
TOWARD shifts for the three families, near-linear F~M response, exact null at
`s=0`, and machine-precision Born cancellation.

## Artifact chain

- [`scripts/poisson_self_field.py`](../scripts/poisson_self_field.py)
- [`POISSON_SELF_FIELD_SUPPLIED_BRANCH_CORE_BOUNDED_NOTE_2026-06-18.md`](POISSON_SELF_FIELD_SUPPLIED_BRANCH_CORE_BOUNDED_NOTE_2026-06-18.md)
- [`scripts/poisson_self_field_supplied_branch_core_2026_06_18.py`](../scripts/poisson_self_field_supplied_branch_core_2026_06_18.py)
- [`logs/runner-cache/poisson_self_field_supplied_branch_core_2026_06_18.txt`](../logs/runner-cache/poisson_self_field_supplied_branch_core_2026_06_18.txt)
- [`logs/2026-04-06-poisson-self-field.txt`](../logs/2026-04-06-poisson-self-field.txt)

## Question

Can the gravitational field be DERIVED from a local equation instead
of imposed as f=s/r?

## Result: PARTIAL

The TRANSVERSE (y, z) profile at each layer is computed by the supplied
2D Poisson branch:

  laplacian_⊥(f) = -source(iy, iz)

The LONGITUDINAL (x) falloff is still imposed via an explicit
1/(dx+0.1) factor in `_make_poisson_field`. So the full 3D field
law is not supplied by a single PDE here; only the transverse
profile is computed inside the supplied Poisson branch.

| Property | Imposed 1/r | Poisson (transverse) |
| --- | ---: | ---: |
| F~M (Fam1) | 0.990 | **0.9997** |
| F~M (Fam2) | 0.993 | **0.9993** |
| F~M (Fam3) | 0.994 | **0.9994** |
| Born (on Poisson branch) | 0.00e+00 | **9.84e-16** |
| Gravity | TOWARD | **TOWARD** |
| Null (s=0) | exact | **exact** |

The Born test is now run with the Poisson field active (not the
zero-field baseline). The measured ratio is below `1.5e-15`, at machine
precision, so the linear propagator is preserved by the Poisson branch.

The transverse Poisson profile gives BETTER F~M than imposed 1/r
(0.9997 vs 0.990), because it is lattice-adapted instead of continuum.

## What this means

Within this supplied branch, the transverse profile is no longer an arbitrary
profile table: it is the numerical solution of the supplied local PDE on each
layer. The PDE, source, boundary condition, normalization, physical readout,
and longitudinal axis remain supplied or imposed. Deriving those ingredients
from framework-native dynamics requires a separate 3D Poisson, wave, or
retarded-field lane.

## Claim boundary

- Transverse profile: computed from the supplied 2D Poisson problem per layer
- Longitudinal profile: still imposed as 1/(dx+0.1)
- PDE/source/boundary/normalization/readout: supplied, not derived here
- Static (no time evolution); dynamical field is the next milestone
- Connection to causal cone / retardation requires time-dependent generalization

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [gate_b_poisson_self_gravity_note](GATE_B_POISSON_SELF_GRAVITY_NOTE.md)
