---
claim_id: opposite_lock_yprobe_minimal_t_existential_opposite_holding_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "The later-tick exist-opposite reverse/face bits on nsopp y-probes at each T, and the smallest T at which both HOLD, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_yprobe_minimal_t_existential_opposite_holding_2026_08_15.py
---

# Minimal T Later-Tick Existential Opposite Holding On Four Opposite-Lock Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the later-tick exist-opposite reverse/face bits on the four
opposite-lock y-probes at each integer T from 0 through the max formation
tick of those probes in `B_3(0)`, and the smallest T at which reverse_T
HOLD and face_T HOLD. Let `t(q)` be the formation tick of probe `q`. Let
`T_max` be the maximum of `t(A)`, `t(B)`, `t(C)`, `t(D)` among those defined
in `B_3(0)`. For each integer T from 0 through `T_max`, at tick T let
`S_T(q)` be the set of locks of six-neighbors of `q` that formed at tick
`≤ T` and are not `q`. Reverse_T holds if and only if some lock in `S_T(A)`
is the vector opposite of some lock in `S_T(B)`. Face_T holds if and only
if some lock in `S_T(C)` is the vector opposite of some lock in `S_T(D)`.
Empty `S_T` on either side of a comparison is `UNDEFINED`; nonempty with no
opposite pair fails. Occupancy `n` is not used. The probe's own incoming
lock is not used. This is not named-sign lettering. This is not a unique
lock-vector leftover and not a sum leftover. This is not leftover of the
global-T=3 later-tick lists on these same y-probes: that display waits for
the first T at which all four probes are recorded and reports different
lock sets. This is not leftover of formation-tick already-recorded sets:
that readout takes strictly earlier neighbors at each probe's own `t` and
finds empty `S(A)`, so reverse is `UNDEFINED`. Uniqueness of incoming locks
is not required. Uniqueness of the lock set is not required. Displayed, not
adopted. This note does not write existential opposite into Admissibility
and does not attach a formation member from later-tick six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_yprobe_minimal_t_existential_opposite_holding_2026_08_15.py`](../scripts/opposite_lock_yprobe_minimal_t_existential_opposite_holding_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse_T and face_T are scored on existence of an opposite pair in
the later-tick six-neighbor lock sets at that T. Named signs `{+,−}` are a
coarser readout and are not used. A singleton unique lock-vector letter is a
different readout and is not used. A `Z^3` sum of those locks is a different
readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of later-tick six-neighbor lock reverse/face bits on the four opposite-lock y-probes at each T through T_max, and of the smallest T at which both HOLD; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_yprobe_minimal_t_existential_opposite_holding
target_blocker_text: "for T=0,1,2,... up to max formation tick of the four nsopp y-probes, score later-tick exist-opposite reverse and face at that T; report the smallest T with reverse AND face HOLD, or none"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse_T and face_T displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with the probe's own incoming step, and do not identify the T=2 sets with the global-T=3 later-tick lists."
conditional_surface_status: "exact on B_3(0) for existential opposite of later-tick six-neighbor locks on the four opposite-lock y-probes at each T through T_max; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose later-tick
six-neighbor lock sets are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`. This seed is not the perp
two-site seed `+e_1/+e_2`.

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

That incoming lock is not a member of `S_T(q)` scored below unless it appears
as a lock of some six-neighbor of `q`.

## Named existential opposite from later-tick six-neighbor locks at each T

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `T_max` be the maximum of those four ticks. Direct enumeration
gives `t(A)=0`, `t(B)=2`, `t(C)=1`, `t(D)=3`, so `T_max=3`. The display
scans T=0,1,2,3. It does not scan a larger ball and does not use formation
ticks of sites other than the four y-probes to set the upper bound.

The scan is for each integer T from 0 through `T_max`. At that T, for each
probe `q`, let `S_T(q)`
be the set of locks of six-neighbors of `q` that formed at tick `≤ T` and
are not `q`. Same-tick and later-than-formation neighbors count whenever they
have formed by T. The probe itself is excluded. This display does not use
occupancy `n`. It does not use the probe's own incoming lock. Duplicate locks
at two neighbors collapse in the set. The construction does not require
`S_T(q)` to be a singleton. It does not sum `S_T(q)`. It is not a unique
lock-vector leftover and not a sum leftover. It is not leftover of the
global-T=3 later-tick lists. It is not leftover of formation-tick
already-recorded lock sets.

