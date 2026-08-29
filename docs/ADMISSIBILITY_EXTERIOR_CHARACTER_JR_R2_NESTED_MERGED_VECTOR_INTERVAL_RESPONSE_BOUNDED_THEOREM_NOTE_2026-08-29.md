---
claim_id: admissibility_exterior_character_jr_r2_nested_merged_vector_interval_response_bounded_theorem_note_2026-08-29
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_NESTED_MERGED_VECTOR_INTERVAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md
claim_type: bounded_theorem
claim_scope: "For the supplied retain-every-two physical Haar isometry on the actual original-link O(3) ladder, and for every finite q and 1<=s<q, compute the exact quadratic compression-defect response between the normalized nested merged defining-vector Wilson loops Y_s=chi_V(delta_s...delta_1) and Z_s=chi_V(delta_s...delta_0). Prove that only the two cross-plaquette action pairings in cell zero survive, both action irreps are forced to V, all four first-order histories lie in ker Q, the global normalized Haar overlap is 1/9, and the exact finite-step entry is epsilon^2(c_V^(n))^2 a_0a_1 t_V^(8s+6)(1+4t_V^2+t_V^4+2t_V^6)/36. This is one nested merged Wilson-loop interval family conditional on the supplied action, temporal multipliers, Haar normalization, ladder, and J_2/Q stack; it is not a tensor-product vector background, a full non-determinant kernel or locality norm, physical time, continuum, Lorentz, gravity, metric/source, matter-current, or action-selection theorem."
depends_on:
  - admissibility_exterior_character_jr_arbitrary_r_scalar_fused_vector_transfer_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28
  - minimal_axioms
dependency_roles:
  admissibility_exterior_character_jr_arbitrary_r_scalar_fused_vector_transfer_bounded_theorem_note_2026-08-29: "reviewed one-cell arbitrary-r vector complement, normalization, parity, and next multicell target"
  admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28: "supplied finite action, temporal multipliers, actual arbitrary-q ladder, physical J_2/Q, and reviewed q=1 vector entry"
  minimal_axioms: "framework boundary only; no axiom or approved primitive is edited"
runner: scripts/admissibility_exterior_character_jr_r2_nested_merged_vector_interval_response_2026_08_29.py
independent_checker: scripts/admissibility_exterior_character_jr_r2_nested_merged_vector_interval_response_independent_2026_08_29.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: null
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_jr_arbitrary_r_scalar_fused_vector_transfer_bounded_theorem_note_2026-08-29
target_blocker_text: "Test the first q>1 defining-vector entry with a retained-rung background and then seek a fixed-memory description of the genuinely multicell vector sector."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Use the exact t_V^8 interval dressing to seek a fixed-memory multicell vector automaton, then test non-merged product-vector backgrounds where additional V tensor V channels occur."
conditional_surface_status: "exact r=2 nested merged-vector interval response conditional on the linked supplied action, temporal multipliers, Haar normalization, original-link ladder, and physical J_2/Q stack"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the interval incidences, unique action channels, global Haar contraction, Q annihilation, temporal polynomial, and normalization are exact finite mathematical results on a fully disclosed supplied carrier"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Nested merged-vector interval response at `r=2`

**Date:** 2026-08-29

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — author-side proposal label only.  The actual
current surface is `conditional-support`; independent audit and closure of the
stacked dependencies remain required.

## Result and boundary

The [arbitrary-width one-cell vector transfer](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_ARBITRARY_R_SCALAR_FUSED_VECTOR_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-29.md)
closes the selected `q=1` scalar-fused response for every fixed `r`.  This note
makes the orthogonal move requested there: keep `r=2` and place the selected
vector change inside a nontrivial neighboring coarse-loop background.

For every finite `q` and `1<=s<q`, the exact offdiagonal quadratic entry is

```text
<Y_s,R_epsilon Z_s>
 =epsilon^2(c_V^(n))^2 a_0a_1/36
   t_V^(8s+6)(1+4t_V^2+t_V^4+2t_V^6),              (1)

R_epsilon=(1/2)partial_lambda^2D_epsilon(0).
```

This is a nested merged Wilson-loop interval family, not a tensor-product
vector background or the full vector kernel.  It is conditional on the finite
action, temporal multipliers, Haar measure, normalization, ladder, and
physical `J_2,Q` construction supplied by the
[temporal--spatial compression-defect theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md).
No axiom or approved primitive changes.

## Authorities and imported inputs

