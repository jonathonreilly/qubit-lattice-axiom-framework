# Theta G1 Defect Closure Current Surface No-Go Note

**Date:** 2026-07-04
**Type:** no_go
**Claim type:** no_go
**Scope boundary:** current-surface test of whether the updated axioms,
approved primitives, and current theta gauge support packets already derive
G1: the closed-branch restriction `dn = 0`, or a dynamical suppression of
branch defects, on the abelianized multi-plaquette dual. This note does not
retire theta, set `theta_bar = 0`, edit any Tier-A registry, primitive,
axiom, audit verdict, lane registry, or publication-status surface, and does
not claim that future defect-closure or defect-suppression routes are
impossible.
**Audit boundary:** independent audit lane only.
**Primary runner:**
[`scripts/theta_g1_defect_closure_current_surface_no_go_2026_07_04.py`](../scripts/theta_g1_defect_closure_current_surface_no_go_2026_07_04.py)

## Target

[`THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md`](THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md)
split the theta gauge-side winding account into four gates. G1 is:

```text
derive the closed-branch restriction dn = 0, or a dynamical suppression of
branch defects, on the abelianized multi-plaquette dual.
```

This block asks whether the current surface already supplies that restriction
or suppression. The answer is no.

## Source Surfaces

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  Lattice, Qubit, Admissibility, and Record, while explicitly withholding
  dynamics, probabilities, update laws, formation rules, source/action,
  physical-observable identification, central-sector decomposition, and
  readout-context selection.
- [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
  keeps theta live through the gauge-side winding account and the mass-side
  determinant-readout bridge.
- [`THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)
  proves the exact closed-branch carrier and names defect closure as the
  carrier residual: with `dn != 0`, the cup-square charge is not class-stable.
- [`THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md`](THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md)
  blocks the broader shortcut that the updated axioms/primitives already
  supply the gauge-side action, `Q`, readout, and weighting structure.
- [`THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md`](THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md)
  leaves G3 open and says the phase insertion still needs an oriented
  functional, coefficient, and physical registration.
- [`THETA_G3_CENTRAL_SECTOR_PHASE_CHARACTER_EXACT_SUPPORT_NOTE_2026-07-04.md`](THETA_G3_CENTRAL_SECTOR_PHASE_CHARACTER_EXACT_SUPPORT_NOTE_2026-07-04.md)
  supplies finite phase-character support and explicitly says `dn != 0`
  must be disciplined before the closed-branch carrier can be treated as
  physical rather than witness-surface support.

## No-Go Statement

On the current surface, G1 is not derived.

The existing carrier packet proves the mathematical necessity of closedness
for the abelianized witness surface:

```text
closed branch dn = 0  -> class-stable cup-square charge
defect branch dn != 0 -> local branch moves change the cup-square value
```

But the current framework sources do not supply the physical premise that
chooses the left side:

| Candidate source | Current standing |
|---|---|
| Lattice | Supplies `Z^3` sites, adjacency, translations, and proper cubic rotations. It does not supply a four-dimensional branch cochain, Bianchi identity, monopole current rule, or gauge-action sector. |
| Qubit | Supplies the local one-site possibility domain. It does not constrain branch 2-cochains or impose `dn = 0`. |
| Admissibility | Supplies one fixed nearest-neighbor availability rule. The axiom memo explicitly says it is not dynamics, transition weights, a Hamiltonian, a transfer operator, or physical persistence. It does not impose a cochain closedness equation. |
| Record | Supplies record occurrence, one-record-per-site locking, permanence, and finite scalar readout additivity. It can register a sector after the readout context exists; it does not create the branch-sector decomposition, impose `dn = 0`, or suppress defects. |
| Approved primitives | Scale, kinetic isotropy, and realized state supply a ruler, an isotropy ratio, and pointwise realized-history evaluation. None is a gauge-sector Bianchi law or monopole-suppression theorem. |
| Current theta packets | They show why G1 is needed and where the carrier lives, but they do not derive the physical closed-branch restriction or its dynamics. |

Thus the route

```text
updated axioms/primitives + closed-branch carrier support
therefore physical branch defects are absent or suppressed
```

is invalid on the current surface.

## Finite Algebraic Boundary

The runner recomputes the exact finite `T^4_2` cochain contrast behind this
no-go.

For a closed branch cochain `n`, with `dn = 0`, the cup-square value

```text
Q_raw(n) = sum n cup n
```

is invariant under local branch moves `n -> n + d lambda`. For a unit
complementary-flux witness, `Q_raw = 2`, and all tested local branch moves
keep `Q_raw = 2`.

For a defectful branch cochain `n_def`, with `dn_def != 0`, the same local
move family produces multiple values:

```text
Q_raw(n_def + d lambda) in {-2, -1, 0, 1, 2}
```

including odd values. Hence the halved integer charge and sector
decomposition are not class-stable on the unrestricted defectful branch sum.
This is why G1 is a real blocker, not bookkeeping.

## What This Moves

| Before | After |
|---|---|
| G1 was named as an open gate next to G2/G3/G4. | G1 is isolated as a current-surface no-go against absorption by Admissibility, Record formation, approved primitives, or closed-branch carrier support. |
| The closed-branch carrier support could be overread as physical closure. | The runner rechecks that closedness is exactly the extra premise: the charge is stable on `dn=0` and unstable on `dn!=0`. |
| G3 phase-character support sharpened the phase slot. | G3 now has an explicit precondition: do not treat the closed-branch carrier as physical until G1 is supplied. |

## What Does Not Move

- Theta is not retired.
- The Tier-A registry is not edited.
- No G1 defect-closure theorem is supplied.
- No defect-suppression dynamics is supplied.
- No G2 physical sector/readout theorem is supplied.
- No G3 phase source, coefficient, action entry, or physical weighting law is
  supplied.
- No G4 gauge/mass theta-bar assembly is supplied.
- No mass-side determinant-channel bridge is supplied.
- No primitive, axiom, audit status, or effective status is changed.

## Remaining Live Routes

1. **G1 positive theorem.** Derive `dn = 0` from a physical gauge-sector
   Bianchi/closedness law, or derive dynamical suppression of `dn != 0`, without
   assuming the theta carrier surface as an input.
2. **G2 sector/readout registration.** Derive that the flux/cocycle data are
   physical SU(3) record/readout content after G1 is disciplined.
3. **G3 phase source.** Derive the odd-sensitive phase insertion, coefficient,
   and action/measure registration after the carrier surface is physical.
4. **Theta mass-side bridge.** Close the determinant-channel readout bridge
   separately before any `theta_bar` assembly attempt.
5. **Governance route.** If theorem routes fail, adopting a defect-closure,
   defect-suppression, phase-source, or sector/readout premise is an explicit
   owner-governance decision, not an axiom consequence.

## Scope Discipline

This is not a universal no-go against defect closure. It proves only that the
current framework surface and current theta support packets do not supply it.
A future retained dynamics theorem, gauge-sector theorem, continuum/limit
bridge, or explicit owner-approved premise could still close G1.

The Record axiom's new formation sentence is also not a defect law. It says
records form, while the axiom memo explicitly withholds which admissible
possibility a new record locks, at which site, with what weight, or at what
rate. That occurrence content cannot be laundered into `dn = 0`.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/theta_g1_defect_closure_current_surface_no_go_2026_07_04.py
```

Expected close: `FAIL=0`.
