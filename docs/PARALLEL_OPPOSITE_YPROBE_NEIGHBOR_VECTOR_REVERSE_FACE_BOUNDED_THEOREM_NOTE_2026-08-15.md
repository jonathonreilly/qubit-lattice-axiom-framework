---
claim_id: parallel_opposite_yprobe_neighbor_vector_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from unique already-recorded 6-NN lock vectors on the four y-probes of the parallel-opposite two-site seed are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/parallel_opposite_yprobe_neighbor_vector_reverse_face_2026_08_15.py
---

# Unique Neighbor-Lock Vector Reverse And Face On The Parallel-Opposite Two-Site Seed Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** unique letter in `{±e_i}` or `UNDEFINED` read from already-recorded
six-neighbor lock *vectors* at the formation tick of four y-probes of the
displayed parallel-opposite two-site seed, scored as reverse and face. The
unique letter is the singleton lock vector of those already-recorded
neighbors, or `UNDEFINED` if the lock-vector set is empty or not a singleton.
Occupancy `n` is not used. The probe's own incoming lock is not used.
Uniqueness of incoming locks is not required. Formation ticks are not scored.
`A` is not a seed site. This seed is not a proper cubic image of the
perp-opposite two-site seed `{0,e_2}` with locks `+e_1/−e_1`; a cubic image of
that seed is `{0,e_1}` with locks `±e_2`. This is not leftover of the four
x-probe lists on the same seed. This is not leftover of the opposite-lock
y-probe lists. Displayed, not adopted. This note does not write the unique
vector letter into Admissibility and does not attach a formation member from
already-recorded six-neighbor locks. This is not a sixteen-combination free
lettering.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/parallel_opposite_yprobe_neighbor_vector_reverse_face_2026_08_15.py`](../scripts/parallel_opposite_yprobe_neighbor_vector_reverse_face_2026_08_15.py)

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
claim_type_reason: "Exact report of already-recorded six-neighbor lock lists and the unique lock-vector letter on the four y-probes of the parallel-opposite two-site seed, with reverse UNDEFINED and face fail; uniqueness of incoming locks is not claimed and the letters are not adopted."
trace_class: frontier_discovery
target_claim_id: parallel_opposite_yprobe_neighbor_vector_reverse_face
target_blocker_text: "display reverse and face from unique already-recorded 6-NN lock vectors on the four y-probes of the parallel-opposite two-site seed, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the unique vector letter into Admissibility, do not reduce to named sign, do not use occupancy n, do not score formation ticks, do not reuse leftover of the four x-probe lists or of the opposite-lock y-probe lists, and do not identify the letter with the probe's own incoming step."
conditional_surface_status: "exact on B_3(0) for unique lock-vector letters from already-recorded six-neighbor locks on the four y-probes of the parallel-opposite two-site seed; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose
already-recorded six-neighbor lock lists and unique vector letters are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(0,1,1)`. `A` is not a seed site.

Lock alphabet of the displayed process: `{±e_1, ±e_2, ±e_3}`.

Seed: the two-record set `{0, (1,0,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(1,0,0)=−e_1`. Those locks are opposite and
parallel to the seed edge. Probe `A` is `(0,1,0)`, not the seed partner.

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

That incoming lock is not the unique vector letter scored below.

Both seed locks lie on the `e_1` axis, so the allowed-step plane at each seed
site is the span of `{e_2,e_3}`. The same plane is allowed for the same-lock
two-site seed `+e_1/+e_1` on `{0,(1,0,0)}`. Formation ticks of the four
y-probes therefore agree with that same-lock process. Reverse and face are
not scored from those ticks.

The parallel-opposite pair `+e_1/−e_1` on `{0,(1,0,0)}` is not a proper cubic
image of the perp-opposite pair `+e_1/−e_1` on `{0,(0,1,0)}`. A cubic image of
that perp-opposite seed is `{0,e_1}` with locks `±e_2`. Seed displacement
dotted with the lock axis is `0` for the perp-opposite seed and `1` for this
seed; proper cubic rotations preserve that inner product. This display is not
the cubic orbit of that perp-opposite two-site seed.

A leftover of the four x-probe already-recorded six-neighbor lock lists on
this same seed is a different object. A leftover of the opposite-lock
y-probe lists on `{0,e_2}` with locks `+e_1/−e_1` is a different object. This
note does not reuse leftover of those lists.

## Named unique letter from already-recorded six-neighbor lock vectors

