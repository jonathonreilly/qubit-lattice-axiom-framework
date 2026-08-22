---
claim_id: opposite_lock_yprobe_own_incoming_set_neighbor_read_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read R of own incoming on the four #7208 y-probes, equality to M, and reverse/face from R are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_yprobe_own_incoming_set_neighbor_read_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Own Incoming Reverse And Face On Four #7208 Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read `R(q)` of own incoming on the four nsmopp #7208
y-probes in `B_3(0)={n:n·n<=9}`, equality of `R` to `M`, and reverse/face
from `R`. Same process as nsopp #7093. Let `t(q)` be the formation tick of
probe `q`. `M(q)` is the set of earliest incoming nearest-neighbor steps at
`q`. Seeds use their seed letter as a singleton. Mixed stays a set. Unformed
is `UNDEFINED`. For formed `q`, `Nbr(q)` is the set of 6-NN of `q` that are
formed in `B_3(0)` and are not `q`. `R(q)` is the set of earliest incoming
NN steps at those neighbors whose step is from `q`:

```text
R(q) = { e in {±e_1,±e_2,±e_3} | q+e in Nbr(q) and (−e) in M(q+e) }.
```

Unformed `q` is `UNDEFINED`. Empty `R` is empty, not `UNDEFINED`. `R` is not
`M` and is not `O`. Read-HOLD at `q` iff `R(q)=M(q)` as sets (both defined,
possibly mixed). Read-fail if both defined and unequal. `UNDEFINED` if either
is `UNDEFINED`. Reverse holds if and only if some lock in `R(A)` is the
vector opposite of some lock in `R(B)`. Face holds if and only if some lock
in `R(C)` is the vector opposite of some lock in `R(D)`. Empty or
`UNDEFINED` on either side of a comparison is `UNDEFINED`; nonempty with no
opposite pair fails. Unique `L` is not the object. The six-neighbor star
`S^+` is not the letter. Occupancy `n` is not used. This is not named-sign
lettering. This is not a unique lock-vector leftover and not a sum leftover.
This is not leftover of unique-L. This is not leftover of #7208 `M`
exist-opposite, which HOLDs reverse from singleton `M(A)={−e_1}` against
`M(B)={+e_1}`. This is not leftover of own outgoing `O`. The letter is
neighbor-read, not own incoming. This is not leftover of #7167 `S^+`. The
six-NN star excluding `A` does not uniquely recover `M(A)`. Uniqueness is
not required. This is not the sister kernel. Displayed, not adopted. Do not
write into Admissibility. Do not attach L1. This note does not write
existential opposite into Admissibility and does not attach a formation
member from already-recorded six-neighbor locks. This display does not use
occupancy. Mixed stays a set. No S⁺.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_yprobe_own_incoming_set_neighbor_read_reverse_face_2026_08_15.py`](../scripts/opposite_lock_yprobe_own_incoming_set_neighbor_read_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `R` is the neighbor-read of those incoming sets. Reverse and face are
scored on existence of an opposite pair in the neighbor-reads. Named signs
`{+,−}` are a coarser readout and are not used. A singleton unique lock-vector
letter is a different readout and is not used as the object: report `R`.
A `Z^3` sum of those locks is a different readout and is not used. The
construction does not sum. No S⁺. R is not M. R is not O.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of R(q) as neighbor-read of own incoming on the four #7208 y-probes, mixed stays a set, with equality R=M as Read-fail at each probe and reverse UNDEFINED plus face UNDEFINED from existential opposite; uniqueness of neighbor-read locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_yprobe_own_incoming_set_neighbor_read_reverse_face
target_blocker_text: "display neighbor-read R of own incoming on the four #7208 y-probes, equality to M, and reverse/face from R, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with unique-L leftover, do not identify the sets with #7208 M leftover, and do not identify the sets with outgoing O leftover."
conditional_surface_status: "exact on B_3(0) for neighbor-read of own incoming on the four #7208 y-probes; displayed, not adopted"
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
neighbor-reads are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed. Same process and y-probes as nsmopp #7208.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`. This seed is not the perp
two-site seed `+e_1/+e_2`. This seed is not the z-symmetric three-site seed
`{0,(0,0,1),(0,0,-1)}`.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept as a
possible lock. Mixed stays a set. Uniqueness is not required. A later parent
does not re-form `q`.

