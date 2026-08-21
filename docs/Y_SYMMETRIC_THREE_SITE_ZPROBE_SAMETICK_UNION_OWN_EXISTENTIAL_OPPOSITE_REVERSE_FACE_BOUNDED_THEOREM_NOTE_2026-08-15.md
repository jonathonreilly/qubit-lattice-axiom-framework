---
claim_id: y_symmetric_three_site_zprobe_sametick_union_own_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from same-tick ∪ own incoming lock on the four y-symmetric three-site z-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/y_symmetric_three_site_zprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py
---

# Same-Tick Union Own Incoming Reverse And Face On Four Y-Symmetric Three-Site Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from same-tick ∪ own incoming lock on the four
y-symmetric three-site z-probes in `B_3(0)`, no global T. Let `t(q)` be the
formation tick of probe `q`. Let `L(q)` be `q`'s own unique incoming lock;
seeds use seed letters. If several earliest incoming steps exist, `L(q)` is
`UNDEFINED`. At `t(q)`, `S(q)` is the set of locks of six-neighbors of `q`
that formed at tick `≤ t(q)` and are not `q`. `S^+(q)` is `S(q)` union
`{L(q)}` when `L(q)` is defined. Reverse holds if and only if some lock in
`S^+(A)` is the vector opposite of some lock in `S^+(B)`. Face holds if and
only if some lock in `S^+(C)` is the vector opposite of some lock in
`S^+(D)`. Empty `S^+` on either side of a comparison is `UNDEFINED`;
nonempty with no opposite pair fails. Occupancy `n` is not used. This is
not named-sign lettering. This is not a unique lock-vector leftover and not
a sum leftover. Same process as the y-symmetric three-site unique-vector
display. Same z-probes as the opposite-lock z-probe unique-vector display.
This is not leftover of same-tick ∪ own incoming lock on the y-symmetric
three-site y-probe frame: that display adds the seed letter `−e_1` at `A`
and reports reverse hold and face hold. This is not leftover of two-site
opposite-lock same-tick ∪ own on these z-probes: that process lacks the
y-mirror seed and reports `S^+(C)` without `+e_2`. This is not leftover of
later-tick `S_*` union own lock: that display waits for a global later T
and reports reverse hold and face hold. This is not leftover of own-lock-in
at formation: that readout scores strictly-earlier neighbors union `L(q)`
and reports reverse fail and face fail. Reverse HOLD does not use `L(A)`:
reverse fails with and without `L(A)` in `S^+(A)`, and `L(A)` already
appears as a same-tick neighbor lock. Uniqueness of incoming locks is not
required. Uniqueness of the lock set is not required. Displayed, not
adopted. This note does not write existential opposite into Admissibility
and does not attach a formation member from same-tick-inclusive six-neighbor
locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/y_symmetric_three_site_zprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py`](../scripts/y_symmetric_three_site_zprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in
`S^+` at each probe's own tick. Named signs `{+,−}` are a coarser readout
and are not used. A singleton unique lock-vector letter is a different
readout and is not used. A `Z^3` sum of those locks is a different readout
and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of t, L, and S^+ as same-tick-inclusive six-neighbor locks union L(q) when defined, no global T, on the four y-symmetric three-site z-probes, with reverse fail and face hold from existential opposite; reverse HOLD does not use L(A); uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: y_symmetric_three_site_zprobe_sametick_union_own_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from same-tick ∪ own incoming lock on the four y-symmetric three-site z-probes, no global T, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not wait for a global later T, do not identify the sets with later-tick leftover, do not identify the sets with own-lock-in at formation, do not identify the sets with y-probe same-tick union leftover, and do not identify the sets with unique own-incoming leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of same-tick-inclusive six-neighbor locks union own incoming lock on the four y-symmetric three-site z-probes; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose
same-tick-inclusive union sets are scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`,
`C=(2,0,0)`, `D=(1,1,0)`. `A` is not a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (0,1,0), (0,-1,0)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,1,0)=−e_1`, and `L(0,-1,0)=−e_1`. The
third site is the y-mirror of the two-site opposite-lock partner `(0,1,0)`.
This seed is not the two-site opposite-lock seed `{0,(0,1,0)}` and not the
three-site opposite-lock seed whose third site is `(1,0,0)` with lock `+e_2`.

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
`q`. Seeds keep their seed letters.

## Named existential opposite from same-tick ∪ own incoming lock

Let `t(q)` be the formation tick of z-probe `q` when that tick is defined in
`B_3(0)`. This display does not wait for a global later T. At the own
formation tick of each probe `q`, let `S(q)` be the set of locks of
six-neighbors of `q` that formed at tick `≤ t(q)` and are not `q`.
Same-tick neighbors count. Later-than-formation neighbors do not. The probe
itself is excluded. Let `L(q)` be `q`'s own unique incoming lock; if several
earliest incoming steps exist, `L(q)` is `UNDEFINED`. Then `S^+(q) = S(q)`
union `{L(q)}` when `L(q)` is defined, and `S^+(q) = S(q)` when `L(q)` is
`UNDEFINED`. This display does not use occupancy `n`. Duplicate locks at two
neighbors collapse in the set. The construction does not require `S^+(q)` to
be a singleton. It does not sum `S^+(q)`. It is not a unique lock-vector
leftover and not a sum leftover. It is not leftover of later-tick `S_*`
union own lock. It is not leftover of own-lock-in at formation. It is not
leftover of formation-tick existential opposite that excludes `q`. It is
not leftover of same-tick-inclusive existential opposite that excludes `q`.
It is not leftover of same-tick ∪ own incoming lock on the y-symmetric
three-site y-probe frame. It is not leftover of two-site opposite-lock
same-tick ∪ own on these z-probes. It is not leftover of unique own-incoming
lock-vector letters on these z-probes.

Incoming `{±e_i}` tags of the probe itself are members of `S^+(q)` only
through the union when `L(q)` is defined, or if they already appear as a
neighbor lock in `S(q)`. Identifying a named sign of those locks with
reverse or face is refused: named-sign lettering lost the axis. Reverse and
face are scored on existence of a pair of lock vectors that add to zero.
They are not scored on `{+,−}` names and are not an occupancy-kernel inner
product.

Reverse and face (displayed):

```text
reverse  <=>  some a in S^+(A) and some b in S^+(B) with a+b=(0,0,0)
face     <=>  some c in S^+(C) and some d in S^+(D) with c+d=(0,0,0)
```

If `S^+(A)` or `S^+(B)` is empty, reverse is `UNDEFINED`. Else reverse
fails if no such pair exists. If `S^+(C)` or `S^+(D)` is empty, face is
`UNDEFINED`. Else face fails if no such pair exists. The report is one of
`hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility.

