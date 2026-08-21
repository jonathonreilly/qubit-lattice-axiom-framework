---
claim_id: opposite_lock_xprobe_sametick_union_own_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from same-tick-inclusive 6-NN locks union own incoming lock on the four nsopp x-probes, no global T, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_xprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py
---

# Same-Tick-Inclusive Neighbor-Lock Union Own Incoming Lock Reverse And Face On Four Opposite-Lock X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from same-tick-inclusive 6-NN locks union
own incoming lock on the four nsopp x-probes, no global T, in `B_3(0)`.
Let `t(q)` be the formation tick of probe `q`. Let `L(q)` be `q`'s own
unique incoming lock; seeds use seed letters. If several earliest incoming
steps exist, `L(q)` is `UNDEFINED`. At `t(q)`, `S^+(q)` is the set of locks
of six-neighbors of `q` that formed at tick `≤ t(q)` and are not `q`, union
`{L(q)}` when `L(q)` is defined. There is no global later T. Reverse holds
if and only if some lock in `S^+(A)` is the vector opposite of some lock in
`S^+(B)`. Face holds if and only if some lock in `S^+(C)` is the vector
opposite of some lock in `S^+(D)`. Empty `S^+` on either side of a
comparison is `UNDEFINED`; nonempty with no opposite pair fails. Occupancy
`n` is not used. This is not named-sign lettering. This is not a unique
lock-vector leftover and not a sum leftover. This is a cubic-frame transfer
of same-tick-inclusive six-neighbor locks union own incoming lock, not leftover of later-tick S_* union own lock
on these x-probes: that display waits for a global T equal to the max of the
four formation ticks and enlarges `S^+(B)`. This is not leftover of
own-lock-in existential opposite at formation: that display takes tick
`< t(q)` and reports reverse fail and face hold. This is not leftover of same-tick-inclusive 6-NN locks union own incoming lock on the opposite-lock
y-probe frame: that display uses seed letter `−e_1` at `A=(0,1,0)` and
reverse hold uses `L(A)`. Uniqueness of incoming locks is not required.
Uniqueness of the lock set is not required. Displayed, not adopted. This
note does not write existential opposite into Admissibility and does not
attach a formation member from same-tick-inclusive six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_xprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py`](../scripts/opposite_lock_xprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
same-tick-inclusive six-neighbor lock sets union `{L(q)}` when defined.
Named signs `{+,−}` are a coarser readout and are not used. A singleton
unique lock-vector letter is a different readout and is not used. A `Z^3`
sum of those locks is a different readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of t, L, and S^+ as same-tick-inclusive six-neighbor locks union L(q) when defined, on the four nsopp x-probes with no global T, with reverse hold and face hold from existential opposite; reverse hold does not use L(A); uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_xprobe_sametick_union_own_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from same-tick-inclusive 6-NN locks union own incoming lock on the four nsopp x-probes, no global T, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with later-tick union leftover, do not identify the sets with formation own-lock-in leftover, and do not identify the sets with y-probe same-tick union leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of same-tick-inclusive six-neighbor locks union own incoming lock on the four nsopp x-probes; displayed, not adopted"
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
same-tick-inclusive union sets are scored:

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

## Named existential opposite from same-tick-inclusive six-neighbor locks union own incoming lock

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `L(q)` be `q`'s own unique incoming lock in `{±e_i}`. Seeds
use seed letters. If several earliest incoming steps exist, `L(q)` is
`UNDEFINED`. There is no global later T. Each probe is scored at its own
`t(q)`.

At tick `t(q)`, for each probe `q`, let the same-tick-inclusive neighbor set
be the set of locks of six-neighbors of `q` that formed at tick `≤ t(q)`
and are not `q`. Same-tick neighbors count. The probe itself is excluded.
Then `S^+(q)` is that set union `{L(q)}` when `L(q)` is defined, and equals
the neighbor set when `L(q)` is `UNDEFINED`. This display does not use
occupancy `n`. Duplicate locks at two neighbors collapse in the set. The
construction does not require `S^+(q)` to be a singleton. It does not sum
`S^+(q)`. It is not a unique lock-vector leftover and not a sum leftover.
It is not leftover of later-tick S_* union own lock. It is not leftover of
own-lock-in at formation. It is not leftover of unique own-incoming
lock-vector letters on these x-probes. It is not leftover of
same-tick-inclusive 6-NN locks union own incoming lock on the opposite-lock
y-probes.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not scored on `{+,−}`
names and are not an occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  some a in S^+(A) and some b in S^+(B) with a+b=(0,0,0)
face     <=>  some c in S^+(C) and some d in S^+(D) with a+b replaced by c+d=(0,0,0)
```

