---
claim_id: perpnn_xprobe_later_tick_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from existential opposite 6-NN locks at the first later tick when all four perpnn x-probes are recorded are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/perpnn_xprobe_later_tick_existential_opposite_reverse_face_2026_08_15.py
---

# Later-Tick Existential Opposite Neighbor-Lock Reverse And Face On Four Perpnn X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from existential opposite six-neighbor locks at
the first later tick in `B_3(0)` at which all four perpnn x-probes are
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
This is a 1-seed transfer of later-tick existential opposite, not leftover
of perpnn formation-tick reverse/face at `k=1`: those inequalities hold,
while later-tick reverse fails. This is not leftover of two-site or
three-site later-tick existential opposite: those displays hold reverse and
hold face on different seeds. This is not leftover of formation-tick
existential opposite on opposite-lock y-probes: that readout has empty
`S(A)` at the seed and reports reverse `UNDEFINED`. Uniqueness of incoming
locks is not required. Uniqueness of the lock set is not required.
Displayed, not adopted. This note does not write existential opposite into
Admissibility and does not attach a formation member from later-tick
six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/perpnn_xprobe_later_tick_existential_opposite_reverse_face_2026_08_15.py`](../scripts/perpnn_xprobe_later_tick_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
later-tick six-neighbor lock sets. Named signs `{+,−}` are a coarser readout
and are not used. A singleton unique lock-vector letter is a different
readout and is not used. A `Z^3` sum of those locks is a different readout
and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of later-tick six-neighbor lock sets on the four perpnn x-probes at the first T with all four recorded, with reverse fail and face hold from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: perpnn_xprobe_later_tick_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from existential opposite 6-NN locks at the first later tick when all four perpnn x-probes are recorded, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with the probe's own incoming step, and do not identify the bits with perpnn formation-tick inequalities."
conditional_surface_status: "exact on B_3(0) for existential opposite of later-tick six-neighbor locks on the four perpnn x-probes; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose later-tick
six-neighbor lock sets are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are the same x-probes as the opposite-lock two-site display. They are
not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)`. `A` is
not a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the origin is recorded at tick `0` with lock letter `+e_1`. This is
the perpnn 1-seed. It is not the two-site opposite-lock seed
`{0,(0,1,0)}` with `+e_1/−e_1`, not the perp two-site seed `+e_1/+e_2`, and
not the three-site seed `{0,(0,1,0),(1,0,0)}`.

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

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `T` be the maximum of those four ticks. This `T` is the first
tick in `B_3(0)` at which all four x-probes are recorded.

At tick `T`, for each probe `q`, let `S_*(q)` be the set of locks of
six-neighbors of `q` that formed at tick `≤ T` and are not `q`. Same-tick
and later-than-formation neighbors count whenever they have formed by `T`.
The probe itself is excluded. This display does not use occupancy `n`. It
does not use the probe's own incoming lock. Duplicate locks at two neighbors
collapse in the set. The construction does not require `S_*(q)` to be a
singleton. It does not sum `S_*(q)`. It is not a unique lock-vector leftover
and not a sum leftover. It is a 1-seed transfer of later-tick existential
opposite, not leftover of perpnn formation-tick reverse/face at `k=1`. It is
not leftover of two-site or three-site later-tick existential opposite. It
is not leftover of formation-tick existential opposite on opposite-lock
y-probes. It is not leftover of nnseed later-tick lists: that display uses
the perp two-site seed and has `S_*(C)={−e_2}`.

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

## Theorem 1 — later-tick lock sets at each x-probe

Direct enumeration of the displayed perpnn 1-seed process on `B_3(0)` forms
all four x-probes. The formation ticks are `t(A)=3`, `t(B)=3`, `t(C)=4`,
`t(D)=2`. `A` is not a seed. All four are defined in `B_3(0)`, so

```text
T = max{t(A), t(B), t(C), t(D)} = 4.
```

At tick `T=4` the six-neighbor lock lists and lock sets are:

```text
A: +e_1 at (2, 0, 0), +e_1 at (0, 0, 0), +e_1 at (1, 1, 0),
   +e_1 at (1, -1, 0), +e_1 at (1, 0, 1), +e_1 at (1, 0, -1);
   S_*(A) = {+e_1}
B: +e_1 at (2, 1, 1), +e_3 at (0, 1, 1), +e_2 at (0, 1, 1),
   +e_3 at (1, 2, 1), +e_2 at (1, 2, 1), +e_1 at (1, 2, 1),
   +e_1 at (1, 0, 1), +e_3 at (1, 1, 2), +e_2 at (1, 1, 2),
   +e_1 at (1, 1, 2), +e_1 at (1, 1, 0);
   S_*(B) = {+e_1, +e_2, +e_3}
C: −e_2 at (1, 0, 0), −e_3 at (1, 0, 0), +e_3 at (1, 0, 0),
   +e_2 at (1, 0, 0);
   S_*(C) = {+e_2, −e_2, +e_3, −e_3}
D: +e_2 at (0, 1, 0), +e_2 at (1, 2, 0), −e_2 at (1, 0, 0),
   −e_3 at (1, 0, 0), +e_3 at (1, 0, 0), +e_2 at (1, 0, 0),
   +e_3 at (1, 1, 1), +e_2 at (1, 1, 1), +e_1 at (1, 1, 1),
   −e_3 at (1, 1, -1), +e_2 at (1, 1, -1), +e_1 at (1, 1, -1);
   S_*(D) = {+e_1, +e_2, −e_2, +e_3, −e_3}
```

