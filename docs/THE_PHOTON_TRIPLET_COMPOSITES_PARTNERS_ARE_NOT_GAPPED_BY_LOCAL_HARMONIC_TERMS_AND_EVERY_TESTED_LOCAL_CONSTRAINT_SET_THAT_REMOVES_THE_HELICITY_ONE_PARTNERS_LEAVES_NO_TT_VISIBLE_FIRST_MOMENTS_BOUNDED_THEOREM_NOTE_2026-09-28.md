---
claim_id: the_photon_triplet_composites_partners_are_not_gapped_by_local_harmonic_terms_and_every_tested_local_constraint_set_that_removes_the_helicity_one_partners_leaves_no_tt_visible_first_moments_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Probe 11's composite E = curl_1(A~ - I tr A~/2) of a photon triplet (electric components A~_lj, vector potentials a_lj), on probe 11's placement. (A) eps_mij E_ij equals photon m's Gauss law row for row (exact at 37 momenta incl. axes, zone edges and corners), so exact E symmetry is exact U(1) gauge invariance of every photon. (B) Harmonic regime with local forms (bounded local kinetic form; finite-range potential in the curls, higher-derivative kernels allowed; finite-range E-B cross terms): every frequency -> 0 as q -> 0, so no such term gaps the partners; a Proca mass (gauge-breaking) or a non-local B(-Delta)^-1 B term would gap them. (C) A fixed photon-index block removes only partner weight for q along z but helicity-2 weight for q along x (fixed-block check only). (D) Constraint sets, physical / seen by E / invisible to E: Gauss 6/3/3; +rotation (A~_lj = A~_jl, pointwise) 3/2/1, the invisible mode being the transverse trace K K^T - K^2 I (a helicity-0 partner survives); +rotation+trace 2/2/0; +first-index Gauss 4/3/1; +first-index Gauss+trace 3/3/0; +trace alone keeps helicity +-1. With the rotation constraint the Gauss laws equal the landed momentum rule exactly (4^3 torus). (E) Moves (box kernels): Gauss only, TT-visible first moments (rank 9); +rotation, zeroth and first moments 0; +rotation+trace (4^3 box), second moments 0 too; +first-index Gauss, one first moment, totally antisymmetric and TT-invisible, with or without the trace. (F) All 15 cubic-covariant pointwise constraint sets: every set that removes helicity +-1 and keeps a TT mode has no first-moment space. (G) Harmonic comparators on the full physical space: +rotation, all three modes omega ~ q^2; +rotation+trace, both TT modes omega ~ q^3. Pre-registered outcome FAIL for the tested sets. Not shown: non-harmonic phases, derivative or non-linear constraint sets beyond those tested, other composites, anything for one qubit per site."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - one_qubit_per_slot_under_the_tensor_momentum_rule_an_exact_sum_rule_bounds_the_graviton_channel_by_q4_a_light_cone_mode_needs_an_incompressible_electric_pattern_bounded_theorem_note_2026-09-28
  - the_incompressible_tensor_pattern_exists_but_isotropy_ties_a_spin_two_fields_helicities_a_positive_models_first_order_graviton_carries_helicity_one_partners_bounded_theorem_note_2026-09-28
runner: scripts/the_photon_triplet_composites_partners_cannot_be_gapped_harmonically_and_constraints_removing_helicity_one_leave_no_tt_visible_first_moments_2026_09_28.py
---

# The photon-triplet composite's partners are not gapped by local harmonic terms, and every tested local constraint set that removes the helicity-1 partners leaves no TT-visible first moments

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** exact symbol and integer checks, specified harmonic comparators;
pre-registered; unaudited. Revised after the first referee's FAILS verdict.
Independent checks are recorded below.

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
- (a) no local gauge-invariant quadratic term gaps the partners;
- (b) every tested constraint set that removes helicity ±1 leaves no
  TT-visible first moment;
- (c) the specified harmonic comparators are soft.

