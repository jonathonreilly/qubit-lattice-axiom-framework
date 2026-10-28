# REVIEW_S13_S14: independent hostile review of sessions 13 and 14

Reviewer: an independent agent that did not write the proof.

Inputs:
- PROOF.md, byte-identical to PROOF_session14_snapshot.md (`cmp` empty).
- `diff PROOF_session12_snapshot.md PROOF_session14_snapshot.md` (814 lines). The S13/S14 block is l.2563-3037 of
  PROOF.md, read by offset; the header is l.3-64, and the tally and orders are l.4014-4290.
- RTARGET.md §19 and §24-32; LOG.md sessions 13-14 (l.651-711); REVIEW_S11_S12.md (its 11 binding fixes).
- Checks c28 and c29: criteria, scripts, outputs, time files. **c28 A-D and c29 A, B, D were re-run. c29 C was
  re-run too: load 1.95 and 46% free at its start** (results in §4).
- **Provenance.** The session-13 and session-14 agent transcripts (subagents aa93502… and a0b5f48…; tool-call
  timestamps, UTC), and file mtimes.

Scratch work is in the scratchpad `rev1314/`:
- `indep_consts.py` and `fine_scan.py`: an independent re-implementation, from the PROOF text only and in mpmath at
  30 digits, of the EXP-strip and EXP-strip' constant chains, with an r_0 scan;
- `notol/`: a copy of c29 with every float tolerance in Part B removed;
- all re-run outputs.

No other file was edited.

**Bottom line.**
- **R1112 fixes.** All 11 are applied correctly, including the decision-4 "by inference from" label and the
  parenthesis reading. Two scope residues remain, in places the earlier review did not list:
  - l.634-636 drops "n ≥ 1";
  - the S12 header l.79-80 still says the r symbol has a "non-analytic part", which S13 has since disproved.
- **The S13/S14 items survive. None is WRONG; none is a GAP.**
  - Five items need wording or scope fixes: N2-exp, N2-exp', NA-alg, NA-FP, SRC-id.
  - PG^{(k)} (with IT-line) is CONFIRMED in every step.
- **The strip estimates are rigorous.** They are explicit closed-form inequalities, each re-derived here, checked
  at one point (η, r_0) by an independent mpmath evaluation. They are not root-finding.
  - The stated (η, r_0) PAIRS are slightly off: the stated η is rounded up past the bisection value for the stated r_0.
  - The stated η VALUES are still valid with a nearby r_0. Every one is confirmed.
- **The uncounted reduction B-NA-red has a real hole: (FP♯) names the wrong operator.**
  - It also passes from "critical on the slice" to "critical", which needs a Lagrange step.
  - (G♯) is a template, not a statement: its norms are not fixed.
  - So RTARGET §32's "the pre-stated acceptable partial outcome is met" is an overclaim. §29(a) "met" is also an
    overclaim: the target asked for a background-independent constant, and FP_U depends on the background.
- **NA-FP is a Hessian-level (Gaussian) identity.** The header and the tally should say so.
- **Checks.** Every re-run reproduces the stored outputs exactly, apart from timing and RSS lines.
  - The failures are honestly recorded: c28 B, C3, C4 and c29 C1.
  - c29 B's added float tolerances, which the criteria file forbids, turn out not to be load-bearing. Without them it
    still PASSES.
- **Corrected tally: 60 / 2 / 7 / 24 + 1, unchanged.**

## [R1112-fix] audit (REVIEW_S11_S12 binding fixes 1-11)

| # | Fix | Where now | Verdict |
|---|---|---|---|
| 1 | Dimock citation §4.7, l.1672 | l.1787-1788 | Applied |
| 2 | c21 annotation appended (l.52-53 untouched) | checks/c21_criteria.md tail | Applied (wording correct) |
| 3 | "by inference from"; why the CL parenthesis is not applied | l.72-73, 188-199, 4076-4078 | Applied; the reading is stated as a reading, with a fallback ("the record moves to the CL with no change of content"). Correct |
| 4 | CE-geo' → upper inequality of (122), Dimock d = 3 | l.136, 1689, 2060-2068, 4086; RTARGET l.409 | Applied, including the sharper Σℓ_j\|u_j\|_1 form |
| 5 | N2-a set-valued | l.2106-2109, 2134-2136 | Applied |
| 6 | WA: a > 0; F̂(0) = 0 | l.2361-2362, 2372-2374 | Applied |
| 7 | Power-tail BOUNDS | l.2417-2419, 4288-4289 | Applied. Residue (b) |
| 8 | BG-b scope (n ≥ 1, small curvature); "for the linearised chain" | l.82-84, 2458-2459, 4066 | Applied where listed. Residue (a) |
| 9 | PG-ext Collect split | l.2505-2509 | Applied. Re-computed: 88 + 281664 + 2·2·20·2·(π/2)⁸·216/9 = 88 + 281664 + 142328 = 424080 = 4.241·10⁵. Correct |
| 10 | c26 c/T fit informational; Part B slopes not tail exponents | l.2449-2452 | Applied |
| 11 | N2 kernels vs N5 covariance | l.2558-2561, 2013-2016 | Applied |

