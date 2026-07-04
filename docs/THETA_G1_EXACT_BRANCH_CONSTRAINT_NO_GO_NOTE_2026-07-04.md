# Theta G1 Exact-Branch Constraint No-Go Note

**Date:** 2026-07-04
**Type:** no_go
**Claim type:** no_go
**Scope boundary:** first-principles route test for the G1 constraint-level
shortcut in the theta gauge-side positive route: impose defect closure by
making the branch 2-cochain globally exact, `n = dA`. This note does not
retire theta, does not set `theta_bar = 0`, does not edit any Tier-A registry,
primitive, axiom, audit verdict, or publication-status surface, and does not
claim that future closed-nonexact bundle, sector, or dynamical
defect-suppression routes are impossible.
**Audit boundary:** independent audit lane only.
**Primary runner:**
[`scripts/theta_g1_exact_branch_constraint_no_go_2026_07_04.py`](../scripts/theta_g1_exact_branch_constraint_no_go_2026_07_04.py)

## Target

[`THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md`](THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md)
left the next G1 action as:

```text
search for a native branch constraint that imposes dn = 0.
```

The most direct candidate is the Bianchi-style exactness shortcut:

```text
n = dA  =>  dn = d^2 A = 0.
```

This block asks whether that exact-branch route can close G1 while preserving
the theta carrier. It cannot. Exactness enforces closure, but it also kills
the nontrivial `H^2(T^4,Z)` flux sectors and makes the theta intersection
charge vanish. The route closes the defect by deleting the carrier.

## Inputs

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  approved four-axiom baseline and withholds action, dynamics, weighting,
  source/action, context-selection, and arbitrary physical-observable bridges.
