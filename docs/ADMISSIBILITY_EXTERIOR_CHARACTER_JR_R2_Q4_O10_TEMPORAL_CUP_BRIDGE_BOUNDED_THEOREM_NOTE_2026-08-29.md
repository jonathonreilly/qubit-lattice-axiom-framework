---
claim_id: admissibility_exterior_character_jr_r2_q4_o10_temporal_cup_bridge_bounded_theorem_note_2026-08-29
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_O10_TEMPORAL_CUP_BRIDGE_BOUNDED_THEOREM_NOTE_2026-08-29.md
claim_type: bounded_theorem
title: Exact q=4 O01/O10 temporal response and cup-compression defect
claim_scope: "For the supplied parity-resolved central multipliers, prove exactly all eight q=4 O01/O10 temporal-history formulas on the finite 19-path carrier. Haar-projector sliding, the Block242 cup-cut trace-bundle reversal, the Block241 cyclic permutation intertwiner, and nested-projector orthogonality eliminate every mixed-label assignment and give coefficient (2K+1)/243. Prove that physical conditional-Haar Q=JJ^* annihilates all of this first-order history span at fixed delta0, so (I-Q) acts as the identity there; Q is not the static cup projector. Separately prove that inserting an artificial intermediate static cup projection loses the nonzero finite-carrier bridge Delta4. This is the first exact combined q=4 quadratic response conditional on the supplied formal multipliers and outer response coefficient, not a derivation of those inputs, a general Gram-positivity theorem, minimal memory, arbitrary words, continuum dynamics, gravity, or a theory of everything."
depends_on:
  - admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_support_note_2026-08-29
  - admissibility_exterior_character_jr_r2_q4_v4_all_spin_permutation_kernel_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_r2_q4_o10_cup_factorization_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_r2_q3_seven_channel_temporal_response_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_time_refinement_semigroup_obstruction_bounded_theorem_note_2026-08-28
  - minimal_axioms
dependency_roles:
  admissibility_exterior_character_jr_r2_q4_v4_junction_recoupling_exact_support_note_2026-08-29: "supplies the Block240 original-link network and degree-eight Brauer contraction used by the all-link companion"
  admissibility_exterior_character_jr_r2_q4_v4_all_spin_permutation_kernel_bounded_theorem_note_2026-08-29: "supplies the Block241 sequential 19-path (L,J,K) structure used by the candidate formula"
  admissibility_exterior_character_jr_r2_q4_o10_cup_factorization_bounded_theorem_note_2026-08-29: "supplies the reviewed raw cup C, normalized cup isometry, and static row-reduced O10 checkpoint"
  admissibility_exterior_character_jr_r2_q3_seven_channel_temporal_response_bounded_theorem_note_2026-08-29: "supplies the Block239 temporal-history convention inherited by the q=4 candidate"
  admissibility_exterior_character_time_refinement_semigroup_obstruction_bounded_theorem_note_2026-08-28: "supplies the formal central spin multipliers; this note does not derive them from a one-parameter exterior curve"
  minimal_axioms: "framework boundary only; no axiom or approved primitive is edited"
runner: scripts/admissibility_exterior_character_jr_r2_q4_combined_temporal_response_2026_08_29.py
independent_checker: scripts/admissibility_exterior_character_jr_r2_q4_temporal_all_link_finite_field_2026_08_29.py
date: 2026-08-29
status: conditional-support
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_jr_r2_q3_seven_channel_temporal_response_bounded_theorem_note_2026-08-29
target_blocker_text: "extend the finite exact response from q=3 to the first q=4 junction without assuming static cup closure commutes with temporal insertion"
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
proposal_allowed: false
proposal_allowed_reason: "The multiplier weights and outer response coefficient are supplied formal inputs on an open stacked dependency chain."
axiom_policy: "framework boundary only; no axiom or approved primitive is edited"
next_trace_action: "Test positivity and minimal history memory of the exact combined kernel, then compare against the arbitrary-r scalar-fused transfer route."
conditional_surface_status: "exact finite-carrier cup-compression defect and exact eight-history combined q=4 response after physical Q on the supplied formal multiplier family and open Block232--242 stack"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the complete V^5 carrier calculation, four spin-sector defect formulas, all eight independently weighted history identities, and the action of physical Q on their first-order history span are exact"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# q=4 combined temporal response and cup bridge — bounded theorem

