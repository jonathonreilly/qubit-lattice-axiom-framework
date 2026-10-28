# REVIEW_BFT_A_S6: hostile line-by-line review of BFT lane A, session 6 (BFT_A.md §26-§30, BFT_A_LOG session 6, checks/ba6*)

Reviewer: independent session (did not write BFT_A). Date 2026-10-28 (UTC). Files read: REVIEW_BFT_A_S5.md (all);
BFT_A.md l.200-235 (§3.9), l.258-300 (§3.11), l.525-566 (BL-6, BL-7), l.684-720 (8.7), l.815-842 ([RBA2-fix] B3-B5),
l.925-945 (TS, W, LR-pot, FP), l.1060-1068, l.1148-1160 (13.13), l.1688-1757 (§21.0-21.3), l.2185-2728 (§26-§30 in full);
BFT_A_LOG.md session 6; PROOF.md l.3418-3475 (LES-div, (G♯_0-fine)); checks/ba6_criteria.md, ba6_w0.py (all),
ba6_out_{A,K}.txt, ba6_err_A.txt, ba6_time.txt; BFT_B.md §18-§20 (l.2446-2815). Only this file was written in the repo.
Reviewer scripts and outputs:
`/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revbftA6/`
(run.sh, rev6_diag.py, time.log, re_ba6_out_{A,K}.txt, re_ba6_err_{A,K}.txt, diag_K1.txt, diag_K2.txt).

Verdict vocabulary: CONFIRMED / CONFIRMED-WITH-FIX / GAP / WRONG. ARGUED marks reasoning of mine that is not a written
proof. Nothing below counts in PROOF's tally.

## Bottom line

