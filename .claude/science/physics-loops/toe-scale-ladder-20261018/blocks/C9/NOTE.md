# C9 — SU(2) rigidity: under the full soldering action a U(1)-conserving one-qubit QCA is the identity

**Block:** C9 of `toe-scale-ladder-20261018`, following C4b (Lemma 2: U(1) + full action ⇒
SU(2)), C4f (S^- remark: monomial SU(2) pairs are static) and C4d (spectator lemma).
**Date:** 2026-10-19. **Status:** author work only; not independently reviewed; unaudited. No
axiom, primitive or dynamics clause is adopted.

## Result up front

The target asked whether, under the full action, a U(1)-conserving (hence SU(2)-symmetric) one-qubit
O-covariant QCA can move a bound pair, a cluster, or anything at finite density once
non-permutation (entangling) dynamics is allowed. **Answer: no. The premise class contains
exactly one QCA, the identity.**

1. **Theorem 1 (proved; any range, any d ≥ 1).** Every Z^d-translation-invariant QCA on one qubit
   per site that commutes with global SU(2) is a lattice translation τ_c.
   - Covariance is not used. Frozen singles are not used. Non-permutation dynamics is not excluded
     by assumption: the theorem quantifies over **all** *-automorphisms with finite-range images.
2. **Corollary 2 (proved).** Under the full action, every TI one-qubit QCA that conserves an
   on-site U(1) charge and is covariant under some H ≤ O acting irreducibly on R^3 (e.g. O or T) is the
   **identity**. So nothing moves in any sense: no T1, T2 or T3. There are no single, pair or
   k-cluster motions, no finite-density transport, and no operator spreading. Moving bound
   pairs, the target of this block, are therefore excluded. This proves C4b's open item W1 for the
   full action and closes it negatively. W1′ is closed negatively too.
3. **Step (1) of the task (proved plus exact sector-level witnesses).** On its own, the
   2-magnon S^- argument does **not** extend beyond permutation-type maps. With singles frozen,
   SU(2) fixes U on im(S^+) ⊂ H_2 and leaves U **arbitrary** on ker S^- ∩ H_2, which has
   dimension N(N−3)/2. `c9_02` builds two exact sector-level unitaries that satisfy every S^±
   constraint:
   - a TI speed-1 pair glider built on a 6-cycle ker S^- state with orthonormal translates;
   - an O-covariant, TI pair unitary with a dispersive band. Its maximum group velocity is
     0.70 sites/tick at θ = 0.3.

   So the obstruction is **not** sector-level. It is the operator-algebra rigidity of Theorem 1,
   which couples all sectors. Neither sector unitary extends to a QCA.
4. **Side lemma (Lemma C, proved).** Any family of all Z^d translates of a local SU(2)-invariant
   qubit operator that mutually commute consists of scalars. So "commuting TI layers of
   Heisenberg/exp(iθ P_swap)-type gates" is empty as a construction strategy, even before
   Theorem 1.

**Claim types.** Theorem 1, Corollary 2, Lemmas B and C: proved, with exact or numerical finite
certificates of their ingredients in `c9_01`. Step-1 sector statements: proved, with exact
witnesses in `c9_02`. The optimisation search in `c9_03` is a sampled numerical check of the
"swap → swap" step by a different method. It is evidence, not proof.

## Premises (named)

- Lattice and Qubit axioms: Z^d, with d = 3 in the campaign, and M_2(C) per site.
- (D-QCA): α is a *-automorphism of the quasi-local algebra that maps local operators to local
  operators and commutes with all translations τ_t, t ∈ Z^d. Finite range is used only in this
  form. It is not assumed to be Clifford, permutation-type, or a circuit.
- (SU(2)): α γ_D = γ_D α for every D ∈ SU(2), where γ_D = Ad(D^{⊗Z^d}). For the full action this
  *follows* from U(1) conservation plus covariance (C4b Lemma 2(a), reproved in one line below).
- Recalled standard facts:
  - (R1) Schur–Weyl duality for qubits: the commutant of {D^{⊗n}} is the span of the
    site-permutation operators. `c9_01` A checks the dimensions 1, 2, 5, 14, 42 for n ≤ 5 against
    Catalan numbers.
  - (R2) The quasi-local (UHF) algebra has a unique tracial state, so every automorphism
    preserves it.
  - (R3) Every local operator g has a unique minimal support, the smallest finite S with
    g ∈ A(S) ⊗ 1.

## Proof of Theorem 1

Notation: σ^j_x are the Paulis, P_{xy} = (1 + σ_x·σ_y)/2 is the swap, and an "invariant" operator
is one fixed by every γ_D. Since α commutes with γ_D, α maps invariant operators to invariant
operators.

