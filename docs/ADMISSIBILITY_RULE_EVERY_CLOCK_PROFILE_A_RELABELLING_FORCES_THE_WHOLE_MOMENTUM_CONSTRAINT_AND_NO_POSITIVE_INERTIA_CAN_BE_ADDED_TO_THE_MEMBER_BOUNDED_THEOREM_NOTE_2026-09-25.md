---
claim_id: admissibility_rule_every_clock_profile_a_relabelling_forces_the_whole_momentum_constraint_and_no_positive_inertia_can_be_added_to_the_member_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: Supplied flat-strain constraint stencil at the term linear in canonical momentum, with nonzero K, nonzero
  alpha and nonsingular kinetic blocks. Delta lapses span all bonds on lattices of side at least three; a uniform
  lapse spans gradients. A coefficient-independent quotient rank certificate on the 3^3 torus forces gamma=0 and
  beta=-alpha for prescriptions required to close there, within the specified timing. That line contains no nonzero
  positive semidefinite quadratic form. The displayed free filled-band formal adiabatic inertia is positive semidefinite
  and nonzero; adding it leaves the line, conditional on using it in the same supplied action. Its physical adiabatic
  interpretation requires state preparation and a gap, and is not established at zero mass. For the stipulated one-walker
  energy and momentum placements, uniform lapses suffice for exact bracket matching, arbitrary pairs fail, and the
  defect starts at cubic wave-number order. The extreme-hop proof excludes exact matching for finite-support energy
  placements with cube rotations and time reversal against nearest-neighbour relabellings. It does not rule out
  the full coupled algebra, whose cross terms remain open, singular kinetic theories, other timings or nonlocal
  placements.
upstream_dependencies:
- admissibility_rule_the_curvature_members_constraint_algebra_closes_on_the_lattice_only_at_beta_equals_minus_alpha_and_there_the_walkers_own_states_cannot_be_its_content_bounded_theorem_note_2026-09-24
- admissibility_rule_blindness_to_coin_rotations_that_vary_in_time_leaves_exactly_block_62s_two_kinetic_numbers_and_no_ratio_makes_a_transverse_relabelling_in_time_a_symmetry_bounded_theorem_note_2026-09-24
- admissibility_rule_the_members_pull_carries_the_velocity_terms_that_give_pull_bound_pairs_weight_one_along_every_axis_at_first_order_bounded_theorem_note_2026-09-25
- admissibility_rule_one_light_cone_exactly_on_the_lattice_the_two_step_content_meets_the_members_identity_for_every_state_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
- admissibility_rule_two_step_content_keeps_symmetric_books_where_the_member_keeps_its_fields_and_a_bond_shift_keeps_every_constraint_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
- admissibility_rule_the_books_admit_one_rest_energy_the_staggered_mass_keeps_them_exactly_so_massive_content_meets_the_member_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
- admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
- admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_bounded_theorem_note_2026-09-25
- minimal_axioms
runner: scripts/admissibility_rule_every_clock_profile_a_relabelling_forces_the_whole_momentum_constraint_and_no_positive_inertia_can_be_added_to_the_member_2026_09_25.py
---

# Every clock profile a relabelling forces the whole momentum constraint, and no positive inertia can be added to the member

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 112's bracket and the landed kinetic family, walk, staggered mass and walker placements; a consolidating note of lemmas; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within blocks 54, 112, 124, 135, 136, 139 and 144 as landed on main (the walk and its staggered mass, the member's lattice bracket of lapse constraints, its kinetic family and its drifting relabellings, and the walker's placements of energy and momentum); it reports what the member's clock algebra implies for two reading questions; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 112 (landed; a harvest refereed by another model family) found the member's clock algebra on the lattice: the bracket of two lapse constraints is a relabelling of the strains, exactly, for every pair of lapses, if and only if `β = −α` and each face term is timed symmetrically. Two of the owner's reading questions (decision-record addenda 39 and 40) turn on that algebra. This note is a consolidating note of lemmas, not a new programme.

- **T1: which clock profiles may drive the evolution decides the shift.** Block 112's relabelling fields `ξ(M, N)` span every bond field. Lapses concentrated at the two ends of one bond give that bond alone, and the bracket is then exactly that bond's relabelling. A uniform lapse gives only gradients.
  - So if every clock profile may drive the evolution, keeping the clock constraints forces the whole momentum constraint at this order. Block 144's drifting relabellings violate it.
  - If only a uniform clock profile may, only the lattice divergence of the constraint is forced.
