# Theta G3 Central-Sector Phase Character Exact-Support Note

**Date:** 2026-07-04
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** exact-support source-side split; independent audit required
before any effective-status change. This note does not retire theta, does
not set `theta_bar = 0`, does not edit any Tier-A registry, axiom,
primitive, audit verdict, or publication-status surface, and does not claim
that the physical G3 phase source, coefficient, action entry, or SU(3)
sector/readout registration has been derived.
**Primary runner:**
[`scripts/theta_g3_central_sector_phase_character_exact_support_2026_07_04.py`](../scripts/theta_g3_central_sector_phase_character_exact_support_2026_07_04.py)

## Purpose

G3 asks for an odd-branch-sensitive multi-plaquette phase-type `F cup F`
insertion. The current-surface no-go split G3 into three missing pieces:

```text
oriented functional, phase coefficient, and physical registration.
```

Block31 exposed SU(3) triple joint-star data that pairwise classes cannot
determine. Block32 then showed that, on a supplied central-sector projection,
closed Heisenberg triples carry an ordered central cocycle. This note extracts
the exact finite phase-character slot from that cocycle.

The result is support for the shape of G3, not a derivation of G3. It shows
what an odd-sensitive central-sector phase character looks like once the
central projection is supplied.

## Inputs

- [`THETA_SU3_STAR_PAIRWISE_REDUCTION_OBSTRUCTION_NO_GO_NOTE_2026-07-04.md`](THETA_SU3_STAR_PAIRWISE_REDUCTION_OBSTRUCTION_NO_GO_NOTE_2026-07-04.md)
  proves that SU(3) pairwise composite class data do not determine all triple
  joint-star data.
- [`THETA_SU3_STAR_CENTRAL_SECTOR_PROJECTION_EXACT_SUPPORT_NOTE_2026-07-04.md`](THETA_SU3_STAR_CENTRAL_SECTOR_PROJECTION_EXACT_SUPPORT_NOTE_2026-07-04.md)
  proves that a supplied central-sector projection kills nonclosed triples and
  records a central phase on closed triples.
- [`THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)
  shows that real class-weight gluing is orientation-reversal-even, pushing
  odd theta content to a phase-type insertion.
- [`THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md`](THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md)
  records that the current surface does not derive the G3 phase insertion,
  coefficient, or physical registration.
- [`THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md`](THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md)
  ranks G3 as the highest-leverage theta gauge-side target.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  current axiom boundary and withholds source/action, phase weighting,
  physical-observable identification, central-sector decomposition, and
  readout-context selection.
- [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
  keeps theta live through the gauge-side winding account and mass-side
  determinant-readout bridge.

## Supplied Central-Sector Surface

Use the same finite SU(3) clock/shift convention as Block32:

```text
X^3 = Z^3 = I,     Z X = omega X Z,     omega = exp(-2 pi i / 3),
E(a,b)=X^a Z^b,
E(a,b) E(c,d) = omega^(-b c) E(a+c, b+d).
```

For a closed triple `(A,B,C)` of noncentral Heisenberg staples, define

```text
k_ABC by ABC = omega^(k_ABC) I,
k_ACB by ACB = omega^(k_ACB) I,
q_c(A,B,C) = k_ABC - k_ACB mod 3.
```

If the vector sum is not closed, the central-sector projection kills both
orders and `q_c` is not a supplied readout value.

## Exact Support Theorem

On the supplied closed central-sector surface,

```text
q_c(A,B,C) = a_A b_B - b_A a_B mod 3.
```

Swapping the first two staples reverses the oriented cocycle:

```text
q_c(B,A,C) = -q_c(A,B,C) mod 3.
```

Therefore a central phase character

```text
chi_m(q_c) = omega^(m q_c),     m in {1,2}
```

is the exact finite odd-branch-sensitive slot: orientation reversal conjugates
`chi_m`, its real part is even, and its imaginary part changes sign. Real
class weights can see only the even part. A complex phase character is the
first finite object in this supplied central sector that distinguishes the
two oriented branches.

## Witness

For

```text
T_+ = (E(1,0), E(0,1), E(2,2)),
T_- = (E(0,1), E(1,0), E(2,2)),
```

the separate and pairwise class signatures match, but

```text
q_c(T_+) = 1,
q_c(T_-) = 2 = -1 mod 3.
```

Thus

```text
Re chi_1(T_+) = Re chi_1(T_-) = -1/2,
Im chi_1(T_+) = - Im chi_1(T_-).
```

This is the finite central-sector analogue of the G3 need for an
odd-branch-sensitive phase-type insertion.

## What This Moves

| Before | After |
|---|---|
| G3 needed an odd-sensitive phase insertion, but the finite SU(3) central-sector role was only implicit. | The supplied central-sector projection has an exact orientation-odd cocycle `q_c` and a nontrivial phase character. |
| Real class-weight evenness and central-sector projection support were separate packets. | They now meet in a checked split: real weights are even, the imaginary part of the supplied character is odd. |
| The phase route could still be described vaguely as "add a phase." | The finite support target is sharper: derive a physical action/source law that supplies this kind of central cocycle character, or its 4D `F cup F` analogue, with coefficient and registration. |

## What Does Not Move

- Theta is not retired.
- The Tier-A registry is not edited.
- No physical SU(3) theta sector is registered.
- No G3 phase source, coefficient, action entry, or physical weighting law is
  supplied.
- No G1 defect-closure or defect-suppression theorem is supplied.
- No G2 physical sector/readout theorem is supplied.
- No G4 gauge/mass theta-bar assembly is supplied.
- No mass-side determinant-channel bridge is supplied.
- No audit status or effective status is changed.

## Remaining Live Routes

1. **Physical G3 phase source.** Derive an action-side or measure-side law that
   supplies the odd-sensitive phase character, or its 4D `F cup F` analogue,
   with a coefficient.
2. **G2 sector/readout registration.** Derive that the central cocycle is
   physical SU(3) record/readout content, not only a supplied finite witness.
3. **G1 defect closure or suppression.** Discipline `dn != 0` before treating
   the closed-branch carrier as physical rather than witness-surface support.
4. **Theta mass-side bridge.** Keep the determinant-channel readout bridge
   separate until the gauge-side phase and sector gates are supplied.
5. **Governance route.** If theorem routes fail, any explicit phase/source or
   sector/readout adoption would need owner governance rather than being
   smuggled in through Record or Admissibility.

## Scope Discipline

This exact support is conditional on the supplied central-sector projection
from Block32. The Record axiom can discipline a readout once record content
exists; it does not create a central-sector cocycle, select a complex
character, provide an action coefficient, or identify the result as the
physical theta gauge sector.

The theorem is also finite and central-sector-scoped. It supports the G3
shape; it does not prove the full 4D continuum or lattice `F cup F` insertion.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/theta_g3_central_sector_phase_character_exact_support_2026_07_04.py
```

Expected close: `FAIL=0`.
