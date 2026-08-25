---
claim_id: two_axis_opposite_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Directed 2-step cyclic-frame transport along −e3 freeze t+1 vs t+2 on the two-axis opposite seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# Directed Two-Step Cyclic-Frame Transport Along −e3 Freeze t+1 Versus t+2

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact directed two-step bits along `−e_3` at `τ1=t+1` and at
`τ2=t+2` on the two-axis opposite seed in Euclidean `B_3(0)`, together with
reverse and face at each cut, and composition of those bits.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

## Result up front

On the two-axis opposite seed, cyclic-frame transport along a named edge is
the signed-permutation map of the ordered triple `F=(m,o_next,o_prev)`. This
note displays the *directed* two-step along `−e_3` twice from each of the four
seed sites at each site's own cut `τ1=t+1` and again at `τ2=t+2`. Directed
2-step as nm2frm2sz. It is two hops of the same vector, not one. It is
not leftover remaining-bit of HOLDING 1-step freeze. It is not leftover of a
prior freeze: this is the first t+2 of this letter. Uniqueness is not
required.

At each seed's own cuts (`t=0`, so `τ1=1` and `τ2=2` at the seeds) the reverse
2-step bits fail and the face 2-step bits HOLD, so

```text
2-step at (0,0,0) at τ1: fail
2-step at (0,1,0) at τ1: fail
2-step at (0,0,1) at τ1: hold
2-step at (0,1,1) at τ1: hold
2-step at (0,0,0) at τ2: fail
2-step at (0,1,0) at τ2: fail
2-step at (0,0,1) at τ2: hold
2-step at (0,1,1) at τ2: hold
reverse at τ1: fail
face at τ1: hold
reverse at τ2: fail
face at τ2: hold
composition: hold
```

The reverse bits and the face bits at `τ1` equal those at `τ2`. The bits are
Displayed, not adopted. Do not write into Admissibility. Do not attach L1.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact 2-step bits on Euclidean B_3(0) at each site's own t+1 versus t+2; reverse/face at each cut and composition are displayed and not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_directed_two_step_minus_e3_cyclic_frame_transport_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
target_blocker_text: "display directed 2-step cyclic-frame transport along -e3 freeze t+1 vs t+2 and the reverse/face pair at each cut with composition"
source_of_blocker_text: frontier_question
reachability_to_target: closed_finite_target
artifact_role: theorem
next_trace_action: "independent audit of the landed note and invocation-bound runner evidence"
conditional_surface_status: "exact only for the declared two-axis opposite seed, Euclidean B_3(0), and the named -e3 two-step at t+1 versus t+2"
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

From a recorded site `p` with lock `L(p)=±e_i`, a step `s` to `q=p+s` is
allowed iff `s·e_i=0`. If `q` lies in `B_3(0)` and is unformed, `q` forms at
`t(p)+1` and the incoming set `M(q)` is the set of earliest such steps. If
several allowed parents reach `q` at the same earliest formation, each such
incoming step is kept. Mixed remains a set and mixed sites still emit along
each recorded incoming letter. Seed incoming sets are the assigned locks.

Let `t(q)` be the formation tick. The cuts are `τ1=t+1` and `τ2=t+2` at each
site: there is no global T. A site is formed at a cut `τ` iff it is recorded
with tick `≤ τ`. Unformed at `τ` is fail, not UNDEFINED. A vertex outside
`B_3(0)` is fail, not UNDEFINED.

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

Directed-edge HOLD from `q` to `q+e` at a named offset `k∈{1,2}` iff `q` and
`q+e` lie in `B_3(0)`, both are formed, split holds at both at each site's
own `τ=t+k`, Orient is `±1` at both, and the unique `3×3` integer matrix `P`
sending columns of `F(q)` to columns of `F(q+e)` (`F(q+e)=F(q)P`) is a signed
permutation with `det P=Orient(q)Orient(q+e)`. Else that edge fails, not
UNDEFINED.

Directed 2-step along `−e_3` HOLDs at `q` at that cut iff `q`, `q−e_3`, and
`q−2e_3` lie in `B_3(0)` and both named edges `(q,q−e_3)` and
`(q−e_3,q−2e_3)` HOLD at that cut. A vertex outside `B_3(0)` is fail, not
UNDEFINED.