**Residue (a), l.634-636 (L2 note [S12]).** "So BG-b holds for the linearised chain at small coarse curvature,
unconditionally" lacks "for the levels n ≥ 1 (the n = 0 term needs the current step's residual)". The S11-S12 review did
not list this line, so it is a new residue, not a failed fix.

**Residue (b), l.79-81 (S12 header).** "whose non-analytic part at p = 0 is homogeneous of degree 2 (for r) …" is now
contradicted by Theorem N2-exp: the r symbol and the B_k-symbols are analytic. Annotate it: "[S13: an upper bound only;
the r and B_k-symbols are analytic (N2-exp); only F-representatives of f_0 carry a non-analytic term]".

## (1) Session-13 PROVEN-HERE items

### Theorem N2-exp, with EXP-id, EXP-real, EXP-strip and Corollary N2-exp-b (l.2572-2728): CONFIRMED-WITH-FIX

**EXP-id: CONFIRMED.**
- Δ_α = φ_αδ_α is the Fejér identity: |D_n|² = sin²(θ/2)/(n²sin²(θ/2n)), φ_α = 4n²sin²(θ/2n), Δ_α = 4sin²(θ/2).
- aΣ = Σ_μaφ_μδ_μ/β_μ = Σ_μφ_μ(β_μ - φR_μ)/β_μ = φΨ.
- 𝓡̂ = -φν̄/(β_μβ_νΣ) = -aν̄/(β_μβ_νΨ).
- The f_0 bracket was re-derived. ν_σD_σ/δ_σ = ν_σ/D̄_σ = ν^{(n)}_σ, so the ν^{(n)}_ρν^{(n)}_σ term cancels
  antisymmetrically, and what is left carries φ.
- The P̂_μ = β_μ/φ identity is confirmed numerically in c28 A (relative error ≤ 2.4e-13, re-run).

**EXP-real (R1)-(R6): CONFIRMED.** Each line was re-derived.
- (R1): sinc²s ≥ max(1 - s²/3, 4/π²) on |s| ≤ π/2.
- (R3): S_s(x) ≤ S_s(0) = s^{-2} because t ≥ 0. Σ_K Πδ = 1 by Parseval. For K ≠ 0, φ^{(K)} ≥ 4n²sin²(π/2n) ≥ 9.
- (R4): Π(1 - u_i) ≥ 1 - Σu_i with u_i ∈ [0, 1], and κ(1 - t/6) + (4/π²)t is linear in t.
- (R5): the stated Ψ_U, with κ in place of κ(1 - r_0²/6) in the denominator, is a weaker but valid form.

**EXP-strip (P1)-(P7): CONFIRMED.**
- I re-derived (P4)'s ordered telescoping: z-factors before, x-factors after, with the μ-direction carrying two
  factors. It gives exactly ε(1 + e^η)(1 + e^η + e^{2η} + e^{3η}) + εe^{4η} ≤ 4e^{3η}ε(1 + e^η) + εe^{4η}.
- The Parseval bounds Σ_K|D(z_K)|² ≤ e^{2|y|} and Σ_K|D(z_K) - D(x_K)|² ≤ ε² are right.
- Re sin²(a + ib) ≥ sin²a - sinh²b gives λ.
- (P7) uses Re(1/(1 + f)) ≥ 1/(1 + ρ) on |f| ≤ ρ.

**Theorem N2-exp: rigorous; CONFIRMED-WITH-FIX.**
- **Is the strip estimate a proof?** Yes. η_* is defined by finitely many explicit inequalities in (η, r_0, κ, κ̂, L).
  The theorem only needs them to hold at one point. I re-implemented the chain from the PROOF text (mpmath, 30 digits):
  - The values are valid: the best η over r_0 is 0.01141 (κ = 1, r_0 = 0.574), 0.00807 (κ = 0.25), 0.01182 (κ = 4).
  - **Fix (l.2661):** the stated pairs fail at the stated η. The binding conditions:
    - (0.0111, r_0 = 0.55): br_V ratio 0.998 < 1;
    - (0.0118, 0.65): e_Ψ/(Ψ_U/2) = 1.0002 > 1.
    So the η values are rounded up past the bisection value for the printed r_0. Quote a valid pair (e.g. 0.0111 at
    r_0 = 0.57), or round η down. c28 B ran at the script's unrounded η (≈ 0.01109), so the check is unaffected.
  - The f_0 condition "≤ 0.15φ(x)" (l.2674) holds at all three: 0.131, 0.143, 0.117. It is not in the script's `ok`
    test; add it.
- **Periodicity at ∂Q (l.2670-2672): CONFIRMED-WITH-FIX (wording).** "both have φ ≥ 9 or are the K = 0 term, and the
  same bounds apply" does not prove a gluing. The closed cubes S_η(Q) and S_η(Q + 2πe_α) meet only on a face. The
  correct argument is short:
  - each alias term is 2πn-periodic in each variable, and the K-sum runs over residues mod n;
  - so P̂_μ, D and 𝓡̂ are 2π-periodic meromorphic functions on C⁴;
  - g = 𝓡̂ on S_η(Q) minus a null set;
  - a locally bounded meromorphic function is analytic (Riemann extension).
  The same holds for the f_0 symbols, since e^{i(p+2πK)·u/n} is n-periodic in K for integer u. Replace the sentence.