At the formation tick of a y-probe `q`, collect the locks of already-recorded
six-neighbors of `q`. A neighbor is already recorded if and only if it formed
strictly earlier. A same-tick partner is not already-recorded. The probe
itself is still unread. This display does not use occupancy `n`. It does not
use the probe's own incoming lock.

If that set of lock vectors is a singleton `{v}` subset `{±e_i}`, the unique
letter is `v`. Else (empty, mixed axes, mixed orientations, or no recorded
neighbor) the unique letter is `UNDEFINED`.

A process-determined unique letter at a probe is a value in `{±e_i}` assigned
by that named construction from already-recorded six-neighbor lock vectors, or
`UNDEFINED`. Incoming `{±e_i}` tags of the probe itself are not that
assignment. Identifying a named sign of those locks with the unique letter is
refused: named-sign lettering lost the axis. Reverse and face are scored on
the unique lock vector. They are not scored on `{+,−}` names, not scored on
formation ticks, and are not an occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  L(A) and L(B) are defined and L(A)+L(B)=(0,0,0)
face     <=>  L(C) and L(D) are defined and L(C)+L(D)=(0,0,0)
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. If both letters are defined and the vector sum is the origin,
the comparison is `hold`. If both letters are defined and the vector sum is
not the origin, the comparison is `fail`. The report is one of `hold`,
`fail`, or `UNDEFINED`.

Admissibility is not edited. Unique letters are not written into
Admissibility.

## Theorem 1 — recorded-neighbor lock list and unique vector letter at each y-probe

Direct enumeration of the displayed parallel-opposite process on `B_3(0)`
forms all four y-probes. Formation ticks are `t(A)=t(0,1,0)=1`,
`t(B)=t(1,1,1)=2`, `t(C)=t(0,2,0)=4`, `t(D)=t(1,1,0)=1`. Those ticks locate
the already-recorded six-neighbor set. They are not occupancy kernels and are
not the reverse/face scoring.

At each formation tick the already-recorded six-neighbor lock list and unique
vector letter are:

```text
A: +e_1 at (0, 0, 0);                                                                L(A) = +e_1
B: +e_3 at (1, 0, 1), +e_2 at (1, 1, 0);                                            L(B) = UNDEFINED
C: +e_2 at (-1, 2, 0), +e_2 at (0, 1, 0), +e_2 at (0, 2, 1), +e_2 at (0, 2, -1);  L(C) = +e_2
D: −e_1 at (1, 0, 0);                                                                L(D) = −e_1
```

`A` is not a seed. It forms at tick 1 from the origin by the allowed step
`+e_2`. Its already-recorded six-neighbor is the origin locking `+e_1`, so
`L(A)=+e_1`. That letter is not `A`'s own incoming lock `+e_2`.

`B`'s already-recorded neighbors lock `+e_3` and `+e_2`. Those lock vectors
are not a singleton, so `L(B)` is `UNDEFINED`. Named signs of both vectors
are `+`; named-sign lettering lost the axis.

`C`'s already-recorded neighbors are four copies of `+e_2`, so the lock-vector
set is a singleton and `L(C)=+e_2`. Incoming locks at `C` mix `+e_1`, `+e_3`,
and `−e_3`. That mixed incoming set is not the unique letter.

`D` forms at tick 1 from the seed partner `(1,0,0)` by the allowed step
`+e_2`. Its already-recorded six-neighbor is that seed partner locking
`−e_1`, so `L(D)=−e_1`. That letter is not `D`'s own incoming lock `+e_2`.

Incoming locks exist and need not be unique (`B` keeps two earliest incoming
steps; `C` keeps three). That non-uniqueness is not the unique-lettering of
already-recorded neighbor locks. The unique letters are not identified with
those incoming steps. Uniqueness is not required.

No y-probe has an empty recorded-neighbor lock list. `B` is `UNDEFINED` from
mixed lock vectors, not from emptiness.

This four-tuple of lists is not leftover of the four x-probe lists on the
same seed. The x-probes `A=(1,0,0)`, `C=(2,0,0)` are different sites. Shared
sites `B` and `D` do not make the y-probe display a reprint. It is not
leftover of the opposite-lock y-probe lists: there `A` is a seed with an
empty already-recorded list.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if `L(A)` and `L(B)` are defined and
`L(A)+L(B)=(0,0,0)`. The unique letters are `L(A)=+e_1` and
`L(B)=UNDEFINED`. Reverse is `UNDEFINED`.

Reverse: UNDEFINED

