---
claim_id: su2_equivariant_one_qubit_qca_translation_rigidity_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For every integer d >= 1, a complex-linear *-automorphism of the infinite qubit quasi-local tensor algebra over Z^d which maps every local operator to an operator of finite support, commutes with every one-site lattice translation, and commutes with global on-site SU(2), is a lattice translation. On Z^3, covariance under the supplied full action beta_R = Ad(D_R^tensor) pi_R of an irreducible proper cubic subgroup H, together with conservation of a supplied nonzero on-site U(1), forces identity. A local SU(2)-invariant qubit operator whose translates all commute is scalar. These are conditional algebraic statements; neither the dynamics nor the symmetry conditions are derived from the framework axioms."
upstream_dependencies:
  - minimal_axioms
runner: scripts/su2_equivariant_one_qubit_qca_translation_rigidity_2026_10_21.py
---

# Strictly local SU(2)-equivariant one-qubit QCAs are translations

**Date:** 2026-10-21
**Type:** bounded_theorem
**Status:** conditional theorem with an analytic proof below; unaudited.

## Result and supplied premises

**Theorem 1.** For any integer d >= 1, let A be the norm completion of the
union of the finite tensor algebras A(F) = tensor_{x in F} M_2(C), F a finite
subset of the infinite lattice Z^d. Let alpha be a complex-linear
*-automorphism of A. Assume:

- strict finite locality: alpha maps every finite-support operator to a
  finite-support operator;
- exact one-site translation invariance: alpha tau_t = tau_t alpha for every
  t in Z^d;
- exact on-site SU(2) equivariance: alpha gamma_D = gamma_D alpha for every
  D in SU(2), where gamma_D acts as Ad(D) on every site.

Then alpha = tau_c for a single c in Z^d. Translation is allowed and need
not be zero. The full-action conserved-U(1) corollary below sets c = 0 under
additional stated hypotheses. Lemma C also proves that all translates of a
local SU(2)-invariant qubit operator commute only when it is scalar.

