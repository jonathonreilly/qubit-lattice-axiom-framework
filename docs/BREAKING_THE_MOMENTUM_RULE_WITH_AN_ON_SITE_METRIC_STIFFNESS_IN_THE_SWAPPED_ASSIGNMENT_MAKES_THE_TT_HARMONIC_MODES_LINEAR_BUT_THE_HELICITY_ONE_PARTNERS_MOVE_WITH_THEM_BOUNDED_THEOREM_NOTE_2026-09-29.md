---
claim_id: breaking_the_momentum_rule_with_an_on_site_metric_stiffness_in_the_swapped_assignment_makes_the_tt_harmonic_modes_linear_but_the_helicity_one_partners_move_with_them_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: "Probe 15's swapped assignment (metric stored on spin-S slots with S >= 1; exact scalar Gauss law; kinetic terms from Gauss-law-compatible moves) with an added on-site metric stiffness, in specified harmonic comparators: the landed lattice E-H symbol; kinetic forms from the 2^3 integer box kernel of S (U = 1), or isotropic families (alpha: gauge patterns sym(K (x) xi); beta: symmetric curls sym(K x A)); stiffness m^2 |h|^2 or Fierz-Pauli m^2 (|h|^2 - (tr h)^2) in the tensor norm. (A) m^2 |h|^2 commutes with the scalar Gauss law and breaks the momentum-rule strings; for S = 1/2 it is a constant. (B) Box-kernel form, scalar law exact: E-H is positive semidefinite on ker S(q), so the comparator is stable for every m^2 > 0; all five modes of ker S(q) are gapless with omega ~ q, with q -> 0 slopes proportional to m; the modes mix helicities because this form is not covariant. (C) Isotropic forms: clean helicities, and with |h|^2 the q -> 0 speeds obey c1^2 = c0^2/2 + c2^2/4, so the helicity +-1 partners move at no less than half the TT speed whenever the TT modes move; alpha = 0 freezes the helicity-0 partner; a Fierz-Pauli stiffness freezes the helicity-0 partner and keeps the helicity +-1 partners. (D) Both rules soft: exact zone stability needs m^2 > 12 (the conformal eigenvalue -|K|^2 is largest at the zone corner), then every mode is gapped, the smallest gap sqrt(m^2 - 12) at the corner. Pre-registered outcome FAIL. Not shown: states beyond the harmonic comparators; derivative or non-on-site symmetry-breaking terms; one qubit per slot."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - the_incompressible_tensor_pattern_exists_but_isotropy_ties_a_spin_two_fields_helicities_a_positive_models_first_order_graviton_carries_helicity_one_partners_bounded_theorem_note_2026-09-28
  - the_swapped_quantum_link_assignment_metric_diagonal_makes_einstein_hilbert_exactly_invariant_but_the_tt_metric_f_sum_of_gauss_law_compatible_moves_is_bounded_by_q_squared_bounded_theorem_note_2026-09-28
runner: scripts/breaking_the_momentum_rule_with_an_on_site_metric_stiffness_in_the_swapped_assignment_helicity_one_partners_2026_09_29.py
---

# Breaking the momentum rule with an on-site metric stiffness, in the swapped assignment, makes the TT harmonic modes linear, but the helicity-1 partners move with them

**Date:** 2026-09-29
**Type:** bounded_theorem
**Status:** specified harmonic comparators with exact checks; pre-registered;
unaudited. Revised after the first referees. Independent checks are
recorded below.

## In one paragraph

Probe 15 stored the metric on each slot. Its spin-2 (TT) waves came out
slow: frequency ∝ q². A light-cone wave needs the metric to resist being
pushed at long wavelength. The simplest way to give it that is a local
stiffness on each slot, which is how photons become light-like.

It works for the TT waves: they turn linear. But the stiffness breaks the
momentum rule, and the directions that rule used to remove as pure gauge
become physical waves.
- In clean (isotropic) versions, the helicity ±1 partners move at no less
  than half the TT speed whenever the TT waves move.
- The helicity-0 partner is either linear too, or frozen. A Fierz–Pauli-type
  stiffness freezes it.

If the time rule is softened as well, everything becomes massive (gapped).

This needs slots of spin at least 1. For a qubit the stiffness is just a
constant.

## Pre-registration

Written in the probe's scratch file before any check was built.
- **PASS (route open)** if, with the scalar law exact and the momentum rule
  broken by the stiffness, the TT modes turn linear and no other gapless
  mode appears.
