---
claim_id: x_symmetric_three_site_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Forall-orthogonal M vs O at t+1 on the four #7213 x-probes, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/x_symmetric_three_site_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py
---

# Forall-Orthogonal Incoming Versus Outgoing At T Plus One On Four #7213 X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** forall-orthogonal own incoming set `M` versus own outgoing dual `O`
at each probe's `τ=t+1` on the four nmszopx #7213 x-probes in
`B_3(0)={n:n·n<=9}`. Same process and x-probes as nmszopx #7213. Let
`t(q)` be the formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is
the set of earliest incoming nearest-neighbor steps at `q` using only
records with tick `<= τ`. Seeds use their seed letter as a singleton.
Unformed at `τ` is `UNDEFINED`. `O(q,τ)` is the outgoing dual of `M`: the
set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed in `B_3(0)` and
`e` is in `M(q+e,τ)`. Unformed `q` at `τ` is `UNDEFINED`. Empty `O` is
empty, not `UNDEFINED`. Forall-perp holds if and only if every `m` in
`M(q,τ)` and every `o` in `O(q,τ)` have integer dot `m·o=0`. Empty or
`UNDEFINED` on either side is `UNDEFINED`. Reverse holds if and only if
forall-perp holds at `A` and at `B`. Face holds if and only if forall-perp
holds at `C` and at `D`. Unique `L` is not the object. Occupancy `n` is
not used. This is not named-sign lettering. This is not a unique
lock-vector leftover and not a sum leftover. This is not leftover of
unique-L, which is `UNDEFINED` when mixed. This is not leftover of
exist-opposite, which scores a pair that sums to zero inside `M` or inside
`O`. This is not leftover of exist-perp, which HOLDs from a single
orthogonal pair while a parallel pair remains. This is not leftover of O
at t, which leaves reverse and face `UNDEFINED` from empty `O` at `A`,
`B`, and `C`. This is not leftover of empty intersection: disjointness of
`M` and `O` is weaker than every pair having integer dot zero. The
construction does not use a six-neighbor star. Uniqueness of incoming or
outgoing locks is not required. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1. This note does not write forall-orthogonal
into Admissibility and does not attach a formation member from
already-recorded six-neighbor locks. This display does not use occupancy.
Mixed stays a set. O is not M.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/x_symmetric_three_site_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py`](../scripts/x_symmetric_three_site_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at a per-probe cut
`τ=t+1`. Forall-perp is scored on integer dots of every pair from `M`
against `O`. Reverse and face are scored on forall-perp at the named pair
of probes. Named signs `{+,−}` are a coarser readout and are not used. A
singleton unique lock-vector letter is a different readout and is not used
as the object: report `M`, `O`, the dots, and forall-perp. A `Z^3` sum of
those locks is a different readout and is not used. The construction does
not sum. Occupancy `n` is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of forall-orthogonal M vs O at t+1 on the four #7213 x-probes, with reverse hold and face hold from forall-perp at A,B and at C,D; uniqueness of incoming or outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: x_symmetric_three_site_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face
target_blocker_text: "display forall-orthogonal M vs O at t+1 on the four #7213 x-probes, and reverse/face from that, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep forall-perp, reverse, and face displayed; do not write forall-orthogonal into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the report with unique-L leftover, do not identify the report with exist-opposite leftover, do not identify the report with exist-perp leftover, and do not identify the report with O at t."
conditional_surface_status: "exact on B_3(0) for forall-orthogonal M vs O at t+1 on the four #7213 x-probes; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose own
incoming sets and outgoing duals are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. `A` is a seed. Same process and x-probes as nmszopx #7213.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (1,0,0), (-1,0,0)}` is recorded at formation
tick 0 with locks `+e_2` at the origin, `−e_2` at `(1,0,0)`, and `−e_2` at
`(-1,0,0)`. The third site is the x-mirror of the two-site opposite-lock
partner `(1,0,0)`. This seed is not the two-site opposite-lock seed
`{0,(1,0,0)}` and not the three-site opposite-lock seed whose third site is
`(0,1,0)` with lock `+e_1`. This seed is not the perp two-site seed
`+e_2/+e_1`. This seed is not the y-symmetric three-site seed
`{0,(0,1,0),(0,-1,0)}`. This seed is not the z-symmetric three-site nszmenu
#7188 seed `{0,(0,0,1),(0,0,-1)}`.

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

