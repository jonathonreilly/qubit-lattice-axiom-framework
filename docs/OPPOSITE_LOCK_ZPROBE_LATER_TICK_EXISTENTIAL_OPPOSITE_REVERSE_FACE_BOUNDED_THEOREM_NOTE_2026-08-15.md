---
claim_id: opposite_lock_zprobe_later_tick_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from existential opposite 6-NN locks at the first later tick when all four nsopp z-probes are recorded are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_zprobe_later_tick_existential_opposite_reverse_face_2026_08_15.py
---

# Later-Tick Existential Opposite Neighbor-Lock Reverse And Face On Four Opposite-Lock Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from existential opposite six-neighbor locks at
the first later tick in `B_3(0)` at which all four opposite-lock z-probes are
recorded. Let `t(q)` be the formation tick of probe `q`. Let `T` be the
maximum of `t(A)`, `t(B)`, `t(C)`, `t(D)` among those defined in `B_3(0)`.
At tick `T`, `S_*(q)` is the set of locks of six-neighbors of `q` that
formed at tick `≤ T` and are not `q`. Reverse holds if and only if some
lock in `S_*(A)` is the vector opposite of some lock in `S_*(B)`. Face
holds if and only if some lock in `S_*(C)` is the vector opposite of some
lock in `S_*(D)`. Empty `S_*` on either side of a comparison is
`UNDEFINED`; nonempty with no opposite pair fails. Occupancy `n` is not
used. The probe's own incoming lock is not used. This is not named-sign
lettering. This is not a unique lock-vector leftover and not a sum leftover.
This is a cubic-frame transfer of the holding later-tick existential-opposite
readout, not leftover of the opposite-lock y-probe lists: that display uses
the same two-site seed `+e_1/−e_1` and the y-probe frame
`A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)` with `T=3` and different
lock sets. This is not leftover of later-tick existential opposite on the
nnseed x-probes: that display uses the perp two-site seed `+e_1/+e_2` and the
x-probe frame. This is not leftover of the unique own-incoming lock-vector
letters on these same opposite-lock z-probes: that readout requires a
singleton incoming step and reports reverse fail with face `UNDEFINED` at
mixed `C`. Uniqueness of incoming locks is not required. Uniqueness of the
lock set is not required. Displayed, not adopted. This note does not write
existential opposite into Admissibility and does not attach a formation
member from later-tick six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_zprobe_later_tick_existential_opposite_reverse_face_2026_08_15.py`](../scripts/opposite_lock_zprobe_later_tick_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
later-tick six-neighbor lock sets. Named signs `{+,−}` are a coarser readout
and are not used. A singleton unique lock-vector letter is a different
readout and is not used. A `Z^3` sum of those locks is a different readout
and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of later-tick six-neighbor lock sets on the four opposite-lock z-probes at the first T with all four recorded, with reverse hold and face hold from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_zprobe_later_tick_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from existential opposite 6-NN locks at the first later tick when all four nsopp z-probes are recorded, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with the probe's own incoming step, and do not identify the sets with opposite-lock y-probe later-tick leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of later-tick six-neighbor locks on the four opposite-lock z-probes; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose later-tick
six-neighbor lock sets are scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`,
`C=(2,0,0)`, `D=(1,1,0)`. `A` is not a seed.

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

That incoming lock is not a member of `S_*(q)` scored below unless it appears
as a lock of some six-neighbor of `q`.

## Named existential opposite from later-tick six-neighbor locks

Let `t(q)` be the formation tick of z-probe `q` when that tick is defined in
`B_3(0)`. Let `T` be the maximum of those four ticks. This `T` is the first
tick in `B_3(0)` at which all four z-probes are recorded.

