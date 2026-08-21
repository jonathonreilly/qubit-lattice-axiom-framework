---
claim_id: z_symmetric_three_site_xprobe_sametick_union_own_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from same-tick ∪ own incoming lock on the four z-symmetric three-site x-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/z_symmetric_three_site_xprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py
---

# Same-Tick-Inclusive Union Own Incoming Reverse And Face On Four Z-Symmetric Three-Site X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from same-tick ∪ own incoming lock on the four
z-symmetric three-site x-probes in `B_3(0)={n:n·n<=9}`, no global T. Let
`t(q)` be the formation tick of probe `q`. Let `L(q)` be `q`'s own unique
incoming lock; seeds use seed letters. If several earliest incoming steps
exist, `L(q)` is `UNDEFINED`. At that tick, `S^+(q)` is the set of locks of
six-neighbors of `q` that formed at tick `<= t(q)` and are not `q`, union
`{L(q)}` when `L(q)` is defined. Reverse holds if and only if some lock in
`S^+(A)` is the vector opposite of some lock in `S^+(B)`. Face holds if and
only if some lock in `S^+(C)` is the vector opposite of some lock in
`S^+(D)`. Empty `S^+` on either side of a comparison is `UNDEFINED`;
nonempty with no opposite pair fails. Occupancy `n` is not used. This is
not named-sign lettering. This is not a unique lock-vector leftover and not
a sum leftover. This is not leftover of unique already-recorded 6-NN lock
vectors on these same x-probes. This is not leftover of two-site opposite-lock
same-tick union own: that display uses the two-site seed `{0,(0,0,1)}` and
reports `S^+(A)` without `+e_3`. This is not leftover of z-symmetric
three-site y-probe same-tick union own: that unlaunched display reports
reverse fail on the y-probes of this same seed. This is not leftover of
y-symmetric three-site x-probe same-tick union own: that display uses the
y-mirror seed `{0,(0,1,0),(0,-1,0)}` and reports `S^+(B)={+e_1, +e_3}` with
`t(D)=3` and `L(D)` `UNDEFINED`. This is not leftover of y-symmetric
three-site y-probe same-tick union own: that display uses seed letter `−e_1`
at `A=(0,1,0)` and reverse HOLD uses L(A). This is not leftover of
same-tick-inclusive existential opposite that excludes `q`: that display
does not report `L` or the union. This is not leftover of strictly-earlier
own-lock-in: that display takes tick `< t(q)` union own lock and reports
reverse fail from `{+e_1}` at `A`. This is not leftover of later-tick union
own: that display waits for a global later T equal to the max of the four
formation ticks and enlarges `S^+(B)`. This is not leftover of the unique
own-incoming lock-vector letters on these x-probes: that readout reports
reverse `UNDEFINED` with face fail from mixed `A` and unique `+e_1` at `C`
and `D`. This is not leftover of the three-site opposite-lock seed whose
third site is `(1,0,0)` with lock `+e_2`. Uniqueness of incoming locks is
not required. Uniqueness of the lock set is not required. Displayed, not adopted.
Do not write into Admissibility. Do not attach L1. This note does not write
existential opposite into Admissibility and does not attach a formation
member from already-recorded six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/z_symmetric_three_site_xprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py`](../scripts/z_symmetric_three_site_xprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
same-tick-inclusive six-neighbor lock sets union the probe's own incoming
lock when defined. Named signs `{+,−}` are a coarser readout and are not
used. A singleton unique lock-vector letter is a different readout and is
not used. A `Z^3` sum of those locks is a different readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of S^+ as same-tick-inclusive six-neighbor locks union L(q) when defined, on the four z-symmetric three-site x-probes at each probe's own t, no global T, with reverse hold that does not use L(A) and face hold from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: z_symmetric_three_site_xprobe_sametick_union_own_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from same-tick ∪ own incoming lock on the four z-symmetric three-site x-probes, no global T, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with same-tick leftover that excludes q, do not identify the sets with strictly-earlier own-lock-in leftover, do not identify the sets with later-tick union own leftover, do not identify the sets with two-site opposite-lock leftover, do not identify the sets with z-symmetric three-site y-probe leftover, do not identify the sets with y-symmetric three-site x-probe leftover, and do not identify the sets with y-symmetric three-site y-probe leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of same-tick-inclusive six-neighbor locks union own incoming lock on the four z-symmetric three-site x-probes, no global T; displayed, not adopted"
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

Seed: the three-record set `{0, (0,0,1), (0,0,-1)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,0,1)=−e_1`, and `L(0,0,-1)=−e_1`. The
third site is the z-mirror of the two-site opposite-lock partner `(0,0,1)`.
This seed is not the two-site opposite-lock seed `{0,(0,0,1)}` and not the
three-site opposite-lock seed whose third site is `(1,0,0)` with lock `+e_2`.
This seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
y-symmetric three-site seed `{0,(0,1,0),(0,-1,0)}`.

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

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
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
leftover. It is not leftover of unique already-recorded 6-NN lock vectors on
these x-probes. It is not leftover of two-site opposite-lock same-tick union
own. It is not leftover of z-symmetric three-site y-probe same-tick union
own. It is not leftover of y-symmetric three-site x-probe same-tick union
own. It is not leftover of y-symmetric three-site y-probe same-tick union
own. It is not leftover of same-tick-inclusive existential opposite that
excludes `q`. It is not leftover of strictly-earlier own-lock-in. It is not
leftover of later-tick union own. It is not leftover of unique own-incoming
lock-vector letters on these x-probes.

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

## Theorem 1 — formation ticks, own incoming locks, and S^+ at each x-probe

Direct enumeration of the displayed z-symmetric three-site process on
`B_3(0)` forms all four x-probes. The formation ticks are `t(A)=3`,
`t(B)=2`, `t(C)=4`, `t(D)=2`. `A` is not a seed. Those ticks locate the
same-tick-inclusive six-neighbor set. They are not occupancy kernels and are
not a global later T.

Own incoming locks and same-tick-inclusive union sets at each probe's own
formation tick are:

```text
A: incoming −e_2, +e_2; +e_1 at (0, 0, 0), +e_1 at (1, 1, 0),
   +e_1 at (1, -1, 0), −e_2 at (1, 0, 1), −e_3 at (1, 0, 1),
   +e_2 at (1, 0, 1), −e_2 at (1, 0, -1), +e_3 at (1, 0, -1),
   +e_2 at (1, 0, -1);
   t(A)=3;  L(A) = UNDEFINED;  S^+(A) = {+e_1, +e_2, −e_2, +e_3, −e_3}
