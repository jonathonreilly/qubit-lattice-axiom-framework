---
claim_id: formation_weight_energy_dictionary_underdetermination_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "For positive normalized two-channel dictionaries D(w,E_tot), the declared share map is one member of an explicit affine family joining inverse share, equal share, and declared share; all members obey the same total-energy constraint but give different r images away from w=1/2, while current Record supplies no scalar/additive or content-to-energy selector."
upstream_dependencies:
  - minimal_axioms
  - koide_formation_gate_relocation_tied_measure_per_cell_weight_compatibility_bounded_theorem_note_2026-07-12
  - admissibility_support_constrains_content_not_formation_site_bounded_theorem_note_2026-08-13
runner: scripts/formation_weight_energy_dictionary_underdetermination_2026_08_13.py
---

# Formation-Weight Energy-Dictionary Underdetermination

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact algebra of a declared two-channel energy dictionary, an
explicit normalized counterfamily, and the current Record type boundary. No
physical energy dictionary, formation law, or value of `r` is selected.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/formation_weight_energy_dictionary_underdetermination_2026_08_13.py`](../scripts/formation_weight_energy_dictionary_underdetermination_2026_08_13.py)

**Runner cache:**
[`logs/runner-cache/formation_weight_energy_dictionary_underdetermination_2026_08_13.txt`](../logs/runner-cache/formation_weight_energy_dictionary_underdetermination_2026_08_13.txt)

## Result Up Front

The July 12 formation-gate relocation note
[`KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md`](KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md)
explicitly labels the energy-to-formation-state bridge

`D_*(w,E_tot)=(wE_tot,(1-w)E_tot)`

as its own declared modeling element. Conditional on that declaration and the
channel split

`E_s=3a^2`, `E_d=6|b|^2`, `r=|b|^2/a^2`,

the familiar solve

`r=(1-w)/(2w)`, `w=1/(1+2r)`

is exact. It is still conditional algebra, not a derivation of the dictionary.

The exact new content is an explicit continuum of normalized alternatives.
For `0≤t≤1`, define

`g_t(w)=t w+(1-t)(1-w)`

and

`D_t(w,E_tot)=(g_t(w)E_tot,(1-g_t(w))E_tot)`.

Every `D_t` is positive for `0<w<1`, preserves
`E_s+E_d=E_tot`, and uses the same inputs. The endpoints are inverse share and
declared share; `t=1/2` is equal share. At `w=1/3`, their images are

`r_t=(1+t)/(2(2-t))`,

which ranges from `1/4` through `1/2` to `1`. At `w=1/2`, all members
coincide at `r=1/2`. Thus the half-weight point is not a discriminator, and
positivity plus total-energy normalization do not select `D_*`.

The post-reset Record axiom contains no scalar collection functional, no
finite additivity, and no value at absence. It also names no energy codomain
or content-to-energy map. The earlier union-scalar argument is therefore
retired rather than repaired. This note makes no claim that the full framework
can never derive `D_*`; a dynamics, symmetry, calibration, or explicit
content-to-energy bridge remains live.

## Current Premise Boundary

The current Record wording in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

These sentences type locking and content-determined readout. They do not
define a scalar on record collections, identify readout values with energy,
or equate a formation weight with an energy share. No such structure is used
below.

The current formation-site boundary is supplied by
[`ADMISSIBILITY_SUPPORT_CONSTRAINS_CONTENT_NOT_FORMATION_SITE_BOUNDED_THEOREM_NOTE_2026-08-13.md`](ADMISSIBILITY_SUPPORT_CONSTRAINS_CONTENT_NOT_FORMATION_SITE_BOUNDED_THEOREM_NOTE_2026-08-13.md):
Admissibility support constrains which content may be locked conditional on
formation, but does not select the formation site, probability, process, or
rate. The present algebra does not close that gap.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The conditional D_* solve, normalized affine counterfamily, exact r_t image, and half-weight coalescence are rational identities. Current Record supplies no scalar/additive or energy-typing selector, while any wider physical derivation remains open."
trace_class: negative_route_pruning
target_claim_id: koide_energy_dictionary_r_from_w
target_blocker_text: "derive the physical energy dictionary relating formation weight w to channel energies and r"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Supply a physical dynamics, symmetry, calibration, or content-to-energy bridge that selects one normalized dictionary; do not adopt D_* by declaration."
conditional_surface_status: "exact for conditional channel algebra and nonuniqueness under positivity plus total-energy normalization; physical selection remains open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Take `E_tot>0`, `0<w<1`, and positive two-channel energies satisfying

`E_s+E_d=E_tot`.

The channel coordinates are

`a^2=E_s/3`, `|b|^2=E_d/6`,

so whenever `E_s>0`,

`r=|b|^2/a^2=E_d/(2E_s)`.

A **normalized dictionary** is a map

`D:(w,E_tot)↦(E_s,E_d)`

with `E_s>0`, `E_d>0`, and `E_s+E_d=E_tot` on the declared domain. This is
an algebraic comparison class, not a set of physically realized laws.

The declared member is `D_*`. Additional named members are

- inverse share `D_inv=((1-w)E_tot,wE_tot)`;
- equal share `D_eq=(E_tot/2,E_tot/2)`;
- carrier-dimension share `D_dim=(E_tot/3,2E_tot/3)`.

The one-parameter `D_t` family contains `D_inv`, `D_eq`, and `D_*` at
`t=0,1/2,1`, respectively. `D_dim` is a further normalized comparator.

## Theorem 1 — Conditional Declared Solve

Under `D_*`,

`a^2=wE_tot/3`, `|b|^2=(1-w)E_tot/6`.

Therefore

`r=((1-w)E_tot/6)/(wE_tot/3)=(1-w)/(2w)`.

Solving gives `w=1/(1+2r)`. At the comparison points,

`w=1/3 ⇒ r=1`, and `w=1/2 ⇒ r=1/2`.

This theorem is explicitly conditional on `D_*`. It proves no physical
selection statement.

## Theorem 2 — Normalized Affine Counterfamily

For `0≤t≤1`, `g_t(w)` is a convex combination of `w` and `1-w`. Hence
`0<g_t(w)<1` whenever `0<w<1`. Both components of `D_t` are positive and

`g_t(w)E_tot+(1-g_t(w))E_tot=E_tot`.

At the three parameter values,

`D_0=D_inv`, `D_{1/2}=D_eq`, `D_1=D_*`.

Thus `D_*` is not unique in the declared normalized class. This is a direct
counterfamily, not an inference from missing evidence.

## Theorem 3 — Exact Image And Half-Weight Coalescence

For any `t`, the image of `D_t` is

`r_t(w)=(1-g_t(w))/(2g_t(w))`.

At `w=1/3`, `g_t=(2-t)/3`, so

`r_t(1/3)=(1+t)/(2(2-t))`.

The endpoint and midpoint values are

| dictionary | `t` | `r(1/3)` | `r(1/2)` |
|---|---:|---:|---:|
| `D_inv` | `0` | `1/4` | `1/2` |
| `D_eq` | `1/2` | `1/2` | `1/2` |
| `D_*` | `1` | `1` | `1/2` |

For `w=1/2`, `g_t=1/2` for every `t`, hence `r_t=1/2` for the entire
family. Agreement at the half-weight point cannot select the declared
dictionary. The carrier-dimension comparator has constant image `r=1`; it
agrees with `D_*` at `w=1/3` and disagrees at `w=1/2`.

## Theorem 4 — Scoped Underdetermination

The explicitly stated algebraic conditions—positive shares, a fixed total,
the channel definitions, and the inputs `(w,E_tot)`—do not uniquely select
`D_*`, because every `D_t` satisfies those conditions and distinct `t` give
distinct shares whenever `w≠1/2`.

Current Record cannot supply the old proposed scalar/additive selector: that
structure is not current axiom content. Record also states no energy-valued
content map. This is a premise boundary, not a proof that every possible
framework derivation fails.

The theorem does **not** say that `D_*` is false, that no dictionary exists,
or that `r=1/2` is impossible. It says only that the declared comparison
class and current named Record content do not select a unique member.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current Record lock/content/absence boundary | quoted; scalar clauses retired |
| July 12 declared dictionary and channel split | source-bound declared algebra |
| current formation-site residual | source-bound through the August 13 parent |
| conditional solve for `D_*` | exact |
| positivity and normalization of every `D_t` | exact convexity identity |
| image formula and comparison table | exact rational algebra |
| nonuniqueness in normalized class | closed by counterfamily |
| physical selector of `t=1` | open |
| formation dynamics and energy/content map | open |

## Imports And Non-Claims

The July 12 note is imported only for its declared modeling element and
channel definitions. Its historical discussion of Record supplies no current
premise. The August 13 formation-site note supplies only the current residual.

No empirical energy, fitted weight, formation frequency, Hamiltonian,
dynamics, symmetry selector, calibration rule, or physical content-to-energy
map is imported. The algebraic comparator class is not treated as physical
law.

## Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It addresses the named energy-dictionary residual by isolating the exact algebra that is conditional and the exact normalization route that is nonunique. |
| V2 | The July 12 parent declares `D_*`; the present continuous counterfamily and post-reset Record boundary are new on current main. |
| V3 | Positivity, normalization, inversion, and the image table are independently checkable in rational arithmetic. |
| V4 | The affine family strengthens a finite list of alternatives into an exact continuum and explains why `w=1/2` cannot discriminate. |
| V5 | It does not relabel a conditional solve as physics; selection of one member remains the open bridge. |

## No-Go Discipline Gate

The negative claim is restricted to uniqueness from the declared normalized
comparison class and to use of retired Record scalar/additive structure. No
global energy-dictionary impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| declared share `D_*` | set energy shares equal to formation weights | exact conditional solve; remains a declaration |
| inverse share | swap the weights | normalized live comparator; different image away from `1/2` |
| equal share | ignore `w` | normalized live comparator; constant `r=1/2` |
| carrier dimensions | use `1:2` channel multiplicity | normalized live comparator; constant `r=1` |
| affine family `D_t` | interpolate inverse to declared share | executed continuum of counterexamples to uniqueness |
| dynamics or symmetry | derive a selector for `t` | live route outside the stated algebra |
| calibrated energy readout | add a physical content-to-energy map | live route under current Record semantics |
| observation | select a dictionary empirically | live route; no observation is admitted here |

### N2 — wall independence

Dynamics, symmetry, calibration, formation, and content-to-energy typing are
independent possible selectors. The theorem claims no complete wall
collection and no global no-go.

### N3 — hidden-condition scan

Positivity, total-energy normalization, the channel definitions, `D_*`, the
comparison domain, and the `D_t` family are explicit. Physical realization,
formation, an energy readout, and a selector for `t` are not silently assumed.

### N4 — source residual matching

The July 12 source calls `D_*` a declared modeling element not supplied by
Record. Current minimal axioms have since removed scalar/additive Record
structure. The August 13 formation-site result preserves the formation
residual. The repaired theorem matches all three current boundaries.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | two channel energies and comparison weights | no exhaustive physical state classification |
| per site | one declared two-channel formation coordinate | no multisite dynamics |
| per mode | channel multiplicities `3` and `6` | no spectral-mode exhaustion |
| per block | normalized dictionary family and image map | no physical selector or formation law |
| lattice wide | checked and not executed | no global energy no-go |

### N6 — live partial-closure paths

A dynamics-derived energy partition, symmetry principle, calibrated Record
content map, formation law, or observation can select a dictionary. Those
routes remain live and are not functions of retired scalar collection data.

### N7 — hostile steelman

**Steelman:** The energy shares are defined to equal `(w,1-w)`, so `D_*` is
tautologically unique.

**Answer:** It is unique only after making that declaration. The theorem asks
whether the weaker positive normalized class selects the declaration. The
explicit `D_t` family proves it does not.

### N8 — cross-cycle echo

The July 12 source already distinguishes its declared bridge from axiom
content. The post-reset Record boundary removes the scalar route used by the
submission. The current result neither validates nor invalidates downstream
uses of `D_*`; it records their exact conditional premise and the missing
selection step.

**Gate disposition:** PASS for conditional algebra and nonuniqueness in the
declared normalized class. FAIL / DO NOT SHIP for “no energy dictionary can be
derived,” “`D_*` is false,” or “`r=1/2` is impossible.”

## Primary Runner

The primary runner checks the current premise boundary, July 12 declaration,
August 13 formation residual, conditional inversion, the affine family on an
exact rational grid, analytic image identities, comparison table, half-weight
coalescence, and mutation controls. It authors no audit verdict.
