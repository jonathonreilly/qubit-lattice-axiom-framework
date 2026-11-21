# LSC gate: line-by-line check of library/lsc.md

Referee: Claude (fresh session), 2026-11-05. One honest check, not a hostile reading. Text: library/lsc.md (552 lines). Source: scratchpad/sa/ca_II.tex, ca_III.tex.

## Notes as I go

- Read: lsc.md §§1-7 in full by section. CA-II 62824-63935 (standing parameters, block-exponent floor, cumulants, first passage, source classes, data families, constant-dependence remark, one-sided floors, the label 63365, printed parts (b)-(e), corollary, per-ball reading remark), 63964-64290 (per-ball theorem and proof), 64437-64480, 64596-64606, 68352-68370, 59600-59830 (torus-bound proof), 679-760, 2791-2966 (correlation theorem), 60695-60770 ((L)(A)(B)(S)(F)), 62030-62045, 62140-62152, 62300-62312, 61417-61432, 7992-8073, 14650-14668, 109859-109976. CA-I 474-492, 897-950, 1721-1760, 2520-2526, 2590-2635, 153570-153618, 153720-153728, 154018-154062, 155035-155100, 157014-157185. CA-III 110890-110900. SA (ym4.tex) 23500-23515.

## Report

First failing step: lsc.md §3 "Normalization", line 214, as used in the floor (21), lines 342-353. The note identifies the correlation theorem's zero-source integral with the Chapter 4 integral ∫ρ^sf_{K'} dV and then applies the Chapter 4 lower member (9). In the bare normalization this fixes (Chapter 1: ρ_0 = exp[-g_0^{-2}A(U)], Haar probability, CA-I 478-481 and 929), (9) together with (i-c) gives a bound on the bare Wilson integral that an elementary estimate refutes once K' ≥ 1 at small g. So the uniform floor, and with it the second assertion of (5) and the constant E_* of (23), is not established.

### The failing step in detail

