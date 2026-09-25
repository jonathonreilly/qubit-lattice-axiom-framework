---
claim_id: admissibility_rule_forward_streaming_on_the_26_neighbours_isotropy_of_the_second_order_term_is_one_number_and_constant_rate_rules_capture_isotropically_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Supplied homogeneous 26-neighbor rates. Nonzero nonnegative shell weights have the stated sphere-averaged
  fourth-rank isotropy line. Mean-s sign-compatible cubic-covariant rules reduce this isotropy to beta=1/16; forward
  rate-one rules cannot have pointwise isotropic second moment on the stated arcs. Two explicit continuous cubic-covariant
  rate-one constructions give content-independent single-site influx in an independent homogeneous upstream reservoir.
  Finite periodic exchange dynamics preserves uniform measure, including reversal-symmetric reflecting solids. No
  isotropic spatial shadow, hydrodynamic limit, or exact isotropic mixture is established.
upstream_dependencies:
- admissibility_rule_a_streaming_clause_with_an_isotropic_second_order_term_content_as_a_bias_on_a_symmetric_walk_unbiased_capture_and_its_price_bounded_theorem_note_2026-09-21
- admissibility_rule_free_capturing_bodies_are_carried_by_the_wind_capture_law_anisotropic_collisionless_shadow_dilution_law_of_motion_and_its_window_bounded_theorem_note_2026-09-21
- admissibility_rule_records_with_inertia_content_as_direction_of_travel_conserved_momentum_structureless_equilibrium_sound_speed_forces_need_capture_or_emission_bounded_theorem_note_2026-09-20
- admissibility_rule_the_wind_of_a_capturing_body_is_not_isotropic_lattice_streaming_gives_a_viscous_term_of_cubic_symmetry_direction_dependence_does_not_decay_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_forward_streaming_on_the_26_neighbours_isotropy_is_one_number_constant_rate_rules_capture_isotropically_2026_09_24.py
---

# Forward streaming on 26 neighbours: averaged isotropy, rate-one constructions and scoped capture

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within the streaming clause of blocks 44, 51 and 52 as landed, with the hop set enlarged; one numerical statement marked as such; harvest block from three Grok-refereed probes attempts; nothing adopted or registered; unaudited)

This note works within the inertial streaming clause of blocks 44, 51 and 52, as landed on main, with the hop set enlarged to the 26 neighbours; it reports when forward streaming, a record moving only along its content, has an isotropic second-order term and an isotropic capture; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 51, as landed, found that a record which steps only forward along an axis gives streaming with a viscous term of cubic symmetry. Block 52 made the second-order term isotropic by letting records step against or across their content. Its gate left two routes open: "Hops to more neighbours … Not worked", and `αδ_kl + β s_k s_l` with more than six neighbours. This note works both.

- **T1: shell rules.** Rates `λ_{|d|²}(s·d/|d|)_+` on the 6 axis, 12 face and 8 body neighbours.
  - The mean step is `κ s`.
  - The fourth-rank moment is isotropic exactly on the line `λ₁ = λ₂ + (8/3)λ₃`. There the streaming term vanishes on a potential inflow, which is block 51's obstruction.
  - Axis hops alone are never isotropic.
  - The total rate of these rules is never constant, so a body still captures records unevenly by direction.
- **T2: one number decides isotropy.** For any rule with mean step `s`, the diagonal second moment is at least `|s_m|`, with simultaneous equality in all three coordinates exactly for sign-compatible rules, which never step against any component of `s`.
  - So every mean-s sign-compatible rule has the same diagonal. If it is also cubic-covariant, its fourth-rank moment is isotropic iff one number, `β = ⟨|s₁s₂| W₁₂⟩`, equals `1/16`.
  - No mean-s forward rule of total rate exactly one is isotropic pointwise; isotropy can only come from the sphere average.
- **T3: forward rules with a constant total rate exist.** Every content is the average of its forward neighbours: the staircase rule. So does a rule on axes and face diagonals only.
  - Both are sign-compatible, continuous and cubic-covariant.
  - A capturing site takes every content at the same rate.
- **T4: stationarity.** On a finite periodic torus, spatially homogeneous exchange rates preserve the uniform fixed-count measure and its product mixtures.
- **Numerical only.** Quadrature gives `β = 0.06490` for the staircase rule and `0.05613` for the axes-and-faces rule, reported on opposite sides of `1/16`; not executed by this runner. If independently established with bounds, a mixture with weight about `0.2735` has an exactly isotropic second-order term.

