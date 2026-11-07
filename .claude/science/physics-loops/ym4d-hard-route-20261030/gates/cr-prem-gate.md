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
- Induction. t_{r+1} ≤ t_r + (K/L)ηL^r t_r^2 follows from a_{r+1} ≤ La_r + Ka_r^2. With t_r ≤ 2a for r < s and Σ_{r<s} ηL^r ≤ 1/(L−1), t_s ≤ a + 4Ka^2/(L(L−1)) ≤ 3a/2 when a ≤ L(L−1)/(8K). Also a_s = ℓ_s t_s ≤ 2a ≤ r/2, where r is the note's chart radius (note 265), so (5) stays applicable. Correct.
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

## 6. A step of the stopping lemma: no fibre identity at an interface

Proved here by Claude; not yet checked by the other model. It decides the first alternative of the stopping lemma (note 697–702), the "native representation" that preserves the constraint fibres. The answer is negative at every interface, already at the trivial datum.

**Setting.**

- 𝔅 is a determining set on a domain X in the sense of CA-I 42965–42970. Its averaging map satisfies (c) of CA-I 43018–43027: normalised, gauge covariant, local. Nothing else is assumed. In particular any choice of the interface rows left open at CA-I 43015–43016 is allowed. Its base-point set is 𝒵.
- N is a native system on X in the sense of CMP 119 (2.2), (2.11): nested Ω_0 = X ⊃ Ω_1 ⊃ …, each Ω_m a union of aligned cubes of side M_1ℓ_m, with lattice distance dist(Ω_{m+1}, Ω_m^c) ≥ M_1ℓ_{m+1}. Its rows are the bonds of T^(m) in Γ_m, with datum M^mU. The inward bonds of SA 9625 may or may not be kept. Its node set 𝒩 is the set of row endpoints.
- Both use one nested L-adic family of cubes. This is the account's own description: the cubes "anchored at the origin" of CA-I 42962–42964 are the centred blocks B(y) of CA-I 789–799, 849–851, whose faces lie on ℓ_mℤ^d.
- Facts used about N. It is normalised. It is covariant at its nodes: M^m(U^σ) = (M^mU)^{σ|T^(m)}. It is local: the row ⟨w, w′⟩ of level m reads U only on bonds with both ends in B^m(w) ∪ B^m(w′) (SA 7127; `b98.md` Lemma 2). At a commuting configuration U = exp(iaH) with small a, each row equals exp(i(Q^m a)(row)H) with Q^m linear: all logarithms in (3), or in SA 7069, are then the commuting ones.
- Interface. B ∈ 𝔅 has level j ≥ 1. Across its +μ face F it meets the r = L^{d−1} blocks b_1, …, b_r ∈ 𝔅 of level j−1, along the pieces F_1, …, F_r. (If one level-(j−1) block meets B across F and the cube B + ℓ_je_μ lies in X, all r cubes of that face layer are blocks: that cube is subdivided, and blocks that meet differ in level by at most one, CA-I 42997–42998.) A crossing bond of F_i is a fine bond with one end in B and the other in b_i.

**Proposition N.** Let d ≥ 2, L^{d−1} > 2 + 6d and M_1 > 3d/2. Then C(𝔅, 1) ≠ C_N(1). There is a configuration U, as close to 1 as desired, with N(U) = N(1) and M_𝔅(U) ≠ M_𝔅(1), or with M_𝔅(U) = M_𝔅(1) and N(U) ≠ N(1). Hence no map Φ from native data to graph data satisfies C(𝔅, Φ(V)) = C_N(V) for all V in a class that contains the trivial datum. (If it did, 1 ∈ C_N(1) would force Φ(1) = M_𝔅(1) = 1.)

For d = 4 the conditions are L ≥ 3 and M_1 > 6. The account has L ≥ 15 (CA-I 43575) and M_1 = R′_⋆𝔐 ≥ R_1 ≥ L (CA-I 32845–32851).

