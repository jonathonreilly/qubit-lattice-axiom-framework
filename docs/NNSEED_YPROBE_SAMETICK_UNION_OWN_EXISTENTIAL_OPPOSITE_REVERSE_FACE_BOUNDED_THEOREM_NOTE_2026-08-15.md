---
claim_id: nnseed_yprobe_sametick_union_own_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from same-tick-inclusive 6-NN locks union own incoming lock on the four nnseed y-probes, no global T, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/nnseed_yprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py
---

# Same-Tick-Inclusive Union Own Incoming Reverse And Face On Four Nnseed Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from same-tick-inclusive six-neighbor locks union
the probe's own incoming lock on the four nnseed y-probes in `B_3(0)`, no
global T. Let `t(q)` be the formation tick of probe `q`. Let `L(q)` be `q`'s
own unique incoming lock; seeds use seed letters. If several earliest
incoming steps exist, `L(q)` is `UNDEFINED`. At that tick, `S^+(q)` is the
set of locks of six-neighbors of `q` that formed at tick `<= t(q)` and are
not `q`, union `{L(q)}` when `L(q)` is defined. Reverse holds if and only if
some lock in `S^+(A)` is the vector opposite of some lock in `S^+(B)`. Face
holds if and only if some lock in `S^+(C)` is the vector opposite of some
lock in `S^+(D)`. Empty `S^+` on either side of a comparison is `UNDEFINED`;
nonempty with no opposite pair fails. Occupancy `n` is not used. This is
not named-sign lettering. This is not a unique lock-vector leftover and not
a sum leftover. This is not leftover of same-tick-inclusive existential
opposite that excludes `q`: that display reports `{+e_1}` at seed `A` from
the origin partner and still fails reverse. This is not leftover of
strictly-earlier own-lock-in: that display takes tick `< t(q)` union own
lock and reports `S^+(A)={+e_2}` without the same-tick origin partner.
This is not leftover of later-tick union own: that display waits for a
global later T equal to the max of the four formation ticks and reports
reverse hold and face hold. This is not later-tick leftover and is not
later-tick seed-transfer. This is not leftover of the unique own-incoming
lock-vector letters on these y-probes: that readout requires a singleton
incoming step and reports reverse `UNDEFINED` with face `UNDEFINED` at
mixed `B` and mixed `C`. This is not leftover of own-lock-in existential
opposite on the four nsopp y-probes: that leftover holds both bits from
seed letter `−e_1` at `A`. Uniqueness of incoming locks is not required.
Uniqueness of the lock set is not required. Displayed, not adopted. This
note does not write existential opposite into Admissibility and does not
attach a formation member from already-recorded six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/nnseed_yprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py`](../scripts/nnseed_yprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
same-tick-inclusive six-neighbor lock sets union the probe's own incoming
lock when defined. Named signs `{+,−}` are a coarser readout and are not
used. A singleton unique lock-vector letter is a different readout and is
not used. A `Z^3` sum of those locks is a different readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of S^+ as same-tick-inclusive six-neighbor locks union L(q) when defined, on the four nnseed y-probes at each probe's own t, no global T, with reverse fail and face fail from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: nnseed_yprobe_sametick_union_own_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from same-tick-inclusive 6-NN locks union own incoming lock on the four nnseed y-probes, no global T, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with same-tick leftover that excludes q, do not identify the sets with strictly-earlier own-lock-in leftover, and do not identify the sets with later-tick union own leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of same-tick-inclusive six-neighbor locks union own incoming lock on the four nnseed y-probes, no global T; displayed, not adopted"
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
same-tick-inclusive union sets are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
perp-consistent locks `L(0)=+e_1` and `L(0,1,0)=+e_2`. This seed is not the
opposite two-site seed `+e_1/−e_1`.

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

## Named existential opposite from same-tick-inclusive six-neighbor locks union own incoming lock

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `L(q)` be `q`'s own unique incoming lock in `{±e_i}`. Seeds
use seed letters. If several earliest incoming steps exist, `L(q)` is
`UNDEFINED`. At the own formation tick of each probe `q`, let `S^+(q)` be
the set of locks of six-neighbors of `q` that formed at tick `<= t(q)`
(same-tick-inclusive) and are not `q`, union `{L(q)}` when `L(q)` is defined.
Same-tick partners are kept when they are neighbors. The probe itself is
excluded from the neighbor set and re-enters only through `{L(q)}` when
that letter is defined. This display does not wait for a global later T.
This display does not use occupancy `n`. Duplicate locks collapse in the
set. The construction does not require `S^+(q)` to be a singleton. It does
not sum `S^+(q)`. It is not a unique lock-vector leftover and not a sum
leftover. It is not leftover of same-tick-inclusive existential opposite
that excludes `q`. It is not leftover of strictly-earlier own-lock-in. It
is not leftover of later-tick union own. It is not later-tick leftover. It
is not leftover of unique own-incoming lock-vector letters on these
y-probes. It is not leftover of own-lock-in existential opposite on the
four nsopp y-probes.

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

Direct enumeration of the displayed nnseed process on `B_3(0)` forms all four
y-probes. The formation ticks are `t(A)=0`, `t(B)=2`, `t(C)=3`,
`t(D)=1`. `A` is a seed. Those ticks locate the same-tick-inclusive
six-neighbor set. They are not occupancy kernels and are not a global later
T.

Own incoming locks and same-tick-inclusive union sets at each probe's own
formation tick are:

```text
A: +e_1 at (0, 0, 0); seed letter +e_2;
   t(A)=0;  L(A) = +e_2;  S^+(A) = {+e_1, +e_2}
