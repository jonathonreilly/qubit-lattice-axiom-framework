---
claim_id: two_axis_opposite_directed_two_step_minus_e2_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Directed 2-step cyclic-frame transport along −e2 at t+1 on the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_directed_two_step_minus_e2_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# Directed 2-Step Cyclic-Frame Transport Along −e2 At t+1 Reverse And Face On The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** directed 2-step cyclic-frame transport along −e_2 of simultaneous
earliest incoming set `M` and outgoing dual `O` at each seed's `τ=t+1`,
and reverse/face from that 2-step, on the four seeds of the two-axis
opposite seed in `B_3(0)={n:n·n<=9}`. `F`, Orient, directed-edge as
nm2frm2sx with step −e_2. HOLDING cyclic-frame transport #7490 is
existential (some 6-NN). First display: the named in-plane direction
−e_2 twice from each of the four seeds (all four 2-step chains stay in
`B_3`). Not a 4-cycle. Not leftover of 10→+e1. Uniqueness is not
required. Mixed remains a set. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_directed_two_step_minus_e2_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_directed_two_step_minus_e2_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named seeds. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-site cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Split is cover together with `|Axis(M)|=1`. The cyclic next/prev
lex-largest oriented frame is the integer sign of
`det(m,o_next,o_prev)` with unique signed incoming letter `m` and the
lex-largest signed outgoing letter on the cyclic next and prev axes of
`Axis(M)` under `+e < −e`. When split HOLDs, `F=(m,o_next,o_prev)` is
that LIVE three-axis frame. Directed-edge HOLD from `q` to `q−e_2` if and
only if both sites are in `B_3(0)`, both formed at `τ`, split HOLDs at
both, Orient is `±1` at both, and the unique 3×3 integer matrix sending
the columns of `F(q)` to the columns of `F(q−e_2)` is a signed permutation
`P` with `det P = Orient(q)Orient(q−e_2)`. Else that edge fails, not
`UNDEFINED`. Directed 2-step along −e_2 HOLDs at `q` if and only if `q`,
`q−e_2`, and `q−2e_2` are in `B_3(0)` and both named directed edges HOLD.
A vertex outside `B_3(0)` is fail, not `UNDEFINED`. Reverse HOLDs if and
only if 2-step HOLDs at origin and at `(0,1,0)`. Face HOLDs if and only if
2-step HOLDs at `(0,0,1)` and at `(0,1,1)`. Occupancy of sites is not used.
A six-neighbor star is not the letter.

Quoted axiom sentences used as input:

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

When present, a record locks exactly one admissible local possibility.

Content is conditional on formation at that site; it does not supply the formation site, probability, or rate.

Records form.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of directed 2-step cyclic-frame transport along -e2 at t+1 on the four seeds of the two-axis opposite seed, P on each named edge, 2-step bits, reverse fail and face fail; uniqueness is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_directed_two_step_minus_e2_cyclic_frame_transport_tplus1_reverse_face
target_blocker_text: "display directed 2-step cyclic-frame transport along -e2 reverse/face on the four seeds of the two-axis opposite seed, not a 4-cycle, not leftover of 10 to +e1, not existential 6-NN transport"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep directed 2-step cyclic-frame transport along -e2 of F at t+1 displayed; do not write the bits into Admissibility, do not reduce to a 4-cycle, do not reduce to leftover of 10 to +e1, do not reduce to existential 6-NN transport, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for directed 2-step cyclic-frame transport along -e2 at t+1 on the two-axis opposite seed and reverse/face from that; displayed, not adopted"
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
2-step along −e_2 is scored as reverse/face probes:

```text
A = (0,0,0),  B = (0,1,0),  C = (0,0,1),  D = (0,1,1).
```

`A` and `B` are the reverse probes. `C` and `D` are the face probes. These
are the four seeds of the two-axis opposite process, not the z-probes
`A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`, `D=(1,0,1)`.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. The second pair is a new seed, not a formed
child of the first pair.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s·e_i=0
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept. A later
parent does not re-form `q`. Uniqueness is not required. Mixed remains a set.

