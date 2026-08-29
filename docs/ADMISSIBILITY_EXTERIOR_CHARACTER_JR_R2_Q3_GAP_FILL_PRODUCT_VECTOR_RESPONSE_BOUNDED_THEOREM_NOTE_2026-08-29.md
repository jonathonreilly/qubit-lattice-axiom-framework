---
claim_id: admissibility_exterior_character_jr_r2_q3_gap_fill_product_vector_response_bounded_theorem_note_2026-08-29
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_GAP_FILL_PRODUCT_VECTOR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md
claim_type: bounded_theorem
claim_scope: "For the supplied retain-every-two physical Haar isometry on the actual q=3 original-link O(3) ladder, compute the selected quadratic response between the split singleton-product words Y=chi_V(delta_0)chi_V(delta_2) and Z=chi_V(delta_0)chi_V(delta_1)chi_V(delta_2). Prove the complete action selector, physical-Q cancellation, both two-rung Haar kernels, the exact nine channel weights, and the resulting two-multiplier temporal response. This is one central gap-fill coordinate, not arbitrary-q product closure, an invariant sector, a full vector kernel, locality, action selection, or a physical interpretation."
depends_on:
  - admissibility_exterior_character_jr_r2_adjacent_product_vector_channel_response_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_r2_contiguous_vector_interval_endpoint_automaton_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28
  - admissibility_exterior_character_co_scaled_temporal_trotter_and_cylindrical_refinement_boundary_bounded_theorem_note_2026-08-28
  - minimal_axioms
dependency_roles:
  admissibility_exterior_character_jr_r2_adjacent_product_vector_channel_response_bounded_theorem_note_2026-08-29: "reviewed two-vector projectors, channel multipliers, and the first product-background blocker"
  admissibility_exterior_character_jr_r2_contiguous_vector_interval_endpoint_automaton_bounded_theorem_note_2026-08-29: "prior-art boundary separating this split product word from the single merged-interval family"
  admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28: "supplied exterior action amplitude, original-link ladder, J_2 and Q, temporal convolution, C J_2=J_2 C_c, and [C,Q]=0"
  admissibility_exterior_character_co_scaled_temporal_trotter_and_cylindrical_refinement_boundary_bounded_theorem_note_2026-08-28: "normalized ell>=1 crossing multipliers and parity independence r_(ell,p)=alpha_n u_ell"
  minimal_axioms: "framework boundary only; no axiom or approved primitive is edited"
runner: scripts/admissibility_exterior_character_jr_r2_q3_gap_fill_product_vector_response_2026_08_29.py
independent_checker: scripts/admissibility_exterior_character_jr_r2_q3_gap_fill_product_vector_response_independent_2026_08_29.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: null
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_jr_r2_adjacent_product_vector_channel_response_bounded_theorem_note_2026-08-29
target_blocker_text: "Use the three-channel shared-rung alphabet to test the first longer product or multirun vector word."
source_of_blocker_text: next_trace_action
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Compute the orientation-sensitive 3 by 3 Racah matrix for the first overlapping merged/product word; do not infer closure or failure from V-cubed multiplicities alone."
conditional_surface_status: "exact one-coordinate q=3 singleton-product gap-fill response on the supplied r=2 carrier"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the original-link Haar network, complete selector, physical-Q cancellation, and temporal polynomial are finite exact results on a fully disclosed supplied carrier"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The first two-rung product-vector gap fill at `r=2`, `q=3`

**Date:** 2026-08-29

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — author-side proposal only.  The actual current
surface is `conditional-support`; independent audit and closure of the stacked
dependencies remain required.

## Result and boundary

On the supplied `r=2`, `q=3` carrier, take the split singleton-product states

```text
Y=chi_V(delta_0) chi_V(delta_2),
Z=chi_V(delta_0) chi_V(delta_1) chi_V(delta_2).          (1)
```

They are normalized and orthogonal.  In the selected quadratic vector-action
response

```text
R_epsilon=(1/2) partial_lambda^2 D_epsilon(0),
```

only the two opposite fine-plaquette placements in the missing central cell
survive, both action irreps are `V=(1,-)`, and all four first-order histories
lie in `ker Q`.  The two retained rungs adjacent to that cell independently
carry

```text
V tensor V=(0,+) direct-sum (1,+) direct-sum (2,+).      (2)
```

For `L,M=0,1,2`, with `d=(1,3,5)`, their exact joint Haar weights are

```text
g_(L,M)=d_L d_M/243.                                    (3)
```