The [minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the one-site
M_2(C) and Z^3 baseline only. The tensor-algebra dynamics, strict locality,
exact SU(2) symmetry, conserved U(1) and selected full action are supplied
mathematical conditions. The d != 3 generalization is a mathematical domain,
not a change to the framework lattice. No evolution, physical observable,
transport law or action selection is derived from the axioms.

Three elementary mathematical facts used in the proof are explicit:

- On two qubits, the singlet and triplet are inequivalent irreducible SU(2)
  representations of dimensions one and three. An invariant operator is a
  scalar on each, so their commutant is span{1, P_swap}. This is the only
  Schur–Weyl consequence needed by the proof; the runner's n <= 5 checks
  are supplementary finite matrix checks.
- Every tracial state restricts on A(F) to its unique normalized matrix
  trace. These traces agree under tensoring with identity; density of the
  local union gives the unique tracial state on A. Therefore alpha preserves it.
- Expanding a local operator in the tensor Pauli basis gives a unique minimal
  support: the union of sites carrying a nonidentity factor in a nonzero
  coefficient. Removing a site is equivalent to all its vector channels
  vanishing. This also justifies the fresh-site step below.

## Proof of Theorem 1


Notation: σ^j_x are the Paulis, P_{xy} = (1 + σ_x·σ_y)/2 is the swap, and an "invariant" operator
is one fixed by every γ_D. Since α commutes with γ_D, α maps invariant operators to invariant
operators.

**Lemma B (one-site overlap).** Let g ∈ A(A) and h ∈ A(B) be invariant, with A ∩ B = {a}.
1. Write g = X_0 ⊗ 1_a + Σ_j X_j ⊗ σ^j_a and h = Y_0 ⊗ 1_a + Σ_k Y_k ⊗ σ^k_a. These
   decompositions are unique, with X's in A(A∖a) and Y's in A(B∖a).
2. Invariance makes X_0 invariant and (X_j) a vector operator: γ_D(X_j) = Σ_k R_{kj}(D) X_k.
3. All cross terms commute because their supports are disjoint. Hence
   **[g,h] = 2i Σ_{jkl} ε_{jkl} X_j Y_k σ^l_a**.
4. Suppose [g,h] = 0. Apply functionals φ ⊗ ψ: x × y = 0 for every x ∈ V_X := {(φ(X_j))_j} and
   y ∈ V_Y.
5. V_X and V_Y are SO(3)-invariant subspaces of C^3. Since C^3 is irreducible, each is 0 or C^3.
   If both were C^3, then x × y = 0 would fail.
6. Hence [g,h] = 0 ⟺ X = 0 or Y = 0. That is, one of g, h acts trivially on a.

The canonical runner B checks the commutator formula with tolerance 1e-10,
rank V_X = 3 in its sampled cases, 20 random non-commuting pairs,
and the converse.

**Lemma C (lexicographic translate).** Let g be invariant and non-scalar, with minimal support S.
Then |S| ≥ 2, because single-site invariant operators are scalars. Fix any total order ≺ on Z^d
compatible with translations, for instance by a generic linear functional ℓ. Here "generic" means injective on Z^d, i.e. ℓ(v) ≠ 0 for every v ∈ Z^d ∖ {0}. Let s1 = max S,
s2 = min S, and t = s1 − s2 ≠ 0.
1. Then S ∩ (S+t) = {s1}. If p ∈ S and p − t ∈ S, then p ⪯ s1 and p ⪰ s2 + t = s1.
2. τ_t g has vector channel at s1 equal to the translate of g's vector channel at s2. By
   minimality both vector channels are nonzero.
3. So by Lemma B, **[g, τ_t g] ≠ 0**.

Corollary: if F is finite, A ∈ A(F) is invariant and non-scalar, and β is a TI automorphism
preserving invariance, then [β(A), τ_t β(A)] = β([A, τ_t A]). This vanishes whenever
F ∩ (F+t) = ∅. Hence **for every generic ℓ, t_ℓ(β(A)) ∈ (F − F) ∖ {0}**. Lemma C itself is also
the commuting-translates side lemma: a nonscalar invariant g has at least
one translate with a nonzero commutator.

**Step D (swaps go to bonds).** Let e be a coordinate nearest-neighbor vector (one of the unit lattice vectors).
Take F = {0, e} and A = P_{0e}, so F − F = {0, ±e}.
1. For every generic ℓ, the ℓ-extreme points of S := supp α(P_{0e}) differ by ±e.
2. Let v = s − s′ for any s, s′ ∈ S. Then |ℓ(v)| ≤ max_S ℓ − min_S ℓ = |ℓ(e)| for every generic ℓ.
   By density this holds for every ℓ ∈ R^d, and that forces v ∈ R·e with |v| ≤ |e|. As v is in
   Z^d, v ∈ {0, ±e}. With |S| ≥ 2, S = {p, p+e}.
3. The runner exhausts sets in the 3^3 box with 2 ≤ |S| ≤ 4 against 40 sampled
   linear functionals and finds only the 18 x-bonds. This finite check does not
   prove the universal quantifier in Step 2.
4. The invariant algebra of two qubits is span{1, P} (the singlet/triplet argument above). So α(P_{0e}) = a + bP_{p,p+e}.
5. α(P_{0e}) is a non-scalar self-adjoint unitary with normalised trace τ(P) = 1/2 (the unique trace argument above). That
   forces a = 0 and b = +1.
6. So **α(P_{x,x+e}) = P_{x+c_e, x+c_e+e}**, where TI gives the x-dependence.

**Step F (one common shift).**
1. Two NN swaps fail to commute iff their bonds share exactly one site, and α preserves
   (non)commutation.
2. For arbitrary i != j, the e_i-bond at 0 and the e_j-bond at y, sharing happens iff y ∈ D_ij = {0, e_i, −e_j,
   e_i − e_j}.
3. The images share iff y + c_j − c_i ∈ D_ij. So D_ij + (c_j − c_i) = D_ij, and a finite set is
   invariant under no nonzero translation. Hence c_i = c_j for every i != j. For d = 1 there is only one bond
   direction, so the common-shift step is vacuous. For every d >= 2, apply the
   argument to all pairs of coordinate directions, giving c_1 = ... = c_d =: c.
   The runner checks the three-dimensional finite examples.

**Step G (identity).** α′ := τ_c^{-1} ∘ α is a TI, SU(2)-symmetric automorphism fixing every NN
swap. NN transpositions generate the symmetric group of every finite box (the canonical runner G: S_8 on the
unit cube). So α′ fixes every P_{yz}.
1. Let W^j := α′(σ^j_0). For y, z ≠ 0, [σ^j_0, P_{yz}] = 0 gives [W^j, P_{yz}] = 0.
2. Suppose y ∈ supp W with y ≠ 0, and choose z ∉ supp W ∪ {0}. Then
   0 = [W, σ_y·σ_z] = Σ_k [W, σ^k_y] ⊗ σ^k_z, so [W, σ^k_y] = 0 for every k. Then W ∈ A(supp W∖y),
   which contradicts minimality.
3. So supp W ⊆ {0}. Single-qubit vector operators are λσ (the canonical runner G: nullity 1). Hermiticity,
   W² = 1 and α′(σ^1)α′(σ^2) = iα′(σ^3) give λ = 1.
4. So α′ = id and **α = τ_c**. ∎

**Corollary 2 (full action plus a conserved on-site U(1), d = 3).**
Retain Theorem 1's algebra, automorphism, strict-locality and translation
hypotheses, but replace its assumed SU(2) equivariance by the conditions below.
Let H be a subgroup of the proper cubic rotation group acting irreducibly on R^3.
Let pi_R permute sites by x -> Rx, choose either spin-half lift D_R in SU(2),
and define beta_R = gamma_{D_R} pi_R. The sign of the lift has no effect on
its adjoint action. Assume alpha beta_R = beta_R alpha for every R in H and
alpha commutes with gamma_{exp(i theta m.sigma/2)} for every real theta,
where m is a fixed nonzero real vector. These are supplied conditions.
Then alpha = id.

1. U(1) about m plus full-action covariance gives conservation of the U(1) about Rm for every
   R ∈ H (conjugate the conserved on-site rotations by beta_R). The span of {Rm} is a nonzero H-invariant subspace, so it is R^3 when
   H is irreducible. The corresponding generators i(Rm).sigma span su(2), so the generated
   connected subgroup is SU(2). Continuity on each finite local algebra extends
   commutation to all of SU(2); alpha is SU(2)-symmetric.
   Irreducibility is needed: for the axis-π group D2 with m = e1, the orbit is ±e1 only.
2. By Theorem 1, α = τ_c.
3. Covariance gives β_R τ_c β_R^{-1} = τ_{Rc} = τ_c. So Rc = c for all R ∈ H. An irreducible H
   fixes no nonzero vector, hence c = 0. ∎
   (If SU(2) is assumed directly, as in Theorem 1, then any H fixing no nonzero vector, including
   D2, already gives α = id.)

## Scope and verification limits

The theorem concerns the infinite tensor algebra and all its local operator
images. A finite torus, a restriction to one particle-number sector, or a
sample of matrices does not establish this infinite statement. The proof
supplies the universal argument; the runner supplies finite checks of its
ingredients. It does not classify motion for larger on-site algebras,
sublattice translations, approximate symmetry or quasi-local Hamiltonian
flows. Cubic covariance alone does not imply SU(2) conservation and does
not select the full action over another action. Hamiltonian motion is not
forbidden by this result. Any application to an exact discretization must
satisfy all hypotheses and retain the translation exception in Theorem 1.

The canonical runner preserves the original finite numerical checks:
commutants through five qubits; one-site overlap; sampled extreme-support
examples; the two-site trace/sign step; bounded-box support and bond-overlap
checks; one-site vector algebra; fresh-site elimination; and nearest-neighbor
transposition generation on the eight-site cube. Seed, dimensions and
thresholds are fixed in the source. Sampled tests are diagnostics, not
exhaustive QCA enumeration or exact infinite-lattice certificates.

## No-Go Discipline Gate

The negative assertion is limited to nontranslation automorphisms under
Theorem 1's hypotheses, and nonidentity automorphisms under Corollary 2's
additional hypotheses. This packet documents the routes and boundaries;
it is not an audit verdict or a claim that failed searches prove the theorem.

### N1 — Distinct attempted mechanisms

The five families below differ in primary object or terminal compatibility
conditions. ATTEMPTED refers to the preserved original campaign, not five
new searches during this canonical repair. None is called RULED OUT BY PRIOR:
no unaudited historical sibling is used as retained authority. The analytic
proof in this note supplies the universal conditional conclusion.

| Family and attempted construction | Terminal obligation and disposition | Evidence and limit |
|---|---|---|
| ATTEMPTED: build a commuting family from all translates of a local SU(2)-invariant gate generator | Every pair of translates must commute; Lemma C excludes every nonscalar local generator | Lemmas B–C here; finite overlap/support diagnostics in the canonical runner |
| ATTEMPTED: monomial pair motion with fixed singles and a lowering map | For a basis pair, S-minus sends the unordered pair {x,y} to the sum of its two distinct singleton basis vectors; that sum fixes both the pair and its phase when singles are fixed | This direct injectivity observation covers only the monomial pair proposal, not general QCA rigidity; historical C4f and C9 sector discussion motivated it |
| ATTEMPTED: nonmonomial motion in highest-weight / kernel-of-S-minus sectors | Sector-level gliders can satisfy lowering constraints; extending a nontranslation proposal to a strictly local SU(2)-equivariant automorphism is the remaining compatibility requirement | Historical C9 sector witnesses are preserved but deferred from this salvage; Theorem 1 closes only the full-algebra extension under its hypotheses, not the sector construction itself |
| ATTEMPTED: choose an SU(2)-invariant image of a swap as a self-adjoint involution of trace 1/2 | The image must commute with all translates corresponding to disjoint original bonds; Steps D–F force a translated bond swap | Historical c9_03 finite optimization is sampled diagnostic evidence, with incomplete runs preserved; the proof does not rely on optimizer convergence |
| ATTEMPTED: choose an equivariant Pauli-image triple | It must satisfy Pauli multiplication and intersite commutation; after the swap argument, Step G forces the translated single-site Pauli triple | Historical r01 finite optimization contains approximate near-shifts, not certified exact solutions; its n=4 distances remain 1.26e-4–1.91e-4 and are not promoted to exact evidence |

The two optimization formulations differ: swap images obey invariant
involution/trace/translate constraints, while Pauli images obey vector
covariance, Pauli multiplication and intersite commutation. Counts of
routes or converged samples have no bearing on universal validity.
Historical scripts and failed logs remain recoverable at original commit
`e294c1dc745dad0c95b4c8688efc6f3f0be03613`, under
`.claude/science/physics-loops/toe-scale-ladder-20261018/blocks/C9/`.

### N2 — Relations among scope conditions

The conditions are a single conjunction, not a count of independent
physical walls. Write T for exact unit translations, Q for one qubit per
site, S for exact SU(2), and L for strict finite locality. No independence
claim is made for any pair.

| Pair | Implication or dependence actually used |
|---|---|
| T, Q | Regrouping a sublattice-invariant qubit system into larger cells changes both the translation unit and on-cell algebra; these relaxations are related |
| T, S | No implication is used; both are separately supplied |
| T, L | No implication is used; both are separately supplied |
| Q, S | The qubit representation permits SU(2), but does not require the dynamics to conserve it |
| Q, L | No implication is used; both are separately supplied |
| S, L | No implication is used; exact conservation does not supply a finite-support propagation rule |

These entries do not assert either direction of a missing implication is
proved false. Pairwise independence is unassessed and no wall count depends
on it. Full-action covariance and conserved U(1) are only the corollary's
explicit sufficient route to S.

### N3 — Premise scan

The proof uses the infinite lattice, finite tensor support, one-site M_2(C),
complex-linear *-automorphism, exact translations and exact SU(2).
The corollary additionally uses the specified beta_R, nonzero conserved
axis m, and irreducibility of H on R^3. Trace preservation, minimal support,
the two-site commutant and single-site vector irreducibility are mathematical
facts explained above, not physical imports. Equivariance implies preservation
of invariant operators. No index classification, GNVW statement, scale,
kinetic-isotropy or realized-state primitive enters the argument. Canonical
file placement and historical review provenance provide no scientific premise.

### N4 — Residual matching

| Reference or mechanism | Residual actually addressed | Use here |
|---|---|---|
| Lemma C in this note | Commuting translates of one local invariant qubit operator | Exact match to the commuting-generator family |
| Monomial lowering-map observation in N1 | Fixed-single monomial pair motion | Narrow diagnostic only; not used to exclude nonmonomial sectors |
| Steps D–G in this note | Full-algebra strictly local SU(2)-equivariant automorphism | Exact match to Theorem 1, retaining arbitrary translation |
| Full-action orbit/Lie-algebra proof in Corollary 2 | Supplied full action and conserved on-site U(1) | Exact match to the corollary; no conclusion for full-action covariance without conserved U(1)/SU(2) |
| Historical sector witnesses and finite optimizers | Restricted sectors or finite ansatz diagnostics | No universal no-go authority imported |

### N5 — Resolution audit

Per-element checks exercise finite Pauli and swap matrices and normalized
traces. Per-site checks exercise the finite vector algebra and fresh-site
elimination mechanism. No mode dynamics or dispersion test is executed.
Per-block checks exercise finite matrices and sampled/bounded support tests.
The lattice-wide statement is proved analytically in the note, not by
numerically enumerating QCAs. The runner emits these five resolution lines
verbatim in its cached stdout. None of its finite PASS counts certifies a
physical evolution or strengthens the quantified theorem.

### N6 — Partial results and premise relaxations

Theorem 1 already allows translation. Corollary 2 excludes it only when its
additional action/symmetry hypotheses hold. Larger cells, sublattice
translation invariance, weaker symmetry and quasi-local evolution change
the premise class; they are not excluded routes within it. Their broader
classification remains outside this salvage. A different physical
identification or convention does not contradict the algebraic theorem and
is not characterized as requiring a new axiom. No axiom or primitive is
adopted or retired here.

### N7 — Strongest counter-route

A hostile counterexample would be a nontranslation SU(2)-equivariant
finite-depth circuit whose complete product commutes with every one-site
translation, even if its individual layers do not. Heisenberg swap gates
make this a concrete design to examine; citing mobile Hamiltonian magnons
or a sector glider alone does not supply the missing full-algebra circuit.
To refute the theorem, exhibit such a product and its finite-support Pauli
images satisfying all constraints. Steps D–G apply directly to that product
and force a translation; no circuit assumption was used. Ordinary even/odd
brickwork has only a sublattice translation symmetry in general, while
quasi-local Hamiltonian flows are outside the strict-locality hypothesis.
No statement that every Hamiltonian flow lacks an exceptional strictly local
time is needed. If any such time meets the hypotheses, its automorphism is
a translation. The proof, not an inability to construct a counterexample,
supplies this boundary.

### N8 — Earlier related work and unresolved scope

The directly inspected historical predecessors are C4f's monomial pair
argument and open nonmonomial sector question, and C4b's full-action
conserved-U(1) transport question. Their relevant reduction is rederived
here; neither note is imported as an authority for the theorem. The canonical
many-body tensor-algebra statement also differs from the current-main
single-particle convolution/tick notes. A targeted current-main search for
SU(2)/QCA rigidity found no earlier canonical theorem of this precise form;
this is a bounded repository check, not a novelty or exhaustive literature
claim. The sector, optimizer and synthesis portions of the original packet
remain deferred. No retired physical wall is being reinstated by this
conditional algebra statement. A new proposed counterexample reopens this
claim only by satisfying its full domain or identifying a faulty proof step.

## Reproduction and historical recovery

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/su2_equivariant_one_qubit_qca_translation_rigidity_2026_10_21.py
```

The canonical invocation writes stdout and returns nonzero if any check
fails. Optional `--log NEW_PATH` creates a new log exclusively and refuses
to overwrite an existing file. The cache is generated using the repository's
runner-cache API and binds this note, the helper and the baseline memo.
Expected finite-check total is `TOTAL: PASS=22 FAIL=0`; this count is not an
independent proof. The declared timeout is 120 seconds.

This note salvages only the original C9 proof, corollary and commuting-
translates lemma from PR #9831, original commit
`e294c1dc745dad0c95b4c8688efc6f3f0be03613`. The full original NOTE, scripts,
review reports, failures, incomplete runs and campaign synthesis remain
preserved at that revision. In particular, original sector formula and
sampled-velocity claims, optimizer convergence language and campaign action-
selection assertions are not adopted by this note. The original PR must
not be treated as accepted by this partial source repair.

The earlier independent exact check used a separate implementation of the
shared-site Pauli commutator, two-site commutant dimension, one-site vector
space, fresh-site elimination and swap trace/sign selection. That evidence
is reused for its unchanged mathematical scope; the present runner is an
author reproduction, not a new independent check. Novelty and literature
priority remain unverified. Formal retained status belongs to the
independent audit path.