## Named directed 2-step along −e_2 at `τ=t+1`

Let `t(q)` be the formation tick of seed `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter.

`O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Empty `O` is empty, not `UNDEFINED`.

When split HOLDs, `F(q)=(m,o_next,o_prev)` and `Orient(q)` is the sign of
`det(m,o_next,o_prev)`, as nm2oricyclz (lex-largest cyclic). `F`, Orient,
and directed-edge are as nm2frm2sx with step −e_2.

Directed-edge HOLD from `q` to `q−e_2` if and only if `q` and `q−e_2` are
in `B_3(0)`, both formed at `τ`, split HOLDs at both, Orient `±1` at both,
and the unique 3×3 integer matrix sending columns of `F(q)` to columns of
`F(q−e_2)` is a signed permutation `P` with `det P = Orient(q)Orient(q−e_2)`.
Else that edge fails, not `UNDEFINED`. A vertex outside `B_3(0)` is fail,
not `UNDEFINED`.

Directed 2-step along −e_2 HOLDs at `q` if and only if `q`, `q−e_2`, and
`q−2e_2` are in `B_3(0)` and directed-edge HOLDs for `(q,q−e_2)` and
`(q−e_2,q−2e_2)`. All four 2-step chains stay in `B_3`. Not a 4-cycle.
Not leftover of 10 to +e_1. HOLDING cyclic-frame transport #7490 is
existential (some 6-NN) and is a different object: this letter names the
in-plane direction −e_2 twice.

Reverse HOLD iff 2-step along −e_2 HOLDs at both reverse probes. Face HOLD
iff both face probes HOLD.

## Theorem 1 — ticks, `F`, Orient, `P` on each named edge, 2-step bits

On this process the four seeds form at tick 0. Each named chain is two
steps of −e_2 and remains in `B_3(0)`:

```text
A: (0,0,0) → (0,-1,0) → (0,-2,0)
B: (0,1,0) → (0,0,0) → (0,-1,0)
C: (0,0,1) → (0,-1,1) → (0,-2,1)
D: (0,1,1) → (0,0,1) → (0,-1,1)
```

```text
t(A)=0
t(B)=0
t(C)=0
t(D)=0
F(A) = (+e_1, −e_2, −e_3)
F(B) = (−e_1, +e_2, −e_3)
F(C) = (+e_2, +e_3, −e_1)
F(D) = (−e_2, +e_3, −e_1)
Orient(A) = +1
Orient(B) = +1
Orient(C) = −1
Orient(D) = +1
edge(A→mid) = hold
P(A→mid) = [0 0 -1; 1 0 0; 0 1 0]
edge(A→end) = fail
P(A→end) = fail
edge(B→mid) = hold
P(B→mid) = [-1 0 0; 0 -1 0; 0 0 1]
edge(B→end) = hold
P(B→end) = [0 0 -1; 1 0 0; 0 1 0]
edge(C→mid) = fail
P(C→mid) = fail
edge(C→end) = fail
P(C→end) = fail
edge(D→mid) = hold
P(D→mid) = [-1 0 0; 0 1 0; 0 0 1]
edge(D→end) = fail
P(D→end) = fail
two_step(A) = fail
two_step(B) = hold
two_step(C) = fail
two_step(D) = fail
```

`A` is the origin seed at tick 0 with seed letter `+e_1`. `B` is the
`(0,1,0)` seed with letter `−e_1`. `C` is the `(0,0,1)` seed with letter
`+e_2`. `D` is the `(0,1,1)` seed with letter `−e_2`. The second pair is a
new seed, not a formed child. Mid of `A` is `(0,-1,0)` at tick 1 with
split HOLD and Orient `−1`. End of `A` is `(0,-2,0)` at tick 4 with split
fail, so the second edge fails and 2-step at `A` fails. Both edges of `B`
HOLD, so 2-step at `B` HOLDs. Mid of `C` is `(0,-1,1)` at tick 2 with split
fail, so the first edge fails and 2-step at `C` fails. End of `D` is
`(0,-1,1)` with split fail, so the second edge fails and 2-step at `D`
fails. Uniqueness of `P` as a matrix is the unique integer sending of
columns of a LIVE frame; uniqueness of a neighbor is not required. This
is not leftover of 10 to +e_1: 2-step along +e_1 fails at each of the four
seeds, including at `B` where 2-step along −e_2 HOLDs. Cover and split do
not score handedness. O is not M.

