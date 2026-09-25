---
claim_id: admissibility_rule_the_members_pull_carries_the_velocity_terms_that_give_pull_bound_pairs_weight_one_along_every_axis_at_first_order_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "For the explicitly supplied continuum quadratic action, positive K and alpha, conserved sources and\
  \ nonzero spatial momentum: the generic nonzero-frequency exchange formula requires omega\xB2 different from p\xB2\
  . The static clock formula is separate. With supplied spinless point-body stress and a conservative near-zone\
  \ prescription, the displayed order-v\xB2 velocity-dependent interaction gives W=1 through the first weak-binding\
  \ order using tensor virial averages. No finite response at the wave pole, nonlinear completion, lattice result\
  \ or physical gravity identification is established."
upstream_dependencies:
- admissibility_rule_one_light_cone_exactly_on_the_lattice_the_two_step_content_meets_the_members_identity_for_every_state_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
- admissibility_rule_one_light_cone_from_the_source_link_the_walkers_smooth_states_meet_the_members_identity_at_leading_order_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
- admissibility_rule_the_books_admit_one_rest_energy_the_staggered_mass_keeps_them_exactly_so_massive_content_meets_the_member_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
- admissibility_rule_the_walk_carries_an_exact_boost_charge_its_brackets_give_the_fall_weight_and_an_exactly_kept_angular_momentum_with_the_face_spin_bounded_theorem_note_2026-09-25
- admissibility_rule_two_step_content_keeps_symmetric_books_where_the_member_keeps_its_fields_and_a_bond_shift_keeps_every_constraint_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
runner: scripts/admissibility_rule_the_members_pull_carries_the_velocity_terms_that_give_pull_bound_pairs_weight_one_along_every_axis_at_first_order_2026_09_25.py
---