At tick `T`, for each probe `q`, let `S_*(q)` be the set of locks of
six-neighbors of `q` that formed at tick `≤ T` and are not `q`. Same-tick
and later-than-formation neighbors count whenever they have formed by `T`.
The probe itself is excluded. This display does not use occupancy `n`. It
does not use the probe's own incoming lock. Duplicate locks at two neighbors
collapse in the set. The construction does not require `S_*(q)` to be a
singleton. It does not sum `S_*(q)`. It is not a unique lock-vector leftover
and not a sum leftover. It is not leftover of opposite-lock y-probe later-tick
existential opposite. It is not leftover of nnseed x-probe later-tick
existential opposite. It is not leftover of unique own-incoming lock-vector
letters on these z-probes.

Incoming `{±e_i}` tags of the probe itself are not `S_*(q)`. Identifying a
named sign of those locks with reverse or face is refused: named-sign
lettering lost the axis. Reverse and face are scored on existence of a pair
of lock vectors that add to zero. They are not scored on `{+,−}` names and
are not an occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  some a in S_*(A) and some b in S_*(B) with a+b=(0,0,0)
face     <=>  some c in S_*(C) and some d in S_*(D) with c+d=(0,0,0)
```

If `S_*(A)` or `S_*(B)` is empty, reverse is `UNDEFINED`. Else reverse fails
if no such pair exists. If `S_*(C)` or `S_*(D)` is empty, face is
`UNDEFINED`. Else face fails if no such pair exists. The report is one of
`hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility.

## Theorem 1 — later-tick lock sets at each z-probe

Direct enumeration of the displayed opposite-lock process on `B_3(0)` forms
all four z-probes. The formation ticks are `t(A)=1`, `t(B)=2`, `t(C)=4`,
`t(D)=2`. `A` is not a seed. All four are defined in `B_3(0)`, so

```text
T = max{t(A), t(B), t(C), t(D)} = 4.
```

At tick `T=4` the six-neighbor lock lists and lock sets are:

```text
A: +e_1 at (1, 0, 1), −e_1 at (-1, 0, 1), +e_3 at (0, 1, 1),
   −e_2 at (0, -1, 1), +e_3 at (0, -1, 1), −e_1 at (0, 0, 2),
   +e_2 at (0, 0, 2), +e_1 at (0, 0, 2), +e_1 at (0, 0, 0);
   S_*(A) = {+e_1, −e_1, +e_2, −e_2, +e_3}
B: +e_3 at (0, 1, 1), +e_3 at (1, 2, 1), +e_2 at (1, 2, 1),
   +e_1 at (1, 2, 1), +e_1 at (1, 0, 1), +e_3 at (1, 1, 2),
   −e_2 at (1, 1, 0), −e_3 at (1, 1, 0), +e_3 at (1, 1, 0);
   S_*(B) = {+e_1, +e_2, −e_2, +e_3, −e_3}
C: +e_3 at (1, 0, 2), +e_3 at (-1, 0, 2), −e_1 at (0, 1, 2),
   −e_2 at (0, 1, 2), +e_1 at (0, 1, 2), +e_3 at (0, -1, 2),
   +e_3 at (0, 0, 1);
   S_*(C) = {+e_1, −e_1, −e_2, +e_3}
D: +e_3 at (0, 0, 1), +e_1 at (1, 1, 1), −e_2 at (1, -1, 1),
   +e_3 at (1, -1, 1), +e_1 at (1, -1, 1), +e_3 at (1, 0, 2),
   −e_3 at (1, 0, 0), +e_3 at (1, 0, 0), +e_2 at (1, 0, 0);
   S_*(D) = {+e_1, +e_2, −e_2, +e_3, −e_3}
```

`A`'s later-tick neighbors include the same-tick seed origin locking `+e_1`
and later `C` mixing `−e_1`, `+e_2`, and `+e_1`. `A`'s own incoming `+e_3`
appears in `S_*(A)` as a neighbor lock at `(0, 1, 1)` and `(0, -1, 1)`, but
`S_*(A)` is not `{+e_3}`: the probe is excluded, and the later-tick set
mixes five axes. `D`'s later-tick neighbors include `A` locking `+e_3`.
Mixed remains a set.

