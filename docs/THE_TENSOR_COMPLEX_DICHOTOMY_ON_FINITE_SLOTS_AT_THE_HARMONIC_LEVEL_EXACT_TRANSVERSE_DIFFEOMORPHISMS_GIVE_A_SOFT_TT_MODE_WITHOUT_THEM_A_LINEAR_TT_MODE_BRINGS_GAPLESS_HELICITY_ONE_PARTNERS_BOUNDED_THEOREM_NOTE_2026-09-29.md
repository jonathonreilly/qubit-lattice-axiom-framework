---
claim_id: the_tensor_complex_dichotomy_on_finite_slots_at_the_harmonic_level_exact_transverse_diffeomorphisms_give_a_soft_tt_mode_without_them_a_linear_tt_mode_brings_gapless_helicity_one_partners_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: "The landed tensor complex with finite slots, local (finite-range, analytic-symbol) harmonic models, the scalar (time) rule exact, and the two storage assignments of probes 10/14 (momentum stored, DeWitt kinetic term) and 15 (metric stored, kinetic terms from Gauss-law-compatible moves). (i) If every transverse linearised diffeomorphism (shift h -> h + G^T curl zeta) is an exact symmetry, the TT harmonic mode is soft in both assignments: momentum stored, the invariant moves (curl(G mu) = 0) have pure-trace zeroth moments and TT-invisible first moments (3^3 box), so the TT potential is O(q^4); metric stored, the transverse shifts' leading symbols sym(q (x) (q x zeta)) span the traceless tensors, so an invariant local potential has X(0) = 0 on traceless tensors and the TT stiffness is O(q^2), against O(q^2) kinetic weight. (ii) If no transverse diffeomorphism is exact, a TT mode linear in every direction forces gapless helicity +-1 modes, linear on an open set of directions, in both assignments: the TT directions over all qhat span the traceless tensors (so a q^0 TT stiffness reaches helicity +-1, or its absence leaves them ungapped), and over all 18 first-moment dimensions the direction-averaged helicity +-1 weight is at least 1/4 of the TT weight (exact quadrature, Schur complement); the DeWitt form is positive on helicity +-1 directions. A harmonic illustration (momentum stored, momentum rule broken, random local moves) shows five linear modes with both TT and +-1 weight. Pre-registered outcome FAIL. Not shown: intermediate symmetry groups (a proper subgroup of transverse diffeomorphisms), states beyond harmonic comparators, non-local terms, composite metrics, a softened scalar rule, one qubit per site."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - one_qubit_per_slot_under_the_tensor_momentum_rule_an_exact_sum_rule_bounds_the_graviton_channel_by_q4_a_light_cone_mode_needs_an_incompressible_electric_pattern_bounded_theorem_note_2026-09-28
  - the_swapped_quantum_link_assignment_metric_diagonal_makes_einstein_hilbert_exactly_invariant_but_the_tt_metric_f_sum_of_gauss_law_compatible_moves_is_bounded_by_q_squared_bounded_theorem_note_2026-09-28
  - every_gauss_law_compatible_move_that_feeds_the_tt_channel_feeds_the_helicity_one_channel_at_least_a_quarter_as_much_on_direction_average_bounded_theorem_note_2026-09-29
runner: scripts/the_tensor_complex_dichotomy_exact_transverse_diffeomorphisms_soft_tt_or_gapless_helicity_one_partners_2026_09_29.py
---

# The tensor-complex dichotomy on finite slots, at the harmonic level: exact transverse diffeomorphisms give a soft TT mode; without them a linear TT mode brings gapless helicity-1 partners

**Date:** 2026-09-29
**Type:** bounded_theorem
**Status:** exact symbol and moment checks, one harmonic illustration;
pre-registered; unaudited. Independent checks are recorded below.

## In one paragraph

This note collects what the gravity lane has found into one either-or, for
the simplest (harmonic) models on finite records with the time rule kept
exact.