**Type:** `bounded_theorem`

**Status:** `conditional-support`. This is an exact finite-carrier eight-history
response theorem on the supplied formal multiplier family and response prefactor,
not a retained proposal or a derivation of those supplied inputs.

## Exact obstruction

Let `W=V^3=DEF`, and normalize Block242's raw cup by

```text
Chat = C/sqrt(3) : W -> V_p x V_A x W,
P_C = Chat Chat^dagger.
```

For the even four-strand temporal operator use spin weights

```text
z_0,...,z_4 = (1,t,u,v,w),
R_A = R_(ADEF),
R_p = R_(pDEF).
```

The operators are exchanged by `p <-> A`. Their separate cup compressions are
equal, but their actions on the cup image are not. The exact omitted bridge is

```text
Delta4 = Chat^dagger R_p (I-P_C) R_A Chat
       = Chat^dagger R_p R_A Chat
         - (Chat^dagger R_p Chat)(Chat^dagger R_A Chat).
```

It is `O(3)`-equivariant, symmetric, and equals `delta_J I` on the complete
spin-`J` isotypic component of `W`, including its multiplicity space. Its
sector scalars are

```text
delta_0 = 0,
delta_1 = [4 - 48t + 40u + 9t^2 + 30tu - 35u^2]/162,
delta_2 = -[3t^2 + 50tu - 56tv - 25u^2 + 28v^2]/150,
delta_3 = -[80u^2 + 560uv - 720uw - 343v^2
             + 126vw + 297w^2]/1764.
```

At `(t,u,v,w)=(3/10,2/5,1/2,3/5)` the exact result is

```text
(delta_0,delta_1,delta_2,delta_3)
  = (0,49/1800,-29/5000,-1097/176400).
```

Multiplying the two separate cup compressions therefore discards a genuine
complement excursion in every non-scalar `V^3` sector at this sample. The
identity crossing `t=u=v=w=1` has zero defect, including zero first
derivatives, so this is a quadratic dynamical effect rather than a static cup
normalization error.

## What this changes

The Block242 map `C^dagger/243` remains the correct static column-closed O10
control. An intermediate calculation that identifies the primed and unprimed
`DEF` axes and inserts `P_C` between temporal operators loses `Delta4`.
However, the actual all-link Haar network has eight independent axes at its
degree-eight links and does not insert that intermediate cup projection. The
local bridge is therefore an exact falsifier of that projection route, not by
itself the mechanism of the full scalar response.

## Exact all-link four-history path selection

The four exact O10 selected-power incidence censuses are

```text
pre/pre:   Counter({1:15, 2:8, 3:13, 4:5}),
pre/post:  Counter({1:16, 2:8, 3:13, 4:2, 5:3}),
post/pre:  Counter({1:17, 2:8, 3:11, 4:7}),
post/post: Counter({1:18, 2:8, 3:11, 4:4, 5:3}).
```

This replaces the O01 census `Counter({1:16, 2:8, 3:10, 4:8})` used in the
first comparison. The census alone does not prove that different links share
one globally coherent sequence of representation labels. Define the 19-path
set

```text
P4 = {(L,J,K): L=0,1,2; |L-1| <= J <= L+1;
                    |J-1| <= K <= J+1}.
```

With `x=(1,t,u)`, `y=(d,t,u,v)`, and `z=(1,t,u,v,w)`, the four expressions are

```text
G_pre/pre   = sum_P4 (2K+1)/243 t^15 x_L^8 y_J^13 z_K^5,
G_pre/post  = sum_P4 (2K+1)/243 t^16 x_L^8 y_J^16 z_K^2,
G_post/pre  = sum_P4 (2K+1)/243 t^17 x_L^8 y_J^11 z_K^7,
G_post/post = sum_P4 (2K+1)/243 t^18 x_L^8 y_J^14 z_K^4.
```

To prove it, first give every insertion an independent central weight and expand
in pure spectral projectors. For a degree-`d` link Haar moment

```text
H_d = integral_O(3) g^(tensor d) dg,
```

any selected-subset central projector `A` obeys

```text
H_d A_column = A_row H_d,
```

