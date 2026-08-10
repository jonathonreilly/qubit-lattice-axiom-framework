---
claim_id: admissibility_cnot_contact_gaussian_extractor_type_order_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For the explicit full-support Gaussian Admissibility family and the displayed isotropic density-operator-extractor family on one M_2(C) site, a basis-control incoming CNOT extends algebraically as X-conjugation and transports every extractor member covariantly. It does not type a generic raw M_2(C) realization as a density operator: the qubit density-operator set has Gaussian measure zero. At C=P_z, a fixed half-P_z effect receives (3/10,1/5) across the two control conditions for lambda=0 and (2/7,3/14) for lambda=1, while co-transporting the effect restores the original grade but changes the effect. A random or coherent control with supplied one-weight q prepares diag(1-q,q) from a blank target, including q=2/5 and q=3/7 for the two displayed extractor members, so CNOT is an exact carrier of a supplied spectrum but does not select its weight. The result proves a bounded type-order and fixed-effect boundary for the declared one-edge contact route; it proves no global unitary/contact no-go, no physical compiler selection, and no axiom necessity claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_gaussian_second_moment_quantile_decoder_effect_quotient_bounded_theorem_note_2026-08-10
runner: scripts/admissibility_cnot_contact_gaussian_extractor_type_order_2026_08_10.py
---

# CNOT Contact, Gaussian Extractor Equivariance, And Type Order

