---
claim_id: three_axis_farface_opposite_directed_three_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Directed 3-step cyclic-frame transport along −e3 at t+1 on the three-axis far-face opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_farface_opposite_directed_three_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# Directed Three-Step Cyclic-Frame Transport Along −e3 At t+1 On The Three-Axis Far-Face Opposite Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact directed three-step bits along `−e_3` at `τ=t+1` on the
three-axis far-face opposite seed in Euclidean `B_3(0)`, together with reverse
and face from those bits.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_farface_opposite_directed_three_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_farface_opposite_directed_three_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

## Result up front

On the three-axis far-face opposite seed, cyclic-frame transport along a named
edge is the signed-permutation map of the ordered triple `F=(m,o_next,o_prev)`.
This note displays the *directed* three-step along `−e_3` from each of the four
probes. It is the opposite named direction from `+e_3`. Not leftover of +e3.
Not leftover of 2-step. The third pair is a new seed, not a formed child. First
display: three hops along `−e_3` on the far-face seed.

At the common cut `τ=t+1` of each seed (`t=0`, so `τ=1`), origin split fails,
so the origin first hop fails and the origin three-step fails. The remaining
reverse probe HOLDs its first hop, fails its second hop because the second
dest is unformed in `B_3(0)`, and has third dest `(0,1,-3)` outside `B_3(0)`:
fail not UNDEFINED. Face probe `(0,0,1)` fails its first hop (dest is origin).
Face probe `(0,1,1)` HOLDs its first two hops and fails its third hop because
`(0,1,-2)` is unformed in `B_3(0)`. Therefore

```text
reverse: fail
face: fail
```

The bits are Displayed, not adopted. Do not write into Admissibility. Do not
attach L1. Uniqueness is not required.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact 3-step bits on Euclidean B_3(0) at one declared cut; the bits are displayed and not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_farface_opposite_directed_three_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
target_blocker_text: "display directed 3-step cyclic-frame transport along -e3 at t+1 on the three-axis far-face opposite seed and the reverse/face pair from those bits"
source_of_blocker_text: frontier_question
reachability_to_target: closed_finite_target
artifact_role: theorem
next_trace_action: "independent audit of the landed note and invocation-bound runner evidence"
conditional_surface_status: "exact only for the declared three-axis far-face opposite seed, Euclidean B_3(0), and the named -e3 three-step at t+1"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise boundary

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Admissibility does not supply the formation site, probability, or rate. The
perp-step incoming-lock process used below is a declared finite host process,
not an axiom edit.

## Exact objects

Euclidean B_3(0)={n:n·n<=9} inside `Z^3`. No larger ball is used. Nearest
neighbors are the six axial steps `{±e_1,±e_2,±e_3}` with
`e_1=(1,0,0)`, `e_2=(0,1,0)`, `e_3=(0,0,1)`.

Seed at tick `0`, two disjoint opposite pairs plus far-face third pair:

```text
(0,0,0) locks +e_1
(0,1,0) locks -e_1
(0,0,1) locks +e_2
(0,1,1) locks -e_2
(0,0,-1) locks +e_3
(0,1,-1) locks -e_3
```

The third pair is a new seed, not a formed child.

From a recorded site `p` with unique lock `L(p)=±e_i`, a step `s` to
`q=p+s` is allowed iff `s·e_i=0`. If `q` lies in `B_3(0)` and is unformed,
`q` forms at `t(p)+1` and the incoming set `M(q)` is the set of earliest such
steps. If that set is not a singleton, `q` has no unique lock and does not
emit. Seed incoming sets are the assigned locks.

Let `t(q)` be the formation tick. The cut is `τ=t+1`. For each seed probe,
`t=0` so `τ=1`. A site is formed at `τ` iff it is recorded with tick `≤ τ`.
Unformed at `τ` is fail, not UNDEFINED. A vertex outside `B_3(0)` is fail, not
UNDEFINED.

