---
claim_id: x_axis_same_lock_sametick_union_own_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from same-tick ∪ own incoming lock on the four x-axis same-lock y-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/x_axis_same_lock_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py
---

# Same-Tick Union Own Incoming Reverse And Face On Four X-Axis Same-Lock Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from same-tick ∪ own incoming lock on the four
x-axis same-lock y-probes in `B_3(0)`, no global T. Let `t(q)` be the
formation tick of probe `q`. Let `L(q)` be `q`'s own unique incoming lock;
seeds use seed letters. If several earliest incoming steps exist, `L(q)` is
`UNDEFINED`. At that tick, `S^+(q)` is the set of locks of six-neighbors of
`q` that formed at tick `<= t(q)` and are not `q`, union `{L(q)}` when
`L(q)` is defined. Reverse holds if and only if some lock in `S^+(A)` is the
vector opposite of some lock in `S^+(B)`. Face holds if and only if some
lock in `S^+(C)` is the vector opposite of some lock in `S^+(D)`. Empty
`S^+` on either side of a comparison is `UNDEFINED`; nonempty with no
opposite pair fails. Occupancy `n` is not used. This is not named-sign
lettering. This is not a unique lock-vector leftover and not a sum leftover.
This is not leftover of same-tick-inclusive existential opposite that
excludes `q`: that display omits `L` even though on these y-probes the union
happens to leave every neighbor set unchanged. This is not leftover of
strictly-earlier own-lock-in: that display takes tick `< t(q)` union own
lock and reports reverse fail with face fail from `{+e_2}` at `D`. This is
not leftover of later-tick union own: that display waits for a global later
T equal to the max of the four formation ticks and enlarges `S^+(B)`. This
is not leftover of the unique own-incoming lock-vector letters on these
y-probes: that readout requires a singleton incoming step and reports
reverse `UNDEFINED` with face `UNDEFINED` at mixed `A` and mixed `D`. This
is not leftover of same-tick union own incoming lock on the four nssame
y-probes: that leftover reports reverse fail and face fail from seed letter
`+e_1` at `A=(0,1,0)`. This is not leftover of same-tick union own incoming
lock on the four x-axis same-lock x-probes: that leftover reports reverse
fail and face fail because `A=(1,0,0)` is a seed. This is not leftover of
same-tick-inclusive union own incoming lock on the four x-axis opposite
y-probes: that leftover reports `{+e_1, +e_2, −e_2, +e_3, −e_3}` at `D`
from seed letter `−e_2` at `(1,0,0)`. Uniqueness of incoming locks is not
required. Uniqueness of the lock set is not required. Displayed, not
adopted. This note does not write existential opposite into Admissibility
and does not attach a formation member from already-recorded six-neighbor
locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/x_axis_same_lock_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py`](../scripts/x_axis_same_lock_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py)

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
claim_type_reason: "Exact report of S^+ as same-tick-inclusive six-neighbor locks union L(q) when defined, on the four x-axis same-lock y-probes at each probe's own t, no global T, with reverse hold that does not use L(A) and face hold from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: x_axis_same_lock_sametick_union_own_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from same-tick ∪ own incoming lock on the four x-axis same-lock y-probes, no global T, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with same-tick leftover that excludes q, do not identify the sets with strictly-earlier own-lock-in leftover, do not identify the sets with later-tick union own leftover, do not identify the sets with nssame y-probe leftover, and do not identify the sets with x-axis same-lock x-probe leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of same-tick-inclusive six-neighbor locks union own incoming lock on the four x-axis same-lock y-probes, no global T; displayed, not adopted"
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
`D=(1,1,0)`. `A` is not a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (1,0,0)}` is recorded at formation tick 0 with
same-letter locks `L(0)=+e_2` and `L(1,0,0)=+e_2`. This seed is not the
nssame two-site seed `{0, (0,1,0)}` with `+e_1/+e_1`. This seed is not the
opposite two-site seed `+e_2/−e_2`. This seed is not the nnseed two-site
seed `+e_2/+e_1`.

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
is not leftover of later-tick union own. It is not leftover of unique
own-incoming lock-vector letters on these y-probes. It is not leftover of
same-tick union own incoming lock on the four nssame y-probes. It is not
leftover of same-tick union own incoming lock on the four x-axis same-lock
x-probes. It is not leftover of same-tick-inclusive union own incoming lock
on the four x-axis opposite y-probes.

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

