---
claim_id: admissibility_rule_eight_species_of_the_walk_the_nearest_neighbour_frame_shows_them_the_same_lengths_the_relabellings_coupling_shows_them_different_lengths_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "Supplied uniform lattice symbols have eight corner zeros. A uniform invertible frame gives conjugate principal quadratic forms DgD; a uniform strain gives leading forms (I+BD)^T(I+BD). A separately supplied axial smooth-ray comparison has local factors 1+beta or 1-beta at the reference rate. No universal packet fall or integrated bending law is established."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21
  - admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
  - admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21
  - admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_eight_species_of_the_walk_the_nearest_neighbour_frame_shows_them_the_same_lengths_2026_09_21.py
---

# Corner expansions under frame and strain couplings

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

H(k)=sum_a sigma_a sin k_a is the supplied free walk, with the usual anticommuting two-by-two coin matrices. Near k=pi n+q let D=diag((-1)^n_a). A real uniform frame E gives H_E=sum_j(E^j dot sigma)sin k_j and g=E^T E. Require E invertible when g is called an inverse metric; otherwise it is only positive semidefinite. A real uniform strain B gives H_B=sum_a sigma_a[sin k_a+cos k_a sum_j B_a^j sin k_j]. These are alternative supplied families, not dynamics derived from the axioms. The local metric terminology concerns the leading quadratic dispersion, not exact finite-wavelength trajectories. Equal principal eigenvalues or diagonal entries do not make shear trajectories identical in common coordinates.

## Theorem T1 — corner zeros and uniform rate scaling

*Statement.* (a) `H(k)² = Σ_a sin² k_a`; it vanishes iff every `k_a ∈ {0, π}`: eight wave vectors modulo 2pi in the continuous reciprocal cell; a finite torus contains all eight when every side is even. (b) Near `k = πn + q`, `H = Σ_a D_a σ_a q_a + O(q³)`. (c) For a uniform rate `H → wH`: the energy of every species is `w` times a function of the sines that does not depend on the species.

*Proof.* The three coin matrices anticommute; `sin(πn_a + q_a) = (−1)^{n_a} sin q_a`. ∎

Uniform scaling does not imply a universal force identity for arbitrary finite packets. The corrected clocked-walk note explicitly separates these claims.

## Theorem T2 — the frame: the same lengths, mirrored angles

*Statement.* For a uniform frame and every `k`, `H(k)² = Σ_ij g^{ij} s_i s_j`. In the species' own wave vector, `H² = Σ_ij (DgD)^{ij} sin q_i sin q_j`: the diagonal of `DgD` is that of `g` for every species, and `(DgD)^{ij}=D_i D_j g^{ij}`. Nonzero off-diagonal entries reverse sign exactly when n_i differs from n_j; a zero entry remains zero.

*Proof.* Block 62 T1 and `s = D sin q`. ∎

## Theorem T3 — the strain: different lengths for different species

*Statement.* For a uniform strain and every `k`, `H(k)² = Σ_a [s_a + c_a(Bs)_a]²`. Near `k = πn + q`, `H² = qᵀ(1 + BD)ᵀ(1 + BD)q + O(q⁴)`. For `B = diag(b, 0, 0)` the entry along axis 1 is `(1 + b)²` if `n_1 = 0` and `(1 − b)²` if `n_1 = 1`.

*Proof.* Anticommutation gives the sum of squares. With `s = Dq`, `c = D` at leading order, `s_a + c_a(Bs)_a = D_a[q + BDq]_a`. ∎

The reason is visible in block 63 T2: a relabelling is generated with the lattice's own momentum `S_j`, whose symbol `sin k_j` has the sign `D_j` on species `n`; what it generates carries the hop `C_a`, whose symbol `cos k_a` has the sign `D_a`. The exactly conserved momentum of block 63 is, species by species, `D` times the species' own.

## Theorem T4 — a local axial ray comparison

Supply a positive-energy smooth ray approximation near a corner and the relation ell=(wbar/w)^beta. Put u=log(w/wbar). For the isotropic frame E=ell^-1 I, the leading massless axial speed factor is v=w/ell, giving d log v/du=1+beta. For the strain family with 1+b=ell^-1=exp(beta u), an axis reflected at that corner has speed factor v=w(1-b) near u=0, where 1-b>0. Its derivative d log v/du at u=0 is 1-beta.

To interpret these derivatives as an acceleration ratio, use a massless ray initially along that coordinate axis, a log-rate gradient transverse to it, and a supplied massive comparator released from rest at the same reference wbar. For the local symbol E=v|p|, the supplied canonical ray equations give transverse acceleration -v grad_perp v. For the comparator E=w sqrt(m^2+|p|^2), m>0, at p=0 they give -w grad w. At the reference v=w, their nonzero corresponding components have ratio d log v/du. This is a local leading-order comparison only; no integrated deflection, arbitrary packet law, finite-wavevector isotropy or finite-velocity massive law follows. A zero denominator has no ratio; beta=1 cancels only this leading reflected-axis component.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
The ray comparison has small-momentum, smooth-field, reference-rate, axial and nonzero-component hypotheses. The exact symbol identities do not establish universal packet forces or species-independent arbitrary trajectories.

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
The ray comparison has small-momentum, smooth-field, reference-rate, axial and nonzero-component hypotheses. The exact symbol identities do not establish universal packet forces or species-independent arbitrary trajectories.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8581; no premise adoption or retained grade is inferred.
- [admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8592; no premise adoption or retained grade is inferred.
- [admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8593; no premise adoption or retained grade is inferred.
- [admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8595; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8599 head `d297893d4a6d492761723181f00117eb7530eb8d`, branch `physics-loop/admissibility-induced-law-block68-eight-species-of-the-walk-one-set-of-lengths-or-eight-20260921`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_eight_species_of_the_walk_the_nearest_neighbour_frame_shows_them_the_same_lengths_2026_09_21.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