In plain terms, block 51 asked whether a record that only moves forward along its own direction can stream the same way in every direction. On a cubic lattice it can, but only by stepping to diagonal neighbours as well as to face neighbours. Doing so while also being caught at the same rate from every direction needs a rule that reads the ordering of the record's direction components. Whether the second-order term is then exactly the same in every direction comes down to one number, `1/16`, which two explicit rules straddle numerically. The same difficulty is known from lattice gases used to model fluids: four-fold symmetry of velocity moments needs diagonal velocities.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "A site never carries more than one record; records are permanent." Exchange at an occupied target is a separately supplied rule, not a consequence of this sentence.
  - "Each site has a domain of local possibilities." The content, read as the direction of travel.
  - "Admissibility is not a dynamics axiom." The streaming clause and its rates are supplied. Nothing is adopted.
- **The clause** (blocks 44, 51 and 52 as landed).
  - A record of unit content `s` at `x` attempts a hop to `x + d` at rate `a(s, d)`.
    - If `x + d` is empty, it moves.
    - If it is occupied, the two records exchange sites.
    - If it is solid, the record stays and its content reverses.
  - The streaming is expanded to second order as in block 51 T1, exact on fields of degree two. `M_kl(s) = Σ_d a(s, d) d_k d_l` and `T_ijkl = ⟨s_i s_j M_kl(s)⟩` over the uniform sphere.
  - Here the hop set is enlarged from 6 to the 26 neighbours `d ∈ {−1, 0, 1}³ ∖ 0`.
- **Terms.**
  - *Forward*: `a(s, d) > 0` only when `s·d > 0`.
  - *Sign-compatible*: every weighted `d` has `d_m ∈ {0, sign s_m}`.
  - *Total rate*: `r(s) = Σ_d a(s, d)`.
  - `W₁₂` is the rate of steps that move both coordinates 1 and 2.
- **Capture** (block 48). In an independent infinite homogeneous upstream reservoir with one absorber, a site that captures takes content `s` at rate `ρ r(s)`: along a forward walk `s·x` increases, so the density upstream of the site is not disturbed by it.

## Theorem T1 — shell rules

*Statement.* Take `a(s, d) = λ_{|d|²}(s·d/|d|)_+`, with nonnegative shell weights, not all zero. The identically zero rule is excluded from every nonconstancy or anisotropy assertion.
- (a) `⟨s_i s_j |s·n|⟩ = (δ_ij + n_i n_j)/8`. The shell-geometry tensor `S = Σ_d λ_|d|² d dᵀ` is `(2λ₁ + 8λ₂ + 8λ₃)I`; this is not the hop second moment `M(s)`, which depends on content, and the only obstruction to an isotropic `T` is
  `T₁₁₁₁ − T₁₁₂₂ − 2T₁₂₁₂ = (λ₁ − λ₂ − (8/3)λ₃)/8`.
  - So `T` is isotropic exactly on `λ₁ = λ₂ + (8/3)λ₃`.
  - Block 51's clause, `λ₁ = 1/√3` with no diagonals, gives `1/(4√3)`, `1/(8√3)` and `0`.
- (b) **The mean step** is `κ s` with `κ = λ₁ + 2√2λ₂ + 4λ₃/√3`.
- (c) **The total rate** is
  `r(s) = λ₁|s|₁ + λ₂√2 Σ_{i<j} max(|s_i|, |s_j|) + (λ₃/√3) Σ_{±,±} |s₁ ± s₂ ± s₃|`.
  - It is never constant on the sphere.
  - On the isotropy line, `r(body) − r(axis) = (√3 + √6 − 1 − 2√2)λ₂ + (4√3/3 − 2/3)λ₃`, and both coefficients are positive.
- (d) **Potential inflow.** On the line the streaming term is a combination of `∇²g` and `∇(∇·g)`, and both vanish on `g = ∇(1/r)`.

*Proof.*
- (a) `t = s·n` is uniform on `[−1, 1]`, and the transverse part is uniform on a circle of radius `√(1 − t²)`. So `⟨|t|³⟩ = 1/4` and `⟨x²|t|⟩ = 1/8`.
  - The odd part of `(t)_+` averages to zero.
  - Sum over the shells: `T = (1/16)[δ_ij S_kl + Q_ijkl]`, where `Q_ijkl = Σ_d λ_|d|² d_i d_j d_k d_l/|d|²`.