**Date:** 2026-08-10
**Type:** bounded theorem and constructive physical-compiler interface test
**Scope:** one `M_2(C)` target, one basis-control neighbor, the explicit
Gaussian law, and the displayed isotropic extractor family.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/admissibility_cnot_contact_gaussian_extractor_type_order_2026_08_10.py`](../scripts/admissibility_cnot_contact_gaussian_extractor_type_order_2026_08_10.py)
**Runner cache:**
[`logs/runner-cache/admissibility_cnot_contact_gaussian_extractor_type_order_2026_08_10.txt`](../logs/runner-cache/admissibility_cnot_contact_gaussian_extractor_type_order_2026_08_10.txt)

## Result Up Front

Block 4 constructed a complete fixed-condition mathematical
measure-to-density-operator-to-quantile-decoder compiler on one explicit
Gaussian completion, but physical selection and program registration remained
open. The new finite contact seed in PR #6069 supplies exact covariant
incoming-CNOT/XOR dependence on basis states. This block tests that seed
against the continuous compiler without importing the PR's branch artifacts.

The exact result has six parts.

1. The current raw possibility content is an arbitrary element of `M_2(C)`.
   The density-operator set `D_2` has real dimension three inside the
   eight-real-dimensional content space. The full-support Gaussian law is
   absolutely continuous, so `mu_C(D_2)=0`. A generic locked possibility is
   therefore not already a density operator.
2. With a basis control `n`, incoming CNOT acts on a typed target operator by
   `T_n(B)=X^n B X^n`. The same formula is a valid algebra automorphism on raw
   matrix content. It pushes the Gaussian center `C` to `X^n C X^n` and
   transports every displayed `lambda` extractor member covariantly.
3. Contact covariance does not select the extractor. Every `lambda>=0`
   survives. At `C=P_z`, the fixed effect `E_0=(1/2)P_z` gives
   `(w_0,w_1)=(3/10,1/5)` at `lambda=0` and `(2/7,3/14)` at `lambda=1`.
4. Co-transporting the effect restores the grade exactly, but that is
   covariance between `(rho,E)` pairs, not the same-effect quotient across
   two program conditions.
5. A supplied random or coherent control with one-weight `q` and a blank
   target prepares `diag(1-q,q)` after CNOT and control erasure. Thus `q_0=2/5`
   prepares the raw second-moment fixture and `q_1=3/7` prepares the
   `lambda=1` fixture. This is an exact positive escape, but the contact does
   not select the control weight.
6. With a fixed pure control, the target update is unitary conjugation and
   preserves its spectrum. It cannot turn one common blank target into the
   Block 4 family whose spectrum changes between `C=0` and `C=P_z`. Mixing or
   erasing a control can change the spectrum only by importing the control law,
   blank, and reduction interface.

The contact is therefore a carrier, not a selector. The conclusion is bounded
to the declared conditioned-CNOT route. Larger local instruments, dissipative
laws, measure-level aggregators, record-derived process laws, and direct
quantile comparators remain live. No global unitary or contact no-go is
claimed, and no canonical axiom is edited.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Gaussian density-set typing, conditioned-CNOT extractor equivariance, fixed-versus-transported effect grades, and supplied-control mixture factorization; physical extractor/control selection, program registration, occurrence, and axiom adoption remain open."
trace_class: upstream_support
target_claim_id: admissibility_record_physical_compiler_selection_bridge
target_blocker_text: "derive physical compiler selection and preparation/program registration from local contact dynamics"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Test a local law that derives rather than supplies the control mixture/eigenbasis or directly computes the Gaussian quantile, while preserving physical preparation equivalence and Record occurrence."
conditional_surface_status: "exact one-edge CNOT carrier/equivariance and fixed-effect boundary on the displayed Gaussian extractor family; compiler selection and physical preparation/program registration remain open"
hypothetical_axiom_status: "the missing selector is narrowed to a law-derived density functional or law-derived control mixture/eigenbasis plus program quotient; no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Target And Obligation Graph

**Exact target.** Decide whether the finite covariant incoming-CNOT contact
mechanism can select and physically register Block 4's Gaussian
density-operator/decoder compiler, rather than merely act on an already typed
and prepared target.

| Obligation | Role | Disposition |
|---|---|---|
| type a raw Gaussian realization as a physical density operator | state typing | not supplied; the density-operator subset has Gaussian measure zero |
| extend incoming CNOT to the continuous algebra | contact action | closed algebraically by conditioned `X` conjugation |
| transport the Gaussian law and extractor | covariance | closed for every displayed `lambda` member |
| select raw second moment over the isotropic family | physical selector | open; contact covariance preserves the entire family |
| preserve one fixed-effect grade across program-dependent conditions | preparation/effect quotient | fails on the biased exact fixtures if the conditions are identified |
| preserve the grade under simultaneous state/effect transport | operational covariance | closed, but the transported effects differ |
| prepare the displayed spectrum from a common blank | state preparation | closed only after supplying a control weight and erasure/reduction interface |
| encode direction, basis, effect menu, and equivalence physically | program registration | open |
| cause contact, control mixing, and Records | occurrence | open |

The theorem is not circular: the CNOT action is first treated as an algebraic
map on arbitrary matrices. Physical channel language is used only after a
density operator or control state is explicitly supplied. The density
extractor is never smuggled in as an input to a proof that purports to select
it.

## Current Objects And Type Boundary

The canonical source
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) declares the
one-site possibility domain to be `M_2(C)` and supplies a probability measure
on that entire domain. It does not identify each possibility with a quantum
density operator.

Let

`D_2={rho in M_2(C):rho=rho^dagger, rho>=0, Tr(rho)=1}`.

Hermitian `2x2` matrices have four real coordinates. The trace-one condition
removes one, and positivity selects a full-dimensional convex body within that
three-dimensional affine space. Thus `D_2` has real dimension three, while
`M_2(C)` has real dimension eight. It has eight-dimensional Lebesgue measure
zero. The Block 3/4 Gaussian `mu_C` has a strictly positive Lebesgue density,
so

`mu_C(D_2)=0`.

This rejects only the direct sample-as-density-operator identification. A raw
matrix may still be an amplitude, operation, code word, or input to a derived
functional if a physical law supplies that typing.

## Theorem 1 — Conditioned CNOT Extends As Conjugation

For a basis-state neighbor control `n in {0,1}`, incoming CNOT acts on a typed
target density operator as

`rho -> T_n(rho)=X^n rho X^n`.

The same expression is algebraically defined for every raw content matrix:

`T_n(A)=X^n A X^n`.

It is an involutive `M_2(C)` algebra automorphism. For the explicit Gaussian
law

`d mu_C(A)=pi^(-4) exp(-||A-C||_HS^2)d^8A`,

Frobenius invariance and the unit Jacobian give

`T_n#mu_C=mu_(X^n C X^n)`.

This is the continuous algebraic shadow of the basis law `y=x XOR n`. It does
not by itself say that `A` is a state, that CNOT occurs, or that a target basis
is physically registered.

## Theorem 2 — Every Displayed Extractor Survives Contact Covariance

For a probability law `mu` with finite nonzero matrix second moment, define

`M_mu=integral A A^dagger dmu(A)`

and, where the denominator is nonzero,