## Named forall-orthogonal `M` versus `O` at `τ=t+1`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global later T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter. Mixed stays a set. Duplicate incoming steps
collapse in the set. The construction does not require `M(q,τ)` to be a
singleton. It does not sum `M(q,τ)`. Occupancy `n` is not used. Unique
`L(q)` is not used as the letter. This display does not use a six-neighbor
star.

`O(q,τ)` is the outgoing dual of `M`:

```text
O(q,τ) = { e in {±e_1,±e_2,±e_3} | q+e formed in B_3(0) and e in M(q+e,τ) }.
```

If `q` is unformed at `τ`, then `O(q,τ)` is `UNDEFINED`. Empty `O` is empty,
not `UNDEFINED`. Duplicate outgoing steps collapse in the set. The
construction does not require `O(q,τ)` to be a singleton. It does not sum
`O(q,τ)`. It does not replace `O` by `M`. O is not M.

Forall-perp at a formed probe with both sets nonempty:

```text
forall-perp(q)  <=>  every m in M(q,τ) and every o in O(q,τ) have m·o = 0
```

If `M(q,τ)` or `O(q,τ)` is empty or `UNDEFINED`, forall-perp is
`UNDEFINED`. Else forall-perp fails if any pair has nonzero integer dot.
Exist-perp (some pair dots to 0) is comparison only and is not the letter.
Exist-opposite inside `M` or inside `O` is comparison only and is not the
letter.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on
forall-perp of integer dots. They are not scored on `{+,−}` names and are
not an occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  forall-perp at A and forall-perp at B
face     <=>  forall-perp at C and forall-perp at D
```

If either side of a comparison is `UNDEFINED`, that bit is `UNDEFINED`.
Else the bit fails if either side fails. The report is one of `hold`,
`fail`, or `UNDEFINED`.

Admissibility is not edited. Forall-orthogonal is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — formation ticks, `M`, `O`, dots, and forall-perp at `τ=t+1`

Direct enumeration of the displayed nmszopx #7213 process on `B_3(0)` forms
all four x-probes. The formation ticks are `t(A)=0`, `t(B)=2`, `t(C)=1`,
`t(D)=3`. `A` is a seed. Those ticks locate the per-probe cut `τ=t+1`.
They are not occupancy kernels and are not a global later T.

Own incoming sets, outgoing duals, integer dots, and forall-perp at `τ=t+1`
are:

```text
A: seed letter −e_2;
   t(A)=0;  M(A, τ) = {−e_2}
            O(A, τ) = {+e_1, +e_3, −e_3}
            dots: (−e_2)·(+e_1)=0, (−e_2)·(+e_3)=0, (−e_2)·(−e_3)=0
            forall-perp(A) = hold
B: incoming +e_2;
   t(B)=2;  M(B, τ) = {+e_2}
            O(B, τ) = {+e_1, +e_3, −e_3}
            dots: (+e_2)·(+e_1)=0, (+e_2)·(+e_3)=0, (+e_2)·(−e_3)=0
            forall-perp(B) = hold
C: incoming +e_1;
   t(C)=1;  M(C, τ) = {+e_1}
            O(C, τ) = {+e_2, −e_2, +e_3, −e_3}
            dots: (+e_1)·(+e_2)=0, (+e_1)·(−e_2)=0, (+e_1)·(+e_3)=0, (+e_1)·(−e_3)=0
            forall-perp(C) = hold
D: incoming −e_1, −e_3, +e_3;
   t(D)=3;  M(D, τ) = {−e_1, +e_3, −e_3}
            O(D, τ) = {+e_2, −e_2}
            dots: (−e_1)·(+e_2)=0, (−e_1)·(−e_2)=0, (+e_3)·(+e_2)=0,
                  (+e_3)·(−e_2)=0, (−e_3)·(+e_2)=0, (−e_3)·(−e_2)=0
            forall-perp(D) = hold
