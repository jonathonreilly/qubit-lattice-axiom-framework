---
claim_id: the_photon_triplet_composites_partners_are_not_gapped_by_gauge_invariant_local_harmonic_terms_and_every_tested_constraint_set_removing_the_helicity_one_partners_leaves_no_tt_visible_first_moments_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Probe 11's composite E = curl_1(A~ - I tr A~/2) of a photon triplet (electric components A~_lj, vector potentials a_lj), on probe 11's placement. (A) eps_mij E_ij equals photon m's Gauss law row for row (exact at 37 momenta incl. axes, zone edges and corners), so exact E symmetry is exact U(1) gauge invariance of every photon. (B) Harmonic regime with local forms (bounded local kinetic form; finite-range potential in the curls, higher-derivative kernels allowed; finite-range E-B cross terms): every frequency -> 0 as q -> 0, so no such term gaps the partners; a Proca mass (gauge-breaking) or a non-local B(-Delta)^-1 B term would gap them. (C) A fixed photon-index block removes only partner weight for q along z but helicity-2 weight for q along x (fixed-block check only). (D) Constraint sets, physical / seen by E / invisible to E: Gauss 6/3/3; +rotation (A~_lj = A~_jl, pointwise) 3/2/1, the invisible mode being the transverse trace K K^T - K^2 I (a helicity-0 partner survives); +rotation+trace 2/2/0; +first-index Gauss 4/3/1; +first-index Gauss+trace 3/3/0; +trace alone keeps helicity +-1. With the rotation constraint the Gauss laws equal the landed momentum rule exactly (4^3 torus). (E) Moves (box kernels): Gauss only, TT-visible first moments (rank 9); +rotation, zeroth and first moments 0; +rotation+trace (4^3 box), second moments 0 too; +first-index Gauss, one first moment, totally antisymmetric and TT-invisible, with or without the trace. (F) All 15 cubic-covariant pointwise constraint sets: every set that removes helicity +-1 and keeps a TT mode has no first-moment space. (G) Harmonic comparators on the full physical space: +rotation, all three modes omega ~ q^2; +rotation+trace, both TT modes omega ~ q^3. Pre-registered outcome FAIL for the tested sets. Not shown: non-harmonic phases, derivative or non-linear constraint sets beyond those tested, other composites, anything for one qubit per site."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - one_qubit_per_slot_under_the_tensor_momentum_rule_an_exact_sum_rule_bounds_the_graviton_channel_by_q4_a_light_cone_mode_needs_an_incompressible_electric_pattern_bounded_theorem_note_2026-09-28
  - the_incompressible_tensor_pattern_exists_but_isotropy_ties_a_spin_two_fields_helicities_a_positive_models_first_order_graviton_carries_helicity_one_partners_bounded_theorem_note_2026-09-28
runner: scripts/the_photon_triplet_composites_partners_cannot_be_gapped_harmonically_and_constraints_removing_helicity_one_leave_no_tt_visible_first_moments_2026_09_28.py
---

# The photon-triplet composite's partners are not gapped by gauge-invariant local harmonic terms, and every tested local constraint set that removes the helicity-1 partners leaves no TT-visible first moments

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** exact symbol and integer checks, specified harmonic comparators;
pre-registered; unaudited. Revised after the first referee's FAILS verdict.
Independent checks are recorded below. Renamed on 2026-09-29 to a shorter file name, so that the audit
ledger's shard names fit the macOS filename limit; the content is
unchanged.

## In one paragraph

Probe 11 built a light-cone spin-2 pattern out of three photons. Its catch
was three extra, unwanted modes (partners) sitting in the photons: two with
helicity ±1 and one helicity-0 "transverse trace".

This probe asks whether the partners can be gapped or removed while the
composite keeps obeying the momentum rule.
- **Gapping.** In the simplest (harmonic) regime, with local terms, no:
  keeping the composite exact is the same as keeping each photon's own gauge
  law exact, and a local gauge-invariant energy cannot give a photon mode a
  gap.
- **Removing.** Every local constraint set tried that removes the helicity-1
  partners also removes every first moment the spin-2 channel could see:
  - a rotation constraint;
  - a rotation constraint plus a trace constraint;
  - a first-index Gauss law;
  - all 15 cubic-symmetric pointwise constraints.

  Without those first moments the spin-2 spring is two or more powers of q
  weaker, and the simplest versions give ω ∝ q² or q³.

