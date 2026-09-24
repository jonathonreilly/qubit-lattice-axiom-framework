---
claim_id: admissibility_rule_amplitudes_of_negative_energy_fall_like_the_others_and_source_the_opposite_field_a_negative_body_at_rest_has_a_largest_size_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "Conditional signed-source algebra in supplied hopping and static field models: site-local twins reverse energy density; prescribed even ray branches share trajectories after momentum reversal. A grounded one-source model has exact charge roots and a positivity threshold; a rates-operator criterion assumes an existing length solution. The exact infinite-lattice positive-energy orthogonal projector is not finite range. No universal chase dynamics or extended-body threshold is derived."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_strong_field_exactly_bodies_at_rest_make_the_clock_law_linear_in_the_root_of_the_rate_the_ledger_is_a_surface_term_bounded_by_a_capacity_bounded_theorem_note_2026-09-21
  - admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_amplitudes_of_negative_energy_fall_like_the_others_and_source_the_opposite_field_2026_09_21.py
---

# Signed sources: weak pair identities, finite grounded fields and spectral projectors

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

For supplied hopping H and phi>0 use H_w=phi H phi and e_x=Re psi_x^dagger(H_w psi)_x. The twin A_n=Theta V_n uses an odd exchange map of PR #8602. The reduced massive comparator in T1(b) is H=sigma3 S+m sigma1, with chi_x(1,-1)/sqrt(2), real chi_x, so its local mass density is -m w_x chi_x^2. It is distinct from the massless three-dimensional twin construction.

For T2 supply an even translation-invariant weak-field kernel G0, source strength S=cE with c>0, and force -E times the central difference of the other source's field -gamma S G0. For the local massive ray use m>0 and positive w; this is an independent smooth ray model.

For T3 set K>0, mu=m/(8K), Delta the nearest-neighbour difference on a finite connected box with chi=N=1 at the held boundary. Supply equations Delta chi=-mu_x/chi_x and Delta N=(Q_x/chi_x)N with Q_x=mu_x/chi_x, w=N/chi. The grounded inverse kernel is g=(-Delta)^-1 delta at the one source and g0 its diagonal, with 0<g<=g0. For several sources L=-Delta+diag(Q/chi), with fixed positive boundary forcing. These are diagonal-source static field equations, not stationary matter wavefunctions.

## Theorem T1 — twins source oppositely

*Statement.* (a) For every state, every positive rate field and every odd `n`: `e_x[A_nψ] = −e_x[ψ]` and `|A_nψ|²_x = |ψ|²_x` at every site. (b) On the reduced walk with any rate field, an amplitude with a real envelope and the content `(1, −1)` has `e_x = −m w_x|χ_x|²` at every site. (c) Block 55 T1 and T2 hold for amplitudes of either sign; under block 55's law the twin of an amplitude is the source of the opposite weak field.

*Proof.* (a) Block 70 T1(d): `V_n` multiplies the energy density by `s_n = −1`. `Θ` commutes with `H_w`, so `(Θψ)†_x(H_wΘψ)_x = (σ_2ψ̄)†_x(σ_2\overline{H_wψ})_x` is the complex conjugate of `ψ†_x(H_wψ)_x`, with the same real part. Both maps are unitary or antiunitary site by site. (b) `(1, −1)σ_3(1, −1)ᵀ = 0` and `(1, −1)σ_1(1, −1)ᵀ = −2`. (c) The proofs of block 55 T1, T2 use that `⟨H_w⟩` is a quadratic form in `φ`, not its sign. ∎

The real-envelope example has a vanishing instantaneous hopping-energy contribution; it is not thereby an eigenstate or a stationary quantum body. Negative total expectation does not force every local energy density to be negative.

## Theorem T2 — pairs

