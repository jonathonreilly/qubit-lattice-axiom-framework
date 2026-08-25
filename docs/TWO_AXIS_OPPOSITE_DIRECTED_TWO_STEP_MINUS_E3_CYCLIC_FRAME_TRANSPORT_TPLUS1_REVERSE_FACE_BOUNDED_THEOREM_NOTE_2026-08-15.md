---
claim_id: two_axis_opposite_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Directed 2-step cyclic-frame transport along −e3 at t+1 on the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# Directed 2-Step Cyclic-Frame Transport Along −e3 At t+1 Reverse And Face On The Four Seeds Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** directed 2-step cyclic-frame transport along `−e_3` of
simultaneous earliest incoming set `M` and outgoing dual `O` at each
seed's `τ=t+1`, and reverse/face from that 2-step, on the four seeds of
the two-axis opposite seed in `B_3(0)={n:n·n<=9}`. F, Orient,
directed-edge as nm2frm2sx with step `−e_3`. Orient as nm2oricyclz
(lex-largest cyclic); HOLDING cyclic-frame transport #7490 is existential
(some 6-NN). z-probes are the HOLDING probes of that field. First
display: the named direction `−e_3` twice from each of the four seeds
(all four 2-step chains stay in `B_3`). Not a 4-cycle. This is not leftover of ±e1/±e2. Let `t(q)` be the formation tick of seed `q`. Let
`τ(q)=t(q)+1`. There is no global T. `M(q,τ)` is the set of earliest
incoming nearest-neighbor steps at `q` using only records with tick
`<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the outgoing dual
of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed
and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is
empty, not `UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals
`{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover HOLDs and
`|Axis(M)|=1` (hence `|Axis(O)|=2`). When split HOLDs, `m` is unique in
`M`. Let `i` in `{1,2,3}` be the axis index of `m`. `e_next = e_{i+1}`
with `3+1→1`. `e_prev = e_{i-1}` with `1−1→3`. `O_next = O ∩ {±e_next}`.
`O_prev = O ∩ {±e_prev}`. If either empty, Orient fails, not `UNDEFINED`.
Order `+e < −e`. `o_next` is the lex-largest vector in `O_next` (hence
`−e` if both signs). `o_prev` likewise. `Orient(q)` is the sign of the
integer determinant of the 3×3 matrix with columns `m`, `o_next`,
`o_prev`. If split fails, Orient fails, not `UNDEFINED`. When split
HOLDs, `F(q)=(m,o_next,o_prev)` is an oriented lattice frame. Directed-edge
HOLDs from `q` to `q+e` if and only if `q` and `q+e` are in `B_3(0)`, both
are formed at their own `τ=t+1`, split HOLDs at both, `Orient` is `±1` at
both, and the 3×3 integer matrix sending the columns of `F(q)` to the
columns of `F(q+e)` is a signed permutation `P` with
`det P = Orient(q)Orient(q+e)`. Else that edge fails, not `UNDEFINED`.
Directed 2-step along `−e_3` HOLDs at `q` if and only if `q`, `q−e_3`, and
`q−2e_3` are in `B_3(0)` and directed-edge HOLDs for `(q,q−e_3)` and
`(q−e_3,q−2e_3)`. A vertex outside `B_3(0)` is fail, not `UNDEFINED`. An
unformed vertex inside `B_3(0)` makes that edge fail, not `UNDEFINED`.
Reverse probes: origin and `(0,1,0)`. Face probes: `(0,0,1)` and
`(0,1,1)`. Reverse HOLDs if and only if 2-step along `−e_3` HOLDs at both
reverse probes. Face HOLDs if and only if both face probes HOLD. This is
not leftover of existential 6-NN cyclic-frame transport #7490. This is
not leftover of nm2cycfrmz cyclic-frame transport sending to some formed
six-neighbor. This is not leftover of equal `±1` Orient signs. This is
not leftover of a unique nonnegative permutation sending. This is not
leftover of nm2axz axis-cover. This is not leftover of nm2ax12z 1-in 2-out
split. Uniqueness is not required. Mixed remains a set. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named seeds. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-seed cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Split is cover together with `|Axis(M)|=1`. The cyclic next/prev
lex-largest oriented frame is the integer sign of
`det(m,o_next,o_prev)` with unique signed incoming letter `m` and the
lex-largest signed outgoing letter on the cyclic next and prev axes of
`Axis(M)` under `+e < −e`. When split HOLDs, `F=(m,o_next,o_prev)` is
that LIVE three-axis frame. Directed-edge is the named neighbor sending of
those frames along one declared step. Directed 2-step is two successive
named directed-edges of the same step. Reverse and face are scored on
2-step HOLD at the paired seeds. Existential 6-NN transport is a different
readout and is not used as the object. A unique nonnegative permutation
sending is a different readout and is not used as the object. Named signs
`{+,−}` of locks are a coarser readout and are not used as the object.
Occupancy of sites is not used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of directed 2-step cyclic-frame transport along -e3 of (m,o_next,o_prev) of M and O at t+1 on the four seeds of the two-axis opposite seed, P on each named edge, 2-step bits at A,B,C,D, reverse fail and face hold from those bits; uniqueness of P is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face
target_blocker_text: "display directed 2-step cyclic-frame transport along -e3 reverse/face on the four seeds of the two-axis opposite seed, not a 4-cycle, not leftover of +/-e1/+/-e2, not leftover of existential 6-NN transport"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep directed 2-step cyclic-frame transport along -e3 of (m,o_next,o_prev) of M and O at t+1 displayed; do not write the bits into Admissibility, do not reduce to a 4-cycle, do not reduce to +/-e1/+/-e2 2-step, do not reduce to existential 6-NN cyclic-frame transport, do not reduce to unique nonnegative permutation sending, do not reduce to cover, do not reduce to split, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for directed 2-step cyclic-frame transport along -e3 of (m,o_next,o_prev) of M and O at t+1 on the four seeds of the two-axis opposite seed and reverse/face from that 2-step; displayed, not adopted"
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

No larger host is used. The four seeds are the only sites whose directed
2-step along `−e_3` is scored:

```text
A = (0,0,0),  B = (0,1,0),  C = (0,0,1),  D = (0,1,1).
```

Reverse probes are `A` and `B`. Face probes are `C` and `D`. These are not
the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`, `D=(1,0,1)`. These are
not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)`. These
are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`.
`C` is a seed of the second opposite pair. Same process as nm2axz, scored
at the four seeds rather than at the four z-probes.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. The second pair is a new seed, not a formed
child of the first pair. This seed is not the 1-axis opposite two-site seed
`{0,(0,1,0)}` with only `+e_1/−e_1`. This seed is not the perp two-site
seed `+e_1/+e_2`. This seed is not the same-lock two-site seed
`+e_1/+e_1`. This seed is not the z-symmetric three-site seed
`{0,(0,0,1),(0,0,-1)}`. This seed is not the y-symmetric three-site seed
that also records `(0,-1,0)` at tick 0.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept. A later
parent does not re-form `q`. Uniqueness is not required. Mixed remains a set.

