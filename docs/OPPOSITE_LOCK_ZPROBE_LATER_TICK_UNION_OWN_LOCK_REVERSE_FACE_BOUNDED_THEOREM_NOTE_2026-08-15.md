---
claim_id: opposite_lock_zprobe_later_tick_union_own_lock_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from existential opposite in later-tick 6-NN locks union the probe's own incoming lock on the four nsopp z-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_zprobe_later_tick_union_own_lock_reverse_face_2026_08_15.py
---

# Later-Tick Six-Neighbor Locks Union Own Incoming Reverse And Face On Four Opposite-Lock Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from existential opposite in later-tick
six-neighbor locks union the probe's own incoming lock on the four nsopp
z-probes in `B_3(0)`. Let `t(q)` be the formation tick of probe `q`. Let
`L(q)` be `q`'s own unique incoming lock; seeds use seed letters. If several
earliest incoming steps exist, `L(q)` is `UNDEFINED`. Let `T` be the maximum
of `t(A)`, `t(B)`, `t(C)`, `t(D)` among those defined in `B_3(0)`: the first
later tick at which all four z-probes are recorded. At tick `T`, `S_*(q)` is
the set of locks of six-neighbors of `q` that formed at tick `≤ T` and are
not `q`. `S^T_+(q)` is `S_*(q)` union `{L(q)}` when `L(q)` is defined.
Reverse holds if and only if some lock in `S^T_+(A)` is the vector opposite
of some lock in `S^T_+(B)`. Face holds if and only if some lock in
`S^T_+(C)` is the vector opposite of some lock in `S^T_+(D)`. Empty `S^T_+`
on either side of a comparison is `UNDEFINED`; nonempty with no opposite
pair fails. Occupancy `n` is not used. This is not named-sign lettering.
This is not a unique lock-vector leftover and not a sum leftover. This is a
cubic-frame transfer of later-tick `S_*` union own lock, not leftover of
later-tick existential opposite that excludes `q`: that display does not
use `L(q)`, and the union happens to leave `S_*` unchanged on these four
z-probes because each defined `L(q)` already appears as a neighbor lock.
This is not leftover of own-lock-in at formation: that readout scores
strictly-earlier neighbors union `L(q)` at `t(q)` and reports reverse fail
and face fail. This is not leftover of later-tick S_* union own lock on the opposite-lock
y-probe frame: that display uses seed letter `L(A)=−e_1` and a different
frame at `T=3`. This is not leftover of unique own-incoming
lock-vector letters on these z-probes: that readout reports reverse fail
with face `UNDEFINED` at mixed `C`. Uniqueness of incoming locks is not
required. Uniqueness of the lock set is not required. Displayed, not
adopted. This note does not write existential opposite into Admissibility
and does not attach a formation member from later-tick six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_zprobe_later_tick_union_own_lock_reverse_face_2026_08_15.py`](../scripts/opposite_lock_zprobe_later_tick_union_own_lock_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in
`S^T_+`. Named signs `{+,−}` are a coarser readout and are not used. A
singleton unique lock-vector letter is a different readout and is not used.
A `Z^3` sum of those locks is a different readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of T, L, S_*, and S^T_+ as later-tick six-neighbor locks union L(q) when defined, on the four nsopp z-probes, with reverse hold and face hold from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_zprobe_later_tick_union_own_lock_reverse_face
target_blocker_text: "display reverse and face from existential opposite in later-tick 6-NN locks union the probe's own incoming lock on the four nsopp z-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with later-tick leftover that excludes q, do not identify the sets with own-lock-in at formation, do not identify the sets with y-probe later-tick union leftover, and do not identify the sets with unique own-incoming leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of later-tick six-neighbor locks union own incoming lock on the four nsopp z-probes; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose later-tick
union sets are scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`,
`C=(2,0,0)`, `D=(1,1,0)`. `A` is not a seed.

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
`q`. Seeds keep their seed letters.

## Named existential opposite from later-tick six-neighbor locks union own incoming

Let `t(q)` be the formation tick of z-probe `q` when that tick is defined in
`B_3(0)`. Let `T` be the maximum of those four ticks. This `T` is the first
later tick in `B_3(0)` at which all four z-probes are recorded.

