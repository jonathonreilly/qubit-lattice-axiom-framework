---
claim_id: admissibility_exterior_character_jr_r2_q3_oriented_vector_triple_channel_resolution_bounded_theorem_note_2026-08-29
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_ORIENTED_VECTOR_TRIPLE_CHANNEL_RESOLUTION_BOUNDED_THEOREM_NOTE_2026-08-29.md
claim_type: bounded_theorem
claim_scope: "For one supplied r=2, q=3 nested product of defining-vector exterior characters on the actual original-link O(3) ladder, prove the complete action selector and physical-Q cancellation, exactly contract both oriented open Haar networks, derive the convention-fixed vector Racah block from the contracted strand map, and show that the first triple-overlap history resolves into seven finite multiplicity channels rather than the previous three pair irreducible channels. This is finite channel-resolution growth, not a minimal-memory theorem, a complete temporal response, an arbitrary-word theorem, unbounded growth, an invariant sector, locality, dynamics, physical action selection, or a physical interpretation."
depends_on:
  - admissibility_exterior_character_jr_r2_q3_gap_fill_product_vector_response_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_r2_adjacent_product_vector_channel_response_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28
  - minimal_axioms
dependency_roles:
  admissibility_exterior_character_jr_r2_q3_gap_fill_product_vector_response_bounded_theorem_note_2026-08-29: "reviewed q=3 product-word checkpoint and the orientation-sensitive overlapping-word blocker"
  admissibility_exterior_character_jr_r2_adjacent_product_vector_channel_response_bounded_theorem_note_2026-08-29: "reviewed scalar, axial-vector, and spin-two pair channels on the first adjacent product"
  admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28: "supplied exterior action amplitude, original-link ladder, J_2, Q, crossing, and commutators"
  minimal_axioms: "framework boundary only; no axiom or approved primitive is edited"
runner: scripts/admissibility_exterior_character_jr_r2_q3_oriented_vector_triple_channel_resolution_2026_08_29.py
independent_checker: scripts/admissibility_exterior_character_jr_r2_q3_oriented_vector_triple_recoupling_independent_2026_08_29.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_jr_r2_q3_gap_fill_product_vector_response_bounded_theorem_note_2026-08-29
target_blocker_text: "Compute the orientation-sensitive 3 by 3 Racah matrix for the first overlapping merged/product word; do not infer closure or failure from V-cubed multiplicities alone."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Compute the temporal crossing multipliers and complete response on all seven allowed (L,J) triple channels; then test whether any channels are dynamically identified before making a memory-minimality claim."
conditional_surface_status: "exact one-coordinate q=3 oriented original-link open kernels and finite three-to-seven multiplicity-channel resolution"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the selectors, physical-Q cancellation, O(3) Haar tensors through sixth moment, both open kernels, and representation decomposition are finite exact results on a fully disclosed supplied carrier"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The first oriented vector-triple channel resolution at `r=2`, `q=3`

**Date:** 2026-08-29

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — author-side proposal only.  The actual current
surface is `conditional-support`; independent audit and closure of the stacked
dependencies remain required.

## Result and boundary

On the supplied retain-every-two `r=2`, `q=3` carrier, write

```text
A=chi_V(delta_0),
D=chi_V(delta_1 delta_0),
E=chi_V(delta_2 delta_1 delta_0),
Y=D E,
Z=A D E.                                                   (1)
```

The two states are normalized and orthogonal.  In the selected quadratic
vector-action response only

```text
O01=(p_0 Y,p_1 Z),       O10=(p_1 Y,p_0 Z)                 (2)
```

survive.  Both insertions are forced to the defining vector `V=(1,-)`, and all
four first-order histories lie in `ker Q`.

Leave the shared original link `h_0` open.  Exact rational `O(3)` integration
of the remaining sixteen links gives

```text
K01=(1/81) I_V tensor I_V tensor I_V,                      (3)
K10=(1/81) [scalar cup on p_0 tensor A]
             tensor I_(D,D) tensor I_(E,E).                (4)
```

Equation (3) acts on all of

```text
V tensor V tensor V
 =(0,-) direct-sum 3(1,-) direct-sum 2(2,-) direct-sum (3,-). (5)
```

Thus a coupling basis labelled by the old pair spin `L=0,1,2` and the total
spin `J` contains exactly seven allowed routes,

```text
(L,J)=(0,1),
      (1,0),(1,1),(1,2),
      (2,1),(2,2),(2,3).                                  (6)
```

The three pair irreducible labels do not by themselves resolve the complete
triple tensor decomposition.  The exact algebraic statement proved here is
finite channel-resolution growth: three pair irreducible channels become seven
`(L,J)` triple coupling channels.  It is not a theorem that seven states are
minimal dynamical memory: the temporal response could identify channels.  It
does not prove unbounded growth.  The complete temporal response remains open.

### Exact proof target and obligation graph

