---
claim_id: two_axis_same_lock_directed_three_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Directed 3-step cyclic-frame transport along −e3 at t+1 on the two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_directed_three_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# Directed Three-Step Cyclic-Frame Transport Along −e3 At t+1 On The Two-Axis Same-Lock Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact directed three-step bits along `−e_3` at `τ=t+1` on the
two-axis same-lock seed in Euclidean `B_3(0)`, together with reverse and face
from those bits.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_directed_three_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_directed_three_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

## Result up front

On the two-axis same-lock seed, cyclic-frame transport along a named edge is
the signed-permutation map of the ordered triple `F=(m,o_next,o_prev)`. This
note displays the *directed* three-step along `−e_3` from each of the four
seed sites. It is three hops, not one and not two. Not leftover of 1-step or 2-step.
It is not leftover of the opposite-lock directed three-step along `−e_3`.

At each site's own cut `τ=t+1` every three-step bit fails: the reverse chains
fail on the second hop, `B−3e_3` lies outside `B_3(0)`, the first face hop
fails from split, and the third hop of `(0,1,1)` fails. Therefore

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
claim_type_reason: "Finite exact 3-step bits on Euclidean B_3(0) at each site's own t+1; the bits are displayed and not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_directed_three_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
target_blocker_text: "display directed 3-step cyclic-frame transport along -e3 at t+1 on the two-axis same-lock seed and the reverse/face pair from those bits"
source_of_blocker_text: frontier_question
reachability_to_target: closed_finite_target
artifact_role: theorem
next_trace_action: "independent audit of the landed note and invocation-bound runner evidence"
conditional_surface_status: "exact only for the declared two-axis same-lock seed, Euclidean B_3(0), and the named -e3 three-step at t+1"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premise boundary

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

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

Seed at tick `0`, two disjoint same-lock pairs:

```text
(0,0,0) locks +e_1
(0,1,0) locks +e_1
(0,0,1) locks +e_2
(0,1,1) locks +e_2
```

Neither pair is opposite. The second pair is a new seed, not a formed child of
the first pair.

From a recorded site `p` with unique lock `L(p)=±e_i`, a step `s` to
`q=p+s` is allowed iff `s·e_i=0`. If `q` lies in `B_3(0)` and is unformed,
`q` forms at `t(p)+1` and the incoming set `M(q)` is the set of earliest such
steps. If that set is not a singleton, `q` has no unique lock and does not
emit. Seed incoming sets are the assigned locks.

Let `t(q)` be the formation tick. The cut is `τ=t+1` at each site: there is
no global T. A site is formed at a cut `τ` iff it is recorded with tick
`≤ τ`. Unformed at `τ` is fail, not UNDEFINED. A vertex outside B_3(0) is fail, not UNDEFINED.

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

Directed-edge HOLD from `q` to `q+e` iff `q` and `q+e` lie in `B_3(0)`, both
are formed at each site's own `τ=t+1`, split holds at both, Orient is `±1`
at both, and the unique `3×3` integer matrix `P` sending columns of `F(q)` to
columns of `F(q+e)` (the unique `P` with `P F(q)=F(q+e)`) is a signed
permutation with `det P=Orient(q)Orient(q+e)`. Else that edge fails, not
UNDEFINED.

Directed 3-step along `−e_3` HOLDs at `q` iff `q`, `q−e_3`, `q−2e_3`, and
`q−3e_3` lie in `B_3(0)` and the three named edges `(q,q−e_3)`,
`(q−e_3,q−2e_3)`, and `(q−2e_3,q−3e_3)` HOLD.

Reverse probes: origin and `(0,1,0)`. Face probes: `(0,0,1)` and `(0,1,1)`.
Reverse HOLD iff 3-step along `−e_3` HOLDs at both reverse probes. Face HOLD
iff both face probes HOLD.

## Theorem 1

At `τ=t+1` the four seeds are formed at tick `0`. Frames at the four seeds:

```text
F((0,0,0)) columns (+e_1,-e_2,-e_3); Orient((0,0,0))=+1
F((0,1,0)) columns (+e_1,+e_2,-e_3); Orient((0,1,0))=-1
F((0,0,1)) split fail; Orient((0,0,1)) fail, not UNDEFINED
F((0,1,1)) columns (+e_2,+e_3,-e_1); Orient((0,1,1))=-1
```

The twelve named `−e_3` hops and the four three-step bits:

```text
(0,0,0)->(0,0,-1)
  dest t=1; F dest columns (-e_3,-e_1,-e_2); Orient dest=-1
  P=[0 1 0; 0 0 1; -1 0 0]; det P=-1; edge hold
(0,0,-1)->(0,0,-2)
  dest t=4; M={+e_1,-e_1}; O empty; split fail; P fail; edge fail
(0,0,-2)->(0,0,-3)
  dest in B_3(0) and unformed; P fail; edge fail
  3-step at (0,0,0): fail

(0,1,0)->(0,1,-1)
  dest t=1; F dest columns (-e_3,-e_1,+e_2); Orient dest=+1
  P=[0 -1 0; 0 0 -1; -1 0 0]; det P=-1; edge hold
(0,1,-1)->(0,1,-2)
  dest t=4; M={+e_1,-e_1}; O empty; split fail; P fail; edge fail
(0,1,-2)->(0,1,-3)
  dest outside B_3(0); P fail; edge fail
  3-step at (0,1,0): fail

(0,0,1)->(0,0,0)
  dest t=0; F dest as origin; Orient dest=+1
  src split fail; Orient src fail, not UNDEFINED; P fail; edge fail
(0,0,0)->(0,0,-1)
  dest t=1; P=[0 1 0; 0 0 1; -1 0 0]; det P=-1; edge hold
(0,0,-1)->(0,0,-2)
  dest t=4; split fail; P fail; edge fail
  3-step at (0,0,1): fail

(0,1,1)->(0,1,0)
  dest t=0; F dest as (0,1,0); Orient dest=-1
  P=[0 1 0; 0 0 1; 1 0 0]; det P=+1; edge hold
(0,1,0)->(0,1,-1)
  dest t=1; P=[0 -1 0; 0 0 -1; -1 0 0]; det P=-1; edge hold
(0,1,-1)->(0,1,-2)
  dest t=4; split fail; P fail; edge fail
  3-step at (0,1,1): fail
```

Each `det P` on a HOLDING edge equals the product of the two Orient signs.
Vertex `(0,1,-3)` lies outside `B_3(0)` and is fail, not UNDEFINED. Vertex
`(0,0,-3)` lies in `B_3(0)` and is unformed, so that edge fails, not
UNDEFINED. Split fails at `(0,0,1)` because `O` includes the partner seed
letter `+e_2`, so `Axis(M)` meets `Axis(O)`. This is three hops, not leftover
of 1-step or 2-step: 1-step reverse HOLDs, 2-step at `(0,1,1)` HOLDs, while
every 3-step bit fails. This is not leftover of the opposite-lock directed
three-step along `−e_3`: that member HOLDs the first two face hops, while this
first face hop fails from split.

## Theorem 2

Reverse probes are origin and `(0,1,0)`. Both three-step bits fail, neither
is UNDEFINED, so reverse: fail.

## Theorem 3

Face probes are `(0,0,1)` and `(0,1,1)`. Both three-step bits fail, neither
is UNDEFINED, so face: fail. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.

## What this does not show

The packet does not select a physical Record readout, a formation law, or a
4-cycle. It does not write the displayed bits into Admissibility. It does
not attach L1. It does not enlarge Euclidean `B_3(0)`. It does not claim
uniqueness of `F` among other frame conventions. It does not replace the
three-step by the one-step or by the two-step product along `−e_3`. It does
not replace this same-lock member by the opposite-lock directed three-step
along `−e_3`.
