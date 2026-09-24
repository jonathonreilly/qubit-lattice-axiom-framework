---
claim_id: admissibility_rule_records_with_inertia_content_as_direction_of_travel_conserved_momentum_structureless_equilibrium_sound_speed_forces_need_capture_or_emission_bounded_theorem_note_2026-09-20
claim_type: bounded_theorem
claim_scope: "CONDITIONAL on a supplied clause that is not in the axioms memo and is not adopted: a record's content is its direction of travel. (S) streaming: each record, at rate 1, tries to step along its content; an empty target is entered, an occupied target exchanges contents with the record (the two records pass through each other), a solid site reflects it. (C) scattering: each bond, at rate gamma, re-draws the contents of its two records uniformly on their momentum class (six axes: an opposite pair becomes a uniformly random opposite pair, any other pair is exchanged with probability 1/2; sphere menu: P/2 +- r w with w uniform on the unit circle orthogonal to P = s + s', r^2 = 1 - |P|^2/4). (T1) every bulk event conserves record number and gas momentum; reflection conserves momentum only after including the body impulse,, the sum of the unit vectors of the contents, and the clause commutes with the 24 proper rotations; (T2) the uniform measure on configurations is stationary on every finite torus, with or without reflecting bodies, because every record of every configuration has exactly one streaming preimage and the scattering kernel is symmetric on each momentum class; it is not stationary if blocked attempts do nothing, nor under a head-on rule triggered by blocked attempts (1458 and 486 unbalanced configurations among the 12636 two-record configurations of the 3^3 torus); (T3) in a product state with content densities rho_d the mass current is (1 - rho) g, g the momentum density, and at isotropy the momentum flux is (rho/3) times the identity, the exchange term rho^2/3 restoring what exclusion removes from rho(1 - rho)/3, while the bond scattering carries no net momentum; the linearized conservation equations built on these currents have the speed squared (1 - rho)/3, and for the sphere menu with streaming probabilities max(0, s.e_k)/sqrt 3 the corresponding value is (1 - rho)/9; (T4) in the uniform state the mean force on a reflecting body is exactly zero for a body whose exposed faces balance in opposite directions, in the uniform gas state; (T5) the sphere menu's pair re-drawing keeps unit length and the sum. HISTORICAL AUTHOR OBSERVATIONS, NOT FRESH EVIDENCE: standing density waves oscillate at the predicted speeds; bodies that capture records attract each other and the dependence on separation; bodies that emit records. NOT claimed: a hydrodynamic limit theorem, any force law, any gravitational statement, that the clause is compatible with the Record axiom's locking sentence (the scattering re-draws contents), any adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_records_with_inertia_conserved_momentum_structureless_equilibrium_sound_speed_forces_need_capture_2026_09_20.py
---

# Conservation, stationary uniform measures and conditional sound closure for a supplied inertial gas

**Date:** 2026-09-20
**Type:** bounded_theorem
**Status:** bounded-support (exact for the declared clause; the waves and the forces between bodies executed, not claimed; nothing adopted or registered; unaudited)

This note works out a supplied clause, in which a record's content is its direction of travel; the clause is not in the axioms memo and is not adopted.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 43 (PR #8549) showed that the two fields found in the record layer arrive by a random walk, so that a field over a distance `R` costs of the order of `R²` ticks; a carrier of a long-range field between bodies that move needs a speed. The six contents of the six-axis menu are the six lattice directions. This note takes that literally: **a record travels along its content.** A record then has inertia, and the question is what the record layer becomes.