**Lemma B (one-site overlap).** Let g ∈ A(A) and h ∈ A(B) be invariant, with A ∩ B = {a}.
1. Write g = X_0 ⊗ 1_a + Σ_j X_j ⊗ σ^j_a and h = Y_0 ⊗ 1_a + Σ_k Y_k ⊗ σ^k_a. These
   decompositions are unique, with X's in A(A∖a) and Y's in A(B∖a).
2. Invariance makes X_0 invariant and (X_j) a vector operator: γ_D(X_j) = Σ_k R_{jk}(D) X_k.
3. All cross terms commute because their supports are disjoint. Hence
   **[g,h] = 2i Σ_{jkl} ε_{jkl} X_j Y_k σ^l_a**.
4. Suppose [g,h] = 0. Apply functionals φ ⊗ ψ: x × y = 0 for every x ∈ V_X := {(φ(X_j))_j} and
   y ∈ V_Y.
5. V_X and V_Y are SO(3)-invariant subspaces of C^3. Since C^3 is irreducible, each is 0 or C^3.
   If both were C^3, then x × y = 0 would fail.
6. Hence [g,h] = 0 ⟺ X = 0 or Y = 0. That is, one of g, h acts trivially on a.

`c9_01` B checks the commutator formula to 3e−15, rank V_X = 3, 20 random non-commuting pairs,
and the converse.

**Lemma C (lexicographic translate).** Let g be invariant and non-scalar, with minimal support S.
Then |S| ≥ 2, because single-site invariant operators are scalars. Fix any total order ≺ on Z^d
compatible with translations, for instance by a generic linear functional ℓ. Let s1 = max S,
s2 = min S, and t = s1 − s2 ≠ 0.
1. Then S ∩ (S+t) = {s1}. If p ∈ S and p − t ∈ S, then p ⪯ s1 and p ⪰ s2 + t = s1.
2. τ_t g has vector channel at s1 equal to the translate of g's vector channel at s2. By
   minimality both vector channels are nonzero.
3. So by Lemma B, **[g, τ_t g] ≠ 0**.

Corollary: if F is finite, A ∈ A(F) is invariant and non-scalar, and β is a TI automorphism
preserving invariance, then [β(A), τ_t β(A)] = β([A, τ_t A]). This vanishes whenever
F ∩ (F+t) = ∅. Hence **for every generic ℓ, t_ℓ(β(A)) ∈ (F − F) ∖ {0}**. Lemma C itself is also
the side lemma of Result 4: take t to be any translate in the family.

**Step D (swaps go to bonds).** Take F = {0, e} and A = P_{0e}, so F − F = {0, ±e}.
1. For every generic ℓ, the ℓ-extreme points of S := supp α(P_{0e}) differ by ±e.
2. Choosing ℓ close to each coordinate axis shows that S has a single value in every coordinate
   ⊥ e, and extent exactly 1 along e. So S = {p, p+e}.
3. `c9_01` E confirms exhaustively, in the 3^3 box with |S| ≤ 4 and 40 generic ℓ, that only the
   18 x-bonds qualify.
4. The invariant algebra of two qubits is span{1, P} (R1). So α(P_{0e}) = a + bP_{p,p+e}.
5. α(P_{0e}) is a non-scalar self-adjoint unitary with normalised trace τ(P) = 1/2 (R2). That
   forces a = 0 and b = +1.
6. So **α(P_{x,x+e}) = P_{x+c_e, x+c_e+e}**, where TI gives the x-dependence.

**Step F (one common shift).**
1. Two NN swaps fail to commute iff their bonds share exactly one site, and α preserves
   (non)commutation.
2. For the e_i-bond at 0 and the e_j-bond at y, sharing happens iff y ∈ D_ij = {0, e_i, −e_j,
   e_i − e_j}.
3. The images share iff y + c_j − c_i ∈ D_ij. So D_ij + (c_j − c_i) = D_ij, and a finite set is
   invariant under no nonzero translation. Hence c_1 = c_2 = c_3 =: c. `c9_01` F checks this.

**Step G (identity).** α′ := τ_c^{-1} ∘ α is a TI, SU(2)-symmetric automorphism fixing every NN
swap. NN transpositions generate the symmetric group of every finite box (`c9_01` G: S_8 on the
unit cube). So α′ fixes every P_{yz}.
1. Let W^j := α′(σ^j_0). For y, z ≠ 0, [σ^j_0, P_{yz}] = 0 gives [W^j, P_{yz}] = 0.
2. Suppose y ∈ supp W with y ≠ 0, and choose z ∉ supp W ∪ {0}. Then
   0 = [W, σ_y·σ_z] = Σ_k [W, σ^k_y] ⊗ σ^k_z, so [W, σ^k_y] = 0 for every k. Then W ∈ A(supp W∖y),
   which contradicts minimality.