B: +e_3 at (0, 1, 1), +e_1 at (1, 0, 1), +e_1 at (1, 1, 0);
   incoming +e_1, +e_3;
   t(B)=2;  L(B) = UNDEFINED;  S^+(B) = {+e_1, +e_3}
C: incoming −e_1, −e_3, +e_3, +e_1; +e_2 at (1, 2, 0), +e_2 at (-1, 2, 0),
   +e_2 at (0, 1, 0), +e_2 at (0, 2, 1), +e_2 at (0, 2, -1);
   t(C)=3;  L(C) = UNDEFINED;  S^+(C) = {+e_2}
D: incoming +e_1; +e_2 at (0, 1, 0);
   t(D)=1;  L(D) = +e_1;  S^+(D) = {+e_1, +e_2}
```

`A` is a seed at tick 0. Its same-tick partner at the origin is a
six-neighbor locking `+e_1`. Same-tick-inclusive leftover that excludes `q`
reports `{+e_1}` at `A`. `L(A)` is the seed letter `+e_2`, so
`S^+(A)={+e_1, +e_2}`. Reverse HOLD does not use L(A): the own–own channel
is unavailable because `L(B)` is `UNDEFINED`, the own–neighbor channel that
would read `L(A)=+e_2` against a same-tick-inclusive lock at `B` does not
fire because `S^+(B)={+e_1, +e_3}` has no `−e_2`, and neighbor–neighbor
reverse also fails because `{+e_1}` at `A` has no opposite in `S^+(B)`.
`B` keeps the earlier neighbor `(0, 1, 1)` locking `+e_3`, the same-tick
neighbor `(1, 0, 1)` locking `+e_1`, and the earlier neighbor `(1, 1, 0)`
locking `+e_1`; `L(B)` is `UNDEFINED` from two earliest incoming steps, so
`S^+(B)={+e_1, +e_3}`. `C`'s already-recorded neighbors are five copies of
`+e_2`, including the seed `A`, and `L(C)` is `UNDEFINED` from four earliest
incoming steps, so `S^+(C)={+e_2}`. `D`'s already-recorded neighbor is the
seed `A` locking `+e_2`, and `L(D)=+e_1`, so `S^+(D)={+e_1, +e_2}`. Mixed
remains a set at `B` and at `D`.

Incoming locks exist and need not be unique (`B` has two earliest incoming
steps `+e_1` and `+e_3`; `C` has four earliest incoming steps `±e_1` and
`±e_3`). That non-uniqueness leaves `L(B)` and `L(C)` `UNDEFINED` and does
not empty `S^+(B)` or `S^+(C)`. Uniqueness is not required.

The unique own-incoming letters on these same y-probes are `+e_2`,
`UNDEFINED`, `UNDEFINED`, `+e_1`. Those are different objects: `S^+(A)` is
not `{+e_2}`, and `S^+(B)` is nonempty. Same-tick-inclusive leftover that
excludes `q` reports `{+e_1}` at `A` and reverse fail. Strictly-earlier
own-lock-in reports `{+e_2}` at `A` without the same-tick origin partner.
Later-tick union own reports `{+e_1, −e_1, +e_2, +e_3, −e_3}` at `A` after
waiting for a global later T. Own-lock-in existential opposite on the four
nsopp y-probes reports `{−e_1}` or `{+e_1, −e_1}` at seed `A=(0,1,0)`.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S^+(A)` and `b` in
`S^+(B)` with `a+b=(0,0,0)`. Both sets are nonempty: `S^+(A)={+e_1, +e_2}`
and `S^+(B)={+e_1, +e_3}`. The pairs are `+e_1+(+e_1)=(2,0,0)`,
`+e_1+(+e_3)=(1,0,1)`, `+e_2+(+e_1)=(1,1,0)`, and `+e_2+(+e_3)=(1,1,1)`.
No pair is opposite. Reverse fails.