- **Provenance: CONFIRMED,** with one undisclosed forward reference (fix P6-1): pre-stated §26.3 (l.2271) cites "the
  sharpened condition of §27 (U4')", which did not yet exist at 09:30:07Z.
- **RBA5 fixes P1''', S4-T2, U1-U9: all applied faithfully.** The support-side correction q ≤ 2(r + 2) + 8n + 1 and
  **U4' (L^c ≥ max(260, 3476C_j)): CONFIRMED** (arithmetic re-done).
- **Lemma CS, TOPD, LE: CONFIRMED.** Lemma LE is the standard L^∞ → BMO bound for an order-0 Calderón-Zygmund kernel. It
  is correct and is the genuinely new idea that closes PROOF's (LED-src) at m = 0.
- **Theorem YH: CONFIRMED.** **Theorem W0: CONFIRMED.** **Corollary WR (a): CONFIRMED-WITH-FIX** (a hypothesis must be
  named). **Theorem GU: CONFIRMED** (0 < α < θ; the sup part needs only θ > 0). **Corollary LIN0: CONFIRMED in its stated
  scope** (BL-7's pair, level-wise co-closed sources, m = 0, trivial background, 0 < α < θ < 1).
- **Lemma FG, Lemma BOG, Proposition NC: CONFIRMED. Corollary NC: CONFIRMED-WITH-FIX** (no-wrap condition on small tori
  at the top levels, fix P6-4; the wording about V_l needs one precision, fix P6-5).
- **(NC-Γ): OPEN, correctly. Lane B's elliptic slice S_E does not settle it.** It removes the ambiguity about which Γ is
  meant and makes the problem local and gauge-invariant (Part 4, exact reformulation). It does not remove the level sum.
- **m > 0:** Lemma BW, the 𝒩_m part of Theorem Y_m, the weighted plain-current sup bound and the weighted top residual are
  all **CONFIRMED** for 0 ≤ m ≤ m_Y. m_Y is astronomically small. §26.3's Corollary Y_m is narrowed (fix P6-7). The
  remaining weighted work is modest, about one session (Part 5), if the weighted Hölder parts go through a local equation
  for F rather than Lemma LE.
- **ba6 re-run under the lock: A and K are identical to the stored outputs apart from timing/RSS.**
  - A reviewer extension at k = 1, T = 6, 8, 10 shows U_H saturating: 10.14, 10.53, 10.65. The coarse-shell sums decay by
    a factor of about 0.33 per coarse shell.
  - So T-uniformity at k = 1 is now *observed* (post-hoc, no weight). k-uniformity is still untested (k ≤ 2).
- **Completeness verdict for (H-lin^∇) at m = 0, trivial background (Part 7):**
  - It is NOT "complete except (NC-Γ)".
  - Even granting lane B's unreviewed session 6, it is complete only on the following scope: for **level-wise co-closed
    sources** of 𝒴^∇ and the soft-RG rows, for **T ≥ 5**, for **0 < α < θ**, with **non-explicit constants**.
  - Open besides (NC-Γ): T = 1-4 for the configuration half, and the non-co-closed parts of every row (that is (NC-Γ)
    itself).

---

# Part 1. Provenance (priority 1)

**Filesystem record** (stat in local EDT, quoted in UTC):
- BFT_A.md: born 05:39:32, modified 09:40:30, size 256215. ba6_criteria.md: 09:30:35.
- ba6_w0.py: born 09:31:37, modified 09:31:57.
- ba6_out_A: 09:32:18-09:32:40. ba6_out_K: 09:32:40-09:33:50. ba6_time.txt: 09:33:50.

**Confirmed.**
1. **Byte boundary.** The first 218296 bytes end exactly at §26.5's last line ("…No constant derived in this session
   appears in them."), at l.2299. The first 207093 bytes end at §25's last line. Birth time unchanged, so every edit was
   an append.
2. **Criteria.** `grep -cE '3476|1738|260|6952|1296|10⁴|192|C_E|C_YH|4\.2' ba6_criteria.md` = 0. The criteria hold only
   tolerances, the factor 2 and trend rules.
3. **Order.** §26 < criteria < script (one pre-run fix) < runs < §28. §27 was appended during part K. Nothing in §27
   depends on ba6: U4' is pure arithmetic on §23.6.
4. **After the runs.** All PROVEN-HERE headings and constants of §28 were written after the runs, and §29 says so (l.2631).
   The run protocol (one acquisition, one rmdir, no pkill, ps check logged with its command) matches U9.

**Fix P6-1 (disclosure).**
- §26.3 l.2271 (pre-stated, 09:30:07Z) refers to "the sharpened condition of §27 (U4')". It also fixes
  m_Y = ln 2/(16L^c) and Σ|G_e| ≤ ¼ in a form that presupposes the U4' sharpening.
- So U4' was conceived before the §26 append, but §26's disclosure list (l.2192-2195) does not mention it. Add it.
- Nothing is invalidated: U4' is elementary and checked below.

# Part 2. [RBA5-fix] items (§27)

- **P1''' (l.2308-2312): CONFIRMED.** The timeline is now correct, and the statement "all §23 headings postdate the B1
  FAIL" is explicit.
- **S4-T2, U1, U2, U3, U5, U6, U7, U8: CONFIRMED.**
  - Each is a faithful transcription of REVIEW_BFT_A_S5's text.
  - U2: the "first sum" now reads -(-e_a(z)) = e_a(z) ✓.
- **U4 (l.2330-2338): CONFIRMED.**
- **U9 (l.2378-2381): CONFIRMED.**
  - ba6 keeps ba5_y.cg's relative tolerance. That is defensible, because every ba6 right-hand side is an O(1) source.
  - The logged CG residuals (≤ 1e-12) and the re-run agree.

**Support-side correction (l.2339-2341): CONFIRMED.**
- e = d*G' - (Q_str^{(0→k)})^TJ. The tent average reads links within ℓ¹ distance 4(n - 1).
- A single coordinate can therefore move by 4(n - 1) in either direction, and the cube side grows by 8(n - 1), not 4n.
- So q ≤ 2(r + 2) + 1 + 8(n - 1) ≤ 2r + 8n + 5. For r = L^cn with L^c ≥ 9: 2r + 8n + 5 ≤ 4r ⇔ 8n + 5 ≤ 2r, true for
  n ≥ 3 ✓.
- §23.6's numbers stand.

**U4' (l.2343-2349): CONFIRMED.**
- Σ|e| ≤ (links in the cube) · sup|e| = 4q⁴ · 4nC_jr^{-6}. Σ|G_e| ≤ 3qΣ|e| = 48q⁵nC_jr^{-6} = 48(q/r)⁵C_jL^{-c} ✓.
- With q = 4r this reproduces 49152 ✓.
- L^c ≥ 260 ⇒ r ≥ 260n ⇒ 8n + 5 ≤ 13n ≤ 0.05r (n ≥ 3) ⇒ q ≤ 2.05r. Then (2.05)⁵ = 36.2 and 48 · 36.2 = 1738 ✓.
- ½ needs L^c ≥ 3476C_j ✓. ¼ needs L^c ≥ 6952C_j ✓.
- A factor of 28 in L^c is real but cosmetic: U4's reading ("astronomical, asymptotic only") stands, and §27 says so.

# Part 3. Step 2 (§28.1-28.8), line by line (priority 2)

**Lemma CS (28.1, l.2401-2407): CONFIRMED.**
- d*d* = 0 ✓. There are 3 nonzero μ ≠ ν terms, so sup|d*G| ≤ 6sup|G| ✓.
- Q_str sum: for the μ-term, the y_μ-sum over the s consecutive values in the block telescopes to the two boundary values
  of G_{μν} ✓. The remaining s³ (other y) × s (t) = s⁴ terms cancel s^{-4} ✓.
- "Own units of level m" means raw values: a constant c maps to sc. So the content is that a divergence does not grow
  under straight averaging, which is exactly 𝔉_l's second clause (l.1698) ✓.
- Remark (no fix): ba6 E4 uses random G (0.04-0.32). An adversarial G alternating at block faces would approach 2 per μ.
  The bound 6 is rigorous either way.

**Lemma TOPD (28.2): CONFIRMED.** It uses the symmetry of Ê and the two criticality identities. The source-free reading of
Y^{(b)} is Lemma TS (l.925) ✓.

**Lemma LE (28.3, l.2414-2425): CONFIRMED.**
- *Kernel bound.* K = ∇d*Δ_0^{-1} is defined on non-exact F_1 through d*F_1, which has mean zero. Equivalently, the symbol
  ν_aν̄_μ/ψ is bounded and is set to 0 at p = 0.
- *Near part.* Cauchy-Schwarz gives |Σ_μν̄_μĤ_{μν}|² ≤ ψΣ_μ|Ĥ_{μν}|². Then Σ_a|ν_a|²|B̂_ν|² ≤ Σ_μ|Ĥ_{μν}|², and the
  sum over ν counts each plane twice ⇒ ||KH||_2² ≤ 2||H||_2² ✓.
  - 2 · 6 · (2n)⁴ = 192n⁴ ✓.
- *Far part.* For w ∈ Q (|w - x|_∞ ≤ n/8) and y ∉ Q*: |w - y|_∞ ≥ (7/8)|y - x|_∞ ✓.
  - The ℓ¹ diameter of Q_{n/4} is n ✓.
  - #{|z|_∞ = t} = 64t³ + 16t ≤ 216t³ ✓. Σ_{t≥n}t^{-2} ≤ 2/n for n ≥ 2 ✓.
  - n · 6 · (8/7)⁵ · 216 · 2/n · C_K = 2592 · 1.95 · C_K ≈ 5.1·10³C_K ≤ 10⁴C_K ✓.
  - |DK| ≤ C_K(1 + |z|)^{-5} is TK with T1 (j = 3, a = 2), confirmed in REVIEW_BFT_A_S5 Part 2 ✓.
- *Normalisation.* E_∇ = n^{-4}Σ_Q|n²(·)|² = Σ_Q|·|² = PROOF's ψ(n/4). So W0's "n^{-4}ψ(n/4) = n^{-4}E_∇" (l.2484) is
  consistent ✓.
- *Reading.* This is the classical "CZ maps L^∞ to BMO". It is the right way around PROOF's G0-F2 (l.3460: Π_ex is not
  bounded on ℓ^∞). The Hölder norm of the source is spent once, in the sup bound (YH). The local energy is then charged to
  the *output* sup, not to the source.

