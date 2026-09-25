---
claim_id: admissibility_rule_under_one_record_per_site_the_a_terms_levels_are_frozen_or_out_of_reach_the_middle_level_is_one_record_per_site_and_a_full_lattice_has_a_constant_generator_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Supplied two-state nearest-neighbor family on even cubic tori, a>0, and separately supplied symmetric
  or antisymmetric many-record hard-core compression. Exact free-comparator state counts, constant fully occupied
  compressed generator, hole-sector norm bound, and alternating corner moments. The lower-window hole count is a
  free-comparator record-number estimate, with the stated infinite-volume density upper bound for 0<a<1/12. No free
  band-filling interpretation for the interacting compressed model, no impossibility of mobile lower fillings or
  single-orientation interacting excitations.
upstream_dependencies:
- admissibility_rule_one_record_per_site_is_an_interaction_not_a_free_sea_two_records_under_exclusion_against_free_antisymmetric_and_symmetric_pairs_bounded_theorem_note_2026-09-22
- admissibility_rule_the_axioms_own_generator_the_scalar_hop_splits_the_eight_species_into_four_levels_of_one_sense_and_a_staggered_term_gives_them_mass_bounded_theorem_note_2026-09-22
runner: scripts/admissibility_rule_under_one_record_per_site_the_a_terms_levels_are_frozen_or_out_of_reach_2026_09_24.py
---

# Free-comparator filling counts and the fully occupied hard-core generator

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 77 and 78 as landed, with the compression extended to many records; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within blocks 77 and 78 as landed on main, with block 77's supplied family and staggered sign and block 78's hard-core compression extended to many records; it reports where the family's levels sit in record number and what one record per site does there; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The free two-state comparator has N-z/2 states strictly below a0 and z at a0. Half filling is N records after occupying half the zero-level space; a0 is a spectral midpoint, not one of the four corner levels when a>0. Its upper-window filling counts exceed N and cannot be realized as the same record count with at most one record per site.

Separately, at N records the supplied compressed hopping generator is a scalar on all coin configurations: only a global phase evolves. This does not erase the coin space or possible translation labels. Lower fillings are allowed and can move. Counting comparator levels does not establish band filling, crossing content or absence of single-orientation excitations for the interacting compressed generator.

For Nh holes on an even torus the moving part has norm at most6(|a|+1/2)Nh. A separate free-comparator count shows that its lower window has a small hole density as a tends to0. The eight free corner moments cancel through degree2. These are conditional algebraic statements, not an interacting-gas classification.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "A site never carries more than one record; records are permanent." This is the premise of the hard-core compression.
  - "Records form." Which states the records fill is not given by the axioms.
  - "Admissibility is not a dynamics axiom." The family, the staggered term and the composition are supplied clauses. Nothing is adopted.
- **The family** (block 77 as landed). `H_a = a₀I + 2aΣ_jC_j + Σ_jσ_jS_j` on the torus `Z_L³` with `L>=4` even, where:
  - `C_j = (T_j + T_j⁻¹)/2` and `S_j = (T_j − T_j⁻¹)/(2i)`;
  - `N = L³` sites carry a two-state coin, so the one-record space has dimension `2N`;
  - `a₀` and `a` are real, with `a > 0` here, and `A = H_a − a₀I`.

  Its two bands are `E_± = a₀ + 2aΣcos k_j ± |sin k|`.
- **The staggered term** (block 77 as landed). `mε`, with `ε_x = (−1)^{x₁+x₂+x₃}` and real `m`. It is supplied.
- **The free comparator.** The antisymmetric many-record state filled to a level `μ`. It allows two records on a site with different coin states, so it is a comparator only: block 78, as landed, shows that one record per site is an interaction.
- **The hard-core compression.** Block 78's compressed generator, extended to many records: the free many-record generator restricted to configurations with at most one record per site. It comes with the antisymmetric or the symmetric composition. Block 78 calls the compression and the composition supplied model choices; so does this note.
- **Comparators, named only:** the filling of a band up to its top level (the Fermi level of a metal); the lattice theorems on the net sense of crossings (Nielsen–Ninomiya, and 't Hooft's anomaly matching for interacting content).

## Theorem T1 — free-comparator midpoint and window counts

