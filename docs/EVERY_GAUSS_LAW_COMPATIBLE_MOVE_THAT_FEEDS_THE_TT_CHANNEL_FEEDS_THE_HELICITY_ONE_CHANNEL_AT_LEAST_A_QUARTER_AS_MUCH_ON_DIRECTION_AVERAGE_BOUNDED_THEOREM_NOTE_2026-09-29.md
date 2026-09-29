---
claim_id: every_gauss_law_compatible_move_that_feeds_the_tt_channel_feeds_the_helicity_one_channel_at_least_a_quarter_as_much_on_direction_average_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: "Probe 15's swapped assignment (metric stored; exact scalar Gauss law); moves r with S r = 0, fixed range. Their O(q^2) kinetic form is fixed by first moments: r_hat(q) = -i M(q) + O(q^2). (A) The lattice first moments (integer kernel of S on a 2^3 box) are exactly the 8-dimensional family M(q) = sym(q (x) xi) + sym(q x A), xi in R^3, A symmetric traceless. (B) Exact sphere quadrature: <|M_+-1|^2> = (1/4) <|M_TT|^2> + (1/3)|xi|^2 with no xi-A cross term; so for any move family the direction-averaged helicity +-1 kinetic weight is at least a quarter of its TT weight, and every nonzero first moment is helicity +-1 visible. (C) Lattice families (box kernel, 200 random integer combinations, 30 random sub-families) meet the bound (min exactly 1/4). (D) The helicity +-1 directions sym(qhat (x) e), e _|_ qhat, span the traceless symmetric tensors, so an on-site positive stiffness that stiffens a TT direction stiffens helicity +-1 directions on an open set. (E) In harmonic comparators with random non-covariant 3-move families and an |h|^2 stiffness, every family has linear modes with helicity +-1 weight in some sampled direction. Hence breaking the momentum rule by an on-site stiffness to make the TT modes linear also makes helicity +-1 partners gapless and linear on an open set of directions. Registered after the scratch computation. Not shown: O(q^3) kinetic terms, states beyond the harmonic comparators, non-on-site symmetry breaking."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - the_incompressible_tensor_pattern_exists_but_isotropy_ties_a_spin_two_fields_helicities_a_positive_models_first_order_graviton_carries_helicity_one_partners_bounded_theorem_note_2026-09-28
  - the_swapped_quantum_link_assignment_metric_diagonal_makes_einstein_hilbert_exactly_invariant_but_the_tt_metric_f_sum_of_gauss_law_compatible_moves_is_bounded_by_q_squared_bounded_theorem_note_2026-09-28
  - breaking_the_momentum_rule_with_an_on_site_metric_stiffness_in_the_swapped_assignment_makes_the_tt_harmonic_modes_linear_but_the_helicity_one_partners_move_with_them_bounded_theorem_note_2026-09-29
runner: scripts/every_gauss_law_compatible_move_that_feeds_the_tt_channel_feeds_helicity_one_2026_09_29.py
---

# Every Gauss-law-compatible move that feeds the TT channel feeds the helicity-1 channel, at least a quarter as much on direction average

**Date:** 2026-09-29
**Type:** bounded_theorem
**Status:** an exact lemma (quadrature) with lattice checks; registered
after the scratch computation; unaudited. Independent checks are recorded
below.

## In one paragraph

In probe 18, the spin-2 (TT) waves became light-like when a local stiffness
broke the momentum rule, and the helicity ±1 partners moved too. That was
shown for isotropic move sets.

This probe shows it holds for every move set that respects the time rule.
Each move's first moment either shifts the metric like a gauge change or
curls it. Averaged over directions, the curling part always feeds the
helicity ±1 channel exactly a quarter as much as the spin-2 channel, and the
gauge part feeds only helicity ±1 (and 0).

So a move set that gives the spin-2 waves any kinetic weight gives the ±1
partners kinetic weight too, in an open set of directions. And a local
stiffness that holds the spin-2 waves also holds the ±1 directions. The
partners are then light-like waves as well.

## Registration

Written in the probe's scratch file **after** the scratch computation that
found the ¼. So it fixes how the outcome is read; it is not independent
evidence.
- **PASS (route open)** if some move family gives TT kinetic weight at
  O(q²) while its helicity ±1 weight vanishes in every direction.
- **FAIL** if the helicity ±1 weight is bounded below by a fixed fraction of
  the TT weight for every family.

**Outcome: FAIL, with fraction ¼.**

## Prior art

On main:
- the 2026-09-14 tensor note (the stencils, the moment lemma).

Of this PR:
- **[probe 11](THE_INCOMPRESSIBLE_TENSOR_PATTERN_EXISTS_BUT_ISOTROPY_TIES_A_SPIN_TWO_FIELDS_HELICITIES_A_POSITIVE_MODELS_FIRST_ORDER_GRAVITON_CARRIES_HELICITY_ONE_PARTNERS_BOUNDED_THEOREM_NOTE_2026-09-28.md):**
  in an isotropic model a spin-2 field's sum rules obey v₁ ≥ v₂/4 (T2);
  cubic forms evade that only with direction dependence (T6). This note is
  the kinetic-channel version for any move family, by direction averaging.
