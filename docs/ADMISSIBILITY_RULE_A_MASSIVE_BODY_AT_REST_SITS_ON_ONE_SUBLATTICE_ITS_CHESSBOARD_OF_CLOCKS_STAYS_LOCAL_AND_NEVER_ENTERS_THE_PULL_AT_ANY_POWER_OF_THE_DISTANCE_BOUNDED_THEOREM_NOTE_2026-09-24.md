---
claim_id: admissibility_rule_a_massive_body_at_rest_sits_on_one_sublattice_its_chessboard_of_clocks_stays_local_and_never_enters_the_pull_at_any_power_of_the_distance_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: 'Supplied finite even-torus staggered-mass walk m>0: positive band-edge eigenspace spans even-sublattice
  corner modes, positive-energy eigenstate densities and mass expectation, and fixed-state clocked-density identities.
  The pure extended corner state has the stated mean-removed checkerboard source and linearized field at wbar1.
  Opposite-parity hopping is invariant under a global reciprocal checkerboard clock, while a mass term changes.
  Weak-field kernel identities hold for the stated matched rest-source equations. Rapid spatial decay requires an
  explicitly smooth spectral source vanishing near zero; arbitrary localized staggered envelopes do not satisfy
  that requirement. The original universal no-power-law-tail and interbody-pull conclusions are withdrawn.'
upstream_dependencies:
- admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
- admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
- admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21
- admissibility_rule_the_axioms_own_generator_the_scalar_hop_splits_the_eight_species_into_four_levels_of_one_sense_and_a_staggered_term_gives_them_mass_bounded_theorem_note_2026-09-22
- admissibility_rule_the_filled_seas_energy_as_the_ledgers_field_term_a_chessboard_of_clocks_is_invisible_the_sea_induces_a_clock_stiffness_not_the_curvature_member_bounded_theorem_note_2026-09-22
- admissibility_rule_the_strong_field_exactly_bodies_at_rest_make_the_clock_law_linear_in_the_root_of_the_rate_the_ledger_is_a_surface_term_bounded_by_a_capacity_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_a_massive_body_at_rest_sits_on_one_sublattice_its_chessboard_of_clocks_stays_local_and_never_enters_the_pull_2026_09_24.py
---

