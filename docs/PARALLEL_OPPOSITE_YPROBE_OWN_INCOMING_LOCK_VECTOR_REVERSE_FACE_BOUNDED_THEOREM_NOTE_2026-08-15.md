---
claim_id: parallel_opposite_yprobe_own_incoming_lock_vector_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from the probe's own unique incoming lock vector on the four parallel-opposite y-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/parallel_opposite_yprobe_own_incoming_lock_vector_reverse_face_2026_08_15.py
---

# Own Incoming Lock Vector Reverse And Face On Four Parallel-Opposite Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** unique letter in `{±e_i}` or `UNDEFINED` read from the probe's own
unique earliest incoming lock on four y-probes of the displayed
parallel-opposite two-site process, scored as reverse and face. The unique
letter is that singleton incoming lock vector, or `UNDEFINED` if several
earliest incoming steps exist. Seeds keep their seed letters. Probe `A` is
not a seed. Occupancy `n` is not used. Already-recorded six-neighbor locks
are not the letter. This is not named-sign lettering. Uniqueness of incoming
locks is not required. This is not leftover of the unique already-recorded
six-neighbor lock-vector lists on these same y-probes. This is not the four
parallel-opposite x-probes. This is not the opposite-lock y-probe
own-incoming seed `{0,e_2}` with locks `±e_1` (different seed). Displayed,
not adopted. This note does not write the unique vector letter into
Admissibility and does not attach a formation member from already-recorded
six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/parallel_opposite_yprobe_own_incoming_lock_vector_reverse_face_2026_08_15.py`](../scripts/parallel_opposite_yprobe_own_incoming_lock_vector_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. The unique letter is a lock vector in `{±e_i}`, or `UNDEFINED`. Named
signs `{+,−}` are a coarser readout and are not the unique letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of own unique incoming lock vectors on the four parallel-opposite y-probes, with reverse UNDEFINED and face UNDEFINED; uniqueness of incoming locks is not claimed and the letters are not adopted."
trace_class: frontier_discovery
target_claim_id: parallel_opposite_yprobe_own_incoming_lock_vector_reverse_face
target_blocker_text: "display reverse and face from the probe's own unique incoming lock vector on the four parallel-opposite y-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the unique vector letter into Admissibility, do not reduce to named sign, do not use occupancy n, do not use already-recorded six-neighbor locks as the unique letter, and do not treat this as leftover of those lists, as the parallel-opposite x-probes, or as the opposite-lock y-probe own-incoming seed."
conditional_surface_status: "exact on B_3(0) for own unique incoming lock-vector letters on the four parallel-opposite y-probes; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Displayed process

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, and `e_3=(0,0,1)`. The six nearest-neighbor
steps are

```text
NN = {+e_1,-e_1,+e_2,-e_2,+e_3,-e_3}.
```

The finite host is the closed Euclidean ball of radius 3 centered at the
origin,

```text
B_3(0) = { n in Z^3 : n·n <= 9 }.
```

No larger host is used. The four y-probes are the only sites whose own unique
incoming lock vectors are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. A is not a seed.

Lock alphabet of the displayed process: `{±e_1, ±e_2, ±e_3}`.

Seed: the two-record set `{0, (1,0,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(1,0,0)=−e_1`. Those locks are opposite and
parallel to the seed edge. Seeds have their seed letters. This seed is not
the opposite-lock y-probe own-incoming seed `{0,e_2}` with locks `±e_1`.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept as a
possible lock. Uniqueness is not required. A later parent does not re-form
`q`.

## Named unique letter from the probe's own incoming lock

Letter at a formed probe `q` is `q`'s own unique incoming lock: the singleton
earliest incoming step in `{±e_i}`. If several earliest incoming steps exist,
the unique letter is `UNDEFINED`. Seeds have their seed letters. Probe `A` is
not a seed. This display does not use occupancy `n`. It does not use
already-recorded six-neighbor locks as the unique letter. It does not use a
six-neighbor star.

A process-determined unique letter at a probe is a value in `{±e_i}` assigned
by that named construction from the probe's own unique incoming lock, or
`UNDEFINED`. Already-recorded six-neighbor lock vectors are not that
assignment. Identifying a named sign of those locks with the unique letter is
refused: named-sign lettering lost the axis. Reverse and face are scored on
the unique lock vector. They are not scored on `{+,−}` names.

This is not leftover of the unique already-recorded six-neighbor lock-vector
lists on these same y-probes: that leftover assigned `L(A)=+e_1` from the
origin's already-recorded neighbor lock and `L(D)=−e_1` from the seed
partner's already-recorded neighbor lock, and assigned a unique neighbor
lock at `C`. Record readout at A is A's own incoming lock. Record readout at D is D's own incoming lock. Record readout at C is C's own incoming lock.

This is not the four parallel-opposite x-probes: those sites used the seed
partner as probe `A` and reported `L(A)=−e_1`.

Reverse and face (displayed):

```text
reverse  <=>  L(A) and L(B) are defined and L(A)+L(B)=(0,0,0)
face     <=>  L(C) and L(D) are defined and L(C)+L(D)=(0,0,0)
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. If both letters are defined and the vector sum is not zero, the
comparison fails. The report is one of `hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Unique letters are not written into
Admissibility.

## Theorem 1 — own incoming lock (or UNDEFINED) at each y-probe

Direct enumeration of the displayed parallel-opposite process on `B_3(0)`
forms all four y-probes. Formation ticks locate the earliest incoming set.
They are not occupancy kernels and are not the reverse/face scoring. The own
unique incoming lock vector at each y-probe is:

```text
A: incoming +e_2;                      L(A) = +e_2
B: incoming +e_2, +e_3;                L(B) = UNDEFINED
C: incoming +e_1, +e_3, −e_3;          L(C) = UNDEFINED
D: incoming +e_2;                      L(D) = +e_2
```

`A` is not a seed. It forms at tick 1 with unique incoming step `+e_2`, so
`L(A)=+e_2`. That letter is not the leftover already-recorded neighbor lock
`+e_1` at the origin, and it is not the seed letter `−e_1` of the seed
partner.

`B` has two earliest incoming steps `+e_2` and `+e_3`. Those vectors are not
a singleton, so `L(B)` is `UNDEFINED`. Named signs of both vectors are `+`;
named-sign lettering lost the axis.

`C` has three earliest incoming steps `+e_1`, `+e_3`, and `−e_3`. Those
vectors are not a singleton, so `L(C)` is `UNDEFINED`. Record readout at C is
C's own incoming lock, not an already-recorded neighbor lock.

`D`'s own earliest incoming step is `+e_2`. Record readout at D is D's own
incoming lock, not an already-recorded neighbor lock at the seed partner.

Incoming locks exist and need not be unique. Uniqueness is not required.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if `L(A)` and `L(B)` are defined and
`L(A)+L(B)=(0,0,0)`. The unique letters are `L(A)=+e_2` and
`L(B)=UNDEFINED`. Reverse is `UNDEFINED`.

Reverse: UNDEFINED

This is not `hold` and not `fail`. The leftover unique already-recorded
six-neighbor lock-vector lists on these same y-probes assigned `L(A)=+e_1`
and `L(B)=UNDEFINED` and also reported reverse UNDEFINED, but from a
different letter at `A`. That leftover is a different object and is not
used. The own unique incoming lock-vector display on the opposite-lock
y-probe seed `{0,e_2}` with locks `±e_1` (different seed) assigned
`L(A)=−e_1` and `L(B)=+e_1` and reported reverse hold. That seed is a
different object and is not used. A named-sign readout of `B`'s mixed
incoming locks would hide the axis mix. That readout is a different object
and is not used.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if `L(C)` and `L(D)` are defined and
`L(C)+L(D)=(0,0,0)`. The unique letters are `L(C)=UNDEFINED` and
`L(D)=+e_2`. Face is `UNDEFINED`.

Face: UNDEFINED

Displayed, not adopted. The letters are not written into Admissibility.

This is not `hold` and not `fail`. The leftover already-recorded
six-neighbor lists on these same y-probes assigned `L(C)=+e_2` and
`L(D)=−e_1` and reported face fail. That leftover is a different object:
here Record readout at C mixes three earliest incoming steps, and Record
readout at D is D's own incoming lock `+e_2`. Face remains `UNDEFINED` from
`C` alone even though `D` is defined.

On the opposite-lock y-probe own-incoming seed `{0,e_2}` with locks `±e_1`
(different seed), `A` is a seed site with letter `−e_1`, reverse holds, and
`D` mixes, so face is `UNDEFINED` from that mix. Here `A` is not a seed and
reverse is `UNDEFINED` from `B`.

## What this note does not claim

- It does not require a unique incoming lock.
- It does not use already-recorded six-neighbor locks as the unique letter.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not use a six-neighbor star.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a free lettering independent of own incoming lock
  vectors.
- It does not enlarge the host beyond `B_3(0)`.
- It does not treat this display as leftover of the unique already-recorded
  six-neighbor lock-vector lists on these same y-probes.
- It does not treat this display as the four parallel-opposite x-probes.
- It does not treat this display as the opposite-lock y-probe own-incoming
  seed `{0,e_2}` with locks `±e_1`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.

## Current premise boundary

The Lattice, Qubit, Admissibility, and Record premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

The Admissibility reading note says the distribution concerns which possibility
a forming record locks, conditional on formation at that site; it does not
supply the formation site, probability, or rate.

This display uses Lattice to name `B_3(0)` and the four y-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
parallel-opposite process, the own unique incoming lock vectors, and the
reverse/face predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; parallel-opposite two-site seed `+e_1/−e_1` on `{0,(1,0,0)}` |
| own unique incoming lock vector at each y-probe | Theorem 1; `+e_2`, `UNDEFINED`, `UNDEFINED`, `+e_2` |
| reverse and face | Theorems 2–3; `UNDEFINED` / `UNDEFINED` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| already-recorded six-neighbor locks as the letter | not used |
| leftover of those neighbor-lock lists on these y-probes | different object; `L(A)=+e_1` and `L(D)=−e_1` are not this readout |
| four parallel-opposite x-probes | different sites; seed `A=(1,0,0)` is not this `A` |
| opposite-lock y-probe own-incoming seed `{0,e_2}` with locks `±e_1` | different seed; reverse hold is not this reverse |
| six-neighbor star | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| unique letters as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: the probe's own unique incoming lock vector on the four parallel-opposite y-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed own-incoming-lock-vector reverse/face report on these four parallel-opposite y-probes. |
| V3 | Own incoming lock sets, unique vector letters, and the `UNDEFINED`/`UNDEFINED` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the probe's own unique incoming lock and scores the vector sum. |
| V5 | It is not an adopted content rule: the letters remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those letters into
Admissibility, does not use already-recorded six-neighbor locks as the unique
letter, does not reduce them to named signs, does not use occupancy `n`, and
does not use a six-neighbor star. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| leftover unique already-recorded six-neighbor lock vectors on these y-probes | assign `L(A)=+e_1`, `L(C)=+e_2`, `L(D)=−e_1` and report face fail | refused; Record readout at A is A's own incoming lock `+e_2`, at D is D's own incoming `+e_2`, and at C mixes, so face is `UNDEFINED` |
| own unique incoming lock on the opposite-lock y-probe seed | reuse `{0,e_2}` with locks `±e_1` letters `−e_1`, `+e_1`, `+e_2`, `UNDEFINED` and reverse hold | different seed; not this parallel-opposite display |
| own unique incoming lock on the four parallel-opposite x-probes | reuse seed `A=(1,0,0)` with letter `−e_1` | refused; these y-probes have `A=(0,1,0)` at tick 1 |
| named-sign lettering of the same incoming locks | map `±e_i` to `{+,−}` | refused; lost the axis; `B`'s `{+e_2,+e_3}` would collapse to `+` |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; occupancy `n` is not used |
| six-neighbor star | score a star of neighbor locks as the letter | refused; a six-neighbor star is not used |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt letters into Admissibility | rewrite the local rule by `{±e_i}` | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; `B` keeps two earliest incoming steps and `C` keeps three |

Honesty marker for each row: `ATTEMPTED`.

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of the unique vector
letter are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1` on `{0,(1,0,0)}`,
perpendicular step rule, incoming-step lock, unique letter from the probe's
own unique incoming lock, four y-probes with `A` not a seed, and reverse/face
as vector-sum zero are declared. No uniqueness of incoming locks, no occupancy
`n`, no named-sign reduction, no already-recorded six-neighbor lock as the
letter, no leftover of those lists, no six-neighbor star, and no Admissibility
rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`UNDEFINED`/`UNDEFINED` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unique letter from own incoming lock | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four unique letters and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Opposite seed locks that are parallel to the seed edge should
force reverse to hold because the opposite-lock y-probe own-incoming display
already reported reverse hold on these same four y-probes, leftover
neighbor-lock lists should be the unique letter because they already scored
the same four sites and reported face fail, probe `A` should use a seed
letter because other own-incoming displays used a seed `A`, named signs
should suffice because they keep orientation, and occupancy `n` should track
that vector.

**Answer:** The named construction assigns unique letters `+e_2`,
`UNDEFINED`, `UNDEFINED`, `+e_2` at `A,B,C,D` from each probe's own unique
incoming lock. `A` is not a seed. Occupancy `n` is not used. Named signs lost
the axis. Reverse is `UNDEFINED` because `B` mixes. Face is `UNDEFINED`
because `C` mixes. The leftover neighbor-lock lists are a different object.
The opposite-lock y-probe own-incoming seed `{0,e_2}` with locks `±e_1` is a
different seed. The four parallel-opposite x-probes are different sites. The
bits remain displayed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A leftover unique already-recorded six-neighbor lock-vector display on these
same parallel-opposite y-probes assigned `L(A)=+e_1`, `L(B)=UNDEFINED`,
`L(C)=+e_2`, `L(D)=−e_1` and reported reverse UNDEFINED with face fail. An
own unique incoming lock-vector display on the four parallel-opposite
x-probes assigned `L(A)=−e_1`, `L(B)=UNDEFINED`, `L(C)=UNDEFINED`,
`L(D)=+e_2` and reported reverse UNDEFINED with face UNDEFINED. An own
unique incoming lock-vector display on the opposite-lock y-probe seed
`{0,e_2}` with locks `±e_1` (different seed) assigned `L(A)=−e_1`,
`L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` and reported reverse hold with
face UNDEFINED. This note is not those displays: Record readout at `A` is
own incoming `+e_2`, readout at `D` is own incoming `+e_2`, reverse is
`UNDEFINED` because `L(B)` mixes, and face is `UNDEFINED` because `L(C)`
mixes.

**Gate disposition:** PASS for the own unique incoming lock-vector
reverse/face reports on the four parallel-opposite y-probes above. FAIL / DO NOT SHIP
for “the unique letter equals the named sign,” “the unique letter equals an
already-recorded six-neighbor lock,” “letters are Admissibility,” “the letter
is occupancy `n`,” “reverse holds,” “face holds,” “this is leftover of the
y-probe neighbor-lock lists,” “this is the four parallel-opposite x-probes,”
or “this is the opposite-lock y-probe own-incoming seed.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the parallel-opposite
two-site perp-step incoming-lock process, reads each y-probe's own unique
incoming lock vector at the four y-probes, and checks Theorems 1--3. It also
checks that the construction is not named-sign lettering, that
already-recorded six-neighbor locks are not the unique letter, that occupancy
`n` is not used, that a six-neighbor star is not used, that the seed is not
the opposite-lock y-probe own-incoming seed, that the probes are not the four
parallel-opposite x-probes, that leftover of the unique already-recorded
six-neighbor lock-vector lists is not reused, and that a formation member
from already-recorded six-neighbor locks is not attached. No runner cache is
written.
