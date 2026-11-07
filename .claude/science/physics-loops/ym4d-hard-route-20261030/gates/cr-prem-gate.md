lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T16:57Z

# CR premises: line-by-line check of library/cr-prem.md

Claude (Opus 5.5, effort max), fresh session on the Mac mini worker; branch `claude/ym4d-hard-route` at `7babf904f`; FINISH row 410. One reading by one other model. Not an audit, not human review, no status. No numerics were run; every step below is a written argument.

## 1. Sources, scope and duplicate check

**Object.** `library/cr-prem.md`, Git blob `2882068e9b1c99c612cc38d8418adbe6ed271bdc` (commit `f3f872a47`), Codex gpt-6-astra max. "Note n" means its line n. Read first, as the row asks: `gates/cr-r2-gate.md` §9 (blob `bef9610e`) and `library/cr-r2.md` (blob `76370e07`).

**Sources.** CA-I (`theorem_0_complete_account_raw_I.tex`) and SA (`YM4_sketch_500.tex`) were fetched at `31a47c543775` into a scratch folder. Their SHA-256 values equal the note's (note 30–32), so the note's line numbers are the lines read here. Every cited CA-I and SA line was read. Bałaban's CMP 119 was read from the owner's local PDF (`~/ym4d-papers/balaban_cmp119_243.pdf`, SHA-256 `c629e628…`), journal pages 255–256, rendered as images: (2.2) Γ_0 = Ω_1^c, Γ_j = Ω_j^(j) \ Ω_{j+1}^(j), Γ_k = Ω_k^(k), **B** = ∪Γ_j; (2.11) M_**B**(U) = M^j(U) on Γ_j; and the minimal set **B**_j(Ω) with Ω_n a union of L^n ξ M_1-cubes and dist(Ω_n, Ω_{n−1}^c) ≥ L^n ξ M_1. The note had no PDF access (note 27); these pages confirm its §3 and §7 readings. CMP 98 was not re-read; like the note, this check uses its formula as reconstructed in `library/b98.md` (5).

**Duplicate check (rule 0a).** `library/open-core.md` lines 80–99 list CR as a core statement. `library/open-registry.md` line 14 gives CR one owner, the `cr-claude` lane family; rows 348, 396, 398, 403, 408 and this row 410 are that family. Rows 404–426 attack other lemmas (frame change, CH4-AUX, layer theorem, PRINT-INVERSE, B98-P5). No row attacks the actual-system lemma of note 695–705. So §6 below, which proves a statement about that lemma, duplicates no lane.

**Credit.** CR, its inside proof and every cited input are from Ethan Sussman and Levent Alpoge's complete account (Claude and Codex are authors of their text). The averaging, variational and response theory is Tadeusz Bałaban's. The ladder is Claude's `cr-claude.md`, repaired in `cr-r2.md` after Codex's two gates. The note under check is Codex's.

**Verdicts in one table.** Details follow in §§2–5; the new result is §6; the answers to the row's questions are §7.

| Part of the note | Verdict |
|---|---|
| §1 (EC) counterexample (1) | ADVANCE |
| §1 (EC′) and its local proof | ADVANCE, local scope only |
| §2 (BP) | ADVANCE |
| §3 (R-form) flat-interface counterexample | ADVANCE (CMP 119 (2.2) now confirmed from the PDF) |
| §3 three failed attacks | ADVANCE; attack 2's stated reason is incomplete, and §6 supplies the full reason |
| §3 "equivalence of constrained problems" as the corrected requirement | REVISE: impossible at every interface (§6) |
| §4 P6, eq. (4) | ADVANCE |
| §5 COMP, COMP(=) | ADVANCE for native ladders; REVISE: state the gap floor in terms of M, M_1 |
| §6 (G-c) slab counterexample and set identities | ADVANCE |
| §7 (G-t), eqs. (7)–(10), and counterexample (11) | ADVANCE |
| §8 (S), eq. (12) | ADVANCE; REVISE two missing citations |
| §9 clause (c) and the transfer | ADVANCE |
| Result: the stopping lemma | REVISE: not stated exactly; its first alternative is impossible (§6) |

## 2. The three counterexamples

**(EC), note 55–79, eq. (1): ADVANCE.** Recomputed from SA 7065–7071 and `b98.md` (5). Put U = 1 except on one fine bond b = ⟨w, w+ηe_μ⟩ crossing the face between B(y) and B(y′), with U(b) = e^{itH} and w off the central straight path. A segment [x, x′], x ∈ B(y), contains b if and only if x has w's transverse coordinates; the normal coordinate of x is then free, because w lies in the last layer of B(y). So exactly L of the L^d segments contain b. The connectors Γ_{y,x}, Γ_{y′,x′} stay inside one block, so they never contain b; the central path U[c] misses b. For small t every logarithm is the commuting one, so 𝓜(U)(c) = exp(iL·L^{−d}tH) = exp(itL^{1−d}H). A word in the datum bonds equals exp(intH) with n ∈ ℤ. Since 0 < L^{1−d} < 1, the t-derivatives differ. The note claims exactly this: a native seam test (SA 9623 uses 𝓜(V_{j−1}) on finer-layer bonds) is not a word in the independent native data. It refutes that substitution only, not CR and not (EC) for the undefined graph circuits, as note 75–79 says.

