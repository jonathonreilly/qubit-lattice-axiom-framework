---
claim_id: admissibility_rule_each_species_needs_the_inversion_odd_curl_split_by_derivative_direction_only_per_axis_hops_carrying_each_axis_part_serve_all_eight_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "WITHIN block 62's framed walk H[E] = (1/2) sum_j {E^j.sigma, S_j} and block 70's species maps as landed, with block 158's inversion-odd curl eps.C = eps_abc E^i_b E^j_c (d_i e^a_j - d_j e^a_i) and block 161's links as placed (pushed), at long wavelength (smooth envelopes, smooth real weights), for coin-scalar placements (a site term plus real symmetric hops): (T1) eps.C = X_1 + X_2 + X_3 with X_d = 2 eps_abc E^d_b E^j_c d_d e^a_j its part with derivative along axis d, and species A (D = diag cos A, s = det D, rho = sD) sees s eps.C[rho E rho] = sum_d D_d X_d, so its comparator completion (the definition of 'needs' here) is the coin scalar N_A = (1/8) sum_d cos(A_d) X_d; (T2) a symmetric hop by m reaches species A with the sign prod_d D_d^(m_d mod 2) and a site term is unchanged; the eight sign patterns are orthogonal characters, so a placement serves all eight species iff its long-wave weight per displacement-parity class is X_d/8 on the class odd along axis d alone and zero on the others (unique per class; within Euclidean or l1 range 2 that class holds only the nearest-neighbour hops along d); (T3) with weight (1/8) eps.C a site term or face-diagonal hops serve k = 0 only and the body diagonal serves k = 0 and (pi,pi,pi); with free weights, any placement on even-degree classes gives a corner and its antipode the same scalar while N_A changes sign, so it serves both only where N_A = 0; (T4) on the lengths' frame e = 1 + eta every X_d vanishes at first order, while block 161's per-axis link scalars L_j = (1/4) eps_jab omega_jab, omega_jab = d_b eta_aj - d_a eta_jb, are nonzero (they sum to zero), giving the six mixed species a spurious first-order coin scalar (-1 at (pi,0,0) for the jet d_3 eta_12 = 1). Exact (sympy, integers). A harvest of probe HIT #9367 (a Claude Opus 5.5 worker), refereed by Claude Sonnet 5 (same vendor family; the owner ruled on 2026-09-28 that a Sonnet referee counts). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_each_species_needs_the_inversion_odd_curl_split_by_derivative_direction_2026_09_28.py
---

# Each species needs the inversion-odd curl split by derivative direction; only per-axis hops carrying each axis's part serve all eight

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 62 and 70 as landed and blocks 158 and 161 as placed; a harvest of probe HIT #9367, refereed by Claude Sonnet 5; nothing adopted or registered; unaudited)

This note works within block 62's framed walk and block 70's species maps as landed, and places block 158's curl term and block 161's links; it reports where on the lattice the curl term must sit to serve all eight species of the walk; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 158 (pushed) found that the walker which sees only the member's lengths needs one extra coin-scalar term, `(1/8)ε·C`, to keep the member's relabellings at second order. Here `ε·C` is the frame's inversion-odd curl. Block 158 derived it for the species at `k = 0`. Block 161 (pushed) supplied it from links on the bonds. Neither said where on the lattice the term must sit so that all eight species of the walk get what they need. Probe HIT #9367 answered that; this note harvests it with the referee's scope.

- **T1: what each species needs.**
  - The curl splits by the direction of its derivative: `ε·C = X₁ + X₂ + X₃`, where `X_d = 2ε_abc E^d_b E^j_c ∂_d e^a_j`.
  - Species `A` sees the frame as `ρEρ` (block 70, landed), and `s ε·C[ρEρ] = Σ_d cos(A_d) X_d`.
  - So its own comparator completion is the coin scalar `N_A = (1/8)Σ_d cos(A_d) X_d`. Each species weights each axis's part of the curl by the sign of its own momentum along that axis.