```

`A` is a seed at tick 0. Mixed stays a set: `M(D,τ)` has three earliest
incoming steps `−e_1`, `−e_3`, and `+e_3`, and `O(A,τ)` has three outgoing
steps `+e_1`, `+e_3`, and `−e_3`. Unique-L leftover would assign
`UNDEFINED` from those mixes. Here uniqueness is not required.

`M` is frozen from formation to `t+1`: `M(q,t+1)=M(q,t)` at every scored
probe, matching nmszopx HOLDING `M`. `O` is not frozen from `t`:
`O(A,t)={}`, `O(B,t)={}`, `O(C,t)={}`, `O(D,t)={−e_2}`. Empty `O` at `t`
for `A`, `B`, and `C` is empty, not `UNDEFINED`, so forall-perp at `t` is
`UNDEFINED` at those probes. New six-neighbor records at `t+1` enter `O`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0), (1, 0, 1), (1, 0, -1)
new 6-NN of B at t(B)+1: (2, 1, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, 1, 0), (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (1, 2, 0)
```

Every scored pair has integer dot zero. Forall-perp holds at `A`, `B`,
`C`, and `D`. O is not M. The own-incoming letters that HOLD exist-opposite
of nmszopx, `−e_2` in `M(A)` against `+e_2` in `M(B)`, are not the
forall-perp letter: that leftover scores a pair inside `M`, while
forall-perp scores every pair from `M` against `O`.

This is not leftover of exist-opposite: that leftover HOLDs reverse and
face from a pair that sums to zero inside `M` and inside `O`, including on
the three-site opposite-lock seed whose third site is `(0,1,0)` with lock
`+e_1`, where forall-perp fails at `B` and at `D` because `+e_1` and `+e_2`
meet themselves in `M` and `O`. This is not leftover of exist-perp: that
leftover HOLDs at those mixed probes from a single orthogonal pair while a
parallel pair remains. This is not leftover of unique-L. This is not
leftover of O at t.

Incoming and outgoing locks exist and need not be unique. That
non-uniqueness does not empty the sets. Uniqueness is not required.

## Theorem 2 — reverse from forall-perp at `A` and `B`

Reverse holds if and only if forall-perp holds at `A` and at `B`. Both
probes are formed at `τ` with nonempty `M` and nonempty `O`. Forall-perp
holds at `A` from `{−e_2}` against `{+e_1, +e_3, −e_3}`. Forall-perp holds
at `B` from `{+e_2}` against `{+e_1, +e_3, −e_3}`. Reverse holds.

Reverse: hold

This is not `fail` and not `UNDEFINED`. Reverse holds.

O at t leftover reports reverse `UNDEFINED` from empty `O` at `A` and at
`B`. Unique-L leftover reports reverse `UNDEFINED` from mixed `O(A,τ)`.
Exist-opposite leftover also HOLDs reverse from `M` on this seed, but it
HOLDs reverse from `M` on the three-site opposite-lock leftover where
forall-perp reverse fails. Reverse holds.

## Theorem 3 — face from forall-perp at `C` and `D`

Face holds if and only if forall-perp holds at `C` and at `D`. Both probes
are formed at `τ` with nonempty `M` and nonempty `O`. Forall-perp holds at
`C` from `{+e_1}` against `{+e_2, −e_2, +e_3, −e_3}`. Forall-perp holds at
`D` from `{−e_1, +e_3, −e_3}` against `{+e_2, −e_2}`. Face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Unique-L leftover reports face
`UNDEFINED` from mixed `M(D,τ)` and mixed `O`. O at t leftover reports
face `UNDEFINED` from empty `O` at `C`. Exist-opposite leftover HOLDs face
from `M` on the three-site opposite-lock leftover where forall-perp face
fails at mixed `D`. Those are different objects. Face holds because every
pair from `M` against `O` at `C` and at `D` has integer dot zero.

Face holds.

## What this note does not claim

- It does not select a unique incoming lock or a unique outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the own incoming set or the outgoing dual to be a
  singleton.
- It does not sum the own incoming set or the outgoing dual.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  lock vectors.
- It does not reprint unique-L letters on these x-probes as the object.
- It does not reprint exist-opposite reverse/face of `M` or of `O` as the
  letter.
