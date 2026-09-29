---
claim_id: the_tensor_complex_on_finite_slots_at_the_harmonic_level_whatever_the_residual_symmetry_tt_modes_linear_in_every_direction_bring_helicity_one_content_among_the_gapless_modes_bounded_theorem_note_2026-09-29
claim_type: bounded_theorem
claim_scope: "Supplied comparator premises (not supplied by the axioms): the landed tensor carrier with finite slots, local (finite-range, analytic-symbol) harmonic models whose quadratic forms are positive semidefinite (stable), the scalar (time) rule exact, and the two storage assignments (momentum stored with the DeWitt kinetic term; metric stored with kinetic terms from Gauss-law-compatible moves). No assumption on which transverse linearised diffeomorphisms (shifts h -> h + G^T curl zeta) are exact, except in (i). (i) All exact: momentum stored, curl(G mu) = 0 reads qhat x (M(q) qhat) = 0 order by order, forcing the zeroth and first moments of every invariant move to pure trace (symbol proof), so TT amplitudes start at O(q^2), the TT potential at O(q^4), and omega_TT = O(q^2); metric stored, the transverse shifts' leading symbols span the traceless tensors, so an exactly invariant local potential has X(0) = 0 on traceless tensors, and with positive semidefiniteness the TT stiffness is O(q^2), against O(q^2) kinetic weight: omega_TT = O(q^2). (ii) Whatever the residual symmetry (the argument uses none; observed by the Fable referee and a panel lens): if both TT polarisations are linear in every direction, then on an open dense set of directions the gapless modes are not two pure-TT modes: momentum stored, some linear mode carries helicity +-1 weight, because the DeWitt form preserves helicity sectors and is positive on them while the move potential's +-1 block is nonzero on an open dense set (the quarter lemma over 18 first-moment dimensions); metric stored, some linear mode carries helicity +-1 weight on a dense set of directions (probe 20: the split lemma with premise P, and Lemmas H and H2 without it; the kinetic range's soft modes cannot hide the +-1 content). Illustrations: a residual azimuthal subgroup lets only one TT polarisation stiffen in some directions; random momentum-stored models show five linear modes. Pre-registered outcome FAIL. Not shown: states beyond harmonic comparators, non-local terms, composite metrics, a softened scalar rule, one qubit per site."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - one_qubit_per_slot_under_the_tensor_momentum_rule_an_exact_sum_rule_bounds_the_graviton_channel_by_q4_a_light_cone_mode_needs_an_incompressible_electric_pattern_bounded_theorem_note_2026-09-28
  - the_swapped_quantum_link_assignment_metric_diagonal_makes_einstein_hilbert_exactly_invariant_but_the_tt_metric_f_sum_of_gauss_law_compatible_moves_is_bounded_by_q_squared_bounded_theorem_note_2026-09-28
  - every_gauss_law_compatible_move_that_feeds_the_tt_channel_feeds_the_helicity_one_channel_at_least_a_quarter_as_much_on_direction_average_bounded_theorem_note_2026-09-29
runner: scripts/the_tensor_complex_dichotomy_exact_transverse_diffeomorphisms_soft_tt_or_gapless_helicity_one_partners_2026_09_29.py
---

# The tensor complex on finite slots at the harmonic level: whatever the residual symmetry, TT modes linear in every direction bring helicity-1 content among the gapless modes

**Date:** 2026-09-29
**Type:** bounded_theorem
**Status:** symbol proofs and linear-algebra lemmas with checks;
pre-registered; unaudited. Revised after the first referee's FAILS verdict,
which narrowed it to two endpoint cases. Revised again after the second
round, which showed that the metric-stored half proves helicity-1 content
among the gapless modes, not necessarily the linear ones. The third
version drops the endpoint restriction: the argument for (ii) never uses
which slides are exact, as the Fable referee and the canonical panel lens
both observed. Independent checks are recorded below.

## In one paragraph