The exact target is the bounded statement (1)--(14): for the supplied
`r=2`, `q=3` action and physical projector `Q`, the only selected quadratic
vector histories are (2), their open original-link tensors are (3)--(4), and
the same-orientation tensor (3) resolves into exactly the seven coupling
routes (6) with weights (13)--(14) and convention-fixed vector Racah block
(11).  No temporal-response or minimal-memory conclusion is part of the
target.

| Obligation | Discharge in this note | Dependency boundary |
|---|---|---|
| normalize `Y,Z` and prove orthogonality | independent Haar coordinates in (7) and the zero first moment of `A` | normalized Haar measure from the supplied action |
| exhaust action selectors and their irreps | fine-word enumeration leaves (2); the scalar-in-`V tensor (ell,p)` rule forces both insertions to `V` | action menu from the supplied action/defect theorem |
| put all four histories in `ker Q` | every conditional vector-entry mean vanishes and `[C,Q]=0` preserves the result | the supplied definitions of `Q` and crossing `C` |
| compute both open kernels | exact second-, fourth-, and sixth-moment Brauer contractions give (3)--(4) entrywise | exact `O(3)` Haar calculus, independently reconstructed |
| identify the physical strand permutation | occurrence matching in (9)--(10) gives the inverse slot map `(2,0,1)` | no imported Racah orientation |
| decompose the same-orientation kernel | `V tensor V tensor V` gives (5)--(6), (11), and weights (13)--(14) | standard `O(3)` tensor-product rules, checked by explicit Cartesian intertwiners |
| delimit the reverse orientation | (4) is a scalar cup in the fifteen-dimensional `Hom_O(3)(V^2,V^4)` space, not a `3 by 3` Racah block | no reduction beyond the exact cup tensor is claimed |

The hypotheses exclude any altered action, projector, refinement order,
exterior irrep, or temporal multiplier.  Degenerate cases are explicit: a
selector outside (2) is zero; an insertion irrep other than `V` has no scalar
rail and is zero; the reverse orientation remains the cup tensor (4) rather
than being forced into the same-orientation coupling basis.  The strongest
missing downstream lemma is the exact supplied temporal multiplier on every
route in (6).  It is not needed for the bounded channel-resolution theorem,
but it is required before any channel-identification or memory claim.

## Authorities and recomputed inputs

| Input | Used here | Recomputed here |
|---|---|---|
| [Block237 gap fill](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_GAP_FILL_PRODUCT_VECTOR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md) | reviewed q=3 checkpoint and named Racah blocker | the nested-product state and both open kernels |
| [Block236 pair channels](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_ADJACENT_PRODUCT_VECTOR_CHANNEL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md) | pair projectors and their three-label boundary | all triple-channel routes and orientation phases |
| [supplied action/defect theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md) | action menu, `J_2`, `Q`, and original-link ladder | the selectors, conditional means, and Haar contractions |
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | framework boundary | no axiom or approved primitive |

The independent checker constructs the second, fourth, and sixth `O(3)` Haar
moments from exact Brauer Gram inverses and contracts the original-link indices
with Python integers and rational denominators.  No floating tolerance carries
(3) or (4).

## Imports

| Input | Role | Provenance | Open bridge status |
|---|---|---|---|
| supplied `r=2` exterior action, original-link ladder, `J_2`, and `Q` | defines the action selector and physical projection tested here | linked supplied action/defect theorem above | its independent audit and the stacked dependency chain remain pending |
| exact `O(3)` Haar/Brauer calculus through degree six | computes both open tensors | standard representation-theory machinery, reconstructed independently in the paired checker | no numerical or physical import; every tensor entry used here is recomputed |
| displayed real Cartesian intertwiner phases | fixes the signs of (11) | basis convention defined by the explicit tensors in the paired checker | no physical bridge; only phase-invariant content is used outside the displayed convention |

No fitted value, observation, continuum identification, metric, source,
statistics premise, or gravity premise enters the calculation.

## Gram, selector, and physical `Q`

The triangular Haar change of variables

```text
A=delta_0,
D=delta_1 delta_0,
E=delta_2 delta_1 delta_0                             (7)
```

has inverse `delta_0=A`, `delta_1=D A^-1`,
`delta_2=E D^-1` and Haar Jacobian one.  Hence `A,D,E` are independent
normalized Haar coordinates.  Equation (1) then has unit norms, while its
overlap contains the zero first moment of `A`.

The fine parity words are `000011` for `Y` and `110011` for `Z`.  Exhausting
both insertion locations and both inversion parities leaves exactly (2), with
negative parity on each action.  An exclusive vector rail forces the first
insertion to `V`; a scalar occurs in `V tensor (ell,p)` only at `(ell,p)=V`, so
the partner is also `V`.  This is the complete arbitrary-`O(3)` selector, not
an imported choice of action irrep.

