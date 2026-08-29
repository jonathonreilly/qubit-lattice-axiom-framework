---
claim_id: admissibility_exterior_character_jr_r2_adjacent_product_vector_channel_response_bounded_theorem_note_2026-08-29
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_ADJACENT_PRODUCT_VECTOR_CHANNEL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md
claim_type: bounded_theorem
claim_scope: "For the supplied retain-every-two physical Haar isometry on the actual q=2 original-link O(3) ladder, compute the selected quadratic response between Y=chi_V(delta_1) and Z=chi_V(delta_0)chi_V(delta_1). Prove the complete action-placement and action-irrep selector, the physical-Q cancellation, the exact scalar/axial-vector/spin-two shared-rung Haar weights, and the resulting two-multiplier temporal polynomial. This is one adjacent product-background coordinate, not a closed product-word transfer, invariant subspace, locality theorem, action selection, or physical spin-two identification."
depends_on:
  - admissibility_exterior_character_jr_r2_contiguous_vector_interval_endpoint_automaton_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_r2_nested_merged_vector_interval_response_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28
  - admissibility_exterior_character_co_scaled_temporal_trotter_and_cylindrical_refinement_boundary_bounded_theorem_note_2026-08-28
  - minimal_axioms
dependency_roles:
  admissibility_exterior_character_jr_r2_contiguous_vector_interval_endpoint_automaton_bounded_theorem_note_2026-08-29: "reviewed blocker: product backgrounds require all three V tensor V channels"
  admissibility_exterior_character_jr_r2_nested_merged_vector_interval_response_bounded_theorem_note_2026-08-29: "reviewed original-link ladder, J_2 carrier, changed-cell action placement, and Q method"
  admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28: "supplied action amplitude, temporal convolution, parity-independent ell>=1 multipliers, C J_2=J_2 C_c, and [C,Q]=0"
  admissibility_exterior_character_co_scaled_temporal_trotter_and_cylindrical_refinement_boundary_bounded_theorem_note_2026-08-28: "exact parity independence r_(ell,p)=alpha_n u_ell for ell>=1 on the supplied exterior temporal kernel"
  minimal_axioms: "framework boundary only; no axiom or approved primitive is edited"
runner: scripts/admissibility_exterior_character_jr_r2_adjacent_product_vector_channel_response_2026_08_29.py
independent_checker: scripts/admissibility_exterior_character_jr_r2_adjacent_product_vector_channel_response_independent_2026_08_29.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: null
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_jr_r2_contiguous_vector_interval_endpoint_automaton_bounded_theorem_note_2026-08-29
target_blocker_text: "Resolve the minimal adjacent product-vector background into the scalar, axial-vector, and spin-two shared-rung channels."
source_of_blocker_text: next_trace_action
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Use the three-channel shared-rung alphabet to test the first longer product or multirun vector word; do not claim a closed product-sector transfer until the state alphabet and invariance are proved."
conditional_surface_status: "exact one-coordinate adjacent product-vector response on the supplied r=2 q=2 carrier"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the original-link Haar network, complete action selector, physical-Q cancellation, and exact temporal polynomial are finite mathematical results on a fully disclosed supplied carrier"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Adjacent product-vector shared-rung response at `r=2`

**Date:** 2026-08-29

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — author-side proposal only. The actual surface
is `conditional-support`; independent audit and dependency closure remain
required.

## Result and boundary

On the supplied `r=2`, `q=2` carrier set

```text
Y=chi_V(delta_1),
Z=chi_V(delta_0) chi_V(delta_1).                         (1)
```

These coarse states have unit norm and are orthogonal.  In the selected
quadratic vector-action response

```text
R_epsilon=(1/2) partial_lambda^2 D_epsilon(0),
```

only the two opposite fine-plaquette placements in coarse cell zero survive,
and both action irreps are the defining vector `V=(1,-)`.  The shared retained
rung carries

```text
V tensor V=(0,+) direct-sum (1,+) direct-sum (2,+),       (2)
```

