---
claim_id: admissibility_rule_the_potential_of_the_wind_solves_the_lattice_poisson_equation_with_capture_rates_as_sources_inertial_gas_has_the_conserved_tensor_of_radiation_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "Conditional finite periodic bond-field identities: zero circulation and prescribed zero-mean divergence determine a current up to three constant components; fixing those determines the Green-function gradient. Curl-free evolution follows in the supplied linear gradient closure, not the exact viscous gas. Six-axis isotropic product states have pressure rho/3 and zero rest trace in the stated units. For nonzero mean momentum J=(1-rho)g breaks generic tensor symmetry; at rest J=g=0 even at finite density. No radiation species, gravity, general stationary potential flow or infinite-volume asymptotic is established."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_the_potential_of_the_wind_lattice_poisson_equation_capture_rates_as_sources_conserved_tensor_of_radiation_2026_09_21.py
---

# Finite periodic potential currents and rest-state tensor identities in the supplied inertial gas

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within a supplied clause; a correspondence of form, not a claim; nothing adopted or registered; unaudited)

This note works within the supplied inertial clause of block 44 and states a correspondence of form with the weak-field packet on main; neither the clause nor the correspondence is adopted, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Conditional finite periodic bond-field identities: zero circulation and prescribed zero-mean divergence determine a current up to three constant components; fixing those determines the Green-function gradient. Curl-free evolution follows in the supplied linear gradient closure, not the exact viscous gas. Six-axis isotropic product states have pressure rho/3 and zero rest trace in the stated units. For nonzero mean momentum J=(1-rho)g breaks generic tensor symmetry; at rest J=g=0 even at finite density. No radiation species, gravity, general stationary potential flow or infinite-volume asymptotic is established.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "owner, 2026-09-20: 'run a 12 hour campaign on this lane please'; the record-pair source note on main: the shortest remaining positive bridge must identify the branchwise Record source and supply an absolute source/response/unit law consumed by the same gravity carrier"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the wind's field equation is derived (permanence plus zero circulation) with the capture rates as sources, and the gas's conserved tensor identified as radiation's; next: whether the stationary wind of capturing bodies is circulation-free beyond the linearized regime, the drag and growth that come with capture, and a clause joining inertia with the rule's weights; the owner's fork on whether an encounter may re-draw a record's content gates all of it"
conditional_surface_status: "T1-T3 exact; the zero-circulation hypothesis is derived only for the linearized evolution from rest; the correspondence with the weak-field packet is one of form"
hypothetical_axiom_status: "the inertial clause of block 44, including its scattering, which re-draws contents; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full) is used through "A site never carries more than one record; records are permanent." Block 01 (on `main`, proposed and unaudited) supplies the menu. Blocks 44 and 45 (open PRs #8550, #8553) supply the clause, the product-state current and pressure, and the local conservation laws; the runner re-derives what it uses. The weak-field packet (`GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11` on `main`) is cited for the form of its three statements only.

- **Bond field.** A number on each oriented bond, `J(x→y) = −J(y→x)`. Divergence at `x`: the sum over the six bonds out of `x`. Circulation: the oriented sum around a plaquette.
- **Sinks.** Capture rates `Q_a ≥ 0` at sites `x_a`; on a torus the uniform part `mean Q` is subtracted (a reservoir returns what the bodies take).
- **`G_L`, `G₀`.** The Green function of `−Δ_lat` on the torus with the zero mode removed, and on the infinite lattice.
- **The tensor.** `T⁰⁰ = n`, `Tⁱ⁰ = gᵢ` (momentum density), `T⁰ⁱ = Jᵢ` (mass current), `Tⁱʲ = Πᵢⱼ` (momentum flux), with `∂_t T⁰⁰ + ∂_i T⁰ⁱ = 0` and `∂_t Tⁱ⁰ + ∂_j Tⁱʲ = 0` holding locally and exactly (block 45).

The decomposition of a bond field into a gradient, a circulation part and harmonic constants is that of Hodge and Helmholtz; the field equation is that of Poisson; conservation identities of this form in momentum space are those of Ward; a traceless conserved tensor is the mark of the radiation of Maxwell; a symmetric one goes with the symmetry of Noether's theorem under boosts, which the lattice gas lacks at finite density. None is used as authority.

## Prior art and what is new

Discrete potential theory and the equation of state of a gas of particles of one speed are classical. What is new is their place here: the statement that the campaign's wind law has a derived field equation of the weak-field packet's form, with the capture rates as its sources; the exact uniqueness statement on the torus, checked by an exact rank; and the observation that one record per site leaves the equation of state of radiation untouched at every density while breaking the symmetry of the conserved tensor by exactly the factor `1 − ρ`.