- **T2: a cubic-only kinetic term breaks the closure.** With a term `γΣḣ_ii²`, the bracket leaves the span of the relabellings for every kinetic ratio. Closure needs `γ = 0` and `β = −α`.
- **T3: the closing line admits no positive addition.** On uniform strains the closing line takes the values `(−6, 2, 2)α` on the dilation, E and T strains. It is indefinite, so no nonzero positive semidefinite kinetic term lies on it.
- **T4: the sea's inertia is such an addition.** The walker sea's adiabatic inertia on uniform strains is positive semidefinite, and nonzero on the T strain, for every staggered mass `μ ≥ 0`. So the member at its landed numbers plus the sea's inertia is off the closing line.
  - At `μ = 0` the inertia has no dilation part, and its own ratio `β/α = −μ_E/(3μ_T)` lies strictly between −1 and 0.
- **T5: the walker's clocks close for a uniform lapse, but not for all pairs.** Couple the lapse to block 135's energy `e′ = C₁C₂C₃e`, and take block 136's momentum `P^B`.
  - When one lapse is uniform, the walker's bracket is block 112's `G[ξ]` exactly, with `K/(4α) = 1`. That is block 136's books; the curl part of `P^B` drops out against gradients.
  - For general lapse pairs no `c` closes it. Lapses at two sites two steps apart along an axis give `ξ = 0` on every bond, yet their bracket is not zero.
  - The defect vanishes through second order in the lapses' wave numbers, for every walker momentum. At third order it is the walker's momentum density against a third-order bilinear in the two lapses.
  - So with walker content in the landed placements, T1's first reading holds only through second order.
  - No local placement of the walker's energy fixes this. For any finite-range placement with the cube's rotations and time reversal, two sites that share no bond have energies that fail to commute.

In plain terms: the member's clock rules fit together only for one kind of kinetic term, and that kind has a negative part. First, if the clocks may be reset differently at different sites, the rules force the full shift constraint, so the drifting twists cannot occur; if only a uniform reset is allowed, only a weaker part of the constraint is forced. Second, the walker sea resists stretching with a positive inertia. Adding it to the member's landed kinetic term gives a kind of term the clock rules do not accept. This is conditional on treating the displayed adiabatic coefficient as an additive term in the same supplied action; it does not exhaust possible dynamics, states or couplings. Third, the walkers' own clock rules agree with the member's when one of the two clock changes is uniform: that is the books. For general profiles the walker-only brackets disagree by cubic wave-number terms, which can be small at long wavelength but do not vanish exactly there. The finite-support obstruction has precisely the rotation and time-reversal hypotheses of T5(d). It does not classify the order attainable by every other placement or settle the full coupled algebra.

## Premises and declared objects

Supply nonzero `K` and `α`, nonsingular kinetic blocks, side at least three for the delta-bond argument, and the explicitly displayed finite-range stencil. A uniform lapse is a sufficient special case in T5, not a necessary condition: proportional lapses also give zero on both sides. The sea here is the free filled-negative-band comparator, not a derivation of the excluded many-record ground state. For `μ > 0` the adiabatic interpretation additionally needs a prepared gapped state and slow driving; at `μ = 0` the finite integral is only a formal response coefficient, not a proof of a local dynamical action or absence of absorption. Its positivity and the off-line algebra remain valid within that coefficient model.

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The clocks, the lengths, the member's kinetic term, the walk and its sea are supplied clauses. Nothing is adopted.
- **Block 112** (landed; the harvest of three probe attempts refereed by another model family).
  - The placement (block 62): `h_jj` and `P_jj` on sites, `h_ij` and `P_ij` (`i < j`) on faces, relabellings `ξ_j` on the bonds `x → x + e_j`.
  - `C[N]` is the per-tick energy with the clocks replaced by a lapse `N` on sites. Its kinetic part is the Legendre transform `(1/(4α))[Σ_jP_jj² − c(Σ_jP_jj)²] + Σ_{i<j}P_ij²/(8α)`, `c = β/(α + 3β)`, each face term timed by the mean of its four corners (or either opposite pair).
  - `G[ξ] = ΣP·δ_ξh`, with `δ_ξh_jj(x) = 2(ξ_j(x) − ξ_j(x − e_j))` and `δ_ξh_ij = ∇_iξ_j + ∇_jξ_i` on the face.
  - T1: at flat strain, for the term linear in canonical momentum, `{C[N], C[M]} = G[ξ]` with `ξ_j(x → x + e_j) = (K/(4α))(N_{x+e_j}M_x − N_xM_{x+e_j})`, for every pair of lapses, iff `c = 1/2` and the timing is symmetric. T2: at `β = −α` the gradient relabelling with `u → u − (2α/(Kw̄²))ζ̈` is a symmetry of the quadratic action up to source terms, for any `ζ(x, t)`.
