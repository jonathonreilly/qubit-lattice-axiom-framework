---
claim_id: admissibility_rule_the_wind_of_a_capturing_body_is_not_isotropic_lattice_streaming_gives_a_viscous_term_of_cubic_symmetry_direction_dependence_does_not_decay_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "Conditional dilute independent streaming and first-harmonic local closure. Axis hops have the exact displayed second-order expansion and cubic viscosity term, with nu_lat=sqrt(3)/16. For a separately supplied elliptic creeping continuum model with nu>0 and 0<=eta<=1, a point sink has a homogeneous distributional response of degree -2 away from the origin. For eta>0 the harmonic inverse-distance potential fails its curl compatibility condition; generic wavevectors have circulation. The collision viscosity, actual lattice hydrodynamic limit and universal far field are not derived; historical direction-resolved simulations are author reports."
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

Conditional dilute independent streaming and first-harmonic local closure. Axis hops have the exact displayed second-order expansion and cubic viscosity term, with nu_lat=sqrt(3)/16. For a separately supplied elliptic creeping continuum model with nu>0 and 0<=eta<=1, a point sink has a homogeneous distributional response of degree -2 away from the origin. For eta>0 the harmonic inverse-distance potential fails its curl compatibility condition; generic wavevectors have circulation. The collision viscosity, actual lattice hydrodynamic limit and universal far field are not derived; historical direction-resolved simulations are author reports.

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

The operator `∂_i²g_i` is invariant under the symmetries of the cube and not under rotations: the initial longitudinal projection of a wave along n-hat has damping coefficient `ν_lat q²(1 + Σ_i n̂_i⁴)`, that is `2`, `3/2`, `4/3` times `ν_lat q²` along an axis, a face diagonal and a body diagonal, these symmetry directions are eigenpolarizations; at a generic direction the operator also generates a transverse component. ∎

Scattering adds a viscosity `ν_coll` that comes from the departure of the content law from local equilibrium. To the extent that this part is isotropic (the first-order transport `s·∇` is isotropic on the sphere menu; not proved here), the viscous operator is `ν(∇²g_i + η∂_i²g_i)` plus an isotropic gradient of the divergence, assuming nu_coll>=0, with nu=nu_lat+nu_coll and eta=nu_lat/(nu_lat+nu_coll) in [0,1]. `ν_coll` is not computed here; in kinetic theory more scattering makes it smaller, and `η` larger.

## Theorem T3 — the potential inflow does not solve the creeping equations

Let `g = ∇χ` with `∇²χ = 0`. Then `∇²g = 0`, the divergence of `g` vanishes, and the viscous term reduces to `νη(∂_x³χ, ∂_y³χ, ∂_z³χ)`. The momentum equation asks for a pressure with `∇P` equal to that field, which requires its curl to vanish. It does not: for the harmonic polynomial `χ = x⁵ − 10x³y² + 5xy⁴` the component of the curl along `z` is `∂_x∂_y³χ − ∂_y∂_x³χ = 240y`; for `χ = 1/r` it is `−105xy(x² − y²)/r⁹`, which is `70/2187` at `(1, 2, 2)`. So for `η ≠ 0` no pressure balances the viscous stress of a potential inflow, and the stationary creeping wind is not the potential flow of blocks 45 and 46. ∎

## Theorem T4 — the creeping inflow, its scaling and its circulation

In wave-vector space the creeping equations read `ik·ĝ = −Ŝ` and `−ik_iP̂ − ν(k² + ηk_i²)ĝ_i = 0`. Assume nu>0, 0<=eta<=1 and nonzero k. Their solution is `ĝ_i = −ik_iP̂/(ν(k² + ηk_i²))` with `P̂ = −νŜ/Σ_i[k_i²/(k² + ηk_i²)]`, with the displayed divergence convention ik.g=-S. For a point sink `Ŝ` is constant, and `ĝ(λk) = ĝ(k)/λ`: interpreting the inverse transform as a homogeneous distribution on infinite continuum space, its restriction away from the point source is homogeneous of degree -2 in distance, `g(x) = f(x̂)/r²`. A radial field `f(x̂)x̂/r²` has no divergence away from the origin whatever `f`, so the conservation of records does not constrain `f` beyond its mean. For eta=0, g-hat=+ik S-hat/k²: the potential flow. For `η > 0`, `k × ĝ ≠ 0` at generic wave vectors (at `η = 1/2`, `k = (1, 2, 0)`: g-hat=i S-hat (7/29,11/29,0), and k cross g-hat=i S-hat (0,0,-3/29)): the wind has circulation. ∎

Two consequences. The direction dependence is not a near-field effect: it has the same size at every distance at which the flow is creeping. And it is a property of creeping flow: neglecting viscous stress permits a potential-flow closure, but does not prove that actual solutions become irrotational; in every flow executed in blocks 44 to 49 the ratio of inertial to viscous forces is below `0.1` (block 45).

## Historical author observations (not fresh evidence): the wind of one capturing body by direction, and the angular function of the creeping solution (not proved)

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
1. *Fast flows* (inertial forces dominating viscous ones) — neglecting viscous stress allows a potential-flow ansatz, but irrotationality and isotropy still need boundary and evolution assumptions; none of the campaign's executed flows is there (all below `0.1`), and whether a body large enough to reach that regime exists inside the other limits of blocks 47 to 49 is not examined.
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

