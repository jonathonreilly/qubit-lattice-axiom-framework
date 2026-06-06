# Flavor Z=det Fermionic-Statistics Locator

**Date:** 2026-06-04
**Claim type:** open_gate
**Actual current-surface status:** bounded-support
**Trace class:** negative_route_pruning
**Reachability to target:** prunes the route "finite local dimension, ordinary tensor-product ladders, or Jordan-Wigner realizability by themselves select cross-site CAR/Grassmann statistics".
**Bare retained allowed:** false
**Audit required before effective status change:** true
**Runner:** `scripts/flavor_zdet_fermionic_statistics_admission_2026_06_04.py` (SCORECARD PASS=7).

## Closed Packet

This note isolates the determinant-amplitude input:

```text
Z = det(D + J)
```

The finite packet verifies two sides of the gate:

1. If Grassmann/CAR matter variables are supplied, the finite Berezin Gaussian
   gives the determinant.
2. The tested finite hard-core/tensor-product carrier data do not by themselves
   select cross-site CAR/Grassmann statistics.

The packet does not derive the choice of Grassmann/CAR variables from baseline
axioms, and it does not introduce a new axiom or admission.

## Direct Checks

1. **Supplied Grassmann variables realize `det`.** The signed permutation sum
   matches `det(M)` for the tested finite matrix.

2. **Ordinary cross-site qubit ladders commute.** The ordinary two-site tensor
   product does not satisfy CAR across sites.

3. **Jordan-Wigner is a realization, not a selector.** A dressed generator set
   realizes cross-site CAR, but the dressing is an additional representation
   choice inside this packet.

4. **Local dimension two is not enough.** Fermions and hard-core bosons share
   nilpotent two-state local carriers; the difference is cross-site statistics.

5. **Determinant and permanent differ.** Signed determinant statistics and
   unsigned hard-core/permanent-style statistics are distinct finite choices.

6. **Koide internal chirality is separate.** `Gamma_chi` acts on the internal
   generation factor and commutes with the tested `C3`-equivariant mass
   operator. Spatial CAR selection does not settle that internal residual.

## Scope

This is not a universal spin-statistics theorem and not a baseline derivation
of FS. It only says the tested finite routes do not force FS, while supplied
Grassmann/CAR variables do realize the determinant amplitude.

If later work derives or admits a cross-site CAR/Grassmann matter premise, that
could supply the determinant-amplitude input for downstream log-det consumers.
This file does not promote those consumers or rewrite their dependency state.

## No-Go Discipline Gate

The no-go applies only to the finite routes represented in the runner:

| Route | Status in this packet |
| --- | --- |
| On-site Clifford/local dimension | Does not force cross-site CAR. |
| Ordinary tensor-product ladders | Commute across sites. |
| Jordan-Wigner | Realizes CAR after a generator/string choice; not a selector. |
| Determinant-character mathematics | Works after determinant amplitude is supplied. |
| Koide chirality transport | Separate internal-generation residual. |
| Continuum spin-statistics | Not tested here and left open. |

## Provenance

- The runner checks determinant/permanent arithmetic, ordinary ladder
  commutation, Jordan-Wigner CAR realization, local nilpotency, and internal
  `Gamma_chi` separation.
- No `docs/audit/**` status is updated by this packet.
- No new axiom is introduced.