## Theorem 1 — t, L, and S^+ at each z-probe

Direct enumeration of the displayed y-symmetric three-site process on
`B_3(0)` forms all four z-probes. The formation ticks are t(A)=1, t(B)=2,
t(C)=4, t(D)=2. `A` is not a seed. Those ticks locate the same-tick-inclusive
six-neighbor set. They are not occupancy kernels and are not a global later T.

Own unique incoming letters:

```text
L(A) = +e_3
L(B) = +e_1
L(C) = UNDEFINED
L(D) = +e_1
```

`C` has two earliest incoming steps `−e_1` and `+e_1`, so `L(C)` is
`UNDEFINED`. Uniqueness is not required.

At each probe's own tick the six-neighbor lock lists, lock sets, and union
sets are:

```text
A: +e_3 at (0, 1, 1), +e_3 at (0, -1, 1), +e_1 at (0, 0, 0);
   S(A) = {+e_1, +e_3}
   S^+(A) = {+e_1, +e_3}
B: +e_3 at (0, 1, 1), +e_1 at (1, 0, 1);
   S(B) = {+e_1, +e_3}
   S^+(B) = {+e_1, +e_3}
C: +e_3 at (1, 0, 2), +e_3 at (-1, 0, 2), −e_1 at (0, 1, 2),
   −e_2 at (0, 1, 2), +e_1 at (0, 1, 2), −e_1 at (0, -1, 2),
   +e_2 at (0, -1, 2), +e_1 at (0, -1, 2), +e_3 at (0, 0, 1);
   S(C) = {+e_1, −e_1, +e_2, −e_2, +e_3}
   S^+(C) = {+e_1, −e_1, +e_2, −e_2, +e_3}
D: +e_3 at (0, 0, 1), +e_1 at (1, 1, 1), +e_1 at (1, -1, 1);
   S(D) = {+e_1, +e_3}
   S^+(D) = {+e_1, +e_3}
```

