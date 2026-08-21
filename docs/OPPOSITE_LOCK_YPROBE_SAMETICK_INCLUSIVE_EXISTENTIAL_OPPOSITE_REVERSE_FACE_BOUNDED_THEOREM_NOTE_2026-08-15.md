---
claim_id: opposite_lock_yprobe_sametick_inclusive_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from existential opposite 6-NN locks formed by each nsopp y-probe's own tick (same-tick-inclusive, q excluded, no global later T) are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_yprobe_sametick_inclusive_existential_opposite_reverse_face_2026_08_15.py
---

# Same-Tick-Inclusive Existential Opposite Neighbor-Lock Reverse And Face On Four Opposite-Lock Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from existential opposite six-neighbor locks
formed by each opposite-lock y-probe's own tick (same-tick-inclusive, the
probe excluded, no global later T) in `B_3(0)`. Let `t(q)` be the formation
tick of probe `q`. At that tick, `S(q)` is the set of locks of six-neighbors
of `q` that formed at tick `<= t(q)` and are not `q`. Reverse holds if and
only if some lock in `S(A)` is the vector opposite of some lock in `S(B)`.
Face holds if and only if some lock in `S(C)` is the vector opposite of some
lock in `S(D)`. Empty `S` on either side of a comparison is `UNDEFINED`;
nonempty with no opposite pair fails. Occupancy `n` is not used. The probe's
own incoming lock is not used. This is not named-sign lettering. This is not
a unique lock-vector leftover and not a sum leftover. This is not leftover
of strictly-earlier formation-tick existential opposite on these same
y-probes: that display takes tick `< t(q)` and reports reverse `UNDEFINED`
because `S(A)` is empty. This is not leftover of later-tick existential
opposite on these same y-probes: that display waits for a global later T
equal to the max of the four formation ticks and reports reverse hold. This
is not leftover of the unique own-incoming lock-vector letters on these
y-probes: that readout requires a singleton incoming step and reports reverse
hold with face `UNDEFINED` at mixed `D`. Uniqueness of incoming locks is not
required. Uniqueness of the lock set is not required. Displayed, not
adopted. This note does not write existential opposite into Admissibility
and does not attach a formation member from already-recorded six-neighbor
locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_yprobe_sametick_inclusive_existential_opposite_reverse_face_2026_08_15.py`](../scripts/opposite_lock_yprobe_sametick_inclusive_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
same-tick-inclusive six-neighbor lock sets at each probe's own tick. Named
signs `{+,−}` are a coarser readout and are not used. A singleton unique
lock-vector letter is a different readout and is not used. A `Z^3` sum of
those locks is a different readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of same-tick-inclusive six-neighbor lock sets on the four opposite-lock y-probes at each probe's own t, with reverse fail and face hold from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_yprobe_sametick_inclusive_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from existential opposite 6-NN locks formed by each nsopp y-probe's own tick (same-tick-inclusive, q excluded, no global later T), or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with the probe's own incoming step, do not identify the sets with strictly-earlier leftover, and do not identify the sets with later-tick leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of same-tick-inclusive six-neighbor locks on the four opposite-lock y-probes; displayed, not adopted"
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
same-tick-inclusive six-neighbor lock sets are scored:

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

That incoming lock is not a member of `S(q)` scored below unless it appears
as a lock of some six-neighbor of `q` formed at tick `<= t(q)`.

## Named existential opposite from same-tick-inclusive six-neighbor locks

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. At the own formation tick of each probe `q`, let `S(q)` be the set
of locks of six-neighbors of `q` that formed at tick `<= t(q)`
(same-tick-inclusive). The probe itself is excluded. Same-tick partners are
kept when they are neighbors. This display does not wait for a global later
T. This display does not use occupancy `n`. It does not use the probe's own
incoming lock. Duplicate locks at two neighbors collapse in the set. The
construction does not require `S(q)` to be a singleton. It does not sum
`S(q)`. It is not a unique lock-vector leftover and not a sum leftover. It
is not leftover of strictly-earlier formation-tick existential opposite. It
is not leftover of later-tick existential opposite. It is not leftover of
unique own-incoming lock-vector letters on these y-probes.

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

If `S(A)` or `S(B)` is empty, reverse is `UNDEFINED`. Else reverse fails if
no such pair exists. If `S(C)` or `S(D)` is empty, face is `UNDEFINED`. Else
face fails if no such pair exists. The report is one of `hold`, `fail`, or
`UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility.