- (b) The `|s·d|` parts cancel between `d` and `−d`, and each shell's `Σ d dᵀ` is a multiple of `I`.
- (c) Pair the opposite neighbours. `r` is a positive combination of finitely many `|s·d̂|`, so it is linear on each open cone between the planes `s·d̂ = 0`. A linear function is not constant on an open subset of the sphere.
- (d) `∇(1/r)` is divergence-free and harmonic away from the origin. ∎

*Checked (B1, B2).*
- (a): all 81 components of `T`, symbolic in the three rates, on and off the line.
- (b) and (c): five contents, including generic ones.
- (d): symbolically.

The smallest isotropic members are axes plus face diagonals at equal rates (18 targets), and axes plus body diagonals at `8:3` (14 targets).

## Theorem T2 — one number decides isotropy

*Statement.*
- (a) **The least-diffusion bound.** For every rule with mean `s`, `M_mm ≥ |s_m|`, with simultaneous equality in all coordinates iff the rule is sign-compatible; equality in just coordinate m excludes opposite-sign hops in that coordinate only. This is block 52 T1's bound, unchanged by diagonal hops.
- (b) **The universal diagonal.** Every mean-s sign-compatible rule has `M_mm(s) = |s_m|`.
  - Hence `T₁₁₁₁ = ⟨|s₁|³⟩ = 1/4` and `T₁₁₂₂ = ⟨s₁²|s₂|⟩ = 1/8`, for every such rule.
  - A cubic-covariant sign-compatible rule has `T = (1/8)δ_ijδ_kl + β(δ_ikδ_jl + δ_ilδ_jk) + (1/8 − 2β)δ_ijkl`, where `β = T₁₂₁₂ = ⟨|s₁s₂| W₁₂⟩`.
  - It is isotropic iff `β = 1/16`. Axis hops have `β = 0`.
  - At block 51's speed the momentum term is `ν_lat[∇²g_i + 16β ∂_i(∇·g) + (1 − 16β)∂_i²g_i]` with `ν_lat = √3/16`.
- (c) **No pointwise route.** On the unit arc `s = (a, b, 0)`, `0 < b < a`, a forward rule with mean s and total rate 1 has `M₁₁ = a` and `M₁₂ = a + b − 1`. `M = α'I + β' s sᵀ` would then force
  `M₂₂ − b = −(a − b)(1 − a)(1 − b)/(ab) < 0`,
  which is impossible because `M₂₂ ≥ b`. So isotropy can only come from the sphere average.

*Proof.*
- (a) `d_m² = |d_m|` for `d_m ∈ {−1, 0, 1}`, so `M_mm = Σ a|d_m| ≥ |Σ a d_m| = |s_m|`.
- (b) If `d_m ∈ {0, sign s_m}`, then `d_m² = sign(s_m) d_m`.
  - Cubic covariance leaves only `T₁₁₁₁`, `T₁₁₂₂` and `T₁₂₁₂`.
  - `s₁s₂M₁₂ = |s₁s₂| W₁₂`.
- (c) The forward set at `(a, b, 0)` is `{d₁ = 1} ∪ {(0, 1, ∗)}`. The total `1 − a` on `d₁ = 0` carries `d₂ = 1`. Then use `(a + b)² = 1 + 2ab`. ∎

*Checked (C1, C2).* The moments are exact. The diagonal and sign-compatibility hold for both rules of T3 at 342 rational contents. The arc identity is symbolic, with its sign checked at four rational arc points.

## Theorem T3 — forward rules with a constant total rate

*Statement.* Let `a ≥ b ≥ c ≥ 0` be the sorted `|s_m|`, on axes `i, j, k`, and let `u_m = sign(s_m)e_m`.
- (a) **The staircase rule.** Put weight `(1 − t)[(a − b)u_i + (b − c)(u_i + u_j) + c(u_i + u_j + u_k)] + t[a u_i + b u_j + c u_k]`, with `t = (1 − a)/(b + c)`, defined as zero at an axis.
  - The weights are non-negative and total 1, and the mean step is exactly `s`.
  - Every weighted target is forward and sign-compatible, with at most five targets.
  - The rule is continuous on the sphere, covariant under the 48 cubic symmetries, and has `a(−s, d) = a(s, −d)`.
- (b) **The axes-and-faces rule.** Merge weight from pairs of axes into face diagonals, as far as the budgets allow, and scale the merge so the total is 1. It has the same properties, with at most six targets.
- (c) **Consequence.** With the total rate constant, a capturing site takes every content at the same rate, at first order in the density. This does not determine the angular spatial shadow or a far-field coefficient.

