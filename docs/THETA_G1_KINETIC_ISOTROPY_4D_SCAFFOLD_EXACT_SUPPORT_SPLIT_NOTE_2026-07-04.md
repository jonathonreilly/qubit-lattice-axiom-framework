# Theta G1 Kinetic-Isotropy 4D Scaffold Exact-Support Split

**Date:** 2026-07-04
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** exact-support source-side split for the local 4D regulator
scaffold only. This note does not retire theta, does not set
`theta_bar = 0`, does not edit any Tier-A registry, axiom, primitive, audit
verdict, or publication-status surface, and does not claim that the current
framework derives the physical 4D gauge carrier, compact topology, branch
cochains, defect closure, sector/readout registration, or phase weighting.
**Audit boundary:** independent audit lane only.
**Primary runner:**
[`scripts/theta_g1_kinetic_isotropy_4d_scaffold_exact_support_split_2026_07_04.py`](../scripts/theta_g1_kinetic_isotropy_4d_scaffold_exact_support_split_2026_07_04.py)

## Target

Blocks 37 and 38 sharpened the G1 route:

- the physical 4D theta carrier is not already supplied by spatial `Z^3`,
  Record, kinetic isotropy, or anomaly-time support;
- a supplied defect penalty has the right algebraic behavior once a 4D carrier
  and branch variables are supplied.

This note splits one useful positive subfact out of that wall. The approved
kinetic-isotropy primitive does supply the **local 4D regulator scaffold**:

```text
Z^3 x Z_tau
```

with the time tick grained on the same footing as the spatial edge. That is
enough for local 4D hypercubic cells and for the algebraic slot

```text
2-cochain cup 2-cochain -> 4-cochain.
```

It is not enough for the physical theta carrier.

## Inputs

- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  explicitly declares the Euclidean regulator block `Z^3 x Z_tau` and the
  kinetic-form isotropy `c_t=c_s`.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  spatial `Z^3` lattice and withholds source/action, readout-context
  selection, physical-observable bridges, dynamics, and downstream theory
  consequences.
- [`docs/audit/data/axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json)
  registers `kinetic_isotropy_primitive` as an approved primitive premise that
  chain-satisfies without bounding downstream rows.
- [`THETA_G1_4D_CARRIER_SUPPLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md`](THETA_G1_4D_CARRIER_SUPPLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md)
  blocks treating the whole physical 4D carrier as already supplied.
- [`THETA_G1_DEFECT_SUPPRESSION_SUPPLIED_PENALTY_EXACT_SUPPORT_NOTE_2026-07-04.md`](THETA_G1_DEFECT_SUPPRESSION_SUPPLIED_PENALTY_EXACT_SUPPORT_NOTE_2026-07-04.md)
  records the conditional suppression route once branch data and a penalty are
  supplied.
- [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
  keeps theta live through the gauge-side winding account and mass-side
  determinant-readout bridge.

## Exact Support Statement

On the local regulator scaffold licensed by the kinetic-isotropy primitive:

1. **There are four edge directions.** The local directions are the three
   spatial lattice axes plus the emergent tick axis `tau`.
2. **There are six plaquette orientations and one 4-cell orientation.** This
   is the exact local cell structure needed for a 2-form cup 2-form expression
   to land in a 4-cell slot.
3. **Spatial-only `Z^3` still lacks the slot.** In three dimensions,
   `C^4=0`; a 2-cup-2 expression has no local 4-cell target.
4. **Complementary plane pairs exist locally in 4D.** Plane pairs such as
   `(0,1)` and `(2,tau)` span all four directions and can feed a nonzero
   local 4-cell orientation. This is the local scaffold counterpart of the
   cross-plane support used by the `T^4` carrier theorem.

Thus the geometric scaffold sub-wall is partially discharged: the framework's
approved primitive already supplies the local 4D regulator geometry needed for
an `F cup F`-shaped expression.

## What Is Still Not Supplied

The physical theta carrier requires more than this local scaffold. This note
does **not** supply:

- compact `T^4` topology or boundary conditions;
- gauge links, branch 2-cochains, or integer shift variables;
- non-exact `H^2` sectors or any topological-sector primitive;
- the closedness law `dn=0` or a physical defect-suppression action;
- a gauge action, measure, energy, probability, or sector weighting;
- physical record/readout registration of flux classes;
- the `F cup F` phase coefficient, phase source, or theta-bar assembly.

Therefore Block37 remains correct: the current framework does not yet supply
the physical 4D carrier. Block39 only isolates that the missing carrier is no
longer missing a local four-dimensional **geometric scaffold**; it is missing
the gauge/topological/physical bridge on that scaffold.

## What This Moves

| Before | After |
|---|---|
| "Physical 4D carrier" was a single residual phrase. | It splits into a supplied local 4D scaffold plus still-open compact/gauge/topological/registration content. |
| Kinetic isotropy could be treated as either irrelevant or over-promoted. | Its exact contribution is pinned: local `Z^3 x Z_tau` regulator geometry only. |
| The next route was broad. | The next positive target is narrower: derive gauge branch data/topological sectors/closedness on the already approved local 4D scaffold. |

## What Does Not Move

- Theta is not retired.
- The Tier-A registry is not edited.
- No axiom or primitive is changed.
- No audit status or effective status is changed.
- No physical 4D carrier theorem is supplied.
- No G1 closedness or defect-suppression theorem is supplied.
- No G2 sector/readout theorem is supplied.
- No G3 phase source, coefficient, or action entry is supplied.
- No G4 assembly or mass-side determinant bridge is supplied.

## Remaining Live Routes

1. **Gauge branch carrier theorem on the scaffold.** Derive gauge links,
   branch 2-cochains, integer shifts, and non-exact sectors on the local 4D
   regulator scaffold.
2. **Compact/topological sector theorem.** Derive the compact/periodic or
   otherwise topological surface needed for `H^2` flux classes and
   intersection pairing.
3. **G1 closedness or defect suppression.** Derive `dn=0` or a physical
   defect-penalty action on the branch carrier.
4. **G2/G3/G4.** Register sectors physically, derive the phase source, and
   assemble only after the mass-side determinant bridge closes.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/theta_g1_kinetic_isotropy_4d_scaffold_exact_support_split_2026_07_04.py
```

Expected close: `FAIL=0`.