Direct enumeration of the displayed x-axis same-lock process on `B_3(0)`
forms all four y-probes. The formation ticks are `t(A)=3`, `t(B)=2`,
`t(C)=4`, `t(D)=3`. `A` is not a seed. Those ticks locate the
same-tick-inclusive six-neighbor set. They are not occupancy kernels and
are not a global later T.

Own incoming locks and same-tick-inclusive union sets at each probe's own
formation tick are:

```text
A: incoming −e_3, +e_3, +e_1; −e_1 at (1, 1, 0), −e_3 at (1, 1, 0),
   +e_3 at (1, 1, 0), +e_2 at (-1, 1, 0), +e_2 at (0, 0, 0),
   +e_2 at (0, 1, 1), +e_2 at (0, 1, -1);
   t(A)=3;  L(A) = UNDEFINED;  S^+(A) = {−e_1, +e_2, +e_3, −e_3}
B: incoming +e_2; +e_2 at (0, 1, 1), +e_3 at (1, 0, 1);
   t(B)=2;  L(B) = +e_2;  S^+(B) = {+e_2, +e_3}
C: incoming +e_2; +e_2 at (1, 2, 0), −e_3 at (0, 1, 0), +e_3 at (0, 1, 0),
   +e_1 at (0, 1, 0);
   t(C)=4;  L(C) = +e_2;  S^+(C) = {+e_1, +e_2, +e_3, −e_3}
D: incoming −e_1, −e_3, +e_3; +e_2 at (2, 1, 0), −e_3 at (0, 1, 0),
   +e_3 at (0, 1, 0), +e_1 at (0, 1, 0), +e_2 at (1, 0, 0),
   +e_2 at (1, 1, 1), +e_2 at (1, 1, -1);
   t(D)=3;  L(D) = UNDEFINED;  S^+(D) = {+e_1, +e_2, +e_3, −e_3}
```

`A` is not a seed. `L(A)` is `UNDEFINED` from three earliest incoming steps
`−e_3`, `+e_3`, and `+e_1`, so `S^+(A)` equals the same-tick-inclusive
neighbor set. Reverse HOLD does not use L(A). `L(B)=+e_2` already sits in
the neighbor set at `B`, so the union does not enlarge `B`. `L(C)=+e_2`
already sits in the neighbor set at `C`, so the union does not enlarge `C`.
`L(D)` is `UNDEFINED` from three earliest incoming steps `−e_1`, `−e_3`,
and `+e_3`, so `S^+(D)` equals the neighbor set. On these y-probes the union
happens to leave every neighbor set unchanged. Mixed remains a set.
`+e_1` is incoming at `A` and is not in `S^+(A)`.

Incoming locks exist and need not be unique (`A` has three earliest incoming
steps `−e_3`, `+e_3`, and `+e_1`; `D` has three earliest incoming steps
`−e_1`, `−e_3`, and `+e_3`). That non-uniqueness leaves `L(A)` and `L(D)`
`UNDEFINED` and does not empty `S^+(A)` or `S^+(D)`. Uniqueness is not
required.