At fixed `delta_0`, the two relevant fine plaquette variables can be written
`W_0=x` and `W_1=delta_0 x^-1`.  All nine entry means of Haar `x` vanish, so
both vector characters have zero conditional mean.  The four first-order
histories therefore lie in `ker Q`; the supplied commutator `[C,Q]=0` preserves
that status after crossing.

## Exact oriented original-link tensors

The seven trace factors in either orientation contain eight links at second
Haar moment, four at fourth moment, four at sixth moment, and the open `h_0`.
For `O01`, three strands occur on each side of `h_0`.  The exact contraction of
all other links has 729 nonzero Cartesian entries, each equal to `1/81` exactly
when the three left strands match their three right partners and zero otherwise.
This proves (3), including its same-order orientation.

For `O10`, two strands occur on the left and four on the right.  Its 729
nonzero entries instead impose the scalar cup between the inserted `p_0` and
`A` strands and match the `D` and `E` strands across the two sides.  This proves
(4).  The ambient invariant space `Hom_O(3)(V^2,V^4)` has dimension fifteen;
there is no honest `3 by 3` Racah interpretation of this orientation.  The
specific cup in (4) selects its scalar factor and leaves the three diagonal
pair weights

```text
d_L/27=(1/27,3/27,5/27),   L=0,1,2.                      (8)
```

Their sum is `1/3`.

## Convention-fixed vector Racah block and all seven channels

Use normalized Cartesian intertwiners from `V^3` to the three copies of `V`.
The `O01` open-occurrence order is

```text
left:  (p_0,D,E),       right: (A,D,E).                  (9)
```

Equation (3) pairs `p_0<->A`, `D<->D`, and `E<->E`.  The physical coupling
orders are

```text
left rows:  ((D,E)->L,p_0),
right cols: ((A,D)->M,E).                                (10)
```

Thus left tensor indices `(a,b,c)=(D,E,p_0)` populate the right physical
slots `(A,D,E)` as `(c,a,b)`.  The independent runner derives this inverse
permutation `(2,0,1)` from the contracted occurrence names before evaluating
the intertwiner overlap.  In the displayed real Cartesian phase convention,
the resulting row-left/column-right matrix is

```text
G=[[1/3,       -sqrt(3)/3,  sqrt(5)/3],
   [sqrt(3)/3, -1/2,       -sqrt(15)/6],
   [sqrt(5)/3,  sqrt(15)/6, 1/6       ]].                (11)
```

Exactly,

```text
G^T G=I,       det G=1,       G^3=I.                     (12)
```

Independent sign rephasings of the three left or right intertwiners multiply
`G` by diagonal sign matrices; those are basis changes, not different network
physics.  Equation (11), including `det G=1` and `G^3=I`, is exact in the
globally identified Cartesian/cyclic convention used here.  Under independent
left/right rephasings, orthogonality, singular values, and `|det G|=1` remain
invariant, but the determinant sign and order-three identity need not.

The vector-multiplicity response is `G/27`.  It is one isotypic subblock of
(3), not the complete open kernel.  For every route in (6), the raw identity-
kernel weight is

```text
w_(L,J)=d_J/81.                                           (13)
```

The seven weights are

```text
3/81;
1/81,3/81,5/81;
3/81,5/81,7/81,                                           (14)
```

and sum to `27/81=1/3`.  Equivalently, (5) has isotypic dimensions
`1,9,10,7`, totaling 27.  The two raw orientation closures are therefore
`1/3+1/3`.  This identity-limit normalization is not a completed response:
the supplied temporal theorem has not yet been evaluated on every `(L,J)`
triple channel.

## What remains open

- the temporal multiplier and full selected response on all seven routes (6);
- arbitrary nested products, longer histories, whether channels are
  dynamically identified, and whether minimal memory remains bounded;
- an invariant product-word span or a full vector transfer operator;
- other exterior irreps and arbitrary refinement order;
- action selection, locality, physical time or distance, continuum or
  Lorentzian dynamics, gravity, metric/source, matter-current, or particle
  interpretation.

No axiom or approved primitive changes.

## Review record

Hostile review removed the draft's inference from seven resolved channels to
seven minimal dynamical memory states.  The retained statement is the positive
finite channel-resolution theorem above.  Review also replaced a hard-coded
Racah orientation with the occurrence-level strand map (9)-(10), separated
phase-invariant content from convention-fixed determinant/order data, and
replaced a finite spin scan with the exact arbitrary-`O(3)` selector argument.
The theorem's boundary ends before the temporal response and any memory-
minimality statement.

## No-go-discipline applicability

The N1-N8 gate is not triggered: this note asserts no route closure, no
impossibility theorem, no required new axiom, and no bounded claim conditional
on named residual walls.  The items under **What remains open** are unattempted
future computations, not claims that those computations fail or are necessary.
The next positive calculation is the seven-channel temporal response.