- **FAIL (partners)** if the former gauge directions are gapless too.
- The case with both rules soft is recorded either way.

**Outcome: FAIL.** The helicity ±1 partners are gapless in every tested
comparator.

## Prior art

On main:
- the 2026-09-14 tensor note (the stencils; the penalty block);
- the landed lattice E-H symbol (2026-09-24).

Of this PR:
- [probe 15](THE_SWAPPED_QUANTUM_LINK_ASSIGNMENT_METRIC_DIAGONAL_MAKES_EINSTEIN_HILBERT_EXACTLY_INVARIANT_BUT_THE_TT_METRIC_F_SUM_OF_GAUSS_LAW_COMPATIBLE_MOVES_IS_BOUNDED_BY_Q_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-28.md):
  the swapped assignment; its second referee noted that an on-site mass
  gives a bounded χ_h;
- [probe 11](THE_INCOMPRESSIBLE_TENSOR_PATTERN_EXISTS_BUT_ISOTROPY_TIES_A_SPIN_TWO_FIELDS_HELICITIES_A_POSITIVE_MODELS_FIRST_ORDER_GRAVITON_CARRIES_HELICITY_ONE_PARTNERS_BOUNDED_THEOREM_NOTE_2026-09-28.md):
  isotropy ties the helicities' sum rules, 4v₁ = v₂ + 3v₀. C is a concrete
  instance.

External, reference only:
- **Fierz–Pauli massive gravity** (review arXiv:1105.3735): a tuned,
  massive, five-polarisation spectrum, not the gapless one here.
- **Lorentz-violating massive gravity** (Dubovsky, hep-th/0409124): the mode
  count depends on which symmetries remain.
- **Hořava gravity with broken symmetry:** mainly an extra scalar
  (Blas–Pujolàs–Sibiryakov, arXiv:0906.3046).
- **Lattice counterpoints:** Gu and Wen (arXiv:0907.1203); Xu and Hořava
  (arXiv:1003.0009).

## Premises (supplied)

- **The swapped assignment** (probe 15): h = S^z stored, on spin-S slots
  with S ≥ 1; the scalar Gauss law exact; kinetic terms from moves in ker S.
- **Two stiffnesses, per slot, in the tensor norm:** m²|h|², and the
  Fierz–Pauli form m²(|h|² − (tr h)²).
- **Kinetic forms:**
  - the 2³ integer box kernel of S (U = 1). This is a basis-dependent Gram
    sum and not cubic-covariant.
  - isotropic families: gauge patterns sym(K ⊗ ξ), weight α; symmetric
    curls sym(K × A), weight β.

## A — the stiffness breaks the momentum rule (check A)

- m²|h|² is diagonal, so it commutes with the scalar Gauss law.
- It changes under every sampled gauge shift, so it breaks the momentum
  strings.
- For S = ½, (S^z)² = ¼, so the stiffness is a constant. Slots of spin at
  least 1 are needed.

## B — box-kernel form: five gapless modes (check B)

- E-H is positive semidefinite on ker S(q); its eigenvalues there are
  (0, 0, 0, K², K²). So the comparator is stable for every m² > 0.
- All five modes of ker S(q) are gapless with ω ∝ q: fitted exponents
  1.00 ± 0.02 on the axis, the body diagonal and a generic direction.
- The q → 0 slopes scale as m (m² = 1, 4, 16), so a stronger stiffness gaps
  none.
- This kinetic form is not covariant, so its five modes mix helicities. The
  count is what this form shows.

## C — isotropic forms: the helicity-1 partners move with the TT modes (check C)

With isotropic kinetic forms the modes carry clean helicities (purity
> 0.999). The speeds below are per unit m.

| Kinetic form (α, β) | Stiffness | c₀ (helicity 0) | c₁ (helicity ±1) | c₂ (TT) |
| --- | --- | --- | --- | --- |
| (1, 1) | \|h\|² | 1.000 | 0.866 | 1.000 |
| (0, 1) | \|h\|² | 0 (frozen) | 0.500 | 1.000 |
| (1, 0) | \|h\|² | 1.000 | 0.707 | 0 (frozen) |
| (2, 0.5) | \|h\|² | 1.414 | 1.061 | 0.707 |
| (1, 1) | Fierz–Pauli | 0 (frozen) | 0.866 | 1.000 |
| (2, 0.5) | Fierz–Pauli | 0 (frozen) | 1.061 | 0.707 |