# Conditional quadratic exchange and first weak-binding curvature of a supplied two-body action

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** bounded-support (exact at first order in 1/K and order v² within the landed member, with block 136's shift supplied and blocks 134–136, 139 and 140 as landed; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note studies the expressly supplied model and only the conditional scope recorded in its claim_scope and Landing review boundary; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

For the explicitly supplied continuum quadratic action, positive K and alpha, conserved sources and nonzero spatial momentum: the generic nonzero-frequency exchange formula requires omega² different from p². The static clock formula is separate. With supplied spinless point-body stress and a conservative near-zone prescription, the displayed order-v² velocity-dependent interaction gives W=1 through the first weak-binding order using tensor virial averages. No finite response at the wave pole, nonlinear completion, lattice result or physical gravity identification is established.


The member's clock obeys a constraint (block 101), so the clock's pull acts at once, like a potential. A pair held together only by a pull that acts at once does not move as one body. Its weight, `W = E₀ ∂²E/∂P²` at rest, differs from one by about its binding fraction (probes refill o). Probes refill r asks whether the member's whole pull, carried by the clock, the shift and the lengths, restores weight one. It does, at first order.

- **T1: the member is the comparator's quadratic action.** At the closing ratio, with block 136's shift, the member's Lagrangian is `K` times the second-order part of the comparator's action in its lapse-and-shift form, up to a total derivative, if and only if `α = K/4`. So the number the books fix (blocks 134–136) is the comparator's normalization, with `K` in the place of `1/(16πG)`.
- **T2: the exchange.** Take sources that keep the books. At `α = K/4` the member's equations have a solution at nonzero frequency away from the wave pole (`omega² != p²`, `p != 0`). A second source then feels `(1/(2K))[T′·T − ½T′T]/(p² − ω²)`, where `T` is the four-by-four array of energy, momentum and stress, contracted with signature `(−,+,+,+)`. This holds with or without the shift. For positive `α != K/4`, a nonzero-frequency source with nonzero energy density has no solution: the one condition is `(K − 4α)e/(4α) = 0`.
- **T3: the pull between two slow bodies.** Two compact bodies with rest energies `m₁` and `m₂`, at separation `r` along `n`, feel, to order `v²`, `L = (m₁m₂/(16πKr))[1 + (3/2)(v₁² + v₂²) − (7/2)v₁·v₂ − ½(n·v₁)(n·v₂)]`.
- **T4: pairs bound by the member move as one body.** Take any pull `(k/r)[1 + a(v₁² + v₂²) + bv₁·v₂ + c(n·v₁)(n·v₂)]`.
  - A bound pair's weight along a direction `P̂` is `W = 1 + [(1 + 2(2a + b))⟨U⟩ + (1 + 2c)⟨U_P̂⟩]/M`, with `U = −k/r`, `U_P̂ = −k(n·P̂)²/r` and `M = m₁ + m₂`.
  - So `W = 1` along every axis, for every bound state, if and only if `2a + b = −½` and `c = −½`. These are exactly the pulls that a long-wave change of velocity leaves unchanged.
  - The member's pull has `a = 3/2`, `b = −7/2` and `c = −½`. Pairs it binds have weight one along every axis, at first order in the binding.
  - The clock's pull alone (`a = b = c = 0`) gives `W = 1 + (⟨U⟩ + ⟨U_P̂⟩)/M`, which is below one.
- **T5: without the shift.** `α = K/4` is still required, and the exchange, the pull and the weight are unchanged. What changes is that the member gains lengths that drift linearly in time by a transverse relabelling. They carry a conserved residual of the momentum constraint and act on moving content like a fixed vector potential.

In plain terms: push a pair that is held together by a pull acting at once, and it responds as if it weighed less than its energy, because the binding energy does not ride along with the motion. The member's pull is more than the clocks' instantaneous tug. Moving bodies also pull on each other through the member's shift and lengths, with strengths set by the same number `α = K/4` that gives the member's waves the walker's top speed. Those velocity terms are exactly the ones that make a bound pair's momentum equal its energy times its velocity. So a pair bound by the member moves as one body, at least to first order in how tightly it is bound. Dropping the shift does not change this pull. It only lets the member hold frozen twists of its lengths, which would push sideways on anything moving through them.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-25.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The member, its shift, its kinetic term, the source link and the bodies are supplied clauses. Nothing is adopted.
- **The member** (blocks 62 and 101 as landed), at the closing ratio `β = −α` (blocks 112, 124 and 129) and unit rate `w̄ = 1`, written in position space at long wavelength (`p_j = 2 sin(k_j/2) → k_j`):
  - `L = α[tr(Ḣ²) − (tr Ḣ)²] + K(uR₁ + R₂) − eu + N·P + ½Σ Θ_ij h_ij`;
  - `Ḣ_ij = ∂_t h_ij − ∂_iN_j − ∂_jN_i`;
  - `R₁ = ∂_i∂_j h_ij − ∇² tr h` and `R₂ = −¼(∂_k h_ij)² + ½(∂_i h_ik)(∂_j h_jk) − ½(∂_i h_ij)∂_j tr h + ¼(∂_k tr h)²`.
  - The bond shift `N` and its coupling are block 136's, supplied there and here. As landed, block 136 states that the shift preserves initially satisfied nonzero-mode lapse and shift constraints for free-walk sources iff `α = K/4`, and that the conserved-source quadratic action is invariant under time-dependent relabellings up to a boundary term. T2 uses only that form. Block 136 writes them in plane-wave form with its own sign for `N`. In position space, as here, the coupled action keeps relabellings in time as a symmetry only with `+N·P`: with the opposite sign no source that keeps the books has a solution (the runner's mutation `shift_coupling_sign_flipped`).
