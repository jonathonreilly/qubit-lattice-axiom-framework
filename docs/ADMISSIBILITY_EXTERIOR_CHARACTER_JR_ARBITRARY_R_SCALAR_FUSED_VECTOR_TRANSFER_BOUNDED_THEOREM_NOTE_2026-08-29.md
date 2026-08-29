---
claim_id: admissibility_exterior_character_jr_arbitrary_r_scalar_fused_vector_transfer_bounded_theorem_note_2026-08-29
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_ARBITRARY_R_SCALAR_FUSED_VECTOR_TRANSFER_BOUNDED_THEOREM_NOTE_2026-08-29.md
claim_type: bounded_theorem
claim_scope: "For every supplied fixed finite blocking width r>=2 on one retained cell of the reviewed original-link O(3) ladder, derive the exact first possible vacuum-to-coarse-defining-vector action response of the physical J_r temporal compression defect. Prove that all derivatives below r vanish, all proper order-r complement histories project doubled defining-vector rungs to the scalar channel, their normalized Haar overlap is 3^(1-r), and their complete finite-step temporal sum is an explicit positive bond-dimension-three transfer polynomial P_r(t_V), with a separate two-state endpoint subtraction. Recover the reviewed r=2 and r=3 formulas and the general small-step coefficient (2^r-2)/3^(r-1). This is one selected q=1 defining-vector entry conditional on the supplied action, normalization, temporal multipliers, Haar measure, ladder, and J_r stack; it is not a full vector/non-determinant kernel, physical time, continuum, Lorentz, gravity, metric/source, matter-current, or action-selection theorem."
depends_on:
  - admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28
  - minimal_axioms
dependency_roles:
  admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28: "reviewed complete defect, physical J_r/Q carrier, supplied temporal/action normalization, and exact r=2/r=3 defining-vector entries"
  minimal_axioms: "framework boundary only; no axiom or approved primitive is edited"
runner: scripts/admissibility_exterior_character_jr_arbitrary_r_scalar_fused_vector_transfer_2026_08_29.py
independent_checker: scripts/admissibility_exterior_character_jr_arbitrary_r_scalar_fused_vector_transfer_independent_2026_08_29.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: null
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28
target_blocker_text: "Generalize the exact r=3 scalar-fused defining-vector complement transfer to arbitrary fixed r or a multicell vector history, retaining the physical projector and original-link temporal weights."
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Test the first q>1 defining-vector entry with a retained-rung background and then seek a fixed-memory description of the genuinely multicell vector sector; keep action selection, physical time, continuum, and the full non-determinant kernel open."
conditional_surface_status: "exact selected q=1 vector response conditional on the linked supplied action, temporal multipliers, normalization, ladder, Haar measure, and physical J_r stack"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the arbitrary-r response, original-link incidence, scalar O(3) recoupling, Haar normalization, positive transfer polynomial, and small-step match are exact finite mathematical results under explicitly supplied action and temporal data"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Arbitrary-`r` scalar-fused defining-vector transfer

**Date:** 2026-08-29

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — author-side proposal label only.  The actual
current surface remains `conditional-support`, with independent audit and
dependency closure required before any retained-grade classification.

## Status and boundary

This note closes the next finite-width calculation named by the
[temporal--spatial compression-defect theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md):
the selected finite-step defining-vector complement transfer is no longer
restricted to `r=2` or `r=3`.  It is exact for every supplied fixed finite
`r>=2` on one retained cell.  The result is **conditional support**, not an
adopted action, physical Hamiltonian, full vector kernel, or TOE closure.  No
axiom or approved primitive changes.

**Exact target.** Under the supplied finite-ladder action, temporal
multipliers, Haar measure, normalization, and physical `J_r,Q` stack, compute
the first potentially nonzero vacuum-to-coarse-defining-vector derivative for every fixed
finite `r>=2`, including its exact finite-step polynomial and small-step
normalization.

## Authorities and imported inputs

- The [temporal--spatial compression-defect theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md)
  supplies the action-amplitude convention, link-diagonal temporal
  multipliers, normalized Haar measure, physical `J_r,Q` construction,
  `(r-1)`-wise conditional-Haar lemma, and the reviewed `r=2,3` entries. These
  are explicit supplied mathematical inputs; this note does not derive or
  select them.