with exact matched-orientation Haar weights

```text
g_0=1/27,       g_1=1/9,       g_2=5/27.                 (3)
```

Let `t=r_(1,-)=r_(1,+)` and `u=r_(2,+)`.  The equality of the two `ell=1`
multipliers is imported from the supplied co-scaled crossing theorem, where
the improper-component density is constant and `r_(ell,p)=alpha_n u_ell` is
parity independent for every `ell>=1`.  It is not a generic `O(3)` assumption.
Define

```text
A=1+3t+5u,          B=1+3t^2+5u^2.                       (4)
```

Then

```text
<Y,R_epsilon Z>
 =epsilon^2(c_V^(n))^2 a_0 a_1 /108
   [t^14 A+t^16(9+2A+B)+t^18 B+t^20(9+A)].              (5)
```

The independent `u` dependence is load-bearing: the scalar-only interval
automaton from Block 235 does not contain enough channel data for this product
background.  Equation (5) is only one offdiagonal coordinate.  It does not
prove a product-word transfer, a closed or invariant vector sector, a locality
or decay theorem, a selected physical action, or a graviton interpretation of
the `(2,+)` gauge-rung channel.  No axiom or approved primitive changes.

## Authorities and imported inputs

| Input | Used here | Not supplied by it |
|---|---|---|
| [Block 235 interval automaton](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_CONTIGUOUS_VECTOR_INTERVAL_ENDPOINT_AUTOMATON_BOUNDED_THEOREM_NOTE_2026-08-29.md) | identifies the product-background blocker | equation (5) |
| [Block 234 nested interval result](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_NESTED_MERGED_VECTOR_INTERVAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md) | original-link geometry, `J_2`, action/Q method | shared-rung channel weights |
| [co-scaled temporal theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_CO_SCALED_TEMPORAL_TROTTER_AND_CYLINDRICAL_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md) | action amplitude, crossing multipliers, parity independence, `C J_2=J_2 C_c`, `[C,Q]=0` | the product-background Haar contraction |
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | framework boundary | any new axiom or primitive |

## Complete action selector and physical `Q`

The coarse occupation words for (1) are `01` and `11`; under retain-every-two
they become fine parity words `0011` and `1111`.  Before assuming any angular
label, equality of original-link inversion parities after two insertions
forces both action irreps to have negative parity and forces their placements
to be the two distinct fine plaquettes `p_0,p_1` of cell zero.  Thus the only
ordered placements are `(p_0,p_1)` and `(p_1,p_0)`.

On the exclusive rail of the shorter-history insertion, Peter--Weyl
orthogonality forces its arbitrary `O(3)` irrep to be `V`.  The other side
requires `V tensor sigma` to contain the scalar; angular momentum and parity
give `sigma=V`.  The explicit `n=1` exterior menu
`{V,det tensor V,det}` is separately exhausted as a control and also leaves
only `(V,V)`; it is not used as the completeness proof.

Write the four first-order histories as `psi_Y0,psi_Y1,psi_Z0,psi_Z1`.  At
fixed `delta_0`, take `W_0=x` and `W_1=delta_0 x^{-1}`.  Haar centering gives

```text
int chi_V(x) dx=0,
int chi_V(delta_0 x^-1) dx=0.                            (6)
```

The `delta_1` factors are spectators, so all four conditional means vanish:
`Q psi_Yi=Q psi_Zi=0`.  The supplied commutator `[C,Q]=0` preserves this after
temporal crossing.  There is therefore no hidden cylindrical subtraction in
this coordinate.

## Original-link channel normalization

Orient

```text
p_j=tr(u_j h_(j+1) v_j^-1 h_j^-1),
C_0=tr(u_0 u_1 h_2 v_1^-1 v_0^-1 h_0^-1),
C_1=tr(u_2 u_3 h_4 v_3^-1 v_2^-1 h_2^-1).              (7)
```

For either matched cross history, multiply the five traces `p_0 C_1` against
`p_1 C_0 C_1` (or the reflected ordering) and leave `h_2` open.  Every one of
the other 11 links appears twice.  Applying

