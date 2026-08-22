---
claim_id: y_symmetric_three_site_own_outgoing_set_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from the own outgoing *set* on the four #7211 y-probes are reported. No S⁺. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/y_symmetric_three_site_own_outgoing_set_existential_opposite_reverse_face_2026_08_15.py
---

# Own Outgoing Set Existential Opposite Reverse And Face On Four #7211 Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from the probe's own outgoing *set* `O(q)` on the
four nmsyop #7211 y-probes in `B_3(0)={n:n·n<=9}`. Same process as nsyopp
#7132. Let `t(q)` be the formation tick of probe `q`. `M(q)` is the set of
earliest incoming nearest-neighbor steps at `q`. Seeds use their seed letter
as a singleton. Mixed stays a set. Unformed is `UNDEFINED`. `O(q)` is the
outgoing dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e`
is formed in `B_3(0)` and `e` is in `M(q+e)`. Unformed `q` is `UNDEFINED`.
Empty `O` is empty, not `UNDEFINED`. Reverse holds if and only if some lock
in `O(A)` is the vector opposite of some lock in `O(B)`. Face holds if and
only if some lock in `O(C)` is the vector opposite of some lock in `O(D)`.
Empty or `UNDEFINED` on either side of a comparison is `UNDEFINED`; nonempty
with no opposite pair fails. Unique `L` is not the object. The six-neighbor
star `S^+` is not the letter. Occupancy `n` is not used. This is not
named-sign lettering. This is not a unique lock-vector leftover and not a
sum leftover. This is not leftover of unique-L, which is `UNDEFINED` when
mixed. This is not leftover of #7211 `M` exist-opposite, which HOLDs reverse
from singleton `M(A)={−e_1}` against `M(B)={+e_1}`. Reverse HOLD of #7211
does not use an incoming letter that is also outgoing. O is not M. The own
outgoing set does not use a six-neighbor star. Uniqueness of outgoing locks
is not required. Displayed, not adopted. Do not write into Admissibility.
Do not attach L1. This note does not write existential opposite into
Admissibility and does not attach a formation member from already-recorded
six-neighbor locks. This display does not use occupancy. Mixed stays a set.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/y_symmetric_three_site_own_outgoing_set_existential_opposite_reverse_face_2026_08_15.py`](../scripts/y_symmetric_three_site_own_outgoing_set_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets. Reverse and face are
scored on existence of an opposite pair in the own outgoing sets. Named signs
`{+,−}` are a coarser readout and are not used. A singleton unique lock-vector
letter is a different readout and is not used as the object: report `O`.
A `Z^3` sum of those locks is a different readout and is not used. The
construction does not sum. No S⁺. O is not M.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of O(q) as the probe's own outgoing dual of M on the four #7211 y-probes, mixed stays a set, with reverse hold and face hold from existential opposite; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: y_symmetric_three_site_own_outgoing_set_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from the own outgoing set on the four #7211 y-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with unique-L leftover, and do not identify the sets with #7211 M leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of the own outgoing set on the four #7211 y-probes; displayed, not adopted"
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
outgoing sets are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed. Same process and y-probes as nmsyop #7211.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (0,1,0), (0,-1,0)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,1,0)=−e_1`, and `L(0,-1,0)=−e_1`. The
third site is the y-mirror of the two-site opposite-lock partner `(0,1,0)`.
This seed is not the two-site opposite-lock seed `{0,(0,1,0)}` and not the
three-site opposite-lock seed whose third site is `(1,0,0)` with lock `+e_2`.
This seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
z-symmetric three-site seed `{0,(0,0,1),(0,0,-1)}`.

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

## Named existential opposite from the own outgoing set

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `M(q)` be the set of earliest incoming nearest-neighbor steps
at `q`. Seeds use their seed letter as a singleton. Mixed stays a set.
Unformed is `UNDEFINED`. Let `O(q)` be the outgoing dual of `M`:

```text
O(q) = { e in {±e_1,±e_2,±e_3} | q+e is formed in B_3(0) and e is in M(q+e) }.
```

Unformed `q` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Unique
`L(q)` is not used as the letter. This display does not use a six-neighbor
star. Occupancy `n` is not used. Duplicate outgoing steps collapse in the
set. The construction does not require `O(q)` to be a singleton. It does not
sum `O(q)`. It is not a unique lock-vector leftover and not a sum leftover.
It is not leftover of unique-L. It is not leftover of #7211 own incoming
`M`. O is not M.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not scored on `{+,−}`
names and are not an occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  some a in O(A) and some b in O(B) with a+b=(0,0,0)
face     <=>  some c in O(C) and some d in O(D) with c+d=(0,0,0)
```

If `O(A)` or `O(B)` is empty or `UNDEFINED`, reverse is `UNDEFINED`. Else
reverse fails if no such pair exists. If `O(C)` or `O(D)` is empty or
`UNDEFINED`, face is `UNDEFINED`. Else face fails if no such pair exists.
The report is one of `hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — formation ticks, M, and O at each y-probe

Direct enumeration of the displayed nsyopp #7132 process on `B_3(0)` forms
all four y-probes. The formation ticks are `t(A)=0`, `t(B)=2`, `t(C)=1`,
`t(D)=3`. `A` is a seed. Those ticks locate the earliest incoming set and
the outgoing dual. They are not occupancy kernels and are not a global
later T.

Own incoming sets of #7211 and own outgoing duals at each probe's own
formation tick are:

```text
A: seed letter −e_1;
   t(A)=0;  M(A) = {−e_1};  O(A) = {+e_2, +e_3, −e_3}
B: incoming +e_1;
   t(B)=2;  M(B) = {+e_1};  O(B) = {+e_2, +e_3, −e_3}
C: incoming +e_2;
   t(C)=1;  M(C) = {+e_2};  O(C) = {+e_1, −e_1, +e_3, −e_3}
D: incoming −e_2, −e_3, +e_3;
   t(D)=3;  M(D) = {−e_2, +e_3, −e_3};  O(D) = {+e_1, −e_1}
```

`A` is a seed at tick 0. Mixed stays a set: `O(A)` has three outgoing steps
`+e_2`, `+e_3`, and `−e_3`, and `O(D)` has two outgoing steps `+e_1` and
`−e_1`, so both are multi-element sets, not `UNDEFINED`. Unique-L leftover
of `O` would assign `UNDEFINED` at all four probes from that mix and would
leave reverse and face `UNDEFINED`. Here uniqueness is not required and
mixed stays a set.

Compare O to M of #7211. Same process reports `L(A) = −e_1` as the unique
incoming letter at the seed, with

```text
M(A) = {−e_1},  M(B) = {+e_1},  M(C) = {+e_2},  M(D) = {−e_2, +e_3, −e_3}
```

and Reverse HOLD of #7211 uses `−e_1` in `M(A)` against `+e_1` in `M(B)`.
Those incoming letters are absent from `O(A)` and `O(B)`.
Reverse HOLD of #7211 does not use an incoming letter that is also outgoing.
O is not M.
`M` and `O` are disjoint at each of the four probes. No S⁺.

Outgoing locks exist and need not be unique (`A` has three earliest outgoing
steps `+e_2`, `+e_3`, and `−e_3`). That non-uniqueness does not empty
`O(A)`. Uniqueness is not required.

The two-site opposite-lock leftover reports the same four own outgoing sets
on these y-probes, but its seed omits the y-mirror, so `(0,-1,0)` forms at
tick 1 rather than tick 0 and its leftover `S^+(D)` gains an extra `+e_2`.
The three-site leftover whose third site is `(1,0,0)` with lock `+e_2` mixes
`O(B)` by `+e_1` and replaces `O(D)` by `{−e_1}`. Those are different seeds.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `O(A)` and `b` in `O(B)`
with `a+b=(0,0,0)`. Both sets are nonempty: `O(A)={+e_2, +e_3, −e_3}` and
`O(B)={+e_2, +e_3, −e_3}`, so `+e_3+(−e_3)=(0,0,0)`. Reverse holds.

Reverse: hold

This is not `fail` and not `UNDEFINED`. Reverse holds. Unique-L leftover of
`O` reports reverse `UNDEFINED` because every outgoing set is mixed. Unique-L
leftover of `M` reports reverse hold from unique `L(A)=−e_1` and
`L(B)=+e_1`, but that leftover already left face `UNDEFINED` at mixed `D`.
#7211 `M` leftover reports reverse hold from `−e_1` in `M(A)` against
`+e_1` in `M(B)`. Reverse HOLD of #7211 does not use an incoming letter that
is also outgoing. Reverse holds because a pair from `O(A)` and `O(B)` is
opposite.

Reverse holds.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `O(C)` and `d` in `O(D)` with
`c+d=(0,0,0)`. Both sets are nonempty: `O(C)={+e_1, −e_1, +e_3, −e_3}` and
`O(D)={+e_1, −e_1}`, so `+e_1+(−e_1)=(0,0,0)`. Face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Face holds. Unique-L leftover of
`O` reports face `UNDEFINED` from mixed outgoing sets. Unique-L leftover of
`M` reports face `UNDEFINED` from mixed `D`. #7211 `M` leftover reports face
hold from `+e_2` in `M(C)` against `−e_2` in `M(D)`. Hold of face from the
own outgoing set is a different pair, `±e_1`, and is not leftover of that
incoming HOLD. Named-sign lettering lost the axis in mixed `{+,−}` at `A`
and at `D`. Face already holds at each probe's own formation tick from the
own outgoing set.

Face holds.

## What this note does not claim

- It does not select a unique outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the own outgoing set to be a singleton.
- It does not sum the own outgoing set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  lock vectors.
- It does not reprint unique-L letters on these y-probes as the object.
- It does not reprint #7211 `M` as the letter.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
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
y-symmetric three-site process, the own outgoing sets, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nsyopp #7132 seed `+e_1/−e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| own incoming sets `M(A)`, `M(B)`, `M(C)`, `M(D)` of #7211 | Theorem 1; `{−e_1}`, `{+e_1}`, `{+e_2}`, `{−e_2, +e_3, −e_3}` |
| own outgoing sets `O(A)`, `O(B)`, `O(C)`, `O(D)` | Theorem 1; `{+e_2, +e_3, −e_3}`, `{+e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_3, −e_3}`, `{+e_1, −e_1}` |
| compare O to M of #7211 | Theorem 1; disjoint at each probe; O is not M |
| reverse HOLD of #7211 uses an incoming letter that is also outgoing | Theorem 1; no |
| reverse and face | Theorems 2–3; `hold` / `hold` |
| unique outgoing lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed stays a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique-L | not this display |
| leftover of #7211 `M` exist-opposite | not this display |
| six-neighbor star as the letter | not used |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: own outgoing set on the four #7211 y-probes, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed own-outgoing-set existential-opposite reverse/face report on these four #7211 y-probes. |
| V3 | Own outgoing sets and the `hold`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the probe's own outgoing dual of `M` and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique-L,
does not reprint #7211 `M` as the letter, does not use a six-neighbor
star, and does not use occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique-L leftover | require a singleton `{v}` subset `{±e_i}` else `UNDEFINED` | refused; leftover; reverse and face of `O` would be `UNDEFINED` when mixed while the own outgoing sets are nonempty and reverse and face hold |
| #7211 `M` exist-opposite | reuse the own incoming set as the letter | refused; leftover; that readout HOLDs reverse from `−e_1` in `M(A)` against `+e_1` in `M(B)`, and Reverse HOLD of #7211 does not use an incoming letter that is also outgoing |
| sum of the same outgoing sets | replace `O` by the `Z^3` sum | refused; leftover; the construction does not sum; sum of mixed `O(A)` cancels to `+e_2` while `O(A)` stays a three-element set |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `M` and `O` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique outgoing lock required | demand one outgoing step per probe | uniqueness is not required; all three earliest outgoing steps at `A` are kept and mixed stays a set |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, y-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, own outgoing dual of the
earliest nearest-neighbor incoming sets, mixed stays a set, existential
opposite, four y-probes with seed `A`, and reverse/face as existence of a pair
that sums to zero are declared. No uniqueness of outgoing locks, no occupancy
`n`, no named-sign reduction, no singleton leftover as the object, no sum
leftover, no unique-L leftover, no #7211 `M` leftover, no six-neighbor star as
the letter, no global later T, no formation attachment from already-recorded
six-neighbor locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in an own outgoing set | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four outgoing sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** The own outgoing set is leftover of unique-L because reverse
already HOLDs from #7211 singleton `M(A)={−e_1}`, the sets should be replaced
by their sums, #7211 `M` already answered exist-opposite with HOLD, named
signs should suffice because they keep orientation, and occupancy `n` should
track that vector.

**Answer:** The named construction reports outgoing sets `{+e_2, +e_3, −e_3}`,
`{+e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_3, −e_3}`, `{+e_1, −e_1}` at `A,B,C,D`
from the probe's own outgoing dual of `M`. Mixed stays a set. The construction
does not sum. Occupancy `n` is not used. Named signs lost the axis. The pair
from `O(A)` and `O(B)` is opposite, so reverse holds. Reverse HOLD of #7211
does not use an incoming letter that is also outgoing. The pair from `O(C)`
and `O(D)` is opposite, so face holds. Unique-L leftover of `O` reports reverse
`UNDEFINED` and face `UNDEFINED` from mixed outgoing sets. #7211 `M` leftover
reports reverse hold and face hold from incoming sets that are disjoint from
`O` at each probe. Hold from outgoing `±e_3` at reverse while incoming reverse
uses `±e_1` is a discriminator. The sets are not those leftovers. The bits
remain displayed. Outgoing-lock uniqueness is not required. O is not M.

### N8 — cross-cycle echo

A unique-L display on these same #7211 y-probes would assign
`L(A)=−e_1`, `L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` and report reverse
hold with face `UNDEFINED`. A #7211 own incoming display reports
`M(A) = {−e_1}` with reverse hold and face hold, and Reverse HOLD of #7211
uses an incoming letter that is not outgoing. Unique lock-vector lettering of
the outgoing sets would report reverse `UNDEFINED` and face `UNDEFINED`
because every probe mixes. A sum leftover of the same lists would replace
mixed `O(A)` by `+e_2` after cancelling `+e_3` and `−e_3`. The two-site
outgoing display on the omitted-mirror seed reports the same four outgoing
sets on these y-probes, but that seed is not nsyopp #7132. This note is not
those displays: mixed stays a set, the construction does not sum, the letter
is the own outgoing set, Reverse HOLD of #7211 does not use an incoming letter
that is also outgoing, reverse holds, and face holds.

**Gate disposition:** PASS for the own-outgoing-set existential-opposite
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals the sum of the lock set,” “bits are Admissibility,” “the
letter is occupancy `n`,” “the sets equal unique-L leftover,” “the sets
equal #7211 `M` leftover,” “reverse fails,” or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsyopp #7132 perp-step
incoming-lock process, reads each probe's own outgoing dual of the incoming
set of earliest nearest-neighbor steps, scores reverse and face by
existential opposite, reports whether reverse HOLD of #7211 uses an incoming
letter that is also outgoing, and checks Theorems 1--3. It also checks that
the construction is not named-sign lettering, that mixed stays a set, that
the construction does not sum, that occupancy `n` is not used, that a
formation member from already-recorded six-neighbor locks is not attached,
that the sets are not leftover of unique-L, and that the sets are not leftover
of #7211 `M`. No runner cache is written.
