---
claim_id: admissibility_rule_one_record_per_site_keeps_the_books_only_at_leading_order_two_excluded_records_lose_their_energy_current_in_two_and_three_dimensions_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: For the supplied two-record compressed free walk at uniform rate, explicit finite-support witnesses
  give nonconservation of the compressed energy-dipole current on Z^2 and Z^3 for both exchange signs. Free antisymmetric
  pairs and excluded infinite-line pairs conserve it; the specified minimal-image ring current is checked on all
  states at L=7. The first-moment obstruction excludes a universal double-divergence identity with the same energy
  first moment and finite-range number-conserving stress on finite-support states. The small-offset cubic expansion
  is conditional kinematics of asymptotic free channels, not a derived collision estimate, scattering theorem, or
  approximate interacting conservation law.
upstream_dependencies:
- admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
- admissibility_rule_one_record_per_site_is_an_interaction_not_a_free_sea_two_records_under_exclusion_against_free_antisymmetric_and_symmetric_pairs_bounded_theorem_note_2026-09-22
- admissibility_rule_under_one_record_per_site_the_source_is_the_compressed_density_on_a_chain_two_records_are_two_free_fermions_of_the_charge_band_and_action_equals_reaction_survives_bounded_theorem_note_2026-09-24
runner: scripts/admissibility_rule_one_record_per_site_keeps_the_books_only_at_leading_order_two_excluded_records_lose_their_energy_current_in_two_and_three_dimensions_2026_09_25.py
---

# Two-record exclusion obstructs conservation of a specified energy-dipole current

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact for two records within the landed walk and exclusion, with block 121's source placed; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 54 and 78 as landed on main (the walk and one record per site), with blocks 121, 135 and 136 placed; it reports whether two records under exclusion keep the books that the member's identity needs; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Blocks 135 and 136 (open) showed that one walker, or free walkers, keep exact books in the member's placement: energy flows as the two-step momentum, and the momentum flows as a symmetric stress. These are conditional conservation identities; their reviewed versions do not establish unrestricted coupled solvability. The owner's reading of the records is one record per site (block 78: an interaction). Do records under that reading keep the same books?

- **T1: not exactly, in two or three dimensions.** For two records under exclusion, with either exchange sign, the total energy current is not kept.
- **T2: exactly on a line, and without exclusion.**
  - On the infinite line excluded pairs keep it; the ring assertion below is the complete finite L = 7 check for its separately defined current.
  - Free antisymmetric pairs keep it in every dimension. Such pairs let two records share a site with opposite coins.
- **T3: why it matters.** With any local stress, the member's identity forces the total energy current to be kept. So with block 121's compressed source, or block 135's average, no stress in the stated finite-range, zero-vacuum class serves two excluded records in two or three dimensions.
- **T4: conditional channel kinematics.** For asymptotic free incoming and outgoing channels whose momenta all remain within a small offset of species corners and whose total crystal momenta agree, the change in the sum of free one-record currents has a cubic expansion. No existence or completeness of such scattering channels, or small error during a collision, is proved.

The exact obstruction concerns one specified energy density and its first moment. It is not a general conflict between exclusion and all possible field couplings.

## Premises and declared objects

Infinite-lattice statements use the common finite-support two-record domain for the unbounded dipole. A local stress in T3 means finite-range number-conserving operator densities with zero vacuum value, so their expectation in each finite-support state is finitely supported; sufficient decay with vanishing boundary terms also suffices. Nonlocal stresses and altered first moments are not excluded. The torus current is defined using minimal-image displacements and is not a globally defined coordinate dipole commutator.


- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, its exclusion, the currents and their placements, the member and the source link are supplied clauses. Nothing is adopted.
- **The walk** (block 54 as landed). `H = Σ_{a<d}σ_aS_a` on `ℤ^d`, with `S_a = (T_a − T_a⁻¹)/(2i)`, at a uniform rate.
- **Two records** (block 78 as landed).
  - Pair states are symmetric or antisymmetric in the two records.
  - `P` removes every state with both records on one site. The compressed generator is `H₂ = P(H⊗1 + 1⊗H)P`.
- **Energy and its current.**
  - The compressed energy density `h_x = P(e_x⊗1 + 1⊗e_x)P`, with `e_x = ½(Π_xH + HΠ_x)`, is block 121's source.
  - The energy dipole is `D₂ = Σ_x x h_x = P(D⊗1 + 1⊗D)P`, with `⟨t|D|s⟩ = ½(x_t + x_s)⟨t|H|s⟩`.
  - The total energy current is `J = i[H₂, D₂] = ½Σ_{x,y}(x − y) i[h_y, h_x]`.
- **The member's identity** (block 135): `ë_u = Σ_ij∇̄_i∇̄_jΘ_ij`, with `∇̄_if(x) = f(x) − f(x − e_i)`.
- **Comparators, named only:** a boost-invariant stress (the symmetry of the energy current and the momentum density); the conservation of the energy current in integrable chains.