## Theorem 2 — reverse from directed 2-step along −e_2 at `τ`

Reverse directed 2-step along −e_2 holds if and only if 2-step HOLDs at
`A` and at `B`. `two_step(A)=fail` and `two_step(B)=hold`. Reverse fails.
Both sides are defined, so this is not `UNDEFINED`.

Reverse directed 2-step along −e_2 at τ: fail

This is not leftover of 10 to +e_1: that reverse also fails, but 2-step
along +e_1 fails at `B` while 2-step along −e_2 HOLDs at `B`. This is not
a 4-cycle: the named chain is two steps of −e_2, not a return around a
unit square. HOLDING cyclic-frame transport #7490 is existential some
6-NN and is not this named direction.

Reverse fails.

## Theorem 3 — face from directed 2-step along −e_2 at `τ`

Face directed 2-step along −e_2 holds if and only if 2-step HOLDs at `C`
and at `D`. `two_step(C)=fail` and `two_step(D)=fail`. Face fails. Both
sides are defined, so this is not `UNDEFINED`.

Face directed 2-step along −e_2 at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Face fails.

## What this note does not claim

- It does not replace named directed 2-step along −e_2 by existential
  6-NN cyclic-frame transport.
- It does not replace the letter by a 4-cycle holonomy.
- It does not reprint leftover of 10 to +e_1 as this −e_2 2-step.
- It does not require a unique formed six-neighbor witness.
- It does not select a unique outgoing or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not use occupancy of sites.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not write the bits into Admissibility.

## Current premise boundary

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
2-step `fail`/`hold` reports do not close that residual.

## Exact target and obligation graph

| Obligation | Source |
|---|---|
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; all `0` |
| cyclic frame `F` and Orient at `τ` | Theorem 1 |
| `P` on each named −e_2 edge | Theorem 1 |
| 2-step bits at the four seeds | Theorem 1; fail, hold, fail, fail |
| reverse from 2-step at `τ` | Theorem 2; `fail` |
| face from 2-step at `τ` | Theorem 3; `fail` |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: directed 2-step cyclic-frame transport along −e_2 at `t+1` from each of the four seeds of the two-axis opposite seed, and reverse/face from that. |
| V2 | Current main has no landed directed 2-step along −e_2 reverse/face of timed `F` on these four seeds. |
| V3 | Four 2-step reports and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads two named directed edges of the cyclic frame along −e_2 at the same `t+1` cut; 2-step HOLDs only at `B` while leftover of 10 to +e_1 fails at `B`. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to a 4-cycle, does not reduce them to
leftover of 10 to +e_1, does not reduce them to existential 6-NN
transport, and does not attach L1. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover of 10 to +e_1 | reuse directed 2-step along +e_1 | 2-step along +e_1 fails at each seed, including at `B` where 2-step along −e_2 HOLDs | ATTEMPTED |
| 4-cycle holonomy | reuse a unit-square product of four sendings | the named chain is two steps of −e_2 and does not return | ATTEMPTED |
| existential 6-NN transport #7490 | reuse some formed 6-NN sending | this letter names the in-plane direction −e_2 twice, not an existential neighbor | ATTEMPTED |
| z-probe transport | score A,B,C,D as nm2cycfrmz z-probes | reverse probes here are origin and `(0,1,0)`, the four seeds | ATTEMPTED |
| unique nonnegative sending | require a unique sending with no minus signs | uniqueness is not required; `P(A→mid)` has a minus sign | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover is a different unsigned object | ATTEMPTED |
| 1-axis opposite two-site seed | reuse only `+e_1/−e_1` | the second pair is a new seed, not a formed child | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | this display scores named directed edges of `F` along −e_2 at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` | different process | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until a common later tick | `τ(q)=t(q)+1` is per-site; no global T | ATTEMPTED |
| attach L1 | form the probes by a neighbor-lock letter | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the 2-step bits | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of this 2-step with
leftover of 10 to +e_1, missing identification with a 4-cycle, and missing
identification with existential 6-NN transport are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite seed pairs `+e_1/−e_1` and
`+e_2/−e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-site `τ=t+1`,
cyclic lex-largest frame, directed-edge along −e_2, two-step of that edge,
outside-host fail not `UNDEFINED`, four seed probes, second pair as a new
seed not a formed child, and mixed remains a set are declared. No
uniqueness of outgoing locks, no occupancy, no six-neighbor star as the
scored object, no lock-count clock, no global later T, no formation
attachment from already-recorded six-neighbor locks, and no Admissibility
rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
2-step reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | directed 2-step of `F=(m,o_next,o_prev)` along −e_2 with signed-permutation `P` on each named edge | no continuum alphabet |
| per site | four seeds on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four 2-step reports, reverse/face from 2-step at paired seeds | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for directed 2-step
reverse/face, a formation-rate rule, and a physical selector among named
in-plane directions. None is taken here.

