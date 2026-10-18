# C4b — Independent review

**Reviewer:** Claude Opus 5.5 (model id `claude-opus-5-5`). This was a fresh-context subagent
launched by the orchestrating session. It is the same model family as the author, so it is not
independent in the human sense. It read the NOTE, the WORKLOG, the author's logs and the C4 NOTE.
It wrote all code itself and did not import or copy the author's scripts. It looked at the
author's `c4b_02` only to find out what "9 Pauli components" referred to.
**Date:** 2026-10-18. Single core, nice 10.
**Evidence:** `review_scripts/rv_SUMMARY.log` → **TOTAL: PASS=83 FAIL=0**.

| script | content | result |
|---|---|---|
| `rv1_e1_pauli.py` | E1 by explicit Pauli conjugation on Z^3 with Z4 phases | PASS=28 FAIL=0 |
| `rv2_gnvw_reflection.py` | GNVW index from the support-algebra definition; (I7) | PASS=21 FAIL=0 |
| `rv3_group_lemmas.py` | exact group steps of Lemmas 1–5; Margolus stabiliser | PASS=30 FAIL=0 |
| `rv4_diag_exhibit.py` | Lemma 4(c) exhibit and the freeze form | PASS=4 FAIL=0 |

The first run of rv4 had one FAIL. It was a bug in my own test: I compared against an
elementwise complex conjugate, where the right comparison is e^{+2iφf}. I fixed the test and
reran it, and the log is the corrected run. The physics claim was unchanged.

## Verdict table