*Proof.*
- (a) The axis form `a u_i + b u_j + c u_k` has mean `s` and total `a + b + c ≥ 1`. The staircase form has mean `s` and total `a ≤ 1`.
  - The mixture's total is 1 at `t = (1 − a)/(b + c) ∈ [0, 1]`.
  - `1 − a = (b² + c²)/(1 + a) ≤ (b + c)²`, so `t ≤ b + c`, and the rule tends to `u_i` near an axis.
  - At ties the orderings give the same weights.
- (b) Explicitly, put `z_ij=b,z_ik=c,z_jk=0` when `a>=b+c`; otherwise put `z_ij=(a+b-c)/2,z_ik=(a-b+c)/2,z_jk=(-a+b+c)/2`. These are nonnegative and consume no more than each axis budget. Let `S=a+b+c`, `Z=sum z`, `theta=(S-1)/Z` away from an axis; use the single axis step at an axis. In the first case Z=b+c and theta<=1 because a<=1; in the second Z=S/2 and theta<=1 because S<=sqrt3<2. Also S>=1, so theta>=0. Give face i+j weight theta z_ij and axis i weight |s_i|-theta sum_j z_ij. They are nonnegative, have mean s and total S-theta Z=1. The two formulas agree at a=b+c. Equal-coordinate ties give identical pair weights, and vanishing coordinates have vanishing incident face weights. Near an axis all non-axis weights tend to zero, proving continuity there. These facts prove continuity and signed-permutation covariance beyond the finite tests.
- (b, bookkeeping) Merging `z` from `u_m` and `u_n` into `u_m + u_n` keeps the mean and lowers the total by `z`. The maximal merge is scaled by `(a + b + c − 1)/Σz ∈ [0, 1]`.
- (c) Supply independent walkers on the infinite lattice, one absorbing site and a homogeneous upstream reservoir of content density rho f(s). Every forward step strictly increases s.x. Absorption at zero cannot affect x=-d for an incoming hop d, since s.(-d)<0. The undisturbed incoming flux is therefore rho f(s) sum_d a(s,d)=rho f(s). This proves content-independent influx only in this dilute single-site model. Finite-density exclusion, multiple absorbers and spatial angular shadow isotropy require separate arguments. ∎

*Checked (D1, D2).*
- At 342 rational contents (twelve base points and their images under the 48 signed permutations): weights `≥ 0`, total exactly 1, mean exactly `s`, every target forward, `0 ≤ t ≤ b + c`, and `a(−s, d) = a(s, −d)`.
- Covariance under permutations at four tied contents.

## Theorem T4 — stationarity

*Statement.* On a finite periodic torus, take spatially homogeneous finite rates a(s,d), a symmetric hop set, and either a finite uniform content menu or uniform sphere measure. Exchange at occupied targets preserves the uniform fixed-count measure and its Bernoulli-density product mixtures. For reflecting solids the menu/measure must be antipodally symmetric and a(-s,d)=a(s,-d). These statements do not assert ergodicity or a hydrodynamic limit.

*Proof.* Take a configuration `c`, a record at `y` with content `s`, and a hop vector `d`. Look at `y − d`.
- If it is empty, `c` is reached from it by a hop.
- If it holds `s'`, `c` is reached by an exchange from the configuration with `s` at `y − d` and `s'` at `y`.
- If it is solid, `c` is reached by reflection from `−s` at `y` attempting `−d`.

Each labeled event has one predecessor with rate a(s,d). Summing over records and directions gives total inflow sum r(s), equal to outflow. Self-events cancel on both sides. For continuous contents use the measure-preserving swap or antipodal change of variables instead of counting; the total rates are finite. Fixed record number is conserved, so mixtures of its invariant uniform sectors give the product occupancy measure. ∎

*Checked (E1).* On the `3³` torus, with all 26 hop vectors and random positive integer rates obeying `a(−s, d) = a(s, −d)`, every configuration balances:
- 11700 configurations with a solid site and two records of six contents;
- 23400 with three records of two contents.

With exchange suppressed, most configurations of a smaller census do not balance.

## Historical author quadrature (not fresh evidence)

- The joint-step numbers are
  `β_stair = (1/3)⟨(1 − t)(ab² + ac² + bc²)⟩_sector`,
  and the corresponding piecewise-rational average for the axes-and-faces rule.
