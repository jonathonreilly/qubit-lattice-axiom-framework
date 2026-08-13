---
claim_id: axioms_do_not_select_which_pvm_a_luders_instrument_reads_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "At one M_2(C) site, the Born weights on two declared rank-one projective menus disagree at an explicit polarized density matrix. The current Qubit and Admissibility sentences name the possibility domain and a nearest-neighbor-determined distribution; they do not name P_z versus P_x. A later compiler that returns Born weights still consumes a declared PVM. The result does not replace the August 9 frame-lift theorem, does not deny Born form, does not select n=z by cubic covariance, does not force r=1/2, and does not adopt a PVM axiom."
upstream_dependencies:
  - minimal_axioms
  - born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09
runner: scripts/axioms_do_not_select_which_pvm_a_luders_instrument_reads_2026_08_13.py
---

# Axioms Do Not Select Which PVM A Lüders Instrument Reads

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact one-site menu-declaration hygiene under the current
`M_2(C)` possibility-domain wording.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/axioms_do_not_select_which_pvm_a_luders_instrument_reads_2026_08_13.py`](../scripts/axioms_do_not_select_which_pvm_a_luders_instrument_reads_2026_08_13.py)

## Result Up Front

Born weights on a declared projector-valued menu are the ordinary trace
kernel. That kernel does not pick the menu.

Two explicit rank-one menus at one qubit site already disagree on an explicit
polarized density matrix. The current Qubit and Admissibility sentences do
not name either menu. A later Lüders compiler that returns those Born
weights still consumes a declared projector, or an equivalent unit Bloch
vector. The menu is extra structure.

This note does not improve or replace
[`BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md).
It does not say Born is false. It does not select `n=z` by cubic covariance:
a polarized density matrix is allowed. It does not force `r=1/2`. It does
not adopt a PVM axiom. Both menus

`{P_z, I-P_z}` and `{P_x, I-P_x}`

are displayed; neither is adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The two-menu Born disagreement and the textual non-selection of P_z versus P_x are exact on declared one-site objects, while a later instrument compiler, physical menu registration, and any PVM-selecting law remain extra or open."
trace_class: negative_route_pruning
target_claim_id: axioms_select_luders_pvm_menu
target_blocker_text: "show that the four axioms do not name which declared PVM a later Lüders compiler reads"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
conditional_surface_status: "exact for the displayed two-menu kernel values and the quoted axiom sentences; physical compilation of a preferred menu remains open"
hypothetical_axiom_status: "no PVM-selecting clause is displayed, recommended, or adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work at one site, with `H=C^2`. Write `I` for the `2x2` identity and

`P_z = diag(1,0)`,
`P_x = (I+sigma_x)/2 = [[1/2,1/2],[1/2,1/2]]`,
`rho = diag(3/5, 2/5)`.

Both pairs `{P_z, I-P_z}` and `{P_x, I-P_x}` are rank-one resolutions of
`I`. They are the two declared projective menus used below.

On a declared projector `P`, the Born kernel is the exact trace

`K(sigma,P)=Tr(sigma P)`.

The same kernel evaluated on `I-P` is `1-K(sigma,P)` whenever
`Tr(sigma)=1`. The kernel is a function of a supplied pair `(sigma,P)`. It
does not invent `P`.

The Bloch form of the displayed state is

`rho = (I + (1/5) sigma_z)/2`.

Its Bloch radius is `1/5`, not `1/2`. The state is polarized and positive
with trace one.

## Theorem 1 — The Two Declared Menus Disagree

`K(rho, P_z)=Tr(rho P_z)=3/5`.

`K(rho, P_x)=Tr(rho P_x)=(3/5)(1/2)+(2/5)(1/2)=1/2`.

Therefore

`3/5 != 1/2`,

so the predicate `K(rho, P_z)=K(rho, P_x)` fails at this `rho`. The two
declared menus are not interchangeable as readout data for the same state.
The complementary weights are `2/5` on `I-P_z` and `1/2` on `I-P_x`.

This is ordinary finite-matrix arithmetic. No continuity, measurability, or
frame-function hypothesis is used.

## Theorem 2 — The Current Axiom Sentences Do Not Name Either Menu

The current Qubit sentences in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) are:

> The full one-site possibility domain has algebraic presentation `M_2(C)`.
>
> No possibility is privileged. Possibilities are distinguished by the
> supplied algebraic structure alone.

The current Admissibility distribution sentence is:

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

Neither sentence names `P_z` versus `P_x`. Neither sentence names a unit
Bloch vector `n`, a distinguished rank-one projector, or a preferred
projective menu. The predicate "axioms name `P_z`" therefore fails on the
canonical text.

Qubit supplies the carrier on which both projectors live. Admissibility
supplies a nearest-neighbor-determined distribution over possibilities. Those
are not a declared PVM.

## Theorem 3 — A Later Lüders Compiler Still Needs A Declared PVM

Suppose a later compiler is given a projector `P` and returns the two-outcome
Lüders instrument that reads `{P, I-P}` with Born weights `K(sigma,P)` and
`1-K(sigma,P)`. The output of that compiler is then exactly the kernel of
Theorem 1.

