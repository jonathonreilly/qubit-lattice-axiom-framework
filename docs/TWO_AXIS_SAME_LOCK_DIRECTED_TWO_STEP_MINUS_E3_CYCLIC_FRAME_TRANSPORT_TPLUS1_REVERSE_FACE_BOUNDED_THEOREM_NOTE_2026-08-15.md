---
claim_id: two_axis_same_lock_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Directed 2-step cyclic-frame transport along −e3 at t+1 on the two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# Directed 2-Step Cyclic-Frame Transport Along −e3 At t+1 Reverse And Face On The Four Seeds Of The Two-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** directed 2-step cyclic-frame transport along `−e_3` of
simultaneous earliest incoming set `M` and outgoing dual `O` at each
seed's `τ=t+1`, and reverse/face from that 2-step, on the four seeds of
the two-axis same-lock seed in Euclidean B_3(0)={n:n·n<=9}. F, Orient,
directed-edge as nm2frm2sx with step `−e_3`. Directed 2-step along `−e_3`
as nm2frm2sz. Reverse probes: origin and `(0,1,0)`. Face probes: `(0,0,1)`
and `(0,1,1)`. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

## Result up front

On the two-axis same-lock seed, cyclic-frame transport along a named edge is
the signed-permutation sending of the ordered triple `F=(m,o_next,o_prev)`
with `F(q+e)=F(q)P`. This note displays the *directed* two-step along `−e_3`
twice from each of the four seed sites. It is two hops, not one. It is not
leftover of the 1-step along `−e_3` on this same seed. It is not leftover of
the opposite-lock directed 2-step along `−e_3`.

At each seed's own cut `τ=t+1` (`t=0`, so `τ=1` at the seeds) the reverse
pair fails on the second hop and the face pair is mixed: `(0,0,1)` fails
because split fails, while `(0,1,1)` HOLDs both hops. Therefore

```text
reverse: fail
face: fail
```

The bits are Displayed, not adopted. Do not write into Admissibility. Do not
attach L1. Uniqueness of P is not required.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of directed 2-step cyclic-frame transport along -e3 of (m,o_next,o_prev) of M and O at t+1 on the four seeds of the two-axis same-lock seed, P on each named edge, 2-step bits at A,B,C,D, reverse fail and face fail from those bits; uniqueness of P is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face
target_blocker_text: "display directed 2-step cyclic-frame transport along -e3 reverse/face on the four seeds of the two-axis same-lock seed, not a 4-cycle, not leftover of the 1-step, not leftover of opposite-lock 2-step"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep directed 2-step cyclic-frame transport along -e3 of (m,o_next,o_prev) of M and O at t+1 displayed; do not write the bits into Admissibility, do not reduce to a 4-cycle, do not reduce to the 1-step, do not reduce to opposite-lock 2-step, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for directed 2-step cyclic-frame transport along -e3 of (m,o_next,o_prev) of M and O at t+1 on the four seeds of the two-axis same-lock seed and reverse/face from that 2-step; displayed, not adopted"
hypothetical_axiom_status: no edit
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

Reverse probes are `A` and `B`. Face probes are `C` and `D`.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `+e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `+e_2`. Neither pair is opposite. The second pair is a
new seed, not a formed child of the first pair. This seed is not the
two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2`. This seed is not the
1-axis same-lock two-site seed `{0,(0,1,0)}` with only `+e_1/+e_1`.

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
not `UNDEFINED`. Duplicate steps collapse in the set.

Unsigned axis of a defined lock set:

```text
Axis(S) = { e_i | some ±e_i in S }.
```