B: incoming +e_1; +e_2 at (0, 1, 1), +e_1 at (1, 1, 0);
   t(B)=2;  L(B) = +e_1;  S^+(B) = {+e_1, +e_2}
C: incoming +e_1; −e_2 at (1, 0, 0), +e_2 at (1, 0, 0),
   +e_1 at (2, 0, 1), +e_1 at (2, 0, -1);
   t(C)=4;  L(C) = +e_1;  S^+(C) = {+e_1, +e_2, −e_2}
D: incoming +e_1; +e_2 at (0, 1, 0), +e_1 at (1, 1, 1),
   +e_1 at (1, 1, -1);
   t(D)=2;  L(D) = +e_1;  S^+(D) = {+e_1, +e_2}
```

`A` is not a seed. `L(A)` is `UNDEFINED` from two earliest incoming steps
`−e_2` and `+e_2`, so `S^+(A)` equals the same-tick-inclusive neighbor set.
Reverse HOLD does not use L(A). `L(B)=+e_1` already sits in the neighbor set
at `B`, so the union does not enlarge `B`. `L(C)=+e_1` already sits in the
neighbor set at `C`, so the union does not enlarge `C`. `L(D)=+e_1` already
sits in the neighbor set at `D`, so the union does not enlarge `D`. On these
x-probes the union happens to leave every neighbor set unchanged. Mixed
remains a set. Same-tick `(1,0,1)` and `(1,0,-1)` supply `+e_2`, `−e_2`,
`+e_3`, and `−e_3` into `S^+(A)`; those letters are not a unique incoming
lock at `A`. The two-site opposite-lock leftover omits `+e_3` from
`S^+(A)` because it lacks the z-mirror seed `(0,0,-1)`. Y-symmetric
three-site x-probe leftover reports `S^+(B)={+e_1, +e_3}`, `t(D)=3`, and
`L(D)` `UNDEFINED`.

Incoming locks exist and need not be unique (`A` has two earliest incoming
steps `−e_2` and `+e_2`). That non-uniqueness leaves `L(A)` `UNDEFINED` and
does not empty `S^+(A)`. `D` happens to have one incoming lock `+e_1`.
Uniqueness is not required.

The unique own-incoming letters on these x-probes are `UNDEFINED`, `+e_1`,
`+e_1`, `+e_1`. Those are different objects: `S^+(A)` is nonempty, and unique
own-incoming reverse is `UNDEFINED` with face fail. Same-tick-inclusive
leftover that excludes `q` reports the same neighbor lists and does not
report `L` or the union. Strictly-earlier own-lock-in reports `{+e_1}` at
`A` without the same-tick partners of `A`. Later-tick union own reports
`{+e_1, +e_2, −e_2, +e_3, −e_3}` at `B` after waiting for a global later T.
Unique already-recorded 6-NN lock vectors on this seed report reverse
`UNDEFINED` at mixed `B`. Z-symmetric three-site y-probe same-tick union own
reports reverse fail at `A=(0,1,0)` with `L(A)=+e_2`. Y-symmetric three-site
y-probe same-tick union own reports seed letter `−e_1` at `A=(0,1,0)` and
reverse HOLD uses L(A).

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S^+(A)` and `b` in
`S^+(B)` with `a+b=(0,0,0)`. Both sets are nonempty:
`S^+(A)={+e_1, +e_2, −e_2, +e_3, −e_3}` and `S^+(B)={+e_1, +e_2}`, so
`−e_2+(+e_2)=(0,0,0)`. Reverse holds.

