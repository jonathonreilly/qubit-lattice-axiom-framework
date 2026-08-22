---
claim_id: opposite_lock_yprobe_own_outgoing_set_neighbor_read_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read R_O of own outgoing on the four #7208 y-probes, equality to O, and reverse/face from R_O are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_yprobe_own_outgoing_set_neighbor_read_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Own Outgoing Reverse And Face On Four #7208 Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read `R_O(q)` of own outgoing on the four nsmopp #7208
y-probes in `B_3(0)={n:n·n<=9}`, equality of `R_O` to `O`, and reverse/face
from `R_O`. Same process as nsopp #7093. Let `t(q)` be the formation tick of
probe `q`. `M(q)` is the set of earliest incoming nearest-neighbor steps at
`q`. Seeds use their seed letter as a singleton. Mixed stays a set. Unformed
is `UNDEFINED`. `O(q)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed in `B_3(0)` and `e` is in
`M(q+e)`. Unformed `q` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`.
For formed `q`, `Nbr(q)` is the set of 6-NN of `q` that are formed in
`B_3(0)` and are not `q`. `R_O(q)` is the neighbor-read of own outgoing:

```text
R_O(q) = { e in {±e_1,±e_2,±e_3} | q+e in Nbr(q) and (−e) in O(q+e) }.
```

Unformed `q` is `UNDEFINED`. Empty `R_O` is empty, not `UNDEFINED`. `R_O`
is not `O` and is not `R(M)`. Read-HOLD at `q` iff `R_O(q)=O(q)` as sets
(both defined, possibly mixed). Read-fail if both defined and unequal.
`UNDEFINED` if either is `UNDEFINED`. Reverse holds if and only if some lock
in `R_O(A)` is the vector opposite of some lock in `R_O(B)`. Face holds if
and only if some lock in `R_O(C)` is the vector opposite of some lock in
`R_O(D)`. Empty or `UNDEFINED` on either side of a comparison is
`UNDEFINED`; nonempty with no opposite pair fails. Unique `L` is not the
object. The six-neighbor star `S^+` is not the letter. Occupancy `n` is not
used. This is not named-sign lettering. This is not a unique lock-vector
leftover and not a sum leftover. This is not leftover of unique-L. This is
not leftover of #7208 `M` exist-opposite, which HOLDs reverse from singleton
`M(A)={−e_1}` against `M(B)={+e_1}`. This is not leftover of own outgoing
`O`, which HOLDs reverse from `±e_3` in `O(A)` and `O(B)`. This is not
leftover of neighbor-read `R(M)` of own incoming, which is `UNDEFINED` on
#7167 reverse/face from empty `R(A)` and empty `R(C)`. The letter is
neighbor-read of outgoing, not own outgoing. This is not leftover of #7167
`S^+`. The six-NN star excluding `q` does not recover `O(q)`. Uniqueness is
not required. This is not the sister kernel. This is not the sister #7210 kernel. Displayed, not adopted.
Do not write into Admissibility. Do not attach L1. This note does not write
existential opposite into Admissibility and does not attach a formation
member from already-recorded six-neighbor locks. This display does not use
occupancy. Mixed stays a set. No S⁺. Not Cl.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_yprobe_own_outgoing_set_neighbor_read_reverse_face_2026_08_15.py`](../scripts/opposite_lock_yprobe_own_outgoing_set_neighbor_read_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets. `R_O` is the
neighbor-read of those outgoing sets. Reverse and face are scored on
existence of an opposite pair in the neighbor-reads of outgoing. Named signs
`{+,−}` are a coarser readout and are not used. A singleton unique lock-vector
letter is a different readout and is not used as the object: report `R_O`.
A `Z^3` sum of those locks is a different readout and is not used. The
construction does not sum. No S⁺. R_O is not O. R_O is not R(M). R_O is not
M.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of R_O(q) as neighbor-read of own outgoing on the four #7208 y-probes, mixed stays a set, with equality R_O=O as Read-fail at each probe and reverse hold plus face hold from existential opposite; uniqueness of neighbor-read locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_yprobe_own_outgoing_set_neighbor_read_reverse_face
target_blocker_text: "display neighbor-read R_O of own outgoing on the four #7208 y-probes, equality to O, and reverse/face from R_O, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with unique-L leftover, do not identify the sets with #7208 M leftover, do not identify the sets with outgoing O leftover, and do not identify the sets with R(M) leftover."
conditional_surface_status: "exact on B_3(0) for neighbor-read of own outgoing on the four #7208 y-probes; displayed, not adopted"
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
neighbor-reads of outgoing are scored:

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

## Named neighbor-read of own outgoing

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `M(q)` be the set of earliest incoming nearest-neighbor steps
at `q`. Seeds use their seed letter as a singleton. Mixed stays a set.
Unformed is `UNDEFINED`. Let `O(q)` be the outgoing dual of `M`:

```text
O(q) = { e in {±e_1,±e_2,±e_3} | q+e is formed in B_3(0) and e is in M(q+e) }.
```

Unformed `q` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. For formed
`q`, `Nbr(q)` is the set of 6-NN of `q` that are formed in `B_3(0)` and are
not `q`. Let `R_O(q)` be the neighbor-read of own outgoing:

```text
R_O(q) = { e in {±e_1,±e_2,±e_3} | q+e in Nbr(q) and (−e) in O(q+e) }.
```

Unformed `q` is `UNDEFINED`. Empty `R_O` is empty, not `UNDEFINED`. Unique
`L(q)` is not used as the letter. This display does not use a six-neighbor
star as the letter. Occupancy `n` is not used. Duplicate neighbor-read steps
collapse in the set. The construction does not require `R_O(q)` to be a
singleton. It does not sum `R_O(q)`. It is not a unique lock-vector leftover
and not a sum leftover. It is not leftover of unique-L. It is not leftover
of #7208 own incoming `M`. It is not leftover of own outgoing `O`. It is not
leftover of neighbor-read `R(M)` of own incoming. R_O is not O. R_O is not
R(M). R_O is not M. The six-NN star excluding `q` does not recover `O(q)`.
Uniqueness is not required. This is not the sister #7210 kernel.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not scored on `{+,−}`
names and are not an occupancy-kernel inner product.

Read equality, reverse, and face (displayed):

```text
read(q)  <=>  R_O(q) = O(q) as sets, both defined
reverse  <=>  some a in R_O(A) and some b in R_O(B) with a+b=(0,0,0)
face     <=>  some c in R_O(C) and some d in R_O(D) with c+d=(0,0,0)
```

If `R_O(q)` or `O(q)` is `UNDEFINED`, read is `UNDEFINED`. Else Read-HOLD if
the sets are equal and Read-fail if they are unequal. If `R_O(A)` or
`R_O(B)` is empty or `UNDEFINED`, reverse is `UNDEFINED`. Else reverse fails
if no such pair exists. If `R_O(C)` or `R_O(D)` is empty or `UNDEFINED`,
face is `UNDEFINED`. Else face fails if no such pair exists. The report is
one of `hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — formation ticks, O, and R_O at each y-probe

