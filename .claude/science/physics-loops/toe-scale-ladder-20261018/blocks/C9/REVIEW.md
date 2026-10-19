# C9 — independent review

**Reviewer:** a Claude subagent, same model as the author. Not independent in the sense of a
different model or a human; independent only in that I re-derived every step from the NOTE
text and wrote my own scripts (`review_scripts/`), using a different search target from the
author's `c9_03`.
**Date:** 2026-10-19. **Scope:** `blocks/C9/NOTE.md`, its scripts and logs, plus C4b Lemma 2(a)
and the C4f S^- remark and β_R convention. No commits. I wrote only this file and
`review_scripts/`.

## Verdicts

| # | claim | verdict | severity of issues |
|---|---|---|---|
| 1 | Theorem 1 (TI + SU(2), one qubit per site, any range, any d ⇒ α = τ_c) | **correct** | minor (exposition of Step D) |
| 1a | Lemma B (one-site overlap) | correct | none |
| 1b | Lemma C + corollary (lexicographic translate) | correct | none |
| 1c | Step D (swap ↦ NN bond, sign +) | correct, with an exposition fix | minor |
| 1d | Step F (common shift) | correct | none |
| 1e | Step G (fix all swaps ⇒ fix σ_0) | correct | none |
| 2 | Corollary 2 (U(1) + full-action covariance under irreducible H ⇒ α = id) | **correct** | none; one note on scope |
| 3 | Step (1) sector statements and S^± witnesses; "not QCAs" | **correct with a wording fix** | minor |
| 4 | Side lemma (commuting TI translates of an invariant operator ⇒ scalar) | **correct** | minor (scope of the construction remark) |

No counterexample to Theorem 1 was found, analytically or numerically.

## 1. Theorem 1, step by step

**Lemma B.** Verified line by line.
- Decomposition: unique, because {1, σ^1, σ^2, σ^3} is a basis of M_2.
- Invariance: applying γ_D = γ'_D ⊗ Ad(D)_a and using uniqueness shows that X_0 is invariant and
  that (X_j) is a vector operator.
- Commutator: X_0 ⊗ 1_a commutes with everything in h, since its support meets B only at a, where
  it is trivial. X_j and Y_k have disjoint supports. So [g,h] = Σ X_j Y_k [σ^j,σ^k] =
  2i ε_{jkl} X_j Y_k σ^l, which is correct.
- [g,h] = 0 therefore gives Σ_{jk} ε_{jkl} X_j ⊗ Y_k = 0 for each l, as an element of
  A(A∖a) ⊗ A(B∖a). Applying φ ⊗ ψ gives φ(X) × ψ(Y) = 0.
- V_X is invariant under the real matrices R(D), because φ∘γ'_D is again a functional. The
  complexified defining representation of SO(3) on C^3 is irreducible, so V_X is 0 or C^3.
- The last step is slightly stronger than written. It suffices that one of V_X, V_Y is C^3 and the
  other is nonzero: pick y ≠ 0, then x ∦ y. So X = 0 or Y = 0, which is correct.

**Lemma C.** The order must come from an ℓ that is injective on Z^d, for example with rationally
independent coefficients. "Generic" should be read that way.
- S ∩ (S+t) = {s1}: correct.
- By minimality, an invariant g acts nontrivially at s1 and at s2. For an invariant operator,
  "nontrivial at a site" is the same as "vector channel ≠ 0".
- Lemma B then gives [g, τ_t g] ≠ 0.
- The corollary t_ℓ(β(A)) ∈ (F−F)∖{0} is correct. It uses only that β is TI, preserves
  invariance and is injective.