- **Uniform M.** The |x| ≥ r_0 bound 4(1 + |Δφ|/b_*)/(ψ_0br_V) was re-derived, with |β_μβ_ν||Σ| ≥ ¼β_0ψbr_V.
  - The K ≠ 0 f_0 majorant |D_n(w)| ≤ e^η min(1, π/|Re w|) holds, since |sin(w/2n)| ≥ |sin(Re w/2n)|.
  - The step "e^{cη} × LED-unif (2)'s real-axis majorant" is a one-line sketch but correct.
- **Uniformity.** No bound depends on n beyond n ≥ 3. T enters only through periodisation. u enters only through
  |e^{iθ_K·u/n}| ≤ e^{4η}. EXP-F2 and EXP-F3 do not occur. CONFIRMED.
- **"True rate" (header l.53, L2 l.639, l.2717, LOG l.667).** The rate ≈ 0.98 is a numerically located zero of Den
  on p = (iw, 0, 0, 0), scanned over p_⊥ ∈ {0, π/2, π}³. Call it "the located rate (numerical, not proven)". Never call
  it "the true rate".
- **Post-run fit ranges (l.2715-2716).** The six fits in c28_time.txt are 0.950, 0.972, 0.934 (k = 1) and 0.906, 0.930,
  0.884 (k = 3). "0.95-0.97" and "0.91-0.93" drop 0.934 and 0.884. Write "0.93-0.97" and "0.88-0.93".

**Corollary N2-exp-b (which kernels are exponential): CONFIRMED-WITH-FIX.**
- **Exponential (proven): CONFIRMED.**
  - 𝓡 (F ↦ r) on all 2-forms;
  - B_k ↦ r_{k-1} and B_k ↦ f_0 at each offset u;
  - via J-str (c), B_k ↦ r_i and B_k ↦ J^c_0: (Q_str^T)^m has bounded coarse range, so the rate is kept in coarse
    units.
- **Power-tail: CONFIRMED as stated, but not counted.**
  - The unrestricted f_0 extension contains the degree-0 symbol Π_ex. This is standard; that its coefficient is
    nonzero at p = 0 is asserted, not shown.
  - 𝒦̂_u + Π_coex is "not shown exponential" (honest). My re-run of C5 at T = 16 flattens at x = 6-8 (periodic images).
    At T = 24 the decay is consistent with |x|^{-6}.
- **"What N6 consumes" (l.2693-2697): ARGUED, not proven. Label it so.**
  - The B_k-kernels act on the gauge-variant B_k. The N2-lin sup bounds in terms of dB_k are only ℓ¹ / power-tail
    kernels in F.
  - Exponential decay in B_k plus sup bounds in F is not exponential locality in the curvature. To get that, N6 needs
    either:
    - exponential F-kernels for the gauge-invariant outputs it actually uses (r, which N2-exp gives on all F, and the
      fine curvature df_0), or
    - a localisation lemma (local axial gauge plus cut-off). S14 states this only for SU(N), as "argued only"
      (l.2964-2966).
  - **Recommendation:** prove that F ↦ df_0 is exponential on all 2-forms. dΠ_ex = 0 on 1-forms removes the degree-0
    term, and d(1 - e^{ip·u/n})Π_coex = (1 - e^{ip·u/n})d is analytic. So the fine CURVATURE response is plausibly
    exponential without any representative issue. That would turn the N6 sentence into a proven statement.
  - The κ > 457 arithmetic (M ≳ 457/m_*) is right as a necessary condition.

### Proposition PG^{(k)} with Lemma IT-line (l.2729-2764): CONFIRMED

- **IT-line (a).** h^{(m+1)}(dλ) = M(M^{(m)}λ - ev^{(m)}λ) + h(d ev^{(m)}λ) = M^{(m+1)}λ - ev^{(m+1)}λ. This uses
  MM^{(m)} = M^{(m+1)}, and ev∘ev^{(m)} = ev^{(m+1)} (nested centres, L odd). CONFIRMED.
- **(b).** ∫_P dh^{(m)} = h^{(m)}(Y) - h^{(m)}(Y_c), and avg_Y h^{(m)}(Y) = Mh^{(m)}(X), so the Mh^{(m)} terms cancel.
  CONFIRMED.
- **(c).**
  - The link value V_l is an average of L^{5m} fine values with multiplicity ≤ L^m per fine bond, so
    |V_l|² ≤ L^{-8m}·L^{5m}·L^m·Σ = L^{-2m}Σ_slab.
  - |H_m|² ≤ max|P|·Σ_{all internal l}|V_l|² ≤ 2(L - 1)·2L^{-2m}Σ_{B(X)}a². The step bounds Σ_{l∈P} by the sum over all
    internal links: crude, but valid.
  - Σ_mL^{-m} ≤ L/(L - 1) gives 4L²/(L - 1).
  - There is no contradiction with PG-line's ε^{-1} loss: at k = 1 the funnel has n = L fixed. CONFIRMED.