Einstein's graviton is a light-like spin-2 wave with no partners. Its
partners are removed by a symmetry: sliding the metric along the lattice
(diffeomorphisms), in particular the "transverse" slides.
- **If the transverse slides are exact rules of the lattice,** the spin-2
  wave is slow, with frequency ∝ q², whichever variable the records store.
- **If they are not,** a spin-2 wave that is light-like in every direction
  comes with light-like helicity ±1 partners, in some directions at least.
  Every local way of feeding the spin-2 wave feeds the ±1 partners at least
  a quarter as much on average.

So, among local harmonic models on finite records, the light-like,
partner-free graviton does not appear. The one construction that has it is
the landed comparator with continuous (non-finite) variables.

## Pre-registration

Written in the probe's scratch file before the note. Parts of (ii) were
computed in scratch first (the ¼ over 18 dimensions).
- **PASS (route open)** if some local harmonic model, in either
  assignment, has TT modes linear in every direction and no gapless
  helicity ±1 mode.
- **FAIL** if (i) and (ii) hold as stated.

**Outcome: FAIL.**

## Prior art

On main:
- the 2026-09-14 tensor note (the stencils; the moment lemma; the
  both-compact O(k³) class);
- the 2026-09-24 comparator (continuous variables, a linear partner-free TT
  mode; unaudited conditional support).

Of this PR:
- probe 10 (momentum stored: the O(q⁴) bound);
- probe 11 (isotropy ties the helicities);
- probe 15 (metric stored: the O(q²) metric f-sum);
- probes 18 and 20 (breaking the momentum rule brings ±1 partners; the ¼
  lemma).

External, reference only: Dubovsky (hep-th/0409124), on how residual
symmetries remove modes in Lorentz-violating massive gravity. The
transverse slides play that role here.

## Premises (supplied)

- **The landed tensor complex, with finite slots.**
- **Local harmonic models:** finite-range terms with analytic symbols.
- **The scalar (time) rule exact.**
- **The two storage assignments:**
  - momentum stored: DeWitt kinetic term, potential from moves;
  - metric stored: potential polynomial in h, kinetic term from
    Gauss-law-compatible moves.
- **Transverse diffeomorphisms:** shifts h → h + Gᵀ curl ζ. The dichotomy
  is between all of them exact and none of them exact.

## A — (i), momentum stored (check A)

- A move commutes with the transverse generators iff curl(G μ) = 0.
- On a 3³ box: 42 such moves. Their zeroth moments are pure trace, and
  their first moments are invisible to TT in all 60 sampled directions.
- So the TT potential starts at O(q⁴). With the O(1) DeWitt kinetic term
  the TT mode has ω ∝ q².

## B — (i), metric stored (check B)

- The transverse shifts' leading symbols, sym(q ⊗ (q × ζ)), span all five
  traceless tensors (rank 5 from 40 samples).
- An exactly invariant local potential X(q) therefore has X(0) = 0 on
  traceless tensors. This follows from the order-q² term of
  X(q)·Gᵀ(q)C(q)ζ = 0.
- So the TT stiffness is O(q²). With O(q²) Gauss-law kinetic weight
  (probe 15), ω ∝ q².

## C — (ii), without exact transverse diffeomorphisms (check C)

- **The span fact.** The TT directions TT(q̂), over all q̂, span the
  traceless tensors (rank 5).
  - Momentum stored: a TT mode gapless in every direction needs X(0) = 0 on
    TT(q̂) for every q̂, hence on all traceless tensors. So the ±1
    directions get no q⁰ stiffness either: they are ungapped.
  - Metric stored: a linear TT mode needs a q⁰ TT stiffness. That stiffness
    reaches ±1 directions on an open set (probe 20, D).
- **The ¼ lemma, over all 18 first-moment dimensions** (any local move,
  whether or not it respects a rule). The direction-averaged ±1 weight is
  at least ¼ of the TT weight: the minimum is exactly 0.25, from the
  spin-2 part, with spin 3 at 1.6 (exact quadrature, Schur complement).