*Statement.* On an even torus, let `z = #(E = a₀)` in the one-record spectrum.
- (a) Exactly `N − z/2` one-record states lie below `a₀`, and `z` is even.
- (b) For every `μ ∈ (a₀ + 2a, a₀ + 6a)`, at least `N + 6 + z/2` states lie below `μ`.
- (c) For every `μ ∈ (a₀ − 6a, a₀ − 2a)`, at most `N − 6 − z/2` states lie below `μ`.
- (d) With `mε`, `m ≠ 0`: exactly `N` states lie below `a₀`, and none within `|m|` of it.

*Proof.*
- (a) `A` has no on-site part, and `ε` anticommutes with every one-step hop, so `εAε = −A`. The spectrum of `A` is therefore symmetric about zero with multiplicities. So `#(A < 0) = #(A > 0) = (2N − z)/2`.
- (b) The three corners with `|n| = 1` carry six states at `a₀ + 2a`, which lies in `(a₀, μ)`. So at least `(N − z/2) + z + 6` states lie below `μ`.
- (c) The three corners with `|n| = 2` carry six states at `a₀ − 2a`, which is at least `μ` and below `a₀`. So at most `N − z/2 − 6` states lie below `μ`.
- (d) `X = εT₁` anticommutes with `A + mε`. `T₁` commutes with `A` and flips `ε`, and the outer `ε` flips both. Also `(A + mε)² = A² + m² ≥ m²` (block 77 T3). So the spectrum of `A + mε` is symmetric about zero with no state inside `(−|m|, |m|)`, and exactly `N` states lie below zero.

∎

*Checked (B1).*
- Exact band counts on `4³` and `6³` for `(a₀, a) = (1/3, 1/10)`, `(0, 1/4)` and `(−2/5, 2/3)`.
- The odd `3³` torus gives `26` of `54`: even sides are needed.
- The three operator identities on every basis vector of `4³`, with symbolic `a` and `m`.

## Theorem T2 — at one record per site the generator is a constant

*Statement.* Under the hard-core compression at most `N` records fit. At `N` records the generator of either composition is `Σ_x(a₀ + mε_x) = Na₀` times the identity on the `2^N` coin configurations. In the clocked form the site part is `Σ_x w_x(a₀ + mε_x)`, again a multiple of the identity.

*Proof.*
- Every term of `A` moves a record by one site, and `a₀` and `mε` are site terms.
- At `N` records every site is occupied, so every hop lands on an occupied site and the compression removes it.
- What remains is the site part. `ε` sums to zero on an even torus.
- No hop survives, so the composition's sign plays no role.

∎

*Checked (C1).*
- Four records on block 78's ring of four, with the family's one-axis member: the generator is exactly `4a₀` times the identity on all `16` coin configurations, for both compositions.
- With three records the generator is hermitian and moves the hole.

## Theorem T3 — just below one record per site only holes move

*Statement.*
- (a) On an even torus, with `N − N_h` records, the generator is `D + T`, where `D` is diagonal with `|D − (N − N_h)a₀| ≤ |m|N_h`, and `‖T‖ ≤ 6(|a| + ½)N_h`. The whole compressed-sector spectrum lies within `N_h(6(|a| + ½) + |m|)` of `(N − N_h)a₀`.
- (b) In the unstaggered free comparator (m=0), for a filling level `μ ∈ (a₀ − 6a, a₀ − 2a)`, the holes number at most `z/2 + #(a₀ − 6a < E < a₀)`. For `a < 1/12` this is at most `16 arcsin(12a)³/π³` per site as `L → ∞`.

*Proof.*
- (a)
  - A configuration with `N_h` holes allows at most `6N_h` hops, since each hole has six neighbours.
  - Each hop carries the coin matrix `a·1 ± σ_j/(2i)`. Its column sums of moduli are `|a| + ½` for `σ₁` and `σ₂`, and `√(a² + ¼) ≤ |a| + ½` for `σ₃`. The composition's signs do not change moduli.
  - `T` is hermitian, so its norm is at most its largest row sum of moduli.
  - The diagonal is `Σ_{occupied}(a₀ + mε_x) = (N − N_h)a₀ − mΣ_{holes}ε_x`.