At tick `T`, for each probe `q`, let `S_*(q)` be the set of locks of
six-neighbors of `q` that formed at tick `≤ T` and are not `q`. Same-tick
and later-than-formation neighbors count whenever they have formed by `T`.
The probe itself is excluded. Let `L(q)` be `q`'s own unique incoming lock;
if several earliest incoming steps exist, `L(q)` is `UNDEFINED`. Then
`S^T_+(q) = S_*(q)` union `{L(q)}` when `L(q)` is defined, and
`S^T_+(q) = S_*(q)` when `L(q)` is `UNDEFINED`. This display does not use
occupancy `n`. Duplicate locks at two neighbors collapse in the set. The
construction does not require `S^T_+(q)` to be a singleton. It does not sum
`S^T_+(q)`. It is not a unique lock-vector leftover and not a sum leftover.
It is not leftover of later-tick existential opposite that excludes `q`. It
is not leftover of own-lock-in at formation. It is not leftover of later-tick
`S_*` union own lock on the opposite-lock y-probe frame. It is not leftover
of unique own-incoming lock-vector letters on these z-probes.

Incoming `{±e_i}` tags of the probe itself are members of `S^T_+(q)` only
through the union when `L(q)` is defined, or if they already appear as a
neighbor lock in `S_*(q)`. Identifying a named sign of those locks with
reverse or face is refused: named-sign lettering lost the axis. Reverse and
face are scored on existence of a pair of lock vectors that add to zero.
They are not scored on `{+,−}` names and are not an occupancy-kernel inner
product.

Reverse and face (displayed):

```text
reverse  <=>  some a in S^T_+(A) and some b in S^T_+(B) with a+b=(0,0,0)
face     <=>  some c in S^T_+(C) and some d in S^T_+(D) with c+d=(0,0,0)
```

If `S^T_+(A)` or `S^T_+(B)` is empty, reverse is `UNDEFINED`. Else reverse
fails if no such pair exists. If `S^T_+(C)` or `S^T_+(D)` is empty, face is
`UNDEFINED`. Else face fails if no such pair exists. The report is one of
`hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility.

## Theorem 1 — later-tick T, L, S_*, and S^T_+ at each z-probe

Direct enumeration of the displayed opposite-lock process on `B_3(0)` forms
all four z-probes. The formation ticks are t(A)=1, t(B)=2, t(C)=4, t(D)=2.
`A` is not a seed. All four are defined in `B_3(0)`, so

```text
T = max{t(A), t(B), t(C), t(D)} = 4.
```

Own unique incoming letters:

```text
L(A) = +e_3
L(B) = +e_1
L(C) = UNDEFINED
L(D) = +e_1
```

`C` has three earliest incoming steps `−e_1`, `+e_2`, and `+e_1`, so `L(C)`
is `UNDEFINED`. Uniqueness is not required.

At tick `T=4` the six-neighbor lock lists, lock sets, and union sets are:

```text
A: +e_1 at (1, 0, 1), −e_1 at (-1, 0, 1), +e_3 at (0, 1, 1),
   −e_2 at (0, -1, 1), +e_3 at (0, -1, 1), −e_1 at (0, 0, 2),
   +e_2 at (0, 0, 2), +e_1 at (0, 0, 2), +e_1 at (0, 0, 0);
   S_*(A) = {+e_1, −e_1, +e_2, −e_2, +e_3}
   S^T_+(A) = {+e_1, −e_1, +e_2, −e_2, +e_3}
B: +e_3 at (0, 1, 1), +e_3 at (1, 2, 1), +e_2 at (1, 2, 1),
   +e_1 at (1, 2, 1), +e_1 at (1, 0, 1), +e_3 at (1, 1, 2),
   −e_2 at (1, 1, 0), −e_3 at (1, 1, 0), +e_3 at (1, 1, 0);
   S_*(B) = {+e_1, +e_2, −e_2, +e_3, −e_3}
   S^T_+(B) = {+e_1, +e_2, −e_2, +e_3, −e_3}
C: +e_3 at (1, 0, 2), +e_3 at (-1, 0, 2), −e_1 at (0, 1, 2),
   −e_2 at (0, 1, 2), +e_1 at (0, 1, 2), +e_3 at (0, -1, 2),
   +e_3 at (0, 0, 1);
   S_*(C) = {+e_1, −e_1, −e_2, +e_3}
   S^T_+(C) = {+e_1, −e_1, −e_2, +e_3}
D: +e_3 at (0, 0, 1), +e_1 at (1, 1, 1), −e_2 at (1, -1, 1),
   +e_3 at (1, -1, 1), +e_1 at (1, -1, 1), +e_3 at (1, 0, 2),
   −e_3 at (1, 0, 0), +e_3 at (1, 0, 0), +e_2 at (1, 0, 0);
   S_*(D) = {+e_1, +e_2, −e_2, +e_3, −e_3}
   S^T_+(D) = {+e_1, +e_2, −e_2, +e_3, −e_3}