1. **Two conservation laws, event by event.** With streaming (step along the content; pass through a record in the way) and scattering (a bond re-draws its pair of contents on their momentum class), every bulk event conserves record number and gas momentum; reflection conserves momentum only after including the body impulse, `Σ e(s)`, and the clause is covariant under the rotations of the cube (T1). These are local laws with explicit currents and a cadence, which is the second of the three pieces the record-pair source note on `main` lists as missing between records and a gravity carrier.
2. **Equilibrium is structureless.** The uniform measure is stationary on every finite torus, with or without reflecting bodies (T2). Both details of the clause matter: if blocked attempts do nothing, or if head-on pairs scatter when an attempt is blocked, it is not.
3. **A speed.** In product states the mass current is `(1 − ρ)g` and the pressure is exactly `ρ/3`: the exchange restores precisely what exclusion takes away. The linearized conservation equations built on these currents carry density waves at `c = √((1 − ρ)/3)` lattice units per tick, `1/√3` of the limiting speed at low density; for the sphere menu `c = √(1 − ρ)/3` (T3). Executed at density `0.3`: standing waves oscillate at `0.464` against `0.483` (six axes; strongly damped at the wavelength used) and at `0.277`, `0.278` against `0.279` (sphere; weakly damped).
4. **No force without capture or emission.** In equilibrium the mean force on a reflecting body is exactly zero for separated bodies with balanced exposed faces in the uniform gas state (T4). Executed: a reflecting pair at separation 12 feels `−0.004 ± 0.020` per tick.
5. **Bodies that capture records attract.** Executed in the sphere-menu gas: two bodies of radius 3, each capturing `7.8` records per tick, are pulled together by `0.237, 0.144, 0.065, 0.043, 0.023` per tick at separations `12, 16, 24, 32, 40`; the product `F r²` is `34, 37, 38, 44, 37`, constant within the errors, an inverse-square law over this range. The estimate `√3 Q₁Q₂/(4π ρ(1−ρ) r²)`, obtained from T3's exact current by letting each body capture records that carry the mean momentum of the other's inflow, gives `40`. Bodies that emit records: two reflecting bodies each emitting `5` records per tick are pushed apart, `−0.209, −0.061, −0.004` (errors `0.02`) at separations `12, 20, 32`: each stands in the other's outflow.

So a record layer with inertia has a carrier with a speed, exact local conservation of number and momentum, and zero mean force for the specified uniform reflecting state; nonequilibrium force laws require additional work. The attraction of capturing bodies is the shadow mechanism of the eighteenth century in the owner's vocabulary; its classical difficulties (bodies grow by what they capture; a moving body is dragged; an opaque body acts by its cross-section, not its record count) are listed under Boundaries and none is resolved here.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "owner, 2026-09-20: 'run a 12 hour campaign on this lane please'; block 43's conclusion that a carrier needs a speed; the record-pair source note on main: a local conservation/attachment law, including cadence, consumed by the same carrier"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "a clause under which records have inertia is worked out exactly (conservation, covariance, structureless equilibrium, product-state currents) and executed (sound at the predicted speed; forces only with capture or emission; capturing bodies attract). Next: the distance law of the attraction in a larger box and its dependence on the bodies' record counts; the drag on a moving body against the attraction; whether the scattering clause can be had without re-drawing contents; loaded on ai/probes"
conditional_surface_status: "T1-T5 exact for the declared clause; the wave speed is that of the linearized equations built on exact product-state currents, no hydrodynamic limit is proved; the executed waves and forces (floating point, sides 64 and 96, one or a few seeds) are in the controls and not claimed"
hypothetical_axiom_status: "the clause that a record travels along its content, with pass-through streaming and momentum-class scattering; the scattering re-draws contents, which the Record axiom's locking sentence does not obviously allow; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full) is used through "A site never carries more than one record; records are permanent." (number is conserved) and "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." (the clause is required to be covariant). The memo lists update laws among its open gates; this note supplies one candidate and adopts nothing. Block 39 (open PR #8530) supplies the moving-records reading; block 43 (open PR #8549) the need for a speed. The record-pair source note on `main` is cited for its list of missing pieces, as a statement of requirements.