- [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
  keeps theta live through the gauge-side winding account and mass-side
  determinant-readout bridge.
- [`THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md`](THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md)
  names G1 as the defect-closure gate.
- [`THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)
  supplies the exact closed-branch witness surface: sector labels
  `H^2(T^4,Z)=Z^6`, with theta charge the cross-plane intersection pairing,
  conditional on `dn=0`.
- [`THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md`](THETA_GAUGE_WINDING_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md)
  blocks the shortcut that the updated axioms/primitives already supply the
  gauge action, `Q` readout, or sector weighting.
- [`THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md`](THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md)
  blocks the neighboring shortcut that current surfaces already derive the
  phase-type insertion.

## Route Fan-Out

### Frame 1: exact branches do close defects

On the finite cubical `T^4` cochain complex, `d^2 = 0`. Therefore an exact
branch 2-cochain `n = dA` is automatically closed:

```text
dn = d(dA) = 0.
```

This is a real constraint-level mechanism. It is not the whole G1 theorem.

### Frame 2: exact branches erase the cohomology carrier

The theta carrier from the 4D witness surface is not merely closedness. It is
closedness plus nontrivial cohomology:

```text
H^2(T^4,Z) = ker(d:C^2 -> C^3) / im(d:C^1 -> C^2) = Z^6.
```

The runner rechecks, over exact rational ranks on `T^4_2`,

```text
rank d1 = 45,
rank d2 = 45,
dim ker d2 = 51,
dim H^2 = 51 - 45 = 6.
```

Each of the six unit flux representatives is closed but not exact. Requiring
`n = dA` therefore throws away exactly the six flux integers that the theta
carrier uses.

### Frame 3: exact branches have zero theta charge

For exact branches, the cup square is a total coboundary on the closed torus.
The runner checks deterministic integer link cochains and finds:

```text
n = dA  =>  Q_raw(n) = sum n cup n = 0.
```

By contrast, the closed non-exact branch `e01 + e23` has

```text
Q_raw = 2,    Q = 1,
```

and is not in `im d1`. This is the odd-support sector the theta carrier needs.
The exact-branch route removes it.

### Frame 4: exactness is not the physical bundle/sector bridge

A future positive route could still derive closed non-exact sectors through a
bundle, transition-function, abelianized torus-dual, or sector-readout theorem.
That would be a different route: it must derive why physical records carry
closed non-exact branch classes and how the sector label is registered. The
global-exact shortcut does not do that.

### Frame 5: Record and Admissibility do not select exactness

Record readout can read an already-licensed sector label. Admissibility can
constrain available local possibilities. Neither supplies a gauge bundle,
transition data, branch action, defect energy, probability/suppression rule,
or physical theta-sector readout. Thus the exact-branch shortcut is not in the
updated axioms/primitives either.

## No-Go Statement

The implication

```text
native G1 constraint = exact branch n=dA
therefore theta gauge-side winding account is retired
```

is invalid.

Exactness is too strong. It enforces `dn=0`, but it collapses the quotient
`ker d2 / im d1`, removes the six flux-cohomology integers, and makes the
intersection charge vanish. The theta carrier requires closed non-exact
sector data, not global exactness. Therefore G1 cannot be closed by the
global-link exactness shortcut.

## What This Moves

| Before | After |
|---|---|
| The next G1 route was "search for a native branch constraint that imposes `dn=0`." | The simplest exactness/Bianchi shortcut is pruned: it closes defects only by erasing the carrier. |
| `d^2=0` could be overread as solving the carrier residual. | It is classified as exact-branch closure, not closed-nonexact sector derivation. |
| The remaining G1 target was broad. | The target is now a closed-nonexact sector theorem or a dynamical defect-suppression theorem, not global exactness. |

## What Does Not Move

- Theta is not retired.
- The Tier-A registry is not edited.
- No axiom or primitive is changed.
- No audit status or effective status is changed.
- No physical `SU(3)` theta sector, continuum limit, or record/readout
  registration is asserted.
- No claim is made that future bundle, transition-function, closed-nonexact,
  or defect-suppression routes are impossible.
- No mass-side determinant-channel bridge is supplied.

## Remaining Live Routes

1. **Closed-nonexact sector theorem.** Derive physical branch records as
   closed but not globally exact, with `H^2(T^4,Z)` flux labels licensed as
   sector data.
2. **Dynamical defect suppression.** Derive an action, measure, or scaling
   route that suppresses `dn != 0` while preserving closed non-exact sectors.
3. **G2 registration.** If G1 closes, register flux/pairing data as physical
   record/readout content on the nonabelian sector.
4. **G3 action-side phase source.** Derive the phase-type insertion rather
   than merely localizing it.
5. **G4 assembly.** Assemble `theta_bar` only after gauge-side G1-G3 and the
   mass-side determinant channel are supplied.
6. **Owner governance.** Approve a narrow sector/bundle/readout primitive if
   derivation is not required.

## No-Go Discipline Gate

**N1 alternative route enumeration.** The exact-branch route, closed-nonexact
sector route, dynamical defect-suppression route, G2 registration, G3
phase-source route, G4 assembly, and governance route are separated.

**N2 wall independence.** No new wall is introduced. This is a sub-route test
inside G1 defect closure for the gauge-side winding account.

**N3 hidden-wall scan.** The proof imports no measured neutron-EDM bound, no
comparator, no fitted value, no axion assumption, no bundle/sector primitive,
no defect-energy primitive, no action-class primitive, and no registry edit.

**N4 residual matching.** The result matches the theta gauge-side residual:
the carrier needs a closed non-exact topological sector account, not a global
exact 2-cochain.

**N5 proven surface.** Proven here is a no-go for the global exactness shortcut
on the finite `T^4` cochain surface. It is not a universal no-go against
closed-nonexact bundle or dynamical suppression routes.

**N6 partial closure.** G1 is sharpened: do not try to close it with
`n=dA`; derive closed non-exact sectors or defect suppression.

**N7 steelman.** A reviewer can say a real lattice gauge theory has Bianchi
constraints. Correct. This note distinguishes global exactness from
closed-nonexact bundle/sector structure. The latter remains a live route.

**N8 cross-cycle echo.** As in AC and R-eta, a correct algebraic identity
(`d^2=0`) is not enough unless it preserves and licenses the physical readout
carrier.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/theta_g1_exact_branch_constraint_no_go_2026_07_04.py
```

Expected close:

```text
TOTAL: PASS=138 FAIL=0
```
