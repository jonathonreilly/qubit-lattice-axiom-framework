---
claim_id: three_axis_farface_opposite_directed_two_step_plus_e2_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Directed 2-step cyclic-frame transport along +e2 at t+1 on the three-axis far-face opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_farface_opposite_directed_two_step_plus_e2_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# Directed Two-Step Cyclic-Frame Transport Along +e2 At t+1 On The Three-Axis Far-Face Opposite Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact directed two-step bits along `+e_2` at `τ=t+1` on the
three-axis far-face opposite seed in Euclidean `B_3(0)`, together with reverse
and face from those bits.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_farface_opposite_directed_two_step_plus_e2_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_farface_opposite_directed_two_step_plus_e2_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

## Result up front

On the three-axis far-face opposite seed, cyclic-frame transport along a named
edge is the signed-permutation map of the ordered triple `F=(m,o_next,o_prev)`.
This note displays the *directed* two-step along `+e_2` from each of the four
probes. First display of two hops along +e2 on the far-face seed. It is two
hops, not one. Uniqueness is not required. The third pair is a new seed, not
a formed child.

At the common cut `τ=t+1` of each seed (`t=0`, so `τ=1`), origin split fails,
so the origin two-step bit fails. The remaining reverse probe fails at the
second hop: `(0,2,0)` is formed with empty outgoing set. The face probe
`(0,0,1)` HOLDs the first hop and fails the second. The face probe `(0,1,1)`
fails because `(0,3,1)` lies outside `B_3(0)`. Vertex outside B_3 is fail not
UNDEFINED. Therefore

```text
reverse: fail
face: fail
```

The bits are Displayed, not adopted. Do not write into Admissibility. Do not
attach L1.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact 2-step bits on Euclidean B_3(0) at one declared cut; the bits are displayed and not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_farface_opposite_directed_two_step_plus_e2_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
target_blocker_text: "display directed 2-step cyclic-frame transport along +e2 at t+1 on the three-axis far-face opposite seed and the reverse/face pair from those bits"
source_of_blocker_text: frontier_question
reachability_to_target: closed_finite_target
artifact_role: theorem
next_trace_action: "independent audit of the landed note and invocation-bound runner evidence"
conditional_surface_status: "exact only for the declared three-axis far-face opposite seed, Euclidean B_3(0), and the named +e2 two-step at t+1"
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

Directed-edge HOLD from `q` to `q+e_2` iff `q` and `q+e_2` lie in `B_3(0)`,
both are formed at `τ`, split holds at both, Orient is `±1` at both, and the
`3×3` integer matrix `P` sending columns of `F(q)` to columns of `F(q+e_2)`
(the `P` with `P F(q)=F(q+e_2)`) is a signed permutation with
`det P=Orient(q)Orient(q+e_2)`. Else that edge fails, not UNDEFINED.

Directed 2-step along `+e_2` HOLDs at `q` iff `q`, `q+e_2`, and `q+2e_2` lie
in `B_3(0)` and directed-edge HOLDs for `(q,q+e_2)` and `(q+e_2,q+2e_2)`.
Vertex outside B_3 is fail not UNDEFINED.

Reverse probes: origin and `(0,1,0)`. Face probes: `(0,0,1)` and `(0,1,1)`.
Reverse HOLD iff 2-step along `+e_2` HOLDs at both reverse probes. Face HOLD
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

Frames at the four probes:

```text
F((0,0,0)) fails
  M={+e_1}, O={-e_2}; Axis(M)={e_1}, Axis(O)={e_2}; split fails
F((0,1,0)) columns (-e_1,+e_2,-e_3); Orient((0,1,0))=+1
F((0,0,1)) columns (+e_2,+e_3,-e_1); Orient((0,0,1))=-1
F((0,1,1)) columns (-e_2,+e_3,-e_1); Orient((0,1,1))=+1
```

Origin split fails because the far-face seed at `(0,0,-1)` locks `+e_3`, so
the step `−e_3` from origin is not in `M((0,0,-1))` and is not in origin
`O`. Intermediate chain vertices at the same cut:

```text
(0,2,0) t=1; M={+e_2}; O empty; split fails
(0,3,0) in B_3(0); unformed at τ=1; F fails
(0,2,1) in B_3(0); unformed at τ=1; F fails
(0,3,1) outside B_3(0); fail not UNDEFINED
```

The named `+e_2` edges and the four two-step bits:

```text
(0,0,0)->(0,1,0)
  dest t=0; F dest columns (-e_1,+e_2,-e_3); Orient dest=+1
  src split fail; edge fail
(0,1,0)->(0,2,0)
  dest t=1; formed, split fail (O empty); P fail; edge fail
  2-step at (0,0,0): fail

(0,1,0)->(0,2,0)
  dest t=1; formed, split fail (O empty); P fail; edge fail
(0,2,0)->(0,3,0)
  dest unformed at τ=1; edge fail
  2-step at (0,1,0): fail

(0,0,1)->(0,1,1)
  dest t=0; F dest columns (-e_2,+e_3,-e_1); Orient dest=+1
  P=[(1,0,0); (0,-1,0); (0,0,1)]; det P=-1; edge hold
(0,1,1)->(0,2,1)
  dest unformed at τ=1; P fail; edge fail
  2-step at (0,0,1): fail

(0,1,1)->(0,2,1)
  dest unformed at τ=1; edge fail
(0,2,1)->(0,3,1)
  dest outside B_3(0); fail not UNDEFINED
  2-step at (0,1,1): fail
```

On the HOLDING first hop, `det P` equals the product of the two Orient
signs. The first hop HOLD at `(0,0,1)` is not a two-step HOLD: both hops
are required.

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
It does not treat the far-face third pair as a formed child of the first pair.
The displayed reverse and face bits are not adopted.