This is not `hold` and not `fail`. A leftover of the four x-probe lists on
this same seed also reported reverse `UNDEFINED`, but that leftover used
x-probe `A=(1,0,0)` as a seed site. Those are not these y-probes: here `A` is
`(0,1,0)` and forms at tick 1. Named-sign lettering of `B` would collapse
`+e_2` and `+e_3` to a shared `+` and would report a defined letter at `B`.
That readout is a different object and is not used. Formation ticks `t(A)=1`
and `t(B)=2` are displayed process data and are not the reverse predicate.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if `L(C)` and `L(D)` are defined and
`L(C)+L(D)=(0,0,0)`. The unique letters are `L(C)=+e_2` and `L(D)=−e_1`.
Both letters are defined. Their vector sum is `(1,-1,0)`, not the origin.
Face is `fail`.

Face: fail

Displayed, not adopted. The letters are not written into Admissibility.

This is not `hold` and not `UNDEFINED`. A leftover of the four x-probe lists
on this same seed had `L(C)=UNDEFINED` from mixed locks at x-probe
`C=(2,0,0)` and reported face `UNDEFINED`. Here y-probe `C=(0,2,0)` has a
singleton recorded-neighbor lock `+e_2`, and face fails against `L(D)=−e_1`.
A leftover of the opposite-lock y-probe lists had `L(C)=−e_1` and
`L(D)=UNDEFINED`. Named-sign lettering of `C` and `D` would assign `+` and
`−` and would lose that the vectors are `+e_2` and `−e_1`.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify unique letters with the probe's own incoming `{±e_i}`.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not score reverse or face from formation-tick inequalities.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  recorded-neighbor lock vectors.
- It does not enlarge the host beyond `B_3(0)`.
- It does not treat the parallel-opposite seed as a proper cubic image of the
  perp-opposite two-site seed.
- It does not reprint leftover of the four x-probe lists on this seed.
- It does not reprint leftover of the opposite-lock y-probe lists.
- It does not treat `A` as a seed site.
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
parallel-opposite two-site process, the already-recorded six-neighbor lock
lists, the unique vector letter from those locks, and the reverse/face
predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; parallel-opposite two-site seed `+e_1/−e_1` on `{0,(1,0,0)}` |
| already-recorded six-neighbor lock lists at each y-probe formation tick | Theorem 1 |
| unique vector letter from those locks | Theorem 1; `+e_1`, `UNDEFINED`, `+e_2`, `−e_1` |
| reverse and face | Theorems 2–3; `UNDEFINED` / `fail` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| occupancy-kernel inner product | not used |
| probe's own incoming lock as the letter | not used |
| formation-tick reverse/face | not scored; allowed-step plane of `±e_1` agrees with the same-lock seed |
| formation member from already-recorded six-neighbor locks | not attached |
| unique letters as Admissibility content | not adopted |
| cubic orbit of the perp-opposite two-site seed | not this seed |
| leftover of the four x-probe lists | different object; not reused |
| leftover of the opposite-lock y-probe lists | different object; not reused |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: unique lock-vector letter from already-recorded six-neighbor locks on the four y-probes of the parallel-opposite two-site seed, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed unique-vector neighbor-lock reverse/face report on these four parallel-opposite y-probes. |
| V3 | Recorded-neighbor lock lists, unique vector letters, and the `UNDEFINED`/`fail` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads already-recorded six-neighbor lock vectors at formation and scores their sum. |
| V5 | It is not an adopted content rule: the letters remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those letters into
Admissibility, does not identify them with the probe's own incoming steps,
does not reduce them to named signs, does not score formation ticks, does not
reuse leftover of the four x-probe lists or of the opposite-lock y-probe
lists, and does not use occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| leftover of the four x-probe lists | copy `+e_1`, `UNDEFINED`, `UNDEFINED`, `−e_1` and face `UNDEFINED` | refused; these are the y-probes `A=(0,1,0)`, `C=(0,2,0)`; `L(C)=+e_2` and face is `fail` |
| leftover of the opposite-lock y-probe lists | copy `UNDEFINED`, `+e_3`, `−e_1`, `UNDEFINED` | refused; here `A` is not a seed, `L(A)=+e_1`, and `L(C)=+e_2` |
| named-sign lettering of the same neighbor locks | map `±e_i` to `{+,−}` | refused; lost the axis; `B`'s `{+e_2,+e_3}` would collapse to `+` while the unique vector is `UNDEFINED`; `C` and `D` would be `+` and `−` while the vectors `+e_2` and `−e_1` fail to sum to the origin |
| identify unique letter with the probe's own incoming `{±e_i}` | map `A`'s incoming `+e_2` to `L(A)` | refused; `L(A)=+e_1` from the origin's already-recorded lock |
| reverse/face from self-incoming lock vectors | reuse mixed incoming at `B` and at `C` | different object; not this display |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score any tick order | different object; ticks agree with the same-lock seed and are not scored |
| treat this seed as a cubic image of `{0,e_2}` with locks `±e_1` | rotate the perp-opposite seed onto `{0,e_1}` with locks `±e_1` | refused; a cubic image is `{0,e_1}` with locks `±e_2` |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt letters into Admissibility | rewrite the local rule by `{±e_i}` | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; `B` keeps two earliest incoming steps and `C` keeps three |
| treat `A` as a seed | count a same-tick partner or report an empty list at `A` | refused; `A` forms at tick 1 and `L(A)=+e_1` |