Reverse: fail

Reverse HOLD does not use L(A). Same-tick-inclusive leftover that excludes
`q` leaves `S(A)={+e_1}` and also reports reverse fail. Including `L(A)=+e_2`
does not create an opposite pair with `S^+(B)`. Holding reverse on these
nnseed y-probes still needs a global later T: later-tick union own reports
reverse hold from `−e_1` at `A` after waiting for T equal to the max of the
four formation ticks. That later-tick leftover is not this display.

This is not `hold` and not `UNDEFINED`. This is not leftover of
same-tick-inclusive existential opposite that excludes `q`. Unique
lock-vector lettering of the same union sets would report reverse
`UNDEFINED` because both sides mix. A sum leftover of the same lists would
replace `S^+(A)` by `(1,1,0)` and `S^+(B)` by `(1,0,1)` and would also fail
reverse, for a different reason. Unique own-incoming letters on these
y-probes report reverse `UNDEFINED` from mixed `B`. Strictly-earlier
own-lock-in also reports reverse fail, but from `{+e_2}` at `A` without the
same-tick origin partner. Later-tick union own reports reverse hold on a
later five-lock set at `A`. Own-lock-in on the four nsopp y-probes reports
reverse hold from seed letter `−e_1` at `A` opposite `+e_1` at `B`. Reverse
fails because neither `+e_1` nor `+e_2` at `A` has an opposite in `S^+(B)`.