Reverse: hold

Reverse HOLD does not use L(A). `L(A)` is `UNDEFINED`, and the holding pair
is `−e_2` at same-tick neighbors of `A` against `+e_2` at `B`. Same-tick-inclusive
leftover that excludes `q` reports the same neighbor lists and also
holds; the algebra is still the union because `L` is reported. Holding
reverse does not need a global later T.

This is not `fail` and not `UNDEFINED`. This is not leftover of
same-tick-inclusive existential opposite that excludes `q`. Unique
lock-vector lettering of the same union sets would report reverse
`UNDEFINED` because both sides mix. A sum leftover of the same lists would
replace `S^+(A)` by `+e_1` and `S^+(B)` by `(1,1,0)` and would fail
reverse, while existential opposite holds. Unique own-incoming letters on
these x-probes report reverse `UNDEFINED` from mixed `A`. Strictly-earlier
own-lock-in reports reverse fail from `{+e_1}` at `A`. Later-tick union
own reports reverse hold on a later five-lock set at `B`. Z-symmetric
three-site y-probe same-tick union own reports reverse fail. Y-symmetric
three-site y-probe same-tick union own reports reverse hold, but reverse
HOLD uses L(A) there from seed letter `−e_1`. Y-symmetric three-site
x-probe same-tick union own also reports reverse hold, but from a different
`S^+(B)={+e_1, +e_3}`. Two-site opposite-lock same-tick union own also
reports reverse hold, but from a different `S^+(A)` that omits `+e_3`.
Reverse holds because `−e_2` already sits in the same-tick neighbor set of
`A`.

