---
claim_id: opposite_lock_yprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Simultaneous M and O at t+1 on the four #7208 y-probes, intersection, and reverse/face of each are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_yprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py
---

# Simultaneous Own-Incoming And Own-Outgoing Reverse And Face At t+1 On Four #7208 Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** simultaneous earliest incoming set `M` and outgoing dual `O` at
each probe's `τ=t+1`, their intersection, and reverse/face of each, on the
four nsmopp #7208 y-probes in `B_3(0)={n:n·n<=9}`. Same process as nsopp
#7093. Let `t(q)` be the formation tick of probe `q`. Let `τ(q)=t(q)+1`.
`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. Seeds are a singleton seed letter.
`O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`.
Intersection is `M(q,τ)∩O(q,τ)` when both are defined. Reverse of `M` at
`τ` holds if and only if some `a` in `M(A,τ)` and some `b` in `M(B,τ)`
have `a+b=(0,0,0)`. Reverse of `O` at `τ` likewise on `O(A,τ)` and
`O(B,τ)`. Face likewise on `C,D`. Empty or `UNDEFINED` on either side is
`UNDEFINED`. This is not leftover of nmt2opp `M` frozen at `t`. This is
not leftover of nmot2opp `O` empty at `t` then HOLD at `t+1` as a
two-tick composition. This is not leftover of nmoutopp untimed eventual-`O`.
This is not leftover of nmunopp untimed union. This is not leftover of mixed #7188 fail/fail. Uniqueness of incoming or
outgoing locks is not required. Mixed remains a set. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_yprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py`](../scripts/opposite_lock_yprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Reverse and face of each of `M` and `O` are scored on existence of
an opposite pair at that same cut. Named signs `{+,−}` are a coarser readout
and are not used. A singleton unique lock letter is a different readout and
is not used as the object. A `Z^3` sum of those locks is a different readout
and is not used. Occupancy `n` is not used. A six-neighbor star is not the
letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of simultaneous own incoming M and own outgoing O at t+1 on the four #7208 y-probes, empty intersection, reverse hold and face hold from M, reverse hold and face hold from O; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_yprobe_simultaneous_incoming_outgoing_tplus1_reverse_face
target_blocker_text: "display M and O together at t+1 on the four #7208 y-probes, their intersection, and reverse/face of each, no untimed O leftover"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep simultaneous M and O at t+1 displayed; do not write existential opposite into Admissibility, do not reduce to a unique letter, do not replace either set by six-neighbor lock union, do not replace timed O at t+1 by untimed eventual-O, do not identify the display with nmt2opp M frozen at t, do not identify the display with nmot2opp two-tick composition, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for simultaneous M and O at t+1 on the four #7208 y-probes, intersection, and reverse/face of each; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose own
incoming and outgoing sets are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed. Same process and y-probes as nsmopp #7208.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`. This seed is not the perp
two-site seed `+e_1/+e_2`. This seed is not the z-symmetric three-site seed
`{0,(0,0,1),(0,0,-1)}`. This seed is not the y-symmetric three-site seed
that also records `(0,-1,0)` at tick 0.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept. A later
parent does not re-form `q`. Uniqueness is not required. Mixed remains a set.

## Named incoming set `M` and outgoing set `O` at `τ=t+1`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter.

`O(q,τ)` is the outgoing dual of `M`:

```text
O(q,τ) = { e in {±e_1,±e_2,±e_3} | q+e formed and e in M(q+e,τ) }.
```

If `q` is unformed at `τ`, then `O(q,τ)` is `UNDEFINED`. Empty `O` is empty,
not `UNDEFINED`. Duplicate steps collapse in the set. The construction does
not require `M` or `O` to be a singleton. It does not sum either set. It
does not replace `O` by `M`. It does not wait for a global later T.
Occupancy `n` is not used. O is not M.

Intersection at the same cut is

```text
(M ∩ O)(q,τ) = M(q,τ) ∩ O(q,τ)
```

when both sides are defined. If either is `UNDEFINED`, the intersection is
`UNDEFINED`. Empty intersection is empty, not `UNDEFINED`.

Reverse of `M` at `τ` holds if and only if some `a` in `M(A,τ)` and some
`b` in `M(B,τ)` have `a+b=(0,0,0)`. Reverse of `O` at `τ` holds if and
only if some `a` in `O(A,τ)` and some `b` in `O(B,τ)` have `a+b=(0,0,0)`.
Face of `M` at `τ` holds if and only if some `c` in `M(C,τ)` and some `d`
in `M(D,τ)` have `c+d=(0,0,0)`. Face of `O` at `τ` likewise on `O(C,τ)`
and `O(D,τ)`. Empty or `UNDEFINED` on either side of a comparison is
`UNDEFINED`; nonempty with no opposite pair fails.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero inside the named set.

## Theorem 1 — ticks, `M`, `O`, and intersection at `τ=t+1`

On this process the four y-probes form. Compare to nmt2opp: that leftover
reports `M` frozen, `M(q,t+1)=M(q,t)` at every scored probe. Compare to
nmot2opp: that leftover reports `O` empty at `t` for `A`, `B`, and `C`,
then HOLD at `t+1`. This display reads `M` and `O` together at the same
cut `τ=t+1`:

```text
t(A)=0
t(B)=2
t(C)=1
t(D)=3
M(A, τ) = {−e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_2, +e_3, −e_3}
O(A, τ) = {+e_2, +e_3, −e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ) = {+e_1, −e_1}
(M ∩ O)(A, τ) = {}
(M ∩ O)(B, τ) = {}
(M ∩ O)(C, τ) = {}
(M ∩ O)(D, τ) = {}
```

`A` is a seed at tick 0. Mixed remains a set: `M(D,τ)` has three earliest
incoming steps and `O(A,τ)` has three outgoing steps. Unique letters would
assign `UNDEFINED` at mixed probes. Here uniqueness is not required.
`M` and `O` are disjoint at each of the four probes at `τ`, so the
intersection is empty at each probe. Empty intersection is empty, not
`UNDEFINED`. O is not M.

Investment nmt2opp: `M` is frozen at `t`, and the `τ=t+1` incoming sets
equal the formation-tick sets. Investment nmot2opp: `O` is empty at `t`
for `A`, `B`, and `C` (`O(D,t)={−e_1}`), then HOLD at `t+1`. Those two
leftovers are sequential. This is the first display of `M` and `O`
together at `t+1`. This is not untimed O leftover: nmoutopp eventual-`O`
already reports the `τ` outgoing sets with no `t` versus `t+1` cut and
hides empty `O` at `t`. Timed `O(q,τ)` is read from records with tick
`<= τ`.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, 1), (0, 1, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

## Theorem 2 — reverse and face from `M` at `τ`

Reverse of `M` at `τ` holds if and only if some `a` in `M(A,τ)` and some
`b` in `M(B,τ)` have `a+b=(0,0,0)`. The sets are `{−e_1}` and `{+e_1}`.
The pair sums to zero. Reverse holds. Reverse HOLD uses a singleton
`M(A,τ)`. Both sides are nonempty and defined, so this is not `UNDEFINED`.

Reverse of M at τ: hold

Face of `M` at `τ` holds if and only if some `c` in `M(C,τ)` and some `d`
in `M(D,τ)` have `c+d=(0,0,0)`. The sets are `{+e_2}` and
`{−e_2, +e_3, −e_3}`. The pair `+e_2+(−e_2)` sums to zero. Face holds.

Face of M at τ: hold

These bits equal nmt2opp `M` at both cuts because incoming is frozen at
formation. Unique own-incoming letters would report face `UNDEFINED` from
mixed `D`. That leftover is not this display.

## Theorem 3 — reverse and face from `O` at `τ`

Reverse of `O` at `τ` holds if and only if some `a` in `O(A,τ)` and some
`b` in `O(B,τ)` have `a+b=(0,0,0)`. The sets are `{+e_2, +e_3, −e_3}` and
`{+e_2, +e_3, −e_3}`. The pair `+e_3+(−e_3)` sums to zero. Reverse holds.

Reverse of O at τ: hold

Face of `O` at `τ` holds if and only if some `c` in `O(C,τ)` and some `d`
in `O(D,τ)` have `c+d=(0,0,0)`. The sets are `{+e_1, −e_1, +e_3, −e_3}`
and `{+e_1, −e_1}`. The pair `+e_1+(−e_1)` sums to zero. Face holds.

Face of O at τ: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

These bits equal nmot2opp `O` at `t+1` and nmoutopp eventual-`O`. They
are not nmot2opp composition: that leftover also reports empty `O` at
`t` with reverse `UNDEFINED` and face `UNDEFINED`, then composition fail.
This display scores reverse/face of `O` at `τ=t+1` only, together with
`M` at the same cut. Unique own-outgoing letters would report reverse
`UNDEFINED` and face `UNDEFINED` from mixed `O`. That leftover is not
this display.

Empty intersection does not empty reverse of `M` or reverse of `O`.
Reverse and face are scored inside each named set, not inside the
intersection. Intersection reverse would be `UNDEFINED` because
`(M ∩ O)(A,τ)` is empty.

## What this note does not claim

- It does not select a unique incoming or outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require either set to be a singleton.
- It does not sum either set.
- It does not replace `O` by `M`.
- It does not replace either set by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmt2opp `M` frozen at `t` as this simultaneous
  display.
- It does not reprint nmot2opp two-tick composition of empty-then-HOLD `O`.
- It does not reprint nmoutopp untimed eventual-`O`.
- It does not reprint nmunopp untimed union.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not use occupancy `n`.
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
opposite-lock two-site process, the simultaneous incoming and outgoing sets
at `t+1`, the intersection, and the reverse/face bits of each are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nsopp #7093 seed `+e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| intersection `M ∩ O` at `τ` | Theorem 1; empty at each probe |
| reverse and face from `M` at `τ` | Theorem 2; `hold` / `hold` |
| reverse and face from `O` at `τ` | Theorem 3; `hold` / `hold` |
| unique incoming or outgoing lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nmt2opp `M` frozen at `t` | not this simultaneous display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| leftover of nmunopp untimed union | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| global later T | not used |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: `M` and `O` together at `t+1` on the four #7208 y-probes, intersection, and reverse/face of each. |
| V2 | Current main has no landed simultaneous incoming/outgoing `t+1` reverse/face on these four #7208 y-probes. |
| V3 | Simultaneous sets at one cut, empty intersection, and the four reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads own incoming and own outgoing at the same `t+1` cut and scores existence of an opposite pair in each. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique letter, does not replace `O` by `M`, does not replace either set by
six-neighbor lock union, does not identify this display with untimed
eventual-`O`, does not identify it with nmt2opp `M` frozen at `t`, and does
not identify it with nmot2opp two-tick composition. No global impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nmt2opp `M` frozen at `t` | reuse incoming two-tick HOLD/HOLD as the simultaneous display | that leftover never reads `O`; `M` is frozen and disjoint from `O` at `τ` | ATTEMPTED |
| nmot2opp two-tick `O` | reuse empty-at-`t` then HOLD-at-`t+1` composition | that leftover reports reverse `UNDEFINED` at `t` and composition fail; this display scores `O` at `τ` together with `M` | ATTEMPTED |
| nmoutopp untimed eventual-`O` | read neighbor locks with no `t`/`t+1` cut | that leftover already reports the `τ` outgoing sets and hides empty `O` at `t`; this cut is timed `τ=t+1` | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is a different object; this display reports intersection empty and reverse/face of each set separately | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `M(D,τ)` and mixed `O(A,τ)` remain sets; unique-letter face of `M` and reverse of `O` are `UNDEFINED` | ATTEMPTED |
| intersection as the letter | score reverse/face inside `M ∩ O` | intersection is empty; reverse of the intersection is `UNDEFINED` while reverse of `M` and of `O` hold | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes `+e_1` at `A` from the origin partner; `M(A,τ)` is `{−e_1}` | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores own incoming and outgoing step sets at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process and probes; this member reports hold/hold from `M` and hold/hold from `O` | ATTEMPTED |
| sum of a set | replace each set by its `Z^3` sum | the construction does not sum; sum of mixed `M(D,τ)` cancels to `−e_2` while the set stays three-element | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of `O` with `M`, missing
identification of timed `O` at `t+1` with untimed eventual-`O`, and missing
Record identification of existential opposite are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, own incoming set and own outgoing dual from
records with tick `<= τ`, per-probe `τ=t+1`, existential opposite, four
y-probes with seed `A`, empty intersection empty not `UNDEFINED`, and mixed
remains a set are declared. No uniqueness of locks, no six-neighbor lock
union as the scored object, no lock-count clock, no global later T, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
simultaneous `hold`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each earliest incoming or outgoing nearest-neighbor step | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four incoming sets, four outgoing sets, four intersections, reverse/face of each | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Simultaneous `M` and `O` at `t+1` is only nmt2opp `M` frozen
at `t` next to nmoutopp untimed `O`; intersection empty is only the already
displayed disjointness; reverse/face of each is only two leftover HOLDs;
union already answered one reverse from both letters; mixed `D` should make
face of `M` `UNDEFINED`; mixed `A` should make reverse of `O` `UNDEFINED`;
and empty intersection should make reverse `UNDEFINED`.

**Answer:** `M` at `τ` is earliest incoming from the record prefix and is
frozen, but `O` at `τ` is the timed outgoing dual at `t+1`, not untimed
eventual-`O`. Intersection empty is reported at the same cut as both sets.
Reverse and face of each are scored separately at that cut; they are not
nmunopp union and not nmot2opp composition. Mixed `M(D,τ)` remains
`{−e_2, +e_3, −e_3}` and face of `M` holds. Mixed `O(A,τ)` remains
`{+e_2, +e_3, −e_3}` and reverse of `O` holds. Empty intersection does not
empty those named sets.

### N8 — cross-cycle echo

nsmopp #7208 reported reverse hold and face hold from own incoming `M`.
nmt2opp reported those bits frozen from `t` to `t+1` with composition HOLD.
nmot2opp reported `O` empty at `t` then HOLD at `t+1` with composition fail.
nmoutopp reported untimed eventual-`O` hold/hold. nmunopp reported reverse
hold and face hold from the untimed union. This note is not those displays:
it reports `M` and `O` together at `τ=t+1`, empty intersection, reverse hold
and face hold from `M`, and reverse hold and face hold from `O`.

**Gate disposition:** PASS for the simultaneous incoming/outgoing `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals six-neighbor lock union,” “the predicate equals untimed
eventual-`O`,” “the predicate equals nmt2opp `M` frozen at `t`,” “the
predicate equals nmot2opp two-tick composition,” “the predicate equals
nmunopp union,” “bits are Admissibility,” “intersection is nonempty,”
“reverse of `M` fails,” “face of `M` is `UNDEFINED`,” “reverse of `O`
fails,” or “face of `O` is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsopp #7093 perp-step
incoming-lock process, reads each probe's own earliest incoming set and own
outgoing dual from the record prefix at that probe's `t+1`, reports the
intersection, lists new records in `B_3(0)` between `t` and `t+1` that meet
a probe's six-neighbors, and checks Theorems 1--3. It also checks that `M`
is frozen from `t` to `t+1`, that `O` is empty at `t` for `A`, `B`, and `C`,
that mixed sets remain sets, that unique-letter reverse of `O` is
`UNDEFINED`, that untimed eventual-`O` equals timed `O` at `t+1` but is not
this display, that the construction does not sum, that a formation member
from already-recorded six-neighbor locks is not attached, and that the
display is not the two-tick lock-count clock composition. No runner cache is
written.
