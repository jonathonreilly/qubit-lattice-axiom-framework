---
claim_id: the_tensor_complex_on_finite_slots_at_the_harmonic_level_two_endpoint_cases_all_transverse_diffeomorphisms_exact_gives_a_soft_tt_mode_none_exact_leaves_helicity_one_content_in_the_linear_modes_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: "Supplied comparator premises (not supplied by the axioms): the landed tensor carrier with finite slots, local (finite-range, analytic-symbol) harmonic models whose quadratic forms are positive semidefinite (stable), the scalar (time) rule exact, and the two storage assignments (momentum stored with the DeWitt kinetic term; metric stored with kinetic terms from Gauss-law-compatible moves). Two endpoint cases of the transverse linearised diffeomorphisms (shifts h -> h + G^T curl zeta); intermediate residual symmetry groups are not covered. (i) All exact: momentum stored, curl(G mu) = 0 reads qhat x (M(q) qhat) = 0 order by order, forcing the zeroth and first moments of every invariant move to pure trace (symbol proof), so TT amplitudes start at O(q^2), the TT potential at O(q^4), and omega_TT = O(q^2); metric stored, the transverse shifts' leading symbols span the traceless tensors, so an exactly invariant local potential has X(0) = 0 on traceless tensors, and with positive semidefiniteness the TT stiffness is O(q^2), against O(q^2) kinetic weight: omega_TT = O(q^2). (ii) None exact: if both TT polarisations are linear in every direction, then on an open dense set of directions the linear modes carry helicity +-1 weight (they are not pure TT): metric stored by probe 20's corollary (the TT-plane and traceless-2-plane lemmas); momentum stored because the DeWitt form preserves helicity sectors and is positive on them while the move potential's +-1 block is nonzero on an open dense set (the quarter lemma over 18 first-moment dimensions). Illustrations: a residual azimuthal subgroup lets only one TT polarisation stiffen in some directions; random momentum-stored models show five linear modes. Pre-registered outcome FAIL for the two endpoint cases. Not shown: intermediate symmetry groups (Dubovsky-type residual symmetries are a known escape route in the continuum), states beyond harmonic comparators, non-local terms, composite metrics, a softened scalar rule, one qubit per site."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - one_qubit_per_slot_under_the_tensor_momentum_rule_an_exact_sum_rule_bounds_the_graviton_channel_by_q4_a_light_cone_mode_needs_an_incompressible_electric_pattern_bounded_theorem_note_2026-09-28
  - the_swapped_quantum_link_assignment_metric_diagonal_makes_einstein_hilbert_exactly_invariant_but_the_tt_metric_f_sum_of_gauss_law_compatible_moves_is_bounded_by_q_squared_bounded_theorem_note_2026-09-28
  - every_gauss_law_compatible_move_that_feeds_the_tt_channel_feeds_the_helicity_one_channel_at_least_a_quarter_as_much_on_direction_average_bounded_theorem_note_2026-09-29
runner: scripts/the_tensor_complex_dichotomy_exact_transverse_diffeomorphisms_soft_tt_or_gapless_helicity_one_partners_2026_09_29.py
---

# The tensor complex on finite slots at the harmonic level, two endpoint cases: all transverse diffeomorphisms exact gives a soft TT mode; none exact leaves helicity-1 content in the linear modes

**Date:** 2026-09-29
**Type:** bounded_theorem
**Status:** symbol proofs and linear-algebra lemmas with checks;
pre-registered; unaudited. Revised after the first referee's FAILS verdict,
which narrowed it to two endpoint cases. Independent checks are recorded
below.

## In one paragraph

This note collects what the gravity lane has found for the simplest
(harmonic) models on finite records, with the time rule kept exact. It
covers two cases of one symmetry: sliding the metric sideways (the
transverse diffeomorphisms), which is what removes a graviton's unwanted
partners.
- **If every such slide is an exact rule,** the spin-2 wave is slow, with
  frequency at most ∝ q², whichever variable the records store.
- **If none is,** and the spin-2 waves are light-like in every direction,
  the light-like modes are not pure spin-2. In an open, dense set of
  directions they carry helicity ±1 content.

Neither case gives Einstein's graviton, which is light-like and
partner-free. Cases in between, where only some of the slides are exact,
are not covered. In continuum gravity such residual symmetries are a known
way to remove partners (Dubovsky), so they are the natural next question.

## Pre-registration