- **Block 124** (landed): the kinetic family `α tr(ḣ²) + β(tr ḣ)²`. The cubic-only term `γΣḣ_ii²` is the one quadratic form of the cube's symmetry outside it; block 62's T4(c) (landed) gave a witness that it spoils direction-free travelling speed.
- **Block 144** (landed), T5: without the shift, `h = t(∇ξ + ∇ξᵀ)`, `u = 0` solves the source-free member for every `ξ`, with momentum-constraint residual `K(∇²ξ − ∇ div ξ)`.
- **The walk and its sea** (blocks 54 and 139, landed). `H = Σ_aσ_aS_a` with plane-wave block `σ·s`, `s_a = sin k_a`; with the staggered mass, the block on `(k, k + (π, π, π))` is `τ_z ⊗ σ·s + μτ_x`. The sea fills every negative-energy state.
- **A uniform strain** enters the walk through its frame `(1 + h)^{−1/2}` (block 62's frame response), so a strain rate `v` enters as `−½σ·(vs)`.
- **The sea's adiabatic inertia.** For a slow uniform strain `h(t)`, the sea's energy to second order in the rate is `½ḣ·M·ḣ`, with `v·M·v = 2Σ|⟨p|∂H·v|h⟩|²/(E_p − E_h)³` over particle-hole pairs (the adiabatic, or cranking, formula of Inglis; a standard import named at definition level). At `μ = 0` the sea has no gap at the eight corners, but `M` is finite there; the absorption of a slow drive by the gapless corners is outside this note.
- **The walker's placements** (blocks 135 and 136, landed).
  - The lapse couples to `e′ = C₁C₂C₃e`, with `e(x) = Re ψ†(x)(Hψ)(x)` and `C_a` the average over `x ± e_a`. So the walker's part of `C[N]` is the one-walker operator `H_N = ½{Ñ, H}`, `Ñ = C₁C₂C₃N`.
  - The momentum density is block 136's `P^B = (P″ + Q)/2`, and the walker's part of `G[ξ]` is `Σ_{x,j}ξ_j(x)P^B_j(x)`. On plane waves, as derived here from block 136's placements, `⟨k + Q|Σ_xe^{iQx}P″_j(x)|k⟩ = ½(1 + e^{−iQ_j})Π_{l≠j}cos Q_l · ½(P_j(k) + P_j(k + Q))`, with `P_j = sin k_j cos k_j`, and `⟨k + Q|Σ_xe^{iQx}Q_j(x)|k⟩ = Π_a cos Q_a · ¼(e^{−i(k+Q)_j} + e^{ik_j})(σ_jH(k) + H(k + Q)σ_j)`. Runner H1 recovers block 136's books from them.
  - The bracket of two quadratic forms `ψ†Aψ`, `ψ†Bψ` is `ψ†(−i[A, B])ψ`. So `{C[M], C[N]}` has walker part `X = −i[H_M, H_N]`, and block 112's orientation `{C[N], C[M]} = G[ξ(N, M)]` asks for `X = −c·Y`, with `Y` the walker part of `G[ξ(N, M)]` at `c = 1`.
- **Consistency of constraints.** A constraint that must stay satisfied under every allowed evolution must have a weakly vanishing bracket with every allowed generator (the standard constraint algorithm of Dirac and Bergmann; named only).
- **Standard imports, named at definition level:** exact rational and symbolic arithmetic; the arithmetic-geometric mean inequality.

## Theorem T1 — which clock profiles drive the evolution decides the shift

*Statement.* Within block 112's scope:
- (a) For lapses `M = δ_x` and `N = δ_{x+e_j}`, block 112's `ξ(M, N)` is `K/(4α)` on the bond `x → x + e_j` and zero on every other bond, and `{C[N], C[M]}` is exactly that bond's relabelling generator. So the `ξ(M, N)` span every bond field.
- (b) For a uniform lapse `N = 1`, `ξ(M, 1)_j = −(K/(4α))(M_{x+e_j} − M_x)`: over all `M` these span only the gradients, and `G[ξ(M, 1)] = (K/(4α))Σ_xM_x(∇̄·G)(x)`, with `∇̄` the backward difference.
- (c) Hence, at this order:
  - if every clock profile may drive the evolution, every `C[M]` stays satisfied only if `G[ξ] ≈ 0` for every bond field `ξ`: the whole momentum constraint. Block 144's drifting relabellings, whose residual `K(∇²ξ − ∇ div ξ)` is nonzero for transverse `ξ`, are then excluded;
  - if only the uniform profile may, only `∇̄·G ≈ 0` is forced, and the drifting relabellings survive.

*Proof.* (a) and (b): direct from block 112's `ξ` (runner B1–B3; the bracket itself is recomputed from block 112's stencil for twelve bonds). (c): the preservation of `C[M]` under the evolution generated by `C[N]` is `{C[M], C[N]} = −G[ξ(N, M)] ≈ 0`; for every allowed `N` and every `M` this is (a) or (b). ∎

Block 112's T2 is the reason the first reading is natural at linear order: at `β = −α` the member's quadratic action accepts every clock profile as a relabelling. Whether that holds beyond linear order is the reading question.

## Theorem T2 — a cubic-only kinetic term breaks the closure