`rho_mu^(lambda)=(M_mu+lambda I)/Tr(M_mu+lambda I)`, `lambda>=0`.

For `T_n#mu`, direct substitution gives

`M_(T_n#mu)=X^n M_mu X^n`.

Because the trace and identity are invariant,

`rho_(T_n#mu)^(lambda)=X^n rho_mu^(lambda) X^n`.

Thus contact covariance preserves the entire isotropic family. It supplies no
equation that distinguishes `lambda=0` from `lambda=1`, or any other member.
This is nonselection inside one displayed family, not a theorem about every
possible local dynamics.

There is also a spectrum boundary. With a fixed pure basis control, `T_n` is
unitary conjugation and preserves the target eigenvalues. At the Gaussian blank
`C=0`, every displayed member is `I/2`, with determinant `1/4`. At `C=P_z`, the
raw member is `diag(3/5,2/5)`, with determinant `6/25`. No conditioned unitary
conjugation of one common blank can make those spectra differ. A mixed or
discarded control can do so, but then its mixing law and reduction become
load-bearing inputs.

## Theorem 3 — Fixed Effect And Transported Effect Separate

At `C=P_z`, Block 4 gives

`rho_0^(lambda)=diag(lambda+3,lambda+2)/(2lambda+5)`.

For control `n=1`, the target state is

`rho_1^(lambda)=X rho_0^(lambda) X`.

Hold the exact same effect fixed:

`E_0=(1/2)P_z`.

Then

`w_0^(lambda)=Tr(rho_0^(lambda)E_0)=(lambda+3)/(2(2lambda+5))`,

`w_1^(lambda)=Tr(rho_1^(lambda)E_0)=(lambda+2)/(2(2lambda+5))`,

and

`w_0^(lambda)-w_1^(lambda)=1/(2(2lambda+5))>0`.

The exact fixtures are

`lambda=0: (w_0,w_1)=(3/10,1/5)`,

`lambda=1: (w_0,w_1)=(2/7,3/14)`.

Consequently, if the two complete neighbor conditions are declared to be one
physical preparation while `E_0` is the same registered effect, the declared
CNOT contact violates descent for every finite `lambda` in this family. That
does not prove the conditions should be identified: an incoming CNOT is a
physical intervention and may change the preparation.

Now transport the effect with the program:

`E_n=X^n E_0 X^n`.

Cyclicity gives

`Tr(rho_n^(lambda)E_n)=Tr(rho_0^(lambda)E_0)`.

This exact covariance compares transported pairs. Since `E_1=(1/2)P_(-z)` is
not `E_0`, it is not the same-effect quotient. The physical program/effect map
must say which comparison is intended.

## Theorem 4 — Random-Control Preparation Is An Exact Escape

Start the target in `|0><0|`. Supply a control whose classical one-weight is
`q`, or a coherent control `sqrt(1-q)|0>+sqrt(q)|1>` followed by control
restriction. Incoming CNOT yields the reduced target

`rho_target(q)=(1-q)P_z+q P_(-z)=diag(1-q,q)`.

Therefore

`q_0=2/5`

prepares `diag(3/5,2/5)`, and

`q_1=3/7`

prepares `diag(4/7,3/7)`.

The CNOT exactly carries whichever spectrum the control supplies. It does not
select the control weight: every `q in [0,1]` is accepted. For a general center
one must additionally supply or derive the eigenbasis rotation of `rho_C`.

The basis XOR marginal makes the same point from the opposite orientation. If
the target input has one-weight `p`, then

`P(Y=1|n=0)=p`, `P(Y=1|n=1)=1-p`,

with response gap `|1-2p|`. Fixed target input gives maximal dependence and
point outputs. Uniform `p=1/2` supplies half-half splitting but erases neighbor
dependence exactly, as PR #6069 reports on its finite family. Nontrivial
mixing plus nonzero dependence is possible for other `p`, but its value remains
supplied.

## Refined Axiom-Side Residual

The one-edge contact test orders the interfaces rather than adding a new wall.
A CNOT or other instrument acts after state/control typing. It can implement a
selected compiler but cannot, by covariance alone, select the density
functional or the control law it consumes.

A narrower sufficient interface is:

> For each physical preparation condition, the local law derives a positive
> normalized density functional of the Admissibility measure, or derives an
> equivalent control mixture and eigenbasis from that measure. Registered
> contact programs act on that typed object and carry registered operational
> effects. A preparation equivalence specifies which program-dependent full
> conditions must share the same density functional and which are physical
> interventions that transport it. The same law supplies any splitting or
> restriction resource used by the program and causes the corresponding
> Record.

Choosing the raw second moment, the centered trace-CDF uniformizer, and the
spectral control factorization realizes this wording mathematically on the
Gaussian option. The wording remains a hypothetical consequence map, not an
adopted axiom update, recommendation, minimality theorem, or necessity claim.

The remaining exact tasks are:

- derive the density functional or control weight/eigenbasis from local law;
- encode the continuous program and effect resolution in physical content;
- define preparation equivalence across apparatus-dependent conditions;
- derive control restriction, atom splitting, and Record occurrence;
- connect one-shot kernels to repeated trials, realized history, time, and
  frequencies.

## Relation To Prior Results

The parent
[`Gaussian compiler source`](ADMISSIBILITY_GAUSSIAN_SECOND_MOMENT_QUANTILE_DECODER_EFFECT_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-10.md),
lines 122--329, supplies the explicit extractor family, quantile compiler, and
physical selection/preparation residual. This note tests one local contact
mechanism against that exact residual.

The tracked
[`Record instrument interface`](RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md),
lines 28--64 and 100--108, begins with a supplied density operator and supplied
instrument. It correctly derives kernels after those inputs; it does not
reverse the type order or select them.

The finite
[`preterminal process source`](work_history/repo/review_feedback/PRETERMINAL_CONTEXT_QUANTUM_PROCESS_CYCLE189_NOTE_2026-07-16.md),
lines 88--99 and 505--527, reconstructs a density operator from complete records
and a fixed process, but explicitly imports preparation, intervention, Born
pairing, and process category. It is a live record-derived route, not a current-
axiom selection theorem.