**Theorem YH (28.4, l.2427-2463): CONFIRMED** (given Theorem W, Corollary FP, Lemma LD/PC, §23.6 steps 2-4, all reviewed).
- *Seminorms and invariance* ✓. The bootstrap triangle inequality ✓. 𝒬_H only sees dY_0.
- *Step 1 (constant subtraction).*
  - dg_0 is exact on the torus and Ḡ is constant, so ⟨Ḡ, dg_0⟩ = ⟨d*Ḡ, g_0⟩ = 0 ✓.
  - |G^c - Ḡ| ≤ (d/n)^α for d ≤ n and ≤ 2 beyond ✓. The t = 0 shell contributes 0 ✓.
  - n^{-α}Σ_{t≤n}t^{α-1} ≤ 1 + 1/α ✓. The far sum to r + 2 is ≤ c ln L + 1 ✓.
  - **BA6-F1 does not occur** ✓.
  - The kernel bound |dg_0| ≤ C_d(1 + |z - p|)^{-4} (dd*(χω) has two derivatives on ω ~ |z|^{-2}; Leibniz with U3's χ
    bounds) ✓. The numerical value of C_d was not re-derived. It is harmless.
- *Step 2.* Σ|dZ'_0| = n^{-2}Σ|f_0(Z')| with |f_0(Z')| ≤ C_Z(c)n^{-2}e^{-m'd} on 6n⁴ plaquettes per cell ⇒ 6C_Z(c)S(m') ✓.
- *Step 3.* ||g_0||_1 ≤ 864C_0'(r + 2) ≤ 1728C_0'L^cn ✓.
- *Step 4.*
  - Composite-gauge invariance of 𝒩 ✓. Corollary FP's coarse bound times "own = coarse/n" times 4n⁴ links per cell gives
    O(n) ✓.
  - C_FP(m') matches 13.13's e^{20m}(1083G_D + 40, 1083G_R) ✓. FP needs T ≥ 3, which Case A has ✓.
- *Case B.* r = ∞, so every bound carries the torus size through ln(4L^c) and (8L^c)⁴. These are finite and
  T-independent because T < 8L^c ✓.
  - **Periodic lift for T ≤ 2:** CONFIRMED. P(lift) - lift = Ξλ with ev^{(k)}λ a single constant (FG (i)). A shift of a
    root is a root, so λ(z + Tne_ν) - λ(z) = 0 and λ is T-periodic ✓.
- **Reading for ba6 (important).** Every reachable size is in Case B (T < 8L^c, with L^c ≥ 3476C_j). There the theorem's
  own bound grows like ln T until T ~ L^c. So **ba6 cannot test YH's uniformity at all.** It can only test that nothing
  grows faster. See Part 6 for what the k = 1 extension shows.

**Theorem W0 (28.5, l.2465-2494): CONFIRMED.**
- Step 1 (duality) ✓. Step 2: ⟨j_0, dλ⟩ = ⟨d*j_0, λ⟩ = 0 ✓. n² · n^{-3}||j^c|| · C_YNn = C_YN||j^c|| ✓. BL-C conversion ✓.
- *Step 3.*
  - No sources at levels ≥ 1 ⇒ κ_ir_i = κ_{k-1}(Q^{(i+1→k)})^Tr_{k-1}. This is lane B's Lemma RT (c) with G = j = s = 0
    (BFT_B l.2488) ✓.
  - TOPD: sup|G_0| · Σ|dy_0| = n^{-2}||G^c|| · 6n²G_DS/κ_- ✓. 𝒩(Y^{(b)}) ≤ 4n³(…) ✓.
  - The weights L^{2(k-1-i)}|r_i| ≤ κ̂L^{-(k-1-i)}sup|r_{k-1}| are summable ✓.
- *Step 4.*
  - dB = F because F is exact on the torus. ΔB = d*F = d*G_0 + j_0 - κ_{k-1}(Q_str^{(0→k)})^Tr_{k-1} ✓, which is
    LES-div's form componentwise. LES-div is used with R = n at every centre (dated precision 2) ✓.
  - Coarse conversion:
    - n^{2+α} · n^{-α} · n^{-2}E_∇^{1/2} ≤ C_E||f_0||_∞ ✓;
    - n^{2+α}[G_0]_{α;fine} = [G^c_0]_α ✓;
    - n^{2+α} · n^{1-α} · sup|h| = n³sup|h| ≤ ||j^c_0|| + κ_+sup|r_{k-1}| ✓.
  - The n < 16 branch is crude but correct (Osc_2 ≤ sup and ρ_c ≥ 1/n) ✓.
  - **This is exactly (LED-src) of PROOF l.3449-3451 at m = 0, together with the coarse-box mean (sup part).**
- Step 5 (U5 order; Lemma RH with k - 1 - i ≥ k - j) ✓.
- *Scope remark (no fix).* "Every 0 < α < 1" is right for W0 alone. Downstream it is used only inside the package window.

**Corollary WR (28.6, l.2496-2508): (a) CONFIRMED-WITH-FIX; (b) CONFIRMED as a decomposition.**
- (a) Φ is analytic with Φ(0) = 0 and DΦ(0) = 0 ⇒ |Φ(a) - Φ(a')| ≤ C_q max(|a|, |a'|)|a - a'|_∞ ✓.
  - |x_0(b + v) - x_0(b)| ≤ |v|_1n^{-2}||∇^cx^c_0||_∞ ✓. n² · C_q(η/n)(4δη/n) = 4C_qη²δ ✓, and δ ≤ δ^α ✓.
  - **Fix P6-2:** the proof uses ||∇^cx^c_0||_∞ ≤ η and max|x_0| ≤ η/n ≤ 1/20 (link values ≤ 1/20) at the configuration's
    own gauge representative. State both as the hypothesis "||x||_𝔐^∇ ≤ η ≤ η_0, with 𝔐^∇ containing ||∇^cx^c_0||_∞",
    citing the clause of 𝔐^∇ (§3.9 table, l.222).
  - This replaces §3.9's ARGUED algebra-property row (l.224) for the Hölder of q_p: update that row's status by a
    pointer.
- (b) σ ≤ 3C_qη²n^{-3} (η ≤ 1/9) ✓. A link lies in 6 plaquettes ✓. NC with (q_R, N_R) = (2, 6) ✓. The size of the
  co-closed part is 18C_NCC_qη² ✓. The no-wrap condition needs Tn ≥ 5 (fix P6-4).

**Theorem GU (28.7, l.2510-2531): CONFIRMED.**
- Step 2: n² · 6L^{-2(k-l)}||G^c|| · C_YB(k - l + 1)²L^{-2l} = 6C_YB(k - l + 1)²||G^c|| ✓.
- Step 3:
  - Top: sup|G_l| · Σ|dy_l| ≤ L^{-2(k-l)} · 6L^{4(k-l)}L^{-2(k-l)}G_DS/κ_- = 6G_DS/κ_- ✓. This uses Proposition W's f_l
    bound at level l, which is in ||·||_inv ✓.
  - The level-(l - 1) jump by d*G_l and the weights ✓.
- Step 4 (R = 4max(4, L^l)):
  - n^{2+α}R^{1-α} · 6L^{-3l}L^{-2(k-l)} = 6 · 4^{1-α}L^{α(k-l)} ≤ 24L^{α(k-l)} for L^l ≥ 4, and ≤ 96L^{α(k-l)} when
    R = 16 ✓;
  - (R/n)^{1-α} ≤ 16L^{-(1-α)(k-l)} ✓.
- Step 5 and the l-sum Σ_t(t + 1)²L^{-(θ-α)t} < ∞ ⇔ α < θ ✓.
- The sup part needs only θ > 0 ✓.
- Consistent with the S5 window remark: (G♯-up) at α = θ is not proven here and should be listed with G♯-rough at α = θ
  as OPEN.
- **Fix P6-3 (FOR OTHER FILES l.2723):** "its sup part is Theorem GU (2)" understates the result. GU step 4 also gives the
  Hölder part, so (G♯_0-fine-up) at m = 0, trivial background, α < θ is GU (2) + (4).

**Corollary LIN0 (28.8, l.2533-2544): CONFIRMED in its stated scope.**
- The superposition is linear. Each slot is covered:
  - data + (R): BL-5 (a), α ≤ θ;
  - (G) at level 0: W0 (needs [G^c_0]_α, which is in ||G||_Y per BL-7 (d));
  - (G) at levels ≥ 1: GU;
  - (P0): W0;
  - (Pl-c): BL-6 (a) ⇒ residual sources + one level-0 current. That current is co-closed because d*Q^T = ev^Td*
    (BFT_B l.2580), and of size ||j||_{Pc}/(L^θ - 1). Then W0;
  - rough currents: G♯R.
- "This is BL-7 (d)'s open statement for the gauge-invariant outputs" ✓.
- Precision (fix P6-5, part): "level-wise co-closed" is strictly narrower than "composite-co-closed" (Ξ^TS = 0, Lemma FG
  (iii)). LIN0 does not cover sources that are only composite-co-closed. They arise exactly from (NC-Γ) (Part 4).

# Part 4. Step 3 (§28.9-28.12) and (NC-Γ) (priority 3)

**Lemma FG (28.9): CONFIRMED.**
- (i): dx_0 = 0 ⇒ x_0 = dλ + h. x_k = 0 ⇒ h = 0 and ev^{(k)}λ constant ✓.
- (ii): ⟨Y^p_Γ, Hx⟩ = ⟨Y^p_Γ, S⟩ - ⟨ΓY^p_Γ, Γx⟩ and ΓY^p_Γ = 0 ✓.
- (iii): ⟨ΓΞλ, Γx⟩ = ⟨Ξλ, S⟩ - ⟨HΞλ, x⟩ = 0, and Γx ∈ Ran Γ ⇒ Γx = 0 ✓.
- (iv) ✓.

**Lemma BOG (28.10): CONFIRMED.**
- d = 1 ✓. The inductive step: v_a(z - e_a) - v_a(z) = u - Uδ_{z_a,b} ✓. The transverse construction on the slice ✓.
  Σ|v| ≤ 4qΣ|u| ✓.
- Moment identity: Σ_zz_ν(d*y)(z) = Σ_zy_ν(z) ✓, valid in the cover / without wrap.

**Proposition NC (28.11): CONFIRMED.**
- d*R'_c = 0, and its totals vanish (moment identity), so Lemma PC applies ✓.
- Σ|W_c| ≤ 3q(1 + 8q)4q⁴σ ✓. The overlap count is 4N_R(2q + 1)⁴ ✓ ⇒ C_NC = 48N_R(2q + 1)⁴q⁵(1 + 8q) ✓.
- BA6-F7 does not occur ✓.

**Corollary NC (28.12): CONFIRMED-WITH-FIX.**
- The BCH₂ piece sizes match lane B's independent count: own |r_l||x_l| ~ L²L^{-3(k-l)}η², i.e. π_l ≤ 2C_B'κ_+L²η²
  (BFT_B l.2615-2616) ✓.
- ||W^c_l|| ≤ CL^{-(k-l)}η² ⇒ GU gives (k - l + 1)²L^{-(1-α)(k-l)}η², which is summable ✓.
- **Fix P6-4 (no-wrap on small tori).**
  - BOG, PC and the moment identity need the piece cube (side q = q_R + 1, about 5L + 2 at level l for the BCH₂ rows) to
    satisfy q + 1 < M_l = TL^{k-l}.
  - At l = k - 1 this fails for T ≤ 5 (and at l = 0 for the Wilson row when Tn < 5).
  - Repair (elementary): build each piece's W_c, v_c in the cover Z⁴, where the pieces are defined by local formulas, and
    push forward by periodisation. Periodisation commutes with d* and preserves locality. The sup bounds pick up at most
    (1 + q/M_l)⁴ ≤ (1 + q)⁴.
  - Alternatively, state Corollary NC for T ≥ 6. Either way, say it.
- **Fix P6-5 (wording, l.2588-2590, l.2708).** V_l is not "the non-co-closed part" of R_l. V_l = Σ_c𝔅d*R_c is a local
  1-form with d*V_l = d*R_l, and it also carries co-closed content.
  - The precise statement (reviewer, PROVEN below) is that **the Γ-dependence of every output enters only through the
    composite divergence Ξ^TV = Σ_lev^{(l)T}d*R_l**.

**Exact reformulation of (NC-Γ) (reviewer; PROVEN, linear algebra, using only Lemma FG's hypotheses on Γ).**
- *(a) Direct sum.* Chain space = (Ran Ξ)^⊥ ⊕ Ran Γ^T.
  - Dimensions: rank Γ = dim Ran Γ = dim Λ_0/const = dim Ran Ξ.
  - Intersection: Γ^Tμ ⊥ Ran Ξ ⇒ μ ⊥ ΓΞΛ_0 = Ran Γ ⇒ Γ^Tμ = 0.
  - Hence every source splits uniquely as **S = S^Γ_0 + Γ^Tμ**, with S^Γ_0 composite-co-closed and
    μ = (ΓΞ)^{-T}Ξ^TS.
- *(b) Feynman form 𝓛_Γ = H + Γ^TΓ.*
  - 𝓛_ΓΞλ = Γ^T(ΓΞλ). Choosing λ := (ΓΞ)^{-1}μ_{Ran Γ} gives 𝓛_Γ^{-1}Γ^Tμ = Ξλ, a pure composite gauge direction.
  - With FG (iii): **x_Γ(S) = x_LIN(S^Γ_0) + Ξλ**.
- *(c) Hard slice Ker Γ.*
  - Criticality gives Hx - S ∈ Ran Γ^T, hence Hx - S^Γ_0 ∈ Ran Γ^T ∩ (Ran Ξ)^⊥ = 0.
  - So **Hx = S^Γ_0**, i.e. x is the slice representative of x_LIN(S^Γ_0).
- *Consequence.*
  - (NC-Γ) ⟺ the gauge-invariant bound sup_p|⟨S^Γ_0(V), Y^p⟩| (any representative of Y^p), where
    **S^Γ_0(V) = V - Γ^T(ΓΞ)^{-T}Ξ^TV**.
  - In both gauge-fixing styles, Γ enters only through the correction driven by Ξ^TV.
  - The configuration outputs differ by the explicit gauge direction Ξ(ΓΞ)^{-1}μ.

**Does lane B's S_E settle (NC-Γ)? NO.** It helps in three ways and leaves the hard part.
1. **It fixes the target.**
   - §26.2 l.2263 states (NC-Γ) "for the gauge fixing of B-NA-red" (a per-level Feynman slice).
   - Lane B proves the configuration half in its hard elliptic slice S_E (BFT_B l.2801: "(W-lin-Π) for S_E ⟺ (H-lin^∇)
     in the best gauge").
   - By (a)-(c) the two give *different* gauge-invariant outputs on non-composite-co-closed sources, because the
     corrections Γ^T(ΓΞ)^{-T} differ.
   - **Binding (P6-6):** state (NC-Γ) for Γ = Γ_E (lane B's slice), or prove the transfer between the two slices. The
     lanes must use one Γ.
2. **It makes the problem local.** Π_E has range 4 (BFT_B l.2536). The correction Γ_E^T(Γ_EΞ)^{-T} is box-local (box
   Neumann problems glued by tents), so S^{Γ_E}_0(V) is a local, composite-co-closed source of the same size as V (ARGUED:
   locality of (Γ_EΞ)^{-T} is read off the construction, not written).
3. **Lane B's machinery does not touch V.**
   - Lemma RT (a)-(c) and Theorem RH assume d*j_l = 0 at every level (Setting RH, BFT_B l.2453). bb6 A5 shows the funnel
     term is O(1) off co-closed forms (l.2587).
   - **Consistency flag (for lane B's owner):** Corollary RH-inv's BCH₂ clause (l.2615-2616) is valid for lane A's
     co-closed completions d*W_l, not for the raw rows.
- **The hard part remains.**
  - S^{Γ_E}_0(V) is composite-co-closed, not level-wise co-closed. Its exact BL-1 (ii) push-down gives residual sources
    (fine) plus one co-closed level-0 current Σ_l(Q^{(0→l)})^TV_l of coarse size O(η²) *per level*. That is the
    level-count loss Ω = k already identified in [RBA2-fix] B3 (l.819-824) and in lane A's Remark 1 (l.2592).
  - So (NC-Γ) needs a cancellation: either smooth-part decay of V_l (Remark 1) or smallness of the composite divergence
    Ξ^TV (Remark 2, l.2595-2598).
  - Remark 2's identity Ξ^T(rows) = -K_x^T∇𝔉_k(x) is the natural lever. With (a)-(c), at a critical point the Γ-correction
    vanishes identically. Along the contraction it is bilinear in x and ∇𝔉_k. That is a statement for (H-rem^∇), not for
    (H-lin^∇).
  - **Recommendation:** move the non-co-closed parts into (H-rem^∇) through this identity, rather than bounding
    𝓛_Γ^{-1}V_l level by level.

# Part 5. Step 4: m > 0 (§28.13) (priority 4)

**Lemma BW: CONFIRMED.**
- supp G_e lies in a cube of side ≤ 2.05r about p. The coarse ℓ¹ cell distance is ≤ 4(1.025L^c + 1) ≤ 4.2L^c (true for
  L^c ≥ 50) ✓.
- ¼e^{4.2mL^c} ≤ ½ ⇔ m ≤ ln 2/(4.2L^c) ⊇ [0, m_Y] ✓.
- Note: the weighted bootstrap uses its own c (L^c ≥ 6952C_j). That is harmless.

**Theorem Y_m, 𝒩_m part: CONFIRMED.**
- 𝒩_m(Y^q; p) ≤ e^{md(q,p)}𝒩_m(Y^q; q) (triangle inequality) ✓. ||e^{md}g_0||_1 ✓.
- Corollary FP at m' ≥ 2m gives S(m' - m) ✓. Case B's factor e^{32mL^c} ≤ 4 for m ≤ m_Y ✓.
- **Consequence:**
  - e^{md(p,X_0)} ≤ e^{md(b,X_0)}e^{md(b,p)} ⇒ ||f_0||_{∞,m} ≤ C_YN(m)||j^c_0||_{∞,m} ✓;
  - the weighted top residual through Proposition W at m' ≥ 2m ✓ (sketched, "by the same argument", but it is the same
    two lines).

**Fix P6-7 (scope of §26.3 Corollary Y_m, l.2276-2277).**
- Pre-stated: "the sup parts of CO-0R, CO-B, W0 and GU hold in ||·||_{∞,m}". Proven: only the plain-current part of W0's
  sup and the weighted top residual. The G_0 part of W0's sup needs 𝒬_{H,m}, which is ARGUED.
- §30's row l.2686 says this correctly. Add one dated line at §28.13 that Corollary Y_m is proven only in that part.

**"Weighted LE is false for the global Coulomb potential" (l.2620-2622): CONFIRMED as ARGUED, and probably true.**
- A localised exact F with nonzero moments gives ∇B ~ |z|^{-4}, so the oscillation on a far box is ~ (n/R)⁵.
- That is a power, which no exponential weight can absorb.

**How much work remains for m > 0 (reviewer estimate; ARGUED).**
1. **𝒬_{H,m}: about half a page.**
   - Use a Lipschitz weight, e.g. e^{m|z - p|_1/n} at the fine scale. It is equivalent to the cell weight up to e^{4m}.
   - In step 1, G - Ḡ splits into e^{mφ}(H - H(z_p)) + (e^{mφ} - 1)H(z_p). The second term costs
     Σ_{t≤r}t^{-1}·mt/n ≲ mL^c ≤ ln 2 on [0, m_Y].
2. **DX_m, DB_m: mechanical, 1-2 pages.** DX and DB pair against Φ_{m'}-weighted objects. Test currents of growth e^{md}
   shift m' to m' - m. All of Theorem Y's explicit pieces live within L^c coarse units of p, so the weights cost
   e^{4.2mL^c} ≤ 2.
3. **Weighted Hölder parts: one new local lemma instead of Lemma LE.**
   - Since dF = 0, ΔF = dd*F = d(d*G_0 + h): a **local** double-divergence equation for the curvature itself. Under the
     same equation one has F_{μν} = ∂_μ(Σ_a∂^-_aG_{aν} + h_ν) - (μ ↔ ν).
   - The lattice Campanato step for Δu = ∂∂g + ∂h ("LES-dd"):
     - take w := Δ^{-1}∂∂((g - ḡ)1_{Q_r}) + Δ^{-1}∂(h1_{Q_r}) on the whole lattice. Its L² bound follows from the
       bounded symbols ν_aν̄_b/ψ;
     - v := u - w is harmonic in Q_r and has u-level decay (ρ/r)⁶;
     - the iteration lemma gives [F]_α on a box from sup_{box}|F| + [G^c_0]_α + n³sup|h|.
   - This is entirely box-local, so the weighted Hölder parts of W0, CO-0R, GU and CO-upR cost only e^{O(m)}. It is also
     an alternative proof of W0 step 4 at m = 0. It is about the length of LES-div.
- **Total:** roughly one session. **The real cost is m_Y**, which is ~ ln 2/(16L^c) with L^c ≥ 6952C_j. It is uniform,
  but it is meaningful only if every downstream use needs merely *some* uniform m > 0. Check that against the package's
  (H-rem^∇) and the BFT-1 decay statement before investing.
  - Decoupling m from L^c needs a better bootstrap, e.g. iterating LD on e as REVIEW_BFT_A_S5 suggested.

# Part 6. ba6 and its re-run under the lock (priority 5)

**Script review (ba6_w0.py).**
- U_H is a rigorous upper bound of 𝒬_H(Y^p). dY^p_0 is exact, so the constant subtraction holds exactly, and the weight
  (d/n)^α / 2 is the step-1 bound ✓.
- D_N is a valid lower bound of 𝒩(Y^p)/n (|⟨j*, Y + dλ⟩| ≤ max|j*|𝒩, since j* is co-closed) ✓.
- The LE ratio uses B = d*Δ^{-1}F ✓, but at k = 1 the box has side 2 (n/4 < 1). LE1 is therefore a very weak test: the
  maximising box is next to p at every T, which explains the constant 0.1203.
- E4 uses the direct straight average matching 28.1 ✓, with random rather than adversarial G.

**Re-run.**
- One acquisition: lock 09:48:54Z (load 2.10, 44% free), released by one rmdir at 09:51:23Z.
- Settings: nice 10, OMP/OPENBLAS/MKL/VECLIB threads 1, PYTHONDONTWRITEBYTECODE=1, python3 without -I, no timeout, no
  trap, no pkill.
- Afterwards: `pgrep -fl 'ba6_w0|rev6_diag'` → none; no __pycache__ in checks/; the lock directory was absent.
- Outputs went to the scratchpad only.

| job | peak RSS | result |
|---|---|---|
| ba6 A | 112 MB | **identical** to checks/ba6_out_A.txt after stripping timing/RSS (diff) |
| ba6 K | 714 MB | **identical** to checks/ba6_out_K.txt after stripping timing/RSS; all verdicts PASS reproduced |
| diag K1 (k = 1, T = 6, 8, 10) | 477 MB | see below |
| diag K2 (k = 2, T = 4, shell profile) | 538 MB | see below |

**Reviewer extension (post-hoc, no pre-registration weight).**

| k, T | U_H | S1 | D_N | coarse-shell sums S_t of \|dY^p_0\| (t = ℓ^∞ cell distance 0, 1, 2, …) |
|---|---|---|---|---|
| 1, 6 | 10.137 | 10.071 | 0.455 | 6.745, 2.508, 0.746, 0.073 |
| 1, 8 | 10.526 | 10.266 | 0.430 | 6.745, 2.507, 0.741, 0.248, 0.025 |
| 1, 10 | 10.654 | 10.330 | 0.429 | 6.745, 2.507, 0.741, 0.245, 0.084, 0.008 |
| 2, 4 | 11.064 | 13.260 | - | 11.26, 1.94, 0.061 |

**Reading.**
1. At k = 1 the far field is exponentially screened. S_{t+1}/S_t = 0.37, 0.30, 0.33, 0.34: a rate of about 1.1 per coarse
   unit, and the last shell is a torus-wrap artefact. U_H's increments shrink like 0.39, 0.13.
   - **U_H converges in T, to ≈ 10.7.** This is the T-uniformity that ba6's H1 (concavity only) could not show.
   - It is stronger than YH's Case B bound, which allows ln T.
   - D_N is flat at 0.43.
2. From k = 1 to k = 2, all the growth of S1 sits in the t = 0 cell (6.75 → 11.26). That is the near-field log n which the
   Hölder weight removes: U_H(2, 4) = 11.06 against U_H(1, ∞) ≈ 10.7.
   - This is consistent with YH (BA6-F1 absent in the data too), but k ≤ 2 cannot distinguish a k-uniform bound from slow
     growth. §29's scope statement stands.
3. Peak 755 MB (ba6 K) / 714 MB (re-run) at k = 2, T = 4. That is the ceiling of this design, as §29 says.

# Part 7. Exact completeness verdict: (H-lin^∇) at m = 0, trivial background

(H-lin^∇) (§3.9 l.207) is ||𝓛^{-1}||_{𝒴^∇→𝔐^∇} ≤ G together with the data map. 𝔐^∇ has a gauge-invariant half
(||·||_inv) and a configuration half (C^{1,α} potentials in a slice).

**PROVEN, given the reviewed package, REVIEW_BFT_A_S5's and this review's fixes** (constants k-, T-uniform, not explicit,
astronomically large through L^c; window 0 < α < θ < 1, θ ≤ 1 - α where the F3 slot enters):
1. **Gauge-invariant half, for every level-wise co-closed source of 𝒴^∇ and every T ≥ 1:**
   - data + (R) (BL-4, BL-5);
   - (G) at level 0, with [G^c_0]_α (W0);
   - (G) at levels ≥ 1, sup-only, with the ω_l weight (GU);
   - (P0) (W0);
   - (Pl-c) (BL-6 (a) + W0);
   - rough currents in the F3 weight (G♯R);
   - the soft-RG rows: commutator, BA-6 residual part and co-closed BCH₂ rows (HL/CO-B);
   - the Wilson BCH row (WR (a), with P6-2);
   - the co-closed completions d*W_l of the BCH₂ rows and the Wilson plain row (Corollary NC, with P6-4).
2. **Residual-gradient part** (C^{1,α} of residuals): lane B's Theorem RH / Corollary RH-inv, from item 1. It is
   consistent with lane A: W0's and GU's residuals are lane B's Lemma RT (c), and "(P0) j_0 and G_0 do not enter" matches
   W0 step 3. **Lane B session 6 is unreviewed.**

**Conditional on lane B's unreviewed session 6:**

3. **Configuration half in S_E: only for T ≥ 5** (Corollary LRL(b)-E, BFT_B l.2510-2512, l.2643-2648). It covers the same
   source class as item 1, through (W-lin-Π) ⟸ (H-inv) (RH-inv + EP-lin).

**NOT proven:**
- (i) **(NC-Γ)**: the composite-divergence content of the non-co-closed parts of the BCH₂ rows and the Wilson plain row.
  Exactly: the gauge-invariant response to S^{Γ}_0(V) of Part 4, a composite-co-closed but not level-wise co-closed
  source, for the one Γ fixed by P6-6.
- (ii) **T = 1-4 for the configuration half** (lane B: "T = 3, 4 not covered"; T ≤ 2 not addressed).
- (iii) **the endpoint α = θ** (G♯-rough and (G♯-up) OPEN there, possibly false).
- (iv) explicit or non-astronomical constants.

So the claim "(H-lin^∇) at m = 0, trivial background is complete except (NC-Γ)" is **too strong**. The correct statement:

> At m = 0 and the trivial background, the gauge-invariant half of (H-lin^∇) holds for all level-wise co-closed sources
> of 𝒴^∇ and all T ≥ 1 (lane A, sessions 5-6, reviewed). Its residual-gradient part and its configuration half in S_E
> follow for T ≥ 5 (lane B session 6, unreviewed). The only source content not covered is the composite-divergence part
> of the non-co-closed rows ((NC-Γ), to be stated in lane B's slice). Small tori T ≤ 4 are not covered for the
> configuration half.

# Binding fixes

- **P6-1** §26 disclosure (l.2190-2195): add that U4' (and the ¼-contraction form used for m_Y) was conceived before the
  §26 append, which forward-references §27 at l.2271.
- **P6-2** 28.6 (a): name the hypotheses ||∇^cx^c_0||_∞ ≤ η (the 𝔐^∇ clause) and link values ≤ 1/20 in the gauge of the
  configuration. Point §3.9's table row "Hölder: … ARGUED" (l.224) to WR (a).
- **P6-3** §30 FOR OTHER FILES l.2723: (G♯_0-fine-up) at m = 0, α < θ, is GU steps 2 and 4 (sup and Hölder), not only the
  sup part. Record (G♯-up) at α = θ as OPEN.
- **P6-4** BOG / PC / NC / Corollary NC / WR (b): the no-wrap condition q + 1 < M_l fails at the top levels for T ≤ 5. Do
  the constructions in the cover and push forward (sup factor ≤ (1 + q)⁴), or restrict to T ≥ 6. State which.
- **P6-5** 28.12 l.2588-2590 and §30 l.2708:
  - V_l is a local 1-form with d*V_l = d*R_l, not "the non-co-closed part". The Γ-dependence of the outputs is exactly
    through Ξ^TV (Part 4 (a)-(c)).
  - LIN0 covers level-wise, not composite, co-closed sources.
- **P6-6** §26.2 l.2263, §30 l.2685: state (NC-Γ) for Γ = Γ_E (lane B's S_E), or prove the transfer from B-NA-red's
  Feynman slice. Record the reformulation (NC-Γ) ⟺ the gauge-invariant bound for S^Γ_0(V) = V - Γ^T(ΓΞ)^{-T}Ξ^TV.
- **P6-7** §28.13: Corollary Y_m (§26.3) is proven only for the plain-current part of W0's sup and the top residual. The
  remaining parts are ARGUED (𝒬_{H,m}) or OPEN (DX_m, DB_m, weighted Hölder).
- **For lane B's owner (not binding on lane A):** Corollary RH-inv's BCH₂ clause (BFT_B l.2615-2616) holds for the
  co-closed completions d*W_l. Lemma RT needs level-wise co-closed sources.

# Strategic verdict

- **Session 6 is a substantial and correct advance.** Both walls named by REVIEW_BFT_A_S5, (G♯_0-lev0) (with (LED-src))
  and (G♯-up), are proven at m = 0 and the trivial background.
  - The two key ideas are both right:
    - pairing the plaquette response against Hölder sources *after subtracting the constant*;
    - bounding the local energy by the output sup (L^∞ → BMO, Lemma LE).
  - The plain-current ℓ¹-modulo-gauge bootstrap reuses Theorem Y's machinery soundly.
  - Corollary LIN0 is the gauge-invariant half of (H-lin^∇) on BL-7's whole pair.
- **What it is not:**
  - The constants are existence-only and astronomically large (U4/U4').
  - The data probe k ≤ 2 cannot confirm k-uniformity. My T-extension does confirm T-uniformity at k = 1.
- **Live walls, in order:**
  1. **(NC-Γ)**, best attacked as an (H-rem^∇) statement through Remark 2's identity Ξ^T(rows) = -K_x^T∇𝔉_k. By Part 4
     the Γ-correction vanishes at critical points. First fix one Γ (P6-6).
  2. **Small tori T ≤ 4** for the configuration half (lane B).
  3. **m > 0**: about a session of mostly mechanical work if the weighted Hölder parts use a local LES-dd step for F
     instead of Lemma LE. First confirm that a uniform but astronomically small m suffices downstream.
  4. Nontrivial backgrounds.
- **Recommended next session (lane A):**
  - (a) P6-4 and P6-6 (short).
  - (b) The Part 4 reformulation written into BFT_A, plus a proof attempt that the rows' composite divergence is bilinear
    and small along the contraction (Remark 2), moving (NC-Γ) into (H-rem^∇).
  - (c) If time: 𝒬_{H,m} with a Lipschitz weight, and LES-dd.
- **Review lane B's session 6 before** citing the T ≥ 5 configuration half as established.