3. So supp W ⊆ {0}. Single-qubit vector operators are λσ (`c9_01` G: nullity 1). Hermiticity,
   W² = 1 and α′(σ^1)α′(σ^2) = iα′(σ^3) give λ = 1.
4. So α′ = id and **α = τ_c**. ∎

**Corollary 2.**
1. U(1) about m plus full-action covariance gives conservation of the U(1) about Rm for every
   R ∈ H (C4b Lemma 2(a)). The span of {Rm} is a nonzero H-invariant subspace, so it is R^3 when
   H is irreducible. U(1)s about three independent axes generate SU(2), so α is SU(2)-symmetric.
   Irreducibility is needed: for the axis-π group D2 with m = e1, the orbit is ±e1 only.
2. By Theorem 1, α = τ_c.
3. Covariance gives β_R τ_c β_R^{-1} = τ_{Rc} = τ_c. So Rc = c for all R ∈ H. An irreducible H
   fixes no nonzero vector, hence c = 0. ∎
   (If SU(2) is assumed directly, as in Theorem 1, then any H fixing no nonzero vector, including
   D2, already gives α = id.)

## Step (1) in detail: what SU(2) + frozen singles force on H_2 (sector level)

On the torus, U commutes with S^±. It is c_0 on the S = N/2 multiplet and c_1 on the S = N/2−1
multiplicity space. Frozen singles give c_0 = c_1, because U|x⟩ must be local (C4b Lemma 2).
1. Since U S^+ = S^+ U, U|H_2 = c_0 on im S^+|_{H_1} (dimension N, `c9_02`: rank 64 at L = 4).
2. U preserves ker S^- ∩ H_2, of dimension N(N−1)/2 − N, and is otherwise unconstrained there.
3. The monomial S^- argument (C4f) works because S^-|x,y⟩ = |x⟩+|y⟩ pins {x,y} (`c9_02`). For a
   non-monomial U it gives nothing more.

**Witnesses (exact).**
- ψ = 6^{-1/2} Σ_i (−1)^i |v_i, v_{i+1}⟩ around the cycle 0, e1, e1+e2, (1,1,1), e3, (1,−1,0).
  Its six edge vectors are pairwise ±-distinct, so translates are orthonormal (exact on Z^3), and
  S^-ψ = 0.
- W_g = Σ_x |ψ_{x+e3}⟩⟨ψ_x| + (1 − Π_ψ) is unitary and TI. It equals 1 on im S^+ and on all pairs
  with |ρ|∞ ≥ 2, satisfies S^- W_g = S^-, and moves ψ at speed 1.
- H_O = Σ_{R∈O} Σ_x |π_Rψ_x⟩⟨π_Rψ_x| commutes with all 24 π_R and translations, and has its range
  in ker S^-. It has a dispersive 13-band Bloch structure, cross-checked against the torus
  spectrum on 832 eigenvalues. W_O = e^{0.3 i H_O} has maximum sampled group velocity 0.70.

These are **not QCAs**. Theorem 1 shows that no QCA restricts to them. The full action's
O-covariance is irrelevant at this level: π_R covariance is easy to satisfy.

## Checks

| script | content | result |
|---|---|---|
| `c9_01_lemmas.py` | Schur–Weyl dims; Lemma B formula, rank, non-commutation, converse, vector-operator covariance; Lemma C on 24 random supports; 2-qubit algebra and the a+bP step; exhaustive geometric step; commutation-pattern step; one-qubit vector operators; site elimination; S_8 generation | `logs/c9_01_lemmas_run1.txt` PASS=22 FAIL=0 |
| `c9_02_sector.py` | H_2 decomposition at L = 4; monomial step; ψ properties; W_g and W_O as above; exact Z^3 Bloch table | `logs/c9_02_sector_run1.txt` PASS=19 FAIL=0 |
| `c9_03_search.py` | least-squares search, from 100 random starts per window, over the whole invariant Hermitian algebra of a 4-site window (1D chain and 2D 2×2) for self-adjoint unitaries with τ = 1/2 commuting with every disjoint-from-{0,e1} translate; prediction: only NN e1-swaps | `logs/c9_03_search_run1.txt` (see SUMMARY) |

`logs/SUMMARY.txt` gives the combined total.

**Disclosure.**
- The dry run of `c9_01` in scratch had one FAIL, in check G. The cause was a transposed rotation
  matrix in the test's own linear system (R[j,k] where the derivation gives R[k,j]). It was fixed
  before the official run, and the dry-run log is kept as `logs/c9_01_lemmas_dryrun0_HAS_FAIL.txt`.
