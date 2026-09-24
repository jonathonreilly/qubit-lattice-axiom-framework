---
claim_id: admissibility_rule_the_wind_law_flux_theorems_inverse_square_wind_of_a_capturing_body_second_order_momentum_flux_force_proportional_to_product_of_capture_rates_bounded_theorem_note_2026-09-20
claim_type: bounded_theorem
claim_scope: "Conditional on the supplied inertial gas. Exact finite generator identities give number and momentum flux conservation. A spherical stationary continuum closure gives the inverse-square mean inflow, not pointwise isotropy of the lattice gas. The sphere product-state momentum flux has the stated second-order coefficients; the six-axis flux includes -g_i g_j despite diagonal single-record second moments. The inviscid force is A q g1/sqrt(3), subject to potential flow and pressure closure. Capture gives Q u only for the stated first-harmonic content law and balanced axis faces (or an explicitly unbiased capture model). No hydrodynamic limit or general force law is proved. Historical simulations are author reports, not fresh evidence."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_the_wind_law_flux_theorems_inverse_square_wind_second_order_momentum_flux_force_product_of_capture_rates_2026_09_20.py
---

# Finite flux identities and conditional wind-force coefficients for the supplied inertial gas

**Date:** 2026-09-20
**Type:** bounded_theorem
**Status:** bounded-support (exact identities and exact product-state fluxes for a supplied clause; the wind and the forces executed, not claimed; nothing adopted or registered; unaudited)

This note works within the supplied inertial clause of block 44 and derives what that clause implies for the flow around capturing bodies; neither the clause nor anything here is adopted.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Conditional on the supplied inertial gas. Exact finite generator identities give number and momentum flux conservation. A spherical stationary continuum closure gives the inverse-square mean inflow, not pointwise isotropy of the lattice gas. The sphere product-state momentum flux has the stated second-order coefficients; the six-axis flux includes -g_i g_j despite diagonal single-record second moments. The inviscid force is A q g1/sqrt(3), subject to potential flow and pressure closure. Capture gives Q u only for the stated first-harmonic content law and balanced axis faces (or an explicitly unbiased capture model). No hydrodynamic limit or general force law is proved. Historical simulations are author reports, not fresh evidence.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "owner, 2026-09-20: 'run a 12 hour campaign on this lane please'; block 44's executed inverse-square attraction between capturing bodies; the record-pair source note on main: a local conservation law consumed by the same carrier, and an absolute source/response law"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the attraction of capturing bodies is traced to exact local conservation (the wind), an exact second-order flux and a closure coefficient bracketed by the executed force; next: transparent bodies (is the capture rate proportional to the record count in the dilute limit), the drag on a moving body (the same coupling), and the six-axis menu's anisotropy; loaded on ai/probes"
conditional_surface_status: "T1, T2, T4 exact; T3 is a statement in the local-equilibrium closure with spherical symmetry; T5 gives the inviscid and the free-streaming values; the wind profile and the forces (floating point, side 96, 8000 ticks, one seed each unless stated) are in the controls and not claimed"
hypothetical_axiom_status: "the inertial clause of block 44, including its scattering, which re-draws contents; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full) is used through "A site never carries more than one record; records are permanent." Block 01 (on `main`, proposed and unaudited) supplies the menus. Block 44 (open PR #8550) supplies the clause, its conservation laws, the stationarity of the uniform measure and the product-state current and pressure; they are restated, and this note's runner re-derives what it uses.

