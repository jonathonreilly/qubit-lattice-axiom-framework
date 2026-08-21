---
claim_id: same_lock_yprobe_own_lock_in_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from own-lock-in exist-opposite on the four nssame y-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/same_lock_yprobe_own_lock_in_existential_opposite_reverse_face_2026_08_15.py
---

# Own-Lock-In Existential Opposite Reverse And Face On Four Nssame Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from own-lock-in exist-opposite on the four
nssame y-probes in `B_3(0)`. Let `t(q)` be the formation tick of probe `q`.
Let `L(q)` be `q`'s own unique incoming lock; seeds use seed letters. If
several earliest incoming steps exist, `L(q)` is `UNDEFINED`. At that tick,
`S^+(q)` is the set of locks of six-neighbors of `q` that formed at tick
`< t(q)` (strictly earlier), union `{L(q)}` when `L(q)` is defined. Reverse
holds if and only if some lock in `S^+(A)` is the vector opposite of some
lock in `S^+(B)`. Face holds if and only if some lock in `S^+(C)` is the
vector opposite of some lock in `S^+(D)`. Empty `S^+` on either side of a
comparison is `UNDEFINED`; nonempty with no opposite pair fails. Occupancy
`n` is not used. This is not named-sign lettering. This is not a unique
lock-vector leftover and not a sum leftover. This is not leftover of
formation-tick existential opposite that excludes `q`: that display leaves
`S(A)` empty and reports reverse `UNDEFINED`. This is not leftover of the
unique own-incoming lock-vector letters on these y-probes: that readout
requires a singleton incoming step and reports reverse fail with face
`UNDEFINED` at mixed `D`. This is not leftover of later-tick existential
opposite on these y-probes and is not later-tick seed-transfer: that leftover
waits for a global later T and reports reverse hold and face hold. This is
not leftover of own-lock-in existential opposite on the four nsopp y-probes:
that leftover holds both bits from seed letter `−e_1` at `A`. This is not
leftover of own-lock-in existential opposite on the four nnseed y-probes:
that leftover fails both bits from seed letter `+e_2` at `A`. Opposite seed
letters are not required by the construction; this first display asks whether
they are required for HOLD by scoring the same-letter seed `+e_1/+e_1`.
Uniqueness of incoming locks is not required. Uniqueness of the lock set is
not required. Displayed, not adopted. This note does not write existential
opposite into Admissibility and does not attach a formation member from
already-recorded six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/same_lock_yprobe_own_lock_in_existential_opposite_reverse_face_2026_08_15.py`](../scripts/same_lock_yprobe_own_lock_in_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
own-lock-in union sets. Named signs `{+,−}` are a coarser readout and are
not used. A singleton unique lock-vector letter is a different readout and
is not used. A `Z^3` sum of those locks is a different readout and is not
used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of S^+ as the union of strictly-earlier six-neighbor locks with L(q) when defined, on the four nssame y-probes, with reverse fail and face fail from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: same_lock_yprobe_own_lock_in_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from own-lock-in exist-opposite on the four nssame y-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with formation-tick leftover that excludes q, do not identify the sets with unique own-incoming leftover, do not identify the sets with later-tick leftover, and do not identify the sets with nsopp or nnseed y-probe own-lock-in leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of own-lock-in union sets on the four nssame y-probes; displayed, not adopted"
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
own-lock-in union sets are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
same-letter locks `L(0)=+e_1` and `L(0,1,0)=+e_1`. This seed is not the
opposite two-site seed `+e_1/−e_1`. This seed is not the nnseed two-site
seed `+e_1/+e_2`.

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

## Named existential opposite from own-lock-in union

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `L(q)` be `q`'s own unique incoming lock in `{±e_i}`. Seeds
use seed letters. If several earliest incoming steps exist, `L(q)` is
`UNDEFINED`. At the own formation tick of each probe `q`, let `S^+(q)` be
the set of locks of six-neighbors of `q` that formed at tick `< t(q)`
(strictly earlier), union `{L(q)}` when `L(q)` is defined. Same-tick partners
are not already recorded as neighbors. The probe itself is not a neighbor of
itself. This display does not wait for a global later T. This display does
not use occupancy `n`. Duplicate locks at two neighbors collapse in the set.
The construction does not require `S^+(q)` to be a singleton. It does not
sum `S^+(q)`. It is not a unique lock-vector leftover and not a sum leftover.
It is not leftover of formation-tick existential opposite that excludes `q`.
It is not leftover of unique own-incoming lock-vector letters on these
y-probes. It is not leftover of later-tick existential opposite. It is not
later-tick seed-transfer.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not scored on `{+,−}`
names and are not an occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  some a in S^+(A) and some b in S^+(B) with a+b=(0,0,0)
face     <=>  some c in S^+(C) and some d in S^+(D) with c+d=(0,0,0)
```