This note collects what the gravity lane has found for the simplest
(harmonic) models on finite records, with the time rule kept exact, in the
two ways of storing the tensor (momentum or metric).
- **If the spin-2 waves are light-like in every direction,** they are not
  alone. In an open, dense set of directions, some other gapless mode (or
  a mixed one) carries helicity ±1 content:
  - if the records store the momentum, a light-like mode;
  - if they store the metric, also a light-like mode (probe 20, Lemmas H
    and H2).

  This holds whichever of the sideways slides of the metric (the
  transverse diffeomorphisms) are exact rules. The argument never uses
  them.
- **If every such slide is an exact rule,** the spin-2 wave is not
  light-like at all: its frequency is at most of order q².

So no choice of residual symmetry gives Einstein's spectrum here: two
light-like, pure spin-2 waves and nothing else gapless.

## Pre-registration

Written in the probe's scratch file before the note; parts of (ii) were
computed in scratch first.
- **PASS** if a local harmonic model in either assignment has TT modes
  linear in every direction and no helicity ±1 content in its linear modes.
- **FAIL** if (i) and (ii) hold.

History:
- The first version presented "all exact / none exact" as exhaustive.
- The second narrowed the claim to those two endpoints.
- This version observes that (ii)'s proof covers every residual symmetry.

**Outcome: FAIL.** An earlier version had an exception for metric stored
without premise P. Probe 20's Lemmas H and H2 removed it.

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
  massive gravity.
  - Linearised, x^i → x^i + ξ^i(t) and t → t + ξ⁰(x) shift only
    h₀ᵢ, by ∂₀ξᵢ + ∂ᵢξ⁰. Neither changes the lapse or the spatial metric,
    so neither is a transverse slide of the spatial metric.
  - The phase they protect keeps two tensor polarisations with a mass,
    not light-like ones.
  - This is from the literature, reference only, not re-derived here. It
    is not an escape from (ii), whose hypothesis is that both TT
    polarisations are light-like.

## Premises (supplied)

The axioms supply none of these:
- the tensor carrier with finite slots;
- local harmonic models (finite range, analytic symbols) whose quadratic
  forms are positive semidefinite (stable);
- the scalar (time) rule exact;
- the two storage assignments.

No residual-symmetry assumption is made in (ii). Case (i) assumes every
transverse diffeomorphism h → h + Gᵀ curl ζ is exact.

## (i) All transverse diffeomorphisms exact (checks A, B)

**Momentum stored (A).**
- A move commutes with the transverse generators iff curl(G μ) = 0. Order
  by order in q this reads q̂ × (M(q) q̂) = 0.
- That forces the zeroth moment to a·I (the symbol kernel is 1-dimensional)
  and the first moment to ℓ(q)·I (3-dimensional). Both are pure trace and
  invisible to TT. This is proved for every finite support; the 3³ box
  exhibits 42 such moves.
- In real space (Fable referee and panel lens): curl(Gμ) = 0 iff Gμ is a
  lattice gradient, iff μ = φδ + ν with ν in ker G. On the 3³ box this is
  42 = 27 + 15 (checked in A).
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
- The Fable referee sharpens this: exact invariance alone already removes
  it. Every column of X lies in ker(curl∘G), so X(q) = δ φ̂(q)ᵀ + O(q²).
  That is its computation, reference here.
- With O(q²) Gauss-law kinetic weight (probe 15), ω_TT = O(q²).

## (ii) TT linear in every direction, whatever the residual symmetry (check C, probe 20)

Hypothesis: both TT polarisations are linear in every direction. No
assumption is made about which transverse slides are exact. The steps
below use only the hypothesis, the premises and the moves' first moments.
The ¼ lemma holds for every family of moves, including one restricted by
a partial symmetry.

**Metric stored.** The kinetic weight is O(q²), so the stiffness V must be
positive on every TT plane. By probe 20's corollary:
- every ±1 tensor is a TT tensor for another direction;
- every traceless 2-plane contains such a tensor;
- so V is positive definite on TT ⊕ ±1 off a cone;
- the kinetic form's range R has a ±1 component on an open dense set of
  directions (the ¼ lemma).