## Named neighbor-read of own incoming

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `M(q)` be the set of earliest incoming nearest-neighbor steps
at `q`. Seeds use their seed letter as a singleton. Mixed stays a set.
Unformed is `UNDEFINED`. For formed `q`, `Nbr(q)` is the set of 6-NN of `q`
that are formed in `B_3(0)` and are not `q`. Let `R(q)` be the neighbor-read
of own incoming:

```text
R(q) = { e in {±e_1,±e_2,±e_3} | q+e in Nbr(q) and (−e) in M(q+e) }.
```

Unformed `q` is `UNDEFINED`. Empty `R` is empty, not `UNDEFINED`. Unique
`L(q)` is not used as the letter. This display does not use a six-neighbor
star as the letter. Occupancy `n` is not used. Duplicate neighbor-read steps
collapse in the set. The construction does not require `R(q)` to be a
singleton. It does not sum `R(q)`. It is not a unique lock-vector leftover
and not a sum leftover. It is not leftover of unique-L. It is not leftover
of #7208 own incoming `M`. It is not leftover of own outgoing `O`. R is not
M. R is not O. The six-NN star excluding `A` does not uniquely recover
`M(A)`. Uniqueness is not required. This is not the sister kernel.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not scored on `{+,−}`
names and are not an occupancy-kernel inner product.

Read equality, reverse, and face (displayed):

```text
read(q)  <=>  R(q) = M(q) as sets, both defined
reverse  <=>  some a in R(A) and some b in R(B) with a+b=(0,0,0)
face     <=>  some c in R(C) and some d in R(D) with c+d=(0,0,0)
```

If `R(q)` or `M(q)` is `UNDEFINED`, read is `UNDEFINED`. Else Read-HOLD if
the sets are equal and Read-fail if they are unequal. If `R(A)` or `R(B)` is
empty or `UNDEFINED`, reverse is `UNDEFINED`. Else reverse fails if no such
pair exists. If `R(C)` or `R(D)` is empty or `UNDEFINED`, face is
`UNDEFINED`. Else face fails if no such pair exists. The report is one of
`hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — formation ticks, M, and R at each y-probe

Direct enumeration of the displayed nsopp #7093 process on `B_3(0)` forms
all four y-probes. The formation ticks are `t(A)=0`, `t(B)=2`, `t(C)=1`,
`t(D)=3`. `A` is a seed. Those ticks locate the earliest incoming set and
the neighbor-read. They are not occupancy kernels and are not a global
later T.

Own incoming sets of #7208 and neighbor-reads at each probe are:

```text
A: seed letter −e_1;
   t(A)=0;  M(A) = {−e_1};  R(A) = {}
B: incoming +e_1;
   t(B)=2;  M(B) = {+e_1};  R(B) = {−e_3}
C: incoming +e_2;
   t(C)=1;  M(C) = {+e_2};  R(C) = {}
D: incoming −e_2, −e_3, +e_3;
   t(D)=3;  M(D) = {−e_2, +e_3, −e_3};  R(D) = {−e_2}