**(R-form), note 166–189: ADVANCE.** CA-I 42969–42970 puts one graph bond on each pair of blocks that share a (d−1)-dimensional face piece. A level-j block B of side Ls whose face is covered by level-(j−1) blocks of side s therefore has L^{d−1} graph rows through that face. CMP 119 (2.2) and (2.11) (PDF p. 255–256) make every native row a bond of the homogeneous lattice T^(j), with datum M^jU. The outward row from the top y of B goes to z = y + Lse_μ, the centre of the neighbouring level-j cube. For odd L ≥ 3 the block of z is the central sub-block of that cube, not a sub-block adjacent to B. So one native row faces L^{d−1} graph rows, and the row sets differ for d = 4, L > 1. Thickening the strata does not remove a local discrepancy (note 176–178). With inward bonds kept (SA 9625), up to L^{d−1} inward bonds end at seam nodes inside B, not at the single graph vertex of B (note 180–182). Correct.

**(G-c), note 456–469, slab: ADVANCE.** The boundary of {c = 2} sits at (NM_1+1)ℓ_2. This is a multiple of ℓ_2, so {c ≥ 2} is a union of level-2 blocks. It is not a multiple of M_1ℓ_2 when M_1 > 1, so {c ≥ 2} cuts an aligned M_1ℓ_2-cube. The c = 1 slabs have width w ∈ ℓ_2ℤ, so both their faces lie on the level-1 grid. On a torus with no exterior, W_0 = W_2 = +∞, and W_1 ≥ w − ℓ_2 ≥ Mℓ_1. Levels of neighbouring blocks differ by one. The width clause of (G-c) holds and the alignment clause fails on the whole torus. This refutes "width implies alignment" only (note 467–469).

**The smaller counterexamples: ADVANCE.**

- (BP), note 128–142. CA-I 42999 and 43055–43059 require only z_B ∈ B, fixed per determining set, so two sets may give one block different base points. At a flat field 1^g, covariance and normalisation give the row g(z_B)g(z_C)^{−1}, so the two rows are 1 and e^{itH}. Correct.
- (G-t), note 563–572, eq. (11). One level-k cube with t = c = k and uniform level-p partitions satisfies item (iii) of CA-I 42985–43006, including (4.12:eq-determining-sets-b). Then W_0(t) = dist((X″)^c, X″) ≤ η < LM_1η. Correct.
- Locality is not COMP(=), note 394–401. Two transports between the same corners of a square are both normalised, covariant and local to the square, and they differ by the square's holonomy. Correct.
- (S), note 670–681. The three set-level counterexamples (a domain meeting a collar, a single filing domain, a far bond) are immediate. Correct.

None of these is a configuration that violates conclusion (a) or (b) of CA-I 45085. Each refutes a proposed inference to a premise.

## 3. The three failed attacks on the stopping lemma (note 191–211)

1. **Identify the rows without changing coordinates: ADVANCE.** The flat-interface count of §2 refutes it.
2. **Compress the extra graph rows by endpoint transports: ADVANCE as a refutation of the shortcut; the stated reason is incomplete.** The note shows that two transports differ at nonzero curvature, so the extra rows are not redundant "up to a small error". That is true but leaves open an exact compression. §6 closes it: no native system has the graph's constraint fibres at any interface, already at the trivial datum. So this attack cannot be repaired by a better choice of transports.
3. **Apply R to the minimum of the level functions: ADVANCE.** The minimum fixes a partition, not the row functions. The proviso of CMP 119 (2.14) quoted at CA-I 94792–94796 asks that ∂Ω meet one stratum, and a box whose boundary crosses a flat level interface fails it.

The three attacks are distinct and each failure is correctly located. The note claims no impossibility theorem (note 712–713); §6 supplies one for the first alternative.

## 4. The positive results

**P6, eq. (4), note 239–344: ADVANCE.** Checked step by step.

