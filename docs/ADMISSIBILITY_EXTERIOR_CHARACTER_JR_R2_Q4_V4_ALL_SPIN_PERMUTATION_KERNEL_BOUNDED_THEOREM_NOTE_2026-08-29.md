---
claim_id: admissibility_exterior_character_jr_r2_q4_v4_all_spin_permutation_kernel_bounded_theorem_note_2026-08-29
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_V4_ALL_SPIN_PERMUTATION_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-29.md
claim_type: bounded_theorem
title: Exact all-spin permutation kernel at the first four-vector junction
claim_scope: "For the supplied r=2, q=4 O01 original-link word, integrate every non-h0 link with exact O(3) Haar moments and close the four h0 column pairs with the declared trace-normalized I/3. Prove the complete row-reduced eight-index tensor is identity support in occurrence order with coefficient 1/243, hence the directed physical four-cycle P/243. Construct nested rational C12, C123, C1234 and M=0 path projectors and resolve all 19 sequential paths in total-spin multiplicities 3,6,6,3,1, including exact rational coordinate blocks. This is a finite conditional static O01 theorem, not the unrestricted sixteen-index endpoint, the O10 V3-to-V5 kernel, the full q=4 temporal response, minimal or unbounded memory, arbitrary words, physical-Q propagation, continuum dynamics, gravity, or a theory of everything."
depends_on:
  - admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_support_note_2026-08-29
  - admissibility_exterior_character_jr_r2_q3_seven_channel_temporal_response_bounded_theorem_note_2026-08-29
  - minimal_axioms
dependency_roles:
  admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_support_note_2026-08-29: "supplies the exact q=4 original-link geometry, independent degree-eight Brauer image, four I/3 column closures, physical strand orders, and reviewed K=0 control"
  admissibility_exterior_character_jr_r2_q3_seven_channel_temporal_response_bounded_theorem_note_2026-08-29: "supplies the sequential pair/triple coupling convention and the finite q=4 response target"
  minimal_axioms: "framework boundary only; no axiom or approved primitive is edited"
runner: scripts/admissibility_exterior_character_jr_r2_q4_v4_all_spin_permutation_kernel_exact_2026_08_29.py
date: 2026-08-29
status: conditional-support
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_support_note_2026-08-29
target_blocker_text: "Resolve the K=1,2,3,4 multiplicity blocks and the seven odd V^3 residual routes, then insert the supplied central multipliers and test the complete finite q=4 temporal response."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
proposal_allowed: false
proposal_allowed_reason: "The result depends on the open Block232--240 stack and has not received an effective retained audit verdict."
axiom_policy: "framework boundary only; no axiom or approved primitive is edited"
next_trace_action: "Resolve the full O10 V3-to-V5 kernel or prove exact cup factorization, then insert the nested pair/triple/quadruple central multipliers and physical Q."
conditional_surface_status: "exact static column-closed O01 row operator and all five multiplicity blocks, conditional on the supplied open Block232--240 stack"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the complete rational 3^8 original-link contraction, all 19 nested-Casimir paths, and every all-spin coordinate block are exact on a fully disclosed finite carrier"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# q=4 all-spin O01 permutation kernel — bounded theorem

**Type:** `bounded_theorem`

**Status:** `conditional-support`.  Independent audit and the open stacked
dependency chain remain pending; this note is not a retained proposal.

## Result

For the supplied `r=2`, `q=4`, cell-zero O01 word, integrate every non-`h0`
original link with the exact `O(3)` Haar moments and close the four column pairs
at `h0` with the same trace-normalized identity `I/3` used in Block240.  Leave
all eight row indices open.  In the occurrence orders

```text
left:  (p0,D,E,F)
right: (A,D,E,F)
```

the resulting row-reduced endpoint kernel is exactly

```text
K01[(p,D,E,F),(A,D',E',F')]
  = (1/243) delta(p,A) delta(D,D') delta(E,E') delta(F,F').
```

The exact rational tensor has shape `3^8`, exactly 81 nonzero entries, and every
nonzero entry is `1/243`.  The same complete tensor identity has zero mismatches
over `F_1009`, `F_1013`, and `F_1019`.  This is a result about the row-reduced
kernel after a declared column closure, not the complete sixteen-index open
endpoint tensor.

## Physical strand order and all spin blocks

The sequential coupling orders are different on the two sides:

```text
left physical order:  (D,E,F,p0)
right physical order: (A,D,E,F).
```

Consequently the identity support in occurrence order is the directed cyclic
permutation

```text
P |A,D,E,F> = |D,E,F,A>
```

in physical order, and the static O01 operator is `P/243`.  Reversing the
direction gives `P^-1=P^T`; that error is invisible in the symmetric `K=0`
block but visible in `K=1,2,3`.

The exact four-vector decomposition is

```text
V^4 = 3 V_0 + 6 V_1 + 6 V_2 + 3 V_3 + V_4.
```

Since `P` commutes with diagonal `O(3)`, in orthonormal multiplicity bases it
restricts as

```text
P = direct_sum_K (U_K tensor I_(2K+1)).
```

