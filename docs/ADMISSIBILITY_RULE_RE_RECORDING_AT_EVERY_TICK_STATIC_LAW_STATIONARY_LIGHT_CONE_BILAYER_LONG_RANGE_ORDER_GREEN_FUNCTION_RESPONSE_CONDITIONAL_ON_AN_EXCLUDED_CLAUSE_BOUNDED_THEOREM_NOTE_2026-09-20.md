---
claim_id: admissibility_rule_re_recording_at_every_tick_static_law_stationary_light_cone_bilayer_long_range_order_green_function_response_conditional_on_an_excluded_clause_bounded_theorem_note_2026-09-20
claim_type: bounded_theorem
claim_scope: "CONDITIONAL on a supplied clause that the axioms memo excludes (a record at every site of Z^3 at every tick, each new record drawn from the covariant rule given the previous tick's records on a symmetric stencil; the memo says a site never carries more than one record). On finite even tori, for a symmetric positive weight: (T1) with the axioms' nearest-neighbour stencil, asynchronous re-recording is reversible for the static law of block 01, which is its only stationary law; synchronous re-recording splits into two independent alternating chains whose space-time checkerboard has the static law as a stationary law; (T2) with the site's own previous record added to the past (seven-site stencil) the synchronous chain is reversible for pi(s) prop. to prod_x Z_x(s), pi is one layer of the pair law on the doubled graph, and the doubled graph is the bilayer (Z/L)^3 x K_2 under (x, a) -> (x, a + |x| mod 2); (T3) for the sphere menu with weight e^{beta s.s'}: <|m_0|^2>_pi >= 1 - (3/(2 beta))(G_L + H_L), G_L = N^-1 sum_{k != 0} 1/E(k), H_L = N^-1 sum_k 1/(14 - E(k)), E(k) = 6 - 2 sum_j cos k_j, by reflection positivity of the bilayer (bond planes and the layer swap), the domination of the twisted partition function, the infrared bound <|s^_+(k)|^2> <= 3N/(beta E(k)) and the sum rule; with G_L <= I_0 + (3/(8L))(1 + log(L/2))^2 + pi^2/(16L) and |H_L - I_2| <= (3/4)^L/2 this gives long-range order on large even tori for beta > beta_0 = (3/2)(I_0 + I_2), and beta_0 < 5914/10000 given block 22's bracket 3 I_0 < 76/100 (open PR #8156, restated); (T4) the linearized seven-site law has static response 7/E(k) to a persistent source (seven times the lattice Green function) and equal-tick covariance (7 sigma^2/2)(1/E + 1/(14 - E)), with response/covariance = (1 + phi)/sigma^2, phi = 1 - E/7; the six-site law has response 6/E(k) and a second pole at (pi,pi,pi). EXECUTED, not claimed: the sphere law's plateau (none at beta = 1/2, 0.41 at beta = 3/5, 0.762-0.767 at beta = 1 for L = 16-48), the potential around a persistent field source at 0.96-0.99 of the linear prediction and symmetric, and the agreement of the chains' plateaus with an independent sampler of the equilibrium laws to 0.001. The clause is not adopted and no statement is made that the axioms permit it."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_re_recording_at_every_tick_static_law_stationary_bilayer_ferromagnet_long_range_order_green_function_response_2026_09_20.py
---

# If records re-form at every tick: the static law is the stationary law, the light-cone variant is one layer of a bilayer ferromagnet with long-range order, and a persistent source is surrounded by the lattice Green function (conditional on a clause the axioms exclude)

