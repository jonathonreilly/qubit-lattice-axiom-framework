# Theta G1 Defect Suppression Supplied-Penalty Exact-Support Note

**Date:** 2026-07-04
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** conditional exact-support source-side split. This note does not
retire theta, does not set `theta_bar = 0`, does not edit any Tier-A registry,
axiom, primitive, audit verdict, or publication-status surface, and does not
claim that the current framework derives a defect-penalty action, physical 4D
carrier, or physical G1 theorem.
**Audit boundary:** independent audit lane only.
**Primary runner:**
[`scripts/theta_g1_defect_suppression_supplied_penalty_exact_support_2026_07_04.py`](../scripts/theta_g1_defect_suppression_supplied_penalty_exact_support_2026_07_04.py)

## Target

Block36 left two concrete positive G1 routes:

1. derive the closed-nonexact branch interface directly; or
2. derive a dynamical suppression law for `dn != 0` defects while preserving
   closed non-exact sectors.

Block37 showed that the physical 4D carrier itself is not already supplied by
spatial `Z^3`, Record formation, kinetic isotropy, or anomaly-time support.
This block studies route (2) under a supplied 4D carrier and a supplied defect
penalty. It asks whether that supplied penalty has the right algebraic shape:
does it suppress defects without collapsing the branch sum to global exactness?

Yes, conditionally.

## Source Packets Read

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  current Lattice, Qubit, Admissibility, and Record surface and withholds
  action, measure, probability, weighting, source/action, and physical
  observable selection.
- [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
  keeps theta live through the gauge-side winding account and mass-side
  determinant-readout bridge.
- [`THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)
  supplies the exact `T^4` witness: closed non-exact sectors have stable
  intersection charge; defectful branches do not.
- [`THETA_G1_CLOSED_NONEXACT_INTERFACE_EXACT_SUPPORT_NOTE_2026-07-04.md`](THETA_G1_CLOSED_NONEXACT_INTERFACE_EXACT_SUPPORT_NOTE_2026-07-04.md)
  identifies the supplied closed-nonexact interface `I1-I4` as the positive
  G1 shape.
- [`THETA_G1_4D_CARRIER_SUPPLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md`](THETA_G1_4D_CARRIER_SUPPLY_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md)
  blocks treating the physical 4D carrier as already supplied by the updated
  axiom/primitive/time-support surface.
- [`THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md`](THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md)
  blocks treating G1 closedness or suppression as already current-surface
  content.
- [`THETA_G1_EXACT_BRANCH_CONSTRAINT_NO_GO_NOTE_2026-07-04.md`](THETA_G1_EXACT_BRANCH_CONSTRAINT_NO_GO_NOTE_2026-07-04.md)
  prunes global exactness `n=dA` because it erases the `H^2` carrier.

## Supplied Penalty Interface

This note studies a supplied interface, not current-surface content:

```text
S1. A physical 4D branch carrier is supplied.
S2. Branches are integer 2-cochains n on that carrier.
S3. The defect current is J(n) = d n.
S4. The branch weight contains a positive local penalty
    exp(-kappa ||J(n)||^2), with kappa >= 0.
S5. The regulated branch family is finite, or a finite truncation is taken
    before the kappa -> infinity projection.
S6. Closed non-exact sectors are included in the branch family.
```

No observed theta value, neutron-EDM comparator, fitted selector, axion
premise, or physical defect-energy theorem is supplied here.

## Exact Support Theorem

On the finite `T^4_2` cochain surface used by the theta carrier, and more
generally in any finite regulated branch family satisfying `S1-S6`:

1. **The penalty is exact-move invariant.** Since `d^2=0`,

   ```text
   J(n + d a) = d n.
   ```

   The penalty is constant on exact local branch orbits.
2. **Closed non-exact sectors survive.** If `dn=0`, then
   `exp(-kappa ||dn||^2)=1` for every `kappa`. In particular the closed
   non-exact branch `e01 + e23` has `Q_raw=2` and remains unsuppressed.
3. **Global exactness is not imposed.** Exact branches have `dn=0`, but they
   are only a subset of the zero-penalty set. Closed non-exact representatives
   are also zero-penalty branches, so the penalty does not delete the `H^2`
   theta carrier.
4. **Defectful branches are projected away in the supplied strong-penalty
   limit.** In a finite branch family, every defectful branch has an integer
   norm `||dn||^2 >= c_min > 0`. Therefore the total defect weight obeys

   ```text
   W_def(kappa) <= N_def exp(-kappa c_min),
   ```

   and `W_def(kappa) -> 0` as `kappa -> infinity`, while closed-sector weights
   remain finite.

Thus a supplied local defect penalty has exactly the algebraic behavior needed
for the second G1 route: it suppresses `dn != 0` without replacing the target
by global exactness.

## What This Moves

| Before | After |
|---|---|
| The dynamical-suppression route was named but not algebraically pinned. | A precise supplied interface is pinned: penalize `||dn||^2` on a physical 4D carrier. |
| Suppression could be confused with exactness. | The support theorem separates them: exact branches and closed non-exact branches both have zero penalty. |
| Defect suppression could be overread as current-surface content. | It remains conditional on a physical carrier and a derived or approved defect-penalty action/measure. |

## What Does Not Move

- Theta is not retired.
- The Tier-A registry is not edited.
- No axiom or primitive is changed.
- No audit status or effective status is changed.
- No physical 4D carrier is supplied.
- No current-surface defect penalty, action, measure, energy, or probability
  law is derived.
- No finite-`kappa` physical suppression strength is claimed.
- No G2 physical sector/readout theorem is supplied.
- No G3 phase source, coefficient, action entry, or physical weighting law is
  supplied.
- No G4 theta-bar assembly or mass-side determinant bridge is supplied.

## Remaining Live Routes

1. **Physical 4D carrier theorem.** Supply the carrier named by Block37.
2. **Defect-penalty action theorem.** Derive an action/measure/energy law whose
   effective branch weight includes `exp(-kappa ||dn||^2)` or an equivalent
   projection onto `dn=0`.
3. **Closed-nonexact interface theorem.** Alternatively derive `dn=0` as a
   branch/Bianchi constraint while allowing non-exact `H^2` sectors.
4. **G2 sector/readout registration.** Register the surviving flux/cocycle data
   as physical record/readout content.
5. **G3 phase source.** Derive the `F cup F` insertion, coefficient, and
   action/measure registration.
6. **Mass-side determinant channel.** Close W2/K-real/determinant-channel
   gates before theta-bar assembly.

## Scope Discipline

This is conditional exact support, not a current-surface G1 theorem. It may be
used as a target specification for a future dynamics/action derivation. It may
not be cited as theta retirement, as a physical defect-suppression theorem, or
as evidence that the updated axioms already contain a defect-energy law.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/theta_g1_defect_suppression_supplied_penalty_exact_support_2026_07_04.py
```

Expected close: `FAIL=0`.
