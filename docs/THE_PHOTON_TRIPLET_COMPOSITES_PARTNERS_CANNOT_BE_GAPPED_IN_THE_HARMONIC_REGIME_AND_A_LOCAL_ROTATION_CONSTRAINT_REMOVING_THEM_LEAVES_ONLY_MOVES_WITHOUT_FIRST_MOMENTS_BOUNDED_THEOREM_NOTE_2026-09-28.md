---
claim_id: the_photon_triplet_composites_partners_cannot_be_gapped_in_the_harmonic_regime_and_a_local_rotation_constraint_removing_them_leaves_only_moves_without_first_moments_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Probe 11's composite E = curl_1(A~ - I tr A~/2) of a photon triplet (photon l's electric components A~_lj, vector potentials a_lj), on probe 11's placement. (A) At 30 sampled zone momenta the antisymmetric part of E and the three photon Gauss laws span the same 3-dimensional row space, so E is exactly symmetric iff every photon's Gauss law holds. (B) Harmonic regime: for quadratic Hamiltonians with a bounded positive kinetic form on A~ and a potential depending on a only through the photons' curls (as the Gauss laws require), every physical mode has omega -> 0 as q -> 0; for 5 random positive local forms all six have omega/|K| converging to positive constants. No such quadratic term gaps the helicity +-1 and 0 partners. (C) A photon-index-selective mechanism (acting on photon z) removes only partner weight for q along z but removes helicity-2 weight for q along x. (D) The local rotation constraint A~_lj = A~_jl (the two slots share a site) makes A~ a symmetric tensor on the landed placement shifted by s; on that embedding the three Gauss laws equal the landed momentum rule exactly (4^3 torus). On boxes, Gauss-only moves keep first moments (rank 9), while Gauss+rotation moves have vanishing zeroth and first moments and nonzero second moments; so exactly invariant periodic potentials are move-built with probe 10's O(q^4) form factor. (E) In the specified harmonic comparator (Maxwell-type kinetic on symmetric A~, Gauss+rotation box-kernel moves) both TT modes have omega ~ q^2. Pre-registered outcome FAIL. Not shown: non-harmonic mechanisms (confinement, partial Higgs phases), other partner-removing constraint sets, a light-cone graviton, or anything for one qubit per site."
upstream_dependencies:
  - minimal_axioms
  - local_finite_clock_tensor_constraints_cubic_dispersion_and_linear_gravity_boundaries_bounded_theorem_note_2026-09-14
  - one_qubit_per_slot_under_the_tensor_momentum_rule_an_exact_sum_rule_bounds_the_graviton_channel_by_q4_a_light_cone_mode_needs_an_incompressible_electric_pattern_bounded_theorem_note_2026-09-28
  - the_incompressible_tensor_pattern_exists_but_isotropy_ties_a_spin_two_fields_helicities_a_positive_models_first_order_graviton_carries_helicity_one_partners_bounded_theorem_note_2026-09-28
runner: scripts/the_photon_triplet_composites_partners_cannot_be_gapped_harmonically_and_a_rotation_constraint_leaves_only_moves_without_first_moments_2026_09_28.py
---

# The photon-triplet composite's partners cannot be gapped in the harmonic regime, and a local rotation constraint that removes them leaves only moves without first moments

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** exact symbol and integer checks, specified harmonic comparators;
pre-registered; unaudited. Independent checks are recorded below.

## In one paragraph

Probe 11 built a light-cone spin-2 pattern out of three photons. Its catch
was three extra, unwanted modes (partners) sitting in the photons.

This probe asks whether the partners can be gapped or removed while the
composite keeps obeying the momentum rule. In the simplest (harmonic)
regime, no local term can gap them: keeping the composite exact is the same
as keeping each photon's own gauge law exact, and a gauge-invariant energy
cannot give a photon mode a gap.