If `S^+(A)` or `S^+(B)` is empty, reverse is `UNDEFINED`. Else reverse
fails if no such pair exists. If `S^+(C)` or `S^+(D)` is empty, face is
`UNDEFINED`. Else face fails if no such pair exists. The report is one of
`hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility.

## Theorem 1 — formation ticks, own incoming locks, and S^+ at each x-probe

Direct enumeration of the displayed opposite-lock process on `B_3(0)` forms
all four x-probes. The formation ticks are t(A)=3, t(B)=2, t(C)=4,
t(D)=3. `A` is not a seed. There is no global later T.

Own incoming locks, same-tick-inclusive neighbor lock lists, and `S^+` at
each probe's own tick are:

```text
A: incoming −e_3, +e_3, +e_2; +e_1 at (0, 0, 0), −e_2 at (1, 1, 0),
   −e_3 at (1, 1, 0), +e_3 at (1, 1, 0), +e_1 at (1, -1, 0),
   +e_1 at (1, 0, 1), +e_1 at (1, 0, -1);
   t(A)=3;  L(A) = UNDEFINED;
   S^+(A) = {+e_1, −e_2, +e_3, −e_3}
B: incoming +e_1; +e_3 at (0, 1, 1), +e_1 at (1, 0, 1);
   t(B)=2;  L(B) = +e_1;
   S^+(B) = {+e_1, +e_3}
C: incoming +e_1; −e_3 at (1, 0, 0), +e_3 at (1, 0, 0), +e_2 at (1, 0, 0),
   +e_1 at (2, 1, 0);
   t(C)=4;  L(C) = +e_1;
   S^+(C) = {+e_1, +e_2, +e_3, −e_3}
D: incoming −e_2, −e_3, +e_3; −e_1 at (0, 1, 0), +e_1 at (1, 2, 0),
   −e_3 at (1, 0, 0), +e_3 at (1, 0, 0), +e_2 at (1, 0, 0),
   +e_1 at (1, 1, 1), +e_1 at (1, 1, -1);
   t(D)=3;  L(D) = UNDEFINED;
   S^+(D) = {+e_1, −e_1, +e_2, +e_3, −e_3}
```

`A` is not a seed. L(A) is UNDEFINED from three earliest incoming steps
`−e_3`, `+e_3`, and `+e_2`, so `S^+(A)` equals the same-tick-inclusive
neighbor set. Reverse hold does not use L(A). `L(B)=+e_1` already sits in
the neighbor set at `B`, so the union does not enlarge `B`. `L(C)=+e_1`
already sits in the neighbor set at `C`, so the union does not enlarge `C`.
`L(D)` is `UNDEFINED` from three earliest incoming steps `−e_2`, `−e_3`,
and `+e_3`, so `S^+(D)` equals the neighbor set. On these x-probes the union
happens to leave every neighbor set unchanged. Mixed remains a set.

Incoming locks exist and need not be unique (`A` has three earliest incoming
steps `−e_3`, `+e_3`, and `+e_2`; `D` has three earliest incoming steps
`−e_2`, `−e_3`, and `+e_3`). That non-uniqueness leaves `L(A)` and `L(D)`
`UNDEFINED` and does not empty `S^+(A)` or `S^+(D)`. Uniqueness is not
required. `+e_2` is incoming at `A` and is not in `S^+(A)`.

The unique own-incoming letters on these x-probes are `UNDEFINED`, `+e_1`,
`+e_1`, `UNDEFINED`. Those are different objects: `S^+(A)` is nonempty and
is not `{−e_3, +e_3, +e_2}`. Same-tick-inclusive existential opposite that
excludes `q` reports the same neighbor lists and does not report `L` or the
union. Own-lock-in at formation reports `{+e_1}`, `{+e_1, +e_3}`,
`{+e_1, +e_2, +e_3, −e_3}`, `{+e_1, −e_1}` at each probe's own `t(q)` with
tick `< t(q)`. Later-tick `S_*` union own lock on these x-probes reports
`S^+(B)={+e_1, +e_2, −e_2, +e_3, −e_3}` at global `T=4`. Same-tick-inclusive
6-NN locks union own incoming lock on the opposite-lock y-probes reports
seed letter `−e_1` at `A=(0,1,0)` and reverse hold uses `L(A)`. Those lists
are not these lists. Same-tick-inclusive existential opposite on the nnseed
x-probes uses the perp two-site seed.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S^+(A)` and `b` in
`S^+(B)` with `a+b=(0,0,0)`. Both sets are nonempty:
`S^+(A)={+e_1, −e_2, +e_3, −e_3}` and
`S^+(B)={+e_1, +e_3}`. The pair `−e_3+(+e_3)=(0,0,0)` holds. Reverse holds.