- **PG^{(k)}.**
  - Λ_res is unchanged, by (a). On H_0^{(k)}, Q^{(k)} = Q_str^{(n)}, so PG (1)-(3) and PG-ext are unchanged.
  - In step (4), 160ε²Σ|h^{(k)}|² ≤ 160·(4L²/(L - 1))||A_c||². This replaces PG's 1 + 1280/9 = 143.2 by
    1 + 640L²/(L - 1) = 2881 at L = 3.
  - C_IT(3) = 3.4·10⁶ + 69 + 44160·4.5 = 3.5988·10⁶ ≤ 3.6·10⁶. The QA coefficient is 4·2881 + 8.5·10⁵ = 8.62·10⁵. The
    margin is thin but correct.
  - Uniform in k ≥ 1, T ≥ 2. IT-F1 and IT-F2 do not occur. **CONFIRMED.**

## (2) Session-14 PROVEN-HERE items

### Lemma NA-alg (l.2774-2806): CONFIRMED-WITH-FIX (domain of (b))

- **(a): every constant was re-derived at y = 1/20, and all improve for smaller y.**
  - |E| ≤ (y²/2)e^y = 0.526y²;
  - 4.5e^{0.15} = 5.228;
  - (3 + 5.23y)(1 + 0.53y) = 3.348;
  - |K| ≤ 9.11y²;
  - Lip ≤ (e^{3y} - 1) + (1 + 3.24y)(1.03y) = 4.44y ≤ 0.23.
  - The global-maximiser step:
    - Re tr(W_*^{-1}M) ≥ Re tr M gives N - Re tr W_* ≤ |W_*^{-1} - 1||Δ_M|;
    - |W - 1|² = 2(N - Re tr W), so |W_* - 1| ≤ 2.06y;
    - eigenvalue arguments: |θ| ≤ (4arcsin(¼))|e^{iθ} - 1| = 1.0107|e^{iθ} - 1|, so |log W_*| ≤ 2.082y < 3y;
    - log W_* is traceless because Σθ_j ∈ 2πZ and the angles are small.
  - G = H + iθ1, with ||H - 1|| ≤ ||G - 1|| ≤ 18.4y² (HS ≥ op). CONFIRMED.
- **(b): fix.** The expansion uses "tr ρ = 0". For the principal log of an element of SU(N), tr ρ ∈ 2πiZ can be nonzero
  (N = 3, all eigenvalues e^{2πi/3}). Then the linear θ-term θ·Im tr ρ survives.
  - Add the hypothesis ||ρ||_op < 2π/N, which implies Σθ_j = 0. Alternatively, define ρ as the log in su(N) nearest
    to 0.
  - In the intended small-|ρ| use this is automatic.
- With that, the √N factors and the remainder 2√N(e^r - 1 - r - r²/2)/N ≤ e^r r³/(3√N) are right. The θ-part
  vanishes at second order because tr ρ² is real.

### Proposition NA-FP with Lemmas NA-inv, NA-crit (l.2807-2856): CONFIRMED-WITH-FIX (scope)

- **NA-crit: CONFIRMED** (trivial and correct).
- **NA-inv: CONFIRMED.**
  - The orbit tangent: log(e^{sλ(x)}U_be^{-sλ(y)}U_b^{-1}) has derivative λ(x) - Ad(U_b)λ(y) = -(D_Uλ)_b.
  - Invariance of S under 𝒢_V follows from the covariance of W_0(M̄).
  - c29 D2/D3 confirm (re-run identical): 3.7e-8 at U*, 1.9e-2 off criticality.
- **(i) telescoping: CONFIRMED.**
  - Forward link: Ad(T_{j-1})(D_Uλ)_b = Ad(T_j)λ(x_j) - Ad(T_{j-1})λ(x_{j-1}).
  - Backward link (T_j = T_{j-1}U_b^{-1}): the same, with ã_j = -Ad(U_b^{-1})(D_Uλ)_b.
  - c29 D1: 1.9e-15.
- **(ii): CONFIRMED.**
  - Injectivity holds by parallel transport.
  - M_U is onto: an axial path to c_X + e_μ is the single link.
  - The dimension count and the χ_UΓ injectivity (⟨λ, P_resD^*Dλ⟩ = ||Dλ||² on Λ_res) are right.
- **(iii): CONFIRMED.** The FP-ab change of variables gives FP_U = (2π)^{m_2/2}|det χ_UΓ|^{-1}det(Γ^TΓ)^{1/2}.
- **Fix 1 (scope; header l.22, tally l.4020, LOG l.698, RTARGET l.567).**
  - The identity is for the Gaussian integral at a critical background: I = F·e^{-½H_U}, invariant under the LINEAR
    action A ↦ A + D_Uλ.
  - It is not the non-linear Faddeev-Popov identity, where the orbit is A ↦ log(e^{λ}·e^AU)U^{-1} and the determinant
    depends on A. Gribov copies are relevant at large fields.
  - Write "at the Hessian (Gaussian) level" in the header and the tally.
- **Fix 2 (composite slice, l.2853-2856).**
  - "linearises to Q^{(m)}_UD_U = D_{V^{(m)}}ev^{(m)}" is asserted. Write the one-line differentiation of the
    covariance, with its sign convention.
  - The induction itself is right: M_V(M^{(m)}λ - ev^{(m)}λ) + M_Vev^{(m)}λ - ev^{(m+1)}λ.
  - The onto-ness of M^{(k)}_U for the composite is not "unchanged": paths to a fine neighbour of c_X are no longer
    single links. It holds, because the composite weight of a fine site is a positive weight times an Ad of a transport,
    but state it.