- (b)
  - `N_h = N − #(E < μ) ≤ N − #(E ≤ a₀ − 6a) = z/2 + #(a₀ − 6a < E < a₀)`, by T1(a).
  - `|E − a₀| ≥ |sin k| − 6a`, so `|E − a₀| < 6a` forces `|sin k| < 12a`.
  - The zero-level states in z/2 obey the same strict |sin k|<12a bound when a>0. Thus count the union of these and the negative-window states, bounding each momentum by two bands, not adding a second copy of the zero states. Then each `k_j` lies within `θ = arcsin(12a)` of `0` or `π`: a fraction (2theta/pi)^3 of the continuous zone, for each of the two bands. Uniform finite grids approach this box volume since its boundary has zero volume. This gives the limsup density bound16theta^3/pi^3; it is not that bound for every finite torus.

∎

*Checked (D1).*
- The coin matrices' column sums, exactly.
- On the ring of six with one and two holes, for both compositions:
  - the generator is hermitian;
  - every row sum is at most `2(|a| + ½)N_h` (two hops per hole on a ring).
- `56` of the `1728` momenta of `12³` have `|sin k| < 12a` at `a = 1/20`.
- On `6³` at `μ = a₀ − 4a` the hole count is within its bound.

## Theorem T4 — the corners' senses net to zero

*Statement.* With `L_n = a₀ + 2a(3 − 2|n|)` and `χ_n = (−1)^{|n|}` over the eight corners, `Σ_nχ_nL_n^p` is `0` for `p = 0, 1, 2` and `384a³` for `p = 3`, for every `a₀`.

*Proof.* Write `s_j = (−1)^{n_j}`. Then `χ_n = s₁s₂s₃` and `L_n = a₀ + 2a(s₁ + s₂ + s₃)`. A sum over `s ∈ {±1}³` of a monomial vanishes unless each `s_j` appears to an even power, so only terms of `L_n^p` containing `s₁s₂s₃` survive. That needs `p ≥ 3`, and at `p = 3` the term `3!(2a)³s₁s₂s₃` gives `8·6·8a³`. ∎

*Checked (E1).* The four moments, symbolically in `a₀` and `a`, and the multiplicities.

*Reading.* The moment identity concerns eight free corners. It does not determine the content of the interacting hole gas. The fully occupied case is frozen under this hopping generator, but the lower-window comparator count is below N and supplies no obstruction to mobile compressed states at that number. No equivalence of their excitation spectra is assumed.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 77 as landed: the corner levels are not a claim about a filling or an occupation; the fork probe of 2026-09-22 asked whether a filling between the levels carries content of one sense"
source_of_blocker_text: block 77 as landed; the fork probe of 2026-09-22
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the one-hole problem in a coin background (its crossings in total momentum and their senses); the net sense of the interacting hole gas; the parked larger-site-algebra decision stays parked"
conditional_surface_status: "T1 exact on even tori; T2 exact on every even torus; T3(a) even tori, T3(b) for 0<a<1/12 in the infinite-volume density limit; the family, the stagger and the compression supplied"
hypothetical_axiom_status: "the family, the stagger and the many-record compression are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 77: the family, its corner levels and senses, the staggered sign and `(K + mε)² = K² + m²`.
  - Block 78: one record per site is an interaction, and the compression and the composition are supplied choices.