| Input | Role here | Not proved here |
|---|---|---|
| Block 232 temporal--spatial compression-defect theorem | supplies the finite action, temporal multipliers, original-link ladder, `C J_2=J_2 C_c`, and `[C,Q]=0` | action selection, physical time, or continuum interpretation |
| Block 233 arbitrary-width one-cell vector theorem | supplies the reviewed `q=1` normalization/parity comparison and the multicell target | the present `q>1` interval result |
| minimal axioms | fixes the framework boundary | any new axiom or primitive |

Everything else in (1)—the interval support census, irrep forcing, global Haar
factor, and temporal polynomial—is reconstructed below and in two independent
runners.

## Exact target and proof obligations

**Exact target.** Compute one genuinely multicell defining-vector response on
the actual original links, including every action placement and exterior irrep
that can contribute, the physical residual projector, the global Haar factor,
and the complete finite temporal weights.

| Obligation | Disposition |
|---|---|
| actual `6q+1` links and merged-loop incidences | proved by symmetric difference below |
| complete action-placement census | only `(0,1)` and `(1,0)` match; exhaustive finite scan agrees |
| exterior-irrep completeness | an exclusive rail forces both insertions to `V` |
| physical `Q` | all four first-order histories have zero conditional first moment |
| normalized recoupling | global three-variable Haar contraction is exactly `1/9` |
| temporal and half-action normalization | both matched channels are evaluated explicitly |
| context comparison | `t->1` coefficient is one third of the normalized vacuum entry |

No target-equivalent lemma remains.  The wider product-background/full-kernel
problem is a different target, recorded in the scope and N-gate rather than
used as a premise.

## Actual original-link geometry

Let the `2q` fine plaquettes have supports

```text
P_j={u_j,v_j,h_j,h_(j+1)},       0<=j<2q.           (2)
```

Their union contains `6q+1` original links.  In the rail-forest gauge write

```text
W_j=X_(j+1)X_j^-1,
delta_c=W_(2c+1)W_(2c).
```

For `1<=s<q`, put

```text
A_s=delta_s...delta_1,
Y_s=chi_V(A_s),
Z_s=chi_V(A_s delta_0).                             (3)
```

These are residual-gauge-invariant coarse Hilbert-space Wilson-loop states.
Character orthogonality gives

```text
||Y_s||=||Z_s||=1,                 <Y_s,Z_s>=0.
```

Their fine-space pullbacks are `J_2Y_s=chi_V(A_s)` and
`J_2Z_s=chi_V(A_s delta_0)`.  Their original-link supports
are the boundaries of the fine intervals `{2,...,2s+1}` and
`{0,...,2s+1}`, so

```text
w(Y_s)=4s+2,             w(Z_s)=4s+6.               (4)
```

They are orthogonal: the second state carries an additional nontrivial
defining-vector label through coarse cell zero.

## Complete first-order residual census

Let `p_i=chi_V(W_i)` and define the four fine-space cell-zero histories

```text
H_iY=p_i J_2Y_s,         H_iZ=p_i J_2Z_s,   i=0,1. (5)
```

Symmetric-difference support equality leaves exactly two pairings:

| pairing | doubled edges on `Y` side | doubled edges on `Z` side | common vector weight |
|---|---|---|---:|
| `(H_0Y,H_1Z)` | none | `u_1,v_1` | `4s+6` |
| `(H_1Y,H_0Z)` | `h_2` | `u_0,v_0,h_0` | `4s+4` |

Every other pair of fine plaquette placements has unequal vector support.  In
each surviving pair an exclusive rail presents the action irrep alone on one
side and the background `V=(1,-)` alone on the other.  Edgewise Peter--Weyl
orthogonality therefore forces that action irrep to be `V`; no other exterior
character can contribute.  The doubled-edge menus
`V tensor V=(0,+) direct-sum (1,+) direct-sum (2,+)` must select their scalar
channel against the trivial opposite edge.  Thus nonscalar doubled channels
also vanish.

This support census is only a channel selector.  It would be wrong to attach a
separate `1/3` to every doubled original link: the histories are gauge-invariant
loops, and their normalized overlap is one global contraction.

## Physical projector and global Haar contraction

At fixed `delta_0`, write `W_0=x`, `W_1=delta_0x^-1`.  Normalized Haar gives

```text
E[chi_V(W_0)|delta_0]=E[chi_V(W_1)|delta_0]=0.       (6)
```

The factors `Y_s,Z_s` are fixed under this conditional integral, hence all
four histories in (5) lie in `ker Q`.  The supplied temporal convolution is
diagonal in original-link irreducible labels.  The parent identities
`C J_2=J_2 C_c` and `[C,Q]=0` therefore preserve the typed coarse pullbacks
and keep these histories in `ker Q` after temporal convolution.