## Exact target and obligation graph

Target: the field equation of the wind and the conserved tensor of the gas. Obligations: (O1) uniqueness and form of a circulation-free current with given divergence; (O2) why the wind is circulation-free; (O3) the tensor. T1–T3 discharge them at their stated levels.

## Theorem T1 — a circulation-free current with given divergence is the gradient of the Green-function potential

On the torus `(Z/L)³` a bond field with zero circulation around every plaquette is a lattice gradient plus a constant field along each axis (the three non-contractible directions); if its divergence also vanishes the gradient part is that of a harmonic function, hence constant, and only the three constants remain. So two circulation-free currents with the same divergence differ by constants. The field `J(x→y) = Φ(x) − Φ(y)` with `Φ = −G_L * (Q − mean Q)` has divergence `−Δ_lat Φ = −(Q − mean Q)` (because `−Δ_lat G_L` is the point source minus its mean), zero circulation and no constant part: it is the solution. The infinite-lattice analogue needs existence, boundary decay and a kernel asymptotic; these are deferred here. The finite-torus calculation does not establish an infinite-volume inverse-square law. ∎

On the `4³` torus the `64` divergence and `192` circulation constraints on the `192` bonds have rank `189`; on the `3³` torus `108` constraints on `81` bonds have exact rational rank `78`.

## Theorem T2 — the wind that builds up from rest has no circulation

In the linearized conservation equations about rest (block 44, T3), `∂_t g = −∇(ρ/3)`. Here g is represented as a bond field in the supplied gradient discretization. This is a closure assumption, not an exact derivation of the microscopic viscous dynamics. If `g` vanishes initially it is at every time a lattice gradient, and the circulation of a lattice gradient around a plaquette is a telescoping sum. ∎

Beyond the linearized regime, and in the presence of viscous stress near bodies, zero circulation of the stationary wind is an assumption of this note; block 45's executed wind profile is consistent with it to a few per cent.

## Theorem T3 — the conserved tensor is that of radiation, and generically asymmetric at nonzero momentum and finite density

In a product state at rest the momentum flux is `(ρ/3)δᵢⱼ` for the six-axis menu at every density (block 44, T3: the exchange restores what exclusion removes), so `T⁰⁰ − Σᵢ Tⁱⁱ = ρ − 3(ρ/3) = 0`; with the speed of a record written explicitly the pressure is the density times the speed over three, for the sphere menu `ρ/(3√3)` with speed `1/√3`. The mass current is `(1 − ρ)` times the momentum density (block 44, T3), so `T⁰ⁱ = (1 − ρ)Tⁱ⁰`. ∎

## No-Go Discipline Gate

The note has one negative sentence: the mixed components differ at finite density when g is nonzero; at rest they are both zero.