- A 10-start dry run of `c9_03` in scratch had two FAILs on "each expected bond is found". There
  were too few starts, about 20 % of starts converge. It found no non-swap solution.
- The theorem was derived analytically before any code was written (`WORKLOG.md`).

## No-Go Discipline Gate (N1–N8)

The negative claim is the quantified Theorem 1 and Corollary 2, proved. The gate checks scope.

- **N1, routes to a moving pair, and why each fails.**
  1. Commuting TI layers of SU(2) gates: Lemma C. ATTEMPTED.
  2. Non-commuting circuits, or a rule-based reversible design with a TI composite: covered,
     because Theorem 1 quantifies over all automorphisms. ATTEMPTED.
  3. Sector-level ker S^- motion: exists (`c9_02`) but cannot extend (Thm 1). ATTEMPTED.
  4. Permutation/monomial type: RULED OUT BY PRIOR (C4f S^- remark), and subsumed.
  5. Sublattice-TI (Margolus, Trotter brickwork): out of premise. C4b exhibits SU(2) Margolus blocks
     that move singles. RULED OUT BY PRIOR as premise-violating.
  6. Axis action, where only Q_n is conserved: out of this premise. C4f's positive glider stands.
  7. Quasi-local evolutions e^{iH} with Heisenberg-type H: not finite-range QCAs, so out of premise
     and **not covered**.
- **N2, walls.** None remain inside the premise. The scope boundaries are:
  - (a) full Z^d TI;
  - (b) one qubit per site;
  - (c) exact SU(2) symmetry;
  - (d) strict locality.

  (a) and (b) are not independent: a sublattice-TI qubit model is a TI model with a larger cell.
  C4b's Margolus model is a witness that relaxing them admits motion. For (c), C4f is a witness that
  U(1) alone admits motion. For (d) the status is unresolved.
- **N3, hidden premises promoted.** R1–R3; that α maps invariant operators to invariant
  operators (immediate from commuting with γ_D); C4b Lemma 2(a) for the full action.
- **N4, residual matching.** Theorem 1 is stated for exactly the premise class of the target. The
  C4f remark is cited only for its monomial residual.
- **N5, resolutions.** Operator-algebra level (all sectors at once) in Theorem 1; sector level in
  `c9_02`.
- **N6, partial closures.** These are only by premise change: a spin-1 or multi-qubit cell
  (open), a sublattice (Margolus, known to move), the axis action (C4f), and quasi-local
  generators (open).
- **N7, steelman.** "Heisenberg ferromagnets have mobile two-magnon bound states, and SU(2)
  Trotter circuits move magnons." Both are true and both are out of premise. The Hamiltonian
  is not a finite-range QCA, and its single magnons also move. Brickwork circuits are 2Z^d-TI
  only. Theorem 1 says the exact-TI qubit setting is rigid, and no claim is made beyond it.
- **N8, cross-cycle echo.** This extends and supersedes C4f's "non-monomial SU(2) pair motion is
  open" and C4b's W1 for the full action. The axis-action positive result (C4f) is unaffected.

**Gate status: PASS for the scoped claims.**

## Not covered

- More than one qubit per site, for example spin-1. There the 2-site invariant algebra has
  dimension 3, and Step D fails as written.
- Quasi-local (LGA) dynamics.
- Approximate symmetry.
- Sublattice TI.
- The axis action beyond C4f.
- Any physical identification.

**Novelty:** no literature search was done. The statement is elementary, and may be known for
symmetric QCAs or matrix-product unitaries. Novelty does not bear on correctness.

## Load-bearing steps for independent check

1. **Lemma B**: [g,h] = 0 for a one-site overlap forces a trivial vector channel. The key input is
   that C^3 is irreducible for SO(3).
2. **Step D**: the lexicographic/extremal argument gives supp α(P_{0e}) = {p, p+e}, and the trace
   gives the sign +.
3. **Step G**: the site-elimination argument that α′ fixing all swaps gives α′(σ_0) = σ_0.

A blind route is to attempt a counterexample: a 1D TI SU(2) qubit QCA other than a shift.

## Reproduction

```bash
cd blocks/C9/scripts      # OMP_NUM_THREADS=1 nice -n 10
python3 c9_01_lemmas.py ../logs/c9_01_lemmas_runN.txt     # ~3 s
python3 c9_02_sector.py ../logs/c9_02_sector_runN.txt     # ~35 s
python3 c9_03_search.py ../logs/c9_03_search_runN.txt 100 # ~15 min
```
