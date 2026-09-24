---
claim_id: admissibility_rule_the_two_step_momentum_is_the_only_one_among_conserved_covariant_momenta_of_reach_two_that_is_every_species_own_wave_number_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "In the infinite-lattice polynomial commutant of the supplied free walk, vector coefficients are a scalar polynomial times sin k. Reach-one scalar symbols cannot have unit own-coordinate slopes at every corner. At reach two the normalized scalar solutions have six quadratic freedoms removed by cubic covariance; a permitted term along the walk changes only higher-order dispersion. This classifies the stated normalized momenta, not all field couplings."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_the_two_step_momentum_is_the_only_one_2026_09_21.py
---

# Finite-range conserved momenta with normalized corner slopes

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

Work on the infinite cubic lattice with translation-invariant finite-range symbols over the complex Laurent-polynomial ring in z_j=exp(i k_j). H=sigma dot s, s_j=sin k_j. Any two-by-two symbol is a I+b dot sigma; Hermitian generators have symbols real in these coefficients on real k. Displacement reach is max |m|_1 of exponents with nonzero coefficients; zero symbols have no positive reach.

A normalized own-coordinate scalar momentum a_j vanishes at every corner pi n and has gradient e_j there. The 25 real scalar basis functions of reach at most two are 1; sin k_j,cos k_j,sin 2k_j,cos 2k_j for each j; and sin(k_i+k_j),cos(k_i+k_j),sin(k_i-k_j),cos(k_i-k_j) for each i<j. The evaluation and derivative constraints in T3 have rank 19, leaving six homogeneous directions. Proper cubic covariance rotates spatial and coin indices together and leaves H invariant.

Supply G=sum_j{xi_j,M_j}/2 for Hermitian conserved M_j. Since [H,M_j]=0 its commutator is the sum of {sigma_a C_a[d_a xi_j],M_j}/2. This is a chosen class of generators; finite tori with aliasing are not the Laurent-polynomial classification domain.

## Theorem T1 — what can be conserved

*Statement.* For `M(k) = a(k) + b(k)·σ`: `[M, H] = 2i(b × s)·σ`, `s_a = sin k_a`. `M` commutes with the walk iff `b = c s` with `c` a trigonometric polynomial, and, for nonzero c, the maximal displacement reach of the vector b=c s is reach(c)+1.

*Proof.* `[σ_a, σ_b] = 2iε_{abc}σ_c`. If `b × s = 0` then `b_1 sin k_2 = b_2 sin k_1`; `sin k_1` and `sin k_2` are polynomials in different variables `e^{±ik_1}`, `e^{±ik_2}` with no common factor, so `sin k_1` divides `b_1`, and `c = b_1/sin k_1 = b_2/sin k_2 = b_3/sin k_3`. For the needed special product c sin k_j, choose a nonzero coefficient at an exponent m of maximal L1 norm R and choose j and a sign pointing outward (any j if R=0). The coefficient at m plus that signed unit vector cannot cancel: its only alternative contribution would be at m plus twice that vector, whose norm exceeds R. The upper bound is R+1. This proves the vector reach assertion. No general product-reach rule is used; arbitrary polynomial factors can cancel their outer terms. ∎

## Theorem T2 — reach one

*Statement.* (a) No real combination of `1, cos k_b, sin k_b` (`b = 1, 2, 3`) vanishes at all eight zeros with gradient `e_j`. (b) A relabelling generated with `M_j = Σ_bα_{jb} sin k_b` and a uniform strain give `H(k) = Σ_aσ_a[s_a + c_aΣ_jB_a^jM_j]`, and species `n` sees the inverse metric `(1 + BαD)ᵀ(1 + BαD)`. It is the same for every species and every strain only if `α = 0`. (c) A constant `c_j` is unchanged by every rotation and is a vector only if it vanishes.