`A`'s later-tick neighbors include the seed origin locking `+e_1` and later
`C` locking `+e_1`. `A`'s incoming set `{−e_2, +e_2, −e_3, +e_3}` is not
`S_*(A)`: those four incoming steps at `A` are absent from `S_*(A)`, while
`+e_1` is in `S_*(A)` and is not incoming at `A`. `C`'s later-tick neighbors
are only `A`, with mixed locks `{+e_2, −e_2, +e_3, −e_3}`. That set is not
the nnseed later-tick singleton `{−e_2}`. Mixed remains a set.

Incoming locks exist and need not be unique (`A` has four earliest incoming
steps `±e_2` and `±e_3`; `B` has three earliest incoming steps `+e_1`,
`+e_2`, and `+e_3`). That non-uniqueness is not a unique-lettering of
later-tick neighbor lock vectors. The lock sets are not identified with
those incoming steps. Uniqueness is not required.

The unique own-incoming letters on these x-probes are `UNDEFINED`,
`UNDEFINED`, `+e_1`, `+e_1`. Those are different objects: `S_*(A)` is
nonempty and is not `{−e_2, +e_2, −e_3, +e_3}`. Formation-time
already-recorded neighbor locks at `A,B,C,D` are `{+e_1}`,
`{+e_1, +e_2, +e_3}`, `{+e_2, −e_2, +e_3, −e_3}`, `{+e_2}`. Those are
different lists: later-tick `S_*(D)` is mixed and is not `{+e_2}`.

The same four ticks `t(A)=3`, `t(B)=3`, `t(C)=4`, `t(D)=2` are the perpnn
`k=1` formation ticks. Direct integer arithmetic on those ticks gives
`3 t(A)^2 = 27 > 9 = t(B)^2` and `t(C)^2 = 16 > 8 = 2 t(D)^2`, so tick
reverse and tick face hold. Those inequalities are a different readout.
This display scores later-tick lock vectors, not those inequalities.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S_*(A)` and `b` in `S_*(B)`
with `a+b=(0,0,0)`. Both sets are nonempty: `S_*(A)={+e_1}` and
`S_*(B)={+e_1, +e_2, +e_3}`. The pairs are `+e_1++e_1=(2,0,0)`,
`+e_1++e_2=(1,1,0)`, and `+e_1++e_3=(1,0,1)`. No pair is opposite. Reverse
fails.

Reverse: fail

This is not `hold` and not `UNDEFINED`. Unique lock-vector lettering of the
same lists would assign mixed `S_*(B)` and would report reverse
`UNDEFINED`. That readout is a different object and is not used. A sum
leftover of the same lists would replace the sets by `+e_1` and `(1,1,1)`
and would report reverse fail for a different reason. A named-sign readout
of the same neighbor locks would assign `+` and `+` at `A` and `B` and
would report reverse fail for a different reason. Perpnn formation-tick
reverse at `k=1` holds from `3 t(A)^2 > t(B)^2`. That leftover is a
different object: later-tick reverse fails. Two-site and three-site
later-tick existential opposite hold reverse on different seeds. Formation-
tick existential opposite on opposite-lock y-probes reports reverse
`UNDEFINED` from empty `S(A)` at the seed. Unique own-incoming letters on
these x-probes report reverse `UNDEFINED` from mixed `A`.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S_*(C)` and `d` in `S_*(D)`
with `c+d=(0,0,0)`. Both sets are nonempty:
`S_*(C)={+e_2, −e_2, +e_3, −e_3}` and
`S_*(D)={+e_1, +e_2, −e_2, +e_3, −e_3}`, so `−e_2+(+e_2)=(0,0,0)` and
`+e_3+(−e_3)=(0,0,0)`. Face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.

