---
claim_id: breaking_the_momentum_rule_with_an_on_site_metric_stiffness_in_the_swapped_assignment_makes_the_tt_harmonic_modes_linear_but_three_partner_modes_turn_linear_too_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: "Probe 15's swapped assignment (metric stored, h = S^z; exact scalar Gauss law; kinetic terms from Gauss-law-compatible moves) with an added on-site isotropic metric stiffness m^2 |h|^2 (tensor norm), in specified harmonic comparators (the 2^3 integer box kernel of S as moves, U = 1, the landed lattice E-H symbol). (A) The stiffness commutes with the scalar Gauss law and breaks the momentum-rule strings. (B) Scalar law exact, momentum rule broken: E-H is positive semidefinite on ker S(q), so the comparator is stable for every m^2 > 0; all five modes of ker S(q) (the two TT directions and the three former gauge directions, which carry helicity +-1 and 0) are gapless with omega proportional to q (fitted exponents 1.00 +- 0.02 on axis, body and a generic direction), and the speeds scale as m (omega/(m K) independent of m^2 = 1, 4, 16). (C) Both rules soft (single-slot moves, tensor-normalised): stability over the zone needs m^2 above the largest conformal instability of E-H (about 11.97, sampled); then every mode is gapped, omega -> m. Pre-registered outcome FAIL (partners). Not shown: states beyond the harmonic comparators; other symmetry-breaking terms; any encoding other than the swapped one; one qubit per site."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - the_incompressible_tensor_pattern_exists_but_isotropy_ties_a_spin_two_fields_helicities_a_positive_models_first_order_graviton_carries_helicity_one_partners_bounded_theorem_note_2026-09-28
  - the_swapped_quantum_link_assignment_metric_diagonal_makes_einstein_hilbert_exactly_invariant_but_the_tt_metric_f_sum_of_gauss_law_compatible_moves_is_bounded_by_q_squared_bounded_theorem_note_2026-09-28
runner: scripts/breaking_the_momentum_rule_with_an_on_site_metric_stiffness_in_the_swapped_assignment_2026_09_29.py
---

# Breaking the momentum rule with an on-site metric stiffness, in the swapped assignment, makes the TT harmonic modes linear, but three partner modes turn linear too

**Date:** 2026-09-29
**Type:** bounded_theorem
**Status:** specified harmonic comparators with exact checks; pre-registered;
unaudited. Independent checks are recorded below.

## In one paragraph

Probe 15 stored the metric on each slot. Its spin-2 (TT) waves came out
slow: frequency ∝ q². A light-cone wave needs the metric to resist being
pushed at long wavelength (a bounded metric susceptibility). The simplest
way to give it that is a local stiffness on each slot, which is the
mechanism that makes photons light-like.

It works for the TT waves: they become linear, ω ∝ q. But the stiffness
breaks the momentum rule. The three directions that the momentum rule used
to remove as pure gauge then turn into physical waves, also linear. These
are the helicity ±1 and 0 partners of probe 11.

If the time rule is softened as well, everything becomes massive (gapped).

## Pre-registration

Written in the probe's scratch file before any check was built.
- **PASS (route open)** if, with the scalar law exact and the momentum rule
  broken by the stiffness, the TT modes turn linear and no other gapless
  mode appears.
- **FAIL (partners)** if the TT modes turn linear but the former gauge
  directions are gapless too.
- The case with both rules soft is recorded either way.

**Outcome: FAIL.**

## Prior art

On main:
- the 2026-09-14 tensor note (the stencils; the penalty block);
- the landed lattice E-H symbol (2026-09-24).

Of this PR:
- probe 15 (the swapped assignment; its second referee pointed out that an
  on-site mass gives a bounded χ_h);
- probe 11 (a first-order spin-2 mode carries helicity-1 partners,
  4v₁ = v₂ + 3v₀).

External, reference only: Fierz–Pauli and Lorentz-violating massive
gravity, where breaking diffeomorphisms makes the extra polarisations
physical.

## Premises (supplied)

- **The swapped assignment** (probe 15): h = S^z stored, the scalar Gauss
  law exact, kinetic terms from the integer box kernel of S (U = 1).
- **The stiffness:** m²|h|² per slot, in the tensor norm. It is diagonal,
  local and isotropic.
- **The harmonic comparators:** the landed lattice E-H symbol with the
  stiffness added.

## A — the stiffness breaks the momentum rule (check A)

- m²|h|² is diagonal, so it commutes with the scalar Gauss law.
- It changes under every sampled gauge shift (by at least 1.00 at m² = 1),
  so it does not commute with the momentum-rule strings.

## B — scalar law exact, momentum rule broken: five linear modes (check B)

- The physical space is ker S(q), 5-dimensional. It is the two TT
  directions plus the three former gauge directions sym(K ⊗ ξ), which lie
  inside ker S(q) and carry helicity ±1 and 0.
- E-H is positive semidefinite on ker S(q), so the comparator is stable for
  every m² > 0.
- All five modes are gapless, with ω ∝ q: fitted exponents 1.00 ± 0.02 on
  the axis, the body diagonal and a generic direction.
- The speeds scale as m. ω/(mK) is the same at m² = 1, 4 and 16, so a
  stronger stiffness speeds every mode up and gaps none.
- Probe 15's case with both rules exact has two modes, with ω ∝ q². Here
  three partners have joined them.
- The box-kernel moves are not isotropic, so the five modes mix helicities.
  The count is what is robust.

## C — both rules soft: everything gapped (check C)

- With single-slot moves (the scalar law soft), E-H's conformal mode is
  negative, down to about −11.97 over the zone (sampled).
