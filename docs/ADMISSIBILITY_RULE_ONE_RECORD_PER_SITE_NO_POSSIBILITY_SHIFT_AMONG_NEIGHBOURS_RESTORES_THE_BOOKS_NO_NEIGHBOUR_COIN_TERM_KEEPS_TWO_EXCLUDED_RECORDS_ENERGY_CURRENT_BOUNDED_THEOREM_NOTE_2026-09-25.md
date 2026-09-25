---
claim_id: admissibility_rule_one_record_per_site_no_possibility_shift_among_neighbours_restores_the_books_no_neighbour_coin_term_keeps_two_excluded_records_energy_current_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: 'WITHIN block 54''s walk H = sum_a sigma_a S_a and block 78''s compression to one record per site,
  as landed on main and supplied, with block 121''s compressed source and block 137 (open) placed; two records on
  the open Z^2 and Z^3. Exact: (T1-T2) for either exchange sign, add any coin term acting on neighbouring records,
  V = sum over neighbouring pairs of M_a on the pair''s two coins, with M_a a general Hermitian 4 x 4 matrix for
  each axis a (32 real unknowns on Z^2, 48 on Z^3) and V''s energy anywhere on the bond''s line; then the defect
  [H2, J] v of the total energy current, for test pairs v, has entries that involve none of the unknowns and are
  nonzero, so no such term keeps the current. (T3) without exclusion and without a term the defect vanishes; the
  witnesses are exclusion''s (for the pair at (0,0), (1,0), both coins up, the entry on records at (-1,-1) up and
  (0,0) down is -i/16 for every term). (T4) on the line excluded records keep the current with no term (block 137),
  so the obstruction belongs to two and three dimensions. Correlated hops and other placements are not treated.
  The supervisor''s own derivation (Claude Opus 5.5), checked by its runner; not refereed by another model family.
  Nothing adopted; no gravitational claim.'
upstream_dependencies:
- admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
- admissibility_rule_one_record_per_site_is_an_interaction_not_a_free_sea_two_records_under_exclusion_against_free_antisymmetric_and_symmetric_pairs_bounded_theorem_note_2026-09-22
- admissibility_rule_one_record_per_site_keeps_the_books_only_at_leading_order_two_excluded_records_lose_their_energy_current_in_two_and_three_dimensions_bounded_theorem_note_2026-09-25
- admissibility_rule_under_one_record_per_site_the_source_is_the_compressed_density_on_a_chain_two_records_are_two_free_fermions_of_the_charge_band_and_action_equals_reaction_survives_bounded_theorem_note_2026-09-24
runner: scripts/admissibility_rule_one_record_per_site_no_possibility_shift_among_neighbours_restores_the_books_no_neighbour_coin_term_keeps_two_excluded_records_energy_current_2026_09_25.py
---

# A three-hop witness against fixed-position neighbour coin repairs

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact for two records within the landed walk and exclusion, with blocks 121 and 137 placed; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 54 and 78 as landed on main (the walk and one record per site), with blocks 121 and 137 placed; it reports whether a coin interaction between neighbouring records can restore the books that exclusion breaks; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 137 (open) found that two records under one record per site lose their total energy current in two and three dimensions, so the member's identity cannot hold exactly for them. The owner's reading of records is that the possibility at a site shifts as the neighbourhood changes. The simplest form of such a shift is a coin interaction between neighbouring records. Can one restore the current?

- **T1 (plane) and T2 (space): no.** Take any coin term on neighbouring records: a general Hermitian matrix on the pair's two coins for each axis, with its energy anywhere on the bond's line. Then the defect of the total energy current still has entries that involve none of the term's unknowns and are nonzero. This holds for either exchange sign, on `ℤ²` (32 unknowns) and on `ℤ³` (48 unknowns).
- **T3: the controls.**
  - Without exclusion, pairs keep the current.
  - With exclusion, a witness entry is `−i/16` both with no term and with a rational term, while the term changes other entries.
- **T4: only the plane and space are affected.** On a line excluded records keep the current, so there is nothing to repair. In a plane a record must go around the other's site, and exclusion removes paths that no change of the neighbours' coins restores.

In plain terms, when two records can't share a site, a collision spoils the energy bookkeeping the field relies on. Letting neighbouring records twist each other's possibilities, within the stated fixed-position matrix class, does not fix it: some of the spoiled accounts are never touched by such twists. Repairing them would need records that move one another, or energy counted in other places. Both remain open questions for the probes.

## Premises and declared objects

Work on the common finite-support two-record core at unit rate. The interaction has constant real coefficients per axis, acts only on the two coins, and never moves either occupied site. Its energy-dipole contribution is the stated scalar placement times this same fixed-position operator. This is a supplied candidate interaction class, not a definition of the owner's general possibility-shift mechanism. No claim covers arbitrary dynamics, correlated hopping, or other density improvements.


- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The walk, its exclusion, the currents and their placements, the member and the source link are supplied clauses. Nothing is adopted.
- **Two records** (blocks 54 and 78 as landed).
  - `H = Σ_{a<d}σ_aS_a` on `ℤ^d`.
  - The pair states are antisymmetric or symmetric, and `P` removes both records on one site.
  - `H₂ = P(H⊗1 + 1⊗H)P + V`.
- **The neighbour coin term.** `V = Σ_{pairs x, x+e_a} M_a` on the two coins, lower record first. Here `M_a = Σ_bc c_{a,b,c} σ_b⊗σ_c` is a general Hermitian `4 × 4` matrix with 16 real unknowns per axis. `V`'s energy sits at the pair's midpoint plus an offset `t` along the bond, with `t` free.
- **The total energy current** (block 137). `J = i[H₂, D₂]`, with `D₂` the compressed energy dipole plus `V`'s energy at its placement. The reviewed block 137 first-moment argument applies to finite-range zero-vacuum stress densities with vanishing boundary terms and this same energy first moment.
- **Comparators, named only:** the integrable chains, where exclusion keeps the energy current.

## Theorem T1 — the plane

*Statement.* On `ℤ²`, for either exchange sign, `[H₂, J]v` has entries free of all 32 unknowns and nonzero, for the test pairs `v` (records at `0` and `e₁`, `e₂`, `e₁ + e₂`, `2e₁`, with every coin pair). So no neighbour coin term keeps `J`.

*Proof.* The explicit matrix entry below and the minimum-hop support proof exclude every parameter choice. ∎

*Checked (B1).* Symbolically; one specified nonzero matrix entry for each exchange sign, together with the three-hop support argument below; no exhaustive census is required.

## Theorem T2 — space

*Statement.* The same holds on `ℤ³`, with 48 unknowns.

*Proof.* The explicit matrix entry below and the minimum-hop support proof exclude every parameter choice. ∎

*Checked (C1).* The same three-hop witness for both signs; no third-axis hop can reach its endpoints in three steps.

## Three-hop support proof

Let v have sites {0,e1}, both coins up, and let w have sites {−e1−e2,0}, with the first coin up and second down. The minimum number of one-record nearest-neighbour hops between these unordered configurations is three: both possible matchings have total distance three. Expand [H₂,J] = i(H₂²D₂ − 2H₂D₂H₂ + D₂H₂²). Each of its three factors is either a one-hop part of H₂ or D₂, or a zero-hop interaction part. Every monomial containing V or its dipole therefore has at most two hops and has zero w,v matrix element, irrespective of coin coefficients and placement offset. Only the three free-hop factors remain. Exact evaluation gives −i/16 for both exchange signs. The same endpoints embedded in three dimensions still need three hops, leaving no step for a third-axis excursion. This proves both no-go statements without extrapolating numerical parameter samples or enumerating all residual entries.

## Theorem T3 — the controls, the witness, the placement

*Statement.*
- Without exclusion and without a term, the defect vanishes on every test pair, on `ℤ²` and `ℤ³`.
- With exclusion, for the pair at `(0,0)` and `(1,0)` with both coins up, the entry on the state with records at `(−1,−1)` (up) and `(0,0)` (down) is `−i/16`. It has that value with no term and with a rational term, while the rational term changes other entries (the runner reports the count).
- With `V`'s energy anywhere on the bond's line (a free offset `t`), the same entries stay free of every unknown.

*Proof.* Exact computation. The three-hop proof excludes every monomial containing V or its dipole, so a free real offset along the bond cannot change the specified witness. Constant entries at the midpoint alone would not have established this. ∎

*Checked (D1).* All three items.

## Theorem T4 — the line

*Statement.* On `ℤ`, excluded pairs keep the current with no term. So the obstruction of T1–T2 belongs to two and three dimensions.

*Proof.* Use the reviewed block 137 infinite-line argument: the site-unitary scalar-chain reduction carries both the hop and energy dipole to the free scalar two-record lift with spectator ordered coins. Its two-step current commutes with the infinite-chain hop. The finite test pairs are checks, not the proof for arbitrary separations. ∎

