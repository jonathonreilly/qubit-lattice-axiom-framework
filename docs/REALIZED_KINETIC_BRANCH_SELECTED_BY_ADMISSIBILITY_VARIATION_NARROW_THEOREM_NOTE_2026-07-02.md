# Realized Kinetic Branch: Selected by Admissibility Variation on the Two-Flux-Class Surface

**Date:** 2026-07-02
**Type:** positive_theorem
**Claim type:** positive_theorem
**Claim scope:** On the parent two-flux-class kinetic surface, the clarified
Admissibility clause adds a variation premise to the nearest-neighbor
availability rule. The finite one-qubit classification gives only two
proper-cubic-covariant per-direction algebra-dimension patterns:
neighbor-constant `[1, 1, 1]` and direction-tagged varying `[2, 2, 2]`.
The sibling computations identify K0 with the neighbor-constant
`[1, 1, 1]` structure and K1 with the direction-tagged varying
`[2, 2, 2]` structure. Therefore, on this representative-level surface
and under the enlarged premise set, the clarified clause selects K1.
The boundary is that pairing terms remain outside by the parent's
surface declaration; this note does not re-grade the parent, does not
touch the Tier-A registry, and sets no audit status.
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Primary runner:**
[`scripts/realized_kinetic_branch_selected_by_admissibility_variation_2026_07_02.py`](../scripts/realized_kinetic_branch_selected_by_admissibility_variation_2026_07_02.py)

## Why This Note Exists

The minimal axiom note now states the clarified Admissibility clause:
"For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions."

The kinetic-class parent left the one-bit residual explicit:
"the flux(-1) selector is not forced because K0 also satisfies the constraints".
That verdict concerned the parent's own constraint set; the clarified
Admissibility clause is an additional axiom premise, so selection under
the enlarged premise set does not contradict the parent's audited scope.

The reset context `AXIOM_RESET_IMPACT_2026-06-29.md` says a realized
branch statement should name the "nonzero first-order Dirac-square kinetic
carrier" and the "mutually anticommuting self-adjoint-unitary coefficient
family". This note supplies the narrow rule-level selector that was not
available to the parent before the clarified variation clause.

## Statement

The parent representatives are used exactly as in the sibling notes:

```text
K0: phi=+1, representative t == 1 (scalar tight-binding; extensive zero surface).
K1: phi=-1, representative eta0: eta0_1 = 1, eta0_2 = (-1)^{x1}, eta0_3 = (-1)^{x1+x2}
(Kawamoto-Smit class; 8 isolated Dirac zeros; = absorbed naive Dirac).
```

For each direction `mu`, a nearest-neighbor availability structure is a
conditioning projector family on the one-site qubit factor. Proper cubic
rotations permute the three directions, and translations copy the same
rule to each site.

**T1 - rule-level classification.** On the one-qubit-per-site lattice,
the finite blocked-cell classification has a vacuous neighbor-constant
family for any internal content. A varying covariant structure requires
a nontrivial one-qubit conditioning algebra in any direction where it
varies. On `C^2`, such a projector family generates a dim-2 maximal
abelian algebra. Proper-cubic transitivity on the axes then forces the
same nontrivial structure on all three directions. Thus a rule satisfying
the clarified variation clause cannot be carried by per-direction
algebra dimensions `[1, 1, 1]`.

**T2 - surface selection.** On the parent's licensed surface, the
nearest-neighbor structures available to carry the rule are exactly the
classified kinetic systems. By the sibling conditional-record note's
T-A computation, K0 realizes only neighbor-constant maps, with dimensions
`[1, 1, 1]`. By the sibling discriminator note's D4 and the sibling
conditional-record note's T-B computation, K1 carries the direction-tagged
varying family, with dimensions `[2, 2, 2]`. Hence the clarified
Admissibility clause selects the flux(-1) class on the licensed surface.
The kinetic-order selector bit is derived here under the enlarged premise
set. Composing with the sibling D1/D2 computations and the parent
absorbing-frame theorem gives the nonzero first-order Dirac-square kinetic
carrier with the mutually anticommuting self-adjoint-unitary coefficient
family.

