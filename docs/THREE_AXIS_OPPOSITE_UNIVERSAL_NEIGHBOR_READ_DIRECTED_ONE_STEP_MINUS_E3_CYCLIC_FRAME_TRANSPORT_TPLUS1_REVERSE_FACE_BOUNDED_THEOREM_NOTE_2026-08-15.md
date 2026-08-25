---
claim_id: three_axis_opposite_universal_neighbor_read_directed_one_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Universal neighbor-read of directed 1-step cyclic-frame transport along −e3 at t+1 on the three-axis opposite near-face seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_opposite_universal_neighbor_read_directed_one_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py
---

# Universal Neighbor-Read Of Directed One-Step Cyclic-Frame Transport Along −e3 At t+1 On The Three-Axis Opposite Near-Face Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact universal neighbor-read of directed one-step bits along
`−e_3` at `τ=t+1` on the three-axis opposite near-face seed in Euclidean
`B_3(0)`, together with reverse and face from those universal bits.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_opposite_universal_neighbor_read_directed_one_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_opposite_universal_neighbor_read_directed_one_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_2026_08_15.py)

## Result up front

On the three-axis opposite near-face seed, cyclic-frame transport along a
named edge is the signed-permutation map of the ordered triple
`F=(m,o_next,o_prev)`. Directed 1-step along `−e_3` is that named one-hop
bit at each site's own `τ=t+1`. Let `T(q)` be the formed six-neighbors of
`q` that lie in `B_3(0)` at the cut `τ=t(q)+1`. Universal neighbor-read
HOLDs at `q` iff the 1-step along `−e_3` HOLDs at `q`, `T(q)` is nonempty,
and every `r` in `T(q)` has 1-step along `−e_3` HOLD. Uniqueness is not required.
Empty T or 1-step fail is fail not UNDEFINED.

At each seed's own cut `τ=t+1` (`t=0`, so `τ=1` at the seeds) every named
`−e_3` 1-step HOLDs and each `T(q)` is nonempty, but each `T(q)` also
contains a formed six-neighbor whose 1-step fails. Therefore every universal
neighbor-read bit fails, so

```text
reverse: fail
face: fail
```

This is not leftover of existential neighbor-read of the same directed
1-step, which HOLDs because some formed six-neighbor HOLDs. Universal fails
because not every formed six-neighbor HOLDs.

The bits are Displayed, not adopted. Do not write into Admissibility. Do not
attach L1.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact universal neighbor-read of 1-step bits on Euclidean B_3(0) at each site's own t+1; the bits are displayed and not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_opposite_universal_neighbor_read_directed_one_step_minus_e3_cyclic_frame_transport_tplus1_reverse_face_bounded_theorem_note_2026-08-15
target_blocker_text: "display universal neighbor-read of directed 1-step cyclic-frame transport along -e3 at t+1 on the three-axis opposite near-face seed and the reverse/face pair from those bits"
source_of_blocker_text: frontier_question
reachability_to_target: closed_finite_target
artifact_role: theorem
next_trace_action: "independent audit of the landed note and invocation-bound runner evidence"
conditional_surface_status: "exact only for the declared three-axis opposite near-face seed, Euclidean B_3(0), and universal neighbor-read of the named -e3 one-step at t+1"
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

Directed 1-step along `−e_3` HOLDs at `q` iff `q` and `q−e_3` lie in
`B_3(0)` and the named edge `(q,q−e_3)` HOLDs.

`T(q)` is the set of formed six-neighbors of `q` that lie in `B_3(0)` at
`τ=t(q)+1`. Universal neighbor-read HOLDs at `q` iff 1-step along `−e_3`
HOLDs at `q`, `T(q)` is nonempty, and every `r` in `T(q)` has 1-step along
`−e_3` HOLD. Empty T or 1-step fail is fail not UNDEFINED. If 1-step
fails at `q`, universal neighbor-read fails, not UNDEFINED. Uniqueness is not required.

Reverse probes: origin and `(0,1,0)`. Face probes: `(0,0,1)` and `(0,1,1)`.
Reverse HOLD iff universal neighbor-read HOLDs at both reverse probes. Face
HOLD iff both face probes HOLD.

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

