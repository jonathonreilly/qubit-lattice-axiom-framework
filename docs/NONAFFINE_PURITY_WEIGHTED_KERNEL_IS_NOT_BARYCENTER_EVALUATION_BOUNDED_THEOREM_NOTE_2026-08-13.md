---
claim_id: nonaffine_purity_weighted_kernel_is_not_barycenter_evaluation_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On finite-support measures on the density body, the purity-weighted kernel K(μ,E)=Tr(ρ_μ^2 E)/Tr(ρ_μ^2) is a well-defined menu-independent positive normalized kernel. It agrees with barycenter evaluation w_μ(E)=Tr(ρ_μ E) at I/2 and disagrees at diag(3/5,2/5) by 9/26 versus 3/10; it is not affine in μ. August 9 uniqueness of Born is among affine or similarly restricted kernels. The exhibit does not say Born is false, does not say that no uniqueness theorem exists in a larger class, and is not an axiom edit."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
  - admissibility_global_measure_menu_kernel_type_separation_bounded_theorem_note_2026-08-10
runner: scripts/nonaffine_purity_weighted_kernel_is_not_barycenter_evaluation_2026_08_13.py
---

# A Live Non-Affine Menu-Independent Kernel Is Not Barycenter Evaluation

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
unique-ifies a menu-independent low-arity grade as `Tr(ρ E)` for one density
`ρ`. That is uniqueness among affine, or similarly restricted, kernels. The
present `K` is a concrete non-affine menu-independent positive normalized
kernel that is not `Tr(ρE)` in the barycenter state. This exhibit does not
say Born is false. This exhibit does not say that no uniqueness theorem
exists in a larger class.

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
`(μ,E)` that is not barycenter evaluation, and scope August 9 uniqueness of
Born to affine or similarly restricted kernels.

| Obligation | Role | Disposition |
|---|---|---|
| well-definedness, endpoints, positivity, menu-independence | Theorem 1 | proved from `Tr(ρ^2)>0` and the pairing |
| agreement with `w` at `I/2` | Theorem 2 | `K=1/4=w(E0)` |
| disagreement at `diag(3/5,2/5)` | Theorem 3 | `9/26≠3/10` |
| failure of affinity in `μ` | Theorem 4 | atom mix `3/10` versus barycenter `9/26` |
| scope August 9 uniqueness | Theorem 5 | affine or similarly restricted class only |
| declare Born false | non-claim | not attempted |
| deny every larger uniqueness theorem | non-claim | not attempted |
| edit an axiom sentence | non-claim | not attempted |

## Theorem 1 — Well-Defined Menu-Independent Positive Normalized Kernel

**Claim.** `K` is well-defined on `D`, depends on `μ` only through `ρ_μ`,
satisfies `K(μ,I)=1` and `K(μ,0)=0`, and obeys `K(μ,E)≥0` whenever `E` is
positive semidefinite.

**Proof.** For `ρ∈D` the Hilbert--Schmidt identity `Tr(ρ^2)=‖ρ‖_HS^2` and
the trace-one constraint give `ρ≠0`, hence `Tr(ρ^2)>0`. The ratio is
therefore defined. It is a function of the pair `(ρ_μ,E)` and has no menu
argument, so the same effect receives the same value in every menu: `K` is
menu-independent.

Linearity of the pairing in the second slot gives

`K(μ,I)=Tr(ρ_μ^2)/Tr(ρ_μ^2)=1`, `K(μ,0)=0`.

If `E≥0`, then `ρ_μ^2≥0` and `Tr(ρ_μ^2 E)≥0`, so `K(μ,E)≥0`.

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

## Theorem 5 — Scoped Uniqueness (N5)

**Claim.** August 9 uniqueness of Born is among affine, or similarly
restricted, kernels. The present `K` is a concrete non-affine
menu-independent positive normalized kernel that is not `Tr(ρE)`. This
exhibit does not say Born is false. This exhibit does not say that no
uniqueness theorem exists in a larger class.

**Proof.** The August 9 theorem states that a menu-independent grading on
the scaled domain `S`, normalized on every binary and ternary nonzero
resolution of `I`, has a unique density-matrix trace form
`w(E)=Tr(ρ E)` on `S`. That hypothesis class is a restriction: the grade is
a function of the effect alone, the eligible menus are the low-arity scaled
family, and the representing state is unique. Equivalently, once a state is
identified with a barycenter `ρ_μ`, uniqueness of `w_μ(E)=Tr(ρ_μ E)` is a
statement about kernels affine in the Bloch coordinates of `ρ_μ`, or about
kernels similarly restricted to a single trace pairing against that
barycenter.

The kernel `K` of Theorems 1--4 lies outside that class as a function of
`μ`. It is menu-independent, positive on PSD effects, and normalized at
`0` and `I`, yet Theorem 4 shows it is not affine in `μ`, and Theorem 3
shows it is not barycenter evaluation. That is the executed exhibit.