- **RTARGET §29(a) "met" (l.567) is an overclaim.** The pre-stated target asked for "a background- and
  field-independent constant", and FP_U depends on the background. The ledger says this honestly (l.2850-2851).
  - §32 should read "(a) met except the background independence of the constant, which fails (FP_U = FP_U(V);
    its locality and analyticity are OPEN)".

### Lemma SRC-id (l.2874-2907): CONFIRMED-WITH-FIX (the f_0 half is unwritten and unchecked)

- **(i) and (ii): CONFIRMED.**
  - The Euler-Lagrange equations hold; dB_0 = dΔ^{-1}d*dB_0 because dΔ^{-1}d = 0.
  - The effective datum follows by the LED-dual (ii) iteration.
  - c29 A1/A2 (re-run identical): ≤ 1.1e-12 against LSMR with a source.
- **(iii) r-part: CONFIRMED.** The algebra was re-derived:
  - b̂ = ĝ^{(0)} = -cW̄ĵ/φ;
  - by the c29 A3 identity aΣν̄W̄ĵ/β = ΠD̄[Σν̄^{(n)}ĵ - φΣν̄^{(n)}Rĵ/β], the d*j = 0 term drops;
  - this gives exactly the stated r̂^{(0)}.
- **(iii) f_0 part: CONFIRMED by my re-derivation, but the PROOF text (l.2897-2899) is a one-sentence sketch, and c29
  A3 tests only the r-identity. Fix: write out the two lines.**
  1. ĵ_σ - κc^{-1}W_σ·cW̄_σĵ_σ/β_σ = (1 - aδ_σ/β_σ)ĵ_σ = (φR_σ/β_σ)ĵ_σ.
  2. The ν-part is κW_σν_σΠD̄S/(β_σΨ) = aν^{(n)}_σ(δ_σ/β_σ)S/Ψ (using W_σν_σ = ΠDν^{(n)}_σδ_σ and κΠDΠD̄ = a). Its
     curl is (aS/Ψ)ν^{(n)}_ρν^{(n)}_σ(δ_σ/β_σ - δ_ρ/β_ρ) = S/Ψ·φν^{(n)}_ρν^{(n)}_σ(R_ρ/β_ρ - R_σ/β_σ).
  Both carry φ. Add a check of the f_0 identity at complex points (c30).
- **Scope: correct and honest.** Only the K = 0 alias is analytic; the K ≠ 0 Biot-Savart part is not bounded uniformly
  in n (l.2903-2907).

### Theorem N2-exp' with Lemma EXP-strip' (l.2967-3018): CONFIRMED-WITH-FIX (stated pairs)

- **(S1)-(S7), line by line: CONFIRMED.**
  - (S1): Σw_l|l| = (n² - 1)/(3n) and Σw_ll² = (n² - 1)/6 were re-derived, and sinh(ts) ≤ t sinh s.
  - (S2): sup_{|x|≤π} min(1/3, |x|/6)/max(4/π², 1 - x²/12) = π²/12, attained for x ≥ 2.672.
  - (S3): 2n²(cosh(η/n) - 1) and n sinh(η/n) are decreasing in n; n|sin(x/n)| ≤ √φ_α.
  - (S5): Re φ·Re R ≥ φ(R - e_RR) - 4c_φ(R̄ + e_RR) holds for either sign of Re φ, which is what the stated ρ_R needs.
    ρ_R^+ and ρ_I match term by term.
  - (S6): |R(z)| ≤ R̄ + e_RR + e_RI.
  - (S7): the positive part is over |β|² ≤ D_2β², the negative over |β|² ≥ (1 - ρ_R)²β².
- **"First-order changes are imaginary" is the right mechanism.** My evaluation gives c_Z ≈ 1.32η and ρ_I ≈ 10.75η at
  κ = 1. These are the limiting terms, as stated.
- **Values: fix (l.3005-3007).**
  - The best η over r_0 (fine scan) is 0.03854 (κ = 1, r_0 = 0.704), 0.02750 (0.25, 0.375), 0.03077 (4, 0.909); so
    0.0385, 0.0273 and 0.0307 are VALID.
  - At the stated pairs, br'_V/(required) = 0.989 (κ = 1, r_0 = 0.70) and 0.993 (κ = 4, r_0 = 0.90) fail. The
    bisection value at r_0 = 0.70 is 0.03845.
  - Fix as for N2-exp: quote valid pairs, or round down (0.0384, 0.0306).
  - κ̂ = 16 (r_0 grid 0.01): 0.01406, 0.02269, 0.02166 versus the stated 0.0141, 0.0227, 0.0217. These are rounded
    up by < 0.3%; the same fix applies.
- **The arithmetic is right.** 3.5×; M ≳ 457/0.0385 = 1.19·10⁴; the located/proven ratio is ≈ 25.

## (3) Uncounted items and the S14 reduction

### Proposition NA-IFT (l.2908-2918): CONFIRMED

- (r + s)² ≤ 9(1 + G_D)²s²;
- G_Ds + (9/16)s ≤ r;
- Lip ≤ 5GC(1 + G_D)s ≤ 5/16;
- the derivative bound 2(G_{D,w} + G_wC_w(r + s)) ≤ 2G_{D,w} + 6G_wC_w(1 + G_D)s.
Standard and correct. Needs C¹ of 𝔑, which is implicit.

