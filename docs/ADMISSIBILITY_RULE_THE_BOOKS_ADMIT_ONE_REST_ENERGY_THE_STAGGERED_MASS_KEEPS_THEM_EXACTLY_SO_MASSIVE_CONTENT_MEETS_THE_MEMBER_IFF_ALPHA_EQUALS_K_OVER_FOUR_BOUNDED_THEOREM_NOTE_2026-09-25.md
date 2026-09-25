---
claim_id: admissibility_rule_the_books_admit_one_rest_energy_the_staggered_mass_keeps_them_exactly_so_massive_content_meets_the_member_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: 'WITHIN block 54''s walk H = sum_a sigma_a S_a at a uniform rate, block 73''s two-step momentum and
  block 77''s staggered rest energy m eps (eps(x) = (-1)^(x1+x2+x3)), as landed on main and supplied, with blocks
  119, 136 and 137 (open) placed. Exact: (T1) with H + m eps the averaged energy e''_m = C_1 C_2 C_3 Re psi^dag
  (H + m eps) psi still obeys de''_m/dt = - sum_j dbar_j P''''_j with the same carried two-step momentum, and both
  momentum laws of block 136 keep their stresses: a massive walker keeps the books on Z^3 (operators over Q(i) on
  6^3 and 10^3). (T2) for a site term M the energy law''s defect is linear in M; among the eight terms 1, eps, sigma_a,
  eps sigma_a it vanishes only for eps, and the other seven defects are independent: with the two-step momentum
  within this eight-dimensional real span, the fixed energy law admits only multiples of the staggered term, the
  staggered mass. (T3) m eps anticommutes with H, so (H + m eps)^2 = H^2 + m^2 and each wave''s energy current is
  its two-step momentum at every k; a uniform coin mass shifts the current; a constant offset adds the velocity,
  which is not conserved, so no finite-range zero-vacuum stress can give the double-divergence identity with an
  offset while preserving this energy first moment. (T4) so, with block 136''s bond shift at beta = -alpha, the
  specified massive sources preserve the initially satisfied nonzero-mode constraints for all states iff alpha =
  K/4. The supervisor''s own derivation (Claude Opus 5.5), checked by its runner; not refereed by another model
  family. Nothing adopted; no gravitational claim.'
upstream_dependencies:
- admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
- admissibility_rule_one_record_per_site_keeps_the_books_only_at_leading_order_two_excluded_records_lose_their_energy_current_in_two_and_three_dimensions_bounded_theorem_note_2026-09-25
- admissibility_rule_the_axioms_own_generator_the_scalar_hop_splits_the_eight_species_into_four_levels_of_one_sense_and_a_staggered_term_gives_them_mass_bounded_theorem_note_2026-09-22
- admissibility_rule_the_two_step_momentum_is_the_only_one_among_conserved_covariant_momenta_of_reach_two_that_is_every_species_own_wave_number_bounded_theorem_note_2026-09-21
- admissibility_rule_two_step_content_keeps_symmetric_books_where_the_member_keeps_its_fields_and_a_bond_shift_keeps_every_constraint_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
runner: scripts/admissibility_rule_the_books_admit_one_rest_energy_the_staggered_mass_keeps_them_exactly_so_massive_content_meets_the_member_iff_alpha_equals_k_over_four_2026_09_25.py
---

# Staggered mass preserves the supplied conservation laws; a bounded site-term classification

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact within the landed walk, two-step momentum and staggered rest energy, with blocks 119, 136 and 137 placed; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 54, 73 and 77 as landed on main (the walk, the two-step momentum and the staggered rest energy), with blocks 119, 136 and 137 placed; it reports which rest energies keep the books that the member needs; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Blocks 135 and 136 (open) showed that the massless walker keeps exact books in the member's placement, and block 137 (open) showed that one record per site does not. Block 77 (landed) gave the walker a rest energy through a staggered term `mε`, and block 119 (open) found that this is the only rest energy a full coin frame admits. Does a massive walker keep the books?

- **T1: yes, exactly.** With `mε`, the averaged energy still flows exactly as the same carried two-step momentum. Both momentum laws keep their stresses. So a massive walker keeps the books, for every state.
- **T2: it is the only site term that does.** Among the eight site terms `1, ε, σ_a, εσ_a`, only `ε` keeps the energy law with the two-step momentum. A constant offset, a uniform coin mass and a staggered coin mass each break it.
- **T3: why.**
  - `mε` anticommutes with the walk, so the squared energy is `|sin k|² + m²`, and each wave's energy current is its two-step momentum at every `k`, massive or not.
  - A uniform coin mass shifts one component of `sin k`.
  - A constant offset adds the velocity to the current. The velocity is not conserved, so no finite-range zero-vacuum stress can give the double-divergence identity with an offset while preserving this energy first moment.
- **T4: the light cone does not move.** The specified massive sources preserve the initially satisfied nonzero-mode constraints for all states, with block 136's bond shift, iff `α = K/4`. The massive walker's waves are slower than `w̄`, but its books carry the same coefficient `w̄²`.

The staggered mass preserves the specified identities. The uniqueness result concerns the fixed density, momentum, averaging and eight-dimensional site-term family. It does not fix a physical zero of energy or classify arbitrary site potentials, other densities, or field couplings.

## Premises and declared objects

Take real m (zero allowed) and even periodic tori or the infinite cubic lattice. T4 uses K, α, w̄ positive, p nonzero, β = −α, the explicit phase pullback and initially satisfied constraints of the reviewed block 136; zero modes and interacting coupling are not solved. Infinite dipole comparisons use finite-support states. Site-term classification means V(x) = A + ε(x)B with constant Hermitian two-by-two A,B, not arbitrary site dependence. At uniform rate w̄ multiply H+mε, energy and stress by w̄; Q, P″ and P^B retain their unit-rate definitions.


- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, its rest energy, the currents and their placements, the member and the source link are supplied clauses. Nothing is adopted.
- **The walk with rest energy** (blocks 54 and 77 as landed). `H + mε`, with `ε(x) = (−1)^{x₁+x₂+x₃}`, at a uniform rate.
- **Densities** (block 136).
  - `e′_m = C₁C₂C₃ Re ψ†(H + mε)ψ`.
  - `P″_j = φ_jᵀ Re ψ†P_jψ`, with `P_j = S_jC_j` (block 73: a normalized covariant conserved momentum in the reviewed reach-two class).
  - `Θ_ij = φ_jᵀK_i^j`, and `Q_j` as in block 136.
- **Site terms.** `M = Σ_x|x⟩⟨x| ⊗ V(x)` with `V(x) ∈ {1, ε(x), σ_a, ε(x)σ_a}`.
- **The member** (block 136 T4): with a bond shift at `β = −α`, the clock constraint is kept iff `ė_u = (Kw̄²/(4α)) p·P`.
- **Comparators, named only:** the equality of energy current and momentum for massive waves in the comparator (its dispersion `E² = p² + m²`); a mass term that anticommutes with the massless generator.

## Theorem T1 — the staggered mass keeps the books

*Statement.* For every state on `ℤ³`:
- `i[H + mε, e′_m] = −Σ_j∇̄_jP″_j`;
- `i[H + mε, P″_j] = −Σ_i∇̄_iΘ_ij`;
- `i[H + mε, Q_j] = −Σ_i∇̄_iΘ_ji`.

These are the same momentum and stresses as without the mass.

*Proof.*
- The momentum laws: `mε` commutes with `P″` and with `Q`, because each of their bilinears joins sites an even number of steps apart. So their rates are block 136's.
- For every site projector Π, [Π,ε]=0 and {H,ε}=0 imply [H,εΠ]+[ε,{Π,H}/2]=0. The m² term also vanishes because [ε,εΠ]=0. Therefore the added terms in i[H+mε,{Π,H+mε}/2] cancel for every real m, before averaging. Apply the fixed linear average and the massless identity. This proof, unlike a diagonal plane-wave current, also covers all off-diagonal coherences.

∎

*Checked (B1).*
- As exact matrices over `ℚ(i)`: on `6³` with `m = 3/4` and `m = 5/2`, and on `10³` with `m = 3/4`.
- The finite shift products bound both matrix endpoints in the coordinate cube [-4,4]^3 before identification, and even side ten separates them and preserves ε. The coordinate support radius is at most 4, so `10³` carries the laws to `ℤ³`.

## Theorem T2 — classification within the eight-dimensional site-term family

*Statement.*
- For a site term `M`, the defect `i[H + M, e′_{H+M}] + Σ_j∇̄_jP″_j` is linear in `M`, since `M` commutes with its own density.
- Among `1, ε, σ_a, εσ_a` it vanishes only for `ε`, and the other seven defects are linearly independent.
- So, with the two-step momentum, within this eight-dimensional real span, the fixed energy law admits only multiples of the staggered term: the staggered mass.

*Proof.* Linearity: the term's own density commutes with it site by site. The rank-seven finite witness excludes every nonzero combination of the seven other directions: any infinite-lattice identity with these periodic coefficients would fold to the even torus. The analytic cancellation above proves the remaining ε direction for every m, including combinations; this is not extrapolation from two mass values. ∎

*Checked (C1).* On `6³`: the eight defects, and the rank 7 of the seven nonzero ones over `ℚ(i)`.

## Theorem T3 — cancellation mechanism and a constant-offset obstruction

*Statement.*
- (a) `(H + mε)² = H² + m²`, because `ε` anticommutes with each hop. So `E² = |sin k|² + m²`, and `E ∂E/∂k_j = sin k_j cos k_j`, the two-step momentum, where the branch is differentiable; the equivalent derivative of E²/2 holds at every k.
- (b) A uniform coin mass `mσ₃` shifts `sin k₃` to `sin k₃ + m`. Its current `(sin k₃ + m)cos k₃` is not the two-step momentum.
- (c) A constant offset `V` adds `V` times the velocity `σ_j cos k_j` to the total energy current, and the velocity does not commute with `σ·s`. By block 137 T3, no such stress with the same first moment then gives the double-divergence identity for all states. This only excludes a nonzero offset within the stipulated density/first-moment convention; changing that convention remains open.

*Proof.*
- (a) `εT_a = −T_aε`.
- (b) The dispersion.
- (c) The first moment of the offset's density is `V` times the position, whose rate is the velocity.

∎

*Checked (D1).* (a) as operators on `6³`, and symbolically; (b) and (c) symbolically.

## Theorem T4 — massive content and the member

*Statement.* With block 136's bond shift at `β = −α`, the member keeps its clock constraint iff `ė_u = (Kw̄²/(4α)) p·P`. By T1 the massive walker's averaged energy flows as `w̄²` times the same momentum. So the specified massive sources preserve the initially satisfied nonzero-mode constraints for all states iff `α = K/4`.

*Proof.* Block 136 T4 and T1. ∎

*Checked (E1).* The member's clock condition, re-derived with the shift, and the solve.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "blocks 135-137 (open): exact books for the massless walker; the rest energy (block 77) untested against them"
source_of_blocker_text: blocks 77 (landed), 135-137 (open)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "terms beyond one site; the massive walker under exclusion (block 137's question with a mass); an other-family referee"
conditional_surface_status: "exact at uniform rates; the eight-dimensional constant-plus-checkerboard site-term span only; the two-step momentum as the momentum"
hypothetical_axiom_status: "nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54: the walk.
  - Block 73: the two-step momentum is a normalized covariant conserved momentum in the reviewed reach-two class.
  - Block 77: the staggered rest energy.
- **Opened, not landed.**
  - Block 119 (PR #9170): the staggered term is the only rest energy a full coin frame admits.
  - Blocks 135 (PR #9195), 136 (PR #9196) and 137 (PR #9197): the books.
- **In the literature.**
  - The equality of energy current and momentum for massive waves in the comparator.
  - Mass terms that anticommute with a massless generator.

  Both reference only.
- **New here:**
  - T1: the massive walker keeps the exact books;
  - T2: uniqueness within the stated eight-dimensional site-term family;
  - T3(c): the zero of energy fixed by the books;
  - T4: the massive light-cone statement.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: which rest energies keep the books. The obligations are:
- (O1) the staggered mass (T1);
- (O2) the other site terms (T2);
- (O3) the mechanism and the offset (T3);
- (O4) the member (T4).

T1–T4 discharge these bounded obligations for the displayed site-term span and nonzero-mode constraint test.

## No-Go Discipline Gate

The note's negative sentence: with the two-step momentum, no site term other than the staggered mass keeps the energy law; and no local placement keeps the books with a constant offset.

### N1 — Routes by which the sentence could fail or mislead
1. *Another momentum.* For a uniform coin mass, a momentum shifted by `mC₃` carries its energy current. That momentum is not covariant (block 73), and it gives a walker at rest a momentum. This is not treated further.
2. *Terms beyond one site.* Not treated.
3. *Exclusion.* The two-record massive interacting problem is not proved here; the massless result does not alone settle it.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied walk, rest energy, currents, placements and member.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 54, 73, 77 (landed) | the walk; the momentum; the rest energy | yes (restated) |
| blocks 136, 137 (open) | the densities and the member; the first-moment argument | yes (restated) |
| block 119 (open) | the rest energy of a full frame | no (placement) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the staggered mass keeps the books; no other term in the stated eight-dimensional family does with the fixed density and momentum; an offset obstructs the stated same-first-moment stress class; initially satisfied nonzero-mode constraints for the supplied free massive content are preserved iff `α = K/4`" | executed: exact operators on `6³` (two masses) and `10³` | executed: eight defects and their rank | executed: the square, the currents, the velocity | executed: the member's condition | exact on the common finite-support domain at uniform rates; only the stated eight-dimensional site-term family |

### N6 — Partial-closure paths and primitive scan
No approved primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A staggered mass distinguishes the two sublattices, so it privileges sites."
  - *Reply:* It is a separately supplied construction from block 77; no classification of arbitrary mass mechanisms is imported. This note adds uniqueness within the stated eight-dimensional span for the fixed energy law.
  - Whether the axioms supply it is not decided here.

### N8 — Cross-cycle echo
- Block 77 gave the rest energy.
- Earlier frame comparisons concern specified anticommuting coin terms, not arbitrary potentials.
- Blocks 135–136 found the books.
- This note finds the rest energy compatible with the books, and the only term in the specified eight-dimensional family that satisfies this fixed law.

## Falsifiers

- A state for which T1 fails on `ℤ³`.
- A combination of the eight site terms, other than a multiple of `ε`, with zero defect.

## Boundaries and non-claims

- The walk, rest energy, currents, placements, member and source link are supplied.
- The eight-dimensional constant-plus-checkerboard site-term span only, at uniform rates.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- [Supplied source, block 54](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 73](ADMISSIBILITY_RULE_THE_TWO_STEP_MOMENTUM_IS_THE_ONLY_ONE_AMONG_CONSERVED_COVARIANT_MOMENTA_OF_REACH_TWO_THAT_IS_EVERY_SPECIES_OWN_WAVE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 77](ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_OF_ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 136](ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 137](ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_KEEPS_THE_BOOKS_ONLY_AT_LEADING_ORDER_TWO_EXCLUDED_RECORDS_LOSE_THEIR_ENERGY_CURRENT_IN_TWO_AND_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-25.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.

- `minimal_axioms`. Blocks 54, 73 and 77, restated. Blocks 136 and 137, restated. Block 119, placed.
- Named standard imports, at definition level:
  - exact arithmetic over `ℚ(i)`;
  - linear algebra (rank);
  - the algebra of the coin matrices.

## Review record

- **Who and when.** Supervisor-run block, the eighty-seventh since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), checked by its own runner. It is not refereed by another model family.
- **Before writing.** The own prior-art check considered earlier restricted frame mass comparisons and block 131's rest energy in frames. It found no test of the books with a mass.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_books_admit_one_rest_energy_the_staggered_mass_keeps_them_exactly_so_massive_content_meets_the_member_iff_alpha_equals_k_over_four_2026_09_25.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