```

`A`'s later-tick neighbors include the same-tick seed origin locking `+e_1`
and later `C` mixing `−e_1`, `+e_2`, and `+e_1`. `L(A)=+e_3` already appears
in `S_*(A)` as a neighbor lock at `(0, 1, 1)` and `(0, -1, 1)`, so the union
happens to leave `S_*(A)` unchanged. `L(B)=+e_1` already appears in
`S_*(B)`. `L(C)` is `UNDEFINED`, so `S^T_+(C)=S_*(C)`. `L(D)=+e_1` already
appears in `S_*(D)`. Mixed remains a set. The construction still unions
`L(q)` when defined: that is a different object from later-tick existential
opposite that excludes `q`, even though the four sets coincide here.

Incoming locks exist and need not be unique. The lock sets are not identified
with those incoming steps alone. Uniqueness is not required.

Later-tick `S_*` union own lock on the opposite-lock y-probe frame reports
`S^T_+(A)={+e_1, −e_1, +e_2, −e_2, +e_3, −e_3}` from seed letter
`L(A)=−e_1` at `T=3` on a different frame: there the union adds `−e_1` that
`S_*(A)` lacks. Later-tick `S_*` union own lock on the opposite-lock x-probe
frame reports `{+e_1, −e_2, +e_3, −e_3}` at `A`. Unique own-incoming letters
on these z-probes are `+e_3`, `+e_1`, `UNDEFINED`, `+e_1`. Own-lock-in at
formation reports `{+e_1, +e_3}`, `{+e_1, +e_3}`, `{+e_3}`, `{+e_1, +e_3}`.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S^T_+(A)` and `b` in
`S^T_+(B)` with `a+b=(0,0,0)`. Both sets are nonempty:
`S^T_+(A)={+e_1, −e_1, +e_2, −e_2, +e_3}` and
`S^T_+(B)={+e_1, +e_2, −e_2, +e_3, −e_3}`. The pairs include
`−e_1+(+e_1)=(0,0,0)`, `+e_2+(−e_2)=(0,0,0)`, and `+e_3+(−e_3)=(0,0,0)`.
Reverse holds.

Reverse: hold