### Proposition B-NA-red (l.2919-2933): CONFIRMED-WITH-FIX as an implication (not counted); hypotheses imprecise

- **Fix 1: (FP♯) names the wrong operator.**
  - NA-IFT solves ∇(E + ½||Γx||²) = 0 inside the slice 𝒮 ("𝓛 the Hessian … on 𝒮"). NA-crit needs criticality in
    every direction, including the gauge directions transverse to 𝒮.
  - The correct step: treat the slice constraint h(x) = 0 with a Lagrange multiplier μ. Then pair the Euler-Lagrange
    equation with τ_xλ: invariance gives ⟨Γ, DΓτλ⟩ = ⟨μ, Dhτλ⟩ for all λ. So Γ = 0 and μ = 0 follow iff the COMBINED
    operator λ ↦ (Dh(x)τ_xλ, DΓ(x)τ_xλ) is onto.
  - So (FP♯) must be stated for the combined slice + residual fixing, not for DΓ_gf∘τ alone. With that, the conclusion
    stands.
- **Fix 2: (G♯) is not stated precisely enough to be provable.**
  - X, Y, D are "norms on chain configurations and sources" with no definition.
  - BNA-F2 says they must be a level-weighted coarse-unit Schauder pair, but neither the pair, the Hölder exponent,
    the level weights, nor the data norm D is fixed.
  - Nor is it said how D = sup|B_k| maps into X = C^{1,α}: G_D needs the chain to smooth the data, which is plausible
    but unstated.
  - (R♯) inherits the same imprecision.
  - **Required:** one displayed definition of (X, Y, D, weights, slice), so that (G♯) is a theorem statement.
- **The F1-F3 diagnosis.**
  - **F1: correct.** The proven kernels are data kernels; SRC-id shows a source acts as the non-local datum.
  - **F2: plausible and standard, labelled "argued".**
    - The YM non-linearity is first order: [A, ∂A] + [A, [A, A]].
    - ∇²Δ^{-1} is Calderón-Zygmund, unbounded on L^∞, so sup norms cannot close.
    - Hölder pairs can: C^{1,α} → C^{0,α} → C^{2,α} ⊂ C^{1,α}.
  - **F3: correct.** Axial or tree gauges put the field on the crossing links.
  - The header (l.12, "Three failure modes are established") overclaims, since F2 is argued. Write "BNA-F1 and F3
    established, F2 argued (scaling count)".
- **RTARGET §32 l.562: "the pre-stated acceptable partial outcome is met" is an overclaim.** §27's acceptable partial
  outcome requires "a precisely stated linear estimate, with every non-linear, algebraic and gauge-fixing step proven
  with explicit constants". Here:
  - (R♯) is a non-linear step left as a hypothesis;
  - (FP♯) is a gauge-fixing step left as a hypothesis, and mis-stated (fix 1);
  - (G♯)'s norms are unstated (fix 2).
  - Correct to: "partially met: the algebraic and fixed-point steps (NA-alg, NA-crit, NA-inv, NA-IFT) are proven;
    (G♯), (R♯) and the combined (FP♯) are hypotheses, and (G♯)'s norms are still to be fixed".
- **SU(N) N2 analogues (l.2957-2966).** These are conditional, not counted, and stated in the D-norm, not as curvature
  statements. That respects §28's "not success" clause. The localisation is "argued only" (honest).

### (NA) gap (l.2857-2873): OPEN, honestly recorded. One substantive question for session 15

- NA-F2 is derived for "one direct S4' step" with n = L^k contours: the defect line traces cost ε^{-1} = n.
- But the SU(N) chain of §27 has per-level kernels (κ_i, one-level Q_root, n = L per level). There, each level's
  defect involves level-i contours of length L, and the trace loss is a fixed factor L.
- IT-line already shows that composite averaging removes line concentration.
- **Before (R1)/(R2), check whether NA-F2 survives in the per-level (composite) kernel setting** that N4's
  fluctuation step actually uses. If it does not, the (NA) gap becomes a multi-level covariant PG^{(k)} with
  O(|f|·L) perturbations, which is uniform in k.
- State explicitly which object N4's fluctuation operator is: direct n = L^k kernel, or the chain's per-level kernels.

## (4) Checks

Setup: laptop, nice 10, OPENBLAS/OMP/MKL/vecLib threads = 1, PYTHONDONTWRITEBYTECODE = 1 (nothing written into
checks/), sequential runs, no `timeout`. Outputs are in `rev1314/`.

| Check | Result | Time | Peak RSS | vs stored |
|---|---|---|---|---|
| c28 A | VALID, all PASS | 2.2 s | 167 MB | identical except timing/RSS |
| c28 B | FAIL (β/b_* float tie at x = 0, n = 27) | 4.7 s | 98 MB | identical |
| c28 C | C1, C2 PASS; C3, C4 FAIL | 22.8 s | 747 MB | identical |
| c28 D | PASS (D4 ratio 1e-4) | 2.4 s | 99 MB | identical |
| c29 A | PASS (A1 1.05e-12, A3 1.06e-12) | 3.3 s | 487 MB | identical except RSS |
| c29 B | PASS | 4.8 s | 100 MB | identical except timing |
| c29 B, tolerances removed (`notol/`) | PASS, identical numbers | 4 s | 0.09 GB | n/a |
| c29 C | VALID; C1 FAIL (D(0.1) = 0.1101, slope 1.041); C-V2, C2-V, C2a, C2b PASS | 1637 s | 1.05 GB | identical except timing/RSS (load 2.2, 47% free at start) |
| c29 D | PASS (1.86e-15; 3.7e-8 vs 1.9e-2) | 96 s | 390 MB | identical except timing |