*Checked (E1).* Adjacent and distance-two pairs, every coin pair.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 137 (open): one record per site loses the books in two and three dimensions; whether a possibility shift among neighbours repairs it"
source_of_blocker_text: block 137 (open); the owner's reading of records
reachability_to_target: advances
artifact_role: no_go
next_trace_action: "correlated hops of neighbouring records; other placements of the energy (probes problems a-possibility-shift-that-keeps-the-books and a-placement-that-keeps-excluded-records-books)"
conditional_surface_status: "exact for two records; coin terms on neighbouring pairs only"
hypothetical_axiom_status: "nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.** Block 54: the walk. Block 78: one record per site is an interaction.
- **Opened, not landed.** Block 121 (PR #9174): the compressed source. Block 137 (PR #9197): the lost current.
- **Probes.** `a-possibility-shift-that-keeps-the-books` (refill m, no attempt yet) asks this question, including correlated hops.
- **In the literature.** The conservation of the energy current in integrable chains; reference only.
- **New here:** T1–T3, the no-go for every neighbour coin term, with its placement freedom along the bond.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: whether a neighbour coin term restores the current. The obligations are:
- (O1) the plane (T1);
- (O2) space (T2);
- (O3) the controls (T3);
- (O4) the line (T4).

T1–T4 discharge them. Open: correlated hops, other placements, and many records.

## No-Go Discipline Gate

The note's negative sentence: no coin interaction between neighbouring records keeps the total energy current of two excluded records on `ℤ²` or `ℤ³`, with its energy anywhere on the bond's line.

### N1 — Routes by which the sentence could fail or mislead
1. *Correlated hops.* A term that moves neighbouring records (for example, letting one hop past the other) is not a coin term, and it is not treated.
2. *Other placements.* Energy placed off the bond's line, or a placement of the walk's own energy different from block 121's, is not treated. Block 137 N1 discusses the latter.
3. *Longer reach.* Coin terms on pairs farther apart are not treated.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied walk, exclusion and term.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 54, 78 (landed) | the walk; exclusion | yes (restated) |
| blocks 121, 137 (open) | the source; the lost current and its meaning for the member | yes (restated) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no neighbour coin term keeps two excluded records' current on `ℤ²` or `ℤ³`" | proved: three-hop support excludes all 32/48 coefficients; executed: exact witness | executed: specified witness for both signs and dimensions; controls | proved: arbitrary offset cannot alter the witness; executed: rational controls | executed: the line | two records; coin terms on neighbouring pairs |

### N6 — Partial-closure paths and primitive scan
No approved primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "The owner's 'possibility shifts' may mean more than a coin interaction."
  - *Reply:* Yes. This note closes only the simplest reading. The probes problem includes records that move one another.

### N8 — Cross-cycle echo
- Block 78 found that exclusion is an interaction.
- Block 137 found the lost current.
- This note finds that no neighbour coin interaction repairs it.

## Falsifiers

- A neighbour coin term, with its energy on the bond's line, that makes T1's witness entries vanish.
- A computation showing a witness entry depends on the term's unknowns.

## Boundaries and non-claims

- Two records, coin terms on neighbouring pairs, and energy on the bond's line.
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- [Supplied source, block 54](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 78](ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_IS_AN_INTERACTION_NOT_A_FREE_SEA_TWO_RECORDS_UNDER_EXCLUSION_AGAINST_FREE_ANTISYMMETRIC_AND_SYMMETRIC_PAIRS_BOUNDED_THEOREM_NOTE_2026-09-22.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 121](ADMISSIBILITY_RULE_UNDER_ONE_RECORD_PER_SITE_THE_SOURCE_IS_THE_COMPRESSED_DENSITY_ON_A_CHAIN_TWO_RECORDS_ARE_TWO_FREE_FERMIONS_OF_THE_CHARGE_BAND_AND_ACTION_EQUALS_REACTION_SURVIVES_BOUNDED_THEOREM_NOTE_2026-09-24.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 137](ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_KEEPS_THE_BOOKS_ONLY_AT_LEADING_ORDER_TWO_EXCLUDED_RECORDS_LOSE_THEIR_ENERGY_CURRENT_IN_TWO_AND_THREE_DIMENSIONS_BOUNDED_THEOREM_NOTE_2026-09-25.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.

- `minimal_axioms`. Blocks 54 and 78, restated. Blocks 121 and 137, restated.
- Named standard imports, at definition level:
  - exact symbolic arithmetic;
  - the algebra of the coin matrices.

## Review record

- **Who and when.** Supervisor-run block, the eighty-ninth since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), checked by its own runner. It is not refereed by another model family.
- **Before writing.** The own prior-art check found only block 137 and the probes problem posed after it.
- **Checks during the work.**
  - Single coin terms (swap, `σ·σ`, `σ₃σ₃`) failed for every coefficient.
  - The general terms were then treated with rotation-related and with independent axes.
  - The witness was confirmed with a random rational term.
  - The offset along the bond was checked separately.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_one_record_per_site_no_possibility_shift_among_neighbours_restores_the_books_no_neighbour_coin_term_keeps_two_excluded_records_energy_current_2026_09_25.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
