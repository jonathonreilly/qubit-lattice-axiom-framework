---
claim_id: y_symmetric_three_site_simultaneous_incoming_outgoing_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Simultaneous M and O at t+1 on the four #7211 y-probes, intersection, and reverse/face of each are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/y_symmetric_three_site_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py
---

# Simultaneous Incoming And Outgoing At t+1 Reverse And Face On Four #7211 Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** simultaneous own incoming set `M(q,τ)` and own outgoing set
`O(q,τ)` at `τ=t+1` on the four nmsyop #7211 y-probes in
`B_3(0)={n:n·n<=9}`. Same process as nsyopp #7132. Same process and
y-probes as nmsyop #7211. Let `t(q)` be the formation tick of probe `q`.
`τ=t(q)+1` is that probe's own next tick, not a global later T. `M(q,τ)`
is the set of earliest incoming nearest-neighbor steps at `q` from records
with tick `≤ τ`. Seeds use their seed letter as a singleton. Mixed stays a
set. Unformed at `τ` is `UNDEFINED`. `O(q,τ)` is the outgoing dual of timed
`M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and
`e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is empty,
not `UNDEFINED`. Reverse of `M` at `τ` holds if and only if some lock in
`M(A,τ)` is the vector opposite of some lock in `M(B,τ)`. Face of `M` at
`τ` holds if and only if some lock in `M(C,τ)` is the vector opposite of
some lock in `M(D,τ)`. Reverse of `O` at `τ` and face of `O` at `τ` are
the same predicate on the outgoing sets. Empty or `UNDEFINED` on either
side of a comparison is `UNDEFINED`; nonempty with no opposite pair fails.
Unique `L` is not the object. The six-neighbor star `S^+` is not the
letter. Occupancy `n` is not used. This is not named-sign lettering. This
is not a unique lock-vector leftover and not a sum leftover. This is not
leftover of unique-L, which is `UNDEFINED` when mixed. This is not leftover
of #7211 `M` exist-opposite at formation, which HOLDs reverse from
singleton `M(A)={−e_1}` against `M(B)={+e_1}` and does not report `O`.
This is not leftover of untimed `O`. This is not leftover of M two-tick
composition. This is not leftover of the two-site nmsimopp seed. No S⁺.
Uniqueness of incoming or outgoing locks is not required. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1. This note does
not write existential opposite into Admissibility and does not attach a
formation member from already-recorded six-neighbor locks. This display
does not use occupancy. Mixed stays a set.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/y_symmetric_three_site_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py`](../scripts/y_symmetric_three_site_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of timed incoming sets. Reverse and face of
each are scored on existence of an opposite pair. Named signs `{+,−}` are a
coarser readout and are not used. A singleton unique lock-vector letter is a
different readout and is not used as the object: report `M` and `O` together
at `τ=t+1`. A `Z^3` sum of those locks is a different readout and is not
used. The construction does not sum. No S⁺.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of simultaneous M(q,τ) and O(q,τ) at τ=t+1 on the four #7211 y-probes, empty intersection, reverse hold and face hold from M, reverse hold and face hold from O; uniqueness of incoming or outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: y_symmetric_three_site_simultaneous_incoming_outgoing_tplus1_reverse_face
target_blocker_text: "display simultaneous M and O at t+1 on the four #7211 y-probes, intersection, and reverse/face of each, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face of M and of O displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the timed pair with unique-L leftover, do not identify the timed pair with #7211 M leftover, and do not identify the timed pair with untimed O leftover."
conditional_surface_status: "exact on B_3(0) for simultaneous M and O at t+1 on the four #7211 y-probes; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose timed
incoming and outgoing sets are scored:

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

## Named existential opposite from timed incoming and timed outgoing

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `τ=t(q)+1`. No global later T is used. Let `M(q,τ)` be the set
of earliest incoming nearest-neighbor steps at `q` from records with tick
`≤ τ`. Seeds use their seed letter as a singleton. Mixed stays a set.
Unformed at `τ` is `UNDEFINED`. Let `O(q,τ)` be the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Unique
`L(q)` is not used as the letter. This display does not use a six-neighbor
star. Occupancy `n` is not used. Duplicate incoming or outgoing steps
collapse in the set. The construction does not require `M(q,τ)` or `O(q,τ)`
to be a singleton. It does not sum either set. It is not a unique
lock-vector leftover and not a sum leftover. It is not leftover of unique-L.
It is not leftover of #7211 own incoming `M` at formation. It is not leftover
of untimed `O`. It is not leftover of M two-tick.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not scored on `{+,−}`
names and are not an occupancy-kernel inner product.

Reverse and face of `M` at `τ` (displayed):

```text
reverse of M  <=>  some a in M(A,τ) and some b in M(B,τ) with a+b=(0,0,0)
face of M     <=>  some c in M(C,τ) and some d in M(D,τ) with c+d=(0,0,0)
```

Reverse and face of `O` at `τ` (displayed, not adopted):

```text
reverse of O  <=>  some a in O(A,τ) and some b in O(B,τ) with a+b=(0,0,0)
face of O     <=>  some c in O(C,τ) and some d in O(D,τ) with c+d=(0,0,0)
```

If either side is empty or `UNDEFINED`, the comparison is `UNDEFINED`. Else
it fails if no such pair exists. The report is one of `hold`, `fail`, or
`UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — t, M, O, and intersection at τ=t+1