*Statement.* With `γΣḣ_ii²` added, the diagonal kinetic block becomes `α + γ` and the faces keep `α`. On the `3³` torus, for lapses at `0` and `e₁`, the bracket is affine in `c`, and for `γ = 1/5, −1/7, 2/3` the whole line misses the span of all relabellings. With `γ = 0` and `c = 1/2` it lies in the span.

*Proof.* Exact rank computation over the rationals (runner C1–C2): the relabellings have rank 78; adding the bracket's line raises it to 80. ∎

To justify the parameter quantifier, write the bracket coefficient vector as `B = d0/a_d + c d1/a_d + f/α`, where `a_d = α + γ`, `d0,d1` are its diagonal constant and trace parts and `f` its face part. These vectors do not depend on the kinetic coefficients. On the same `3³` torus the relabelling matrix has rank 78, adjoining `d0,d1` raises it to 80, and adjoining `d0 + d1/2 + f` leaves it at 78. Thus in the quotient by relabellings,
`[B] = (1/a_d - 1/α)[d0] + (c/a_d - 1/(2α))[d1]`.
The two quotient vectors are independent, so closure forces `a_d = α` and `c = 1/2`, hence `γ = 0` and `β = -α`. This supplies the missing parameter argument; three sampled coefficients alone would not suffice. It is a necessary condition for a local prescription required to close also on the `3³` periodic lattice, with the stipulated timing. Singular kinetic cases `α = 0`, `α + γ = 0` or `α + γ + 3β = 0` are excluded from the inverse kinetic calculation and require a separate constraint analysis.

## Theorem T3 — the closing line admits no positive addition

*Statement.* The family `α tr(v²) + β(tr v)² + γΣv_ii²` takes `3α + 9β + 3γ`, `2α + 2γ` and `2α` on the dilation `v = 1`, the E strain `diag(1, −1, 0)` and the T strain `e₁e₂ᵀ + e₂e₁ᵀ`. On the closing line these are `(−6, 2, 2)α`. A positive semidefinite kinetic term on the line is nonnegative on the dilation and on the T strain, which have opposite signs there, so it vanishes on all three strains and hence has `α = β = γ = 0`.

*Proof.* Direct (runner D1–D2). ∎

## Theorem T4 — the sea's inertia is a positive addition

*Statement.*
- (a) For the plane-wave block `σ·s`, `|⟨+|σ·a|−⟩|² = |a|² − (a·s)²/|s|²`. With the staggered mass, the summed matrix elements of `−½τ_z ⊗ σ·a` are `(|s × a|² + μ²|a|²)/(2(|s|² + μ²))`.
- (b) So `v·M·v = ⟨(|s × vs|² + μ²|vs|²)/(|s|² + μ²)^{5/2}⟩/16` per site: a sum of nonnegative terms. On the T strain the integrand's numerator is `(s₁² − s₂²)² + (s₁² + s₂²)s₃² + μ²(s₁² + s₂²)`, positive near `k = (π/2, 0, 0)`: the inertia is nonzero for every `μ ≥ 0`.
- (c) At `μ = 0` the dilation has `|s × s| = 0`: no dilation part. The E and T integrands are `4s₁²s₂² + (s₁² + s₂²)s₃²` and `(s₁² − s₂²)² + (s₁² + s₂²)s₃²` over `|s|⁵`. Averaged over the six axis permutations, which keep the zone and `|s|`, the E integrand minus three times the T integrand is `−[(s₁² − s₂²)² + (s₁² − s₃²)² + (s₂² − s₃²)²]/|s|⁵ ≤ 0`, strictly negative near `k = (π/2, 0, 0)`. So `μ_E < 3μ_T`.
- (d) Read in the member's family, the sea's inertia at `μ = 0` has `α = μ_T/4`, `γ = (μ_E − μ_T)/4`, `β = −μ_E/12`: ratio `β/α = −μ_E/(3μ_T)`, strictly between −1 and 0.
- (e) Added to the member at `α = K/4`, `β = −α`, the total lies on the closing line only if `μ_T = 0`, which (b) excludes.

*Proof.* (a): the projectors `(1 ± H/E)/2` (runner E1–E2). (b): the adiabatic formula with `E_p − E_h = 2E`, over the two sublattice partners (E2–E3). (c): symbolic identities and the permutation average (E3–E4); the integrands are integrable, since near each corner they grow like `1/|k|`. (d) and (e): linear algebra (E5), and T3. ∎

The sea's inertia is of the order of the hopping; the member's `α = K/4`. Their relative size is set by `K`, which is supplied. Any nonzero share takes the total off the closing line.

## Theorem T5 — the walker's side of the clock algebra