## Theorem 1 — formation ticks and lock sets at each y-probe

Direct enumeration of the displayed opposite-lock process on `B_3(0)` forms
all four y-probes. The formation ticks are `t(A)=0`, `t(B)=2`, `t(C)=1`,
`t(D)=3`. `A` is a seed. Those ticks locate the same-tick-inclusive
six-neighbor set. They are not occupancy kernels and are not a global later
T.

At each probe's own formation tick the six-neighbor lock lists and lock sets
are:

```text
A: +e_1 at (0, 0, 0);
   t(A)=0;  S(A) = {+e_1}
B: +e_3 at (0, 1, 1), +e_1 at (1, 0, 1);
   t(B)=2;  S(B) = {+e_1, +e_3}
C: −e_1 at (0, 1, 0);
   t(C)=1;  S(C) = {−e_1}
D: −e_1 at (0, 1, 0), +e_1 at (1, 2, 0), −e_3 at (1, 0, 0),
   +e_3 at (1, 0, 0), +e_2 at (1, 0, 0), +e_1 at (1, 1, 1),
   +e_1 at (1, 1, -1);
   t(D)=3;  S(D) = {+e_1, −e_1, +e_2, +e_3, −e_3}
```

`A` is a seed at tick 0. Its same-tick partner at the origin is a
six-neighbor locking `+e_1`, so `S(A)` is `{+e_1}`. Strictly-earlier
formation-tick leftover on the same probes drops that partner and leaves
`S(A)` empty. `C`'s already-recorded neighbor is the seed partner `(0,1,0)`
locking `−e_1`. `C` has no same-tick neighbor in `B_3(0)`, so inclusive and
strictly-earlier lists agree at `C`. `B` keeps the earlier neighbor `(0,1,1)`
locking `+e_3` and the same-tick neighbor `(1,0,1)` locking `+e_1`. `D` forms
at tick 3, which equals the max of the four formation ticks, so `S(D)`
coincides with the later-tick leftover set at `D`. Mixed remains a set.

Incoming locks exist and need not be unique (`D` has three earliest incoming
steps `−e_2`, `−e_3`, and `+e_3`). That non-uniqueness is not a
unique-lettering of same-tick-inclusive neighbor lock vectors. The lock sets
are not identified with those incoming steps. Uniqueness is not required.

The unique own-incoming letters on these same y-probes are `−e_1`, `+e_1`,
`+e_2`, `UNDEFINED`. Those are different objects: `S(A)` is `{+e_1}`, not
`{−e_1}`, and `S(D)` is nonempty. Strictly-earlier formation-tick
existential opposite on these same y-probes reports empty `S(A)` and reverse
`UNDEFINED`. Later-tick existential opposite on these same y-probes reports
`{+e_1, +e_2, −e_2, +e_3, −e_3}` at `A` after waiting for a global later T.
Formation-time existential opposite on the nnseed x-probes reports `{+e_1}`,
`{+e_1, +e_3}`, `{−e_2}`, `{+e_2}` at a different seed and different frame.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S(A)` and `b` in `S(B)`
with `a+b=(0,0,0)`. Both sets are nonempty: `S(A)={+e_1}` and
`S(B)={+e_1, +e_3}`. No pair sums to zero. Reverse fails.

Reverse: fail

This is not leftover of strictly-earlier formation-tick existential opposite
on these y-probes: that leftover drops the same-tick origin partner, leaves
`S(A)` empty, and reports reverse `UNDEFINED`. This is not leftover of
later-tick existential opposite on these y-probes: that leftover waits for a
global later T and reports reverse hold from a nonempty later set at `A`
that includes `−e_2` opposite `+e_2`. Unique lock-vector lettering of the
same inclusive lists would report reverse `UNDEFINED` because `S(B)` mixes.
A sum leftover of the same lists would replace `S(A)` by `+e_1` and `S(B)`
by `+e_1++e_3`. Unique own-incoming letters on these y-probes report reverse
hold from `L(A)=−e_1` and `L(B)=+e_1`, which are not these inclusive sets.
Formation-time existential opposite on the nnseed x-probes reports reverse
fail on different nonempty sets at a different seed.

Holding reverse needs the later tick: same-tick-inclusive readout fills
`S(A)` with `+e_1` and still finds no opposite in `S(B)`.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S(C)` and `d` in `S(D)`
with `c+d=(0,0,0)`. Both sets are nonempty: `S(C)={−e_1}` and
`S(D)={+e_1, −e_1, +e_2, +e_3, −e_3}`, so `−e_1+(+e_1)=(0,0,0)`. Face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.

