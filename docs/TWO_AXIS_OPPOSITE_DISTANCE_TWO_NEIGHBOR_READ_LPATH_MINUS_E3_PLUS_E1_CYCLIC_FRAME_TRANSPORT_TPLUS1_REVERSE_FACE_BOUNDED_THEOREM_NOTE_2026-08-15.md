---
claim_id: two_axis_opposite_distance_two_neighbor_read_lpath_minus_e3_plus_e1_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Distance-2 neighbor-read of L-path cyclic-frame transport −e3 then +e1 at t+1 on the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_distance_two_neighbor_read_lpath_minus_e3_plus_e1_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# Distance-2 Neighbor-Read Of L-Path Cyclic-Frame Transport −e3 Then +e1 At t+1

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact distance-2 neighbor-read of L-path bits `−e_3` then `+e_1`
at `τ=t+1` on the two-axis opposite seed in Euclidean `B_3(0)`, together
with reverse and face from those distance-2 bits.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_distance_two_neighbor_read_lpath_minus_e3_plus_e1_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_distance_two_neighbor_read_lpath_minus_e3_plus_e1_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

## Result up front

On the two-axis opposite seed, cyclic-frame transport along a named edge is
the signed-permutation map of the ordered triple `F=(m,o_next,o_prev)`. This
note displays distance-2 neighbor-read of the L-path one `−e_3` hop then one
`+e_1` hop from each of the four seed sites: the turn `+e_1` after the
HOLDING `−e_3` hop, toward the holonomy wall. It is not a 2-step along one
axis. It is not a 4-cycle.

L-path HOLD at `q` iff `q`, `q−e_3`, and `q−e_3+e_1` lie in `B_3(0)` and both
named edges HOLD. Distance-2 of that bit is existential: it HOLDs at `q` iff
L-path HOLDs at `q` and some formed `r` in `B_3(0)` with
`|r1−q1|+|r2−q2|+|r3−q3|=2` has L-path HOLD. Uniqueness is not required. If
L-path fails at `q`, distance-2 fails, not UNDEFINED.

At each site's own cut `τ=t+1` there is no global T. Reverse distance-2 bits
HOLD. Face distance-2 bits fail because the face L-path bits fail on the
second hop, even though each face probe has a formed site at coordinate sum
two with L-path HOLD. Therefore

```text
reverse: hold
face: fail
```

The bits are Displayed, not adopted. Do not write into Admissibility. Do not
attach L1. Uniqueness is not required. This is not leftover of the 1-step along
`−e_3`: every 1-step bit HOLDs, including both face probes.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact distance-2 neighbor-read of L-path bits on Euclidean B_3(0) at each site's own t+1; the bits are displayed and not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_distance_two_neighbor_read_lpath_minus_e3_plus_e1_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
target_blocker_text: "display distance-2 neighbor-read of L-path cyclic-frame transport -e3 then +e1 at t+1 and the reverse/face pair from those bits"
source_of_blocker_text: frontier_question
reachability_to_target: closed_finite_target
artifact_role: theorem
next_trace_action: "independent audit of the landed note and invocation-bound runner evidence"
conditional_surface_status: "exact only for the declared two-axis opposite seed, Euclidean B_3(0), and distance-2 neighbor-read of the named L-path -e3 then +e1 at t+1"
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

Let `t(q)` be the formation tick. The cut is `τ=t+1` at each site: there is
no global T. A site is formed at a cut `τ` iff it is recorded with tick
`≤ τ`. Unformed at `τ` is fail, not UNDEFINED. A vertex outside `B_3(0)` is
fail, not UNDEFINED.

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
are formed, split holds at both at each site's own `τ=t+1`, Orient is `±1`
at both, and the unique `3×3` integer matrix `P` sending columns of `F(q)` to
columns of `F(q+e)` (the unique `P` with `P F(q)=F(q+e)`) is a signed
permutation with `det P=Orient(q)Orient(q+e)`. Else that edge fails, not
UNDEFINED.

L-path HOLD at `q` iff `q`, `q−e_3`, and `q−e_3+e_1` lie in `B_3(0)` and
both named edges `(q,q−e_3)` and `(q−e_3,q−e_3+e_1)` HOLD.

Distance-2 HOLDs at `q` iff L-path HOLDs at `q` and some formed `r` in
`B_3(0)` at the cut `τ=t(q)+1` with `|r1−q1|+|r2−q2|+|r3−q3|=2` has L-path
HOLD. If L-path fails at `q`, distance-2 fails, not UNDEFINED. An empty
formed set at coordinate sum two, or every such formed site with L-path
fail, is fail, not UNDEFINED. Uniqueness is not required. Do not attach L1.

Reverse probes: origin and `(0,1,0)`. Face probes: `(0,0,1)` and `(0,1,1)`.
Reverse HOLD iff distance-2 HOLDs at both reverse probes. Face HOLD iff
both face probes HOLD.

## Theorem 1

At `τ=t+1` the four seeds are formed at tick `0`. Frames at the four seeds:

```text
F((0,0,0)) columns (+e_1,-e_2,-e_3); Orient((0,0,0))=+1
F((0,1,0)) columns (-e_1,+e_2,-e_3); Orient((0,1,0))=+1
F((0,0,1)) columns (+e_2,+e_3,-e_1); Orient((0,0,1))=-1
F((0,1,1)) columns (-e_2,+e_3,-e_1); Orient((0,1,1))=+1
```

The eight named L-path edges, the four L-path bits, formed sites at
coordinate sum two at each seed's own `τ=1`, and the four distance-2 bits:

```text
(0,0,0)->(0,0,-1)
  dest t=1; F dest columns (-e_3,-e_1,-e_2); Orient dest=-1
  P=[0 1 0; 0 0 1; -1 0 0]; det P=-1; edge hold
(0,0,-1)->(1,0,-1)
  dest t=2; F dest columns (+e_1,-e_2,-e_3); Orient dest=+1
  P=[0 0 -1; 1 0 0; 0 1 0]; det P=-1; edge hold
  L-path at (0,0,0): hold
  formed |r1−q1|+|r2−q2|+|r3−q3|=2 at tau=1:
    (-1,0,1) t=1 L-path fail
    (0,0,2) t=1 L-path hold
    (0,1,-1) t=1 L-path fail
    (0,1,1) t=0 L-path fail
    (0,2,0) t=1 L-path fail
    (1,0,1) t=1 L-path fail
  witness (0,0,2)
  distance-2 at (0,0,0): hold

(0,1,0)->(0,1,-1)
  dest t=1; F dest columns (-e_3,-e_1,+e_2); Orient dest=+1
  P=[0 -1 0; 0 0 -1; 1 0 0]; det P=+1; edge hold
(0,1,-1)->(1,1,-1)
  dest t=2; F dest columns (+e_1,+e_2,-e_3); Orient dest=-1
  P=[0 0 -1; -1 0 0; 0 -1 0]; det P=-1; edge hold
  L-path at (0,1,0): hold
  formed |r1−q1|+|r2−q2|+|r3−q3|=2 at tau=1:
    (-1,1,1) t=1 L-path fail
    (0,-1,0) t=1 L-path fail
    (0,0,-1) t=1 L-path fail
    (0,0,1) t=0 L-path fail
    (0,1,2) t=1 L-path hold
    (1,1,1) t=1 L-path fail
  witness (0,1,2)
  distance-2 at (0,1,0): hold

(0,0,1)->(0,0,0)
  dest t=0; F dest as origin; Orient dest=+1
  P=[0 1 0; 0 0 -1; 1 0 0]; det P=-1; edge hold
(0,0,0)->(1,0,0)
  dest t=2; split fail (cover misses an axis); P fail; edge fail
  L-path at (0,0,1): fail
  formed |r1−q1|+|r2−q2|+|r3−q3|=2 at tau=1:
    (-1,1,1) t=1 L-path fail
    (0,-1,0) t=1 L-path fail
    (0,0,-1) t=1 L-path fail
    (0,1,0) t=0 L-path hold
    (0,1,2) t=1 L-path hold
    (1,1,1) t=1 L-path fail
  formed sites with L-path hold: (0,1,0) and (0,1,2)
  distance-2 at (0,0,1): fail

(0,1,1)->(0,1,0)
  dest t=0; F dest as (0,1,0); Orient dest=+1
  P=[0 1 0; 0 0 1; 1 0 0]; det P=+1; edge hold
(0,1,0)->(1,1,0)
  dest t=2; split fail (cover misses an axis); P fail; edge fail
  L-path at (0,1,1): fail
  formed |r1−q1|+|r2−q2|+|r3−q3|=2 at tau=1:
    (-1,0,1) t=1 L-path fail
    (0,0,0) t=0 L-path hold
    (0,0,2) t=1 L-path hold
    (0,1,-1) t=1 L-path fail
    (0,2,0) t=1 L-path fail
    (1,0,1) t=1 L-path fail
  formed sites with L-path hold: (0,0,0) and (0,0,2)
  distance-2 at (0,1,1): fail
```

All twelve listed L-path vertices lie in `B_3(0)`. Each HOLDING `det P`
equals the product of the two Orient signs. Reverse probes each have one
witness, so uniqueness is not used. If L-path fails at `q`, distance-2
fails, not UNDEFINED, even though a formed site at coordinate sum two has
L-path HOLD: that is the face-probe case, with `(0,1,0)` a formed site at
coordinate sum two from `(0,0,1)`.

## Theorem 2

Reverse probes are origin and `(0,1,0)`. Both distance-2 bits hold, neither
is UNDEFINED, so reverse: hold.

## Theorem 3

Face probes are `(0,0,1)` and `(0,1,1)`. Both distance-2 bits fail, neither
is UNDEFINED, so face: fail. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.

## What this does not show

The packet does not select a physical Record readout, a formation law, a
holonomy identity, or a 4-cycle. It does not write the displayed bits into
Admissibility. It does not attach L1. It does not enlarge Euclidean `B_3(0)`.
It does not claim uniqueness of a witnessing site at coordinate sum two, nor
uniqueness of `F` among other frame conventions. It does not replace
distance-2 neighbor-read by the bare L-path bit, nor by the 1-step along
`−e_3`, nor by a 2-step along one axis.
