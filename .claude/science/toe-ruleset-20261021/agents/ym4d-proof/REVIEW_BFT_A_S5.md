# REVIEW_BFT_A_S5: hostile line-by-line review of BFT lane A, session 5 (BFT_A.md §21-§25, BFT_A_LOG session 5, checks/ba5*)

Reviewer: independent session (did not write BFT_A). Date 2026-10-28 (UTC). Files read: REVIEW_BFT_A_S4.md (all);
BFT_A.md l.396-402, l.547-560, l.776-790, l.905-941 (§12.1-12.2 statements), l.1050-1067 (13.7), l.1250-1256 (SPD-H),
l.1284-1290, l.1378-1417 (§18.0-18.1), l.1550-1558 (HX), l.1676-2182 (§21-§25 in full); BFT_A_LOG.md session 5;
checks/ba5_criteria.md, ba5_y.py (all), ba5_out_*.txt, ba5_err_*.txt, ba5_time.txt; BFT_B.md §15 (l.2003-2110) and §17
(l.2356-2440). Only this file was written in the repo. Reviewer scripts and outputs:
`/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revbftA5/`
(rev5_boot.py, run1.sh, run2.sh, run*.log, cmp_out.txt, boot{36,48,60}_out.txt, re_ba5_out_*.txt).

Verdict vocabulary: CONFIRMED / CONFIRMED-WITH-FIX / GAP / WRONG. ARGUED marks reasoning of mine that is not a written
proof. Nothing below counts in PROOF's tally.

## Bottom line

