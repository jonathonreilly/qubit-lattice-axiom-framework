# Standard-Model Relativistic Degrees-of-Freedom Count — Finite Inventory Arithmetic

**Date:** 2026-05-17; narrowed 2026-05-26
**Claim type:** bounded_theorem
**Status:** bounded support theorem. The row is narrowed to a finite
declared-inventory arithmetic certificate for the listed unbroken-Standard
Model relativistic degree-of-freedom bookkeeping.
**Runner:** [`scripts/frontier_sm_relativistic_dof_finite_inventory.py`](../scripts/frontier_sm_relativistic_dof_finite_inventory.py)
**Status authority:** independent audit lane only.

## Purpose

The audit blocker was not the arithmetic `28 + (7/8) * 90 = 106.75`;
it was that the one-hop packet did not contain a self-contained inventory for
the Standard-Model particle-content bookkeeping that produces `28` and `90`.

This note records a finite declared-inventory arithmetic certificate: given the
explicit inventory below, and using the retained fermion/boson thermal factor
supplied by
[`HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md`](HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md),
the effective relativistic count is `g_* = 106.75`.

The declared Standard Model inventory remains an external physical input. This
finite declared-inventory arithmetic certificate is not a framework derivation
of which particles nature contains.

## Declared Inventory

Unbroken electroweak bookkeeping:

| sector | multiplicity | relativistic states |
|---|---:|---:|
| gluons | `8 colors * 2 transverse polarizations` | `16` |
| `SU(2)_L` gauge bosons | `3 bosons * 2 transverse polarizations` | `6` |
| `U(1)_Y` gauge boson | `1 boson * 2 transverse polarizations` | `2` |
| complex Higgs doublet | `4 real scalar components` | `4` |

Therefore `g_bosonic = 16 + 6 + 2 + 4 = 28`.

Fermionic bookkeeping:

| sector | multiplicity | relativistic states |
|---|---:|---:|
| quarks | `6 flavors * 3 colors * 2 spin states * 2 particle/antiparticle` | `72` |
| charged leptons | `3 flavors * 2 spin states * 2 particle/antiparticle` | `12` |
| active neutrinos | `3 flavors * 2 helicity/antiparticle states` | `6` |

Therefore `g_fermionic = 72 + 12 + 6 = 90`.

With the retained fermion weight `7/8`,

```text
g_* = g_bosonic + (7/8) g_fermionic
    = 28 + (7/8) * 90
    = 427/4
    = 106.75.
```

The broken-phase bookkeeping has the same bosonic total:
`16` gluon states + `2` photon states + `9` massive `W+, W-, Z` vector
states + `1` Higgs scalar state = `28`. This is recorded only as a finite
bookkeeping equality, not as a thermal-phase derivation.

## Boundary

This row claims only the finite arithmetic above. It does not claim:

- a framework derivation of the Standard Model particle inventory;
- a framework derivation of the fermion thermal factor;
- a derivation of electroweak thermal equilibrium;
- a physical cosmology theorem;
- closure of any downstream DM-leptogenesis row;
- any new axiom or audit verdict.

Downstream physical use of `g_* = 106.75` still has to carry the declared
Standard Model inventory assumption honestly. This row only removes the
unattributed hard-coded arithmetic from that assumption.

## Context References

These references document the conventional Standard Model thermal inventory;
they are context for the declared inventory, not a framework derivation.

- Kolb & Turner, *The Early Universe* (1990), Table 3.1.
- Husdal, "On Effective Degrees of Freedom in the Early Universe",
  arXiv:1609.04979.
- Mukhanov, *Physical Foundations of Cosmology* (2005), Ch. 3.

## Downstream Usage

This bounded arithmetic wrapper is consumed by thermal-side rows that need the
`g_*` count, including the DM-leptogenesis equilibrium and `H_rad` lanes. Those
rows must cite this note as an explicit Standard Model inventory assumption,
not as a derived framework value.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_sm_relativistic_dof_finite_inventory.py
```

Expected result:

```text
SM relativistic DOF finite inventory certificate: PASS
PASS=28 FAIL=0
```