- **T2: the only placement that serves all eight.**
  - A hop by displacement `m` reaches species `A` with the sign `Π_d cos(A_d)^{m_d mod 2}`, and a site term reaches every species unchanged.
  - The eight sign patterns are the characters of `{±1}³`, so a coin-scalar placement serves all eight species exactly when its long-wave weight is `X_d/8` on the hops odd along axis `d` alone, and zero on the site, the face diagonals and the body diagonal.
  - The shortest such hops are the nearest-neighbour hops along each axis: axis `d` carries its own derivative's part, as block 65's twist hop does.
- **T3: the alternatives fail.** With weight `(1/8)ε·C`:
  - a site term or face-diagonal hops serve `k = 0` only;
  - the body diagonal serves `k = 0` and `(π, π, π)`.

  More generally, a placement on the site or the face diagonals gives a corner and its antipode the same scalar while their need changes sign. So it can serve both only where their need is zero.
- **T4: block 161's links spoil the six mixed species at first order.** On the lengths' own frame every `X_d` vanishes at first order, so every species needs zero. But the links carry per-axis scalars that are nonzero at first order, though they sum to zero. So the six species of mixed sign receive a spurious first-order coin scalar: `−1` at `(π, 0, 0)` for the jet `∂₃η₁₂ = 1`.

In plain terms: the correction block 158 found is not one number per site. It has a piece for each direction, and each kind of wave in the walker needs those pieces with its own signs. Only a correction carried by the bonds along each axis, each bond carrying its own direction's piece, serves every kind of wave at once. Putting the whole correction on the sites serves only one kind. Block 161's bond links split the correction in a different way, and at first order they hand six of the eight kinds a spurious extra term.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-28.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The walk, its frame, the curl term and the links are supplied clauses. Nothing is adopted.
- **The framed walk** (block 62, landed): `H[E] = ½Σ_j{E^j·σ, S_j}`, with co-frame `e` and frame `E = e⁻¹`.
- **The species maps** (block 70, landed), quoted: "`U_nT_aU_n = D_aT_a`" and "| frame `E` | `s_n H[ρ_nEρ_n]` |". The species at `A = πn` has `D = diag cos A`, `s = det D` and `ρ = sD`.
- **The curl term** (block 158, pushed, placed). `ε·C = ε^{abc} E^i_b E^j_c (∂_i e^a_j − ∂_j e^a_i)`. The walker that sees only the lengths needs `(1/8)ε·C` to become the comparator's operator.
- **The links** (block 161, pushed, placed). The lengths' connection is `ω_jab = e^a_k(∂_j E^k_b + Γ^k_jl E^l_b)`, and the link along `j` has `a_{j,c} = ½ε_cab ω_jab`. Its coin-scalar part is `½E^j·a_j`, and these sum to `(1/8)ε·C`.
- **"Needs"** is a definition. It means the comparator completion of each species' own effective frame (block 158 T1 through block 70's map). It is not a claim that relabellings are kept for the six mixed species: for those, block 62's frame coupling already differs from the relabellings' coupling at first order (block 68, landed).
- **Placements.** Coin-scalar only: a site term plus real symmetric hops, with smooth weights. Coin-valued placements and staggered weights, which mix species, are not covered.
- **Imports, named at definition level.**
  - The characters of `{±1}³`.
  - Long-wavelength reduction on smooth envelopes.
  - Exact symbolic arithmetic.
  - The comparator is Weyl's and Fock and Ivanenko's two-component operator, as in block 158.

## Prior art and what is new