because `A` commutes with the diagonal `O(3)` action. Projectors therefore slide
through the exact Block240 Brauer realization and along their trace bundles to
the Block242 cup cut. There `p` and `A` are identified, and real symmetric
total-spin projectors satisfy the strand-reversed relation

```text
Pi_K^(pDEF) C = S_(pA) Pi_K^(ADEF) C.
```

Here `S_(pA)` is absorbed only after the complete left/right trace bundles are
transported to the cut. The two local projector actions are not equal on the
raw cup image; dropping `S_(pA)` would reintroduce exactly the false local
compression that the nonzero `Delta4` rules out.

The three power-five insertions in `pre/post` and `post/post` obey the analogous
equivariant-cup intertwiner

```text
Pi_J^(pADEF) C = C Pi_J^(DEF).
```

They therefore add three powers of `y_J`, rather than importing an independent
five-strand label or the unused supplied value `r_5`.

After strand reversal, the remaining projectors are the commuting Block241
nested chain `EF subset DEF subset V^4`. Hence the independently labelled scalar
is

```text
S({L_a},{J_b},{K_c})
 = (1/243) Tr_V4 [ product_a Pi^EF_(L_a)
                    product_b Pi^DEF_(J_b)
                    product_c Pi^V4_(K_c) ].
```

For each history, projector orthogonality makes the scalar zero unless every
insertion at a given nested level has one common label and `(L,J,K)` lies in
`P4`. For an allowed path the product is its joint path projector, whose rank is
`2K+1`. Thus no mixed-label monomial survives and all four displayed 19-path
expressions follow as formal identities.

The full network also matches all four theorems at eight unrelated rational
samples over each of `F_1009`, `F_1013`, and `F_1019`: the expanded certificate
passes `138/138` checks. At the original post/pre sample its residues are
`(616,332,310)`. At identity,
`sum_P4(2K+1)/243 = 81/243 = 1/3` exactly. The initial mismatch therefore came
from assigning the O01 census to O10, not from discarding valid physics.

## Exact O01 role-resolved continuation

The same full-network companion supports the four O01 expressions

```text
G01_pre/pre   = sum_P4 (2K+1)/243 t^15 x_L^8 y_J^13 z_K^5,
G01_pre/post  = sum_P4 (2K+1)/243 t^15 x_L^8 y_J^15 z_K^3,
G01_post/pre  = sum_P4 (2K+1)/243 t^16 x_L^8 y_J^10 z_K^8,
G01_post/post = sum_P4 (2K+1)/243 t^16 x_L^8 y_J^12 z_K^6.
```

For the right-post histories the raw census contains one extra degree-two cut
and two degree-five cuts. The degree-two cut at `h2` acts only on the `p1,A`
pair. Since

```text
H_2 = (1/3) |cup><cup|
```

and that cup lies in the even spin-zero sector, `H_2 R_2=H_2`; the cut therefore
contributes one rather than another `x_L`. The two degree-five cuts reduce by
`Pi_J^(pADEF) C = C Pi_J^(DEF)` and add `y_J^2`. Treating every degree-two cut
as `x_L` fails the direct network.

At the closure, Block241's physical cyclic permutation maps the right chain
`(A,D,E,F)` to the left chain `(D,E,F,p0=A)`, so every nested path projector
obeys

```text
Pi_alpha^left P = P Pi_alpha^right.
```

Consequently mixed paths vanish, while `P^dagger P` cancels inside the closed
Gram contraction. The non-diagonal multiplicity coordinates of `P/243` are an
exact basis change, not an extra response factor. This proves the four O01
expressions as formal identities.

Across both orientations, all four histories, eight rational samples, three
prime fields, and the identity controls, the expanded direct-network
certificate passes `247/247`, independently checking the role proof.

## Combined response and physical Q

Write the one-side factors

```text
T_Y  = t^7 x_L^4 y_J^9,
T_Z  = t^8 x_L^4 y_J^4 z_K^5,
T_01 = t^8 x_L^4 y_J^6 z_K^3,
T_10 = t^9 x_L^4 y_J^7 z_K^2.
```

The exact stripped response is

```text
sum_P4 (2K+1)/972 [
  (T_Y+T_01)(T_Z+T_01) + (T_Y+T_10)(T_Z+T_10)
].
```