- **Momentum.** `P = Σ_x n_x e(s_x)`, `e(s)` the unit vector of the content; momentum density `g`.
- **(S) Streaming.** Each record at rate `1` attempts `x → x + e(s_x)` (sphere menu: `x → x + e_k` with probability `max(0, s·e_k)/√3`). Empty target: the record moves. Occupied target: the two records exchange contents, which is the same as the two records passing through each other with their contents unchanged. Solid target: the content is reversed (sphere: reflected in the face) and the body receives the difference.
- **(C) Scattering.** Each bond at rate `γ`: the two contents are re-drawn uniformly on the set of pairs with the same sum. This and reflection change individual contents; the bulk scattering also changes the pair labels. **It is a further supplied clause:** the Record axiom says a record "locks exactly one admissible local possibility", and whether an encounter may re-draw it is not decided here. Without (C) each content count is conserved separately; exclusion and exchange still couple their spatial dynamics. The two-variable sound closure is then not justified by this argument.
- **Bodies.** Solid sites. A reflecting body returns what hits it; a capturing body keeps it (the record joins the body, permanence is respected); an emitting body places new records on its surface.

Equations for the densities of conserved quantities are those of Euler; the corresponding viscous equations those of Navier and Stokes; lattice gases with discrete velocities are classical; the attraction of bodies that absorb a flux of corpuscles is the mechanism of Le Sage, and the attraction of pulsating or emitting bodies in a fluid that of Bjerknes; Pearson proposed matter as a source of fluid. None is used as authority.

## Prior art and what is new

Lattice gases that conserve number and momentum, their structureless equilibria and their sound waves are classical, as are the shadow and the hydrodynamic pictures of attraction and the objections to them. What is new is their appearance in the campaign's vocabulary: the identification of the six contents with directions of travel; the exact statement of which details of the clause make the equilibrium structureless (the exchange, and scattering on a bond clock), with the counterexamples; the exact pressure `ρ/3` under one record per site; the exact absence of force on bodies that neither capture nor emit; and the executed sign of the force for capture and for emission. Everything classical is re-derived at scope or executed.

## Exact target and obligation graph

Target: what the record layer becomes if records have inertia. Obligations: (O1) conservation and covariance; (O2) the equilibrium; (O3) the currents and the wave speed; (O4) forces on bodies in equilibrium; (O5) the sphere menu's re-drawing. T1–T5 discharge them; the controls execute waves and forces.

## Theorem T1 — number and momentum are conserved by every event, and the clause is covariant

A move carries one record and its momentum one step. An exchange leaves both sites occupied and permutes the two contents. A re-drawing replaces a pair of contents by a pair with the same sum. A reflection changes one content and credits the body with the difference. Hence `N` and, away from bodies, `P` are conserved event by event, with currents supported on the bond where the event happens. Each event is defined through the content, the bond it points along and the relation of two contents, all of which the rotations carry along. ∎

## Theorem T2 — the uniform measure is stationary; the exchange and the bond clock are what make it so

Fix a configuration `c` on a finite torus, with or without reflecting solid sites. For a record `r` of `c`, at `y` with content `d`, look at the site `x` behind it. If `x` is empty, `c` is reached by `r` moving from `x`. If `x` holds a record of content `d'`, `c` is reached from the configuration with `d` at `x` and `d'` at `y` by the exchange triggered by the record at `x`. If `x` is solid, `c` is reached by the reflection of `r` with content `−d`. In each case there is exactly one streaming event into `c` with `r` in this role, at rate `1`: the inflow by streaming equals the number of records, which is the outflow. The scattering kernel is uniform on each momentum class, hence symmetric. So the uniform measure is stationary. If blocked attempts do nothing, a record whose behind-site is occupied has no preimage; if head-on pairs scatter when an attempt is blocked, the back-to-back pair receives `1/3` where it sends `2`. ∎

On the `3³` torus with two records all `12636` configurations balance; `1458` fail without the exchange and `486` under the blocked-attempt head-on rule.

## Theorem T3 — product-state currents, the pressure ρ/3, and the speed of the linearized equations