`A` forms at tick 1. Its same-tick neighbors `(0, 1, 1)` and `(0, -1, 1)`
lock `+e_3`, equal to `L(A)`, and the earlier seed origin locks `+e_1`.
The y-mirror seed `(0,-1,0)` supplies the extra same-tick neighbor
`(0, -1, 1)` that the two-site opposite-lock process lacks. Later `D`, `C`,
and `(-1, 0, 1)` are excluded. `L(A)=+e_3` already appears in `S(A)`, so the
union happens to leave `S(A)` unchanged. `B` keeps earlier `(0, 1, 1)`
locking `+e_3` and same-tick `D` locking `+e_1`; `L(B)=+e_1` already appears
in `S(B)`. `C` forms at tick 4; same-tick `(0, 1, 2)` mixes `−e_1`, `−e_2`,
and `+e_1`, and same-tick `(0, -1, 2)` mixes `−e_1`, `+e_2`, and `+e_1`,
while earlier neighbors lock `+e_3`. `L(C)` is `UNDEFINED`, so
`S^+(C)=S(C)`. `+e_2` is in `S(C)` from `(0, -1, 2)`. `D` forms at tick 2
with earlier `A` locking `+e_3` and same-tick `B` and `(1, -1, 1)` locking
`+e_1`; `L(D)=+e_1` already appears in `S(D)`. Mixed remains a set. The
construction still unions `L(q)` when defined: that is a different object
from same-tick-inclusive existential opposite that excludes `q`, even though
the four sets coincide here.

Incoming locks exist and need not be unique. The lock sets are not identified
with those incoming steps alone. Uniqueness is not required.

Reverse HOLD does not use L(A). Neighbor-only reverse already fails from
`S(A)={+e_1, +e_3}` against `S(B)={+e_1, +e_3}`. Union with `L(A)=+e_3`
leaves `S^+(A)` unchanged. No own-neighbor pair `L(A)` against `S(B)`, no
own-own pair `L(A)` against `L(B)`, and no neighbor-neighbor pair is
opposite. Including `L(A)` does not create reverse HOLD. This does not use
`L(A)` to hold reverse.