- **The clause** (block 44): (S) a record steps along its content; an occupied target exchanges contents with it; (C) a bond re-draws its pair of contents uniformly on their momentum class at rate `γ`. Sphere menu: steps with probability `max(0, s·e_k)/√3`.
- **Capturing body.** A set of solid sites; a record that steps onto one joins the body, which takes up its momentum. Capture rate `Q`.
- **Current and momentum flux.** `j(x→y) = [record at x pointing to y, y empty] − [record at y pointing to x, x empty]`. The momentum flux across a bond adds: `e_d` for a record moving across it; `e_d − e_{d'}` for an exchange; and for scattering the mean momentum passed, `e(s_x)` for an opposite pair and `(e(s_x) − e(s_y))/2` otherwise, times `γ`.
- **Local-equilibrium closure.** The gas is locally in a product state with density `ρ` and tilted contents (one-site weight `exp(λ·s)`), momentum density `g = ρ⟨s⟩`.
- **`K`.** For two capturing bodies at distance `r`, `K = F r²/(Q₁Q₂)`; the simple estimate is `K₀ = √3/(4π ρ(1−ρ))`.

The flux theorem is that of Gauss; the pressure adjustment at second order is the relation of Bernoulli; the tilted sphere state's first moment is the function of Langevin; potential flow into sinks as a picture of attraction goes back to Riemann and Bjerknes, the shadow picture to Le Sage, and the statement that capture follows the surface of an opaque body is the classical objection to both; capture limited by transport is the problem of Smoluchowski. None is used as authority.

## Prior art and what is new

Continuity equations, the flux theorem, potential flow into sinks and the attraction between sinks are classical. What is new is their exact form for this clause under one record per site: the current observable with its blocking factor, the momentum flux with its exchange term, the exact second-order coefficient `A = (3/5 − ρ)/ρ` with its sign change, the anisotropic diagonal second moments of the six-axis menu together with its exchange term -g_i g_j, and the executed confirmation of the wind to a few per cent with no free parameter and of `F = K Q₁Q₂/r²` with `K` between the two computed limits.

## Exact target and obligation graph

Target: explain block 44's executed inverse-square attraction. Obligations: (O1) local conservation of number; (O2) of momentum; (O3) the wind's coefficient; (O4) the second-order flux; (O5) the force coefficient in the two computable cases. T1–T5 discharge them at their stated levels; the controls execute the wind and the forces.

## Theorem T1 — number is conserved locally; a capturing body draws its capture rate through every surface

An occupancy changes only when a record moves across a bond, which happens when a record points along the bond and the target is empty; an exchange leaves both ends occupied and scattering moves nothing. So `d n_x/dt`, in the sense of the generator, is `−Σ_{y∼x} j(x→y)` with `j` as declared, for every configuration. Summing over the free sites between a capturing body and a closed surface around it, in a stationary state the mean current through the surface equals the mean capture rate `Q`. For the cube of half-side `R` the surface is crossed by `6(2R+1)²` bonds: the mean current per crossing bond is `Q/(6(2R+1)²)`. ∎

## Theorem T2 — momentum is conserved locally; the force on a body is the flux through any surface around it

Each event moves momentum across one bond only: a moving record carries `e_d`; an exchange replaces `e_d` by `e_{d'}` at the near end and the reverse at the far end; a re-drawing changes the two ends by opposite amounts, `e(s_x)` on average for an opposite pair and `(e(s_x) − e(s_y))/2` otherwise. So the rate of change of the momentum at `x` is minus the sum over its six bonds of the declared flux, for every configuration, and in a stationary state the mean momentum absorbed by a body per unit time equals the mean flux through any surface enclosing it and no other body. ∎

Both identities are checked at every site of all `12636` two-record configurations of the `3³` torus, and by a second implementation on `4000` random three-record configurations at another scattering rate.

## Theorem T3 — the wind of a capturing body (closure)

In the local-equilibrium closure the mass current is `J = (1 − ρ) g/√3` (block 44, T3). For a stationary, spherically symmetric inflow T1 gives `4π r² |J| = Q`, hence `g(r) = √3 Q/(4π r² (1 − ρ))`, directed inwards. ∎

Executed (control `specs/supervisor_control_block45_wind.py`; one capturing body of radius 3, side 96, density `0.3`, `γ = 1`, `Q = 7.84`): inward momentum density against `√3 Q⟨1/r²⟩/(4π(1−ρ))` in shells.