# Staggered-mass band-edge states, checkerboard clocks and the limit of a locality claim

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 54, 55, 56, 60, 76 and 77 as landed; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within blocks 54, 55, 56, 60, 76 and 77 as landed on main (the walk and its clock, the source as the amplitudes' energy density, the simplest and the curvature members, the chessboard of clocks, and the staggered mass); it reports where a massive body's energy sits, what its chessboard part does to the clocks, and whether that part enters the pull between bodies; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

On a finite even torus with m>0, the positive band-edge eigenspace of the supplied staggered-mass walk is supported on the even sublattice. Its spanning plane waves are extended states, not localized massive bodies. A fixed even-supported state retains a positive instantaneous mass density under arbitrary positive clocks, but generally ceases to be an eigenstate.

For a single uniform-density corner mode, the mean-removed density is a pure checkerboard and the stated linearized law gives a pure checkerboard field throughout the torus. Reciprocal checkerboard clock factors cancel on odd-parity hops; they do not cancel on the mass term.

The general locality claim does not follow. Multiplication by the checkerboard sign shifts a source's spectrum; it does not force that spectrum to vanish near zero. A point source at an even site is unchanged and retains its nonzero zero-momentum value. Only an explicitly smooth spectral component supported away from zero has the rapid-decay property proved below. No universal interbody force or all-orders multipole conclusion is retained.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "No possibility is privileged." "No site is privileged." The staggered mass breaks one-site translation, as block 77 as landed notes. It is supplied.
  - "Admissibility is not a dynamics axiom." The walk, the mass, the clock laws and the members are supplied. Nothing is adopted.
- **The walk** (block 54 as landed). `H = Σ_jσ_jD_j` with `(D_jψ)(x) = (i/2)(ψ(x − e_j) − ψ(x + e_j))`, whose symbol is `sin k_j`. The clocked walk is `φHφ`, with `w = φ² = e^u`.
- **The staggered mass**, with m>0 on even tori, (block 77 as landed). `ε(x) = (−1)^{x₁+x₂+x₃}` and `H + mε`, with `(H + mε)² = H² + m²` (block 77 T3). Clocked: `φ(H + mε)φ = φHφ + mwε`.
- **The source** (block 55 as landed): `e_x = Re ψ_x†(H_wψ)_x`.
- **The simplest member** (blocks 55–56 as landed). `F = (2/γ)Σ_bonds(φ_x − φ_y)²`. Its weak-field law, as a supplied model, is `(1 − A)u = −(γ/6)(e − ē)/w̄`, where `A` averages over the six neighbours.
- **The curvature member** (block 60 as landed). The rates are multipliers. The weak-field law is `Δu = (e + τ)/(4Kw̄)`, with `γ = 1/(4K)`.
- **The chessboard of clocks** (block 76 T1 as landed). `φ → φc^ε` leaves every opposite-parity hop unchanged.
- **Comparators, named only:** the Hellmann–Feynman theorem; the Coulomb kernel `1/|k|²` and its multipole expansion; staggered (Kogut–Susskind) fermions, whose mass term alternates.

## Theorem T1 — finite-torus positive band-edge eigenspace

*Statement.*
- (a) The eigenstates with eigenvalue+m of H+m epsilon are the linear span of `χ = e^{iπn·x}(1 + ε)u`, `n ∈ {0, 1}³`, `u ∈ ℂ²`. They satisfy `(H + mε)χ = mχ` and vanish on every odd site.
- (b) For normalized vectors in this span, their energy density is `e_x = m|χ_x|² ≥ 0` on the even sites and `0` on the odd ones, and its sum over sites, normalised, is `m`.
- (c) For the same fixed vector, with any positive clock field the instantaneous density is exactly `e_x = mw_x|χ_x|²`.

*Proof.*
- (a) `ε` anticommutes with `H`, so it maps `ker H` to itself. `ker H` is spanned by the eight zero modes `e^{iπn·x}u`, and `(1 + ε)` projects onto its `ε = +1` part, where `H + mε` acts as `m`.
- (b) and (c): at an even site `φHφχ` reads only odd neighbours, where `χ = 0`. So only the mass term contributes to the density. At odd sites the state itself vanishes even if the clocked hopping image is nonzero. Thus the density identity does not prove that the vector stays an eigenstate. Corner labels related by adding(1,1,1) give the same projected state; there are four independent spatial modes and two coin choices, hence dimension8 on nonaliasing even cubic tori. On the infinite lattice these plane waves are not square summable; no localized rest eigenstate is constructed.

∎

*Checked (B1).* On the `4³` torus, every one of the eight rest states with two coin vectors: the eigenvalue, the vanishing on odd sites, and the density and its sum. The density with a rational clock field.

## Theorem T2 — moving, the density stays non-negative

*Statement.* A normalized positive-energy eigenstate of `H + mε` has `e_x = E|ψ_x|² ≥ 0` at every site, with `E = √(|sin k|² + m²)`. Its mass part `Σmε|ψ|²` alternates in sign from site to site and sums, normalised, to `m²/E`. At `k = (π/2, 0, 0)` and `m = 3/4`: `ψ = e^{ik·x}(1 + ε/3)(1, 1)` has `E = 5/4`, weight `4/5` on the even sites and `1/5` on the odd ones, and mass part `9/20`.

*Proof.* `e_x = Re ψ_x†(Eψ)_x`. The anticommutator {epsilon,H+m epsilon}=2mI gives2E mean(epsilon)=2m in any normalized eigenstate with E!=0. This proves the mass expectation without a nondegeneracy assumption. ∎

*Checked (C1).* The eigenstate on the `4³` torus exactly, its weights, its mass part, and its density at every site.

## Theorem T3 — the chessboard of clocks

*Statement.*
- (a) `Aε = −ε`. For a single normalized projected corner plane wave the even density is2m/V, giving mean-removed source m epsilon/V. Set wbar=1. Thus the mean-removed source `(m/V)ε` is solved in the simplest member by `u = −(γm/(12V))ε`: a chessboard of clocks `φ = c^ε` with `c = e^{−γm/(24V)}`, slow on the body's sublattice.
- (b) For gamma>0 and c!=1 this clock pattern has the exact bond energy `(2/γ)·3V(c − 1/c)² > 0`.
- (c) Every bond product `φ_xφ_y` is `1`, so no operator that moves an odd number of steps feels it (block 76 T1).
- (d) A massive walker does feel it: `φ(mε)φ = m(c² − c^{−2})/2 + mε(c² + c^{−2})/2`, a scalar potential plus a factor on the mass.

This solves the linearized field equation; exponentiating u and evaluating its exact bond cost does not make it an exact nonlinear solution. General superpositions of corner modes can have additional density harmonics.

*Proof.*
- (a) Each of a site's six neighbours has the opposite sign.
- (b) Each of the `3V` bonds contributes `(c − 1/c)²`.
- (c) `c^{ε_x}c^{ε_y} = 1` for neighbours.
- (d) `mεc^{2ε}`, split by the sign of `ε`.

∎

*Checked (D1).* The average on the `4³` torus, the field equation, the bond sum, the bond products and the mass identity, exactly.

## Theorem T4 — matched symbols and a conditional spectral-decay lemma

Let Lambda(k)=sum_j2(1-cos k_j), and let A average the six neighbors. Then1-Ahat=Lambda/6. Both are positive away from0 modulo2pi; at pi(1,1,1) they equal2 and12. With wbar=1, gamma=1/(4K), and the curvature source restricted to tau=0 and the same e, both specified weak-field equations give uhat=-gamma ehat/Lambda. Here Lambda is the positive symbol; the curvature note's spatial difference operator has negative symbol-Lambda. This source matching is a hypothesis, not an identity for arbitrary matter states.

Suppose a periodic spectral source fhat is infinitely differentiable and vanishes in a neighborhood of0. Then -gamma fhat/Lambda is infinitely differentiable on the whole momentum torus, including the zero neighborhood where it is defined as0. Its inverse-transform coefficients decay faster than every inverse power: for any integer n, integrate by parts n times in a coordinate with maximal |x_j|. Periodicity eliminates boundary terms and bounds the coefficient by |x_j|^-n times the integral norm of that derivative. A smooth spectral cutoff away from0 gives this result when the source spectrum is smooth. A sharp cutoff does not automatically do so.

This lemma does not apply to every checkerboard-modulated localized source. For f(x)=delta_(x,0), epsilon(x)f(x)=f(x) and its transform equals1 at every momentum, including0. The multiplier retains its inverse-quadratic singularity. More generally the transformed modulated source is fhat(k-pi-vector), which need not vanish near0. A spatially broad smooth envelope need not have an exact spectral gap either.

The primary checks the two symbols and their normalization, and the point-source modulation countercontrol. No universal absence of algebraic tails, interbody potential or force is asserted. In particular a1/R expression would be a potential-energy scale in an additional interaction model, not itself a force law.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "blocks 76-77 as landed: the staggered mass's energy placement and whether its chessboard part sources clocks that enter the pull are not stated"
source_of_blocker_text: blocks 76 and 77 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the chessboard of clocks' self-energy for a localised massive body; the same question in the strong field of block 56"
conditional_surface_status: "T1-T3 under the specified finite-state and linearization hypotheses; T4 a conditional smooth-spectral lemma; walk, mass, clock laws and members supplied"
hypothetical_axiom_status: "the staggered mass and the members are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 54: the walk and its clock.
  - Block 55: the source.
  - Blocks 55–56: the simplest member, as a supplied model.
  - Block 60: the curvature member.
  - Block 76: the chessboard of clocks is invisible to hops.
  - Block 77: the staggered mass.
- **The probes attempt.** `the-rest-energy-density-of-a-massive-walker` a2 (Claude Opus 5.5) found T1–T4. A Grok referee confirmed it (#8996).
- **In the literature.**
  - The Hellmann–Feynman theorem.
  - The Coulomb kernel and multipole expansions.
  - Staggered fermions (Kogut and Susskind).

  All reference only.
- **New here:**
  - an independent exact runner;
  - the results placed against blocks 76 and 77 as landed;
  - the corrected distinction between an extended pure checkerboard mode and a localized modulated source.

## Exact target and obligation graph

Target: where a massive body's energy sits, and whether its chessboard part enters the pull. The obligations are:
- (O1) the rest density (T1);
- (O2) the moving density (T2);
- (O3) the chessboard of clocks (T3);
- (O4) the pull (T4).

The finite-state identities and kernel normalization are retained. The original general locality and pull obligations are not discharged; they are withdrawn.

## No-Go Discipline Gate

The original universal locality statement is false without a source spectral-gap condition and is not retained.

### N1 — Failure routes and conditions
A localized point source survives checkerboard modulation unchanged. Smooth envelopes can also leak into low momentum. A pure torus checkerboard has no spatial decay. Only a smooth spectrum vanishing near0 satisfies T4's rapid-decay lemma. Strong fields, physical forces and localized massive eigenstates remain outside the result.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied walk, mass, clock laws and members.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 54, 55, 56, 60, 76, 77 (landed) | the walk, source, members, chessboard and mass | yes (restated) |
| probes (Grok-refereed #8996) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "finite band-edge states occupy one sublattice; pure checkerboard clocks change the mass; general locality is withdrawn" | executed: the eight rest states, with and without clocks | executed: the moving density at every site | executed: the chessboard's field, cost and action | executed: the symbols and the kernel | T1–T3 on even tori; T4 on the infinite lattice; weak field |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Decisive countercontrol
Checkerboard modulation of a source at an even site leaves its nonzero monopole unchanged. Kernel smoothness near the stagger momentum alone cannot remove the zero-momentum singularity of its full response.

### N8 — Earlier claims
The finite-torus rest and moving-state identities survive. The broad locality and pull conclusions are withdrawn; the source spectral restriction is explicit.

## Falsifiers

- A positive+m finite-torus eigenstate with nonzero odd-sublattice content under the stated free operator.
- Failure of a displayed symbol, density or clock identity under its hypotheses.
- Failure of rapid decay for an infinitely differentiable periodic spectral response vanishing near0.

## Boundaries and non-claims

- The walk, the mass, the clock laws and the members are supplied.
- The strong field is not treated.
- No gravitational claim is made.

## Imports

- [Supplied source, block 54](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 55](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 56](ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 60](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 76](ADMISSIBILITY_RULE_THE_FILLED_SEAS_ENERGY_AS_THE_LEDGERS_FIELD_TERM_A_CHESSBOARD_OF_CLOCKS_IS_INVISIBLE_THE_SEA_INDUCES_A_CLOCK_STIFFNESS_NOT_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-22.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 77](ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_OF_ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.

- `minimal_axioms`. Blocks 54, 55, 56, 60, 76 and 77, restated.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - the Hellmann–Feynman theorem;
  - the decay of the transform of a smooth periodic function (Fourier analysis);
  - Gaussian-rational arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the eighty-first since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results. A Grok referee confirmed them (#8996).
  - The supervisor re-checked them with its own runner.
- **Before writing.**
  - Main was re-fetched, and blocks 54, 55, 56, 60, 76 and 77 were read as landed.
  - Two integer-division traps in the draft runner were caught and replaced by exact rationals.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_massive_body_at_rest_sits_on_one_sublattice_its_chessboard_of_clocks_stays_local_and_never_enters_the_pull_2026_09_24.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