*Statement.* With the walker's placements above, and `X`, `Y` as defined there:
- (a) *One lapse uniform.* For `M = 1` and every `N`, `X = −Y`: the walker's bracket is block 112's `G[ξ]` exactly, with `K/(4α) = 1`. The curl part is orthogonal to gradients, `Σ_j(e^{iq_j} − 1)(Q̂_j − P̂″_j) = 0`, so `P^B` and `P″` give the same. With `e` in place of `e′` the ratio is `−1/Π_a cos q_a`, which no constant matches.
- (b) *No `c` for general lapse pairs.*
  - For delta lapses at `u` and `u + 2e₁`, block 112's `ξ` vanishes on every bond, but `[H_M, H_N]` has 16 nonzero two-by-two entries.
  - Along an axis with `M = e^{−iqx}` and `N = e^{iqx}`, `X = −½cos²q(1 + cos q)·Y`. This is `−Y` only as `q → 0`.
  - At 32 rational `(k, q₁, q₂)` no single `c` gives `X = cY` entrywise.
- (d) *No local placement closes it.* Let `E_u = T_uE_0T_u†`, with `E_0 = Σ_{a,b}|a⟩⟨b| ⊗ W_ab` of finite range and Hermitian, be any placement of the walker's energy with `Σ_uE_u = H`, covariant under the cube's proper rotations and invariant under the walk's time reversal `Θ = iσ_yK`, as `e` and `e′` are. (`Θ` fixes `H`: it sends `σ_a` to `σ_yσ_a*σ_y = −σ_a` and `S_a` to `KS_aK = −S_a`, since `S_a` carries `1/(2i)`.) Then there are sites `u ≠ v` that share no bond with `[E_u, E_v] ≠ 0`. Block 112's `ξ(δ_v, δ_u)` vanishes on every bond for such a pair, so no momentum placement and no `c` closes the walker's bracket exactly.
- (c) *The defect is third order.* Take `q₁ = tu` and `q₂ = tv`. For every `k` and all directions, `X + Y` vanishes at orders `t⁰`, `t¹` and `t²`, while `X` starts at `t¹`. At order `t³` it is `(i/4)Σ_j sin k_j cos k_j (u_j − v_j)(4u·v + u_jv_j)` times the identity: the walker's momentum density against a bilinear of third order in the lapses' wave numbers. Along an axis this is `(5i/8) sin 2k · q₁q₂(q₁ − q₂)`, the plane-wave form of `N′M″ − N″M′` up to a constant.

*Proof.*
- (a) Both sides reduce to `∓(i/2)Π_a cos q_a Σ_j sin q_j sin(2k_j + q_j)`. For `X`, `H(k + q)² − H(k)² = |s(k + q)|² − |s(k)|²`. For `Y`, `(e^{iq_j} − 1)(1 + e^{−iq_j}) = 2i sin q_j` and `P_j(k) + P_j(k + q) = sin(2k_j + q_j) cos q_j`; and `Σ_j(e^{iq_j} − 1)(e^{−i(k+q)_j} + e^{ik_j})(σ_jH(k) + H(k + q)σ_j) = 2i(|s(k + q)|² − |s(k)|²)`. Runner H1 checks it at 729 rational points in exact Gaussian rationals.
- (b) Position space for the delta lapses (runner H2), and rational points (H3).
- (c) An exact expansion in `t`, with `sin k_a` and `cos k_a` as symbols reduced modulo `cos² + sin² = 1` and the directions symbolic (runner H4).
- (d) The hop sites, those in a nonzero off-diagonal block of `E_0`, are not empty, since `H` hops. Take `φ(x) = n·x` with `n` rationally independent, so that `φ` separates sites. Let `a_h` and `b_h` be the hop sites with the largest and smallest `φ`, and `t = a_h − b_h`.
  - For hops `(a_h, a′)` and `(b_h, b′)`, take the element `⟨u + a′|E_uE_{u+t}|u + t + b′⟩`. An intermediate site `m = u + s = u + t + s′` needs a block of `E₀` at `(a′, s)` and one at `(s′, b′)`, and `φ(s) = φ(a_h) − φ(b_h) + φ(s′)`.
    - If both blocks are hops, `s` and `s′` are hop sites, so `φ(s) ≤ φ(a_h)` and `φ(s′) ≥ φ(b_h)`. That forces `s = a_h` and `s′ = b_h`.
    - If the first block is on-site (`s = a′`), then `φ(s′) < φ(b_h)`. So `s′` is not a hop site, and `s′ = b′` is impossible, since `b′` is a hop site other than `b_h`.
    - If the second block is on-site (`s′ = b′`), then `φ(s) > φ(a_h)`. So `s` is not a hop site, and `s = a′` is impossible for the same reason.

    So only the path through `u + a_h = u + t + b_h` contributes. Sites that carry only on-site blocks never enter.
  - For `E_{u+t}E_u`, the row `u + a′` is the site `a′ − t` of `E_{u+t}`, with `φ(a′ − t) < φ(b_h)`. It is not a hop site. If it carries an on-site block, the element needs a block of `E₀` between `a′` and `t + b′`, and `φ(t + b′) > φ(a_h)` rules that out. So that element vanishes, and the commutator's element is `W(a_h, a′)†W(b_h, b′)`.
  - Time reversal forces every block to the form `[[p, q], [−q*, p*]]`, a real quaternion. So `W†W′ = 0` only if `W = 0` or `W′ = 0`.
  - `t` is not a unit vector. Maximality of `a_h = p` under the half-turns about the axes gives `n_ip_i + n_kp_k ≥ 0` for every pair of coordinates, and minimality of `b_h = q` gives the reverse. If `p − q = ±e_j`, the two coordinates other than `j` agree, so they vanish, `n` being generic. Then `a_h` and `b_h` lie in `{0, ±e_j}`, and a half-turn carries the nonzero one beyond the other extreme.
  - Runner H5 checks the body-diagonal placement's witness, `t = (4, 2, 2)`, the quaternion form, and the non-adjacency over every rotation orbit in `[−3, 3]³`. ∎