Let `t=r_(1,-)=r_(1,+)` and `u=r_(2,+)`, with the equality of the two spin-one
multipliers imported only from the supplied co-scaled parity-independent
crossing theorem.  Put

```text
x=(1,t,u),
A=sum_L d_L x_L=1+3t+5u,
B=sum_L d_L x_L^2=1+3t^2+5u^2.                          (4)
```

Then

```text
<Y,R_epsilon Z>
 =epsilon^2(c_V^(n))^2 a_2 a_3 /486
   t^14 (9+A)(t^12 A+t^14 B).                          (5)
```

Equation (5) is the first exact two-sided, two-rung test of the Block236
three-channel alphabet.  It proves that alphabet suffices for this one binary
singleton-product gap fill.  It does not prove arbitrary-`q` product-word
closure, invariance, a full transfer operator, locality, continuum dynamics,
or a gravity or particle interpretation.  No axiom or approved primitive
changes.

## Authorities and recomputed inputs

| Input | Used here | Recomputed here |
|---|---|---|
| [Block236 product-vector entry](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_ADJACENT_PRODUCT_VECTOR_CHANNEL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md) | the three `V tensor V` projectors and named blocker | the complete two-rung original-link kernel and response |
| [Block235 interval automaton](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_CONTIGUOUS_VECTOR_INTERVAL_ENDPOINT_AUTOMATON_BOUNDED_THEOREM_NOTE_2026-08-29.md) | prior-art boundary | the split-product word calculation |
| [supplied action/defect theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md) | action amplitude, `J_2`, `Q`, crossing, and commutators | the `q=3` Gram, selectors, Haar contractions, and temporal exponents |
| [co-scaled temporal theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_CO_SCALED_TEMPORAL_TROTTER_AND_CYLINDRICAL_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md) | normalized multipliers and parity independence | no new temporal law |
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | framework boundary | no axiom or primitive |

## Gram, action selector, and physical `Q`

In independent coarse plaquette-Haar coordinates, (1) has occupation words
`101` and `111`.  Their norms are one and their overlap contains the first
moment `int chi_V(delta_1)d delta_1=0`.

Under retain-every-two, the words become fine parity words `110011` and
`111111`.  Before assuming an angular label, equality after two insertions
forces both action irreps to have negative inversion parity and leaves exactly

```text
(p_Y,p_Z)=(p_2,p_3), (p_3,p_2).                         (6)
```

The exclusive middle rails force the first insertion to be `V`; the scalar in
`V tensor sigma` on the opposite history exists only for `sigma=V`.  Thus the
complete arbitrary-`O(3)` selector is `(V,V)`.  Exhausting the supplied
`n=1` exterior menu separately gives the same answer.

At fixed `delta_1`, write the two fine central plaquette holonomies as
`W_2=x` and `W_3=delta_1 x^-1`.  The outer factors in (1) are spectators and

```text
int chi_V(x)dx=0,
int chi_V(delta_1 x^-1)dx=0.                            (7)
```

All four first-order histories therefore have zero conditional mean and lie
in `ker Q`; `[C,Q]=0` preserves this after temporal crossing.  There is no
hidden cylindrical subtraction in (5).

## Two-rung original-link kernel

Orient the fine plaquettes and three coarse loops as

```text
p_j=tr(u_j h_(j+1) v_j^-1 h_j^-1),
C_0=tr(u_0u_1 h_2 v_1^-1v_0^-1 h_0^-1),
C_1=tr(u_2u_3 h_4 v_3^-1v_2^-1 h_2^-1),
C_2=tr(u_4u_5 h_6 v_5^-1v_4^-1 h_4^-1).                (8)
```

The two matched cross networks are

```text
p_2 C_0 C_2  against  p_3 C_0 C_1 C_2,
p_3 C_0 C_2  against  p_2 C_0 C_1 C_2.                 (9)
```

Leave `h_2,h_4` open.  Every other one of the 15 original links appears
exactly twice.  Applying `int R_ab R_cd dR=delta_ac delta_bd/3` gives ten
closed index classes and eight open classes, hence coefficient
`3^10/3^15=1/243`.  In both orientations the endpoints are identified in the
same order independently at each rung, and the two sets of open classes are
disjoint.  Therefore

```text
K_open=+I_(V tensor V,h_2) tensor I_(V tensor V,h_4)/243. (10)
```

Projecting (10) proves (3), `sum_(L,M)g_(L,M)=1/3`, and excludes a hidden swap
sign or cross-rung permutation.

## Temporal channel sum

For `x_L,x_M` from (4), direct original-link incidence gives

