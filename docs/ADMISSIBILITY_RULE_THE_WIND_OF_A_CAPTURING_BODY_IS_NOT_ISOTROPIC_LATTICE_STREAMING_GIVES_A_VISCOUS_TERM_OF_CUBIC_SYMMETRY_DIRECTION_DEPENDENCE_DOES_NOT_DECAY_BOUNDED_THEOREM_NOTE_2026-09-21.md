---
claim_id: admissibility_rule_the_wind_of_a_capturing_body_is_not_isotropic_lattice_streaming_gives_a_viscous_term_of_cubic_symmetry_direction_dependence_does_not_decay_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied inertial clause of block 44 (PR #8550; sphere menu: a record of content s steps to x + sign(s_k) e_k at the rate |s_k|/sqrt 3); nothing adopted. (T1) On a field of degree two in the site the streaming operator of a record is exactly (1/sqrt 3)[-s.grad + (1/2) sum_k |s_k| d_k^2]; for a smooth field this is its expansion to second order in gradients. (T2) Over the uniform sphere <|s_k|> = 1/2, <s_i^2 |s_i|> = 1/4, <s_i^2 |s_k|> = 1/8 for k different from i, and moments odd in a coordinate vanish; hence, in local equilibrium at small density (content law (1 + 3 u.s)/(4 pi)), the second-order term gives the number equation D_lat Laplacian n, D_lat = 1/(4 sqrt 3), and the momentum equation nu_lat (Laplacian g_i + d_i^2 g_i), nu_lat = sqrt 3/16, the second part (no sum over i) having cubic symmetry only and the same coefficient as the isotropic part: a longitudinal wave is damped at nu_lat q^2 times 2, 3/2, 4/3 along an axis, a face diagonal, a body diagonal. (T3) For a harmonic potential chi the field (d_x^3 chi, d_y^3 chi, d_z^3 chi) is in general not a gradient (curl 240 y along z for chi = x^5 - 10 x^3 y^2 + 5 x y^4; 70/2187 along z at (1, 2, 2) for chi = 1/r), so pressure cannot balance the term of cubic symmetry acting on a potential flow: the potential inflow of blocks 45 and 46 does not solve the creeping equations. (T4) With the viscous operator nu (Laplacian g_i + eta d_i^2 g_i) the creeping inflow towards a sink is, in wave-vector space, g_i = -i k_i P/(k^2 + eta k_i^2), P = S/sum_i k_i^2/(k^2 + eta k_i^2): it satisfies both equations, is homogeneous of degree -1, so that the inflow is a function of direction over r^2 at every distance, and has k x g different from zero at generic wave vectors unless eta = 0. EXECUTED, NOT CLAIMED (one capturing body of about 22 sites, side 64, eight seeds per case; inward momentum density times r^2 over the capture rate, r from 6 to 10, within 15 degrees of the axes / face diagonals / body diagonals): without scattering at density 0.1: 0.180, 0.143, 0.116 (block 48's exact first-order values times 1/(1 - rho): 0.176, 0.147, 0.122); with scattering (density 0.1, gamma 2): 0.175, 0.149, 0.130 (ratio of axes to body diagonals 1.35 +- 0.03); at the density and scattering rate of blocks 45 and 47 (0.3, 1): 0.223, 0.186, 0.172 (ratio 1.30 +- 0.02), where the isotropic closure of block 45 has 0.197 in every direction; the creeping solution gives the ratio 1.18, 1.37, 1.76 for eta = 1/4, 1/2, 1 in the same shell and slightly more farther out. NOT claimed: the value of eta in the gas (the collisional part of the viscosity is not computed), a hydrodynamic limit, the flow when inertial forces dominate viscous ones, the force between two bodies off the axes (not executed), any gravitational statement, any adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_the_wind_of_a_capturing_body_is_not_isotropic_lattice_streaming_viscous_term_of_cubic_symmetry_2026_09_21.py
---

# The wind of a capturing body is not isotropic: the lattice's streaming gives the gas a viscous term of cubic symmetry, and the direction dependence of the creeping inflow does not decay with distance

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements about the streaming operator, its moments and the creeping equations, within a supplied clause; winds by direction executed, not claimed; corrects an assumption of blocks 45 to 48; nothing adopted or registered; unaudited)

