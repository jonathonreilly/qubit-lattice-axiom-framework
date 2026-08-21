---
claim_id: opposite_lock_xprobe_formation_tick_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from existential opposite 6-NN locks at each nsopp x-probe's own formation tick (no global later T) are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_xprobe_formation_tick_existential_opposite_reverse_face_2026_08_15.py
---

# Formation-Tick Existential Opposite Neighbor-Lock Reverse And Face On Four Opposite-Lock X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from existential opposite six-neighbor locks at
each opposite-lock x-probe's own formation tick in `B_3(0)`. There is no
global later tick `T`. Let `t(q)` be the formation tick of probe `q`. At
that tick, `S(q)` is the set of locks of six-neighbors of `q` that formed
at tick `< t(q)` (strictly earlier; `q` excluded). Reverse holds if and
only if some lock in `S(A)` is the vector opposite of some lock in `S(B)`.
Face holds if and only if some lock in `S(C)` is the vector opposite of
some lock in `S(D)`. Empty `S` on either side of a comparison is
`UNDEFINED`; nonempty with no opposite pair fails. Occupancy `n` is not
used. The probe's own incoming lock is not used. This is not named-sign
lettering. This is not a unique lock-vector leftover and not a sum leftover.
This is not leftover of later-tick existential opposite on these same
opposite-lock x-probes: that display waits for a global `T` and reports
reverse hold and face hold on different lists. This is not leftover of
formation-time existential opposite on the nnseed x-probes: that display
uses the perp two-site seed `+e_1/+e_2` and reports reverse fail with face
hold. Uniqueness of incoming locks is not required. Uniqueness of the lock
set is not required. Displayed, not adopted. This note does not write
existential opposite into Admissibility and does not attach a formation
member from already-recorded six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_xprobe_formation_tick_existential_opposite_reverse_face_2026_08_15.py`](../scripts/opposite_lock_xprobe_formation_tick_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
formation-tick six-neighbor lock sets. Named signs `{+,−}` are a coarser
readout and are not used. A singleton unique lock-vector letter is a
different readout and is not used. A `Z^3` sum of those locks is a different
readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of formation-tick six-neighbor lock sets on the four opposite-lock x-probes at each probe's own formation tick, with reverse fail and face fail from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_xprobe_formation_tick_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from existential opposite 6-NN locks at each nsopp x-probe's own formation tick, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with the probe's own incoming step, do not wait for a global later T, and do not identify the sets with later-tick leftover or nnseed formation-time leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of formation-tick six-neighbor locks on the four opposite-lock x-probes; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose
formation-tick six-neighbor lock sets are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. `A` is not a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`. This seed is not the perp
two-site seed `+e_1/+e_2`. From a recorded site `p` with lock
`L_in(p)=±e_i`, a six-neighbor step `s in NN` to `q=p+s` is allowed if and
only if `s` is perpendicular to `e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept as a
possible lock. Uniqueness is not required. A later parent does not re-form
`q`.

That incoming lock is not a member of `S(q)` scored below unless it appears
as a lock of some six-neighbor of `q` that formed strictly earlier.

## Named existential opposite from formation-tick six-neighbor locks

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. There is no global later tick. Reverse and face are scored at each
probe's own `t(q)`, not at a common `T`.

At the formation tick of probe `q`, let `S(q)` be the set of locks of
six-neighbors of `q` that formed at tick `< t(q)`. Same-tick and later
neighbors do not count. The probe itself is excluded. This display does not
use occupancy `n`. It does not use the probe's own incoming lock. Duplicate
locks at two neighbors collapse in the set. The construction does not
require `S(q)` to be a singleton. It does not sum `S(q)`. It is not a unique
lock-vector leftover and not a sum leftover. It is not leftover of
later-tick existential opposite on these same opposite-lock x-probes. It is
not leftover of formation-time existential opposite on the nnseed x-probes.
It is not leftover of unique own-incoming lock-vector letters on these
x-probes.

Incoming `{±e_i}` tags of the probe itself are not `S(q)`. Identifying a
named sign of those locks with reverse or face is refused: named-sign
lettering lost the axis. Reverse and face are scored on existence of a pair
of lock vectors that add to zero. They are not scored on `{+,−}` names and
are not an occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  some a in S(A) and some b in S(B) with a+b=(0,0,0)
face     <=>  some c in S(C) and some d in S(D) with c+d=(0,0,0)
```