This is not `fail` and not `UNDEFINED`. Unique lock-vector lettering of the
same lists would assign mixed `S^T_+(A)` and mixed `S^T_+(B)` and would
report reverse `UNDEFINED`. That readout is a different object and is not
used. A sum leftover of the same lists would replace the sets by `+e_3` and
`+e_1` and would report reverse fail. A named-sign readout of the same
neighbor locks would lose the axis in mixed `{+,−}` at both `A` and `B`.
Unique own-incoming lock-vector letters on these z-probes report reverse
fail from `L(A)=+e_3` and `L(B)=+e_1`. Own-lock-in at formation reports
reverse fail from `{+e_1, +e_3}` at both `A` and `B`. Later-tick existential
opposite that excludes `q` also reports reverse hold, but does not report
`L` and does not form `S^T_+`. Later-tick `S_*` union own lock on the
opposite-lock y-probe frame also reports reverse hold, from a different set
at `T=3` that includes seed letter `−e_1` at `A`.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S^T_+(C)` and `d` in
`S^T_+(D)` with `c+d=(0,0,0)`. Both sets are nonempty:
`S^T_+(C)={+e_1, −e_1, −e_2, +e_3}` and
`S^T_+(D)={+e_1, +e_2, −e_2, +e_3, −e_3}`, so `−e_1+(+e_1)=(0,0,0)`,
`−e_2+(+e_2)=(0,0,0)`, and `+e_3+(−e_3)=(0,0,0)`. Face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.

This is not `fail` and not `UNDEFINED`. Unique own-incoming lock-vector
letters on these same z-probes assign `L(C)=UNDEFINED` from three earliest
incoming steps and report face `UNDEFINED`. Unique lock-vector lettering of
the later-tick lists would also report face `UNDEFINED` because both `C` and
`D` mix. A sum leftover would replace the sets by `(0,−1,1)` and `+e_1` and
would fail face, while existential opposite holds. Named-sign lettering lost
the axis in mixed `{+,−}` at `C` and at `D`. Own-lock-in at formation reports
`S^+(C)={+e_3}` and `S^+(D)={+e_1, +e_3}` and fails face. Later-tick
`S_*` union own lock on the opposite-lock y-probe frame reports face hold on
different sets.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not identify `S^T_+` with the probe's own incoming `{±e_i}` alone.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the later-tick lock set to be a singleton.
- It does not sum the later-tick lock set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from later-tick six-neighbor locks.
- It does not census a sixteen-combination free lettering independent of
  later-tick lock vectors.
- It does not reprint unique own-incoming lock-vector letters on these
  z-probes.
- It does not reprint later-tick existential opposite that excludes `q`.
- It does not reprint own-lock-in at formation.
- It does not reprint later-tick `S_*` union own lock on the opposite-lock
  y-probe frame.
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
opposite-lock process, the later-tick six-neighbor lock sets union own
incoming lock, and the existential-opposite reverse/face predicates are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; opposite-lock two-site seed `+e_1/−e_1` |
| later-tick six-neighbor lock sets union own incoming at first `T` with all four z-probes recorded | Theorem 1 |
| `T`, `L`, `S_*`, `S^T_+` at `A,B,C,D` | Theorem 1; `T=4`; letters `+e_3`, `+e_1`, `UNDEFINED`, `+e_1`; union happens to leave `S_*` |
| reverse and face | Theorems 2–3; `hold` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| probe's own incoming lock as the whole set | not used |
| formation member from later-tick six-neighbor locks | not attached |
| leftover of unique own-incoming letters on these z-probes | not this display |
| leftover of later-tick existential opposite that excludes `q` | not this display |
| leftover of own-lock-in at formation | not this display |
| leftover of later-tick `S_*` union own lock on the opposite-lock y-probe frame | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: existential opposite of later-tick 6-NN locks union the probe's own incoming lock on the four nsopp z-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed later-tick union-own-lock reverse/face report on these four opposite-lock z-probes. |
| V3 | Later-tick lock sets, own letters, and the `hold`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads six-neighbor lock vectors at a later common tick, unions the probe's own incoming lock when defined, and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not identify them with the probe's own incoming steps
alone, does not reduce them to named signs, does not require a singleton
lock vector, does not sum the lock set, does not reprint unique own-incoming
letters, does not reprint later-tick existential opposite that excludes `q`,
does not reprint own-lock-in at formation, does not reprint later-tick `S_*`
union own lock on the opposite-lock y-probe frame, and does not use occupancy
`n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same neighbor locks | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while both pairs of sets are nonempty |
| sum of the same neighbor locks | replace `S^T_+` by the `Z^3` sum | refused; leftover; sum of `S^T_+(A)` and of `S^T_+(B)` is `+e_3` and `+e_1` and would fail reverse while `−e_1+(+e_1)=0`; sum of `S^T_+(C)` and of `S^T_+(D)` is `(0,−1,1)` and `+e_1` and would fail face |
| named-sign lettering of the same neighbor locks | map `±e_i` to `{+,−}` | refused; lost the axis; mixed `{+,−}` at `A` and at `B` would hide `−e_1+(+e_1)=0` |
| identify `S^T_+` with the probe's own incoming `{±e_i}` | map `A`'s incoming `+e_3` onto `S^T_+(A)` | refused; `S^T_+(A)` is not `{+e_3}`; `S^T_+(A)={+e_1, −e_1, +e_2, −e_2, +e_3}` |
| unique own-incoming lock-vector leftover on these z-probes | reuse `L(A)=+e_3`, `L(B)=+e_1`, `L(C)=UNDEFINED`, `L(D)=+e_1` | refused; different object; that leftover reports reverse fail and face `UNDEFINED` while later-tick `S^T_+(C)` is nonempty and reverse and face hold |
| leftover of later-tick existential opposite that excludes `q` | reuse `S_*` without reporting `L` or forming `S^T_+` | refused; cubic-frame transfer of later-tick union own lock; the union happens to leave `S_*` unchanged on these z-probes, but `L(C)` is `UNDEFINED` while `S_*(C)` is nonempty and `L` is part of Theorem 1 |
| leftover of own-lock-in at formation | reuse strictly-earlier neighbors union `L(q)` at `t(q)` | refused; different tick and different sets; that leftover reports reverse fail and face fail while later-tick reverse and face hold |
| leftover of later-tick `S_*` union own lock on the opposite-lock y-probe frame | reuse y-probe lists at `T=3` with seed letter `−e_1` at `A` | refused; cubic-frame transfer, not leftover of those lists; `T=4` and `S^T_+(A)`, `S^T_+(C)` differ |
| leftover of later-tick `S_*` union own lock on the opposite-lock x-probe frame | reuse x-probe lists | refused; different frame; `S^T_+(A)` here is not `{+e_1, −e_2, +e_3, −e_3}` |
| leftover of nnseed x-probe later-tick existential opposite | reuse seed `+e_1/+e_2` and x-probes with reverse fail | refused; different process and different frame; reverse holds here |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; not this display |
| attach a formation member from later-tick six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; all three earliest incoming steps at `C` are kept |

### N2 — wall independence