The four named `−e_3` edges, the four one-step bits, `T(q)` at `τ=1`, and
the four universal neighbor-read bits:

```text
(0,0,0)->(0,0,-1)
  dest t=1; F dest columns (-e_3,-e_1,-e_2); Orient dest=-1
  P=[0 1 0; 0 0 1; -1 0 0]; det P=-1; edge hold
  1-step at (0,0,0): hold
  T((0,0,0)) at tau=1:
    (1,0,0) t=1 1-step fail
    (0,1,0) t=0 1-step hold
    (0,-1,0) t=1 1-step fail
    (0,0,1) t=0 1-step hold
    (0,0,-1) t=1 1-step hold
  fail neighbors (1,0,0) and (0,-1,0)
  universal neighbor-read at (0,0,0): fail

(0,1,0)->(0,1,-1)
  dest t=1; F dest columns (-e_3,-e_1,+e_2); Orient dest=+1
  P=[0 -1 0; 0 0 -1; 1 0 0]; det P=+1; edge hold
  1-step at (0,1,0): hold
  T((0,1,0)) at tau=1:
    (1,1,0) t=1 1-step fail
    (0,2,0) t=1 1-step fail
    (0,0,0) t=0 1-step hold
    (0,1,1) t=0 1-step hold
    (0,1,-1) t=1 1-step fail
  fail neighbors (1,1,0), (0,2,0), and (0,1,-1)
  universal neighbor-read at (0,1,0): fail

(0,0,1)->(0,0,0)
  dest t=0; F dest as origin; Orient dest=+1
  P=[0 1 0; 0 0 -1; 1 0 0]; det P=-1; edge hold
  1-step at (0,0,1): hold
  T((0,0,1)) at tau=1:
    (1,0,1) t=1 1-step hold
    (-1,0,1) t=1 1-step fail
    (0,1,1) t=0 1-step hold
    (0,0,2) t=1 1-step hold
    (0,0,0) t=0 1-step hold
  fail neighbors (-1,0,1)
  universal neighbor-read at (0,0,1): fail

(0,1,1)->(0,1,0)
  dest t=0; F dest as (0,1,0); Orient dest=+1
  P=[0 1 0; 0 0 1; 1 0 0]; det P=+1; edge hold
  1-step at (0,1,1): hold
  T((0,1,1)) at tau=1:
    (1,1,1) t=1 1-step fail
    (-1,1,1) t=1 1-step fail
    (0,0,1) t=0 1-step hold
    (0,1,2) t=1 1-step hold
    (0,1,0) t=0 1-step hold
  fail neighbors (1,1,1) and (-1,1,1)
  universal neighbor-read at (0,1,1): fail
```

All listed vertices lie in `B_3(0)`. Each `det P` equals the product of the
two Orient signs. Each `T(q)` is nonempty. Uniqueness is not used: a single
failing six-neighbor already forces universal fail, and the probes are not
required to share a unique failing neighbor. If 1-step fails at a formed site
such as `(0,-1,0)`, universal neighbor-read fails, not UNDEFINED, even though
origin is a formed six-neighbor with 1-step HOLD.

## Theorem 2

Reverse probes are origin and `(0,1,0)`. Both universal neighbor-read bits
fail, neither is UNDEFINED, so reverse: fail.

## Theorem 3

Face probes are `(0,0,1)` and `(0,1,1)`. Both universal neighbor-read bits
fail, neither is UNDEFINED, so face: fail. Displayed, not adopted. Do not
write into Admissibility. Do not attach L1.

## What this does not show

The packet does not select a physical Record readout, a formation law, a
holonomy identity, or a 4-cycle. It does not write the displayed bits into
Admissibility. It does not attach L1. It does not enlarge Euclidean `B_3(0)`.
It does not claim uniqueness of a failing six-neighbor, nor uniqueness of
`F` among other frame conventions. It does not replace universal
neighbor-read by existential neighbor-read, by the bare directed 1-step bit,
or by undirected transport.
