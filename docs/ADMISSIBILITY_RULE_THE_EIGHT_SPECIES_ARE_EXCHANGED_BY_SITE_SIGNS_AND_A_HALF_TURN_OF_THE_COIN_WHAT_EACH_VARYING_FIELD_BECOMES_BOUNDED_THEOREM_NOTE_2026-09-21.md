---
claim_id: admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "On even finite tori, site-sign and coin maps obey the stated operator transformation table for real supplied rates, frames, linearized twists and strains. Antiunitary symmetry doubles finite static eigenlevels; odd hopping gives spectral reversal. A varying reach-two example lacks spectral symmetry. Formal uniform branch-label orbits do not establish eightfold degeneracy in arbitrary varying fields."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
  - admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21
  - admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_makes_a_varying_rotation_of_the_coin_axes_a_symmetry_bounded_theorem_note_2026-09-21
  - admissibility_rule_eight_species_of_the_walk_the_nearest_neighbour_frame_shows_them_the_same_lengths_the_relabellings_coupling_shows_them_different_lengths_bounded_theorem_note_2026-09-21
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_2026_09_21.py
---

# Exact exchange maps for supplied lattice fields

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

On an even periodic lattice let H=sum_a sigma_a S_a; rates give phi H phi and frames give sum_j{E^j dot sigma,S_j}/2. The linearized twist operator is H+sum_j{(theta cross e_j) dot sigma,S_j}/2+sum_a C_a[d_a theta_a]/2. The two strain families add sum_(a,j) sigma_a{C_a[B_a^j],M_j}/2 with M_j=S_j or P_j=S_j C_j. All fields are real; the finite matrices are Hermitian.

For n in {0,1}^3 set D_a=(-1)^n_a, s=product D_a and rho=sD. The map U_n multiplies by (-1)^(n dot x). R_n is the identity or the coin matrix for the axis fixed by the diagonal proper rotation rho; V_n=R_n U_n. Define Theta=sigma2 followed by complex conjugation, and Pi psi(x)=psi(-x). Even side lengths ensure periodicity of the sign maps. The three nonidentity even V maps anticommute pairwise; the identity does not.

## Theorem T1 — the exchange maps

*Statement.* (a) `U_nT_aU_n = D_aT_a`; hence `S_a → D_aS_a`, `C_a[v] → D_aC_a[v]` for every bond function `v`, `P_a → P_a`, and site functions are unchanged. (b) `V_nHV_n = s_nH`, and `V_n(φHφ)V_n = s_n φHφ` for every rate field. (c) `V_n² = 1`; `V_{(110)}V_{(011)} = −V_{(011)}V_{(110)} = iV_{(101)}`. (d) At every site `ψ†ψ` is unchanged, `ψ†σ_aψ` is multiplied by `(ρ_n)_a`, and `Re ψ†(Hψ)` by `s_n`. (e) Near `k = πn + q`, `H ≈ Σ_a D_aσ_aq_a`: the map from `q` to the coin's vector has determinant `s_n` — the sense of the species; four species have each sense.

*Proof.* (a) `(U T_a U ψ)(x) = (−1)^{n·x}(−1)^{n·(x + e_a)}ψ(x + e_a)`. `P_a` moves two steps. (b) `U_nHU_n = Σ D_aσ_aS_a = s_n Σ(ρ_n)_aσ_aS_a`, and `R_nσ_aR_n = (ρ_n)_aσ_a` because `ρ_n` is a proper rotation. `φ` is a site function. (c) `U_n` and `R_n` are commuting involutions; `σ_3σ_1 = iσ_2`. (d) `V_n` is a unitary acting site by site. (e) The slopes of `sin k_a` at `0` and `π` are `±1`. ∎

## Theorem T2 — what each varying field becomes

*Statement.* For all real fields, varying in any way:

| Field | `V_n H[·] V_n` |
|---|---|
| rates `φ` | `s_n φHφ` (unchanged) |
| frame `E` | `s_n H[ρ_nEρ_n]` |
| twist `ϑ` | `s_n H[ρ_nϑ]` |
| reach-two strain `B` | `s_n H₂[BD_n]` |
| reach-three strain `B` | `s_n H₃[B]` (unchanged) |

*Proof.* Term by term with T1(a), `R_nσ_aR_n = ρ_aσ_a`, `D_a = s_nρ_a`, and `ρ_aρ_j = ρ_b` for `a, b, j` distinct. Frame: `½{E_a^jρ_aσ_a, D_jS_j} = s_n½{(ρ_aE_a^jρ_j)σ_a, S_j}`. Twist: `ρ_aD_jε_{abj}ϑ_b = s_nε_{abj}(ρϑ)_b`, and `D_aC_a[d_aϑ_a] = s_nC_a[d_a(ρϑ)_a]`. Reach two: `ρ_aD_aD_j σ_a½{C_a[B_a^j], S_j} = s_n σ_a½{C_a[B_a^jD_j], S_j}`. Reach three: `P_j` is unchanged, so only `ρ_aD_a = s_n` appears. ∎

The frame's inverse metric `g = EᵀE` becomes `ρgρ = DgD`: block 68 T2, now for frames that vary. `B → BD` acts on one index only; it is not a rotation of the strain, and the inverse metric becomes `(1 + BD)ᵀ(1 + BD)`: block 68 T3. Block 69 T4 is the last row. The table is exact for the displayed linearized twist operator. It does not supply a nonlinear finite-rotation completion or a full coupled field solution.