This is not `fail` and not `UNDEFINED`. Unique lock-vector lettering of the
later-tick lists would report face `UNDEFINED` because both `C` and `D`
mix. A sum leftover would replace the sets by `(0,0,0)` and `+e_1` and
would fail face, while existential opposite holds. Named-sign lettering
lost the axis in mixed `{+,−}` at `C` and at `D`. Unique own-incoming
letters assign `L(C)=+e_1` and `L(D)=+e_1` and would fail face. Formation-
time already-recorded locks at `D` are `{+e_2}` against mixed `C`, so that
leftover also holds face from different lists. Nnseed later-tick
existential opposite holds face from `S_*(C)={−e_2}`, a different set.
Perpnn formation-tick face at `k=1` also holds, from `t(C)^2 > 2 t(D)^2`,
a different readout.

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
  x-probes.
- It does not reprint perpnn formation-tick reverse/face inequalities.
- It does not reprint two-site or three-site later-tick existential
  opposite lists.
- It does not reprint nnseed later-tick existential opposite lists.
- It does not reprint formation-tick existential opposite on opposite-lock
  y-probes.
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

This display uses Lattice to name `B_3(0)` and the four x-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
perpnn 1-seed process, the later-tick six-neighbor lock sets, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; 1-seed origin lock `+e_1` |
| later-tick six-neighbor lock sets at first `T` with all four x-probes recorded | Theorem 1 |
| lock sets `S_*(A)`, `S_*(B)`, `S_*(C)`, `S_*(D)` | Theorem 1; `{+e_1}`, `{+e_1, +e_2, +e_3}`, `{+e_2, −e_2, +e_3, −e_3}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}` |
| reverse and face | Theorems 2–3; `fail` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| probe's own incoming lock as the set | not used |
| formation member from later-tick six-neighbor locks | not attached |
| leftover of perpnn formation-tick reverse/face at `k=1` | not this display; those inequalities hold |
| leftover of two-site later-tick existential opposite | not this display; that readout holds reverse |
| leftover of three-site later-tick existential opposite | not this display; that readout holds reverse |
| leftover of nnseed later-tick existential opposite | not this display; `S_*(C)` there is `{−e_2}` |
| leftover of formation-tick existential opposite on opposite-lock y-probes | not this display; empty `S(A)` at the seed is reverse `UNDEFINED` |
| leftover of unique own-incoming letters on these x-probes | not this display |
| leftover of formation-time already-recorded sets | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: existential opposite of 6-NN locks at the first later tick when all four perpnn x-probes are recorded, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed later-tick existential-opposite neighbor-lock reverse/face report on these four perpnn x-probes. |
| V3 | Later-tick lock sets and the `fail`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads six-neighbor lock vectors at a later common tick and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not identify them with the probe's own incoming steps,
does not reduce them to named signs, does not require a singleton lock
vector, does not sum the lock set, does not reprint perpnn formation-tick
inequalities, does not reprint two-site or three-site later-tick leftover,
does not reprint nnseed later-tick leftover, does not reprint opposite-lock
y-probe formation-tick leftover, and does not use occupancy `n`. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same neighbor locks | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while both pairs of sets are nonempty |
| sum of the same neighbor locks | replace `S_*` by the `Z^3` sum | refused; leftover; sum of `S_*(C)` is `(0,0,0)` and of `S_*(D)` is `+e_1` and would fail face while `−e_2+(+e_2)=0` |
| named-sign lettering of the same neighbor locks | map `±e_i` to `{+,−}` | refused; lost the axis; mixed `{+,−}` at `C` and at `D` would hide `−e_2+(+e_2)=0` |
| identify lock sets with the probe's own incoming `{±e_i}` | map `A`'s incoming `{−e_2, +e_2, −e_3, +e_3}` onto `S_*(A)` | refused; `S_*(A)={+e_1}` from later-tick neighbor locks |
| unique own-incoming lock-vector leftover on these x-probes | reuse `L(A)=UNDEFINED`, `L(B)=UNDEFINED`, `L(C)=+e_1`, `L(D)=+e_1` | refused; different object; that leftover reports reverse `UNDEFINED` and face fail while later-tick `S_*(A)` is nonempty and face holds |
| leftover of perpnn formation-tick reverse/face at `k=1` | reuse `3 t(A)^2 > t(B)^2` and `t(C)^2 > 2 t(D)^2` | refused; different readout; those inequalities hold while later-tick reverse fails |
| leftover of two-site later-tick existential opposite | reuse opposite-lock seed `{0,(0,1,0)}` with reverse hold | refused; different process; reverse fails here |
| leftover of three-site later-tick existential opposite | reuse three-site seed with reverse hold | refused; different process; reverse fails here |
| leftover of nnseed later-tick existential opposite | reuse seed `+e_1/+e_2` and `S_*(C)={−e_2}` | refused; different process; `S_*(C)` here mixes `{+e_2, −e_2, +e_3, −e_3}` |
| leftover of formation-tick existential opposite on opposite-lock y-probes | reuse empty `S(A)` at the seed with reverse `UNDEFINED` | refused; different readout and different probes; `S_*(A)` here is `{+e_1}` and reverse fails |
| leftover of formation-time already-recorded sets | reuse `{+e_2}` at `D` | refused; different set; later-tick `S_*(D)` mixes |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| attach a formation member from later-tick six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; all four earliest incoming steps at `A` are kept |