Missing physical adoption, missing formation attachment from later-tick
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, later-tick lock set of six-neighbors formed by the
first `T` at which all four z-probes are recorded, union with `L(q)` when
defined, existential opposite, four z-probes with non-seed `A`, and
reverse/face as existence of a pair that sums to zero are declared. No
uniqueness of incoming locks, no occupancy `n`, no named-sign reduction, no
singleton leftover, no sum leftover, no unique own-incoming leftover, no
later-tick exclude-`q` leftover, no own-lock-in leftover, no opposite-lock
y-probe leftover, no formation attachment from later-tick six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in a later-tick union set | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `S^T_+` lock sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Once a six-neighbor exists at the later common tick, the site
should lock that unique vector as incoming content, mixed neighbor locks
should make reverse and face `UNDEFINED`, the sets should be replaced by
their sums, unique own-incoming letters already answered reverse fail with
face `UNDEFINED`, later-tick existential opposite that excludes `q` already
answered the later-tick question with the same lists, own-lock-in at
formation already unioned `L(q)`, named signs should suffice because they
keep orientation, and occupancy `n` should track that vector.

**Answer:** The named construction reports lock sets
`{+e_1, −e_1, +e_2, −e_2, +e_3}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}`,
`{+e_1, −e_1, −e_2, +e_3}`, `{+e_1, +e_2, −e_2, +e_3, −e_3}` at
`A,B,C,D` from later-tick six-neighbor locks union `L(q)` at `T=4`. Mixed
remains a set. The construction does not sum. Occupancy `n` is not used.
Named signs lost the axis. Some pair from `S^T_+(A)` and `S^T_+(B)` is
opposite, so reverse holds. Face holds. The union happens to leave `S_*`
unchanged on these z-probes, but Theorem 1 still reports `L` and `S^T_+`.
The sets are not leftover of unique own-incoming letters, not leftover of
own-lock-in at formation, and not leftover of later-tick `S_*` union own
lock on the opposite-lock y-probe frame. The bits remain displayed.
Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same opposite-lock
z-probes assigned `L(A)=+e_3`, `L(B)=+e_1`, `L(C)=UNDEFINED`, `L(D)=+e_1` and
reported reverse fail with face `UNDEFINED`. Own-lock-in at formation on
these z-probes assigned `{+e_1, +e_3}`, `{+e_1, +e_3}`, `{+e_3}`,
`{+e_1, +e_3}` and reported reverse fail and face fail. Later-tick
existential opposite that excludes `q` reported reverse hold and face hold
from `S_*` without unioning `L(q)`. Later-tick `S_*` union own lock on the
opposite-lock y-probe frame reported reverse hold and face hold on different
sets at `T=3`, with seed letter `−e_1` added at `A`. Unique lock-vector
lettering of the later-tick lists would report reverse `UNDEFINED` and face
`UNDEFINED` because every later-tick set mixes. A sum leftover of the same
lists would report reverse fail and face fail because the sums are `+e_3`
and `+e_1`. This note is not those displays: mixed remains a set, the
construction does not sum, `−e_1+(+e_1)=(0,0,0)` so reverse holds, and
`−e_1+(+e_1)=(0,0,0)` so face holds.

**Gate disposition:** PASS for the later-tick six-neighbor-lock union own
incoming reverse/face reports above. FAIL / DO NOT SHIP for “the predicate
equals the named sign,” “the predicate equals the unique singleton lock
vector,” “the predicate equals the sum of the lock set,” “the lock set
equals the probe's own incoming step,” “bits are Admissibility,” “the letter
is occupancy `n`,” “the sets equal unique own-incoming letters,” “the sets
equal later-tick existential opposite that excludes `q` without reporting
`L`,” “the sets equal own-lock-in at formation,” “the sets equal
opposite-lock y-probe later-tick union leftover,” “reverse fails,” or “face
is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the opposite-lock two-site
perp-step incoming-lock process, takes `T` as the first tick at which all four
z-probes are recorded, collects six-neighbor locks formed by `T` at each
probe with the probe excluded, unions `L(q)` when defined, reads `T`, `L`,
`S_*`, and `S^T_+` at the four z-probes, and checks Theorems 1--3. It also
checks that the construction is not named-sign lettering, that mixed sets
remain defined, that the construction does not sum, that occupancy `n` is
not used, that a formation member from later-tick six-neighbor locks is not
attached, that the sets are not leftover of unique own-incoming letters,
that the sets are not leftover of later-tick existential opposite that
excludes `q`, that the sets are not leftover of own-lock-in at formation,
and that the sets are not leftover of later-tick `S_*` union own lock on
the opposite-lock y-probe frame. No runner cache is written.
