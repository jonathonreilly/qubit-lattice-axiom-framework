---
claim_id: three_axis_opposite_lpath_minus_e3_plus_e1_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "L-path cyclic-frame transport −e3 then +e1 at t+1 on the three-axis opposite near-face seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_opposite_lpath_minus_e3_plus_e1_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# L-Path Cyclic-Frame Transport −e3 Then +e1 At t+1 On The Three-Axis Opposite Near-Face Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact L-path bits `−e_3` then `+e_1` at `τ=t+1` on the
three-axis opposite near-face seed in Euclidean `B_3(0)`, together with reverse
and face from those bits.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_opposite_lpath_minus_e3_plus_e1_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_opposite_lpath_minus_e3_plus_e1_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

## Result up front

On the three-axis opposite near-face seed, cyclic-frame transport along a named
edge is the signed-permutation map of the ordered triple `F=(m,o_next,o_prev)`.
This note displays the L-path one `−e_3` hop then one `+e_1` hop from each of
the four reverse/face seed sites: the turn `+e_1` after the HOLDING `−e_3` hop.
It is not a 2-step along one axis. It is not a 4-cycle. Uniqueness is not required.

At each site's own cut `τ=t+1` there is no global T. Both reverse L-path bits
fail on the `+e_1` hop (two-in at the turn destination). The face L-path at
`(0,0,1)` HOLDs and the face L-path at `(0,1,1)` fails. Therefore

```text
reverse: fail
face: fail
```

The bits are Displayed, not adopted. Do not write into Admissibility. Do not
attach L1. This is not leftover of the 1-step along `−e_3`: every 1-step bit
HOLDs, including both reverse probes.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact L-path bits on Euclidean B_3(0) at each site's own t+1; the bits are displayed and not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_opposite_lpath_minus_e3_plus_e1_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
target_blocker_text: "display L-path cyclic-frame transport -e3 then +e1 at t+1 on the three-axis opposite near-face seed and the reverse/face pair from those bits"
source_of_blocker_text: frontier_question
reachability_to_target: closed_finite_target
artifact_role: theorem
next_trace_action: "independent audit of the landed note and invocation-bound runner evidence"
conditional_surface_status: "exact only for the declared three-axis opposite near-face seed, Euclidean B_3(0), and the named L-path -e3 then +e1 at t+1"
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

Seed at tick `0`, two disjoint opposite pairs plus near-face third pair.
The third pair is a new seed, not a formed child:

```text
(0,0,0) locks +e_1
(0,1,0) locks -e_1
(0,0,1) locks +e_2
(0,1,1) locks -e_2
(2,0,0) locks +e_3
(2,1,0) locks -e_3
```

From a recorded site `p` with unique lock `L(p)=±e_i`, a step `s` to
`q=p+s` is allowed iff `s·e_i=0`. If `q` lies in `B_3(0)` and is unformed,
`q` forms at `t(p)+1` and the incoming set `M(q)` is the set of earliest such
steps. If that set is not a singleton, `q` has no unique lock and does not
emit. Seed incoming sets are the assigned locks.

Let `t(q)` be the formation tick. The cut is `τ=t+1` at each site: there is
no global T. A site is formed at a cut `τ` iff it is recorded with tick
`≤ τ`. Unformed at `τ` is fail, not UNDEFINED. A vertex outside `B_3(0)` is
fail, not UNDEFINED. fail not UNDEFINED.

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

Reverse probes: origin and `(0,1,0)`. Face probes: `(0,0,1)` and `(0,1,1)`.
Reverse HOLD iff L-path HOLDs at both reverse probes. Face HOLD iff both face
probes HOLD.

## Theorem 1

At `τ=t+1` the six seeds are formed at tick `0`. Frames at the six seeds:

```text
F((0,0,0)) columns (+e_1,-e_2,-e_3); Orient((0,0,0))=+1
F((0,1,0)) columns (-e_1,+e_2,-e_3); Orient((0,1,0))=+1
F((0,0,1)) columns (+e_2,+e_3,-e_1); Orient((0,0,1))=-1
F((0,1,1)) columns (-e_2,+e_3,-e_1); Orient((0,1,1))=+1
F((2,0,0)) columns (+e_3,-e_1,-e_2); Orient((2,0,0))=+1
F((2,1,0)) columns (-e_3,-e_1,+e_2); Orient((2,1,0))=+1
```

The eight named L-path edges and the four L-path bits:

```text
(0,0,0)->(0,0,-1)
  dest t=1; F dest columns (-e_3,-e_1,-e_2); Orient dest=-1
  P=[0 1 0; 0 0 1; -1 0 0]; det P=-1; edge hold
(0,0,-1)->(1,0,-1)
  dest t=2; formed, split fail (M={-e3,+e1}, two-in); P fail; edge fail
  L-path at (0,0,0): fail

(0,1,0)->(0,1,-1)
  dest t=1; F dest columns (-e_3,-e_1,+e_2); Orient dest=+1
  P=[0 -1 0; 0 0 -1; 1 0 0]; det P=+1; edge hold
(0,1,-1)->(1,1,-1)
  dest t=2; formed, split fail (M={-e3,+e1}, two-in); P fail; edge fail
  L-path at (0,1,0): fail

(0,0,1)->(0,0,0)
  dest t=0; F dest as origin; Orient dest=+1
  P=[0 1 0; 0 0 -1; 1 0 0]; det P=-1; edge hold
(0,0,0)->(1,0,0)
  dest t=1; F dest columns (-e_1,-e_2,-e_3); Orient dest=-1
  P=[-1 0 0; 0 1 0; 0 0 1]; det P=-1; edge hold
  L-path at (0,0,1): hold

(0,1,1)->(0,1,0)
  dest t=0; F dest as (0,1,0); Orient dest=+1
  P=[0 1 0; 0 0 1; 1 0 0]; det P=+1; edge hold
(0,1,0)->(1,1,0)
  dest t=1; formed, split fail (M={-e1}, O={-e1,+e2,-e3}); P fail; edge fail
  L-path at (0,1,1): fail
```

All twelve listed vertices lie in `B_3(0)`. Each HOLDING `det P` equals the
product of the two Orient signs. The near-face third pair makes `(1,0,0)` form
at tick `1` with unique lock `-e_1`, so the `+e_1` hop from the origin HOLDs;
the same third pair makes the reverse turn destinations two-in.

## Theorem 2

Reverse probes are origin and `(0,1,0)`. Both L-path bits fail, neither is
UNDEFINED, so reverse: fail.

## Theorem 3

Face probes are `(0,0,1)` and `(0,1,1)`. The `(0,0,1)` L-path HOLDs and the
`(0,1,1)` L-path fails, neither is UNDEFINED, so face: fail. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1.

## What this does not show

The packet does not select a physical Record readout, a formation law, a
holonomy identity, or a 4-cycle. It does not write the displayed bits into
Admissibility. It does not attach L1. It does not enlarge Euclidean `B_3(0)`.
It does not claim uniqueness of `F` among other frame conventions. It does
not replace the L-path by the 1-step along `−e_3` or by a 2-step along one
axis.