Reverse probes: origin and `(0,1,0)`. Face probes: `(0,0,1)` and `(0,1,1)`.
Reverse HOLD at a cut iff 2-step along `−e_3` HOLDs at both reverse probes
at that cut. Face HOLD at a cut iff both face probes HOLD at that cut.
Composition HOLDs iff the reverse bits and the face bits at `τ1` equal the
reverse bits and the face bits at `τ2`. Else composition fails.

## Theorem 1

At `τ1=t+1` and at `τ2=t+2` the four seeds are formed at tick `0`. Frames at
the four seeds are the same at both cuts:

```text
F((0,0,0)) columns (+e_1,-e_2,-e_3); Orient((0,0,0))=+1
F((0,1,0)) columns (-e_1,+e_2,-e_3); Orient((0,1,0))=+1
F((0,0,1)) columns (+e_2,+e_3,-e_1); Orient((0,0,1))=-1
F((0,1,1)) columns (-e_2,+e_3,-e_1); Orient((0,1,1))=+1
```

The four named `−e_3` two-step chains, `P` on each named edge, and the
two-step bits at both cuts:

```text
(0,0,0)->(0,0,-1)->(0,0,-2)
  dest1 t=1; F dest1 columns (-e_3,-e_1,-e_2); Orient dest1=-1
  P=[0 -1 0; 0 0 1; 1 0 0]; det P=-1; first edge hold
  dest2 t=4; M={+e_1,-e_1,+e_2}; O={-e_3}; split fail; second edge fail
  2-step at (0,0,0) at τ1: fail
  2-step at (0,0,0) at τ2: fail

(0,1,0)->(0,1,-1)->(0,1,-2)
  dest1 t=1; F dest1 columns (-e_3,-e_1,+e_2); Orient dest1=+1
  P=[0 1 0; 0 0 1; 1 0 0]; det P=+1; first edge hold
  dest2 t=4; M={+e_1,-e_1,-e_2}; O empty; split fail; second edge fail
  2-step at (0,1,0) at τ1: fail
  2-step at (0,1,0) at τ2: fail

(0,0,1)->(0,0,0)->(0,0,-1)
  dest1 t=0; F dest1 as origin; Orient dest1=+1
  P=[0 -1 0; 0 0 -1; -1 0 0]; det P=-1; first edge hold
  dest2 t=1; F dest2 as (0,0,-1); Orient dest2=-1
  P=[0 -1 0; 0 0 1; 1 0 0]; det P=-1; second edge hold
  2-step at (0,0,1) at τ1: hold
  2-step at (0,0,1) at τ2: hold

(0,1,1)->(0,1,0)->(0,1,-1)
  dest1 t=0; F dest1 as (0,1,0); Orient dest1=+1
  P=[0 -1 0; 0 0 -1; 1 0 0]; det P=+1; first edge hold
  dest2 t=1; F dest2 as (0,1,-1); Orient dest2=+1
  P=[0 1 0; 0 0 1; 1 0 0]; det P=+1; second edge hold
  2-step at (0,1,1) at τ1: hold
  2-step at (0,1,1) at τ2: hold
```

All twelve listed vertices lie in `B_3(0)`. Each `det P` on a HOLDING edge
equals the product of the two Orient signs. The second reverse hop fails at
both cuts from split fail at `(0,0,−2)` and at `(0,1,−2)`, not UNDEFINED.
This is not leftover of the 1-step freeze: every named first hop along `−e_3`
from the four seeds HOLDs at both cuts, so the 1-step reverse bit HOLDs while
the 2-step reverse bit fails.

## Theorem 2

Reverse probes are origin and `(0,1,0)`. Both two-step bits fail at `τ1` and
at `τ2`, neither is UNDEFINED, so reverse at τ1: fail and reverse at τ2:
fail.

## Theorem 3

Face probes are `(0,0,1)` and `(0,1,1)`. Both two-step bits hold at `τ1` and
at `τ2`, neither is UNDEFINED, so face at τ1: hold and face at τ2: hold.
The reverse bits and the face bits at `τ1` equal those at `τ2`, so
composition: hold. Displayed, not adopted. Do not write into Admissibility.
Do not attach L1.

## What this does not show

The packet does not select a physical Record readout, a formation law, a
holonomy identity, or a 4-cycle. It does not write the displayed bits into
Admissibility. It does not attach L1. It does not enlarge Euclidean `B_3(0)`.
It does not claim uniqueness of `F` among other frame conventions. It does
not replace the two-step by the one-step along `−e_3`. It does not replace
this freeze by a one-cut t+1 display. It does not treat the HOLDING 1-step
freeze remaining-bit as this letter.