*Proof.* (a) The gradient of `Σ_bα_b sin k_b` at `πn` is `(α_b(−1)^{n_b})_b`; for `b = j` it would have to equal 1 at `n_j = 0` and at `n_j = 1`. The cosines and the constant must vanish with the value. (b) Near `πn + q`: `s_a = D_aq_a`, `c_a = D_a`, `M_j = (αDq)_j`: the vector is `D(1 + BαD)q`. For `B = ε` times a matrix unit the first order in `ε` is linear in `αD`, which depends on `n` unless `α = 0`. (c) Immediate. ∎

## Theorem T3 — reach two

*Statement.* (a) Among real combinations of the 25 monomials of reach `≤ 2`, those vanishing at all eight zeros with gradient `e_1` are `½ sin 2k_1 + Σ_{b≤c}e_{bc} sin k_b sin k_c`, the `e_{bc}` arbitrary. (b) If `M_1` is unchanged by the quarter turn about axis 1 and changes sign under the half turn about axis 2, all six `e_{bc}` vanish. (c) The part along the walk with `c_j` of reach `≤ 1` and `M_j` a vector is `γ sin k_j H`.

*Proof.* (a) Thirty-two linear conditions on 25 coefficients; the runner solves them: one particular solution and six free directions, whose overlap matrix with the six functions `sin k_b sin k_c` has rank six. Each of these has a zero of second order at every `πn`. (b) The quarter turn sends `(k_2, k_3)` to `(k_3, −k_2)`: it turns `sin k_2 sin k_3` into its negative, so `e_{23} = 0`; it turns `sin k_1 sin k_2` into `sin k_1 sin k_3` and `sin k_1 sin k_3` into `−sin k_1 sin k_2`, so `e_{13} = e_{12}` and `e_{12} = −e_{13}`, and both vanish. The half turn sends `(k_1, k_3)` to `(−k_1, −k_3)` and leaves the three squares unchanged, where `M_1` must change sign: `e_{11} = e_{22} = e_{33} = 0`. (c) The half turn about axis 2 must reverse `c_1`: constants and cosines are excluded, and `sin k_2` is; the quarter turn about axis 1 then excludes `sin k_3`. ∎

## Theorem T4 — the part along the walk leaves the leading cone unchanged

*Statement.* For a uniform strain, `Σ_{a,j}B_a^j½{σ_aC_a, γ S_jH}` has the symbol `γΣ_{a,j}B_a^j s_a s_j c_a` times the identity; at `k = πn + q` it is `γΣB_a^jD_jq_aq_j + O(q⁴)`.

*Proof.* `½{σ_a, σ·s} = s_a`. `s_ac_a = q_a + O(q³)` and `s_j = D_jq_j + O(q³)`. ∎

The walk's energies near a zero are `± |(1 + B)q| + O(q²)`: this second-order scalar term leaves the leading linear cone and its quadratic inverse metric unchanged, but changes finite-wavevector dispersion. It depends on the species through `D_j`; whether `γ` is present is one more number of the supplied coupling, not examined further.


The scalar unit-gradient condition fixes normalization. Requiring only that all species share a geometry admits the zero scalar momentum or a common rescaling lambda P, with a corresponding rescaling of the strain. Thus the least-reach statement concerns normalized momentum choices in this polynomial commutant class; the resulting deformation has reach at most three and generically three. It is not a classification of every possible coupling. Hermiticity of each M_j is required for G to generate unitary transformations.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Unit corner slopes are an essential normalization. Only the stated polynomial commutant and cubic vector transformation law are classified. A common metric alone allows rescalings or zero deformation, and higher-order scalar terms still alter dispersion.

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
Unit corner slopes are an essential normalization. Only the stated polynomial commutant and cubic vector transformation law are classified. A common metric alone allows rescalings or zero deformation, and higher-order scalar terms still alter dispersion.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8593; no premise adoption or retained grade is inferred.
- [admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8601; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8606 head `69f3c13dd5891a18016bb99941fe0eaeadcb2b9f`, branch `physics-loop/admissibility-induced-law-block73-the-two-step-momentum-is-the-only-one-20260921`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_two_step_momentum_is_the_only_one_2026_09_21.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