```text
int R_ab R_cd dR=(1/3) delta_ac delta_bd                (8)
```

to those links yields eight closed index classes and four open `h_2` classes.
The closed sums and Haar denominators give `3^8/3^11=1/27`; the open endpoints
are identified in the same order.  Hence the open kernel is exactly
`+I_(V tensor V)/27`, not a swapped kernel.

The exact scalar, antisymmetric/axial, and symmetric-traceless projectors are
complete orthogonal idempotents with traces `(1,3,5)`.  Contracting them with
the open kernel proves

```text
g_L=(1/27) Tr P_L=d_L/27,       d_L=(1,3,5),             (9)
```

and `sum_L g_L=1/3` for each matched orientation.  In particular the
antisymmetric channel has positive weight; an unnoticed endpoint swap would
instead introduce a sign and fail the original-link identity certificate.

## Temporal histories

Put `x_L=(1,t,u)` for `L=0,1,2`.  Direct original-link incidence gives

| History | coarse/background crossing | changed-history crossing |
|---|---:|---:|
| `Y, p_0` | `t^6` | `t^10` |
| `Y, p_1, L` | `t^6` | `t^8 x_L` |
| `Z, p_1, L` | `t^10 x_L` | `t^10` |
| `Z, p_0, L` | `t^10 x_L` | `t^8 x_L` |

Combining the two half-action orientations with (9) gives first

```text
epsilon^2(c_V^(n))^2 a_0a_1/108 sum_L d_L [
 (t^6+t^10)t^10(1+x_L)
 +(t^6+t^8 x_L)x_L(t^10+t^8)].                         (10)
```

Exact expansion of (10) is (5).  This channel-first form is the primary
guard against deleting or misplacing the shared-rung multiplier.

At `t=u=1`, the bracket in (5) is 72 and the coefficient is `2/3`, exactly the
two raw cross overlaps `1/3+1/3` when `C=I`.  At `t=0` it vanishes.  For
positive supplied `t,u`, the derivative with respect to `u` is positive; for
signed `a_0a_1`, equation (5) has the corresponding matrix-entry sign.  This
is not operator or reflection positivity.

## What remains open

- the diagonal product-background block and closure of any product-word span;
- the next longer product or multirun vector history and its recoupling state;
- a finite-memory automaton for the full vector kernel;
- arbitrary `r` multicell product backgrounds;
- physical action selection, time/distance, continuum, Lorentzian, gravity,
  metric/source, matter-current, or graviton identification.

## No-Go Discipline Gate

### N1 — live alternatives

The live routes are the next longer product word, a two-run merged word, the
diagonal block, and arbitrary `r`.  Only the first minimal product coordinate
was attempted here.

### N2 — collapse conditions

The result collapses if the original-link open kernel is swapped or differs
from `I/27`, if a nonvector action irrep survives, if any conditional mean is
nonzero, or if the supplied parity-independent crossing relation fails.

### N3 — nontriviality

The new content is the exact three-channel normalization and the load-bearing
spin-two multiplier in (5), not generic compact-group character positivity.

### N4 — assumption firewall

The action, crossing, `J_2`, and `Q` are supplied.  No action-selection,
continuum, geometric, or physical-source input is added.

### N5 — breadth

The proof is per original link and per shared-rung channel for one `r=2,q=2`
coordinate.  It is not lattice-wide or a full-block classification.

### N6 — interpretation firewall

The label `(2,+)` is an `O(3)` gauge-rung representation channel.  It is not a
spacetime spin or graviton claim, and `t,u` are not identified with time or
distance.

### N7 — prior art

Projector ranks and compact-group Haar positivity are standard.  The proposed
conditional claim is their exact placement and normalization in this supplied physical
compression-defect coordinate.

### N8 — honest next step

The next test must enlarge the product/multirun word while retaining all three
channels.  Failure of the scalar interval alphabet proves only that that
alphabet is insufficient; it does not prove that no finite automaton exists.