- It does not reprint exist-perp as the letter.
- It does not reprint O at t `UNDEFINED`/`UNDEFINED` as this cut.
- It does not replace `O` by `M`.
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

This display uses Lattice to name `B_3(0)` and the four x-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
x-symmetric three-site process, the own incoming sets, the outgoing duals at
`t+1`, the integer dots, the forall-perp bits, and the reverse/face
predicates are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nmszopx #7213 seed `+e_2/−e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| `M` at `τ=t+1` | Theorem 1; `{−e_2}`, `{+e_2}`, `{+e_1}`, `{−e_1, +e_3, −e_3}` |
| `O` at `τ=t+1` | Theorem 1; `{+e_1, +e_3, −e_3}`, `{+e_1, +e_3, −e_3}`, `{+e_2, −e_2, +e_3, −e_3}`, `{+e_2, −e_2}` |
| integer dots `m·o` | Theorem 1; all zero |
| forall-perp at `A,B,C,D` | Theorem 1; `hold` / `hold` / `hold` / `hold` |
| reverse from forall-perp at `A` and `B` | Theorem 2; `hold` |
| face from forall-perp at `C` and `D` | Theorem 3; `hold` |
| unique incoming or outgoing lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed stays a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique-L | not this display |
| leftover of exist-opposite | not this display |
| leftover of exist-perp | not this display |
| leftover of O at t | not this display |
| six-neighbor star as the letter | not used |
| forall-orthogonal as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: forall-orthogonal `M` vs `O` at `t+1` on the four #7213 x-probes, reverse/face from that, or `UNDEFINED`. |
| V2 | Current main has no landed forall-orthogonal incoming/outgoing `t+1` reverse/face report on these four #7213 x-probes. |
| V3 | The sets, the integer dots, and the `hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the probe's own incoming set and outgoing dual at `t+1` and scores every pair's integer dot. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique-L,
does not reprint exist-opposite, does not reprint exist-perp, does not
reprint O at t, does not use a six-neighbor star, does not replace `O` by
`M`, and does not use occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique-L leftover | require a singleton `{v}` subset `{±e_i}` else `UNDEFINED` | refused; leftover; reverse and face would be `UNDEFINED` from mixed `O(A,τ)` and mixed `M(D,τ)` while forall-perp holds |
| exist-opposite leftover | score a pair that sums to zero inside `M` or inside `O` | refused; leftover; that readout HOLDs reverse and face from `M` on the three-site opposite-lock leftover where forall-perp reverse fails and face fails |
| exist-perp leftover | score some pair with integer dot zero | refused; leftover; that readout HOLDs at mixed leftover `B` and `D` while a parallel pair remains and forall-perp fails |
| empty-intersection leftover | score `M ∩ O = {}` | refused; leftover; `{+e_1}` against `{−e_1}` is disjoint and forall-perp fails |
| O at t | score outgoing dual at formation instead of `t+1` | refused; leftover; empty `O` at `A`, `B`, and `C` makes reverse and face `UNDEFINED` |
| six-neighbor lock union | score locks of six-neighbors formed by `τ` | refused; leftover; that readout includes `+e_2` at `A` from the origin partner, which is absent from `O(A,τ)` |
| sum of the same sets | replace `M` or `O` by the `Z^3` sum | refused; leftover; the construction does not sum; sum of mixed `M(D,τ)` cancels to `−e_1` while `M(D,τ)` stays a three-element set |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `τ` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by forall-orthogonal | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming or outgoing step per probe | uniqueness is not required; mixed stays a set |
| replace `O` by `M` | identify the outgoing dual with earliest incoming | refused; O is not M |

### N2 — wall independence

Missing physical adoption, missing identification of `O` with `M`, and
missing Record identification of forall-orthogonal are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, x-symmetric three-site seed locks `+e_2`, `−e_2`, and
`−e_2`, perpendicular step rule, incoming-step lock, own incoming set of
earliest nearest-neighbor steps from records with tick `<= τ`, outgoing dual
of that set, mixed stays a set, forall-perp of integer dots, four x-probes
with seed `A`, per-probe `τ=t+1`, empty `O` empty not `UNDEFINED`, and
reverse/face as forall-perp at the named pair of probes are declared. No
uniqueness of incoming or outgoing locks, no occupancy `n`, no named-sign
reduction, no singleton leftover as the object, no sum leftover, no
unique-L leftover, no exist-opposite leftover, no exist-perp leftover, no
O at t leftover, no six-neighbor star as the letter, no global later T, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each pair of lock vectors from an own incoming set against an outgoing dual | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `M` sets, four `O` sets, integer dots, forall-perp, reverse/face | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Forall-orthogonal `M` versus `O` is leftover of exist-opposite
because reverse and face already HOLD from `M` and from `O` on this seed,
leftover of exist-perp because every pair that is orthogonal is some pair
that is orthogonal, leftover of empty intersection because unit steps that
are disjoint cannot share an axis, leftover of unique-L because `M(A)` is
already the singleton `{−e_2}`, leftover of O at t because children will
exist, leftover of a six-neighbor lock union because those neighbors
supply the outgoing steps, the sets should be replaced by their sums,
named signs should suffice because they keep orientation, and occupancy
`n` should track that vector.

**Answer:** The named construction reports incoming sets `{−e_2}`,
`{+e_2}`, `{+e_1}`, `{−e_1, +e_3, −e_3}` and outgoing duals
`{+e_1, +e_3, −e_3}`, `{+e_1, +e_3, −e_3}`, `{+e_2, −e_2, +e_3, −e_3}`,
`{+e_2, −e_2}` at `A,B,C,D` from the record prefix at each probe's `t+1`.
Every pair has integer dot zero. Mixed stays a set. The construction does
not sum. Occupancy `n` is not used. Named signs lost the axis. Reverse
holds. Face holds. Exist-opposite leftover HOLDs reverse and face from `M`
on the three-site opposite-lock leftover where forall-perp reverse fails
and face fails. Exist-perp leftover HOLDs at those mixed leftover probes
while a parallel pair remains. Unique-L leftover reports reverse
`UNDEFINED` and face `UNDEFINED`. O at t leftover reports reverse
`UNDEFINED` and face `UNDEFINED`. `{+e_1}` against `{−e_1}` is disjoint
and forall-perp fails. The bits remain displayed. Incoming-lock uniqueness
is not required.

### N8 — cross-cycle echo

A unique-L display on these same #7213 x-probes would assign
`L(A)=−e_2`, `L(B)=+e_2`, `L(C)=+e_1`, `L(D)=UNDEFINED` and report reverse
`UNDEFINED` from mixed `O(A,τ)`. Exist-opposite of `M` reports reverse
hold and face hold from a pair that sums to zero, including on leftover
seeds where forall-perp reverse fails. Exist-perp reports some orthogonal
pair and HOLDs where forall-perp fails. O at t reports reverse
`UNDEFINED` and face `UNDEFINED` from empty `O` at `A`, `B`, and `C`. A
sum leftover of the same lists would replace mixed `M(D,τ)` by `−e_1`
after cancelling `+e_3` and `−e_3`. This note is not those displays: mixed
stays a set, the construction does not sum, every pair from `M` against
`O` is scored, Reverse holds, and Face holds.

**Gate disposition:** PASS for the forall-orthogonal `M` vs `O` at `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals the sum of the lock set,” “bits are Admissibility,”
“the letter is occupancy `n`,” “the report equals unique-L leftover,”
“the report equals exist-opposite leftover,” “the report equals exist-perp
leftover,” “the report equals O at t,” “O equals M,” “reverse fails,” or
“face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nmszopx #7213
perp-step incoming-lock process, reads each probe's own incoming set and
outgoing dual from records with tick `<= t+1`, scores integer dots of
every pair, scores forall-perp, scores reverse and face from forall-perp
at `A,B` and at `C,D`, and checks Theorems 1--3. It also checks that the
construction is not named-sign lettering, that mixed stays a set, that the
construction does not sum, that occupancy `n` is not used, that a
formation member from already-recorded six-neighbor locks is not attached,
that the report is not leftover of unique-L, that the report is not
leftover of exist-opposite, that the report is not leftover of exist-perp,
and that the report is not leftover of O at t. No runner cache is written.