Reverse: hold

This is not `fail` and not `UNDEFINED`. Reverse hold does not use L(A):
`L(A)` is `UNDEFINED`, and the holding pair is `−e_3` at same-tick neighbor
`D` against `+e_3` at `B`. Unique lock-vector lettering of the same lists
would assign mixed `S^+(A)` and mixed `S^+(B)` and would report reverse
`UNDEFINED`. That readout is a different object and is not used. A sum
leftover of the same lists would replace the sets by `(1,−1,0)` and
`(1,0,1)` and would report reverse fail. A named-sign readout of the same
locks would lose the axis in mixed `{+,−}` at `A`. Unique own-incoming
letters on these x-probes report reverse `UNDEFINED` from mixed `A`.
Own-lock-in at formation reports reverse fail on `{+e_1}` at `A` and
`{+e_1, +e_3}` at `B`. Later-tick S_* union own lock also reports reverse
hold, but from a larger `S^+(B)` at global `T=4` that includes `+e_2` and
`−e_2`. Opposite-lock y-probe same-tick-inclusive union own lock also
reports reverse hold, but reverse hold uses `L(A)=−e_1` at seed `A`. The
holding readout transfers in this cubic frame; the lists do not.

Reverse holds.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S^+(C)` and `d` in
`S^+(D)` with `c+d=(0,0,0)`. Both sets are nonempty:
`S^+(C)={+e_1, +e_2, +e_3, −e_3}` and
`S^+(D)={+e_1, −e_1, +e_2, +e_3, −e_3}`, so `+e_3+(−e_3)=(0,0,0)`. Face
holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.

This is not `fail` and not `UNDEFINED`. Unique own-incoming letters on these
same x-probes assign `L(D)=UNDEFINED` from three earliest incoming steps and
report face `UNDEFINED`. Unique lock-vector lettering of the same-tick union
sets would also report face `UNDEFINED` because both `C` and `D` mix. A sum
leftover would replace the sets by `(1,1,0)` and `+e_2` and would fail face,
while existential opposite holds. Named-sign lettering lost the axis in mixed
`{+,−}` at `C` and at `D`. Own-lock-in at formation reports face hold from
`L(C)=+e_1` against `−e_1` at `D` on a different, smaller set at `D`.
Later-tick S_* union own lock also reports face hold from `S_*` at global
`T`. Opposite-lock y-probe same-tick-inclusive union own lock reports face
hold from different lists.

Face holds.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the same-tick-inclusive union set to be a singleton.
- It does not sum the same-tick-inclusive union set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from same-tick-inclusive six-neighbor locks.
- It does not census a sixteen-combination free lettering independent of
  same-tick-inclusive lock vectors.
- It does not reprint unique own-incoming lock-vector letters on these
  x-probes.
- It does not reprint later-tick S_* union own lock on these x-probes.
- It does not reprint own-lock-in existential opposite at formation.
- It does not reprint same-tick-inclusive 6-NN locks union own incoming lock
  on the opposite-lock y-probes.
- It does not reprint same-tick-inclusive existential opposite on the nnseed
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
opposite-lock process, the same-tick-inclusive six-neighbor lock sets union own
incoming lock, and the existential-opposite reverse/face predicates are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; opposite-lock two-site seed `+e_1/−e_1` |
| formation ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` with no global later T | Theorem 1; `3`, `2`, `4`, `3` |
| own incoming locks `L(A)`, `L(B)`, `L(C)`, `L(D)` | Theorem 1; `UNDEFINED`, `+e_1`, `+e_1`, `UNDEFINED` |
| lock sets `S^+(A)`, `S^+(B)`, `S^+(C)`, `S^+(D)` | Theorem 1; `{+e_1, −e_2, +e_3, −e_3}`, `{+e_1, +e_3}`, `{+e_1, +e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_2, +e_3, −e_3}` |
| whether reverse hold uses `L(A)` | Theorem 1; it does not; `L(A)` is `UNDEFINED` |
| reverse and face | Theorems 2–3; `hold` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from same-tick-inclusive six-neighbor locks | not attached |
| leftover of unique own-incoming letters on these x-probes | not this display |
| leftover of later-tick S_* union own lock | not this display; cubic-frame transfer of the same-tick union construction, not of global-T leftover |
| leftover of own-lock-in at formation | not this display |
| leftover of same-tick-inclusive 6-NN locks union own incoming lock on the opposite-lock y-probes | not this display |
| leftover of nnseed x-probe same-tick-inclusive existential opposite | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: existential opposite in same-tick-inclusive 6-NN locks union own incoming lock on the four nsopp x-probes, no global T, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed same-tick-inclusive union-own reverse/face report on these four opposite-lock x-probes. |
| V3 | Same-tick-inclusive union sets and the `hold`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads six-neighbor lock vectors at each probe's own tick, unions `L(q)` when defined, and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not identify them with the probe's own incoming steps
alone, does not reduce them to named signs, does not require a singleton
lock vector, does not sum the lock set, does not reprint unique
own-incoming letters, does not reprint later-tick S_* union own lock, does
not reprint own-lock-in at formation, does not reprint opposite-lock
y-probe same-tick union leftover, and does not use occupancy `n`. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same union sets | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while both pairs of sets are nonempty |
| sum of the same union sets | replace `S^+` by the `Z^3` sum | refused; leftover; sum of `S^+(A)` is `(1,−1,0)` and of `S^+(B)` is `(1,0,1)` and would fail reverse while `−e_3+(+e_3)=0`; sum of `S^+(C)` is `(1,1,0)` and of `S^+(D)` is `+e_2` and would fail face |
| named-sign lettering of the same union sets | map `±e_i` to `{+,−}` | refused; lost the axis; mixed `{+,−}` at `A` would hide `−e_3+(+e_3)=0` |
| unique own-incoming lock-vector leftover on these x-probes | reuse `L(A)=UNDEFINED`, `L(B)=+e_1`, `L(C)=+e_1`, `L(D)=UNDEFINED` | refused; different object; that leftover reports reverse `UNDEFINED` and face `UNDEFINED` while same-tick `S^+(A)` and `S^+(D)` are nonempty and both bits hold |
| leftover of same-tick-inclusive existential opposite that excludes `q` | reuse neighbor sets without unioning `L(q)` | refused; different algebra; on these x-probes the union happens to leave the neighbor sets unchanged, but `L` is reported and the construction is the union |
| leftover of own-lock-in at formation | reuse `S^+` at each probe's own `t(q)` with tick `< t(q)` and reverse fail face hold | refused; different tick cut; reverse holds here after same-tick neighbors of `A` include `D` |
| leftover of later-tick S_* union own lock | reuse lists at global `T=4` with larger `S^+(B)` | refused; different tick; `S^+(B)` here is `{+e_1, +e_3}` and has no `+e_2` and no `−e_2`; cubic-frame transfer of the same-tick union construction, not leftover of those lists |
| leftover of same-tick-inclusive 6-NN locks union own incoming lock on the opposite-lock y-probes | reuse y-probe lists with seed letter `−e_1` at `A` | refused; different frame; reverse hold uses `L(A)` there and does not here |
| leftover of nnseed x-probe same-tick-inclusive existential opposite | reuse seed `+e_1/+e_2` and x-probes with reverse fail | refused; different process; reverse holds here |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| attach a formation member from same-tick-inclusive six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; all three earliest incoming steps at `A` and at `D` are kept |