*Statement.* (a) Within the supplied weak-field pair ansatz with a translation-invariant even kernel G0, for two distinct point sources with `S = cE`, `c > 0`: the pull on `A` is `γcE_AE_B∇_cG_0(x_A − x_B)`, and the two pulls sum to zero for any signs of the energies. (b) A ray starting from rest obeys `d²x/dt² = −w∇w` whatever the sign of its energy. If the kernel gradient at their separation is nonzero and has the stipulated attractive orientation for a positive source, the resulting initial acceleration has the stated sign: positive-source attraction and negative-source repulsion in this ansatz. Zero force, anisotropy, arbitrary finite boxes, later finite velocities and self-consistent coupled trajectories are not covered. (c) If `(x(t), p(t))` is a ray of `w(x)ε(p)`, `ε` even, then `(x(t), −p(t))` is a ray of `−w(x)ε(p)`.

*Proof.* (a) Block 55 T3's formula; it is antisymmetric under exchange for every sign. (b) For `±w(m² + sin²p)^{1/2}` at small `p`: `dx/dt = ±wp/m`, `dp/dt = ∓m∇w`, so `d²x/dt² = −w∇w` at `p = 0`; the two signs cancel. (c) `∂(−ε)/∂p` at `−p` equals `∂ε/∂p` at `p`, and `d(−p)/dt = −(−ε)∇w`. ∎

The antisymmetric pair-pull formula gives zero total pair force in this specified weak model. It does not supply an exact coupled dynamical conservation theorem. For a negative branch, canonical momentum and velocity can have opposite signs.

## Theorem T3 — a negative body at rest in the curvature member