- **Sources that keep the books.** Energy density `e`, momentum density `P` and symmetric stress `Θ` with `∂_t e = −∇·P` and `∂_t P_j = −∂_iΘ_ij`. Blocks 135 and 136 show the walker's two-step content keeps these books, with `P = P^B` and `Θ` the symmetric stress. `T` is the array `T^{00} = e`, `T^{0i} = P_i`, `T^{ij} = Θ_ij`, contracted with `η = diag(−1, 1, 1, 1)`.
- **Slow compact bodies (premise).** At long wavelength a slow compact body's content, integrated over its extent, has the point form `e = mγ`, `P = mγv`, `Θ = mγ v⊗v` at its position, with `γ = (1 − v²)^{−1/2}`. This is the long-wave content of a walker packet with `E² = m² + k²` (block 139's staggered mass; block 140's long-wave limit). The face spin (block 138) is not included.
- **Bound pairs and weight.** Two bodies with free part `Σ_a −m_a(1 − v_a²)^{1/2}` and a pull `L_int`. A bound state here has finite virial moments, a valid weak-binding expansion with internal velocity squared of order binding energy divided by mass, and a twice differentiable rest energy branch (with degenerate perturbation resolved when necessary). It is a stationary state of the relative motion under `H₀ = q²/(2μ) + U(r)`, or a bounded orbit with time averages. Its weight along `P̂` is `W(P̂) = E₀ ∂²E/∂P²` at `P = 0` along `P̂`. This is refill o's weight, and block 142's `Hess(E²/2)` at rest.
- **The comparator (named only).** The action `(1/(16πG))∫N√γ(K_ijK^ij − K² + R)`, with `K_ij = (1/(2N))(∂_tγ_ij − D_iN_j − D_jN_i)`, in the lapse-and-shift form of Arnowitt, Deser and Misner. Its first-order two-body pull is that of Einstein, Infeld and Hoffmann. Both are used for comparison only.
- **Standard imports, named at definition level.**
  - The fundamental solution of the Laplacian in three dimensions: `1/p²` is `1/(4πr)`.
  - The small-frequency expansion of an exchange between slow sources.
  - First-order perturbation theory for the energy of a bound state, and the first-order Legendre transform.
  - The vanishing of time averages (or stationary expectation values) of the time derivative of a bounded quantity: the virial argument.

## Theorem T1 — the member is the comparator's quadratic action

*Statement.* Let `γ_ij = δ_ij + h_ij`, the lapse be `1 + u` and the shift `N`. The second-order part of `N√γ(K_ijK^ij − K² + R)` is `¼[tr(Ḣ²) − (tr Ḣ)²] + uR₁ + R₂`, up to a total derivative. Hence the member at kinetic coefficients `(α, β)` equals `K` times it, up to a total derivative, if and only if `α = K/4` and `β = −α`.

*Proof.*
- `K_ij` is first order in the fields, and its first-order part is `½Ḣ_ij`. So its quadratic terms at second order are `¼[tr(Ḣ²) − (tr Ḣ)²]`, with `N√γ = 1` at zeroth order.
- The first-order part of `R` is `R₁` exactly (runner B1). So the lapse term at second order is `uR₁` plus the second-order part of `√γR`.
- The second-order part of `√γR` minus `R₂` averages to zero on every plane wave (runner B2). So its integral vanishes for every field, and the two actions agree. The wave vector is taken along one axis. Both densities are rotation-invariant contractions, so any other direction follows by rotating the amplitudes.
- The kinetic coefficients enter the difference independently, and the only match is `α = K/4`, `β = −α` (runner B3). ∎

So `K` plays the part of `1/(16πG)`. The closing ratio `β = −α` found in blocks 112, 124 and 129 is forced again by the match.

## Theorem T2 — the exchange

*Statement.* Let the source keep the books, and take `α = K/4`.
- (a) For `ω != 0`, `p != 0` and `omega² != p²`, the member's equations with source `(e, P, Θ)` have a solution, with the shift and without it (`N ≡ 0`, no `N·P` term).
- (b) The pairing `−e′u + N·P′ + ½Θ′·h` of a second such source with that solution is `(1/(2K))[T̄′·T − ½T̄′T]/(p² − ω²)`. It does not depend on the relabelling freedom, and it is the same with and without the shift.
- (c) At `α ≠ K/4`, with or without the shift, there is no solution unless `e = 0`. The one consistency condition is `(K − 4α)e/(4α) = 0`.
- (d) For static content the clock is `u = −e/(4Kp²)`, block 101's law at unit rate.

