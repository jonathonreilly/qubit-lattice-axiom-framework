---
claim_id: admissibility_rule_no_local_tie_makes_the_coins_rotation_a_bond_strain_every_tie_stationary_content_cannot_feel_is_a_relabelling_at_every_reach_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN block 64's strain coupling H[B] of block 54's walk (identity frame, uniform rates) as landed, for a local linear tie B = T theta of three site rotations to the nine bond strains, whose strain on the bond (x, x + e_a) reads theta within r steps of the bond's ends (any finite r; translation-invariant or not): (T1) on plane-wave pairs the tie's response T^dagger J has the symbol sum_aj chat_aj(q) (e^{ik_a} + e^{-ik'_a})(s_j + s'_j)/4 chi'^dagger sigma_a chi, divergence-free at equal energies; (T2) for q in a non-empty open set the equal-energy pair symbols span the six-dimensional divergence-free space; (T3) T^dagger J = 0 on every bounded stationary state of the infinite lattice iff the tie is a relabelling B = d(M theta) with M reading theta within r steps: 3|ball_r| = (2r+1)(2r^2+2r+3) per rotation component for translation-invariant ties (the supervisor's own proof, unrefereed; the probes' reach-one and reach-two torus computations #8853/#9215, refereed by #8977/#9320, agree); (T4) in block 64's quadratic family (continuum symbols, leading order): blind to bond rotations iff (c1, c2, c3) ~ (1, 2, -4), whose kernel on transverse strains is the three bond rotations; every divergence-free source balanced iff (2c1 - c2)(2c1 + c2)(2c1 + c2 + c3)(2c1 + c2 + 2c3) != 0; beta = c4/(2(2c1 + c2 + 2c3)) (a harvest of #8853 part (b), refereed by #8977). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21
  - admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_makes_a_varying_rotation_of_the_coin_axes_a_symmetry_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_no_local_tie_makes_the_coins_rotation_a_bond_strain_2026_09_27.py
---

# No local tie makes the coin's rotation a bond strain: every tie that stationary content cannot feel is a relabelling, at every reach

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 63–65 as landed; T2 and T3 are the supervisor's own proof, unrefereed; T3 at reaches one and two agrees with probe computations #8853 and #9215, each refereed by another model family in #8977 and #9320; T4 is a harvest of #8853 part (b), refereed in #8977; nothing adopted or registered; unaudited)

This note works within blocks 63, 64 and 65 as landed on main (the walk's bond current, the strain coupling of the bonds, and the rotation of the coin at each site) and asks whether the coin's rotation can be carried by the bond strains; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 64 put a strain `B_a^j` on every bond, nine numbers per site. Block 65 turned the coin at each site, three numbers per site. It named the next step: which variables carry the six symmetric numbers and which the three rotations, in one formulation. Block 65 also noted that turning a site's bonds is not turning its coin.

The question here is whether the three rotations can be written as strains. That would be a tie `B = Tθ`. For such a tie to act like the coin's rotation, the walk must not feel it in any stationary state, as it does not feel the coin's rotation (block 65 T3). That is `T†J = 0`.

- **T1: the symbol.** On two plane waves, the tie's response is a fixed bilinear expression in the tie's symbol and the pair's current. At equal energies that current is divergence-free.
- **T2: the currents fill their space.** For wave vectors `q` in an open set, the currents of equal-energy pairs span every divergence-free pattern at `q`. The proof uses six exact pairs of energy one and continuity.
- **T3: only relabellings.** A local tie of any finite reach that no bounded stationary state feels is a relabelling `B = d(Mθ)`, and conversely. A relabelling carries no rotation: its curls vanish (block 64 T1). So under block 64's coupling the coin's three rotations are not strains of the bonds, and that coupling needs nine strains plus three rotations. At reaches one and two the probes found the same on finite tori, and two referees from another model family confirmed it.
- **T4: the strains' own energy (a harvest).** In block 64's quadratic family, only the blind ratio `(1, 2, −4)` does not see bond rotations. That member leaves the three bond rotations unbalanced, so it cannot hold a bond torque. The family balances every divergence-free source iff four factors are non-zero, and there `β = c₄/(2(2c₁ + c₂ + 2c₃))`.

In plain terms: under block 64's coupling a site's coin can be turned, and a site's bonds can be turned, and no local rule lets one stand in for the other without the walk noticing. So that coupling needs both. Its energy then either ignores the bonds' own turning, with bending exponent one and the torque of stationary content left unbalanced, or it balances the torque, with the exponent supplied.

The landed two-step programme does not meet this choice. Blocks 120 and 136 source the symmetric member with the two-step momentum's symmetric stress, which has no bond torque. Block 179 (pushed) shows why: the torque belongs to the one-step momentum.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-27) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Blocks 63, 64 and 65 are used as landed on main.

- **Walk and current** (block 63, landed). `H = Σ_a σ_a S_a`, `S_a = (T_a − T_a†)/(2i)`. The bond current is `J_a^j(x → x + e_a)`. Block 63 T3(b) gives its pair form, quoted: "`J_a^j = e^{iq_a/2} cos(k̄_a) Θ_a^j`". A relabelling generates "`i[H, G_ξ] = Σ_a Σ_j σ_a ½{C_a[d_aξ_j], S_j}`". Block 63 T2(c), quoted: "If `Hψ = Eψ` — or `ψ` is any superposition of eigenstates of one energy — the left side of (b) vanishes for every `ξ`". Block 63 N3, quoted: "Stationary means a superposition of eigenstates of one energy."
- **Strains** (block 64, landed): "`H[B] = H + Σ_{a,j} σ_a ½{C_a[B_a^j], S_j}`". The field quantities are quoted as "`T_1 = T^j_{kl}T^j_{kl}`, `T_2 = T^j_{kl}T^l_{kj}`, `T_3 = V_lV_l`". The exponent is quoted as "block 59's exponent is `β = c_4/(4c_1 + 2c_2 + 4c_3)`". The rotation of a site's bonds is quoted as "consider the strain `δB_a^j(x) = ω_{aj}(x)`: a rotation of the three bonds that leave `x`". The blind density is quoted as "the second-order part of `D*` has zero variational derivative with respect to the antisymmetric part".
- **The coin's rotation** (block 65, landed). Its response, quoted: "It vanishes at every site if psi is stationary under the unperturbed H." Its N1.2, quoted: "*A rotation of the bonds is not a rotation of the coin.*" Also quoted: "Which lattice variables carry the symmetric six numbers (bonds, by blocks 63 and 64) and which the rotation three (sites, by this note), in one formulation, is the named next step."
- **Tie.** A linear map from a site field `θ` (one rotation component; the three components behave identically) to strains, `B_a^j(x) = Σ_d c_x(a, j, d) θ(x + d)`. It has **reach `r`** if `c_x(a, j, d) = 0` unless `d` lies in the stencil `St_a(r) = Ball_r(0) ∪ Ball_r(e_a)`, with taxicab balls. `St_a(1)` has 12 sites and `St_a(2)` has 38. It is **translation-invariant** if `c_x` does not depend on `x`.
- **Response.** `(T†J)(y) = Σ_{a,j,d} c_{y−d}(a, j, d) J_a^j(y − d)`. By block 64 T1(b) this is `∂⟨H[Tθ]⟩/∂θ(y)`.
- **Bounded stationary states.** Finite superpositions `ψ = Σ χ_k e^{ik·x}` on the infinite lattice with `h(k)χ_k = Eχ_k` for one `E`, where `h(k) = Σ_a σ_a sin k_a`. They are bounded solutions of `Hψ = Eψ`. The current is a local expression in `ψ`, and every identity used is a local finite sum.
- **Relabelling tie.** `B = d(Mθ)`: `B_a^j(x) = ξ_j(x + e_a) − ξ_j(x)` with `ξ_j = M_jθ` linear and local.
- **Symbols.** `q = k − k'`, `s_j = sin k_j`, `s'_j = sin k'_j`. `ĉ_aj(q) = Σ_d c(a, j, d) e^{−iq·d}`. `w_a(q) = 1 − e^{−iq_a}`. `D(q) = {J ∈ ℂ^{3×3}: Σ_a w_a(q) J_aj = 0 for each j}`.

In the comparator, a frame's local rotation is carried by a connection kept apart from the frame. That is the first-order formalism of Kibble and Sciama, with Hehl's account of it. This note uses none of it as authority.

## Domain qualifications

- Identity frame and uniform rates. First order in the strains and rotations, as in blocks 64 and 65.
- Ties are linear and local; nonlinear ties are not treated.
- T3 is stated on the infinite lattice. The probes' torus results are a separate statement: on a finite torus fewer stationary states test the tie.

## Theorem T1 — the symbol of the response

*Statement.* (a) For plane waves `χe^{ik·y}` and `χ'e^{ik'·y}`: `⟨ψ'| σ_a ½{C_a[δ_x], S_j} |ψ⟩ = e^{iq·x} Ĵ_a^j(k', k)`, with `Ĵ_a^j(k', k) = ¼(e^{ik_a} + e^{−ik'_a})(s_j + s'_j) χ'†σ_aχ`. (b) `Σ_a w_a(q) Ĵ_a^j = (i/2)(s_j + s'_j) χ'†(h(k) − h(k'))χ`. This is zero when `χ`, `χ'` are eigen-coins of one energy. (c) A tie of finite reach has `T†J = 0` on every bounded stationary state iff two things hold. First, `Σ_{a,j} ĉ_{aj}(q) Ĵ_a^j(k', k) = 0` for every pair of plane waves of one energy. Second, the same holds site by site, with `ĉ` built from the pattern `γ_y(a, j, d) = c_{y−d}(a, j, d)`, for ties that are not translation-invariant. (d) A relabelling tie with `ξ_j = Σ_d μ_j(d) θ(x + d)` has `ĉ_aj(q) = −w_a(q) μ̂_j(q)`.

*Proof.* (a) `S_j` multiplies a plane wave by `s_j`. `C_a[δ_x]` joins `x` and `x + e_a` with weight ½. The matrix element is `½ · ½(e^{ik_a} + e^{−ik'_a}) e^{iq·x}(s_j + s'_j)`. This is block 63 T3(b)'s form, since `e^{iq_a/2} cos k̄_a = ½(e^{ik_a} + e^{−ik'_a})` (runner B1, at two sites and for all nine index pairs). (b) `(1 − e^{−iq_a})(e^{ik_a} + e^{−ik'_a}) = 2i(s_a − s'_a)`, and `Σ_a s_aσ_a = h(k)` (B2). (c) Take `ψ = χe^{ik·x} + e^{iφ}χ'e^{ik'·x}` with one energy. `J` is quadratic, so `(T†J)(y)` is the sum of the two single-wave terms and `e^{iq·y−iφ}X + c.c.`, where `X = 2Σ ĉ_aj(q) Ĵ_a^j`. A single wave is stationary, and varying `φ` separates `X`. Superpositions of more waves add only such pair terms. (d) Collect coefficients (B3). ∎

## Theorem T2 — the currents of equal-energy pairs fill the divergence-free space

*Statement.* There is a non-empty open set `U` of wave vectors on which the symbols `Ĵ(k', k)` span `D(q)`, where `k − k' = q`, both energies are positive and equal, and the coins are eigen-coins. `D(q)` has dimension six.

*Proof.* Take `q₀ = (q₁, 0, 0)` with `e^{iq₁/2} = (4 + 3i)/5`, so `e^{iq₁} = (7 + 24i)/25` and `sin q₁ = 24/25`. Take six pairs, with `k' = k − q₀` in each:
- Four with `k₁ = q₁/2`. Here `(e^{ik₂}, e^{ik₃})` is `((3 + 4i)/5, ±1)` or `(±1, (3 + 4i)/5)`.
- Two with `k₁ = q₁/2 + π/2`. Here `(e^{ik₂}, e^{ik₃})` is `((4 + 3i)/5, 1)` or `(1, (4 + 3i)/5)`.

In all six, both energies are exactly one (runner C1). The six symbols are divergence-free and have rank six (C2). So they span `D(q₀)`, whose dimension is `9 − 3`.

Now move `q`. `E(k)² − E(k − q)² = Σ_a sin q_a sin(2k_a − q_a)`, and at each base pair its derivative in `k₁` is `2 sin q₁ cos(2k₁ − q₁) = ±48/25 ≠ 0` (C3). By the implicit function theorem, each pair continues to a pair of equal energy for every `q` near `q₀`: `k₁` moves with `q`, and `k₂, k₃` stay fixed. The coins `(E + s₃, s₁ + is₂)` stay continuous and non-zero, since `E + s₃ ≥ 1` at the base. So the six symbols depend continuously on `q`. A non-zero 6×6 minor stays non-zero on a neighbourhood `U` of `q₀`. There the six are independent vectors of `D(q)`, and `dim D(q) = 6` because `w₁(q) ≠ 0`. ∎

## Theorem T3 — every tie that stationary content cannot feel is a relabelling

*Statement.* Let `T` be a local linear tie of finite reach `r`.
- (a) `T†J = 0` on every bounded stationary state iff `T` is a relabelling tie `B = d(Mθ)` with `M` reading `θ` within `r` steps.
- (b) For translation-invariant ties these form a space of dimension `3|Ball_r| = (2r + 1)(2r² + 2r + 3)` per rotation component: 21, 75, 189 at `r = 1, 2, 3`.
- (c) A relabelling carries no rotation: every function of the curls is unchanged by it (block 64 T1(a)).

*Proof.* *Translation-invariant ties.* By T1(c) and T2, `ĉ(q)` annihilates `D(q)` for `q ∈ U`. The annihilator of `D(q)` is `{w(q)mᵀ : m ∈ ℂ³}`, so `w_b ĉ_aj − w_a ĉ_bj = 0` on `U` for all `a, b, j`. These are trigonometric polynomials, and they vanish on an open set, so they vanish identically.

In the ring of polynomials in `y_a^{±1}`, with `y_a = e^{−iq_a}`, this gives `(1 − y₂)ĉ_1j = (1 − y₁)ĉ_2j`. `1 − y₁` is prime and does not divide `1 − y₂`, so `ĉ_1j = (1 − y₁)m_j` with `m_j` a polynomial. Then `ĉ_aj = (1 − y_a)m_j` for every `a`. By T1(d) this is a relabelling tie with `μ_j = −m_j`.

*The chain lemma: `μ_j` lies on `Ball_r`.* The tie's pattern vanishes outside `St_a(r)`. Its pattern is `μ_j(d) − μ_j(d − e_a)` up to sign, so `μ_j(d) = μ_j(d − e_a)` for every `d ∉ St_a(r)`. Let `|d|₁ = R > r`.
- If some `d_a ≥ 0`, then for `n ≥ 1` the site `d + ne_a` lies at distances `R + n` from `0` and `R + n − 1` from `e_a`. Both exceed `r`, so the site is outside the stencil. Hence `μ_j(d) = μ_j(d + e_a) = μ_j(d + 2e_a) = …`, which is 0 because `μ_j` has finite support.
- If every `d_a < 0`, the sites `d − ne_a` lie at distances `R + n` and `R + n + 1`, and the same argument gives `μ_j(d) = 0`.

Conversely, any `μ` on the ball gives a tie inside the stencils. The map `μ ↦` tie is injective: a pattern that vanishes is invariant under every shift, hence zero. That gives (b); runner D1 re-counts it by union-find at `r = 1, 2, 3`.

*Ties that are not translation-invariant.* By T1(c) the argument applies at each site `y` to `γ_y(a, j, d) = c_{y−d}(a, j, d)`. It gives `γ_y(a, j, d) = μ_{y,j}(d) − μ_{y,j}(d − e_a)` with `μ_y` on `Ball_r`. Then `B_a^j(x) = ξ_j(x) − ξ_j(x + e_a)` with `ξ_j(x) = Σ_y μ_{y,j}(y − x) θ(y)`: a relabelling with a local, site-dependent `M`.

*The converse of (a).* `T†J = −M†(div J)`. `div J = 0` at every site for every bounded stationary state, because block 63 T1's continuity identity is local. It holds for `e^{−iEt}ψ`, whose momentum density is constant in time. (c) is block 64 T1(a). ∎

*Checks at reaches one and two.* Runner D3 runs the probes' reach-one system on the `4³` and `6³` tori. It maps `ℤ[1/2][i, √2, √3]` to `F_p` with `p = 1048609`. The `6³` torus has 125184 rows of rank 87 = 108 − 21, and the 21 relabelling ties are in the kernel. So on that torus only relabellings survive. The `4³` torus has rank 81, since offsets `2` and `−2` coincide there. Probe #9215 found rank 267 = 342 − 75 at reach two on the `8³` torus. The referees reran both computations with other primes.

The forward-bond tie of issue #8659, `B_a^j = ε_abj θ_b(x)`, pairs to a non-zero value with some of T2's pairs for each `b` (D2). So it is felt by stationary content.

## Theorem T4 — the strains' own energy once the rotations are separate (a harvest of #8853 part (b))

*Statement* (block 64's continuum symbols, leading order in the wave vector). Consider the quadratic family `c₁T₁ + c₂T₂ + c₃T₃` of a plane-wave strain.
- (a) It is independent of the strain's antisymmetric part, the bond rotations, iff `(c₁, c₂, c₃)` is along `(1, 2, −4)`, block 64's blind ratio.
- (b) At wave vector `κe₃`, where the `B₃^j` are relabellings, the static form on the six transverse strains has eigenvalues `κ²·{2c₁ − c₂, 2c₁ + c₂ (twice), 2c₁ + c₂ + c₃ (twice), 2c₁ + c₂ + 2c₃}`. So every divergence-free source is balanced iff `(2c₁ − c₂)(2c₁ + c₂)(2c₁ + c₂ + c₃)(2c₁ + c₂ + 2c₃) ≠ 0`.
- (c) At the blind ratio the form has rank three, and its kernel is exactly the three bond rotations. A source with a bond torque has no static balance there.
- (d) Block 64 T4's exponent is `β = c₄/(2(2c₁ + c₂ + 2c₃))`. It is one on the blind ratio with block 64's `c₄`. Off the blind ratio, `β = 1` is the hyperplane `c₄ = 2(2c₁ + c₂ + 2c₃)`.

*Proof.* (a) Expand the density of `B = S + A` and match coefficients (runner E1). (b) The characteristic polynomial factors as stated (E2). The walk's source is divergence-free on stationary states (block 63 T2(c)), so it is orthogonal to the relabellings; balancing every such source means the form is non-degenerate. (c) Rank and kernel at the blind ratio (E3). (d) Block 64 T4 (E4). ∎

## What this settles and what it does not

- **Settled.** Block 65 left open how the three rotations and the six symmetric numbers fit into one formulation. Under block 64's one-step coupling, the rotations cannot be moved into the bond strains by any local linear tie that stationary content does not feel, at any reach. So that coupling needs nine strains per site plus three rotations per site.
- **The fork under block 64's coupling.** Its strains' energy can be asked for either of two things.
  - *Blindness to bond rotations.* This is block 64's ratio: `β = 1`, and the bond torque of stationary content has no static balance (T4(c); block 64 T5).
  - *Balance of every divergence-free source.* The four factors must be non-zero, and `β = c₄/(2(2c₁ + c₂ + 2c₃))` is not fixed by this requirement.
  - Block 64 T2 picked out its ratio by treating the frame's antisymmetric part as the coin's rotation. On the lattice that part is the bond rotation, and T3 shows the coin's rotation is not one.
- **Not a fork of the landed two-step programme.**
  - Blocks 69, 120 and 136 (landed) use the two-step momentum. Block 120 sources block 62's symmetric member with its current, and block 136 conserves a symmetric stress with a symmetric momentum.
  - A symmetric stress has no bond torque, and the content it defines does not see bond rotations at all. So neither the fork nor the need for three separate rotations arises there (block 179, pushed).
  - This note's T3 and the fork are therefore properties of block 64's one-step coupling.
- **Not settled.**
  - Ties that are nonlinear.
  - Blindness at order rotation times strain, where the content's own transformation is not constructed (block 65 N1.3).
  - A lattice placement of T4's family.
  - Whether a further principle fixes the ratios.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 65 N1.2 as landed: which lattice variables carry the symmetric six numbers and which the rotation three, in one formulation"
source_of_blocker_text: admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_makes_a_varying_rotation_of_the_coin_axes_a_symmetry_bounded_theorem_note_2026-09-21
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "block 179: the torque belongs to the one-step momentum; the two-step symmetric stress; blindness at order rotation times strain"
conditional_surface_status: "exact within blocks 63-65 as landed at first order; T4 in continuum symbols at leading order"
hypothetical_axiom_status: "the walk, the strain coupling, the ties and the field-energy family are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.** All landed:
  - block 63: the bond current and the relabelling's deformation;
  - block 64: the strain coupling, the family and the bond torque;
  - block 65: the coin's rotation and the named next step.
- **Probes.**
  - #8853 (worker `w-jonathonsmac4f50-jf0c7`, Claude Opus 5.5, the supervisor's family). It found at reach one that only relabelling ties survive on the `6³` torus (rank 87 mod p), and found part (b), T4 here.
  - #8977 (worker `w-macbookpro90c72-j3ef3`, `grok-4.6`, another family) refereed #8853 with another prime and a re-expanded form.
  - #9215 (worker `w-macbookpro9927a-jf66c`, Claude Opus 5.5) did reach two on the `8³` torus (rank 267 of 342).
  - #9320 (worker `w-macbookpro90c72-j3761`, `grok-4.6`) refereed it with two primes.
  - Both attempts left open a lemma independent of the reach: that equal-energy currents test every divergence-free bond pattern.
  - Earlier, #8659 and #9047 showed that two particular ties fail.
- **Landed blocks on the two-step momentum** (the supervisor's own):
  - block 120: only the two-step current can source block 62's symmetric member;
  - block 136: a symmetric stress conserved with the symmetric momentum `(P″ + Q)/2`, and the one-step momentum fails;
  - block 138: the symmetric momentum as the two-step momentum plus half the curl of the spin.
  - This note's first version missed them; see the review record.
- **In the literature.**
  - A frame and a separate rotation connection is the first-order formalism of Kibble and Sciama, with Hehl's account. There the connection is an independent field unless a further condition removes it.
  - The three quadratic invariants of a frame's curl are Hayashi and Shirafuji's family (block 64's prior art).
  - A symbol-level argument through the spanning of a set of test vectors, continuity in the wave vector, and division of multivariate polynomials is standard algebra.
  - No result is imported.
- **New here.**
  - T2 and T3 for every reach, on the infinite lattice. This is the spanning lemma both attempts left open, proved with six exact pairs and continuity, plus the chain lemma.
  - Ties that are not translation-invariant.
  - T4(c): the blind member's kernel.
  - A new exact runner.
- **Provenance.** T2 and T3 are the supervisor's own (Claude Opus 5.5), unrefereed. Their reach-one and reach-two cases agree with the probes' refereed torus computations. T4 is found by the supervisor's family and confirmed by another.

## Exact target and obligation graph

Target: the ties of site rotations to bond strains that stationary content cannot feel. The obligations are:
- (O1) the premises (A3–A5);
- (O2) the symbol and its divergence (B1–B3);
- (O3) spanning on an open set (C1–C3, with the implicit function argument in the text);
- (O4) identities to factorisation to the chain lemma (text; D1);
- (O5) the probes' torus checks (D3);
- (O6) the family's properties (E1–E4).

## No-Go Discipline Gate

The note has two negative sentences. First, no local linear tie other than a relabelling has `T†J = 0` on every bounded stationary state, so the coin's rotation is not a bond strain. Second, the blind member of block 64's family cannot balance a bond torque.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *A tie of larger reach.* T3 holds for every finite reach. ATTEMPTED; closed by the proof.
2. *A tie that varies from site to site.* Handled site by site. ATTEMPTED; closed.
3. *Fewer test states, as on a torus.* The torus is a different statement. At reaches one and two the probes found that the `6³` and `8³` tori already suffice. For larger reaches on tori, not examined.
4. *A nonlinear tie.* At first order only its linear part enters the response. The linear part must then be a relabelling, and higher orders are not examined.
5. *A tie that also involves the time direction, or a rate field.* Not examined.
6. *A tie felt by stationary content, balanced by a field energy that depends on `θ`.* Then the field energy is not blind to the coin's rotation. That is outside the question asked, and it is block 64 T5's route.
7. *A tie into the strains together with other terms, such as block 65's scalar hop.* Not examined. The question here is whether the strains alone carry the rotation.
8. *For the second sentence, a field energy outside the quadratic family, or a lattice placement.* Not examined; T4 is at leading order.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The following are declared: the identity frame, first order, uniform rates, the bounded stationary states, the stencils and linearity.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 63 (landed) | the current, its pair form, divergence-free on stationary states | yes (quoted, A3; re-derived, B1–B2) |
| block 64 (landed) | the strain coupling, the family, `β`, the bond torque, curls unchanged by relabellings | yes (quoted, A4) |
| block 65 (landed) | the coin's rotation unfelt by stationary states; the named next step | yes (quoted, A5) |
| probes #8853, #9215 and referees #8977, #9320 | the torus results; T4 | reach-one torus rerun (D3); T4 rerun (E) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "every tie unfelt by stationary content is a relabelling; the blind member cannot balance a bond torque" | executed: the symbol and divergence, symbolically | executed: the chain lemma by union-find, `r = 1, 2, 3` | executed: six exact pairs, rank six | executed: the reach-one tori mod p; the family's form | proved, not executed: every reach and every `q` near `q₀` |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "At long wavelength the bond rotation and the coin rotation agree (block 65 N1.2), so the continuum identification stands."
  - *Reply:* At leading order it does, and block 64 T2 is a leading-order statement. T3 says there is no exact local tie at any reach. A lattice formulation that keeps the coin's rotation unfelt by stationary content must therefore carry it separately.
- *Objection:* "`β` free is a step back."
  - *Reply:* Only under block 64's one-step coupling. The landed two-step programme sources the symmetric member without a bond torque (blocks 120 and 136), so `β = 1` is not traded against balance there.

### N8 — Cross-cycle echo
- Block 64: `β = 1` from continuum blindness; the bond torque as a conditional obstruction.
- Block 65: the coin's rotation; bond and coin rotations differ.
- #8659 and #9047: two particular ties fail.
- #8853 and #9215: all ties at reaches one and two.
- Blocks 120 and 136: the two-step momentum sources the symmetric member and has a symmetric stress.
- This note: every reach under the one-step coupling, and what that coupling leaves for the strains' energy.

## Falsifiers

- A local linear tie that is not a relabelling, with `T†J = 0` at every site for every bounded stationary state.
- A pair of equal energy near `q₀` at which the six continued symbols are dependent for every nearby choice.
- A member of block 64's family off the blind ratio that is independent of the bond rotations.

## Boundaries and non-claims

- Identity frame, uniform rates, first order in the strains and rotations. Linear local ties.
- T4 is in continuum symbols at leading order in the wave vector. No lattice member is exhibited.
- The walk, the coupling, the ties and the family are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 63, 64 and 65 (landed), quoted.
- Named standard imports, at definition level:
  - the implicit function theorem;
  - continuity of determinants;
  - unique factorisation of polynomials in several variables;
  - trigonometric polynomials vanishing on an open set;
  - ranks over a field, and a ring map into a finite field (`rank over the field ≥ rank mod p`);
  - exact symbolic and integer arithmetic.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.**
  - T2 and T3 for every reach are the supervisor's own, unrefereed.
  - The torus cases at reaches one and two are from #8853 and #9215, refereed in #8977 and #9320 by `grok-4.6`.
  - T4 is #8853 part (b), refereed in #8977.
  - The runner is new, and ports the probes' reach-one torus system with integer arithmetic.
- **Before writing.** Origin was re-fetched. Blocks 63, 64 and 65 were read as landed. The own prior-art check covered memory, the held branches, open PRs, main and the probes' attempts on this task. #8659 and #9047 (two ties) were noted in the block 65 corrigendum only.
- **Correction before any PR (second version).** The first version presented the fork as a new third-column item. It missed the landed blocks 120, 136 and 138, which moved the source to the two-step momentum and its symmetric stress. There the fork does not arise. The theorems are unchanged; the fork is now scoped to block 64's one-step coupling.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_no_local_tie_makes_the_coins_rotation_a_bond_strain_2026_09_27.py
```

Expected: `TOTAL: PASS=23 FAIL=0`.