PR [#6069](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/6069)
is non-load-bearing prior-art context. Its branch theorem exhausts the declared
20-word basis family and reports six covariant incoming-CNOT/XOR witnesses,
while explicitly leaving the continuous `M_2(C)` law open. All load-bearing
CNOT and continuous calculations are rederived here.

## No-Go Discipline Gate

The negative claim is only that the displayed direct-sample and conditioned-
CNOT covariance route does not select the physical Gaussian compiler. No
global unitary or contact no-go is claimed.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| direct sample typing | identify raw `A in M_2(C)` with a density operator | the Gaussian density-operator subset has measure zero (type proof above) | **ATTEMPTED** |
| conditioned CNOT conjugation | extend the basis contact to arbitrary target operators | exact `X` conjugation and Gaussian pushforward succeed, but every `lambda` survives (Theorems 1--2) | **ATTEMPTED** |
| fixed-effect equality | demand one `E_0` grade across the two control conditions | excludes every finite displayed biased member rather than selecting the raw one (Theorem 3) | **ATTEMPTED** |
| transported-effect covariance | co-transport `rho` and `E` with the program | succeeds for every `lambda`, but compares different effects (Theorem 3) | **ATTEMPTED** |
| random/coherent control preparation | prepare the target spectrum through CNOT and control restriction | succeeds for any supplied `q`, including `2/5` and `3/7`; does not select `q` (Theorem 4) | **ATTEMPTED** |
| direct quantile comparator | decode the Gaussian uniformizer without a target density carrier | the [parent construction](ADMISSIBILITY_GAUSSIAN_SECOND_MOMENT_QUANTILE_DECODER_EFFECT_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-10.md) succeeds mathematically; physical comparator/program occurrence remains open | **ATTEMPTED** |
| supplied finite instrument | use a Kraus/pointer law after state preparation | the [instrument interface](RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md) normalizes conditionally but starts from supplied `rho` and `{K_r}` | **ATTEMPTED** |
| record-derived process | reconstruct the density calculator from complete process records | the [Cycle 189 process](work_history/repo/review_feedback/PRETERMINAL_CONTEXT_QUANTUM_PROCESS_CYCLE189_NOTE_2026-07-16.md) succeeds finitely but imports preparation, intervention, Born pairing, and process category | **ATTEMPTED** |
| raw-moment calibration | require the unnormalized functional to satisfy `F(delta_A)=AA^dagger` and mixture linearity | would select `M_mu`, but the calibration is a new physical typing condition, not a current consequence | **ATTEMPTED** |

The routes include positive escapes. The bounded negative is retained only for
selection by the declared contact/covariance structure alone.

### N2 — wall independence and collapse

The direct-sample type issue collapses into density-functional selection, and
random-control weighting collapses into selection plus splitting. The same
three walls from Block 4 remain.

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| density-functional/control selection / splitting resource | no: choosing the target weight does not realize it on atomic content | no: a randomizer does not choose its bias or eigenbasis | independent |
| density-functional/control selection / preparation-program quotient | no: a density functional does not identify physical apparatus conditions | no: a quotient does not choose the functional | independent |
| splitting resource / preparation-program quotient | no: a splittable control does not register effects or preparation identity | no: a program quotient need not supply randomness | independent |

Contact is an implementation layer downstream of all three and is not counted
as a fourth independent wall.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| full-support Gaussian | explicit constructed completion from the stacked parent; not selected by current axioms |
| density-operator set dimension | elementary finite-dimensional geometry proved here |
| Pauli `X` and CNOT basis | supplied program convention for the tested route; not a preferred current-axiom basis |
| density operator as CNOT input | used only in the conditional typed-channel branch; never inferred from raw content |
| control basis state | explicit finite-contact premise |
| random or coherent control weight `q` | explicit escape-route input; selection remains open |
| control restriction / partial trace | textbook finite-system operation; physical realization remains open |
| fixed versus transported effect | both comparisons stated separately; no operational equivalence imported |
| finite second moment | proved for the Gaussian parent, not assumed globally |
| Record occurrence and history | absent and explicitly open |

No density operator, Born target, observed probability, preferred program,
control mixture, branch actuality, IID ensemble, or frequency law is smuggled
in as a current premise.

### N4 — source residual matching

| Source location | Source residual used | Residual attacked here | Closure claimed here | Match |
|---|---|---|---|---:|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), lines 45--73 and 79--84 | raw `M_2(C)` possibility measure and content-only Record readout | type raw content before applying CNOT/channel semantics | direct sample route rejected only on the displayed Gaussian law | yes |
| [`Gaussian compiler source`](ADMISSIBILITY_GAUSSIAN_SECOND_MOMENT_QUANTILE_DECODER_EFFECT_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-10.md), lines 122--163 and 263--329 | extractor exists mathematically; selection and cross-condition preparation quotient remain open | test conditioned CNOT against selection and quotient | exact one-edge equivariance/fixed-effect boundary only | yes |
| [`Record instrument interface`](RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md), lines 28--64 and 100--108 | instrument kernels start after supplied `rho` and `{K_r}` | audit contact/state type order | no reverse derivation borrowed | yes |
| [`Cycle 189 process source`](work_history/repo/review_feedback/PRETERMINAL_CONTEXT_QUANTUM_PROCESS_CYCLE189_NOTE_2026-07-16.md), lines 88--99 and 505--527 | density calculator reconstructs after supplied finite process fields | keep record-derived process route live | no current-axiom process closure borrowed | yes |

PR #6069 is a live external collision/provenance check rather than a
load-bearing citation. Its continuous-boundary statement is re-established by
the calculations here.

### N5 — resolution and rhetoric audit

| Statement | Per element | Per site | Per mode | Per block | Lattice-wide |
|---|---|---|---|---|---|
| raw Gaussian content is not already a density operator | all eight real coordinates versus the three-dimensional density body | one `M_2(C)` target | full-support Gaussian measure | displayed completion only | not executed; global law selection absent |
| conditioned CNOT does not select `lambda` | exact `X` conjugation of every matrix entry | one target/control edge | four exact finite `lambda` fixtures plus analytic all-`lambda` proof | displayed isotropic family | not executed; covariant direction orbit is prior-art context only |
| fixed-effect descent fails | exact half-`P_z` grade | one `C=P_z` target under two controls | `lambda=0,1` fixtures and analytic family gap | one effect/program pair | not claimed when preparation conditions differ |
| random control does not select its weight | exact target diagonal entries | one blank target/control pair | four exact mixture controls | displayed spectral factorization | not executed; no autonomous mixer or occurrence law |

The runner cache emits substantive `per_element`, `per_site`, `per_mode`,
`per_block`, and `lattice_wide` lines.

### N6 — live partial-closure and primitive paths

1. A local dissipative or measurement law could select a unique stationary
   density functional even though conditioned unitary contact does not.