- The [minimal framework axioms](MINIMAL_AXIOMS_2026-06-29.md) set only the
  framework boundary. They do not supply the action, temporal evolution,
  Haar measure, amplitudes, representation carrier, physical clock, or
  continuum interpretation.
- The defining representation and the `O(3)` tensor-product/parity rules are
  standard representation-theory machinery used conditionally on the supplied
  carrier. No measured, fitted, observational, PDG, cosmological, or
  dimensionful value is used.

The open physical bridges are therefore action selection, physical time,
continuum/refinement control, and identification of any vector response with
gravity, metric/source, or matter current. None is used to satisfy the finite
mathematical target above.

## Proof-obligation graph

| Obligation | Disposition |
|---|---|
| actual `3r+1` original-link incidence and boundary census | proved below by symmetric difference |
| scalar-only doubled-rung selection, including `O(3)` parity | proved below edge by edge |
| normalized overlap `3^(1-r)` | proved below by iterated second moments and independently reconstructed from signed frames |
| physical `Q` deletion of exactly the empty/full partitions | inherited conditional-Haar lemma plus the explicit exclusive-rail label argument below |
| complete proper-partition sum and fixed-memory transfer | proved below; direct enumeration and an independent dynamic program agree |
| `r=2,3` recovery and small-step normalization | proved below and checked against the linked supplied parent |

All obligations for the stated conditional finite target are discharged. The
strongest missing lemma belongs to the broader program, not this target: no
result here classifies the full multicell non-determinant kernel. The proof is
therefore conditional on its declared supplied action/transfer inputs, rather
than circular or dependent on a target-equivalent missing lemma.

## Actual original-link carrier

Let `H={0,...,r-1}` index the fine plaquettes in one retained cell.  Plaquette
`i` occupies the four original links

```text
P_i={u_i,v_i,h_i,h_(i+1)}.
```

For `X subseteq H`, let `partial X` be the symmetric difference of the
`P_i`, and put

```text
w(X)=|partial X|=2|X|+2 runs(X),
tau_X=t_V^w(X),
F_Y(X)=sum_(A subseteq X) tau_(Y triangle A).       (1)
```

The complete coarse defining-vector loop has `w(H)=2r+2`.  These are the
actual `3r+1` original links; no reduced increment carrier is used.

## Scalar selection and the physical projector

Write `x_X=product_(i in X) chi_V(W_i)` and
`phi_V=chi_V(W_(r-1)...W_0)`.  On any original link the two complementary
Gram histories contain zero, one, or two defining-vector labels.  Their local
menus are

```text
0 labels: (0,+),
1 label : V=(1,-),
2 labels: V tensor V=(0,+) direct-sum (1,+) direct-sum (2,+).  (2)
```

For `empty != X proper_subset H`, comparing `x_X` with
`x_(H\X) phi_V` leaves exactly `V` on `partial X` and the scalar `(0,+)`
on every doubled edge.  The axial-vector and spin-two channels have unmatched
labels on the opposite Gram history and vanish by edgewise Haar orthogonality.
Equivalently, the vector-side proper history cannot be supplied by a doubled
rung: `V=(1,-)` is absent from
`V tensor V=(0,+) direct-sum (1,+) direct-sum (2,+)` by `O(3)` parity.

Sequential use of the exact defining-representation second moment gives

```text
<x_X,x_(H\X)phi_V>=3^(1-r).                         (3)
```

The value is independent of `X`.  It is reconstructed in the independent
runner from all 48 signed `O(3)` frames: one internal scalar fusion contributes
`1/3`, and there are `r-1` internal fusions.

Every nonempty proper `x_X` has zero conditional mean at fixed coarse
holonomy by the reviewed `(r-1)`-wise Haar lemma, hence `Qx_X=0`.  More
explicitly, a proper subset leaves mixed trivial/`V` labels on the exclusive
upper and lower rail links, whereas every coarse Peter--Weyl state has one
common irreducible label on every exclusive rail pair.  The supplied temporal
convolution is diagonal in those original-link representation labels, so it
cannot turn a proper mixed-label row into a coarse cylindrical row.  Thus the
temporally weighted proper row also remains `Q`-orthogonal, and