If `S(A)` or `S(B)` is empty, reverse is `UNDEFINED`. Else reverse fails
if no such pair exists. If `S(C)` or `S(D)` is empty, face is
`UNDEFINED`. Else face fails if no such pair exists. The report is one of
`hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility.

## Theorem 1 — formation ticks and lock sets at each x-probe

Direct enumeration of the displayed opposite-lock process on `B_3(0)` forms
all four x-probes. The formation ticks are `t(A)=3`, `t(B)=2`, `t(C)=4`,
`t(D)=3`. `A` is not a seed. The four ticks are not a single global `T`.

At each probe's own formation tick the already-recorded six-neighbor lock
lists and lock sets are:

```text
A: +e_1 at (0, 0, 0), +e_1 at (1, -1, 0), +e_1 at (1, 0, 1),
   +e_1 at (1, 0, -1);
   t(A)=3;  S(A) = {+e_1}
B: +e_3 at (0, 1, 1);
   t(B)=2;  S(B) = {+e_3}
C: −e_3 at (1, 0, 0), +e_3 at (1, 0, 0), +e_2 at (1, 0, 0);
   t(C)=4;  S(C) = {+e_2, +e_3, −e_3}
D: −e_1 at (0, 1, 0), +e_1 at (1, 2, 0), +e_1 at (1, 1, 1),
   +e_1 at (1, 1, -1);
   t(D)=3;  S(D) = {+e_1, −e_1}
```

`A`'s already-recorded neighbors are the seed origin and three copies of
`+e_1`. Same-tick `D` and later `C` are excluded. `A`'s incoming set
`{−e_3, +e_3, +e_2}` is not `S(A)`: those three steps are incoming at `A`
and are not in `S(A)`, while `+e_1` is in `S(A)` and is not incoming at `A`.
`D` forms at the same tick as `A`, so `A` is not in `S(D)`. Mixed
remains a set at `C` and at `D`.

Incoming locks exist and need not be unique (`A` has three earliest incoming
steps `−e_3`, `+e_3`, and `+e_2`; `D` has three earliest incoming steps
`−e_2`, `−e_3`, and `+e_3`). That non-uniqueness is not a unique-lettering
of already-recorded neighbor lock vectors. The lock sets are not identified
with those incoming steps. Uniqueness is not required.

The unique own-incoming letters on these x-probes are `UNDEFINED`, `+e_1`,
`+e_1`, `UNDEFINED`. Those are different objects: `S(A)` is `{+e_1}` and is
not `{−e_3, +e_3, +e_2}`. Later-tick existential opposite on these same
x-probes reports `{+e_1, −e_2, +e_3, −e_3}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}`,
`{+e_1, +e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_2, +e_3, −e_3}` at a global
`T=4`. Those lists are not these lists: `S(A)` here is a singleton `{+e_1}`,
and `S(D)` here has no `+e_2`. Formation-time existential opposite on the
nnseed x-probes reports `{+e_1}`, `{+e_1, +e_3}`, `{−e_2}`, `{+e_2}` at a
different seed.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S(A)` and `b` in `S(B)`
with `a+b=(0,0,0)`. Both sets are nonempty: `S(A)={+e_1}` and
`S(B)={+e_3}`. The only pair is `+e_1+(+e_3)=(1,0,1)`. No pair is
opposite. Reverse fails.

Reverse: fail