Incoming locks exist and need not be unique (`C` has three earliest incoming
steps `−e_1`, `+e_2`, and `+e_1`). That non-uniqueness is not a
unique-lettering of later-tick neighbor lock vectors. The lock sets are not
identified with those incoming steps. Uniqueness is not required.

The unique own-incoming letters on these same z-probes are `+e_3`, `+e_1`,
`UNDEFINED`, `+e_1`. Those are different objects: `S_*(A)` is not `{+e_3}`
and `S_*(C)` is nonempty. Later-tick existential opposite on the opposite-lock
y-probes reports `{+e_1, +e_2, −e_2, +e_3, −e_3}`,
`{+e_1, +e_2, −e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_2, +e_3, −e_3}`,
`{+e_1, −e_1, +e_2, +e_3, −e_3}` at `T=3` on a different frame. Later-tick
existential opposite on the nnseed x-probes reports `{+e_1}`,
`{+e_1, +e_2, +e_3}`, `{−e_2}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}` at a
different seed and different frame.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S_*(A)` and `b` in `S_*(B)`
with `a+b=(0,0,0)`. Both sets are nonempty:
`S_*(A)={+e_1, −e_1, +e_2, −e_2, +e_3}` and
`S_*(B)={+e_1, +e_2, −e_2, +e_3, −e_3}`. The pairs include
`−e_1+(+e_1)=(0,0,0)`, `+e_2+(−e_2)=(0,0,0)`, and `+e_3+(−e_3)=(0,0,0)`.
Reverse holds.

Reverse: hold

This is not `fail` and not `UNDEFINED`. Unique lock-vector lettering of the
same lists would assign mixed `S_*(A)` and mixed `S_*(B)` and would report
reverse `UNDEFINED`. That readout is a different object and is not used. A
sum leftover of the same lists would replace the sets by `+e_3` and `+e_1`
and would report reverse fail. A named-sign readout of the same neighbor
locks would lose the axis in mixed `{+,−}` at both `A` and `B`. Unique
own-incoming letters on these z-probes report reverse fail from
`L(A)=+e_3` and `L(B)=+e_1`, which are not these later-tick sets. Later-tick
existential opposite on the opposite-lock y-probes also reports reverse hold,
but from different sets at `T=3`. Later-tick existential opposite on the
nnseed x-probes reports reverse fail on different sets. Formation-time
already-recorded neighbor locks at `A` are `{+e_1}` and at `B` are `{+e_3}`,
so that leftover reverse fails.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S_*(C)` and `d` in `S_*(D)`
with `c+d=(0,0,0)`. Both sets are nonempty:
`S_*(C)={+e_1, −e_1, −e_2, +e_3}` and
`S_*(D)={+e_1, +e_2, −e_2, +e_3, −e_3}`, so `−e_1+(+e_1)=(0,0,0)`,
`−e_2+(+e_2)=(0,0,0)`, and `+e_3+(−e_3)=(0,0,0)`. Face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.

This is not `fail` and not `UNDEFINED`. Unique own-incoming letters on these
same z-probes assign `L(C)=UNDEFINED` from three earliest incoming steps and
report face `UNDEFINED`. Unique lock-vector lettering of the later-tick lists
would also report face `UNDEFINED` because both `C` and `D` mix. A sum
leftover would replace the sets by `(0,−1,1)` and `+e_1` and would fail face,
while existential opposite holds. Named-sign lettering lost the axis in mixed
`{+,−}` at `C` and at `D`. Formation-time already-recorded sets
`S_*(C)={+e_3}` and `S_*(D)={+e_3}` fail face. Later-tick existential
opposite on the opposite-lock y-probes reports face hold on different sets.

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
  z-probes.
- It does not reprint later-tick existential opposite on the opposite-lock
  y-probes.