## Named directed 2-step along `−e_3` at `τ=t+1`

Let `t(q)` be the formation tick of seed `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter.

`O(q,τ)` is the outgoing dual of `M`:

```text
O(q,τ) = { e in {±e_1,±e_2,±e_3} | q+e formed and e in M(q+e,τ) }.
```

If `q` is unformed at `τ`, then `O(q,τ)` is `UNDEFINED`. Empty `O` is empty,
not `UNDEFINED`. Duplicate steps collapse in the set. The construction does
not require `O` to be a singleton. It does not sum either set. It does not
replace `O` by `M`. It does not wait for a global later T. Occupancy of
sites is not used. O is not M.

Unsigned axis of a defined lock set:

```text
Axis(S) = { e_i | some ±e_i in S }.
```

Cover at a seed at the same cut:

```text
cover(q) HOLDs iff Axis(M) intersect Axis(O) is empty
and Axis(M) union Axis(O) equals {e_1,e_2,e_3}.
```

Split at a seed at the same cut:

```text
split(q) HOLDs iff cover HOLDs and |Axis(M)|=1
(hence |Axis(O)|=2).
```

2-in 1-out is fail of split, not UNDEFINED. If `q` is unformed at `τ`, then
split is `UNDEFINED`.

Oriented frame at the same cut:

```text
When split HOLDs, m is the unique signed letter in M.
i in {1,2,3} is the axis index of m.
e_next = e_{i+1} with 3+1→1. e_prev = e_{i-1} with 1−1→3.
O_next = O ∩ {±e_next}. O_prev = O ∩ {±e_prev}.
If either is empty, Orient fails, not UNDEFINED.
Order +e < −e. o_next is lex-largest in O_next (hence −e if both signs).
o_prev likewise.
Orient(q) = sign of the integer determinant of columns (m, o_next, o_prev).
Else fail, not UNDEFINED, if split fails.
UNDEFINED if M or O is UNDEFINED.
When split HOLDs, F(q)=(m, o_next, o_prev).
```

Directed-edge and directed 2-step at the same cut, with step `e=−e_3`:

```text
Directed-edge HOLDs from q to q+e iff q and q+e are in B_3(0),
both formed at their own τ=t+1, split HOLDs at both, Orient ±1 at both,
and the 3×3 integer matrix P sending the columns of F(q) to the columns
of F(q+e) (F(q+e)=F(q)P) is a signed permutation with
det(P)=Orient(q)Orient(q+e).
Else that edge fails, not UNDEFINED.
A vertex outside B_3(0) is fail, not UNDEFINED.

