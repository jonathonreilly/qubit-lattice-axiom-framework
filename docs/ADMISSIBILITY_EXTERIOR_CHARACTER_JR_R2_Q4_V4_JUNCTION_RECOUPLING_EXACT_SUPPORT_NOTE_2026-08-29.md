---
claim_id: admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_support_note_2026-08-29
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_V4_JUNCTION_RECOUPLING_EXACT_SUPPORT_NOTE_2026-08-29.md
claim_type: bounded_theorem
title: Exact support for non-diagonal scalar recoupling at the first four-vector junction
claim_scope: "For one supplied r=2, q=4 nested product of defining-vector exterior characters on the actual original-link O(3) ladder, prove the two parity-allowed action orientations and exactly contract the new K=0 four-vector junction. For O01, derive the full non-diagonal three-by-three scalar multiplicity block over Q. For O10, derive one explicitly unnormalized determinant/cup row overlap over Q and its row-projected eight-index cup/identity endpoint over three declared prime fields. Prove the degree-eight Brauer rank is 91 on those fields and use an explicit independent subbasis. This is finite conditional junction support, not a complete V^4 commutant, the K=1,2,3,4 blocks, a full q=4 temporal response, minimal or unbounded transfer memory, arbitrary words, physical action selection, time, continuum dynamics, gravity, or a theory of everything."
depends_on:
  - admissibility_exterior_character_jr_r2_q3_seven_channel_temporal_response_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_r2_q3_oriented_vector_triple_channel_resolution_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28
  - minimal_axioms
dependency_roles:
  admissibility_exterior_character_jr_r2_q3_seven_channel_temporal_response_bounded_theorem_note_2026-08-29: "supplies the exact q=3 route-resolved checkpoint and the explicit q=4 multiplicity-junction next target"
  admissibility_exterior_character_jr_r2_q3_oriented_vector_triple_channel_resolution_bounded_theorem_note_2026-08-29: "supplies the original-link strand conventions, action-selector machinery, and exact q=3 recoupling boundary"
  admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28: "supplies the exterior action, original-link ladder, J_2, and crossing definitions; its Q and response are inherited but unused here"
  minimal_axioms: "framework boundary only; no axiom or approved primitive is edited"
runner: scripts/admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_2026_08_29.py
date: 2026-08-29
status: exact-support
actual_current_surface_status: exact-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: admissibility_exterior_character_jr_r2_q3_seven_channel_temporal_response_bounded_theorem_note_2026-08-29
target_blocker_text: "After independent review, test the first q=4 word with an uncoupled V^4 multiplicity junction. Do not infer a global minimal-memory theorem from one route-resolved q=3 response."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Resolve the K=1,2,3,4 multiplicity blocks and the seven odd V^3 residual routes, then insert the supplied central multipliers and test the complete finite q=4 temporal response."
conditional_surface_status: "exact O01 scalar multiplicity block over Q and exact unnormalized O10 row overlap over Q, with a three-field row-projected O10 endpoint certificate, conditional on the supplied open Block232--239 stack"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the O01 scalar multiplicity block and O10 unnormalized determinant/cup row overlap are exact rational original-link contractions, while the projected O10 endpoint tensor is exhaustively checked over three declared fields on a fully disclosed finite carrier"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The first `q=4` defining-vector junction has non-diagonal `K=0` recoupling

**Date:** 2026-08-29

**Type:** `bounded_theorem`

**Status:** `exact-support` — the actual current surface is exact support on the
supplied Block232--239 Class-C construction; independent audit and the stacked
dependency chain remain pending.

**Current-surface effect:** upstream support for the open minimal-transfer-memory problem

**Axiom/primitive effect:** none

## Result

Work at the same finite `r=2` strip coordinate and with the same supplied
defining-vector action used by Blocks232--239.  Put

\[
 A=\delta_0,\qquad D=\delta_1\delta_0,\qquad
 E=\delta_2\delta_1\delta_0,\qquad
 F=\delta_3\delta_2\delta_1\delta_0,
\]

and define

\[
 Y=\chi_V(D)\chi_V(E)\chi_V(F),\qquad
 Z=\chi_V(A)Y.
\]