- The original author reports quadrature values `β_stair = 0.064898…` and `β_af = 0.056128…`. Attempt a3 used a product quadrature with the kink split, and its referee checked independently. The supervisor's own adaptive quadrature agrees to eight digits.
- These are on opposite sides of `1/16`, with margins of 3.8% and 10%. `T` is linear in the rule, so the mixture `(1 − λ)·staircase + λ·(axes and faces)` with `λ = (β_stair − 1/16)/(β_stair − β_af) ≈ 0.2735` would have `β = 1/16`.
- **Status.**
  - The existence of such a `λ ∈ (0, 1)` is exact given the two signs. The signs are numerical.
  - A float model of an interval-bound scheme closed the axes-and-faces side (`β_af < 1/16`) with a few thousand cells, but not the staircase side at 400000. It was a sizing experiment, not a certificate, and it is not part of the runner.
  - An exact enclosure of `β_stair` is open.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 52 as landed, its gate: 'Hops to more neighbours ... Not worked' and 'alpha delta_kl + beta s_k s_l ... beta = 0 is forced with six neighbours'; block 51 as landed: the cubic viscous term of axis streaming"
source_of_blocker_text: blocks 51 and 52 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an exact enclosure of beta for the staircase rule (or an exactly computable constant-rate rule to mix with); the shadow at moderate distances; the collisional viscosity; the two-body force off the axes"
conditional_surface_status: "T1-T4 exact within the supplied clause with 26 neighbours; the mixture's isotropy numerical; no spatial shadow isotropy proved"
hypothetical_axiom_status: "the streaming clause, its hop set and rates are hypotheses; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 44 gave the inertial clause and its stationarity with exchange.
  - Block 48 gave the capture law for axis hops (`|s|₁`).
  - Block 51 gave the axis streaming and its cubic term.
  - Block 52 gave the two-way axis rule and the least-diffusion bound, and left the two routes worked here.
