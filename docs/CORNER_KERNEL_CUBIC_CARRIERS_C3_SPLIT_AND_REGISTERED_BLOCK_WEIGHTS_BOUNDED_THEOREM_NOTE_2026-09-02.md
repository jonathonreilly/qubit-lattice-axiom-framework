---
claim_id: corner_kernel_cubic_carriers_c3_split_registered_block_weights
claim_type: bounded_theorem
claim_scope: "On the eight-dimensional kernel of the Kawamoto-Smit staggered hopping read on the coarse lattice 2Z^3 at the Brillouin-zone corner q = (pi,pi,pi), with the Cl(6) cell algebra Gamma = (Y_1, Z_1 Y_2, Z_1 Z_2 Y_3), Xi = (X_1, Z_1 X_2, Z_1 Z_2 X_3), epsilon = Z_1 Z_2 Z_3 and T = i Gamma_1 Gamma_2 Gamma_3 redeclared here, and for the twelve stipulated bilinears listed in the runner only: (T1) H(pi,pi,pi) = 0 so the whole cell is the corner kernel, the L = 4 coarse torus kernel is eight-dimensional, all 24 proper cubic rotations lift to integer signed permutations whose 576 products close on the nose on that kernel, the characters (E, 8C3, 3C2, 6C4, 6C2') = (8, 2, 0, 4, 0) decompose in exact rational arithmetic as 2 A1 + 2 T1, and the isotypic projectors in the corner basis are exactly P_A1 = diag(1,0,0,0,0,0,0,1) = P_hw0 + P_hw3 and P_T1 = diag(0,1,1,1,1,1,1,0) = P_hw1 + P_hw2, with each Hamming block separately O-invariant carrying characters (1,1,1,1,1) on hw = 0, 3 and (3,0,-1,1,-1) on hw = 1, 2. (T2) The 1+3+3+1 grading is the eigen-grading of the O-invariant Cl(6) bilinear i sum_a Gamma_a Xi_a = Z_1 + Z_2 + Z_3, spectrum 3 - 2 hw; the T1 isotypic is T1 (x) C^2 with a commutant of dimension 4 by the exact rational formula (1/24) sum |chi|^2, four independent commuting elements exhibited, so the group alone does not split it; T is O-invariant, unitary, carries hw = 1 onto hw = 2 and back with rank 3, and anticommutes with epsilon = diag((-1)^hw). (T3) On each triplet the C3[111] restriction U has tr U = 0, U^3 = I and eigenvalues {1, omega, omegabar}; its invariant vector has corner weights exactly (1/3, 1/3, 1/3); against the fixed democratic W = (1,1,1)/sqrt3 the overlaps are 1 and 1/9, a corner-sign gauge artefact removed by rephasing a single corner; the singlet projectors have every entry of modulus 1/3 and P_0, P_1 commute with U. (T4) Each of the twelve bilinears restricts to an exactly circulant operator on each triplet with residual 0 and c = conj(b): sum Gamma_a, sum Xi_a and T restrict to zero, i sum Gamma_a Xi_a gives a = +1 / -1 and epsilon a = -1 / +1 with b = 0, (sum Gamma_a)^2 = (sum Xi_a)^2 = 3I, the p_a^2 coefficient of H(pi+p)^2 is the identity on both, the Gamma-Gamma and Xi-Xi bivector sums give a = 0, |b| = 1, and i sum Gamma_a Xi_{a+1} and i sum Gamma_a Xi_{a+2} give a = 0, |b| = 1 with delta differing by pi between the two triplets; the six O-invariant ones have b = 0 by Schur and the six others have O-average exactly 0 hence a = 0, so no listed operator has a != 0 and b != 0 and every hw-diagonal one registers r = 0; and the restriction map from real C3-invariant Hermitian quadratics onto the circulant algebra has real rank 3 on each triplet, with alpha (sum Z_a) + beta i(sum_cyc Gamma_a Gamma_{a+1}) + gamma i(sum_a Gamma_a Xi_{a+1}) realising every (a, |b|, delta), the triples (2,1,1) and (2,1,0) registering r = 1/2 and r = 1/4 exactly. (T5) All six relabellings of each triplet and all 24 cubic conjugations leave (a, |b|, r) unchanged with circulant residual 0 for all twelve; naming C^2 rather than C the generator sends b to its conjugate, delta to -delta, and fixes (a, |b|, r). (T6) Exactly four of the twelve separate the two triplets -- i sum Gamma_a Xi_a and epsilon by the sign of a, and the two Gamma-Xi cross terms by delta differing by pi -- and no listed operator is C3-invariant with b != 0 on exactly one triplet. No corner is named, no bijection to a labelled 3-set is constructed, no sort key, Vandermonde sign, PDG value or species name appears, no block weight is derived, nothing here is derived from any axiom, no axiom is amended, no status is set and no hypothesis is adopted."
upstream_dependencies: []
runner: scripts/corner_kernel_cubic_carriers_c3_split_registered_block_weights_check_2026_09_02.py
---