Direct enumeration of the displayed nsopp #7093 process on `B_3(0)` forms
all four y-probes. The formation ticks are `t(A)=0`, `t(B)=2`, `t(C)=1`,
`t(D)=3`. `A` is a seed. Those ticks locate the earliest incoming set, the
outgoing dual, and the neighbor-read of outgoing. They are not occupancy
kernels and are not a global later T.

Own outgoing duals of #7167 and neighbor-reads of outgoing at each probe
are:

```text
A: seed letter −e_1;
   t(A)=0;  O(A) = {+e_2, +e_3, −e_3};  R_O(A) = {+e_1}
B: incoming +e_1;
   t(B)=2;  O(B) = {+e_2, +e_3, −e_3};  R_O(B) = {−e_1}
C: incoming +e_2;
   t(C)=1;  O(C) = {+e_1, −e_1, +e_3, −e_3};  R_O(C) = {−e_2}
D: incoming −e_2, −e_3, +e_3;
   t(D)=3;  O(D) = {+e_1, −e_1};  R_O(D) = {+e_2, +e_3, −e_3}
```

`A` is a seed at tick 0. Mixed stays a set: `R_O(D)` has three neighbor-read
steps `+e_2`, `+e_3`, and `−e_3`, and `O(A)` has three outgoing steps
`+e_2`, `+e_3`, and `−e_3`. Unique-L leftover of `R_O` would assign
`UNDEFINED` at mixed `D` and would leave face `UNDEFINED`. Uniqueness is not
required.