Directed 2-step along −e_3 HOLDs at q iff q, q−e_3, q−2e_3 are in B_3(0)
and directed-edge HOLDs for (q, q−e_3) and (q−e_3, q−2e_3).
Uniqueness of P is not required.
```

Reverse directed 2-step holds if and only if 2-step HOLDs at `A` and at
`B`. Face directed 2-step holds if and only if 2-step HOLDs at `C` and at
`D`. Either side `UNDEFINED` is `UNDEFINED`. Else if both sides HOLD,
reverse or face HOLDs. Else fail.

The four seeds form a square in the `e_2e_3` plane. The letter is not a
4-cycle around that square: each scored chain is two steps of the same
vector `−e_3`. The four 2-step chains stay in `B_3(0)`.

## Theorem 1 — ticks, `F`, Orient, `P` on each named edge, and 2-step bits at `τ=t+1`

On this process the four seeds form at tick 0. Compare to leftover of
`±e1/±e2`: directed 2-step along `+e_1`, `−e_1`, `+e_2`, and `−e_2` each
fails reverse and fails face on this member. Compare to leftover of
`+e_3`: 2-step along `+e_3` HOLDs reverse and fails face. Compare to
nm2cycfrmz existential 6-NN transport: transport HOLDs at each of the
four seeds, so transport reverse HOLDs and transport face HOLDs, while
this reverse fails. This display reads the named direction `−e_3` twice:

```text
t(A)=0
t(B)=0
t(C)=0
t(D)=0
M(A, τ) = {+e_1}
M(B, τ) = {−e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_2}
O(A, τ) = {−e_2, −e_3}
O(B, τ) = {+e_2, −e_3}
O(C, τ) = {+e_1, −e_1, +e_3}
O(D, τ) = {+e_1, −e_1, +e_3}
split(A) = hold
split(B) = hold
split(C) = hold
split(D) = hold
F(A) = (+e_1, −e_2, −e_3)
Orient(A) = +1
F(B) = (−e_1, +e_2, −e_3)
Orient(B) = +1
F(C) = (+e_2, +e_3, −e_1)
Orient(C) = −1
F(D) = (−e_2, +e_3, −e_1)
Orient(D) = +1
directed-edge(A, A−e_3) = hold
P(A → A−e_3) = [0 -1 0; 0 0 1; 1 0 0]
det P(A → A−e_3) = -1
directed-edge(A−e_3, A−2e_3) = fail
P(A−e_3 → A−2e_3) = fail
two-step(A) = fail
directed-edge(B, B−e_3) = hold
P(B → B−e_3) = [0 1 0; 0 0 1; 1 0 0]
det P(B → B−e_3) = 1
directed-edge(B−e_3, B−2e_3) = fail
P(B−e_3 → B−2e_3) = fail
two-step(B) = fail
directed-edge(C, C−e_3) = hold
P(C → C−e_3) = [0 -1 0; 0 0 -1; -1 0 0]
det P(C → C−e_3) = -1
directed-edge(C−e_3, C−2e_3) = hold
P(C−e_3 → C−2e_3) = [0 -1 0; 0 0 1; 1 0 0]
det P(C−e_3 → C−2e_3) = -1
two-step(C) = hold
directed-edge(D, D−e_3) = hold
P(D → D−e_3) = [0 -1 0; 0 0 -1; 1 0 0]
det P(D → D−e_3) = 1
directed-edge(D−e_3, D−2e_3) = hold
P(D−e_3 → D−2e_3) = [0 1 0; 0 0 1; 1 0 0]
det P(D−e_3 → D−2e_3) = 1
two-step(D) = hold
```

The four 2-step chains are

```text
A: (0,0,0) → (0,0,−1) → (0,0,−2)
B: (0,1,0) → (0,1,−1) → (0,1,−2)
C: (0,0,1) → (0,0,0) → (0,0,−1)
D: (0,1,1) → (0,1,0) → (0,1,−1)
```

Each of those twelve vertices lies in `B_3(0)`. At `A−2e_3=(0,0,−2)`,
`t=4`, `M={+e_1,−e_1,+e_2}`, `O={−e_3}`, split fails from 2-in 1-out, so
the second reverse edge fails, not `UNDEFINED`. At `B−2e_3=(0,1,−2)`,
`t=4`, `M={+e_1,−e_1,−e_2}`, `O` empty, split fails, so the second reverse
edge fails, not `UNDEFINED`. First directed-edges HOLD at all four seeds.
Second directed-edges HOLD only on the face chains. `det P` on each HOLDING
edge equals the product of the two Orient signs. The first sending at `B`
is a nonnegative permutation; the first sendings at `A`, `C`, and `D` are
not. Unique nonnegative sending is not this letter. Uniqueness of `P` is
not required.

`A` is the origin seed at tick 0 with seed letter `+e_1`. Mixed remains a
set: `O(C,τ)` and `O(D,τ)` each have three outgoing steps. Unique outgoing
letters would assign `UNDEFINED` at mixed `O`. Lex-largest picks `−e` on
each mixed cyclic slot, so `(o_next,o_prev)` is defined. Cover and split
HOLD at each seed and do not score the directed 2-step bits. O is not M.

On the 1-axis opposite two-site seed the second pair is absent, so `C` is
a formed child rather than a seed. That is leftover of the first pair.
Here both `(0,0,1)` and `(0,1,1)` are seeds of a second opposite pair on a
second axis.

## Theorem 2 — reverse from directed 2-step along `−e_3` at `τ`

Reverse directed 2-step cyclic-frame transport holds if and only if
2-step HOLDs at `A` and at `B`. `two-step(A)=fail` and
`two-step(B)=fail`. Reverse fails. This is HOLD iff both 2-steps HOLD,
not leftover of nm2cycfrmz cyclic-frame transport sending, not leftover
of `±e1/±e2`, not leftover of `+e_3`, not leftover of equal Orient signs,
not leftover of a unique nonnegative permutation sending, not leftover of
nm2axz axis-cover, and not leftover of nm2ax12z 1-in 2-out split.

Reverse directed 2-step cyclic-frame transport at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Existential 6-NN
transport reverse HOLDs because transport HOLDs at `A` and at `B`. Orient
reverse HOLDs because `Orient(A)=+1` and `Orient(B)=+1`. Cover reverse
HOLDs. Split reverse HOLDs. Those leftovers are not this display. Directed
2-step along `+e_3` HOLDs reverse on this same seed while this reverse
fails.

Reverse fails.

## Theorem 3 — face from directed 2-step along `−e_3` at `τ`

Face directed 2-step cyclic-frame transport holds if and only if 2-step
HOLDs at `C` and at `D`. `two-step(C)=hold` and `two-step(D)=hold`. Face
HOLDs.

Face directed 2-step cyclic-frame transport at τ: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Directed 2-step along `+e_1`, `−e_1`, `+e_2`, and `−e_2` each fails face
on this member while this face HOLDs. Directed 2-step along `+e_3` fails
face because `C−2e_3=(0,0,3)` is unformed in `B_3(0)` and
`D−2e_3=(0,1,3)` lies outside `B_3(0)`; both are fail, not `UNDEFINED`.
Existential 6-NN transport face HOLDs as this face HOLDs from a different
object: two named directed-edges along `−e_3`, not some 6-NN sending.
Cover face HOLDs. Split face HOLDs. Cover and split do not score
handedness.

Face HOLDs.

## What this note does not claim

- It does not replace directed 2-step by a 4-cycle of the four seeds.
- It does not replace directed 2-step along `−e_3` by directed 2-step along `±e1/±e2`.
- It does not replace directed 2-step along `−e_3` by directed 2-step along `+e_3`.
- It does not replace directed 2-step by nm2cycfrmz existential 6-NN sending.
- It does not replace directed 2-step by equal `±1` Orient signs.
- It does not replace directed 2-step by a unique nonnegative permutation sending.
- It does not require a unique sending matrix.
- It does not select a unique outgoing or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require outgoing sides to be singletons.
- It does not sum either set.
- It does not replace Orient by leftover-empty fail.
- It does not replace Orient by leftover of `M` alone.
- It does not replace Orient by leftover of `O` alone.
- It does not replace Orient by axis-cover without the frame sign.
- It does not replace Orient by 1-in 2-out split without the frame sign.
- It does not treat split fail as `UNDEFINED`.
- It does not treat a vertex outside `B_3(0)` as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nm2axz axis-cover reverse hold face hold as this
  directed 2-step.
- It does not reprint nm2ax12z 1-in 2-out split reverse hold face hold as
  this directed 2-step.
- It does not reprint nm2oricyclz cyclic Orient reverse hold as this
  directed 2-step.
- It does not reprint the 1-axis opposite two-site seed as this member.
- It does not score the z-probes, y-probes, or x-probes as this letter.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not use occupancy of sites as the letter.
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

This display uses Lattice to name `B_3(0)` and the four seeds. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
two-axis opposite seed process, directed 2-step cyclic-frame transport of
`(m,o_next,o_prev)` of `M` and `O` along `−e_3` at `t+1`, and the
reverse/face bits from that 2-step are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `0`, `0`, `0` |
| cyclic frame `F=(m,o_next,o_prev)` at `τ=t+1` | Theorem 1; LIVE three-axis at each seed |
| Orient at `τ` | Theorem 1; `+1`, `+1`, `−1`, `+1` |
| `P` on each named `−e_3` edge | Theorem 1; HOLD then fail on reverse; HOLD then HOLD on face |
| directed 2-step along `−e_3` at `τ` | Theorem 1; fail, fail, hold, hold |
| reverse from directed 2-step at `τ` | Theorem 2; `fail` |
| face from directed 2-step at `τ` | Theorem 3; `hold` |
| leftover of `±e1/±e2` 2-step | not this letter; those reverse fail and face fail |
| leftover of `+e_3` 2-step | not this letter; reverse hold and face fail |
| leftover of a 4-cycle of the four seeds | not this letter |
| leftover of existential 6-NN transport | not this letter; that reverse HOLDs |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| unique nonnegative sending as the letter | not used |
| z-probe or y-probe or x-probe 2-step | not this letter |
| leftover of the 1-axis opposite two-site seed | not this display |
| leftover of the same-lock two-site seed | not this display |
| split fail scored as `UNDEFINED` | refused; edge fail |
| vertex outside `B_3(0)` scored as `UNDEFINED` | refused; edge fail |
| global later T | not used |
| directed 2-step as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: directed 2-step cyclic-frame transport along `−e_3` of `(m,o_next,o_prev)` of `M` and `O` at `t+1` on the four seeds of the two-axis opposite seed, and reverse/face from that 2-step. |
| V2 | Current main has no landed directed 2-step cyclic-frame-transport reverse/face along `−e_3` of timed `M` and `O` on these four seeds of the two-axis opposite seed. |
| V3 | Four 2-step reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads two named directed-edges along `−e_3` at the same `t+1` cut, reverse fails and face HOLDs while `±e1/±e2` reverse fail and face fail, while `+e_3` reverse HOLDs and face fails, and while existential 6-NN transport reverse HOLDs. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to a 4-cycle, does not reduce them to
`±e1/±e2`, does not reduce them to existential 6-NN transport, does not
reduce them to unique nonnegative sending, does not reduce them to cover,
does not reduce them to split, and does not identify this seed with the
1-axis opposite two-site seed. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| 4-cycle of the four seeds | walk origin → `(0,1,0)` → `(0,1,1)` → `(0,0,1)` → origin | each scored chain is two steps of the same vector `−e_3`; endpoints are `(0,0,−2)` and `(0,1,−2)`, not a return | ATTEMPTED |
| directed 2-step along `+e_1` | reuse the same 2-step predicate on `+e_1` | reverse fails and face fails while this face HOLDs | ATTEMPTED |
| directed 2-step along `−e_1` | reuse the same 2-step predicate on `−e_1` | reverse fails and face fails while this face HOLDs | ATTEMPTED |
| directed 2-step along `+e_2` | reuse the same 2-step predicate on `+e_2` | reverse fails and face fails; `A` HOLDs but `B` fails from unformed `(0,3,0)` | ATTEMPTED |
| directed 2-step along `−e_2` | reuse the same 2-step predicate on `−e_2` | reverse fails and face fails; `B` HOLDs but `A` fails at the second edge | ATTEMPTED |
| directed 2-step along `+e_3` | reuse the opposite z direction | reverse HOLDs and face fails while this reverse fails and this face HOLDs | ATTEMPTED |
| nm2cycfrmz existential 6-NN transport | HOLD if some formed 6-NN hosts a signed-permutation sending | transport HOLDs at each of `A,B,C,D`, so transport reverse HOLDs while this reverse fails | ATTEMPTED |
| equal Orient signs | reverse HOLD from `Orient(A)=Orient(B)=+1` | Orient reverse HOLDs while this reverse fails | ATTEMPTED |
| unique nonnegative sending | require a sending with no minus signs | first sending at `B` is nonnegative, first sendings at `A,C,D` are not; uniqueness is not required | ATTEMPTED |
| nm2axz axis-cover | reuse cover reverse hold and cover face hold | cover HOLDs reverse and face without named `−e_3` edges | ATTEMPTED |
| nm2ax12z 1-in 2-out split | reuse split reverse hold and split face hold | split HOLDs reverse and face without a sending matrix | ATTEMPTED |
| z-probes of this seed | score `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`, `D=(1,0,1)` | those are HOLDING probes of existential transport #7490; this letter is the four seeds | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(C)` as a formed child | different seed; second pair is a new seed, not a formed child | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is two disjoint opposite pairs | ATTEMPTED |
| vertex outside `B_3(0)` as `UNDEFINED` | treat `(0,1,3)` as unformed | outside is fail, not UNDEFINED | ATTEMPTED |
| split fail as `UNDEFINED` | treat 2-in 1-out at `(0,0,−2)` as unformed | split fail is edge fail, not UNDEFINED | ATTEMPTED |
| global later T | wait until `max t` before reading | `τ(q)=t(q)+1` is per-seed; no global T | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the directed 2-step | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of this 2-step with
`±e1/±e2`, missing identification with a 4-cycle, missing identification
with existential 6-NN transport, missing identification with unique
nonnegative sending, missing identification with cover, missing
identification with split, missing identification of this seed with the
1-axis opposite two-site seed, and missing Record identification of the
2-step bits are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite seed pairs `+e_1/−e_1` and
`+e_2/−e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-seed `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic
next/prev axes of `Axis(M)`, lex-largest signed outgoing letter under
`+e < −e`, integer determinant sign, directed-edge along a named step,
directed 2-step as two successive named edges, vertex outside `B_3(0)` as
fail not `UNDEFINED`, four seeds with reverse `{origin,(0,1,0)}` and face
`{(0,0,1),(0,1,1)}`, second pair as a new seed not a formed child, and
mixed remains a set are declared. No uniqueness of `P`, no six-neighbor
star as the scored object, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
2-step `fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | directed 2-step cyclic-frame sending along `−e_3` | no continuum alphabet |
| per site | seeds origin, `(0,1,0)`, `(0,0,1)`, `(0,1,1)` on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four 2-step reports, reverse/face from those bits | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for directed 2-step
cyclic-frame transport reverse/face, a formation-rate rule, and a
physical selector among named lattice directions. None is taken here.

### N7 — hostile steelman

**Steelman:** Reverse fail and face hold are only leftover of existential
6-NN cyclic-frame transport, or of a 4-cycle of the four seeds, or of
`±e1/±e2` 2-step, or of `+e_3` 2-step, or of equal Orient signs, or of
cover and split; the second pair is only the formed child `(0,0,1)` of
the 1-axis seed; unique nonnegative sending already answers `B`; and the
z-probes already display HOLDING cyclic-frame transport.

**Answer:** Existential 6-NN transport HOLDs at each of the four seeds, so
that reverse HOLDs while this reverse fails. A 4-cycle would return to the
starting seed; `A` ends at `(0,0,−2)`. Directed 2-step along `±e1/±e2`
fails reverse and fails face while this face HOLDs. Directed 2-step along
`+e_3` HOLDs reverse and fails face, the opposite reverse/face pair.
Orient reverse HOLDs from `+1,+1` while this reverse fails. Cover and
split HOLD reverse and face without named `−e_3` edges. The second pair
is a new seed, not a formed child: `(0,0,1)` is recorded at tick 0 with
lock `+e_2`. Unique nonnegative sending at the first `B` edge is not the
four-seed 2-step letter. The z-probes are a different four-tuple.

### N8 — cross-cycle echo

nm2axz cover on this two-axis seed reported cover HOLD at the four
z-probes, reverse hold, and face hold. nm2ax12z 1-in 2-out split on the
same seed reported split HOLD reverse hold and face hold. nm2oricyclz
cyclic next/prev lex-largest Orient on the same seed reported Orient
`−1,−1,+1,+1` at those z-probes, reverse hold, and face hold from equal
signs, without a sending matrix. nm2cycfrmz cyclic-frame transport on the
same seed reported existential 6-NN transport HOLD at those z-probes,
reverse hold, and face hold. HOLDING cyclic-frame transport #7490 is
existential (some 6-NN); the z-probes are the HOLDING probes of that
field. This note is not those displays: it reports directed 2-step
cyclic-frame transport along `−e_3` at `τ=t+1` on the two-axis opposite
seed, with `t(A)=0`, `t(B)=0`, `t(C)=0`, and `t(D)=0`, `two-step(A)=fail`,
`two-step(B)=fail`, `two-step(C)=hold`, `two-step(D)=hold`, reverse fail,
and face hold. Not a 4-cycle. Not leftover of `±e1/±e2`.

**Gate disposition:** PASS for the directed 2-step cyclic-frame-transport
along `−e_3` `t+1` reverse/face reports above. FAIL / DO NOT SHIP for “the
predicate equals a 4-cycle,” “the predicate equals `±e1/±e2` 2-step,”
“the predicate equals `+e_3` 2-step,” “the predicate equals nm2cycfrmz
cyclic-frame transport sending HOLD,” “the predicate equals equal Orient
signs,” “the predicate equals unique nonnegative permutation sending HOLD,”
“the predicate equals nm2axz axis-cover HOLD,” “the predicate equals
nm2ax12z 1-in 2-out split HOLD,” “the predicate equals the 1-axis opposite
two-site seed,” “the predicate equals the z-probes,” “bits are
Admissibility,” “split fail is UNDEFINED,” or “a vertex outside `B_3(0)`
is UNDEFINED.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each seed's own earliest incoming
set and own outgoing dual from the record prefix at that seed's `t+1`,
reports the cyclic frame `F=(m,o_next,o_prev)`, reports Orient as
nm2oricyclz lex-largest cyclic, reports directed-edge along `−e_3` by a
signed-permutation sending to the named neighbor, reports directed 2-step
as both named edges HOLD with all three vertices in `B_3(0)`, and checks
Theorems 1--3. It also checks that reverse fails and face HOLDs, that all
four 2-step chains stay in `B_3(0)`, that the letter is not a 4-cycle,
that directed 2-step along `±e1/±e2` fails reverse and fails face, that
directed 2-step along `+e_3` HOLDs reverse and fails face, that
existential 6-NN transport reverse HOLDs while this reverse fails, that a
vertex outside `B_3(0)` is fail not `UNDEFINED`, that an unformed vertex
inside `B_3(0)` is edge fail not `UNDEFINED`, that split fail at
`(0,0,−2)` is edge fail not `UNDEFINED`, that the 1-axis opposite two-site
seed is a different member, that #7477 same-lock is a different member,
that LIVE three-axis as a three-site seed is a different member, that the
z-probes of this seed are not this letter, that mixed sets remain sets,
that a formation member from already-recorded six-neighbor locks is not
attached, that the second pair is a new seed not a formed child, and that
the display is not the two-tick lock-count clock composition. No runner
cache is written.