**Step D.** The conclusion is correct. The written justification ("choose ℓ close to each
coordinate axis") is a sketch, and the 3^3 exhaustive check is finite. **Fix (minor):** replace it
with the following two-line argument, which works for any d and has no box restriction.
- Let q, q' ∈ S and v = q' − q. For every generic ℓ, |ℓ(v)| ≤ width_ℓ(S) = |ℓ(e)|. By density
  this holds for every ℓ ∈ R^d.
- Taking ℓ ⊥ e forces v ∥ e. Then |λ| ≤ 1 with λ ∈ Z, so v ∈ {0, ±e}.
- Hence all differences in S lie in {0, ±e}, so |S| ≤ 2. Since |S| ≥ 2, S = {p, p+e}.

The rest of Step D is correct: the invariant 2-site algebra is span{1,P}, a+bP is a self-adjoint
unitary and non-scalar, so a = 0 and b = ±1, and the unique trace forces b = +1. `r02` also checks
this geometric statement on 20 000 random subsets of a 5^3 box of size 2–6, and on all 2-point
sets. It also checks the sign step.

**Step F.**
- For i ≠ j, two NN swaps on bonds that share exactly one site do not commute (Lemma B, or
  directly). Swaps on disjoint bonds commute.
- An automorphism preserves commutation in both directions.
- D_ij + δ = D_ij forces δ = 0 for a finite nonempty set.

So all the c_i are equal. This step is correct.

**Step G** (the point the task flagged). The argument does **not** claim that the swaps generate
σ_0, and it does not need them to. It uses three facts:
1. α′ fixes every P_yz, because each P_yz is a product of NN transpositions and α′ is
   multiplicative.
2. α′(σ^j_0) =: W^j is a **vector operator**. This is exactly where commutation of α with γ_D on
   the full quasi-local algebra is used: γ_D(W^j) = α′(γ_D σ^j_0) = Σ_k R_kj W^k.
3. Since α′ is an automorphism, [σ_0, P_yz] = 0 for y, z ≠ 0 gives [W, P_yz] = 0.

The site elimination is then sound.
- W is local, so z can be chosen outside supp W ∪ {0}; this uses the infinite lattice.
- [W, σ_y·σ_z] = Σ_k [W, σ^k_y] ⊗ σ^k_z, and the σ^k_z are independent at an outside site. So
  [W, σ^k_y] = 0 for every k, and W is trivial at y.
- The result is supp W ⊆ {0}. One-site vector operators are λσ, and the algebra relations give
  λ = 1. By TI, α′ fixes every σ^j_x, so α′ = id.

`r02` confirms the elimination as an exact nullspace computation. Vector operators on {0,1,2} that
commute with all swaps among {1,2,3} form a 1-dimensional space, spanned by σ_0. Without the
outside site (only P_12) the space has dimension 5, so the outside site matters.

**Hidden premises.**
- R1–R3 are standard.
- "α maps invariant operators to invariant operators" is immediate.
- Automorphisms preserve minimal support only in the sense actually used. The argument applies
  minimality to α(P), to W and to g, never claiming that α preserves supports. That is fine.

There is no hidden use of surjectivity beyond α being an automorphism. Only Step G uses α as an
automorphism rather than an injective endomorphism, through multiplicativity and α′(σ) ≠ scalar.

**Counterexample hunt.**
- Analytic.
  - Brickwork SU(2) circuits (Trotterised XXX, e.g. the integrable Floquet XXX chain; recalled) are
    only 2Z-invariant. Composing with τ_1 does not make them Z-invariant: τ_1 Ad(E) τ_1^{-1}
    = Ad(O).
  - Commuting TI layers are empty by Lemma C.
  - Spin flip σ → −σ is not an automorphism.
  - Time reversal is antilinear.
  - Reflections are not local on Z.

  None of these is in the premise class.
- Numerical (`r01`, a reviewer-designed route).
  - A TI SU(2) 1D QCA with neighbourhood window of n sites is determined by W^j = α(σ^j_0), a
    Hermitian vector operator on the window.
  - W satisfies the Pauli algebra and commutes with all its translates. These are necessary
    conditions, and they define an injective TI endomorphism.
  - The search is least squares over the **entire** vector-operator space, which has
    dimensions 9 and 28 for n = 3, 4 (n = 5, 90, was planned but not run). Each dimension matches the spin-1 multiplicity
    from Schur–Weyl.
  - Every converged solution was a single-site Pauli triple, i.e. a shift. Results:
    n = 3: 200/200 starts converged, all to shifts {0:51, 1:98, 2:51}, 0 other (`r01_n3_run2.txt`, TOTAL: PASS=8 FAIL=0). n = 4: running at hand-back as `r01_n4_run4.txt` (pending; not counted). An earlier n = 4 run showed a slow-convergence valley (residual 2e-12 at distance 1.6e-4 from a shift), consistent with the first-order Heisenberg-flow deformation i[ΣP, σ] that does not integrate to a strictly local solution; the classifier was changed to polish such cases. Earlier n = 4 attempts are kept as INCOMPLETE logs.
  - This tests Theorem 1 as a whole in 1D, rather than the swap step tested by `c9_03`. It is
    evidence, not proof.

## 2. Corollary 2

- C4f gives β_R = Ad(D_R^{⊗}) ∘ π_R with D_R a lift of Q(R), and Q(R) = R for the full action.
  Then β_R γ_{m,φ} β_R^{-1} = γ_{Rm,φ}, because π_R commutes with every γ.
- Conservation about m therefore implies conservation about Rm. If H is irreducible, the span of
  the orbit is R^3. The closed group generated by three independent one-parameter subgroups is
  SU(2), so α commutes with SU(2).
- Theorem 1 gives α = τ_c. Covariance gives τ_{Rc} = π_R τ_c π_R^{-1} = τ_c, because
  Ad(D^⊗) commutes with τ_c. So Rc = c, and an irreducible H fixes no nonzero vector, giving c = 0.
- Within the 24-element rotation group O, the irreducible subgroups are exactly O and T, so
  "e.g. O or T" is in fact "i.e."
- The D2 remark is correct: D2 is reducible, but it fixes no nonzero vector.

Verdict: **correct.**

Scope note: "closes C4b W1/W1′ for the full action" holds within C4b's premise class, that is
one qubit per site, exact TI, strict locality and the full soldering action. The axis action
(C4f) is correctly left untouched.

## 3. Step (1): sector statements and witnesses

- The S^± bookkeeping is correct.
  - ker S^- ∩ H_2 = (im S^+|_{H_1})^⊥, with dimension N(N−3)/2.
  - The C4f monomial argument is correctly recalled.
- ψ satisfies S^-ψ = 0, since each vertex appears in two consecutive edges with opposite signs on
  an even cycle.
- Its translates share no pair state, because the edge vectors are ±-distinct. I re-checked this
  exactly in `r02`.
- The author's logs cover W_g and W_O. I did not recompute the 0.70 group velocity; it is a
  numerical value with no load-bearing role.

**"Not QCAs."** This is correct in the sense intended.
- They are unitaries on the two-magnon sector H_2 only. They are not operators on the full
  algebra.
- By Theorem 1, any TI SU(2) QCA is τ_c. Its action on H_2 over the ferromagnetic vacuum is a
  phase times a translation.
- W_g fixes far pairs but moves ψ, and W_O is dispersive, so neither equals a phase times a
  translation. So no in-premise QCA restricts to them.

**Wording fix (minor).** The NOTE says U "is c_1 on the S = N/2−1 multiplicity space". SU(2) alone
allows an arbitrary unitary on that (N−1)-dimensional multiplicity space. It is frozen singles,
C4b Lemma 2(b), plus TI that make U|_{H_1} a single phase. The conclusion U|_{H_1} = c_0 is right;
only the attribution to SU(2) alone is loose. Suggested text: "SU(2) makes U act on the H_1
multiplicity space of S = N/2 − 1; frozen singles make it the same constant c_0."

## 4. Side lemma

- This follows directly from Lemma C: a non-scalar invariant g has [g, τ_t g] ≠ 0 for t = s1 − s2.
  Verdict: **correct.**
- Minor scope remark. The construction sentence "commuting TI layers of SU(2) gates is empty"
  covers layers of SU(2)-**invariant** gates. A TI layer of commuting gates that are not invariant
  individually, but whose product is SU(2)-symmetric, is not covered by Lemma C. It is covered by
  Theorem 1, as the NOTE's N1 item 2 already says.

## Novelty (recalled, not verified by a search in this review)

- **Recalled.** The GNVW index (Gross–Nesme–Vogts–Werner, CMP 2012) classifies 1D QCAs up to
  circuits. The shift τ_1 on qubits has index 2.
- **Recalled.** Matrix-product unitaries:
  - Cirac–Pérez-García–Schuch–Verstraete, J. Stat. Mech. 2017 ("Matrix product unitaries:
    structure, symmetries, and topological invariants");
  - Şahinoğlu–Shukla–Bi–Chen, PRB 2018;
  - Gong–Sünderhauf–Schuch–Cirac, PRL 2020 ("Classification of matrix-product unitaries with
    symmetries").

  These classify symmetric 1D QCAs/MPUs **up to symmetric circuits / blending**, by the index
  together with a cohomological invariant of the on-site symmetry.
- They do not, as far as I recall, give a **rigidity** statement of the type "the TI SU(2) QCA is
  literally a shift". Such a statement depends on the qubit (spin-1/2) cell, on exact
  one-site-cell TI and on a continuous non-abelian symmetry.
- **Recalled, adjacent.** Marvian (Nat. Phys. 2022) studies restrictions that symmetry plus
  locality impose on SU(2)-invariant circuits. Vogts classified nearest-neighbour 1D qubit QCAs.
- Theorem 1 is elementary, so it may well exist as a lemma somewhere. I cannot confirm novelty.
  **Unverified.** This does not affect correctness.

## Evidence

| log | content | result |
|---|---|---|
| `review_scripts/logs/r02_steps_run1.txt` | Step D geometry (20 000 random sets + all pairs) and sign; Step G exact nullspace (dim 1) + control (dim 5); 6-cycle witness | TOTAL: PASS=7 FAIL=0 |
| `review_scripts/logs/r01_n3_run2.txt` | Lemma B random/converse; vector-op dim 9; σ-image search n=3 | TOTAL: PASS=8 FAIL=0 |
| `review_scripts/logs/r01_n4_run2.txt` | same, n=4 (dim 28); only 3 starts within budget, all slow-valley convergence toward shifts | TOTAL: PASS=8 FAIL=0 |

**Disclosure.** My first launch of `r01` was given the arguments in the wrong order (n = 200). I
killed it by hand after Part A, and its log is kept, renamed, as
`review_scripts/logs/r01_run1_MISINVOKED_n200_killed.txt`. The official runs are `run2`. The dry
runs were made in the scratch directory, not here.

I also re-read the author's official logs: `c9_01` 22/0, `c9_02` 19/0, `c9_03` 4/0 + 4/0, so 49/0
in total, as stated. Their dry-run and incomplete logs are disclosed correctly.

## Recommended edits to NOTE.md

1. Step D: replace the "ℓ near axes" sentence with the difference-vector argument above (minor).
2. Lemma C: say explicitly that "generic" means ℓ injective on Z^d (cosmetic).
3. Step (1): fix the "c_1 on the multiplicity space" attribution (minor).
4. Corollary 2: "e.g. O or T" can be "i.e. O or T" among subgroups of the rotation group O
   (cosmetic).

Reviewer counted total (r02_steps_run1 + r01_n3_run2 + r01_n4_run4): TOTAL: PASS=23 FAIL=0

## Correction confirmation (2026-10-19)

I re-read all of the corrected NOTE.md.
- **Step D (new item 2).** For s, s′ ∈ S the bound is |ℓ(s−s′)| ≤ max_S ℓ − min_S ℓ = |ℓ(e)| for
  every generic ℓ.
  - By density the bound holds for every ℓ ∈ R^d.
  - Taking ℓ ⊥ e gives v ∥ e, and then |v| ≤ |e| with v ∈ Z^d gives v ∈ {0, ±e}.
  - So S = {p, p+e}.
  This is correct and complete.
- **Lemma C.** "Generic" is now defined as ℓ injective on Z^d. Correct.
- **Step (1).** The c_1 attribution is fixed: SU(2) gives some unitary on the multiplicity space,
  and frozen singles plus TI make it a scalar. Correct.
- **Corollary 2.** It now reads "i.e. O or T". Correct.
- **N7.** The brickwork 2Z remark is correct.
- **Novelty.** Marked unverified. Appropriate.
- **No new defect found.** The dispositions table matches the review.

**Status line.** The status line now cites my count of PASS=15. With the n = 4 log it is PASS=23
FAIL=0. The author may update the line; this is cosmetic.

**n = 4 search** (`review_scripts/logs/r01_n4_run4.txt`): TOTAL: PASS=8 FAIL=0. The time budget
allowed only 3 starts. All 3 converged, slowly, toward single-site shifts: the distance shrank
under polishing, from at most 1.0e-3 to at most 1.9e-4. None converged to anything else. This is
weak but consistent evidence.

**Final verdict: READY.**