The unique own-incoming letters on these y-probes are `UNDEFINED`, `+e_2`,
`+e_2`, `UNDEFINED`. Those are different objects: `S^+(A)` is nonempty and
is not `{−e_3, +e_3, +e_1}`. Same-tick leftover that excludes `q` reports
the same neighbor lists and does not report `L` or the union. Strictly-earlier
own-lock-in reports `{+e_2}`, `{+e_2, +e_3}`, `{+e_1, +e_2, +e_3, −e_3}`,
`{+e_2}` at `A,B,C,D`. Later-tick union own reports
`S^+(B)={+e_1, −e_1, +e_2, +e_3, −e_3}` at global `T=4`. Same-tick union own
on the four nssame y-probes reports `{+e_1}` at seed `A=(0,1,0)`. Same-tick
union own on the four x-axis same-lock x-probes reports `{+e_2}` at seed
`A=(1,0,0)`. Same-tick-inclusive union own on the four x-axis opposite
y-probes reports `{+e_1, +e_2, −e_2, +e_3, −e_3}` at `D`.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S^+(A)` and `b` in
`S^+(B)` with `a+b=(0,0,0)`. Both sets are nonempty:
`S^+(A)={−e_1, +e_2, +e_3, −e_3}` and `S^+(B)={+e_2, +e_3}`. The pair
`−e_3+(+e_3)=(0,0,0)` holds. Reverse holds.

Reverse: hold

This is not `fail` and not `UNDEFINED`. Reverse HOLD does not use L(A):
`L(A)` is `UNDEFINED`, and the holding pair is `−e_3` at same-tick neighbor
`D` against `+e_3` at `B`. Unique lock-vector lettering of the same lists
would assign mixed `S^+(A)` and mixed `S^+(B)` and would report reverse
`UNDEFINED`. That readout is a different object and is not used. A sum
leftover of the same lists would replace the sets by `(−1,1,0)` and
`(0,1,1)` and would report reverse fail. A named-sign readout of the same
locks would lose the axis in mixed `{+,−}` at `A`. Unique own-incoming
letters on these y-probes report reverse `UNDEFINED` from mixed `A`.
Strictly-earlier own-lock-in reports reverse fail on `{+e_2}` at `A` and
`{+e_2, +e_3}` at `B`. Later-tick union own also reports reverse hold, but
from a larger `S^+(B)` at global later T that includes `+e_1` and `−e_1`.
Nssame y-probe same-tick union own reports reverse fail from seed letter
`+e_1` at `A=(0,1,0)`. X-axis same-lock x-probe same-tick union own reports
reverse fail from seed letter `+e_2` at `A=(1,0,0)`. X-axis opposite y-probe
same-tick union own also reports reverse hold, but from a different `D`
that carries seed letter `−e_2`. Opposite seed letters are not supplied
here; reverse still holds from `−e_3` against `+e_3`.

Reverse holds.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S^+(C)` and `d` in `S^+(D)`
with `c+d=(0,0,0)`. Both sets are nonempty:
`S^+(C)={+e_1, +e_2, +e_3, −e_3}` and
`S^+(D)={+e_1, +e_2, +e_3, −e_3}`, so `+e_3+(−e_3)=(0,0,0)`. Face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.

This is not `fail` and not `UNDEFINED`. Own–own face is `UNDEFINED` because
`L(D)` is `UNDEFINED`. Unique own-incoming letters on these same y-probes
assign `L(D)=UNDEFINED` from three earliest incoming steps and report face
`UNDEFINED`. Unique lock-vector lettering of the union sets would report
face `UNDEFINED` because `C` and `D` mix. A sum leftover would replace
`S^+(C)` by `(1,1,0)` and `S^+(D)` by `(1,1,0)` and would fail face, for a
different reason. Named-sign lettering lost the axis: mixed `{+,−}` at `C`
and at `D` drop the axis of `+e_3`. Same-tick leftover that excludes `q`
also reports face hold, because the union happens to leave the neighbor
sets unchanged, but that leftover does not report `L`. Strictly-earlier
own-lock-in reports face fail from `{+e_2}` at `D` rather than
`{+e_1, +e_2, +e_3, −e_3}`. Later-tick union own reports face hold after a
global later T on a larger `S^+(B)`. Nssame y-probe same-tick union own
reports face fail from `{+e_1, +e_2}` at `C` against
`{+e_1, +e_2, +e_3, −e_3}` at `D`. X-axis same-lock x-probe same-tick union
own reports face fail because seed `A=(1,0,0)` is scored. X-axis opposite
y-probe same-tick union own reports face hold from a different `D` that
includes `−e_2`. Face holds from the same-tick union at these x-axis
same-lock y-probes; it does not wait for a later-tick enlargement and does
not use opposite seed letters.

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
  y-probes.