- **The probes attempts.**
  - `filling-between-the-a-terms-levels-chiral-content` a2 (Claude Opus 5.5, issue #9106) found T1–T4. A Grok referee confirmed them (#9126).
  - Attempt a1 (Claude Opus 5.5, no HIT) treated the free comparator's crossings and the staggered gap. It is credited there and not used here.
- **In the literature.**
  - The filling of bands to a top level (the Fermi level).
  - The crossing theorems of Nielsen and Ninomiya, and 't Hooft's anomaly matching.
  - The Gershgorin bound on a matrix's spectrum by row sums.

  All reference only.
- **New here:**
  - an independent exact runner;
  - the results placed against blocks 77 and 78 as landed;
  - the distinction between comparator record counts and the separate compressed-sector generator; interacting excitation content remains open.

## Exact target and obligation graph

Target: where block 77's levels sit in record number, and what one record per site does there. The obligations are:
- (O1) the counts (T1);
- (O2) the full lattice (T2);
- (O3) the nearly full lattice (T3);
- (O4) the senses (T4).

T1–T4 discharge them. Open: the hole gas's own crossings and senses.

## No-Go Discipline Gate

The negative statements are only that more than N records cannot fit under the site constraint, and that the supplied fully occupied hopping generator has no off-diagonal action. Neither excludes mobile lower fillings.

### N1 — Routes by which the sentence could fail or mislead
1. *Another reading of "one record per site at a time".* Two coin states on a site, or records that share a site in passing, would change T2. That is the parked decision on a larger site algebra, which this note does not touch.
2. *Interacting content.* The hole gas of T3 is interacting. Its low-energy content is not solved here, and its senses are not claimed.
3. *Odd tori and infinite volume.* T1(a)'s exact count needs even sides. In infinite volume it holds as a density, by the symmetric spectral measure.
4. *Other compositions.* T2 and T3 hold for either of the two supplied composition signs, because hops either vanish or keep their moduli.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied family, the stagger and the compression.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | one record per site; records form; no dynamics in the axioms | yes |
| blocks 77, 78 (landed) | the family, the levels, the stagger; the compression as a supplied choice | yes (restated) |
| probes (#9106; Grok-refereed #9126) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "half filling is N after half of the zero-level space; upper-window comparator fillings need more; at one record per site the generator is constant; near it only holes move" | executed: the stagger identities on every basis vector of `4³`, symbolic `a` and `m` | executed: the full ring under both compositions; the hole generator's hermiticity and row sums | executed: exact counts on `4³`, `6³`, `3³`; the thin window on `12³` | executed: the sense-weighted moments; the hole count against its bound | even tori for T1; every even torus for T2; T3(b) in the infinite-volume limit for `0<a<1/12`; the family, the stagger and the compression supplied |

### N6 — Partial-closure paths and primitive scan
The hard-core compression is a model choice compatible with one record per site, not the unique dynamics implied by it. No registered primitive is used, and nothing is proposed for registration. The parked decision on a larger site algebra is named in N1 and not touched.

### N7 — Steelman
- *Objection:* "The free comparator's crossings are the physics, and the compression is an artefact."
  - *Reply:* The axioms say a site never carries more than one record. Block 78 as landed shows that the compression is an interaction, not a small correction.
  - The comparator's fillings between the upper levels need more records than there are sites. That is not a matter of degree.

### N8 — Cross-cycle echo
- Block 77 found the levels and their senses, and left the occupation open.
- Block 78 found that one record per site is an interaction.
- This note finds where the levels sit in record number and what the interaction does there.

## Falsifiers

- An even torus on which the number of states below `a₀` differs from `N − z/2`.
- A filling level in `(a₀ + 2a, a₀ + 6a)` below which fewer than `N + 6 + z/2` states lie.
- A full lattice on which the compressed generator moves a record.
- A configuration with `N_h` holes whose moving part has a row sum above `6(|a| + ½)N_h`.

## Boundaries and non-claims

- The family, the stagger and the compression are supplied.
- The hole gas's crossings and senses, and the anomaly question for interacting content, are not claimed.
- The parked decision on a larger site algebra is not touched.
- No gravitational claim is made.

## Imports

- [Supplied source, block 77](ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_OF_ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 78](ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_IS_AN_INTERACTION_NOT_A_FREE_SEA_TWO_RECORDS_UNDER_EXCLUSION_AGAINST_FREE_ANTISYMMETRIC_AND_SYMMETRIC_PAIRS_BOUNDED_THEOREM_NOTE_2026-09-22.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.

- `minimal_axioms`. Blocks 77 and 78, restated.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - the spectral symmetry of an operator anticommuting with an involution;
  - the Gershgorin bound on a hermitian matrix's norm by its largest row sum of moduli;
  - exact rational and symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the seventy-third since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results (#9106). A Grok referee confirmed them (#9126).
  - The supervisor re-checked them with its own runner, including the ring generator for both compositions.
- **Before writing.**
  - Main was re-fetched, and blocks 77 and 78 were read as landed.
  - The own-prior-art check found no earlier block on the occupation of the levels. Block 80, as landed, keeps no claim about the interacting sea.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_under_one_record_per_site_the_a_terms_levels_are_frozen_or_out_of_reach_2026_09_24.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