`M(q,τ)` is the earliest incoming set of `q` from records with tick `≤ τ`,
defined only if `q` is formed at `τ`.

`O(q,τ)={e in {±e_1,±e_2,±e_3} | q+e formed at τ and e in M(q+e,τ)}`.

`Axis(S)={e_i | some ±e_i in S}`. Cover holds iff `Axis(M)∩Axis(O)` is empty
and `Axis(M)∪Axis(O)={e_1,e_2,e_3}`. Split holds iff cover holds and
`|Axis(M)|=1` with `m` unique in `M`. Two-in one-out is fail. If split fails,
Orient fails, not UNDEFINED.

When split holds, let `i` be the axis index of `m`. Set `e_next=e_{i+1}` with
`3+1→1` and `e_prev=e_{i-1}` with `1-1→3`. Let
`O_next=O∩{±e_next}` and `O_prev=O∩{±e_prev}`. If either is empty, Orient
fails, not UNDEFINED. Order `+e < -e`. Then `o_next` is the lex-largest
vector in `O_next` (hence `-e` if both signs), and `o_prev` likewise.
`F(q)` is the `3×3` integer matrix with columns `(m,o_next,o_prev)`.
`Orient(q)` is the sign of `det F(q)`. Split plus nonempty leftover axes
makes `Orient∈{±1}` and makes `F` a signed permutation matrix.

Directed-edge HOLD from `q` to `q−e_3` iff `q` and `q−e_3` lie in `B_3(0)`,
both are formed at `τ`, split holds at both, Orient is `±1` at both, and the
`3×3` integer matrix `P` sending columns of `F(q)` to columns of `F(q−e_3)`
(the `P` with `P F(q)=F(q−e_3)`) is a signed permutation with
`det P=Orient(q)Orient(q−e_3)`. Else that edge fails, not UNDEFINED.

Directed 3-step along `−e_3` HOLDs at `q` iff `q`, `q−e_3`, `q−2e_3`, and
`q−3e_3` lie in `B_3(0)` and the three named edges `(q,q−e_3)`,
`(q−e_3,q−2e_3)`, and `(q−2e_3,q−3e_3)` HOLD.

Reverse probes: origin and `(0,1,0)`. Face probes: `(0,0,1)` and `(0,1,1)`.
Reverse HOLD iff 3-step along `−e_3` HOLDs at both reverse probes. Face HOLD
iff both face probes HOLD.

## Theorem 1

At `τ=1` the six seeds are formed at tick `0`. The tick-1 records in
`B_3(0)` are exactly twenty sites: the six seeds together with

```text
(0,-1,0)   M={-e_2}
(0,2,0)    M={+e_2}
(1,0,1)    M={+e_1}
(-1,0,1)   M={-e_1}
(0,0,2)    M={+e_3}
(1,1,1)    M={+e_1}
(-1,1,1)   M={-e_1}
(0,1,2)    M={+e_3}
(1,0,-1)   M={+e_1}
(-1,0,-1)  M={-e_1}
(0,-1,-1)  M={-e_2}
(1,1,-1)   M={+e_1}
(-1,1,-1)  M={-e_1}
(0,2,-1)   M={+e_2}
```

Frames at the four probes and the two far-face dest seeds:

```text
F((0,0,0)) fails
  M={+e_1}, O={-e_2}; Axis(M)={e_1}, Axis(O)={e_2}; split fails
F((0,1,0)) columns (-e_1,+e_2,-e_3); Orient((0,1,0))=+1
F((0,0,1)) columns (+e_2,+e_3,-e_1); Orient((0,0,1))=-1
F((0,1,1)) columns (-e_2,+e_3,-e_1); Orient((0,1,1))=+1
F((0,0,-1)) columns (+e_3,-e_1,-e_2); Orient((0,0,-1))=+1
F((0,1,-1)) columns (-e_3,-e_1,+e_2); Orient((0,1,-1))=+1
```