- It does not reprint later-tick existential opposite on the nnseed x-probes.
- It does not reprint formation-time already-recorded lock sets.
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

This display uses Lattice to name `B_3(0)` and the four z-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
opposite-lock process, the later-tick six-neighbor lock sets, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; opposite-lock two-site seed `+e_1/−e_1` |
| later-tick six-neighbor lock sets at first `T` with all four z-probes recorded | Theorem 1 |
| lock sets `S_*(A)`, `S_*(B)`, `S_*(C)`, `S_*(D)` | Theorem 1; `{+e_1, −e_1, +e_2, −e_2, +e_3}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}`, `{+e_1, −e_1, −e_2, +e_3}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}` |
| reverse and face | Theorems 2–3; `hold` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| probe's own incoming lock as the set | not used |
| formation member from later-tick six-neighbor locks | not attached |
| leftover of unique own-incoming letters on these z-probes | not this display |
| leftover of opposite-lock y-probe later-tick existential opposite | not this display |
| leftover of nnseed x-probe later-tick existential opposite | not this display |
| leftover of formation-time already-recorded sets | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: existential opposite of 6-NN locks at the first later tick when all four nsopp z-probes are recorded, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed later-tick existential-opposite neighbor-lock reverse/face report on these four opposite-lock z-probes. |
| V3 | Later-tick lock sets and the `hold`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads six-neighbor lock vectors at a later common tick and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not identify them with the probe's own incoming steps,
does not reduce them to named signs, does not require a singleton lock
vector, does not sum the lock set, does not reprint unique own-incoming
letters, does not reprint opposite-lock y-probe later-tick leftover, does
not reprint nnseed x-probe later-tick leftover, and does not use occupancy
`n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same neighbor locks | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while both pairs of sets are nonempty |
| sum of the same neighbor locks | replace `S_*` by the `Z^3` sum | refused; leftover; sum of `S_*(A)` and of `S_*(B)` is `+e_3` and `+e_1` and would fail reverse while `−e_1+(+e_1)=0`; sum of `S_*(C)` and of `S_*(D)` is `(0,−1,1)` and `+e_1` and would fail face |
| named-sign lettering of the same neighbor locks | map `±e_i` to `{+,−}` | refused; lost the axis; mixed `{+,−}` at `A` and at `B` would hide `−e_1+(+e_1)=0` |
| identify lock sets with the probe's own incoming `{±e_i}` | map `A`'s incoming `+e_3` onto `S_*(A)` | refused; `S_*(A)` is not `{+e_3}`; `S_*(A)={+e_1, −e_1, +e_2, −e_2, +e_3}` |
| unique own-incoming lock-vector leftover on these z-probes | reuse `L(A)=+e_3`, `L(B)=+e_1`, `L(C)=UNDEFINED`, `L(D)=+e_1` | refused; different object; that leftover reports reverse fail and face `UNDEFINED` while later-tick `S_*(C)` is nonempty and reverse and face hold |
| leftover of opposite-lock y-probe later-tick existential opposite | reuse y-probe lists at `T=3` | refused; cubic-frame transfer of the holding readout, not leftover of those lists; `T=4` and `S_*(A)`, `S_*(C)` differ |
| leftover of nnseed x-probe later-tick existential opposite | reuse seed `+e_1/+e_2` and x-probes with reverse fail | refused; different process and different frame; reverse holds here |
| leftover of formation-time already-recorded sets | reuse `{+e_1}` at `A` and `{+e_3}` at `B` with reverse fail | refused; different set; later-tick reverse holds |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| attach a formation member from later-tick six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; all three earliest incoming steps at `C` are kept |

### N2 — wall independence

Missing physical adoption, missing formation attachment from later-tick
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, later-tick lock set of six-neighbors formed by the
first `T` at which all four z-probes are recorded, existential opposite, four
z-probes with non-seed `A`, and reverse/face as existence of a pair that sums
to zero are declared. No uniqueness of incoming locks, no occupancy `n`, no
named-sign reduction, no singleton leftover, no sum leftover, no unique
own-incoming leftover, no opposite-lock y-probe leftover, no nnseed x-probe
leftover, no formation attachment from later-tick six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in a later-tick set | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four lock sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Once a six-neighbor exists at the later common tick, the site
should lock that unique vector as incoming content, mixed neighbor locks
should make reverse and face `UNDEFINED`, the sets should be replaced by
their sums, unique own-incoming letters already answered reverse fail with
face `UNDEFINED`, opposite-lock y-probe later-tick existential opposite
already answered the later-tick question with the same lists, named signs
should suffice because they keep orientation, and occupancy `n` should track
that vector.

**Answer:** The named construction reports lock sets
`{+e_1, −e_1, +e_2, −e_2, +e_3}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}`,
`{+e_1, −e_1, −e_2, +e_3}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}` at
`A,B,C,D` from later-tick six-neighbor locks at `T=4`. Mixed remains a set.
The construction does not sum. Occupancy `n` is not used. Named signs lost
the axis. Some pair from `S_*(A)` and `S_*(B)` is opposite, so reverse holds.
Face holds. The sets are not leftover of unique own-incoming letters and not
leftover of opposite-lock y-probe later-tick lists. The bits remain
displayed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same opposite-lock
z-probes assigned `L(A)=+e_3`, `L(B)=+e_1`, `L(C)=UNDEFINED`, `L(D)=+e_1` and
reported reverse fail with face `UNDEFINED`. A unique already-recorded
six-neighbor lock-vector display on formation-time neighbors assigned
`{+e_1}` at `A` and `{+e_3}` at `B` and reported reverse fail with face fail.
Later-tick existential opposite on the opposite-lock y-probes reported
reverse hold and face hold on different sets
`{+e_1, +e_2, −e_2, +e_3, −e_3}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}`,
`{+e_1, −e_1, +e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_2, +e_3, −e_3}` at
`T=3`. Later-tick existential opposite on the nnseed x-probes reported
reverse fail and face hold on different sets `{+e_1}`, `{+e_1, +e_2, +e_3}`,
`{−e_2}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}`. Unique lock-vector lettering of
the later-tick lists would report reverse `UNDEFINED` and face `UNDEFINED`
because every later-tick set mixes. A sum leftover of the same lists would
report reverse fail and face fail because the sums are `+e_3` and `+e_1`.
This note is not those displays: mixed remains a set, the construction does
not sum, `−e_1+(+e_1)=(0,0,0)` so reverse holds, and `−e_1+(+e_1)=(0,0,0)`
so face holds.

**Gate disposition:** PASS for the later-tick six-neighbor-lock
existential-opposite reverse/face reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique singleton
lock vector,” “the predicate equals the sum of the lock set,” “the lock set
equals the probe's own incoming step,” “bits are Admissibility,” “the letter
is occupancy `n`,” “the sets equal unique own-incoming letters,” “the sets
equal opposite-lock y-probe later-tick leftover,” “the sets equal nnseed
x-probe later-tick leftover,” “reverse fails,” or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the opposite-lock two-site
perp-step incoming-lock process, takes `T` as the first tick at which all four
z-probes are recorded, collects six-neighbor locks formed by `T` at each
probe with the probe excluded, reads the lock sets at the four z-probes, and
checks Theorems 1--3. It also checks that the construction is not named-sign
lettering, that mixed sets remain defined, that the construction does not
sum, that the probe's own incoming step is not the lock set, that occupancy
`n` is not used, that a formation member from later-tick six-neighbor locks
is not attached, that the sets are not leftover of unique own-incoming
letters, that the sets are not leftover of opposite-lock y-probe later-tick
existential opposite, and that the sets are not leftover of nnseed x-probe
later-tick existential opposite. No runner cache is written.