## Theorem T1 — the current is not kept in two or three dimensions

*Statement.* Under exclusion, for both exchange signs, `[H₂, J] ≠ 0` on `ℤ²` and `ℤ³`.

*Proof.* Exact witnesses: `[H₂, J]` applied to adjacent pairs of records is nonzero. The same holds on the `5 × 5` torus, with `J` built from the site densities by minimal image. ∎

*Checked (B1).* Over `ℚ(i)`: every coin pair on the open lattices, and a sample of pair states on the torus.

## Theorem T2 — where the current is kept

*Statement.* `[H₂, J] = 0` in these cases:
- free antisymmetric pairs, on `ℤ`, `ℤ²` and `ℤ³`, where a site may hold two records with opposite coins;
- excluded pairs of both signs on the line, where block 121 T2 shows the chain pair is free;
- excluded pairs on the ring of 7 sites.

*Proof.*
- Free pairs: `J` is the sum of the two records' currents, and each record's current is its two-step momentum `P_j = S_jC_j`, which commutes with `H` (block 136).
- The infinite line: the site-dependent unitary from reviewed block 121 transforms the nearest-neighbour coin hop to a uniform scalar hop. Ordered particle positions cannot cross. Both exchange sectors therefore become the exterior-square scalar chain operator tensored with spectator ordered-coin space. The same unitary transforms D to its scalar energy dipole because it commutes with positions. On the infinite scalar chain i[h,{X,h}/2] is the two-step shift current and commutes with h; its two-record lift commutes as well. This argument would not remove open finite-chain boundary terms.
- The ring: exact computation. On a ring the excluded pair is one twisted band (blocks 121 and 130).

∎

*Checked (C1).* On adjacent pairs (open lattices), on a sample of pair states of the `5 × 5` torus (free), and on every basis state of the ring.

## Theorem T3 — why no stress in the stated finite-range, zero-vacuum class serves excluded records

*Statement.*
- (a) For any finitely supported stress, `Σ_x x_k Σ_ij∇̄_i∇̄_jΘ_ij(x) = 0`. So the member's identity with a local stress keeps `d/dt Σ_x x e_u(x)`, which is the total energy current of the placement `e_u`.
- (b) The body-diagonal average keeps every first moment.
- (c) So with block 121's compressed source, or with block 135's average of it, the total current is T1's `J`, and no stress in the stated finite-range, zero-vacuum class serves two excluded records in two or three dimensions.

*Proof.*
- (a) Sum by parts twice; each difference of a first moment is a total sum of a finitely supported field.
- (b) The average is symmetric about each site.
- (c) Combine (a), (b) and T1.

∎

*Checked (D1).*
- (a) On a rational stress supported on `5³`, where the double divergence is nonzero but its first moments vanish.
- (b) On a rational field.

## Theorem T4 — conditional small-offset channel expansion

*Statement.* A free record has current j_a(k) = sin(2k_a)/2. For incoming and outgoing two-record momentum tuples k_r = π n_r + κ_r, suppose every offset component has magnitude at most ε, ε < π/4, and total crystal momentum agrees modulo 2π. Then the total corner parity is unchanged in each coordinate and ΔΣ_r κ_r = 0. Consequently ΔΣ_r j_a(k_r) = −(2/3)ΔΣ_r κ_ra^3 + O(ε^5).

*Proof.* Crystal-momentum conservation gives ΔΣκ = −πΔΣn modulo 2π. Its absolute value is at most 4ε < π, so the corner sum must change by an even integer and ΔΣκ = 0. Expand the analytic periodic function j at each corner; the remainder is uniform over the four offsets. This is kinematics, conditional on such free channels. Translation symmetry alone does not supply asymptotic scattering, keep interacting states in the small-offset regime, or bound the compressed current during collisions. The runner's example conserves momentum only; it is not asserted to be energy-conserving or dynamically realizable.

*Checked (E1).* The single-record expansion, corner periodicity, and a fixed-momentum tuple example.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "blocks 135-136 (open): exact books for one or free walkers; the owner's reading of records (one per site, block 78) not tested"
source_of_blocker_text: blocks 78 (landed), 135 and 136 (open)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "other local placements (a total time derivative of a local sum); many records; whether a record's exclusion can be relaxed to opposite coins"
conditional_surface_status: "exact for two records at uniform rates; T3 for the placements with block 121's first moment"
hypothetical_axiom_status: "the exclusion, the placements and the member are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54: the walk.
  - Block 78: one record per site is an interaction.