Honesty marker for each row: `ATTEMPTED`.

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of the unique vector
letter are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, parallel-opposite two-site seed `+e_1` and `−e_1` on
`{0,(1,0,0)}`, perpendicular step rule, incoming-step lock, unique letter from
already-recorded six-neighbor lock vectors, four y-probes, `A` not a seed,
and reverse/face as vector-sum zero are declared. No uniqueness of incoming
locks, no occupancy `n`, no named-sign reduction, no tick reverse/face, no
leftover of the four x-probe lists, no leftover of the opposite-lock y-probe
lists, no formation attachment from already-recorded six-neighbor locks, and
no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`UNDEFINED`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unique letter from recorded-neighbor lock vectors | no continuum alphabet |
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
force reverse to hold because the origin already locks `+e_1`, leftover of
the four x-probe lists should be imported including face `UNDEFINED`, leftover
of the opposite-lock y-probe lists should make `A` empty, face should hold
from opposite named signs at `C` and `D`, and occupancy `n` should track the
unique vector.

**Answer:** The named construction assigns unique letters `+e_1`,
`UNDEFINED`, `+e_2`, `−e_1` at `A,B,C,D` from already-recorded six-neighbor
lock vectors. Occupancy `n` is not used. Reverse is `UNDEFINED` because `L(B)`
mixes `+e_2` and `+e_3`. Face is `fail` because `+e_2` and `−e_1` do not sum
to the origin. Formation ticks are not scored. Leftover of the four x-probe
lists is a different object. Leftover of the opposite-lock y-probe lists is a
different object. `A` is not a seed. The bits remain displayed. Incoming-lock
uniqueness is not required.

### N8 — cross-cycle echo

A leftover of the four x-probe lists on this same parallel-opposite seed
reports unique letters `+e_1`, `UNDEFINED`, `UNDEFINED`, `−e_1` with reverse
`UNDEFINED` and face `UNDEFINED`. That is not this display: the y-probes are
`A=(0,1,0)` and `C=(0,2,0)`, `L(C)=+e_2`, and face is `fail`. A leftover of
the opposite-lock y-probe lists on `{0,e_2}` with locks `+e_1/−e_1` reports
`UNDEFINED`, `+e_3`, `−e_1`, `UNDEFINED` with reverse `UNDEFINED` and face
`UNDEFINED`; there `A` is a seed. Named-sign lettering of the y-probe lists
would assign a defined `+` at `B` and opposite signs at `C` and `D`, and would
lose the axis. A self-incoming lock-vector readout on this same process sees
`+e_2` at `A` and at `D` and mixed incoming steps at `B` and at `C`. This note
does not reuse those scorings.

**Gate disposition:** PASS for the unique-vector already-recorded
six-neighbor-lock reverse/face reports on the four parallel-opposite y-probes
above. FAIL / DO NOT SHIP for “the unique letter equals the named sign,”
“the unique letter equals the probe's own incoming step,” “letters are
Admissibility,” “the letter is occupancy `n`,” “reverse holds,” “face holds,”
“this is leftover of the four x-probe lists,” or “this is leftover of the
opposite-lock y-probe lists.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the parallel-opposite
two-site perp-step incoming-lock process, collects already-recorded
six-neighbor locks at each y-probe's formation tick, reads the unique
lock-vector letter at the four y-probes, and checks Theorems 1--3. It also
checks that the construction is not leftover of the four x-probe lists, that
it is not leftover of the opposite-lock y-probe lists, that it is not
named-sign lettering, that the probe's own incoming step is not the unique
letter, that occupancy `n` is not used, that formation ticks are not scored,
that the seed is not a proper cubic image of the perp-opposite two-site seed,
that `A` is not a seed, and that a formation member from already-recorded
six-neighbor locks is not attached. No runner cache is written.