*Proof.* Exact linear algebra on the plane-wave form of `L` (runner C1–C4). The wave vector is along one axis, by rotation invariance.
- With the shift, the plane-wave matrix at `α = K/4` is hermitian of rank 6 of 10. The four missing directions are the relabellings: three in space and one in time.
- Without the shift it has rank 6 of 7. The missing direction is a relabelling in time together with its compensating relabelling in space.
- Sources that keep the books are orthogonal to these directions, so a solution exists and the pairing does not see them.
- At `α ≠ K/4` the relabelling in time is deformed to `δu = (4α/K)ξ̇⁰`, `δN = −∇ξ⁰` (without the shift: `δu = (4α/K)ξ̇⁰`, `δh = 2∇∇Ξ` with `Ξ̇ = ξ⁰`). In both cases a source must obey `(4α/K)∂_t e + ∇·P = 0`, and with the books this forces `∂_t e = 0`. ∎

At `α = K/4` the exchange is `(T′·T − ½T′T)/(p² − ω²)`. It travels at the walker's top speed, and its form is the same in every frame moving at constant velocity. T3 and T4 use exactly these two facts.

The inverse requires a boundary prescription. T3 uses the time-symmetric conservative near-zone expansion with homogeneous radiative solutions set to zero, `|omega|/|p|` small in the potential sector. At `omega²=p²` a transverse trace-free stress provides a counterexample to finite monochromatic solvability. Conservation alone does not remove this pole.

## Theorem T3 — the pull between two slow bodies

*Statement.* Take two compact bodies (premise) with rest energies `m₁` and `m₂`, positions `x₁` and `x₂`, velocities `v₁` and `v₂`, `r = |x₁ − x₂|` and `n = (x₁ − x₂)/r`. At first order in `1/K` and to order `v²`, up to a total time derivative,

`L_int = (m₁m₂/(16πKr))[1 + (3/2)(v₁² + v₂²) − (7/2)v₁·v₂ − ½(n·v₁)(n·v₂)]`.

*Proof.*
- The cross term of the exchange (T2) between the bodies is `(1/(2K))∫∫[T₁·T₂ − ½T₁T₂] G`, where `G` is the kernel of `1/(p² − ω²)`.
- Exactly, `1/(p² − ω²) = 1/p² + ω²/p⁴ + ω⁴/(p⁴(p² − ω²))`. The last term is of order `v⁴` between slow bodies. `1/p²` is `1/(4πr)`, and `1/p⁴` is `−r/(8π)` because `∇²r = 2/r` (runner D2). `ω²` acts as `∂_{t₁}∂_{t₂}` on the two worldlines.
- *The part that acts at once.* For point bodies, `T₁·T₂ − ½T₁T₂ = m₁m₂γ₁γ₂(1 − v₁·v₂)² − ½m₁m₂/(γ₁γ₂) = (m₁m₂/2)[1 + (3/2)(v₁² + v₂²) − 4v₁·v₂]` plus terms of order `v⁴` (runner D1).
- *The delay.* At leading order the bodies enter with weight `m₁m₂/2`, and `∂_{t₁}∂_{t₂}|x₁(t₁) − x₂(t₂)| = −[v₁·v₂ − (n·v₁)(n·v₂)]/r` (runner D3). This part contributes `(m₁m₂/(16πKr))·½[v₁·v₂ − (n·v₁)(n·v₂)]`.
- Add the two parts (runner D4). ∎

## Theorem T4 — pull-bound pairs have weight one along every axis

