---
claim_id: scaled_effect_is_not_a_projector_axioms_pick_neither_instrument_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "At one M_2(C) site, the August 10 shared effect E0=(1/2)P with P=diag(1,0) fails to be a projector, and the Born traces of P and E0 against rho=diag(3/5,2/5) disagree. Admissibility and Record name a distribution over possibilities and the lock of one possibility; neither sentence names P versus cP. A later Born compiler must still declare the scale of each effect. The two binary menus {P,I-P} and {E0,I-E0} are displayed; neither is adopted. August 9 and August 10 are not replaced, and r=1/2 is not forced."
upstream_dependencies:
  - minimal_axioms
  - admissibility_global_measure_menu_kernel_type_separation_bounded_theorem_note_2026-08-10
runner: scripts/scaled_effect_is_not_a_projector_axioms_pick_neither_instrument_2026_08_13.py
---

# A Scaled Effect `cP` Is Not A Projector; Axioms Pick Neither Instrument

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact one-site algebra on the pair `P` versus `(1/2)P`; instrument
selection only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/scaled_effect_is_not_a_projector_axioms_pick_neither_instrument_2026_08_13.py`](../scripts/scaled_effect_is_not_a_projector_axioms_pick_neither_instrument_2026_08_13.py)

## Result Up Front

The August 10 shared effect `E_0=(1/2)P` is a scaled rank-one matrix, not a
projector. Against a single density `rho=diag(3/5,2/5)` the two candidate first
outcomes disagree: `Tr(rho P)=3/5` and `Tr(rho E_0)=3/10`.

Admissibility names a nearest-neighbor-determined distribution over
possibilities. Record names the lock of one admissible possibility. Neither
sentence names `P` versus `cP`. A later Born compiler that evaluates effects
must still declare the scale of each effect. This note displays the two binary
menus `{P,I-P}` and `{E_0,I-E_0}` and does not adopt either.

The result does not replace the August 9 frame-lift theorem or the August 10
type-separation theorem. It does not force `r=1/2`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The projector identity, the exact Born-trace split 3/5 versus 3/10, and the axiom-text reading that neither sentence names P versus cP are proved on declared one-site matrices. Menu adoption, a later scale-declaring compiler, replacement of August 9/10, and a forced r=1/2 remain outside the claim."
trace_class: negative_route_pruning
target_claim_id: scaled_effect_versus_projector_instrument_selection
target_blocker_text: "declare the scale of each effect; axioms name neither P nor cP as the instrument"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for P versus E0=(1/2)P on the displayed density; later compilers remain open"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work at one site with `H=C^2`. Fix the rank-one diagonal projector

`P=diag(1,0)`

and the August 10 object

`E_0=(1/2)P=diag(1/2,0)`.

The complementary matrices are

`I-P=diag(0,1)`, `I-E_0=diag(1/2,1)`.

The displayed density is

`rho=diag(3/5,2/5)`.

A matrix `E` is a projector when `E^2=E`. The Born evaluation used below is
the ordinary trace pairing

`Tr(rho E)`.

Two binary resolutions of the identity are displayed, not adopted:

`M_P={P,I-P}`, `M_{E_0}={E_0,I-E_0}`.

The first is a projective menu. The second is a two-outcome effect menu whose
first member is the scaled matrix `E_0`. The complement `I-E_0` is a valid
effect (`0 <= I-E_0 <= I`) but is not itself a rank-one scaled projector.

This block is `P` versus `(1/2)P`. It is not a comparison of two distinct
projective bases, and it does not assume a Lüders update.

## Exact Target And Obligation Graph

**Exact target.** Decide whether `E_0` is already a projector, whether the two
first-outcome evaluations agree on the displayed density, and whether the
current Admissibility and Record sentences already name `P` versus `cP`.

| Obligation | Role | Disposition |
|---|---|---|
| test the projector identity on `P` and on `E_0` | type split | [Theorem 1](#theorem-1--e0-is-not-a-projector) |
| evaluate both first outcomes on `rho` | numerical split | [Theorem 2](#theorem-2--the-two-instruments-disagree) |
| quote Admissibility and Record | axiom reading | [Theorem 3](#theorem-3--admissibility-and-record-name-neither-p-nor-cp) |
| display both menus and refuse adoption | claim boundary | [Theorem 4](#theorem-4--a-later-compiler-must-declare-scale-display-both-adopt-neither) |
| refuse replacement of August 9/10 and refuse `r=1/2` | claim boundary | [Theorem 5](#theorem-5--august-910-are-not-replaced-r12-is-not-forced) |

The fixed matrices are load-bearing witnesses. A different scale `c`, a
different density, or a later physical compiler is outside Theorems 1--2.

## Theorem 1 — `E_0` Is Not A Projector

Direct matrix multiplication gives

`P^2=diag(1,0)=P`

and

`E_0^2=diag(1/4,0)`.

The right-hand side is not `E_0`, because `1/4 != 1/2`. Therefore `E_0` is
not a projector. A predicate "`E_0` is a projector" fails.

The same identity confirms that `P` itself is a projector. Scaling a projector
by `1/2` leaves the August 10 object, which is an effect and not a projection.

## Theorem 2 — The Two Instruments Disagree

The trace pairing on the displayed density is

`Tr(rho P)=3/5`, `Tr(rho E_0)=3/10`.

These fractions are unequal. The two first-outcome instruments therefore
disagree at this `rho`. A predicate `Tr(rho P)=Tr(rho E_0)` fails because
`3/5 != 3/10`.

The complementary evaluations are `Tr(rho(I-P))=2/5` and
`Tr(rho(I-E_0))=7/10`. Each displayed pair sums to `1`, so the disagreement
is a genuine split of one and the same probability, not a normalization
error.

## Theorem 3 — Admissibility And Record Name Neither `P` Nor `cP`

The current Admissibility axiom states that, for each site, the probability
distribution over the possibilities is determined by, and varies with, the
nearest-neighbor conditions.

The current Record axiom states that, when present, a record locks exactly
one admissible local possibility.

The first sentence names a distribution over possibilities. The second
sentence names the lock of one possibility. Neither sentence names `P` versus `cP`.
Neither sentence names the menus `{P,I-P}` or `{E_0,I-E_0}`,
the scale of an effect, or the trace pairing of Theorem 2.

The axiom memo also records that context selection, measurement basis
selection, Born weight values, probability rules beyond the distribution
clause, and update laws remain outside axiom content.

## Theorem 4 — A Later Compiler Must Declare Scale; Display Both; Adopt Neither

A later Born compiler that consumes effects must still declare the scale of
each effect. The pair `P` and `E_0=(1/2)P` is the exact witness: they share a
support ray and they are not interchangeable as first outcomes.

This note displays

`{P,I-P}` and `{E_0,I-E_0}`

and does not adopt either. Neither menu is installed as a physical instrument.
Neither is named `L_phys`.

### N5 — resolution and rhetoric audit (Theorem 4)

Theorem 4 is a display-and-boundary statement, not a selection of an
instrument.

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | the two displayed first outcomes `P` and `E_0`, with exact squares and traces | no classification of every effect or every POVM |
| per site | one `M_2(C)` site and one displayed density | no composite, multi-site, or formation-site theorem |
| per mode | the rank-one ray of `P` and its scale `c=1/2` | no spectral-mode or harmonic exhaustion |
| per block | scale declaration and non-adoption of either binary menu | no adoption of `L_phys`, no forced `r=1/2`, no Lüders map |
| lattice-wide | not executed | no lattice-wide dynamics, gravity, or measurement-process claim |

Rhetoric that "the axioms pick the projector menu," "the axioms pick the
scaled menu," or "the two first outcomes are the same instrument" is outside
this resolution.

## Theorem 5 — August 9/10 Are Not Replaced; `r=1/2` Is Not Forced

Nothing above claims that the August 9 binary/ternary frame-lift theorem or
the August 10 global-measure / menu-kernel type-separation theorem is
replaced, improved, or withdrawn. The August 10 parent remains the source of
the shared object `E_0=(1/2)P(z)`. The present block only compares that
object with the unscaled projector `P` as two candidate first outcomes.

The note does not force `r=1/2`. No ratio dictionary is introduced. A later
selector of scale, or a later physical compiler, is not ruled out.

## No-Go Discipline Gate

The negative claims are restricted to: (i) `E_0` is not a projector, (ii) the
two first-outcome traces disagree, (iii) Admissibility and Record do not name
`P` versus `cP`, and (iv) neither displayed menu is adopted and `r=1/2` is
not forced. The gate does not certify that no later compiler can declare a
scale.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Treat `E_0` as a projector | demand `E_0^2=E_0` | [Theorem 1](#theorem-1--e0-is-not-a-projector): `E_0^2=diag(1/4,0)` | **ATTEMPTED** |
| Identify the two first outcomes | demand `Tr(rho P)=Tr(rho E_0)` | [Theorem 2](#theorem-2--the-two-instruments-disagree): `3/5 != 3/10` | **ATTEMPTED** |
| Read scale off Admissibility | treat "distribution over possibilities" as naming `P` or `cP` | [Theorem 3](#theorem-3--admissibility-and-record-name-neither-p-nor-cp): the sentence names neither | **ATTEMPTED** |
| Read scale off Record | treat "locks one possibility" as selecting a projector menu | Theorem 3: lock is not an effect scale | **ATTEMPTED** |
| Adopt a displayed menu | install `{P,I-P}` or `{E_0,I-E_0}` as `L_phys` | [Theorem 4](#theorem-4--a-later-compiler-must-declare-scale-display-both-adopt-neither) refuses adoption | **ATTEMPTED** |
| Force `r=1/2` | take the scale `1/2` as a universal dictionary | [Theorem 5](#theorem-5--august-910-are-not-replaced-r12-is-not-forced) refuses the force | **ATTEMPTED** |
| Replace August 9/10 | treat this split as a successor theorem | Theorem 5: those standing results are not replaced | **ATTEMPTED** |
| Later scale-declaring compiler | derive a physical rule that names `c` for each effect | Theorem 4 keeps the obligation live; Theorem 5 does not exhaust it | **LIVE** |

The broad statement "the axioms can never supply an instrument" is not
shipped.

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| projector identity / Born-trace split | no: a non-projector can still share a trace with `P` on some states | no: unequal traces do not compute `E_0^2` | independent |
| Born-trace split / axiom-text reading | no: `3/5 != 3/10` does not quote Admissibility or Record | no: unnamed menus do not evaluate traces | independent |
| axiom-text reading / non-adoption | no: "not named now" is not "unlistable later" | no: refusing adoption does not quote the axiom sentences | independent |
| non-adoption / August 9/10 non-replacement | no: displaying two menus does not touch those theorems | no: leaving August 9/10 in place does not adopt a menu | independent |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `P=diag(1,0)` | declared rank-one projector; not axiom content |
| `E_0=(1/2)P` | August 10 shared-effect object, reused here as a scale witness |
| `rho=diag(3/5,2/5)` | declared one-site density; not derived and not adopted |
| `{P,I-P}`, `{E_0,I-E_0}` | displayed binary resolutions; not adopted instruments |
| `L_phys` | unused adoption slot; neither menu is placed in it |
| `r=1/2` | not introduced and not forced |
| Lüders update | not used |
| observations or fitted frequencies | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Admissibility distribution sentence; Record lock of one admissible possibility; Born weights and update laws outside axiom content | exact current wording; no instrument is borrowed |
| [`docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md`](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md) | the shared object `E_0=(1/2)P(z)` | object identity only; the August 10 type-separation theorems are not reused as premises and are not replaced |

No other scientific parent is used. The identities `P^2=P`,
`E_0^2=diag(1/4,0)`, `Tr(rho P)=3/5`, and `Tr(rho E_0)=3/10` are proved here
and checked by the runner.

### N6 — live partial-closure paths

1. A later physical compiler could declare a scale `c` for each registered
   effect and then evaluate the trace pairing on that declared effect.
2. A later derivation could restrict eligible menus to projective resolutions
   and thereby exclude `E_0` as a first outcome.
3. A later derivation could keep the full scaled domain and treat `c` as part
   of the registered effect, as the August 10 kernel interface already types.
4. An approved primitive could name one of the displayed menus. None is
   adopted here.

None of these paths is closed here. None is claimed exhausted.

### N7 — hostile steelman

> Once a rank-one ray is fixed, the only idempotent on that ray is `P`, so
> the axioms already pick the projector. The matrix `E_0` is just a rescaled
> label for the same outcome. Displaying `{E_0,I-E_0}` is bookkeeping, not a
> second instrument.

This steelman is accepted as a *program*, not as a present theorem. Theorem 1
agrees that only `P` is idempotent. Theorem 2 shows that the rescaled label
is not bookkeeping: the Born numbers differ. If a later argument derives that
only idempotents are eligible first outcomes, that argument is the selector.
It is not supplied by the current Admissibility or Record sentences.

### N8 — cross-cycle echo

| Earlier surface | Later movement | Echo here |
|---|---|---|
| August 10 used `E_0=(1/2)P(z)` as a shared ternary effect | that object remains live and is not a projector | Theorem 1 records the projector failure on the same matrix |
| August 10 separated a global measure from a menu kernel | the kernel still consumes a declared effect | Theorem 4 repeats that the scale must be declared |
| August 9 forced a unique trace form after a grade is supplied | the grade still needs an effect, not a bare ray | this note does not replace that implication |

**Gate disposition:** PASS for (i) `E_0` is not a projector, (ii) the two
first-outcome traces disagree, (iii) Admissibility and Record do not name
`P` versus `cP`, and (iv) both menus are displayed and neither is adopted.
FAIL / DO NOT SHIP for "an axiom update is necessary," "August 9/10 are
replaced," "the axioms force `r=1/2`," "either displayed menu is the
physical instrument," or "no later compiler can declare a scale."

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current four axiom sentences | semantic baseline | supplied; no edit |
| August 10 shared effect `E_0` | object identity | reused; theorems not replaced |
| `P`, `rho`, both binary menus | witnesses | constructed here; not adopted |
| later scale-declaring compiler | possible extra structure | open |
| `L_phys` | unused adoption slot | not adopted |
| `r=1/2` | unused dictionary | not introduced and not forced |
| August 9 frame-lift theorem | standing neighbor | not replaced and not a premise |
| observations or fits | none | not used |

## Review Record

The scientific parents are the current axiom memo and the August 10
type-separation note, used only for the shared object `E_0` and the standing
claim that a menu kernel consumes a declared effect. Independent audit
remains required before any effective status may change.
