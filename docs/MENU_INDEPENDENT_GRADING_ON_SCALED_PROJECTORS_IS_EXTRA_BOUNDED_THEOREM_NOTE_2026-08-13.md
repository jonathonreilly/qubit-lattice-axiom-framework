---
claim_id: menu_independent_grading_on_scaled_projectors_is_extra_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "At one M_2(C) site, two exact trial grades on the scaled family {0, P_z, I} disagree at P_z. The current Admissibility and Record sentences name a nearest-neighbor distribution over possibilities and a lock-plus-additive-readout, not a menu-independent grade w on scaled projectors. The August 9 uniqueness theorem supplies a unique density matrix only after such a w is already the instrument. This note names that extra matching. It does not improve August 9, import Gleason as physics, say Born is false, force r=1/2, or adopt L_phys."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
runner: scripts/menu_independent_grading_on_scaled_projectors_is_extra_2026_08_13.py
---

# A Menu-Independent Grading On Scaled Projectors Is Extra

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact one-site type comparison among two displayed trial grades,
the current axiom sentences, and the August 9 uniqueness hypothesis.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/menu_independent_grading_on_scaled_projectors_is_extra_2026_08_13.py`](../scripts/menu_independent_grading_on_scaled_projectors_is_extra_2026_08_13.py)

## Result Up Front

August 9 uniqueness is uniqueness *among* menu-independent, low-arity-normalized
grades on the scaled-projector domain. This block names the extra matching,
not a new Gleason theorem.

Two exact trial grades already disagree on `{0,P_z,I}`. The current
Admissibility and Record sentences do not name either grade. Selecting
`w_ρ` as the instrument is therefore an extra matching, displayed here and
not adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: negative_route_pruning
target_claim_id: menu_independent_grading_on_scaled_projectors_is_extra
target_blocker_text: "name the extra matching that a menu-independent scaled-projector grade exists and is the instrument"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
conditional_surface_status: "exact disagreement of two displayed grades; extra matching named; no axiom edit"
hypothetical_axiom_status: "no candidate wording is adopted"
admitted_observation_status: null
claim_type_reason: "The two grades, the axiom-text comparison, and the August 9 conditional uniqueness statement are exact finite objects. The matching that such a w exists and is the instrument remains extra."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work at one site with `H=C^2`. Write

`P_z=diag(1,0)` and `I=diag(1,1)`.

The trial domain is the scaled family

`{0,P_z,I}={c P_z:0<=c<=1} union {c I:0<=c<=1}`.

Two trial grades on that family are displayed, not adopted:

- `w_ρ(c P_z)=c·3/5` and `w_ρ(c I)=c`, from `ρ=diag(3/5,2/5)`;
- `w_*(c P_z)=c·1/2` and `w_*(c I)=c`, from `I/2`.

Both send `0` to `0` and `I` to `1`. They are exact rational functions. They
are not identified with a physical instrument, a selected density law, or an
axiom sentence.

The August 9 parent,
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md),
works on the larger scaled domain `S` of nonnegative multiples of rank-one
projectors and of the identity. Its uniqueness statement is recalled only as
already written there. This note does not extend, re-prove, or improve it.

## Theorem 1 — Two Different Grades

Evaluate the displayed grades at the unscaled projector:

`w_ρ(P_z)=3/5 ≠ 1/2=w_*(P_z)`.

The same split persists under scaling: for every `c in (0,1]`,

`w_ρ(c P_z)=c·3/5 ≠ c·1/2=w_*(c P_z)`.

The two functions agree on the identity ray, since both satisfy
`w_ρ(c I)=c=w_*(c I)`. Agreement on `{0,I}` does not force agreement on
`P_z`. Therefore a predicate `w_ρ=w_*` fails at `P_z`.

This is only a witness that more than one exact grade exists on the trial
family. It does not select a density matrix, force `r=1/2`, or say that Born
weights are unavailable later.

## Theorem 2 — The Axiom Sentences Do Not Name `w`

The current Admissibility sentence in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is:

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

The current Record sentences used here are:

> When present, a record locks exactly one admissible local possibility.

and

> For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

Admissibility names a nearest-neighbor-determined distribution over
possibilities. Record names a lock of one possibility and an additive scalar
readout of record collections. Neither sentence names a grade `w` on scaled
projectors. In particular, neither sentence names `w_ρ`. A predicate
“axioms name `w_ρ`” fails.

This is a textual comparison with the linked axiom memo. It is not a theorem
that no later derivation can produce a grade.

## Theorem 3 — August 9 Uniqueness Is Conditional On The Extra Matching

The August 9 parent states the exact claim:

> There is a unique density matrix `rho in M_2(C)` such that
> `w(E)=Tr(rho E)` for every `E in S`.

The parent’s declared inputs are a menu-independent function `w` on the
scaled-projector domain and normalization on every binary and ternary nonzero
scaled-projector resolution of the identity. The uniqueness is therefore
uniqueness *among such grades*: *if* a grade is menu-independent and
normalized on binary and ternary scaled-projector menus, then it is
`Tr(ρ E)` for a unique `ρ`.

That uniqueness is conditional on the extra matching “such a `w` exists and
is the instrument.” Display `w_ρ`; do not adopt it. Displaying `w_ρ` shows
one Born-shaped grade that August 9 would recover *after* the matching is
supplied. The matching is not written in the Admissibility or Record
sentences of Theorem 2, and Theorem 1 shows that a different displayed grade
`w_*` is available on the same trial family.

## Theorem 4 — No Improvement, No Gleason-As-Physics, No Born Denial

This note does not claim that the August 9 theorem is improved. The parent
already records uniqueness among the grades it assumes. Naming the extra
matching does not enlarge the mathematical domain, drop a hypothesis, or
replace the parent’s named frame step.

This note does not import Gleason as physics. No frame-function theorem is
re-proved or treated as a physical registration of menus.

This note does not say Born is false. Both displayed grades are Born-shaped
on the trial family. The claim is only that the axioms do not already name
one of them as the instrument.

## Theorem 5 — No Forced Maximally Mixed Ray And No `L_phys`

This note does not force `r=1/2`. The grade `w_*` is a displayed control,
not a selected physical state. Nothing here installs a preferred Bloch
radius, a preferred mixed state, or a preferred value of `w(P_z)`.

This note does not adopt `L_phys`. No physical-length primitive, spacetime
metric, or laboratory scale is introduced or selected.

## Mutation Predicates

The runner’s identity gates call `w_rho(Pz)` and `w_star(Pz)` and check

`w_rho(Pz)=3/5` and `w_star(Pz)=1/2`.

The equality predicate `w_ρ=w_*` is tested only at `P_z` and must fail.
The naming predicate “axioms name `w_ρ`” is tested against the current axiom
memo and must fail.

## Claim Boundary

| Claim | Status in this note |
|---|---|
| `w_ρ(P_z)=3/5 ≠ 1/2=w_*(P_z)` | proved on the displayed trial family |
| Admissibility and Record name a grade `w` on scaled projectors | false as written; extra matching |
| August 9 uniqueness among supplied menu-independent low-arity grades | recalled, not improved |
| such a `w` exists and is the physical instrument | extra matching; displayed, not adopted |
| Gleason is a physical law of the lattice | not claimed; not imported |
| Born is false | not claimed |
| `r=1/2` is forced | not claimed |
| `L_phys` is adopted | not claimed |
| no later compiler can supply a grade | not claimed |

## Imports And Claim Boundary

| Item | Role | Provenance | Open-bridge status |
|---|---|---|---|
| `M_2(C)` one-site possibility presentation | carrier context | current Qubit axiom | supplied algebraic presentation |
| Admissibility distribution sentence | textual baseline | current axiom memo | does not name `w` |
| Record lock and additive `I` | textual baseline | current axiom memo | does not name `w` |
| August 9 uniqueness among menu-independent low-arity grades | parent mathematics | linked August 9 note | conditional on the extra matching |
| displayed `w_ρ` and `w_*` | exact trial grades | this note | not adopted as instruments |
| Gleason / frame theorem as physics | none | not imported | not applicable |
| `L_phys`, forced `r=1/2` | none | not used | not applicable |

Independent audit remains required before the repository may assign any
effective claim status.
