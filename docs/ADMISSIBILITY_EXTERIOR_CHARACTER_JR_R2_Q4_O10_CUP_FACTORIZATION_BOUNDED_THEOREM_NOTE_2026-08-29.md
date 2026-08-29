---
claim_id: admissibility_exterior_character_jr_r2_q4_o10_cup_factorization_bounded_theorem_note_2026-08-29
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_O10_CUP_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-29.md
claim_type: bounded_theorem
title: Exact row-reduced O10 cup factorization at the first four-vector junction
claim_scope: "For the supplied r=2, q=4 O10 original-link word, integrate every non-h0 link with exact O(3) Haar moments and close the h0 column endpoint with four declared trace-normalized I/3 pairings, equivalently the cup-line closure tensor C/81. Prove that the complete row-reduced eight-index tensor is C-adjoint/243 from V^5 to V^3, so all 91 possible equivariant coordinates of this reduced static map are fixed and the cup complement has zero leakage. This is not the unrestricted sixteen-index endpoint, a statement for other column closures, the q=4 temporal response, physical-Q propagation, minimal or unbounded memory, arbitrary words, continuum dynamics, gravity, or a theory of everything."
depends_on:
  - admissibility_exterior_character_jr_r2_q4_v4_all_spin_permutation_kernel_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_support_note_2026-08-29
  - minimal_axioms
dependency_roles:
  admissibility_exterior_character_jr_r2_q4_v4_all_spin_permutation_kernel_bounded_theorem_note_2026-08-29: "supplies the reviewed q=4 all-spin O01 checkpoint and exact tensor-contraction implementation"
  admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_support_note_2026-08-29: "supplies the exact O10 original-link geometry and the determinant/cup control overlap"
  minimal_axioms: "framework boundary only; no axiom or approved primitive is edited"
runner: scripts/admissibility_exterior_character_jr_r2_q4_o10_cup_factorization_exact_2026_08_29.py
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
proposal_allowed_reason: "The result depends on the open Block232--241 stack and has not received an effective retained audit verdict."
axiom_policy: "framework boundary only; no axiom or approved primitive is edited"
next_trace_action: "Insert the exact nested pair/triple/quadruple temporal multipliers into the O01 cycle and O10 cup maps, then apply physical Q and test the finite q=4 response."
conditional_surface_status: "exact static row-reduced O10 cup map, conditional on the supplied open Block232--241 stack"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the complete rational 3^8 reduced original-link contraction and its cup-image identities are exact on a fully disclosed finite carrier"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# q=4 O10 cup factorization — bounded theorem

**Type:** `bounded_theorem`

**Status:** `conditional-support`. Independent audit and the open stacked
dependency chain remain pending; this note is not a retained proposal.

## Exact result

Let the raw cup embedding be

```text
C : V^3 -> V^5,
(C x)_(p0,A,D,E,F) = delta(p0,A) x_(D,E,F).
```

For the supplied `r=2`, `q=4` O10 word, integrate every non-`h0` original link
with exact `O(3)` Haar moments. Close the column endpoint with four
trace-normalized `I/3` pairings: three copy the `D,E,F` strands and one cups
`p0` with `A`. Equivalently this is the cup-line closure tensor `C/81`, because
`81=tr(C^dagger C)` is the Hilbert--Schmidt norm squared of the complete cup
map. Leave the eight row indices open in the orders

```text
left:  (D,E,F)
right: (p0,A,D',E',F').
```

The complete row-reduced kernel is exactly

```text
K10[(D,E,F),(p0,A,D',E',F')]
  = (1/243) delta(p0,A) delta(D,D') delta(E,E') delta(F,F')
  = (C^dagger/243)[(D,E,F),(p0,A,D',E',F')].
```

The rational tensor has shape `3^8`, exactly 81 nonzero entries, and every
nonzero entry is `1/243`; all 6,561 entries match. The same full tensor identity
has zero mismatches over `F_1009`, `F_1013`, and `F_1019`.

The normalization and complement tests are exact:

```text
C^dagger C = 3 I_(V^3),
P_C = C C^dagger / 3,
P_C^2 = P_C,
K10 C = I_(V^3)/81,
K10 P_C = K10,
K10 (I-P_C) = 0.
```

Thus the reduced map has rank 27 and no component outside the cup image. The
tensor-power multiplicities are

```text
V^3: (1,3,2,1),
V^5: (6,15,15,10,4,1),
```

so `dim Hom_O(3)(V^5,V^3)=91`. The operator identity fixes all 91 possible
equivariant coordinates of this reduced static map at once; it does not say
that 91 coefficients are nonzero or that 91 states are minimal.

Contracting the result with the unnormalized determinant vector on `V^3` and
its cup image on `V^5` gives

```text
<epsilon, K10 C epsilon> = 2/27,
```

which recovers Block240's selected overlap and explains it as a consequence of
the full reduced cup identity rather than an independent channel weight.

## Why this matters for the bridge

Block241 solved the static O01 side but left a 91-coordinate O10 obstruction.
The present identity collapses that obstruction to one exact geometric cup
map. The two static orientation kernels needed for the first `q=4` junction are
therefore now basis-free and exact after their declared column closures. This
opens the next genuinely dynamical calculation: insert the supplied nested
pair, triple, and quadruple central multipliers, then apply physical `Q` and
test the complete finite response.

## Imported boundaries and hostile scope

- The original-link word and exact Haar/Brauer machinery are inherited from
  [Block240](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_V4_JUNCTION_RECOUPLING_EXACT_SUPPORT_NOTE_2026-08-29.md).
  The O01 checkpoint and exact tensor contraction are inherited from
  [Block241](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_V4_ALL_SPIN_PERMUTATION_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-29.md).
  The framework boundary is the
  [minimal-axiom authority](MINIMAL_AXIOMS_2026-06-29.md). The new load-bearing
  result is the complete O10 reduced tensor and its cup-complement tests.
- The four `I/3` factors are trace-normalized column pairings. The code
  algebraically concentrates their total factor `1/81` on one delta. This is
  the cup-line closure tensor `C/81`, not a unit-norm cup on each vector;
  `C/sqrt(3)` is the isometry.
- This is a row-reduced endpoint after one specified column closure. It is not
  the unrestricted sixteen-index endpoint and does not determine how the
  original endpoint acts on a different column boundary state.
- The 91-dimensional equivariant Hom space is the pre-factorization obligation,
  not a physical state count. Exact factorization fixes those coordinates but
  does not prove a memory minimum.
- No pair, triple, or quadruple temporal multiplier is inserted here. Physical
  `Q`, Gram histories, reachability, and observability remain open.
- No full `q=4` temporal response is claimed. No arbitrary-word, continuum,
  gravity, or TOE-completion claim is made.

**Axiom/primitive effect:** none. No axiom or approved primitive is edited,
weakened, or supplemented.

## Executable evidence

- Exact-rational primary:
  `scripts/admissibility_exterior_character_jr_r2_q4_o10_cup_factorization_exact_2026_08_29.py`
- Three-field companion:
  `scripts/admissibility_exterior_character_jr_r2_q4_o10_cup_factorization_2026_08_29.py`
- Imported original-link primary:
  `scripts/admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_2026_08_29.py`

The primary reconstructs all 6,561 rational entries, proves the cup projector
identities, and recovers the Block240 control overlap. The companion separately
realizes the arithmetic over three finite fields while sharing the reviewed
original-link geometry; it is not an independent derivation of that geometry.