*Statement.* Take `L = Σ_a −m_a(1 − v_a²)^{1/2} + (k/r)[1 + a(v₁² + v₂²) + bv₁·v₂ + c(n·v₁)(n·v₂)]`, at first order in `k` and order `v²` in the bracket. Take a bound state, and write `M = m₁ + m₂`, `μ = m₁m₂/M`, `U = −k/r`, `U_P̂ = −k(n·P̂)²/r` and `T_P̂ = (P̂·q)²/(2μ)`. Then:
- (a) `W(P̂) = 1 + [⟨U⟩ − 2⟨T_P̂⟩ + 2(2a + b)⟨U⟩ + 2c⟨U_P̂⟩]/M`, up to terms of order `v⁴` and `k²`;
- (b) `2⟨T_P̂⟩ = −⟨U_P̂⟩`, so `W(P̂) = 1 + [(1 + 2(2a + b))⟨U⟩ + (1 + 2c)⟨U_P̂⟩]/M`;
- (c) `W = 1` along every axis, for every bound state, if and only if `2a + b = −½` and `c = −½`;
- (d) under the long-wave change of velocity, `δx_a = −εt + v_a(ε·x_a)`, the Lagrangian changes by `dF/dt − (k/r)[(2a + b + ½)ε·(v₁ + v₂) + (c + ½)(n·ε)(n·(v₁ + v₂))]`, through the order kept, with `F = Σ_a m_a(v_a²/2 − 1)(ε·x_a) + (k/(2r))ε·(x₁ + x₂)`. So the pull is unchanged by it, up to a total derivative, exactly when (c) holds;
- (e) the member's pull (T3: `k = m₁m₂/(16πK)`, `a = 3/2`, `b = −7/2`, `c = −½`) meets (c). Pairs it binds have weight one along every axis at first order in the binding;
- (f) the clock's pull alone (`a = b = c = 0`) gives `W(P̂) = 1 + (⟨U⟩ + ⟨U_P̂⟩)/M < 1`:
  - for a circular orbit, `1 + ⟨U⟩/M` across the orbit's plane and `1 + (3/2)⟨U⟩/M` within it;
  - for an isotropic state, `1 + (4/3)⟨U⟩/M`;
  - for equal masses on a line, before the virial step, `1 + ⟨U⟩/(2m) − ⟨T⟩/m`, which is refill o's expectation.

*Proof.*
- (a) Changing from velocities to momenta at first order gives `H = Σ_a[m_a + p_a²/(2m_a) − p_a⁴/(8m_a³)] − k/r − (k/r)[a(p₁²/m₁² + p₂²/m₂²) + b p₁·p₂/(m₁m₂) + c(n·p₁)(n·p₂)/(m₁m₂)]`, up to higher orders.
  - Write `p₁ = (m₁/M)P + q` and `p₂ = (m₂/M)P − q`. The `P²` part of the corrections is `(P²/(2M))·{−(T + 2T_P̂)/M + (2/M)[(2a + b)U + cU_P̂]}` (runner E1).
  - By first-order perturbation theory, `E(P) = E₀ + (P²/(2M))(1 + ⟨{…}⟩)` up to terms odd in `P` and terms of order `P⁴`, with `E₀ = M + ⟨T + U⟩`. For an isolated or appropriately diagonalized branch, the odd-in-P perturbation contributes only beyond the retained weak-binding order; a uniform estimate as a spectral gap closes is not claimed. This is velocity/binding power counting, not an expansion in k at a fixed Coulomb bound state.
  - So `W = E₀(1 + ⟨{…}⟩)/M`, which expands to (a).
- (b) The bracket of `2(e·x)(e·q)` with `H₀` is `2(e·q)²/μ − 2k(e·x)²/r³` (runner E2). Its average vanishes in a bound state, since it is the time derivative of a bounded quantity.
- (c) For a circular orbit, `⟨U_P̂⟩ = 0` across the plane and `⟨U⟩/2` within it. So the two coefficients must vanish separately.
- (d) Runner E4, with `v` counted as `λ`, `k` and the accelerations as `λ²`, through `λ³`. The free part's change is an exact total derivative. The clock's pull contributes `−(k/2r)[ε·(v₁ + v₂) + (ε·n)(n·(v₁ + v₂))]`, and the velocity terms' change under `δv = −ε` contributes the rest.
- (e) and (f): substitution (runner E3 and E5). ∎

(c) and (d) are the same two conditions. A pull meets them exactly when the pair's momentum is its energy times the velocity of its centre of energy, which is what weight one means.

## Theorem T5 — without the shift

*Statement.*
- (a) Without the shift, moving content still requires `α = K/4` (T2(c)). At `α = K/4` the exchange (T2(b)) is unchanged at nonzero frequency away from the wave pole (`omega² != p²`, `p != 0`), so T3 and T4 are unchanged.
- (b) Without the shift, `C_j = 4α∂_i(ḣ_ij − δ_ij tr ḣ) + P_j` is conserved. With the shift, the shift's equation sets it to zero, with `Ḣ` in place of `ḣ`.
- (c) Without the shift, `h_ij = t(∂_iξ_j + ∂_jξ_i)`, `u = 0` solves the source-free member for every field `ξ(x)`. Its residual is `C = K(∇²ξ − ∇(∇·ξ))`, which vanishes only for longitudinal `ξ`. With the shift, `N = ξ` makes it a pure relabelling (`Ḣ = 0`).
- (d) Content that keeps its books feels such lengths as `−ξ·P`, up to total derivatives. For a body this is `−mγ v·ξ(x)`: a fixed vector potential, whose curl pushes moving bodies across their velocity.