- With |h|², **c₁² = c₀²/2 + c₂²/4** in every case. So c₁ ≥ c₂/2: the
  helicity ±1 partners move at no less than half the TT speed whenever the
  TT modes move. This is probe 11's identity in a concrete model.
- The helicity-0 partner is frozen when there are no gauge-pattern moves
  (α = 0), and, for Fierz–Pauli, for every α tested. On ker S the scalar law
  itself makes K̂K̂ : h = tr h, which is what freezes it.

## D — both rules soft: everything gapped (check D)

- With single-slot moves the conformal eigenvalue is −|K|². It is largest
  in magnitude at the zone corner, where |K|² = 12.
- So exact stability over the zone needs m² > 12.
- Then every mode is gapped. The smallest gap is √(m² − 12), at the
  corner. As q → 0, ω → m.

## What this means

In the swapped assignment's harmonic comparators:

| Momentum rule | Scalar rule | TT modes | Partners |
| --- | --- | --- | --- |
| exact | exact | ω ∝ q² (probe 15) | none |
| broken by an on-site stiffness | exact | ω ∝ q | helicity ±1 gapless (c₁ ≥ c₂/2); helicity 0 linear or frozen |
| broken | soft (m² > 12) | gapped | gapped |

A linear TT mode without partners appeared, among the comparators tested,
only in the landed comparator with continuous variables. That comparator is
itself unaudited conditional support. This note does not show that no
other finite-slot model could do it.

## No-Go Discipline Gate

The bounded negative claim: in the specified comparators, breaking the
momentum rule by an on-site stiffness, with the scalar law exact, leaves the
helicity ±1 partners gapless alongside the linear TT modes.

- **N1 — attack routes.** Each route, with its honesty marker.
  1. *A larger stiffness gaps the partners.* ATTEMPTED (B: m² = 1, 4, 16).
     The slopes scale as m and no mode gaps. Fails.
  2. *An on-site stiffness that spares the gauge directions.* ATTEMPTED
     (argument and C). The gauge tensors sym(K ⊗ ξ), over all K and ξ, span
     all symmetric tensors. So a non-zero on-site form stiffens some gauge
     direction. The Fierz–Pauli form spares exactly the helicity-0 one on
     ker S, not the ±1. Fails for ±1.
  3. *Removing the partners' kinetic weight.* ATTEMPTED (C). With α = 0 the
     helicity-0 partner is frozen. But the ±1 partners draw weight from the
     same symmetric-curl moves as the TT modes (c₁ ≥ c₂/2). Fails for ±1.
  4. *Softening the scalar law too.* ATTEMPTED (D): everything is gapped,
     TT included. It gives no light-cone TT mode.
  5. *Another move set.* ATTEMPTED (B and C: the box kernel and six
     isotropic forms). Under the exact scalar law the kinetic weight is
     O(q²) or smaller (probe 15 B). A kinetic null direction is a frozen
     coordinate, not a gap. The ±1 partners are gapless in every set
     tested.

  **Open routes:**
  - (i) derivative or non-on-site symmetry-breaking terms;
  - (ii) states beyond the harmonic comparators;
  - (iii) partners that do not couple to matter.
- **N2 — pairwise table, with directions.**
  - W1: the exact scalar Gauss law.
  - W2: an on-site stiffness (|h|² or Fierz–Pauli).
  - W3: the harmonic comparators.
  - W4: S ≥ 1 slots.

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no: the Gauss law does not supply a stiffness | no: a stiffness does not impose the law | independent |
  | W1, W3 | no | no: comparators exist without the law (D) | independent |
  | W1, W4 | no | no | independent |
  | W2, W3 | no | no: comparators exist without the stiffness (probe 15) | independent |
  | W2, W4 | no | yes: for S = ½ the stiffness is a constant, so W2 needs W4 | W2 requires W4 |
  | W3, W4 | no | no | independent |

- **N3 — hidden-wall scan.** The scan hits, and how each is classified:
  - "box kernel": promoted, and tested against the isotropic forms in C;
  - "U = 1": a normalisation that only scales speeds;
  - "sampled": D now uses the exact corner value;
  - "spin S ≥ 1": made explicit as W4.