**Date:** 2026-09-20
**Type:** bounded_theorem
**Status:** bounded-support (exact under the supplied clause; the nonlinear law's memory and source potential executed, not claimed; the clause contradicts the axioms memo as written and is not adopted; unaudited)

## Result up front

This note is conditional on a clause that the axioms memo excludes: it supposes a record at every site at every tick, while the memo says that a site never carries more than one record and that records are permanent. Under the memo as written every site is recorded once; blocks 13, 26 and 35 (PRs #8147, #8170, #8180) showed that a continuous menu then loses its memory and that no three-dimensional Green-function kernel appears. This note computes what the opposite clause would give, so that the choice can be made knowing its price and its yield. It makes no claim that the axioms permit the clause.

**The clause.** At every tick `t = 0, 1, 2, …` every site `x ∈ Z³` carries a record `s_{(t,x)}`; records are permanent; the record at `(t+1, x)` is drawn from the covariant rule given the tick-`t` records on `x + N`, with `N` a symmetric stencil: the six nearest neighbours (`N₆`, the axioms' own neighbourhood) or those six and the site itself (`N₇`, a light-cone past). The asynchronous variant re-draws one site at a time from its six neighbours' current records.

1. **With the axioms' own rule the comparator is the stationary law (T1).** Asynchronous re-recording is reversible for the static law of block 01, and that law is its only stationary law on a finite window. Synchronous re-recording on an even torus splits into two independent alternating chains, and the space-time checkerboard of each (one parity class at tick `t`, the other at tick `t+1`) has the static law as a stationary law. Every static-law result of the campaign is then a statement about the stationary regime of a re-recorded lattice.
2. **The light-cone variant (T2).** With the site's own record in the past the synchronous chain is reversible for `π(s) ∝ Π_x Z_x(s)`, `Z_x` the rule's normalizer at `x`. Two consecutive ticks carry the pair law on the doubled graph, and for even `L` the doubled graph is the bilayer `(Z/L)³ × K₂`: two stacked cubic lattices with a rung at every site.
3. **Long-range order (T3).** For the sphere menu, `⟨|m₀|²⟩_π ≥ 1 − (3/(2β))(G_L + H_L)`, from the bilayer's reflections, the domination of the twisted partition function and the infrared bound `⟨|ŝ_+(k)|²⟩ ≤ 3N/(βE(k))`. On large even tori this is positive for `β > β₀ = (3/2)(I₀ + I₂)`, and `β₀ < 0.5914` given block 22's bracket for `I₀`.
4. **The response to a persistent source is the lattice Green function (T4).** In the linearized law the stationary mean around a source of strength `f` is `f · 7/E(k)`, seven times the lattice Green function, a one-over-distance potential with no drift and the full cubic symmetry; the equal-tick covariance is `(7σ²/2)(1/E + 1/(14 − E))`.
5. **Executed, not claimed.** The sphere law keeps no plateau at `β = 0.5`, keeps `0.41` at `β = 0.6`, and `0.767, 0.763, 0.762` at `β = 1` on planes of side `16, 32, 48`. The potential around a persistent field source is `0.96` to `0.99` of the linear prediction at distances `1` to `8`, symmetric to `10⁻⁵`. An independent sampler of the equilibrium laws reproduces both chains' plateaus to `0.001`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "block 35 (PR #8180): under the axioms' write-once formation the Green-function kernel of the gravity node does not appear; the probes' axioms map (ai/probes, 2026-09-20): a record at every tick is excluded by the memo's sentence that a site never carries more than one record; the owner's question whether records re-form"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "what a record-per-tick clause would give, exactly: the comparator as the stationary law of the axioms' own rule, a bilayer ferromagnet with long-range order above beta_0 < 5914/10000 for the light-cone variant, and a Green-function potential around a persistent source. Next: the owner's decision on the clause (an axiom change, not this campaign's); if wanted, the six-axis menu's ordered side for pi, the uniqueness region, and the infinite-volume states"
conditional_surface_status: "T1-T4 proved on finite even tori under the supplied clause, which contradicts the axioms memo as written and is not adopted; T3's numerical bound on beta_0 uses block 22's bracket (open PR #8156), restated; the nonlinear executed numbers are in the controls and not claimed; the standard mathematical imports named at definition level"
hypothetical_axiom_status: "the clause 'a record at every site at every tick' replaces the memo's 'a site never carries more than one record'; stated as a hypothesis only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", "Records form.", and, as the sentence this note's clause contradicts, "A site never carries more than one record; records are permanent." Block 01 (`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`, on `main`, proposed and unaudited) supplies the rule as a product of pair weights and the static law of a product rule.

Declared objects.
- **Window, menu, weight.** `Λ = (Z/L)³`, `L` even, `N = L³`. A menu `M` with a symmetric positive pair weight `W(s, s')`: the six axes with `W = p, q, r` for equal, opposite, orthogonal axes; or the sphere `S²` with `W = e^{β s·s'}` against the uniform probability measure. The static law is `μ(s) ∝ Π_{⟨xy⟩} W(s_x, s_y)`. The rule: a new record given the records on a finite set `F` has law `K(a | s_F) ∝ Π_{y∈F} W(a, s_y)`, with normalizer `Z(s_F)`.
- **The clause.** As stated under Result. `P(s, s') = Π_x K(s'_x | s_{x+N})` is the synchronous chain; `Z_x(s) := Z(s_{x+N})`.
- **The doubled graph** `Γ_N`: vertices `Λ × {0,1}`, an edge `(x,0)–(y,1)` whenever `y − x ∈ N`. The pair law `μ_Γ(s⁰, s¹) ∝ Π_{edges} W`. The **bilayer** `Λ × K₂`: two copies of the torus with their nearest-neighbour edges and a rung `(x,0)–(x,1)` at every site.
- **Sphere-menu objects.** `m₀ = N⁻¹ Σ_x s_{(x,0)}`; `E(k) = 6 − 2Σ_j cos k_j` on `k ∈ (2π/L)(Z/L)³`; `G_L = N⁻¹ Σ_{k≠0} 1/E(k)`; `H_L = N⁻¹ Σ_k 1/(14 − E(k))`; `I₀ = (2π)⁻³∫ 1/E`, `I₂ = (2π)⁻³∫ 1/(14 − E)`; `ŝ_±(k) = 2^{−1/2} Σ_{x,a} e^{−ik·x}(±1)^a s_{(x,a)}`.
- **The linearized law.** `θ_{t+1} = Pθ_t + ξ_t + f δ₀` on the torus, `P` the average over `x + N`, symbol `φ(k)`, noise variance `σ²` per component (for the sphere rule with `n` predecessors `σ² = A(nβ)/(nβ)`, `A(κ) = coth κ − 1/κ`, by block 26's computation, PR #8170, restated).

The static law, the pair law and the bilayer law are laws of the kind first written by Gibbs; the bilayer law with the sphere menu is the classical model of Heisenberg on that graph; the two-valued instance of the runner is the model of Ising. Asynchronous re-recording is the dynamics of Glauber for the static law. None of these names is used as authority.

## Prior art and what is new

Reversible probabilistic cellular automata and their pair laws on a doubled graph are classical; so is the proof of long-range order by reflection positivity, the domination of the twisted partition function and the infrared bound (Fröhlich, Simon, Spencer, 1976), which block 19 (PR #8153) re-proved for the campaign's static sphere law. What is new here: (i) the statement for the campaign: with the axioms' own rule, re-recording has the comparator as its stationary law (asynchronous) or as the law of its space-time checkerboard (synchronous), so blocks 01–24's comparator is the equilibrium of a re-recorded lattice and of nothing in the write-once reading; (ii) for the light-cone stencil, the identification of the doubled graph with the bilayer and the full proof of long-range order with the two bands `E` and `14 − E`, where the layer swap is the reflection that a first attempt lacked; (iii) the exact linear response `7/E(k)`; (iv) the executed potential around a source in the nonlinear law. The derivation attempts and the cross-family referee reports that led here are on the `ai/probes` branch (`probes/work/derive/lightcone-formation`, `lightcone-long-range-order`, `re-recording`, `axioms-and-the-event-lattice`); every statement used is re-proved below.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| T1 | asynchronous: reversible for the static law; synchronous on a bipartite window: the checkerboard has the static law | detailed balance at one site; conditional independence of a parity class | B |
| T2 | seven-site stencil: reversible for `Π Z_x`; pair law on the doubled graph; doubled graph = bilayer | the symmetric double product; an explicit bijection | C |
| T3 | `⟨|m₀|²⟩ ≥ 1 − (3/(2β))(G_L + H_L)`; the constants | reflections, domination, infrared bound, sum rule; exact series | C, D |
| T4 | response `7/E`, covariance `(7σ²/2)(1/E + 1/(14 − E))` | symbols; exact propagation on `3³` | E |

## Theorem T1 — the axioms' rule, re-recorded, has the comparator as its stationary law

**(a) Asynchronous.** Let `s, s'` differ only at `x`. The factors of `μ` not containing `x` cancel in `μ(s)/μ(s')`, leaving `Π_{y∼x} W(s_x, s_y)/Π_{y∼x} W(s'_x, s_y) = K(s_x | s_{∂x})/K(s'_x | s_{∂x})`, the normalizer being common. Hence `μ(s) K(s'_x | s_{∂x}) = μ(s') K(s_x | s_{∂x})`: re-recording `x` is in detailed balance with `μ`, and so is any mixture over sites chosen independently of the values. With `W > 0` the chain on a finite window reaches every configuration, so `μ` is its only stationary law. ∎

**(b) Synchronous.** On the even torus let `A, B` be the two parity classes. Sites of a class are pairwise non-adjacent, so `μ(s_A | s_B) = Π_{x∈A} K(s_x | s_{x+N₆})`: a synchronous step, restricted to `A`, is a draw from `μ(· | s_B)`. The tick-`(t+1)` records on `A` depend on the tick-`t` records on `B` only, so the chain is the product of two independent alternating chains `A_t → B_{t+1} → A_{t+2} → …`. In one of them, if the class-`B` records at tick `t` have law `μ_B` then (class `B` at tick `t`, class `A` at tick `t+1`) has law `μ_B(s_B) μ(s_A | s_B) = μ`, the class-`A` records have law `μ_A`, and the next pair has law `μ` again. So the space-time checkerboard has the static law as a stationary law, and the tick-`t` configuration has the stationary law `μ_A ⊗ μ_B`. ∎

## Theorem T2 — the light-cone stencil: reversibility, the doubled graph, the bilayer

For any symmetric stencil `N`, `π(s) P(s, s') ∝ Π_x Z_x(s) · Π_x [Π_{y∈x+N} W(s'_x, s_y)]/Z_x(s) = Π_x Π_{y∈x+N} W(s'_x, s_y) =: Φ(s', s)`. Since `W` is symmetric and `y ∈ x + N` exactly when `x ∈ y + N`, `Φ(s', s) = Φ(s, s')`: the chain is reversible for `π ∝ Π_x Z_x`. The law of two consecutive ticks at stationarity is `Φ` normalized, which is the pair law `μ_Γ` on the doubled graph, and summing over one layer gives `Π_x Z_x`, so `π` is a layer marginal of `μ_Γ`. For the sphere menu `Z_x(s) = sinh(β|S_x|)/(β|S_x|)`, `S_x = Σ_{y∈x+N} s_y`.

For `N = N₇` and `L` even put `f(x, a) = (x, a + |x| mod 2)`, `|x| = x₁ + x₂ + x₃`. The vertical edge `(x,0)–(x,1)` goes to the rung at `x`; the edge `(x,0)–(x ± e_j, 1)` goes to `(x, |x|)–(x ± e_j, |x|)`, a nearest-neighbour edge inside one layer, because `1 + |x ± e_j| ≡ |x|`. Counting `7N` edges on both sides, `f` is an isomorphism of `Γ_{N₇}` onto the bilayer, and layer `0` of `Γ` becomes one class of the bilayer's bipartition. For `N = N₆` the doubled graph is two disjoint copies of the torus, which is T1(b) again. ∎

## Theorem T3 — long-range order of the light-cone law for the sphere menu

**Reflections.** In bilayer coordinates take (i) the reflection through a pair of antipodal bond planes, acting on both layers, and (ii) the layer swap `σ`. Each is an involutive automorphism that exchanges two halves of the vertex set, and every edge between the halves joins a vertex to its image. In `Γ` coordinates (i) is `(x, a) → (ρx, 1 − a)` with `ρ` the spatial reflection, and (ii) has the two bipartition classes as its halves, the crossing edges being exactly the vertical ones. Every edge is crossed by one of these reflections.

**Domination.** For `h : V → R³` let `Z(h) = ∫ Π_u dω(s_u) exp(−(β/2) Σ_{⟨uv⟩} |s_u − s_v − h_u + h_v|²)`; `Z(0)` is the partition function of `μ_Γ` up to a constant. *(a)* For a reflection `θ` with halves `V_±`, write each crossing factor as `e^{−(β/2)|X_u|²} e^{−(β/2)|Y_u|²} e^{β X_u·Y_u}`, `X_u = s_u − h_u`, `Y_u = s_{θu} − h_{θu}`, and expand `e^{β Σ X_u·Y_u}` in its power series, whose coefficients `c_I` are non-negative: `Z(h) = Σ_I c_I a_I(h|V_+) a_I(h∘θ|V_−)`, the second integral being the first one evaluated on the reflected field because `θ` is an automorphism and `ω` is the same at every vertex. The inequality `(Σ c a b)² ≤ (Σ c a²)(Σ c b²)` gives `Z(h)² ≤ Z(h⁺) Z(h⁻)`, with `h⁺ = h` on `V_+` and `h∘θ` on `V_−`, and `h⁻` the mirror construction. *(b)* `Z` depends on the gradients of `h` only, and a gradient `g` with `|g| > 2` makes its factor at most `e^{−(β/2)(|g| − 2)²}`, so the supremum is attained; among the maximizers choose `h*` with the fewest edges of non-zero gradient, `n(h*)`. *(c)* For each reflection `h*⁺` and `h*⁻` are maximizers too, with `2n_+` and `2n_−` such edges (their crossing edges carry none); a crossing edge of non-zero gradient would give `min(2n_+, 2n_−) ≤ n(h*) − n_cross < n(h*)`. So `h*` has zero gradient on every crossing edge of every reflection, that is on every edge, and `Z(h) ≤ Z(0)` for all `h`.

**Infrared bound.** `⟨s_u⟩ = 0` by the symmetry `s → −s`, so the second order of `Z(εh) ≤ Z(0)` reads `⟨(s^α, Δh)²⟩ ≤ (h, Δh)/β` for every real `h` and component `α`, `Δ` the graph Laplacian. The functions `ψ_{k,±}(x, a) = 2^{−1/2} e^{ik·x}(±1)^a` are eigenfunctions of `Δ` with eigenvalues `E(k)` and `14 − E(k)` (the symbol is `[[7, −A], [−A, 7]]`, `A = 1 + 2Σ cos k_j`), orthogonal with `(ψ, ψ) = N`. Applying the bound to their real and imaginary parts, `⟨|ŝ_+(k)|²⟩ ≤ 3N/(βE(k))` for `k ≠ 0` and `⟨|ŝ_−(k)|²⟩ ≤ 3N/(β(14 − E(k)))` for every `k`.

**Order.** The transform is an isometry up to the factor `N`: `Σ_{k,±} |ŝ_±(k)|² = N · 2N`. The zero mode of the `+` band is `ŝ_+(0) = (M₀ + M₁)/√2`, `M_a = Σ_x s_{(x,a)}`. So `⟨|M₀ + M₁|²⟩/2 ≥ 2N² − (3N²/β)(G_L + H_L)`. The layer swap preserves `μ_Γ`, so `M₀` and `M₁` have the same law and `⟨|M₀ + M₁|²⟩ ≤ 4⟨|M₀|²⟩`. Therefore

`⟨|m₀|²⟩_π ≥ 1 − (3/(2β))(G_L + H_L).` ∎

**The constants.** *`G_L`.* `1/E` decreases in each `|k_j|`; give each grid point with no zero coordinate the cell of side `2π/L` on its origin side: the cells are disjoint and `1/E` on a cell is at least its value at the point, so these points contribute at most `I₀`. With `2(1 − cos x) ≥ 4x²/π²`, the points with exactly one zero coordinate contribute at most `(3/(4L)) Σ_{m₁,m₂=1}^{L/2} 1/(m₁² + m₂²) ≤ (3/(8L))(1 + log(L/2))²` (because `m₁² + m₂² ≥ 2m₁m₂`), and the points on the axes at most `π²/(16L)`. *`H_L`.* `1/(14 − E) = (1/8) Σ_n (−c/4)ⁿ`, `c = Σ cos k_j`; the torus moments of `c` are `2^{−n}` times closed torus walks, which equal the `Z³` moments for `n < L` and lie between them and `3ⁿ` otherwise, so `|H_L − I₂| ≤ (3/4)^L/2`. Hence `liminf_L ⟨|m₀|²⟩ ≥ 1 − β₀/β` with `β₀ = (3/2)(I₀ + I₂)`. *Numbers.* `I₀ = (1/6) Σ_m p_{2m}` and `I₂ = (1/8) Σ_m (9/16)^m p_{2m}`, `p_{2m} = b_m/36^m` the return probability of the cubic walk, `b_m = C(2m,m) Σ_k C(m,k)² C(2k,k)`. The runner gives `I₂ ∈ (0.1409314, 0.1409316)` by `61` exact terms and a geometric tail. Block 22 (PR #8156, open, restated) gives `3I₀ < 76/100`. Together `β₀ < 0.5914`; the partial sums alone give `β₀ > 0.55`.

## Theorem T4 — the linearized law: the response to a persistent source and the covariance

For the seven-site stencil `φ(k) = (1 + 2Σ cos k_j)/7 = 1 − E(k)/7`. The stationary mean of `θ_{t+1} = Pθ_t + ξ_t + f δ₀` solves `(I − P) θ̄ = f(δ₀ − 1/N)`, so `θ̄` has transform `f · 7/E(k)`: seven times the lattice Green function, real and cubic-symmetric, with no drift. The stationary equal-tick covariance of the non-zero modes is `σ²/(1 − φ²) = (7σ²/2)(1/E + 1/(14 − E))`, and response over covariance is `(1 + φ)/σ²`, so the two are not proportional: the chain is reversible, but in discrete time the relation between response and fluctuation carries the factor `1 + P`. For the six-site stencil `φ = 1 − E/6`, the response is `6/E`, the covariance `3σ²(1/E + 1/(12 − E))`, and `φ = −1` at `(π,π,π)`: a second pole, which is the pair of alternating chains of T1(b); with the site in the past `φ = −5/7` there. The runner checks the symbols and, exactly on the `3³` torus, the mean around a unit source and the fixed point of the covariance recursion. ∎

## Executed: the nonlinear sphere law (not proved)

Controls in the pack (`specs/supervisor_control_block36_*`), one seed each.

| Coupling `β` | Side `L` | Plateau of `|m|` (levels `1875`–`2500`) | Low-`k` structure factor over `σ²/(1 − φ²)` |
|---|---|---|---|
| `0.5` | `32` | `0.016` | `0.25` |
| `0.6` | `32` | `0.415` | `1.25` |
| `1.0` | `16` | `0.767` | `1.01` |
| `1.0` | `32` | `0.763` | `1.20` |
| `1.0` | `48` | `0.762` | `1.11` |

The linear calibration run gives `1.06` for the same estimator. The potential around a persistent field source `h = 0.5` (two copies on common random numbers) against `(h/(7β)) · 7/E`: mean ratio over `r = 1…4` of `0.964` at `β = 1` and `0.992` at `β = 6` on `32³`, forward-backward asymmetry `2·10⁻⁴` and `4·10⁻⁶`; on the backward four-predecessor lattice of the probes the ratio is `0.970` and the asymmetry `3·10⁻³`, the response being one-sided there. The refuting control samples the equilibrium laws with a single-site acceptance sampler: the seven-site chain's plateau against one layer of the doubled graph, `0.7699` against `0.7706` (`β = 1`, `L = 12`), `0.8601` against `0.8594` (`β = 1.5`), `0.6451` against `0.6455` (`β = 0.75`, `L = 16`); the six-site chain's space-time checkerboard against the static law, `0.6919` against `0.6928`, `0.8210` against `0.8206`, `0.4507` against `0.4503`.

## No-Go Discipline Gate

The note's sentences are positive under a hypothesis, with one negative sentence about the axioms (the memo excludes the clause); the gate applies.

### N1 — Routes by which the sentences could fail
1. *The clause* — it contradicts the memo's one-record-per-site sentence; the note is conditional on it and says so in its first fence.
2. *Bipartiteness* — T1(b) and the bilayer map need an even torus (or a box); on an odd torus the synchronous six-site chain does not split.
3. *The reflections* — T3 needs the rung, that is the site's own record in the past; for the six-site stencil the doubled graph is two copies of the torus and block 19's bound for the static law applies instead.
4. *The number `0.5914`* — it uses block 22's tail bound for `I₀` (open PR); without it the statement is `β₀ = (3/2)(I₀ + I₂)` with `I₀` the lattice constant.
5. *Stationary law against the path from an aligned start* — T3 is a statement about `π` on finite tori; that the chain started aligned stays near one ordered direction is executed, not proved.
6. *The source coupling* — T4 is the linear model; the map from the field `h` to the source strength `f` is measured (`0.96`–`0.99` of `h/(7β)`), not derived.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The inputs are the axioms' sentences, block 01's rule and static law, block 22's bracket and block 26's `σ²`, all declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the rule's sentences; the one-record-per-site sentence that the clause contradicts | yes (premise and boundary) |
| block 01 (`main`) | the rule as a product of pair weights; the static law | yes (premise, proposed) |
| block 22 (open PR #8156) | `3I₀ < 76/100` | yes, for the number `0.5914` only (restated) |
| block 26 (open PR #8170) | `σ² = A(nβ)/(nβ)` | for the normalization of the executed ratios only |
| blocks 13, 26, 35 (open PRs) | the write-once results this note is set against | placement |
| block 19 (open PR #8153) | the same method for the static law | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "under a record-per-tick clause the static law is stationary for the axioms' rule, the light-cone variant is a bilayer ferromagnet with long-range order, and the response to a source is the lattice Green function" | executed: detailed balance at one site; the conditional of a class; the band, response and covariance symbols | executed: every configuration of the four-cycle; all 256 pairs for the seven-site stencil; the `3³` propagation | executed: the infrared bound on every mode of both bands of a small two-valued instance | executed: the doubled graph onto the bilayer for `L = 4, 6`; the reflections' crossing edges and their cover | proved for every even torus under the clause; the clause contradicts the memo and is not adopted; executed numbers not claimed |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no tick for records: the kinetic-isotropy primitive's `Z_τ` is a loop regulator and its note says time remains derived. None is a wall and none supplies the clause.

### N7 — Steelman
Hostile reviewer: "T1 is the statement that heat-bath dynamics has its equilibrium law as stationary law, and T3 is a textbook proof on a bilayer. Nothing here is new mathematics." Reply: that is the point. The campaign treated the static law as a comparator with no dynamics behind it, and the owner asked what a universe in which nothing re-forms would mean. Under the memo as written nothing re-forms, and the kernel is absent (blocks 13, 26, 35). Under the one clause that lets records re-form, the comparator is the equilibrium of the axioms' own rule, and blocks 17 to 23 and 29 become statements about that equilibrium. The note prices the clause; it does not adopt it.

### N8 — Cross-cycle echo
Block 19's method returns on the bilayer; block 22's constant returns in `β₀`; block 35's conclusion (no kernel under write-once formation) is the contrast; the decision record's first consequence is restated with its cause identified: the kernel needs records that re-form.

## Falsifiers
- A configuration, site and value on the four-cycle violating detailed balance with the static law, or a parity class whose conditional is not the product of the rule's kernels (B1–B3).
- A pair of configurations violating detailed balance with `Π Z_x` for the seven-site stencil; a layer marginal of the pair law different from `Π Z_x`; an edge of the doubled graph not carried onto the bilayer; a crossing edge not of the form `{u, θu}`; an edge crossed by no reflection (C1–C6).
- Bands other than `E` and `14 − E`; a mode of the small two-valued instance above the infrared bound; `I₂` outside its bracket; `β₀` above `0.5914` with block 22's bracket (D1–D4).
- A response symbol other than `7/E`, a covariance other than `(7σ²/2)(1/E + 1/(14 − E))`, or a failure of the exact `3³` propagation (E1–E3).
- For the executed part: a plateau at `β = 1` that shrinks with `L`; a potential around a source that is one-sided on the symmetric stencil; an equilibrium sampler disagreeing with the chain.

## Boundaries and non-claims
This note is conditional on a clause that the axioms memo excludes: it supposes a record at every site at every tick, while the memo says that a site never carries more than one record and that records are permanent. It does not adopt the clause, does not say that the axioms permit it, and does not say that the write-once reading is wrong. It proves T1–T4 on finite even tori; it makes no statement about infinite-volume states, about uniqueness at small `β`, about the six-axis menu's ordered side under the light-cone stencil, or about the path from an aligned start. The executed numbers are in the controls and are not claims. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 01 (on `main`): the rule and the static law; proposed, unaudited. Block 22 (PR #8156, open): `3I₀ < 76/100`, restated, used for one number. Block 26 (PR #8170, open): `σ²`, restated. Blocks 13, 19, 35 as evidence addresses.
- Named standard imports at definition level (never as authority for physics): detailed balance; the power series of the exponential; the inequality of Cauchy and Schwarz; the diagonalization of a translation-invariant operator by the characters of the torus (Fourier) and the isometry of that transform (Parseval); the return probabilities of the cubic walk.
- Reference only: Fröhlich, Simon, Spencer (1976) for the method of T3; Glauber (1963) for the asynchronous dynamics; the literature on reversible probabilistic cellular automata for T2.

## Review record
Supervisor-run block (owner 2026-09-20: "harvest again, and then write any blocks that are meaningful / valuable"). Lens: the probes' derivation round found the light-cone law's reversibility, its doubled graph and a proof of long-range order (attempt by a Claude Opus worker, after a cross-family referee had located the gap of a first attempt), and the axioms map (another worker) showed that the memo excludes a record at every tick. The supervisor re-derived every step: the bilayer map is the observation that makes the reflections the ordinary ones; the consistency test that a proved ordering coupling must lie at or above the executed onset was applied before the proof was accepted (`0.5914` against an onset between `0.5` and `0.6`). Refuting pass: an acceptance sampler of the equilibrium laws, disjoint from the chains' exact heat bath, agrees with both chains to `0.001` at three couplings; the infrared bound was verified exactly on a two-valued instance (largest ratio `0.318`). Fold: the six-site stencil was added after the seven-site one, when it became clear that the axioms' own neighbourhood gives the comparator itself; the number `0.5914` was made conditional on block 22 instead of re-proving its tail bound. Mutation census: nine mutations, each failing in its own family.

## Verification

```bash
python3 scripts/admissibility_rule_re_recording_at_every_tick_static_law_stationary_bilayer_ferromagnet_long_range_order_green_function_response_2026_09_20.py
python3 scripts/admissibility_rule_re_recording_at_every_tick_static_law_stationary_bilayer_ferromagnet_long_range_order_green_function_response_2026_09_20.py --list-mutations
python3 scripts/admissibility_rule_re_recording_at_every_tick_static_law_stationary_bilayer_ferromagnet_long_range_order_green_function_response_2026_09_20.py --mutation infrared_bound_wrong
```