Reverse holds.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S^+(C)` and `d` in `S^+(D)`
with `c+d=(0,0,0)`. Both sets are nonempty: `S^+(C)={+e_1, +e_2, −e_2}` and
`S^+(D)={+e_1, +e_2}`, so `−e_2+(+e_2)=(0,0,0)`. Face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Unique own-incoming letters on these
same x-probes assign `L(C)=+e_1` and `L(D)=+e_1` and report face fail.
Unique lock-vector lettering of the union sets would report face
`UNDEFINED` because `C` and `D` mix. A sum leftover would replace `S^+(C)`
by `+e_1` and `S^+(D)` by `(1,1,0)` and would fail face, while existential
opposite holds. Named-sign lettering lost the axis in mixed `{+,−}` at `C`.
Face already holds at each probe's own formation tick with same-tick
partners included and own lock unioned; holding face does not need a global
later T. Two-site opposite-lock leftover reports face hold from the same
`S^+(D)={+e_1, +e_2}` but a different `S^+(C)` that includes `+e_3`.
Y-symmetric three-site x-probe leftover reports face hold from a different
`S^+(D)={+e_1, −e_1, +e_3, −e_3}`. Y-symmetric three-site y-probe leftover
reports face hold from `{−e_1, +e_2}` at `C`.

Face holds.

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
  x-probes.
- It does not reprint unique already-recorded 6-NN lock vectors on these
  x-probes.
- It does not reprint two-site opposite-lock same-tick union own.
- It does not reprint z-symmetric three-site y-probe same-tick union own.
- It does not reprint y-symmetric three-site x-probe same-tick union own.
- It does not reprint y-symmetric three-site y-probe same-tick union own.
- It does not reprint same-tick-inclusive existential opposite that excludes
  `q`.
- It does not reprint strictly-earlier own-lock-in.
- It does not reprint later-tick union own.
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

This display uses Lattice to name `B_3(0)` and the four x-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
z-symmetric three-site process, the same-tick-inclusive union sets, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; z-symmetric three-site seed `+e_1/−e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `3`, `2`, `4`, `2` |
| own incoming locks `L(A)`, `L(B)`, `L(C)`, `L(D)` | Theorem 1; `UNDEFINED`, `+e_1`, `+e_1`, `+e_1` |
| lock sets `S^+(A)`, `S^+(B)`, `S^+(C)`, `S^+(D)` | Theorem 1; `{+e_1, +e_2, −e_2, +e_3, −e_3}`, `{+e_1, +e_2}`, `{+e_1, +e_2, −e_2}`, `{+e_1, +e_2}` |
| reverse HOLD uses L(A) | Theorem 1; no; `L(A)` is `UNDEFINED` |
| reverse and face | Theorems 2–3; `hold` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique already-recorded 6-NN lock vectors | not this display |
| leftover of unique own-incoming letters on these x-probes | not this display |
| leftover of two-site opposite-lock same-tick union own | not this display |
| leftover of z-symmetric three-site y-probe same-tick union own | not this display |
| leftover of y-symmetric three-site x-probe same-tick union own | not this display |
| leftover of y-symmetric three-site y-probe same-tick union own | not this display |
| leftover of same-tick-inclusive existential opposite that excludes `q` | not this display |
| leftover of strictly-earlier own-lock-in | not this display |
| leftover of later-tick union own | not this display |
| leftover of nnseed x-probe formation-time existential opposite | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: same-tick ∪ own incoming lock on the four z-symmetric three-site x-probes, no global T, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed same-tick-inclusive union-own-lock existential-opposite reverse/face report on these four z-symmetric three-site x-probes. |
| V3 | Same-tick-inclusive union sets and the `hold`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads same-tick-inclusive six-neighbor lock vectors union `L(q)` when defined and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique
own-incoming letters, does not reprint unique already-recorded leftover,
does not reprint two-site opposite-lock leftover, does not reprint
z-symmetric three-site y-probe leftover, does not reprint y-symmetric
three-site x-probe leftover, does not reprint y-symmetric three-site
y-probe leftover, does not reprint same-tick leftover
that excludes `q`, does not reprint strictly-earlier own-lock-in, does not
reprint later-tick union own, and does not use occupancy `n`. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same union sets | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while the mixed union sets are nonempty and both bits hold |
| unique already-recorded 6-NN lock vectors on this seed | reuse formation-time singleton neighbor letters | refused; leftover; that readout reports reverse `UNDEFINED` at mixed `B` |
| sum of the same union sets | replace `S^+` by the `Z^3` sum | refused; leftover; sum of `S^+(A)` is `+e_1` and sum of `S^+(B)` is `(1,1,0)`, which would fail reverse while `−e_2+(+e_2)=0`; sum of `S^+(C)` is `+e_1` and sum of `S^+(D)` is `(1,1,0)` and would fail face |
| named-sign lettering of the same union sets | map `±e_i` to `{+,−}` | refused; lost the axis; mixed `{+,−}` at `A` and `C` would hide `−e_2+(+e_2)=0` |
| unique own-incoming lock-vector leftover on these x-probes | reuse `L(A)=UNDEFINED`, `L(B)=+e_1`, `L(C)=+e_1`, `L(D)=+e_1` | refused; different object; that leftover reports reverse `UNDEFINED` and face fail while same-tick union reverse holds and face holds |
| leftover of same-tick-inclusive existential opposite that excludes `q` | reuse neighbor sets without unioning `L(q)` | refused; different algebra; on these x-probes the union happens to leave the neighbor sets unchanged, but `L` is reported and the construction is the union |
| leftover of strictly-earlier own-lock-in | reuse tick `< t(q)` union own lock with `S^+(A)={+e_1}` | refused; different set; this display keeps same-tick partners and reverse holds |
| leftover of later-tick union own | reuse global later T and a five-lock set at `B` | refused; different set; this display does not wait for a global later T |
| leftover of two-site opposite-lock same-tick union own | reuse seed `{0,(0,0,1)}` with `S^+(A)` missing `+e_3` | refused; different process; this `S^+(A)` includes `+e_3` from the z-mirror seed |
| leftover of z-symmetric three-site y-probe same-tick union own | reuse y-probes of this seed | refused; different frame; reverse fails there and holds here |
| leftover of y-symmetric three-site x-probe same-tick union own | reuse y-mirror seed on these x-probes | refused; different process; that display has `S^+(B)={+e_1, +e_3}` and `t(D)=3` |
| leftover of y-symmetric three-site y-probe same-tick union own | reuse y-probes with seed letter `−e_1` at `A` | refused; different frame; reverse HOLD uses L(A) there and does not here |
| leftover of nnseed x-probe formation-time existential opposite | reuse seed `+e_1/+e_2` and x-probes | refused; different process; reverse fails there |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `S^+` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; both earliest incoming steps at `A` are kept and `L(A)` is `UNDEFINED` |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, z-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, same-tick-inclusive
lock set of six-neighbors formed at tick `<=` each probe's own `t` with the
probe excluded, union with `L(q)` when defined, existential opposite, four
x-probes with non-seed `A`, and reverse/face as existence of a pair that sums
to zero are declared. No uniqueness of incoming locks, no occupancy `n`, no
named-sign reduction, no singleton leftover, no sum leftover, no unique
own-incoming leftover, no unique already-recorded leftover, no two-site
opposite-lock leftover, no z-symmetric three-site y-probe leftover, no
y-symmetric three-site x-probe leftover, no y-symmetric three-site y-probe leftover, no
same-tick exclude-`q` leftover, no strictly-earlier own-lock-in leftover, no
later-tick leftover, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in a same-tick-inclusive union set | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
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
already-recorded letters already answered reverse `UNDEFINED`, unique
own-incoming letters already answered reverse `UNDEFINED` with face
fail, same-tick-inclusive existential opposite already answered
the exist-opposite question because the union is a no-op, two-site
opposite-lock same-tick union own already answered hold/hold with a
different `S^+(A)`, y-symmetric three-site x-probe same-tick union own
already answered hold/hold so this is leftover, z-symmetric three-site
y-probe same-tick union own already answered reverse fail, strictly-earlier
own-lock-in already answered the union question without same-tick
partners, later-tick union own already answered the union question after
a global T, named signs should suffice because they keep orientation,
and occupancy `n` should track that vector.