Same-tick ∪ own incoming lock on the y-symmetric three-site y-probe frame
reports `S^+(A)={+e_1, −e_1}` from seed letter `L(A)=−e_1` added to `{+e_1}`
at `t(A)=0` on a different frame: there the union is not a no-op and reverse
holds. Same-tick ∪ own incoming lock on the y-symmetric three-site x-probe
frame reports `{+e_1, +e_2, −e_2, +e_3, −e_3}` at `A`. Unique own-incoming
letters on these z-probes are `+e_3`, `+e_1`, `UNDEFINED`, `+e_1`. Own-lock-in
at formation reports `{+e_1, +e_3}`, `{+e_1, +e_3}`, `{+e_3}`, `{+e_1, +e_3}`.
Later-tick `S_*` union own lock on these z-probes reports
`{+e_1, −e_1, +e_3}` at `A` after waiting for a global later T. Two-site
opposite-lock same-tick ∪ own on these z-probes reports
`S^+(C)={+e_1, −e_1, −e_2, +e_3}` without `+e_2`.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S^+(A)` and `b` in
`S^+(B)` with `a+b=(0,0,0)`. Both sets are nonempty:
`S^+(A)={+e_1, +e_3}` and `S^+(B)={+e_1, +e_3}`. Every pair sums to
`(2,0,0)`, `(1,0,1)`, or `(0,0,2)`. No pair is opposite. Reverse fails.

Reverse: fail

This is not `hold` and not `UNDEFINED`. Reverse HOLD does not use `L(A)`.
Unique lock-vector lettering of the same lists would assign mixed `S^+(A)`
and mixed `S^+(B)` and would report reverse `UNDEFINED`. That readout is a
different object and is not used. A sum leftover of the same lists would
replace the sets by `(1,0,1)` and `(1,0,1)` and would also fail reverse,
while mixing remains a set here. Unique own-incoming lock-vector letters on
these z-probes report reverse fail from `L(A)=+e_3` and `L(B)=+e_1`; that
leftover is a different object because its face report at mixed `C` is
`UNDEFINED`. Own-lock-in at formation also reports reverse fail, from the
same pair of mixed sets at `A` and `B` but a different face set at `C`.
Formation-tick existential opposite that excludes `q` reports reverse fail
from `{+e_1}` against `{+e_3}`. Later-tick `S_*` union own lock on these
z-probes reports reverse hold after waiting for a global later T that fills
`S^+(A)` with `−e_1`. Same-tick ∪ own incoming lock on the y-symmetric
three-site y-probe frame reports reverse hold from seed letter `−e_1` at
`A`. Reverse fails.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S^+(C)` and `d` in
`S^+(D)` with `c+d=(0,0,0)`. Both sets are nonempty:
`S^+(C)={+e_1, −e_1, +e_2, −e_2, +e_3}` and `S^+(D)={+e_1, +e_3}`, so
`−e_1+(+e_1)=(0,0,0)`. Face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.

This is not `fail` and not `UNDEFINED`. Face hold uses the same-tick mixed
neighbors `(0, 1, 2)` and `(0, -1, 2)` at `C`, not `L(C)`: `L(C)` is
`UNDEFINED`. Unique own-incoming lock-vector letters on these same z-probes
assign `L(C)=UNDEFINED` from two earliest incoming steps and report face
`UNDEFINED`. Unique lock-vector lettering of the inclusive lists would also
report face `UNDEFINED` because `C` mixes. A sum leftover would replace the
sets by `(0,0,1)` and `(1,0,1)` and would fail face, while existential
opposite holds. Named-sign lettering lost the axis in mixed `{+,−}` at `C`.
Own-lock-in at formation reports `S^+(C)={+e_3}` and `S^+(D)={+e_1, +e_3}`
and fails face. Formation-tick existential opposite that excludes `q`
reports `{+e_3}` at both `C` and `D` and fails face. Later-tick `S_*` union
own lock on these z-probes reports face hold from a larger later set at `D`.
Same-tick ∪ own incoming lock on the y-symmetric three-site y-probe frame
reports face hold on different sets. Two-site opposite-lock same-tick ∪ own
on these z-probes also reports face hold, but from
`S^+(C)={+e_1, −e_1, −e_2, +e_3}` without `+e_2`.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify `S^+` with the probe's own incoming `{±e_i}` alone.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the same-tick-inclusive lock set to be a singleton.
- It does not sum the same-tick-inclusive lock set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from same-tick-inclusive six-neighbor locks.
- It does not census a sixteen-combination free lettering independent of
  same-tick-inclusive lock vectors.
- It does not wait for a global later T.
- It does not reprint unique own-incoming lock-vector letters on these
  z-probes.
