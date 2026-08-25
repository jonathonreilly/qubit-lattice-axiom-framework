---
claim_id: two_axis_opposite_directed_two_step_minus_e1_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Directed 2-step cyclic-frame transport along -e1 at t+1 on the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_directed_two_step_minus_e1_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# Directed Two-Step Cyclic-Frame Transport Along -e1 At t+1

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact directed two-step bits along `-e_1` at `τ=t+1` on the
two-axis opposite seed in Euclidean `B_3(0)`, together with reverse and face
from those bits.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_directed_two_step_minus_e1_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_directed_two_step_minus_e1_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

## Result up front

On the two-axis opposite seed, cyclic-frame transport along a named edge is
the signed-permutation map of the ordered triple `F=(m,o_next,o_prev)`. This
note displays the *directed* two-step along `-e_1` twice from each of the four
seed sites (into the occupied half). It is not leftover of the +e1 product.
It is not a 4-cycle.

At the common cut `τ=t+1` of each seed (`t=0`, so `τ=1`), every named
`-e_1` edge fails, so every two-step bit fails. Therefore

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
claim_type_reason: "Finite exact 2-step bits on Euclidean B_3(0) at one declared cut; the bits are displayed and not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_directed_two_step_minus_e1_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
target_blocker_text: "display directed 2-step cyclic-frame transport along -e1 at t+1 and the reverse/face pair from those bits"
source_of_blocker_text: frontier_question
reachability_to_target: closed_finite_target
artifact_role: theorem
next_trace_action: "independent audit of the landed note and invocation-bound runner evidence"
conditional_surface_status: "exact only for the declared two-axis opposite seed, Euclidean B_3(0), and the named -e1 two-step at t+1"
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

Seed at tick `0`, two disjoint opposite pairs:

```text
(0,0,0) locks +e_1
(0,1,0) locks -e_1
(0,0,1) locks +e_2
(0,1,1) locks -e_2
```

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

Directed-edge HOLD from `q` to `q+e` iff `q` and `q+e` lie in `B_3(0)`, both
are formed at `τ`, split holds at both, Orient is `±1` at both, and the unique
`3×3` integer matrix `P` sending columns of `F(q)` to columns of `F(q+e)`
(the unique `P` with `P F(q)=F(q+e)`) is a signed permutation with
`det P=Orient(q)Orient(q+e)`. Else that edge fails, not UNDEFINED.

Directed 2-step along `-e_1` HOLDs at `q` iff `q`, `q-e_1`, and `q-2e_1` lie
in `B_3(0)` and both named edges `(q,q-e_1)` and `(q-e_1,q-2e_1)` HOLD.

Reverse probes: origin and `(0,1,0)`. Face probes: `(0,0,1)` and `(0,1,1)`.
Reverse HOLD iff 2-step along `-e_1` HOLDs at both reverse probes. Face HOLD
iff both face probes HOLD.

## Theorem 1

At `τ=1` the four seeds are formed at tick `0`. The tick-1 records in
`B_3(0)` are exactly fourteen sites: the four seeds together with

```text
(0,-1,0)  M={-e_2}
(0,0,-1)  M={-e_3}
(0,2,0)   M={+e_2}
(0,1,-1)  M={-e_3}
(1,0,1)   M={+e_1}
(-1,0,1)  M={-e_1}
(0,0,2)   M={+e_3}
(1,1,1)   M={+e_1}
(-1,1,1)  M={-e_1}
(0,1,2)   M={+e_3}
```

Frames at the four seeds:

```text
F((0,0,0)) columns (+e_1,-e_2,-e_3); Orient((0,0,0))=+1
F((0,1,0)) columns (-e_1,+e_2,-e_3); Orient((0,1,0))=+1
F((0,0,1)) columns (+e_2,+e_3,-e_1); Orient((0,0,1))=-1
F((0,1,1)) columns (-e_2,+e_3,-e_1); Orient((0,1,1))=+1
```

The eight named `-e_1` edges and the four two-step bits:

```text
(0,0,0)->(-1,0,0)  (-1,0,0) unformed at τ=1; P fail; edge fail
(-1,0,0)->(-2,0,0)  both unformed at τ=1; P fail; edge fail
2-step at (0,0,0): fail

(0,1,0)->(-1,1,0)  (-1,1,0) unformed at τ=1; P fail; edge fail
(-1,1,0)->(-2,1,0)  both unformed at τ=1; P fail; edge fail
2-step at (0,1,0): fail

(0,0,1)->(-1,0,1)  (-1,0,1) formed, split fail (O empty); P fail; edge fail
(-1,0,1)->(-2,0,1)  (-2,0,1) unformed at τ=1; P fail; edge fail
2-step at (0,0,1): fail

(0,1,1)->(-1,1,1)  (-1,1,1) formed, split fail (O empty); P fail; edge fail
(-1,1,1)->(-2,1,1)  (-2,1,1) unformed at τ=1; P fail; edge fail
2-step at (0,1,1): fail
```

All twelve listed vertices lie in `B_3(0)`.

## Theorem 2

Reverse probes are origin and `(0,1,0)`. Both two-step bits fail, neither is
UNDEFINED, so reverse: fail.

## Theorem 3

Face probes are `(0,0,1)` and `(0,1,1)`. Both two-step bits fail, neither is
UNDEFINED, so face: fail. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.

## What this does not show

The packet does not select a physical Record readout, a formation law, a
holonomy identity, or a 4-cycle. It does not write the displayed bits into
Admissibility. It does not attach L1. It does not enlarge Euclidean `B_3(0)`.
It does not claim uniqueness of `F` among other frame conventions.
Not leftover of the +e1 product.