If `S^+(A)` or `S^+(B)` is empty, reverse is `UNDEFINED`. Else reverse fails
if no such pair exists. If `S^+(C)` or `S^+(D)` is empty, face is
`UNDEFINED`. Else face fails if no such pair exists. The report is one of
`hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility.

## Theorem 1 — formation ticks, own incoming locks, and S^+ at each y-probe

Direct enumeration of the displayed nssame process on `B_3(0)` forms all four
y-probes. The formation ticks are `t(A)=0`, `t(B)=2`, `t(C)=1`, `t(D)=3`.
`A` is a seed. Those ticks locate the already-recorded six-neighbor set.
They are not occupancy kernels and are not a global later T.

Own incoming locks and own-lock-in union sets at each probe's own formation
tick are:

```text
A: seed letter +e_1; earlier neighbors empty;
   t(A)=0;  L(A) = +e_1;  S^+(A) = {+e_1}
B: incoming +e_1; +e_3 at (0, 1, 1);
   t(B)=2;  L(B) = +e_1;  S^+(B) = {+e_1, +e_3}
C: incoming +e_2; +e_1 at (0, 1, 0);
   t(C)=1;  L(C) = +e_2;  S^+(C) = {+e_1, +e_2}
D: incoming −e_2, −e_3, +e_3; +e_1 at (0, 1, 0), +e_1 at (1, 2, 0),
   +e_1 at (1, 1, 1), +e_1 at (1, 1, -1);
   t(D)=3;  L(D) = UNDEFINED;  S^+(D) = {+e_1}
```

`A` is a seed at tick 0. Its six-neighbors are the same-tick partner at the
origin and later sites. Same-tick is not already-recorded, so the strictly-
earlier neighbor set is empty. `L(A)` is the seed letter `+e_1`, so
`S^+(A)={+e_1}`. `B`'s already-recorded neighbor locks `+e_3` at `(0, 1, 1)`,
and `L(B)=+e_1`, so `S^+(B)={+e_1, +e_3}`. `C`'s already-recorded neighbor is
the seed `A` locking `+e_1`, and `L(C)=+e_2`, so `S^+(C)={+e_1, +e_2}`. `D`'s
already-recorded neighbors are four copies of `+e_1`, and `L(D)` is
`UNDEFINED` from three earliest incoming steps, so `S^+(D)={+e_1}`. Mixed
remains a set at `B`. Uniqueness is not required at `D`.

Incoming locks exist and need not be unique (`D` has three earliest incoming
steps `−e_2`, `−e_3`, and `+e_3`). That non-uniqueness leaves `L(D)`
`UNDEFINED` and does not empty `S^+(D)`. Uniqueness is not required.

Reverse HOLD does not use L(A). The own–own channel reads `L(A)=+e_1`
against `L(B)=+e_1` and fails: same letter is not opposite. The own–neighbor
channel that would read `L(A)=+e_1` against an earlier lock at `B` does not
fire: `S^+(B)={+e_1, +e_3}` has no `−e_1`. Neighbor–neighbor reverse is
`UNDEFINED` because the strictly-earlier set at `A` is empty. Including
`L(A)` fills that empty set and turns reverse from `UNDEFINED` into fail.
Reverse therefore fails on the union sets and does not hold.

The unique own-incoming letters on these same y-probes are `+e_1`, `+e_1`,
`+e_2`, `UNDEFINED`. Those are different objects: `S^+(B)` is
`{+e_1, +e_3}` and `S^+(C)` is `{+e_1, +e_2}`. Formation-tick existential
opposite that excludes `q` reports empty `S(A)`, not `{+e_1}`. Later-tick
existential opposite on these same y-probes reports
`{+e_1, +e_2, −e_2, +e_3, −e_3}` at `A` after waiting for a global later T.
Own-lock-in existential opposite on the four nsopp y-probes reports `{−e_1}`
at seed `A=(0,1,0)`. Own-lock-in existential opposite on the four nnseed
y-probes reports `{+e_2}` at seed `A`.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S^+(A)` and `b` in
`S^+(B)` with `a+b=(0,0,0)`. Both sets are nonempty: `S^+(A)={+e_1}` and
`S^+(B)={+e_1, +e_3}`. The pairs are `+e_1+(+e_1)=(2,0,0)` and
`+e_1+(+e_3)=(1,0,1)`. No pair is opposite. Reverse fails.