Direct enumeration of the displayed nsyopp #7132 process on `B_3(0)` forms
all four y-probes. The formation ticks are `t(A)=0`, `t(B)=2`, `t(C)=1`,
`t(D)=3`. `A` is a seed. Those ticks locate `τ=t+1`. They are not occupancy
kernels and are not a global later T.

Own incoming sets, own outgoing duals, and their intersections at each
probe's own `τ=t+1` are:

```text
A: seed letter −e_1;
   t(A)=0;  τ=1;
   M(A,τ) = {−e_1};  O(A,τ) = {+e_2, +e_3, −e_3};
   M(A,τ)∩O(A,τ) = {}
B: incoming +e_1;
   t(B)=2;  τ=3;
   M(B,τ) = {+e_1};  O(B,τ) = {+e_2, +e_3, −e_3};
   M(B,τ)∩O(B,τ) = {}
C: incoming +e_2;
   t(C)=1;  τ=2;
   M(C,τ) = {+e_2};  O(C,τ) = {+e_1, −e_1, +e_3, −e_3};
   M(C,τ)∩O(C,τ) = {}
D: incoming −e_2, −e_3, +e_3;
   t(D)=3;  τ=4;
   M(D,τ) = {−e_2, +e_3, −e_3};  O(D,τ) = {+e_1, −e_1};
   M(D,τ)∩O(D,τ) = {}
```

`A` is a seed at tick 0. Mixed stays a set: `M(D,τ)` has three earliest
incoming steps `−e_2`, `−e_3`, and `+e_3`, and `O(A,τ)` has three outgoing
steps, so both are multi-element sets, not `UNDEFINED`. Unique-L leftover
of mixed `O` would assign `UNDEFINED` at `A`, `B`, `C`, and `D` and would
leave reverse and face of `O` `UNDEFINED`. Here uniqueness is not required
and mixed stays a set.

`M(q,τ)` at `τ=t+1` equals the #7211 own incoming set at formation: `M` is
frozen between `t` and `t+1`. `O(q,τ)` at `A`, `B`, and `C` is empty at `t`
and nonempty at `t+1`. Intersection `M(q,τ)∩O(q,τ)` is empty at each of
A, B, C, D. HOLDING M of #7211 and timed outgoing at `t+1` are disjoint.
Reverse HOLD of #7211 uses incoming `−e_1` at `A`, which is not outgoing at
`τ`. No S⁺.