The parity words leave the same two cell-zero orientations as at `q=3`:
`O01=(p0Y,p1Z)` and `O10=(p1Y,p0Z)`.  The supplied scalar action selector
forces the inserted irrep to be `V` on both rails.  This note resolves the
new four-vector junction created at the open link `h0`.

For `O01`, couple the four defining vectors sequentially as
`((V tensor V)_L tensor V)_{J=1} tensor V -> K=0`.  The three allowed paths
are labelled by `L=0,1,2`.  In the integer Cartesian invariant basis

\[
\begin{aligned}
R_0&=\delta_{ab}\delta_{ce},\\
R_1&=\delta_{ac}\delta_{be}-\delta_{ae}\delta_{bc},\\
R_2&=3(\delta_{ac}\delta_{be}+\delta_{ae}\delta_{bc})
      -2\delta_{ab}\delta_{ce},
\end{aligned}
\]

whose squared norms are `(9,12,180)`, exact rational contraction of all
non-`h0` original links gives

\[
 K_{01}^{\rm raw}=\frac1{81}
 \begin{pmatrix}
 1&-2&10\\[-1mm]
 -2&2&10\\[-1mm]
 10&10&10
 \end{pmatrix}.
\]

After normalizing the three invariants, this is

\[
 K_{01}^{K=0}=\frac1{243}U_0,
 \qquad
 U_0=
 \begin{pmatrix}
 \frac13&-\frac{\sqrt3}{3}&\frac{\sqrt5}{3}\\
 -\frac{\sqrt3}{3}&\frac12&\frac{\sqrt{15}}6\\
 \frac{\sqrt5}{3}&\frac{\sqrt{15}}6&\frac16
 \end{pmatrix}.
\]

Here `U0` is symmetric and orthogonal, `det(U0)=-1`, `tr(U0)=1`, and every
off-diagonal entry is nonzero.  Thus the `q=4` crossing is not diagonal in the
old pair-channel label: a same-`L` scalar-multiplier shortcut already fails in
the `K=0` block.  This does not prove that `(L,J)` is an insufficient state
coordinate or establish a minimal enlarged memory.  Deciding that requires the
remaining `K=1,2,3,4` multiplicity blocks and their subsequent propagation.

For `O10`, `h0` carries `V^3` on the left and `V^5` on the right.  The latter
has six spin-zero copies.  The cup topology used here selects one particular
vector in that six-dimensional scalar multiplicity space; it does not resolve
the other five copies.  Contracting the row endpoint with raw epsilon tensors
on the two `V^3` triples and a raw delta cup on `(p0,A)` gives exactly
`18/243=2/27` over the rationals.  This is an explicitly **unnormalized raw
overlap**: the raw epsilon and cup have squared norms `6` and `3`, respectively,
so `2/27` is not a normalized determinant-channel weight.

After that same raw row projection, the remaining `3^8` column-endpoint tensor
was exhaustively enumerated over `F_1009`, `F_1013`, and `F_1019`.  In each
field it has exactly 81 nonzero entries, each with coefficient `2/27` modulo
the field, on the `cup(p0,A) tensor I(D,E,F)` support and no mismatches.  This
is an exact three-field certificate for the row-projected endpoint, not a
symbolic identity over `Q` for the complete unprojected `3^16` tensor.  In
particular, the tempting unprojected coefficient `1/243` and the associated
normalized-route value `1/81` are not source results here.

## Exact proof target and obligation graph

The exact target is the finite statement above: on the supplied `r=2,q=4`
carrier, the two selected orientations expose the displayed four-vector
junctions; the `O01` scalar multiplicity block is the rational matrix `U0/243`;
and the `O10` unnormalized raw row overlap and row-projected endpoint have the
stated coefficients and strand placement.  A complete `q=4` response is not
part of the target.

