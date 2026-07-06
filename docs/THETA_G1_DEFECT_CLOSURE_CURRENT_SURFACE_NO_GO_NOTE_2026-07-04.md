# Theta G1 Defect Closure Current Surface No-Go Note

**Date:** 2026-07-04
**Type:** no_go
**Claim type:** no_go
**Scope boundary:** first-principles route test for G1, the defect-closure
gate on the abelianized theta gauge carrier. This note does not retire theta,
does not set `theta_bar = 0`, does not edit any Tier-A registry, primitive,
axiom, audit verdict, or publication-status surface, and does not claim that a
future constraint-level or dynamical defect-suppression route is impossible.
**Audit boundary:** independent audit lane only.
**Current-main posture (2026-07-06):** live `main` now records Tier-A count
zero: theta was retired 2026-07-05 by retained derivation, and
`AC_phi_lambda` was retired by owner-governance adoption. This note banks the
historical G1 defect-closure no-go only; it does not reopen, modify, or
re-grade either retirement record, `tier_a_admissions.json`, or owner-governed
premise data.
**Primary runner:**
[`scripts/theta_g1_defect_closure_current_surface_no_go_2026_07_04.py`](../scripts/theta_g1_defect_closure_current_surface_no_go_2026_07_04.py)

## Target

[`THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md`](THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md)
split the gauge-side theta residual into four gates. G1 is:

```text
derive the closed-branch restriction dn = 0, or a dynamical suppression of
branch defects, on the abelianized multi-plaquette dual.
```

This block asks whether the current framework surface already supplies that
restriction or suppression. It does not.

## Source Packets Read

- [`THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)
  proves the exact closed-branch carrier and the defect witness: with
  `dn != 0`, the cup square is not branch-move invariant and no sector
  decomposition exists on the unrestricted branch sum.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
  withholds source/action, weighting, dynamics, context-selection, and
  arbitrary physical-observable identification.
- [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
  keeps theta in Tier-A, with a gauge-side winding residual and a mass-side
  determinant residual.
- [`THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md`](THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md)
  blocks the shortcut that the updated axioms/primitives already supply the
  gauge-side action/Q/readout/weighting structure.
- [`THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md`](THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md)
  blocks the neighboring shortcut that the current surfaces already derive the
  phase-type `F cup F` insertion.

## No-Go Statement

On the current surface, G1 is not derived.

The carrier theorem proves a conditional exact surface:

```text
if dn = 0, then flux sectors exist and theta couples to the intersection
charge alone.
```

It also proves the reason that condition is load-bearing:

```text
if dn != 0, local branch moves change the cup square and may make Q_raw odd,
so the branch-summed surface has no class-stable theta sector decomposition.
```

Neither statement is a derivation that physical branch cochains satisfy
`dn = 0`, and neither supplies a measure or action that suppresses `dn != 0`.
The present framework surface therefore localizes G1; it does not close it.

## Route Fan-Out

| Candidate route | Current standing |
|---|---|
| Algebraic identity `d^2 = 0` | Applies to exact branch moves `d lambda`; it does not make an arbitrary branch 2-cochain closed. |
| Closed-branch carrier | Exact and useful once `dn = 0` is imposed; conditional on the closure gate. |
| Defect witness | Shows why unrestricted defects are not harmless; it is evidence for needing G1, not a proof of G1. |
| Minimal axioms and approved primitives | No branch-action, no update law, no defect energy, no probability or suppression rule. |
| Record/readout rule | Reads existing record content; it does not manufacture closedness or select a defect-free sector. |
| Admissibility | Allows possibilities; it is not a dynamics axiom and does not select the closed branch. |
| G3 phase insertion work | The phase slot remains open and cannot bypass the carrier's need for defect discipline. |
| Tier-A registry | The gauge-side winding residual remains present; the registry is not edited by this block. |

## Exact Algebraic Boundary

The runner rechecks the finite `T^4_2` cochain facts behind the boundary:

- `d^2 = 0` for the cubical complex, so exact branch moves preserve
  closedness;
- the six unit-flux representatives are closed and give the expected
  cross-plane intersection form on the closed branch;
- `Q_raw(n + d lambda) = Q_raw(n)` and `Q_raw` is even for closed `n`;
- a single-plaquette branch cochain has `dn != 0`;
- after local branch moves of that open cochain, the cup-square takes multiple
  values including odd values, so no branch-class theta charge exists on the
  unrestricted branch sum;
- the closure condition is a proper constraint on 2-cochains, not a tautology
  of the complex.

These checks prove non-supply by the current surface. They do not prove that a
future constraint-level, defect-energy, or scaling-limit route cannot close G1.

## What This Moves

| Before | After |
|---|---|
| G1 was a named blocker in the positive theta-gauge route. | G1 is now isolated as the missing closedness-or-suppression premise. |
| The closed-branch carrier could be overread as deriving the physical branch condition. | The carrier is explicitly conditional on `dn = 0`; the defect witness proves the condition is necessary. |
| Defect failure could be mistaken for a theta no-go. | It is only an unrestricted-branch-sum no-go; it leaves closed or dynamically suppressed routes open. |

## What Does Not Move

- Theta is not retired.
- The Tier-A registry is not edited.
- No axiom or primitive is changed.
- No audit status or effective status is changed.
- No claim is made that future defect-closure or defect-suppression work is
  impossible.
- No physical `SU(3)` theta sector, continuum limit, or record/readout
  registration is asserted.
- No mass-side determinant-channel bridge is supplied.

## Next Attack Plan

1. **Constraint-level route:** search for a native branch law that forces
   `dn = 0` before summing the theta carrier.
2. **Dynamical route:** search for an action, measure, or scaling-limit
   argument that suppresses `dn != 0` without adding a Tier-A premise.
3. **G2 registration after G1:** if either route closes, register the flux and
   intersection data as record/readout content on the nonabelian sector.
4. **G4 assembly last:** only after G1-G3 and the mass-side bridge are supplied
   should the invariant `theta_bar` interface be attempted.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/theta_g1_defect_closure_current_surface_no_go_2026_07_04.py
```

Expected close: `FAIL=0` with at least 105 checks.