| shell (mean `r`) | density | measured | predicted | ratio |
|---|---|---|---|---|
| 6–8 (7.1) | `0.2888` | `0.03061` | `0.03115` | `0.983` |
| 8–11 (9.6) | `0.2899` | `0.01694` | `0.01691` | `1.002` |
| 11–15 (13.2) | `0.2901` | `0.00893` | `0.00901` | `0.991` |
| 15–20 (17.7) | `0.2899` | `0.00497` | `0.00496` | `1.003` |
| 20–27 (23.8) | `0.2900` | `0.00267` | `0.00274` | `0.974` |
| 27–36 (31.9) | `0.2899` | `0.00151` | `0.00153` | `0.991` |

## Theorem T4 — the momentum flux to second order in the wind

The uniform sphere has `⟨s_z²⟩ = 1/3`, `⟨s_z⁴⟩ = 1/5`, `⟨s_x² s_z²⟩ = 1/15`. Expanding the one-site weight `exp(λ·s)`, `⟨s_i s_j⟩_λ = δ_ij/3 + (1/2) λ_k λ_m (⟨s_i s_j s_k s_m⟩ − ⟨s_i s_j⟩⟨s_k s_m⟩) + … = δ_ij/3 + λ_iλ_j/15 − δ_ij λ²/45`, and `⟨s⟩ = λ/3` to first order. In a product state the streaming flux is `ρ(1−ρ)⟨s_i s_j⟩/√3` and the exchange flux `ρ²(⟨s_i s_j⟩ − ⟨s_i⟩⟨s_j⟩)/√3` (block 44, T3); with `g = ρλ/3`, `√3 Π_ij = (ρ/3)δ_ij + A g_i g_j + B g² δ_ij`, `A = (3/5 − ρ)/ρ`, `B = −1/(5ρ)`. A gas without exclusion would have `A = 3/(5ρ)`; one record per site lowers it by one and makes it negative above `ρ = 3/5`. For the six-axis menu no content has two non-zero components, `⟨s_i s_j⟩` is diagonal, `⟨s_1²⟩ = 1/3 + λ_1²/9 − (λ_2² + λ_3²)/18`, and the full flux is rho< s_i s_j >-g_i g_j in six-axis rate units; off-diagonal entries are -g_i g_j. ∎

## Theorem T5 — the force of a wind on a capturing body: the inviscid value and the free-streaming value

*Inviscid value.* Around a body drawing the inflow `g₂ = −q n/(4π R²)` in a uniform wind `g₁`, the second-order momentum balance of an irrotational, divergence-free flow fixes the pressure, `δp = −(A/2 + B) g² + const`, so the isotropic coefficient becomes `B_eff = −A/2`. The cross term of the flux through a sphere is `A[g₁(g₂·n) + g₂(g₁·n)] + 2B_eff (g₁·g₂) n`, whose integral, with `⟨n_i n_j⟩ = δ_ij/3`, is `−A q g₁ (1 + 1/3 − 1/3)`: the body is pushed along the wind with the force A q g1/sqrt(3), since the displayed stress is sqrt(3) times the physical momentum flux. With `q = √3 Q₂/(1 − ρ)` this is `(3/5 − ρ)/(1 − ρ)` times `Q₂ g₁/ρ`: `31/71` at `ρ = 29/100`, zero at `3/5`, `−3/5` at `3/4`.

*Capture closure.* For a homogeneous first-harmonic content law and a body with equal exposed-face counts along all three axes, the capture-weight moments in the companion capture note give F=Q2 g1/rho. General forward-hop capture weights contents by |s|_1; it is not an unbiased sample for every law or shape. The constant-projected-area argument is withdrawn.

With the wind of T3, the force between two capturing bodies is `K Q₁Q₂/r²` with `K = K₀ = √3/(4π ρ(1−ρ))` for that capture closure and `K = K₀ (3/5 − ρ)/(1 − ρ)` for the inviscid value; at `ρ = 0.29`, `0.67` and `0.29`.