| # | claim | verdict | severity |
|---|---|---|---|
| 1 | E1: α_Cα_K is an O-covariant Clifford QCA with phases (axis and full), range 4, τ = O-orbit sum of (4,2,0), radius 4n | **correct** | — |
| 1' | "No localized excitation moves", attributed to C4 Thm 2(d) | **correct with fix** | minor |
| 2 | Lemma 1, including (I7) and the f = Rf argument | **correct** (conditional on the recalled facts listed below) | — |
| 3a | Lemma 2(a), (b), including the vacuum-stabiliser step for the axis action | **correct** | — |
| 3b | Lemma 3: frozen far pairs, invariance of S_near, d_1 = 13 | **correct**; the covariance group is **wrong as stated for the axis action** | minor |
| 3c | "U(1) transport reduces exactly to the pair walk" (Result 4, Bottom line, Answer 3, N2) | **incorrect as stated → fix** | moderate |
| 3d | Lemma 4(a)–(c) | **correct** (the exhibit's description needs a cosmetic fix) | cosmetic |
| 4a | Margolus symmetry relaxation to 2Z^3 ⋊ O_c | **correct**, and correctly described | — |
| 4b | Margolus dynamics (c4b_04/06/07 numerics) | inversion-block velocity 2 pen-checked; Lemma 5's combinatorial step verified; the remaining numerics **unverified** (author evidence only) | — |
| 4c | Scope of the no-go (no universal T3 no-go claimed) | **correct**, subject to the fixes in 1' and 3c | — |
| — | non-Clifford family α(θ1,θ2) is covariant for all θ | **correct**; it follows from β_R(C_r) = +C_{Rr}, β_R(K_r) = +K_r and commuting translates (rv1) | — |

## (1) E1 — correct

Implementation (rv1). A Pauli is i^k ∏ X^x Z^z. The layer is computed from the identity
e^{iπ/4 P} Q e^{-iπ/4 P} = iPQ for anticommuting P, Q. All translates of the string commute, so
α_P(Q) = ∏_{r∈A(Q)} (iP_r) Q. The soldering follows C4: σ_a at r ↦ Σ_b Q(R)_{ba} σ_b at Rr, with
full Q = R and axis Q = s(R)|R|. Results:

- **Strings.**
  - C_0 and K_0 are Hermitian involutions.
  - All translates within [-4,4]^3 commute.
  - β_R(P_0) = +P_0 for all 24 R, for both strings and both actions.
  - C_0 anticommutes with exactly 24 translates of K.
- **Single layers.** Each has radius 2 and α^2 = id with phases. This reproduces C4 [1] and [2].
- **Composite.**
  - The images of X_0 and Z_0 are Hermitian and anticommute.
  - All translates in [-8,8]^3 \ 0 commute, so commutation is preserved.
  - α^{-1}α = αα^{-1} = id, with phases.
  - Range 4, and the inverse also has range 4.
  - |supp α(X_0)| = |supp α(Z_0)| = 145.
- **Covariance with phases.** It holds for all 24 R, for both actions, and in both orders C·K and
  K·C. α_C and α_K do not commute.
- **Trace.** τ = X-part of α(X_0) + Z-part of α(Z_0). It is exactly the 24-point O-orbit of
  (4,2,0), and every exponent is even.
- **Iterates, n = 1..8.**
  - tr M^n computed from the iterates equals the Dickson recursion D_n(τ). This is an internal
    consistency check of Cayley–Hamilton.
  - All 24 vertex monomials n·v occur.
  - The Chebyshev radius is exactly 4n for both X_0 and Z_0.
  - |supp α^n(X_0)| = 145, 633, 2449, 4369, 5921, 12841, 25089, 33697, which matches the author.

Radius 4n holds at every n, not only for n ≤ 8. The upper bound comes from range 4. The lower
bound is Theorem 2(c), since the vertex (4,2,0) has Chebyshev norm 4. "Permutohedron" is correct:
the convex hull of the signed permutations of (4,2,0) is twice the standard truncated octahedron.

**1' — fix (minor).** C4 Theorem 2(d) concerns operators: a finite Pauli operator, and by a
permutation argument any local operator, that returns to a translate of itself. It does **not**
cover excitations above an α-invariant state when the two differ by a stabilizer of that state,
that is, α^n(A)ω = T_t(A)ω with α^n(A) ≠ T_t(A). Replace "No localized excitation moves" with
"no local operator glider exists (C4 Thm 2(d)); motion of excitations relative to an invariant
state is not addressed". Make the same change in N1 row (v): "T3 at the Clifford point excluded".
For E1 no invariant state has been identified anyway, because the C and K code spaces are
incompatible.

## (2) Lemma 1 — correct

**(I7) from the definition (proved here).** GNVW, as recalled, works with a nearest-neighbour
(after blocking) QCA and the pair algebra A = A_{2x}⊗A_{2x+1}. It defines
α(A) = R_L ⊗ R_R, where R_L and R_R are the support algebras on (2x-1, 2x) and (2x+1, 2x+2), and
sets ind α = √(dim R_R)/d.

1. Since α(A) ≅ A, dim R_L · dim R_R = d^4.
2. A cell-wise reflection P exchanges the two sides. So ind(PαP^{-1}) = √(dim R_L)/d.
3. By step 1 this equals d/√(dim R_R) = 1/ind α.

This uses GNVW's independence of the cut and of the pairing parity, because P maps an
(even, odd) pair to an (odd, even) pair. rv2 computes the support algebras directly from slices
and algebra closure on a 10-qubit ring with 2-qubit cells. That is a different route from the
author's RWW mutual-information check. Results:

- ind = 1, 2, 1/2, 1, 2, 1/2, 4 for the identity, the right shift, the left shift, a random
  brickwork, shift∘brickwork, left-shift∘brickwork and shift²;
- dim R_L · dim R_R = 256 = d^4 in every case;
- ind(PαP^{-1}) · ind(α) = 1 in every case.

**f = Rf.**
- If Re_i = s e_j, then R maps the e_i-transverse lattice LZ^2 onto the e_j-transverse one
  (rv3). So π_R α π_R^{-1}, compactified along e_j, is a cell-wise relabelling of α
  compactified along e_i, composed with the reflection x → −x when s = −1.
- The on-site layer Ad(u^{⊗}) has index 1, and the index is multiplicative in an abelian group,
  so conjugating by it leaves the index unchanged.
- Hence f_j = s f_i, which is f = Rf.
- O, T, D4, D3 and D2 are all groups with zero fixed space (rv3, exact). So f = 0 for every L.

**Recalled, not re-derived (by me either):**
- the GNVW definition and the factorisation α(A) = R_L⊗R_R;
- cut and pairing independence;
- multiplicativity (I2);
- shift index = d (I4; reproduced numerically);
- ind = 1 ⇔ block-partitioned two-layer circuit (I5);
- invariance under cell-wise isomorphisms (I6);
- the inverse of a QCA is a QCA of finite range (Arrighi–Nesme–Werner);
- strip compactification is a well-defined QCA for L large compared with the range.

The author's L > 4·max(r, r') is sufficient. The scope remarks are accurate: index 1 excludes
only T1, and it does not make the 3D QCA a circuit.

