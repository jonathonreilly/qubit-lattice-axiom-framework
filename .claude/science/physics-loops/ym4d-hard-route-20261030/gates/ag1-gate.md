# AG1 gate (pass 3): library/ag1.md

First failing step: Lemma 1, lines 412–413. The step says each surviving designated cell is counted in M_D at every paid level. This needs an ancestry input that §1 does not list (Finding 2). The step is repairable, not fatal.

Text checked: `library/ag1.md`, all 1,344 lines. Cross-read: `tp1.md` lines 40–48 and 144–155; `in1.md` lines 14–40 and 372–387; `nl1-L.md` lines 381–515. Source files are in `scratchpad/sa/`. Their SHA-256 values match the five values at ag1.md lines 1246–1250.

## Findings

**1. Line 42 against tp1.md line 48. The event 𝔏 has a different meaning in the two texts. Repairable.**
AG1 defines 𝔏_k^{≥a}(c) as "c belongs to a live component of age ≥ a". TP1's hypothesis AG (2.11) uses "a live component of lineage age at least b meets history cell c". AG1 line 26 says that adjacency means "closures meet". Under that reading TP1's event also counts components that only touch c.
Repair: TP1's event is contained in the union over the at most 3^4 = 81 cells c′ equal or adjacent to c. Thus (AG-k1*) gives (2.11) with C_AG multiplied by 81. Alternatively, state in AG1 that "meets" means "contains". Rate and weight are unchanged.

**2. Lines 412–413 (Lemma 1, the proof of (MB)). An ancestry input is used but not listed. Repairable. This is the first failing step.**
The proof says: "Every designated surviving cell is counted by a terminal or a designated healed lineage, once at each paid level." Take a designated cell z that survives over [n,q]. Let C_j be its live component at level j. The claim needs C_{j−1} ⊂ C_j, so that C_{j−1} ∈ pred(j,C_j). Then every C_j lies in the lineage that contains z at its designated level n. If C_{j−1} ⊄ C_j, then C_j can be in a lineage that is healed by k and does not contain z at level n. That lineage is not in M_D, and the payment at level j is lost. (R0)–(R3) and §1.1 do not give this inclusion. Line 52 ("nestedness proves this directly") covers only the other direction, from lineage to survival.
SA states the property at 23328: a cell live at levels n,…,k "belongs to the lineage of the component that is live at level k and contains it". It follows from two facts: the live region at j−1 propagates into Z_j^pre (SA 17328–17330), and healing removes whole components of Z_j^pre.
Repair: add the property as a named LF1(2) input next to (R0)–(R3). The alternative is to designate z at every paid level and count C_D once per pair (cell, level). That alternative changes the C_D bookkeeping in Lemma 9 and in Lemma 11's small-torus case.

**3. Lines 596–616 and 649–658 (Lemma 4, (21)–(22), and the (OS) discussion). The NL1 citation is out of date, and an NL1 outstanding item is not named. Repairable.**
AG1 cites "NL1 Proposition S, with its (V1)–(V6)" and "`nl1-L-draft.md` §6.2". The distilled NL1 (`nl1-L.md`) has neither name. It states the cap as Lemma 5, (16)–(17), with R_cap = c_cap/(c_T C_A e^{κ̄} g). AG1's (21) and c_* agree with that formula.
NL1 Lemma 5 also has an **Outstanding** item (nl1-L.md lines 494–502): the lower bound D_f ≥ 10LMŘ_i − C is not shown for the full source carrier. AG1's (22) assumes exactly this bound. So do the bracket in (24) and the form ε_scr(ℓ) on the right side of (23). Inside Theorem 5 the bound is contained in the hypothesis (OS), so the theorem is not wrong as a conditional statement. But lines 649–658 describe only the ℓ_m formation-level loss. Lines 1299–1302 do not list the distance item either.
Repair: cite `nl1-L.md` Lemma 5 under Theorem 4's hypotheses. State that (OS) also contains the full-source distance input that NL1 marks Outstanding, or name that input separately.

**4. Lines 660–674 together with the proof of Theorem 5 (lines 699–720). Some live-attached terms are not covered. Repairable.**
Lines 663–665 put "carried constraint factors whenever they do not satisfy the ordinary local norm" into the live-attached sum. (OS), equation (23), bounds only "the contributions of kept forms and islands", N^♮_{K,I}. The proof of Theorem 5 bounds N^♮ by (15) plus (23). So it uses a bound on the carried constraint factors that neither (15) nor (23) supplies.
Repair: state (OS) for the whole live-attached sum (kept forms, islands and these carried factors). Alternatively, prove that these factors satisfy (L-K)- or (L-I)-type size bounds.

**5. Line 1182 against tp1.md lines 148–151. The floor and the admissible tori are not carried over. Minor.**
Theorem 12 holds only when x_j ≥ X_*, and only on the tori that (CB) admits. TP1's (2.11) is written "uniformly in j,c" with neither restriction. For x_j < X_* the left side is not uniformly bounded, because the age sum can run to j−1. TP1 uses (2.11) only at j = k_1, in its large-x regime, and on "compatible volume" (tp1.md line 41). So TP1's argument is not affected.
Repair: add "for x_j ≥ X_* on (CB)-admissible tori" when AG1's result is quoted as TP1's hypothesis AG.