The modes inside R split into linear modes and soft modes, the soft modes
being R ∩ ker V (probe 20's split lemma). So on that set some mode in R,
linear or soft, carries ±1 weight, and the gapless modes are not two
pure-TT modes.

With premise P (ker V ∩ ker s(q̂) = 0), R has no soft modes and a linear
mode carries the ±1 weight. P holds off a quadric cone when ker V has
dimension at most 1.

With no premise at all, probe 20's Lemmas H and H2 give the same
conclusion. A two-dimensional stiffness kernel is the only kind where P
fails everywhere, and it cannot hide the ±1 content in soft modes.
- H: the linear modes are not all pure TT on a dense set of directions.
- H2: the moves that would keep only helicity-0 non-TT content form at
  most one family, and that family's single mode is linear and carries ±1
  weight.

So in the metric-stored assignment too, some linear mode carries ±1 weight
on a dense set of directions.

The second-round referee's counterexample shows the premise is needed
pointwise. At q̂ = ẑ it has pure-TT linear modes, and the ±1 content sits
in a soft mode along q̂q̂ + H1 (probe 20 G).

**Momentum stored.**
- The DeWitt form preserves the helicity sectors and is positive on the
  traceless ones.
- The TT potential is O(q²), from first moments, with X(0) = 0 on TT. By the
  TT span that means X(0) = 0 on all traceless tensors, so no ±1 direction
  is gapped.
- The potential's ±1 block is nonzero on an open dense set: the ¼ lemma over
  all 18 first-moment dimensions (min ¼ from spin 2, 8/5 from spin 3).
- Hence the linear modes carry ±1 weight on an open dense set. The
  linear modes span K·Range V, and the DeWitt form K maps each helicity
  sector to itself invertibly. So the ±1 content of Range V reaches a
  linear mode, and no soft-mode alternative arises here.

**Check C** verifies:
- the TT span (rank 5);
- the 18-dimensional ¼ lemma (exact quadrature, Schur complement);
- the DeWitt form on ±1 directions (minimum 1.0).

In either assignment the result says the gapless modes are not two pure-TT
modes. It does not say how many extra modes appear.

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

  So under this partial symmetry TT is not linear in every direction, and
  (ii)'s hypothesis fails. (ii) itself needs no classification of partial
  symmetries.
- **Another partial symmetry** (Fable referee, momentum stored, only
  slides with ζ ∥ ẑ exact): the invariant moves' zeroth moments span
  e₃e₃ and e₁e₁ + e₂e₂. These are TT-visible in 200 of 200 directions, so TT
  is gapped unless the zeroth moments are restricted to pure trace, and
  then (ii) applies as written. That is the referee's computation.

## What this means

| Transverse diffeomorphisms | Momentum stored | Metric stored |
| --- | --- | --- |
| all exact | ω_TT = O(q²) | ω_TT = O(q²) |
| any, with TT linear everywhere | a linear mode carries ±1 weight (open dense set) | a linear mode carries ±1 weight (dense set; probe 20 H, H2) |

At the harmonic level, with the time rule exact, no residual symmetry
gives Einstein's spectrum on finite records in either assignment.
Einstein's spectrum means two pure-TT light-like modes and no other
gapless mode.

The open questions:
- metric stored with a two-dimensional stiffness kernel: can the ±1
  content hide in soft modes on an open set of directions?
- strongly correlated states;
- non-local terms;
- composite metrics;
- a softened time rule;
- continuous local variables, which is an axiom change.

## No-Go Discipline Gate

The bounded negative claims:
- (a) with every transverse diffeomorphism exact, ω_TT = O(q²) in both
  assignments;
- (b) whatever the residual symmetry, both TT polarisations linear in every
  direction imply helicity ±1 content among the gapless modes on an open dense
  set:
  - in a linear mode, momentum stored;
  - in a linear mode, metric stored (probe 20: the corollary with P, and H
    and H2 without it).

- **N1 — attack routes.** Each route, with its honesty marker.
  1. *An invariant move with a TT-visible first moment (i, momentum
     stored).* ATTEMPTED (A: a symbol proof for all supports). Fails.
  2. *A q⁰ or O(q) TT stiffness under exact invariance (i, metric
     stored).* ATTEMPTED (B: the symbol span plus positivity). Fails.
  3. *Kinetic and stiffness ±1 blocks that are orthogonal (ii, metric
     stored).* ATTEMPTED (probe 20 D). Excluded on TT ⊕ ±1 off a cone.
     Fails there.
  3b. *A stiffness kernel inside ker s(q̂), which may contain a trace
     direction, and absorbs the ±1 content into a soft mode (ii, metric
     stored; the second-round counterexample).* ATTEMPTED (probe 20 G).
     Succeeds pointwise, at single directions. Premise P excludes it on a
     dense set when the kernel has dimension at most 1. Probe 20's H and H2
     exclude it for two-dimensional kernels. Fails for (b).
  4. *A ±1 potential block vanishing everywhere (ii, momentum stored).*
     ATTEMPTED (C: the ¼ lemma over 18 dimensions). Fails.
  5. *A kinetic form that mixes helicities (ii, momentum stored).*
     ATTEMPTED (C): the DeWitt form preserves the helicity sectors. Fails.
  6. *An intermediate residual symmetry.* ATTEMPTED.
     - (b)'s proof uses no symmetry assumption, so a partial symmetry
       cannot evade it. It either leaves TT non-linear somewhere (the
       azimuthal example; the Fable referee's ζ ∥ ẑ example) or meets (b).
     - Dubovsky's residual symmetries shift only h₀ᵢ and protect a massive
       tensor, so they fall outside (b)'s hypothesis.
     Fails.

  **Open routes:**
  - (i) none from the symmetry side at this level;
  - (ii) strongly correlated states;
  - (iii) non-local terms;
  - (iv) composite metrics;
  - (v) a softened scalar rule;
  - (vi) continuous slots;
- **N2 — pairwise table, with directions.**
  - W1: finite slots.
  - W2: locality with analytic symbols.
  - W3: harmonic, positive-semidefinite forms.
  - W4: the exact scalar rule.
  - W5: every transverse diffeomorphism exact (for (a) only).
  - W6: both TT polarisations linear in every direction (for (b)).
  - W7: premise P. It is used only by the first proof for metric stored;
    probe 20's H and H2 remove the need for it.

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no: finite slots allow non-local terms | no: local terms allow continuous slots | independent |
  | W1, W3 | no: finite slots allow indefinite or anharmonic terms | no: harmonic stable forms exist for continuous slots (the comparator) | independent |
  | W1, W4 | no: finite slots fix no rule | no: the rule holds for continuous slots too | independent |
  | W1, W5 | no: finite slots fix no symmetry | no: gauge invariance is defined for continuous slots too | independent |
  | W1, W6 | no: finite slots allow soft TT (probe 10) | no: linear TT occurs with continuous slots | independent |
  | W1, W7 | no: finite slots fix no stiffness | no: P is a property of V for any slots | independent |
  | W2, W3 | no: local forms can be indefinite | no: harmonic forms can be non-local | independent |
  | W2, W4 | no: local terms can break the rule | no: the rule constrains moves, not their range | independent |
  | W2, W5 | no: local terms can break every slide | no: invariance allows non-local invariant terms | independent |
  | W2, W6 | no: local models can have soft TT | no: linear TT does not force finite range | independent |
  | W2, W7 | no: local V can meet ker s | no: P does not bound the range | independent |
  | W3, W4 | no: stable forms can break the rule | no: the rule allows indefinite forms | independent |
  | W3, W5 | no: stable forms can break every slide | no: invariant forms can be indefinite | independent |
  | W3, W6 | no: stable forms can leave TT soft | no: linear TT is possible with an unstable direction elsewhere | independent |
  | W3, W7 | no: positive semidefinite V can meet ker s (probe 20 G3) | no: P allows indefinite V | independent |
  | W4, W5 | no: the scalar rule does not make the slides exact | no: exact slides do not force the scalar rule | independent |
  | W4, W6 | no: the rule allows soft TT | no: linear TT with the rule broken is possible (probe 18's D is gapped only when both are soft) | independent |
  | W4, W7 | no: the rule fixes no stiffness | no: P refers to s, the rule's symbol, but does not impose the rule | W7 is stated in W4's terms |
  | W5, W6 | yes: W5 makes TT soft, so W6 fails | yes: W6 excludes W5 | mutually exclusive; (a) uses W5, (b) uses W6 |
  | W5, W7 | no: exact slides fix no stiffness kernel | no: P does not make any slide exact | independent |
  | W6, W7 | no: probe 20 G3's kernel satisfies W6's stiffness condition, not W7 | no: V = 1 satisfies P and gives TT linear only with TT-fed moves | independent |

  (a) uses W1–W5. (b) uses W1–W4 and W6; W7 is no longer needed. (b)
  assumes nothing about residual symmetry.
- **N3 — hidden-wall scan.** The scan hits, and how each is classified:
  - "positive semidefinite": explicit (W3);
  - "both TT polarisations": explicit (W6);
  - "operator overlap": settled by the DeWitt form's helicity preservation
    (momentum stored). For metric stored it is settled on TT ⊕ ±1 by probe
    20 D. The helicity-0 direction q̂q̂ was a hidden condition. It was made
    explicit as W7 and is now discharged by probe 20's H and H2;
  - "endpoint": retired; (b) holds for every residual symmetry, and W5
    is used only in (a);
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
  | "soft in (i)" | the symbol kernels (A) | the plaquette constraints on the box | not applicable | the 3³ box (exhibits moves) | proved by the symbol arguments; an upper order O(q²) |
  | "±1 content among the gapless modes" | not applicable | not applicable | D's sample; probe 20 G (illustration) | random families | proved for the premises on an open dense set of directions: a linear mode in both assignments (metric stored via probe 20's corollary, H and H2) |

- **N6 — primitive scan.** None invoked. The tensor carrier and slots are
  supplied.
- **N7 — steelman, in a hostile reviewer's voice.** "Residual symmetries
  are known to remove unwanted modes. Dubovsky's protect the massive
  graviton in Lorentz-violating gravity (hep-th/0409124), and Hořava's
  extended U(1) (arXiv:1007.2410) removes an extra scalar. And in the
  metric-stored assignment, a stiffness kernel that meets ker s(q̂), for
  example one containing a trace direction, can hide the ±1 content in
  soft modes." The first part does not bite at this level:
  - (b) uses no symmetry;
  - Dubovsky's symmetries shift only h₀ᵢ, and his phase has a massive
    tensor;
  - Hořava's U(1) acts on the scalar sector, not on ±1.
  The second part was convincing against the second version. It is now
  answered by probe 20's H and H2.
- **N8 — cross-cycle echo.**

  | Prior wall | Retired? | Mechanism | Applies here? |
  | --- | --- | --- | --- |
  | probes 10 and 15's bounds | no | non-exact rules | yes, in (ii) |
  | probe 11's partner theorem | extended | probe 20 | yes |
  | the landed both-compact O(k³) class | no | continuous variables | outside the premise |

- **Outcome.** PASS as scoped, at the harmonic level. The pre-registered
  outcome is FAIL.

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
- **gpt-5.6-sol, second round: FAILS.**
  - Resolved: findings 2–5 and 7. Findings 2–5 are the TT quantifiers and
    stability, the endpoint scope, the symbol proof for case (i) momentum
    stored, and positivity for case (i) metric stored. Finding 7 is the
    prior art.
  - The momentum-stored half of (ii) was confirmed valid.
  - The metric-stored half relied on probe 20's step from the kinetic range
    to the modes, which fails pointwise: a stiffness with a traceful kernel
    in ker s(q̂) leaves pure-TT linear modes and puts the ±1 content into a
    soft mode. Answered: (ii) metric stored now reads "linear or softer",
    with premise P (W7) for "linear", and the title says "among the gapless
    modes".
  - The gate: N1.3, N3, N5 and N7 are rewritten; N2 is now the full
    21-pair table.
  - Still unresolved in that round: the changed-evidence checker reported
    `checked: []`, because ledger seeding aborted on an over-long shard
    filename. The third round traced this to probe 14's own claim id.
- **Fable check (same family; it reviewed the second version): STANDS
  WITH CORRECTIONS.** It reproduced the runner and wrote its own checks.
  Its findings, and how this version answers each:
  1. Case (i) momentum stored: confirmed. Sharpened in real space,
     ker(curl G) = φδ ⊕ ker G (42 = 27 + 15 on the 3³ box). Now checked
     in A.
  2. Case (i) metric stored: confirmed. Exact invariance alone removes the
     O(q) term. Noted in B as its computation.
  3. Mode mixing: the result is "linear modes carry ±1 weight", not
     separate partners. In its two-move example there are two mixed linear
     modes and three softer ones. This version already states the content,
     not a count.
  4. "None exact" is never used, so (ii) holds for every residual
     symmetry. Applied: the title, scope and text now say so, and the
     endpoint framing is retired. The panel's canonical lens made the same
     point independently.
  5. Under-claims: metric stored, the stiffness is positive on every ±1
     direction at every q̂. Noted via probe 20 D.
  6. "Whichever variable the records store" covers only the two
     assignments. The paragraph now names the two.
- **gpt-5.6-sol, third round: STANDS WITH CORRECTIONS.**
  - Resolved: findings 1–5. The referee checked the symmetry-free claim
    independently: no algebraic step of (ii) assumes an absent transverse
    symmetry, and a partial symmetry evades neither lemma.
  - Its corrections, now applied:
    - the title says "TT modes" (both polarisations);
    - every N2 cell has a directional rationale;
    - the Dubovsky gloss: his symmetries shift only h₀ᵢ.
  - The changed-evidence receipt could not run. The cause was this PR's own
    probe 14, whose claim id was too long for the ledger's temporary shard
    names. Probes 14 and 16 are now renamed, and the pipeline is being
    re-run.
- **Changed-evidence receipt.** After the renames, an isolated worktree at
  a5cfca702e ran the full pipeline. Ledger seeding passed, with 22 rows
  newly seeded. `check_changed_audit_evidence.py --base origin/main
  --include-worktree` reported checked=21, failures=0. The pipeline's only
  failure was the final invariants guard, which requires the citation-graph
  manifest to acknowledge the 22 new nodes. That derived file is
  regenerated at integration.
- **gpt-5.6-sol, fourth round: STANDS WITH CORRECTIONS.**
  - Resolved:
    - the N2 rationales;
    - the Dubovsky gloss;
    - the changed-evidence receipt. The referee ran the pipeline with
      `--stage-citation-manifest` on a clone of the current head and got
      checked=21, failures=0.
  - Corrected in that round: the bounded claim (b) and the runner's N5
    line said "a TT mode"; they now say "both TT polarisations".
- **gpt-5.6-sol, fifth round: STANDS WITH CORRECTIONS.** The claim surfaces
  are fixed. The runner's question (line 9), check C's docstring (line 27)
  and one prior-art line still used the singular; all three now say "both
  TT polarisations". The previous entry's "fully corrected" was premature.
- **Strengthened after the fifth round.** Probe 20's Lemmas H and H2 were
  added after that note's confirmation. H2's derivation came from the Fable
  check of H. With them, (ii) metric stored reads "a linear mode carries
  ±1 weight", with no premise. The title's "among the gapless modes" stays
  true and is now weaker than what is proved.
- Sixth round: pending.

## Reproduction

`python3 scripts/the_tensor_complex_dichotomy_exact_transverse_diffeomorphisms_soft_tt_or_gapless_helicity_one_partners_2026_09_29.py`
prints 4 checks, A–D, the N5 lines and TOTAL, in about 1 s. The canonical
cache is at
logs/runner-cache/the_tensor_complex_dichotomy_exact_transverse_diffeomorphisms_soft_tt_or_gapless_helicity_one_partners_2026_09_29.txt.