So with walker content in the landed placements, the clock constraints close for a uniform lapse, but not for all pairs. T1's first reading, that every clock profile may drive the evolution, then holds for the walker only through second order in the lapses' wave numbers. Taken exactly, it would put a further condition on the content, since the bracket of the two delta lapses in (b) would have to vanish on every allowed state. By (d) no finite-range placement with the cube's rotations and time reversal avoids this. The statement is against block 112's member, whose relabelling fields live on nearest-neighbour bonds. A member with relabellings of range two is not excluded, and neither are placements of infinite range or placements that break time reversal. The cross bracket between the member's and the walker's parts at first order in the member's momenta, through the walker's frame response, is not examined either. It is a further obligation of the full coupled algebra. The walker-only obstruction does not by itself establish an obstruction for that full algebra.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "decision-record addenda 39-40: the owner's reading questions on relabellings in time and on the zero of energy the member sees"
source_of_blocker_text: decision-record addenda 39 and 40; block 112 (landed); block 144 (landed)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the order to which a local placement can push the walker's clock defect; the member's cubic terms on the lattice; the owner's readings"
conditional_surface_status: "block 112's scope: flat strain, the term linear in canonical momentum, symmetric face timing; uniform strains for the sea; the walker's landed placements"
hypothetical_axiom_status: "the clocks, the lengths, the kinetic term, the walk and its sea are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 112: the lattice clock algebra and the gradient relabelling at `β = −α`.
  - Block 124: the kinetic family. Block 62: the placement, the frame response and the cubic-only witness T4(c).
  - Block 144: the drifting relabellings without the shift.
  - Blocks 54 and 139: the walk and its staggered mass.
  - Blocks 135 and 136: the walker's energy `e′` and momentum `P^B`, and the books.
- **Opened, not landed.** Blocks 146–149 are not used. Block 147's reading question is the second one treated here.
- **Probes.** Refill v asked for the walker's side of block 112's algebra, a check of T1(c), the sea's response and the member's cubic terms. Two attempts answered, both by Claude Opus 5.5 workers, the same model family as the supervisor, and neither refereed by another family:
  - #9254 found T5(a) and the delta-lapse witness of T5(b) first, in position space on the `6³` torus, with the two-step element `−(i/16)[(m₀n₁ − m₁n₀) + (m₁n₂ − m₂n₁) + (m₀n₂ − m₂n₀)]`, whose last term no bond's `ξ` produces. It also found that with block 137's `e` no normalization matches even at first order. This note's T5 re-derives (a) and (b) in plane-wave form and adds (c).
  - #9259 computed T4's inertia independently. It claims, without verification in this note, that the sea's inertia has a positive cubic-only part for every `μ`, so `μ_E > μ_T`, and that `β/α` lies in `[−0.4648, −0.4645]` at `μ = 0`. No interval or decimal assertion from that draft is adopted here.
- **In the literature.**
  - That the algebra of the time constraints forces the space constraints: Hojman, Kuchař and Teitelboim; the constraint algorithm of Dirac and Bergmann.
  - The adiabatic inertia of a driven ground state (Inglis).
  - Terms induced by a lattice's vacuum that break a continuum symmetry, and their retuning in lattice practice.
  - All reference only.
- **New here:**
  - T1: on the lattice, block 112's relabellings span every bond field, so the reading on clock profiles decides the drifting relabellings.
  - T2: a cubic-only kinetic term breaks block 112's closure.
  - T3–T4: the closing line admits no positive addition, and the walker sea's inertia is one, with its own ratio in (−1, 0) at `μ = 0`.
  - T5(c): the walker's defect is of third order, with its form, for every walker momentum and all lapse directions.
  - T5(d): no finite-range placement with the cube's rotations and time reversal closes the walker's clock algebra with block 112's `ξ`.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: what block 112's algebra implies for the two reading questions. The obligations are:
