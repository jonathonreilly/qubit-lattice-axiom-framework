# Fermionic Gaussian N-Point Convergence Reduces to Two-Point Convergence

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict. Effective status is
pipeline-derived after independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_fermionic_gaussian_npoint_from_two_point.py`](../scripts/frontier_fermionic_gaussian_npoint_from_two_point.py)
**Cached log:**
[`logs/runner-cache/frontier_fermionic_gaussian_npoint_from_two_point.txt`](../logs/runner-cache/frontier_fermionic_gaussian_npoint_from_two_point.txt)

## Statement

For a free fermionic Gaussian/Berezin field whose `2n`-point correlators are
Pfaffians of the antisymmetric two-point matrix `C`, convergence of the
two-point matrix implies convergence of every fixed finite `2n`-point
correlator.

The reason is elementary and finite-dimensional: the Pfaffian is a polynomial in
the matrix entries. Therefore if `C_a -> C`, then `Pf(C_a) -> Pf(C)` for every
fixed finite correlator size. In this restricted fermionic Gaussian setting, the
``beyond the two-point'' hierarchy reduces to the supplied two-point
convergence premise plus Pfaffian/Wick structure.

## What this establishes

- `Pf(C)^2 = det(C)` for antisymmetric matrices of sizes `2, 4, 6, 8` in the
  runner.
- Pfaffian values change continuously under small two-point perturbations.
- In a concrete convergence sequence `C_a -> C`, the tested Pfaffian
  correlators converge to the limiting Pfaffian.
- The free fermionic Gaussian hierarchy has no additional finite `n`-point
  convergence datum beyond the two-point convergence premise and the Wick
  hierarchy.

## Boundary

This note does not itself prove the two-point continuum convergence premise. It
does not set the status of that premise, close the OS reconstruction package,
derive a boost/Poincare representation, prove positive energy or
microcausality, supply partner chirality, construct a Wightman field, or touch
interacting theory. It is free `U=1` Gaussian/Berezin algebra only.

In particular, this note should be read as:

```text
fixed finite fermionic Gaussian n-point convergence
    <= supplied two-point convergence + Pfaffian hierarchy + continuity.
```

It must not be read as an audit-status promotion of the two-point parent, the
OS reconstruction parent, or any larger free-field closure surface.

## Load-Bearing Inputs

- [`FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md`](FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md)
  for the conditional OS/Wightman context and the free Gaussian Pfaffian
  hierarchy being reduced.
- [`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
  for the two-point continuum-convergence target; this note does not promote
  or re-audit that target.

## Forbidden-Imports Check

No PDG value, fitted selector, observed mass, external numerical comparator, or
new axiom is consumed. The runner verifies finite Pfaffian algebra and
continuity diagnostics only.

## Validation

Run:

```bash
python3 scripts/frontier_fermionic_gaussian_npoint_from_two_point.py
```

Expected: `TOTAL: PASS=6 FAIL=0`.