Equality `R_O=O` at each probe is Read-fail: both sides are defined and
unequal. The six-NN star excluding `q` does not recover `O(q)`. `Nbr(A)` has
six formed neighbors and omits `A`; `R_O(A)={+e_1}` while
`O(A)={+e_2, +e_3, −e_3}`.

Compare R_O to O, to M of #7208, and to R(M) of #7167. Same process reports

```text
M(A) = {−e_1},  M(B) = {+e_1},  M(C) = {+e_2},  M(D) = {−e_2, +e_3, −e_3}
O(A) = {+e_2, +e_3, −e_3},  O(B) = {+e_2, +e_3, −e_3},
O(C) = {+e_1, −e_1, +e_3, −e_3},  O(D) = {+e_1, −e_1}
R(A) = {},  R(B) = {−e_3},  R(C) = {},  R(D) = {−e_2}
```

and Reverse HOLD of #7208 uses `−e_1` in `M(A)` against `+e_1` in `M(B)`.
Own outgoing leftover uses `±e_3` in `O(A)` and `O(B)`. Neighbor-read
`R(M)` of own incoming is empty at `A` and at `C`. Those letters are not
the neighbor-read of outgoing. R_O is not O. R_O is not M. R_O is not R(M).
`M` and `O` are disjoint at each of the four probes. No S⁺. Not Cl.

Outgoing locks exist and need not be unique. Neighbor-read locks of outgoing
need not be unique (`D` has three steps). That non-uniqueness does not empty
`R_O(D)`. Uniqueness is not required.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `R_O(A)` and `b` in
`R_O(B)` with `a+b=(0,0,0)`. Both sets are nonempty: `R_O(A)={+e_1}` and
`R_O(B)={−e_1}`, so `+e_1+(−e_1)=(0,0,0)`. Reverse holds.

Reverse: hold

This is not `fail` and not `UNDEFINED`. Reverse holds. Unique-L leftover of
`O` reports reverse `UNDEFINED` because every outgoing set is mixed.
Unique-L leftover of `M` reports reverse hold from unique `L(A)=−e_1` and
`L(B)=+e_1`. #7208 `M` leftover reports reverse hold from `−e_1` in `M(A)`
against `+e_1` in `M(B)`. Own outgoing leftover reports reverse hold from
`±e_3` in `O(A)` and `O(B)`. Neighbor-read `R(M)` leftover reports reverse
`UNDEFINED` from empty `R(A)`. Reverse HOLD of neighbor-read of outgoing
uses `+e_1` in `R_O(A)` against `−e_1` in `R_O(B)`, which is not the
outgoing pair `±e_3` and is not leftover of the #7167 `R(M)` kill-gate.
Neighbor-read is not only an `M` kill-gate. Reverse holds.

Reverse holds.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `R_O(C)` and `d` in `R_O(D)`
with `c+d=(0,0,0)`. Both sets are nonempty: `R_O(C)={−e_2}` and
`R_O(D)={+e_2, +e_3, −e_3}`, so `−e_2+(+e_2)=(0,0,0)`. Face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Face holds. Unique-L leftover of
`R_O` reports face `UNDEFINED` from mixed `D`. Unique-L leftover of `O`
reports face `UNDEFINED` from mixed outgoing sets. Unique-L leftover of `M`
reports face `UNDEFINED` from mixed `D`. #7208 `M` leftover reports face
hold from `+e_2` in `M(C)` against `−e_2` in `M(D)`. Own outgoing leftover
reports face hold from `±e_1` in `O(C)` and `O(D)`. Neighbor-read `R(M)`
leftover reports face `UNDEFINED` from empty `R(C)`. Hold of face from the
neighbor-read of outgoing uses `±e_2` and is not leftover of the outgoing
`±e_1` HOLD. Named-sign lettering lost the axis. Face already holds at each
probe's own formation tick from the neighbor-read of outgoing.

Face holds.

## What this note does not claim