This is not `fail` and not `UNDEFINED`. Unique own-incoming letters on these
same y-probes assign `L(D)=UNDEFINED` from three earliest incoming steps and
report face `UNDEFINED`. Unique lock-vector lettering of the inclusive lists
would also report face `UNDEFINED` because `D` mixes. A sum leftover would
replace `S(C)` by `−e_1` and `S(D)` by `+e_2` and would fail face, while
existential opposite holds. Named-sign lettering lost the axis in mixed
`{+,−}` at `D`. Face already holds at each probe's own formation tick with
same-tick partners included; holding face does not need a global later T.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify lock sets with the probe's own incoming `{±e_i}`.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the same-tick-inclusive lock set to be a singleton.
- It does not sum the same-tick-inclusive lock set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  same-tick-inclusive lock vectors.
- It does not reprint unique own-incoming lock-vector letters on these
  y-probes.
- It does not reprint strictly-earlier formation-tick existential opposite
  on these y-probes.
- It does not reprint later-tick existential opposite on these y-probes.
- It does not wait for a global later T.
- It does not reprint formation-time already-recorded lock sets on nnseed
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

This display uses Lattice to name `B_3(0)` and the four y-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
opposite-lock process, the same-tick-inclusive six-neighbor lock sets, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; opposite-lock two-site seed `+e_1/−e_1` |
| same-tick-inclusive six-neighbor lock sets at each y-probe's own `t` | Theorem 1 |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| lock sets `S(A)`, `S(B)`, `S(C)`, `S(D)` | Theorem 1; `{+e_1}`, `{+e_1, +e_3}`, `{−e_1}`, `{+e_1, −e_1, +e_2, +e_3, −e_3}` |
| reverse and face | Theorems 2–3; `fail` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| probe's own incoming lock as the set | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique own-incoming letters on these y-probes | not this display |
| leftover of strictly-earlier formation-tick existential opposite | not this display |
| leftover of later-tick existential opposite on these y-probes | not this display |
| leftover of nnseed x-probe formation-time existential opposite | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: existential opposite of 6-NN locks formed by each nsopp y-probe's own tick (same-tick-inclusive, q excluded, no global later T), reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed same-tick-inclusive existential-opposite neighbor-lock reverse/face report on these four opposite-lock y-probes. |
| V3 | Same-tick-inclusive lock sets and the `fail`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads six-neighbor lock vectors at each probe's own formation tick with same-tick partners included and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not identify them with the probe's own incoming steps,
does not reduce them to named signs, does not require a singleton lock
vector, does not sum the lock set, does not reprint unique own-incoming
letters, does not reprint strictly-earlier leftover, does not reprint
later-tick leftover, and does not use occupancy `n`. No global impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same neighbor locks | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse would be `UNDEFINED` because `S(B)` mixes, and face would be `UNDEFINED` while `S(D)` is nonempty and face holds |
| sum of the same neighbor locks | replace `S` by the `Z^3` sum | refused; leftover; sum of `S(C)` is `−e_1` and sum of `S(D)` is `+e_2`, which would fail face while `−e_1+(+e_1)=0` |
| named-sign lettering of the same neighbor locks | map `±e_i` to `{+,−}` | refused; lost the axis; mixed `{+,−}` at `D` would hide `−e_1+(+e_1)=0` |
| identify lock sets with the probe's own incoming `{±e_i}` | map `A`'s seed letter `−e_1` into `S(A)` | refused; `S(A)` is `{+e_1}`; `S(A)` is not `{−e_1}` |
| unique own-incoming lock-vector leftover on these y-probes | reuse `L(A)=−e_1`, `L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` | refused; different object; that leftover reports reverse hold and face `UNDEFINED` while inclusive reverse fails and face holds |
| leftover of strictly-earlier formation-tick existential opposite | reuse tick `< t(q)` and empty `S(A)` with reverse `UNDEFINED` | refused; different set; this display keeps same-tick partners; reverse fails here |
| leftover of later-tick existential opposite | reuse global later T and nonempty `S_*` at `A` with reverse hold | refused; different set; this display does not wait for a global later T; reverse fails here |
| leftover of nnseed x-probe formation-time existential opposite | reuse seed `+e_1/+e_2` and x-probes with reverse fail | refused; different process and different frame |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `S` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; all three earliest incoming steps at `D` are kept |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, same-tick-inclusive lock set of six-neighbors formed
at tick `<=` each probe's own `t` with the probe excluded, existential
opposite, four y-probes with seed `A`, and reverse/face as existence of a pair
that sums to zero are declared. No uniqueness of incoming locks, no occupancy
`n`, no named-sign reduction, no singleton leftover, no sum leftover, no
unique own-incoming leftover, no strictly-earlier leftover, no later-tick
leftover, no global later T, no formation attachment from already-recorded
six-neighbor locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in a same-tick-inclusive set | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four lock sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Same-tick partners should already have been scored as
already-recorded, so this display is leftover of strictly-earlier
formation-tick exist-opposite. Once a six-neighbor exists at a later common
tick, the site should lock that unique vector as incoming content, mixed
neighbor locks should make reverse and face `UNDEFINED`, the sets should be
replaced by their sums, unique own-incoming letters already answered reverse
hold with face `UNDEFINED`, later-tick existential opposite already answered
the exist-opposite question, named signs should suffice because they keep
orientation, and occupancy `n` should track that vector.