1. (9) is CA-I 4.33 (i-b)(1), 157028-157130: ρ_k dV_k ≥ χ_k exp[-x_k A(U_k) - E_- N_k] dV_k, with E_- independent of g_k, k, K and g_0. (i-c), 157110, gives ∫ρ_k dV_k = ∫ρ_0 dU. Here ρ_0 is the Chapter 1 bare density with no additive constant (Def. 1.5 points to Def. 1.1).
2. LSC's own §5 computation on the set B is correct (see below). With (9) and (i-c) it gives Z_bare := ∫exp(-x_0 A) dU ≥ exp(-C*_low(g) N^4), where C*_low ≈ 6 log x* + O(1) and N^4 = N_{K'} is the number of last-lattice sites.
3. Upper bound on Z_bare. Use complete axial gauge: set the temporal bonds to 1 off one time slice. For t ≤ T-2, the (i,4) plaquette is then 1 - Re tr(U_i(x,t)U_i(x,t+1)^{-1}). Drop every other plaquette (a_p ≥ 0) and integrate the slices one at a time with Haar invariance. This gives Z_bare ≤ c(x_0)^{3(T-1)T^3}, where c(x) = ∫_{SU(2)} e^{-x(1-Re tr U)} dU ≤ C x^{-3/2}. The number of bare sites is T^4 = L^{4K'} N^4. So log Z_bare ≤ -(9/2)(1-1/T) L^{4K'} N^4 log x_0 + O(L^{4K'} N^4).
4. x_0 > x_{K'} > X, and x* = X + O(m_J), so log x* ≈ log X. For K' ≥ 1 and small g, (9/2)(1/2) L^4 log X exceeds C*_low(g). So 2 and 3 contradict each other. Along every sequence g_0 ↓ 0 this happens, because K' = K - b → ∞. That sequence is exactly the regime the consumers use.
5. Consequence. In Chapter 1's normalization, (9) with its stated independence of K and g_0 is false for K' ≥ 1. So at least one of its hypotheses (h1)-(h4)(a), or of the inputs (10)/(11), fails as stated in CA. The natural candidate is (h4)(a). Its claim l_k ≥ 0 is the only place where a quantity extensive in finer volume is discarded. I have not verified which hypothesis fails. The note can be read in only two ways, and neither works:
   - E = 0. Then (21) is a false statement about Z̃(0).
   - E is a nonzero "vacuum constant". Chapter 4 has no such constant. Then Z^J(0) ≠ ∫ρ^sf_{K'}, and (9) does not apply to Z̃(0).
   The note itself warns (line 212) not to mix normalizations. The defect is that no CA normalization makes both (9) and (13) true.
6. The upper exponent (13) is not refuted. In the E = 0 normalization it is plausibly true but weak (Z̃(0) ≤ 1). A uniform sum E_+^♯ + C_low needs the floor and the upper bound in Balaban's normalized form: the bare density times the accumulated Gaussian vacuum constant. CA's Chapter 4 does not state that form. The same issue affects CA's own 8.8:lem-stability-exponent (II:109918-109975) and hypothesis 8 of the torus-bound proof (II:59677, 59814-59818), unless the correlation theorem's free constant E (II:730-739) is Balaban's normalization. In that case a floor in that normalization is still owed.

### Findings by check item

(1) Statement versus consumers. LSC (a)-(e) is the right statement. It is neither weaker nor stronger in substance.
- (a) is exactly what (d), (e) and the corollary use: K ≤ K_J (II:63700-63705), and a ∈ A for the finite set B(g).
- (b) carries the identification of data, the cumulant identity, norm domination, x_{K'} ≤ x*(g), and a bound on E_+^♯ + C_low uniform in K, g_0, m_1, a. The consumers at 63919 and 64262-64273 need these. The existential reading ("chosen valid per-site bounds") suffices, because the consumers use only (S) and (F) and the sum.
- (c), (d), (e) match the printed parts. II:63531-63565 is a remark on what is used and needs nothing more.
- The §6.4 addition is needed. The principal clause (iii-b), I:2610-2620, asks only m ≥ m_T(g_-) and L^m ≥ ℓ(n,R). The printed part (c) and its corollary use the stronger floor (6.3:eq-one-sided-floors-c).
- The ceiling γ_D is admissible. (iii) is "∀ϱ ∃γ_J ∀g≤γ_J" (I:1739-1742), and γ_D depends only on (L,p,γ).

(2) Steps.
- Offset (a), lines 247-253. Correct. K ≤ K_J follows from clause (0) and the identification. λa - 2c_2 ≤ x_K - x_{K_J} < B^♯ gives λa < B^♯ + c_5. Minor: in Case B, (1) is used outside the correlation theorem's printed quantifier "m_T(g) ≤ m ≤ K" (II:2869-2872). No consumer needs a ∈ A in Case B; (d) uses only K ≤ K_J.
- Floor existence, lines 218-245. Correct. D_g ≥ e, the log bound, and the ratio argument check. L^{m_J} ≥ L^{11} M R_J(X) → ∞ as g ↓ 0, and γ_D exists.
- Identification (15)-(16) and the coupling bound, lines 255-287. Correct; checked against II:63414-63508. x* agrees with the source's X + b_+ + max{0, 3λm_J + 2c_2}, since c_2 ≥ 0.
- Small-field calculation (17)-(20). Correct.
  - Telescoping gives ||∏V_j - 1|| < 4s*. The margins 4s* ≤ a_1/2 and 4B_3 s* ≤ ε*/2 ≤ ε(x) hold.
  - For SU(2), 1 - Re tr W = ½||W-1||²_op. Then A(U_{K'}) < 6Vη^{-4}·½(4B_3 s* η²)² = 48 B_3² s*² V, and xA ≤ ¾V.
  - c_H = 8/(3π³) is right.
  - Minor: the window lemma's alternative reading puts C_Q B_3 in place of B_3 (I:155088-155094). That only changes constants.
- Floor (21). Arithmetic correct. Not established, because its input (9) is refuted in the fixed normalization (above). This is the failing step.
- Upper exponent (12a)-(13). A schematic port, not a derivation. a_Γ, b_Γ, c_gas are named, not computed. Support:
  - II:59729-59739: the history payments change the constants by (d,L)-numbers.
  - II:14655: explicit per-cell bound C_♯[K⁰_cell + 3(N_0(log x)+3)C_0^♯], with N_0 = 4 + 2r log_L(T+1).
  - II:8036-8045: C_♯ ≤ C̄_♯.
  - CA-I (12): explicit (9/2) log x form.
  - Against: the account itself says Balaban's E_± "depend on g_k" with no stated form (II:59768-59769).
  Acceptable at the torus-bound proof's own standing, with its eight retained hypotheses. The note's line 208 claim that no unspecified function of x is assumed is too strong: the log-linear form of the non-top Balaban constants is read from Chapter 4's source-free analogue, not from a sourced statement.
- Constant (23). Inherits the floor failure. Uniformity in K, g_0, m_1, a, N_T and positions would hold if (21) and (13) held in a common normalization.
- §6.1 per-ball deduction with symbolic t. Correct. No circle; the source's own proof invokes LSC only in its constants paragraph (II:64271-64273). The Schwarz/Cauchy step reproduces (log 2)(2Q+2)^n r^n (n/ϱ)^n.
- §6.2 (27). Correct; matches II:63607-63620.
- §6.3, (8) and (e). Correct. The local count matches II:63713-63796. The moment-cumulant coefficient is right. K ≥ (x_0 - X)/B^♯ - 1 follows from clause (0). The finite-set subsequence argument is right.
- §6.4 finite-torus completion, (28)-(29). Logic correct: J, N ≤ N_max, Δ, the monotone C_UV majorant of II:2945-2947, and Case B by (8). It uses (5), so it inherits the floor failure.

(3) Ported parts. All match the source:
- unit rescaling and ℓ(n,RL^b) ≤ L^b ℓ(n,R): II:63600-63620;
- plaquette count P_R = 6(2R+3)^4 L^{4m_J} and C^B_n: II:63735-63787;
- subsequence argument: II:63800-63833;
- Φ of (7): II:63634-63640; it agrees with 6.4:eq-per-ball-bound-b, since Q_∞^n = e^{n[tℓ^4+2C_face]};
- C_UV, C_face and 𝔞 of (24): II:62145-62147, 62306-62308, 6.2:eq-tree-sum-a.
LSC correctly keeps Case B, which II:64437-64448 calls unnecessary. It correctly notes that II:64466-64470 (whole-torus count) is stale.

(4) Inputs, and which are open in their account.
- Used as stated: clause (0); the identification b_{k+1}(0) = β_{k+1} (II:63072-63081, a standing hypothesis); correlation theorem (i), (iii), (iv) (II:2791-2966); CA-I (9) and (i-c); (10)-(11) (I:154052-154058, 155039-155096); the eight retained torus-bound hypotheses; the 6.2 lemmas; Balaban 116 (1.26).
- Open or conditional in their account: the correlation theorem assumes the window-data statement "whose proof is outstanding" (II:2810-2812). The torus-bound floor (hypothesis 8) is unproved (that is LSC's target). The window lemma rests on its window statement 4.31:eq-window-counting-nesting-a.
- New finding: 4.33 (i-b)(1), as stated, contradicts (i-c) and Def. 1.1 at K' ≥ 1. Its hypotheses cannot all hold. The same holds for standing input 4.31(d) (I:154024-154031), which states the same lower member.

(5) Quotations and line citations. Every cited line range I checked matches its content:
- II:63365-63367, 63369-63833, 63701 (I1)-(I3);
- III:110895-110899, II:64603;
- consumers 63531-63565, 63907-63925, 64255-64285, 64436-64478, 68357-68367;
- II:688-699, 2867, 59645-59821 and its sub-ranges, 7992-8073, 14644-14772, 60715-60731, 61417-61432, 62030-62067, 62127-62157, 62293-62314, 63275-63280, 109859;
- I:2610-2620, 157049 (C_Γ), 157110 (i-c);
- SA 23504-23513.
One imprecision: line 52 attributes "(8c_2+4)^{-1/2} ≤ 1/2" to II:2865-2868. The II lines give only γ_J ≤ (8c_2+4)^{-1/2}; the "≤ 1/2" is CA-I 1726-1727 (2.3:eq-thresholds-1). The note quotes no source sentence verbatim beyond labels, and it fabricates no source sentence.

## Verdict

Proved for a smaller scope. These hold as an implication from CA inputs: (a); the identification and coupling half of (b); (d) and (e); (c) and the completion (29) once a valid uniform E_* is available. Not proved: the uniform last-scale floor, hence the second assertion of (5) and the bound (23). The proof as written rests on a CA lower member that is refuted in the normalization the note fixes.

What changes for clause (iii-b): its combinatorial and offset parts are now closed, including the finite-torus completion to the original floor I:2610-2620. (iii-b) still depends on one input. That input is a zero-source floor Z̃(0) ≥ e^{-C(g)N^4} at the last lattice of the run with m = m_J(g), uniform in K, g_0, m_1, a. It must hold in the same bare normalization as the sourced upper bound (13). Chapter 4's (9) cannot supply it in Chapter 1's normalization. Balaban's normalized (0.1) lower member, read with the accumulated vacuum constant, would be the natural source; CA does not state it in that form. Frozen o4-two-point.md stays at CA standing for (iii-b).

Checked line by line by Claude (fresh session).