Reverse: fail

This is not `hold` and not `UNDEFINED`. Reverse HOLD does not use L(A):
`L(A)=+e_1` has no opposite in `S^+(B)`, own–own is fail at same-letter
`+e_1/+e_1`, and neighbor–neighbor reverse is `UNDEFINED` on empty earlier
`S(A)`. This is not leftover of formation-tick existential opposite that
excludes `q`: that leftover leaves `S(A)` empty and reports reverse
`UNDEFINED`. Unique lock-vector lettering of the union sets would report
reverse `UNDEFINED` because `B` mixes. A sum leftover of the same lists
would replace `S^+(A)` by `+e_1` and `S^+(B)` by `(1,0,1)` and would also
fail reverse, for a different reason. Unique own-incoming letters on these
y-probes report reverse fail from `L(A)=+e_1` against `L(B)=+e_1`; that
leftover is a different object because its face report at mixed `D` is
`UNDEFINED`. Later-tick existential opposite on these same y-probes reports
reverse hold on different lists that wait for a global later T; that leftover
is later-tick seed-transfer, not this display. Own-lock-in on the four nsopp
y-probes reports reverse hold from seed letter `−e_1` at `A` opposite `+e_1`
at `B`. Own-lock-in on the four nnseed y-probes reports reverse fail from
seed letter `+e_2` at `A` with no opposite in `S^+(B)`. Opposite seed letters
are not supplied here; reverse fails.