- Derivative. At A = 0, d log W_x = i[A(Γ_{y,x}) + A([x,x′]) − A(Γ_{y′,x′}) − A([c])]. The reference term cancels after Σ_x L^{−d} = 1 and the factor U[c]. The factors m_y^{−1}, m_{y′} remove the two connector sums, because x ↦ x′ is a bijection of B(y) onto B(y′). So DH(0)A = Σ_x L^{−d}A([x,x′]), and each segment has L bonds: ‖DH(0)A‖ ≤ L‖A‖. This agrees with the main term L(Q_0A)_c of CA-I 24349–24369.
- Recursion (6). By covariance, 𝓜(e^{iA}) = (e^{iH(A)})^{m(A)}. With (D^v)^{v′} = D^{v′v} (CA-I 42978), g_{r+1} = (g_r restricted to the next sites)·m(A_r). Correct.
- Induction. t_{r+1} ≤ t_r + (K/L)ηL^r t_r^2 follows from a_{r+1} ≤ La_r + Ka_r^2. With t_r ≤ 2a for r < s and Σ_{r<s} ηL^r ≤ 1/(L−1), t_s ≤ a + 4Ka^2/(L(L−1)) ≤ 3a/2 when a ≤ L(L−1)/(8K). Also a_s = ℓ_s t_s ≤ 2a ≤ r/2, so (5) stays applicable. Correct.
- Endpoints. ‖g_m − 1‖ ≤ K′Σ_{r<m} a_r ≤ 2K′aℓ_m/(L−1) by unitary telescoping. Then ‖𝓜^m(e^{iηa})(c) − 1‖ ≤ 2·2K′aℓ_m/(L−1) + 2aℓ_m, so C_6 = 2 + 4K′/(L−1). Correct.
- Support. Every path read lies in the two endpoint blocks (`b98.md` Lemma 2), so the bound holds on a complete equal-level carrier. Correct.

Scope: the native CMP 98 iterate, centre endpoints, real SU(2) data with ‖a‖_∞ ≤ a_*. It does not identify the account's base points or graph rows; that is (BP) and §6.

**COMP and COMP(=), note 361–406: ADVANCE for native ladders; REVISE one sufficient condition.** The evaluation-tree induction is correct, and so is the restricted-criticality consequence (CA-I 44959–44962). For a native ladder step q → q+1, the new rows of level q+1 read level-q rows on double blocks (SA 7127), and the finer native set retains all those rows when it has level q there. *Repair.* The note's sufficient condition is "a gap greater than 2ℓ_{q+1}, in sup-distance, from the new top region to the finer levels below q and to the exterior". From `cr-r2.md` Corollary 3.2, which gives Euclidean widths, this holds when min(M, LM_1)/√d > 2L. For d = 4 that is M > 4L and M_1 > 4. Add M > 4L to the one-sided floors on M; M_1 ≥ L ≥ 15 already gives M_1 > 4. The order of constants is unchanged.

**(G-t), eqs. (7)–(10), note 488–582: ADVANCE.** CA-I 32840–32851 and 32871–32883 are quoted exactly; CMP 119 p. 256 (PDF) prints the 𝔯_2 rule. With t extended by −1 off X″, {t ≤ i−1} = Ω_i^c and {t ≥ i+1} = Ω_{i+1}, so 𝔯_2 gives W_i(t) ≥ M_1ℓ_{i+1} = LM_1ℓ_i, including i = 0 and hence the exterior (9). Then LM_1 = LR′_⋆𝔐 > R_1𝔐 = w_adm (10), using L > 1 and R′_⋆ ≥ R_1. The account states the same margin at CA-I 32884–32885 ("satisfies the conditions of [CMP102b (1)] with block 𝔐 and R := R′_⋆ ≥ R_1"). The metric conversion is correct: d_∞ ≤ d_1 ≤ d·d_∞ on ℤ^d, so a d_1-gap gives d_∞ ≥ LM_1ℓ_i/d, and LR′_⋆ ≥ 15R_1 > 4R_1 by CA-I 43575. Euclidean widths are covered in the same way, since d_2 ≥ d_1/√d.

**(S), eq. (12), note 610–647: ADVANCE; REVISE two citations.** Checked: CA-I 93534–93536 (C^♯ adds m_♯ layers of π_k-cubes; CA-I 63713 identifies π_k-cubes with level-k M-cubes), 93601–93604, 96084–96086, 96110–96115, 20443–20448 and 53758–53760. Cells are closed cubes of side a = MŘ_k cornered in aℤ^d. Cells that do not touch have index difference at least 2 in some coordinate, hence sup-distance at least a. Points of C^♯ lie within m_♯M ≤ (a−M)/2 < a of C. So C^♯ meets no other component, and C^♯ \ C ⊂ Λ_k. *Repairs.* (i) The step "different components are a apart" needs Λ_k^c to be a union of level-k cells. The note uses this but does not cite it; CA-I 53816–53819 supplies it (Z_i is a union of level-i cells for i > h, with Z_k = Λ_k^c, component by component, on one grid). (ii) Λ_k ⊂ Ω_k^old reads CA-I 43221's "old domains" as the label in force of CA-I 53755–53760. This is the natural reading, but the account does not state it; say so. With these, (S) holds for every full read X″ ⊂ Y_4 ⊂ C^♯, and (S′) holds for every full read in Z ∩ Y_4 (CA-I 53807–53810 places the collars R_n inside Z).