### N2 — wall independence

Missing physical adoption, missing formation attachment from
same-tick-inclusive six-neighbor locks, and missing Record identification of
existential opposite are distinct open premises. This note claims no complete
wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, same-tick-inclusive lock set of six-neighbors formed
by each probe's own `t(q)`, no global later T, union with `L(q)` when
defined, existential opposite, four x-probes with non-seed `A`, and reverse/face
as existence of a pair that sums to zero are declared. No uniqueness of incoming
locks, no occupancy `n`, no named-sign reduction, no singleton leftover, no
sum leftover, no unique own-incoming leftover, no later-tick union leftover, no
own-lock-in formation leftover, no opposite-lock y-probe leftover, no nnseed
x-probe leftover, no formation attachment from same-tick-inclusive
six-neighbor locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in same-tick-inclusive six-neighbor locks union `L(q)` when defined | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `S^+` lock sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** The union is leftover of later-tick S_* union own lock because
reverse and face both hold, leftover of exclude-`q` lists because `S^+`
equals the neighbor set on these x-probes, mixed neighbor locks should make
reverse and face `UNDEFINED`, the sets should be replaced by their sums,
unique own-incoming letters already answered reverse `UNDEFINED` with face
`UNDEFINED`, own-lock-in at formation already answered reverse fail with
face hold, y-probe same-tick union already answered hold/hold so this is
leftover, named signs should suffice because they keep orientation, and
occupancy `n` should track that vector.

