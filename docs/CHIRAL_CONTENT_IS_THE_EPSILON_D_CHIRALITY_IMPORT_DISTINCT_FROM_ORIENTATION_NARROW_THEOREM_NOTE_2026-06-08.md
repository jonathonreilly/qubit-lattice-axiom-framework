# Staggered Chirality, Qubit Pseudoscalar, and Generation Handedness Are Distinct Orientation Data

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/chiral_content_distinct_recurring_import_2026_06_08.py`](../scripts/chiral_content_distinct_recurring_import_2026_06_08.py)

## Scope

This note checks a narrow finite-algebra correction: three objects that were
loosely conflated as one orientation `Z2` live in different sectors and do not
collapse to one object.

The checked objects are:

| object | sector | `K`-parity | role |
|---|---|---|---|
| `epsilon(x)=(-1)^(x+y+z)` | spatial `Z^3` site grading | even | staggered chirality grading; anticommutes with the tested nearest-neighbor Dirac hop |
| `omega=sigma_1 sigma_2 sigma_3=iI` | one-qubit operator algebra | odd | qubit pseudoscalar |
| `sign(Vandermonde)` | supplied generation-sector handedness | even | orientation sign on a `C3`/`S3` generation ordering |

Therefore the chiral-content import, the qubit pseudoscalar, and the
generation handedness are distinct supplied data. In particular,
`omega = sign(Vandermonde) = epsilon` is not a valid identity.

## Runner Result

The runner verifies:

1. On a finite periodic `Z^3` lattice, the staggered site grading is real and
   anticommutes with the tested nearest-neighbor Dirac hop.
2. In the one-qubit algebra, `sigma_1 sigma_2 sigma_3=iI` is `K`-odd.
3. For the supplied `C3` generation circulant used in the Koide/generation
   sector, the Vandermonde sign is real and lives on the generation labels.
4. The three objects differ by sector and, for `omega` versus the other two,
   by `K`-parity.
5. In a finite tensor-factor model, an independent weak/coupling factor
   commutes with the chirality grading, and vector/left/right dressings remain
   indistinguishable to the grading check. The grading supplies a grading, not
   a chiral-gauging selection.

## Correction

Earlier session prose treated the gauge pseudoscalar, generation handedness,
and staggered chirality as if they were literally one `Z2`. This note lands the
correction only: they are not one object. Any broader claim that the admission
floor is unified by an action-form or coupling-sector theorem remains outside
this note and must be landed separately if supported.

## What Is And Is Not Claimed

- **Is:** the three named structures are finite-algebraically distinct by
  sector, and `omega` is `K`-odd while the staggered grading and generation
  Vandermonde sign are `K`-even.
- **Is:** the tested grading check is blind to the chiral-vs-vector coupling
  choice in the finite tensor-factor model.
- **Is not:** does not derive the staggered chirality grading, the generation
  handedness, the qubit pseudoscalar's physical use, the chiral gauging, or
  `r=1/2`.
- **Is not:** does not claim Record supplies chirality, a coupling, a
  generation orientation, a pseudoscalar orientation, or an action-form
  theorem.
- **Is not:** does not add an axiom, primitive, fitted value, audit verdict, or
  retained status.

## Load-Bearing Inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) supplies only
  the `Z^3` lattice and one-qubit operator algebra used for `epsilon` and
  `omega`.
- [`CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md`](CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md)
  and [`CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05.md`](CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05.md)
  are context for the existing chirality-import boundary.
- [`KOIDE_DELTA_C3_CIRCULANT_SPECTRAL_BOUNDARY_NOTE_2026-06-08.md`](KOIDE_DELTA_C3_CIRCULANT_SPECTRAL_BOUNDARY_NOTE_2026-06-08.md)
  supplies the `C3` circulant/Vandermonde generation-sector context used here.
  This note does not inherit any separate cross-sector identification with the
  qubit pseudoscalar.

## Forbidden-Imports Check

No PDG, fitted, or literature value is consumed. The runner performs only
finite algebra checks on the stated objects. The generation circulant is a
supplied generation-sector object, not an axiom.