In a product state with content densities `ρ_d` (total `ρ`): a record of content `d` moves forward when the site ahead is empty, so the mass current along the axis of `d` is `(ρ_d − ρ_{−d})(1 − ρ)`, that is `J = (1 − ρ) g`. Momentum crosses a bond in two ways: a moving record carries `e_d` (`ρ_d(1 − ρ)`), and an exchange passes `e_d` forward and `e_{d'}` back (`ρ_d ρ_{d'}`). At isotropy, `ρ_d = ρ/6`, the first gives `(ρ(1 − ρ)/3) δ_ij` and the second `(ρ²/3) δ_ij`: the momentum flux is `(ρ/3) δ_ij`, as if there were no exclusion. The scattering moves no net momentum across a bond at isotropy. Away from reflecting bodies, weights proportional to exp(mu N+b.P) give stationary product measures because events conserve N and P and balance the uniform measure. Using such measures as local equilibria is a further closure assumption, and the equations `∂_t ρ + ∇·((1 − ρ) g) = 0`, `∂_t g + ∇(ρ/3) = 0`, linearized about rest at density `ρ₀`, have waves of speed `c² = (1 − ρ₀)/3`. For the sphere menu the streaming probabilities give the mean step `s/√3`, `J = (1 − ρ) g/√3`, the flux `ρ/(3√3)`, and `c² = (1 − ρ₀)/9`. ∎

The currents are exact; that the gas follows these conservation equations at large scales is not proved here. Executed (control `specs/supervisor_control_block44_inertial.py`, side 64, density `0.3`, `γ = 1`, four runs, damped-cosine fit; the compiled generator seeded): six axes `0.464` (first mode; `0.421` for the second, which is overdamped) against `0.483`; sphere `0.277` and `0.278` (first and second mode) against `0.279`.

## Theorem T4 — a body that neither captures nor emits feels no force

With reflecting bodies present the uniform measure is still stationary (T2). In it every free site is occupied with the same probability and every content is equally likely, so the mean impulse per unit time on a face of a body is the same for every exposed face, directed along the inward normal; summed over the closed surface of the body it vanishes. This requires that other bodies do not remove an unbalanced set of faces by contact. A separated lattice body has equally many exposed faces of each opposite pair; individual touching bodies need not. A composite union retains the cancellation. ∎

On the `4³` torus with two separate solid sites and two records (`68076` configurations) the mean force on each is exactly zero.

## Theorem T5 — the sphere menu's re-drawing

For unit vectors `s, s'` with `P = s + s'`, and a unit vector `w` orthogonal to `P`, the pair `P/2 ± r w` with `r² = 1 − |P|²/4` consists of unit vectors with sum `P`; the set of such pairs is the circle of directions `w`, on which the re-drawing is uniform, and by symmetry about P the conditional measure is uniform on that circle when 0<|P|<2. At P=0 the class is the full sphere of opposite pairs, with normalized surface measure; at |P|=2 it is a singleton. These degenerate classes must be handled separately. ∎

## Historical author observations (not fresh evidence): forces between bodies in the sphere-menu gas (not proved)

Control `specs/supervisor_control_block44_bodies.py` (floating point; side 96; density `0.3`; `γ = 1`; spherical bodies of radius 3; a reservoir at density `0.3` on the two outer layers; 2000 warm-up and 8000 measured ticks; force per tick along the joining axis, positive towards the other body, mean and standard error over ten blocks).

| bodies | separation | force towards the other body per tick | `F r²` | captures per tick per body |
|---|---|---|---|---|
| reflecting pair | 12 | `−0.004 ± 0.020` | — | — |
| one capturing body (control) | — | `+0.007 ± 0.012` | — | `7.79` |
| capturing pair | 12 | `+0.237 ± 0.012` | `34 ± 2` | `7.76` |
| capturing pair | 16 | `+0.144 ± 0.011` | `37 ± 3` | `7.77` |
| capturing pair | 24 | `+0.065 ± 0.007` | `38 ± 4` | `7.80` |
| capturing pair | 32 | `+0.043 ± 0.006` | `44 ± 6` | `7.85` |
| capturing pair | 40 | `+0.023 ± 0.015` | `37 ± 24` | `7.81` |
| emitting pair (`Q = 5`), reflecting | 12 | `−0.209 ± 0.016` | `−30 ± 2` | — |
| emitting pair | 20 | `−0.061 ± 0.019` | `−24 ± 8` | — |
| emitting pair | 32 | `−0.004 ± 0.022` | — | — |