- It does not reprint same-tick-inclusive existential opposite that excludes
  `q`.
- It does not reprint strictly-earlier own-lock-in.
- It does not reprint later-tick union own.
- It does not wait for a global later T.
- It does not reprint same-tick union own incoming lock on the four nssame
  y-probes.
- It does not reprint same-tick union own incoming lock on the four x-axis
  same-lock x-probes.
- It does not reprint same-tick-inclusive union own incoming lock on the
  four x-axis opposite y-probes.
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
x-axis same-lock process, the same-tick-inclusive union sets, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-site seed `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `3`, `2`, `4`, `3` |
| own incoming locks `L(A)`, `L(B)`, `L(C)`, `L(D)` | Theorem 1; `UNDEFINED`, `+e_2`, `+e_2`, `UNDEFINED` |
| lock sets `S^+(A)`, `S^+(B)`, `S^+(C)`, `S^+(D)` | Theorem 1; `{−e_1, +e_2, +e_3, −e_3}`, `{+e_2, +e_3}`, `{+e_1, +e_2, +e_3, −e_3}`, `{+e_1, +e_2, +e_3, −e_3}` |
| reverse HOLD uses `L(A)` | Theorem 1; reverse holds; does not use L(A) |
| reverse and face | Theorems 2–3; `hold` / `hold` |
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
| leftover of same-tick union own incoming lock on the four nssame y-probes | not this display |
| leftover of same-tick union own incoming lock on the four x-axis same-lock x-probes | not this display |
| leftover of same-tick-inclusive union own incoming lock on the four x-axis opposite y-probes | not this display |
| leftover of nnseed y-probe same-tick union own | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: same-tick ∪ own incoming lock on the four x-axis same-lock y-probes, no global T, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed same-tick-inclusive union-own-lock existential-opposite reverse/face report on these four x-axis same-lock y-probes. |
| V3 | Same-tick-inclusive union sets and the `hold`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads same-tick-inclusive six-neighbor lock vectors union `L(q)` when defined and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique
own-incoming letters, does not reprint same-tick leftover that excludes
`q`, does not reprint strictly-earlier own-lock-in, does not reprint
later-tick union own, does not reprint nssame y-probe same-tick union own,
does not reprint x-axis same-lock x-probe same-tick union own, does not
reprint x-axis opposite y-probe same-tick union own, and does not use
occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same union sets | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while the mixed union sets are nonempty and both bits hold |
| sum of the same union sets | replace `S^+` by the `Z^3` sum | refused; leftover; sum of `S^+(A)` is `(−1,1,0)` and sum of `S^+(B)` is `(0,1,1)`; sum of `S^+(C)` is `(1,1,0)` and sum of `S^+(D)` is `(1,1,0)`; those sums fail reverse and fail face, while existential opposite holds |
| named-sign lettering of the same union sets | map `±e_i` to `{+,−}` | refused; lost the axis; mixed `{+,−}` at `A` would hide `−e_3+(+e_3)=0` |
| unique own-incoming lock-vector leftover on these y-probes | reuse `L(A)=UNDEFINED`, `L(B)=+e_2`, `L(C)=+e_2`, `L(D)=UNDEFINED` | refused; different object; that leftover reports reverse `UNDEFINED` and face `UNDEFINED` while same-tick union reverse holds and face holds |
| leftover of same-tick-inclusive existential opposite that excludes `q` | reuse neighbor sets without unioning `L(q)` | refused; different algebra; on these y-probes the union happens to leave the neighbor sets unchanged, but `L` is reported and `+e_1` is incoming at `A` without entering `S^+(A)` |
| leftover of strictly-earlier own-lock-in | reuse tick `< t(q)` union own lock with `S^+(D)={+e_2}` and reverse fail face fail | refused; different set; this display keeps same-tick partners at `A` and at `D` |
| leftover of later-tick union own | reuse global later T and a larger `S^+(B)` | refused; different sets; this display does not wait for a global later T |
| leftover of same-tick union own incoming lock on the four nssame y-probes | reuse seed `{0,(0,1,0)}` with `+e_1/+e_1` and reverse fail face fail | refused; different process; x-axis same-lock seed letter is `+e_2` and y-probe `A` is not a seed |
| leftover of same-tick union own incoming lock on the four x-axis same-lock x-probes | reuse x-probes with reverse fail and face fail | refused; different frame; y-probe `A` is not a seed |
| leftover of same-tick-inclusive union own incoming lock on the four x-axis opposite y-probes | reuse seed letter `−e_2` at `(1,0,0)` with `{+e_1, +e_2, −e_2, +e_3, −e_3}` at `D` | refused; different process; x-axis same-lock seed letter at `(1,0,0)` is `+e_2` |
| leftover of nnseed y-probe same-tick union own | reuse seed `+e_2/+e_1` with reverse fail | refused; different process; reverse holds here |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `S^+` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; all three earliest incoming steps at `A` and at `D` are kept and `L(A)`, `L(D)` are `UNDEFINED` |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_2` and `+e_2`, perpendicular step
rule, incoming-step lock, same-tick-inclusive lock set of six-neighbors formed
at tick `<=` each probe's own `t` with the probe excluded, union with `L(q)`
when defined, existential opposite, four y-probes with non-seed `A`, and
reverse/face as existence of a pair that sums to zero are declared. No
uniqueness of incoming locks, no occupancy `n`, no named-sign reduction, no
singleton leftover, no sum leftover, no unique own-incoming leftover, no
same-tick exclude-`q` leftover, no strictly-earlier own-lock-in leftover, no
later-tick leftover, no nssame y-probe leftover, no x-axis same-lock x-probe
leftover, no x-axis opposite y-probe leftover, no global later T, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold` reports do not close that residual.

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

**Steelman:** The union is leftover of exclude-`q` lists because `S^+`
equals the neighbor set on these y-probes, leftover of later-tick union own
because reverse and face both hold, mixed neighbor locks should make reverse
and face `UNDEFINED`, the sets should be replaced by their sums, unique
own-incoming letters already answered reverse `UNDEFINED` with face
`UNDEFINED`, strictly-earlier own-lock-in already answered reverse fail with
face fail, nssame y-probe same-tick union own already answered fail/fail
because `A` is a seed, x-axis same-lock x-probe same-tick union own already
answered fail/fail, x-axis opposite y-probe same-tick union own already
answered hold/hold, named signs should suffice because they keep
orientation, occupancy `n` should track that vector, and reverse HOLD must
use `L(A)`.

**Answer:** The named construction reports lock sets
`{−e_1, +e_2, +e_3, −e_3}`, `{+e_2, +e_3}`, `{+e_1, +e_2, +e_3, −e_3}`,
`{+e_1, +e_2, +e_3, −e_3}` at `A,B,C,D` from same-tick-inclusive
six-neighbor locks union `{L(q)}` when defined. Mixed remains a set. The
construction does not sum. Occupancy `n` is not used. Named signs lost the
axis. Some pair from `S^+(A)` and `S^+(B)` is opposite, so reverse holds.
Reverse HOLD does not use L(A): `L(A)` is `UNDEFINED`, and the holding pair
is `−e_3` at same-tick neighbor `D` against `+e_3` at `B`. Face holds. On
these y-probes the union happens to leave the neighbor sets unchanged
because `L(A)` and `L(D)` are `UNDEFINED` and `L(B)`, `L(C)` already sit in
the neighbor sets. The algebra is still the union: `L` is reported, and
incoming `+e_1` at `A` is not in `S^+(A)`. Strictly-earlier own-lock-in
reports `{+e_2}` at `D` and fails both bits. Later-tick leftover waits for a
global later T and enlarges `S^+(B)`. Nssame y-probe same-tick union own
fails reverse from a different seed `A`. X-axis same-lock x-probe same-tick
union own fails both bits because that `A` is a seed. X-axis opposite
y-probe same-tick union own holds both bits from a different `D` that
includes `−e_2`. The sets are not those leftovers. Opposite seed letters
are not supplied; both bits hold from same-tick neighbors. The bits remain
displayed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same x-axis same-lock
y-probes assigned `L(A)=UNDEFINED`, `L(B)=+e_2`, `L(C)=+e_2`,
`L(D)=UNDEFINED` and reported reverse `UNDEFINED` with face `UNDEFINED`. A
same-tick-inclusive existential opposite display that excludes `q` reports
the same neighbor lists without `L`. Strictly-earlier own-lock-in assigned
`{+e_2}`, `{+e_2, +e_3}`, `{+e_1, +e_2, +e_3, −e_3}`, `{+e_2}` and
reported reverse fail with face fail. Later-tick union own reported reverse
hold and face hold on a larger `S^+(B)={+e_1, −e_1, +e_2, +e_3, −e_3}`
after a global later T. Same-tick union own incoming lock on the four
nssame y-probes reported reverse fail and face fail from seed letter `+e_1`
at `A=(0,1,0)`. Same-tick union own incoming lock on the four x-axis
same-lock x-probes reported reverse fail and face fail from seed letter
`+e_2` at `A=(1,0,0)`. Same-tick-inclusive union own incoming lock on the
four x-axis opposite y-probes reported reverse hold and face hold from
`{+e_1, +e_2, −e_2, +e_3, −e_3}` at `D`. Unique lock-vector lettering of
the union sets would report reverse `UNDEFINED` and face `UNDEFINED` because
`A`, `B`, `C`, and `D` mix. A sum leftover of the same lists would report
reverse fail and face fail because the sums are `(−1,1,0)` with `(0,1,1)`
and `(1,1,0)` with `(1,1,0)`. This note is not those displays: mixed remains
a set, the construction does not sum, `S^+(A)` is nonempty from same-tick
neighbors, reverse holds, reverse HOLD does not use L(A), and face holds.

**Gate disposition:** PASS for the same-tick-inclusive six-neighbor-lock union
own incoming existential-opposite reverse/face reports above. FAIL / DO NOT SHIP
for “the predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals the sum of the lock set,”
“bits are Admissibility,” “the letter is occupancy `n`,” “the sets equal
unique own-incoming letters,” “the sets equal same-tick leftover that
excludes `q`,” “the sets equal strictly-earlier own-lock-in,” “the sets
equal later-tick union own,” “reverse is `fail`,” or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the x-axis same-lock
two-site perp-step incoming-lock process, reads each probe's own unique
incoming lock or `UNDEFINED`, collects six-neighbor locks formed at tick
`<=` each probe's own formation tick with the probe excluded, unions those
locks with `{L(q)}` when defined, reads the union sets at the four
y-probes, reports whether reverse HOLD uses L(A), and checks Theorems 1--3.
It also checks that reverse HOLD does not use L(A), that the construction
is not named-sign lettering, that mixed sets remain defined, that the
construction does not sum, that occupancy `n` is not used, that a formation
member from already-recorded six-neighbor locks is not attached, that the
sets are not leftover of unique own-incoming letters, that the sets are not
leftover of same-tick-inclusive existential opposite that excludes `q`, that
the sets are not leftover of strictly-earlier own-lock-in, that the sets
are not leftover of later-tick union own, that the sets are not leftover of
same-tick union own on the four nssame y-probes, that the sets are not
leftover of same-tick union own on the four x-axis same-lock x-probes, and
that the sets are not leftover of same-tick-inclusive union own incoming
lock on the four x-axis opposite y-probes. No runner cache is written.
