---
claim_id: parallel_step_incoming_lock_formation_b3_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Parallel-step incoming-lock formation-tick reverse and face at k=1 on B_3(0) with seed lock +e_1 are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/parallel_step_incoming_lock_formation_b3_2026_08_15.py
---

# Parallel-Step Incoming-Lock Formation On B_3(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact formation-tick report for the displayed parallel-step
incoming-lock process on the finite host `B_3(0)` with seed lock `+e_1`.
Reverse and face are displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/parallel_step_incoming_lock_formation_b3_2026_08_15.py`](../scripts/parallel_step_incoming_lock_formation_b3_2026_08_15.py)

Do not attach L1. Do not write into Admissibility. Uniqueness is not required.

## Result Up Front

On the cubic lattice, let `B_3(0)` be the nearest-neighbor graph ball of
radius `3` about the origin: the finite set of sites `x` with
`|x_1|+|x_2|+|x_3| ≤ 3`. The lock alphabet is the six unit steps
`{±e_1, ±e_2, ±e_3}`. Seed: the origin is recorded at tick `0` with lock
letter `+e_1`.

From a recorded site `p` with lock `L(p)=±e_i`, a 6-NN step `s` to `q=p+s`
is allowed iff `s` is parallel to the current lock, that is `s=±e_i`
(equivalently `s · e_i ≠ 0` and `s` is a unit NN step). If `q` lies in
`B_3(0)`, is unformed, and the step is allowed, then `q` forms at `t(p)+1`
and locks `s`. This is a displayed construction. It is not a Record-rate
law and is not an Admissibility edit.

The process fills only the seed-lock axis. Off-axis sites in `B_3(0)` remain
unformed. Consequently the reverse and face predicates, which compare
on-axis ticks to off-axis ticks, are undefined. That is the load-bearing
content of the parallel constraint: without perpendicular allowed steps,
those displays have no second operand.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Admissibility
does not supply the formation site, probability, or rate.

The current Record boundary is:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

The incoming-lock letter in this note is a displayed step tag on a forming
site. It is not identified with a physical local possibility in `M_2(C)`,
and it does not enlarge Record.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite B_3(0) enumeration of a displayed parallel-step incoming-lock process, with reverse and face reported as undefined."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed, not adopted. Do not attach L1. Do not write into Admissibility."
conditional_surface_status: "exact on B_3(0) for the declared seed and parallel-step rule"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `0=(0,0,0)`, `e_1=(1,0,0)`, `e_2=(0,1,0)`, `e_3=(0,0,1)`. The open
six-neighbor set is `N(x)={x±e_1,x±e_2,x±e_3}`. The host is

`B_3(0)={x in Z^3 : |x_1|+|x_2|+|x_3| ≤ 3}`.

Seed: `t(0)=0` and `L(0)=+e_1`.

Allowed-step rule, from recorded `p` with `L(p)=±e_i`: a unit NN step `s`
is allowed iff `s` is parallel to the current lock, i.e. `s=±e_i`. If
`q=p+s` is in `B_3(0)` and unformed, then `q` forms at `t(p)+1` and the
incoming lock is `L(q)=s`. First write wins if several parents could name
the same child. Uniqueness is not required.

Probes: `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`. All four lie in
`B_3(0)`. The symbol `t` means formation tick when defined.

The tick-1 6-mask of the origin is the six-tuple of indicators, in the order
`+e_1,-e_1,+e_2,-e_2,+e_3,-e_3`, that the corresponding neighbor forms at
tick `1`.

Reverse predicate: `3 t(A)^2 > t(B)^2`. Face predicate:
`t(C)^2 > 2 t(D)^2`. Each is `hold`, `fail`, or `undefined`. A missing
operand makes the predicate undefined. Displayed, not adopted.

## Theorem 1 — Tick-1 6-Mask And Probe Ticks

From the origin, the only allowed steps are `±e_1`. Both land in `B_3(0)`
and are unformed. Therefore the tick-1 6-mask is

`(1,1,0,0,0,0)`.

The two formed neighbors are `A=(1,0,0)` with incoming lock `+e_1` and
`(-1,0,0)` with incoming lock `-e_1`. So `t(A)=1`.

Every later allowed step remains parallel to `e_1`. By induction the formed
set is exactly the axial segment `{(n,0,0) : |n| ≤ 3}`, with `t(n,0,0)=|n|`
and incoming lock `sign(n) e_1` for `n ≠ 0`. In particular `t(C)=t(2,0,0)=2`.

`B=(1,1,1)` and `D=(1,1,0)` are in `B_3(0)` but not on that axis, so they
never form: `t(B)` and `t(D)` are undefined.

## Theorem 2 — Reverse Display

The reverse predicate is `3 t(A)^2 > t(B)^2`. Here `t(A)=1` is defined and
`t(B)` is undefined, so reverse is undefined. Displayed, not adopted.

## Theorem 3 — Face Display

The face predicate is `t(C)^2 > 2 t(D)^2`. Here `t(C)=2` is defined and
`t(D)` is undefined, so face is undefined. Displayed, not adopted.

These two undefined reports are the dual of a perpendicular-step process:
if off-axis steps were allowed, `B` and `D` could receive ticks and the
predicates would become boolean. The parallel constraint is therefore
load-bearing for reverse and face at this seed. The predicates are not
attached as L1 and are not written into Admissibility.

## Closed Form On The Host

The finite history is:

| site | `t` | incoming lock |
|---|---|---|
| `(0,0,0)` | `0` | `+e_1` (seed) |
| `(n,0,0)`, `n=1,2,3` | `n` | `+e_1` |
| `(n,0,0)`, `n=-1,-2,-3` | `|n|` | `-e_1` |
| every other site of `B_3(0)` | undefined | unformed |

No two parents write the same child on this seed. That observation is
incidental: uniqueness is not required.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It reports the dual of a perpendicular-step display: allowed steps parallel to the current lock, and whether reverse/face are defined. |
| V2 | Current main has no landed parallel-step incoming-lock formation-tick report on `B_3(0)` with this seed. |
| V3 | The host is finite. The allowed-step rule and the four probes are exact. |
| V4 | The report is more than a restatement of Admissibility because Admissibility does not supply a formation process. |
| V5 | Reverse and face remain displayed, not adopted. No physical compiler is claimed. |

## No-Go Discipline Gate

The negative content is narrow: parallel-to-lock allowed steps do not form
the off-axis probes, so reverse and face are undefined on this seed. No
global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| parallel-step incoming lock | allow only `s=±e_i` from lock `±e_i` | executed; reverse and face undefined |
| perpendicular-step dual | allow only `s · e_i = 0` | different displayed process; not executed here |
| unrestricted 6-NN growth | ignore the lock axis | different process; would fill `B_3(0)` by graph radius |
| same-sign only | allow `s=L(p)` but not `-L(p)` | still leaves `B` and `D` unformed; not the declared rule |
| unbounded host | drop the `B_3(0)` cutoff | outside the declared host |
| attach reverse/face | adopt the predicates as a law | refused; displayed, not adopted |

### N2 — wall independence

The missing off-axis ticks, the un-adopted reverse/face predicates, the
lock-to-possibility identification, and a physical formation rate are
distinct residuals. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, the lock alphabet, the seed lock `+e_1`, and the
parallel-to-current-lock rule are declared. Reverse and face are not
assumed to hold. Uniqueness is not assumed. Formation uses only the
declared unit NN steps.

### N4 — source residual matching

The current axiom memo supplies the cubic nearest-neighbor substrate, the
local-law condition sentence, and the Record lock/content/absence boundary
used as host language. It does not supply the displayed step rule. The
residual therefore matches current sources: formation site, probability, and
rate remain outside Admissibility.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | tick-1 6-mask and four named probes | no exhaustive alphabet classification |
| per site | incoming lock is the forming NN step | no `M_2(C)` identification |
| per mode | no mode calculation | no spectral exhaustion |
| per block | reverse and face as hold/fail/undefined | no adopted inequality |
| lattice wide | checked and not executed | no unbounded-host theorem |

### N6 — live partial-closure paths

Live routes are a perpendicular-step dual on the same host, a separately
derived formation law, a lock-to-possibility map, and any later decision to
adopt or reject reverse/face. Those routes are not taken here.

### N7 — hostile steelman

**Steelman:** If reverse and face are the intended k=1 displays, the
parallel-step process should be judged as failing them.

**Answer:** A predicate with a missing operand is undefined, not false. `B`
and `D` never form, so the comparisons are not instantiated. Reporting
`fail` would smuggle an implicit tick at unformed sites. The honest report
is undefined, and that already shows the parallel constraint is
load-bearing.

### N8 — cross-cycle echo

This note does not import a perpendicular-step theorem or an adopted
reverse/face law. It reports one finite displayed process on `B_3(0)`.

**Gate disposition:** PASS for the finite tick-1 6-mask, the four probe
reports, and the undefined reverse/face displays above. FAIL / DO NOT SHIP
for “reverse holds,” “face holds,” “attach L1,” or “Admissibility now
includes this step rule.”

## Primary Runner

The primary runner enumerates `B_3(0)`, executes the parallel-step
incoming-lock rule from the declared seed, prints the tick-1 6-mask, reports
`t(A)`, `t(B)`, `t(C)`, `t(D)`, and evaluates reverse and face as
hold/fail/undefined. It authors no audit verdict.
