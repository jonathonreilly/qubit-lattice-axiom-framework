---
claim_id: admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "A one-dimensional scalar reach-one symbol cannot vanish at both corners with unit slope at both. The two-step momentum commutes with the supplied free walk and has unit corner slopes. Its Hermitian site-dependent generator produces a coupling of reach at most three with a local current identity and common leading quadratic dispersion. Divergence compatibility does not imply static field existence."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
  - admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21
  - admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21
  - admissibility_rule_eight_species_of_the_walk_the_nearest_neighbour_frame_shows_them_the_same_lengths_the_relabellings_coupling_shows_them_different_lengths_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_2026_09_21.py
---

# Two-step momentum: exact current and a common leading corner geometry

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

Use finite periodic cubic lattices with the usual Hermitian free walk H=sum_a sigma_a S_a, S_a=(T_a-T_a^-1)/(2i), C_a=(T_a+T_a^-1)/2. Set P_j=S_j C_j=(T_j^2-T_j^-2)/(4i). A real site field xi defines G=sum_j{xi_j,P_j}/2, a supplied Hermitian generator of unitary changes of amplitude; it is not a literal permutation of sites. On the infinite lattice require bounded fields or a specified common operator domain.

For a bond x to y=x+e_a define d_a xi_j=xi_j(y)-xi_j(x), the Hermitian weighted hop C_a[d xi], and
`K_a^j(x,y)=Re[psi_y^dagger sigma_a(P_j psi)_x+(P_j psi)_y^dagger sigma_a psi_x]/2`.
The bound on reach uses displacement distance on a nonaliasing lattice. It classifies neither all possible couplings nor all matrix-valued momentum choices.

## Theorem T1 — not with reach one

*Statement.* There are no real `a, b, c` with `f(k) = a sin k + b cos k + c` satisfying `f(0) = f(π) = 0` and `f'(0) = f'(π) = 1`.

*Proof.* `f(0) = b + c`, `f(π) = −b + c`, so `b = c = 0`; then `f'(0) = a` and `f'(π) = −a`. ∎

## Theorem T2 — a momentum that is the same for all species

*Statement.* `P_j = S_jC_j` has the symbol `½ sin 2k_j`, which vanishes at `k_j = 0, π` with slope `+1` at both; `[H, P_j] = 0`; `d⟨P_j⟩/dt = 0` for every state.

*Proof.* `S_j` and `C_j` are functions of the shifts, which commute with `H`. ∎

Near species `n`, `½ sin 2(πn_j + q_j) = q_j + …`: the species' own wave number, with no sign.

## Theorem T3 — the relabelling it generates

*Statement.* (a) `i[H, G] = Σ_a Σ_j σ_a ½{C_a[d_aξ_j], P_j}`. (b) Its displacement reach is at most three. Generic nonconstant xi on a nonaliasing lattice realizes that reach; constant xi makes the commutator zero, and small periodic lattices can identify endpoints. (c) `⟨ψ|i[H, G]|ψ⟩ = Σ_{a,j,x}(d_aξ_j)(x) K_a^j(x → x + e_a)` for every state; on stationary states the left side vanishes, so `K` is divergence-free there.

*Proof.* As block 63 T2: `[S_a, P_j] = 0` and `i[S_a, ξ_j] = C_a[d_aξ_j]`. `C_a` moves one step along `a`, `P_j` two along `j`. For (c), `⟨G⟩ = Σ_{j,x} ξ_j(x) Re ψ†(P_jψ)(x)` since `P_j` is Hermitian, and `d⟨G⟩/dt = ⟨i[H, G]⟩`: for a state in motion the statement is the local conservation law of the two-step momentum density `Re ψ†(P_jψ)` with `K` as its current. ∎

For a field functional depending on the stated discrete curls, divergence freedom of its field derivative gives a necessary source compatibility condition. The stationary current meets that condition, but this does not prove a solution exists. A constant field functional has zero derivative and cannot match a nonzero divergence-free current.

## Theorem T4 — one geometry for all eight

*Statement.* For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]` and `H² = Σ_a[s_a + c_a Σ_j B_a^j s_jc_j]²`. Near `k = πn + q`: `H² = qᵀ(1 + B)ᵀ(1 + B)q + O(q⁴)` for every `n`. When I+B is invertible, this is a common positive leading inverse metric; otherwise it is semidefinite. With an isotropic B, the separately supplied local axial ray comparison of PR #8599 gives 1+beta at the reference rate, under all of that comparison's smoothness, small-momentum and nonzero-component hypotheses. No integrated deflection is claimed.

*Proof.* `s = Dq`, `c = D`, `s_jc_j = D_j²q_j = q_j`: `s_a + c_a(Bq)_a = D_a[q + Bq]_a`, and `D² = 1`. ∎

Compare block 68: the frame gives `DgD` (angles mirrored), reach two gives `(1 + BD)ᵀ(1 + BD)` (lengths species-dependent).

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
The reach-one obstruction concerns the stated scalar symbol only. A vanishing divergence is necessary, not sufficient, for field equations. Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion.

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
The reach-one obstruction concerns the stated scalar symbol only. A vanishing divergence is necessary, not sufficient, for field equations. Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion.

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
- [admissibility_rule_eight_species_of_the_walk_the_nearest_neighbour_frame_shows_them_the_same_lengths_the_relabellings_coupling_shows_them_different_lengths_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_EIGHT_SPECIES_OF_THE_WALK_THE_NEAREST_NEIGHBOUR_FRAME_SHOWS_THEM_THE_SAME_LENGTHS_THE_RELABELLINGS_COUPLING_SHOWS_THEM_DIFFERENT_LENGTHS_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8599; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8601 head `40fa4423f2a36eb874c895e430da7139a95ca484`, branch `physics-loop/admissibility-induced-law-block69-reach-three-exact-books-and-one-geometry-for-all-eight-species-20260921`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_2026_09_21.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