### N1 — Routes by which the sentence could fail
1. *Another definition of the momentum* — with `e(s)` as the momentum of a record the statement is exact; a definition that absorbs the factor `1 − ρ` into the momentum would make the tensor symmetric and the momentum non-additive over records.
2. *Another clause* — a clause without exclusion has `ρ → 0` effectively and a symmetric tensor; the axioms' one record per site is what breaks it.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The zero-circulation hypothesis of T1, declared; block 44's re-drawing of contents, declared there.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | permanence: the divergence of the current is fixed by the capture rates | yes (premise) |
| block 01 (`main`) | the menu | yes (premise, proposed) |
| blocks 44, 45 (open PRs #8550, #8553) | the clause; product-state current and pressure; local conservation | yes (restated; the runner re-derives what it uses) |
| the weak-field packet (`main`) | the form of its three statements | correspondence of form only; not a premise |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "a circulation-free current with divergence fixed by the capture rates is the gradient of the Green-function potential; the gas has radiation's equation of state and a tensor symmetric at rest, and approximately symmetric for dilute nonzero-momentum states" | executed: flux and current of product states at four densities | executed: divergence at all 64 sites and circulation around all 192 plaquettes of the `4³` torus | executed: the Green function as a mode sum with the zero mode removed | executed: the rank of the 256 constraints; five random density fields | T1 on finite tori; the infinite-volume extension is deferred; T2 an identity; T3 exact for product states at rest |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no update law. The correspondence with the weak-field packet does not supply that packet's premises and is not proposed for any registry.

### N7 — Steelman
Hostile reviewer: "A potential flow into sinks obeys the field equation of potential theory; calling it a correspondence with gravity is decoration." Reply: the note calls it a correspondence of form and nothing more. Its use is for the owner's decision: the weak-field packet's field equation is supplied, and here is a clause in the campaign's vocabulary under which an equation of that form is derived, with an identified source and an executed bilinear response, together with what that clause costs (re-drawing contents; capture, growth and drag; transparency).

### N8 — Cross-cycle echo
Block 41's production halo obeyed the same equation for a walk; block 43 showed that a walk is too slow; blocks 44 and 45 replaced the walk by a flow with a speed and executed the wind; this note writes the flow's potential.

## Falsifiers

- A bond field on a torus with zero divergence and zero circulation that is not constant along each axis.
- A product state at rest whose momentum flux is not `(ρ/3)δᵢⱼ`, or whose mass current is not `(1 − ρ)` times its momentum density.

## Boundaries and non-claims

The stationary wind's zero circulation is assumed except in the linearized evolution from rest. No hydrodynamic limit is proved. The correspondence with the weak-field packet is one of form inside a supplied clause; no gravitational statement is made and nothing is adopted. Capture makes bodies grow and drags moving bodies; neither is treated here.

## Imports
- `minimal_axioms`: the sentence quoted under Premises. Block 01 (on `main`): the menu; proposed, unaudited. Blocks 44, 45 (PRs #8550, #8553, open): restated.
- Named standard imports at definition level: on a torus a circulation-free bond field is a gradient plus a constant along each axis; a harmonic function on a finite connected graph is constant; the Green function of the lattice Laplacian and its infinite-lattice decay, mentioned as a deferred extension.
- Reference only: Hodge, Helmholtz, Poisson, Ward, Maxwell, Noether for the named notions.

## Review record — original author provenance
Supervisor-run block of the 12-hour campaign. Lens: the decision record for the owner needed the correspondence with the weak-field packet stated exactly rather than in words; the exact content is a uniqueness statement and an equation of state. Refuting pass (`specs/supervisor_control_block46_refuter.py`, machinery disjoint from the runner's): W1 the exact rational rank on the `3³` torus by elimination over fractions (the runner works modulo a prime on the `4³` torus); W2 three sinks on the `6³` torus; W3 the pressure by enumeration of a bond's states at a fifth density and the sphere menu's pressure symbolically. All pass. A first version of W1 used a symbolic rank routine that did not finish in ten minutes on a loaded machine; replaced. Mutation census: 7 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Current review boundaries and dependencies

Conditional finite periodic bond-field identities: zero circulation and prescribed zero-mean divergence determine a current up to three constant components; fixing those determines the Green-function gradient. Curl-free evolution follows in the supplied linear gradient closure, not the exact viscous gas. Six-axis isotropic product states have pressure rho/3 and zero rest trace in the stated units. For nonzero mean momentum J=(1-rho)g breaks generic tensor symmetry; at rest J=g=0 even at finite density. No radiation species, gravity, general stationary potential flow or infinite-volume asymptotic is established.

Historical simulations and auxiliary refuters remain on original branch head `b9398e0fec91a0e238f4770aba99daf988746928`; their reported values are preserved but not freshly verified by this canonical runner. Companion links identify supplied mathematical models, not audited physical authority.

- [Companion model and limitations](ADMISSIBILITY_RULE_RECORDS_WITH_INERTIA_CONTENT_AS_DIRECTION_OF_TRAVEL_CONSERVED_MOMENTUM_STRUCTURELESS_EQUILIBRIUM_SOUND_SPEED_FORCES_NEED_CAPTURE_OR_EMISSION_BOUNDED_THEOREM_NOTE_2026-09-20.md)
- [Companion model and limitations](ADMISSIBILITY_RULE_THE_WIND_LAW_FLUX_THEOREMS_INVERSE_SQUARE_WIND_OF_A_CAPTURING_BODY_SECOND_ORDER_MOMENTUM_FLUX_FORCE_PROPORTIONAL_TO_PRODUCT_OF_CAPTURE_RATES_BOUNDED_THEOREM_NOTE_2026-09-20.md)
- [Companion model and limitations](ADMISSIBILITY_RULE_THE_WIND_OF_A_CAPTURING_BODY_IS_NOT_ISOTROPIC_LATTICE_STREAMING_GIVES_A_VISCOUS_TERM_OF_CUBIC_SYMMETRY_DIRECTION_DEPENDENCE_DOES_NOT_DECAY_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Finite-window rule](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)

## Verification

```bash
python3 scripts/admissibility_rule_the_potential_of_the_wind_lattice_poisson_equation_capture_rates_as_sources_conserved_tensor_of_radiation_2026_09_21.py
python3 scripts/admissibility_rule_the_potential_of_the_wind_lattice_poisson_equation_capture_rates_as_sources_conserved_tensor_of_radiation_2026_09_21.py --list-mutations
python3 .claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block46_refuter.py
```