- **[probe 15](THE_SWAPPED_QUANTUM_LINK_ASSIGNMENT_METRIC_DIAGONAL_MAKES_EINSTEIN_HILBERT_EXACTLY_INVARIANT_BUT_THE_TT_METRIC_F_SUM_OF_GAUSS_LAW_COMPATIBLE_MOVES_IS_BOUNDED_BY_Q_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-28.md):**
  the 8-dimensional first-moment space (B).
- **[probe 18](BREAKING_THE_MOMENTUM_RULE_WITH_AN_ON_SITE_METRIC_STIFFNESS_IN_THE_SWAPPED_ASSIGNMENT_MAKES_THE_TT_HARMONIC_MODES_LINEAR_BUT_THE_HELICITY_ONE_PARTNERS_MOVE_WITH_THEM_BOUNDED_THEOREM_NOTE_2026-09-29.md):**
  the isotropic instance, c₁² = c₀²/2 + c₂²/4; its Fable referee noted
  v₁ = v₂/4 for the curl family.

External, reference only: Schur's lemma, which forbids spin-1/spin-2
cross terms in rotation-averaged forms.

## Premises (supplied)

- **The swapped assignment** (probe 15): metric stored, the scalar Gauss
  law exact.
- **Moves.** Patterns r with S r = 0, fixed range. Their kinetic
  contribution at O(q²) is |w·M(q)|² for an observable w.
- **Helicity channels.** Taken about q̂: TT (±2), ±1 (the directions
  sym(q̂ ⊗ e), e ⊥ q̂) and 0.

## A — the first-moment space (check A)

- The first moments of the 14 integer kernel moves on a 2³ box fit exactly
  (residual 1e-14) to M(q) = sym(q ⊗ ξ) + sym(q × A), with ξ ∈ ℝ³ (gauge
  patterns) and A symmetric traceless (symmetric curls).
- The fit coefficients have rank 8: the lattice realises the whole space.

## B — the lemma (check B, exact quadrature)

With product Gauss–Legendre × uniform quadrature, exact for the degrees
involved, the direction averages are:
- ⟨|M_TT|²⟩ = 0.4 |A|², with no contribution from ξ;
- ⟨|M_±1|²⟩ = 0.1 |A|² + (1/3)|ξ|², with no ξ–A cross term (Schur).

So, per unit of first moment:
- `⟨|M_±1|²⟩ = ¼ ⟨|M_TT|²⟩ + ⅓ |ξ|²`, exactly.
- For any move family (a sum over moves), the direction-averaged helicity
  ±1 kinetic weight is at least ¼ of the TT weight.
- The ±1 form is positive definite on all 8 dimensions, so every nonzero
  first moment is ±1-visible in some direction. Its ±1 weight is a
  polynomial in q̂, so it is nonzero on an open set.

## C — lattice families (check C)

With lattice first moments and the exact quadrature:
- the box kernel: ratio 0.81;
- 200 random integer combinations and 30 random 3-move sub-families:
  minimum exactly 0.2500, reached by pure-curl combinations.

## D — on-site stiffnesses reach the ±1 directions (check D)

- The ±1 directions sym(q̂ ⊗ e), with e ⊥ q̂, span all five traceless
  symmetric tensors as q̂ varies (rank 5 from 60 samples).
- So an on-site positive form that stiffens any TT direction is nonzero on
  ±1 directions for an open set of q̂.

## E — harmonic check (check E)

- Random non-covariant 3-move families, with an |h|² stiffness.
- Every family with linear TT-carrying modes also has, in some sampled
  direction, a linear mode with helicity ±1 weight (0.70–0.91).
- In a given direction a family may show only two linear modes. The lemma
  promises an open set of directions, not every direction.

## What this means

On finite slots with the time rule exact, making the spin-2 waves
light-like by breaking the momentum rule with a local stiffness always
brings light-like helicity ±1 partners. Their kinetic weight is at least a
quarter of the spin-2 weight on average.

This closes probe 18's route "another move set", at the level of first
moments. With probe 15, the swapped assignment's options are:
- exact rules: soft spin-2 waves;
- on-site symmetry breaking: linear spin-2 waves with ±1 partners.

## No-Go Discipline Gate

The bounded negative claim: no Gauss-law-compatible move family feeds the
TT channel at O(q²) without feeding helicity ±1 at no less than a quarter of
its direction-averaged TT weight.