**6. Lines 545–546 and 1229. Citation range. Minor.**
The hard-core tree inequality that Lemma 3 uses is the Lemma at SA 1225–1269. SA 1270–1347 contains the rooted-tree iteration and the convergence/log theorem. That theorem invokes the inequality but does not prove it. The reading itself is correct.
Repair: cite SA 1225–1347.

**7. Line 590 (Lemma 4, Γ_X). Minor.**
Γ_X = sup_ξ(C_Ψ V° − Ψ(ξ,p_*)) requires Ψ(ξ,p_*) to be real. The hypotheses give only that Φ(ξ,p_*) is real and that Φ − Ψ does not depend on p.
Repair: replace Ψ by Re Ψ in Γ_X. The Schwarz step and the domination by e^{1/4} times the centre density then go through unchanged.

**8. Line 381 ((MB)). Minor.** The symbol m is not defined. From (8) it must be |D|, the number of designated cells; Lemma 9 and Lemma 11 use it that way. State this.

**9. Lines 22 and 59, against in1.md lines 20–23 and 387. Conventions. Minor.**
(3) uses c_f, which ag1.md never defines. IN1 calls this constant c_0. IN1 Lemma 4's proof gives exactly (3), with lower rate λ_♯ ≥ 3c_0/4 ≥ c_0/2 and upper bound (c_0+ς)(j−i)+2c_2.
IN1 also defines R_j from the running minimum of the frame θ. AG1, TP1 and SA 17334 use the running minimum of x. All texts must use one convention, because cell sides c_j = MR_j a_j are construction data. AG1's estimates survive either choice, with changed constants in (36) and in c_AG.
Notation: δ denotes both the BGL background rate and the thresholds δ_j. R_1 denotes both an early constant (§6 step 2) and R_j at j = 1.

**10. Lines 210–211 and 990–991 (designation entropy). Minor clarity in the assumed interface.**
QL′ allows a path cell to lie "within R_* cells of … the hull of one at i−1". D_des counts only level-(i−1) cells within about R_*+1 cells of the path cell. The count and the s_* separation are correct only if the designated live (i−1)-cell itself lies within R_*+1 cells. Since R_* = 14 + b_1 and bx(B) ⊂ B^{+b_1} (line 422), this is presumably intended.
Repair: say so in the interface.

## Steps checked and found correct