*Proof.*
- (a) T2.
- (b) The divergence of the lengths' equation is `∂_t[4α∂_i(ḣ_ij − δ_ij tr ḣ) + P_j] = 0`. The curvature terms drop out because they are unchanged by relabellings, and the stress term uses the books.
- (c) `h` is linear in `t`. The only time derivatives in the member's equations are the lengths' second derivatives, and the static part of the equations annihilates a relabelling (runner C5). The residual is then direct (runner C5).
- (d) `½Θ_ij h_ij = d/dt(t ξ·P) − ξ·P + ∂_i(tΘ_ij ξ_j)` by the books (runner C6). ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 101 (landed): the clock's law is a constraint that acts at once; block 142 (open): pairs bound without velocity terms do not move as one body; whether the member's whole pull binds pairs that do (probes problem the-members-velocity-dependent-pull, refill r)"
source_of_blocker_text: block 101 (landed); block 142 (open); probes refills o and r
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the passive weight of a pull-bound pair (second order in 1/K, which needs the member's cubic order, not supplied); spin couplings; the exchange on the lattice beyond long wavelength; an other-family referee"
conditional_surface_status: "long wavelength; first order in 1/K; order v^2; slow compact bodies in point form; block 136's shift supplied"
hypothetical_axiom_status: "the member, the shift, its coupling and the bodies' point form are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 62: the member's curvature terms, which are the quadratic spatial terms of Fierz and Pauli.
  - Block 101: the member's quadratic action; the clock is a constraint.
  - Blocks 112, 124 and 129: the closing ratio `β = −α`.
  - Blocks 134 and 135: one light cone, `α = K/4`.
  - Block 136: symmetric books; with a bond shift the initially satisfied nonzero-mode constraints are preserved iff `α = K/4`.
  - Block 139: the staggered mass.
  - Block 140: the exact boost charge and its long-wave limit.
- **Opened, not landed.** Block 142 (PR #9227): pairs bound under one record per site do not move like records; the weight `Hess(E²/2)`.
- **Probes.** Refill r's problem `the-members-velocity-dependent-pull` poses (a)–(c) of this note; refill o's `the-inertia-of-a-static-binding` poses the static expectation. Neither has an attempt yet.
- **In the literature.**
  - The lapse-and-shift form of the comparator's action (Arnowitt, Deser and Misner).
  - The first-order two-body pull with velocity terms: Einstein, Infeld and Hoffmann. The analogous electromagnetic pull is Darwin's.
  - The inertia of a bound, stressed system (Laue), and the condition that a two-body pull be unchanged by a change of velocity at order `v²`, both standard in the theory of two-body motion.
  - The fall of a body's own binding energy in an outside field is Nordtvedt's question. It needs second order in the coupling and is not treated here.
  - All of these are reference only.
- **New here:**
  - T1: the books' `α = K/4`, with block 136's shift, is exactly the comparator's quadratic lapse-and-shift action, with `K` in the place of `1/(16πG)`.
  - T2: the member's exchange for sources that keep the books, from its own equations, with and without the shift; the obstruction at other `α` in exchange form.
  - T3: the member's pull between two slow bodies to order `v²`.
  - T4: the weight of a bound pair for any first-order pull, its two conditions, and their identity with invariance under a change of velocity. The member's pull meets them; the clock's pull alone gives `W < 1` along every axis (refill o's line formula is its one-dimensional case).
  - T5: without the shift the pull is unchanged, and the drifting relabellings act on moving content as a fixed vector potential.
- **Provenance.** This is the supervisor's own derivation, in the same model family as the probes workers. No other model family has refereed it.

## Exact target and obligation graph

Target: refill r's (a)–(c). What the member's pull between two slow bodies is at first order and order `v²`, whether it gives pull-bound pairs weight one, and what changes without the shift. The obligations are:
- (O1) the member against the comparator's quadratic action (T1);
- (O2) the exchange, with and without the shift, and at other `α` (T2);
- (O3) the pull between point bodies (T3);
- (O4) the weight of a bound pair for any first-order pull, and the boost condition (T4);
- (O5) the member without the shift (T5).

T1–T5 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- at any `α ≠ K/4`, with or without the shift, the member has no solution for content whose energy density changes;
- a pull without velocity terms never gives a bound pair weight one (its `W` is below one along every axis).

### N1 — Routes by which the sentences could fail or mislead
1. *Order.* Everything is at first order in `1/K` and order `v²`. At second order the member's own energy would have to pull, which needs its cubic order. That is not supplied.
2. *Long wavelength.* The lattice member (`p_j = 2 sin(k_j/2)`) and the walker's lattice kinematics (block 140's `cos 2k`) add corrections at short wavelength. The separation is taken large against the lattice spacing.
3. *Point form.* Bodies are compact and slow, with no spin couplings.
4. *The shift.* Block 136's shift is supplied. T5 shows the pull does not need it, but `α = K/4` is needed either way.
5. *Imports.* The small-frequency expansion, the fundamental solution and first-order perturbation theory are standard and named.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied member, shift, source link and bodies, and the named imports.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 62, 101 (landed) | the member's action | yes (restated) |
| blocks 112, 124, 129 (landed) | the closing ratio | yes (restated; also forced by T1) |
| blocks 134, 135, 136 (landed) | `α = K/4`; the books; the shift | yes (restated; T2 re-derives the `α` condition) |
| blocks 139, 140 (landed) | the walker's long-wave content and change of velocity | yes (premise of the point form) |
| blocks 142 (open), refills o and r | the weight and the question | no (comparison) |
| the comparator | comparison only | no |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "at first order the member's pull gives pull-bound pairs weight one along every axis; the clock's pull alone does not; no other `α` carries moving content" | executed: the curvature terms against the comparator's on every plane wave | executed: the plane-wave equations solved for every conserved source in the stated nonresonant domain | executed: the obstruction at other `α`; the drifting relabellings | executed: the point-body pull, the weight formula, the virial bracket, the boost remainder | long wavelength; first order in `1/K`; order `v²` |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository. It is not used: `α = K/4` comes from blocks 134–136 and is re-derived in T2(c). `scale_reference_primitive` is not used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "This is the comparator's first-order pull, rederived. Nothing is learned about the lane."
  - *Reply:* The lane's member was built from records and walkers, and its `α` was fixed by the books, not by matching the comparator. T1 shows those choices land exactly on the comparator's quadratic action, and T4 shows the velocity terms are what make bound pairs move as one body.
  - It also answers two open questions. Block 142's contact binding cannot give weight one, and neither can any pull without velocity terms. And the shift is not needed for the pull (T5).

### N8 — Cross-cycle echo
- Block 101: the clock is a constraint.
- Block 142: bound pairs under one record per site do not move like records.
- Refills o and r: the static expectation and the question.
- This note: the member's whole pull gives pull-bound pairs weight one at first order; the clock's pull alone does not.

## Falsifiers

- A source that keeps the books for which the member's equations at `α = K/4` have no solution, or whose exchange differs from T2(b).
- A bound state of the member's pull whose weight differs from one at first order in the binding.
- A pull without velocity terms that gives some bound pair weight one.
- An error in the runner's plane-wave algebra, series or brackets.

## Boundaries and non-claims

- First order in `1/K`, order `v²`, long wavelength, slow compact bodies in point form, no spin couplings.
- The weight is inertia (`E₀ ∂²E/∂P²`). How a pull-bound pair falls in an outside clock gradient, including the fall of its binding energy, needs second order in `1/K` and the member's cubic order. It is not treated.
- The shift is supplied. No landed clause supplies it (probes #9226, unrefereed).
- Not refereed by another model family.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 62, 101, 112, 124, 129, 134, 135, 136, 139 and 140 (landed), restated. Block 142 (open), restated.
- Named standard imports, at definition level:
  - exact symbolic arithmetic;
  - the fundamental solution of the Laplacian in three dimensions;
  - the small-frequency expansion of an exchange between slow sources (the near zone);
  - first-order perturbation theory for a bound state's energy, and the first-order Legendre transform;
  - the virial argument: the time average of the time derivative of a bounded quantity vanishes.

## Review record — original author history

- **Who and when.** Supervisor-run block, the ninety-second since the source-link direction opened; 2026-09-25.
- **Provenance.** The supervisor's own derivation (Claude Opus 5.5), with exact checks by its own runner. It is not refereed by another model family.
- **Before writing.** The own prior-art check (memory, open PRs, probes attempts, main) found no velocity-dependent pull, no identification of `K` with the comparator's `1/(16πG)`, and no attempt on refills o or r. The one landed mention of Infeld and Hoffmann (2026-09-21, the fall owed by the ledger) cites them as prior art only for equations of motion following from field equations.
- **Checks during the work.**
  - A first comparison with the comparator used the full second-order density with position-dependent exponentials and took minutes. The runner uses plane waves with a single Laurent symbol, the wave vector along one axis, and the first-order extrinsic curvature (T1's first step). It runs in seconds.
  - The first expectation was that dropping the shift would change the pull. The exact exchange (runner C2) shows it does not at nonzero frequency away from the wave pole (`omega² != p²`, `p != 0`). What changes is confined to the drifting relabellings (T5).
  - The sign of the shift's coupling was fixed by requiring relabellings in time to be a symmetry of the coupled action (see Premises). Block 136's plane-wave convention differs by that choice of sign.
- **After opening.** Blocks 111–141 landed on main the same day. The citations now point to the landed text. Block 136's landed scope (initially satisfied nonzero-mode constraints; invariance of the conserved-source quadratic action) is the form T2 uses.
- **Independence.** Mutation census: seven mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_members_pull_carries_the_velocity_terms_that_give_pull_bound_pairs_weight_one_along_every_axis_at_first_order_2026_09_25.py
```

Expected: `TOTAL: PASS=25 FAIL=0`.

## Landing review boundary

The alpha obstruction concerns nonzero-frequency energy density, with positive alpha and K. It is necessary, not a claim that every exceptional resonant source is solvable when e=0. Static zero modes need separate boundary data. The no-shift exchange uses the same particular conservative solution; arbitrary conserved constraint residuals add background fields, so they are not silently fixed by source conservation. Point-body stress is a supplied effective model, not derived for arbitrary compact lattice composites. W is an inertial energy-curvature diagnostic; passive response is separate.

This same-session landing review is independent of the original author and applies no audit verdict. The original branch and complete campaign sources remain recoverable. Historical source titles and quoted block numbers are identifiers, not additional theorem scope.

## Dependencies

The following actual sources are used only within their current narrowed scopes; the equations explicitly supplied above remain conditional.

- [Source 9193](ADMISSIBILITY_RULE_ONE_LIGHT_CONE_FROM_THE_SOURCE_LINK_THE_WALKERS_SMOOTH_STATES_MEET_THE_MEMBERS_IDENTITY_AT_LEADING_ORDER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [Source 9195](ADMISSIBILITY_RULE_ONE_LIGHT_CONE_EXACTLY_ON_THE_LATTICE_THE_TWO_STEP_CONTENT_MEETS_THE_MEMBERS_IDENTITY_FOR_EVERY_STATE_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [Source 9196](ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [Source 9201](ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_THE_STAGGERED_MASS_KEEPS_THEM_EXACTLY_SO_MASSIVE_CONTENT_MEETS_THE_MEMBER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [Source 9203](ADMISSIBILITY_RULE_THE_WALK_CARRIES_AN_EXACT_BOOST_CHARGE_ITS_BRACKETS_GIVE_THE_FALL_WEIGHT_AND_AN_EXACTLY_KEPT_ANGULAR_MOMENTUM_WITH_THE_FACE_SPIN_BOUNDED_THEOREM_NOTE_2026-09-25.md)