## Theorem T3 — two classes of eight, mirror twins, and the energy reversal

*Statement.* (a) With rates and reach-three strains in any configuration, the three nonidentity even maps commute with the generator: they carry every solution to a solution in the same fields with the same site densities and energy densities. (b) `Θ` commutes with the walk in all five kinds of field, and `Θ² = −1`, so every eigenvalue of a finite static Hermitian member is at least doubly degenerate; an infinite operator requires appropriate domain invariance and a separate interpretation of any continuous spectrum. For odd `n`, `A_n = ΘV_n` is antilinear with `A_nH = −HA_n` for rates and reach-three strains: for static real fields it carries every solution to a solution in the same fields with the same site probabilities and energy density reversed. For uniform fields in a regime with identifiable nonzero-energy corner branches, the sixteen formal labels fall into two orbits of eight under these sign transformations, labelled by s_n times sign(E). This is not eightfold eigenspace degeneracy or a count of linearly independent states. Arbitrary varying fields have no exact corner momentum label. (c) `ΠH[F]Π = −H[F∘Π]` for each of the five kinds of field, `F∘Π` the mirror image (a site field at `−x`; a bond field on the inverted bond): `ΘΠ` carries a solution of one class in `F` to a solution of the other class in `F∘Π`. (d) `U_{(111)}HU_{(111)} = −H` for rates, frames, twists and reach-three strains, so their spectra are symmetric about zero in every configuration; `U_{(111)}H₂[B]U_{(111)} = −H₂[−B]`, and the spectrum of `H₂[B]` is not symmetric in general: `tr H₂[B]³ = −735/8192` for the rational strain field of the runner on a `4×4×4` torus.

*Proof.* (a) T2 with `s_n = 1`. (b) `ΘS_jΘ⁻¹ = −S_j`, `ΘP_jΘ⁻¹ = −P_j`, `ΘC_a[v]Θ⁻¹ = C_a[v]`, `Θσ_aΘ⁻¹ = −σ_a`, real fields unchanged; each term of each generator contains an even number of reversed factors. If `Hψ = Eψ` then `HΘψ = EΘψ`; an antiunitary map has `⟨Θa|Θb⟩ = ⟨b|a⟩`, so `⟨Θψ|Θ²ψ⟩ = ⟨Θψ|ψ⟩`, while the left side is `−⟨Θψ|ψ⟩`: `Θψ` is orthogonal to `ψ`. An antilinear `A` with `AH = −HA` gives `i∂_t(Aψ) = −A(i∂_tψ) = −AHψ = HAψ`. Even maps keep the species' parity and the energy; odd maps flip both; In the free uniform corner labelling Theta keeps both. Since it is antiunitary and commutes with H, its same-time application reverses time evolution; the same-time solution statement instead uses the antiunitary A that anticommutes with H. (c) `ΠS_jΠ = −S_j`, `ΠP_jΠ = −P_j`, `ΠC_a[v]Π = C_a[v∘Π]`, and the difference of `ϑ_a∘Π` along the inverted bond is minus the image of `d_aϑ_a`. `Π` keeps the species and reverses the energy. (d) T2 with `ρ = 1`, `D = −1`. The rate, frame, twist-hop and reach-three terms move an odd number of steps; the reach-two term moves none or two. A spectrum symmetric about zero has vanishing cubic trace. ∎

The Lattice axiom names the proper rotations only; the mirror image of (c) is not among the symmetries the axioms supply (block 54 T1(c) added an antilinear inversion as a supplied symmetry).


The equality of site probabilities does not make all local observables equal: coin densities rotate as T1(d) and energy density can change sign. The uniform reach-two symbol has a symmetric pair of coin eigenvalues; the nonzero cubic trace is a specific varying-field counterexample, not a claim that every varying strain has asymmetry.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Static finite-level doubling is distinct from uniform momentum labels and from an infinite continuous-spectrum claim. The twist table concerns the displayed linearized operator. Equal position densities do not equate coin or energy observables.

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
Static finite-level doubling is distinct from uniform momentum labels and from an infinite continuous-spectrum claim. The twist table concerns the displayed linearized operator. Equal position densities do not equate coin or energy observables.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8592; no premise adoption or retained grade is inferred.
- [admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8593; no premise adoption or retained grade is inferred.
- [admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8595; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_makes_a_varying_rotation_of_the_coin_axes_a_symmetry_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_THE_BLIND_WALK_A_SCALAR_HOP_WEIGHTED_BY_THE_TWIST_OF_THE_COIN_ALONG_THE_BOND_MAKES_A_VARYING_ROTATION_OF_THE_COIN_AXES_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8596; no premise adoption or retained grade is inferred.
- [admissibility_rule_eight_species_of_the_walk_the_nearest_neighbour_frame_shows_them_the_same_lengths_the_relabellings_coupling_shows_them_different_lengths_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_EIGHT_SPECIES_OF_THE_WALK_THE_NEAREST_NEIGHBOUR_FRAME_SHOWS_THEM_THE_SAME_LENGTHS_THE_RELABELLINGS_COUPLING_SHOWS_THEM_DIFFERENT_LENGTHS_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8599; no premise adoption or retained grade is inferred.
- [admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8601; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8602 head `8b4eccab5cb0cda8a42b254cd9af8261e2cde203`, branch `physics-loop/admissibility-induced-law-block70-species-exchange-maps-what-each-varying-field-becomes-20260921`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_2026_09_21.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