- **N4 — residual matching.**

  | Citation (path:line) | Residual attacked | Status here | Match |
  | --- | --- | --- | --- |
  | docs/THE_SWAPPED_QUANTUM_LINK_ASSIGNMENT_METRIC_DIAGONAL_MAKES_EINSTEIN_HILBERT_EXACTLY_INVARIANT_BUT_THE_TT_METRIC_F_SUM_OF_GAUSS_LAW_COMPATIBLE_MOVES_IS_BOUNDED_BY_Q_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-28.md:132 | Gauss-law moves with a zeroth moment | used in route 5 | yes |
  | docs/THE_INCOMPRESSIBLE_TENSOR_PATTERN_EXISTS_BUT_ISOTROPY_TIES_A_SPIN_TWO_FIELDS_HELICITIES_A_POSITIVE_MODELS_FIRST_ORDER_GRAVITON_CARRIES_HELICITY_ONE_PARTNERS_BOUNDED_THEOREM_NOTE_2026-09-28.md:137 | isotropic helicity sum rules | instanced by C | yes |

  Both are unaudited parents.
- **N5 — rhetoric audit.**

  | Phrase | per_element | per_site | per_mode | per_block | lattice_wide |
  | --- | --- | --- | --- | --- | --- |
  | "helicity-1 partners move" | the isotropic families' patterns | not applicable (Fourier comparators) | five modes, six isotropic forms, one direction at q = 10⁻³ | the box kernel | specified comparators only |
  | "everything gapped" | not applicable | not applicable | the zone corner and six momenta | single-slot moves | the exact threshold m² > 12 is lattice-wide |

- **N6 — primitive scan.** None invoked. The spin slots are supplied, and
  the Qubit axiom's one qubit per site does not carry the stiffness.
- **N7 — steelman, in a hostile reviewer's voice.** "Only on-site
  stiffnesses were tried. A derivative stiffness, or one depending on a
  second field, might lift the helicity ±1 partners while the TT modes
  stay linear, as symmetry-protected Lorentz-violating massive gravity
  does (Dubovsky, hep-th/0409124). The terminal obligation is a
  classification of symmetry-breaking terms by the partners they keep,
  which is not attempted." This is convincing against a broad no-go, so
  none is claimed.
- **N8 — cross-cycle echo.**

  | Prior wall | Retired? | Mechanism | Applies here? |
  | --- | --- | --- | --- |
  | probe 11's partner theorem (compressible route) | no | an incompressible TT channel | no: here the channel is compressible (on-site stiffness) |
  | probe 15's q² bound | circumvented by breaking the momentum rule | the on-site stiffness | yes, at the cost of partners |
  | the landed penalty block | no | the exact scalar law | yes, in B and C; D shows the soft case |

- **Outcome.** PASS as scoped. The pre-registered outcome is FAIL.

## Independent checks

- **gpt-5.6-sol (other vendor), first round: STANDS WITH CORRECTIONS.** Its
  findings, and how this version answers each:
  1. The box-kernel modes are mixed. The labels now come from isotropic
     forms (C).
  2. The stiffness is trivial for a qubit. S ≥ 1 is now stated (A, W4).
  3. D's threshold and gap are exact, not sampled: m² > 12, gap
     √(m² − 12).
  4. The m-scaling holds for the q → 0 slopes only. Stated.
  5. N1 routes 2, 3 and 5 overclaimed. Rewritten: the span argument,
     "O(q²) or smaller", and frozen coordinates.
  6. The gate. Rewritten.
  7. The synthesis and prior art. The table no longer claims coverage, and
     Fierz–Pauli, Dubovsky, Blas–Pujolàs–Sibiryakov, Gu–Wen and Xu–Hořava
     are added.
- **Fable check (same family): STANDS WITH CORRECTIONS.**
  - It verified A–C with its own conventions and gave the isotropic speed
    relation, which is reproduced in C with independent normalisations.
  - Also from it: the Fierz–Pauli freezing of helicity 0, the exact
    threshold 12, and the non-covariance of the box-kernel form. All
    applied.
- Second rounds: pending.

## Reproduction

`python3 scripts/breaking_the_momentum_rule_with_an_on_site_metric_stiffness_in_the_swapped_assignment_helicity_one_partners_2026_09_29.py`
prints 4 checks, A–D, the N5 lines and TOTAL, in about 5 s. The canonical
cache is at
logs/runner-cache/breaking_the_momentum_rule_with_an_on_site_metric_stiffness_in_the_swapped_assignment_helicity_one_partners_2026_09_29.txt.