- It does not reprint later-tick `S_*` union own lock.
- It does not reprint own-lock-in at formation.
- It does not reprint formation-tick existential opposite that excludes `q`.
- It does not reprint same-tick-inclusive existential opposite that excludes
  `q`.
- It does not reprint same-tick ∪ own incoming lock on the y-symmetric
  three-site y-probe frame.
- It does not reprint two-site opposite-lock same-tick ∪ own leftover.
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
y-symmetric three-site process, the same-tick-inclusive six-neighbor lock sets
union own incoming lock, and the existential-opposite reverse/face predicates
are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; y-symmetric three-site seed `+e_1/−e_1/−e_1` |
| same-tick-inclusive six-neighbor lock sets union own incoming at each probe's own `t`, no global T | Theorem 1 |
| `t`, `L`, `S^+` at `A,B,C,D` | Theorem 1; ticks `1,2,4,2`; letters `+e_3`, `+e_1`, `UNDEFINED`, `+e_1`; union happens to leave `S` |
| reverse HOLD uses `L(A)` | Theorem 1; no; reverse fails |
| reverse and face | Theorems 2–3; `fail` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| probe's own incoming lock as the whole set | not used |
| formation member from same-tick-inclusive six-neighbor locks | not attached |
| leftover of unique own-incoming letters on these z-probes | not this display |
| leftover of later-tick `S_*` union own lock | not this display |
| leftover of own-lock-in at formation | not this display |
| leftover of formation-tick existential opposite that excludes `q` | not this display |
| leftover of same-tick-inclusive existential opposite that excludes `q` | not this display |
| leftover of same-tick ∪ own incoming lock on the y-symmetric three-site y-probe frame | not this display |
| leftover of two-site opposite-lock same-tick ∪ own on these z-probes | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: same-tick ∪ own incoming lock on the four y-symmetric three-site z-probes, no global T, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed same-tick-inclusive union-own-lock reverse/face report on these four y-symmetric three-site z-probes. |
| V3 | Own-tick lock sets, own letters, and the `fail`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads six-neighbor lock vectors at each probe's own tick, unions the probe's own incoming lock when defined, and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not identify them with the probe's own incoming steps
alone, does not reduce them to named signs, does not require a singleton
lock vector, does not sum the lock set, does not wait for a global later T,
does not reprint unique own-incoming letters, does not reprint later-tick
`S_*` union own lock, does not reprint own-lock-in at formation, does not
reprint same-tick ∪ own incoming lock on the y-symmetric three-site y-probe
frame, does not reprint two-site opposite-lock leftover, and does not use
occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same neighbor locks | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while both pairs of sets are nonempty |
| sum of the same neighbor locks | replace `S^+` by the `Z^3` sum | refused; leftover; sum of `S^+(A)` and of `S^+(B)` is `(1,0,1)` and `(1,0,1)`; sum of `S^+(C)` and of `S^+(D)` is `(0,0,1)` and `(1,0,1)` and would fail face while `−e_1+(+e_1)=0` |
| named-sign lettering of the same neighbor locks | map `±e_i` to `{+,−}` | refused; lost the axis; mixed `{+,−}` at `C` would hide `−e_1+(+e_1)=0` |
| identify `S^+` with the probe's own incoming `{±e_i}` | map `A`'s incoming `+e_3` onto `S^+(A)` | refused; `S^+(A)` is not `{+e_3}`; `S^+(A)={+e_1, +e_3}` |
| unique own-incoming lock-vector leftover on these z-probes | reuse `L(A)=+e_3`, `L(B)=+e_1`, `L(C)=UNDEFINED`, `L(D)=+e_1` | refused; different object; that leftover reports reverse fail and face `UNDEFINED` while same-tick `S^+(C)` is nonempty and face holds |
| leftover of later-tick `S_*` union own lock | wait for a global later T and reuse later lists | refused; no global T; later-tick reverse holds from `−e_1` at `A` while this reverse fails |
| leftover of own-lock-in at formation | reuse strictly-earlier neighbors union `L(q)` at `t(q)` | refused; different sets; that leftover reports reverse fail and face fail while this face holds |
| leftover of formation-tick existential opposite that excludes `q` | reuse tick `< t(q)` without `L(q)` | refused; different sets `{+e_1}`, `{+e_3}`, `{+e_3}`, `{+e_3}`; that leftover reports face fail |
| leftover of same-tick-inclusive existential opposite that excludes `q` | reuse `S` without reporting `L` or forming `S^+` | refused; the union happens to leave `S` unchanged on these z-probes, but `L(C)` is `UNDEFINED` while `S(C)` is nonempty and `L` is part of Theorem 1 |
| leftover of same-tick ∪ own incoming lock on the y-symmetric three-site y-probe frame | reuse y-probe lists with seed letter `−e_1` at `A` | refused; cubic-frame transfer, not leftover of those lists; `t(A)=1` and reverse fails here |
| leftover of same-tick ∪ own incoming lock on the y-symmetric three-site x-probe frame | reuse x-probe lists | refused; different frame; `S^+(A)` here is not `{+e_1, +e_2, −e_2, +e_3, −e_3}` |
| leftover of two-site opposite-lock same-tick ∪ own on these z-probes | reuse seed `{0,(0,1,0)}` and `S^+(C)` without `+e_2` | refused; different process; the y-mirror seed site `(0,-1,0)` is a seed here and `+e_2` is in `S^+(C)` |
| leftover of three-site opposite-lock seed with third site `(1,0,0)` | reuse seed `+e_1/−e_1/+e_2` | refused; different process; the third seed here is `(0,-1,0)` with `−e_1` |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| attach a formation member from same-tick-inclusive six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; both earliest incoming steps at `C` are kept |
| reverse HOLD from `L(A)` | claim reverse holds by adding `L(A)` | refused; reverse HOLD does not use `L(A)`; reverse fails |