```text
<x_X,(I-Q)y>=<x_X,y>.                               (4)
```

The exclusive-rail test is exhaustive in both Gram orientations.  On the
vacuum-side row `x_X`, the two rails of plaquette `i` carry `(0,+)` when `i`
is absent and `V=(1,-)` when it is present.  On the coarse-side row
`x_(H\X) phi_V`, they carry `V=(1,-)` for `i in X` and the complete even menu
`{(0,+),(1,+),(2,+)}` for `i notin X`.  In either orientation a common
coarse Peter--Weyl label exists on all `2r` rails exactly when
`X=emptyset` or `X=H`; for a proper `X`, the coarse-side intersection is empty
specifically by `O(3)` parity.  Every temporal half-subpartition changes only
the diagonal multiplier and preserves these rail menus.  Together with the
supplied conditional-Haar lemma, this proves that no proper row can acquire a
cylindrical component before the physical projection.  Only the empty/full
derivative partitions are absent, because the zeroth leakage
`(I-Q)S_epsilon(0)J_r` vanishes.  Thus physical cylindrical subtraction does
not delete an additional proper complement history.

At derivative order `k<r`, at least one plaquette supplies no action
insertion.  One of its exclusive rail links therefore leaves the outer
defining-vector label unpaired, and edgewise Haar orthogonality makes that
history vanish.  Consequently every vacuum-to-`phi_V` derivative below order
`r` is zero; (5) is the first possible entry.

## Exact finite-step response

Leibniz expansion of the reviewed Gram defect, including both supplied
half-action factors, now gives

```text
(1/r!)<1,partial_lambda^r D_epsilon(0) phi_V>
 = (epsilon c_V^(n)/2)^r 3^(1-r) product_(i in H)a_i P_r(t_V),

P_r(t)=sum_(empty != X proper_subset H)
          F_0(X) F_H(H\X).                          (5)
```

Every coefficient of `P_r` is a positive integer.  Therefore (5) is
nonnegative for nonnegative supplied amplitudes and is strictly positive when
all amplitudes are positive and `0<t_V<=1`.  With arbitrary signed amplitudes,
the sign also carries `product_i a_i`.

## Fixed-memory transfer

Equation (5) has an exact bond-dimension-three representation.  The allowed
pair bits satisfy `u<=v`; let the state be ordered as `00,01,11`, and define

```text
mu(00)=1,  mu(01)=2,  mu(11)=1,
eta((p,q),(u,v))
 =2u+2(1-p)u+2v+2(1-q)v,
K_t[(p,q),(u,v)]=mu(u,v)t^eta((p,q),(u,v)).          (6)
```

The multiplicity two of `(u,v)=(0,1)` remembers the two possible placements
of the derivative partition bit.  Also define the two-state one-history
matrix

```text
E_t[p,u]=t^[2u+2(1-p)u].                            (7)
```

With `e_00,e_0` the zero-state basis columns and `1_d` all-ones columns,

```text
P_r(t)=e_00^T K_t^r 1_3
       -(1+t^(2r+2)) e_0^T E_t^r 1_2.              (8)
```

Equivalently, with `q=t^2`, the two transfer matrices are

```text
E=[[1,q^2],[1,q]],
K=[[1,2q^2,q^4],[1,2q,q^3],[1,2q,q^2]].            (9)
```

The first contraction sums all partition/subpartition histories.  The second
term removes exactly `X=emptyset` and `X=H`.  Product order is the original
plaquette order and is load-bearing; the memory dimension is independent of
`r`.

Direct subset enumeration and (8) agree exactly through `r=8` in two
independent implementations.  The first reviewed cases are

```text
P_2(t)=2t^4+2t^6+2t^8+2t^10,

P_3(t)=3t^4+6t^6+12t^8+8t^10+15t^12+2t^14+2t^16. (10)
```

Substitution into (5) reproduces the reviewed quadratic and cubic formulas.

## Small-step match

At `t=1`, each proper `X` contributes
`2^|X| 2^(r-|X|)=2^r`, so

```text
P_r(1)=2^r(2^r-2).                                  (11)
```

The global `2^-r` in (5) cancels the first factor and yields