Cover HOLDs iff `Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union
`Axis(O)` equals `{e_1,e_2,e_3}`. Split HOLDs iff cover HOLDs and
`|Axis(M)|=1` (hence `|Axis(O)|=2`). When split HOLDs, `m` is unique in
`M`. Let `i` in `{1,2,3}` be the axis index of `m`. `e_next = e_{i+1}`
with `3+1→1`. `e_prev = e_{i-1}` with `1−1→3`. `O_next = O ∩ {±e_next}`.
`O_prev = O ∩ {±e_prev}`. If either empty, Orient fails, not `UNDEFINED`.
Order `+e < −e`. `o_next` is the lex-largest vector in `O_next` (hence
`−e` if both signs). `o_prev` likewise. `Orient(q)` is the sign of the
integer determinant of the 3×3 matrix with columns `m`, `o_next`,
`o_prev`. If split fails, Orient fails, not `UNDEFINED`. When split
HOLDs, `F(q)=(m,o_next,o_prev)` is an oriented lattice frame.

Directed-edge HOLDs from `q` to `q+e` if and only if `q` and `q+e` are in
`B_3(0)`, both are formed at their own `τ=t+1`, split HOLDs at both,
`Orient` is `±1` at both, and the 3×3 integer matrix sending the columns of
`F(q)` to the columns of `F(q+e)` (`F(q+e)=F(q)P`) is a signed permutation
`P` with `det P = Orient(q)Orient(q+e)`. Else that edge fails, not
`UNDEFINED`. A vertex outside B_3(0) is fail, not UNDEFINED. An unformed
vertex inside `B_3(0)` makes that edge fail, not `UNDEFINED`.

Directed 2-step along `−e_3` HOLDs at `q` if and only if `q`, `q−e_3`, and
`q−2e_3` are in `B_3(0)` and directed-edge HOLDs for `(q,q−e_3)` and
`(q−e_3,q−2e_3)`. Uniqueness of P is not required.

Reverse HOLDs if and only if 2-step along `−e_3` HOLDs at both reverse
probes. Face HOLDs if and only if both face probes HOLD. Either side
`UNDEFINED` is `UNDEFINED`. Else if both sides HOLD, reverse or face HOLDs.
Else fail.

## Theorem 1 — ticks, `F`, Orient, `P` on each named edge, and 2-step bits at `τ=t+1`

On this process the four seeds form at tick 0. Frames at the four seeds:

```text
t(A)=0
t(B)=0
t(C)=0
t(D)=0
M(A, τ) = {+e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {+e_2}
O(A, τ) = {−e_2, −e_3}
O(B, τ) = {+e_2, −e_3}
O(C, τ) = {+e_1, −e_1, +e_2, +e_3}
O(D, τ) = {+e_1, −e_1, +e_3}
split(A) = hold
split(B) = hold
split(C) = fail
split(D) = hold
F(A) = (+e_1, −e_2, −e_3)
Orient((0,0,0))=+1
F(B) = (+e_1, +e_2, −e_3)
Orient((0,1,0))=-1
F(C) fail
Orient((0,0,1)) fail, not UNDEFINED
F(D) = (+e_2, +e_3, −e_1)
Orient((0,1,1))=-1
directed-edge(A, A−e_3) = hold
P(A → A−e_3) = [0 -1 0; 0 0 1; 1 0 0]
P=[0 -1 0; 0 0 1; 1 0 0]
det P(A → A−e_3) = -1
directed-edge(A−e_3, A−2e_3) = fail
P(A−e_3 → A−2e_3) = fail
two-step(A) = fail
directed-edge(B, B−e_3) = hold
P(B → B−e_3) = [0 -1 0; 0 0 1; 1 0 0]
det P(B → B−e_3) = -1
directed-edge(B−e_3, B−2e_3) = fail
P(B−e_3 → B−2e_3) = fail
two-step(B) = fail
directed-edge(C, C−e_3) = fail
P(C → C−e_3) = fail
two-step(C) = fail
directed-edge(D, D−e_3) = hold
P(D → D−e_3) = [0 1 0; 0 0 -1; -1 0 0]
P=[0 1 0; 0 0 -1; -1 0 0]
det P(D → D−e_3) = 1
directed-edge(D−e_3, D−2e_3) = hold
P(D−e_3 → D−2e_3) = [0 -1 0; 0 0 1; 1 0 0]
det P(D−e_3 → D−2e_3) = -1
two-step(D) = hold
```

The four 2-step chains are

```text
A: (0,0,0) → (0,0,−1) → (0,0,−2)
B: (0,1,0) → (0,1,−1) → (0,1,−2)
C: (0,0,1) → (0,0,0) → (0,0,−1)
D: (0,1,1) → (0,1,0) → (0,1,−1)
```

Each of those twelve vertices lies in `B_3(0)`. At `A−e_3=(0,0,−1)`,
`t=1`, `F=(−e_3,−e_1,−e_2)`, `Orient=−1`. At `B−e_3=(0,1,−1)`, `t=1`,
`F=(−e_3,−e_1,+e_2)`, `Orient=+1`. At `A−2e_3=(0,0,−2)`, `t=4`,
`M={+e_1,−e_1,+e_2}`, `O={−e_3}`, split fails from 2-in 1-out, so the
second reverse edge fails, not `UNDEFINED`. At `B−2e_3=(0,1,−2)`, `t=4`,
`M={+e_1,−e_1,−e_2}`, `O` empty, split fails, so the second reverse edge
fails, not `UNDEFINED`. First directed-edges HOLD at `A`, `B`, and `D`.
The first directed-edge at `C` fails because split fails: `O(C)` includes
the partner seed letter `+e_2`, so `Axis(M)` meets `Axis(O)`. Second
directed-edges HOLD only on the `D` chain. `det P` on each HOLDING edge
equals the product of the two Orient signs.

This is not leftover of the 1-step: directed 1-step along `−e_3` HOLDs at
`A` and at `B`, so 1-step reverse HOLDs, while this reverse fails on the
second hop. This is not leftover of the opposite-lock directed 2-step:
that member HOLDs at `C` and at `D`, so opposite-lock face HOLDs, while
this face fails because `C` split-fails. This is not leftover of `+e_3`
2-step: that member HOLDs at `B` and fails at `D`, the opposite seed of
this letter. Mixed remains a set. Occupancy of sites is not used. O is
not M.

## Theorem 2 — reverse from directed 2-step along `−e_3` at `τ`

Reverse directed 2-step cyclic-frame transport holds if and only if
2-step HOLDs at `A` and at `B`. `two-step(A)=fail` and
`two-step(B)=fail`. Reverse fails. Both sides are defined, so this is not
`UNDEFINED`. Directed 1-step reverse HOLDs on this same seed while this
reverse fails.

Reverse fails.

## Theorem 3 — face from directed 2-step along `−e_3` at `τ`

Face directed 2-step cyclic-frame transport holds if and only if 2-step
HOLDs at `C` and at `D`. `two-step(C)=fail` and `two-step(D)=hold`. Face
fails. Both sides are defined, so this is not `UNDEFINED`. Opposite-lock
directed 2-step face HOLDs on the opposite seed while this face fails.

Face fails.

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

## What this note does not claim

- It does not replace directed 2-step by a 4-cycle of the four seeds.
- It does not replace directed 2-step along `−e_3` by directed 1-step along `−e_3`.
- It does not replace this same-lock member by the opposite-lock directed 2-step along `−e_3`.
- It does not replace directed 2-step along `−e_3` by directed 2-step along `+e_3`.
- It does not replace directed 2-step along `−e_3` by directed 2-step along `±e1/±e2`.
- It does not require a unique sending matrix.
- It does not select a unique outgoing or leftover lock.
- It does not treat split fail as `UNDEFINED`.
- It does not treat a vertex outside `B_3(0)` as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not wait for a global later T.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not attach L1.

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
two-axis same-lock seed process, directed 2-step cyclic-frame transport of
`(m,o_next,o_prev)` of `M` and `O` along `−e_3` at `t+1`, and the
reverse/face bits from that 2-step are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis same-lock seed `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `0`, `0`, `0` |
| cyclic frame `F=(m,o_next,o_prev)` at `τ=t+1` | Theorem 1; LIVE three-axis at `A,B,D`; split fail at `C` |
| Orient at `τ` | Theorem 1; `+1`, `−1`, fail, `−1` |
| `P` on each named `−e_3` edge | Theorem 1; HOLD then fail on reverse; fail then HOLD on `C`; HOLD then HOLD on `D` |
| directed 2-step along `−e_3` at `τ` | Theorem 1; fail, fail, fail, hold |
| reverse from directed 2-step at `τ` | Theorem 2; `fail` |
| face from directed 2-step at `τ` | Theorem 3; `fail` |
| leftover of the 1-step along `−e_3` | not this letter; that reverse HOLDs |
| leftover of the opposite-lock directed 2-step | not this letter; that face HOLDs |
| leftover of `+e_3` 2-step | not this letter; that HOLDs at `B` and fails at `D` |
| leftover of a 4-cycle of the four seeds | not this letter |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| split fail scored as `UNDEFINED` | refused; edge fail |
| vertex outside `B_3(0)` scored as `UNDEFINED` | refused; edge fail |
| global later T | not used |
| directed 2-step as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: directed 2-step cyclic-frame transport along `−e_3` of `(m,o_next,o_prev)` of `M` and `O` at `t+1` on the four seeds of the two-axis same-lock seed, and reverse/face from that 2-step. |
| V2 | Current main has no landed directed 2-step cyclic-frame-transport reverse/face along `−e_3` of timed `M` and `O` on these four seeds of the two-axis same-lock seed. |
| V3 | Four 2-step reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads two named directed-edges along `−e_3` at the same `t+1` cut, reverse fails and face fails while 1-step reverse HOLDs, and while opposite-lock 2-step face HOLDs. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to a 4-cycle, does not reduce them to
the 1-step, does not reduce them to opposite-lock 2-step, and does not
identify this seed with the two-site same-lock seed. No global impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| 4-cycle of the four seeds | walk origin → `(0,1,0)` → `(0,1,1)` → `(0,0,1)` → origin | each scored chain is two steps of the same vector `−e_3`; endpoints are `(0,0,−2)` and `(0,1,−2)`, not a return | ATTEMPTED |
| directed 1-step along `−e_3` | reuse the first named edge only | 1-step reverse HOLDs while this reverse fails | ATTEMPTED |
| opposite-lock directed 2-step along `−e_3` | reuse opposite pairs `+e_1/−e_1` and `+e_2/−e_2` | opposite-lock face HOLDs while this face fails | ATTEMPTED |
| directed 2-step along `+e_3` | reuse the opposite z direction | HOLDs at `B` and fails at `D`, while this fails at `B` and HOLDs at `D` | ATTEMPTED |
| directed 2-step along `±e1/±e2` | reuse the same 2-step predicate | those letters do not HOLD at `D` along `−e_3` | ATTEMPTED |
| vertex outside `B_3(0)` as `UNDEFINED` | treat `(0,1,3)` as unformed | outside is fail, not UNDEFINED | ATTEMPTED |
| split fail as `UNDEFINED` | treat 2-in 1-out at `(0,0,−2)` as unformed | split fail is edge fail, not UNDEFINED | ATTEMPTED |
| global later T | wait until `max t` before reading | `τ(q)=t(q)+1` is per-seed; no global T | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the directed 2-step | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of this 2-step with the
1-step, missing identification with opposite-lock 2-step, missing
identification with a 4-cycle, and missing Record identification of the
2-step bits are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock seed pairs `+e_1/+e_1` and
`+e_2/+e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-seed `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, unique signed `m` when split HOLDs, cyclic
next/prev axes of `Axis(M)`, lex-largest signed outgoing letter under
`+e < −e`, integer determinant sign, directed-edge along a named step,
directed 2-step as two successive named edges, vertex outside `B_3(0)` as
fail not `UNDEFINED`, four seeds with reverse `{origin,(0,1,0)}` and face
`{(0,0,1),(0,1,1)}`, second pair as a new seed not a formed child, and
mixed remains a set are declared. No uniqueness of `P` and no Admissibility
rewrite are silently assumed.

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

**Steelman:** Reverse fail and face fail are only leftover of the 1-step
on this seed, or of opposite-lock 2-step, or of `+e_3` 2-step, or of a
4-cycle of the four seeds.

**Answer:** Directed 1-step reverse HOLDs while this reverse fails. Opposite-lock
directed 2-step face HOLDs while this face fails. Directed 2-step along
`+e_3` HOLDs at `B` and fails at `D`, while this fails at `B` and HOLDs at
`D`. A 4-cycle would return to the starting seed; `A` ends at `(0,0,−2)`.

### N8 — cross-cycle echo

Same-lock directed 1-step along `−e_3` on this seed reported reverse hold
and face fail. Opposite-lock directed 2-step along `−e_3` reported reverse
fail and face hold. This note is not those displays: it reports directed
2-step cyclic-frame transport along `−e_3` at `τ=t+1` on the two-axis
same-lock seed, with `two-step(A)=fail`, `two-step(B)=fail`,
`two-step(C)=fail`, `two-step(D)=hold`, reverse fail, and face fail.

**Gate disposition:** PASS for the directed 2-step cyclic-frame-transport
along `−e_3` `t+1` reverse/face reports above. FAIL / DO NOT SHIP for “the
predicate equals the 1-step,” “the predicate equals opposite-lock 2-step,”
“the predicate equals `+e_3` 2-step,” “the predicate equals a 4-cycle,”
“bits are Admissibility,” “split fail is UNDEFINED,” or “a vertex outside
`B_3(0)` is UNDEFINED.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each seed's own earliest incoming
set and own outgoing dual from the record prefix at that seed's `t+1`,
reports the cyclic frame `F=(m,o_next,o_prev)`, reports Orient as
lex-largest cyclic, reports directed-edge along `−e_3` by a
signed-permutation sending to the named neighbor with `F(q+e)=F(q)P`,
reports directed 2-step as both named edges HOLD with all three vertices
in `B_3(0)`, and checks Theorems 1--3. It also checks that reverse fails
and face fails, that all four 2-step chains stay in `B_3(0)`, that the
letter is not leftover of the 1-step, that the letter is not leftover of
the opposite-lock directed 2-step, that a vertex outside `B_3(0)` is fail
not `UNDEFINED`, and that split fail at `(0,0,−2)` is edge fail not
`UNDEFINED`. No runner cache is written.