## (3) Lemmas 2–4

**Lemma 2(a): correct.**
- Full action: Q(O) acts on R^3 as the irreducible representation T1, so every orbit spans R^3.
- Axis action: Q(O) ≅ D3 acts as (sign rep on n) ⊕ E. The orbit of m spans 1 dimension only for
  m = ±n. It spans 2 dimensions for m ⊥ n, which is already enough to give SU(2) (rv3).
- Cosmetic: "axis forces m = ±n" should read "forces m = ±n or global SU(2)", which is
  equivalent up to the choice of m.

**Lemma 2(b): correct.** I re-derived each step.
1. Ad U_L commutes with the U(1). Hence U Q U† = Q + c, and c = 0 by the spectrum.
2. The polarised vacuum is the unique minimiser, so it is an eigenvector.
3. The one-particle amplitudes ⟨y|α(σ^+_x)|Ω⟩ depend only on y − x, vanish for |y − x|_∞ > r and
   are L-independent once the vacuum phase is stripped.
4. |u| = 1 on a dense set gives uū = 1 in C[z^±], so u is a monomial.
5. Step 5 uses U V_R = ω V_R U with V_R|k⟩ = c_R|Rk⟩. This gives u(Rk) = ω' u(k); evaluating at
   k = 0 gives ω' = 1, and then Rt₀ = t₀. The note skips the k = 0 detail, which is harmless.

**Vacuum-stabiliser step, axis action (checked exactly, rv3).**
- Q(R)n = s(R)n. So H_n = {R : Q(R)n = n} = T exactly, of order 12.
- Odd R send the vacuum (all spins along −n) to the fully polarised opposite state.
- For R ∈ T, Q(R) is a rotation about n. Explicit SU(2) lifts satisfy
  D σ^+_n D† = e^{iψ_R} σ^+_n, with the same unitary at every site, so c_R does not depend on x.
- T fixes no nonzero vector, so t₀ = 0.
- Sign action: the kernel T acts trivially on-site.
- Full action: with SU(2) symmetry, β_R composed with D(Q(R))^{-⊗} is a pure permutation
  symmetry, so H_m = O.

**Lemma 3: correct, with one fix (minor).**
- Far pairs (|x − y|_∞ > r) acquire the uniform phase e^{2iφ}. Only y ∉ supp α(σ^+_x) is needed.
- S_near is invariant, as the orthogonal complement of the frozen pairs inside the conserved
  two-particle sector.
- The count of unordered relative positions is d_r = ((2r+1)^3 − 1)/2, so d_1 = 13 = 3 faces +
  4 corners + 6 edges, and d_2 = 62 (rv3).
- **Fix.** The pair walk W(K) is covariant only under the vacuum stabiliser H_m. That is O for
  the full action or any SU(2)-symmetric α. For the axis action with only Q_n conserved it is
  **T**, because odd R map the 2-particle sector over Ω to the (N−2)-particle sector over the
  anti-vacuum. "O-covariant d_r-coin walk" should read "H_m-covariant (T for axis, O for
  full/SU(2))". The orbit structure 3 + 4 + 6 is the same under T, so the count is unaffected.

**3c — fix (moderate).** Lemma 3 reduces the **two-particle** sector, not U(1) charge transport.
- A flat W does not exclude mobile bound clusters of k ≥ 3 particles. The same cluster argument
  gives (frozen) ⊕ (finite-coin cluster walks) in each k-sector.
- The author's own Margolus survey shows the pattern "pairs confined, larger clusters not
  closed".
- Charge motion at finite density, or above other vacua, is not reduced either.

So the following overstate what is shown:
- "in-premise transport of a U(1) charge reduces exactly to one question";
- "the open part is pinned to Lemma 3's pair walk";
- "...or prove that none exists" (Answer 3);
- W1 in N2.

A nonflat W is **sufficient** for T3 but not **necessary**. Restate the open set as
{nonflat k-cluster walk for some k ≥ 2} ∪ {finite-density / other-vacuum transport} ∪ W2.

**Lemma 4: correct.**
- Commutant dimensions 2 (axis), 1 (full), 5 (sign) and 9 (trivial). For the axis action the
  SO(3) elements of span{P_n, P_E} are exactly {1, π-rotation about n} (rv3).