*Statement.* One body at rest at a site of a box with held walls, `μ = m/(8K)` of either sign. (a) Writing the algebraic discriminant, the one-source equation has real charge roots iff `1 + 4g_0μ ≥ 0`; they are `χ = 1 + Qg`, `Q = (±r − 1)/(2g_0)`, `r = (1 + 4g_0μ)^{1/2}`. For negative mu with nonnegative discriminant both roots give positive chi; at mu=0 the lower root has chi0=0 and is inadmissible; for `μ > 0` only the upper sign has (block 60's solution). (b) For `r > 0` the rates are `N = 1 − Pg`, `P = Q/(±r)`. With the upper sign: `χ_0 = (1 + r)/2`, `w_0 = 1/r`, all rates positive; for `μ < 0`, `w ≥ 1` everywhere. With the lower sign `N` at the body is `−(1 − r)/(2r)` and the rate there is `−1/r < 0`, for `0 < r < 1`. (c) At `r = 0`, `Q/χ_0 = −1/g_0`, `Lg = 0`, and the rates' equation has no solution. Hence a negative body at rest has a static field with positive rates iff `m > −2K/g_0`. (d) For fixed source coefficients of either sign and an already existing positive chi solution in a finite connected grounded box, positive N solving the linear rates equation exists iff L is positive definite. This does not establish the nonlinear chi solution for arbitrary sources. (e) The ledger of the box is `M = 8KQ = (4K/g_0)(r − 1) > −4K/g_0`; far from the body the lengths carry `2Q` and the rates `P + Q`, and the formal distant weak-exterior ratio of the supplied local ray comparison is `1 + 2r/(1 + r)`: between 2 and 3 for a positive body (block 60), between 1 and 2 for a negative one. (f) In block 56's member `φ_0 = 1/(1 + γmg_0/2)`; at `m = −2/(γg_0)` the same `g` is a zero mode.

*Proof.* (a) Off the body `Δχ = 0`, so `χ = 1 + Qg` with `Q(1 + Qg_0) = μ`; for `μ < 0`, `Q < 0` and `g ≤ g_0` give `χ ≥ 1 + Qg_0 = (1 ± r)/2 > 0` since `r < 1`; for `μ > 0` the lower sign has `χ_0 = (1 − r)/2 < 0`. (b) `N = 1 − Pg` with `P = (Q/χ_0)(1 − Pg_0)`, i.e. `P(1 + 2Qg_0) = Q`, and `1 + 2Qg_0 = ±r`; `N_0 = χ_0/(±r)`. For `μ < 0` and the upper sign `Q, P < 0`, so `χ ≤ 1 ≤ N`. (c) `(−Δg)_z = δ_z` and `(Q/χ_0)g_0 = −1`. Writing `N = 1 + n`, `Ln = −(Q/χ_0)δ`; pairing with the zero mode gives `0 = g_0/g_0 = 1`. (d) If `L` is positive definite and `LN' = b` with `b ≥ 0` the walls' contribution: split `N' = N⁺ − N⁻`; `⟨N⁻, LN⁺⟩ ≤ 0` because the off-diagonal entries are non-positive and the supports disjoint, so `⟨N⁻, LN⁻⟩ ≤ −⟨N⁻, b⟩ ≤ 0` and `N⁻ = 0`; a zero of `N'` at an interior site would force zeros at its neighbours and so up to the walls. Conversely let `f > 0` be the lowest mode of `L` (named under Imports), eigenvalue `λ`: `λ⟨f, N'⟩ = ⟨f, b⟩ > 0`. (e) Block 60 T4(c), (d), whose proofs do not use the sign. (f) Block 56's law is `(2/γ)(−Δφ)_z + m_zφ_z = 0`; `φ = 1 − (γ/2)mφ_0g`. ∎

## Theorem T4 — the exact positive-energy orthogonal projector is not finite range

*Statement.* (a) On the infinite translation-invariant lattice, the exact orthogonal spectral projector onto the positive energies of the walk has the symbol `½(1 + σ·s/|s|)`, `s_a = sin k_a`, which has different limits along different directions at each of the eight zeros. An operator that commutes with translations and has finite range or an absolutely summable translation kernel has a continuous symbol. (b) For the reduced walk with `m > 0` the symbol is continuous, and it is not a trigonometric polynomial.

*Proof.* (a) Along `k = (t, 0, 0)` the unit vector is `±e_1` for `t → 0±`; block 70's maps carry this zero to the others. (b) If it were, `1/ε` would be a trigonometric polynomial `p` with `p²(m² + sin²k) = 1`; the top coefficient of the left side is `−a²/4`, `a` that of `p`. ∎


The projector result concerns this exact spectral projector, not every possible state-selection rule, approximate filter or finite periodic matrix. On a finite torus every operator has finite system-sized reach. The one-source lower energy bounds above are bounds on its supplied bare-energy parameter, not bounds on spatial size. Extending them to an extended source requires solving the coupled source equations and is not established by replacing g0 with a smaller scalar.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Signed pair motion is confined to a prescribed weak ray ansatz. Static field positivity does not establish a stationary quantum body or nonlinear many-source existence. The nonlocality result concerns one exact infinite-lattice orthogonal projector.

### N2 — Wall independence
No repository no-go wall is used.

### N3 — Supplied structure
The operators, domains, boundary conditions and state assumptions stated above are explicit mathematical hypotheses. They do not add a framework axiom or primitive.

### N4 — Dependencies
The dependencies below identify the actual supplied inputs; earlier stronger conclusions are not imported.

### N5 — Resolution
The canonical runner checks the finite examples and identities stated above using exact arithmetic. General conclusions require the displayed arguments, not extrapolation from samples. Historical simulations are deferred.

### N6 — Primitive boundary
No new primitive, species selection, filling rule or physical interpretation is adopted.

### N7 — Strongest objection
Signed pair motion is confined to a prescribed weak ray ansatz. Static field positivity does not establish a stationary quantum body or nonlinear many-source existence. The nonlocality result concerns one exact infinite-lattice orthogonal projector.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8571; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_strong_field_exactly_bodies_at_rest_make_the_clock_law_linear_in_the_root_of_the_rate_the_ledger_is_a_surface_term_bounded_by_a_capacity_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8573; no premise adoption or retained grade is inferred.
- [admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8590; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_THE_EIGHT_SPECIES_ARE_EXCHANGED_BY_SITE_SIGNS_AND_A_HALF_TURN_OF_THE_COIN_WHAT_EACH_VARYING_FIELD_BECOMES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8602; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8603 head `e7ef26762e497345834dacc1c70f978fbd7242fc`, branch `physics-loop/admissibility-induced-law-block71-amplitudes-of-negative-energy-as-sources-20260921`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_amplitudes_of_negative_energy_fall_like_the_others_and_source_the_opposite_field_2026_09_21.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