**Scope.** The negative is only that *this* live kernel is not barycenter
evaluation and is not affine in `μ`, so uniqueness of Born cannot be quoted
as if it applied to every menu-independent positive normalized kernel of
`(μ,E)`. The negative does not say the Born trace form is false: at each
fixed `μ` the map `E↦K(μ,E)` is still the pairing `Tr(σ_μ E)` against the
density `σ_μ=ρ_μ^2/Tr(ρ_μ^2)`. The negative does not say that no uniqueness
theorem exists among a larger class than the affine or similarly restricted
kernels. No such larger theorem is claimed or denied here.

**Steelman.** Because `K(μ,·)` still has a trace form, one might call `K`
Born and conclude that the exhibit is empty. That reading changes the
variable. The comparison target is barycenter evaluation `Tr(ρ_μ E)` as a
kernel of the preparation measure. Theorems 3 and 4 separate `K` from that
target. They do not attack the existence of some density against which `K`
pairs.

## Boundary And Non-Claims

The note does not:

- edit an axiom sentence;
- say Born is false;
- say that no uniqueness theorem exists in a larger class;
- identify `M_2(C)` with the density body `D`;
- register a physical menu or a Record readout;
- exclude other non-affine kernels, or install `K` as a physical law.

Restriction remains a hostile control (`25/142≠1/4` at the mixed point). It
is not this kernel.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The purity-weighted kernel is an exact finite-matrix exhibit: well-defined, menu-independent, positive, and normalized, with K=9/26 versus barycenter evaluation 3/10 at diag(3/5,2/5). Uniqueness of Born is scoped to affine or similarly restricted kernels. The exhibit does not say Born is false."
trace_class: negative_route_pruning
target_claim_id: nonaffine_purity_weighted_kernel_is_not_barycenter_evaluation
target_blocker_text: "exhibit a live non-affine menu-independent kernel that is not barycenter evaluation"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Keep uniqueness claims inside the affine or similarly restricted class. Do not identify every menu-independent kernel with Tr(rho_mu E)."
conditional_surface_status: "exact for the 9/26 versus 3/10 split and the affine-mix gap; physical registration and larger uniqueness theorems remain open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Admissibility distribution sentence | premise | quoted; no edit |
| August 9 frame-lift uniqueness | scoped parent | uniqueness among restricted grades |
| August 10 `E0` and restriction `25/142` | hostile control | recomputed from traces; not this kernel |
| `K=Tr(ρ^2 E)/Tr(ρ^2)` and the `9/26` versus `3/10` split | Theorems 1--4 | computed here |
| physical menu registration / Record identification | residual | open |
| observed frequencies or fitted kernels | none | not used |

The exact advance is a finite-matrix exhibit. Independent audit is required.
This note authors no audit verdict.

## Promotion Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | August 10 leaves barycenter/evaluation live after restriction fails, and August 9 unique-ifies a menu-independent low-arity grade. This note exhibits a live non-affine kernel that is not that barycenter evaluation. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` for `9/26`, `purity-weighted`, and `Tr(ρ^2 E)`. No landed purity-weighted versus barycenter-evaluation split appears on that commit. |
| V3 | Independently checkable? | Yes. The runner recomputes `Tr(ρ^2)`, `Tr(ρ^2 E0)`, `K`, `w`, and the restriction control `25/142` by exact `Fraction` arithmetic. Identity gates call `purity_kernel`. |
| V4 | More than a restatement? | Yes. `9/26≠3/10` and the atom-mix gap are not restatements of August 9 uniqueness or of August 10 restriction. |
| V5 | One-step relabel? | No. Quoting “menu-independent grade” does not by itself produce the purity-weighted ratio or the `45/130` versus `39/130` comparison. |

## No-Go Discipline Gate (Theorem 5)

The negative claims are restricted to: this kernel is not barycenter
evaluation; this kernel is not affine in `μ`; August 9 uniqueness is not a
license to identify every menu-independent kernel with `Tr(ρ_μ E)`. The gate
does not ship “Born is false” or “no uniqueness theorem exists in a larger
class.”

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | `E0` at `I/2` and at `diag(3/5,2/5)`, with values `1/4`, `9/26`, `3/10`, and the control `25/142` | no classification of every map `(μ,E)→R` |
| per site | one `M_2(C)` density-body site | no composite or intervention theorem |
| per mode | the diagonal family `P(z)`, `P(-z)`, `I/2` | no spectral-mode exhaustion |
| per block | Theorem 5 only scopes August 9 uniqueness to affine or similarly restricted kernels | no denial of every larger uniqueness theorem |
| lattice-wide | checked and not executed | no lattice-wide Born no-go |

**Gate disposition.** PASS for the `9/26` versus `3/10` exhibit and the
Theorem 5 scope. FAIL / DO NOT SHIP for “Born is false” or “no uniqueness
theorem exists in a larger class.”

## Primary Runner

[`scripts/nonaffine_purity_weighted_kernel_is_not_barycenter_evaluation_2026_08_13.py`](../scripts/nonaffine_purity_weighted_kernel_is_not_barycenter_evaluation_2026_08_13.py)
recomputes `Tr(ρ^2)`, `Tr(ρ^2 E0)`, `K`, barycenter evaluation, and the
restriction control `25/142` in exact `Fraction` arithmetic. Identity gates
call `purity_kernel(rho, E)`, equivalently `K(rho, E)`. Replacing `K` by
`Tr(ρE)` must fail `9/26` versus `3/10`.