Incoming `{±e_i}` tags of the probe itself are not `S_T(q)`. Identifying a
named sign of those locks with reverse or face is refused: named-sign
lettering lost the axis. Reverse and face are scored on existence of a pair
of lock vectors that add to zero. They are not scored on `{+,−}` names and
are not an occupancy-kernel inner product.

Reverse_T and face_T (displayed):

```text
reverse_T  <=>  some a in S_T(A) and some b in S_T(B) with a+b=(0,0,0)
face_T     <=>  some c in S_T(C) and some d in S_T(D) with c+d=(0,0,0)
```

If `S_T(A)` or `S_T(B)` is empty, reverse_T is `UNDEFINED`. Else reverse_T
fails if no such pair exists. If `S_T(C)` or `S_T(D)` is empty, face_T is
`UNDEFINED`. Else face_T fails if no such pair exists. The report is one of
`hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility.

## Theorem 1 — reverse_T and face_T for each T

Direct enumeration of the displayed opposite-lock process on `B_3(0)` forms
all four y-probes. The formation ticks are `t(A)=0`, `t(B)=2`, `t(C)=1`,
`t(D)=3`. `A` is a seed. All four are defined in `B_3(0)`, so

```text
T_max = max{t(A), t(B), t(C), t(D)} = 3.
```

At each T the six-neighbor lock lists, lock sets, and bits are as follows.

### T=0

```text
A: +e_1 at (0, 0, 0);
   S_0(A) = {+e_1}
B: (empty);
   S_0(B) = {}
C: −e_1 at (0, 1, 0);
   S_0(C) = {−e_1}
D: −e_1 at (0, 1, 0);
   S_0(D) = {−e_1}
```

`S_0(B)` is empty, so reverse_0 is `UNDEFINED`. Both `S_0(C)` and `S_0(D)`
equal `{−e_1}` and `−e_1+(−e_1)≠(0,0,0)`, so face_0 fails.

T=0: reverse UNDEFINED, face fail

### T=1

```text
A: +e_2 at (0, 2, 0), +e_1 at (0, 0, 0), +e_3 at (0, 1, 1),
   −e_3 at (0, 1, -1);
   S_1(A) = {+e_1, +e_2, +e_3, −e_3}
B: +e_3 at (0, 1, 1);
   S_1(B) = {+e_3}
C: −e_1 at (0, 1, 0);
   S_1(C) = {−e_1}
D: −e_1 at (0, 1, 0);
   S_1(D) = {−e_1}
```

Both reverse sides are nonempty. The pair `−e_3` in `S_1(A)` with `+e_3` in
`S_1(B)` sums to zero, so reverse_1 holds. Face_1 still sees `{−e_1}` on
both sides, so face_1 fails.

T=1: reverse hold, face fail

### T=2

```text
A: +e_2 at (0, 2, 0), +e_1 at (0, 0, 0), +e_3 at (0, 1, 1),
   −e_3 at (0, 1, -1);
   S_2(A) = {+e_1, +e_2, +e_3, −e_3}
B: +e_3 at (0, 1, 1), +e_1 at (1, 0, 1);
   S_2(B) = {+e_1, +e_3}
C: +e_1 at (1, 2, 0), −e_1 at (-1, 2, 0), −e_1 at (0, 1, 0),
   +e_3 at (0, 2, 1), +e_2 at (0, 2, 1), −e_3 at (0, 2, -1),
   +e_2 at (0, 2, -1);
   S_2(C) = {+e_1, −e_1, +e_2, +e_3, −e_3}
D: −e_1 at (0, 1, 0), +e_1 at (1, 2, 0), +e_1 at (1, 1, 1),
   +e_1 at (1, 1, -1);
   S_2(D) = {+e_1, −e_1}
