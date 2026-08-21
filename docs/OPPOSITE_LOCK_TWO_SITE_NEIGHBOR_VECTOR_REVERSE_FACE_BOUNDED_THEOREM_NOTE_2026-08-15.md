---
claim_id: opposite_lock_two_site_neighbor_vector_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from unique already-recorded 6-NN lock vectors on the four x-probes of the opposite-lock two-site seed are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_two_site_neighbor_vector_reverse_face_2026_08_15.py
---

# Unique Neighbor-Lock Vector Reverse And Face On The Opposite-Lock Two-Site Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** unique letter in `{±e_i}` or `UNDEFINED` read from already-recorded
six-neighbor lock *vectors* at the formation tick of four x-probes of the
displayed opposite-lock two-site seed, scored as reverse and face. The unique
letter is the singleton lock vector of those already-recorded neighbors, or
`UNDEFINED` if the lock-vector set is empty or not a singleton. Occupancy
`n` is not used. The probe's own incoming lock is not used. Uniqueness of
incoming locks is not required. Formation ticks are not scored: the
allowed-step plane of `±e_1` agrees with the same-lock two-site seed, so a
tick inequality is a different object. This seed is not a proper cubic image
of the perp two-site seed `+e_1/+e_2`. Displayed, not adopted. This note does
not write the unique vector letter into Admissibility and does not attach a
formation member from already-recorded six-neighbor locks. This is not a
sixteen-combination free lettering.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_two_site_neighbor_vector_reverse_face_2026_08_15.py`](../scripts/opposite_lock_two_site_neighbor_vector_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named probes. Incoming lock letters are unit nearest-neighbor
steps. The unique letter is a lock vector in `{±e_i}`, or `UNDEFINED`. Named
signs `{+,−}` are a coarser readout and are not the unique letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of already-recorded six-neighbor lock lists and the unique lock-vector letter on the four x-probes of the opposite-lock two-site seed, with reverse fail and face UNDEFINED; uniqueness of incoming locks is not claimed and the letters are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_two_site_neighbor_vector_reverse_face
target_blocker_text: "display reverse and face from unique already-recorded 6-NN lock vectors on the four x-probes of the opposite-lock two-site seed, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write the unique vector letter into Admissibility, do not reduce to named sign, do not use occupancy n, do not score formation ticks, and do not identify the letter with the probe's own incoming step."
conditional_surface_status: "exact on B_3(0) for unique lock-vector letters from already-recorded six-neighbor locks on the four x-probes of the opposite-lock two-site seed; displayed, not adopted"
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

No larger host is used. The four probes are the only sites whose
already-recorded six-neighbor lock lists and unique vector letters are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

Lock alphabet of the displayed process: `{±e_1, ±e_2, ±e_3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`.

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
two-site seed `+e_1/+e_1`. Formation ticks of the four probes therefore agree
with that same-lock process. Reverse and face are not scored from those
ticks.

The opposite pair `+e_1/−e_1` is not a proper cubic image of the perp pair
`+e_1/+e_2`. This display is not the cubic orbit of that perp two-site seed.

A leftover-closed neighbor-lock reverse on the perp two-site seed is a
different object: there the recorded-neighbor lock set at `B` has no opposite
of `+e_1`. This note does not reuse leftover closure.

## Named unique letter from already-recorded six-neighbor lock vectors

At the formation tick of a probe `q`, collect the locks of already-recorded
six-neighbors of `q`. A neighbor is already recorded if and only if it formed
strictly earlier. The probe itself is still unread. This display does not use
occupancy `n`. It does not use the probe's own incoming lock.

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
reverse  <=>  L(A) and L(B) defined and L(A)+L(B)=(0,0,0)
face     <=>  L(C) and L(D) defined and L(C)+L(D)=(0,0,0)
```

If a letter needed by a comparison is `UNDEFINED`, that comparison is
`UNDEFINED`. If both letters are defined and the vector sum is the origin,
the comparison is `hold`. If both letters are defined and the vector sum is
not the origin, the comparison is `fail`. The report is one of `hold`,
`fail`, or `UNDEFINED`.

Admissibility is not edited. Unique letters are not written into
Admissibility.

## Theorem 1 — recorded-neighbor lock list and unique vector letter at each probe

Direct enumeration of the displayed opposite-lock process on `B_3(0)` forms
all four probes. At each formation tick the already-recorded six-neighbor
lock list and unique vector letter are:

```text
A: +e_1 at (0, 0, 0), +e_1 at (1, -1, 0), +e_1 at (1, 0, 1), +e_1 at (1, 0, -1);  L(A) = +e_1
B: +e_3 at (0, 1, 1);                                                             L(B) = +e_3
C: −e_3 at (1, 0, 0), +e_3 at (1, 0, 0), +e_2 at (1, 0, 0);                      L(C) = UNDEFINED
D: −e_1 at (0, 1, 0), +e_1 at (1, 2, 0), +e_1 at (1, 1, 1), +e_1 at (1, 1, -1);  L(D) = UNDEFINED
```

`C`'s already-recorded neighbor is `A`. The incoming locks kept at `A` are
`+e_2`, `+e_3`, and `−e_3`. Those lock vectors are not a singleton, so
`L(C)` is `UNDEFINED`. `D`'s already-recorded neighbors mix `−e_1` at the
opposite-lock seed partner `(0,1,0)` with three copies of `+e_1`, so `L(D)`
is `UNDEFINED`.

Incoming locks exist and need not be unique (`A` keeps three earliest
incoming steps). That non-uniqueness is not a unique-lettering of
already-recorded neighbor locks at `A`: those neighbor locks all equal
`+e_1`. The unique letters are not identified with those incoming steps.
Uniqueness is not required.

No probe has an empty recorded-neighbor lock list. Both `C` and `D` are
`UNDEFINED` from mixed lock vectors, not from emptiness.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if `L(A)` and `L(B)` are defined and
`L(A)+L(B)=(0,0,0)`. The unique letters are `L(A)=+e_1` and `L(B)=+e_3`.
Both are defined. Their sum is `(1,0,1)`, not the origin. Reverse does not
hold.

Reverse: fail

This is not `hold` and not `UNDEFINED`. A named-sign readout of the same
neighbor locks would assign `L(A)=+` and `L(B)=+` and would report reverse
fail for a different reason. That readout is a different object and is not
used. Formation ticks `t(A)=3` and `t(B)=2` are displayed process data and
are not the reverse predicate.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if `L(C)` and `L(D)` are defined and
`L(C)+L(D)=(0,0,0)`. The unique letters are `L(C)=UNDEFINED` and
`L(D)=UNDEFINED`. Face is `UNDEFINED`.

Face: UNDEFINED

Displayed, not adopted. The letters are not written into Admissibility.

This is not `hold` and not `fail`. A same-lock two-site readout on the same
four probes keeps `L(D)=+e_1` because the seed partner also locks `+e_1`.
Here the seed partner locks `−e_1`, so `D` mixes. Face remains `UNDEFINED`
from `C` alone even before that mix.

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
- It does not treat the opposite-lock seed as a proper cubic image of the
  perp two-site seed.
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

This display uses Lattice to name `B_3(0)` and the four probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
opposite-lock two-site process, the already-recorded six-neighbor lock lists,
the unique vector letter from those locks, and the reverse/face predicates
are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; opposite-lock two-site seed `+e_1/−e_1` |
| already-recorded six-neighbor lock lists at each probe formation tick | Theorem 1 |
| unique vector letter from those locks | Theorem 1; `+e_1`, `+e_3`, `UNDEFINED`, `UNDEFINED` |
| reverse and face | Theorems 2–3; `fail` / `UNDEFINED` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| occupancy-kernel inner product | not used |
| probe's own incoming lock as the letter | not used |
| formation-tick reverse/face | not scored; allowed-step plane of `±e_1` agrees with the same-lock seed |
| formation member from already-recorded six-neighbor locks | not attached |
| unique letters as Admissibility content | not adopted |
| cubic orbit of the perp two-site seed | not this seed |
| leftover-closed reverse on the perp two-site seed | different object; not reused |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: unique lock-vector letter from already-recorded six-neighbor locks on the four x-probes of the opposite-lock two-site seed, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed unique-vector neighbor-lock reverse/face report on these four opposite-lock x-probes. |
| V3 | Recorded-neighbor lock lists, unique vector letters, and the `fail`/`UNDEFINED` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads already-recorded six-neighbor lock vectors at formation and scores their sum. |
| V5 | It is not an adopted content rule: the letters remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those letters into
Admissibility, does not identify them with the probe's own incoming steps,
does not reduce them to named signs, does not score formation ticks, and does
not use occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| named-sign lettering of the same neighbor locks | map `±e_i` to `{+,−}` | refused; lost the axis; `L(A)=+` and `L(B)=+` hide that the vectors are `+e_1` and `+e_3` |
| identify unique letter with the probe's own incoming `{±e_i}` | map `A`'s mixed incoming `{+e_2,+e_3,−e_3}` to `UNDEFINED` | refused; `L(A)=+e_1` from already-recorded neighbor locks |
| reverse/face from self-incoming lock vectors | reuse mixed incoming at `A` and at `D` | different object; not this display |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score `3 t(A)^2 > t(B)^2` or any tick order | different object; ticks agree with the same-lock seed and are not scored |
| leftover-closed reverse on the perp two-site seed | reuse leftover of recorded-neighbor locks at `B` | different object; that leftover has no opposite of `+e_1` |
| treat this seed as a cubic image of `+e_1/+e_2` | rotate the perp two-site seed onto `+e_1/−e_1` | refused; no proper cubic rotation does so |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt letters into Admissibility | rewrite the local rule by `{±e_i}` | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; the three earliest incoming steps at `A` are kept, and that mix is why `L(C)` is `UNDEFINED` |

Honesty marker for each row: `ATTEMPTED`.

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of the unique vector
letter are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, opposite-lock two-site seed `+e_1` and `−e_1`,
perpendicular step rule, incoming-step lock, unique letter from
already-recorded six-neighbor lock vectors, four probes, and reverse/face as
vector-sum zero are declared. No uniqueness of incoming locks, no occupancy
`n`, no named-sign reduction, no tick reverse/face, no formation attachment
from already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`UNDEFINED` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unique letter from recorded-neighbor lock vectors | no continuum alphabet |
| per site | `A,B,C,D` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four unique letters and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Opposite seed locks should force reverse to hold because
`+e_1` and `−e_1` are already opposites, face should hold or at least fail
on a defined pair, formation ticks should be scored because they agree with
the same-lock seed, leftover closure on the perp two-site seed should be
imported, and occupancy `n` should track the unique vector.

**Answer:** The named construction assigns unique letters `+e_1`, `+e_3`,
`UNDEFINED`, `UNDEFINED` at `A,B,C,D` from already-recorded six-neighbor
lock vectors. Occupancy `n` is not used. Reverse is `fail` because
`(+e_1)+(+e_3)≠0`. Face is `UNDEFINED` because both `C` and `D` mix.
Formation ticks are not scored. Leftover closure on the perp two-site seed
is a different object. The bits remain displayed. Incoming-lock uniqueness
is not required.

### N8 — cross-cycle echo

A leftover-closed neighbor-lock reverse on the perp two-site seed reports
that the recorded-neighbor lock set at `B` has no opposite of `+e_1`. That
is not this display: the seed here is `+e_1/−e_1`, and reverse is unique
vector fail at `A` and `B`. A same-lock unique-vector display on the same
four probes has the same `L(A)`, `L(B)`, and `L(C)`, but keeps `L(D)=+e_1`
because the seed partner also locks `+e_1`. Here `D` mixes `−e_1` with
`+e_1`. A named-sign neighbor-lock lettering of the same lists reports
`L(A)=+` and `L(B)=+` and loses the axis. A self-incoming lock-vector
readout on this same process sees mixed incoming steps at `A` and at `D`.
This note does not reuse those scorings.

**Gate disposition:** PASS for the unique-vector already-recorded
six-neighbor-lock reverse/face reports above. FAIL / DO NOT SHIP for “the
unique letter equals the named sign,” “the unique letter equals the probe's
own incoming step,” “letters are Admissibility,” “the letter is occupancy
`n`,” “reverse holds,” or “face holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the opposite-lock two-site
perp-step incoming-lock process, collects already-recorded six-neighbor locks
at each probe's formation tick, reads the unique lock-vector letter at the
four probes, and checks Theorems 1--3. It also checks that the construction is
not named-sign lettering, that the probe's own incoming step is not the unique
letter, that occupancy `n` is not used, that formation ticks are not scored,
that the seed is not a proper cubic image of the perp two-site seed, and that
a formation member from already-recorded six-neighbor locks is not attached.
No runner cache is written.
