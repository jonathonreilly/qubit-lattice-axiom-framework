---
claim_id: admissibility_rule_the_coins_spin_enters_the_source_link_through_its_curl_the_symmetric_momentum_is_the_two_step_momentum_plus_half_the_curl_of_the_spin_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: 'WITHIN block 54''s walk H = sum_a sigma_a S_a at a uniform rate, block 69''s two-step momentum P_j
  = S_j C_j and its current (blocks 73 and 74), and block 62''s frame, all as landed on main and supplied, with
  block 120''s average (open) and block 136''s densities (open) placed. Exact operator identities on Z^3, for every
  state: (T1) the bonds'' coin-energy current Q_j differs from the carried two-step momentum P''''_j by half the
  curl of the coin''s spin on the faces, Q_j - P''''_j = (1/2) sum_kl eps_jkl dbar_k S~_l, where S_l = (1/2)[Re
  psi^dag(x) sigma_l psi(x + e_j + e_k) + Re psi^dag(x + e_k) sigma_l psi(x + e_j)] sits on the face perpendicular
  to l and S~ = C_1 C_2 C_3 S. (T2) so block 136''s symmetric momentum is P^B = P'''' + (1/2) curl(S~/2), the two-step
  momentum plus half the curl of the spin sigma/2, and the curl has zero divergence and therefore changes no term
  in this energy-continuity equation. (T3) the divergence of the antisymmetric stress, the torque that stops the
  canonical momentum from balancing the symmetric stress, is the rate of the spin''s curl: sum_i dbar_i (Theta_ij
  - Theta_ji) = (1/2) d/dt (curl S~)_j. (T4) the eigenvector identity behind T1. The supervisor''s own derivation
  (Claude Opus 5.5), checked by its runner; not refereed by another model family. Nothing adopted; no gravitational
  claim.'
upstream_dependencies:
- admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
- admissibility_rule_only_the_two_step_current_can_source_block_62s_symmetric_member_no_local_placement_of_the_frame_response_or_of_the_one_step_current_keeps_its_divergence_condition_bounded_theorem_note_2026-09-24
- admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
- admissibility_rule_the_two_step_momentum_is_the_only_one_among_conserved_covariant_momenta_of_reach_two_that_is_every_species_own_wave_number_bounded_theorem_note_2026-09-21
- admissibility_rule_three_responses_eight_species_the_frames_site_stress_has_the_wrong_sign_in_shear_for_six_species_only_the_two_step_current_serves_all_bounded_theorem_note_2026-09-21
- admissibility_rule_two_step_content_keeps_symmetric_books_where_the_member_keeps_its_fields_and_a_bond_shift_keeps_every_constraint_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
- admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_the_coins_spin_enters_the_source_link_through_its_curl_the_symmetric_momentum_is_the_two_step_momentum_plus_half_the_curl_of_the_spin_2026_09_25.py
---

# A face-bilinear curl identity for the supplied symmetric lattice momentum

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact within the landed walk and currents, with block 120's average and block 136's densities placed; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 54, 62, 63, 69, 73 and 74 as landed on main (the walk, the frame, the currents and the two-step momentum), with blocks 120 and 136 placed; it reports how the coin's spin enters the symmetric momentum that block 136 couples to a shift; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 136 (open) built the momentum that the member can accept, `P^B = (P″ + Q)/2`, from two densities. `P″` is the carried two-step momentum. `Q` is the bonds' coin-energy current. This note says what `Q` is.

- **T1: `Q − P″` is half the curl of the specified face bilinear.** Carry the coin's spin `σ_l` onto the face perpendicular to `l`, as the mean of the face's two diagonals, and average it over the body diagonals. Then `Q_j − P″_j = ½(∇̄ × S̃)_j` exactly, for every state.
- **T2: the symmetric momentum is the two-step momentum plus half the curl of the spin.** `P^B = P″ + ½∇̄ × (S̃/2)`, where `S̃/2` is the spin `σ/2`. The curl has zero divergence and therefore changes no term in this energy-continuity equation, so the averaged energy flows as `P^B` just as it flows as `P″`.
- **T3: the torque is the spin's turning.** The divergence of the antisymmetric stress is exactly the rate of change of the spin's curl. That antisymmetric stress is the torque on the coin, which block 136 found stops the canonical momentum from balancing the symmetric stress.
- **T4: the identity behind it.** For two eigen-waves, the coin-energy beat splits exactly into the two-step momentum's beat and the curl of the spin's beat.

The identity decomposes two specified currents of the supplied two-component walk. Its face-spin variable is a bilocal correlation, not the on-site spin density or an axiom-derived physical spin. A divergence-free current can circulate and couple to other fields; zero divergence alone does not make it energy-free.

## Premises and declared objects

Use unit rate in all displayed identities. At rate w̄, define Q and P″ using the unit-rate H as written, while Θ and time derivatives scale by w̄; these conventions preserve T3. Infinite-lattice identities concern square-summable states or formal finite wave sums. The face variable S/2 is the explicitly defined bilocal coin-matrix observable; it is not an arithmetic average of on-site spin densities.


- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, its currents and their placements, the member and the source link are supplied clauses. Nothing is adopted.
- **The walk and the densities** (blocks 54, 69, 73 and 136).
  - `H = Σ_aσ_aS_a`, and `P_j = S_jC_j`.
  - `P″_j = φ_jᵀπ_j`, with `π_j = Re ψ†P_jψ` and `φ_jᵀ = ½(1 + T_j)Π_{l≠j}C_l` (block 120).
  - `Q_j = C₁C₂C₃·½Re[ψ†(x+e_j)σ_j(Hψ)(x) + (Hψ)†(x+e_j)σ_jψ(x)]`.
  - `Θ_ij = φ_jᵀK_i^j`, and `P^B = (P″ + Q)/2`.
- **The spin on the faces.**
  - `S_l(x) = ½[Re ψ†(x)σ_lψ(x + e_j + e_k) + Re ψ†(x + e_k)σ_lψ(x + e_j)]`, where `{j, k}` are the two directions other than `l`. It sits at the centre `x + (e_j + e_k)/2` of the face perpendicular to `l`.
  - `S̃ = C₁C₂C₃S`, and `(∇̄ × S̃)_j = Σ_klε_jkl∇̄_kS̃_l`, which lands on the bond `x → x + e_j`.
- **Comparators, named only:** the symmetric momentum as the canonical one plus half the curl of the spin (the Belinfante and Rosenfeld construction); the spin of the two-component waves (Weyl).

## Theorem T1 — `Q − P″` is half the curl of the specified face bilinear

*Statement.* For every state on `ℤ³` and `j = 1, 2, 3`: `Q_j − P″_j = ½Σ_klε_jkl∇̄_kS̃_l`.

*Proof.* Take the beat of two eigen-waves at `q = k − k′`, with `k̄ = (k + k′)/2`.
- `Q_j` carries `Π_m cos q_m · cos k̄_j · ½(l + l′)u′†σ_ju`.
- By T4, `(l + l′)u′†σ_ju = (s_j + s′_j)u′†u + iε_jkl(s − s′)_ku′†σ_lu`.
- The first part is `P″_j`'s beat. Both equal `Π_m cos q_m · cos(q_j/2) · ½ sin 2k̄_j · u′†u`, since `½(s_j + s′_j) = sin k̄_j cos(q_j/2)` and `½(P_j(k) + P_j(k′)) = ½ sin 2k̄_j cos q_j`.
- The second part gives the curl. `(s − s′)_k = 2 sin(q_k/2)cos k̄_k`, and the face spin carries `u′†σ_lu cos k̄_j cos k̄_k`, which is the mean of the two diagonals' factors.

∎

*Checked (B1).*
- As exact matrices over `ℚ(i)`, on the `5³`, `6³` and `9³` tori; both sides are nonzero.
- Before periodic identification the finite shift products put all endpoints in x + [-4,4]^3; body-diagonal shifts add one per coordinate and the bilocal/current shifts at most three more. Side nine separates these endpoints. The coordinate support radius is at most 4 on `9³`, so the identity carries to `ℤ³` without using the proof.

## Theorem T2 — the symmetric momentum

*Statement.* `P^B_j = P″_j + ¼(∇̄ × S̃)_j = P″_j + ½(∇̄ × (S̃/2))_j`, and `Σ_j∇̄_j(∇̄ × S̃)_j = 0`. So the averaged energy flows as `P^B`, as it flows as `P″` (block 136 T1).

*Proof.* T1, and the lattice identity `div curl = 0`: the differences commute. ∎

*Checked (C1).* Both, as exact operators on `5³` and `6³`.

## Theorem T3 — a time-derivative identity for the specified face bilinear

*Statement.* `Σ_i∇̄_i(Θ_ij − Θ_ji) = ½ d/dt(∇̄ × S̃)_j` for every state, as an operator identity. The common operator is nonzero, although its expectation can vanish in particular states.

*Proof.* Block 136 T2 gives `dP″_j/dt = −Σ_i∇̄_iΘ_ij` and `dQ_j/dt = −Σ_i∇̄_iΘ_ji`. Subtract, and use T1. ∎

*Checked (D1).* As exact operators on `5³`.

## Theorem T4 — the eigenvector identity

*Statement.* If `(σ·s)u = lu` and `(σ·s′)u′ = l′u′`, then `(l + l′)u′†σ_ju = (s_j + s′_j)u′†u + iε_jkl(s − s′)_ku′†σ_lu`.

*Proof.* `u′†(σ_j(σ·s) + (σ·s′)σ_j)u = (l + l′)u′†σ_ju`. Expand each product of two coin matrices into its scalar and cross parts. ∎

*Checked (E1).* Symbolically, modulo `l² = |s|²` and `l′² = |s′|²`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 136 (open): the symmetric momentum P^B = (P'' + Q)/2 found, with Q unexplained"
source_of_blocker_text: block 136 (open)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the spin's own balance law on the faces; the member's response to a spin-polarised walker; an other-family referee"
conditional_surface_status: "exact at uniform rates; the walk, currents and placements supplied"
hypothetical_axiom_status: "nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54: the walk.
  - Block 62: the frame, whose antisymmetric part does not enter the metric at first order.
  - Block 63 T5: the site stress's torque turns the coin.
  - Blocks 69, 73 and 74: the two-step momentum and its current.
- **Opened, not landed.**
  - Block 120 (PR #9173): the average.
  - Block 136 (PR #9196): `Q` and `P^B`.
- **In the literature.**
  - The symmetric momentum as the canonical one plus half the curl of the spin (Belinfante, Rosenfeld).
  - The spin of two-component waves (Weyl).

  Both reference only.
- **New here:**
  - T1: the exact lattice identity, with the spin on the faces as the mean of the two diagonals;
  - T2: the lattice form of the symmetric momentum;
  - T3: the torque on the two-step current as the spin's turning.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: what `Q` is. The obligations are:
- (O1) the curl identity (T1);
- (O2) the symmetric momentum (T2);
- (O3) the torque (T3);
- (O4) the mechanism (T4).

T1–T4 discharge them.

## No-Go Discipline Gate

The note's negative sentence: dropping the second diagonal while retaining the original factor 1/2 makes the curl identity fail. This control does not classify all normalized single-diagonal or other face observables.

### N1 — Routes by which the sentence could fail or mislead
1. *Other face placements.* Only the displayed missing-second-diagonal control with unchanged factor 1/2 is tested.
2. *Other spin densities.* A site spin with another average might also work. None is claimed.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied walk, currents and placements.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 54, 62, 63, 69, 73, 74 (landed) | the walk; the frame; the currents | yes (restated) |
| blocks 120, 136 (open) | the average; `Q` and `P^B` | yes (restated and executed) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "`Q − P″` is half the curl of the face spin; `P^B = P″ + ½ curl(S~/2)`; the torque is the spin's turning" | executed: exact operators over `ℚ(i)` on `5³`, `6³` and `9³` | executed: two sites and every component | executed: the eigenvector identity | executed: the symmetric momentum; div curl; the torque | exact on `ℤ³` by support radius at most 4 |

### N6 — Partial-closure paths and primitive scan
No approved primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "This is a rewriting of block 136, not a new fact."
  - *Reply:* It is a rewriting that names the new density. `Q` is the two-step momentum plus half the curl of the specified face bilinear.
  - It rewrites block 136's antisymmetric-current obstruction in terms of the specified face bilinear; no physical spin or repository premise is derived.

### N8 — Cross-cycle echo
- Block 63 found the site stress's torque turning the coin.
- Block 136 found `Q` and `P^B`.
- This note identifies `Q − P″` as the specified face-bilinear curl.

## Falsifiers

- A state for which T1 fails on `ℤ³`.
- A pair of eigenvectors violating T4.

## Boundaries and non-claims

- The walk, its currents and their placements are supplied.
- The result is at uniform rates.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- [Supplied source, block 54](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 63](ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 69](ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 73](ADMISSIBILITY_RULE_THE_TWO_STEP_MOMENTUM_IS_THE_ONLY_ONE_AMONG_CONSERVED_COVARIANT_MOMENTA_OF_REACH_TWO_THAT_IS_EVERY_SPECIES_OWN_WAVE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 74](ADMISSIBILITY_RULE_THREE_RESPONSES_EIGHT_SPECIES_THE_FRAMES_SITE_STRESS_HAS_THE_WRONG_SIGN_IN_SHEAR_FOR_SIX_SPECIES_ONLY_THE_TWO_STEP_CURRENT_SERVES_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 120](ADMISSIBILITY_RULE_ONLY_THE_TWO_STEP_CURRENT_CAN_SOURCE_BLOCK_62S_SYMMETRIC_MEMBER_NO_LOCAL_PLACEMENT_OF_THE_FRAME_RESPONSE_OR_OF_THE_ONE_STEP_CURRENT_KEEPS_ITS_DIVERGENCE_CONDITION_BOUNDED_THEOREM_NOTE_2026-09-24.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 136](ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.

- `minimal_axioms`. Blocks 54, 62, 63, 69, 73 and 74, restated. Blocks 120 and 136, restated and executed.
- Named standard imports, at definition level:
  - the algebra of the coin matrices;
  - exact arithmetic over `ℚ(i)`.

## Review record

- **Who and when.** Supervisor-run block, the eighty-sixth since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), checked by its own runner. It is not refereed by another model family.
- **Before writing.** The own prior-art check found the torque of block 63 T5 and block 136's `Q`. It found no curl identity.
- **Independence.** T1 is checked as an operator identity on tori, separately from the Fourier argument. Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_coins_spin_enters_the_source_link_through_its_curl_the_symmetric_momentum_is_the_two_step_momentum_plus_half_the_curl_of_the_spin_2026_09_25.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