This note works within the supplied inertial clause of block 44; it reports that the streaming of records along lattice axes gives the gas a viscous term of cubic symmetry and what that does to the wind of a capturing body; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Blocks 45 to 47 (PRs #8553, #8554, #8556) gave a capturing body an inverse-square wind that is the same in every direction, and two bodies a force `K Q₁Q₂/r²` with one coefficient. The sameness in every direction was an assumption: block 45's T3 is stated "in the local-equilibrium closure with spherical symmetry", and block 46 assumes that the stationary wind has no circulation. Block 48 (PR #8558) found that without scattering the force depends on direction, and said that one coefficient needs collisions. A control run to show that collisions restore the symmetry showed the opposite, and this note finds the reason.

1. **Executed.** The wind of one capturing body was measured by direction, at distances 6 to 10 where the walls do not matter. Without scattering the inflow along the axes, face diagonals and body diagonals is `0.180, 0.143, 0.116` per unit capture, against block 48's exact first-order values `0.176, 0.147, 0.122`: the measurement is calibrated. **With scattering it is still direction-dependent**: `0.175, 0.149, 0.130` at density `0.1`, `γ = 2`, and `0.223, 0.186, 0.172` at the density and scattering rate of blocks 45 and 47, where the isotropic closure has `0.197` in every direction. The ratio of axes to body diagonals is `1.55 ± 0.05` without scattering, `1.35 ± 0.03` and `1.30 ± 0.02` with it.
2. **The reason.** A record hops along lattice axes. Expanded to second order in gradients its streaming operator is `(1/√3)[−s·∇ + ½Σ_k|s_k|∂_k²]` (T1, exact on fields of degree two). The second term is a diffusion along the axes whose strength depends on the content. Its sphere moments, `⟨s_i²|s_i|⟩ = 1/4` and `⟨s_i²|s_k|⟩ = 1/8`, give the momentum equation, even in perfect local equilibrium, the viscous term `ν_lat(∇²g_i + ∂_i²g_i)` with `ν_lat = √3/16` (T2). The second part has the symmetry of the cube and not of the sphere, and it is as large as the first.
3. **What it does to the wind.** Acting on a potential flow, that part is not a gradient, so pressure cannot balance it: the potential inflow of blocks 45 and 46 does not solve the creeping equations (T3). The solution that does is homogeneous of degree minus two in the distance: a function of direction over `r²` (T4). So the direction dependence does not decay: it is not a near-field effect.
4. **Size.** For the viscous operator `ν(∇²g_i + η∂_i²g_i)` the creeping solution gives the ratio of axes to body diagonals `1.18, 1.37, 1.76` for `η = 1/4, 1/2, 1` in the executed shell. The executed `1.30` to `1.35` is that of `η` between about `0.3` and `0.5`, that is, of a collisional viscosity between one and about two and a half times `ν_lat`; `η` is not computed here.

So, within the clause and for the slow (creeping) flows that every run of this campaign has executed: **the wind of a capturing body is `f(direction)/r²`, not `1/r²`, with or without collisions, and the force between two capturing bodies depends on the lattice direction of their separation.** The forces of blocks 45 and 47 were executed along a lattice axis only; their agreement with the isotropic coefficient is an agreement along that axis.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 48 (PR #8558), Result 3: 'the inverse-square law with one coefficient needs collisions over the distance in question'; block 45 (PR #8553) T3: 'a statement in the local-equilibrium closure with spherical symmetry'; block 46 (PR #8554): 'the stationary wind's zero circulation is assumed'"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "the isotropy assumed in blocks 45 to 48 fails for the creeping flows executed; corrections posted on PRs #8553, #8554, #8556, #8558; next: the force between two capturing bodies off the lattice axes, the collisional viscosity (the value of eta), and the inflow when inertial forces dominate viscous ones; queued on ai/probes"
conditional_surface_status: "T1 exact on fields of degree two; T2 a statement in local equilibrium at small density; T3, T4 exact statements about the creeping equations with a term of cubic symmetry; the winds by direction (floating point; side 64; eight seeds per case) and the angular function of the creeping solution (solved in wave-vector space on a grid) are in the controls and not claimed"
hypothetical_axiom_status: "the inertial clause of block 44 (its scattering re-draws contents) and the capture of records by bodies; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full) is used through "A site never carries more than one record; records are permanent." Block 01 (on `main`, proposed and unaudited) supplies the menus. Blocks 44, 45, 46 and 48 (open PRs #8550, #8553, #8554, #8558) supply the clause, the conserved currents, the pressure `ρ/(3√3)`, the isotropic closure `g = √3Q/(4πr²(1 − ρ))`, and the exact shadow of independent records. They are restated; the runner re-derives what it uses.

- **Streaming operator.** For the density `f(x, s)` of records of content `s`: `Σ_k (|s_k|/√3)[f(x − sign(s_k)e_k, s) − f(x, s)]`.
- **Local equilibrium.** The content law `(n/4π)(1 + 3u·s)` with density `n(x)` and mean content `u(x)`; momentum density `g = nu`. Small density: exchange of contents neglected.
- **Creeping equations.** The stationary linear equations `∇·g = −S` (a sink of strength `S`) and `0 = −∂_iP + ν(∇²g_i + η∂_i²g_i)`, no sum over `i` in the last term.
- **Direction classes.** Sites within 15 degrees of a lattice axis, of a face diagonal, of a body diagonal.

That a gas of particles hopping on a square or cubic lattice has a viscous stress of the lattice's symmetry and not of the sphere's is the classical defect of the first lattice gases (Hardy, Pomeau and de Pazzis), cured in two dimensions by the hexagonal lattice of Frisch, Hasslacher and Pomeau; creeping flow is the regime named after Stokes, in which the flow past a body scales without a length; the expansion in gradients about local equilibrium is that of Chapman and Enskog; the ratio of inertial to viscous forces is the number of Reynolds. None is used as authority.

## Prior art and what is new

The anisotropy of lattice gases on cubic lattices is classical. What is new is its exact form in the campaign's clause (the second-order term of the streaming operator, its moments `1/4` and `1/8`, the coefficient `√3/16` and the equality of the cubic and isotropic parts), the consequence for the campaign's own wind law (the potential inflow is not a solution; the direction dependence is homogeneous and does not decay), and the executed winds by direction, which correct an assumption of blocks 45 to 48.

## Exact target and obligation graph

Target: why the wind of a capturing body depends on direction when the gas scatters, and whether the dependence decays. Obligations: (O1) the second-order streaming term; (O2) its moments and the viscous term; (O3) the potential inflow is not a solution; (O4) the solution and its scaling. T1–T4 discharge them at their stated levels; the controls execute the winds and the angular function.

## Theorem T1 — the streaming operator to second order

A record of content `s` arrives at `x` from `x − sign(s_k)e_k` at the rate `|s_k|/√3`. For a field of degree two, `f(x − σe_k) − f(x) = −σ∂_kf + ½∂_k²f` exactly (`σ = ±1`), so the streaming operator is `(1/√3)[−s·∇f + ½Σ_k|s_k|∂_k²f]`. For a smooth field the same expression is its expansion to second order in gradients. ∎

The first term is transport along the content, the same in every direction. The second is a diffusion along each lattice axis with the coefficient `|s_k|/(2√3)`: it comes from the hops being of one lattice step along an axis, and it is there without any scattering.

## Theorem T2 — the moments, and the viscous term of cubic symmetry

Over the uniform sphere one coordinate is uniform on `[−1, 1]` and, given it, the square of another averages half of what is left. Hence `⟨|s_k|⟩ = 1/2`, `⟨s_i²|s_i|⟩ = 1/4`, `⟨s_i²|s_k|⟩ = (1/2)(1/2 − 1/4) = 1/8` for `k ≠ i`, and moments odd in a coordinate vanish. In local equilibrium the second-order term of T1 therefore contributes

- to the number equation `(1/(2√3))(1/2)∇²n = D_lat∇²n`, `D_lat = 1/(4√3)`;
- to the equation of `g_i`: `(1/(2√3))·3·Σ_k⟨s_i²|s_k|⟩∂_k²g_i = (3/(2√3))[(1/8)∇²g_i + (1/8)∂_i²g_i] = ν_lat(∇²g_i + ∂_i²g_i)`, `ν_lat = √3/16`, no sum over `i` in the last term.

The operator `∂_i²g_i` is invariant under the symmetries of the cube and not under rotations: a longitudinal wave of wave vector `q` along the unit vector `n̂` is damped at the rate `ν_lat q²(1 + Σ_i n̂_i⁴)`, that is `2`, `3/2`, `4/3` times `ν_lat q²` along an axis, a face diagonal and a body diagonal, where any isotropic viscous operator damps it equally in every direction. ∎

Scattering adds a viscosity `ν_coll` that comes from the departure of the content law from local equilibrium. To the extent that this part is isotropic (the first-order transport `s·∇` is isotropic on the sphere menu; not proved here), the viscous operator is `ν(∇²g_i + η∂_i²g_i)` plus an isotropic gradient of the divergence, with `ν = ν_lat + ν_coll` and `η = ν_lat/(ν_lat + ν_coll)` between 0 and 1. `ν_coll` is not computed here; in kinetic theory more scattering makes it smaller, and `η` larger.

## Theorem T3 — the potential inflow does not solve the creeping equations

Let `g = ∇χ` with `∇²χ = 0`. Then `∇²g = 0`, the divergence of `g` vanishes, and the viscous term reduces to `νη(∂_x³χ, ∂_y³χ, ∂_z³χ)`. The momentum equation asks for a pressure with `∇P` equal to that field, which requires its curl to vanish. It does not: for the harmonic polynomial `χ = x⁵ − 10x³y² + 5xy⁴` the component of the curl along `z` is `∂_x∂_y³χ − ∂_y∂_x³χ = 240y`; for `χ = 1/r` it is `−105xy(x² − y²)/r⁹`, which is `70/2187` at `(1, 2, 2)`. So for `η ≠ 0` no pressure balances the viscous stress of a potential inflow, and the stationary creeping wind is not the potential flow of blocks 45 and 46. ∎

## Theorem T4 — the creeping inflow, its scaling and its circulation

In wave-vector space the creeping equations read `ik·ĝ = −Ŝ` and `−ik_iP̂ − ν(k² + ηk_i²)ĝ_i = 0`. Their solution is `ĝ_i = −ik_iP̂/(ν(k² + ηk_i²))` with `P̂ = νŜ/Σ_i[k_i²/(k² + ηk_i²)]` (up to the sign convention of the sink). For a point sink `Ŝ` is constant, and `ĝ(λk) = ĝ(k)/λ`: the inflow is homogeneous of degree `−2` in the distance, `g(x) = f(x̂)/r²`. A radial field `f(x̂)x̂/r²` has no divergence away from the origin whatever `f`, so the conservation of records does not constrain `f` beyond its mean. For `η = 0`, `ĝ = −ikŜ/k²`: the potential flow. For `η > 0`, `k × ĝ ≠ 0` at generic wave vectors (at `η = 1/2`, `k = (1, 2, 0)`: `ĝ ∝ (7/29, 11/29, 0)`, `k × ĝ ∝ (0, 0, −3/29)`): the wind has circulation. ∎

Two consequences. The direction dependence is not a near-field effect: it has the same size at every distance at which the flow is creeping. And it is a property of creeping flow: when inertial forces dominate viscous ones the viscous term is negligible outside thin layers and the potential flow returns; in every flow executed in blocks 44 to 49 the ratio of inertial to viscous forces is below `0.1` (block 45).

## Executed: the wind of one capturing body by direction, and the angular function of the creeping solution (not proved)

Control `specs/supervisor_control_block51_wind_by_direction.py` (sphere menu; one capturing body, a ball of radius 3 filled to `0.18`, about 22 sites, at the centre of an open box of side 64 with a reservoir at the walls; eight seeds per case; the mean momentum density is accumulated over the run). The table gives the inward momentum density times `r²` over the capture rate, averaged over the sites with `r` from 6 to 10 in each direction class.

| case | axes | face diagonals | body diagonals | axes over body diagonals |
|---|---|---|---|---|
| `ρ = 0.1`, `γ = 0`, 40000 ticks | `0.1798 ± 0.0025` | `0.1426 ± 0.0011` | `0.1158 ± 0.0034` | `1.55 ± 0.05` |
| block 48's exact first-order values, times `1/(1 − ρ)` | `0.176` | `0.147` | `0.122` | `1.445` |
| `ρ = 0.1`, `γ = 2`, 20000 ticks | `0.1754 ± 0.0017` | `0.1485 ± 0.0017` | `0.1304 ± 0.0021` | `1.35 ± 0.03` |
| `ρ = 0.3`, `γ = 1`, 12000 ticks | `0.2225 ± 0.0027` | `0.1858 ± 0.0018` | `0.1717 ± 0.0019` | `1.30 ± 0.02` |
| isotropic closure `√3/(4π(1 − ρ))` | `0.153` at `ρ = 0.1`; `0.197` at `ρ = 0.3` | the same | the same | `1` |

The first two rows calibrate the measurement: without scattering the three classes agree within 2 to 5 per cent with the exact multinomial shadow of block 48 summed over the body's sites (the factor `1/(1 − ρ)` is the exclusion factor of block 44's current). At these distances the first-order values are far from block 48's leading term, whose order along the classes they reverse; block 48 had recorded that the remainder is large there. The averages over the three classes weighted by their solid angles are `0.97` and `0.96` of the isotropic value in the two cases with scattering, as the conservation of records requires of the full average.

A first batch at `r` from 10 to 22 in the same box gave `1.34 ± 0.06` without and `1.29 ± 0.10` with scattering, but with scattering the reservoir walls at distance 30 distort a creeping flow by an amount that grows as the fifth power of the distance over the distance to the wall; it is kept in the control's output and not used.

Control `specs/supervisor_control_block51_cubic_inflow.py` (the creeping equations solved in wave-vector space on a periodic grid, the sink smeared over 1.5 to 2 sites; `η = 0` comes out isotropic to one part in a thousand). Inflow times `r²` over its mean, axes / face diagonals / body diagonals:

| `η` | `r` 6 to 10 (grid `128³`) | `r` 12 to 20 (grid `192³`) | `r` 20 to 32 (grid `192³`) |
|---|---|---|---|
| `1/4` | `1.10, 0.98, 0.93` (ratio `1.18`) | ratio `1.23` | ratio `1.26` |
| `1/2` | `1.20, 0.96, 0.87` (ratio `1.37`) | ratio `1.48` | ratio `1.54` |
| `1` | `1.36, 0.92, 0.77` (ratio `1.76`) | ratio `2.01` | ratio `2.18` |

The ratio does not fall with distance; it rises slightly as the smearing of the sink matters less. The executed winds with scattering, over the mean of their classes, are `1.18, 1.00, 0.88` (`ρ = 0.1`, `γ = 2`) and `1.17, 0.98, 0.90` (`ρ = 0.3`, `γ = 1`): the pattern of `η` between about `0.3` and `0.5`.

## No-Go Discipline Gate

The note's negative sentences: the viscous term of the gas is not isotropic; the potential inflow does not solve the creeping equations; the direction dependence of the creeping wind does not decay with distance; the isotropy assumed in blocks 45 to 48 does not hold for the flows executed.

### N1 — Routes by which the sentences could fail
1. *Fast flows* (inertial forces dominating viscous ones) — outside thin viscous layers the flow is a potential flow and isotropic; none of the campaign's executed flows is there (all below `0.1`), and whether a body large enough to reach that regime exists inside the other limits of blocks 47 to 49 is not examined.
2. *A clause with isotropic second-order streaming* — hops to more neighbours (face and body diagonals with suitable rates) can make the fourth-rank moment isotropic, as the classical cure for lattice gases does; block 44's clause hops along axes only. Not worked.
3. *The exclusion at finite density* — T2 is for small density; at density `0.3` the executed dependence on direction is as large as at `0.1`.
4. *The six-axis menu* — its second-order flux already has no isotropic form (block 45); it is not better.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
T2 assumes local equilibrium and small density; T3 and T4 are about the linear stationary equations; the identification of the executed winds with a value of `η` is a comparison of patterns, not a derivation. Declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | permanence | yes (premise) |
| block 01 (`main`) | the menus | yes (premise, proposed) |
| block 44 (open PR #8550) | the streaming rule; the pressure | yes (restated) |
| blocks 45, 46 (open PRs #8553, #8554) | the isotropic closure and the zero-circulation assumption that this note corrects | corrected |
| blocks 47, 48 (open PRs #8556, #8558) | the on-axis forces; the exact shadow used for calibration; the sentence on collisions that this note withdraws | corrected |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the streaming operator to second order; moments `1/2, 1/4, 1/8`; `ν_lat = √3/16` with equal cubic and isotropic parts; damping `2 : 3/2 : 4/3`; the cubic term on a potential flow is not a gradient; the creeping solution is homogeneous with circulation" | executed: the operator on fields of degree two for 150 rational unit contents; the moments | not applicable | executed: the creeping solution at five wave vectors and three values of `η`: both equations, homogeneity, `k × g` | executed: `ν_lat² = 3/256`, `D_lat² = 1/48`; the curls `240y` and `70/2187` | T1 exact on fields of degree two; T2 local equilibrium at small density; T3, T4 exact for the creeping equations; winds and angular function executed only |

### N6 — Partial-closure paths and primitive scan
The registered `kinetic_isotropy_primitive` grants only a structural isotropy of a kinetic form (`c_t = c_s`) and supplies no dynamics; it does not make the viscous stress of this gas isotropic and is not used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "A 30 per cent effect measured at six to ten sites from a body is a near-field artefact." Reply: T4 is the answer: in creeping flow nothing sets a length, and the executed calibration without scattering shows the measurement reproduces an exact prediction in all three classes; the solution on the grid has the same ratio at 6 to 10, 12 to 20 and 20 to 32. Second objection: "Then blocks 45 and 47 are wrong." Reply: their theorems are stated inside a closure with spherical symmetry and stand as such; what falls is the reading that the executed on-axis forces confirm one coefficient in every direction, and block 48's sentence that collisions supply it. The corrections are posted on those PRs.

### N8 — Cross-cycle echo
Block 45 found the six-axis menu's second-order flux to have no isotropic form and turned to the sphere menu for isotropy; the sphere menu is isotropic in its contents, but its records still hop along axes, and the lattice returns through the second-order streaming term. Block 48 met the same fact without collisions (capture and shadow weighted by `|s|₁`). The pattern: in this lane every long-range statement has been exact about the lattice and only approximately about the sphere.

## Falsifiers

- A field of degree two and a content for which the streaming operator differs from T1's expression; sphere moments other than `1/2, 1/4, 1/8`.
- A pressure that balances the viscous term of cubic symmetry acting on the potential inflow; a solution of the creeping equations with `η > 0` whose direction dependence decays with distance.
- For the executed part: winds with scattering that are equal in the three direction classes within errors at distances where the walls do not matter, in a flow whose ratio of inertial to viscous forces is below `0.1`.

## Boundaries and non-claims

One body size and one shell for the executed winds; three parameter sets; the far shells are contaminated by the walls and not used. `η` is not computed: the collisional viscosity and the effect of exclusion on `ν_lat` are open. The force between two capturing bodies off the lattice axes is not executed; by T4 and block 48's capture law it depends on direction, and its coefficient by direction is not given here. Flows in which inertial forces dominate are not examined. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the sentence quoted under Premises. Block 01 (on `main`): the menus; proposed, unaudited. Blocks 44 to 48 (PRs #8550, #8553, #8554, #8556, #8558, open): restated, used for calibration, or corrected.
- Named standard imports at definition level: the expansion of a difference to second order (Taylor), exact on polynomials of degree two; moments of the uniform sphere (Archimedes); the Fourier transform of a linear equation with constant coefficients; the curl of a gradient vanishes.
- Reference only: Hardy, Pomeau and de Pazzis; Frisch, Hasslacher and Pomeau; Chapman and Enskog; Stokes; Reynolds.

## Review record
Supervisor-run block of the 12-hour campaign. It began as a control meant to show an executed form of block 48's sentence that collisions restore one coefficient in every direction. The first batch (distances 10 to 22) showed a direction dependence with scattering as large as without; the supervisor attributed it to the walls, moved to distances 6 to 10 where that effect is negligible, and found `1.35 ± 0.03`. The calibration without scattering against block 48's exact shadow (2 to 5 per cent in all three classes) ruled out the measurement. The cause was then found in the second-order term of the streaming operator, the creeping equations were solved, and the run at the parameters of blocks 45 and 47 (`1.30 ± 0.02`) was made last. Refuting pass (`specs/supervisor_control_block51_refuter.py`, machinery disjoint from the runner's): W1 the expansion symbolically; W2 the moments by symbolic integration; W3 the curl for `1/r` symbolically (`−105xy(x² − y²)/r⁹`); W4 the discrete streaming operator on a longitudinal local-equilibrium wave by quadrature: damping along an axis, a face diagonal, a body diagonal as `2 : 3/2 : 4/3`; W5 the Fourier solution on a `96³` grid: isotropic at `η = 0`, the ratio `1.44` and `1.51` in two shells at `η = 1/2`. All pass. One finding folded: the first form of W4 compared a longitudinal with a transverse wave along one axis (ratio 2), which an isotropic operator with a suitable bulk viscosity also gives; it was replaced by the comparison of directions, and the runner gained the matching exact check. Mutation census: 8 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_wind_of_a_capturing_body_is_not_isotropic_lattice_streaming_viscous_term_of_cubic_symmetry_2026_09_21.py
```

Expected: `TOTAL: PASS=15 FAIL=0`.