**Answer:** The named construction reports lock sets
`{+e_1, +e_2, −e_2, +e_3, −e_3}`, `{+e_1, +e_2}`, `{+e_1, +e_2, −e_2}`,
`{+e_1, +e_2}` at `A,B,C,D` from same-tick-inclusive
six-neighbor locks union `{L(q)}` when defined. Mixed remains a set. The
construction does not sum. Occupancy `n` is not used. Named signs lost the
axis. Some pair from `S^+(A)` and `S^+(B)` is opposite, so reverse holds.
Reverse HOLD does not use L(A). Some pair from `S^+(C)` and `S^+(D)` is
opposite, so face holds. Same-tick leftover that excludes `q` leaves the
same neighbor sets here because `L(A)` is `UNDEFINED` and
`L(B)`, `L(C)`, `L(D)` already sit in the neighbor sets; the algebra is still the
union. Strictly-earlier own-lock-in reports `{+e_1}` at `A` and reverse
fail. Later-tick union own waits for a global later T and enlarges
`S^+(B)`. Unique own-incoming leftover reports reverse `UNDEFINED` and
face fail at mixed `A` and unique `+e_1` at `C` and `D`. Unique already-recorded leftover
reports reverse `UNDEFINED`. Two-site opposite-lock leftover reports a
different `S^+(A)` that omits `+e_3`. Y-symmetric three-site x-probe leftover
reports `S^+(B)={+e_1, +e_3}` and `t(D)=3`. Z-symmetric three-site y-probe leftover
reports reverse fail. Y-symmetric three-site y-probe leftover reports seed letter `−e_1`
at `A` and reverse HOLD uses L(A) there. The sets are not those leftovers.
Holding reverse does not need a global later T. The bits remain displayed.
Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique already-recorded 6-NN lock-vector display on these same
z-symmetric three-site x-probes would assign mixed letters at `B`, `C`,
and `D` and report reverse `UNDEFINED` with face `UNDEFINED`. A unique
own-incoming lock-vector display assigned `L(A)=UNDEFINED`, `L(B)=+e_1`,
`L(C)=+e_1`, `L(D)=+e_1` and reported reverse `UNDEFINED` with face
fail. A same-tick-inclusive existential opposite display that excludes
`q` reports the same neighbor lists without `L`. Strictly-earlier own-lock-in
assigned `{+e_1}`, `{+e_1, +e_2}`, `{+e_1, +e_2, −e_2}`, `{+e_1, +e_2}` and
reported reverse fail with face hold. Later-tick union own reported reverse
hold and face hold on a five-lock set at `B` after a global later T.
Two-site opposite-lock same-tick union own reported reverse hold and face
hold with `S^+(A)={+e_1, +e_2, −e_2, −e_3}` and
`S^+(D)={+e_1, +e_2}`. Y-symmetric three-site x-probe same-tick union own
reported reverse hold and face hold from `S^+(B)={+e_1, +e_3}` and
`t(D)=3`. Z-symmetric three-site y-probe same-tick union own reported reverse
fail. Y-symmetric three-site y-probe
same-tick union own reported reverse hold and face hold from
`S^+(A)={+e_1, −e_1}` at seed `A`, and reverse HOLD uses L(A) there.
Unique lock-vector lettering of the union sets would report reverse
`UNDEFINED` and face `UNDEFINED` because every union set mixes. A sum leftover
of the same lists would report reverse fail and face fail because the sums
are `+e_1` with `(1,1,0)` and `+e_1` with `(1,1,0)`. This note is
not those displays: mixed remains a set, the construction does not sum,
`S^+(A)` includes same-tick `+e_2` and `−e_2`, reverse HOLD does not use
L(A), reverse holds, and `−e_2+(+e_2)=(0,0,0)` so face holds.