- It does not select a unique neighbor-read lock of outgoing.
- It does not recover `O(q)` from the six-NN star excluding `q`.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the neighbor-read of outgoing to be a singleton.
- It does not sum the neighbor-read of outgoing.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  lock vectors.
- It does not reprint unique-L letters on these y-probes as the object.
- It does not reprint #7208 `M` as the letter.
- It does not reprint own outgoing `O` as the letter.
- It does not reprint neighbor-read `R(M)` of own incoming as the letter.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not enlarge the host beyond `B_3(0)`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.
- It is not the sister kernel.
- It is not the sister #7210 kernel.
- It is not leftover of `R(M)`.
- It is not Cl.

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
opposite-lock two-site process, the neighbor-reads of own outgoing, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nsopp #7093 seed `+e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| own incoming sets `M(A)`, `M(B)`, `M(C)`, `M(D)` of #7208 | Theorem 1; `{−e_1}`, `{+e_1}`, `{+e_2}`, `{−e_2, +e_3, −e_3}` |
| own outgoing sets `O(A)`, `O(B)`, `O(C)`, `O(D)` of #7167 | Theorem 1; `{+e_2, +e_3, −e_3}`, `{+e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_3, −e_3}`, `{+e_1, −e_1}` |
| neighbor-reads `R_O(A)`, `R_O(B)`, `R_O(C)`, `R_O(D)` | Theorem 1; `{+e_1}`, `{−e_1}`, `{−e_2}`, `{+e_2, +e_3, −e_3}` |
| equality `R_O=O` at each probe | Theorem 1; Read-fail at each |
| six-NN star excluding `q` recovers `O(q)` | no; uniqueness is not required |
| reverse and face from `R_O` | Theorems 2–3; `hold` / `hold` |
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
| leftover of neighbor-read `R(M)` | not this display |
| leftover of `R(M)` | not this display |
| sister #7210 kernel | not this display |
| six-neighbor star as the letter | not used |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of own outgoing on the four #7208 y-probes, equality to `O`, reverse/face from `R_O` or `UNDEFINED`. |
| V2 | Current main has no landed neighbor-read of own outgoing reverse/face report on these four #7208 y-probes. |
| V3 | Neighbor-reads of outgoing, Read-fail, and the `hold`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads neighbor outgoing whose reverse step is from the probe and scores equality to `O` plus existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique-L,
does not reprint #7208 `M` as the letter, does not reprint outgoing `O`, does
not reprint neighbor-read `R(M)`, does not use a six-neighbor star, does not
recover `O(q)` from six-NN excluding `q`, and does not use occupancy `n`. No
global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique-L leftover | require a singleton `{v}` subset `{±e_i}` else `UNDEFINED` | refused; leftover; unique-L of mixed `R_O(D)` is `UNDEFINED` while face from `R_O` holds |
| #7208 `M` exist-opposite | reuse the own incoming set as the letter | refused; leftover; that readout HOLDs reverse from `−e_1` in `M(A)` against `+e_1` in `M(B)` while neighbor-read of outgoing uses `+e_1` in `R_O(A)` against `−e_1` in `R_O(B)` |
| own outgoing `O` exist-opposite | reuse `e in M(q+e)` as the letter | refused; leftover; `O` HOLDs reverse from `±e_3` while `R_O` HOLDs reverse from `±e_1`; Read-fail `R_O≠O` |
| neighbor-read `R(M)` of own incoming | reuse `(−e) in M(q+e)` as the letter | refused; leftover of `R(M)`; that readout is `UNDEFINED` reverse/face on #7167 from empty `R(A)` and empty `R(C)` while `R_O` HOLDs reverse and face |
| six-NN star excluding `q` as a unique kernel for `O(q)` | demand recovery of `O(q)` | refused; the star does not recover `O(q)`; uniqueness is not required; this is not the sister #7210 kernel |
| sum of the same neighbor-reads | replace `R_O` by the `Z^3` sum | refused; leftover; the construction does not sum; sum of mixed `R_O(D)` cancels to `+e_2` while `R_O(D)` stays a three-element set |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `O` and `R_O` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique neighbor-read lock required | demand one neighbor-read step per probe | uniqueness is not required; mixed `R_O(D)` stays a set |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, own outgoing dual, neighbor-read of own outgoing,
mixed stays a set, existential opposite, four y-probes with seed `A`,
Read-fail when `R_O≠O`, and reverse/face as existence of a pair that sums to
zero are declared. No uniqueness of neighbor-read locks, no occupancy `n`, no
named-sign reduction, no singleton leftover as the object, no sum leftover,
no unique-L leftover, no #7208 `M` leftover, no outgoing leftover, no `R(M)`
leftover, no six-neighbor star as the letter, no sister #7210 kernel, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in a neighbor-read of own outgoing | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four neighbor-reads, equality to `O`, and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Neighbor-read of own outgoing is leftover of unique-L or of
#7208 `M` because reverse already HOLDs from singleton `M(A)={−e_1}`, or it
is leftover of outgoing `O` because both HOLD reverse and face, or it is
leftover of neighbor-read `R(M)` because both read 6-NN excluding `q`, or
the six-NN star excluding `q` recovers `O(q)`, or mixed `R_O(D)` should be
`UNDEFINED`, or occupancy `n` should track that vector, or neighbor-read is
only an `M` kill-gate.