The compiler still consumes the declared menu. The declaration may be written
as a projector `P` or as a unit vector `n` with `P=(I+n·sigma)/2`. Either
form is extra relative to the sentences quoted in Theorem 2.

Both displayed menus are well-formed inputs to such a compiler:

- `{P_z, I-P_z}` yields weights `{3/5, 2/5}` at `rho`;
- `{P_x, I-P_x}` yields weights `{1/2, 1/2}` at `rho`.

Neither menu is adopted here. The later compiler, if written, remains a
downstream map from a declared PVM to an instrument. It is not a selector of
which PVM the current axioms already named.

## Theorem 4 — August 9, Born Form, And Cubic Covariance Are Untouched

This note does not improve or replace the August 9 parent. That parent forces
the trace form on the scaled-projector domain after a menu-independent
low-arity grading is supplied. The present note does not revisit that
forcing, does not weaken it, and does not enlarge its menu family.

This note does not say Born is false. The kernel `K(sigma,P)=Tr(sigma P)` is
used as the declared-menu evaluation rule. The disagreement in Theorem 1 is a
disagreement between two menus, not a failure of the trace formula.

This note does not select `n=z` by cubic covariance. Lattice and
Admissibility are covariant under proper cubic rotations about a site. A
90-degree rotation about the `y`-axis exchanges the `z` and `x` axes and
therefore exchanges `P_z` with `P_x`. A cubic-covariant rule cannot privilege
the `z` menu over the `x` menu. A polarized density matrix remains allowed:
`rho` above is positive, has trace one, and is not `I/2`. Covariance of the
rule is not isotropy of every state.

## Theorem 5 — No Forced Radius And No PVM Axiom

This note does not force `r=1/2`. The displayed Bloch radius is `1/5`. The
`x`-menu weight `1/2` at this `rho` is a matrix identity, not a requirement
that every state or every selector sit at radius `1/2`.

This note does not adopt a PVM axiom. No fifth axiom naming a distinguished
projector, a distinguished Bloch axis, or a preferred Lüders menu is stated,
recommended, or inserted into the canonical memo.

## Relation To The Current Axioms And To August 9

[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) already records,
among the open gates outside the axioms, context selection and measurement
basis selection. Theorem 2 is the one-site matrix reading of that gate:
`P_z` versus `P_x` is a basis-selection datum, not axiom content.

The August 9 parent remains the bounded theorem for the trace form on a
supplied low-arity grading. The present note answers a different question:
once that form is granted on a declared projector, which projector is read.
The four axioms do not answer that question. Displaying two disagreeing
menus keeps the residual visible.

No inference of impossibility is made about a later derivation that would
construct a physical menu from neighboring records, from a contact compiler,
or from another landed structure. Such a derivation would supply the missing
declaration. It would not show that the present axiom sentences already named
`P_z`.

## No-Go Discipline Gate

The negative claims are restricted to (i) equality of the two displayed
Born weights at this `rho` and (ii) the claim that the current axiom
sentences already name `P_z` or otherwise select a PVM. The gate does not
certify a global non-derivability theorem about instruments.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Identify the two menus | require `K(rho,P_z)=K(rho,P_x)` | Theorem 1 gives the exact values `3/5 != 1/2` | **ATTEMPTED** |
| Read `P_z` off Qubit | treat `M_2(C)` plus "no possibility is privileged" as naming a projector | Theorem 2: the quoted sentences do not name `P_z` or `P_x` | **ATTEMPTED** |
| Read `P_z` off Admissibility | treat the nearest-neighbor distribution sentence as a PVM declaration | Theorem 2: that sentence names no projector | **ATTEMPTED** |
| Let cubic covariance pick `n=z` | invoke proper cubic rotations to privilege the `z` axis | Theorem 4: those rotations exchange `P_z` with `P_x`; a polarized `rho` remains allowed | **ATTEMPTED** |
| Force `r=1/2` to erase the disagreement | specialize the Bloch radius until the menus agree | Theorem 5: the displayed radius is `1/5`; the disagreement is the point | **ATTEMPTED** |
| Hide the menu inside a later compiler | treat a Lüders compiler as selecting `P` by itself | Theorem 3: the compiler consumes a declared `P` or `n` | **ATTEMPTED** |
| Replace August 9 | treat menu non-selection as a defect of the trace form | Theorem 4: August 9 is untouched and Born is not denied | **ATTEMPTED** |

The last route is a misreading rather than a live construction. Constructive
routes that *supply* a declared menu from other structure remain open.

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| declared PVM / Born kernel on that PVM | no: a projector does not evaluate itself | no: `K(sigma,P)=Tr(sigma P)` names no distinguished `P` | independent |
| Qubit carrier / distinguished projector | no: `M_2(C)` contains every rank-one projector | no: naming `P_z` does not supply the possibility domain | independent |
| Admissibility distribution / distinguished projector | no: a distribution over possibilities names no menu | no: a declared menu does not determine the nearest-neighbor law | independent |
| cubic covariance of the rule / isotropic states | no: a covariant rule may still admit polarized states | no: one polarized state does not break rule covariance | independent |
| August 9 trace form / PVM selection | no: the parent consumes a supplied grading, not a preferred axis | no: displaying two menus does not revisit the frame lift | independent |