The two-site opposite-lock leftover reports the same four timed `M` and `O`
on these y-probes at `t+1`, but its seed omits the y-mirror, so `(0,-1,0)`
forms at tick 1 rather than tick 0. The three-site leftover whose third site
is `(1,0,0)` with lock `+e_2` mixes `M(B,τ)` by `+e_2`, adds `−e_1` to
`M(D,τ)`, and makes `M∩O` nonempty at `B` and at `D`. Those are different
seeds.

Incoming and outgoing locks exist and need not be unique. That
non-uniqueness does not empty `M` or `O`. Uniqueness is not required.

## Theorem 2 — reverse/face from M at τ

Reverse of `M` at `τ` holds if and only if there exist `a` in `M(A,τ)` and
`b` in `M(B,τ)` with `a+b=(0,0,0)`. Both sets are nonempty:
`M(A,τ)={−e_1}` and `M(B,τ)={+e_1}`, so `−e_1+(+e_1)=(0,0,0)`. Reverse of
`M` holds. Reverse HOLD uses a singleton `M(A,τ)`.

Reverse of M: hold

Face of `M` at `τ` holds if and only if there exist `c` in `M(C,τ)` and
`d` in `M(D,τ)` with `c+d=(0,0,0)`. Both sets are nonempty:
`M(C,τ)={+e_2}` and `M(D,τ)={−e_2, +e_3, −e_3}`, so `+e_2+(−e_2)=(0,0,0)`.
Face of `M` holds.

Face of M: hold

This is not `fail` and not `UNDEFINED`. Reverse of M holds. Face of M holds.
Unique-L leftover of `M` reports reverse hold from unique `L(A)=−e_1` and
`L(B)=+e_1`, but that leftover already left face `UNDEFINED` at mixed `D`.
#7211 `M` leftover reports the same reverse hold and face hold at formation;
that leftover does not report `O` and does not report the empty intersection
at `t+1`. Reverse of M holds because the pair from `M(A,τ)` and `M(B,τ)` is
opposite.

Reverse of M holds. Face of M holds.

## Theorem 3 — reverse/face from O at τ

Reverse of `O` at `τ` holds if and only if there exist `a` in `O(A,τ)` and
`b` in `O(B,τ)` with `a+b=(0,0,0)`. Both sets are nonempty:
`O(A,τ)={+e_2, +e_3, −e_3}` and `O(B,τ)={+e_2, +e_3, −e_3}`, so
`+e_3+(−e_3)=(0,0,0)`. Reverse of `O` holds from outgoing `±e_3`.

Reverse of O: hold

Face of `O` at `τ` holds if and only if there exist `c` in `O(C,τ)` and
`d` in `O(D,τ)` with `c+d=(0,0,0)`. Both sets are nonempty:
`O(C,τ)={+e_1, −e_1, +e_3, −e_3}` and `O(D,τ)={+e_1, −e_1}`, so
`+e_1+(−e_1)=(0,0,0)`. Face of `O` holds from outgoing `±e_1`.

Face of O: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Reverse of O holds. Face of O holds.
Unique-L leftover of `O` reports reverse `UNDEFINED` and face `UNDEFINED`
because every outgoing set at `τ` is mixed. Untimed `O` leftover reports the
same reverse hold and face hold without pairing them to timed `M` at `t+1`.
Hold of reverse and face from `O` at `τ` is displayed, not adopted. Named-sign
lettering lost the axis in mixed `{+,−}` at `A` and at `D`. Reverse of O at
`t` is `UNDEFINED` at empty `O(A,t)`. Simultaneous HOLD of reverse and face
from `M` and from `O` is the `t+1` report.

Reverse of O holds. Face of O holds.

## What this note does not claim