- **The kinetic side.** The DeWitt form is positive on ±1 directions
  (minimum 1.0).
- **Together:** in both assignments, the ±1 modes have kinetic and
  potential weight of the same orders as the TT modes on an open set of
  directions. So they are gapless and linear there.

## D — illustration (check D)

Momentum stored, momentum rule broken: the DeWitt kinetic term, the scalar
law exact, and a potential from 8 random local moves with each slot type's
zeroth moment removed.
- In all 5 families, five modes are linear.
- Both TT-weighted modes (0.82–0.98) and ±1-weighted modes (0.90–0.97)
  appear.

## What this means

For the gravity lane, among local harmonic models on finite records with
the time rule exact:

| Transverse diffeomorphisms | Momentum stored | Metric stored |
| --- | --- | --- |
| all exact | TT soft, ω ∝ q² (A; probe 10) | TT soft, ω ∝ q² (B; probe 15) |
| none exact | linear TT ⇒ linear ±1 partners on an open set (C, D) | linear TT ⇒ linear ±1 partners on an open set (C; probes 18, 20) |

Einstein's linear, partner-free graviton appears, among the constructions
tested, only with continuous local variables (the landed comparator). The
open routes:
- intermediate symmetry groups;
- strongly correlated states;
- non-local terms;
- composite metrics;
- a softened time rule;
- one qubit per site, which is untested at this level.

## No-Go Discipline Gate

The bounded negative claim, inside the premises: no local harmonic model on
the tensor complex with finite slots and an exact scalar rule has a TT mode
linear in every direction without gapless helicity ±1 modes, in the two
symmetry cases treated.

- **N1 — attack routes.** Each route, with its honesty marker.
  1. *Exact transverse diffeomorphisms with a TT-visible first moment,
     momentum stored.* ATTEMPTED (A: 3³ box kernel). None. Fails.
  2. *Exact transverse diffeomorphisms with a q⁰ TT stiffness, metric
     stored.* ATTEMPTED (B: the symbol span). Forbidden. Fails.
  3. *A q⁰ stiffness on ±1 directions alone, gapping the partners.*
     ATTEMPTED (C: the TT span). It would also stiffen TT (metric stored) or
     gap it (momentum stored). Fails.
  4. *Moves whose first moments feed TT but not ±1.* ATTEMPTED (C: the
     18-dimensional ¼ lemma, exact). Fails.
  5. *A kinetic form that vanishes on ±1.* ATTEMPTED. Momentum stored: the
     DeWitt form is positive on ±1 (C). Metric stored: probe 20's ¼ applies
     to the kinetic side. Fails.
  6. *Random local models.* ATTEMPTED (D): five linear modes with ±1
     weight. Consistent.

  **Open routes:**
  - (i) intermediate symmetry groups;
  - (ii) strongly correlated states;
  - (iii) non-local terms;
  - (iv) composite metrics;
  - (v) a softened scalar rule;
  - (vi) one qubit per site.
- **N2 — pairwise table, with directions.**
  - W1: finite slots.
  - W2: locality (finite range, analytic symbols).
  - W3: the harmonic regime.
  - W4: the exact scalar rule.

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no: finite slots allow non-local terms | no: local terms act on continuous slots | independent |
  | W1, W3 | no | no | independent |
  | W1, W4 | no | no | independent |
  | W2, W3 | no | no | independent |
  | W2, W4 | no | no | independent |
  | W3, W4 | no | no | independent |

- **N3 — hidden-wall scan.** The scan hits, and how each is classified:
  - "harmonic": explicit (W3);
  - "local" or "analytic": explicit (W2);
  - "box": A exhibits the invariant moves; the moment statement follows
    from the symbol and is box-independent;
  - "illustration": D, not load-bearing;
  - "canonical" (the cache path): not load-bearing;
  - "all exact / none exact": the two symmetry cases, with intermediate
    groups named as open.