- (O1) the span of the relabellings, for every and for uniform clock profiles (T1);
- (O2) the closing line in the kinetic family with the cube's symmetry (T2);
- (O3) positive additions to the closing line (T3);
- (O4) the sea's inertia on uniform strains (T4);
- (O5) the walker's side of the algebra (T5).

T1–T5 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- with every clock profile allowed, the drifting relabellings are excluded at this order;
- no cubic-only kinetic term keeps block 112's closure;
- no nonzero positive semidefinite term can be added to the member without leaving the closing line;
- no `c` closes the walker's bracket with block 112's `ξ` for every lapse pair, in the landed placements or in any finite-range placement with the cube's rotations and time reversal.

### N1 — Attack routes and the scope they leave
Attack routes on the negative sentences, each tested here:
1. *Another kinetic ratio compensates the cubic-only term.* The bracket is affine in `c`, and for each tested `γ` the whole line misses the relabellings' span (runner C1–C2). ATTEMPTED.
2. *A positive semidefinite addition with a dilation part lands on the closing line.* The line takes `(−6, 2, 2)α` on the dilation, E and T strains, so a form nonnegative on the dilation and the T strain vanishes there (runner D1–D2). ATTEMPTED.
3. *The sea's inertia vanishes on some strain the argument needs.* It is nonzero on the T strain for every `μ ≥ 0`, and its own ratio at `μ = 0` lies strictly inside `(−1, 0)` (runner E1–E5). ATTEMPTED.
4. *Another normalization `c` closes the walker's bracket.* Delta lapses two steps apart have `ξ = 0` and a nonzero bracket, whatever `c` (runner H2); at rational points no single `c` works (H3). ATTEMPTED.
5. *Another momentum placement closes it.* For lapses that share no bond `ξ = 0`, so no momentum placement enters the required identity (runner H2, H5). ATTEMPTED.
6. *Another finite-range energy placement closes it.* Excluded for every placement with the cube's rotations and time reversal by the extreme-hop witness (T5(d); runner H5). ATTEMPTED.

Scope left open by these routes:
- Block 112's scope: flat strain, the term linear in canonical momentum, and its four timings. Higher orders are not treated.
- T1(c) is a reading. It says what each reading implies and does not choose between them.
- The adiabatic inertia is the sea's response to a slow uniform strain. At `μ = 0` the gapless corners also absorb a slow drive, and nonuniform strains are not treated.
- Retuning: a member whose supplied numbers are the closing line minus the sea's inertia would close with the sea included. That is the first of the two consistent readings, not a counterexample.
- T5(a)–(c) hold for block 135's `e′` and block 136's `P^B`. T5(d) does not cover placements of infinite range, placements that break time reversal, or a member whose relabelling fields reach beyond neighbouring sites.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- "canonical momentum" (claim scope, premises, scope list) names block 112's momenta. It is a definition, not an import.
- "the first reading is natural at linear order" (after T1) is annotated context: block 112's T2 is cited for it, and no conclusion rests on the word.
- The supplied member, clocks, walk, sea and the adiabatic formula are the only premises, all stated under Premises.

No hidden condition was found.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 112 (landed) | the bracket, `ξ(M, N)`, the timings, the gradient relabelling | yes (recomputed) |
| block 124 (landed) | the kinetic family | yes (restated) |
| block 62 (landed) | the placement; the frame; the cubic-only witness | yes (restated) |
| block 144 (landed) | the drifting relabellings and their residual | yes (restated) |
| blocks 54, 139 (landed) | the walk; the staggered mass | yes (restated) |
| blocks 135, 136 (landed) | the walker's `e′` and `P^B` | yes (restated in plane-wave form; H1 recovers the books) |
| probes #9254, #9259 (unrefereed, same family) | T5(a)–(b) and T4, found independently | no (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "every clock profile a relabelling forces the whole momentum constraint; no cubic-only term closes; no positive inertia can be added to the member" | executed: delta lapses at a bond's ends; block 112's bracket for twelve pairs | executed: the uniform lapse's gradients and the divergence identity | executed: the cubic-only bracket's rank on the `3³` torus | executed: the sea's matrix elements with and without the mass; positivity; the permutation average; the walker's bracket (one lapse uniform, delta lapses, the third-order defect, the extreme-hop witness) | block 112's scope; uniform strains for the sea |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository. It is not used. `scale_reference_primitive` is not used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "T1 is the continuum result that the algebra of time constraints forces the space constraints, restated."
  - *Reply:* It is the lattice form of it, on block 112's landed bracket. The lattice fact is that the relabellings reach every bond field, not only the continuum's smooth ones. The note's use is to turn a reading question into a statement about which clock profiles may drive the evolution.