Thus the single tensor identity fixes all five static O01 multiplicity blocks
`U_K/243`, including the 82 scalar coefficients outside the Block240 `K=0`
block.  The exact runner uses pivot-normalized rational path vectors rather than
orthonormal vectors.  If `D_K` is their diagonal Gram matrix and `A_K` is the
emitted rational coordinate block, then

```text
A_K^T D_K A_K = D_K,
U_K = D_K^(1/2) A_K D_K^(-1/2).
```

Thus `A_K` is `D_K`-metric orthogonal while `U_K` is Euclidean orthogonal.  In
any phase-fixed sequential Clebsch--Gordan basis the individual matrix entries
are determined; under a change of multiplicity basis the matrices are
conjugated.  Their basis-independent certificates are:

| `K` | multiplicity | `tr U_K` | `tr U_K^2` | eigenvalue multiplicities `(+1,-1,{i,-i} pairs)` | `det U_K` |
|---:|---:|---:|---:|---:|---:|
| 0 | 3 | 1 | 3 | `(2,1,0)` | -1 |
| 1 | 6 | 0 | -2 | `(1,1,2)` | -1 |
| 2 | 6 | 0 | 2 | `(2,2,1)` | +1 |
| 3 | 3 | -1 | -1 | `(0,1,1)` | -1 |
| 4 | 1 | 1 | 1 | `(1,0,0)` | +1 |

Every orthonormal `U_K` is orthogonal and obeys `U_K^4=I`; every emitted
coordinate block obeys `A_K^4=I` and the displayed `D_K`-metric identity.  Only
the `K=0` and `K=4` restrictions are self-adjoint; the `K=1,2,3` restrictions
are not.  Contracting the exact cyclic permutation against Block240's three raw
`K=0` invariants reproduces

```text
[[ 3, -6, 30],
 [-6,  6, 30],
 [30, 30, 30]],
```

so the new all-spin convention reduces exactly to the reviewed Block240
control.

The commutant dimension check is

```text
3^2 + 6^2 + 6^2 + 3^2 + 1^2 = 91,
```

matching the independently computed rank of the degree-eight Brauer image.
This does not mean the physical transfer needs 91 minimal states; it means the
entire equivariant static O01 map is fixed.

## Why this matters for the bridge

Block240 established one non-diagonal scalar junction.  The present identity
shows that the same original-link contraction does not require four unrelated
spin calculations: all `K=0,1,2,3,4` sectors are restrictions of one exact
cyclic strand transport.  It therefore removes the 82-coefficient static O01
bottleneck and gives a basis-free operator suitable for inserting the nested
two-, three-, and four-strand central multipliers next.

This is forward progress on the finite connection-dynamics bridge: the
geometric junction part of O01 is now exact on all of `V^4`.  It is not yet a
complete finite `q=4` transfer theorem.

## Imported boundaries and hostile scope

- The exact original-link geometry, column closure, and `K=0` control come from
  [Block240](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_V4_JUNCTION_RECOUPLING_EXACT_SUPPORT_NOTE_2026-08-29.md).
  The sequential coupling/temporal target comes from
  [Block239](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_SEVEN_CHANNEL_TEMPORAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md).
  The framework boundary is the
  [minimal-axiom authority](MINIMAL_AXIOMS_2026-06-29.md); none of it is edited.
- `I/3` is the declared trace-normalized column closure.  It is not described
  here as a unit-norm cup.  Replacing it by raw `I` multiplies the kernel by
  `3^4=81`.
- Exact `O(3)` Haar moments, the original-link word, and the physical strand
  orders are inherited from Blocks238--240.  The new load-bearing calculation
  is the complete eight-index rational contraction and its all-spin
  representation reduction.
- Central convolution is multiplicity-blind only at fixed total spin.  The
  nested pair/triple temporal multipliers still act in the sequential path
  resolution and have not been inserted here.
- O10 remains a `V^3 -> V^5` equivariant problem with 91 possible multiplicity
  coefficients.  Block240's `2/27` determinant/cup overlap is one selected
  `K=0` component, not a proof of full cup factorization.
- Physical `Q`, all four Gram histories, reachability, observability, and a
  transfer-rank lower bound have not been applied to this new kernel.
- Minimal memory remains open.  No arbitrary word, unbounded memory, gravity,
  dynamics, or TOE completion is claimed.

No full `q=4` temporal response is claimed.

**Axiom/primitive effect:** none.  No axiom or approved primitive is edited,
weakened, or supplemented.

## Executable evidence

- Primary exact proof:
  `scripts/admissibility_exterior_character_jr_r2_q4_v4_all_spin_permutation_kernel_exact_2026_08_29.py`
- Companion three-field endpoint reconstruction:
  `scripts/admissibility_exterior_character_jr_r2_q4_v4_all_spin_permutation_kernel_2026_08_29.py`
- Imported exact original-link machinery:
  `scripts/admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_2026_08_29.py`

The primary contracts the complete row-reduced tensor over `Q`, constructs the
nested `C12`, `C123`, and `C1234` path projectors, emits the exact rational
coordinate matrices for all 19 sequential paths, certifies the cyclic spectra,
and reproduces the reviewed raw `K=0` matrix.  The companion helper reuses the
reviewed original-link/Brauer machinery over three finite fields and compares
every one of the `3^8` entries; it is a separate arithmetic realization in the
same imported geometry chain, not an independent derivation of that geometry.
