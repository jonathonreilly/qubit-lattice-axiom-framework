# C5b REVIEW: independent mathematical review of NOTE.md

**Reviewer:** reviewed in a separate agent context, same model as the author, run as a subagent of the loop's orchestrating session. This is the same model
family as the worker, so it is **not** an independent human or cross-model audit. Date 2026-10-18/19.
I read NOTE.md, WORKLOG.md, `scripts/s3_sheet_witness.py`, the `weyl_chirality` routine in `scripts/lib5b.py`, all the logs, and,
for context, C5 NOTE (Theorem K) and C5 REVIEW.
All reviewer code is in `review_scripts/` (`rlib.py`, `r1–r3`). It imports nothing from `lib5b.py` or `walks5b.py`, and it builds every map from
scratch. Runs used nice 10 on one core, and each took under 10 minutes.
Evidence: `review_scripts/logs/ALL_TOTALS.log` reports **TOTAL: PASS=46 FAIL=0** (r1: 15, r2: 18, r3: 13).

## Verdict table

| Claim | Verdict | Severity | Fix |
|---|---|---|---|
| **L** (localization identity W3 = −Σ_boxes Ch(P_<)) | **correct** | none | I verified the proof line by line and gave a second proof by a different route (§1.2) |
| S(a) (Weyl node: Ch(P_<) = χ = sign det v, contributes −χ) | **correct** | — | — |
| S(c) / "general identity" W3 = −Σχ + ΣΦ | **correct with fix** | low | a tube around a large sheet need not admit a cut φ, so derive it from the cluster version of L in §1.3, not from the box version |
| **NN** headline formula `Σχ_p + Σ_S Φ_S = 0` (results table) | **correct with fix** | **medium (sign error in the headline statement)** | it should read `Σχ_p − Σ_S Φ_S = 0`, i.e. Σχ = ΣΦ, as in §3 of the note. The clean-level corollary Σχ = 0 is unaffected |
| NN clean-level corollary (chiralities at a clean level sum to 0) | **correct** | low (wording) | a clean level can also contain isolated non-degenerate band extrema (charge 0), so not every point is a "band touching" |
| NN′ (continuous Bloch Hamiltonians) | **correct with fix** | low | ask for H(k,t) piecewise continuous in t and C¹ in k (L needs U to be C¹, and χ needs ∂U), or say that L is applied to a smoothing |
| **D** (clean level ⇒ det U null-homotopic ⇒ constant at finite range) | **correct** | — | — (proof in §2.2) |
| Win (window corollary) | **incorrect as stated (proof gap)** | medium for Win, which is not load-bearing for NN | add the hypothesis "in each ball the in-window spectrum belongs to a single adjacent band pair (j, j+1), with j below and j+1 above the window on ∂B" (§2.3) |
| Ans (no "+1 at 0, −1 at π" at finite range, any n) | **correct** | — | — |
| **Wit** T2, T3 witness | **correct with fix** | low | ΣΦ_sheets = **−4**, not "+4" (+4 is the sum of the sheet tubes' Ch(P_<)). Type-I parameters are 0.500 at all 4 nodes, not 0.67/0.99/0.50/0.65, because s3 uses the basis-dependent \|v^{-T}t\| instead of \|v^{-1}t\| |
| Novelty / literature (§6) | correct as hedged ("likely nil") | — | §4 below |

## 1. Theorem L

### 1.1 Line-by-line check of the author's proof (§2, steps 1–6)

- **Step 1.** `∂(M×I) = ∂M×I − M×{1} + M×{0}`, so `0 = ∫_{∂M×I} ω(G) − ∫_M ω(U)`, which gives `∫_M ω(U) = ∫_{∂M×I}ω(G) = −Σ∫_{∂B_i×I} ω(G)`. Correct.
  G is smooth on M×I, because e^{−iε} ∉ spec U on M and holomorphic functional calculus applies.
- **Step 2.** H_reg has spectrum in (φ−2π, φ). On ∂B (off F_ε) the eigenvalues in (φ−2π, ε) move by +2π into (φ, ε+2π) ⊂ (ε, ε+2π), and the
  rest already lie in (ε, φ). So `H_ε = H_reg + 2πP_<`, where the terms are functions of the same normal operator and therefore commute, and
  `G = exp(−itH_reg)·exp(−2πitP_<)`. Correct. r1 checks this to 1e-10 on 50 random U(3) and 150 values of t.
- **Step 3 (PW).** With a = g⁻¹dg and b = dh h⁻¹, `tr θ³ = tr a³ + tr b³ + 3tr(a²b) + 3tr(ab²)`, and `d tr(a∧b) = −tr(a²b) − tr(ab²)`. So the
  cross term is `−3 d tr(g⁻¹dg∧dh h⁻¹)`; the note writes +3, but the sign does not matter. It integrates to ∂(∂B×I) = ∂B×{1} − ∂B×{0}. h ≡ 1 on both slices, so the pullback of dh vanishes
  there, and the term is zero. Correct.
- **Step 4.** g = exp(−itH_reg) is smooth on B×I, with g(0) = 1 and g(1) = U. The same orientation bookkeeping as step 1 gives `∫_{∂B×I}ω(g) = ∫_B ω(U)`. Correct.
- **Step 5 (Lemma T).** I re-derived it: `h⁻¹dh = −2πiP dt + (z−1)dP + |1−z|²PdP`. The relation PdPP = 0 gives `tr(P B∧B) = (z−1)²z̄ tr(PdPdP) = −|1−z|² tr(PdPdP)`,
  so `tr θ³ = 6πi|1−z|² dt∧tr(PdPdP)`. With orientation (Σ, t) and ∫|1−z|²dt = 2, `(1/24π²)∫ = (i/2π)∫_Σ tr(PdPdP) = Ch(P)`. The
  orientation (Σ, t) is exactly the product orientation of ∂B×I in step 1. Correct. r1 checks this by my own 3D quadrature on 4 random Weyl families
  (rank 1, n = 2) and on 2 families in C³ (ranks 1 and 2), with agreement to ≤ 2e-4.
- **Step 6.** The algebra is correct, and `tr θ³ = Σε_abc tr(A_aA_bA_c) d³k`, so W3 = −Σ Ch.

### 1.2 Second proof by a different route (de Rham/universality, no Lemma T)

Let Ω_α = {g ∈ U(n): e^{−iα} ∉ spec g}. The map g ↦ H_α(g) is a diffeomorphism onto the convex set of Hermitian matrices with spectrum in (α, α+2π),
so Ω_α is contractible, and ω = dβ_α on Ω_α, where β_α is the homotopy (transgression) form of the contraction g_t = exp(−itH_α). Then:

1. Since U(M) ⊂ Ω_ε, `∫_{T³}U*ω = Σ_i [∫_{B_i}U*ω − ∫_{∂B_i}U*β_ε]`.
2. Since U(B_i) ⊂ Ω_φ, `∫_{B_i}U*ω = ∫_{∂B_i}U*β_φ`. So `24π²W3 = Σ_i ∫_{∂B_i}U*(β_φ − β_ε)`.
3. On Ω_φ∩Ω_ε, the form β_φ − β_ε is closed. That set deformation-retracts onto ⊔_m Gr_m(Cⁿ), via the spectral projector onto the arc (φ−2π, ε),
   and H²(Gr_m(Cⁿ); R) = R·c₁. So `β_φ − β_ε = λ_{m,n}·tr(PdPdP) + exact`, with a universal constant λ.
4. λ does not depend on (m, n). The forms are built from traces and are therefore additive under block-diagonal sums. A constant block has
   g⁻¹dg = 0, so stabilization changes nothing, and c₁ is additive under direct sums of line bundles (splitting principle).
5. **Calibration.** The hedgehog U = exp(iψ(r)k̂·σ) with ψ: 0 → π has degree +1 analytically. Near the identity, (1/24π²)tr(g⁻¹dg)³ = (1/2π²)d³x
   with x = ψk̂, so the local orientation is +. Its single level-0 node has v = −ψ′(0)·1, so χ = −1 and Ch(P_<) = −1. This forces
   `W3 = −Σ Ch(P_<|∂B_i)`. ∎

This proof uses only contractibility, the cohomology of Grassmannians and one example. It matches Theorem L, sign included.

### 1.3 Scope remark on the sheet form (low)

Lemma S(c) obtains the sheet term from L by putting a tube N around a sheet. A large sheet's tube need not admit any quasienergy φ absent on all of N,
because the other bands can sweep the whole circle along S. The proof of L does not actually need φ. It needs only a smooth H_reg on B with
`exp(−iH_reg) = U` and `H_ε − H_reg = 2πP′` on ∂B. On N, take H_reg = H_ε on the bands that stay away from e^{−iε}, and the continuous branch
E_j ∈ (ε−δ, ε+δ) on band j, which is spectrally isolated on a thin tube. Then P′ = L_j on the side where E_j < ε, and Φ_S follows exactly as stated.
Fix: state L in this "cluster" form, or add this sentence.

### 1.4 Numerical sign checks on explicit maps (r2, own code, W3 from the bulk integral)

| map | bulk W3 | level | content | result |
|---|---|---|---|---|
| hedgehog, n = 2, smooth, infinite range | +1.000000 (N = 64, 80) | 0 | node χ = −1, box Ch = −1 | W3 = −χ = −Ch ✓ |
| | | ±π/2 | one spherical sheet; Φ computed directly (band Ch, oriented by ∇E) = +1; box Ch = −1 | W3 = +Φ = −Ch ✓ |
| V_2 (C5) | −1.00000000 | 0 / π | 7 nodes Σχ = +1 / 1 node χ = +1; box Ch = χ each | ✓ |
| V_0 | +2.00000000 | 0 / π | 4 nodes Σχ = −2 / 4 nodes Σχ = −2 | ✓ |
| plane model (1−P_QWZ) + e^{−ik_z}P_QWZ | −1.00000000 | π | one plane sheet with ∇E = +ẑ, Φ = Ch(P_QWZ) = −1; slab box (T²×I) Ch = +1 with rank {1,2} | W3 = +Φ = −Ch ✓ |
| coupled n = 3: e^{−iK(k)}(hedgehog ⊕ e^{i}) | +1.000000 | 0 | node moves to quasienergy +0.008, so level 0 is a pocket; rank-2 P_< box Ch = −1 = χ | ✓ |

Together these fix the sign of every term in the identity `W3 = −Σ_nodes χ + Σ_sheets Φ`. The node term comes from the hedgehog, V_2 and V_0. The sheet term,
with Φ oriented by ∇E, comes from the hedgehog at ±π/2 and the plane model. My FHS orientation was calibrated against direct quadrature of
(i/2π)∫tr(PdPdP) (r1).

## 2. Corollaries

### 2.1 NN: sign error in the headline formula (medium)

From the general identity and K: `0 = −Σχ + ΣΦ`, so **Σχ = ΣΦ**. Note §3 writes this correctly. The results table and the task phrasing
("chiralities plus sheet fluxes sum to zero", `Σχ_p + Σ_S Φ_S = 0`) have the wrong sign. The witness shows the difference: Σχ = −4, so
ΣΦ = −4. The table's version would require +4. Fix: replace the table entry with `Σ_{nodes} χ_p = Σ_{sheets} Φ_S`, or define Φ with the opposite (−∇E) orientation.
The clean-level statement Σχ = 0 at every clean ε, for every n, is correct. It follows from K and L. Wording: a clean level may also contain isolated non-degenerate
extrema of a single band. The function E_j − ε has constant sign on a punctured ball, so such a point contributes Ch = 0. The note's sentence "every
point of F_ε is an isolated band touching" should allow for these points. Multi-fold touchings contribute their total charge, as S(b) says.

### 2.2 D: "a clean level forces det U constant" is **true**

Proof. On T³∖F_ε, the function `det U = exp(−i tr H_ε)`, and tr H_ε is a continuous real function, because holomorphic functional calculus applies on the whole complement
and eigenvalue crossings away from e^{−iε} do no harm. So det U has a continuous real logarithm on T³∖F_ε. Since F is finite and dim = 3, every loop in T³ can be pushed
off F, and π₁(T³∖F) → π₁(T³) is onto. So the class [det U] ∈ H¹(T³; Z) = [T³, U(1)] vanishes, i.e. det U is null-homotopic. At finite range, U⁻¹ = U† is also
Laurent, so det U is a unit of C[Z³], i.e. c·z^m, with winding m. Hence m = 0 and det U = c is constant. ∎
Remarks: (i) the argument needs only F_ε to miss a set of loops generating H₁, so codimension ≥ 2 suffices if F avoids those loops. (ii) The converse fails, as T3
shows (det constant to 1.2e-15, and level 0 has sheets; r3). (iii) D is not needed for NN, because W3 is insensitive to scalar phases (C5 Prop. A).

### 2.3 Win: proof gap and a counter-configuration (medium for Win)

The step "Σ_i Ch_i = Σ_{all Weyl nodes in the window} χ" fails when one band takes part in two in-window nodes in the same ball. Take bands 1 < 2 < 3 in a ball B.
Node a (bands 1–2) and node b (bands 2–3) both lie in the window, and on ∂B band 2 is below the window. Then P_<|∂B = P₁ + P₂, which extends smoothly over
B∖{b}, so Ch(P_<|∂B) = χ_b, while the node sum is χ_a + χ_b. Directly: Ch(P₁) = χ_a and Ch(P₂) = χ_b − χ_a. Nothing in the hypotheses ("the window meets the
spectrum only inside balls, each holding Weyl cones") excludes this configuration. The 1–2 node can be compensated by a 1–2 node outside the window, so the
stated conclusion is unproved in general. Fix: require that in each ball the in-window spectrum come from one adjacent pair (j, j+1), with band j entirely below and j+1 entirely above the window on ∂B. Then
Ch_i = Σ_{nodes in B_i} χ, and the corollary holds. This does not touch NN, D, Ans or the witness.

### 2.4 Ans and NN′

Ans: "+1 at 0, −1 at π, nothing else at either level" means two clean levels with Σχ ≠ 0, which needs W3 ≠ 0 and is excluded by K. Correct for every n. NN′: for U = T exp(−i∫H(k,t)dt),
the partial evolution is a homotopy to 1, so W3 = 0 (C5 Corollary H), and NN′ follows from L. L and χ need U to be C¹ in k. With H only continuous, apply L to a C¹ approximation, which keeps the
box Chern numbers because the gaps on ∂B are open, or else state the C¹ hypothesis.

## 3. Witness T2 = e^{ik_x}Q_211 and T3 (r3, own construction)

- T2 is a unitary Laurent walk with support |m_x| ≤ 3, |m_y|, |m_z| ≤ 1 (8 hops). W3 = 0 on grids N = 20 and 23 (|sum| ≤ 8e-11). This also follows analytically from C5 Prop. A,
  since it is a scalar times a shift–coin product.
- **Complete analytic node inventory.** Writing S_a(q) = exp(iqσ_a), the condition Q = ±1 forces either (A) sin 2k_x = sin k_y = sin k_z = 0, or (B) cos 2k_x = cos k_y = cos k_z = 0:
  32 points, confirmed by 800 numeric minimizations with 0 extra points. T2 eigenvalue 1 with degeneracy needs e^{ik_x}Q = 1, so e^{ik_x} must be real. Family (B) is excluded, and
  family (A) leaves exactly **(0,0,0), (0,π,π), (π,0,π), (π,π,0)**. This proves completeness. The note's "Not certified (1)" is therefore closed for T2.
- **Linearization.** At all four points, `T2 ≈ 1 + i(δk_x + 2δk_xσ_x + δk_yσ_y + δk_zσ_z)`, so t = (−1,0,0), v = −diag(2,1,1), **χ = −1**. This is analytic and agrees with the
  numerical value. Box (half-width 0.1) Ch(P_<) = −1 at each node, for both T2 and T3. The net level-0 chirality is −4. ✓
- **Type I.** The invariant parameter is |v^{-1}t| = **0.500 at all four nodes**. s3 prints |v^{-T}t| (0.671, 0.985, 0.500, 0.651). That quantity is not invariant under
  the arbitrary choice of degenerate basis (v → vR, R ∈ SO(3)): over random bases r3 finds a range of 0.502–1.000. The type-I conclusion holds, but the printed numbers
  are artifacts. Fix: use `np.linalg.solve(v, tilt)` in `lib5b.weyl_chirality` / s3.
- **Fermi sheets exist.** `f(k) = e^{−ik_x}det(T2−1) = 2cos k_x − tr Q(k)` is real. Level 0 is {f = 0}. At (2π/3, 0, 0), f = 0 with ∇f = (−5.196, 0, 0) ≠ 0, the eigenvalue is
  non-degenerate (the other eigenvalue lies at distance √3 from 1), and the implicit function theorem gives a smooth 2D sheet. All 300 random k_x-lines cross the sheet,
  with 744 sign changes in total.
- **Sheet flux.** ΣΦ = Σχ = **−4**, while the sum of the sheet tubes' Ch(P_<) is +4. The note's §4 sentence "these carry flux +4" is a sign slip, the same slip as in the NN table.
  s3's log correctly prints "sum Ch(P_<|dN) = +4". I did not compute the sheet flux independently (as the note says, it is inferred), but the sign of the inference rests on
  the identity, whose sign is checked in §1.4.
- T3: det U is constant, the 4 nodes are the same with χ = −1, and the extra band adds only the trivial-bundle planes k_x = −0.25 and π − 0.25.

**Verdict:** the witness is correct and does what it is meant to do (clean-level hypothesis sharp; Σχ ≠ 0 compensated at the same level). Two low-severity corrections apply: the sign of the stated sheet flux, and the type-I numbers.

## 4. Novelty and scope wording

The level-wise relation is in the literature. Sun–Xiao–Bzdušek–Zhang–Fan, PRL 121, 196401 (2018), arXiv:1806.09296, state that the
Nielsen–Ninomiya theorem still applies to Floquet lattices, give the 1D statement "right minus left movers at each quasienergy cut = winding", and give the 3D adiabatic two-band statement
(imbalance = 2·W3 of the adiabatic Floquet operator). This comes from one search snippet; I did not read the full text. HNU (arXiv:1806.06868) and Bessho–Sato (arXiv:2006.04204) are cited
appropriately. The note's "novelty unverified and likely nil" is the right hedge. The combination with Theorem K, which gives level-wise balance for every finite-range walk and every n, is the repo-relevant
content. I know of no explicit statement of that combination, but I did not search exhaustively. Scope wording: "Floquet operators from continuous Bloch Hamiltonians" is fine with the C¹ remark (§2.4).
§5's statement about Sun et al. (a band-subspace imbalance must be cancelled at the same quasienergy by the other bands' sheets) follows correctly from NN′ and the identity.

## 5. Required edits (summary)

1. Results table, NN: `Σχ_p + ΣΦ_S = 0` should be `Σχ_p = ΣΦ_S` (medium).
2. §4 witness: "sheets carry flux +4" should read "ΣΦ = −4 (sheet-tube Ch(P_<) sum = +4)" (low).
3. Win: add the single-band-pair-per-ball hypothesis, or drop the corollary (medium for Win).
4. Lemma S(c) / general identity: use the cluster form of L, with no global φ on the tube (low).
5. s3 / lib5b: type-I parameter |v^{-1}t|. All four values are 0.5 (low).
6. Clean-level wording: allow non-degenerate isolated extrema (charge 0) (low). NN′: C¹ in k (low).

Theorem L, the clean-level NN for all n, D, and Ans are correct.
