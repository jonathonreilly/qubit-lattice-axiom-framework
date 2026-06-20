# 3D Inverse-Square Kernel Helper Module

**Date:** 2026-04-04 (wrapper note added 2026-05-17)
**Claim type:** bounded_theorem
**Status:** bounded helper-module wrapper for the 3D inverse-square
kernel propagator-fork module, supplying the width-6 comparator
defaults and the `build_family / barrier_metrics / no_barrier_distance
/ fit_power` helpers used by downstream tail-statistics notes.
**Status authority:** independent audit lane only. This wrapper note
is audit-lane infrastructure for the corresponding helper module.
**Runner:**
[`scripts/lattice_3d_inverse_square_kernel.py`](../scripts/lattice_3d_inverse_square_kernel.py)
**Runner cache:**
[`logs/runner-cache/lattice_3d_inverse_square_kernel.txt`](../logs/runner-cache/lattice_3d_inverse_square_kernel.txt)
**Primary runner / module:** `scripts/lattice_3d_inverse_square_kernel.py`

## Source boundary (2026-06-12)

**Boundary:** renaming / helper-wrapper support only. Effective status is
audit-derived; this source records only the claim boundary.

The load-bearing move is wrapper documentation for constants and helper
function names. This note may be cited only for the module interface. It may
not be cited as a derivation of an inverse-square kernel, asymptotic tail law,
downstream tail-statistics theorem, or implementation-fidelity certificate.

Promotion beyond wrapper support requires the helper source/runner to be
audited for implementation fidelity or a separate theorem deriving the
inverse-square kernel from retained framework inputs.

## 2026-06-17 implementation-fidelity packet

The audit row's re-audit note says to re-check
`scripts/lattice_3d_inverse_square_kernel.py` if the intended target is
implementation fidelity rather than wrapper-level definitional scope. This
source packet supplies that re-check without changing the scientific boundary.

Implementation-fidelity verifier:
[`scripts/lattice_3d_inverse_square_kernel_helper_fidelity_2026_06_17.py`](../scripts/lattice_3d_inverse_square_kernel_helper_fidelity_2026_06_17.py)
with cache
[`logs/runner-cache/lattice_3d_inverse_square_kernel_helper_fidelity_2026_06_17.txt`](../logs/runner-cache/lattice_3d_inverse_square_kernel_helper_fidelity_2026_06_17.txt).

The verifier checks that:

- the module declares the documented width-6 comparator constants;
- `build_family`, `barrier_metrics`, `no_barrier_distance`, and `fit_power`
  are present and callable;
- the propagation helper uses the advertised inverse-square free-kernel
  attenuation `w / L^2` while preserving the spent-delay action expression;
- the SHA-pinned main runner cache is current and zero-exit;
- this note keeps the wrapper-only boundary.

This is an implementation-fidelity certificate only. It may support a
restricted-packet re-audit of the helper interface, but it is not a derivation
of an inverse-square kernel, an asymptotic tail law, or any downstream
tail-statistics theorem. Effective status remains audit-derived.

## Purpose

This wrapper note documents the 3D inverse-square kernel helper
module so downstream notes (notably
`LATTICE_3D_L2_TAIL_STATS_NOTE.md`) can register a one-hop dependency
rather than carry the helper as an unattributed module-top-import.
(Downstream consumer backticked to avoid length-2 cycle — load-bearing
citation direction is *downstream tail-stats → this helper wrapper*,
recorded in the tail-stats note's "## Upstream authority" section.)

## What this module provides

### Module-top configuration constants (the width-6 baseline)

The module declares the canonical comparator configuration as
module-top constants:

- `PHYS_L = 12.0` — physical lattice extent
- `PHYS_W = 6.0` — physical transverse width (the **width-6
  comparator** baseline)
- `PHYS_CONNECTIVITY = 3.0` — physical connectivity radius
- `MASS_Z_VALUES = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0]` — barrier mass scan

These constants define the canonical width-6 comparator row that
downstream `lattice_3d_l2_tail_stats.py` patches via the
`patched_branch` context manager to compare against `PHYS_W = 8.0`.

### Helper functions

- `build_family(...)` — constructs the 3D propagator family on the
  declared `(PHYS_L, PHYS_W, PHYS_CONNECTIVITY)` lattice geometry with
  the declared mass scan.
- `barrier_metrics(...)` — computes the Born probability, `k = 0`
  amplitude, total-variation distance `dTV`, and barrier
  read on the family.
- `no_barrier_distance(...)` — computes the no-barrier centroid,
  `P_near`, and bias readout on the post-peak `z` samples.
- `fit_power(...)` — fits a power-law tail exponent on the post-peak
  segment and reports the exponent and `R^2`.

## What this is used for

The downstream `LATTICE_3D_L2_TAIL_STATS_NOTE.md` patches `PHYS_W` from
the module-default `6.0` to `8.0` while keeping the rest of the
configuration fixed, then re-runs `build_family`, `barrier_metrics`,
`no_barrier_distance`, and `fit_power` to compare the wider lattice
post-peak tail fit against the same-family width-6 baseline.

## Boundary

This wrapper note records the bounded helper-module character of the
3D inverse-square kernel module. It does not claim:

- a framework-level derivation of the inverse-square `1 / L^2` law
  from `Cl(3)` on `Z^3` axioms;
- an asymptotic `b^(-2)` tail-law theorem;
- closure of any downstream tail-statistics theorem.

Its only function is to provide a citeable one-hop authority for the
width-6 comparator constants and helper functions so downstream notes
register the import cleanly instead of carrying it as a module-top
script import without a wrapper.