This is not `hold` and not `UNDEFINED`. Unique lock-vector lettering of the
same lists would assign `L(A)=+e_1` and `L(B)=+e_3` and would also fail
reverse, for a different reason: that readout requires a singleton. A sum
leftover of the same lists would replace the sets by `+e_1` and `+e_3` and
would report reverse fail for a different reason. A named-sign readout of
the same neighbor locks would assign `+` and `+` at `A` and `B` and would
report reverse fail for a different reason. Unique own-incoming letters on
these x-probes report reverse `UNDEFINED` from mixed `A`. Later-tick
existential opposite on these same x-probes reports reverse hold on
different lists that wait for a global `T=4`. Formation-time existential
opposite on the nnseed x-probes also reports reverse fail, but from
different sets `{+e_1}` and `{+e_1, +e_3}`. Holding reverse on this process
needs the later tick.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S(C)` and `d` in `S(D)`
with `c+d=(0,0,0)`. Both sets are nonempty: `S(C)={+e_2, +e_3, −e_3}` and
`S(D)={+e_1, −e_1}`. The pairs are `+e_2+(+e_1)`, `+e_2+(−e_1)`,
`+e_3+(+e_1)`, `+e_3+(−e_1)`, `−e_3+(+e_1)`, and `−e_3+(−e_1)`. No pair
is opposite. Face fails.

Face: fail

Displayed, not adopted. The bits are not written into Admissibility.

This is not `hold` and not `UNDEFINED`. Unique lock-vector lettering of the
same lists would report face `UNDEFINED` because both `C` and `D` mix.
Existential opposite keeps the mixed sets and fails. A sum leftover of the
same lists would replace `S(C)` by `+e_2` and `S(D)` by the origin; that
origin is not an existential pair from `S(C)` and `S(D)`. Named-sign
lettering lost the axis in mixed `{+,−}` at `C` and at `D`. Unique
own-incoming letters on these same x-probes assign `L(D)=UNDEFINED` from
three earliest incoming steps and report face `UNDEFINED`. Later-tick
existential opposite on these same x-probes reports face hold at global
`T=4` because same-tick `A` then counts as a neighbor of `D` and supplies
`±e_3` against the later-tick set at `C`. Formation-time existential
opposite on the nnseed x-probes reports face hold on `{−e_2}` and `{+e_2}`.
Holding face on this opposite-lock process needs the later tick.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify lock sets with the probe's own incoming `{±e_i}`.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the formation-tick lock set to be a singleton.
- It does not sum the formation-tick lock set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not wait for a global later tick `T`.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  formation-tick lock vectors.
- It does not reprint unique own-incoming lock-vector letters on these
  x-probes.
- It does not reprint later-tick existential opposite on these opposite-lock
  x-probes.
- It does not reprint formation-time existential opposite on the nnseed
  x-probes.
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
opposite-lock process, the formation-tick six-neighbor lock sets, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; opposite-lock two-site seed `+e_1/−e_1` |
| formation ticks and six-neighbor lock sets at each x-probe's own tick | Theorem 1 |
| lock sets `S(A)`, `S(B)`, `S(C)`, `S(D)` | Theorem 1; `{+e_1}`, `{+e_3}`, `{+e_2, +e_3, −e_3}`, `{+e_1, −e_1}` |
| reverse and face | Theorems 2–3; `fail` / `fail` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| probe's own incoming lock as the set | not used |
| global later tick `T` | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique own-incoming letters on these x-probes | not this display |
| leftover of later-tick existential opposite on these x-probes | not this display; holding needs the later tick |
| leftover of nnseed x-probe formation-time existential opposite | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: existential opposite of 6-NN locks at each nsopp x-probe's own formation tick, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed formation-tick existential-opposite neighbor-lock reverse/face report on these four opposite-lock x-probes. |
| V3 | Formation ticks, lock sets, and the `fail`/`fail` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads six-neighbor lock vectors at each probe's own formation tick and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not identify them with the probe's own incoming steps,
does not reduce them to named signs, does not require a singleton lock
vector, does not sum the lock set, does not wait for a global later tick,
does not reprint unique own-incoming letters, does not reprint later-tick
leftover on these x-probes, does not reprint nnseed formation-time leftover,
and does not use occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same neighbor locks | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse would still fail, but face would be `UNDEFINED` while both `S(C)` and `S(D)` are nonempty |
| sum of the same neighbor locks | replace `S` by the `Z^3` sum | refused; leftover; sum of `S(A)` is `+e_1` and of `S(B)` is `+e_3`; sum of `S(C)` is `+e_2` and of `S(D)` is the origin; that origin is not an existential pair |
| named-sign lettering of the same neighbor locks | map `±e_i` to `{+,−}` | refused; lost the axis; `L(A)=+` and `L(B)=+` hide that the vectors are `+e_1` and `+e_3` |
| identify lock sets with the probe's own incoming `{±e_i}` | map `A`'s incoming `{−e_3, +e_3, +e_2}` onto `S(A)` | refused; `S(A)={+e_1}`; `+e_1` is not incoming at `A` |
| unique own-incoming lock-vector leftover on these x-probes | reuse `L(A)=UNDEFINED`, `L(B)=+e_1`, `L(C)=+e_1`, `L(D)=UNDEFINED` | refused; different object; that leftover reports reverse `UNDEFINED` and face `UNDEFINED` while `S(A)` and `S(D)` are nonempty |
| leftover of later-tick existential opposite on these x-probes | reuse later-tick lists at global `T=4` | refused; different sets; later-tick reverse hold and face hold; holding needs the later tick |
| leftover of nnseed x-probe formation-time existential opposite | reuse seed `+e_1/+e_2` with reverse fail and face hold | refused; different process; face fails here |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score `3 t(A)^2 > t(B)^2` or any tick order | different object; ticks are reported, not the reverse/face predicate |
| wait for a global later tick `T` | replace each `t(q)` by `max t` | refused; this display does not wait; later-tick leftover holds both bits |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; all three earliest incoming steps at `A` and at `D` are kept |

Honesty marker for each row: `ATTEMPTED`.

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, formation-tick lock set of six-neighbors formed
strictly earlier than each x-probe's own tick, existential opposite, four
x-probes with non-seed `A`, and reverse/face as existence of a pair that sums
to zero are declared. No uniqueness of incoming locks, no occupancy `n`, no
named-sign reduction, no singleton leftover, no sum leftover, no unique
own-incoming leftover, no later-tick leftover, no nnseed leftover, no global
later `T`, no formation attachment from already-recorded six-neighbor locks,
and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in a formation-tick set | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four lock sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Mixed neighbor locks at `C` and at `D` should make face
`UNDEFINED`, the sets should be replaced by their sums, unique own-incoming
letters already answered reverse `UNDEFINED` with face `UNDEFINED`, later-tick
existential opposite on these x-probes already answered the question with
hold/hold so this is leftover, nnseed formation-time existential opposite
already answered formation-time exist with reverse fail and face hold, named
signs should suffice because they keep orientation, occupancy `n` should track
that vector, and holding should not need a later tick.

**Answer:** The named construction reports lock sets `{+e_1}`, `{+e_3}`,
`{+e_2, +e_3, −e_3}`, `{+e_1, −e_1}` at `A,B,C,D` from already-recorded
six-neighbor locks at each probe's own formation tick. Mixed remains a set.
The construction does not sum. Occupancy `n` is not used. Named signs lost
the axis. No pair from `S(A)` and `S(B)` is opposite, so reverse fails. No
pair from `S(C)` and `S(D)` is opposite, so face fails. Empty is not the
reason: both sides of each comparison are nonempty. The sets are not leftover
of unique own-incoming letters, not leftover of later-tick lists on these
x-probes, and not leftover of nnseed formation-time existential opposite.
Holding reverse and face on this process needs the later tick. The bits
remain displayed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same opposite-lock
x-probes assigned `L(A)=UNDEFINED`, `L(B)=+e_1`, `L(C)=+e_1`,
`L(D)=UNDEFINED` and reported reverse `UNDEFINED` with face `UNDEFINED`. A
unique already-recorded six-neighbor lock-vector display on these x-probes
assigned `{+e_1}` at `A` and `{+e_3}` at `B` and reported reverse fail with
face `UNDEFINED`. Later-tick existential opposite on these same x-probes
reported reverse hold and face hold on different sets
`{+e_1, −e_2, +e_3, −e_3}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}`,
`{+e_1, +e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_2, +e_3, −e_3}` at
`T=4`. Formation-time existential opposite on the nnseed x-probes reported
reverse fail and face hold on different sets `{+e_1}`, `{+e_1, +e_3}`,
`{−e_2}`, `{+e_2}`. Unique lock-vector lettering of the formation-tick lists
would report reverse fail and face `UNDEFINED` because `S(C)` and `S(D)` mix.
A sum leftover of the same lists would replace `S(D)` by the origin. This
note is not those displays: mixed remains a set, the construction does not
sum, `+e_1+(+e_3)≠(0,0,0)` so reverse fails, and no pair from `S(C)` and
`S(D)` is opposite so face fails. Holding both bits needs the later tick; the
lists are not leftover of that later-tick display.

**Gate disposition:** PASS for the formation-tick six-neighbor-lock
existential-opposite reverse/face reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique singleton
lock vector,” “the predicate equals the sum of the lock set,” “the lock set
equals the probe's own incoming step,” “bits are Admissibility,” “the letter
is occupancy `n`,” “the sets equal unique own-incoming letters,” “the sets
equal later-tick leftover on these x-probes,” “the sets equal nnseed
formation-time leftover,” “reverse holds,” or “face holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the opposite-lock two-site
perp-step incoming-lock process, collects six-neighbor locks formed strictly
earlier than each x-probe's own formation tick with the probe excluded, reads
the lock sets at the four x-probes, and checks Theorems 1--3. It also checks
that the construction is not named-sign lettering, that mixed sets remain
defined, that the construction does not sum, that the probe's own incoming
step is not the lock set, that occupancy `n` is not used, that a formation
member from already-recorded six-neighbor locks is not attached, that the
sets are not leftover of unique own-incoming letters, that the sets are not
leftover of later-tick existential opposite on these x-probes, that the sets
are not leftover of nnseed x-probe formation-time existential opposite, and
that reverse and face are not scored at a global later tick. No runner cache
is written.