```

Both reverse sides are nonempty. The pair `−e_3` in `S_2(A)` with `+e_3` in
`S_2(B)` sums to zero, so reverse_2 holds. Both face sides are nonempty.
The pair `−e_1` in `S_2(C)` with `+e_1` in `S_2(D)` sums to zero, so face_2
holds. Mixed remains a set. `S_2(A)` has no `−e_1`: the probe is excluded,
and no six-neighbor of `A` formed by T=2 locks `−e_1`.

T=2: reverse hold, face hold

These T=2 sets are not the global-T=3 later-tick lists:
`S_2(A)` lacks `−e_2`, `S_2(B)={+e_1, +e_3}` is not the T=3 five-letter
set, and `S_2(D)={+e_1, −e_1}` is not the T=3 five-letter set.

### T=3

```text
A: −e_2 at (1, 1, 0), −e_3 at (1, 1, 0), +e_3 at (1, 1, 0),
   −e_2 at (-1, 1, 0), −e_3 at (-1, 1, 0), +e_3 at (-1, 1, 0),
   +e_2 at (0, 2, 0), +e_1 at (0, 0, 0), +e_3 at (0, 1, 1),
   −e_3 at (0, 1, -1);
   S_3(A) = {+e_1, +e_2, −e_2, +e_3, −e_3}
B: +e_3 at (0, 1, 1), +e_3 at (1, 2, 1), +e_2 at (1, 2, 1),
   +e_1 at (1, 2, 1), +e_1 at (1, 0, 1), +e_3 at (1, 1, 2),
   −e_2 at (1, 1, 0), −e_3 at (1, 1, 0), +e_3 at (1, 1, 0);
   S_3(B) = {+e_1, +e_2, −e_2, +e_3, −e_3}
C: +e_1 at (1, 2, 0), −e_1 at (-1, 2, 0), −e_1 at (0, 1, 0),
   +e_3 at (0, 2, 1), +e_2 at (0, 2, 1), −e_3 at (0, 2, -1),
   +e_2 at (0, 2, -1);
   S_3(C) = {+e_1, −e_1, +e_2, +e_3, −e_3}
D: −e_1 at (0, 1, 0), +e_1 at (1, 2, 0), −e_3 at (1, 0, 0),
   +e_3 at (1, 0, 0), +e_2 at (1, 0, 0), +e_1 at (1, 1, 1),
   +e_1 at (1, 1, -1);
   S_3(D) = {+e_1, −e_1, +e_2, +e_3, −e_3}