- **The probes attempts**, refereed by a Grok model, confirmed (#9039, #9094, #9129).
  - `isotropic-streaming-clause` a1 (issue #8688, Claude Opus 5.5): T1 and T4.
  - a2 (issue #8583, Claude Opus 5): showed that the anisotropy comes from one-way axis hops, and gave pointwise witnesses.
  - a3 (issue #9127, Claude Opus 5.5): T2, T3 and the quadrature.
- **In the literature.**
  - That four-fold isotropy of velocity moments on a cubic lattice needs diagonal velocities is the known constraint on lattice-gas automata (Frisch, Hasslacher and Pomeau; d'Humières, Lallemand and Frisch).
  - It is also the constraint on the velocity sets and weights of lattice Boltzmann methods (Qian, d'Humières and Lallemand). T1's line is the forward-only analogue of their weight conditions.
  - The zone lemma is Archimedes' hat-box theorem.
- **New here:**
  - an independent exact runner;
  - the results placed against blocks 51 and 52 as landed;
  - the numerical statement marked and scoped;
  - a sizing experiment toward an exact enclosure.

## Exact target and obligation graph

Target: block 52's two open routes. The obligations are:
- (O1) shell rules;
- (O2) the universal diagonal and `β`;
- (O3) constant-rate forward rules;
- (O4) stationarity;
- (O5) the value of `β`.

T1–T4 discharge O1–O4 within the revised domains. O5 remains a historical numerical report; this runner does not execute quadrature, and no exact sign enclosure or isotropic mixture is established.

## No-Go Discipline Gate

The note's negative sentences:
- axis hops alone are never isotropic at fourth rank;
- the shell rules' capture is never isotropic;
- no mean-s forward rule of total rate exactly one is pointwise isotropic along the arcs `(a, b, 0)`.

### N1 — Routes by which the sentences could fail or mislead
1. *Non-shell forward rules.* T3 has isotropic capture. The shell rules' anisotropy is not a statement about all forward rules.
2. *A total rate that is not constant.* The arc lemma needs `r < (1 + ab)/(a + b)` on the arc. A larger total rate escapes it.
3. *The collisional viscosity.* Not treated. Block 51 marks its isotropy as not proved.
4. *The spatial shadow.* Constant content capture does not supply its angular density; that inference is deferred.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The hop set is enlarged to diagonal neighbours. That is outside the six-neighbour stencil of the lane's other clauses, and it needs exchange with diagonal targets.
- Reflection at solids is content reversal.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | one record per site; a site's possibilities; no dynamics in the axioms | yes |
| blocks 44, 48, 51, 52 (landed) | the clause, capture, the streaming expansion, the bound | yes (restated) |
| probes (#8688, #8583, #9127; Grok-refereed #9039, #9094, #9129) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "forward streaming on 26 neighbours: isotropy is one number; constant-rate rules capture isotropically" | executed: the zone moments; `T` for the shell rules, all 81 components, symbolic in the rates | executed: both constant-rate rules at 342 rational contents (weights, total, mean, forward, sign-compatible, diagonal) | executed: the mean step and the total rate at five contents; the potential inflow | executed: stationarity censuses on the `3³` torus with 26 hops | every content and every rate function as stated; the mixture's isotropy numerical; the clause supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Diagonal steps break the six-neighbour lattice." *Reply:* Yes, and the note says so (N3). Block 52 kept six neighbours and paid with hops against the content. This note keeps every step forward and pays with diagonals.
- *Objection:* "The mixture rests on floats." *Reply:* Stated as numerical. The exact content is the reduction to one number and the constant-rate rules.

### N8 — Cross-cycle echo
- Block 51 found the cubic term, and block 52 removed it with backward hops.
- This note removes it with forward diagonal hops, up to one number, and makes single-site reservoir influx content independent; spatial angular isotropy does not follow.

## Falsifiers

- A sign-compatible rule with `M_mm ≠ |s_m|`.
- A content at which the staircase rule has a negative weight, a total other than 1, or a mean other than `s`.
- A configuration of the `3³` census that does not balance with exchange.

## Boundaries and non-claims

- The clause and its hop set are supplied.
- The mixture's exact isotropy is not established.
- The shadow at moderate distances, the collisional viscosity and the two-body force off the axes are not treated.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 44, 48, 51 and 52, restated or placed.
- The probes attempts, refereed by another model family.
- Named standard imports, at definition level:
  - Archimedes' zone lemma;
  - exact symbolic and rational arithmetic.
- Reference only: Frisch; Hasslacher; Pomeau; d'Humières; Lallemand; Qian.

## Review record

- **Who and when.** Supervisor-run block, the sixty-sixth since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - Three probes attempts derived the results (#8688, #8583, #9127). Grok referees confirmed them (#9039, #9094, #9129).
  - The supervisor re-checked the exact parts with its own runner, and the quadrature with its own float code, which is not part of the runner.
- **Before writing.** Main was re-fetched. Blocks 51 and 52 were read as landed.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_forward_streaming_on_the_26_neighbours_isotropy_is_one_number_constant_rate_rules_capture_isotropically_2026_09_24.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.

## Current input identities and limits

The current companion sources below supply conditional models, not physical authority. The second-order statement concerns the truncated sphere-averaged momentum operator under a first-harmonic closure; it is not exact lattice isotropy. Historical quadrature and referee reports are recovery material only. No isotropic spatial shadow, general constant-rate no-go, or exact mixture is landed.

- [Current companion model](ADMISSIBILITY_RULE_RECORDS_WITH_INERTIA_CONTENT_AS_DIRECTION_OF_TRAVEL_CONSERVED_MOMENTUM_STRUCTURELESS_EQUILIBRIUM_SOUND_SPEED_FORCES_NEED_CAPTURE_OR_EMISSION_BOUNDED_THEOREM_NOTE_2026-09-20.md)
- [Current companion model](ADMISSIBILITY_RULE_FREE_CAPTURING_BODIES_ARE_CARRIED_BY_THE_WIND_CAPTURE_LAW_ANISOTROPIC_COLLISIONLESS_SHADOW_DILUTION_LAW_OF_MOTION_AND_ITS_WINDOW_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Current companion model](ADMISSIBILITY_RULE_THE_WIND_OF_A_CAPTURING_BODY_IS_NOT_ISOTROPIC_LATTICE_STREAMING_GIVES_A_VISCOUS_TERM_OF_CUBIC_SYMMETRY_DIRECTION_DEPENDENCE_DOES_NOT_DECAY_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Current companion model](ADMISSIBILITY_RULE_A_STREAMING_CLAUSE_WITH_AN_ISOTROPIC_SECOND_ORDER_TERM_CONTENT_AS_A_BIAS_ON_A_SYMMETRIC_WALK_UNBIASED_CAPTURE_AND_ITS_PRICE_BOUNDED_THEOREM_NOTE_2026-09-21.md)