- **Block 70** (landed): the exchange table. Its twist row is why block 65's per-axis twist hop serves every species. This note extends that to `ε·C` and to every displacement.
- **Blocks 158 and 161** (the supervisor's, pushed): the curl term and the links.
- **Probe HIT #9367** (a Claude Opus 5.5 worker, `w-jonathonsmac4f50-jd018`): the answer harvested here.
- **The referee** (Claude Sonnet 5, 2026-09-28).
  - Verified the sign rule with random real and complex weights, 17 displacements and all 8 maps; the character argument; the index computation for general, non-symmetric frames; and block 161's links.
  - Found that the link scalars sum to `(1/8)ε·C` exactly at a point to all orders, for generic symmetric frames. The worker checked through second order. That stronger statement is the referee's, and is not re-derived here.
- **New here.** The harvest, with the referee's scope: the weight qualifier on the alternatives, the even-degree obstruction, and "needs" as a definition.

## Theorem T1 — what each species needs

*Statement.*
- (a) `ε·C = X₁ + X₂ + X₃`, with `X_d = 2ε_abc E^d_b E^j_c ∂_d e^a_j`.
- (b) For every species, `s ε·C[ρEρ] = Σ_d D_d X_d`, where `ρEρ` is taken with the co-frame `ρeρ`. So species `A`'s comparator completion is the coin scalar `N_A = (1/8)Σ_d cos(A_d) X_d`.

*Proof.*
- (a) In the second term of `ε·C`, exchange `i ↔ j` and `b ↔ c`. The antisymmetry of `ε` makes it equal to the first, so `ε·C = 2ε_abc E^i_b E^j_c ∂_i e^a_j`. Group by `i`.
- (b) Each index of `X_d` picks up a factor of `ρ`; with `ρ_aρ_bρ_c = det ρ = 1` and `ρ_j² = 1`, only `ρ_d` on the derivative index survives, and `sρ_d = D_d`.
- Runner B1 and B2: three rational frames, 27 generic derivatives, all eight species. ∎

## Theorem T2 — the only placement that serves all eight

*Statement.*
- (a) Under species `A`'s site-sign map, a symmetric hop by displacement `m` is multiplied by `Π_d D_d^{m_d mod 2}`, and a site term is unchanged.
- (b) At long wavelength, species `A` receives from a placement the scalar `p_A = Σ_c w_c Π_d D_d^{c_d}`, where `w_c` is the total weight on the displacements of parity class `c ∈ {0,1}³`.
- (c) `p_A = N_A` for all eight `A` if and only if `w_{e_d} = X_d/8` for `d = 1, 2, 3` and `w_c = 0` for every other class.

*Proof.*
- (a) The site sign `(−1)^{n·x}` multiplies the entry `(x, x + m)` by `(−1)^{n·(2x + m)} = Π_d D_d^{m_d}`. Runner C1 checks ten displacements, including two-step and three-axis ones, on a `(4, 6, 4)` torus with random integer weights.
- (b) On a smooth envelope a hop of weight `w` acts as `w` at leading order.
- (c) The eight sign patterns are the characters of `{±1}³`, orthogonal with `χχᵀ = 8·1`. `N_A` has components only on the three characters `D_d`. Runner D1 solves for the weights and finds the solution unique.
- Uniqueness is per parity class, not per hop. Within Euclidean or `ℓ¹` range 2, the class odd along `d` alone holds only the nearest-neighbour hops along `d`. In sup-norm range 2 it holds more, for example `(1, 2, 0)`. ∎

## Theorem T3 — the alternatives fail

*Statement.*
- (a) With total weight `(1/8)ε·C`, a site term serves `k = 0` only; face-diagonal hops spread over the three face classes serve `k = 0` only; and the body diagonal serves `k = 0` and `(π, π, π)`. This holds for independent `X₁, X₂, X₃`.
- (b) For any weights on the even-degree classes (the site and the face diagonals), `p_{A+(π,π,π)} = p_A` while `N_{A+(π,π,π)} = −N_A`. So such a placement serves a corner and its antipode together only where `N_A = 0`.

*Proof.*
- Runner E1: the table for symbolic `X`, and the even-degree obstruction for symbolic weights.
- With free weights, a site term can serve any one chosen corner, and site plus face-diagonal hops can serve four corners, one from each antipodal pair. The table is for the weight `(1/8)ε·C`.
- The `X_d` are independent on the lengths' frame at second order (the probe's check), so the alternatives fail there at second order. ∎

## Theorem T4 — block 161's links spoil the six mixed species at first order

*Statement.* On the lengths' frame `e = 1 + η`, with `η` symmetric:
- (a) every `X_d` vanishes at first order, so every species needs zero;
- (b) the lengths' connection is `ω_jab = ∂_b η_aj − ∂_a η_jb` at first order, and the link along `j` has the coin scalar `L_j = ¼ε_jab ω_jab`;
- (c) `L₁ + L₂ + L₃ = 0`, but for the jet `∂₃η₁₂ = 1` the scalars are `(½, −½, 0)`. So species `(π, 0, 0)` receives `Σ_d D_d L_d = −1` at first order, where it needs zero. Every one of the six mixed species receives a nonzero first-order scalar for some jet.

