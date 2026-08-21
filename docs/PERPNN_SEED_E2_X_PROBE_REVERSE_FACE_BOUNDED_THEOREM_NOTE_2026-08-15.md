---
claim_id: perpnn_seed_e2_x_probe_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Perp-step incoming-lock formation-tick reverse and face at k=1 on B_3(0) with seed lock +e_2 and x-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/perpnn_seed_e2_x_probe_reverse_face_2026_08_15.py
---

# Perp-Step Incoming-Lock Reverse And Face At k=1 With Seed Lock +e_2

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** first-arrival formation ticks on the closed taxicab ball `B_3(0)`
for the declared perp-step incoming-lock process with seed lock `+e_2` and
fixed x-probes. Reverse and face comparisons are reported. Displayed, not
adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/perpnn_seed_e2_x_probe_reverse_face_2026_08_15.py`](../scripts/perpnn_seed_e2_x_probe_reverse_face_2026_08_15.py)

## Result Up Front

Host the closed taxicab ball `B_3(0)={p∈Z^3:|p_1|+|p_2|+|p_3|≤3}`. Lock
letters are the six-neighbor alphabet `{±e_i}`. The origin is recorded at
tick `0` with seed lock `+e_2`. From a recorded site `p` with lock letter
`L(p)=±e_i`, a six-neighbor step `s` to `q=p+s` is allowed if and only if
`s·e_i=0`. If `q` lies in `B_3(0)`, is still unformed, and the step is
allowed, then `q` forms at tick `t(p)+1` and records the incoming letter
`s`. Uniqueness not required: a first-arrival site may admit several
incoming letters.

The k=1 x-probes remain

```text
A=(1,0,0),  B=(1,1,1),  C=(2,0,0),  D=(1,1,0).
```

They are not rotated with the seed. Holding those probes fixed while seeding
`+e_2` is therefore not a cubic relabel of an axis-aligned `+e_1` seed.

Exact first-arrival ticks on this host:

```text
t(A)=1,  t(B)=3,  t(C)=4,  t(D)=2.
```

The tick-1 6-mask of the origin, in the order `+e_1,-e_1,+e_2,-e_2,+e_3,-e_3`,
is `(1,1,0,0,1,1)`. Reverse `3 t(A)^2 > t(B)^2` fails. Face
`t(C)^2 > 2 t(D)^2` holds. Both comparisons are defined. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1.

## Current Premise Boundary

The Lattice and Record sentences used as substrate typing are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

Records form.

When present, a record locks exactly one admissible local possibility.

The perp-step rule, the seed letter `+e_2`, the host `B_3(0)`, and the
tick increment `t(p)+1` are declared process data. They are not derived from
Admissibility, and they do not edit Admissibility. Record supplies locking of
one local possibility when a record is present; it does not supply this
formation schedule, this lock alphabet, or a physical reverse/face law.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "First-arrival ticks on a finite host are exact; reverse and face are displayed comparison values for this seed and these probes, not an adopted law."
trace_class: negative_route_pruning
target_claim_id: reverse_face_k1_physical_adoption
target_blocker_text: "do not adopt reverse or face as Admissibility content from this seed-lock display"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "keep reverse and face as displayed k=1 comparison values; do not attach L1 and do not write them into Admissibility"
conditional_surface_status: "exact for B_3(0), seed lock +e_2, and the declared x-probes; uniqueness of incoming letters is not required"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, `e_3=(0,0,1)`, and `0=(0,0,0)`. The
six-neighbor steps are `{±e_1,±e_2,±e_3}`. Graph distance is the taxicab
metric. The host is only `B_3(0)`.

The lock alphabet is `{±e_i}`. Seed: the origin is recorded at tick `0`
with lock letter `+e_2`. Allowed continuation from `p` is the four steps
orthogonal to `L(p)`. Formation is first arrival: the tick of `q` is the
least `t(p)+1` among allowed parents `p` already recorded. If several
parents attain that least tick, each contributing incoming letter is kept.
Uniqueness not required.

Probes stay on x:

```text
A=(1,0,0), B=(1,1,1), C=(2,0,0), D=(1,1,0).
```

Seed lock `+e_2` is orthogonal to that x-axis: `e_2·e_1=0`. A proper cubic
map sending `e_1` to `e_2` would send `A` to `e_2`, not to `A`. The present
display therefore keeps the probes and changes only the seed letter.

Reverse at k=1 is the comparison `3 t(A)^2 > t(B)^2`. Face at k=1 is the
comparison `t(C)^2 > 2 t(D)^2`. Each is `holds`, `fails`, or `undefined`
according as both ticks in the comparison are defined and the inequality
is true, false, or missing a tick.

## Theorem 1 — Tick-1 Six-Mask And Probe Ticks

The origin forbids the two steps parallel to `+e_2`. Its four orthogonal
neighbors therefore form at tick 1, and the two parallel neighbors do not.
The tick-1 6-mask is

```text
(+e_1,-e_1,+e_2,-e_2,+e_3,-e_3) = (1,1,0,0,1,1).
```

First-arrival continuation on `B_3(0)` then gives

```text
t(A)=1, t(B)=3, t(C)=4, t(D)=2.
```

All four probes lie in `B_3(0)` and are attained before the host boundary
stops the process. Incoming letters at `B` and `C` are non-unique; the ticks
are nevertheless single-valued.

## Theorem 2 — Reverse At k=1

Both `t(A)` and `t(B)` are defined, so reverse is not undefined. The
comparison is

```text
3 t(A)^2 = 3 > 9 = t(B)^2,
```

which is false. Reverse fails.

## Theorem 3 — Face At k=1

Both `t(C)` and `t(D)` are defined, so face is not undefined. The
comparison is

```text
t(C)^2 = 16 > 8 = 2 t(D)^2,
```

which is true. Face holds.

These two comparison values are displayed, not adopted. Do not write into
Admissibility. Do not attach L1.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It reports one finite seed-lock display at k=1; it does not select a physical reverse or face law. |
| V2 | Current main has no landed perp-step `+e_2` x-probe tick theorem on `B_3(0)`. |
| V3 | The host, alphabet, seed, probes, and first-arrival ticks are independently finite and exact. |
| V4 | The report is more than a restatement of Record locking because the schedule and the two inequalities are extra declared process data. |
| V5 | Displayed, not adopted: reverse fails and face holds only for this seed and these probes. |

## No-Go Discipline Gate

The negative content is narrow: this seed lock with these x-probes does not
make reverse hold at k=1. No host beyond `B_3(0)` is used, and no global
compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| seed `+e_1` with the same x-probes | align the seed to the reverse axis | different display; not executed here; would be a different seed letter |
| cubic relabel of an axis seed | rotate probes with the seed | excluded: probes stay on x |
| unique incoming letter | demand a singleton lock at every site | not required; `B` and `C` have several first-arrival letters |
| weighted hop table | replace unit ticks by a cost table | excluded; tick is `t(p)+1` |
| larger host | continue past radius 3 | excluded; host is only `B_3(0)` |
| adopt reverse/face | write the inequalities into Admissibility | excluded; displayed, not adopted |
| attach L1 | treat the display as an L1 lemma | excluded |
| different probes | move `A,B,C,D` off the stated x family | different theorem |

### N2 — wall independence

The missing physical selector for the seed letter, the missing derivation of
the perp-step rule from Admissibility, and the missing reason to adopt
reverse or face are distinct residuals. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host radius, lock alphabet, seed letter, orthogonality rule, first-arrival
tick, and x-probes are declared. Incoming-letter uniqueness is not assumed.
No weighted path cost is used. No clock beyond the integer formation tick is
used.

### N4 — source residual matching

The current axiom memo supplies cubic nearest-neighbor sites and the fact
that a present record locks one admissible possibility. It does not supply
this formation process. The residual therefore matches current sources: the
process is declared, the ticks are exact, and adoption remains open.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | six-neighbor steps and taxicab host membership | no continuum embedding |
| per site | origin seed and the four x-probes | no physical readout map |
| per mode | no mode calculation | no spectral exhaustion |
| per block | tick-1 mask, reverse, and face at k=1 | no adopted reverse/face law |
| lattice wide | checked and not executed | no host beyond `B_3(0)` and no Admissibility rewrite |

### N6 — live partial-closure paths

Live routes are a different declared seed letter, a derivation of the
perp-step rule from existing premises, a uniqueness rule for incoming
letters, or an independent reason to adopt reverse or face. None is taken
here.

### N7 — hostile steelman

**Steelman:** Seeding `+e_2` is only a cubic relabel of seeding `+e_1`, so
reverse and face must hold together.

**Answer:** A cubic map that sends `+e_1` to `+e_2` also moves the x-probes.
The present display keeps `A,B,C,D` on x. Reverse fails and face holds, so
the pair is not the axis-aligned pair. Uniqueness not required, and the
ticks remain defined.

### N8 — cross-cycle echo

This note does not attach L1 and does not treat reverse or face as
Admissibility content. It reports one finite display. FAIL / DO NOT SHIP
for “reverse is adopted,” “face is an Admissibility rule,” or “the display
is an L1 lemma.”

**Gate disposition:** PASS for the finite ticks, the tick-1 6-mask, reverse
fails, and face holds on `B_3(0)` with seed lock `+e_2`. FAIL / DO NOT SHIP
for adoption, L1 attachment, or an Admissibility edit.

## Primary Runner

The primary runner rebuilds first-arrival formation on `B_3(0)`, prints the
tick-1 6-mask, recomputes `t(A),t(B),t(C),t(D)`, evaluates reverse and face,
checks that the seed is orthogonal to the x-probes, and checks that the
display is not a cubic relabel of an axis seed. It writes no runner cache
and authors no audit verdict.