- Stability needs m² above that. At m² = 13 every mode is gapped, and
  ω → m as q → 0.

## What this means

For the swapped assignment in the harmonic comparators, three choices
cover the cases tested:

| Momentum rule | Scalar rule | TT modes | Other modes |
| --- | --- | --- | --- |
| exact | exact | ω ∝ q² (probe 15) | none |
| broken by an on-site stiffness | exact | ω ∝ q | three partners (helicity ±1, 0), ω ∝ q |
| broken | soft | gapped | all gapped |

Einstein's graviton needs the first row's content (only TT, both rules
exact) with the second row's speed (ω ∝ q). In the tested comparators, the
comparator with continuous variables (the landed one) is the only one that
does both.

This matches probe 11: a first-order spin-2 mode carries helicity-1
partners unless the momentum rule removes them.

## No-Go Discipline Gate

The bounded negative claim: in the specified comparators, breaking the
momentum rule by an on-site stiffness, with the scalar law exact, gives
three gapless partner modes alongside the linear TT modes.

- **N1 — attack routes.** Five distinct routes, all ATTEMPTED here.
  1. *A larger stiffness gaps the partners.* Attempted in B (m² = 1, 4, 16):
     the speeds scale as m and no mode gaps. Fails.
  2. *A stiffness acting only on TT directions.* Attempted as an argument.
     An on-site stiffness is q-independent. To stiffen TT(q̂) for every q̂ it
     must be positive on their span, which is all traceless symmetric
     tensors, and that includes the traceless parts of the gauge
     directions. Fails for on-site stiffnesses.
  3. *Giving the partners an O(1) kinetic term, to gap them.* Attempted
     through probe 15's check B: an O(1) kinetic term needs moves with a
     nonzero zeroth moment along gauge directions, which the exact scalar
     law forbids. With no gauge-direction moves at all, the partners are
     frozen (ω = 0), not gapped. Fails.
  4. *Softening the scalar law too.* Attempted in C: everything is gapped,
     TT included. It does not give a light-cone TT mode.
  5. *Different moves (another isotropy).* Attempted as an argument: any
     move set compatible with the Gauss law gives O(q²) kinetic weight on
     gauge directions (first moments) or none. So the partners are linear
     or frozen, never gapped. Illustrated by the box kernel only.

  **Open routes:**
  - (i) other symmetry-breaking terms (derivative stiffnesses);
  - (ii) states beyond the harmonic comparators;
  - (iii) partners that decouple from matter (a coupling question, not a
    spectrum one).
- **N2 — pairwise table.**
  - W1: the exact scalar Gauss law.
  - W2: an on-site isotropic stiffness.
  - W3: the harmonic comparators.

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no | no | independent |
  | W1, W3 | no | no | independent |
  | W2, W3 | no | no | independent |

- **N3 — hidden conditions.** The box-kernel move set (not isotropic); the
  isotropic on-site stiffness; U = 1; the sampled stability threshold in C.
- **N4 — residual matching.**

  | Citation | Residual attacked | Status here | Match |
  | --- | --- | --- | --- |
  | [probe 15](THE_SWAPPED_QUANTUM_LINK_ASSIGNMENT_METRIC_DIAGONAL_MAKES_EINSTEIN_HILBERT_EXACTLY_INVARIANT_BUT_THE_TT_METRIC_F_SUM_OF_GAUSS_LAW_COMPATIBLE_MOVES_IS_BOUNDED_BY_Q_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-28.md), check B | zero zeroth moments of Gauss-law moves | used in route 3 | yes |
  | [probe 11](THE_INCOMPRESSIBLE_TENSOR_PATTERN_EXISTS_BUT_ISOTROPY_TIES_A_SPIN_TWO_FIELDS_HELICITIES_A_POSITIVE_MODELS_FIRST_ORDER_GRAVITON_CARRIES_HELICITY_ONE_PARTNERS_BOUNDED_THEOREM_NOTE_2026-09-28.md), T5 | a compressible graviton without partners | consistent with B | yes |

  Both are unaudited parents.
- **N5 — rhetoric audit.**

  | Phrase | per_element | per_site | per_mode | per_block | lattice_wide |
  | --- | --- | --- | --- | --- | --- |
  | "three partners turn linear" | not applicable (a Fourier-space comparator) | the stiffness under 30 gauge patterns (A) | five modes, three directions, four momenta | the box kernel as moves | specified comparators only; no state tested |
  | "everything gapped" | not applicable | not applicable | lowest mode, two directions, three momenta | single-slot moves | the stability threshold is sampled over the zone |

- **N6 — primitive scan.** None invoked. The spin slots are supplied.
- **N7 — steelman.** A derivative stiffness, or strong correlations, might
  lift the partners while the TT modes stay linear. Or the partners might
  be invisible to matter. Open; not refuted here.
- **N8 — cross-cycle echo.**
  - Probe 11's partner theorem: reproduced in a concrete model.
  - Massive-gravity lore (extra polarisations when diffeomorphisms break):
    consistent, reference only.
- **Outcome.** PASS as scoped. The pre-registered outcome is FAIL.

## Independent checks

Pending.

## Reproduction

`python3 scripts/breaking_the_momentum_rule_with_an_on_site_metric_stiffness_in_the_swapped_assignment_2026_09_29.py`
prints 3 checks, the N5 lines and TOTAL, in about 2 s. The canonical cache
is at
logs/runner-cache/breaking_the_momentum_rule_with_an_on_site_metric_stiffness_in_the_swapped_assignment_2026_09_29.txt.