- **Opened, not landed.**
  - Block 121 (PR #9174): the compressed source.
  - Block 130 (PR #9187): the ring's twisted band.
  - Blocks 135 (PR #9195) and 136 (PR #9196): the exact books for one or free walkers.
- **In the literature.**
  - The symmetry of the energy current and the momentum density under boosts.
  - The conservation of the energy current in integrable chains.

  Both reference only.
- **New here:**
  - T1: the exact failure for excluded records in two and three dimensions;
  - T2: the line, and the free pairs;
  - T3: the consequence for the member;
  - T4: the third-order estimate for slow records.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: whether excluded records keep the member's books. The obligations are:
- (O1) the witness (T1);
- (O2) the controls (T2);
- (O3) the consequence (T3);
- (O4) the leading order (T4).

T1–T4 discharge them for two records. Open: other placements, and many records.

## No-Go Discipline Gate

The note's negative sentence: with block 121's compressed source, or any placement with the same first moment, no stress in the stated finite-range, zero-vacuum class meets the member's identity for two excluded records in two or three dimensions.

### N1 — Routes by which the sentence could fail or mislead
1. *Another placement.* A placement with a different first moment changes the total current by the rate of a local sum. Whether one such placement restores conservation is open. For records that are far apart before and after a collision, such a rate averages to zero, which suggests not; that is not proved here.
2. *Relaxed exclusion.* If two records may share a site with opposite coins (T2's free pairs), the books are exact.
3. *Slow records.* T4 gives conditional free-channel kinematics only; no approximate interacting conservation law is established.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied walk, exclusion, placements and member.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics or time metric in the axioms | yes |
| blocks 54, 78 (landed) | the walk; one record per site | yes (restated) |
| block 121 (open) | the compressed source | yes (restated) |
| blocks 130, 135, 136 (open) | the ring; the books; the identity | no (placement) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "two excluded records lose the total energy current in 2D and 3D, keep it on a line; no stress in the stated finite-range, zero-vacuum class serves them with block 121's first moment; conditional free-channel current changes have cubic leading order" | executed: `[H₂, J]` on adjacent pairs over `ℚ(i)` | executed: the `5 × 5` torus; the ring on every state | executed: first moments of a double divergence | executed: series and species | two records; placements with block 121's first moment |

### N6 — Partial-closure paths and primitive scan
No approved primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "The energy current is defined only up to a total time derivative, so the failure is an artefact of the placement."
  - *Reply:* That is N1's route 1, and it is left open. T3 is stated for the placements the lane already uses: block 121's source, and block 135's average.
  - The exact witness proves nonconservation of the specified current. The conditional free-channel expansion is not a scattering theorem or a classification of other placements.

### N8 — Cross-cycle echo
- Block 78 found that exclusion is an interaction.
- Block 121 found that the compressed source is what pulls.
- Blocks 135 and 136 found the exact books for free content.
- This note proves nonconservation witnesses for the specified density in two and three dimensions, and conservation on the infinite line; it does not classify all interactions or densities.

## Falsifiers

- A failure of the specified nonzero T1 witness calculation. A different state with vanishing residual does not refute a nonzero-operator assertion.
- An excluded pair on a line whose current is not kept.
- A finitely supported stress whose double divergence has a nonzero first moment.

## Boundaries and non-claims

- The walk, the exclusion, the placements and the member are supplied.
- Two records only, at uniform rates. Many records are not treated.
- Other placements are open (N1).
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- [Supplied source, block 54](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 78](ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_IS_AN_INTERACTION_NOT_A_FREE_SEA_TWO_RECORDS_UNDER_EXCLUSION_AGAINST_FREE_ANTISYMMETRIC_AND_SYMMETRIC_PAIRS_BOUNDED_THEOREM_NOTE_2026-09-22.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 121](ADMISSIBILITY_RULE_UNDER_ONE_RECORD_PER_SITE_THE_SOURCE_IS_THE_COMPRESSED_DENSITY_ON_A_CHAIN_TWO_RECORDS_ARE_TWO_FREE_FERMIONS_OF_THE_CHARGE_BAND_AND_ACTION_EQUALS_REACTION_SURVIVES_BOUNDED_THEOREM_NOTE_2026-09-24.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.

- `minimal_axioms`. Blocks 54 and 78, restated. Block 121's source, restated. Blocks 130, 135 and 136, placed.
- Named standard imports, at definition level:
  - exact arithmetic over `ℚ(i)`;
  - series expansion;
  - summation by parts.

## Review record

- **Who and when.** Supervisor-run block, the eighty-fifth since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), checked by its own runner. It is not refereed by another model family.
- **Before writing.**
  - Main was re-fetched.
  - The own prior-art check (memory, open PRs, probes attempts) found no test of the energy current under exclusion.
- **Corrections during the work.** Two drafts of the dipole were wrong: one included cross terms between the records, and one mislabelled the moving record after reordering the pair. The free-pair control failed for each, which exposed them. The dipole now carries `½(x_t + x_s)` on each hop, and the free pairs keep the current.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_one_record_per_site_keeps_the_books_only_at_leading_order_two_excluded_records_lose_their_energy_current_in_two_and_three_dimensions_2026_09_25.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