2. The Gaussian trace-CDF could drive a physical comparator directly, avoiding
   an intermediate density carrier.
3. A coherent control plus physical restriction could realize the selected
   spectrum once its amplitude is derived.
4. A record-derived finite process can reconstruct a density calculator after
   preparation and instrument fields are locally generated.
5. A calibration `F(delta_A)=AA^dagger`, zero-content boundary, or other
   physical amplitude typing could select the raw moment.
6. An owner-approved explicit density-functional/control law could adopt one
   of these routes directly.

The primitive-registry scan used
`docs/audit/data/axiom_premise_nodes.json` and the three approved primitive
sources. The scale reference supplies units only, kinetic isotropy supplies a
kinetic-form ratio only, and the realized-state primitive supplies pointwise
evaluation without a density functional, instrument, control law, probability
selector, or program quotient. None closes the interfaces above.

PR #6069 materially improves the finite contact layer: six incoming-CNOT/XOR
witnesses form one covariant spatial law class. Its own boundary leaves the
continuous `M_2(C)` probability law open, and its exact uniform-target
marginal shows why supplied mixing is not selection. PR #6066 changes no
premise, and PR #6068 is unrelated cell-cutting rank science.

### N7 — hostile steelman

> The Gaussian law already provides an exact uniform scalar, and a local
> comparator can threshold it at `q_C`, drive a coherent CNOT control, and
> rotate into the eigenbasis of `rho_C`. The raw moment is the simplest
> zero-fit covariant density functional, so a compact contact circuit may make
> the `lambda` alternatives physically irrelevant without a new axiom.

This steelman is accepted. The theorem does not reject that construction. Its
terminal obligation is to derive the comparator, `q_C`, eigenbasis, restriction,
program registration, and occurrence from one local law rather than supplying
them. That is the next exact target.

### N8 — cross-cycle echo

| Earlier surface | Later movement | Echo here |
|---|---|---|
| raw possibility/effect identification failed in Block 2 | Block 3 replaced points by decoder fibers | direct sample/state typing now fails for the same whole-domain reason |
| Block 3 found decoder nonselection | Block 4 constructed one exact Gaussian compiler | CNOT transports the constructed compiler but preserves its extractor freedom |
| Cycle 189 reconstructed a density calculator from records | its process fields remained supplied | record reconstruction remains a positive alternative after local process derivation |
| Cycle 321 closed a finite coarse-CP quotient | general physical effect equality remained open | fixed versus transported effects now separate the exact one-edge quotient choices |
| PR #6069 closes finite CNOT covariance | continuous `M_2(C)` remains explicitly open | the algebraic extension closes covariance but not typing or selector choice |

**Gate disposition:** PASS for the Gaussian density-set type boundary,
conditioned-CNOT extractor equivariance, fixed-versus-transported effect split,
and supplied-control preparation factorization. FAIL / DO NOT SHIP for a global
unitary/contact no-go, physical compiler selection, axiom necessity,
preparation equivalence, occurrence, or Born/history closure.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current `M_2(C)` possibility measure and Record wording | semantic baseline | supplied; unchanged |
| explicit Gaussian law and isotropic extractor family | tested compiler family | inherited from stacked parent; not physically selected |
| Pauli `X` and conditioned CNOT conjugation | one-edge contact model | elementary finite quantum algebra rederived here |
| density-operator subset geometry | raw-content type test | elementary dimension/measure argument |
| fixed `E_0=(1/2)P_z` | quotient probe | exact parent fixture; mathematical effect only |
| random/coherent control and restriction | positive preparation escape | conditional operation; weight, blank, and occurrence not derived |
| PR #6069 | prior-art/collision context | external live PR; not a declared runner input |
| canonical axiom edit | governance action | forbidden absent owner authority; not performed |

The exact advance is a type-ordered factorization of what the finite contact
can and cannot do. It does not move the fixed TOE percentages: physical
selection, program/preparation registration, and autonomous occurrence remain
open current-axiom obligations.

## Review Record

This source is stacked on PR #6070 because it consumes the explicit Gaussian
compiler and its exact physical-selection residual. PR #6069 is checked as
adjacent prior art but no branch-local artifact is imported. The canonical
axiom memo remains unchanged. Independent audit is required before any
effective status changes. No `review-loop` was invoked in producing or
directly self-reviewing this artifact.