- **N4 — residual matching.**

  | Citation (path:line) | Residual attacked | Residual status here | Match |
  | --- | --- | --- | --- |
  | docs/ONE_QUBIT_PER_SLOT_UNDER_THE_TENSOR_MOMENTUM_RULE_AN_EXACT_SUM_RULE_BOUNDS_THE_GRAVITON_CHANNEL_BY_Q4_A_LIGHT_CONE_MODE_NEEDS_AN_INCOMPRESSIBLE_ELECTRIC_PATTERN_BOUNDED_THEOREM_NOTE_2026-09-28.md:134 | ker G moves with first moments | the weaker, transverse-only condition gives the same TT result (A) | yes |
  | docs/THE_SWAPPED_QUANTUM_LINK_ASSIGNMENT_METRIC_DIAGONAL_MAKES_EINSTEIN_HILBERT_EXACTLY_INVARIANT_BUT_THE_TT_METRIC_F_SUM_OF_GAUSS_LAW_COMPATIBLE_MOVES_IS_BOUNDED_BY_Q_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-28.md:151 | O(q²) kinetic weight | used in B | yes |
  | docs/EVERY_GAUSS_LAW_COMPATIBLE_MOVE_THAT_FEEDS_THE_TT_CHANNEL_FEEDS_THE_HELICITY_ONE_CHANNEL_AT_LEAST_A_QUARTER_AS_MUCH_ON_DIRECTION_AVERAGE_BOUNDED_THEOREM_NOTE_2026-09-29.md (check B) | the ¼ lemma on 8 dimensions | extended here to 18 | yes |

  All are unaudited parents.
- **N5 — rhetoric audit.**

  | Phrase | per_element | per_site | per_mode | per_block | lattice_wide |
  | --- | --- | --- | --- | --- | --- |
  | "soft with exact transverse diffeomorphisms" | each invariant move's moments (A) | the plaquette constraints at every site touching the box | TT visibility in 60 directions | the 3³ box kernel | the symbol arguments (A, B) are box-independent |
  | "gapless ±1 partners" | not applicable | not applicable | quadrature directions; harmonic modes in 30 family–direction pairs | random families | exact quadrature for the ¼ bound; on an open set of directions, not all |

- **N6 — primitive scan.** None invoked. Continuous local variables are not
  supplied by any registered primitive.
- **N7 — steelman, in a hostile reviewer's voice.** "An intermediate
  symmetry, keeping only part of the transverse slides exact, could remove
  the ±1 partners in the directions that matter while allowing a q⁰ TT
  stiffness elsewhere. In Lorentz-violating massive gravity, residual
  symmetries do exactly this (Dubovsky, hep-th/0409124). A strongly
  correlated ground state could also escape the harmonic analysis. The
  terminal obligations are a classification of local symmetry subgroups and
  a non-perturbative study." Convincing against a broader claim, so the
  claim is limited to the two symmetry cases and the harmonic level.
- **N8 — cross-cycle echo.**

  | Prior wall | Retired? | Mechanism | Applies here? |
  | --- | --- | --- | --- |
  | probe 10's O(q⁴) bound | no | non-exact rules | yes: case (ii) |
  | probe 15's O(q²) bound | no | the same | yes: case (ii) |
  | probe 11's partner theorem | extended | the ¼ lemma over 18 dimensions | yes |
  | the landed both-compact O(k³) class | no | continuous variables | outside the premise |

- **Outcome.** PASS as scoped. The pre-registered outcome is FAIL.

## Independent checks

Pending.

## Reproduction

`python3 scripts/the_tensor_complex_dichotomy_exact_transverse_diffeomorphisms_soft_tt_or_gapless_helicity_one_partners_2026_09_29.py`
prints 4 checks, A–D, the N5 lines and TOTAL, in about 1 s. The canonical
cache is at
logs/runner-cache/the_tensor_complex_dichotomy_exact_transverse_diffeomorphisms_soft_tt_or_gapless_helicity_one_partners_2026_09_29.txt.