Removing them with a local constraint that ties the photons' labels to the
directions (a rotation constraint) does work as a removal. But it turns the
three photons into the same tensor field, with the same momentum rule, as
probe 10. The allowed moves then lose their first moments, and the
spring side is two powers of q weaker again.

So in the constructions tested, the composite route either keeps gapless
partners or becomes probe 10's soft case.

## Pre-registration

Written in the probe's scratch file before any check was built.
- **PASS (route open)** if either:
  - (i) some local quadratic term consistent with exact E symmetry and
    G E = 0 gaps the partners, with helicity 2 still gapless and ω ∝ q
    (harmonic regime); or
  - (ii) some exact local constraint set that removes the partners leaves
    compatible moves with TT-visible first moments.
- **FAIL** if (i) all six modes stay gapless with ω ∝ q, and (ii) under the
  local rotation constraint the compatible moves have vanishing zeroth and
  first moments.
- The rotation constraint is the tested removal mechanism; other constraint
  sets are noted, not exhausted.

**Outcome: FAIL.**

## Prior art

On main:
- **The 2026-09-14 tensor note.** The momentum rule on symmetric tensors,
  the moment lemma for divergence-free symmetric patterns, and the
  statement that nonconstant quadratic energies do not descend to compact
  coordinates (also in the 2026-09-24 note).
- **The 2026-09-21 coins'-frame note** (the records lane). In a continuum
  ansatz, local rotation invariance of a frame with curl field strength
  selects the teleparallel combination, blind to rotations only up to a
  divergence. That combination is a polynomial, and it is used there for
  the frame field, not for compact quantum links.

Of this PR:
- probe 11 (the composite, its exact identities, the partner count);
- probe 10 (the q⁴ sum rule and the moment lemma on the landed complex);
- probe 15 (the ker G box kernel, 15 moves on a 3³ box, the same count as
  D here).

External, reference only:
- tetrad and teleparallel formulations of linearised gravity: a symmetric
  part of a vector-potential triplet with local rotations;
- quantum links (Chandrasekharan and Wiese).

## Premises (supplied)

- **The triplet.** Three photons with electric components A~_lj and vector
  potentials a_lj, on probe 11's placement. Photon l's component j sits at
  x + s − e_l/2 + e_j/2, with s = (½, ½, ½).
- **The composite.** E_ij = Σ ε_ikl D_k A_lj, with A = A~ − I tr A~/2.
- **Harmonic regime.** A quadratic Hamiltonian with a bounded positive
  kinetic form on A~ and a potential in the photons' curls.
- **The rotation constraint.** A~_lj = A~_jl, pointwise. The two slots sit at
  the same site: x + s + (e_j − e_l)/2.

## A — exact symmetry of E is exact gauge invariance (check A)

- At 30 random zone momenta, the antisymmetric part of E (three rows) and
  the three photon Gauss rows span the same 3-dimensional space.
- So E is exactly symmetric iff each photon's Gauss law holds. (Probe 11
  showed one direction; this is the converse.)
- The premise "E symmetric with G E = 0" therefore forces exact U(1) gauge
  invariance of each photon. In particular the potential can depend on the
  a_l only through their curls.

## B — no gap in the harmonic regime (check B)

- A gauge-invariant potential vanishes at q = 0, because the curls do.
- So with a bounded kinetic form every physical frequency goes to zero as
  q → 0.
- For 5 random positive local forms (the kinetic form with q-dependent
  parts; the potential on the curls), all six physical modes have ω/|K|
  converging to positive constants between 1.16 and 3.36.
- No quadratic term of this kind gaps the helicity ±1 and 0 partners. It
  can only change their speeds.

## C — photon-index-selective mechanisms touch helicity 2 (check C)

A mechanism acting on one photon index, such as confining photon z:
- removes only partner weight for q along z (overlap with helicity 2:
  exactly 0);
- but removes helicity-2 weight for q along x (overlap 1).

With cubic symmetry the three photons are alike, so such a mechanism acts
on all of them. This is a statement about index-selective mechanisms. It is
not a theorem about every non-harmonic phase.

