---
claim_id: nonaffine_purity_weighted_kernel_is_not_barycenter_evaluation_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On finite-support measures on the density body, the normalized-square state map σ_μ=ρ_μ^2/Tr(ρ_μ^2) defines the menu-independent positive normalized grade K(μ,E)=Tr(σ_μ E). It agrees with barycenter evaluation at I/2 and disagrees at diag(3/5,2/5) by 9/26 versus 3/10, so it is not affine in μ. For each fixed μ it is inside the August 9 trace-form theorem; it lies outside only the explicit μ-affine ansatz of the August 12 barycenter theorem. The exhibit does not select a physical preparation map or say Born is false."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
  - admissibility_global_measure_menu_kernel_type_separation_bounded_theorem_note_2026-08-10
  - admissibility_barycenter_evaluation_menu_kernel_bounded_theorem_note_2026-08-12
runner: scripts/nonaffine_purity_weighted_kernel_is_not_barycenter_evaluation_2026_08_13.py
---

# Normalized-Square State Map Gives A Non-Affine Measure-To-Grade Kernel

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact finite-support kernels on the qubit density body; one
purity-weighted exhibit compared with barycenter evaluation on `E0=(1/2)P(z)`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nonaffine_purity_weighted_kernel_is_not_barycenter_evaluation_2026_08_13.py`](../scripts/nonaffine_purity_weighted_kernel_is_not_barycenter_evaluation_2026_08_13.py)

## Result Up Front

Let `D` be the `2x2` density body. For a finite-support probability
`μ=Σ_k p_k δ_{ρ_k}` on `D`, write `ρ_μ=Σ_k p_k ρ_k` for the barycenter and

`w_μ(E)=Tr(ρ_μ E)`

for barycenter evaluation. The purity-weighted kernel

`K(μ,E) := Tr(ρ_μ^2 E) / Tr(ρ_μ^2)`

is well-defined on `D`, depends on `μ` only through `ρ_μ`, and is therefore
menu-independent. It satisfies `K(μ,I)=1`, `K(μ,0)=0`, and `K(μ,E)≥0` for
every positive-semidefinite `E`.

At `ρ=I/2` one has `Tr(ρ^2)=1/2` and `Tr(ρ^2 E0)=1/8`, so
`K=1/4=w(E0)`. At `ρ=diag(3/5,2/5)` one has `w(E0)=3/10` while
`Tr(ρ^2)=13/25`, `Tr(ρ^2 E0)=9/50`, and `K=(9/50)/(13/25)=9/26`. The
rationals are distinct because `9/26=45/130` and `3/10=39/130`. The same
biased law is the two-point mixture
`μ=(3/5)δ_{P(z)}+(2/5)δ_{P(-z)}`; the affine mix of `K` at the pure atoms
is `3/10`, not the barycenter value `9/26`, so `K` is not affine in `μ`.

The August 9 frame-lift
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md)
represents every qualifying fixed grade as `Tr(σ E)` for one density `σ`.
The present construction is fully compatible with that theorem: at each fixed
`μ`, its representing density is

`σ_μ=ρ_μ^2/Tr(ρ_μ^2)`.

The relevant comparator is instead the August 12
[`ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md`](ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md),
whose finite-family uniqueness theorem explicitly assumes affine dependence on
`μ` and the spectral endpoints. The present `K` is a concrete non-affine
measure-to-grade kernel outside that ansatz. It does not refute the August 9
trace-form theorem and does not install `σ_μ` as a physical preparation map.

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) remains a
quoted premise and is not edited:

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

## Exact Objects And The Construction

Write `P(n)=(I+n·σ)/2` for a unit Bloch vector `n`. The density body is

`D={ρ∈M_2(C): ρ=ρ^†, ρ≥0, Tr(ρ)=1}`.

A finite-support measure on `D` is `μ=Σ_k p_k δ_{ρ_k}` with `p_k>0`,
`Σ_k p_k=1`, and each `ρ_k∈D`. The barycenter `ρ_μ=Σ_k p_k ρ_k` stays in
`D` by convexity. Barycenter evaluation is `w_μ(E)=Tr(ρ_μ E)`.

The purity-weighted kernel is the ratio

`K(μ,E) := Tr(ρ_μ^2 E) / Tr(ρ_μ^2)`.

On `D` one has `ρ≠0`, so `Tr(ρ^2)=‖ρ‖_HS^2>0` and the denominator never
vanishes. For a qubit, `Tr(ρ^2)` lies in `[1/2,1]`.

The shared effect is the August 10 object

`E0=(1/2)P(z)=diag(1/2,0)`

from
[`ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md`](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md).
That parent records two hostile ternary menus sharing only `E0` and an
atomic restriction witness with

`K_ν(E0|M_A)=25/142`, `K_ν(E0|M_B)=2/11`.

Restriction is a function of the menu. It is used here only as a hostile
control: at `ρ=I/2` one has `K=1/4`, and `25/142≠1/4`.

## Exact Target And Obligation Graph

**Exact target.** Exhibit one menu-independent positive normalized kernel on
`(μ,E)` that is not barycenter evaluation, prove that it is non-affine in
`μ`, and thereby show that the affine hypothesis in the August 12 finite-family
uniqueness theorem is load-bearing. Verify separately that every fixed-`μ`
grade remains inside the August 9 trace-form theorem.

| Obligation | Role | Disposition |
|---|---|---|
| well-definedness, endpoints, positivity, menu-independence | Theorem 1 | proved from `Tr(ρ^2)>0` and the pairing |
| agreement with `w` at `I/2` | Theorem 2 | `K=1/4=w(E0)` |
| disagreement at `diag(3/5,2/5)` | Theorem 3 | `9/26≠3/10` |
| failure of affinity in `μ` | Theorem 4 | atom mix `3/10` versus barycenter `9/26` |
| compare the two parent theorems without conflation | Theorem 5 | inside August 9 pointwise trace form; outside August 12 μ-affine ansatz |
| declare Born false | non-claim | not attempted |
| deny every larger uniqueness theorem | non-claim | not attempted |
| edit an axiom sentence | non-claim | not attempted |

## Theorem 1 — Well-Defined Menu-Independent Positive Normalized Kernel

**Claim.** `K` is well-defined on `D`, depends on `μ` only through `ρ_μ`,
satisfies `K(μ,I)=1` and `K(μ,0)=0`, and obeys `K(μ,E)≥0` whenever `E` is
positive semidefinite. For every finite effect resolution `Σ_i E_i=I`, it
also satisfies `Σ_i K(μ,E_i)=1`.

**Proof.** For `ρ∈D` the Hilbert--Schmidt identity `Tr(ρ^2)=‖ρ‖_HS^2` and
the trace-one constraint give `ρ≠0`, hence `Tr(ρ^2)>0`. The ratio is
therefore defined. It is a function of the pair `(ρ_μ,E)` and has no menu
argument, so the same effect receives the same value in every menu: `K` is
menu-independent.

Linearity of the pairing in the second slot gives

`K(μ,I)=Tr(ρ_μ^2)/Tr(ρ_μ^2)=1`, `K(μ,0)=0`.

If `E≥0`, then `ρ_μ^2≥0` and
`Tr(ρ_μ^2 E)=Tr(E^(1/2)ρ_μ^2E^(1/2))≥0`, so `K(μ,E)≥0`.
Finally, linearity in the effect slot gives

`Σ_i K(μ,E_i)=K(μ,Σ_i E_i)=K(μ,I)=1`.

## Theorem 2 — Agreement With Barycenter Evaluation At The Mixed Point

**Claim.** At `ρ=I/2` one has `Tr(ρ^2)=1/2`, `Tr(ρ^2 E0)=1/8`, and
`K=1/4=w(E0)`.

**Proof.** Direct matrix multiplication yields `ρ^2=I/4`, so
`Tr(ρ^2)=Tr(I)/4=1/2`. Then

`Tr(ρ^2 E0)=Tr((I/4)E0)=(1/4)Tr(E0)=(1/4)(1/2)=1/8`,

and `K=(1/8)/(1/2)=1/4`. Barycenter evaluation is

`w(E0)=Tr((I/2)E0)=1/4`.

The two kernels agree at this mixed point. They still disagree with the
August 10 restriction control: `25/142≠1/4`.

## Theorem 3 — Disagreement At `ρ=diag(3/5,2/5)`

**Claim.** At `ρ=diag(3/5,2/5)` one has `w(E0)=3/10` and `K=9/26`. These
are unequal because `9/26=45/130` and `3/10=39/130`.

**Proof.** Pairing against `E0=diag(1/2,0)` gives

`w(E0)=Tr(ρ E0)=(3/5)(1/2)=3/10`.

The square is `ρ^2=diag(9/25,4/25)`, so `Tr(ρ^2)=13/25` and

`Tr(ρ^2 E0)=(9/25)(1/2)=9/50`.

The purity-weighted value is the ratio

`K=(9/50)/(13/25)=(9/50)·(25/13)=9/26`.

Clearing a common denominator,

`9/26=45/130`, `3/10=39/130`,

and `45≠39`. Thus `K` is not `Tr(ρE)` at this state.

## Theorem 4 — `K` Is Not Affine In `μ`

**Claim.** For `μ=(3/5)δ_{P(z)}+(2/5)δ_{P(-z)}` the barycenter is
`ρ_μ=diag(3/5,2/5)`. The affine mix of `K` at the atoms is `3/10`, while
`K` at the barycenter is `9/26`.

**Proof.** The atoms are pure, so `ρ^2=ρ` and `Tr(ρ^2)=1`. Therefore

`K(δ_{P(z)},E0)=Tr(P(z) E0)=1/2`,
`K(δ_{P(-z)},E0)=Tr(P(-z) E0)=0`.

The affine mix of those values is

`(3/5)·(1/2)+(2/5)·0=3/10`.

Theorem 3 already computed `K(μ,E0)=9/26` at the barycenter of the same
`μ`. Affinity in `μ` would force those two numbers to agree. They do not.

## Theorem 5 — The Affine Preparation Hypothesis Is Load-Bearing

**Claim.** The present `K` is inside the August 9 pointwise trace-form class
for each fixed `μ`, but outside the August 12 ansatz that is affine in `μ`.
It therefore witnesses that the latter affinity hypothesis cannot be dropped
while retaining uniqueness of barycenter evaluation.

**Proof.** For every fixed `μ`, `σ_μ=ρ_μ^2/Tr(ρ_μ^2)` is positive and has
trace one. Hence

`K(μ,E)=Tr(σ_μ E)`.

It is therefore exactly a density-matrix trace grade of the kind classified
by the August 9 theorem; on every effect resolution of `I`, linearity in `E`
gives normalization. August 9 does not take a preparation measure `μ` as an
argument and does not identify its representing density with `ρ_μ`.

The August 12 theorem does take `μ` as an argument and proves uniqueness only
inside the displayed affine Bloch ansatz
`K(μ,E)=a(E)+b(E)·m(μ)`, with positivity, menu normalization, and spectral
endpoints. Theorems 3 and 4 prove that the normalized-square construction is
not affine in `μ` and is not barycenter evaluation. It is consequently
outside that ansatz. It retains the other named hypotheses: Theorem 1 gives
positivity and menu normalization, while for every scaled projector `cP(n)`,
purity gives

`K(δ_{P(n)},cP(n))=c`, `K(δ_{P(-n)},cP(n))=0`.

Thus the construction shows directly that affinity is load-bearing in the
August 12 finite-family uniqueness statement.

**Scope.** The negative is only that this explicit kernel is not barycenter
evaluation and not affine in `μ`. The theorem does not call it a non-Born
probability rule: pointwise in `μ` it is a Born trace grade for `σ_μ`. What
remains open is the physical map from the Admissibility distribution to a
density used for effect evaluation—identity/barycenter, normalized square, or
some other map.

**Steelman.** Because `K(μ,·)` still has a trace form, one should call it a
Born grade at the transformed state `σ_μ`. Correct: the theorem expressly does
so. Its narrower content is that effect-grade uniqueness does not determine
the preparation-to-state map, and the August 12 affine uniqueness theorem
cannot be extended by silently deleting its affinity hypothesis.

## Boundary And Non-Claims

The note does not:

- edit an axiom sentence;
- say Born is false;
- call the normalized-square map a physically selected preparation law;
- identify `M_2(C)` with the density body `D`;
- register a physical menu or a Record readout;
- exclude other non-affine kernels, or install `K` as a physical law.

Restriction remains a hostile control (`25/142≠1/4` at the mixed point). It
is not this kernel.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The normalized-square state map gives an exact finite-matrix exhibit: a pointwise trace-form grade that is menu-independent, positive, and normalized, but is non-affine in the preparation measure and gives 9/26 rather than barycenter evaluation 3/10 at diag(3/5,2/5)."
trace_class: upstream_support
target_claim_id: nonaffine_purity_weighted_kernel_is_not_barycenter_evaluation
target_blocker_text: "exhibit a live non-affine menu-independent kernel that is not barycenter evaluation"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Derive the physical distribution-to-density preparation map and eligible-menu registration; do not confuse pointwise trace-form uniqueness with affinity in the preparation measure."
conditional_surface_status: "exact for the normalized-square map, the 9/26 versus 3/10 split, and the affine-mix gap; physical preparation and Record registration remain open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Admissibility distribution sentence | premise | quoted; no edit |
| August 9 frame-lift uniqueness | pointwise comparator | every fixed-`μ` grade here has its required trace form |
| August 10 `E0` and restriction `25/142` | hostile control | recomputed from traces; not this kernel |
| August 12 barycenter kernel | direct parent | uniqueness only inside its explicit `μ`-affine finite-family ansatz |
| `K=Tr(ρ^2 E)/Tr(ρ^2)` and the `9/26` versus `3/10` split | Theorems 1--4 | computed here |
| physical preparation map / menu registration / Record identification | residual | open |
| observed frequencies or fitted kernels | none | not used |

The exact advance is a finite-matrix exhibit. Independent audit is required.
This note authors no audit verdict.

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The August 12 barycenter theorem expressly leaves non-affine kernels live. This note supplies an exact normalized-square witness while preserving the August 9 pointwise trace-form result. |
| V2 | New content? | Current main contains affine barycenter evaluation and finite-dyadic approximants, but no normalized-square `σ_μ`, `9/26` versus `3/10`, or exact affine-mix gap. |
| V3 | Independently checkable? | Yes. The runner recomputes `Tr(ρ^2)`, `Tr(ρ^2 E0)`, `K`, `w`, and the restriction control `25/142` by exact `Fraction` arithmetic. Identity gates call `purity_kernel`. |
| V4 | More than a restatement? | Yes. `9/26≠3/10` and the atom-mix gap are not restatements of August 9 uniqueness or of August 10 restriction. |
| V5 | One-step relabel? | No. Quoting “menu-independent grade” does not by itself produce the purity-weighted ratio or the `45/130` versus `39/130` comparison. |

## No-Go Discipline Gate (Theorem 5)

The negative claims are restricted to: this kernel is not barycenter
evaluation; this kernel is not affine in `μ`; and the August 12 affine
uniqueness result cannot be widened by deleting affinity. The gate does not
ship “Born is false,” and it expressly keeps the August 9 pointwise trace-form
theorem intact.

### N1 — materially distinct route scan

| Route | Marker | Result against the narrow claim |
|---|---|---|
| normalized-square state map | **ATTEMPTED** | gives the explicit non-affine `9/26` versus `3/10` witness |
| higher normalized powers `ρ↦ρ^q/Tr(ρ^q)` | **ATTEMPTED** | remain live sibling maps for `q>1`; this note classifies none of them |
| [August 12 affine Bloch ansatz](ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md) | **RULED OUT BY PRIOR** | its theorem selects barycenter evaluation only after affinity and endpoint hypotheses are imposed |
| [August 9 fixed-grade frame lift](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md) | **ATTEMPTED** | succeeds pointwise with `σ_μ`; it does not constrain the map `μ↦σ_μ` |
| physical preparation compiler | **ATTEMPTED** | could select barycenter, normalized square, or another density; no such compiler is supplied here |
| convex-mixture operational law | **ATTEMPTED** | a law preserving randomized preparations would impose affinity and exclude this witness; it remains a live physical route |
| [menu restriction of the August 10 atomic measure](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md) | **RULED OUT BY PRIOR** | it is menu-dependent and therefore attacks a different residual |

These are distinct primary mechanisms: nonlinear functional calculus, affine
convexity, pointwise frame representation, physical preparation, operational
mixing, and menu restriction. The theorem closes only existence of one
non-affine mathematical witness.

### N2 — wall independence and collapse

For finite-support measures, affinity together with the pure-state endpoint
map already fixes convex mixtures to barycenter evaluation. “Affinity” and
“barycenter identification” are therefore not counted as independent walls
inside this theorem; they collapse to one preparation-convexity obligation.
Physical menu registration and Record identification are separate downstream
interfaces, outside the mathematical target rather than extra no-go walls.

### N3 — hidden-condition scan

The density-body restriction, finite support, the barycenter `ρ_μ`, the
normalized-square map, the effect `E0`, and the meaning of affinity in `μ` are
all declared. “Menu-independent” refers only to dependence on the effect, not
to physical menu registration. No observed frequency, typicality rule,
continuity premise, Record readout, or physical preparation law is hidden.

### N4 — residual matching

| Source | Source residual | Residual used here | Match? |
|---|---|---|---|
| [August 12 barycenter theorem](ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md) | non-affine kernels lie outside its explicit affine ansatz | construct one such kernel and test the affine-mix identity | yes |
| [August 9 frame lift](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md) | represent one fixed qualifying effect grade by a density | verify `K(μ,·)=Tr(σ_μ·)` for each fixed `μ` | yes; compatibility, not a negative witness |
| [August 10 restriction theorem](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md) | atomic menu restriction is menu-dependent | use `25/142` only as a hostile control | yes; different residual, not uniqueness evidence |
| [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) | no physical distribution-to-effect or preparation map | keep physical selection open | yes |

No earlier no-go is cited as proving that every nonlinear preparation map
fails or succeeds.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | `E0` at `I/2` and at `diag(3/5,2/5)`, with values `1/4`, `9/26`, `3/10`, and the control `25/142` | no classification of every map `(μ,E)→R` |
| per site | one `M_2(C)` density-body site | no composite or intervention theorem |
| per mode | the diagonal family `P(z)`, `P(-z)`, `I/2` | no spectral-mode exhaustion |
| per block | August 9 pointwise trace representation is separated from August 12 preparation affinity | no classification of every nonlinear state map |
| lattice-wide | checked and not executed | no lattice-wide Born no-go |

### N6 — live partial-closure paths

A derived operational rule that randomized preparations map to randomized
states would impose affinity and retire this mathematical freedom. A physical
compiler could instead select the normalized-square map or another nonlinear
map. Effect-menu registration and the Record content bridge remain separate
constructive routes. None is reclassified as requiring an axiom edit.

### N7 — hostile steelman

**Steelman:** This is not a non-Born kernel at all: define
`σ_μ=ρ_μ^2/Tr(ρ_μ^2)`, and the grade is exactly `Tr(σ_μ E)`.

**Answer:** Correct, and that is now part of the theorem. The contribution is
not a counterexample to pointwise Born form. It is an exact witness that the
pointwise trace theorem does not identify the preparation measure's barycenter
with its representing density, and that the August 12 affinity condition is
load-bearing for that identification.

### N8 — cross-cycle echo

The August 12 barycenter theorem left non-affine kernels live. The finite
dyadic theorem later supplied affine finite-`n` approximants that differ from
barycenter evaluation for a separate discretization reason. This note closes
only the outstanding existence example for a genuinely non-affine map; it
does not reuse the dyadic mechanism or promote either construction to a
physical law.

**Gate disposition.** PASS for the normalized-square exhibit, its non-affinity,
and the narrow statement that August 12 affinity is load-bearing. FAIL / DO
NOT SHIP for “Born is false,” “the August 9 theorem fails,” or “this map is
physically selected.”

## Primary Runner

[`scripts/nonaffine_purity_weighted_kernel_is_not_barycenter_evaluation_2026_08_13.py`](../scripts/nonaffine_purity_weighted_kernel_is_not_barycenter_evaluation_2026_08_13.py)
recomputes `Tr(ρ^2)`, `Tr(ρ^2 E0)`, `K`, barycenter evaluation, and the
restriction control `25/142` in exact `Fraction` arithmetic. Identity gates
call `purity_kernel(rho, E)`, equivalently `K(rho, E)`. Replacing `K` by
`Tr(ρE)` must fail `9/26` versus `3/10`.