**Historical interpretation, not a proved regime selection.** The inviscid value is that of a flow in which the second-order flux dominates the viscous stress. With the damping of sound executed in block 44 (`0.0030` per tick at wavelength 64, a diffusivity of about `0.6`) and winds of `0.003` to `0.015` at the executed separations, a body of radius 3 has a Reynolds number between `0.01` and `0.07`: the executed flows are viscous, a net force on a body is carried to the far field by viscous stress at first order in the wind, and the far-field calculation above does not determine it. The executed forces are therefore compared with the free-streaming value, and the inviscid value is recorded as what it is.

## Historical author observations (not fresh evidence): the force between capturing bodies (not proved)

Control `specs/supervisor_control_block45_bodies.py` (sphere menu, side 96, density `0.3`, `γ = 1`, 8000 ticks; a body is a ball of radius `R` in which each site is solid with probability `f`). Separation 20 unless stated; forces per tick towards the other body.

| bodies | solid sites | `Q₁`, `Q₂` | `F₁`, `F₂` | `K = F r²/(Q₁Q₂)` |
|---|---|---|---|---|
| `R = 5`, `f = 0.1` pair | 51, 43 | `9.4`, `8.3` | `0.119 ± 0.017`, `0.108 ± 0.023` | `0.58` |
| `R = 5`, `f = 0.3` pair | 164, 146 | `17.8`, `16.9` | `0.356 ± 0.032`, `0.387 ± 0.017` | `0.50` |
| `R = 5`, `f = 1` pair | 515, 515 | `21.8`, `21.7` | `0.646 ± 0.025`, `0.588 ± 0.028` | `0.52` |
| `f = 0.1` against `f = 1` (`R = 5`) | 51, 515 | `9.3`, `21.9` | `0.298 ± 0.018`, `0.253 ± 0.029` | `0.54` |
| `R = 3` pair | 123, 123 | `7.9`, `7.8` | `0.107 ± 0.012`, `0.085 ± 0.020` | `0.63` |
| `R = 2` against `R = 4` | 33, 257 | `3.2`, `13.2` | `0.073 ± 0.012`, `0.030 ± 0.022` | `0.49` |
| `R = 2` pair | 33, 33 | `3.2`, `3.2` | `0.006 ± 0.007`, `0.011 ± 0.008` | not resolved |
| `R = 3` pairs at separations 12, 16, 24, 32, 40 (block 44's control) | 123 | `7.8` | `0.237, 0.144, 0.065, 0.043, 0.023` | `0.56, 0.60, 0.62, 0.72, 0.60` |

Against density and scattering rate (solid balls of radius 3 at separation 16; `K₀` at the nominal density):

| density | `γ` | `Q` | `F₁`, `F₂` | `K` | `K/K₀` | inviscid `K/K₀` |
|---|---|---|---|---|---|---|
| `0.15` | 1 | `3.9` | `0.074 ± 0.011`, `0.056 ± 0.012` | `1.11` | `1.02` | `0.53` |
| `0.3` (second seed) | 1 | `7.8` | `0.168 ± 0.017`, `0.150 ± 0.017` | `0.67` | `1.0` | `0.44` |
| `0.5` | 1 | `11.9` | `0.244 ± 0.008`, `0.193 ± 0.014` | `0.40` | `0.72` | `0.20` |
| `0.75` | 1 | `15.0` | `0.391 ± 0.013`, `0.354 ± 0.022` | `0.42` | `0.57` | `−0.60` |
| `0.3` | `0.1` | `6.5` | `0.123 ± 0.018`, `0.126 ± 0.017` | `0.75` | `1.13` | `0.44` |
| `0.3` | `4` | `7.4` | `0.121 ± 0.018`, `0.125 ± 0.009` | `0.57` | `0.87` | `0.44` |

Capture rate against record count at `R = 5`: `9.4, 17.8, 21.8` for `51, 164, 515` solid sites; against radius for solid balls: `3.2, 7.8, 13.2, 21.8` at `R = 2, 3, 4, 5`, close to the square of the radius.

## No-Go Discipline Gate

The note's negative sentences: the capture rate of these bodies is not proportional to their number of records (executed); the six-axis second moment is diagonal, but the full flux contains -g_i g_j.

### N1 — Routes by which the sentences could fail
1. *Transparent bodies* — for bodies so dilute that a record of the gas rarely meets two of their sites the capture rate should be proportional to the record count; the forces are then too small for the runs made here. Not executed.
2. *Another scattering clause for the six axes* — diagonality of the single-content second moment is a property of the six-axis menu; it does not remove the exchange contribution -g_i g_j; a clause whose equilibrium is not a product state is outside this note.
3. *The closure* — T3 assumes local equilibrium and the executed wind supports it at the level of a few per cent. T5's inviscid value is not supported by the executed forces and is not claimed for them; whether it is approached at large Reynolds number is not executed.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond block 44's clause, declared, including its re-drawing of contents.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | permanence: number is conserved | yes (premise) |
| block 01 (`main`) | the menus | yes (premise, proposed) |
| block 44 (open PR #8550) | the clause; stationarity of the uniform measure; product-state current and pressure | yes (restated; the runner re-derives what it uses) |
| the record-pair source note (`main`) | the list of missing pieces | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "number and momentum are conserved locally with explicit fluxes; the second-order flux has `A = (3/5 − ρ)/ρ`; the closure force is `(3/5 − ρ)/(1 − ρ)` of the simple estimate" | executed: the sphere's moments `1/3, 1/5, 1/15`; the six-axis second moments | executed: both identities at every site of all 12636 configurations | not applicable | executed: 20 rational tilts; flux coefficients at three densities; force coefficient at four | T1, T2 identities of the generator on every lattice; T4 exact for product states; T3, T5 in the closure; wind and forces executed only |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no update law and no capture clause. Nothing here is proposed for registration.

### N7 — Steelman
Hostile reviewer: "Sinks in a fluid attract; this has been known since the nineteenth century and was abandoned as a theory of gravitation." Reply: agreed, and the note claims no gravitation. What it adds to the campaign is exact: the conservation laws of a clause written in the campaign's own vocabulary, the coefficient of the wind with the blocking factor of one record per site, the second-order coefficient with its sign change, and an executed law whose "charge" is identified, the capture rate, together with the executed fact that for dense bodies this is not the record count. Whether anything in the axioms makes matter capture records, and transparent enough for the rates to add, is the question this leaves.

### N8 — Cross-cycle echo
Block 41's production halo was the same flux theorem for a walk; block 42's capacity was the same failure of sources to add for bodies that are not transparent; block 44's exact current is what fixes the wind's coefficient.

## Falsifiers

- A configuration and a site at which the rate of change of occupancy or momentum differs from minus the divergence of the declared observables.
- A tilt for which the second moments of the sphere state differ from `δ_ij/3 + λ_iλ_j/15 − δ_ij λ²/45` at second order.
- For the executed part: a wind profile departing from `√3 Q/(4π r²(1−ρ))` by more than the statistical error at large `r`; a pair of capturing bodies whose forces are not equal within the errors; at low density, a `K` that differs from `K₀`.

## Boundaries and non-claims

No hydrodynamic limit is proved. The inviscid value of T5 is an exact consequence of the second-order flux and is not the force in the executed, viscous flows. The force law is executed with one seed per entry (two at the reference point); errors are standard errors over ten blocks of one run. The capture rate is not the record count for the bodies executed. The clause re-draws contents (block 44's caveat). The drag on a moving body, which by T5 is the same coupling, is not executed. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the sentence quoted under Premises. Block 01 (on `main`): the menus; proposed, unaudited. Block 44 (PR #8550, open): restated.
- Named standard imports at definition level: the flux theorem for a lattice divergence; moments of the uniform measure on the sphere; the second-order expansion of a tilted measure; potential flow of a divergence-free irrotational field.
- Reference only: Gauss, Bernoulli, Langevin for the named relations; Riemann, Bjerknes, Le Sage for the pictures of attraction; Smoluchowski for transport-limited capture.

## Review record — original author provenance
Supervisor-run block of the 12-hour campaign. Lens: block 44's executed inverse-square force needed a reason; records are conserved, so the reason had to be a flux theorem, and the coefficient had to come from block 44's exact current. The simple estimate (a body takes up the mean momentum of what it captures) matched the first data within ten per cent; a second-order calculation in the closure then gave less than half of it, so the estimate was not the collision-dominated answer; the free-streaming argument showed it is the other limit, and the executed `K` lies between the two. A batch designed to tell "product of capture rates" from "wind times size" (a light porous body against a heavy one of the same radius) came out for the product. A third batch was designed to confirm the supervisor's expectation that the second-order value is approached as scattering grows and that the force reverses above `ρ = 3/5`; it refuted both (`K/K₀ = 0.87` at `γ = 4`; `+0.57` at `ρ = 0.75`). The reason is the Reynolds number, below `0.1`: T5's second-order value is the inviscid one. The theorem was re-scoped and the note rewritten before the gates. Refuting pass (`specs/supervisor_control_block45_refuter.py`, machinery disjoint from the runner's): W1 both continuity identities from configuration differences on 4000 random three-record configurations at scattering rate `3/2`; W2 closed forms of the tilted moments and `A`, `B`; W3 the force by symbolic integration over the sphere, with and without the pressure term; W4 the six-axis second moments. All pass. Mutation census: 10 mutations, each failing in its own family only. The first version of the runner's momentum-flux observable was wrong and failed its own check; rewritten. Author checks only; no independent review has taken place.

## Current review boundaries and dependencies

Conditional on the supplied inertial gas. Exact finite generator identities give number and momentum flux conservation. A spherical stationary continuum closure gives the inverse-square mean inflow, not pointwise isotropy of the lattice gas. The sphere product-state momentum flux has the stated second-order coefficients; the six-axis flux includes -g_i g_j despite diagonal single-record second moments. The inviscid force is A q g1/sqrt(3), subject to potential flow and pressure closure. Capture gives Q u only for the stated first-harmonic content law and balanced axis faces (or an explicitly unbiased capture model). No hydrodynamic limit or general force law is proved. Historical simulations are author reports, not fresh evidence.

Historical simulations and auxiliary refuters remain on original branch head `e07ae767d484763bd9446eb2d5c4c9b05643dd1c`; their reported values are preserved but not freshly verified by this canonical runner. Companion links identify supplied mathematical models, not audited physical authority.

- [Companion model and limitations](ADMISSIBILITY_RULE_RECORDS_WITH_INERTIA_CONTENT_AS_DIRECTION_OF_TRAVEL_CONSERVED_MOMENTUM_STRUCTURELESS_EQUILIBRIUM_SOUND_SPEED_FORCES_NEED_CAPTURE_OR_EMISSION_BOUNDED_THEOREM_NOTE_2026-09-20.md)
- [Companion model and limitations](ADMISSIBILITY_RULE_FREE_CAPTURING_BODIES_ARE_CARRIED_BY_THE_WIND_CAPTURE_LAW_ANISOTROPIC_COLLISIONLESS_SHADOW_DILUTION_LAW_OF_MOTION_AND_ITS_WINDOW_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion model and limitations](ADMISSIBILITY_RULE_THE_WIND_OF_A_CAPTURING_BODY_IS_NOT_ISOTROPIC_LATTICE_STREAMING_GIVES_A_VISCOUS_TERM_OF_CUBIC_SYMMETRY_DIRECTION_DEPENDENCE_DOES_NOT_DECAY_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Finite-window rule](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)

## Verification

```bash
python3 scripts/admissibility_rule_the_wind_law_flux_theorems_inverse_square_wind_second_order_momentum_flux_force_product_of_capture_rates_2026_09_20.py
python3 scripts/admissibility_rule_the_wind_law_flux_theorems_inverse_square_wind_second_order_momentum_flux_force_product_of_capture_rates_2026_09_20.py --list-mutations
python3 .claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block45_refuter.py
```