### N2 — wall independence

Missing physical adoption, missing formation attachment from same-tick-inclusive
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, y-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, same-tick-inclusive lock
set of six-neighbors formed by each probe's own `t` with no global later T,
union with `L(q)` when defined, existential opposite, four z-probes with
non-seed `A`, and reverse/face as existence of a pair that sums to zero are
declared. No uniqueness of incoming locks, no occupancy `n`, no named-sign
reduction, no singleton leftover, no sum leftover, no unique own-incoming
leftover, no later-tick leftover, no own-lock-in leftover, no y-symmetric
y-probe leftover, no two-site opposite-lock leftover, no formation
attachment from same-tick-inclusive six-neighbor locks, and no Admissibility
rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in a same-tick-inclusive union set | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `S^+` lock sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Once a six-neighbor exists at the probe's own tick, the site
should lock that unique vector as incoming content, mixed neighbor locks
should make reverse and face `UNDEFINED`, the sets should be replaced by
their sums, unique own-incoming letters already answered reverse fail with
face `UNDEFINED`, later-tick union own lock already answered the cubic with
hold/hold, own-lock-in at formation already unioned `L(q)`, same-tick
exclude-`q` already has the same lists, y-probe same-tick ∪ own already
holds reverse and face on this seed, two-site opposite-lock same-tick ∪ own
already answered fail/hold on these z-probes, named signs should suffice
because they keep orientation, occupancy `n` should track that vector, and
reverse should hold because `L(A)` is included.