For either matched pairing, product Haar reduces the overlap to

```text
I=int chi_V(W_0)chi_V(W_1)chi_V(A)
      chi_V(AW_1W_0) dW_0 dW_1 dA.                 (7)
```

Expanding the four traces as

```text
(W_0)_(aa)(W_1)_(bb)A_(cc) A_(ij)(W_1)_(jk)(W_0)_(ki)
```

and using `int R_ab R_cd dR=delta_ac delta_bd/3` forces all six indices
equal.  Three assignments survive over `3^3`, so

```text
I=1/9.                                               (8)
```

The same-index pair `(H_0Y,H_0Z)` leaves `W_1` once, and `(H_1Y,H_1Z)` leaves
`W_0` once; their Haar first moments vanish.  The independent runner
reconstructs (6)--(8) over all 48 signed `O(3)` frames without importing the
primary delta-index path.

## Exact temporal response

Let `t=t_V`.  The two matched channels contribute

```text
(t^(4s+2)+t^(4s+6))(t^(4s+6)+t^(4s+6))
 +(t^(4s+2)+t^(4s+4))(t^(4s+6)+t^(4s+4))

=t^(8s+6)(1+4t^2+t^4+2t^6).                        (9)
```

For the selected vector channel, the action/Fourier coefficient entering
`B_i` is `-c_V^(n)a_i`; the `-epsilon B_i/2` term in the half action therefore
gives the positive leakage amplitude `epsilon c_V^(n)a_i/2`.  The product of
the two leakage amplitudes, the global `1/9`, and (9) gives equation (1).  The sign is positive for
positive `a_0a_1`; arbitrary signed amplitudes contribute
`sign(a_0a_1)`.  With `c_V^(n)>0` and `t>0`, nonnegative amplitudes give a
nonnegative entry and positive amplitudes give a strictly positive entry.

At `t=1`,

```text
<Y_s,R_epsilon Z_s>
 =2 epsilon^2(c_V^(n))^2 a_0a_1/9.                 (10)
```

The reviewed `q=1` vacuum entry has coefficient `2/3`, so the occupied merged
background changes the recoupling by a factor `1/3`.  At finite `0<t<1`,
increasing `s` by one multiplies (1) exactly by `t^8`.  This is exact decay for
this single nested interval family, not a norm bound or full locality theorem.
For `s=1`, `c_V^(n)=2`, `epsilon=a_0=a_1=1`, and `t=1/2`, the value is
`67/4718592`.

The lower endpoint `s=0` is excluded and is not a limit of (1): `A_s` is then
absent, the global contraction is `1/3` rather than `1/9`, and the reviewed
one-cell polynomial applies.  Likewise, `t=0` gives zero rather than strict
positivity.  The upper endpoint `s=q-1` is included unchanged: the merged loop
may reach the far boundary because the proof uses only its finite interval
incidence and no exterior cell beyond `q-1`.

## What remains open

- product-vector occupation backgrounds `product_c chi_V(delta_c)`, whose
  doubled rungs have additional recoupling channels;
- noncontiguous merged loops and arbitrary coarse vector words;
- a fixed-memory multicell transfer or connected norm for the full
  non-determinant sector;
- `r>2` multicell vector responses and other `O(3)` irreducible entries;
- selected action, physical time, refinement/continuum, Lorentzian, gravity,
  metric/source, or matter-current identification.

Generic compact-group character orthogonality and finite-state algebra are
prior art.  The framework-specific result is the complete actual-link,
physical-`Q`, background-dependent response (1).

## No-Go Discipline Gate

This is a positive conditional theorem.  The boundary list states what the
calculation quantifies over; it does not assert that any extension is
impossible.

### N1 — live alternative routes

| Route | Attempt this cycle | Outcome and authority | Marker |
|---|---|---|---|
| tensor-product background | Replace the merged character by a product of cell characters and inspect doubled-rung menus. | Extra `V tensor V` channels appear, so equation (1) is not imported into that carrier; the route stays live. | `ATTEMPTED` |
| noncontiguous merged support | Repeat the symmetric-difference scan with a gap. | The run count and matched supports change; no universal interval formula is claimed. | `ATTEMPTED` |
| `r>2` multicell response | Combine the arbitrary-`r` one-cell transfer with a neighboring coarse loop. | The one-cell three-state memory does not encode the new background fusion state; enlarging it is a live construction. | `ATTEMPTED` |
| full vector automaton | Use the parent determinant four-state automaton as a design pattern. | It tracks Boolean determinant words, not `O(3)` vector fusion; it is route context rather than proof authority. | `ATTEMPTED` |
| other exterior irreps | Allow a general action irrep in the selected entry. | The exclusive-rail comparison forces `rho=V` for this entry, while different external states remain unclassified. | `ATTEMPTED` |
| physical metric/source reading | Compare the decaying interval entry with the proposed polarized seam. | No retained identification maps this selected coefficient to a metric, source, or gravity observable. | `ATTEMPTED` |