- *Objection:* "Of course a vacuum's response must be renormalized into the supplied numbers."
  - *Reply:* That is the first consistent reading, and the note says so. What the lattice adds is that the response is not of the closing form at all: at `μ = 0` its own ratio is in (−1, 0), and a cubic-only part is allowed. So absorbing it means supplying numbers off the closing line, tuned against the sea.

### N8 — Cross-cycle echo
- Block 112: the clock algebra.
- Block 144 T5: the drifting relabellings.
- Block 147 (open): the zero of energy.
- This note: what the algebra says about both readings.

## Falsifiers

- A bond field outside the span of block 112's `ξ(M, N)`.
- A cubic-only kinetic term and a ratio at which block 112's bracket is a relabelling.
- A nonzero positive semidefinite kinetic term on the closing line.
- A uniform strain on which the sea's adiabatic inertia is negative, or a vanishing T part.
- A lapse pair two steps apart whose walker bracket vanishes, or a nonzero second-order term in the walker's defect.
- A finite-range placement with the cube's rotations and time reversal whose energies commute at every pair of sites that share no bond.

## Boundaries and non-claims

- Block 112's scope; uniform strains for the sea; the adiabatic formula.
- The member's higher orders are not treated. The walker's side is treated only in the landed placements.
- Not refereed by another model family.
- No gravitational claim is made, and no reading is chosen.

## Imports

- `minimal_axioms`. Blocks 54, 62, 112, 124, 139 and 144 (landed), restated or recomputed.
- Named standard imports, at definition level: exact rational and symbolic arithmetic; the adiabatic (cranking) formula of Inglis; the constraint algorithm of Dirac and Bergmann; the arithmetic-geometric mean inequality.

## Review record

- **Who and when.** Supervisor-run consolidating note, the ninety-eighth since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), with exact checks by its own runner. It is not refereed by another model family.
- **Before writing.** A panel of three Claude Opus 5.5 subagents (same model family) proposed a gate on the lapse placement and a lemma on the sea's inertia (decision-record addendum 40). The own prior-art check then found block 112, which already answers the gate; this note draws the two consequences. It also found block 62's cubic-only witness.
- **Pacing.** This is a consolidating note of lemmas, per the pacing rule of addendum 40.
- **The walker's side (T5).** Added after probe #9254 (same family) answered refill v's first problem. T5 re-derives its (a) and (b) in plane-wave form, and adds the third-order form (c) and the no-go for every local placement (d).
- **A panel's rigour check (2026-09-26).** The strategy lens of a panel (Claude Fable 5.1, same vendor family, not a referee) asked for four changes:
  - T5(d)'s single-path step now handles sites that carry only on-site blocks explicitly.
  - The time reversal is named. The lens thought `H` odd under `iσ_yK`; it is invariant once `S_a`'s own sign flip is counted, and the note now says so.
  - The scope is stated against block 112's nearest-neighbour relabellings.
  - The cross bracket through the walker's frame response is listed as an open obligation.
- **Independence.** Mutation census: ten mutations in families B–E and H, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_every_clock_profile_a_relabelling_forces_the_whole_momentum_constraint_and_no_positive_inertia_can_be_added_to_the_member_2026_09_25.py
```

Expected: `TOTAL: PASS=24 FAIL=0`.

## Dependencies

- [Current scoped input](ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [Current scoped input](ADMISSIBILITY_RULE_BLINDNESS_TO_COIN_ROTATIONS_THAT_VARY_IN_TIME_LEAVES_EXACTLY_BLOCK_62S_TWO_KINETIC_NUMBERS_AND_NO_RATIO_MAKES_A_TRANSVERSE_RELABELLING_IN_TIME_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [Current scoped input](ADMISSIBILITY_RULE_THE_MEMBERS_PULL_CARRIES_THE_VELOCITY_TERMS_THAT_GIVE_PULL_BOUND_PAIRS_WEIGHT_ONE_ALONG_EVERY_AXIS_AT_FIRST_ORDER_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [Current scoped input](ADMISSIBILITY_RULE_ONE_LIGHT_CONE_EXACTLY_ON_THE_LATTICE_THE_TWO_STEP_CONTENT_MEETS_THE_MEMBERS_IDENTITY_FOR_EVERY_STATE_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [Current scoped input](ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [Current scoped input](ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_THE_STAGGERED_MASS_KEEPS_THEM_EXACTLY_SO_MASSIVE_CONTENT_MEETS_THE_MEMBER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [Current scoped input](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Current scoped input](ADMISSIBILITY_RULE_THE_MEMBERS_ZERO_MODE_TESTS_THE_ZERO_OF_ENERGY_IF_THE_MEMBER_SEES_THE_HALF_FILLED_SEA_A_CLOSED_LATTICE_BOUNCES_OR_CANNOT_MOVE_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [Current scoped input](MINIMAL_AXIOMS_2026-06-29.md)