*Proof.*
- (a) At first order `E = 1`, and `X_d = 2ε_adj ∂_d η_aj = 0`, because `ε` is antisymmetric in `(a, j)` and `η` is symmetric.
- (b) `∂_jE^a_b = −∂_jη_ab` and `Γ^a_jb = ∂_jη_ab + ∂_bη_aj − ∂_aη_jb` for `g = 1 + 2η`.
- (c) Runner F1. ∎

## What this settles and what it does not

- **Settled** (within the premises, at long wavelength, for coin-scalar placements).
  - Each species needs block 158's curl term split by derivative direction, weighted by the signs of its own momentum.
  - Only per-axis hops carrying each axis's part serve all eight species.
  - The site term and the face-diagonal hops (with weight `(1/8)ε·C`) serve `k = 0` only.
  - Block 161's links serve `k = 0` and `(π, π, π)`, and give the six mixed species a spurious scalar at first order.
- **For block 161.** Its links realise `(1/8)ε·C` at `k = 0`, but split it by the connection rather than by derivative direction. A range-1 rule that builds the links from the lengths and splits by derivative direction would serve all eight. The probe found such a hop, `v_d = ¼ε_abc Ē^d_b Ē^j_c(e^a_j(x + e_d) − e^a_j(x))`, reproducing `X_d/8` with error of order `ℓ⁻²` in floating point.
- **Not settled.**
  - Coin-valued placements.
  - Staggered weights.
  - Relabelling consistency for the six mixed species, which is a separate question (block 68).
  - The range-1 realisation's error, exactly.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
- T1–T3 are exact algebra, at long wavelength, for coin-scalar placements with smooth weights.
- The alternatives fail at second order, since the `X_d` vanish at first order on the lengths' frame.
- T4 is a first-order failure on the lengths' frame.

### N2 — Wall independence
No repository no-go wall is used.

### N3 — Supplied structure
The walk, its frame, block 158's term and block 161's links are supplied, and "needs" is the comparator completion by definition.

### N4 — Dependencies
The axioms memo and landed block 70 (quoted). Block 62 is landed and used for the form of the walk. Blocks 158 and 161 are placed, and every fact used from them is re-derived.

### N5 — Resolution
- per_element: executed - the split of eps.C by derivative direction; the species map of eps.C for all eight species
- per_site: executed - the sign rule for ten displacements on a (4,6,4) torus
- per_mode: executed - the character argument and the unique serving placement
- per_block: executed - the alternatives with weight (1/8) eps.C; the even-degree obstruction; first order on the lengths' frame and block 161's links
- lattice_wide: checked and not executed - the range-1 realisation's error (floating point in the probe, about l^-2); coin-valued placements; placements with staggered weights; relabelling consistency for the six mixed species

### N6 — Primitive boundary
No new primitive, selection or physical interpretation is adopted.

### N7 — Strongest objection
"Needs" might be read as a consistency requirement. It is a definition here: the comparator completion of each species' own frame. The referee flagged this, and it is stated in the premises and the claim scope.

### N8 — Earlier claims
The probe's table said "serves `k = 0` only" without the weight `(1/8)ε·C`. With free weights that is false, and the note states the weight.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "blocks 158 and 161: the lattice placement of (1/8) eps.C and what it does for the other seven species"
source_of_blocker_text: probes task J:derive:the-lattice-placement-of-the-inversion-odd-curl (after blocks 158 and 161)
reachability_to_target: advances
next_trace_action: "a range-1 link rule split by derivative direction; relabelling consistency for the mixed species"
```

## Review record

- **Author checks (not a review PASS).** The supervisor's own runner, exact, `TOTAL: PASS=14 FAIL=0`. Mutation census 8/8, each failing in its own family only.
- **Provenance.**
  - Derived by probe worker `w-jonathonsmac4f50-jd018` (Claude Opus 5.5), HIT #9367, `check.py` 15/15.
  - Refereed by Claude Sonnet 5 on 2026-09-28: confirmed with scope corrections, all applied here. Same vendor family; the owner ruled on 2026-09-28 that a Sonnet referee counts for harvest.
  - Harvested by the supervisor (Claude Opus 5.5), with its own runner.