The rotation constraint alone also leaves the helicity-0 partner. The first
version missed that.

## Pre-registration

Written in the probe's scratch file before any check was built.
- **PASS (route open)** if either:
  - (i) some local quadratic term consistent with exact E symmetry and
    G E = 0 gaps the partners, with helicity 2 still gapless and ω ∝ q; or
  - (ii) some exact local constraint set that removes the partners leaves
    compatible moves with TT-visible first moments.
- **FAIL** otherwise. The registration named the rotation constraint as the
  mechanism to test.

The first version read the rotation constraint as removing every partner.
It removes only the helicity ±1 ones (D). The revised test covers more
sets, and none gives PASS (ii).

**Outcome: FAIL for the tested sets.**

## Prior art

On main:
- **The 2026-09-14 tensor note:** the momentum rule on symmetric tensors,
  the moment lemma, the both-rules O(k³) class, and the statement that
  nonconstant quadratic energies do not descend to compact coordinates.
- **The 2026-09-21 coins'-frame note** (the records lane): local rotation
  invariance of a frame selects the teleparallel combination, blind to
  rotations only up to a divergence.

Of this PR: probe 11 (the composite; it already states the identity in A),
probe 10 (the moment lemma), probe 15.

External, reference only:
- **Xu and Hořava** (arXiv:1003.0009): the same vector-Gauss symmetric
  tensor has two TT modes and a scalar at z = 2, and a trace constraint
  removes the scalar, giving z = 3. This matches D, E and G here.
- **Xu (2006):** soft gravitons in a rotor model.
- **Gu and Wen** (arXiv:0907.1203): a qubit "L-type" model with only
  helicity ±2 at k³. Their linear "N-type" regime is uncontrolled.
- **Pretko** (arXiv:1604.05329): rank-2 U(1) constraints.
- **Tetrad and teleparallel linearised gravity:** local Lorentz symmetry
  there also needs the spin connection and the remaining gravitational
  constraints. The pointwise rotation constraint here is not that
  formulation.

## Premises (supplied)

- **The triplet.** Photon l's component j sits at x + s − e_l/2 + e_j/2,
  with s = (½, ½, ½).
- **The composite.** E_ij = Σ ε_ikl D_k A_lj, with A = A~ − I tr A~/2.
- **Harmonic regime.** Local quadratic forms: bounded, of finite range, with
  cross terms allowed.
- **The constraint sets tested:**
  - rotation: A~_lj = A~_jl, pointwise;
  - trace: Σ_l A~_ll = 0, pointwise;
  - first-index Gauss: Σ_l D_l A~_lj = 0;
  - the 15 cubic-covariant pointwise sets.

## A — exact symmetry of E is exact gauge invariance (check A)

- ε_mij E_ij equals photon m's Gauss law row for row: the difference is 0
  at 37 momenta, including axes, zone edges and corners. It follows from
  ε_mij ε_ikl = δ_jk δ_ml − δ_jl δ_mk.
- So E is exactly symmetric iff every photon's Gauss law holds. The premise
  forces exact U(1) gauge invariance.

## B — no gap from local harmonic terms (check B)

- By gauge invariance, the potential and the E–B cross block vanish at
  q = 0. With a bounded kinetic form, the Hamilton matrix is nilpotent
  there, so every frequency goes to zero as q → 0.
- 5 random local forms, with cross terms and higher-derivative curl
  kernels, have ω/|K| converging to finite positive constants.
- A Proca mass (gauge-breaking) gaps the photons. So would a non-local
  B(−Δ)⁻¹B term, which locality excludes.
- So no local gauge-invariant quadratic term gaps the partners. Such terms
  change speeds, or make modes softer.

## C — a fixed photon-index block touches helicity 2 (check C)

- The photon-z block removes only partner weight for q along z (overlap
  with helicity 2 exactly 0), but helicity-2 weight for q along x
  (overlap 1).
- This is a fixed-block check only. It does not cover derivative-dependent
  or cubic-covariant selectors.

## D — which constraint sets remove which partners (check D)

Each row counts the physical modes, those E sees, and those invisible to E
(the partners).