- It does not select a unique incoming or outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require timed `M` or timed `O` to be a singleton.
- It does not sum timed `M` or timed `O`.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  lock vectors.
- It does not reprint unique-L letters on these y-probes as the object.
- It does not reprint #7211 `M` at formation as the whole display.
- It does not reprint untimed `O` as the whole display.
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
y-symmetric three-site process, the timed incoming and outgoing sets at
`τ=t+1`, and the existential-opposite reverse/face predicates are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nsyopp #7132 seed `+e_1/−e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| timed incoming `M(A,τ)`, `M(B,τ)`, `M(C,τ)`, `M(D,τ)` | Theorem 1; `{−e_1}`, `{+e_1}`, `{+e_2}`, `{−e_2, +e_3, −e_3}` |
| timed outgoing `O(A,τ)`, `O(B,τ)`, `O(C,τ)`, `O(D,τ)` | Theorem 1; `{+e_2, +e_3, −e_3}`, `{+e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_3, −e_3}`, `{+e_1, −e_1}` |
| intersection `M∩O` at `τ` | Theorem 1; empty at A, B, C, D |
| reverse and face from `M` at `τ` | Theorem 2; `hold` / `hold` |
| reverse and face from `O` at `τ` | Theorem 3; `hold` / `hold`; displayed, not adopted |
| unique incoming or outgoing lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed stays a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique-L | not this display |
| leftover of #7211 `M` at formation | not this display |
| leftover of untimed `O` | not this display |
| leftover of M two-tick | not this display |
| six-neighbor star as the letter | not used |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: simultaneous `M` and `O` at `t+1` on the four #7211 y-probes, intersection, reverse/face of each or `UNDEFINED`. |
| V2 | Current main has no landed simultaneous `M`/`O` at `t+1` reverse/face report on these four #7211 y-probes. |
| V3 | Timed incoming sets, timed outgoing sets, empty intersection, and the `hold`/`hold` reports of each are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads timed incoming and timed outgoing at `τ=t+1` and scores existence of an opposite pair in each. |
| V5 | It is not an adopted content rule: reverse/face of `O` remain displayed, not adopted. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique-L,
does not reprint #7211 `M` as the whole display, does not reprint untimed `O`
as the whole display, does not use a six-neighbor star, and does not use
occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique-L leftover | require a singleton `{v}` subset `{±e_i}` else `UNDEFINED` | refused; leftover; face of `M` would be `UNDEFINED` when mixed while `M(D,τ)` is nonempty and face of `M` holds; reverse of `O` would be `UNDEFINED` while `O` is nonempty and reverse of `O` holds |
| #7211 `M` exist-opposite | reuse formation incoming as the whole display | refused; leftover; that readout HOLDs reverse from `−e_1` in `M(A)` against `+e_1` in `M(B)` and does not report `O` or the empty intersection at `t+1` |
| untimed `O` exist-opposite | reuse formation-blind outgoing as the whole display | refused; leftover; that readout HOLDs reverse from outgoing `±e_3` without pairing to timed `M` at `t+1` |
| M two-tick composition | replace the simultaneous pair by `M(t)` versus `M(t+1)` | refused; leftover; `M` is frozen, so composition would HOLD and would omit `O` |
| sum of the same timed sets | replace `M` or `O` by the `Z^3` sum | refused; leftover; the construction does not sum; sum of mixed `M(D,τ)` cancels to `−e_2` while `M(D,τ)` stays a three-element set |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `τ=t+1` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; all three earliest incoming steps at `D` are kept and mixed stays a set |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, y-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, timed incoming set of
earliest nearest-neighbor steps from records with tick `≤ τ`, timed outgoing
dual, mixed stays a set, existential opposite, four y-probes with seed `A`,
per-probe `τ=t+1`, and reverse/face as existence of a pair that sums to zero
are declared. No uniqueness of incoming or outgoing locks, no occupancy `n`,
no named-sign reduction, no singleton leftover as the object, no sum leftover,
no unique-L leftover, no #7211 `M` leftover as the whole display, no untimed
`O` leftover as the whole display, no six-neighbor star as the letter, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold` reports of `M` and of `O` do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in timed `M(q,τ)` or timed `O(q,τ)` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four incoming sets, four outgoing sets, four intersections, and four reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Simultaneous `M` and `O` at `t+1` is leftover of #7211 `M`
because reverse and face of `M` already HOLD, leftover of untimed `O`
because `O(t+1)` equals untimed `O` on these probes, leftover of two-site
nmsimopp because the four-probe letters match, leftover of M two-tick
because `M` is frozen, the sets should be replaced by their sums, unique-L
should suffice at singleton `M(A,τ)`, and occupancy `n` should track those
vectors.

**Answer:** The named construction reports timed incoming `{−e_1}`,
`{+e_1}`, `{+e_2}`, `{−e_2, +e_3, −e_3}` and timed outgoing
`{+e_2, +e_3, −e_3}`, `{+e_2, +e_3, −e_3}`, `{+e_1, −e_1, +e_3, −e_3}`,
`{+e_1, −e_1}` at `A,B,C,D` at each probe's own `τ=t+1`. Intersection is
empty at each probe. Mixed stays a set. The construction does not sum.
Occupancy `n` is not used. Named signs lost the axis. Reverse of `M` holds
from `−e_1` against `+e_1`. Face of `M` holds from `+e_2` against `−e_2`.
Reverse of `O` holds from outgoing `±e_3`. Face of `O` holds from outgoing
`±e_1`. Unique-L leftover of `O` reports reverse `UNDEFINED`. #7211 `M`
leftover does not report `O`. Untimed `O` leftover does not report timed
`M` or the empty intersection. Two-site leftover omits the y-mirror at tick
0. M two-tick leftover omits `O`. Reverse/face of `O` remain displayed, not
adopted. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique-L display on these same #7211 y-probes would assign
`L(A)=−e_1`, `L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` and report reverse
hold with face `UNDEFINED` from `M`, and would assign unique-L of `O`
`UNDEFINED` at every probe. A #7211 own incoming display reports
`M(A) = {−e_1}` with reverse hold and face hold and does not report `O`.
An untimed outgoing display reports `O(A) = {+e_2, +e_3, −e_3}` with reverse
hold and face hold and does not report timed `M`. A two-site nmsimopp
display reports the same four timed letters on these y-probes but seeds only
`{0,(0,1,0)}`. A sum leftover of mixed `M(D,τ)` would replace that set by
`−e_2` after cancelling `+e_3` and `−e_3`. This note is not those displays:
mixed stays a set, the construction does not sum, the letters are timed `M`
and timed `O` together at `τ=t+1`, intersection is empty, reverse of `M`
holds, face of `M` holds, reverse of `O` holds, and face of `O` holds.

**Gate disposition:** PASS for the simultaneous `M` and `O` at `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals the sum of the lock set,” “bits are Admissibility,” “the
letter is occupancy `n`,” “the pair equals unique-L leftover,” “the pair
equals #7211 `M` leftover,” “the pair equals untimed `O` leftover,”
“reverse of `M` fails,” “face of `M` is `UNDEFINED`,” “reverse of `O`
fails,” or “face of `O` is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsyopp #7132 perp-step
incoming-lock process, reads each probe's timed incoming set and timed
outgoing dual at `τ=t+1`, reports the intersection, scores reverse and face
from `M` and from `O` by existential opposite, and checks Theorems 1--3. It
also checks that the construction is not named-sign lettering, that mixed
stays a set, that the construction does not sum, that occupancy `n` is not
used, that a formation member from already-recorded six-neighbor locks is
not attached, that the timed pair is not leftover of unique-L, that the
timed pair is not leftover of #7211 `M` alone, and that the timed pair is
not leftover of untimed `O` alone. No runner cache is written.