### N2 — independence and collapse

The scope boundaries collapse to five units: `B` background shape, `R`
blocking width, `C` channel completion, `K` full-kernel/locality completion,
and `P` physical dynamics/identification.  `I` means closing either direction
does not close the other.

| | `B` | `R` | `C` | `K` | `P` |
|---|---:|---:|---:|---:|---:|
| `B` | -- | I | I | I | I |
| `R` | I | -- | I | I | I |
| `C` | I | I | -- | I | I |
| `K` | I | I | I | -- | I |
| `P` | I | I | I | I | -- |

The action and temporal multipliers are deliberately collapsed inside `P` as
one supplied finite-step dynamics unit.  No independence is asserted inside a
collapsed unit.

### N3 — hidden-wall scan

| Phrase family | Disposition |
|---|---|
| `supplied`, `conditional`, `fixed` | Maps to the linked action, temporal multipliers, Haar measure, ladder, and `J_2,Q` inputs. |
| `normalized`, `physical` | Means normalized Peter--Weyl/Haar and the linked physical projector construction, not an observed normalization or physical-time claim. |
| `only`, `exactly`, `complete` | Restricted to the action placements and irreps contributing to the displayed matrix element, proved by exclusive rails. |
| `standard`, `prior art` | Credits representation orthogonality and finite-state algebra; neither supplies a framework-specific coefficient. |
| `open`, `not`, `no` | Narrows this theorem's quantified carrier and never ranges over all future extensions. |

### N4 — citation and residual matching

| Citation | Residual supplied | Use here | Match |
|---|---|---|---:|
| `docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md:812-945` | exact `r=2,3`, `q=1` selected vector entries and their action/Q conventions | direct finite-step supplier and one-cell comparison | yes |
| `docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_ARBITRARY_R_SCALAR_FUSED_VECTOR_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-29.md:42-194` | arbitrary-`r` one-cell complement and the named `q>1` residual | direct target authority | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:205-217` | approved distribution boundary, with values/rates downstream | boundary authority only | yes |

The determinant automaton and metric/source seam were inspected but dropped as
proof witnesses because their residuals do not match this vector interval.
They appear only as explicitly non-load-bearing route context in N1/N8.

### N5 — rhetoric and resolution certificate

| Resolution | Executed | Scope |
|---|---|---|
| `per_element` | every original-link incidence and exclusive-rail irrep forcing | exact for the four selected first-order histories |
| `per_site` | changed cell zero and nested spans `s=1,...,6` directly | symbolic formula covers every finite `1<=s<q` |
| `per_mode` | one pair of merged defining-vector characters | no product-background or other-irrep state classification |
| `per_block` | `r=2`, arbitrary finite interval span | no `r>2` multicell theorem |
| `lattice_wide` | not executed; no arbitrary background or volume norm supplied | no infinite-volume, continuum, or full-locality statement |

The primary cached runner emits substantive lines for the same five
resolutions.  Untested resolutions remain unclaimed.

### N6 — primitive and partial-closure scan

`docs/audit/data/axiom_premise_nodes.json` was checked.  It registers
`minimal_axioms` and its dated aliases, but no action, temporal multiplier,
Haar normalization, vector-background classifier, locality norm, clock, or
physical metric/source identification.  Existing conventions can close
presentation choices but not these mathematical extensions.  This note makes
no “new axiom required” claim.

### N7 — hostile steelman

Equation (1) is already a one-parameter family whose added background cells
produce a rank-one-looking `t^8` dressing.  The strongest hostile case is that
the full multicell vector sector may therefore admit a modest finite-memory
automaton once each boundary irrep/parity state is tracked.  The parent
determinant construction shows that original-link subtraction can be encoded
without growing memory.  This is a credible route, so the next target is that
automaton; no obstruction or no-go against it is asserted here.

### N8 — cross-cycle echo

The prior `r=2,3` one-cell restriction was retired by the arbitrary-`r`
three-state transfer.  The determinant sector's multicell sum was retired by a
four-state ordered automaton in
`docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md:1285-1349`.
That mechanism cannot be imported as a vector proof, but it is an explicit
reason to test rather than exclude finite memory.  The current `t^8` interval
dressing supplies the first vector-background datum for that test.