| Constraint set | Physical | Seen by E | Invisible to E |
| --- | --- | --- | --- |
| Gauss | 6 | 3 | 3 (helicity ±1 and the transverse trace) |
| + rotation | 3 | 2 | 1: the transverse trace K Kᵀ − K² I (overlap 1.000) |
| + rotation + trace | 2 | 2 | 0 (TT only) |
| + first-index Gauss | 4 | 3 | 1 |
| + first-index Gauss + trace | 3 | 3 | 0, but one non-TT mode stays physical |
| + trace alone | 5 | 3 | 2 (helicity ±1 kept) |

- The rotation constraint is pointwise: the two slots share a site. With it,
  on the symmetric embedding, the three Gauss laws equal the landed
  momentum rule exactly (difference 0 on the 4³ torus).
- So the rotation-constrained triplet is the landed symmetric tensor with
  only the momentum rule. That is probe 10's case, and Xu–Hořava's z = 2
  theory with its scalar.

## E — moves and their moments (check E)

Integer box kernels (4³ with float kernels for rotation + trace), with
moments taken at physical positions.

| Constraint set | Moves | First-moment rank | TT-visible first moment | Second-moment rank |
| --- | --- | --- | --- | --- |
| Gauss (2³) | 15 | 9 | yes (0.97) | 15 |
| + rotation (3³) | 15 | 0 | – | 6 |
| + rotation + trace (4³) | 14 | 0 | – | 0 |
| + first-index Gauss (3³) | 23 | 1, totally antisymmetric (ε) | no (1e-16) | 9 |
| + first-index Gauss + trace (3³) | 8 | 1, totally antisymmetric | no | 3 |

All zeroth moments vanish.

**For every box size, the first-index result.** For a finitely supported
move, the photon Gauss law (a divergence on the second index) makes the
first moment M_{lj,k} antisymmetric in (j, k). The first-index Gauss law
makes it antisymmetric in (l, k). A tensor antisymmetric in both pairs is
cyclic and antisymmetric, hence totally antisymmetric, so M ∝ ε_ljk. Then
M(q) ∝ ε_ljk q_k is antisymmetric in (l, j) and orthogonal to every
symmetric TT tensor. The boxes show that the space is exactly 1-dimensional
(3³) and occupied.

## F — all cubic-covariant pointwise constraint sets (check F)

The allowed values at each site form a union of the irreducible pieces of a
3×3 matrix under the cubic group: I (trace), E, T2 (off-diagonal symmetric)
and T1 (antisymmetric). With the photon Gauss laws:
- Every set that removes helicity ±1 and keeps a TT mode (I+T2, E+T2,
  I+E+T2) has no first-moment space at all.
- First moments need T1, and T1 brings helicity ±1 back, or leaves no TT
  mode.
- The unconstrained set has the full 9-dimensional first-moment space.

## G — harmonic comparators on the full physical space (check G)

A Maxwell-type kinetic term and the box-kernel moves, reduced on the whole
physical space with no hand projection:
- **+ rotation:** all three modes (TT and the transverse-trace partner)
  have ω ∝ q² (exponents 1.99–2.01 on axis, face and body directions);
- **+ rotation + trace:** both TT modes have ω ∝ q³ (exponents 2.999–3.000),
  the landed both-rules class and Xu–Hořava's z = 3.

## What this means

In the constructions tested:
- **Gapping does not work.** Exact symmetry of the composite is exact gauge
  invariance of the photons, and in the local harmonic regime no
  gauge-invariant term gaps a photon mode.
- **Removing the helicity-1 partners removes the TT channel's first moments
  too.** This holds for every tested constraint set: rotation, rotation plus
  trace, first-index Gauss, and all cubic-covariant pointwise sets.
- **The result is soft.** Rotation leaves the helicity-0 partner with ω ∝ q²
  (probe 10's case). Rotation plus trace leaves only TT, with ω ∝ q³ (the
  landed both-rules case).

Still open:
- non-harmonic phases;
- derivative or non-linear constraint sets beyond those tested;
- composites of another form;
- anything with one qubit per site.

## No-Go Discipline Gate

The bounded negative claims, inside the premises:
- (a) no gauge-invariant local quadratic term gaps the partners;
- (b) every tested constraint set that removes helicity ±1 leaves no
  TT-visible first moment;
- (c) the specified harmonic comparators are soft.