**Answer:** The named construction reports lock sets `{+e_1, +e_3}`,
`{+e_1, +e_3}`, `{+e_1, −e_1, +e_2, −e_2, +e_3}`, `{+e_1, +e_3}` at
`A,B,C,D` from same-tick-inclusive six-neighbor locks union `L(q)` at each
own tick, with no global T. Mixed remains a set. The construction does not
sum. Occupancy `n` is not used. Named signs lost the axis. No pair from
`S^+(A)` and `S^+(B)` is opposite, so reverse fails. Reverse HOLD does not
use `L(A)`. Face holds from `−e_1+(+e_1)=(0,0,0)`. The union happens to
leave `S` unchanged on these z-probes, but Theorem 1 still reports `L` and
`S^+`. The sets are not leftover of unique own-incoming letters, not leftover
of own-lock-in at formation, not leftover of later-tick `S_*` union own lock,
not leftover of same-tick ∪ own incoming lock on the y-symmetric three-site
y-probe frame, and not leftover of two-site opposite-lock same-tick ∪ own:
that leftover omits `+e_2` from `S^+(C)`. The bits remain displayed.
Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same z-probes would
assign `L(A)=+e_3`, `L(B)=+e_1`, `L(C)=UNDEFINED`, `L(D)=+e_1` and report
reverse fail with face `UNDEFINED`. Own-lock-in at formation on these
z-probes assigns `{+e_1, +e_3}`, `{+e_1, +e_3}`, `{+e_3}`, `{+e_1, +e_3}`
and reports reverse fail and face fail. Formation-tick existential opposite
that excludes `q` reports reverse fail and face fail from `{+e_1}`, `{+e_3}`,
`{+e_3}`, `{+e_3}`. Later-tick `S_*` union own lock on these z-probes reports
reverse hold and face hold at a global later T. Same-tick ∪ own incoming
lock on the y-symmetric three-site y-probe frame reports reverse hold and
face hold on different sets, with seed letter `−e_1` added at `A`. Two-site
opposite-lock same-tick ∪ own on these z-probes reports reverse fail and
face hold from `S^+(C)={+e_1, −e_1, −e_2, +e_3}` without `+e_2`. Unique
lock-vector lettering of the inclusive lists would report reverse
`UNDEFINED` and face `UNDEFINED` because `A`, `B`, and `C` mix. A sum
leftover of the same lists would report reverse fail and face fail because
the sums are `(1,0,1)` and `(1,0,1)`. This note is not those displays: mixed
remains a set, the construction does not sum, no opposite pair so reverse
fails, reverse HOLD does not use `L(A)`, and `−e_1+(+e_1)=(0,0,0)` so face
holds.

**Gate disposition:** PASS for the same-tick-inclusive six-neighbor-lock
union own incoming reverse/face reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique singleton
lock vector,” “the predicate equals the sum of the lock set,” “the lock set
equals the probe's own incoming step,” “bits are Admissibility,” “the letter
is occupancy `n`,” “the sets equal unique own-incoming letters,” “the sets
equal later-tick `S_*` union own lock,” “the sets equal own-lock-in at
formation,” “the sets equal y-symmetric three-site y-probe same-tick union
leftover,” “the sets equal two-site opposite-lock leftover,” “reverse holds,”
“reverse HOLD uses `L(A)`,” or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the y-symmetric three-site
perp-step incoming-lock process, collects six-neighbor locks formed by each
probe's own tick with the probe excluded, unions `L(q)` when defined, reads
`t`, `L`, and `S^+` at the four z-probes with no global T, and checks
Theorems 1--3. It also checks that reverse HOLD does not use `L(A)`, that
the construction is not named-sign lettering, that mixed sets remain
defined, that the construction does not sum, that occupancy `n` is not used,
that a formation member from same-tick-inclusive six-neighbor locks is not
attached, that the sets are not leftover of unique own-incoming letters,
that the sets are not leftover of later-tick `S_*` union own lock, that the
sets are not leftover of own-lock-in at formation, that the sets are not
leftover of same-tick ∪ own incoming lock on the y-symmetric three-site
y-probe frame, and that the sets are not leftover of two-site opposite-lock
same-tick ∪ own. No runner cache is written.