*Proof.* **Step 1: node sets.** Let z ∈ 𝒵 \ 𝒩. Put σ(z) = e^{itX} with X ≠ 0 and small t ≠ 0, and σ = 1 at every other site. Then N(1^σ) = 1^{σ|𝒩} = 1 = N(1). Every graph row ⟨z, z′⟩ has value σ(z)σ(z′)^{−1} = e^{itX} ≠ 1, and such a row exists because X is a connected union of at least two blocks. For w ∈ 𝒩 \ 𝒵 exchange the roles. So assume 𝒩 = 𝒵 from now on.

**Step 2: the native rows that read F.** Let e = ⟨x, x+ηe_μ⟩ be a crossing bond of F_i. Let c = ⟨w, w′⟩ be a native row of level m that reads e, so that x and x+ηe_μ lie in B^m(w) ∪ B^m(w′).

(a) *Levels m ≤ j.* The level-m cube that contains x lies in B, because the family is nested and m ≤ j. It is one of the two cubes of c; call its centre w. Then w is a node, hence a base point in B, hence w = z_B. The site x+ηe_μ is not in B, so it lies in the other cube, which is the level-m cube across the +μ face of B^m(z_B). So w′ = z_B + ℓ_me_μ. Each level m ≤ j therefore has at most one such row, c_m = ⟨z_B, z_B+ℓ_me_μ⟩. It reads only crossing bonds whose inner end lies in B^m(z_B). For m ≤ j−1, B^m(z_B) lies in the level-(j−1) sub-cube Q_0 of B that contains z_B. So c_m reads crossing bonds of at most one piece, F_{i_0}, the piece on the face of Q_0, and i_0 is the same for every m ≤ j−1.

(b) *Levels m ≥ j+1.* The level-m cube that contains x contains B, so the carrier of c contains z_B. By the layer lemma below, m ∈ {m(z_B)−1, m(z_B), m(z_B)+1}, where m(p) denotes the native level of a site p, p ∈ Ω_{m(p)} \ Ω_{m(p)+1}. So m takes at most three values. At such a level, every crossing bond of F has its ends in the same two level-m cubes: Q, the cube containing B, and Q′, the cube containing B + ℓ_je_μ. A row reads them only if one of its cubes is Q and its carrier contains Q′. If Q = Q′, these are the bonds of T^(m) at the centre of Q, at most 2d of them. If Q ≠ Q′, it is the one bond that joins the two centres. So at most 6d rows of level ≥ j+1 read crossing bonds of F.

In total, at most 1 + 6d native rows read crossing bonds outside F_{i_0}.

*Layer lemma.* A native row of level m whose carrier contains a site p has m ∈ {m(p)−1, m(p), m(p)+1}. Proof. Each Ω_n with n ≥ m is a union of aligned cubes of side at least ℓ_m, so an aligned level-m cube lies inside it or outside it. Hence the cube of a level-m top lies in Ω_m \ Ω_{m+1}. Next, d_∞ ≥ d_1/d gives dist_∞(Ω_{n+1}, Ω_n^c) ≥ M_1ℓ_{n+1}/d > (3/2)ℓ_{n+1} ≥ (3/2)ℓ_m for n ≥ m−1, by M_1 > 3d/2. Every point of the cube of a row endpoint lies within sup-distance (3/2)ℓ_m of the row's other endpoint. So the cube of an outward end (a site outside Ω_m) lies in Ω_{m−1} \ Ω_m. The cube of a kept inward end (a seam node in Ω_{m+1}) lies in Ω_{m+1} \ Ω_{m+2}. A level-m carrier therefore lies in Ω_{m−1} \ Ω_{m+2}, and m(p) ∈ {m−1, m, m+1}. □

**Step 3: an abelian family.** Each row c of Step 2 that reads a crossing bond outside F_{i_0} gives a linear functional λ_c on ℝ^r, defined below. Choose t ∈ ℝ^r with t ≠ 0, t_{i_0} = 0 and λ_c(t) = 0 for all these at most 1 + 6d functionals. This is possible because r − 1 = L^{d−1} − 1 > 1 + 6d. Then scale t to be small. Let U_t equal e^{−it_iH} on each crossing bond of F_i, oriented from B to b_i, and 1 on every other bond.