## D — the rotation constraint gives the landed tensor complex, and its moves lose first moments (check D)

- The rotation constraint is local and pointwise. On the symmetric
  embedding, A~_ll(x) = p_ll(x) and A~_ij(c + e_i) = A~_ji(c + e_j) =
  p_face(ij)(c). There the three Gauss laws equal the landed momentum rule
  exactly: the difference is 0 on the 4³ torus.
- So the rotation-constrained triplet is the landed symmetric tensor, with
  the momentum rule on its electric side (probe 10's assignment), with the
  placement shifted by s.
- **Moves** (integer box kernels, with moments taken at physical positions):
  - Gauss only, 2³ box: 15 moves, zero zeroth moments, first-moment rank 9
    (loop dipoles, which is why photons are linear);
  - Gauss plus rotation, 3³ box: 15 moves, all symmetric, zero zeroth and
    first moments, second-moment rank 6.
- So exactly invariant periodic potentials are move-built with probe 10's
  O(q⁴) form factor.
- The polynomial teleparallel combination is invariant only up to a
  divergence, as a polynomial. Like Einstein–Hilbert, it does not descend
  to compact link variables (the landed statement).

## E — the rotation-constrained harmonic comparator is soft (check E)

A Maxwell-type kinetic term on symmetric A~, and a potential from the
Gauss-plus-rotation box-kernel moves:
- both TT modes have ω ∝ q², with fitted exponents 1.996–2.002 on the axis,
  face, body and a generic direction;
- this is the same order as probe 15's row for probe 14's assignment.

## What this means

In the constructions tested:
- **The composite route keeps its partners.** Exact symmetry of the
  composite is exact gauge invariance of the photons, and in the harmonic
  regime no gauge-invariant term gaps a photon mode.
- **Removing the partners with the local rotation constraint turns the
  triplet into the landed tensor theory,** with the momentum rule on the
  diagonal variable. That is probe 10's case, and it is soft in the
  harmonic comparator.

This matches the panel's expectation that the composite and tensor routes
are linked. The link found here is the rotation constraint.

Still open:
- non-harmonic phases (confinement or partial Higgs phases that are not
  index-selective);
- constraint sets other than the rotation constraint;
- composite metrics built differently;
- anything with one qubit per site.

## No-Go Discipline Gate

The bounded negative claims, inside the premises:
- (a) in the harmonic regime, no quadratic term compatible with exact E
  symmetry gaps the partners;
- (b) under the rotation constraint, the compatible moves have vanishing
  zeroth and first moments (an O(q⁴) form factor), and the specified
  harmonic comparator has ω ∝ q².

Not claimed: that no mechanism removes the partners and keeps a light cone.

- **N1 — attack routes.** Six distinct routes, all ATTEMPTED here.
  1. *A q⁰ gauge-invariant potential.* Attempted in B: the curls vanish at
     q = 0. Fails.
  2. *Kinetic-form engineering (q-dependent kinetic terms).* Attempted in B
     with random q-dependent forms: all modes stay gapless. Fails.
  3. *Softening E's symmetry, so the Gauss laws need not hold exactly.*
     Attempted in A: the premise forces them. The route leaves the domain.
  4. *Photon-index-selective gapping.* Attempted in C: it touches helicity 2
     in some direction. Fails for index-selective mechanisms.
  5. *A rotation constraint that keeps first moments.* Attempted in D: the
     moves are symmetric, so their first moments vanish (rank 0). Fails.
  6. *A different embedding of the constrained triplet.* Attempted in D: the
     identification with the landed momentum rule is exact. Fails.

  **Open routes (consistent with (a) and (b)):**
  - (i) non-harmonic phases that are not index-selective;
  - (ii) other partner-removing constraint sets, for example a
    first-index Gauss law;
  - (iii) composite metrics not of probe 11's form;
  - (iv) non-compact links.
- **N2 — pairwise table.**
  - W1: exact E symmetry and G E = 0.
  - W2: the harmonic regime.
  - W3: fixed range and uniform norms.
  - W4: the rotation constraint as the removal mechanism (for (b)).

  | Pair | First closes second? | Second closes first? | Relation |
  | --- | --- | --- | --- |
  | W1, W2 | no | no | independent |
  | W1, W3 | no | no | independent |
  | W1, W4 | no | yes: W4 with the Gauss laws keeps E symmetric | W4 is compatible with W1 |
  | W2, W3 | no | no | independent |
  | W2, W4 | no | no | independent |
  | W3, W4 | no | no | independent |

- **N3 — hidden conditions.** All now explicit:
  - the harmonic regime for (a);
  - the rotation constraint as the only tested removal mechanism;
  - box sizes (2³, 3³);
  - the comparator in E is a specified model.
- **N4 — residual matching.**

  | Citation (path:line) | Residual attacked | Residual claimed closed here | Match |
  | --- | --- | --- | --- |
  | probe 11 note (docs/THE_INCOMPRESSIBLE_TENSOR_PATTERN_EXISTS_..._2026-09-28.md):101 | the composite and its partner count | none; A adds the converse | yes |
  | probe 10 note (docs/ONE_QUBIT_PER_SLOT_..._2026-09-28.md):134 | a symmetric divergence-free move with a first moment | none; D re-checks it in the triplet embedding | yes |
  | 2026-09-14 note (docs/LOCAL_FINITE_CLOCK_TENSOR_..._2026-09-14.md):225 | a compact descent of a quadratic polynomial | none; cited for D's last bullet | yes |

  All are unaudited parents, not retained authorities.
- **N5 — rhetoric audit.**

  | Phrase | Resolutions tested | Holds at untested ones? |
  | --- | --- | --- |
  | "cannot be gapped" | per_mode (six modes, five random forms); the symbol argument for all quadratic forms of the stated kind | harmonic regime only |
  | "loses first moments" | per_block (3³ box kernel); per_element (each move's moments) | the lemma is general for symmetric divergence-free patterns (probe 10 T2) |
  | "soft comparator" | per_mode (two TT modes, four directions, four momenta) | specified model only |

  The runner prints the certificate lines.
- **N6 — partial closure and primitive scan.**
  - The registry lists minimal_axioms (Qubit fixes M₂(C) per site) and
    three unrelated primitives.
  - No primitive supplies non-compact links or a rotation constraint.
  - The triplet's spin slots are supplied, outside the Qubit axiom.
  - No convention closes (a) or (b).
- **N7 — steelman.** Some non-harmonic, cubic-covariant phase might gap
  exactly the partners, for instance through their different coupling to
  a matter sector. Or another constraint set might remove them while
  leaving first moments. This is convincing against a broad no-go, so none
  is claimed. Routes (i) and (ii) are the natural next targets.
- **N8 — cross-cycle echo.**
  - **Probe 11's partner dichotomy:** sharpened, not retired.
  - **Probe 10's potential-side bound:** reached again through the rotation
    constraint.
  - **The 2026-09-21 coins'-frame teleparallel result:** its polynomial
    combination is the continuum object whose compact descent fails. Its
    mechanism (invariance up to a divergence) does not transfer to periodic
    link energies.
- **Outcome.** PASS as scoped for (a) and (b). The broader no-go is withheld
  by N7. The pre-registered outcome is FAIL.

## Independent checks

Pending.

## Reproduction

`python3 scripts/the_photon_triplet_composites_partners_cannot_be_gapped_harmonically_and_a_rotation_constraint_leaves_only_moves_without_first_moments_2026_09_28.py`
prints 5 checks, A–E, the N5 lines and TOTAL, in under 1 s. The canonical
cache is at
logs/runner-cache/the_photon_triplet_composites_partners_cannot_be_gapped_harmonically_and_a_rotation_constraint_leaves_only_moves_without_first_moments_2026_09_28.txt.