One body size and one shell for the executed winds; three parameter sets; the far shells are contaminated by the walls and not used. `η` is not computed: the collisional viscosity and the effect of exclusion on `ν_lat` are open. The force between two capturing bodies off the lattice axes is not executed; the closure suggests directional effects, but no actual two-body force coefficient or limit is derived here. Flows in which inertial forces dominate are not examined. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the sentence quoted under Premises. Block 01 (on `main`): the menus; proposed, unaudited. Blocks 44 to 48 (PRs #8550, #8553, #8554, #8556, #8558, open): restated, used for calibration, or corrected.
- Named standard imports at definition level: the expansion of a difference to second order (Taylor), exact on polynomials of degree two; moments of the uniform sphere (Archimedes); the Fourier transform of a linear equation with constant coefficients; the curl of a gradient vanishes.
- Reference only: Hardy, Pomeau and de Pazzis; Frisch, Hasslacher and Pomeau; Chapman and Enskog; Stokes; Reynolds.

## Review record — original author provenance
Supervisor-run block of the 12-hour campaign. It began as a control meant to show an executed form of block 48's sentence that collisions restore one coefficient in every direction. The first batch (distances 10 to 22) showed a direction dependence with scattering as large as without; the supervisor attributed it to the walls, moved to distances 6 to 10 where that effect is negligible, and found `1.35 ± 0.03`. The calibration without scattering against block 48's exact shadow (2 to 5 per cent in all three classes) ruled out the measurement. The cause was then found in the second-order term of the streaming operator, the creeping equations were solved, and the run at the parameters of blocks 45 and 47 (`1.30 ± 0.02`) was made last. Refuting pass (`specs/supervisor_control_block51_refuter.py`, machinery disjoint from the runner's): W1 the expansion symbolically; W2 the moments by symbolic integration; W3 the curl for `1/r` symbolically (`−105xy(x² − y²)/r⁹`); W4 the discrete streaming operator on a longitudinal local-equilibrium wave by quadrature: damping along an axis, a face diagonal, a body diagonal as `2 : 3/2 : 4/3`; W5 the Fourier solution on a `96³` grid: isotropic at `η = 0`, the ratio `1.44` and `1.51` in two shells at `η = 1/2`. All pass. One finding folded: the first form of W4 compared a longitudinal with a transverse wave along one axis (ratio 2), which an isotropic operator with a suitable bulk viscosity also gives; it was replaced by the comparison of directions, and the runner gained the matching exact check. Mutation census: 8 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Current review boundaries and dependencies

Conditional dilute independent streaming and first-harmonic local closure. Axis hops have the exact displayed second-order expansion and cubic viscosity term, with nu_lat=sqrt(3)/16. For a separately supplied elliptic creeping continuum model with nu>0 and 0<=eta<=1, a point sink has a homogeneous distributional response of degree -2 away from the origin. For eta>0 the harmonic inverse-distance potential fails its curl compatibility condition; generic wavevectors have circulation. The collision viscosity, actual lattice hydrodynamic limit and universal far field are not derived; historical direction-resolved simulations are author reports.

Historical simulations and auxiliary refuters remain on original branch head `031d6e9da47044d650d054568d303f410760fb96`; their reported values are preserved but not freshly verified by this canonical runner. Companion links identify supplied mathematical models, not audited physical authority.

- [Companion model and limitations](ADMISSIBILITY_RULE_RECORDS_WITH_INERTIA_CONTENT_AS_DIRECTION_OF_TRAVEL_CONSERVED_MOMENTUM_STRUCTURELESS_EQUILIBRIUM_SOUND_SPEED_FORCES_NEED_CAPTURE_OR_EMISSION_BOUNDED_THEOREM_NOTE_2026-09-20.md)
- [Companion model and limitations](ADMISSIBILITY_RULE_THE_WIND_LAW_FLUX_THEOREMS_INVERSE_SQUARE_WIND_OF_A_CAPTURING_BODY_SECOND_ORDER_MOMENTUM_FLUX_FORCE_PROPORTIONAL_TO_PRODUCT_OF_CAPTURE_RATES_BOUNDED_THEOREM_NOTE_2026-09-20.md)
- [Companion model and limitations](ADMISSIBILITY_RULE_THE_POTENTIAL_OF_THE_WIND_SOLVES_THE_LATTICE_POISSON_EQUATION_WITH_CAPTURE_RATES_AS_SOURCES_INERTIAL_GAS_HAS_THE_CONSERVED_TENSOR_OF_RADIATION_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion model and limitations](ADMISSIBILITY_RULE_FREE_CAPTURING_BODIES_ARE_CARRIED_BY_THE_WIND_CAPTURE_LAW_ANISOTROPIC_COLLISIONLESS_SHADOW_DILUTION_LAW_OF_MOTION_AND_ITS_WINDOW_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Finite-window rule](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_wind_of_a_capturing_body_is_not_isotropic_lattice_streaming_viscous_term_of_cubic_symmetry_2026_09_21.py
```

Expected: `TOTAL: PASS=15 FAIL=0`.