```

`A` is a seed at tick 0. Empty `R` is empty: `R(A)` and `R(C)` are empty
sets, not `UNDEFINED`. Mixed stays a set: `M(D)` has three earliest incoming
steps `−e_2`, `−e_3`, and `+e_3`. Unique-L leftover of `R` would assign
`UNDEFINED` at `A` and at `C` from those empty sets. Uniqueness is not
required.

Equality `R=M` at each probe is Read-fail: both sides are defined and
unequal. The six-NN star excluding `A` does not uniquely recover M(A).
`Nbr(A)` has six formed neighbors and omits `A`; `R(A)` is empty while
`M(A)={−e_1}`.

Compare R to M of #7208 and to O. Same process reports

```text
M(A) = {−e_1},  M(B) = {+e_1},  M(C) = {+e_2},  M(D) = {−e_2, +e_3, −e_3}
O(A) = {+e_2, +e_3, −e_3},  O(B) = {+e_2, +e_3, −e_3},
O(C) = {+e_1, −e_1, +e_3, −e_3},  O(D) = {+e_1, −e_1}
```

and Reverse HOLD of #7208 uses `−e_1` in `M(A)` against `+e_1` in `M(B)`.
Those incoming letters are absent from `R(A)` and `R(B)`. R is not M. R is
not O. No S⁺.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `R(A)` and `b` in `R(B)`
with `a+b=(0,0,0)`. `R(A)` is empty and `R(B)={−e_3}`, so reverse is
`UNDEFINED`.

Reverse: UNDEFINED

This is not `hold` and not `fail`. Reverse is UNDEFINED. Unique-L leftover
of `M` reports reverse hold from unique `L(A)=−e_1` and `L(B)=+e_1`. #7208
`M` leftover reports reverse hold from `−e_1` in `M(A)` against `+e_1` in
`M(B)`. Own outgoing leftover reports reverse hold from `±e_3` in `O(A)` and
`O(B)`. Neighbor-read reverse is `UNDEFINED` because empty `R(A)` supplies
no pair. Reverse is UNDEFINED.

Reverse is UNDEFINED.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `R(C)` and `d` in `R(D)` with
`c+d=(0,0,0)`. `R(C)` is empty and `R(D)={−e_2}`, so face is `UNDEFINED`.

Face: UNDEFINED

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `hold` and not `fail`. Face is UNDEFINED. Unique-L leftover of
`M` reports face `UNDEFINED` from mixed `D`. #7208 `M` leftover reports face
hold from `+e_2` in `M(C)` against `−e_2` in `M(D)`. Own outgoing leftover
reports face hold from `±e_1` in `O(C)` and `O(D)`. Neighbor-read face is
`UNDEFINED` because empty `R(C)` supplies no pair. Named-sign lettering lost
the axis. Face is UNDEFINED.

Face is UNDEFINED.

## What this note does not claim

- It does not select a unique neighbor-read lock.
- It does not uniquely recover `M(A)` from the six-NN star excluding `A`.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the neighbor-read to be a singleton.
- It does not sum the neighbor-read.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  lock vectors.
- It does not reprint unique-L letters on these y-probes as the object.
- It does not reprint #7208 `M` as the letter.
- It does not reprint own outgoing `O` as the letter.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not enlarge the host beyond `B_3(0)`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.
- It is not the sister kernel.

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
opposite-lock two-site process, the neighbor-reads of own incoming, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nsopp #7093 seed `+e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| own incoming sets `M(A)`, `M(B)`, `M(C)`, `M(D)` of #7208 | Theorem 1; `{−e_1}`, `{+e_1}`, `{+e_2}`, `{−e_2, +e_3, −e_3}` |
| neighbor-reads `R(A)`, `R(B)`, `R(C)`, `R(D)` | Theorem 1; `{}`, `{−e_3}`, `{}`, `{−e_2}` |
| equality `R=M` at each probe | Theorem 1; Read-fail at each |
| six-NN star excluding `A` uniquely recovers `M(A)` | no; uniqueness is not required |
| reverse and face from `R` | Theorems 2–3; `UNDEFINED` / `UNDEFINED` |
| unique neighbor-read lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed stays a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique-L | not this display |
| leftover of #7208 `M` exist-opposite | not this display |
| leftover of own outgoing `O` | not this display |
| sister kernel | not this display |
| six-neighbor star as the letter | not used |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of own incoming on the four #7208 y-probes, equality to `M`, reverse/face from `R` or `UNDEFINED`. |
| V2 | Current main has no landed neighbor-read of own incoming reverse/face report on these four #7208 y-probes. |
| V3 | Neighbor-reads, Read-fail, and the `UNDEFINED`/`UNDEFINED` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads neighbor incoming whose step is from the probe and scores equality to `M` plus existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique-L,
does not reprint #7208 `M` as the letter, does not reprint outgoing `O`, does
not use a six-neighbor star, does not uniquely recover `M(A)`, and does not
use occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique-L leftover | require a singleton `{v}` subset `{±e_i}` else `UNDEFINED` | refused; leftover; unique-L of `M` HOLDs reverse while unique-L of empty `R(A)` is `UNDEFINED` |
| #7208 `M` exist-opposite | reuse the own incoming set as the letter | refused; leftover; that readout HOLDs reverse from `−e_1` in `M(A)` against `+e_1` in `M(B)` while neighbor-read reverse is `UNDEFINED` |
| own outgoing `O` exist-opposite | reuse `e in M(q+e)` as the letter | refused; leftover; `O` HOLDs reverse and face while `R` is not `O` and reverse/face from `R` are `UNDEFINED` |
| six-NN star excluding `A` as a unique kernel for `M(A)` | demand unique recovery of `M(A)` | refused; the star does not uniquely recover `M(A)`; uniqueness is not required; this is not the sister kernel |
| sum of the same neighbor-reads | replace `R` by the `Z^3` sum | refused; leftover; the construction does not sum; empty `R(A)` sums to `0` while the letter is the set |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `M` and `R` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique neighbor-read lock required | demand one neighbor-read step per probe | uniqueness is not required; empty `R` stays empty and mixed `M` stays a set |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, neighbor-read of own incoming, mixed stays a set,
existential opposite, four y-probes with seed `A`, Read-fail when `R≠M`, and
reverse/face as existence of a pair that sums to zero are declared. No
uniqueness of neighbor-read locks, no occupancy `n`, no named-sign
reduction, no singleton leftover as the object, no sum leftover, no unique-L
leftover, no #7208 `M` leftover, no outgoing leftover, no six-neighbor star
as the letter, no sister kernel, no global later T, no formation attachment
from already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`UNDEFINED`/`UNDEFINED` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in a neighbor-read of own incoming | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four neighbor-reads, equality to `M`, and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Neighbor-read of own incoming is leftover of unique-L or of
#7208 `M` because reverse already HOLDs from singleton `M(A)={−e_1}`, or it
is leftover of outgoing `O` because both read neighbors, or the six-NN star
excluding `A` uniquely recovers `M(A)`, or empty `R` should be `UNDEFINED`,
or occupancy `n` should track that vector.