**Answer:** The named construction reports neighbor-reads of outgoing
`{+e_1}`, `{−e_1}`, `{−e_2}`, `{+e_2, +e_3, −e_3}` at `A,B,C,D`. Empty
`R_O` is empty. Mixed stays a set. The construction does not sum. Occupancy
`n` is not used. Named signs lost the axis. Equality `R_O=O` is Read-fail at
each probe. The six-NN star excluding `q` does not recover `O(q)`. Reverse
holds because `+e_1` in `R_O(A)` is opposite `−e_1` in `R_O(B)`. Face holds
because `−e_2` in `R_O(C)` is opposite `+e_2` in `R_O(D)`. Unique-L leftover
of `R_O` reports face `UNDEFINED` from mixed `D`. Unique-L leftover of `O`
reports reverse `UNDEFINED` and face `UNDEFINED`. #7208 `M` leftover reports
reverse hold from `−e_1` in `M(A)` against `+e_1` in `M(B)`. Outgoing
leftover reports reverse hold from `±e_3`, not from `±e_1`. Neighbor-read
`R(M)` leftover reports reverse `UNDEFINED` and face `UNDEFINED` on #7167.
Neighbor-read is not only an `M` kill-gate. R_O is not O. R_O is not M. R_O
is not R(M). This is not leftover of `R(M)`. This is not the sister kernel. This is not the sister #7210
kernel. Uniqueness is not required. The bits remain displayed.

### N8 — cross-cycle echo

A unique-L display on these same #7208 y-probes would assign
`L(A)=−e_1`, `L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` and report reverse
hold with face `UNDEFINED`. A #7208 own incoming display reports
`M(A) = {−e_1}` with reverse hold and face hold. An own outgoing display
reports `O(A) = {+e_2, +e_3, −e_3}` with reverse hold and face hold from
`±e_3` / `±e_1`. A neighbor-read `R(M)` display on #7167 reports empty
`R(A)` and empty `R(C)` with reverse `UNDEFINED` and face `UNDEFINED`. Unique
lock-vector lettering of the neighbor-reads of outgoing would report reverse
hold with face `UNDEFINED` because `R_O(D)` is mixed. A sum leftover of the
same lists would replace mixed `R_O(D)` by `+e_2` after cancelling `+e_3`
and `−e_3`. This note is not those displays: mixed stays a set, the
construction does not sum, the letter is the neighbor-read of own outgoing,
R_O is not O, R_O is not M, R_O is not R(M), reverse holds, and face holds.

**Gate disposition:** PASS for the neighbor-read of own outgoing reverse/face
reports above. FAIL / DO NOT SHIP for “the predicate equals the named sign,”
“the predicate equals the unique singleton lock vector,” “the predicate
equals the sum of the lock set,” “bits are Admissibility,” “the letter is
occupancy `n`,” “the sets equal unique-L leftover,” “the sets equal #7208
`M` leftover,” “the sets equal outgoing leftover,” “the sets equal `R(M)`
leftover,” “R_O equals O,” “the six-NN star excluding `q` recovers `O(q)`,”
“reverse fails,” or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsopp #7093 perp-step
incoming-lock process, reads each probe's neighbor-read of own outgoing,
scores equality of `R_O` to `O`, scores reverse and face by existential
opposite, reports that the six-NN star excluding `q` does not recover
`O(q)`, and checks Theorems 1--3. It also checks that the construction is
not named-sign lettering, that mixed stays a set, that the construction does
not sum, that occupancy `n` is not used, that a formation member from
already-recorded six-neighbor locks is not attached, that the sets are not
leftover of unique-L, that the sets are not leftover of #7208 `M`, that the
sets are not leftover of outgoing `O`, and that the sets are not leftover of
neighbor-read `R(M)`. No runner cache is written.