**Provenance (UTC, transcripts).**
- **Session 13.**
  - c28 criteria at 16:50:57, tidied at 16:51:10; the addendum at 16:52:45.
  - The script at 16:54:23. Runs 16:55:05-16:56:27.
  - The S13 derivations were inserted into PROOF at 17:00:48, after the runs, as in earlier sessions.
- **Session 14.**
  - Scratch probes 17:23-17:30 (disclosed).
  - RTARGET §27-31 at 17:32:39; c29 criteria at 17:39:00; the script at 17:41:52.
  - Runs from 17:42:55; the PROOF insertions at 17:51 and 18:15.
- Targets preceded derivations and scripts in both sessions. Pre-registration is weakened (honestly disclosed) by the
  lead's prior exploratory reasoning and, in session 13, by η_* being computed before the criteria.

**c28: CONFIRMED.**
- B's failure is a genuine float tie at a sharp point: -5.6e-16. It is recorded, and the criterion is not edited.
- C3/C4 fail because the window is pre-asymptotic. The post-run fits are labelled informational (fix the quoted
  ranges, §1).
- C1 is a weak criterion (any positive rate passes). Label it as a consistency check only.

**c29: CONFIRMED-WITH-FIX (procedure).**
- The criteria file says "a float tie at a sharp point counts as a FAIL". The script then added, pre-run:
  - a 1e-12 relative tolerance on Re φ(z) - φ(x) ≤ 0;
  - three "|Im| > 1e-15" masks.
  This was disclosed in c29_time.txt, but it contradicts the criterion text.
- I removed all four: Part B still PASSES with identical numbers. So the tolerances were not load-bearing. In future,
  amend the criteria file (addendum) rather than the script alone.
- c29 runs without `-I`, although the criteria name `python3 -I` (disclosed; the script reads no downloaded files).
- C1's failure (D(0.1) = 0.110 > 0.1, slope 1.04) is honestly recorded. The D(t)/t ≈ 1.09 reading (second-order
  non-linear part) is a fair informational reading.
- C2 has only d ∈ {0, 1, 2} on a 4⁴ torus (d = 2 is the antipode), so "0.78 of its rate" is two-point evidence. It is
  labelled as such.

## (5) Overclaims in the header, the tally and RTARGET

1. **Header l.12 / LOG l.693:** "Three failure modes are established" → "BNA-F1, F3 established; F2 argued".
2. **Header l.22, tally l.4020, LOG l.698:** add "at the Hessian (Gaussian) level" to NA-FP.
3. **Header l.27, l.3005-3007, RTARGET l.568:** valid (η, r_0) pairs, or η rounded down. The same at l.2661 and header
   l.50.
4. **Header l.53, l.639, l.2717-2718, LOG l.667:** "true rate" → "located rate (numerical)".
5. **RTARGET l.562 (§27)** and **l.567 (§29(a))**: as in §2-§3 above.
6. **l.2693-2697:** "What N6 consumes" → ARGUED.
7. **l.634-636, l.79-81:** residues (a), (b).
8. **Imports.** No [S13]/[S14] PROVEN-HERE item uses an IMPORTED-NOT-YET-REVERIFIED premise:
   - N2-exp(') uses LED-dual/LED-symb/LED-unif (PROVEN S12);
   - PG^{(k)} uses PG, L3g(a)-glob and FP-ab;
   - NA-alg cites A1-NA(1) step 1 (PROVEN S6), and I re-derived that step;
   - NA-FP uses FP-ab and the L3g(a)-slice conventions;
   - SRC-id uses J-str and LED-dual.
   No conditional SU(N) corollary is counted.

## Verdict counts

**PROVEN-HERE tally items, sessions 13-14: 5.**
- 1 CONFIRMED: Proposition PG^{(k)} with IT-line.
- 4 CONFIRMED-WITH-FIX:
  - Theorem N2-exp: the periodicity argument, the stated (η, r_0) pairs, "true rate", and N6-consumption labelled
    argued;
  - Lemma NA-alg: the tr ρ = 0 domain;
  - Proposition NA-FP: the Hessian-level scope, the composite linearisation, composite onto-ness;
  - Lemma SRC-id: the f_0 half written out, plus a check.
- Strengthened, not counted: Theorem N2-exp', CONFIRMED-WITH-FIX (stated pairs).
- 0 GAP, 0 WRONG among the counted items.

**Uncounted.**
- NA-IFT: CONFIRMED.
- B-NA-red: CONFIRMED-WITH-FIX as an implication. (FP♯) must be for the combined fixing; (G♯) must be precisely stated.
- RTARGET §32's §27 and §29(a) outcome lines: WRONG as written (overclaims). Fix the wording.

**Corrected tally: 60 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / 24 OPEN (main path)
+ 1 comparison branch.** This is unchanged. Sessions 13-14 are now reviewed.

## Required fixes (binding for session 15)

1. **Residues of R1112.**
   - l.634-636: add "for the levels n ≥ 1".
   - l.79-81: annotate the S12 "non-analytic part" claim as superseded by N2-exp.
2. **N2-exp constants (l.2661, header l.50).** Quote valid (η_*, r_0) pairs (0.0111 at r_0 = 0.57; 0.0077 at 0.37;
   0.0117 at 0.65), or round down. Add the f_0 "≤ 0.15φ" condition to the definition of η_* and to the script.
3. **N2-exp periodicity (l.2670-2672).** Replace the sentence with the periodic-meromorphic plus Riemann-extension
   argument.
4. **N2-exp' constants (l.3005-3007, header l.27, RTARGET l.568).** Valid pairs (0.0385 at r_0 = 0.704; 0.0273 at
   0.375; 0.0307 at 0.909), or 0.0384/0.0273/0.0306. The κ̂ = 16 values likewise.