Origin split fails because the far-face seed at `(0,0,-1)` locks `+e_3`, so
the step `−e_3` from origin is not in `M((0,0,-1))` and is not in origin
`O`. The twelve named `−e_3` edges of the four three-hop chains and the four
three-step bits:

```text
(0,0,0)->(0,0,-1)
  dest t=0; F dest columns (+e_3,-e_1,-e_2); Orient dest=+1
  src split fail; edge fail
(0,0,-1)->(0,0,-2)
  dest unformed at τ=1; (0,0,-2) in B_3(0); P fail; edge fail
(0,0,-2)->(0,0,-3)
  src unformed at τ=1; dest unformed at τ=1; (0,0,-3) in B_3(0); P fail; edge fail
  3-step at (0,0,0): fail

(0,1,0)->(0,1,-1)
  dest t=0; F dest columns (-e_3,-e_1,+e_2); Orient dest=+1
  P=[(0,-1,0); (0,0,-1); (1,0,0)]; det P=+1; edge hold
(0,1,-1)->(0,1,-2)
  dest unformed at τ=1; (0,1,-2) in B_3(0); P fail; edge fail
(0,1,-2)->(0,1,-3)
  dest (0,1,-3) has n·n=10 and is outside B_3(0); P fail; edge fail
  3-step at (0,1,0): fail

(0,0,1)->(0,0,0)
  dest t=0; F dest fails
  dest split fail; edge fail
(0,0,0)->(0,0,-1)
  src split fail; edge fail
(0,0,-1)->(0,0,-2)
  dest unformed at τ=1; (0,0,-2) in B_3(0); P fail; edge fail
  3-step at (0,0,1): fail

(0,1,1)->(0,1,0)
  dest t=0; F dest columns (-e_1,+e_2,-e_3); Orient dest=+1
  P=[(0,1,0); (0,0,1); (1,0,0)]; det P=+1; edge hold
(0,1,0)->(0,1,-1)
  dest t=0; F dest columns (-e_3,-e_1,+e_2); Orient dest=+1
  P=[(0,-1,0); (0,0,-1); (1,0,0)]; det P=+1; edge hold
(0,1,-1)->(0,1,-2)
  dest unformed at τ=1; (0,1,-2) in B_3(0); P fail; edge fail
  3-step at (0,1,1): fail
```

All listed vertices of the four chains except `(0,1,-3)` lie in `B_3(0)`.
The vertex `(0,1,-3)` has `n·n=10` and is outside; that hop is fail not
UNDEFINED. Unformed dests inside the ball are fail not UNDEFINED. On each
HOLDING edge, `det P` equals the product of the two Orient signs. At the same
cut, the named `+e_3` three-step fails at origin, fails at `(0,1,0)`, fails at
`(0,0,1)`, and fails at `(0,1,1)`. The named `−e_3` hops
`(0,1,0)->(0,1,-1)` and `(0,1,1)->(0,1,0)` HOLD, so the displayed `−e_3`
object is not leftover of +e3. The two-step along `−e_3` at `(0,1,1)` HOLDs
while the three-step fails, so the three-step is not leftover of 2-step.

## Theorem 2

Reverse probes are origin and `(0,1,0)`. Both three-step bits fail, neither is
UNDEFINED, so reverse: fail.

## Theorem 3

Face probes are `(0,0,1)` and `(0,1,1)`. Both three-step bits fail, neither is
UNDEFINED, so face: fail. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.

## What this does not show

The packet does not select a physical Record readout, a formation law, a
holonomy identity, or a 4-cycle. It does not write the displayed bits into
Admissibility. It does not attach L1. It does not enlarge Euclidean `B_3(0)`.
It does not claim uniqueness of `F` among other frame conventions. Not leftover of +e3.
Not leftover of 2-step.
It does not treat the far-face third pair as a formed child of the first pair.
It does not adopt reverse or face.