- **Provenance: CONFIRMED, with one misstated order line (fix P1''').** Byte boundaries, birth time, criteria-before-script
  and constants-after-runs all check. §24's "runs < §22" is false: §22 (08:46:05Z) was appended while P4b was running.
- **Shell-count dispute: lane A is right, REVIEW_BFT_A_S4 was wrong.** #{v ∈ Z⁴ : |v|_1 = t} = (8/3)t(t² + 2) (brute
  force, t ≤ 16: 8, 32, 88, ..., 9080, 11008). The original "≤ 3(t + 3)³" was true for every t. S4's T2 premise is
  withdrawn. Its replacement bound 6(t + 1)³ is also true, so nothing changes downstream.
- **T1 (TK, j = 3 extension), T3 (barycentre identity), T4-T7: CONFIRMED** (T1 needs one sentence, fix U1).
- **Lemma PC: CONFIRMED** (one sign slip in the exposition, fix U2). **Lemma DUAL, Lemma LD: CONFIRMED.**
- **Lemma EX: CONFIRMED-WITH-FIX** (a factor L^i dropped in |D^iψ_j|, fix U3; harmless).
- **Theorem Y: CONFIRMED-WITH-FIX.** The decomposition is exact (P2 reproduced). The dipole factor is (k - l + 1). The
  remainder carries no T-logarithm. The bootstrap closes as written.
  - Its contraction needs r/n = L^c astronomically large: c is fixed by L^c ≥ 98304C_j.
  - Reviewer numerics (Part 4): the actual Lemma PC coefficient Σ|G_e| is 4.65, 3.29, 2.39, 2.31 at r/n = 2, 3, 4, 5
    (M = 60). It falls like n/r between r/n = 3 and 4, and is still > 1/2 everywhere it can be reached.
  - So the T-uniform constant exists but is of size exp(O(m'L^c)) through Case B. Fix U4: say so.
- **CO-0R, RH, CO-upR, CO-B: CONFIRMED** (CO-upR with a Campanato-vs-pointwise remark, fix U5).
- **Corollary G♯R: CONFIRMED on the sub-window 0 < α < θ ≤ 1 - α.** This is consistent with the package window and
  contains (¼, ½). At α = θ it is not proven, and the depth factor (k - l + 1) may be real there (ARGUED). Its l = 0 line
  is not a 𝒴^∇ slot statement (fix U6).
- **Corollary HL: CONFIRMED in its stated scope (0 < α ≤ θ; it does not use G♯R).** It avoids (SB) entirely, via the
  carrier class 𝔉_l. That is a real advance over 13.7.
- **"Completes the gauge-invariant half of (H-lin^∇)" (l.2086, l.2168): OVERSTATED (fix U7).** What is complete is the
  gauge-invariant half **for the soft-RG source class** (data + residual-type + soft second-order rows: commutator, BA-6
  residual part, co-closed BCH₂), plus rough level-l currents (G♯R, α < θ), at m = 0 and the trivial background.
  - The level-0 Wilson rows remain OPEN: the BCH divergence-form G_0 = q_p and the plain part j_0 (l.226-227), i.e.
    (G♯_0-lev0) = (LED-src) + G♯_0-plain.
  - So does (G♯-up) for (G)-slot sources at levels ≥ 1.
- **ba5 B1 FAIL: a reach limit, not a counterexample** (Part 4). It also shows that "bootstrap" is an asymptotic statement
  with no finite-size margin.
- **Incident: assessed acceptable, with a protocol breach (pkill) on record** (Part 6).
- **ba5 re-run under the lock: P1, P2, P4a, B1, P4b identical to the stored outputs apart from timing/RSS** (Part 7).

---

# Part 1. Provenance

**Filesystem record** (stat in local EDT, quoted in UTC): BFT_A.md born 05:39:32, modified 08:52:26, size 207093.
ba5_criteria.md born 08:30:35, unchanged since. ba5_y.py born 08:32:34, modified 08:44:00 (the post-hoc fix).
- ba5_out_P1: 08:33:12-08:33:13 (acquisition 1).
- ba5_out_P2: born 08:33:13, rewritten up to 08:45:14.
- P4a: 08:45:14-08:45:32. B1: 08:45:32-08:45:34. P4b: 08:45:34-08:48:52.
- ba5_time.txt: 08:50:02.

**Confirmed.**
1. **Byte boundaries.** The first 164731 bytes end at §20's last line, and §21's separator follows. The first 173466 bytes
   end exactly at §21.4's last line ("…No constant derived in this session appears in them."), and §22's separator
   follows. The birth time is unchanged, so every edit was an append.
2. **Order.** §21 < criteria < script < runs < §23. The criteria contain only tolerances (1e-12, 1e-8), the a-priori
   factor 2, and trend rules. No §23 constant appears in them: I checked for 49152, 98304, 4096, C_EX and C_YR.
3. **Disclosure.** §21 states that the dipole, the PC bootstrap and the LES route were sketched before the append.
   BA5-F1/F2/F3/F6 are marked (c) correctly. F4, F5 and F7 carry weight, and none of them occurred.

**Fix P1'''.**
- §24 l.2093-2094 says "runs (…08:44:11-08:48:52Z) < §22 (08:46:05Z)". This is false: §22 was appended during P4b, and
  after B1 had FAILED (08:45:34Z). It should read "runs P2/P4a/B1 < §22 < end of P4b < §23".
- No §22 content depends on ba5, so nothing else changes.
- As in session 4, every "PROVEN-HERE" heading of §23 and "BA5-F1 does not occur in the proof" were written after the
  B1 FAIL. §24's Reading says so implicitly. Make it explicit.

# Part 2. [RBA4-fix] items (§22)

**P2'': CONFIRMED.**

**T1: CONFIRMED-WITH-FIX (U1).**
- §22 extends Lemma TK to j = 3 differences (a = 2). §18.1's proof wrote only j ≤ 2 (l.1407-1409).
- The argument is symbol-generic: (e^{ip}-1)^jσ is in the class with order a - j, |β| ≤ 11 survives Leibniz on B, and the
  j-sum needs (a - j) + 2 > 0 and a - j < 4. So the extension holds.
- **U1:** add one sentence to §22 T1: "the proof of §18.1 applies verbatim to (e^{ip_e}-1)^jσ".

**T2 (shell count): lane A is right; REVIEW_BFT_A_S4's T2 premise is WRONG and is withdrawn.**
- Brute force over Z⁴ (this review) gives #{|v|_1 = t} = 8, 32, 88, 9080, 11008 at t = 1, 2, 3, 15, 16.
- This equals (8/3)t(t² + 2) = Σ_j 2^jC(4, j)C(t - 1, j - 1). S4's (8/3)t(2t² + 1) gives 48 at t = 2, which is already
  wrong.
- 3(t + 3)³ ≥ (8/3)t(t² + 2) for every t ≥ 1 (lane A's two-line proof checked). So the original (Σ1) was true.
- 6(t + 1)³ is also true. Keeping the adopted replacement is harmless, and 648R⁴ stands either way.
- §22's dated remark is correct and should be marked CONFIRMED by this review.

**T3 (barycentre identity): CONFIRMED.**
- All six monomials re-done by hand. Example, ψ = y_ν²: both sides equal s³(2sY_ν + 2s - 1).
- Bound: the anchor z_0, ℓ¹ radius ≤ 3s, and the discrete Taylor remainder ≤ ½|u|_1²max|D²g| give 9s⁵max|D³ψ| ≤ 18s⁵ ✓.

**T4-T7 and the scope lines: CONFIRMED.** These are faithful transcriptions. T7's thresholding is in ba5_y.tsign.

# Part 3. Theorem Y and its lemmas (§23.1-23.6), line by line

**Lemma PC (l.1874-1892): CONFIRMED.**
- Statement: let e be co-closed, supported in a cube C of side q with q + 1 < M. Then G := 𝒫e is supported in C,
  d*G = e, and Σ|G| ≤ 3qΣ|e|.
- Induction checked:
  - (d*G)_ν for ν ≠ a: e_ν - δ_{z_a,b}W_ν + δ_{z_a,b}W_ν ✓.
  - (d*G)_a: the co-closedness of e gives Σ_{ν≠a}[e_ν(z) - e_ν(z - e_ν)] = e_a(z - e_a) - e_a(z). Summing over t ≤ z_a
    with the leading minus gives e_a(z) ✓.
  - W is co-closed in d - 1 dimensions ✓. In two dimensions W = 0 (a compact co-closed 1D form) ✓.
  - Support ✓. Σ|G_{a·}| ≤ qΣ|e| ✓, giving (d - 1)q = 3q ✓.
  - On the torus, q + 1 < M keeps d* of the lift equal to the torus d*. Some hyperplane misses C, so the flux is 0 ✓.
- **U2 (exposition):** l.1886 writes "the first sum into Σ_{t≤z_a}[e_a(t - 1) - e_a(t)] = e_a(z)". That sum is -e_a(z).
  The leading minus of the first term makes the total e_a(z). Insert the sign.
- Numerics: ba5 P1, and my run of the same construction on LD's e at M ≤ 60. d*G_e = e holds to ≤ 1.1e-15, and
  Σ|G_e|/(qΣ|e|) = 0.04-0.07, far below 3.

**Lemma DUAL: CONFIRMED.**
- Symmetry of Ê on chains with v_k = 0, plus the two criticality identities.
- Gauge independence: j is co-closed, and ⟨δ_q, d·⟩ sees only dx_0.

**Lemma LD: CONFIRMED.**
- On the flat torus, Δ commutes with d and d*, which gives d*dg_0 = d*δ_p - d*G' ✓. χ(p) = 1 ✓.
- The commutator support ✓.
- The shift Y ↦ Y - g, with r_j(g) = 0 for j < k ✓.
- BL-1 (iii) turns -⟨(Q^{(0→k)})^TJ, Z_0⟩ into -⟨J, β⟩ - Σ_i⟨s_i, r_i⟩ ✓.
- ⟨G_e, dZ_0⟩ = ⟨e, Z_0⟩ gives x(e) = ΣG_e(q)Y^q ✓.
- BL-2 (c), (Q^{(0→k)})^TJ = (Q_str^{(0→k)})^TJ on co-closed J: I checked it numerically on LD's J (M = 36, r = 6). Lane A's
  c26 Q^T and my independent straight-tent Q_str^T agree to 3.0e-18 (scale 2.3e-4). So ba5's e is the proof's e.

**Lemma EX: CONFIRMED-WITH-FIX (U3).**
- Near shells: ||Q_strv||_1 ≤ L^{-3l}||v||_1 (since Q^T1 = L^{-3} per step) and ||g^{(j)}||_1 ≤ C'L^j give the sum (3/2)C'_g ✓.
- Far shells, rough case: w ⊥ Q_str^T𝔽A_j ✓. Integrand O(L^{2l}L^{-4j}), on O(L^{4(j-l)}) links, gives O(L^{-2l}) per
  shell. So each scale contributes O(1), and the count of far shells is ≤ k - l + c + 3 ≤ (c + 4)(k - l + 1) ✓.
- **This is the dipole factor (k - l + 1), not a power: BA5-F2 genuinely does not occur.**
- Carrier telescoping ✓. Per (m, j) O(L^{-2l}) ✓, with ≤ (k - l + c + 3)(k - l + 1) pairs ✓.
- The top term j > k is bounded by L^{4c}. That is crude but c is fixed ✓.
- **U3:** l.1925 "|D^iψ_j| ≤ 2·4^iC_φL^{-ij}" misses a factor L^i: the Φ_{L^{j-1}} piece gives L^{-i(j-1)}. Read
  "≤ 2·4^iC_φL^iL^{-ij}". It is absorbed in C_g.
- Case B (r = ∞): J + 2 ≤ k + c + 4 pieces ✓. The remainder u_rem obeys the scale-L^J bounds on the whole torus ✓.

**Theorem Y, Case A (l.1977-2007): CONFIRMED.**
- Step 2:
  - β vs β_str differ by a composite gauge direction ✓.
  - |β_str| ≤ C_βn^{-2}(1 + d)^{-3}: n·(probability average of |g_0| ~ (nd)^{-3}) ✓.
  - Support within 4(L^c + 2) ✓.
  - The units are consistent with Theorem W's coarse-unit D-norm. That consistency is corroborated, not proven, by ba5's
    O(1) values of D.
- Step 3: |D^iG'| ≤ C_Gr^{-4-i} (i ≤ 2) uses D^{≤3}ω^p and D^{≤4}χ, so U1 and §23's C^{3,1} precision are needed and
  present ✓. |J| ≤ n³|j'| ✓.
- Step 4: Lemma DX gives L^{2l}L^{2(k-l)}n^{-2} = 1, with no (k - l) factor ✓. Lemma DB gives (k - l + 1) ≤ (k - l + 1)² ✓.
- **Step 5 (the bootstrap):**
  - Q_str^T𝔽j'(b) is a probability average: total weight Σ_Ys^{-4}N(b, Y)s³ = 1 ✓.
  - It is taken over links within ℓ¹ distance 4(n - 1) ✓. So |e| ≤ 4n·max|Dj'|. Measured: max|e|/(4n·max|Dj'|) =
    0.044-0.062, so the bound is loose by about 16×.
  - Σ|e| ≤ 4(4r)⁴·4nC_jr^{-6} ✓. q ≤ 4r needs r ≥ 3n, n ≥ 3 ✓. q + 1 < M follows from r ≤ M/8 ✓.
  - Σ|G_e| ≤ 49152C_jL^{-c} ✓.
  - 𝒬_R and 𝒬_B are seminorms (sups of absolute linear functionals), so the triangle inequality applies termwise ✓.
  - The sup over all q includes every orientation and position ✓. Finiteness at fixed (k, T) ✓.
  - Absorption ✓.
- **Circularity check (S4's caution):** none. The identity is exact, and the coefficient of 𝒬* is an explicit ℓ¹ norm,
  smaller than ½ by the choice of c. c depends on C_j = C(C_K, C_φ) only, and not on k, T or c ✓.
- **No T-logarithm:** r = L^{k+c} is T-independent. Z' is driven by data and sources inside coarse distance L^c + 4, and
  Theorem W localises it exponentially. J_0 is never put through n²dΔ^{-1} ✓.

**Theorem Y, Case B: CONFIRMED.** T < 8L^c makes everything a finite-torus constant, e^{128m'L^c}.

**Fix U4 (size and meaning of the constants).**
- §23.6/§25 should state that c is fixed by L^c ≥ 98304C_j, with C_j built from C_K and C_φ, both uncomputed.
- So C_YR and C_YB contain e^{O(m'L^c)} and L^{4c}. They are T- and k-uniform, but not small or explicit.
- The bootstrap gives no finite-size margin. At the r/n reachable here, the actual coefficient Σ|G_e| is 2.3-4.6 (Part 4),
  so contraction would fail.
- "BA5-F1 does not occur in the proof" is correct only as an asymptotic statement. Add "for r/n ≥ L^c; not observable at
  r/n ≤ 5".

# Part 3b. CO-0R, RH, CO-upR, G♯R, CO-B, HL (§23.7-23.12)

**CO-0R: CONFIRMED.**
- Sup: DUAL + Y ✓.
- Current: |(Q_str^{(0→k)})^Tr_{k-1}| ≤ n^{-3}|r_{k-1}|, and n^{-3}L^{2(k-l)} ≤ L^{-3l} ✓.
- Hölder:
  - LES on the periodic lift with R = 4max(4, L^l) gives n^{2+α}R^{-α}F_0 ≤ L^{α(k-l)}||f_0|| and
    n^{2+α}R^{1-α}|J_0| ≤ 16(1 + C_r)L^{(2+α)(k-l)}a ✓.
  - For ρ > R/4, use Osc ≤ sup ✓.
- This is exactly S4's requested "Hölder down to ρ_0 near the source". It works because the plain current's sup
  L^{-3l}a enters with R^{1-α}, which balances. BA5-F3 does not occur ✓.

**Lemma RH: CONFIRMED.** Exponent bookkeeping re-done:
- α(k - j) - (k - 1 - i) ≤ -(j - 1 - i) ✓.
- The explicit parts in the two regimes j ≤ l and j > l ✓.
- XB: L^{α(k-j)-t} ≤ L^{-(1-α)t} for t ≥ k - j ✓.

**CO-upR: CONFIRMED-WITH-REMARK (U5).**
- 𝒜 is a translation-covariant probability average, so it is controlled by the pointwise Hölder seminorm [f_0]^∞_α.
- CO-0R bounds the Campanato seminorm. The step needs BL-C (Campanato ⟹ pointwise, with the 2·8^α||f||_∞ term) applied to
  f_0 before 𝒜, not to 𝒜f_0 after.
- **U5:** reorder l.2055-2056 so that BL-C is applied to f_0 first. The constants are unchanged.

**Corollary G♯R: CONFIRMED (0 < α < θ, 1 ≤ l ≤ k - 1).**
- N_l(w) = L^{(2+α+θ)(k-l)}a ✓.
- The ratio is sup_t(t + 1)L^{-(θ-α)t}. At L = 3, θ - α = ¼ it is 1.755 (t = 3) ≤ 1.8 ✓.
- **Window consistency:** the package window is 0 < α ≤ θ ≤ 1 - α. G♯R holds on the sub-window α < θ, which is nonempty
  for every α < ½ and contains the working point (¼, ½). Nothing downstream needs α = θ (I checked l.396-560, l.827-834).
  So the strictness is a narrowing, not a conflict.
- The constant blows up like 1/((θ - α)e·ln L) as θ → α.
- ARGUED: the depth factor is probably real. Each scale L^j in Lemma EX contributes O(1) on a disjoint annulus, and one w
  can align signs on all of them. So G♯-rough at α = θ should be listed as OPEN, possibly false. It should not be listed
  as "not proven by this route".
- **U6:** the l = 0 line "||x(w)||_inv ≤ C(k + 1)L^{(2+α)k}sup|w|" is outside the §12.1 target (1 ≤ l ≤ k - 1). It is
  not a bound in the (P0) slot of 𝒴^∇, so it must not be cited as (G♯_0-lev0) for plain level-0 currents. Say so.

**Theorem CO-B: CONFIRMED.**
- (SPD-H) includes the m = l bound C_0, so R_l/(C_*κL^{-3(k-l)}η²) ∈ 𝔉_l ✓.
- Sup: n²L^{-3(k-l)}L^{-2l} = L^{-(k-l)} ✓.
- Current: C_Jn^{-3}η² ✓.
- LES gives (R/n)^{1-α} ≤ 16L^{-(1-α)(k-l)} ✓.
- Σ_l(k - l + 1)²L^{-(1-α)(k-l)} < ∞ ✓.
- This bypasses 13.7's Gap 2 (SB) entirely. Correct, and the most valuable structural gain of the session.

**Corollary HL: CONFIRMED in scope.** It needs only α ≤ θ (through BL-5 (a) and BL-3), and it does not use G♯R ✓. The rows
are data, residual (BL-5 (a)), commutator (CR-1), BA-6 residual, and co-closed BCH₂ (XB + CO-B) ✓.

**Fix U7 (scope of the "complete" claim; l.2086-2087, l.2168-2169, §25 table).** Replace "With Corollary HX this
completes the gauge-invariant half of (H-lin^∇)" with:

> With Corollary HX this proves the gauge-invariant half of (H-lin^∇) **for the soft-RG source class of Theorem
> H-lin_inv** (data, residual-type sources, commutator rows, BA-6's residual part, co-closed BCH₂ rows), and, via
> Corollary G♯R (α < θ), for rough level-l currents (1 ≤ l ≤ k - 1). This holds at m = 0 and at the trivial background.

**Answer to priority 3: what is still excluded from the full (H-lin^∇) on (𝔐^∇, 𝒴^∇).**

The gauge-invariant half of the m = 0, trivial-background linear estimate is **COMPLETE for the soft-RG source class**
(given the reviewed package and this review's fixes). It is **NOT complete for the full 𝒴^∇ pair.** Still excluded:
1. **Level-0 sources, (G♯_0-lev0) = (LED-src) + G♯_0-plain.**
   - These are the Wilson BCH divergence-form row G_0 = q_p (sup and Hölder) and the Wilson plain part
     (∂q/∂x)^T(dx + q) (l.226-227).
   - Theorem Y does not give them. A sup-normed G_0 = ΣG(q)δ_q needs Σ_q|G(q)|·(response), which grows with the volume.
     The curvature f_0 of x(G_0) is a CZ-type kernel sum, not a pairing with a co-closed current.
2. **(G♯-up):** the (G)-slot divergence-form sources at levels ≥ 1.
3. **(P0) plain level-0 currents in general,** and the smooth parts of plain level-l currents beyond BL-6 (a)'s
   residual-type push-down (not re-checked here).
4. **The non-co-closed BCH₂ remainder** (the nonabelian Feynman part, §3.9).
5. **m > 0.**
   - Theorem Y and CO-0R are unweighted. The weighted (CO-0)_m would need LD/PC with e^{md} weights. This is plausible,
     since all pieces live within O(r) of p. But it is not written, and r = L^{k+c} grows with k, so the weights need care.
6. **Nontrivial backgrounds.**
7. **The gauge-variant (configuration-level) half.**
   - LRL (b) is OPEN and was not attempted.
   - Lane B's S_E (BFT_B §15-17, Corollary EP-LRL(b) and Theorem EP-rec) reduces it to **(Res-Hölder)**: the C^{1,α}
     size N_res of the residuals of responses.
   - Lane A's Lemma RH bounds [R_j]_α through sup|r_i|. It does not bound ||r_i||_{C^{1,α}}, so it does not supply
     (Res-Hölder).
8. **Numerics** reach only k ≤ 2, T ≤ 6, L = 3, κ ≡ 1.

**U8 (§25 FOR OTHER FILES).** "Theorem Y … may serve lane B's (LED-src)-type needs" must be narrowed. Theorem Y bounds
pairings of a single plaquette response with co-closed level-l currents (rough or carrier class). It is not (LED-src) for
general sup-normed level-0 sources (item 1 above).

# Part 4. ba5 B1 FAIL and a larger-r test (priority 4)

**Method.**
- rev5_boot.py is a lean scalar re-implementation: δ_p is in plane (0, 1), so ω, χω and G' are single-plane scalars.
  G' = δ_p - Δ(χΔ^{-1}(δ_p - h)).
- It uses an independent straight-tent Q_str^T and ba5's smoothstep φ. It runs Lemma PC on the zero-padded support box,
  so it reports the **actual bootstrap coefficient Σ|G_e|**, not only the proxy q·Σ|e|.
- **Validation:** at M = 36 it reproduces ba5 B1 to every printed digit (Σ|j'|, Σ|e|, q, q·Σ|e|). Its j' equals
  ba5_y.ld_pieces to 4.5e-16.
- Everything ran under the lock (Part 7). k = 1, n = 3.

| M | r/n | Σ\|j'\| | Σ\|e\| | q·Σ\|e\| | **Σ\|G_e\|** (PC) | max\|e\|/(4n max\|Dj'\|) |
|---|---|---|---|---|---|---|
| 36 | 1, 1.33, 2, 3 | 4.55, 3.75, 4.07, 2.66 | 5.15, 4.30, 4.40, 2.55 | 46.4, 51.5, 66.1, 53.5 | 3.19, 3.19, 4.18, 2.56 | 0.044-0.056 |
| 48 | 2, 3, 4 | 4.35, 3.13, 2.44 | 4.71, 3.06, 1.85 | 70.7, 64.2, 49.9 | 4.50, 3.05, 2.11 | 0.045-0.059 |
| 60 | 2, 3, 4, 5 | 4.49, 3.36, 2.79, 2.05 | 4.86, 3.30, 2.12, 1.67 | 72.8, 69.4, 57.2, 55.1 | **4.65, 3.29, 2.39, 2.31** | 0.045-0.062 |

**Reading (post-hoc reviewer test, no pre-registration weight).**
1. **The mechanism switches on where the theory says it should.**
   - For r/n ≤ 2, Σ|e| ≥ Σ|j'|: the tent average does not resolve a current that is smooth only at scale r ~ n.
     §24 diagnosed this correctly.
   - From r/n = 3 on, Σ|e|/Σ|j'| falls (0.98 → 0.76 → 0.82 at M = 60).
   - Σ|G_e| falls with ratio 0.73 from r/n = 3 to 4, matching the predicted n/r ratio 0.75.
2. **Torus contamination at r = M/4.**
   - At fixed r, Σ|G_e| rises with M (r = 12: 2.11 at M = 48, 2.39 at M = 60). At r/n = 5 = M/(4n) the decrease stalls
     (2.31).
   - The proof's regime r ≤ M/8 is not reached for r/n ≥ 3 at M ≤ 60.
3. **Extrapolation (ARGUED).** Σ|G_e| ≈ K·n/r with K ≈ 10-12 would put the contraction threshold Σ|G_e| ≤ ½ near
   r/n ≈ 20-25, i.e. M ≳ 8r ≈ 500-600. That is far beyond 1 GB (M⁴ doubles).
   - So **B1 FAIL is a reach limit, not evidence against the bootstrap.** It stays FAIL as registered.
   - The proof's crude constant (L^c ≥ 98304C_j) is consistent with this but much more conservative. The measured
     |e|/(4n|Dj'|) ≈ 0.06 alone gives a factor of 16.
4. What B1 does show: **Theorem Y's bootstrap has no finite-size content**, which is fix U4. Any explicit-constant use of
   Theorem Y needs either a better constant or a different treatment of e. One option is to iterate LD on e (e is again a
   smooth-at-scale-r current minus its average) instead of using Lemma PC's crude ℓ¹ bound.

**ba5 P1-P4 trends.** Y1-Y4 are correct as computed and re-run identically. Y1, Y2 and Y4 compare k = 2 at T ≤ 4 against
a factor-2 a-priori tolerance. They cannot distinguish (k - l + 1) from a constant, as §24 itself says. Y3 is a partial
replication of S4.

# Part 5. Theorem-level summary of the shell-count dispute (priority 1)

- REVIEW_BFT_A_S4 T2's ground "(8/3)t(2t² + 1), exceeds 3(t + 3)³ for t ≥ 15" was wrong. The reviewer's formula is not
  the ℓ¹-sphere count in Z⁴.
- Lane A's (8/3)t(t² + 2) is right, verified by brute force at t ≤ 16.
- The original inequality was true. The adopted replacement is true. 648R⁴ is unaffected. No downstream change.

# Part 6. The run incident (priority 5)

**What happened.**
- Acquisition 1 stalled in P2 at r = ∞. CG was driven by a roundoff right-hand side, about 2e-16, with a relative
  tolerance.
- `pkill -f "ba5_y.py P2"` also matched the parent shell's command line, which died before its rmdir.
- The lead checked that no ba5 process remained, then released the lock by one manual rmdir (08:43:52Z).
- Post-hoc fix: at r = ∞, j' := 0 (the exact value of Lemma LD) after printing the roundoff. Then P2 was rerun in
  acquisition 2.

**Assessment.**
- **Lock integrity: OK.** The lock directory was still the lead's own: the shell died holding it, so nobody else could
  have acquired it. One rmdir per acquisition was preserved. Nothing was left running: the stored outputs and the
  P1 → P2 → … timestamps are consistent, and I found no ba5 process at my start.
- **Protocol: BREACH, on record.** pkill is prohibited for exactly this reason: pattern kills reach shells and other
  sessions' processes. The stall should have been ended by killing the specific PID (from `pgrep -f` checked first) or by
  letting maxit expire. The "checked no process left" step is not logged with its command.
  - Fix U9: future runners cap CG on a near-zero right-hand side with an absolute tolerance, kill by PID only, and log
    the ps check.
- **The post-hoc fix is legitimate and disclosed.**
  - It replaces a computed 2.2e-16 by its exact 0. It does not touch any criterion.
  - P2 at r = ∞ then tests only the data-shift part of LD. That is the nontrivial part there, since G' ≡ 0 is an
    algebraic identity, and it is shown to 2.2e-16.
  - P1's stored output comes from the pre-fix script, with the "GB" label. My re-run with the current script matches it
    apart from the label.

# Part 7. Re-run of ba5 under the mandatory lock (priority 6)

**Acquisition A** (smoke test): lock 09:01:36Z (load 6.39, 36% free), released by one rmdir at 09:01:38Z. It ran CMP
(Q^T vs Q_str^T) and the M = 36 probe.

**Acquisition B:** lock 09:03:28Z (load 5.17, 41% free), released by one rmdir at 09:08:17Z.
- Settings: nice 10, OMP/OPENBLAS/MKL/VECLIB threads 1, PYTHONDONTWRITEBYTECODE=1, python3 without -I, no timeout,
  no trap, no pkill.
- Order: ba5 P1, P2, P4a, B1, P4b, then the probes at M = 36, 48, 60.
- **ba5: P1, P2 (P2a, P2b), P4a (Y3, P3, k = 1 Y-values), B1 and P4b are identical to the stored checks/ba5_out_*.txt**
  after stripping the timing/RSS fields (diff). Verdicts: P1, P2a, P2b, P3, Y1-Y4 PASS; B1 FAIL, reproduced.
- Peak RSS (time -l): P1 72 MB, P2 131 MB, P4a 100 MB, B1 733 MB, P4b 686 MB, probes 184/486 MB.
- **Disclosure:** my M = 60 probe peaked at 1034 MB at r = 15, above the 1 GB cap, for about 1 s. Free memory was 41%
  and nothing was affected, but it is a cap breach on my side. M = 60 is the ceiling of this design.
- Afterwards: no ba5/rev5 process left. The lock directory present at my last check belongs to another session's job
  (f13_smoke.py), not to mine. No files were written in checks/ (outputs went to the scratchpad), and no __pycache__.

# Binding fixes

- **P1'''** §24 l.2093-2094: §22 (08:46:05Z) was appended after B1's FAIL and during P4b. State that all §23 PROVEN-HERE
  headings postdate the B1 FAIL.
- **S4-T2 withdrawn:** mark §22's dated remark CONFIRMED. (Σ1)'s original bound was true.
- **U1** §22 T1: one sentence that §18.1's proof covers (e^{ip}-1)^jσ for j = 3.
- **U2** l.1886: sign of the telescoped sum (it is -e_a(z); the leading minus makes the total e_a(z)).
- **U3** l.1925: |D^iψ_j| ≤ 2·4^iC_φL^iL^{-ij}.
- **U4** §23.6/§24/§25:
  - c is fixed by L^c ≥ 98304C_j, so the constants carry e^{O(m'L^c)} and L^{4c};
  - the bootstrap contraction is asymptotic only, and Σ|G_e| = 2.3-4.6 at r/n ≤ 5 (this review, Part 4);
  - "BA5-F1 does not occur" holds for r/n ≥ L^c.
- **U5** §23.9: apply BL-C (Campanato → pointwise Hölder) to f_0 before averaging.
- **U6** §23.10: the l = 0 line is outside the §12.1 target and is not a (P0)/(G♯_0-lev0) bound. Record G♯-rough at α = θ
  as OPEN (possibly false: the depth factor).
- **U7** l.2086-2087, l.2168-2169, §25: "complete gauge-invariant half of (H-lin^∇)" is restricted to the soft-RG source
  class (+ rough currents, α < θ). List items 1-7 of Part 3b as OPEN.
- **U8** §25 FOR OTHER FILES: Theorem Y is not (LED-src).
- **U9** run protocol: no pkill; kill by PID; absolute CG tolerance on near-zero right-hand sides; log the ps check.

# Strategic verdict

- **Session 5 is a genuine advance.** S4's recommended next step (the curvature wall (CO-0)/(CO-up) via a
  localized-source dual response) has been carried out correctly, at m = 0 and at the trivial background.
  - Theorem Y combines three pieces: the cut-off dipole, giving the factor (k - l + 1); the localized remainder through
    Theorem W, with no T-log; and the PC bootstrap.
  - Theorem Y is correct as an existence statement for k-, T-uniform constants.
  - CO-B removes 13.7's (SB) gap outright.
  - **Verdict:** the gauge-invariant m = 0, trivial-background linear estimate is **complete for the soft-RG source class
    (Theorem H-lin_inv, co-closed BCH₂) and for rough level-l currents at α < θ**, subject to these fixes. It is not
    complete for the full (𝔐^∇, 𝒴^∇) estimate.
- **Weak points.**
  1. The constants are non-explicit and astronomically large (U4). The bootstrap has no visible margin at any reachable
     size.
  2. The (k - l + 1) dipole factor forces α < θ.
- **The live walls are now:**
  1. **(G♯_0-lev0)**: the level-0 Wilson rows (q_p divergence form, plain j_0), and with it (G♯-up).
  2. **(Res-Hölder)**: with lane B's S_E, this is now the whole gauge-variant half.
  3. **The non-co-closed BCH₂ / Feynman part.**
  4. **m > 0 and nontrivial background.**
- **Recommended next session:**
  1. Weighted Theorem Y and CO-0R (m > 0). LD/PC are local, but r = L^{k+c} grows with k, so weight the dipole shells
     rather than the cut-off.
  2. (Res-Hölder) for the data map, lane B's single remaining input for LRL (b). Lemma RH's termwise structure is the
     natural start: it needs C^{1,α} rather than sup control of the r_i.
  3. Optional: replace Lemma PC's ℓ¹ bootstrap by iterating LD on e, to get a usable constant.