**Answer:** The named construction reports neighbor-reads `{}`, `{−e_3}`,
`{}`, `{−e_2}` at `A,B,C,D`. Empty `R` is empty. Mixed stays a set. The
construction does not sum. Occupancy `n` is not used. Named signs lost the
axis. Equality `R=M` is Read-fail at each probe. The six-NN star excluding
`A` does not uniquely recover `M(A)`. Reverse is UNDEFINED because `R(A)` is
empty. Face is UNDEFINED because `R(C)` is empty. Unique-L leftover of `M`
reports reverse hold. #7208 `M` leftover reports reverse hold and face hold.
Outgoing leftover reports reverse hold and face hold from sets that are not
`R`. R is not M. R is not O. This is not the sister kernel. Uniqueness is
not required. The bits remain displayed.

### N8 — cross-cycle echo

A unique-L display on these same #7208 y-probes would assign
`L(A)=−e_1`, `L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` and report reverse
hold with face `UNDEFINED`. A #7208 own incoming display reports
`M(A) = {−e_1}` with reverse hold and face hold. An own outgoing display
reports `O(A) = {+e_2, +e_3, −e_3}` with reverse hold and face hold. Unique
lock-vector lettering of the neighbor-reads would report reverse `UNDEFINED`
and face `UNDEFINED` because `R(A)` and `R(C)` are empty. A sum leftover of
the same lists would replace empty `R(A)` by `0`. This note is not those
displays: mixed stays a set, the construction does not sum, the letter is
the neighbor-read of own incoming, R is not M, R is not O, reverse is
`UNDEFINED`, and face is `UNDEFINED`.

**Gate disposition:** PASS for the neighbor-read reverse/face reports above.
FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the predicate
equals the unique singleton lock vector,” “the predicate equals the sum of
the lock set,” “bits are Admissibility,” “the letter is occupancy `n`,”
“the sets equal unique-L leftover,” “the sets equal #7208 `M` leftover,”
“the sets equal outgoing leftover,” “R equals M,” “the six-NN star excluding
`A` uniquely recovers `M(A)`,” “reverse holds,” or “face holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsopp #7093 perp-step
incoming-lock process, reads each probe's neighbor-read of own incoming,
scores equality of `R` to `M`, scores reverse and face by existential
opposite, reports that the six-NN star excluding `A` does not uniquely
recover `M(A)`, and checks Theorems 1--3. It also checks that the
construction is not named-sign lettering, that mixed stays a set, that the
construction does not sum, that occupancy `n` is not used, that a formation
member from already-recorded six-neighbor locks is not attached, that the
sets are not leftover of unique-L, that the sets are not leftover of #7208
`M`, and that the sets are not leftover of outgoing `O`. No runner cache is
written.