**Gate disposition:** PASS for the same-tick-inclusive six-neighbor-lock union
own incoming existential-opposite reverse/face reports above. FAIL / DO NOT SHIP
for “the predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals the sum of the lock set,”
“bits are Admissibility,” “the letter is occupancy `n`,” “the sets equal
unique own-incoming letters,” “the sets equal unique already-recorded
letters,” “the sets equal two-site opposite-lock leftover,” “the sets equal
z-symmetric three-site y-probe leftover,” “the sets equal y-symmetric
three-site x-probe leftover,” “the sets equal y-symmetric three-site
y-probe leftover,” “the sets equal same-tick leftover
that excludes `q`,” “the sets equal strictly-earlier own-lock-in,” “the
sets equal later-tick union own,” “reverse fails,” or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the z-symmetric three-site
perp-step incoming-lock process, reads each probe's own unique incoming lock
or `UNDEFINED`, collects six-neighbor locks formed at tick `<=` each probe's
own formation tick with the probe excluded, unions those locks with `{L(q)}`
when defined, reads the union sets at the four x-probes, reports whether
reverse HOLD uses L(A), and checks Theorems 1--3. It also checks that the
construction is not named-sign lettering, that mixed sets remain defined,
that the construction does not sum, that occupancy `n` is not used, that a
formation member from already-recorded six-neighbor locks is not attached,
that the sets are not leftover of unique own-incoming letters, that the sets
are not leftover of unique already-recorded leftover, that the sets are not
leftover of two-site opposite-lock same-tick union own, that the sets are
not leftover of z-symmetric three-site y-probe same-tick union own, that
the sets are not leftover of y-symmetric three-site x-probe same-tick union
own, that the sets are not leftover of y-symmetric three-site y-probe
same-tick union own, that
the sets are not leftover of same-tick-inclusive existential opposite that
excludes `q`, that the sets are not leftover of strictly-earlier own-lock-in,
and that the sets are not leftover of later-tick union own. No runner cache
is written.