# The corner kernel's two cubic carriers, their C3 split, and the block weight as a registered pattern

**Date:** 2026-09-02
**Type:** bounded_theorem
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:**
[`scripts/corner_kernel_cubic_carriers_c3_split_registered_block_weights_check_2026_09_02.py`](../scripts/corner_kernel_cubic_carriers_c3_split_registered_block_weights_check_2026_09_02.py)
**Runner cache:**
[`logs/runner-cache/corner_kernel_cubic_carriers_c3_split_registered_block_weights_check_2026_09_02.txt`](../logs/runner-cache/corner_kernel_cubic_carriers_c3_split_registered_block_weights_check_2026_09_02.txt)
**Parents:** none. Every premise used below is declared in this note.

The framework's landed corner-structure clause grades the eight Brillouin-zone corner states by Hamming weight as `1 + 3 + 3 + 1` and gives the `hw=1` triplet an
irreducible `M_3(C)`. That is stated as a fact about the corners, not as representation content, and it does not say why a triplet rather than some other three-dimensional
space should carry a family of three. This note reads the same eight states as a representation of the proper cubic group and asks two questions of the answer: which
three-dimensional carriers exist there, and what an operator built from the kinetic form assigns to the three members of one. There are exactly two carriers and they are
exactly the two Hamming triplets; and the assignment is empty -- every stipulated bilinear either weights the three members equally or gives them no diagonal weight at all,
while the map from stipulated coefficients onto weights is onto. A block weight on this carrier is supplied, not read off.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-dimensional theorems on an 8x8 algebra: the cubic representation content of the corner kernel, its isotypic projectors, the C3 restriction on each three-dimensional carrier, the exactly circulant restrictions of twelve stipulated bilinears with their block weights, the surjectivity of the restriction map onto the circulant algebra, and a full invariance census. Every statement is symbolic in sympy, exact-rational, or integer and Z[i] matrix arithmetic at zero tolerance; no item is numerical."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Run independent audit on this self-contained finite-algebra theorem, and route to its owner the science-level question this note does not decide: which sign of the chirality grading selects the carrier a generation-monitored family is read on."
conditional_surface_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the six statements below, exactly the runner's check groups `A`-`F`: `T1` (`A`) the corner kernel and its two three-dimensional cubic
carriers; `T2` (`B`) the grading as an eigen-grading, the multiplicity two, and the operator exchanging the carriers; `T3` (`C`) the `C_3[111]` restriction on each carrier
and its singlet; `T4` (`D`) the circulant restrictions of twelve stipulated bilinears, the absence among them of any operator with both a diagonal and an off-diagonal part,
and the surjectivity of the restriction map; `T5` (`E`) the invariance census; `T6` (`F`) which operators separate the two carriers. Every group is exact -- `sympy`
symbolic identities in the three momenta, exact rational character and projector arithmetic, integer and `Z[i]` matrix arithmetic at zero tolerance, exact Gaussian-rational
circulant decomposition -- and no item is `[numerical]`.

## Imports and authority

Imported scientific authority: none load-bearing. The Kawamoto-Smit staggering, the character table of `O`, Schur's lemma and the circulant form of a `Z/3`-equivariant
operator are standard methodology; every object is redeclared here and the runner recomputes every statement, the table's orthonormality included. No observational value,
fitted number or framework premise enters any proof. Non-load-bearing pointers, carrying no grade and no dependency weight:

- `EMERGENT_FERMION_PI_FLUX_SECTOR_IS_THE_STAGGERED_KINETIC_FORM_BOUNDED_THEOREM_NOTE_2026-09-02.md` (open PR #7844): the coarse-lattice `Cl(6)` kinetic form and its eight
  zero modes. Pointer only; the cell algebra is redeclared below and this runner rebuilds it.
- Quoted below, each for one sentence and no grade: `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` (the corner-structure clause);
  `AC_PHI_LAMBDA_PRESERVED_C3_STRUCTURAL_FORECLOSURE_BOUNDED_THEOREM_NOTE_2026-05-10.md` (the circulant form);
  `PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NARROW_THEOREM_NOTE_2026-06-05.md` (the singlet and doublet objects);
  `FLAVOR_HW1_STAGGERED_PROJECTION_DEMOCRATIC_R0_2026-06-02.md` (the landed `r = 0` on the fine cube);
  `ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md` (the carrier-locus residual and guardrail `G3`);
  `RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md` (the within-sector-free guardrail).
- `STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md` and
  `STAGGERED_DIRAC_SUBSTEP4_AMIN_JOINT_C3_AUTOMORPHISM_SELECTOR_INVARIANCE_BRIDGE_NARROW_THEOREM_NOTE_2026-07-05.md`: the labelling lane, pointers only, neither used nor
  re-attacked. `MINIMAL_AXIOMS_2026-06-29.md`: the four axioms quoted in "Setting"; this note cites none of their grades and adopts no hypothesis.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard
translations, and proper cubic rotations about each site." **Qubit**: "Each site has a domain of local possibilities", whose "full one-site possibility domain has algebraic
presentation `M_2(C)`". **Admissibility**: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations", and
"For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." **Record**: "Records form", "a
record locks exactly one admissible local possibility", "records are permanent", "Only records are readable."

The landed corner-structure clause under discussion, the generation lane's singlet and doublet objects, and the structural reason for the circulant form read, verbatim:

> **Corner-structure clause.** The free staggered operator has the 8-element BZ-corner (taste-cube) doubler set, decomposing uniquely by Hamming weight as `1 + 3 + 3 + 1`; the hw=1 triplet carries an exact irreducible `M_3(C)` algebra (translations + `C_3[111]`) with no proper exact quotient.

> On the `hw=1` triplet `V_1` with `W = (1,1,1)/sqrt(3)`, let `P_0 = |W><W| = J/3` (the `C_3`-singlet central-sector projector) and `P_1 = I - P_0` (the doublet sector).

> Any operator `H` commuting with `U_{C_3}` is by Schur's lemma a polynomial in `U_{C_3}` itself on each isotype, hence on `ℂ³` is circulant: `H  =  a · I  +  b · U_{C_3}  +  b̄ · U_{C_3}²`

**Guardrails.** Every statement below is written under these, and the runner checks them:

1. **No orbit-separating selector.** No corner is named, no bijection to any labelled 3-set is constructed, no sort key is used, no Vandermonde sign appears, no PDG value
   appears, and no species name is attached to any corner, carrier or coefficient.
2. **Invariance is checked, not assumed.** Every reported quantity is verified invariant under all six relabellings of each triplet and all 24 cubic conjugations, with the
   circulant residual exactly zero throughout.
3. **A block weight is a registered pattern.** Any `r` here is `r` *of a stipulated operator*, in the sense of the guardrail "`G3`: registered patterns are matched, not
   derived" and of the within-sector-free guardrail: "Weights/measures inside a sector (e.g. the Koide block-weight `r`, the solar/`theta_13` angles) are *not* the record's
   content." No `r` here is derived, and none is "the" `r`.
4. **`epsilon` is not identified with anything, and `AC_phi_lambda` stays exactly where the labelling no-go left it.** `epsilon = Z_1 Z_2 Z_3` is the chirality grading,
   distinct from `T = i Gamma_1 Gamma_2 Gamma_3` and not identified with any Vandermonde sign; the no-go note is a pointer here, and nothing below narrows it, widens it,
   or re-attacks it.
5. **Nothing is derived from the axioms.** The lattice, the sign field, the cell algebra and the twelve bilinears are declared objects; the theorems are about them.
   Composition is **ordinary** throughout, and every object lives in an `8x8` or `64x64` algebra.

## Obligation graph

The proof is acyclic and each node after `P0` is checked by the correspondingly lettered runner group. `P0`, declared here, is the coarse lattice, the KS sign field on it,
the eight-site cell and the `Cl(6)` set. `P1` (`A`) is the corner kernel and the cubic representation content; `P2` (`B`) the eigen-grading, the multiplicity and the
exchanging unitary; `P3` (`C`) the `C_3` restriction and its singlet; `P4` (`D`) the circulant restrictions, the structural fact and the surjectivity; `P5` (`E`) the
census; `P6` (`F`) the carrier-separating operators. The strongest supported scope is exactly `P0`-`P6`.

## Definitions

The **coarse lattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`. The **KS sign** of the coarse bond `(v, v + e_a)` is `eta_1 = 1`, `eta_2(v) = (-1)^{v_1}`,
`eta_3(v) = (-1)^{v_1 + v_2}`. The **cell** is one `2x2x2` block of coarse vertices, eight modes, so the Bloch block of the hopping is an `8x8` matrix `H(q)`; the
**corner** is `q = (pi, pi, pi)`; the **corner basis** indexes the eight cell states by a three-bit string, and **`hw`** is that string's Hamming weight.

```text
Gamma = (Y_1, Z_1 Y_2, Z_1 Z_2 Y_3),   Xi = (X_1, Z_1 X_2, Z_1 Z_2 X_3),   epsilon = Z_1 Z_2 Z_3,   T = i Gamma_1 Gamma_2 Gamma_3,
H(q) = sum_a [(1 + cos q_a) Xi_a + sin q_a Gamma_a],   C = the C_3[111] lift.
```

A **carrier** is a three-dimensional subspace invariant and irreducible under the 24 proper cubic rotations. A **stipulated bilinear** is one of the twelve operators of
Theorem 4, written by hand from the `Cl(6)` set with no coefficient adjusted to any target. For a `C_3`-invariant Hermitian `M` on a carrier, `(a, b)` are its circulant
coefficients in `M = a I + b U + bbar U^2`, `delta = arg b`, and the **block weight** is `r = |b|^2 / a^2` when `a != 0`.

## Theorem 1 -- the corner kernel has exactly two cubic carriers, and they are the Hamming triplets

**Conclusion.** (1) `H(pi, pi, pi) = 0`, so the whole eight-dimensional cell is the kernel at the corner; the `L = 4` coarse torus kernel is eight-dimensional and is
spanned by the corner basis. (2) All 24 proper cubic rotations lift to signed permutations preserving the hopping, and all 576 products close on the nose as integer
matrices on that kernel: a genuine representation of `O`, not projective. (3) Its characters `(E, 8C3, 3C2, 6C4, 6C2') = (8, 2, 0, 4, 0)` decompose, in exact rational
arithmetic against a self-checked orthonormal character table, as `2 A1 + 2 T1`, and the isotypic projectors are in the corner basis exactly `P_A1 = diag(1,0,0,0,0,0,0,1) =
P_hw0 + P_hw3` and `P_T1 = diag(0,1,1,1,1,1,1,0) = P_hw1 + P_hw2`, with `P_A2 = P_E = P_T2 = 0`. (4) Each Hamming block is separately `O`-invariant, with characters
`(1,1,1,1,1)` on `hw = 0, 3` and `(3,0,-1,1,-1)` on `hw = 1, 2` -- one `A1` and one `T1` each.

**Proof.** Item 1 evaluates the closed form symbolically at the corner momentum and verifies over `Z` that the corner basis is annihilated by the torus operator and has
Gram `8 I`. Item 2 solves each lift's signs by breadth-first propagation and compares all 576 products as integer matrices, the kernel-basis matrices obtained by exact
division by `8`. Items 3 and 4 are `Fraction` arithmetic: the orthogonality relations and the projector formula `P_irr = (d/24) sum_R chi_irr(R) M_R`, block by block.

**Reading, not theorem.** The eight corner states sort themselves under the cube's rotations into two singletons and two triplets, and the triplets are exactly the ones the
earlier grading found. The grading was written down as a fact about bit-counts; it turns out to be the representation content, on the nose.

## Theorem 2 -- the grading is an eigen-grading, and the two carriers are exchanged

**Conclusion.** (1) `i sum_a Gamma_a Xi_a = Z_1 + Z_2 + Z_3` exactly; it commutes with all 24 lifts, and its corner spectrum is `3 - 2 hw`, so the `1 + 3 + 3 + 1` grading
is the eigen-grading of that one `O`-invariant `Cl(6)` bilinear. (2) The `T1` isotypic is `T1 (x) C^2`: the commutant of the 24 lifts has dimension `8` on the kernel and
`4` on the `T1` isotypic, by the exact rational formula `(1/24) sum |chi|^2`, and four independent commuting elements `P_hw1`, `P_hw2`, `P_hw2 T P_hw1`, `P_hw1 T P_hw2` are
exhibited -- the group alone does not split the six-dimensional isotypic. (3) `T = i Gamma_1 Gamma_2 Gamma_3` commutes with all 24 lifts, is unitary, carries `hw = 1` onto
`hw = 2` and back with rank `3`, and anticommutes with `epsilon = Z_1 Z_2 Z_3 = diag((-1)^hw)`; `T != epsilon`.

**Proof.** Item 1 is a `Z[i]` matrix identity and a diagonal read-off, with commutation checked against all 24 integer lifts at zero tolerance. Item 2 is the character
formula in `Fraction` arithmetic plus a commutation check and a rank computation for the four exhibited elements. Item 3 is `Z[i]` arithmetic: unitarity, the vanishing of
`P_hw1 T P_hw1` and `P_hw2 T P_hw2`, the rank of the off-diagonal blocks, and the anticommutator. All exact.

**Reading, not theorem.** The rotations see one six-dimensional space with a two-fold multiplicity, not two separate triplets. What cuts it in two is not the group but the
chirality grading, and the operator that carries each half onto the other reverses that grading. The two triplets are the same object twice over, told apart by a sign and by nothing else
the rotations can see. Each of them splits again, under the one rotation that cycles the three axes, into a direction fixed by that rotation -- spread evenly over the three
members, exactly a third on each, and that even spread survives every relabelling -- and a two-dimensional remainder.

## Theorem 3 -- the C3 restriction and its singlet

**Conclusion.** On each carrier, with `U = C|_{T1}`: (1) `tr U = 0`, `U^3 = I`, eigenvalues `{1, omega, omegabar}` -- each carrier is the regular representation of `Z/3`.
(2) The `C`-invariant vector has corner weights exactly `(1/3, 1/3, 1/3)` on both carriers; against the *fixed* democratic `W = (1,1,1)/sqrt3` the overlaps are `|<W|v>|^2 =
1` on one carrier and `1/9` on the other, and that difference is a corner-sign gauge artefact, removed by rephasing a single corner, which carries `U` to the plain 3-cycle
and `v` to `W`. (3) The singlet projectors `P_0 = |v><v|` have every entry of modulus `1/3` -- `P_0 = J/3` in the gauge that carries `v` to `W` -- are idempotent, and `P_0`
and `P_1 = I - P_0` both commute with `U`.

**Proof.** Item 1 is exact `3x3` arithmetic over `Z`: the trace, the cube, and the eigenvalues as exact cube roots of unity. Item 2 computes the nullspace of `U - I`
exactly and evaluates the weights and overlaps as exact rationals, the rephasing being the diagonal sign matrix read off the invariant vector. Item 3 is exact idempotence,
entrywise modulus and commutation.

## Theorem 4 -- the block weight of every stipulated bilinear, and the surjectivity

**Conclusion.** For the twelve stipulated bilinears:

1. Each restricts to an **exactly** circulant operator on each carrier -- residual exactly `0`, `c = conj(b)` throughout -- with the coefficients the runner tabulates:
   `sum_a Gamma_a`, `sum_a Xi_a` and `T` restrict to zero; `i sum_a Gamma_a Xi_a` gives `a = +1 / -1` and `epsilon` gives `a = -1 / +1`, both with `b = 0`; `(sum_a
   Gamma_a)^2 = (sum_a Xi_a)^2 = 3 I`; the `p_a^2` coefficient of `H(pi + p)^2` is the identity on both carriers; the two bivector sums `i(Gamma_x Gamma_y + Gamma_y Gamma_z
   + Gamma_z Gamma_x)` and its `Xi` counterpart give `a = 0`, `|b| = 1`; and the two `Gamma`-`Xi` cross terms give `a = 0`, `|b| = 1` with `delta` differing by `pi` between
   the carriers.
2. **The structural fact.** No listed operator has `a != 0` and `b != 0`. The six that commute with all 24 lifts have `b = 0` by Schur on an irreducible `T1`; the
   `O`-average of each of the other six is exactly `0`, and `a` depends on the `O`-average alone because the Hamming projectors are `O`-invariant, so `a = 0` there. Hence
   every hw-diagonal listed operator registers `r = 0` exactly.
3. **The surjectivity.** The restriction map from real `C_3`-invariant Hermitian quadratics onto the circulant algebra has real rank `3` on each carrier: the three-element
   family `alpha (sum_a Z_a) + beta i(sum_cyc Gamma_a Gamma_{a+1}) + gamma i(sum_a Gamma_a Xi_{a+1})` maps onto `(a, Re b, Im b)` with rank `3`, so every `(a, |b|, delta)`,
   hence every `r` in `[0, inf)`, is realised by stipulated coefficients -- `(alpha, beta, gamma) = (2, 1, 1)` registering `r = 1/2` and `(2, 1, 0)` registering `r = 1/4`,
   exactly and on both carriers. **These are stipulated coefficient choices exhibited as registered patterns; neither is derived, and neither is "the" `r`.**

**Proof.** Item 1 builds each operator over `Z[i]` at zero tolerance, verifies hermiticity and Gaussian-integrality, restricts it and decomposes it exactly by `a = tr M /
3`, `b = tr(M U^2) / 3`, `c = tr(M U) / 3`, comparing the residual against the zero matrix as an exact symbolic identity; the `p_a^2` coefficient comes from symbolic
differentiation of `H(pi + p)^2`. Item 2 checks the 24 commutators, forms the exact integer sum `sum_R M_R O M_R^T` and compares it to `0` or to `24 O`. Item 3 is an exact
rank over the rationals and two exact evaluations.

**Reading, not theorem.** Turning the cube cannot tell the three members of a triplet apart, and no operator built from the kinetic form alone assigns them a weight: it is
either blind to them and weights them equally, or has nothing on the diagonal to weight them with. A weight has to be supplied -- and once one is willing to supply
coefficients every weight is available, so a weight carries exactly as much information as the coefficients chosen for it.

## Theorem 5 -- the invariance census

**Conclusion.** For all twelve operators and both carriers: (1) all six relabellings of a carrier's basis leave `(a, |b|, r)` unchanged, with circulant residual `0`; (2)
all 24 cubic conjugations, `O -> g O g^{-1}` with `C -> g C g^{-1}`, which cover all eight `C_3` elements, leave `(a, |b|, r)` unchanged, with residual `0`; (3) naming
`C^2` rather than `C` the generator sends `b -> conj(b)`, that is `delta -> -delta`, and leaves `(a, |b|, r)` fixed.

**Proof.** Items 1 and 2 re-run the exact circulant decomposition on the relabelled or conjugated data and compare the coefficients as exact symbolic quantities; item 3
re-runs it against `U^2` in place of `U`. All exact.

## Theorem 6 -- which operators separate the two carriers

**Conclusion.** Exactly four of the twelve distinguish the two carriers: `i sum_a Gamma_a Xi_a = sum_a Z_a` and `epsilon`, by the sign of `a` -- that is, through the sign
convention of the chirality grading -- and `i sum_a Gamma_a Xi_{a+1}` and `i sum_a Gamma_a Xi_{a+2}`, with equal `|b|` and `delta` differing by exactly `pi`. The remaining
eight restrict identically to both. No listed operator is `C_3`-invariant with `b != 0` on exactly one carrier.

**Proof.** A direct comparison of the exact table of Theorem 4 across the two carriers, with the phase difference evaluated as an exact symbolic identity.

**Reading, not theorem.** Nothing reported here depends on which member of a triplet is written first, or on which axis the reader calls the first; the one choice that
shows is the direction of the cycle, and it flips the sign of one angle and moves nothing else. As for the two triplets, the only things in this list that tell them apart
are the grading itself and terms mixing the two halves of the Clifford set, and even those give both the same magnitude, differing by a sign or a phase. Nothing here makes
one triplet the one that carries a weight while the other does not.

## Corollary -- what this says about the corner carrier and about `r`

Within the setting declared above, and on the finite algebra named:

1. **Why a triplet, and which one.** The corner kernel admits exactly two three-dimensional cubic carriers, both Hamming-weight triplets of the landed grading, exchanged
   by the `O`-invariant unitary `T`, which reverses the chirality grading. So "why a triplet" is forced by the representation -- the rotations offer nothing else of
   dimension three -- and "which triplet" reduces to the sign of `epsilon`. The species-bridge note's structural residual, "why the generation-monitored family is supported
   on the `hw=1` triplet at all", is thereby **narrowed to that one sign, and not closed**: its own observation that "the naive dispersion is hw-blind" is reproduced here
   exactly, as the statement that the `p_a^2` coefficient of `H(pi + p)^2` is the identity on both carriers.
2. **`r` is registered, never delivered.** On these carriers every stipulated bilinear either registers `r = 0` or has no diagonal part at all, and the restriction map onto
   the circulant algebra is onto, so the block weight is a free function of stipulated coefficients. This reproduces the landed democratic result -- "this projection route
   gives `r = |b|^2/a^2 = 0`" -- on a **new carrier**: that note's scope is one operator `K` on the fine `C^8` cube, while this is structural, about twelve operators on the
   coarse-lattice corner kernel, with a reason (Schur on one side, a vanishing `O`-average on the other) rather than one computation. Guardrail `G3` -- "registered patterns
   are matched, not derived" -- is here a theorem on this carrier, not a discipline imposed on it.
3. **Nothing is labelled and nothing moves.** No corner is named, no bijection to a labelled 3-set exists in this note or its runner, and `AC_phi_lambda` stays exactly
   where the labelling no-go left it.

## What does not move

- No axiom text is amended, extended, reworded, or reinterpreted; no hypothesis is adopted; no status value is set, predicted, or implied; no premise registry, citation
  manifest, or axiom-premise node is created or edited; and no update rule, formation site, formation rate, coupling, absolute unit or dynamical clause appears.
- Nothing here is derived from the axioms: the lattice, the sign field, the cell algebra and the twelve bilinears are declared objects. No corner of the taste cube is
  identified with any named species, no value of `r` is claimed as a physical one, and the labelling no-go and its joint-automorphism bridge are pointers only, their
  scope untouched -- this note computes nothing that separates a `C_3` orbit.

## Interfaces named for other lanes, not moved here

- **The sign of `epsilon` as the carrier selector.** Theorem 6 reduces "which of the two carriers" to the sign of the chirality grading. That sign is a **supplied datum**:
  nothing here derives it, and a lane wanting one carrier rather than the other must supply it and say so -- as Theorem 4 item 3 says what a lane must supply for a nonzero
  `r`, a coefficient triple, and supplies none.
- **The many-body content and the labelling lane.** Everything here is one-particle; what the rotations, the grading and the circulant coefficients do to many-body states
  is untouched. And this note gives representation content and orbit-invariant coefficients, never a labelled bijection: the no-go note states what is not derivable and
  nothing here narrows or widens it, Theorem 6's "which carrier" being a different question on a different orbit from the no-go's "which corner".

## Remaining live routes

1. Other operator classes. Twelve bilinears are what is tested; quartic terms, interactions, non-Hermitian objects and momentum-dependent operators are not.
2. Larger cells and other geometries, and the two `A1` singletons. The `L = 4` coarse torus and the one `2x2x2` cell are what is proved, nothing is claimed beyond them,
   and the `hw = 0` and `hw = 3` states are not examined beyond their characters.

## Executable claim block

```text
setting: eight-dimensional corner kernel of the KS staggered hopping on 2Z^3 at q = (pi,pi,pi); Cl(6) cell algebra Gamma, Xi, epsilon = Z1Z2Z3, T = i G1G2G3; ordinary composition; four axioms quoted from MINIMAL_AXIOMS_2026-06-29.md
carriers: H(pi,pi,pi) = 0; L=4 torus kernel dim 8; 24 lifts, 576 products exact on the kernel, genuine O; chi = (8,2,0,4,0) = 2 A1 + 2 T1; P_A1 = diag(1,0,0,0,0,0,0,1) = P_hw0 + P_hw3 and P_T1 = diag(0,1,1,1,1,1,1,0) = P_hw1 + P_hw2 exactly; hw blocks O-invariant with chi (1,1,1,1,1) and (3,0,-1,1,-1)
grading_multiplicity_and_c3_split: i sum Gamma_a Xi_a = Z1+Z2+Z3, spectrum 3 - 2 hw, O-invariant; commutant dim 8 on the kernel and 4 on the T1 isotypic; T O-invariant, unitary, hw1 <-> hw2 at rank 3, anticommutes with epsilon = diag((-1)^hw); tr U = 0, U^3 = I, eigenvalues {1, omega, omegabar}; invariant-vector corner weights exactly (1/3,1/3,1/3) on both; |<W|v>|^2 = 1 and 1/9, a one-corner rephasing apart; P_0 entries of modulus 1/3, [P_0,U] = [P_1,U] = 0
circulant_table: all 12 restrictions exactly circulant, residual 0, c = conj(b); sum Gamma_a, sum Xi_a, T restrict to 0; i sum Gamma_a Xi_a a = +1/-1, epsilon a = -1/+1, both b = 0; (sum Gamma)^2 = (sum Xi)^2 = 3I; p_a^2 coeff of H(pi+p)^2 = I on both; bivector sums a = 0, |b| = 1; Gamma-Xi cross terms a = 0, |b| = 1, delta differing by pi
structural_fact_and_surjectivity: 6 O-invariant operators have b = 0 by Schur, the other 6 have O-average exactly 0 hence a = 0, so none has a != 0 and b != 0 and every hw-diagonal one registers r = 0; real rank 3 on each carrier from alpha(sum Z_a) + beta i(sum_cyc G_a G_{a+1}) + gamma i(sum G_a Xi_{a+1}), with (2,1,1) registering r = 1/2 and (2,1,0) registering r = 1/4, both stipulated
invariance: 6 relabellings x 12 operators x 2 carriers and 24 conjugations x 12 x 2 leave (a,|b|,r) fixed with residual 0; C -> C^2 sends delta -> -delta only
carrier_locus: exactly 4 of 12 separate the carriers (2 by the sign of a, 2 by delta differing by pi); none is C3-invariant with b != 0 on exactly one carrier
corners_named_labelled_bijections_pdg_values_axioms_amended_status_values_set: 0, 0, 0, 0, 0
runner_result: PASS=20 FAIL=0
```

## Proof boundary

Everything is proved on the **corner kernel** of the coarse-lattice KS operator: an `8x8` algebra, with the cubic lifts built on the `L = 4` coarse torus, a `64x64`
construction. Nothing is claimed for other momenta, other lattices, larger cells, or the fine lattice `Z^3`. The content is **representation structure and circulant
coefficients of stipulated operators**, not dynamics. No coefficient in the twelve is fitted, no coupling, mass, rate or unit appears, and no dynamical clause is supplied.
The two coefficient triples of Theorem 4 item 3 are registered patterns of stipulated operators -- they show the map onto weights is onto and derive nothing; `Q = 1/3 +
(2/3) r` is not evaluated here. The surjectivity statement is about the three-element family named there: it establishes that the image of the restriction map is the whole
real circulant algebra, claims no physical motivation for any member, and supplies no principle for choosing one. The two carriers are distinguished here only by the sign
of `epsilon`, a convention this note does not fix; every statement above is therefore symmetric under exchanging the two carriers together with the sign of the grading, and
the runner's tables should be read that way.

## Review record

An honest auditor should come away with: one exact identification, on an `8x8` algebra, of the landed `1 + 3 + 3 + 1` Hamming grading with the isotypic decomposition `2 A1
+ 2 T1` of the proper cubic group on the corner kernel, so the only three-dimensional carriers there are the two Hamming triplets; one multiplicity statement saying the
group alone does not split them, and one operator exchanging them while reversing the chirality grading; one exact table of twelve stipulated bilinears whose restrictions
are all circulant and none of which carries both a diagonal and an off-diagonal part, so every hw-diagonal one registers `r = 0`; one surjectivity statement showing the
weight is a free function of stipulated coefficients; a full invariance census; and two things deliberately not decided -- which sign of the chirality grading selects a
carrier, and any labelling whatever of the three members of one. The labelling no-go is cited without being used.

This note is self-contained: `upstream_dependencies` is empty, every object is declared in "Definitions", no hypothesis is adopted, and the pointers in "Imports and
authority" carry no grade and no weight. Hard landing conditions are a fresh runner and cache pair closing at `PASS=20 FAIL=0`, runtime under the declared `120` seconds,
stdout under `8000` characters, a zero-dependency citation-manifest entry, and passing pipeline, strict-lint and changed-evidence gates; independent audit is a separate
lane.