The missing declaration is one wall. It is not collapsed into the Born kernel,
the August 9 parent, or a cubic-isotropy demand.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `P_z`, `P_x`, `rho` | explicit finite matrices, written before Theorem 1 |
| `K(sigma,P)=Tr(sigma P)` | declared-menu evaluation rule, not a hidden state-to-menu map |
| "Lüders compiler" | later map from a declared PVM to a two-outcome instrument; not present in the axioms and not adopted |
| "declared PVM" | explicit extra input: a projector or a unit vector `n` |
| cubic rotation about `y` | explicit proper cubic rotation exchanging the two displayed axes |
| Bloch radius `1/5` | exact identity for the displayed `rho` |
| August 9 parent | explicit dependency for the untouched trace-form boundary only |
| observations or fitted radii | none |

No dim-2 frame theorem, hidden preferred axis, or axiom edit is used.

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | one-site `M_2(C)` domain; no possibility privileged; nearest-neighbor-determined distribution; measurement-basis selection listed among open gates | quoted wording only; no projector conclusion borrowed |
| [`docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md`](BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md) | unique trace form after a menu-independent low-arity grading is supplied | used only as the untouched parent; not improved or replaced |

No citation is used as authority for the `3/5` versus `1/2` arithmetic; that
identity is proved here and checked by the runner.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | two rank-one projectors and one polarized density matrix | no classification of every instrument |
| per site | one `M_2(C)` site | no composite or multi-site instrument theorem |
| per mode | the `z` and `x` axes, plus the cubic rotation that exchanges them | no exhaustion of every Bloch direction |
| per block | PVM declaration versus Born evaluation | no complete Record/update closure |
| lattice-wide | cubic covariance is invoked only to refuse a privileged axis | no lattice-wide dynamics or Born denial |

The risky sentence family is "the axioms cannot produce a Lüders instrument."
This note uses the narrower form: the current sentences do not name which
declared PVM such an instrument would read.

### N6 — live partial-closure paths

1. A neighboring-record encoding of an apparatus could derive a declared
   projector from landed content.
2. A contact compiler could supply one physical menu, after which Theorem 1's
   kernel evaluates that menu.
3. An operational equivalence theorem could identify two laboratory
   implementations as the same projector without privileging `z` in the
   axioms.
4. The August 9 parent remains available once a menu-independent grading on
   a declared family is supplied.

None of these paths is closed here. None is a reason to adopt a PVM axiom.

### N7 — hostile steelman

> Cubic covariance plus a unique nearest-neighbor rule might still pick a
> preferred local axis once a polarized neighbor configuration is given, and
> a later Lüders compiler could then read that axis. In that reading the
> axioms already select the PVM, up to an implicit function of the neighbors.

The steelman is a constructive program, not a present derivation. A neighbor
configuration can be polarized, as `rho` itself shows. The current sentences
still do not name the map from those neighbors to `{P_z, I-P_z}` rather than
`{P_x, I-P_x}`. Until that map is derived, the menu remains extra.

### N8 — cross-cycle echo

| Earlier surface | Later movement | Echo here |
|---|---|---|
| August 9 forces Born form on a supplied low-arity grading | the grading and eligible menus remain explicit inputs | this note does not reopen or replace that forcing |
| Admissibility names a distribution over possibilities | August 10 separates that global measure from a menu kernel | the present note separates the same kernel from the choice of PVM |
| open gates already list measurement basis selection | no later landed sentence names `P_z` versus `P_x` | Theorem 2 is the matrix reading of that existing gate |

**Gate disposition:** PASS for (i) `K(rho,P_z)!=K(rho,P_x)` at the displayed
state, (ii) failure of the predicate that the current axiom sentences name
`P_z`, and (iii) the statement that a later Lüders compiler still consumes a
declared PVM. FAIL / DO NOT SHIP for "Born is false," "August 9 is replaced,"
"`n=z` is selected by cubic covariance," "`r=1/2` is forced," or "a PVM axiom is adopted."

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Qubit and Admissibility sentences | exact semantic baseline | supplied; no edit |
| `P_z`, `P_x`, `rho` | Theorem 1 witnesses | constructed here |
| `K(sigma,P)=Tr(sigma P)` | declared-menu evaluation | definition-level mathematics |
| later Lüders compiler | Theorem 3 consumer of a declared PVM | not current authority; not adopted |
| August 9 frame-lift theorem | untouched parent | explicit non-replacement |
| PVM-selecting axiom | forbidden closure in this note | not stated and not adopted |
| observed frequencies or fitted axes | none | not used |

The exact advance is a menu-declaration theorem. It does not move the
August 9 trace-form residual. It makes the next instrument question
testable: derive a declared PVM from landed structure, or leave the menu
explicit. Do not read `P_z` off the present axiom sentences.

## Review Record

Independent audit remains required before any effective status may change.
No `review-loop` was invoked in producing or self-reviewing this artifact.