**Answer:** The named construction reports lock sets
`{+e_1, −e_2, +e_3, −e_3}`, `{+e_1, +e_3}`,
`{+e_1, +e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_2, +e_3, −e_3}` at
`A,B,C,D` from same-tick-inclusive six-neighbor locks union `{L(q)}` when
defined, at each probe's own `t(q)` with no global later T. Mixed remains a
set. The construction does not sum. Occupancy `n` is not used. Named signs
lost the axis. Some pair from `S^+(A)` and `S^+(B)` is opposite, so reverse
holds. Reverse hold does not use L(A). Face holds. On these x-probes the
union happens to leave the neighbor sets unchanged because `L(A)` and
`L(D)` are `UNDEFINED` and `L(B)`, `L(C)` already sit in the neighbor sets.
The algebra is still the union: `L` is reported. Later-tick S_* union own
lock enlarges `S^+(B)` at global `T=4`. Y-probe same-tick union enlarges
seed `A` by `−e_1` and reverse hold uses `L(A)` there. Own-lock-in at
formation reports reverse fail. The holding readout transfers in this cubic
frame; the lists do not. The bits remain displayed. Incoming-lock uniqueness
is not required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same opposite-lock
x-probes assigned `L(A)=UNDEFINED`, `L(B)=+e_1`, `L(C)=+e_1`,
`L(D)=UNDEFINED` and reported reverse `UNDEFINED` with face `UNDEFINED`.
Own-lock-in at formation reported reverse fail and face hold on
`{+e_1}`, `{+e_1, +e_3}`, `{+e_1, +e_2, +e_3, −e_3}`, `{+e_1, −e_1}`.
Later-tick S_* union own lock reported reverse hold and face hold from a
larger `S^+(B)` at global `T=4`. Same-tick-inclusive 6-NN locks union own
incoming lock on the opposite-lock y-probes reported reverse hold and face
hold from seed letter `−e_1` at `A=(0,1,0)`, and reverse hold uses `L(A)`
there. Unique lock-vector lettering of the union sets would report reverse
`UNDEFINED` and face `UNDEFINED` because every same-tick union set mixes. A
sum leftover of the same lists would report reverse fail and face fail
because the sums are `(1,−1,0)` and `(1,0,1)` on reverse and `(1,1,0)` and
`+e_2` on face. This note is not those displays: mixed remains a set, the
construction does not sum, `−e_3+(+e_3)=(0,0,0)` so reverse holds, and
`+e_3+(−e_3)=(0,0,0)` so face holds. The holding readout is a cubic-frame
transfer of same-tick-inclusive 6-NN locks union own incoming lock; the
lists are not leftover of the y-probe display.

**Gate disposition:** PASS for the same-tick-inclusive six-neighbor-lock
union own incoming lock existential-opposite reverse/face reports above.
FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the predicate
equals the unique singleton lock vector,” “the predicate equals the sum of
the lock set,” “the lock set equals the probe's own incoming step,” “bits
are Admissibility,” “the letter is occupancy `n`,” “the sets equal unique
own-incoming letters,” “the sets equal later-tick S_* union own lock,”
“the sets equal own-lock-in at formation,” “the sets equal opposite-lock
y-probe same-tick union leftover,” “reverse fails,” or “face is
`UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the opposite-lock two-site
perp-step incoming-lock process, reads each probe's own unique incoming lock
or `UNDEFINED`, collects six-neighbor locks formed by each probe's own
`t(q)` with the probe excluded, unions those locks with `{L(q)}` when
defined, reads the union sets at the four x-probes, and checks Theorems
1--3, including whether reverse hold uses `L(A)`. It also checks that the
construction is not named-sign lettering, that mixed sets remain defined,
that the construction does not sum, that occupancy `n` is not used, that a
formation member from same-tick-inclusive six-neighbor locks is not
attached, that the sets are not leftover of unique own-incoming letters,
that the sets are not leftover of later-tick S_* union own lock, that the
sets are not leftover of own-lock-in at formation, and that the sets are
not leftover of opposite-lock y-probe same-tick union. No runner cache is
written.