**T3 - load-bearing refutation leg.** If the variation requirement is
dropped and the pre-clarification determination-only reading is recomputed,
K0 survives every remaining constraint, exactly reproducing the parent's
"not forced" verdict. The variation words in the clarified clause are
therefore load-bearing.

**T4 - covariance legs.** The T1 classification is stable under local
`U(1)` frames. Improper mirror contrast changes the handedness of the
computed K1 coefficient family, and a sub-region `SU(2)` frame breaks the
uniform direction-tagged structure; these are contrast legs outside the
proper-cubic plus local-`U(1)` covariance used by the surface.

## Proof Sketch

The runner copies the K0/K1 phase-system and absorbing-frame constructions
from the two sibling runners. It recomputes the parent plaquette flux
anchors on `L = 4` and `L = 6`, extracts K0 scalar direction coefficients,
and extracts the K1 `Gamma_mu` family from the eta0 signs rather than from
target Pauli matrices.

For T1, checks enumerate the finite dimension patterns in `{1, 2}^3` and
the proper-cubic axis permutations. The only covariant dimension patterns
are `[1, 1, 1]` and `[2, 2, 2]`; the only nonconstant covariant variation
pattern is the all-axis dim-2 case. The constant full-subset map is checked
separately and remains covariant for every enumerated internal pattern.

For T2, checks recompute the sibling D4/T-A/T-B surface data. K0 has only
the full projector `I` in each direction, so every realized availability
map is neighbor-constant. K1 has two rank-one orthogonal projectors in each
direction, giving an explicit varying witness. The selected survivor under
the clarified variation clause is exactly `K1`, and the same computed
`Gamma_mu` family verifies the Dirac-square and anticommutation
consequences.

For T3, the same survivor function is rerun with `require_variation=False`.
Both K0 and K1 survive that determination-only reading, while K0 still has
zero conditioned maps. This is the recomputation of the parent's residual,
not a prose restatement.

For T4, checks multiply the direction data by local `U(1)` edge phases and
verify that the algebra dimensions and K1 projectors remain available. The
contrast legs then flip one direction by an improper mirror and apply a
non-diagonal `SU(2)` frame only on a sub-region; the first flips the K1
handedness invariant, and the second produces nonzero spread across the
cell.

## Consequence

On this surface, what this retires is the one-bit kinetic-order selector
residual, P-KIN's surviving bit. The selection is a theorem of the enlarged
premise set: the axioms including the 2026-07-02 clarified clause plus the
landed chain. It does not re-grade the parent, does not touch the Tier-A
registry, and sets no audit status.

The next path this opens: transporting the selection off the representative
level via the parent's frame theorems, and the gauged/interacting surface.

## Boundaries

- Representative-level on the parent's licensed surface.
- The licensed surface is the Q-conserving nearest-neighbor bilinear
  surface; pairing terms remain outside by the parent's declaration.
- Class-level transport is inherited only where the parent's frame theorems
  transport it.
- The selection uses the enlarged premise set and does not re-grade the
  parent.
- No Tier-A registry change and no audit status is set here.

## Dependencies

- [`REALIZED_KINETIC_BRANCH_DISCRIMINATOR_DICHOTOMY_NARROW_THEOREM_NOTE_2026-07-02.md`](REALIZED_KINETIC_BRANCH_DISCRIMINATOR_DICHOTOMY_NARROW_THEOREM_NOTE_2026-07-02.md)
  - D1, D2, and D4 discriminators.
- [`REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-02.md`](REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-02.md)
  - T-A K0 neighbor-constant computation and T-B K1 varying witness.
- [`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md)
  - parent surface and two classes.
- [`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md)
  - absorbing frame.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
  - clarified Admissibility clause.

Context only: `AXIOM_RESET_IMPACT_2026-06-29.md`.

## Runner And Cache

Primary runner:
[`scripts/realized_kinetic_branch_selected_by_admissibility_variation_2026_07_02.py`](../scripts/realized_kinetic_branch_selected_by_admissibility_variation_2026_07_02.py)

No runner cache is generated by this note.

Current local runner result:

```text
TOTAL: PASS=15 FAIL=0
```

## Changelog

- **2026-07-02.** Initial note and numpy runner. The runner reports
  `TOTAL: PASS=15 FAIL=0`.