- **N1 — attack routes.** Each route, with its honesty marker.
  1. *Gauge-curl cancellation of the ±1 weight.* ATTEMPTED (B): the ξ–A
     cross term vanishes exactly (Schur). Fails.
  2. *Anisotropic (cubic or non-covariant) weighting of the curl family.*
     ATTEMPTED (B, C): the direction average is exact for every weighting,
     and the random families reach but never go below ¼. Fails.
  3. *Lattice first moments outside the continuum family.* ATTEMPTED (A):
     residual 1e-14, rank 8. Fails.
  4. *An on-site stiffness that spares the ±1 directions.* ATTEMPTED (D):
     the ±1 directions span the traceless tensors. Fails for stiffnesses
     that stiffen TT.
  5. *Small families that avoid ±1 in the tested directions.* ATTEMPTED (E):
     some directions show no ±1 mode, but every family shows one somewhere,
     as the lemma requires. Fails.

  **Open routes:**
  - (i) O(q³) kinetic terms, i.e. families with zero first moments. They
    make TT soft anyway (probe 15).
  - (ii) non-on-site symmetry breaking;
  - (iii) states beyond the harmonic comparators.
- **N2 — pairwise table, with directions.**
  - W1: the exact scalar Gauss law.
  - W2: fixed range (first moments control O(q²)).
  - W3: an on-site stiffness (for the corollary).

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no: infinite-range Gauss-law terms exist | no: fixed-range terms can break the law | independent |
  | W1, W3 | no | no: a stiffness does not impose the law | independent |
  | W2, W3 | no | no | independent |

  The lemma (B) uses W1 and W2; the corollary adds W3.
- **N3 — hidden-wall scan.** The scan hits, and how each is classified:
  - "first moments": explicit (W2);
  - "quadrature": exact for the polynomial degrees used, not a sampling;
  - "registered after": stated;
  - "box": the lattice realisation (A) is complete (rank 8), so the lemma
    covers all first moments.
- **N4 — residual matching.**

  | Citation (path:line) | Residual attacked | Residual status here | Match |
  | --- | --- | --- | --- |
  | docs/THE_INCOMPRESSIBLE_TENSOR_PATTERN_EXISTS_BUT_ISOTROPY_TIES_A_SPIN_TWO_FIELDS_HELICITIES_A_POSITIVE_MODELS_FIRST_ORDER_GRAVITON_CARRIES_HELICITY_ONE_PARTNERS_BOUNDED_THEOREM_NOTE_2026-09-28.md:137 | v₁ ≥ v₂/4 needs isotropy | extended to any move family, by direction averaging | yes |
  | same note:229 | cubic forms evade the isotropy identity | only pointwise; the average holds (B) | yes |
  | docs/THE_SWAPPED_QUANTUM_LINK_ASSIGNMENT_METRIC_DIAGONAL_MAKES_EINSTEIN_HILBERT_EXACTLY_INVARIANT_BUT_THE_TT_METRIC_F_SUM_OF_GAUSS_LAW_COMPATIBLE_MOVES_IS_BOUNDED_BY_Q_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-28.md:134 | the 8-dimensional first-moment space | re-verified (A) | yes |
  | docs/BREAKING_THE_MOMENTUM_RULE_WITH_AN_ON_SITE_METRIC_STIFFNESS_IN_THE_SWAPPED_ASSIGNMENT_MAKES_THE_TT_HARMONIC_MODES_LINEAR_BUT_THE_HELICITY_ONE_PARTNERS_MOVE_WITH_THEM_BOUNDED_THEOREM_NOTE_2026-09-29.md:108 | helicity-1 partners only for isotropic forms | extended to all move families | yes |

  All are unaudited parents.
- **N5 — rhetoric audit.**

  | Phrase | per_element | per_site | per_mode | per_block | lattice_wide |
  | --- | --- | --- | --- | --- | --- |
  | "at least a quarter" | each move's first moment (A) | the scalar rule at every site touching the box | the quadrature directions | 231 families | exact (quadrature over the whole first-moment space) |
  | "partners gapless" | not applicable | not applicable | five modes, 64 family–direction pairs | random 3-move families | on an open set of directions, not all |

- **N6 — primitive scan.** None invoked. The spin slots are supplied.
- **N7 — steelman, in a hostile reviewer's voice.** "A family with zero
  first moments has no O(q²) weight in any channel. Symmetry breaking that
  is not on-site (derivative, or through another field) could stiffen TT
  while leaving the ±1 directions soft, as symmetry-protected
  Lorentz-violating massive gravity does (Dubovsky, hep-th/0409124). The
  terminal obligation is a classification of non-on-site breaking terms,
  not attempted." Convincing against a broader claim, so the corollary is
  restricted to on-site stiffnesses.
- **N8 — cross-cycle echo.**

  | Prior wall | Retired? | Mechanism | Applies here? |
  | --- | --- | --- | --- |
  | probe 11's isotropic partner identity | extended, not retired | direction averaging | yes |
  | probe 18's isotropic partner result | extended, not retired | the same | yes |

- **Outcome.** PASS as scoped. The registered outcome is FAIL, with
  fraction ¼.

## Independent checks

Pending.

## Reproduction

`python3 scripts/every_gauss_law_compatible_move_that_feeds_the_tt_channel_feeds_helicity_one_2026_09_29.py`
prints 5 checks, A–E, the N5 lines and TOTAL, in about 6 s. The canonical
cache is at
logs/runner-cache/every_gauss_law_compatible_move_that_feeds_the_tt_channel_feeds_helicity_one_2026_09_29.txt.