- (b): if σ_m is fixed, covariance forces σ_{Q(R)m} to be fixed, and these span R^3, so α = id.
- (c): fixing σ_n gives α(σ^+_0) = σ^+_0 f with f n-diagonal, and since α fixes f,
  α^k(σ^+_0) = σ^+_0 f^k. This is confirmed on the exhibit (rv4): f = e^{2iφΣ_e σ_n(e)}, and the
  same form holds at k = 2.
- Cosmetic: the full α(X_0) of the exhibit is supported on the whole 7-site star and has 10272
  Pauli components. The note's "9 Pauli components on {0, e_x}" is a restricted count and should
  say so.

## (4) Margolus and scope

- **Symmetry: correct.** Exact enumeration with half-integer centres (rv3) shows:
  - for each R exactly one class t ≡ c − Rc (mod 2) preserves P0, and then automatically P1;
  - the t = 0 survivors are the C3 about (1,1,1);
  - the only pure translations that survive are 2Z^3, of index 8;
  - (1,1,1) swaps the two partitions, giving the half-step glide.

  O_c ⊂ Z^3 ⋊ O, because c − Rc is integral. So the relaxation "Z^3 ⋊ O_site → 2Z^3 ⋊ O_c, plus a
  glide" is described correctly, and Margolus is rightly placed outside (D-QCA).
- **Lemma 5's combinatorial step is verified:** distinct sites of a P0 cube lie in distinct P1
  cubes.
- **Inversion block, pen check.** Each coordinate moves by ±2 per two-step, giving rigid motion
  along the body diagonals with reach 2√3, which matches the log.
- **Unverified (author evidence only):** the magnon bands for the generic block, and the sampled
  k = 3 and k = 4 cluster results.
- **No-go scope.** The note correctly claims no universal T3 no-go and lists the open families.
  With fixes 1' and 3c applied, the scoped statements are accurate.

## Required edits for the author

1. (moderate) Restate the U(1) reduction (3c) so that the k ≥ 3 cluster sectors and the
   finite-density case remain open, and say that a nonflat W is sufficient, not necessary.
2. (minor) Lemma 3 covariance group: H_m, which is T for the axis action and O for full/SU(2).
3. (minor) Restrict "no localized excitation moves" (E1, N1(v)) to local-operator gliders.
4. (cosmetic) Lemma 2(a) wording "m = ±n or SU(2)"; describe the Lemma 4(c) exhibit's component
   count as restricted.

## Correction confirmation

I read the complete corrected NOTE.md, including its "Review dispositions" section.

- **3c (moderate): resolved.** The reduction is now limited to the two-particle sector, and a
  nonflat pair walk is stated as sufficient, not necessary. The k ≥ 3 clusters and the
  finite-density / other-vacuum cases are open. These edits appear in Result 4, the Bottom line,
  Lemma 3 "Scope of the reduction", Answer 3 ("proving none exists would not close") and N2
  (W1 is now k ≥ 2, and W1' is added).
- **1' (minor): resolved.** Result 1 and N1(v) now say "no local-operator glider", and they state
  that excitations above an invariant state are not addressed. W2 in N2 includes them.
- **3b (minor): resolved.** Lemma 3 and Result 4 now say H_m-covariant: T for the axis action and
  O for full/SU(2). The anti-vacuum reason is given, and the 3+4+6 orbit structure is noted under T.
- **Cosmetic: resolved.**
  - Lemma 2(a) and Result 4 now read "m = ±n or global SU(2)".
  - The Lemma 4(c) component count is marked as restricted, and the full count (10272) is
    attributed to the reviewer.
  - Result 1 now states radius 4n for all n, and validity in both layer orders.
- **New defects:** none of substance.
  - One cosmetic leftover remains. The intro sentence "cut the open part down to one precise
    sub-question" no longer matches the corrected multi-part open set in N2. Suggested wording:
    "a short list of precise sub-questions".
  - N7 still opens with "the only obstruction to pair transport is constructing one U(1) QCA".
    It is in quotes and marked as a steelman, and it concerns pairs only, so it is acceptable.
- The Review dispositions section reports the evidence accurately: PASS=83 FAIL=0, and the
  unverified items are listed as author evidence.

**Final verdict: READY.** One optional cosmetic edit remains: the intro sentence above.