```

Both pairs of sets are nonempty. Reverse_3 holds by `+e_2+(−e_2)=(0,0,0)`.
Face_3 holds by `−e_1+(+e_1)=(0,0,0)`. This T=3 row is the global later-tick
display; it is recorded here only as the last row of the T-scan. The
minimal-T answer below is not this row.

T=3: reverse hold, face hold

Incoming locks exist and need not be unique (`D` has three earliest incoming
steps `−e_2`, `−e_3`, and `+e_3`). That non-uniqueness is not a
unique-lettering of later-tick neighbor lock vectors. The lock sets are not
identified with those incoming steps. Uniqueness is not required.

## Theorem 2 — smallest T with reverse_T HOLD and face_T HOLD

Scan T=0,1,2,3 from Theorem 1. Both bits HOLD first at T=2. No smaller T in
the scan has reverse_T hold and face_T hold: T=0 has reverse `UNDEFINED` and
face fail; T=1 has reverse hold and face fail. T=3 also has both hold, but
it is later.

Smallest T: 2

The T=2 lock sets are not leftover of the global-T=3 later-tick lists, as
recorded in Theorem 1. They are not leftover of formation-tick
already-recorded sets: formation-tick `S(A)` is empty, so that leftover
reverse is `UNDEFINED`, while `S_2(A)` is nonempty and reverse_2 holds.

## Theorem 3 — displayed, not adopted

Displayed, not adopted. The bits are not written into Admissibility.

The T-scan and the smallest T=2 are theorem-domain data. This note does not
rewrite the local rule by existential opposite. It does not attach a
formation member from later-tick six-neighbor locks.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify lock sets with the probe's own incoming `{±e_i}`.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the later-tick lock set to be a singleton.
- It does not sum the later-tick lock set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from later-tick six-neighbor locks.
- It does not census a sixteen-combination free lettering independent of
  later-tick lock vectors.
- It does not reprint unique own-incoming lock-vector letters on these
  y-probes.
- It does not reprint later-tick existential opposite on the nnseed x-probes.
- It does not reprint formation-tick already-recorded lock sets as the
  scored object.
- It does not take the global-T=3 later-tick lists as the scored object for
  the smallest-T answer.
- It does not enlarge the host beyond `B_3(0)`.
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
opposite-lock process, the later-tick six-neighbor lock sets at each T, the
existential-opposite reverse_T/face_T predicates, and the smallest T at which
both HOLD are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; opposite-lock two-site seed `+e_1/−e_1` |
| later-tick six-neighbor lock sets at each T through `T_max=3` | Theorem 1 |
| reverse_T and face_T at T=0,1,2,3 | Theorem 1; `UNDEFINED`/`fail`, `hold`/`fail`, `hold`/`hold`, `hold`/`hold` |
| smallest T with both HOLD | Theorem 2; `2` |
| displayed, not adopted | Theorem 3 |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| probe's own incoming lock as the set | not used |
| formation member from later-tick six-neighbor locks | not attached |
| leftover of unique own-incoming letters on these y-probes | not this display |
| leftover of nnseed x-probe later-tick existential opposite | not this display |
| leftover of formation-tick already-recorded sets | not this display |
| leftover of the global-T=3 later-tick lists | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: later-tick exist-opposite reverse/face on nsopp y-probes at each T through T_max, and the smallest T at which both HOLD, or none. |
| V2 | Current main has no landed per-T later-tick existential-opposite reverse/face scan on these four opposite-lock y-probes, and no smallest-T HOLD report. |
| V3 | The per-T lock sets, the `UNDEFINED`/`fail`/`hold` reports, and smallest T=2 are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads six-neighbor lock vectors at each later tick T and scores existence of an opposite pair, then takes the first T at which both bits HOLD. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not identify them with the probe's own incoming steps,
does not reduce them to named signs, does not require a singleton lock
vector, does not sum the lock set, does not reprint unique own-incoming
letters, does not reprint nnseed x-probe later-tick leftover, does not
reprint formation-tick leftover, does not take the global-T=3 lists as the
minimal-T object, and does not use occupancy `n`. No global impossibility is
claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same neighbor locks | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while both pairs of sets at T=2 are nonempty |
| sum of the same neighbor locks | replace `S_T` by the `Z^3` sum | refused; leftover; sum of `S_2(A)` is `+e_1++e_2` and sum of `S_2(B)` is `+e_1++e_3`, which do not cancel, while `−e_3++e_3=0` |
| named-sign lettering of the same neighbor locks | map `±e_i` to `{+,−}` | refused; lost the axis; mixed `{+,−}` at `A` would hide `−e_3++e_3=0` |
| identify lock sets with the probe's own incoming `{±e_i}` | map `A`'s seed letter `−e_1` into `S_2(A)` | refused; `S_2(A)` has no `−e_1`; `S_2(A)={+e_1, +e_2, +e_3, −e_3}` |
| unique own-incoming lock-vector leftover on these y-probes | reuse `L(A)=−e_1`, `L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` | refused; different object; that leftover reports face `UNDEFINED` while later-tick `S_2(D)` is nonempty and face_2 holds |
| leftover of nnseed x-probe later-tick existential opposite | reuse seed `+e_1/+e_2` and x-probes with reverse fail | refused; different process and different frame; reverse_2 holds here |
| leftover of formation-tick already-recorded sets | reuse empty `A` and reverse `UNDEFINED` | refused; different set; later-tick `S_2(A)` is nonempty and reverse_2 holds |
| leftover of the global-T=3 later-tick lists | reuse `S_3` as the scored object for the smallest T | refused; `S_2` differs from `S_3`; smallest T is 2, not 3 |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| attach a formation member from later-tick six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; all three earliest incoming steps at `D` are kept |

### N2 — wall independence

Missing physical adoption, missing formation attachment from later-tick
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, later-tick lock set of six-neighbors formed by each
integer T through the max formation tick of the four y-probes, existential
opposite, four y-probes with seed `A`, reverse_T/face_T as existence of a
pair that sums to zero, and smallest T with both HOLD are declared. No
uniqueness of incoming locks, no occupancy `n`, no named-sign reduction, no
singleton leftover, no sum leftover, no unique own-incoming leftover, no
nnseed x-probe leftover, no formation-tick leftover, no global-T=3 list
leftover, no formation attachment from later-tick six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
smallest-T HOLD report does not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in a later-tick set | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four lock sets at each T and two reverse/face comparisons, then smallest T | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Once a six-neighbor exists at a later tick, the site should
lock that unique vector as incoming content, mixed neighbor locks should
make reverse and face `UNDEFINED`, the sets should be replaced by their
sums, unique own-incoming letters already answered reverse hold with face
`UNDEFINED`, nnseed x-probe later-tick existential opposite already answered
the later-tick question, the global-T=3 lists already answered HOLD so the
smallest T is 3, formation-tick already-recorded sets already answered the
per-probe question, named signs should suffice because they keep
orientation, and occupancy `n` should track that vector.

**Answer:** The named construction reports, at each T through `T_max=3`, the
later-tick six-neighbor lock sets and the reverse_T/face_T bits. Mixed
remains a set. The construction does not sum. Occupancy `n` is not used.
Named signs lost the axis. Both bits HOLD first at T=2 on sets
`S_2(A)={+e_1, +e_2, +e_3, −e_3}`, `S_2(B)={+e_1, +e_3}`,
`S_2(C)={+e_1, −e_1, +e_2, +e_3, −e_3}`, `S_2(D)={+e_1, −e_1}`, which are
not the global-T=3 lists and not the formation-tick empty-`A` leftover. The
bits remain displayed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same opposite-lock
y-probes assigned `L(A)=−e_1`, `L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` and
reported reverse hold with face `UNDEFINED`. Formation-tick already-recorded
six-neighbor locks on these y-probes found empty `S(A)` and reported reverse
`UNDEFINED`. Later-tick existential opposite on the nnseed x-probes reported
reverse fail and face hold on different sets `{+e_1}`, `{+e_1, +e_2, +e_3}`,
`{−e_2}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}`. The global-T=3 later-tick lists
on these y-probes are
`{+e_1, +e_2, −e_2, +e_3, −e_3}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}`,
`{+e_1, −e_1, +e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_2, +e_3, −e_3}` with both
bits hold. Unique lock-vector lettering of the T=2 lists would report reverse
`UNDEFINED` and face `UNDEFINED` because every T=2 set mixes. A sum leftover
of the T=2 lists would miss `−e_3++e_3=0`. This note is not those displays:
it scans each T, mixed remains a set, the construction does not sum, both
bits HOLD first at T=2, and the T=2 sets are not the T=3 lists.

**Gate disposition:** PASS for the per-T later-tick six-neighbor-lock
existential-opposite reverse/face reports and for smallest T=2 above.
FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the predicate
equals the unique singleton lock vector,” “the predicate equals the sum of
the lock set,” “the lock set equals the probe's own incoming step,” “bits
are Admissibility,” “the letter is occupancy `n`,” “the sets equal unique
own-incoming letters,” “the sets equal nnseed x-probe later-tick leftover,”
“the sets equal formation-tick leftover,” “the smallest T is the global T=3
lists,” “reverse fails at T=2,” or “face is `UNDEFINED` at T=2.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the opposite-lock two-site
perp-step incoming-lock process, takes `T_max` as the max formation tick of
the four y-probes, collects six-neighbor locks formed by each T at each
probe with the probe excluded, reads reverse_T and face_T, and checks
Theorems 1--3 including that the smallest T with both HOLD is 2. It also
checks that the construction is not named-sign lettering, that mixed sets
remain defined, that the construction does not sum, that the probe's own
incoming step is not the lock set, that occupancy `n` is not used, that a
formation member from later-tick six-neighbor locks is not attached, that
the T=2 sets are not leftover of unique own-incoming letters, that they are
not leftover of nnseed x-probe later-tick existential opposite, that they
are not leftover of formation-tick already-recorded sets, and that they are
not leftover of the global-T=3 later-tick lists. No runner cache is written.