- **N1 — attack routes.** Each route, with its honesty marker.
  1. *A q⁰ gauge-invariant local potential or cross term.* ATTEMPTED (B:
     the nilpotency argument, and random local forms). Fails.
  2. *Softening E's symmetry.* ATTEMPTED (A: the row identity forces the
     Gauss laws). The route leaves the domain.
  3. *A fixed photon-index block.* ATTEMPTED (C). Fails for fixed blocks.
  4. *The rotation constraint.* ATTEMPTED (D, E, G). Removes helicity ±1,
     leaves no first moments, and keeps the helicity-0 partner. Fails.
  5. *Rotation plus trace.* ATTEMPTED (D, E, G). TT only, with no first or
     second moments and ω ∝ q³. Fails.
  6. *A first-index Gauss law, with or without trace.* ATTEMPTED (D, E, and
     the all-box-sizes argument). The only first moment is ε and
     TT-invisible. Fails.
  7. *Cubic-covariant pointwise sets.* ATTEMPTED (F, all 15). Fails.

  **Open routes:**
  - (i) non-harmonic phases;
  - (ii) derivative or non-linear constraints beyond those tested;
  - (iii) other composites;
  - (iv) non-compact links.
- **N2 — pairwise table, with directions.**
  - W1: exact E symmetry and G E = 0, equivalently exact photon Gauss laws
    (A).
  - W2: locality: finite range, bounded forms.
  - W3: the harmonic regime.
  - W4: the tested constraint families, imposed on top of W1.

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no: a non-local B(−Δ)⁻¹B term is gauge-invariant | no: a local Proca mass breaks gauge invariance | independent |
  | W1, W3 | no: gauge invariance allows anharmonic terms | no: harmonic forms can break it | independent |
  | W1, W4 | no: Gauss laws alone keep all partners (D) | yes: every W4 family includes the Gauss laws | W4 refines W1 |
  | W2, W3 | no: local anharmonic terms exist | no: non-local harmonic forms exist | independent |
  | W2, W4 | no: W2 restricts the Hamiltonian's range, W4 the constraints | no, for the same reason | independent |
  | W3, W4 | no: D–F are exact algebra without W3 | no: W3 does not select constraints | independent |

  The collapsed set is W1 (refined by W4 for (b)), W2 and W3. (a) uses W1,
  W2 and W3; (b) uses W4 only; (c) uses W3 and W4.
- **N3 — hidden-wall scan.** The scan hits, and how each is classified:
  - "harmonic": explicit as W3.
  - "local": explicit as W2.
  - "box": the moment statements are proved for all box sizes where D and
    E's arguments apply. The first-index case is proved above, and the
    rotation case by probe 10's lemma. The boxes only exhibit the moves.
  - "specified comparator": G, not load-bearing for (a) or (b).
  - "cubic-covariant": F's scope, explicit.
- **N4 — residual matching.**

  | Citation (path:line) | Residual attacked | Residual status here | Match |
  | --- | --- | --- | --- |
  | docs/THE_INCOMPRESSIBLE_TENSOR_PATTERN_EXISTS_BUT_ISOTROPY_TIES_A_SPIN_TWO_FIELDS_HELICITIES_A_POSITIVE_MODELS_FIRST_ORDER_GRAVITON_CARRIES_HELICITY_ONE_PARTNERS_BOUNDED_THEOREM_NOTE_2026-09-28.md:101 | the composite and its partners | re-verified (A); partner types corrected (D) | yes |
  | docs/ONE_QUBIT_PER_SLOT_UNDER_THE_TENSOR_MOMENTUM_RULE_AN_EXACT_SUM_RULE_BOUNDS_THE_GRAVITON_CHANNEL_BY_Q4_A_LIGHT_CONE_MODE_NEEDS_AN_INCOMPRESSIBLE_ELECTRIC_PATTERN_BOUNDED_THEOREM_NOTE_2026-09-28.md:134 | a symmetric divergence-free move with a first moment | re-verified in the triplet embedding (E) | yes |
  | docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md:186 | the both-rules O(k³) class | matched by G, rotation + trace | yes |

  All are unaudited parents.
- **N5 — rhetoric audit.**

  | Phrase | per_element | per_site | per_mode | per_block | lattice_wide |
  | --- | --- | --- | --- | --- | --- |
  | "not gapped" | the row identity at 37 momenta | not applicable (symbol level) | six modes, 5 random local forms | not applicable | holds for all local bounded gauge-invariant forms, by the nilpotency argument |
  | "no TT-visible first moments" | each move's moments | every constraint row touching the boxes | not applicable | five box kernels, 15 pointwise sets | proved for all box sizes for the rotation and first-index families; untested families are open |
  | "soft comparators" | not applicable | not applicable | 3 + 2 modes, three directions, three momenta | the box kernels as moves | specified models only |