Reverse fails.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S^+(C)` and `d` in `S^+(D)`
with `c+d=(0,0,0)`. Both sets are nonempty: `S^+(C)={+e_1, +e_2}` and
`S^+(D)={+e_1}`. The pairs are `+e_1+(+e_1)=(2,0,0)` and
`+e_2+(+e_1)=(1,1,0)`. No pair is opposite. Face fails.

Face: fail

Displayed, not adopted. The bits are not written into Admissibility.

This is not `hold` and not `UNDEFINED`. Own-lock-in fills `C` with
`L(C)=+e_2` and does not flip face: the exclude-`q` sets already fail face
as `{+e_1}` against `{+e_1}`, and adding `+e_2` still supplies no `−e_1`.
Own–own face is `UNDEFINED` because `L(D)` is `UNDEFINED`. Unique
own-incoming letters on these same y-probes assign `L(D)=UNDEFINED` from
three earliest incoming steps and report face `UNDEFINED`. Unique lock-vector
lettering of the union sets would report face `UNDEFINED` because `C` mixes.
A sum leftover would replace `S^+(C)` by `(1,1,0)` and `S^+(D)` by `+e_1`
and would also fail face, for a different reason. Named-sign lettering lost
the axis: `C+` against `D+` does not keep the axis of `+e_1`. Formation-tick
existential opposite that excludes `q` also reports face fail, but from
`{+e_1}` at `C` rather than `{+e_1, +e_2}`. Later-tick existential opposite
reports face hold after a global later T on a different set at `C` that
includes `−e_1`. Own-lock-in on the four nsopp y-probes reports face hold
from `−e_1` at `C` against `+e_1` at `D`. Face fails from the own-lock-in
union at these nssame y-probes; it does not wait for a later-tick
seed-transfer of `−e_1`.

Face fails.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the own-lock-in union set to be a singleton.
- It does not sum the own-lock-in union set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  lock vectors.
- It does not reprint unique own-incoming lock-vector letters on these
  y-probes.
- It does not reprint formation-tick existential opposite that excludes `q`.
- It does not wait for a global later T.
- It does not reprint later-tick existential opposite on these y-probes.
- It does not reprint own-lock-in existential opposite on the four nsopp
  y-probes.
- It does not reprint own-lock-in existential opposite on the four nnseed
  y-probes.
- It does not reprint own-lock-in on the four nssame x-probes.
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
nssame process, the own-lock-in union sets, and the existential-opposite
reverse/face predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/+e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| own incoming locks `L(A)`, `L(B)`, `L(C)`, `L(D)` | Theorem 1; `+e_1`, `+e_1`, `+e_2`, `UNDEFINED` |
| lock sets `S^+(A)`, `S^+(B)`, `S^+(C)`, `S^+(D)` | Theorem 1; `{+e_1}`, `{+e_1, +e_3}`, `{+e_1, +e_2}`, `{+e_1}` |
| reverse HOLD uses `L(A)` (own–neighbor or own–own) or only neighbor–neighbor | Theorem 1; reverse does not hold; does not use L(A); neighbor–neighbor is `UNDEFINED` |
| reverse and face | Theorems 2–3; `fail` / `fail` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique own-incoming letters on these y-probes | not this display |
| leftover of formation-tick existential opposite that excludes `q` | not this display |
| leftover of later-tick existential opposite on these y-probes | not this display |
| leftover of own-lock-in existential opposite on the four nsopp y-probes | not this display |
| leftover of own-lock-in existential opposite on the four nnseed y-probes | not this display |
| leftover of nssame x-probe own-lock-in existential opposite | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: own-lock-in exist-opposite on the four nssame y-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed own-lock-in existential-opposite reverse/face report on these four nssame y-probes. |
| V3 | Own-lock-in union sets and the `fail`/`fail` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the union of strictly-earlier six-neighbor lock vectors with `L(q)` when defined and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique
own-incoming letters, does not reprint formation-tick leftover that excludes
`q`, does not reprint later-tick leftover, does not reprint nsopp y-probe
own-lock-in leftover, does not reprint nnseed y-probe own-lock-in leftover,
and does not use occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same union sets | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while the mixed union sets are nonempty and both bits fail |
| sum of the same union sets | replace `S^+` by the `Z^3` sum | refused; leftover; sum of `S^+(A)` is `+e_1` and sum of `S^+(B)` is `(1,0,1)`; sum of `S^+(C)` is `(1,1,0)` and sum of `S^+(D)` is `+e_1`; those sums also fail, but they are a different readout |
| named-sign lettering of the same union sets | map `±e_i` to `{+,−}` | refused; lost the axis; `A+` against `B+` and `C+` against `D+` drop the axis of `+e_1` |
| unique own-incoming lock-vector leftover on these y-probes | reuse `L(A)=+e_1`, `L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` | refused; different object; that leftover reports reverse fail and face `UNDEFINED` while own-lock-in reverse fails and face fails |
| leftover of formation-tick existential opposite that excludes `q` | reuse empty `S(A)` with reverse `UNDEFINED` | refused; different set; `S^+(A)={+e_1}` and reverse fails |
| leftover of later-tick existential opposite | reuse global later T and reverse hold with face hold | refused; different sets; this display does not wait for a global later T and is not later-tick seed-transfer |
| leftover of own-lock-in existential opposite on the four nsopp y-probes | reuse seed letter `−e_1` at `A` with reverse hold and face hold | refused; different process; nssame seed letter at `A` is `+e_1` and reverse fails |
| leftover of own-lock-in existential opposite on the four nnseed y-probes | reuse seed letter `+e_2` at `A` with reverse fail and face fail | refused; different process; nssame seed letter at `A` is `+e_1` |
| leftover of nssame x-probe own-lock-in | reuse x-probes with reverse fail and face fail | refused; different frame; y-probe `A` is a seed |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `S^+` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; all three earliest incoming steps at `D` are kept and `L(D)` is `UNDEFINED` |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `+e_1`, perpendicular step
rule, incoming-step lock, formation-tick lock set of six-neighbors formed
strictly earlier than each probe's own `t`, union with `L(q)` when defined,
existential opposite, four y-probes with seed `A`, and reverse/face as
existence of a pair that sums to zero are declared. No uniqueness of incoming
locks, no occupancy `n`, no named-sign reduction, no singleton leftover, no
sum leftover, no unique own-incoming leftover, no formation-tick exclude-`q`
leftover, no later-tick leftover, no later-tick seed-transfer, no nsopp
y-probe own-lock-in leftover, no nnseed y-probe own-lock-in leftover, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in an own-lock-in union set | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four lock sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** The union is leftover of unique own-incoming letters plus
formation-tick neighbor locks, mixed neighbor locks should make reverse and
face `UNDEFINED`, the sets should be replaced by their sums, unique
own-incoming letters already answered reverse fail with face `UNDEFINED`,
formation-tick existential opposite already answered the exist-opposite
question with reverse `UNDEFINED`, later-tick existential opposite already
answered with hold/hold so this is leftover later-tick seed-transfer, nsopp
y-probe own-lock-in already answered with hold/hold because `A` is a seed,
nnseed y-probe own-lock-in already answered with fail/fail because `A` is a
seed, named signs should suffice because they keep orientation, occupancy
`n` should track that vector, and reverse HOLD must use `L(A)`.

**Answer:** The named construction reports lock sets `{+e_1}`, `{+e_1, +e_3}`,
`{+e_1, +e_2}`, `{+e_1}` at `A,B,C,D` from strictly-earlier six-neighbor
locks union `{L(q)}` when defined. Mixed remains a set. The construction
does not sum. Occupancy `n` is not used. Named signs lost the axis. No pair
from `S^+(A)` and `S^+(B)` is opposite, so reverse fails. Reverse HOLD does
not use L(A): `L(A)=+e_1` has no opposite in `S^+(B)`, and neighbor–neighbor
is `UNDEFINED` on empty earlier `S(A)`. No pair from `S^+(C)` and `S^+(D)`
is opposite, so face fails. Formation-tick leftover that excludes `q` leaves
`S(A)` empty and reverse `UNDEFINED`. Unique own-incoming leftover reports
face `UNDEFINED`. Later-tick leftover waits for a global later T and holds
both bits. Nsopp y-probe own-lock-in holds reverse from a different seed
letter `−e_1`. Nnseed y-probe own-lock-in fails reverse from a different
seed letter `+e_2`. The sets are not those leftovers. Opposite seed letters
are not supplied; both bits fail. The bits remain displayed. Incoming-lock
uniqueness is not required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same nssame y-probes
assigned `L(A)=+e_1`, `L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` and
reported reverse fail with face `UNDEFINED`. A formation-tick existential
opposite display that excludes `q` assigned empty `S(A)` and `{+e_1}` at
`C` and at `D` and reported reverse `UNDEFINED` with face fail. Later-tick
existential opposite on these y-probes reported reverse hold and face hold
on different later sets `{+e_1, +e_2, −e_2, +e_3, −e_3}` and
`{+e_1, −e_1, +e_2, +e_3, −e_3}` after a global later T. Own-lock-in
existential opposite on the four nsopp y-probes reported reverse hold and
face hold from seed letter `−e_1` at `A=(0,1,0)`. Own-lock-in existential
opposite on the four nnseed y-probes reported reverse fail and face fail
from seed letter `+e_2` at `A`. Unique lock-vector lettering of the union
sets would report reverse `UNDEFINED` and face `UNDEFINED` because `B` and
`C` mix. A sum leftover of the same lists would report reverse fail and face
fail because the sums are `+e_1` with `(1,0,1)` and `(1,1,0)` with `+e_1`.
This note is not those displays: mixed remains a set, the construction does
not sum, `S^+(A)` is nonempty from the seed letter `+e_1`, reverse fails,
reverse HOLD does not use L(A), and face fails.

**Gate disposition:** PASS for the own-lock-in union existential-opposite
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals the sum of the lock set,” “bits are Admissibility,” “the
letter is occupancy `n`,” “the sets equal unique own-incoming letters,” “the
sets equal formation-tick leftover that excludes `q`,” “the sets equal
later-tick leftover,” “reverse is `hold`,” or “face is `hold`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nssame two-site
perp-step incoming-lock process, reads each probe's own unique incoming lock
or `UNDEFINED`, collects six-neighbor locks formed strictly earlier than
each probe's own formation tick, unions those locks with `{L(q)}` when
defined, reads the union sets at the four y-probes, and checks Theorems
1--3. It also checks that reverse HOLD does not use L(A), that the
construction is not named-sign lettering, that mixed sets remain defined,
that the construction does not sum, that occupancy `n` is not used, that a
formation member from already-recorded six-neighbor locks is not attached,
that the sets are not leftover of unique own-incoming letters, that the sets
are not leftover of formation-tick existential opposite that excludes `q`,
that the sets are not leftover of later-tick existential opposite, and that
the sets are not leftover of nsopp y-probe own-lock-in. No runner cache is
written.
