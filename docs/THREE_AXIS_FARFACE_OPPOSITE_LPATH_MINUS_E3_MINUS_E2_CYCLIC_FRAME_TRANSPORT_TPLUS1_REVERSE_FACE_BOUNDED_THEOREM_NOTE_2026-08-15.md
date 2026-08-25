---
claim_id: three_axis_farface_opposite_lpath_minus_e3_minus_e2_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "L-path cyclic-frame transport −e3 then −e2 at t+1 on the three-axis far-face opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_farface_opposite_lpath_minus_e3_minus_e2_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# L-Path Cyclic-Frame Transport −e3 Then −e2 At t+1 On The Three-Axis Far-Face Opposite Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact L-path bits, one hop along `−e_3` then one hop along `−e_2`,
at each site's own `τ=t+1` on the three-axis far-face opposite seed in
Euclidean `B_3(0)`, together with reverse and face from those bits.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_farface_opposite_lpath_minus_e3_minus_e2_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_farface_opposite_lpath_minus_e3_minus_e2_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

## Result up front

On the three-axis far-face opposite seed, cyclic-frame transport along a named
edge is the signed-permutation map of the ordered triple `F=(m,o_next,o_prev)`.
This note displays the same named L-path as on the two-axis opposite seed: one
`−e_3` hop then one `−e_2` hop from each of the four seed probes. It is not a
2-step along one axis. It is not a 4-cycle. The third pair is a new seed, not a
formed child.

At each site's own cut `τ=t+1` origin split fails, so the origin first hop
fails and the origin L-path fails. The reverse probe `(0,1,0)` HOLDs both hops.
Both face L-path bits fail. Therefore

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
claim_type_reason: "Finite exact L-path bits on Euclidean B_3(0) at each site's own t+1; the bits are displayed and not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_farface_opposite_lpath_minus_e3_minus_e2_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
target_blocker_text: "display L-path cyclic-frame transport -e3 then -e2 at t+1 on the three-axis far-face opposite seed and the reverse/face pair from those bits"
source_of_blocker_text: frontier_question
reachability_to_target: closed_finite_target
artifact_role: theorem
next_trace_action: "independent audit of the landed note and invocation-bound runner evidence"
conditional_surface_status: "exact only for the declared three-axis far-face opposite seed, Euclidean B_3(0), and the named -e3 then -e2 L-path at t+1"
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

L-path HOLD at `q` iff `q`, `q−e_3`, and `q−e_3−e_2` lie in `B_3(0)` and both
named edges `(q,q−e_3)` and `(q−e_3,q−e_3−e_2)` HOLD.

Reverse probes: origin and `(0,1,0)`. Face probes: `(0,0,1)` and `(0,1,1)`.
Reverse HOLD iff L-path HOLDs at both reverse probes. Face HOLD iff both face
probes HOLD.

## Theorem 1

At `τ=t+1` the six seeds are formed at tick `0`. Frames at the four probes,
the two far-face dest seeds, and the two second-hop dests that are not those
seeds:

```text
F((0,0,0)) fails
  M={+e_1}, O={-e_2}; Axis(M)={e_1}, Axis(O)={e_2}; split fails
F((0,1,0)) columns (-e_1,+e_2,-e_3); Orient((0,1,0))=+1
F((0,0,1)) columns (+e_2,+e_3,-e_1); Orient((0,0,1))=-1
F((0,1,1)) columns (-e_2,+e_3,-e_1); Orient((0,1,1))=+1
F((0,0,-1)) columns (+e_3,-e_1,-e_2); Orient((0,0,-1))=+1
F((0,1,-1)) columns (-e_3,-e_1,+e_2); Orient((0,1,-1))=+1
F((0,-1,-1)) columns (-e_2,-e_3,-e_1); Orient((0,-1,-1))=-1
F((0,-1,0)) columns (-e_2,+e_3,-e_1); Orient((0,-1,0))=+1
```

Origin split fails because the far-face seed at `(0,0,-1)` locks `+e_3`, so
the step `−e_3` from origin is not in `M((0,0,-1))` and is not in origin
`O`. The eight named edges and the four L-path bits:

```text
(0,0,0)->(0,0,-1)->(0,-1,-1)
  hop1 dest t=0; F dest columns (+e_3,-e_1,-e_2); Orient dest=+1
  src split fail; P fail; edge fail
  hop2 dest t=1; F dest columns (-e_2,-e_3,-e_1); Orient dest=-1
  P=[0 1 0; 0 0 -1; 1 0 0]; det P=-1; edge hold
  L-path at (0,0,0): fail

(0,1,0)->(0,1,-1)->(0,0,-1)
  hop1 dest t=0; F dest columns (-e_3,-e_1,+e_2); Orient dest=+1
  P=[0 -1 0; 0 0 -1; 1 0 0]; det P=+1; edge hold
  hop2 dest t=0; F dest columns (+e_3,-e_1,-e_2); Orient dest=+1
  P=[1 0 0; 0 -1 0; 0 0 -1]; det P=+1; edge hold
  L-path at (0,1,0): hold

(0,0,1)->(0,0,0)->(0,-1,0)
  hop1 dest t=0; F dest fails
  dest split fail; P fail; edge fail
  hop2 dest t=1; F dest columns (-e_2,+e_3,-e_1); Orient dest=+1
  src split fail; P fail; edge fail
  L-path at (0,0,1): fail

(0,1,1)->(0,1,0)->(0,0,0)
  hop1 dest t=0; F dest as (0,1,0); Orient dest=+1
  P=[0 1 0; 0 0 1; 1 0 0]; det P=+1; edge hold
  hop2 dest t=0; dest split fail; P fail; edge fail
  L-path at (0,1,1): fail
```

All twelve listed vertices lie in `B_3(0)`. On each HOLDING edge, `det P`
equals the product of the two Orient signs. This is the same named `−e_3`
then `−e_2` L-path as on the two-axis opposite seed, read on the six-site
far-face host: origin `F` HOLDs on the four-site two-axis seed and fails here,
and that two-axis face bit HOLDs while this face bit fails. This is
not leftover of +e2: the `+e_2` L-path bits on this host are `(fail, hold)`
on reverse and `(fail, hold)` on face, while this reverse fails with bits
`(fail, hold)` and this face fails with bits `(fail, fail)`. This is
not leftover of the 1-step along `−e_3`: that reverse bit fails with bits
`(fail, hold)` and that face bit fails with bits `(fail, hold)`, while this
reverse fails with bits `(fail, hold)` and this face fails with bits
`(fail, fail)`. This is not leftover of the 2-step along `−e_3`: that reverse
bit fails with bits `(fail, fail)` and that face bit fails with bits
`(fail, hold)`, while this reverse fails with bits `(fail, hold)` and this
face fails with bits `(fail, fail)`.

## Theorem 2

Reverse probes are origin and `(0,1,0)`. Origin L-path fails, `(0,1,0)` L-path
holds, neither is UNDEFINED, so reverse: fail.

## Theorem 3

Face probes are `(0,0,1)` and `(0,1,1)`. Both L-path bits fail, neither is
UNDEFINED, so face: fail. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.

## What this does not show

The packet does not select a physical Record readout, a formation law, a
holonomy identity, or a 4-cycle. It does not write the displayed bits into
Admissibility. It does not attach L1. It does not enlarge Euclidean `B_3(0)`.
It does not claim uniqueness of `F` among other frame conventions. It does
not replace the opposite in-plane turn `−e_2` by leftover `+e_2`, by the
1-step along `−e_3`, or by the 2-step along `−e_3`. It does not treat the
far-face third pair as a formed child of the first pair.