## 5. Every other step

| Note lines | Claim | Verdict |
|---|---|---|
| 3–39 | Provenance, hashes, target CA-I 45085–45106 "Proof outstanding", which exports only (a), (b) of CA-I 44167–44185 | ADVANCE (hashes reproduced; statement lines read) |
| 43–53 | CA-I 42981–42984 leaves "elementary" undefined; CA-I 43113–43127 imports T1 through word tests; SA 9607, 9610, 9623 describe native rows and seam tests | ADVANCE (quotes exact) |
| 81–91 | (EC′): ‖T_P(e^{iB}D) − T_P(D)‖ ≤ C_T‖B‖_∞ replaces n_P = 16 in Lemma 6′ | ADVANCE. Under (EC) a test is a word of at most 2^d factors, so (EC′) holds with C_T = 2^d; (EC′) is the weaker input |
| 93–102 | (EC′) for a fixed finite native test on a fixed smaller chart | ADVANCE at that scope. A seam test multiplies four factors, each a datum entry or a one-step average; on a closed ball inside the chart each has a bounded derivative, so C_T depends on L, d and the chart only. That the ladder's data lie in one common chart is not shown; the note says so (note 101–102) |
| 104–111 | Three routes to literal (EC) fail | ADVANCE |
| 115–126, 144–145 | (BP) holds on the native hierarchy (CA-I 24244–24246, 24373–24374, 794–799); the abstract hypothesis asks only z_B ∈ B (CA-I 42999, 43055–43059) | ADVANCE |
| 149–164 | R is restricted to {Γ_i} or **B**_p(X″) ∪ {Γ_i}_{i<p} (CA-I 10175–10178), with CMP 119 meanings (CA-I 9833–9837); (2.14) is a set identity with three provisos (CA-I 92521–92530, 94792–94796) | ADVANCE |
| 184–189 | The corrected requirement is "an equivalence of constrained problems, or a response theorem directly for the graph problem" | REVISE: the first alternative is impossible at every interface (§6) |
| 215–237 | The named equal-level average is CMP 98 (1.5) (CA-I 43013–43016); CA-I 16546–16552 carries Σ_{q<n}L^{q+1}η before its final O(1); SA 7268–7270 states the anchored form; (3) is `b98.md` (5) | ADVANCE. (3) is a reconstruction of a garbled OCR formula (`b98.md` line 233); P6 is proved for (3) as written |
| 353–359 | COMP is a grant at CA-I 44874 and 44949–44953; native composition is SA 7127 and CA-I 24373–24374 | ADVANCE |
| 410–435 | CA-I 43520–43524, 53641–53660, 53779–53785, 53836–53837 quoted exactly; subdivision and restriction facts | ADVANCE. The subdivision needs M/M_1 ∈ ℕ, which holds because both are powers of L and M ≥ M_1 (Φ1) |
| 437–454 | Class table K1–K5 (CA-I 43359–43367); truncation at j keeps W_i for i < j and empties the upper set for i ≥ j | ADVANCE (checked: for i ≤ j, {min(o,j) ≤ i−1} = {o ≤ i−1}; for i < j, {min(o,j) ≥ i+1} = {o ≥ i+1}) |
| 471–484 | Three routes to the universal (G-c) stop at distinct points | ADVANCE |
| 586–608 | Source bound on Y_4 ∩ (Z ∪ Ω_k^old) (CA-I 43223–43225, 43295–43299); (S′) is the minimal replacement; AV and T1 read all of X″ | ADVANCE (AV(e) reads every fine plaquette in the blocks through which P passes, CA-I 43044–43052, and these blocks cover X″) |
| 649–668 | Reads in B_5 or in a collar R_n ⊂ Z (CA-I 53807–53810) satisfy SRC when contained in Y_4; the warnings at CA-I 43347–43351, 93595–93606, 77033–77038 | ADVANCE |
| 730–765 | At n = k the radii are ϑ_Eα_kη² and ϑ_Eα_kℓ_p^{−1} (CA-I 43402–43405); deducing (c) from (b) needs ϑ_E > 2L²B_3 and ϑ_E > 2L³B_3; α_k cancels; floors exist only for n < k and for K4 in B_5 (CA-I 43425–43434, with (Γ_3) at 43611 giving 4L³B_3 there); CA-I 43437–43440 is box-restricted | ADVANCE |
| 767–781 | Transfer of the real-factor corollary (CA-I 44803–44843) under equality on the full read | ADVANCE |
| 688–728 | Result and stopping lemma | REVISE, §7(1) |