The full Block239-normalized response multiplies this by the supplied outer
factor `epsilon^2 (c_V^(n))^2 a_0 a_1`; this block does not derive that factor.

At fixed `delta0`, the two vector endpoints are `W_0=x` and
`W_1=delta0 x^(-1)`. Normalized Haar averages of vector entries vanish, and
the q=4 `Y/Z` character factors are conditional spectators. Every first-order
history used above is therefore in `ker Q`. The supplied commutation
`[C,Q]=0` preserves this statement through the crossing. Hence `(I-Q)` acts as
the identity on the exact history span. This physical `Q=JJ^*` is not the
static cup projector and no cup-image closure is assumed.

At the identity crossing the stripped response is exactly `2/3`. At the
disclosed rational sample it is

```text
16403381271764259325016205411
--------------------------------------------- ,
400000000000000000000000000000000000000000000
```

with residues `(82,411,188)` over `F_1009`, `F_1013`, and `F_1019`.

## Boundaries and falsifiers

- `P_C` is the static cup-image projector. It is not physical `Q=JJ^*`, the
  history-space conditional-Haar projector.
- `Delta4` is not positive. It is a composition defect rather than a Gram norm;
  the negative spin-2 and spin-3 sample values are legitimate.
- The sample is a falsifier for independent cup compression. It is not asserted
  to lie on a derived one-parameter exterior-character curve.
- The odd scalar `d` and five-strand weight `r_5` do not occur in this local
  bridge. Their absence is not evidence that they cancel from the full response.
- Nonzero `Delta4` proves nonclosure of an intermediate cup-projection route;
  it does not modify the separately proved eight-axis four-history identities.
- No general Gram-positivity, minimal-memory, arbitrary-word, continuum,
  gravity, or TOE-completion claim is made.

**Axiom/primitive effect:** none. No axiom or approved primitive is edited.

## Dependency anchors

The exact original-link geometry comes from the
[q=4 junction recoupling note](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_V4_JUNCTION_RECOUPLING_EXACT_SUPPORT_NOTE_2026-08-29.md).
The nested 19-path carrier and physical cyclic permutation come from the
[q=4 all-spin permutation-kernel note](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_V4_ALL_SPIN_PERMUTATION_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-29.md).
The cup and static O10 checkpoint come from the
[q=4 cup-factorization note](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_O10_CUP_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-29.md).
The temporal-history and physical-response convention comes from the
[q=3 temporal-response note](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_SEVEN_CHANNEL_TEMPORAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md),
while the supplied formal multiplier boundary is recorded in the
[time-refinement obstruction note](ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md).
The framework boundary is the
[minimal-axiom authority](MINIMAL_AXIOMS_2026-06-29.md).

## Executable evidence

The primary response runner
`scripts/admissibility_exterior_character_jr_r2_q4_combined_temporal_response_2026_08_29.py`
checks all eight exact history formulas, the combined factorization, physical-Q
scope, the exact rational response, the `2/3` identity control, and hostile
mutations. The local exact runner
`scripts/admissibility_exterior_character_jr_r2_q4_o10_temporal_cup_bridge_exact_2026_08_29.py`
constructs both subset Casimirs on `V^5`, evaluates the cup-complement bridge,
and checks the rational defect sample.

The finite-field companion, independent of the local `Delta4` calculation but
importing the reviewed Block240 geometry and Block241 path structure,
`scripts/admissibility_exterior_character_jr_r2_q4_temporal_all_link_finite_field_2026_08_29.py`
reconstructs all eight original-link Gram terms at the disclosed control sample,
checks the four exact O10 formulas, and checks the four role-resolved O01
candidates at eight rational samples over three primes plus identity controls:
`247/247` checks pass.

The projector-resolved checker
`scripts/admissibility_exterior_character_jr_r2_q4_o10_post_pre_path_selection_2026_08_29.py`
inserts pure, independently labelled projectors in the full network. It checks
all 19 coherent paths over three primes, 26 one-insertion mismatches, five
forbidden nested triples, the exact O10 census, and the pre-Q scope:
`90/90` primary checks pass.

An independently written all-history scratch checker also resolves the other
three histories projector by projector: `182/182` checks pass, including the
power-five wrong-spin controls. This scratch result is corroborating evidence;
the tracked all-link companion is the review artifact.