```text
(1/r!)<1,partial_lambda^r D_epsilon(0) phi_V>
 =epsilon^r(c_V^(n))^r [(2^r-2)/3^(r-1)]
   product_i a_i + o(epsilon^r),                    (12)
```

exactly the defining-vector Fourier component of equation (32) in the linked
temporal--spatial compression-defect theorem.

## What remains open

- The first `q>1` vector block and its retained-rung background context.
- Other irreducible `O(3)` channels and mixed vector/tensor entries.
- Closure, positivity, or locality of the full non-determinant kernel.
- A selected action, physical time/Hamiltonian, continuum/refinement family,
  Lorentzian interpretation, or extended metric/source/matter carrier.

Generic compact-group character positivity and generic finite-state transfer
algebra are credited prior art.  The framework-specific increment is the
actual original-link `J_r,Q` scalar-fused complement formula (5) and its exact
fixed-memory realization (8).

## No-Go Discipline Gate

This is a positive conditional theorem.  The scope sentences above are not a
claim that any broader route fails.  The N1--N8 record is included because the
note names boundaries that remain outside its quantified domain.

### N1 — live alternative routes

Each marker records a route actually inspected in this cycle.  A route can be
live even when the present artifact does not execute its terminal obligation.

| Route | Attempt | Result and authority | Marker |
|---|---|---|---|
| action selection from admissibility | Search the approved premise registry and the minimal axioms for a coefficient or action selector. | The registry names `minimal_axioms`; its distribution clause leaves extensional values and formation site/rate downstream (`docs/MINIMAL_AXIOMS_2026-06-29.md:205-217`). This is an import boundary for this theorem, not a global impossibility result. | `ATTEMPTED` |
| physical-time reconstruction | Test whether the supplied multipliers and small-step coefficient define a clock or Hamiltonian. | Equations (5), (8), and (12) use a supplied step and produce an asymptotic coefficient; no map from the step to physical time is part of the declared inputs. | `ATTEMPTED` |
| refinement/continuum family | Take the exact `t->1` limit and search for an `r,q,n` refinement law. | Equation (12) closes the fixed-`r` coefficient only; the note supplies no joint refinement family. The limit remains a live next construction. | `ATTEMPTED` |
| multicell vector transfer | Set up the complement census on a retained-rung background. | No scratch result is imported into this theorem. The determinant-sector four-state construction (`docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md:1285-1349`) is a concrete mechanism to test, and the vector automaton remains the terminal obligation named in `next_trace_action`. | `ATTEMPTED` |
| other `O(3)` channels | Replace the selected defining-vector entry by other irreducible labels and repeat the edgewise fusion. | The parity-resolved local menus in (2) close only the displayed complement. They do not classify every vector/tensor block. | `ATTEMPTED` |
| metric/source identification | Compare the selected response with the polarized-seam metric/source construction. | `docs/ADMISSIBILITY_EXTERIOR_CHARACTER_METRIC_SOURCE_POLARIZED_SEAM_BOUNDED_THEOREM_NOTE_2026-08-28.md` provides a proposed conditional seam route, but no retained identification turns (5) into a physical metric, source, or gravity equation. | `ATTEMPTED` |

### N2 — independence and deliberate collapse

The boundaries collapse to five units.  `A` combines action coefficients and
their temporal multiplier because both are input to the same finite step;
`K` combines channel and multicell completion because both enlarge the kernel
being computed.  `I` means closing either direction does not close the other.

| | `A` step dynamics | `T` physical time | `R` refinement | `K` full kernel | `P` physical identification |
|---|---:|---:|---:|---:|---:|
| `A` step dynamics | -- | I | I | I | I |
| `T` physical time | I | -- | I | I | I |
| `R` refinement | I | I | -- | I | I |
| `K` full kernel | I | I | I | -- | I |
| `P` physical identification | I | I | I | I | -- |

For example, choosing an action does not identify its step with physical time;
a continuum family need not compute every representation block; and a
mathematical metric reading does not select the microscopic coefficients.
The table makes no independence claim inside either collapsed unit.

### N3 — hidden-wall scan