*Graph side.* Let σ_i = e^{it_iH} on b_i and 1 elsewhere. On the bonds with both ends in B ∪ b_i, U_t equals 1^{σ_i}: it is 1 inside B, e^{it_iH}e^{−it_iH} = 1 inside b_i, and e^{−it_iH} on a bond from B to b_i, which crosses F_i. Locality, covariance and normalisation give M_𝔅(U_t)(⟨z_B, z_{b_i}⟩) = σ_i(z_B)σ_i(z_{b_i})^{−1} = e^{−it_iH}. Some t_i ≠ 0, so M_𝔅(U_t) ≠ 1.

*Native side.* A row that reads no crossing bond of F reads only bonds where U_t = 1, so its value is 1. The rows c_m with m ≤ j−1 read crossing bonds of F_{i_0} only, where U_t = 1; their value is 1. Every other row c reads the commuting configuration U_t = exp(ia_tH), with a_t linear in t. For small t its value is exp(iλ_c(t)H), where λ_c(t) := (Q^m a_t)(c), and λ_c(t) = 0 by the choice of t. So N(U_t) = 1 = N(1). □

**What it shows and what it does not.**

1. *Scope.* It needs only (c) for the graph, so no definition of the interface rows avoids it. The interface hypothesis holds whenever a block B of level j ≥ 1 meets a level-(j−1) block across a face and the neighbouring cube B + ℓ_je_μ lies in X: each of its face-layer sub-cubes is then a level-(j−1) block, by the one-level rule. Take a ladder set 𝔅^(q) under the geometry of `cr-r2.md` Corollary 3.2, on a face-connected part of X″ that contains a top block and a point with c_E < q. Some top block B meets a non-top block across a face; by the one-level rule that block has level q−1. Corollary 3.2 gives W_{q−1}(b_q) ≥ min(M, LM_1)ℓ_{q−1} > ℓ_q when M > L, and every point of B + ℓ_qe_μ is within Euclidean distance ℓ_q of B. So B + ℓ_qe_μ lies in X″, and every ladder rung that changes anything has such an interface. The trivial datum lies in the data class of T1 (its plaquette products are 1), and the background 1 lies in R's regularity class. A representation valid on those classes must therefore cover it.
2. *Not excluded.* A representation that holds only near the actual non-flat bases U^(q), and fails at flat data, is not excluded by this argument. No mechanism for one is known: the account gives no formula for the interface rows from which to build it.
3. *For the literal graph systems, the load-bearing statement is the second alternative.* That is R proved directly for the graph problem, at regular real bases, with the five members of CMP 102 (190) and decay in the layered metric. Bałaban's CMP 102 theory concerns the native problem, the one CMP 119 (2.11)–(2.12) restates and refers back to. By Proposition N the graph problem is a different constrained problem at every interface, so the Bałaban theorems the account cites do not supply R-graph. The same holds for the account's other graph-system inputs taken "by statement": T1 (CA-I 43122–43127), the response at the identity (CA-I 43157–43205), AV(e) on graph plaquettes that pass through blocks of two levels (CA-I 43066–43074), and AV(d) at interface rows (CA-I 43080–43084, which the account already calls a hypothesis).
4. *The consumers read native sets.* CA-I 9844–9845 (CMP 119 (2.34), one of the consumers' spaces) defines the derived configuration as U_{p,X} = U(**B**_p(X) ∪ {Γ_i}_{i<p}, M^·(**U**)). CA-I 43060–43064 says item (iii) abstracts these native sets, and CA-I 43342–43344 says the consumers' spaces are Bałaban's. If the chain reads Bałaban's spaces, the statement it needs is CR for the native sets. By Proposition N that is a different statement from CR for the graph sets, not a restatement of it. For native sets, (R-form) holds by the form of the set (R admits **B**_p(X″) ∪ {Γ_i}_{i<p}, CA-I 10176–10177) once the sequence is admissible. Every native row is an equal-level M^j average, so P6 (note §4) covers every row and the interface averaging hypothesis is not used. (BP), COMP and COMP(=) hold natively (note §§2, 5), (EC′) holds locally (note §1), and the 𝔯_2 tower margin holds (note §7).
5. Proposition N refutes neither CR for the graph sets nor CR for the native sets.

## 7. Answers to the row's questions

**(1) Is the stopping lemma stated exactly, and is it the first unproved step for CR (a), (b)? No on both counts.**

*Not exact.* (i) Its first alternative, a native representation that preserves the constraint fibres, is impossible at every interface (§6). (ii) "Native representation" and "the twist and support bounds used by the ladder" are not precise statements. (iii) It bundles independent premises with different scopes: (S′), (G-c), the tower identification, (EC′), and (BP) with COMP(=). The bundle covers every open premise, so nothing is missing from it, but it is not one lemma.

*Not the first step.* Conclusion (a), and (b) for n ≥ p, never use the representation. The inside argument (CA-I 44226–44303) needs only T1, AV(e) and the source bound on all of X″. So the first unproved step for (a) is (S′) on the actual outside reads. Under the literal graph reading, (a) also rests on T1 for graph systems, which by §6 is not Bałaban's theorem at an interface. The representation part enters only for (b) with n < p, through R at the rungs.

*Exact restatement.* Two forms, depending on how §4.12 is read.

- **(SL-graph), literal reading.** For every outside K2–K4 pair (E, p, X″) of CA-I 45085 and every rung q with n < q ≤ p: (S′) holds on X″; and R holds for the graph problem on 𝔅^(q) := 𝔅_E(q, X″). That is, at the real minimiser U^(q) = U(𝔅^(q), M_{𝔅^(q)}Ū), for complex data twists B on the bonds of 𝕃(𝔅^(q)) in the half polydisc of radius r_P, the five members of CMP 102 (190), each times its power of ℓ, are at most C_H sup_{y′}|B(y′)|e^{−δ_H d(y,y′)}, in the contour metric of 𝔅^(q), with C_H, δ_H depending only on L and d. Add (EC′) for the plaquettes of 𝕃(𝔅^(q)) at the ladder's data, COMP and COMP(=) for the rung, and (BP).
- **(SL-native), the reading of CA-I 9844–9845 and 43060–43064.** Read 𝔅_E(q, X″) as Bałaban's **B**_q(X″) ∪ {Γ_i}_{i<q}, with the consumer's levels. Then R is CMP 102 Proposition 9 for these sets once the sequence is admissible. The open items are: (S′) on X″; admissibility of the native rung sequence, namely (G-c) for the old and prepared levels and the identification of t_{X″} with the 𝔯_2 tower of X″ (whose margin note §7 proves); one common chart for the ladder data in (EC′); and the ladder lemmas of `cr-claude.md` and `cr-r2.md` rewritten for native rows. In that rewrite every row, outward rows included, is an equal-level M^j average, so P6 replaces Lemmas 4(b), 5.1 and 5.2 and the interface averaging hypothesis drops out. This rewrite is not yet written.

The literal and native statements are different statements (§6). If the chain reads Bałaban's spaces (CA-I 43342–43344), it needs (SL-native); a proof of (SL-graph) would not supply the native derived slot.

**(2) Does any counterexample refute CR itself, or only a premise as stated? Only premises.** Each counterexample refutes one proposed inference: native tests as datum words (§1), the literal row identity (§3), (BP) from z_B ∈ B (§2), alignment from width (§6), (G-t) from the abstract tower rule (§7), COMP(=) from locality (§5), and three set extensions of (S) (§8). None gives a consumer pair, a datum or a minimiser that violates (a) or (b) of CA-I 45085. Proposition N (§6 here) refutes only the fibre-identity route.

**(3) Which premises of `cr-r2.md`'s table are discharged, and at which scope?**

| Premise | Status after the note and this check | Scope |
|---|---|---|
| (EC) | Not discharged. Replaced by the weaker (EC′). | (EC′) is proved for a fixed finite native test on a fixed smaller chart (note §1). Not for graph plaquettes, which are undefined. That the ladder data lie in one chart is not shown. |
| (R-form) | Not discharged. | Refuted as a literal row identity (note §3), and as any fibre identity at an interface (§6). It holds by the form of the set under the native reading, given admissibility. |
| (BP) | Discharged natively. | Bałaban's fixed hierarchy, where the base point of a block is its centre (note §2). It does not follow from the abstract hypothesis. |
| (S) | Discharged on two source domains. | (S) for every full read X″ ⊂ Y_4 ⊂ C^♯ (eq. (12), with the two citations of §4 added); (S′) for every full read in Z ∩ Y_4, including B_5 and the collars R_n. Open for general outside reads. |
| (G-c) | Not discharged. | Width and alignment hold for the upper prepared members i ∈ I_M (CA-I 53779–53785, with M/M_1 ∈ ℕ) when the consumer's superlevel sets are those members or their complements, restricted to X″. Open for the old and lower members, where the account withholds Hypothesis (G). Width alone does not give alignment (slab). |
| (G-t) | Margin discharged; identification open. | For an 𝔯_2 tower: aligned M_1ℓ_i-cubes, W_i(t) ≥ LM_1ℓ_i including the exterior, and LM_1 > R_1𝔐 = w_adm in d_1, d_2 and d_∞ (the last needs LR′_⋆ > dR_1, which holds). That the abstract t_{X″} is an 𝔯_2 tower is open; the abstract rule (11) does not give it. |
| P6 | Discharged natively. | The CMP 98 iterate (3) at centre endpoints, for real fields with ‖a‖_∞ ≤ a_*, with C_6 = 2 + 4K′/(L−1). For the account's graph rows it needs those rows to be these iterates at centre base points. Under the native reading it covers every row. |
| COMP, COMP(=) | Discharged natively. | Native one-level rungs with double-block coverage: a sup-distance gap greater than 2ℓ_{q+1}, which Corollary 3.2 gives when M > 2√d·L and M_1 > 2√d. Not for graph interface rows: locality does not give COMP(=). |

## 8. Defects that change a statement, ranked

1. **Result, note 695–705: the stopping lemma's first alternative is impossible.** Failure: Proposition N (§6). Repair: state (SL-graph) or (SL-native) of §7(1) instead, and record which reading the chain uses.
2. **Result: the stopping lemma is presented as the first unproved step.** Failure: (a) and (b) with n ≥ p do not use it; (S′) blocks them first. Repair: list (S′) first, as the open premise of (a), and the rung statement after it.
3. **Note 384–391, COMP's sufficient gap is not tied to M and M_1.** Repair: from Corollary 3.2 it holds when M > 2√d·L and M_1 > 2√d. For d = 4, add the one-sided floor M > 4L in step 2 of the order of constants; M_1 ≥ 15 already exceeds 4.
4. **Note 623–633, eq. (12) uses "Λ_k^c is a union of level-k cells" without a source.** Repair: cite CA-I 53816–53819 (Z_i is a union of level-i cells for i > h, component by component, on one grid; Z_k = Λ_k^c).
5. **Note 642, Λ_k ⊂ Ω_k^old.** Repair: say that it reads CA-I 43221's "old domains" as the label in force of CA-I 53755–53760. That reading is natural but not stated in the account.

No other step fails. Every quotation checked is exact at the cited lines.

RESULT: library/cr-prem.md checked line by line. The counterexamples ((EC) eq. (1), (R-form) flat interface, (G-c) slab, and the smaller ones) and the positive results P6 (4), native COMP and COMP(=), (G-t) (7)–(10) and (S) (12) all ADVANCE. COMP and (12) need small repairs (a floor M > 4L for d = 4; two citations). The stopping lemma is REVISE: it is not exact and not the first unproved step, since (S′) blocks (a) first. New and proved here, not yet checked by the other model: Proposition N. At every interface, already at the trivial datum, no Bałaban native system has the graph system's constraint fibres. So the "native representation" branch is impossible, and the account's graph-system T1, response at the identity and R are not Bałaban's theorems there. No counterexample refutes CR. Open: (S′) for general outside reads; R for the graph problem, or (SL-native), meaning admissibility of the native rungs ((G-c) for old and prepared levels, the 𝔯_2 identification of the tower), one chart for (EC′), and the native rewrite of the ladder; clause (c).

Checked line by line by Claude (Opus 5.5).