### N2 — wall independence

Missing physical adoption, missing formation attachment from later-tick
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, 1-seed origin lock `+e_1`, perpendicular step rule,
incoming-step lock, later-tick lock set of six-neighbors formed by the first
`T` at which all four x-probes are recorded, existential opposite, four
x-probes with non-seed `A`, and reverse/face as existence of a pair that sums
to zero are declared. No uniqueness of incoming locks, no occupancy `n`, no
named-sign reduction, no singleton leftover, no sum leftover, no perpnn
formation-tick leftover, no two-site leftover, no three-site leftover, no
nnseed leftover, no opposite-lock y-probe formation-tick leftover, no
formation attachment from later-tick six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in a later-tick set | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
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
their sums, reverse and face should both hold because the same ticks already
hold the `k=1` inequalities, two-site and three-site later-tick existential
opposite already answered the later-tick question with hold/hold, nnseed
later-tick already answered the 1-seed-adjacent x-probe question, named
signs should suffice because they keep orientation, and occupancy `n`
should track that vector.

**Answer:** The named construction reports lock sets `{+e_1}`,
`{+e_1, +e_2, +e_3}`, `{+e_2, −e_2, +e_3, −e_3}`,
`{+e_1, +e_2, −e_2, +e_3, −e_3}` at `A,B,C,D` from later-tick six-neighbor
locks at `T=4`. Mixed remains a set. The construction does not sum.
Occupancy `n` is not used. Named signs lost the axis. No pair from
`S_*(A)` and `S_*(B)` is opposite, so reverse fails. Face holds. The bits
are not leftover of perpnn formation-tick reverse/face at `k=1`. The sets
are not leftover of two-site or three-site later-tick lists and not leftover
of nnseed later-tick lists. This is a 1-seed transfer of later-tick
existential opposite, not leftover of those ticks. The bits remain
displayed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A perpnn formation-tick reverse/face display at `k=1` on these same four
x-probes reported both inequalities hold from `t(A)=3`, `t(B)=3`,
`t(C)=4`, `t(D)=2`. Later-tick existential opposite on two-site and
three-site seeds reported reverse hold and face hold. Later-tick
existential opposite on the nnseed x-probes reported reverse fail and face
hold on different sets `{+e_1}`, `{+e_1, +e_2, +e_3}`, `{−e_2}`,
`{+e_1, +e_2, −e_2, +e_3, −e_3}`. Formation-tick existential opposite on
opposite-lock y-probes reported reverse `UNDEFINED` from empty `S(A)` at
the seed. Unique own-incoming lock-vector letters on these x-probes assign
`UNDEFINED`, `UNDEFINED`, `+e_1`, `+e_1` and report reverse `UNDEFINED`
with face fail. Unique lock-vector lettering of the later-tick lists would
report reverse `UNDEFINED` and face `UNDEFINED` because `B`, `C`, and `D`
mix. A sum leftover of the same lists would report face fail because the
sums are `(0,0,0)` and `+e_1`. This note is not those displays: mixed
remains a set, the construction does not sum, no pair from `S_*(A)` and
`S_*(B)` is opposite, reverse fails, and `−e_2+(+e_2)=(0,0,0)` so face
holds. This is a 1-seed transfer of later-tick existential opposite, not
leftover of the formation-tick inequalities.

**Gate disposition:** PASS for the later-tick six-neighbor-lock
existential-opposite reverse/face reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique singleton
lock vector,” “the predicate equals the sum of the lock set,” “the lock set
equals the probe's own incoming step,” “bits are Admissibility,” “the letter
is occupancy `n`,” “the bits equal perpnn formation-tick reverse/face,” “the
sets equal two-site later-tick leftover,” “the sets equal three-site
later-tick leftover,” “the sets equal nnseed later-tick leftover,” “reverse
holds,” or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the perpnn 1-seed
perp-step incoming-lock process, takes `T` as the first tick at which all
four x-probes are recorded, collects six-neighbor locks formed by `T` at
each probe with the probe excluded, reads the lock sets at the four
x-probes, and checks Theorems 1--3. It also checks that the construction is
not named-sign lettering, that mixed sets remain defined, that the
construction does not sum, that the probe's own incoming step is not the
lock set, that occupancy `n` is not used, that a formation member from
later-tick six-neighbor locks is not attached, that the bits are not leftover
of perpnn formation-tick reverse/face at `k=1`, that the sets are not
leftover of two-site or three-site later-tick existential opposite, and that
the sets are not leftover of nnseed later-tick existential opposite. No
runner cache is written.