### N7 — hostile steelman

**Steelman:** Reverse fail and face fail are only leftover of 10 to +e_1,
or only a 4-cycle that does not close, or only existential 6-NN transport
failing at the same seeds; the second pair is only the formed child of the
1-axis seed.

**Answer:** 2-step along +e_1 fails at `B` while 2-step along −e_2 HOLDs at
`B`, so leftover of 10 to +e_1 is a different letter. The named chain is
two steps of −e_2 and does not return, so it is not a 4-cycle. HOLDING
cyclic-frame transport #7490 is existential some 6-NN; this letter names
the in-plane direction −e_2 twice. The second pair is a new seed, not a
formed child: `(0,0,1)` is recorded at tick 0 with lock `+e_2`.

### N8 — cross-cycle echo

nm2cycfrmz cyclic-frame transport on the four z-probes of this seed
reported transport HOLD at each z-probe, reverse hold, and face hold from
an existential 6-NN sending. This note is not that display: it reports
directed 2-step along −e_2 from the four seeds, with `t(A)=t(B)=t(C)=t(D)=0`,
`two_step(A)=fail`, `two_step(B)=hold`, `two_step(C)=fail`,
`two_step(D)=fail`, reverse fail, and face fail. Cover and split do not
score handedness. Not leftover of 10 to +e_1. Not a 4-cycle.

**Gate disposition:** PASS for the directed 2-step along −e_2 `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
leftover of 10 to +e_1,” “the predicate equals a 4-cycle,” “the predicate
equals existential 6-NN transport,” “the predicate equals the 1-axis
opposite two-site seed,” “bits are Admissibility,” or “outside `B_3(0)` is
UNDEFINED.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each seed's own earliest incoming
set and own outgoing dual from the record prefix at that seed's `t+1`,
reports the cyclic frame `F=(m,o_next,o_prev)`, reports Orient as
nm2oricyclz lex-largest cyclic, reports directed-edge `P` along −e_2,
reports 2-step along −e_2 at each of the four seeds, and checks Theorems
1--3. It also checks that 2-step HOLDs only at `B`, that reverse fails and
face fails, that leftover of 10 to +e_1 fails at `B`, that a vertex
outside `B_3(0)` is fail not `UNDEFINED`, that the second pair is a new
seed not a formed child, that the construction is not a 4-cycle, that a
formation member from already-recorded six-neighbor locks is not attached,
and that the display is not the two-tick lock-count clock composition.
No runner cache is written.