**Answer:** The named construction reports lock sets `{+e_1}`, `{+e_1, +e_3}`,
`{−e_1}`, `{+e_1, −e_1, +e_2, +e_3, −e_3}` at `A,B,C,D` from six-neighbor
locks formed at tick `<=` each probe's own formation tick with the probe
excluded. Same-tick partners are kept. Mixed remains a set. The construction
does not sum. Occupancy `n` is not used. Named signs lost the axis. Both
`S(A)` and `S(B)` are nonempty with no opposite pair, so reverse fails.
Some pair from `S(C)` and `S(D)` is opposite, so face holds. Holding reverse
needs the later tick. The sets are not leftover of strictly-earlier
formation-tick lists, not leftover of unique own-incoming letters, and not
leftover of later-tick existential opposite. The bits remain displayed.
Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same opposite-lock
y-probes assigned `L(A)=−e_1`, `L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` and
reported reverse hold with face `UNDEFINED`. A unique already-recorded
six-neighbor lock-vector display on these y-probes assigned empty `A` and
mixed `D` and reported reverse `UNDEFINED` with face `UNDEFINED`.
Strictly-earlier formation-tick existential opposite on these y-probes
reported reverse `UNDEFINED` and face hold on empty `S(A)` and mixed `S(D)`.
Later-tick existential opposite on these y-probes reported reverse hold and
face hold on different later sets `{+e_1, +e_2, −e_2, +e_3, −e_3}` and
`{+e_1, −e_1, +e_2, +e_3, −e_3}` after a global later T. Unique lock-vector
lettering of the inclusive lists would report reverse `UNDEFINED` and face
`UNDEFINED` because `B` mixes and `D` mixes. A sum leftover of the same lists
would report face fail because the sums are `−e_1` and `+e_2`. This note is
not those displays: mixed remains a set, the construction does not sum,
reverse fails because `{+e_1}` has no opposite in `{+e_1, +e_3}`, and
`−e_1+(+e_1)=(0,0,0)` so face holds.

**Gate disposition:** PASS for the same-tick-inclusive six-neighbor-lock
existential-opposite reverse/face reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique singleton
lock vector,” “the predicate equals the sum of the lock set,” “the lock set
equals the probe's own incoming step,” “bits are Admissibility,” “the letter
is occupancy `n`,” “the sets equal unique own-incoming letters,” “the sets
equal strictly-earlier leftover,” “the sets equal later-tick leftover,”
“reverse holds,” “reverse is `UNDEFINED`,” or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the opposite-lock two-site
perp-step incoming-lock process, collects six-neighbor locks formed at tick
`<=` each probe's own formation tick with the probe excluded, reads the lock
sets at the four y-probes, and checks Theorems 1--3. It also checks that the
construction is not named-sign lettering, that mixed sets remain defined,
that the construction does not sum, that the probe's own incoming step is
not the lock set, that occupancy `n` is not used, that a formation member
from already-recorded six-neighbor locks is not attached, that the sets are
not leftover of unique own-incoming letters, that the sets are not leftover
of strictly-earlier formation-tick existential opposite, and that the sets
are not leftover of later-tick existential opposite. No runner cache is
written.