- **Lemma 1 (16).** The chain sum λ/(1−λ) ≤ 1/5 and the ε-split give 3v(P)/10. The event-node bound uses |pred| + Σ(d′+1) ≤ 3e. V(1 − 13λ/10) gives C_G = (60/47)(4A+C_1). The leftmost-leaf charging is injective. Acted predecessors are paid at p_{j−1}. Markov's inequality then gives (MB), apart from Finding 2.
- **Lemma 2.** The Schwarz constants 2ωt/(1−t) ≤ 4tω hold. The telescoping in switches and the iterated Schwarz step give 2o_f e^{−κ̄j}. The shell sum is at most 4e^{κ̄} o_f e^{−κ̄m}, and κ̄ ≥ 4κ_P gives (17). In the exempt-hull step: at most 1 + |T_f|/(R_i−1) hulls, A_g = 4 + 2C_0^isl L, and stopping at the first hull gives the gap. Cauchy constants √3/ρ and 12/ρ² with Schur sums give (18).
- **Lemma 3 (Kotecký–Preiss).** The T^{(h)} iteration and the KP induction hold. Rooting gives (c). The t-scaling and continuity argument gives (b) without a branch choice. This agrees with SA 1270–1347. (d) is correct as a conditional statement under (H-Mayer) and (KP-h).
- **Lemma 4.** The largest power in (20) is 2p_0 + 9r. The zero-free radius gives exponent change 2Γ/(8Γ+1) ≤ 1/4. Then e^{1/4} − 1 ≤ 1/3 by the termwise bound e^{1/4} ≤ (1 − 1/4)^{−1}, and |log| ≤ Σ 3^{−n} = 1/2. (21)–(22) follow.
- **Theorem 5.** The choice of ℓ_1, ℓ_2 is possible because q − σ > p_0. C_* comes from the running minimum, (3), and |x−θ| ≤ θ/4. With (24), N^♮ ≤ (C_ord+2)ℓ^{τ_B}. Then 4e^{κ̄} ℓ^{−σ} C_N^an ℓ^{τ_B} ≤ 1, and X_P is correct. The hypothesis q ≥ τ_I is not used in the proof; this is harmless.
- **Prékopa–Leindler / sub-Gaussian bound (Lemma 6).** The quantile transport and AM–GM step is correct. It agrees with SA 27149–27212. The marginal potential satisfies ψ″ ≥ λ. In the variance identity both boundary terms have the stated sign. Linear tilts are allowed. (25) has no dimension factor and no volume factor.
- **Lemma 7.** The Combes–Thomas conjugation gives 2/a_− and K_∞. Convolution with the force bound gives μ′. The cutoff integration by parts has no boundary term. The six-direction tail is 6e^{−λr_in²/24}. The s-homotopy with the even point s = 0 and the first-exit argument is valid.
- **Theorem 8 (TT).** δ_{i−1} = g_{i−1}𝔟, so a trigger forces |ℓY| > t, and the mean bound uses C_∞ = √J C_2. Disjoint supports give squared norm ≤ mC_2². Chernoff then gives exp[−λmt²/(24C_2²)], which yields the stated c_T exactly. Fine-to-coarse elimination is correct: under (CL0) every later indicator is a function of R_i. (MB+T) follows by Markov's inequality on history-measurable EC.
- **Lemma 9.** The C_L budget holds: the v_k part is n/[128(1−L^{−1})] < n/64, M is chosen after n, and the total is ≤ 5n/64 < n/8. Visited-window freshness and the bound K_i·2ε_i = η_i hold, and the conditioning error of the draft is correctly removed. On the cluster-type payments, the "no long cluster" hypothesis is replaced by paying O_i or Z_i through the path. This works: N″ ≥ 8, H bounds the exclusions, at most one cell is discarded, the entropy is ≤ 3N″χ/4, N″χ/8 ≥ δD_i, and the final display holds since K_i^4 ≥ n^4L^{4s}. All conditions in (30) follow from one floor, uniformly in i ≤ k.
- **Theorem 10.** The four tile functions cover true survival by the first bad level. The chessboard norms are e^{−c_a r_k(k−h+1)} for good survival and η_i e^{−c_a r_k(i−h)_+} for the other types. The sum is ≤ 10e^{−v_k}Q^{−(k−h)}. The summed norms use subadditivity of ‖·‖_ch. That property is standard and follows from (5) by expansion, but (CB) does not state it.
- **Lemma 11.** The deepness claims for the 16 shifted tilings hold. The counts m/16, m/256 and m/512 hold. (34) gives (160n^4 α^{1/512})^m ≤ 2^{−m}. The identity L^{12a}Q^{−a} = (2L)^{−a} holds. The small-torus case gives e^{−c_a r_k(a+1)} ≤ e^{−v_k}Q^{−a}.
- **Theorem 12 and (36).** Here x_j ≥ 4c_2, r ≥ 2, log(x_j/2) ≥ 1 and x_j ≥ 4, so v_j ≥ δnM(log x_j)²/2048. X_* = 2X_0 + 4c_2 gives x_i ≥ X_0 for all i ≤ j.
- **Match with TP1 (2.11).** The rate (log x)², the weight L^{8a}, the running minimum of x (tp1.md lines 45–47; equal to AG1's R_j above the floor), lineage age, the stopped law P^{(j)} and κ_T = 1/4 all match. The two exceptions are Findings 1 and 5.
- **Random-threshold measure identity.** (MI-1)–(MI-7) do not appear in ag1.md. They are condensed into the (K)/(MI) LF1 input at lines 72–80. That bullet contains every property the text uses: an own uniform used at most once, adapted visiting, p_τ measurable before u_τ, disjoint tile uniforms, and the kernel image law. Lemma 9 and Theorem 10 use only these. The draft's proof of (MI-4)–(MI-5) from (MI-1)–(MI-3) (`ag1-draft2.md` Lemma 5.2) is correct.
- **Constants order (§6).** The order agrees with SA 19469–19470. The tile size n is fixed before κ, independent of M and κ̄. The M-dependence of C_I, S_d(κ_P/M), c_P and c_AG is explicit. The κ̄-dependence of c_* and of the floor X_P is stated. No circular choice of constants was found.
- **Outstanding items.** (OS), the QL′ derivation and the identification of (11) are used only where they are named: Theorem 5, Theorem 12, and §1.4/§1.5. The silent uses found are those in Findings 2, 3 and 4.
- **Source readings.** The readings of SA 1270–1347, 6185–6212, 9783–9789, 17317–17407, 17471–17564, 17575–17610, 17642–17664, 17800–17831, 17841–17920, 17959–17997, 19459–19497, 23250–23340 (including 23265), 27149–27212 and 28207–28224 are correct. So are CA-I 49495–49546 and 54985–55011; CA-II 79847–80060, 84948–85075, 113200–113235, 126214–126220, 126262–126282 and 127294–127316; CA-III 111180–111205 and 111418–111436; and YM3 52576–52590. The one exception is Finding 6.

## Verdict

No step is fatal. Theorem 12 proves TP1's AG-k1* as a conditional implication from its named hypotheses. Two silent inputs must be added first: the ancestry property (Finding 2) and the extension of (OS) to all live-attached terms (Finding 4). With these, AG-k1* matches TP1's (2.11) in rate, weight and running-minimum convention, up to the factor 81 for "meets" (Finding 1) and the stated floor and tori (Finding 5). The outstanding list should also name NL1's full-source distance item (Finding 3). The other findings are notation and citation fixes.

Checked line by line by Claude (fresh session).