Reverse fails.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S^+(C)` and `d` in `S^+(D)`
with `c+d=(0,0,0)`. Both sets are nonempty: `S^+(C)={+e_2}` and
`S^+(D)={+e_1, +e_2}`. The pairs are `+e_2+(+e_1)=(1,1,0)` and
`+e_2+(+e_2)=(0,2,0)`. No pair is opposite. Face fails.

Face: fail

Displayed, not adopted. The bits are not written into Admissibility.

This is not `hold` and not `UNDEFINED`. Same-tick-inclusive leftover that
excludes `q` already fails face as `{+e_2}` against `{+e_2}`. Including
`L(D)=+e_1` still supplies no `−e_2`. Own–own face is `UNDEFINED` because
`L(C)` is `UNDEFINED`. Unique own-incoming letters on these same y-probes
assign `L(C)=UNDEFINED` from four earliest incoming steps and report face
`UNDEFINED`. Unique lock-vector lettering of the union sets would also
report face `UNDEFINED` because `D` mixes. A sum leftover would replace
`S^+(C)` by `+e_2` and `S^+(D)` by `(1,1,0)` and would also fail face, for
a different reason. Named-sign lettering lost the axis: `C+` against `D+`
does not keep the axis of `+e_2`. Strictly-earlier own-lock-in also reports
face fail from the same `{+e_2}` against `{+e_1, +e_2}`. Later-tick union
own reports face hold after a global later T on a different set at `D` that
includes `−e_2`. Own-lock-in on the four nsopp y-probes reports face hold
from `−e_1` at `C` against `+e_1` at `D`. Face fails from the same-tick-
inclusive union at these nnseed y-probes; it does not wait for a later-tick
seed-transfer of `−e_2`. Holding face on these nnseed y-probes still needs
a global later T.

Face fails.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the same-tick-inclusive union set to be a singleton.
- It does not sum the same-tick-inclusive union set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  lock vectors.
- It does not reprint unique own-incoming lock-vector letters on these
  y-probes.
- It does not reprint same-tick-inclusive existential opposite that excludes
  `q`.
- It does not reprint strictly-earlier own-lock-in.
- It does not reprint later-tick union own.
- It does not wait for a global later T.
- It does not reprint later-tick existential opposite on these y-probes.
- It does not reprint own-lock-in existential opposite on the four nsopp
  y-probes.
- It does not reprint same-tick-inclusive union own on the four nnseed
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
nnseed process, the same-tick-inclusive union sets, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_1/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `3`, `1` |
| own incoming locks `L(A)`, `L(B)`, `L(C)`, `L(D)` | Theorem 1; `+e_2`, `UNDEFINED`, `UNDEFINED`, `+e_1` |
| lock sets `S^+(A)`, `S^+(B)`, `S^+(C)`, `S^+(D)` | Theorem 1; `{+e_1, +e_2}`, `{+e_1, +e_3}`, `{+e_2}`, `{+e_1, +e_2}` |
| reverse HOLD uses `L(A)` (own–neighbor or own–own) or only neighbor–neighbor | Theorem 1; reverse does not hold; does not use L(A); neighbor–neighbor fails |
| reverse and face | Theorems 2–3; `fail` / `fail` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique own-incoming letters on these y-probes | not this display |
| leftover of same-tick-inclusive existential opposite that excludes `q` | not this display |
| leftover of strictly-earlier own-lock-in | not this display |
| leftover of later-tick union own | not this display |
| leftover of later-tick existential opposite on these y-probes | not this display |
| leftover of own-lock-in existential opposite on the four nsopp y-probes | not this display |
| leftover of nnseed x-probe same-tick-inclusive union own | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: same-tick-inclusive 6-NN locks union own incoming lock on the four nnseed y-probes, no global T, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed same-tick-inclusive union-own-lock existential-opposite reverse/face report on these four nnseed y-probes. |
| V3 | Same-tick-inclusive union sets and the `fail`/`fail` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads same-tick-inclusive six-neighbor lock vectors union `L(q)` when defined and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique
own-incoming letters, does not reprint same-tick leftover that excludes
`q`, does not reprint strictly-earlier own-lock-in, does not reprint
later-tick union own, and does not use occupancy `n`. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same union sets | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while the mixed union sets are nonempty and both bits fail |
| sum of the same union sets | replace `S^+` by the `Z^3` sum | refused; leftover; sum of `S^+(A)` is `(1,1,0)` and sum of `S^+(B)` is `(1,0,1)`; sum of `S^+(C)` is `+e_2` and sum of `S^+(D)` is `(1,1,0)`; those sums also fail, but they are a different readout |
| named-sign lettering of the same union sets | map `±e_i` to `{+,−}` | refused; lost the axis; `A+` against `B+` and `C+` against `D+` drop the axis of `+e_2` |
| unique own-incoming lock-vector leftover on these y-probes | reuse `L(A)=+e_2`, `L(B)=UNDEFINED`, `L(C)=UNDEFINED`, `L(D)=+e_1` | refused; different object; that leftover reports reverse `UNDEFINED` and face `UNDEFINED` while same-tick union reverse fails and face fails |
| leftover of same-tick-inclusive existential opposite that excludes `q` | reuse `S(A)={+e_1}` with reverse fail | refused; different set; `S^+(A)={+e_1, +e_2}` |
| leftover of strictly-earlier own-lock-in | reuse tick `< t(q)` union own lock with `S^+(A)={+e_2}` | refused; different set; this display keeps the same-tick origin partner |
| leftover of later-tick union own | reuse global later T and reverse hold with face hold | refused; different sets; this display does not wait for a global later T and is not later-tick seed-transfer |
| leftover of own-lock-in existential opposite on the four nsopp y-probes | reuse seed letter `−e_1` at `A` with reverse hold and face hold | refused; different process; nnseed seed letter at `A` is `+e_2` and reverse fails |
| leftover of nnseed x-probe same-tick-inclusive union own | reuse x-probes with reverse fail and face hold | refused; different frame; y-probe `A` is a seed and face fails |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `S^+` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; both earliest incoming steps at `B` and all four at `C` are kept and `L(B)`, `L(C)` are `UNDEFINED` |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `+e_2`, perpendicular step
rule, incoming-step lock, same-tick-inclusive lock set of six-neighbors formed
at tick `<=` each probe's own `t` with the probe excluded, union with `L(q)`
when defined, existential opposite, four y-probes with seed `A`, and
reverse/face as existence of a pair that sums to zero are declared. No
uniqueness of incoming locks, no occupancy `n`, no named-sign reduction, no
singleton leftover, no sum leftover, no unique own-incoming leftover, no
same-tick exclude-`q` leftover, no strictly-earlier own-lock-in leftover, no
later-tick leftover, no later-tick seed-transfer, no nsopp y-probe own-lock-in
leftover, no global later T, no formation attachment from already-recorded
six-neighbor locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in a same-tick-inclusive union set | no continuum alphabet |
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
same-tick neighbor locks, mixed neighbor locks should make reverse and
face `UNDEFINED`, the sets should be replaced by their sums, unique
own-incoming letters already answered reverse `UNDEFINED` with face
`UNDEFINED`, same-tick-inclusive existential opposite already answered the
exist-opposite question with reverse fail, strictly-earlier own-lock-in
already answered the union question without same-tick partners and with
fail/fail, later-tick union own already answered the union question after a
global T with hold/hold so this is leftover later-tick seed-transfer, nsopp
y-probe same-tick union own already answered with hold/hold because `A` is a
seed, named signs should suffice because they keep orientation, occupancy
`n` should track that vector, reverse HOLD must use `L(A)`, and later T is
not needed once the own lock is included.

**Answer:** The named construction reports lock sets `{+e_1, +e_2}`,
`{+e_1, +e_3}`, `{+e_2}`, `{+e_1, +e_2}` at `A,B,C,D` from
same-tick-inclusive six-neighbor locks union `{L(q)}` when defined. Mixed
remains a set. The construction does not sum. Occupancy `n` is not used.
Named signs lost the axis. No pair from `S^+(A)` and `S^+(B)` is opposite,
so reverse fails. Reverse HOLD does not use L(A): `L(A)=+e_2` has no
opposite in `S^+(B)`, and neighbor–neighbor also fails. No pair from
`S^+(C)` and `S^+(D)` is opposite, so face fails. Same-tick leftover that
excludes `q` leaves `S(A)={+e_1}` without the seed letter. Strictly-earlier
own-lock-in reports `{+e_2}` at `A` without the same-tick origin partner.
Later-tick leftover waits for a global later T and holds both bits. Nsopp
y-probe same-tick union own holds reverse from a different seed letter
`−e_1`. Including the own lock is not enough to hold reverse on these
nnseed y-probes; holding reverse still needs a global later T. The sets are
not those leftovers. The bits remain displayed. Incoming-lock uniqueness is
not required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same nnseed y-probes
assigned `L(A)=+e_2`, `L(B)=UNDEFINED`, `L(C)=UNDEFINED`, `L(D)=+e_1` and
reported reverse `UNDEFINED` with face `UNDEFINED`. A same-tick-inclusive
existential opposite display that excludes `q` assigned `{+e_1}` at `A` and
`{+e_2}` at `C` and at `D` and reported reverse fail with face fail.
Strictly-earlier own-lock-in assigned `{+e_2}`, `{+e_1, +e_3}`, `{+e_2}`,
`{+e_1, +e_2}` and reported reverse fail with face fail. Later-tick union
own reported reverse hold and face hold on different later sets
`{+e_1, −e_1, +e_2, +e_3, −e_3}` and `{+e_1, +e_2, −e_2, +e_3, −e_3}` after
a global later T. Own-lock-in existential opposite on the four nsopp
y-probes reported reverse hold and face hold from seed letter `−e_1` at
`A=(0,1,0)`. Unique lock-vector lettering of the union sets would report
reverse `UNDEFINED` and face `UNDEFINED` because `A`, `B`, and `D` mix. A
sum leftover of the same lists would report reverse fail and face fail
because the sums are `(1,1,0)` with `(1,0,1)` and `+e_2` with `(1,1,0)`.
This note is not those displays: mixed remains a set, the construction does
not sum, `S^+(A)` includes the seed letter and the same-tick origin partner,
reverse fails, reverse HOLD does not use L(A), and face fails.

**Gate disposition:** PASS for the same-tick-inclusive six-neighbor-lock union
own incoming existential-opposite reverse/face reports above. FAIL / DO NOT SHIP
for “the predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals the sum of the lock set,”
“bits are Admissibility,” “the letter is occupancy `n`,” “the sets equal
unique own-incoming letters,” “the sets equal same-tick leftover that
excludes `q`,” “the sets equal strictly-earlier own-lock-in,” “the sets
equal later-tick union own,” “reverse is `hold`,” or “face is `hold`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nnseed two-site
perp-step incoming-lock process, reads each probe's own unique incoming lock
or `UNDEFINED`, collects six-neighbor locks formed at tick `<=` each probe's
own formation tick with the probe excluded, unions those locks with `{L(q)}`
when defined, reads the union sets at the four y-probes, reports whether
reverse HOLD uses L(A), and checks Theorems 1--3. It also checks that the
construction is not named-sign lettering, that mixed sets remain defined,
that the construction does not sum, that occupancy `n` is not used, that a
formation member from already-recorded six-neighbor locks is not attached,
that the sets are not leftover of unique own-incoming letters, that the sets
are not leftover of same-tick-inclusive existential opposite that excludes
`q`, that the sets are not leftover of strictly-earlier own-lock-in, and that
the sets are not leftover of later-tick union own. No runner cache is
written.