- **N6 — primitive scan.** The registry's minimal_axioms fixes M₂(C) per
  site. No primitive supplies the triplet's spin slots or non-compact
  links, and none is invoked.
- **N7 — steelman, in a hostile reviewer's voice.** "The note tests
  pointwise constraints, one first-index divergence law and their unions.
  A derivative constraint that removes helicity ±1 only at small q, or a
  non-linear one, is not excluded. Gu and Wen (arXiv:0907.1203) report a
  linear graviton from a qubit model in their N-type regime; if it holds,
  the composite route is not closed. The terminal obligation for a no-go
  is a classification of every local linear constraint module on the
  triplet, which is not attempted." This is convincing against a broad
  no-go, so none is claimed. (a)–(c) concern only the tested sets.
- **N8 — cross-cycle echo.**

  | Prior wall | Retired? | Mechanism that would retire it | Applies here? |
  | --- | --- | --- | --- |
  | probe 11's partner dichotomy | no | a partner-removing constraint with TT-visible first moments | not found in the tested sets |
  | probe 10's O(q⁴) potential bound | no | an incompressible state or a non-diagonal momentum | not tested here |
  | the landed both-rules O(k³) class, and Xu–Hořava's z = 3 | no | non-compact slots | outside the premise |
  | the 2026-09-21 teleparallel combination | not a wall | invariance up to a divergence, as a polynomial | no: polynomials do not descend to compact links |

- **Outcome.** PASS as scoped for (a)–(c). The broader no-go is withheld by
  N7. The pre-registered outcome is FAIL for the tested sets.

## Independent checks

- **gpt-5.6-sol (other vendor), first round: FAILS.** Its findings, and how
  this version answers each:
  1. The rotation constraint leaves the transverse trace. Confirmed (D,
     overlap 1.000). Title, scope and text are corrected, and G now reduces
     on the full physical space.
  2. The no-gap class needed locality, and cross terms. B is restated for
     local bounded forms with cross terms and higher derivatives, with a
     Proca control.
  3. The gate did not follow its contract. Rewritten.
  4. C is a fixed-block check. Scoped.
  5. A and the moment algebra were confirmed exactly.
  6. The first-index Gauss law was settled by the referee. It keeps an
     antisymmetric, TT-invisible first moment, with or without the trace.
     Reproduced in E.
  7. Prior art: Xu–Hořava, Gu–Wen, Pretko. Added; the tetrad
     identification is withdrawn.
- **Fable check (same family), first version: STANDS WITH CORRECTIONS.**
  - The same main correction: a helicity-0 partner survives the rotation
    constraint.
  - A exact from ε-algebra.
  - B holds in a broader class.
  - It supplied the 15 cubic pointwise sets (reproduced in F) and the
    rotation + trace second-moment loss (reproduced in E).
- **gpt-5.6-sol, fourth round: CONFIRMED AS REVISED.** The third round's two integration items (the runner docstring and a map link) were fixed.
- **gpt-5.6-sol, second round: STANDS WITH CORRECTIONS.**
  - It confirmed all the new material independently: D's six rows by
    exact ranks, E's ranks (and the 4³ nullity by modular ranks), F's 15
    dimensions, and G's exponents.
  - Its corrections are applied here:
    - the title says "gauge-invariant" (a local Proca mass does gap);
    - the gate has per-route markers, directional N2 rationales, full
      N4 paths and lines, a hostile N7 and N8 dispositions;
    - the first-index result is proved for all box sizes;
    - the lattice_wide certificate line is restated.

## Reproduction

`python3 scripts/the_photon_triplet_composites_partners_cannot_be_gapped_harmonically_and_constraints_removing_helicity_one_leave_no_tt_visible_first_moments_2026_09_28.py`
prints 7 checks, A–G, the N5 lines and TOTAL, in about 2 s. The canonical
cache is at
logs/runner-cache/the_photon_triplet_composites_partners_cannot_be_gapped_harmonically_and_constraints_removing_helicity_one_leave_no_tt_visible_first_moments_2026_09_28.txt.