| Phrase family | Disposition |
|---|---|
| `supplied`, `conditional`, `under` | Maps to the action, temporal multiplier, Haar normalization, ladder, and `J_r,Q` inputs listed in **Authorities and imported inputs**. |
| `standard` | Appears only for the explicitly imported `O(3)` representation machinery; no empirical constant or physical selector is smuggled in. |
| `framework`, `axiom`, `approved primitive` | Marks the minimal-axiom boundary and the zero-axiom-change statement; it is not used to manufacture the action. |
| `reviewed`, `linked`, `parent` | Names the dependency note supplying the finite-step conventions and the `r=2,3` checks. |
| `load-bearing`, `exactly`, `only` | Refers to the original-link ordering, parity selection, or exhaustive exclusive-rail classification proved in this note and runners. |
| `open`, `not`, `no` | Restricts the domain of this positive theorem. None quantifies over every future extension or says that a broader construction is impossible. |

### N4 — citation/residual matching

| Citation | Residual attacked | Residual closed here | Match |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:205-217` | distinguishes the approved distribution premise from downstream values/rates | none; it is boundary authority only | yes |
| `docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md:906-946` | exact `r=3` vector complement and the arbitrary-`r` residual | arbitrary-fixed-`r`, one-cell selected vector transfer | yes |

The determinant-sector automaton (`docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md:1285-1349`)
and metric/source seam (`docs/ADMISSIBILITY_EXTERIOR_CHARACTER_METRIC_SOURCE_POLARIZED_SEAM_BOUNDED_THEOREM_NOTE_2026-08-28.md:1-45`)
were inspected and dropped as proof witnesses because their residuals do not
match the selected vector theorem.  They remain explicitly non-load-bearing
route context in N1/N8.  The sole approved premise node used here is
`minimal_axioms`, and it does not supply the finite-step action.

### N5 — rhetoric and resolution certificate

| Resolution | What was executed | Honest scope |
|---|---|---|
| `per_element` | Every original-link label menu, boundary incidence, and scalar overlap in the selected complement was checked. | Exact for the stated local histories. |
| `per_site` | One retained `q=1` cell was proved for arbitrary fixed finite `r`; direct checks cover `2<=r<=8`. | No multicell classification is inferred. |
| `per_mode` | The vacuum-to-coarse-defining-vector entry, including `O(3)` parity, was checked. | Other irreducible entries remain live calculations. |
| `per_block` | The three-state transfer and two-state endpoint subtraction were proved independent of fixed `r`. | This is a one-cell block, not the full non-determinant kernel. |
| `lattice_wide` | Not executed: no volume family or lattice-wide norm is among the inputs. | No infinite-volume or continuum statement is made. |

The primary runner emits the same five resolutions as substantive certificate
lines.  “Outside this theorem” always means outside this declared computation,
never impossible in the framework.

### N6 — partial closure and primitive scan

`docs/audit/data/axiom_premise_nodes.json` was checked.  It registers
`minimal_axioms` and its dated aliases, but no action, clock, continuum map,
vector-kernel classifier, or metric/source identification used here.  The
controlled vocabulary and current source notes were also searched for a
ratified primitive that would close those units; none is invoked.  The live
routes in N1 can close by additional mathematics or supplied physical data;
this note makes no “new axiom required” claim.

### N7 — hostile steelman

The strongest objection to the scope boundary is that the same ordered-subset
mechanism should extend to several retained cells: the determinant sector
already admits a fixed-memory automaton.  A larger state alphabet could track
boundary irrep/parity and background cancellations, yielding a genuine
multicell vector transfer without new axioms.  This is convincing as a research
route, so the present result is deliberately one-cell and the multicell
automaton is the next terminal obligation; no no-go is asserted against it.

### N8 — cross-cycle echo

The parent note's `r=2` and `r=3` restriction was retired here by identifying
the ordered pair-bit state and endpoint subtraction.  Its determinant-sector
multicell residual was previously advanced by a four-state cell automaton
(`docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md:1285-1349`),
which is precisely a mechanism worth testing for the vector sector.  The
metric/source polarized-seam note records another conditional response route,
but it remains proposed and does not identify this vector coefficient with
physical gravity.  These echoes strengthen the live routes in N1; none supports
a universal negative conclusion.