| History | crossing multiplier |
|---|---:|
| `Y` | `t^12` |
| `Z,L,M` | `t^14 x_L x_M` |
| `p_2 Y,L` | `t^14 x_L` |
| `p_3 Y,M` | `t^14 x_M` |
| `p_3 Z,L,M` | `t^14 x_L` |
| `p_2 Z,L,M` | `t^14 x_M` |

The acted shared rung in the last two rows contains three vector strands.
Resolve its background pair through `M=0,1,2`; the exact Clebsch rule

```text
(M,+) tensor (1,-)=direct-sum_(j=|M-1|)^(M+1) (j,-)    (11)
```

contains the output `V=(1,-)` exactly once for every `M`.  Peter--Weyl pairing
with the opposite single-vector history selects that copy, so the acted rung
has output multiplier `t`, not the input-pair multiplier `x_M`.  The unacted
rung retains `x_L`.  This is the load-bearing guard against treating triple
occupancy as three independent scalar factors.

Combining (3), the two action orientations, and the half-action coefficients
gives the channel-first expression

```text
epsilon^2(c_V^(n))^2 a_2a_3/972 sum_(L,M) d_Ld_M [
 (t^12+t^14x_L)t^14x_L(1+x_M)
 +(t^12+t^14x_M)t^14x_M(1+x_L)].                       (12)
```

The sum in (12) is
`2t^14(9+A)(t^12A+t^14B)`, proving (5).  At `t=u=1`, the coefficient is
`2/3`, the two identity-crossing overlaps `1/3+1/3`.  At `t=0` it vanishes.
For positive supplied `t,u` and positive `a_2a_3`, it is positive; signed
amplitudes give the corresponding matrix-entry sign.  This is not operator or
reflection positivity.

Define

```text
f_L=d_L t^14 x_L(t^12+t^14x_L),
g_L=d_L(1+x_L).
```

The half-action-normalized channel-resolved response matrix is
`[f_Lg_M+g_Lf_M]/972`.  Its nine entries sum exactly to the stripped response
coefficient in (5), while its rank is at most two and generically two.  The
pre-half-action Haar matrix `d_Ld_M/243` has rank one.  Thus the first longer
word does not merely repeat a scalar Block236 coefficient; the two temporal
orientations carry genuinely independent finite channel data, still on the
same three-label alphabet.

## What remains open

- arbitrary-`q` binary singleton-product words and diagonal product entries;
- overlapping products of merged intervals and their orientation-sensitive
  recoupling matrices;
- whether any product-word span is invariant under `R_epsilon`;
- the complete vector kernel, arbitrary `r`, and other exterior irreps;
- physical action selection, time/distance, continuum, Lorentzian, gravity,
  metric/source, matter-current, or particle interpretation.

The next overlapping-word test contains `V tensor V tensor V`, whose vector
isotypic component has multiplicity three.  The labels `L=0,1,2` may already
index those three copies.  Consequently multiplicity alone proves neither
closure nor failure.  The next exact object is the original-link `3 by 3`
Racah/intertwiner matrix, including orientation signs.

## No-Go Discipline Gate

### N1 — live alternatives

The live routes are the `3 by 3` overlapping-word recoupling matrix, longer
binary product words, diagonal product entries, and arbitrary `r`.

### N2 — collapse conditions

The result collapses if either open kernel is swapped, if the rungs are
permuted, if any nonvector action irrep survives, if a conditional mean is
nonzero, or if the acted triple rung retains `x_M` instead of selecting `t`.

### N3 — nontriviality

The new content is the exact two-rung `1/243` kernel, nine channel weights,
acted-rung selection, and rank-two temporal channel matrix, not generic
compact-group character positivity.

### N4 — assumption firewall

The action, crossing, `J_2`, and `Q` are supplied.  No action selection,
continuum, geometric, or physical-source input is added.

### N5 — breadth

The proof is one `r=2,q=3` offdiagonal coordinate.  It is not lattice-wide or
a classification of product words.

### N6 — interpretation firewall

The `O(3)` labels are gauge-rung representation channels, not spacetime spins;
the spin-two channel is not a graviton, and `t,u` are not time or distance.

### N7 — prior art

Clebsch rules, projector ranks, and Haar orthogonality are standard.  The
proposed conditional claim is their exact orientation, normalization, and
temporal placement in this supplied compression-defect coordinate.

### N8 — honest next step

Compute the overlapping-word Racah matrix from actual oriented original-link
contractions.  Do not infer it from a phase-free textbook `6j` matrix and do
not infer a no-go from `V` multiplicity three.