5. **"True rate" → "located rate (numerical, not proven)"** (l.53, 639, 2717; LOG l.667). Fit ranges: "0.93-0.97" and
   "0.88-0.93" (l.2715-2716).
6. **Corollary N2-exp-b (l.2693-2697).** Label "What N6 consumes" ARGUED. Add the open item: exponential F-kernels for
   the gauge-invariant outputs N6 uses (r is done; F ↦ df_0 is open), or the localisation lemma.
7. **NA-alg (b) (l.2780-2782).** Add ||ρ||_op < 2π/N (or ρ the su(N) log nearest 0), so that tr ρ = 0.
8. **NA-FP scope (header l.22, tally l.4020, LOG l.698).** Write "at the Hessian (Gaussian) level, critical
   background". Composite slice (l.2853-2856): write out the linearised covariance and the composite onto-ness.
9. **SRC-id (l.2897-2899).** Write the two-line f_0 computation (above). Add an f_0-identity check at complex points to
   the next check file.
10. **B-NA-red (l.2928-2933).**
    - Restate (FP♯) for the combined map λ ↦ (Dh(x)τ_xλ, DΓ_gf(x)τ_xλ), and add the Lagrange-multiplier step.
    - Define (X, Y, D, weights, slice) explicitly in (G♯) and (R♯).
11. **Header l.12, LOG l.693:** "BNA-F1, F3 established; F2 argued".
12. **RTARGET §32.**
    - Do not edit l.562 or l.567; append an annotation, as for c21.
    - §27: "acceptable partial outcome partially met: (R♯), (FP♯) open, (G♯)'s norms unfixed".
    - §29(a): "met except background independence of the FP constant".
13. **c29 procedure.** Record in c29_time.txt that the Part B tolerances were not load-bearing (this review's re-run).
    Future tolerances go into a criteria addendum.

## Strategic verdict: the next target

**A precisely stated abelian (G♯) at the trivial background, "(G♯)_0", is first, with the per-level question for (NA)
as a short parallel item. Then the SU(N) (R♯). N5 after; N6 last.**

- **Why (G♯)_0 first.**
  - Both B-NA (through B-NA-red) and the (NA) gap reduce to one missing linear estimate: the gauge-fixed multi-level
    linearised chain on general sources, in a smooth covariant multi-level slice (BNA-F3).
  - At U = 1 this is linear and translation-invariant. It is attackable with exactly the machinery that worked in
    S12-S13:
    - the symbols at K = 0, with SRC-id's screening;
    - strip analyticity for the exponential weights (N2-exp's EXP-strip' technique);
    - for the K ≠ 0 Biot-Savart part, a finite-range decomposition of Δ^{-1}.
  - Schauder (C^{1,α}/C^{0,α}) bounds follow from kernel-derivative bounds, once the kernels are exponential and their
    first differences have the CZ structure.
  - First, write the norms down (fix 10). Without that (G♯) is not a target.
  - The S14 order's "one-level B-NA(1) first" is a fine warm-up with explicit constants. But it does not touch the
    k-uniformity, which is the actual wall.
- **The (NA) gap: first settle the per-level question** (section (3) above).
  - If NA-F2 is an artefact of the direct n = L^k kernel, the gap becomes a covariant PG^{(k)} perturbation with
    O(L|f|) defects, and (R1)/(R2) may be unnecessary.
  - FP_U(V)'s locality and analyticity is an N6/N10-type item. Record it; it is not urgent.
- **(R♯) after (G♯)_0.** It is mostly bookkeeping from NA-alg and BCH once the norms are fixed. But BNA-F2's marginal
  4D count means the C^{1,α} control must be level-uniform, so (R♯) is not free.
- **Not yet.**
  - **N5** (the soft Hessian covariance: ℓ¹ bound, random walk) needs the (NA) gap or (G♯)_0's slice.
  - **N6** needs N5 and a proven exponential gauge-invariant interface (fix 6). Its block size is M ≳ 1.2·10⁴ at the
    proven rate and ≈ 470 at the located rate. A sharper m_* is optional, not urgent.
- **Decision 4 is unaffected.** No finding of sessions 13-14 tells against the soft kernel. The linear response is
  exponential (proven), and the SU(N) obstruction is the standard one for any smooth gauge.