| Obligation | Discharge here | Dependency boundary |
|---|---|---|
| exhaust parity/action orientations | explicit finite fine-word enumeration leaves `O01,O10`, with the vector insertion fixed by the supplied action selector | action menu is supplied by the linked action/defect theorem; `Q` is unused here |
| represent the degree-eight Haar moment without a singular inverse | construct 105 pairings, select a 91-dimensional subbasis, and invert only its Gram block | standard finite `O(3)` Haar/Brauer calculus |
| compute the `O01` scalar block | exact rational contraction of all non-`h0` links gives all nine entries, then invariant norms give `U0/243` | strand order follows the linked `q=3` original-link convention |
| compute the `O10` raw overlap and projected endpoint | exact rational unnormalized row contraction plus exhaustive three-field `3^8` endpoint comparison | no normalized determinant-channel weight or complete unprojected `3^16` identity is claimed |
| delimit temporal consequences | even and odd scalar parities are kept distinct; all non-scalar multiplicity blocks remain open | central multipliers and response definition are supplied by the linked stack |

The boundary and degenerate cases are explicit: only `r=2,q=4`, the displayed
nested word, normalized `O(3)` Haar measure, and the two selected orientations
are covered.  Altered actions, projectors, words, groups, endpoint orderings,
or modular characteristics outside the declared primes are not covered.  The
strongest missing lemma is the exact original-link contraction of every
`K=1,2,3,4` multiplicity block and the seven odd residual routes.

## Why degree eight is not a routine extension

At degree eight there are 105 Brauer pairings but the `O(3)` Gram matrix has
rank 91.  Inverting the 105 by 105 matrix, or applying a floating pseudoinverse,
would be invalid.  Both runners select an explicit 91-pairing independent
subbasis and use

\[
 \mathbb E[O^{\otimes8}]=B\,G_B^{-1}B^T.
\]

This keeps the computation memory-safe and makes the singularity visible.
The reopened-link moment census is `{2:9, 4:4, 6:4, 8:4}` for both
orientations.

## Temporal and parity boundary

No full `q=4` temporal response is claimed here.  For later use, the even
four-vector sectors have central multipliers indexed by total spin
`K=0,1,2,3,4`, with the even scalar `K=0` multiplier equal to `1`.  By contrast,
the selected `O10` raw determinant/cup overlap is odd and would carry the
determinant multiplier in a later response calculation.  Replacing either
scalar parity by the other is a parity error.

This block does **not** establish all `K=1,2,3,4` multiplicity blocks, the full
nineteen-path temporal response, arbitrary `q`, arbitrary words, minimal or
unbounded memory, locality, physical time, gravity, or a theory of everything.

## Reproduction

**Primary runner:**
`scripts/admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_2026_08_29.py`

Fast exact-field and projected-endpoint certificate:

```bash
python3 scripts/admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_2026_08_29.py
```

Exact-rational decisive-block certificate (expected runtime under 180 seconds):

```bash
python3 scripts/admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_2026_08_29.py
```

Observed results are `24/24` and `27/27`, respectively.  The exact-rational
script is the audit primary: it imports the finite-field runner, executes its
24 checks, and adds three rational checks.  This creates a discoverable
primary/helper source chain, not two independent implementations.

## Authority and import boundary

- The action family and original-link construction are supplied by the
  [`J_r` action/defect theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md).
  Its physical conditional expectation `Q` and response definition are
  inherited context but are not used or discharged by this junction proof.
- The original-link geometry and `q=3` recoupling machinery are supplied by the
  [oriented vector-triple theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_ORIENTED_VECTOR_TRIPLE_CHANNEL_RESOLUTION_BOUNDED_THEOREM_NOTE_2026-08-29.md)
  and its [seven-route temporal response](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_SEVEN_CHANNEL_TEMPORAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md).
- Blocks232--239 are open stacked Class-C proposals.  This note is therefore
  an exact-support child on that explicit dependency stack, not an
  audit-ratified retained result.
- The framework boundary remains the four
  [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md); none is changed or extended.
- No axiom, approved primitive, authority registry, active review queue, or
  canonical harness is changed.

## Remaining hard residual

The next exact step is to resolve the `K=1,2,3,4` multiplicity blocks and the
seven odd `V^3` residual routes, then insert the correct central temporal
multipliers and test the full `q=4` response.  Only after that calculation can
one assess whether a finite path-memory transfer law closes beyond the scalar
junction.