- **N1 — attack routes.** Seven distinct routes, all ATTEMPTED here.
  1. *A q⁰ gauge-invariant local potential or cross term.* Attempted in B.
     Fails.
  2. *Softening E's symmetry.* Attempted in A: the identity forces the Gauss
     laws. The route leaves the domain.
  3. *A fixed photon-index block.* Attempted in C: it touches helicity 2 in
     some direction. Fails for fixed blocks.
  4. *The rotation constraint.* Attempted in D, E and G: helicity ±1
     removed, no first moments, the helicity-0 partner kept. Fails.
  5. *Rotation plus trace.* Attempted in D, E and G: TT only, O(q³). Fails.
  6. *A first-index Gauss law, with or without trace.* Attempted in D and E:
     the only first moment is antisymmetric and TT-invisible. Fails.
  7. *Cubic-covariant pointwise sets.* Attempted in F, all 15. Fails.

  **Open routes:**
  - (i) non-harmonic phases;
  - (ii) derivative or non-linear constraints beyond those tested;
  - (iii) other composites;
  - (iv) non-compact links.
- **N2 — pairwise table.**
  - W1: exact E symmetry and G E = 0.
  - W2: locality (finite range, bounded forms).
  - W3: the harmonic regime.
  - W4: the tested constraint families.

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no | no | independent |
  | W1, W3 | no | no | independent |
  | W1, W4 | no | no: the constraint sets are added on top of W1 | independent |
  | W2, W3 | no | no | independent |
  | W2, W4 | no | no | independent |
  | W3, W4 | no | no: D, E and F do not use W3; G does | independent |

- **N3 — hidden conditions.** All now explicit:
  - locality for B;
  - the tested constraint families for (b);
  - box sizes;
  - the specified comparators in G.
- **N4 — residual matching.**

  | Citation (path:line) | Residual attacked | Residual status here | Match |
  | --- | --- | --- | --- |
  | probe 11 note (docs/THE_INCOMPRESSIBLE_TENSOR_PATTERN_EXISTS_..._2026-09-28.md):101 | the composite and its partners | re-verified (A), with the partner types corrected (D) | yes |
  | probe 10 note (docs/ONE_QUBIT_PER_SLOT_..._2026-09-28.md):134 | a symmetric divergence-free move with a first moment | re-verified in the triplet embedding (E) | yes |
  | 2026-09-14 note (docs/LOCAL_FINITE_CLOCK_TENSOR_..._2026-09-14.md):186 | the both-rules O(k³) class | matched by G, rotation + trace | yes |

  All are unaudited parents.
- **N5 — rhetoric audit.**

  | Phrase | per_element | per_site | per_mode | per_block | lattice_wide |
  | --- | --- | --- | --- | --- | --- |
  | "not gapped" | the row identity at 37 momenta | – (symbol level: not applicable) | six modes, 5 random local forms | – (not applicable) | holds for all local bounded forms, by the nilpotency argument |
  | "no TT-visible first moments" | each move's moments | every constraint row touching the boxes | – (not applicable) | five box kernels, 15 pointwise sets | a moment statement, box-size independent for the tested families; untested families are open |
  | "soft comparators" | – (not applicable) | – (not applicable) | 3 + 2 modes, three directions, three momenta | the box kernels as moves | specified models only |

- **N6 — primitive scan.** The registry's minimal_axioms fixes M₂(C) per
  site. No primitive supplies the triplet's spin slots or non-compact links,
  and none is invoked.
- **N7 — steelman.** A non-harmonic, cubic-covariant phase, or a derivative
  constraint not tested here, might remove the partners and keep a light
  cone. That is convincing against a broad no-go, so none is claimed.
- **N8 — cross-cycle echo.**
  - Probe 11's partner dichotomy: sharpened.
  - Probe 10's bound: reached again.
  - The landed both-rules O(k³) class and Xu–Hořava's z = 3: matched by
    rotation plus trace.
  - The 2026-09-21 teleparallel mechanism (invariance up to a divergence):
    not tested here for compact links.
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
- Second rounds: pending.

## Reproduction

`python3 scripts/the_photon_triplet_composites_partners_cannot_be_gapped_harmonically_and_constraints_removing_helicity_one_leave_no_tt_visible_first_moments_2026_09_28.py`
prints 7 checks, A–G, the N5 lines and TOTAL, in about 2 s. The canonical
cache is at
logs/runner-cache/the_photon_triplet_composites_partners_cannot_be_gapped_harmonically_and_constraints_removing_helicity_one_leave_no_tt_visible_first_moments_2026_09_28.txt.