Written in the probe's scratch file before the note; parts of (ii) were
computed in scratch first.
- **PASS** if a local harmonic model in either assignment has TT modes
  linear in every direction and no helicity ±1 content in its linear modes.
- **FAIL** if (i) and (ii) hold.

The first version presented the two cases as exhaustive. They are
endpoints.

**Outcome: FAIL for the two endpoint cases.**

## Prior art

On main:
- the 2026-09-14 tensor note (the stencils; the both-compact O(k³) class);
- the 2026-09-24 comparator (continuous variables; a linear, partner-free
  TT mode; unaudited conditional support).

Of this PR:
- probes 10 and 15 (the two assignments' f-sum bounds);
- probe 20 (the ¼ lemma, and its corollary with the TT-plane and
  traceless-2-plane lemmas).

External, reference only:
- **Xu and Hořava** (arXiv:1003.0009): lattice z = 2 and z = 3 gravitons.
- **Gu and Wen** (arXiv:0907.1203): a reliable qubit model at k³, and a
  tentative linear one with only helicity ±2.
- **Hořava gravity** (arXiv:0901.3775) and its extended-U(1) version
  (arXiv:1007.2410): a relevant flow to z = 1, and a symmetry that removes
  the extra scalar.
- **Pretko** (arXiv:1604.05329): other rank-2 constraints.
- **Dubovsky** (hep-th/0409124): residual symmetries in Lorentz-violating
  massive gravity, a known escape for intermediate cases.

## Premises (supplied)

The axioms supply none of these:
- the tensor carrier with finite slots;
- local harmonic models (finite range, analytic symbols) whose quadratic
  forms are positive semidefinite (stable);
- the scalar (time) rule exact;
- the two storage assignments.

Endpoint symmetry cases: all transverse diffeomorphisms h → h + Gᵀ curl ζ
exact, or none.

## (i) All transverse diffeomorphisms exact (checks A, B)

**Momentum stored (A).**
- A move commutes with the transverse generators iff curl(G μ) = 0. Order
  by order in q this reads q̂ × (M(q) q̂) = 0.
- That forces the zeroth moment to a·I (the symbol kernel is 1-dimensional)
  and the first moment to ℓ(q)·I (3-dimensional). Both are pure trace and
  invisible to TT. This is proved for every finite support; the 3³ box
  exhibits 42 such moves.
- So TT amplitudes start at O(q²) and the positive move potential on TT at
  O(q⁴). With the DeWitt kinetic term, ω_TT = O(q²). That is an upper
  order: it could be softer.

**Metric stored (B).**
- The transverse shifts' leading symbols, sym(q ⊗ (q × ζ)), span all five
  traceless tensors.
- The order-q² term of X(q)·Gᵀ(q)C(q)ζ = 0 then forces X(0) = 0 on
  traceless tensors.
- Analyticity alone would still allow an O(q) term on TT. Positive
  semidefiniteness removes it, so the TT stiffness is O(q²).
- With O(q²) Gauss-law kinetic weight (probe 15), ω_TT = O(q²).

## (ii) No transverse diffeomorphism exact (check C, probe 20)

Hypothesis: both TT polarisations are linear in every direction.

**Metric stored.** The kinetic weight is O(q²), so the stiffness must be
positive on every TT plane. By probe 20's corollary:
- every ±1 tensor is a TT tensor for another direction;
- every traceless 2-plane contains such a tensor;
- so the stiffness is positive definite on TT ⊕ ±1 off a cone, and the ±1
  kinetic block is nonzero on an open dense set (the ¼ lemma).

Hence the linear modes carry ±1 weight on an open dense set of directions.

**Momentum stored.**
- The DeWitt form preserves the helicity sectors and is positive on the
  traceless ones.
- The TT potential is O(q²), from first moments, with X(0) = 0 on TT. By the
  TT span that means X(0) = 0 on all traceless tensors, so no ±1 direction
  is gapped.
- The potential's ±1 block is nonzero on an open dense set: the ¼ lemma over
  all 18 first-moment dimensions (min ¼ from spin 2, 8/5 from spin 3).
- Hence, again, the linear modes carry ±1 weight on an open dense set.

**Check C** verifies:
- the TT span (rank 5);
- the 18-dimensional ¼ lemma (exact quadrature, Schur complement);
- the DeWitt form on ±1 directions (minimum 1.0).

In either assignment the result says the linear modes are not pure TT. It
does not say how many extra modes appear.

## Illustrations (check D, and an intermediate case)

- **Momentum stored, momentum rule broken:** five random local models each
  show five linear modes, with both TT weight (0.82–0.98) and ±1 weight
  (0.90–0.97).
- **An intermediate case:** keep only the slides generated within the xy
  plane exact. Their leading shifts span four of the five traceless
  directions. The only allowed on-site traceless stiffness is along
  diag(1, 1, −2):
  - along z neither TT polarisation is stiffened;
  - along x one is;
  - along the body diagonal both are, partly (overlaps 0.29 and 0.50).

  So this case gives no TT mode linear in every direction. It is one
  example, not a classification.

## What this means

| Transverse diffeomorphisms | Momentum stored | Metric stored |
| --- | --- | --- |
| all exact | ω_TT = O(q²) | ω_TT = O(q²) |
| none exact, TT linear everywhere | linear modes carry ±1 weight (open dense set) | the same |
| some exact | not covered | not covered |

At the harmonic level, with the time rule exact, the two endpoint cases do
not give a light-like, partner-free graviton on finite records.

The open questions:
- intermediate residual symmetries (the Dubovsky-type route);
- strongly correlated states;
- non-local terms;
- composite metrics;
- a softened time rule;
- continuous local variables, which is an axiom change.

## No-Go Discipline Gate

The bounded negative claims:
- (a) in endpoint (i), ω_TT = O(q²) in both assignments;
- (b) in endpoint (ii), a TT mode linear in every direction implies helicity
  ±1 content in the linear modes on an open dense set.

- **N1 — attack routes.** Each route, with its honesty marker.
  1. *An invariant move with a TT-visible first moment (i, momentum
     stored).* ATTEMPTED (A: a symbol proof for all supports). Fails.
  2. *A q⁰ or O(q) TT stiffness under exact invariance (i, metric
     stored).* ATTEMPTED (B: the symbol span plus positivity). Fails.
  3. *Kinetic and stiffness ±1 blocks that are orthogonal (ii, metric
     stored).* ATTEMPTED (probe 20 D). Excluded off a cone. Fails.
  4. *A ±1 potential block vanishing everywhere (ii, momentum stored).*
     ATTEMPTED (C: the ¼ lemma over 18 dimensions). Fails.
  5. *A kinetic form that mixes helicities (ii, momentum stored).*
     ATTEMPTED (C): the DeWitt form preserves the helicity sectors. Fails.
  6. *An intermediate residual symmetry.* ATTEMPTED for one example (the
     azimuthal subgroup): no TT mode linear everywhere. Not classified, so
     it stays open.

  **Open routes:**
  - (i) intermediate symmetry groups in general;
  - (ii) strongly correlated states;
  - (iii) non-local terms;
  - (iv) composite metrics;
  - (v) a softened scalar rule;
  - (vi) continuous slots.
- **N2 — pairwise table, with directions.**
  - W1: finite slots.
  - W2: locality with analytic symbols.
  - W3: harmonic, positive-semidefinite forms.
  - W4: the exact scalar rule.
  - W5: an endpoint symmetry case.
  - W6: both TT polarisations linear in every direction (for (b)).

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no | no | independent |
  | W1, W3 | no | no | independent |
  | W2, W3 | no: local forms can be indefinite | no: harmonic forms can be non-local | independent |
  | W3, W5 | no | no | independent |
  | W5, W6 | no | yes, partly: W6 excludes endpoint (i), where TT is soft | W6 selects endpoint (ii) |
  | W4, W5 | no | no | independent |
  | (other pairs) | no | no | independent |

  W5 does not exhaust the symmetry cases: the endpoint wall is explicit.
- **N3 — hidden-wall scan.** The scan hits, and how each is classified:
  - "positive semidefinite": explicit (W3);
  - "both TT polarisations": explicit (W6);
  - "operator overlap": settled by probe 20 D (metric stored) and by the
    DeWitt form's helicity preservation (momentum stored);
  - "endpoint": explicit (W5);
  - "box": A is proved for all supports;
  - "canonical" (the cache path): not load-bearing.
- **N4 — residual matching.**

  | Citation (path:line) | Residual attacked | Residual status here | Match |
  | --- | --- | --- | --- |
  | docs/ONE_QUBIT_PER_SLOT_UNDER_THE_TENSOR_MOMENTUM_RULE_AN_EXACT_SUM_RULE_BOUNDS_THE_GRAVITON_CHANNEL_BY_Q4_A_LIGHT_CONE_MODE_NEEDS_AN_INCOMPRESSIBLE_ELECTRIC_PATTERN_BOUNDED_THEOREM_NOTE_2026-09-28.md:134 | ker G moves' first moments | the weaker, transverse-only condition gives the same TT result (A) | yes |
  | docs/THE_SWAPPED_QUANTUM_LINK_ASSIGNMENT_METRIC_DIAGONAL_MAKES_EINSTEIN_HILBERT_EXACTLY_INVARIANT_BUT_THE_TT_METRIC_F_SUM_OF_GAUSS_LAW_COMPATIBLE_MOVES_IS_BOUNDED_BY_Q_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-28.md:151 | O(q²) kinetic weight | used in B | yes |
  | docs/EVERY_GAUSS_LAW_COMPATIBLE_MOVE_THAT_FEEDS_THE_TT_CHANNEL_FEEDS_THE_HELICITY_ONE_CHANNEL_AT_LEAST_A_QUARTER_AS_MUCH_ON_DIRECTION_AVERAGE_BOUNDED_THEOREM_NOTE_2026-09-29.md, check D (the corollary) | kinetic and stiffness overlap | used for (ii), metric stored | yes |

  All are unaudited parents.
- **N5 — rhetoric audit.**

  | Phrase | per_element | per_site | per_mode | per_block | lattice_wide |
  | --- | --- | --- | --- | --- | --- |
  | "soft in endpoint (i)" | the symbol kernels (A) | the plaquette constraints on the box | not applicable | the 3³ box (exhibits moves) | proved by the symbol arguments; an upper order O(q²) |
  | "±1 content in the linear modes" | not applicable | not applicable | D's sample (illustration) | random families | proved for the premises, on an open dense set of directions |

- **N6 — primitive scan.** None invoked. The tensor carrier and slots are
  supplied.
- **N7 — steelman, in a hostile reviewer's voice.** "The two endpoints are
  not the whole space. Residual symmetries that remove the ±1 modes only
  where needed, or only for some q, are known to protect massive-graviton
  spectra in Lorentz-violating gravity (Dubovsky, hep-th/0409124).
  Hořava's extended-U(1) symmetry (arXiv:1007.2410) removes an extra mode
  the same way. The terminal obligation is a classification of local
  residual subgroups of the lattice diffeomorphisms, which is not
  attempted." Convincing against any broad claim, so none is made. The
  note is limited to the endpoints.
- **N8 — cross-cycle echo.**

  | Prior wall | Retired? | Mechanism | Applies here? |
  | --- | --- | --- | --- |
  | probes 10 and 15's bounds | no | non-exact rules | yes, in (ii) |
  | probe 11's partner theorem | extended | probe 20 | yes |
  | the landed both-compact O(k³) class | no | continuous variables | outside the premise |

- **Outcome.** PASS as scoped: two endpoint cases at the harmonic level.
  The pre-registered outcome is FAIL for these endpoints.

## Independent checks

- **gpt-5.6-sol (other vendor), first round: FAILS.** Its findings, and how
  this version answers each:
  1. Weights are not modes. (ii) now rests on probe 20's corollary (metric
     stored) and on the DeWitt form's helicity preservation (momentum
     stored), and is stated as "±1 content in the linear modes".
  2. TT quantifiers and stability. Both polarisations are now required (W6)
     and positive semidefiniteness is assumed (W3). The orders are stated
     as O(q²), not ∝ q².
  3. "Dichotomy" overreached. Narrowed to two endpoint cases in the title,
     scope and text; intermediate cases are open.
  4. Case (i), momentum stored, needed a proof for all supports. Given (the
     symbol kernels).
  5. Case (i), metric stored, needed positivity. Stated.
  6. The gate. Rewritten.
  7. Prior art: Xu–Hořava, Gu–Wen, Hořava, extended U(1), Pretko,
     Dubovsky. Added.
- Fable check: pending.
- Second rounds: pending.

## Reproduction

`python3 scripts/the_tensor_complex_dichotomy_exact_transverse_diffeomorphisms_soft_tt_or_gapless_helicity_one_partners_2026_09_29.py`
prints 4 checks, A–D, the N5 lines and TOTAL, in about 1 s. The canonical
cache is at
logs/runner-cache/the_tensor_complex_dichotomy_exact_transverse_diffeomorphisms_soft_tt_or_gapless_helicity_one_partners_2026_09_29.txt.