**Historical conditional interpretation (not proved).** The force estimate below additionally assumes isotropic inflow and unbiased capture; neither follows for general lattice streaming or body geometry.  Records are conserved, so steady net flux crosses every enclosing surface at the same rate. Pointwise inverse-square isotropic wind needs an additional isotropy assumption; it does not follow from flux conservation. A body standing in a wind is dragged along it; a capturing body takes up the mean momentum of the records it captures. With T3's exact relation `J = (1 − ρ) g/√3` the inflow of a body capturing `Q₁` records per tick carries the momentum `√3 Q₁/(4π r² ρ(1−ρ))` per record at distance `r`, and a second body capturing `Q₂` of them per tick is pulled by `√3 Q₁Q₂/(4π ρ(1−ρ) r²)`: with `Q = 7.8` and `ρ = 0.29` this is `40/r²`, against the executed `36 ± 2`. The same coupling is a drag on a body that moves through a gas at rest; it is not executed here. Whether the capture rate of a body is proportional to its number of records (dilute bodies) or to its cross-section (opaque ones, as here) is not executed either.

## No-Go Discipline Gate

The note's negative sentence is T4: no force on a body that neither captures nor emits, in equilibrium.

### N1 — Routes by which the sentence could fail
1. *Other clauses* — the uniform equilibrium belongs to this clause; T2 shows two nearby clauses without it. A clause with a structured equilibrium could give reflecting bodies a force of the range of that structure.
2. *Out of equilibrium* — a gas with a flow or a gradient pushes a reflecting body; T4 is an equilibrium statement.
3. *Finite-size bodies and exclusion* — T4 is exact for the clause as declared, where a solid site is simply not available; no depletion effect arises because the measure is uniform on the available sites.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The scattering clause re-draws contents; declared under Premises as a further supplied clause.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | permanence (number conserved); covariance required of the clause | yes (premise) |
| block 01 (`main`) | the six-axis menu | yes (premise, proposed) |
| blocks 39, 43 (open PRs #8530, #8549) | moving records; the need for a speed | placement |
| the record-pair source note (`main`) | the list of missing pieces | statement of requirements |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "number and momentum conserved; structureless equilibrium; pressure `ρ/3`; no force without capture or emission" | executed: 42 streaming cases, 36 scattering pairs, 24 rotations | executed: inflow against outflow at all 12636 configurations of the `3³` torus and all 68076 of the `4³` torus with two solids; the force on each solid | not applicable to the exact part; waves executed in the controls | executed: currents and momentum flux at three densities; three rational instances of the sphere re-drawing | T1 event by event on every lattice; T2, T4 by a counting argument on every finite torus; T3's currents exact for product states; forces with capture or emission executed only |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no update law. The clause is a candidate for the memo's open gate on update laws; proposing it for adoption is not attempted.

### N7 — Steelman
Hostile reviewer: "This is a textbook lattice gas with the labels changed, and the shadow attraction was abandoned two centuries ago." Reply: yes to both, and the note says so. What the campaign gains is specific: the contents of its own menu are directions, so inertia costs no new object; the exact conditions under which the equilibrium is structureless; a carrier with a speed, which block 43 showed the record layer lacked; and the exact statement that forces require capture or emission, which ties the question of attraction to the campaign's formation and transit clauses. The classical objections are carried into the Boundaries, not answered.

### N8 — Cross-cycle echo
Block 41's T5 (the transit Laplacian is sourced by production) and its exact closure under exclusion return as the mass current `(1 − ρ) g`; block 43's demand for a speed is met by the wave of T3; block 39's pair-weight transit had no momentum, which is why its fields diffuse.

## Falsifiers

- A bulk event that changes N or gas P, or a reflection that fails to balance the body impulse, or a rotation it does not commute with.
- A finite torus and a configuration with unequal inflow and outflow under the clause.
- A product state whose mass current differs from `(1 − ρ) g`, or an isotropic one whose momentum flux differs from `ρ/3`.
- A reflecting body with a non-zero mean force in the uniform state.
- For the executed part: a standing wave that decays without oscillating at long wavelength; capturing bodies that repel.

## Boundaries and non-claims

No force law and no gravitational statement is made. No hydrodynamic limit is proved. The attraction of capturing bodies is executed at one density, one body size and a few separations. The classical difficulties of the shadow mechanism apply and are not addressed: a capturing body grows by what it captures; a body moving through the gas is dragged; a dense body acts through its cross-section, not its record count; with six directions of travel the shadows are beams, and only the sphere menu spreads them. The scattering clause re-draws contents, against the plain reading of the Record axiom's locking sentence; the absence of re-drawing alone proves neither the presence nor the absence of waves. Nothing is adopted.

## Imports
- `minimal_axioms`: the sentences quoted under Premises. Block 01 (on `main`): the menu; proposed, unaudited. Blocks 39, 43 (PRs #8530, #8549, open) and the record-pair source note on `main`: placement.
- Named standard imports at definition level: stationarity of a measure as balance of inflow and outflow; product states as local equilibria of a dynamics with a uniform invariant measure and conserved sums; the linearization of a pair of conservation laws.
- Reference only: Euler, Navier and Stokes for the equations; Boltzmann for kinetic theory; Le Sage, Bjerknes and Pearson for the mechanical pictures of attraction and Poincare for the drag objection; none is relied on.

## Review record — original author provenance
Supervisor-run block of the 12-hour campaign (owner 2026-09-20: "run a 12 hour campaign on this lane please"). Lens: block 43 asked for a carrier with a speed; the menu's contents are directions. First simulations used a head-on rule triggered by blocked attempts; an exact enumeration showed that rule does not keep the uniform measure stationary, the clause was cleaned (exchange when blocked; scattering on a bond clock), and everything executed was re-run with the clean clause. Found while writing the runner: an integer zero divided by two silently produced a floating-point number inside an "exact" check; the inputs are now wrapped as fractions and the check asserts the type. Refuting pass (`specs/supervisor_control_block44_refuter.py`, machinery disjoint from the runner's): W1 the bijection behind T2 built explicitly for all 1895400 (configuration, record) pairs with three records on the `3³` torus; W2 the momentum flux across a bond by enumeration of its 49 states and events; W3 the sphere re-drawing as a symbolic identity; W4 `⟨s_i s_j⟩ = δ_ij/3` by exact integration and the speed `(1−ρ)/9`; W5 an L-shaped reflecting body. All pass. Mutation census: 10 mutations, each failing in its own family only. The first force batch used the superseded rule and was discarded; the numbers in this note are from the clean clause. Author checks only; no independent review has taken place.

## Current review boundaries and dependencies

The historical simulations and auxiliary refuters remain author reports on original branch head `502a7a2149a88543c2507b42ce7eec265e6b840e`; their tables are preserved but are not freshly verified by the canonical runner. No physical propagation, force law, or hydrodynamic limit follows from these finite identities.

- [Companion model](ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md)
- [Companion model](ADMISSIBILITY_RULE_RECORD_LAYER_FIELDS_ARRIVE_BY_DIFFUSION_ESTABLISHMENT_TIME_GROWS_AS_THE_SQUARE_OF_THE_RANGE_TRANSIT_HALO_AND_MASSLESS_ODDS_FIELD_BOUNDED_THEOREM_NOTE_2026-09-20.md)
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Finite-window rule](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)

## Verification

```bash
python3 scripts/admissibility_rule_records_with_inertia_conserved_momentum_structureless_equilibrium_sound_speed_forces_need_capture_2026_09_20.py
python3 scripts/admissibility_rule_records_with_inertia_conserved_momentum_structureless_equilibrium_sound_speed_forces_need_capture_2026_09_20.py --list-mutations
python3 .claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block44_refuter.py
```
