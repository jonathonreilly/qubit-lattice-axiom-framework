# REVIEW_BFT_A_S3: hostile line-by-line review of BFT lane A, session 3 (BFT_A.md §11-§15, BFT_A_LOG session 3, checks/ba3_*)

Reviewer: independent session (did not write BFT_A). Date 2026-10-28 (UTC). Files read: REVIEW_BFT_A_S2.md (all);
BFT_A.md l.18-47, l.437-575 (definitions, §7), l.797-1222 (§11-§15 in full); BFT_A_LOG.md (all); LINEAR_PACKAGE.md
l.137-200, l.360-384 (Lemmas 2.4, 2.5, 3.1, 3.2/3.2'/3.2'', 3.4-3.8, 6.6-6.8); PROOF_session16_snapshot.md l.1961-1963 (LES
box convention); checks/ba3_criteria.md, ba3_rough.py, ba3_out.txt, ba3_time.txt; checks/c26_led.py l.26-128 and
checks/ba2_lin.py l.24-100 (chain code). Only this file was written in the repo; rerun outputs and the reviewer probe are
in the session scratchpad
(`/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revbftA3/`).

Verdict vocabulary: CONFIRMED / CONFIRMED-WITH-FIX / GAP / WRONG. ARGUED marks reasoning of mine that is not a written
proof. Nothing below is counted in PROOF's tally.

## Bottom line

- **Provenance: file order CONFIRMED (three byte boundaries); epistemic pre-statement NOT established, again.** §12's
  BR-2 (iii) already asserts the BA3-F4 outcome. The ba3 criteria (06:33:50Z) already carry the final §13 constants (75,
  155, 8, 40, C_Λ = 10). So the §13 proofs existed before the script ran. That is good for "not fitted to ba3". It is bad
  for "pre-stated failure modes": BA3-F1..F7 carry no pre-registration weight (fix P1').
- **Lemma RS, BR-1, BR-2 (i)-(iii): CONFIRMED** (I re-derived each identity and exponent). The exact rough reduction is
  right, and BA3-F4 (||J^c|| = ||w^c|| exactly) is right. "(G♯-rough) ⟺ the response to the level-0 images" is CONFIRMED.
- **CR-1: CONFIRMED, exact.** The commutator row is the residual-type source (κ_l/2)[x_{l+1}, r_l(x)], up to the E_src
  sign convention. Its (R) size is κ_+L^θL^{-(1-θ)(k-1-l)}η², and BL-5 (a) covers it **componentwise** in an orthonormal
  basis of su(N) (fix B3').
- **SPD: CONFIRMED as a bound on the carrier Q_str^{(l→m)}R^B_l** (every count and exponent re-derived; C_SPD = 20472p_L²/L
  stands). It is **not** (W2): the §15 table's "Proposition SPD (W2) … PROVEN" overclaims. (W2) = SPD + (SB) (fix B2').
  My probe P1 confirms SPD's carrier formula (tent U, pairing identity) to machine precision. The cancellation step itself
  is not numerically testable without nonabelian S4' code; it rests on F6/BA-4 (reviewed earlier).
- **(RP) in sup form: expected FALSE (CZ logarithm), and not needed.** For the X_s part of (G♯-rough) the walls merge:
  route (B) closes with a single-level lattice Coulomb-Schauder estimate, LRL (a) below, and needs no primitive at all.
  The same LRL (a), with SPD, gives the X_s response to the BCH₂ rows **without (SB) and without (G♯-rough)** (ARGUED,
  Part 6).
- **LR-grad as stated (§12.2 l.940-941) is FALSE** for general configurations. A rough exact residual r_{j-1} = dψ forces
  [∇^cx^c]_α ≳ L^{α(k-j)}||x||_inv in every gauge. It must be restated for the data map (LRL (b)).
- **Step 3 (TS, W, Λ, LR-pot, FP): CONFIRMED** (C_Λ = 10 k-free; LR-pot constants 75/155/8/40/775/205; FP 1083).
  Proposition W is CONFIRMED given the package, with crude e^{O(m)} bookkeeping.
- **ba3 rerun (lock 07:02:25-07:02:46Z): byte-identical** to checks/ba3_out.txt apart from timing, all PASS.
- **Reviewer probe:**
  - P1 (SPD/BR-2 tent formula) PASS at 6e-14;
  - P2 shows Q_str does not preserve co-closedness (ratio 0.18-0.28), so the rough potential is non-local;
  - P3 shows a designed rough current's Hodge primitive ratio growing 1.16 → 1.47 from side 6 to 12: consistent with a
    logarithm, but inconclusive.

---

# Part 1. Provenance audit

**Filesystem record (TZ=UTC stat, birth | modification | size), taken during this review, after 06:42:28Z and before my runs:**

| file | born | modified | size |
|---|---|---|---|
| BFT_A.md | 05:39:32 | 06:42:14 | 121185 |
| BFT_A_LOG.md | 04:56:48 | 06:42:28 | 8392 |
| checks/ba3_criteria.md | 06:33:50 | 06:33:50 | 3809 |
| checks/ba3_rough.py | 06:35:30 | 06:35:30 | 10102 |
| checks/ba3_out.txt | 06:36:20 | 06:36:35 | 2414 |
| checks/ba3_time.txt | 06:36:20 | 06:36:35 | 882 |

**Confirmed.**
1. **Byte boundaries.**
   - `head -c 79088` ends with §10's last FOR-OTHER-FILES line, and byte 79089 starts "\n---\n\n# 11.". This is session 2's final size.
   - `head -c 85494` ends with §11's last paragraph (8.6 consequence scope), and byte 85495 starts "\n---\n\n# 12.".
   - `head -c 93716` ends with BA3-F7, and byte 93717 starts "\n---\n\n# 13.".
   - All three sizes are the ones the log records.
   - The birth time is still 05:39:32Z, so there was no Write/Edit-tool rewrite in session 3. That is consistent with
     "shell >> only". A truncating `cat >` cannot be excluded, but nothing in the content suggests one.
2. **ba3 ordering.** Criteria (06:33:50) < script (06:35:30) < outputs (06:36:20) < §13 (log 06:41:13; the file was
   last modified at 06:42:14). The criteria file was never modified after birth. ba3_time.txt matches the log (lock
   06:36:20Z, load 2.38, 35% free, 14.82 s, 725 MB). No `__pycache__` in checks/ (checked).
3. **The §11 heading time.** "≈06:35" is wrong, and the log discloses it (the true time is 06:30:57Z). Confirmed by the
   85494 boundary.

**Not established.**
1. **§12 records outcomes.**
   - BR-2 (iii) (l.910) states "no bound ||J^c||_∞ ≤ C·N uniform in k holds on R_l". That *is* BA3-F4's outcome.
   - The same section then lists BA3-F4 as a failure mode "stated before the proofs are written" (l.943-946).
   - The criteria file (06:33:50) contains R4's bound 10 and R5c's 75||f_0|| + 8max|Λ| and 155/8/40. These are exactly the
     §13.11-13.12 constants, while §12 only says "C_Λ depending only on L" and "c_0, C_1, C_2, C_3 depending only on L".
   - So the proofs of Λ and LR-pot existed by 06:33:50, before §13 was appended. The log's "exploratory reasoning (not
     recorded) preceded §12" is accurate but understated: the reasoning included finished proofs with constants.
   - Positive side: the constants were fixed **before** ba3 ran, so §13 is not fitted to ba3.
2. **"≈06:43 UTC" on the 13.4 correction (l.1161)** postdates the file's last modification (06:42:14Z). It is a heading
   estimate error of the same kind as §11's, harmless.

**Provenance verdict: ACCEPTABLE WITH RELABELLING (binding fix P1').** The ba3 pre-registration is real for the checks.
§12's file-order priority over §13 is real. "Failure modes (stated before the proofs are written …)" must read "stated
after the outcomes (and §13's constants) were known; not pre-registered".

---

# Part 2. §11 [RBA2-fix]: CONFIRMED

- P1, B1, B2, B3, B4, B5, B6, B8, B9 and the 8.6 scope note are applied as REVIEW_BFT_A_S2 asked, by appended notes.
- **B7 CONFIRMED independently.** PROOF_session16_snapshot l.1961-1963 defines Osc_2(F; Q_ρ(x)) with the prefactor
  ρ^{-4} = 1/|Q_ρ|, so Q_ρ is the box of side ρ, and LES needs side R ≥ 16. The factor 4 and C_L(α) stand.

---

# Part 3. Step 2 lemmas (§13.1-13.4)

**Lemma RS (l.957-963): CONFIRMED.**
- C_l = R_l ⊕ S_l is finite-dimensional orthogonal complement.
- "w ∈ R_l ⟺ Q_lw ∈ Ran d": ⟨w, Q^Tv⟩ = ⟨Qw, v⟩ for v ∈ C_{l+1}, and C_{l+1}^⊥ = Ran d.
- Constants lie in S_l because Q^T(ce_μ) = L^{-3}ce_μ on co-closed inputs.

**Lemma BR-1 (l.965-977): CONFIRMED, exact.** I re-derived it.
- Q_lu_l - u_{l+1} = 0 and Q_mu_m - u_{m+1} = 0, by Q∘d = d∘ev.
- r_{l-1}(x) = r_{l-1}(y) - w/κ.
- The completed square is (κ/2)||r - w/κ||² - ⟨w, y_l + w/κ⟩ = (κ/2)||r||² - ⟨w, r + y_l⟩ + c, and
  r_{l-1}(y) + y_l = Q_{l-1}y_{l-1}.
- The data shift u_k = d ev φ/κ is a level-k gradient. It is removed by a composite gauge with λ_0(c_X) := φ(X)/κ, since
  r_{k-1} changes by Q d ev λ - dψ = 0. So y's outputs are those for data B_k: this is the Lemma 2.5 step, and it holds.
- ba3 R1c tests it with the right data shift (B_2 - Q_1w/κ_0 at k = 2, l = 1).

**Proposition BR-2 (l.979-993): CONFIRMED.**
- (i) The constants check out: |dw| ≤ 4a, coarse factor L^{2(k-l)}, and N = L^{(2+α+θ)(k-l)}a. The residual weight is
  L^{k-l}·L^{k-l}a/κ. The 13.4 correction to 8/κ_- is right.
- (ii) The exponent 1 - (1-θ)(l-i) - α(k-l) is right (I recomputed it). It is ≤ -α(k-l) for l - i ≥ 2 at θ = ½. The sum
  over i is a max, since (R) is a max-norm, so ||s||_R ≤ L^{-α(k-l)}N.
- (iii) The tent formula is right. For a link at offset t, the count from block X is t + 1 and from X - e_μ it is s - 1 - t.
  At t = s - 1 this gives J = s^{-3}w(X), so ||J^c|| = ||w^c|| exactly. Probe P1 confirms the formula and the equality on
  random co-closed inputs (Part 9).
- **BA3-F4 occurs; the reading is right.** No sup-level gain is possible, and any bound must use the fine-scale
  cancellation.

**13.4 (G♯-rough reduced): CONFIRMED.** The reduction runs in both directions:
- x(w) = u + x(J) + x(s), by linearity;
- the reverse direction is ||x(J)|| ≤ ||x(w)|| + explicit terms + G_R||s||_R.

Two points on the routes:
- **Route (A) "(RP) ⇒ X_s part": CONFIRMED as an implication.** Theorem 6.8 (a)-(b) use only sup norms of G_l. But (RP) in
  sup form is expected false (Part 5), so route (A) is the wrong route.
- **Route (B): the right route, and it closes the X_s part without LR-grad's composite slice (Part 6).**

---

# Part 4. CR-1 and SPD (§13.5-13.7)

**CR-1 (l.1010-1022): CONFIRMED, exact.** I redid the algebra.
- DC[u] = -½[u_{l+1}, q] - ½[x_{l+1}, Q_lu_l]. Substitute Q_lu_l = r_l(u) + u_{l+1}. The two u_{l+1} terms combine to
  -½[u_{l+1}, q - x_{l+1}] = -½[u_{l+1}, r].
- ⟨r, [u, r]⟩ = 0 by ad-invariance, and -½⟨r, [x, r_l(u)]⟩ = ½⟨[x, r], r_l(u)⟩.
- Sizes:
  - |x_{l+1}| ≤ L^{-(k-1-l)}η and |r_l| ≤ L^{-2(k-1-l)}η (own units), so |s^C| ≤ κL^{-3(k-1-l)}η². The bound |[a, b]| ≤ 2|a||b|
    is valid for Frobenius norms (√2 suffices).
  - (R) weight: L^{θ(k-l)}L^{2(k-1-l)}|s^C| = κL^θL^{-(1-θ)(k-1-l)}η² ✓.
  - The Lipschitz form follows from bilinearity ✓.
- **Fix B3' (scope, wording only).** E_src carries -⟨s, r⟩, so the source in E_src's convention is -s^C. The sign is
  immaterial for sizes. BL-5 (a) is a one-real-component theorem (Setting LIN): apply it componentwise in an orthonormal
  basis of su(N). At the trivial background the components decouple, and the sup-norm constants pick up at most √(N²-1).
- ba3 R2 tests CR-1 against a *random* matrix Q. That is legitimate, because the identity is linear-algebraic in Q. The
  BCH sign check is correct for log(e^{-a}e^{b}) = b - a - ½[a, b] + O(ε³).

**SPD (l.1024-1048): CONFIRMED as stated (a bound on Q_str^{(l→m)}R^B_l); mislabelled as (W2) in §15.** Line by line:
- **U = (Q_str^{(s)})^Tδ_{(Z,ν)}.** It is a tent in z_ν of peak s·s^{-4}, a box transversally, and zero off ν-links;
  |U| ≤ s^{-3}; slope s^{-4} (including the end steps). Probe P1 checks the formula against the actual S4' chain on
  co-closed inputs (rel ≤ 1e-12, Part 9).
- **Support of B_c.** In the c26 template the go path, the straight leg and the return path have base points in
  [-h, h]⁴ ∪ (Le_μ + [-h, h]⁴). The leg's interior points y + je_μ (j < L) stay in [-h, L + h] ✓. Alignment (L | s) makes
  every ρ ≠ μ range a single level-(l+1) block range. So boundary c need μ ≠ ν and a μ-straddle (2 values of X_μ) ✓.
- **Counts.** 4(2s' + 3)(s' + 2)³ ≤ 540s'⁴ and 3·2·(2s' + 2)(s' + 1)² ≤ 96s'³; both are tight at s' = 1 ✓.
- **Sizes.**
  - Interior terms 1080 + 2700 + 5400 = 9180; the s' ≤ L^{k-l-1} and L^{1-(k-l)} ≤ 1 steps are valid since k - l ≥ 1.
  - Boundary term 1056.
  - Total (9180 + 1056)·2κ = 20472κp_L²/L ✓.
  - The no-cancellation comparison 540s' ✓, so the gain is exactly s' = L^{m-l-1} ✓.
- **Carried current.** L^{3(k-m)}L^{2(m-l)}·L^{-3(k-l)} = L^{-(m-l)} ✓. The normalisation L^{2(m-l)} is the inverse of
  QQ^T on constants (Qc = sc, Q^Tc = s^{-3}c) ✓.
- **Fix B2' (label).** SPD bounds the natural carrier, not the Ran Q^T component of an orthogonal split. §15's row
  "Proposition SPD (W2) … PROVEN-HERE" must read "SPD (the carrier bound) PROVEN-HERE; (W2) ⟸ SPD + (SB), (SB) OPEN"
  (13.7 already says so). Better still, Part 6 shows that (W2)/(SB) are not needed for the X_s output.

**13.7 (H-lin_inv implication): CONFIRMED, with one gap.**
- The weights are right (exponent 1 - (1-θ)(k-i); the double geometric sum (1 - L^{-1})^{-2}; F3 sizes L^{-(k-m)/4}).
- **GAP (B4'): the l = m = 0 piece.** Lemma RS, BR-1 and (G♯-rough) are stated for 1 ≤ l ≤ k - 1. The recursive split of
  R^B_0 starts with a rough part at level 0 (a level-0 current orthogonal to Q_0^T(C_1)). BR-1 has no level -1 to push it
  to, so its response is a (G♯_0-lev0) instance that the implication silently omits. Either extend (G♯-rough) to l = 0
  as a level-0 statement, or list it as a third gap.
- The (SB) diagnosis is right: the orthogonal split's projector involves the Gram inverse and the Hodge projector, which
  are CZ-type operators.

---

# Part 5. BA3-F4, (G♯-rough), (RP) and (SB)

**(G♯-rough) ⟺ the response to J = (Q^{(0→l)})^Tw: CONFIRMED (Part 3).** The real question is the X_s output and the
curvature outputs of x(J), or equivalently of x(w).

**A simplification the file misses (ARGUED, elementary).**
- Below a single rough source at level l, the Euler-Lagrange equations at levels 0 < i < l and at level 0 have no source.
  So r_{i-1} = (κ_i/κ_{i-1})Q_str^Tr_i for i < l, and d*dx_0 = -κ_0Q_str^Tr_0. This is J-str's argument: the source-free
  levels propagate co-closedness.
- At level l: r_{l-1} = (κ_lQ_l^Tr_l - w)/κ_{l-1}. Above l, J-str holds unchanged.
- Hence **every residual of x(w) is a transport of r_{k-1}(x(w)) plus the explicit -w/κ_{l-1} term**, and the whole X_s
  output reduces to the single number field r_{k-1}(x(w)). No sup bound on any primitive g is needed for the lower
  residuals; Theorem 6.8 (b)'s Σ||G_l|| term never enters.

**(RP) in sup form: expected FALSE (CZ logarithm). Reviewer analysis, ARGUED.**
1. Low-momentum structure.
   - On R_l the K = 0 alias of w is O(|p|) times the K ≠ 0 aliases. I confirm the author's count: co-closedness makes
     ŵ_0 ⊥ p, and exactness of Q_strw forces Π_T[Lŵ_0 + Σ_{K≠0}q_K(p)ŵ_K] = 0 with q_K(p) = O(|p|).
   - So the Hodge primitive g = dΔ^{-1}w has a low-momentum symbol p̂_μp̂_ν∂_νq_{K,μ}(0)·(envelope of ŵ_K). That is a
     Riesz-transform pair, homogeneous of degree 0 and direction-dependent.
   - On L^∞ envelopes such an operator is L^∞ → BMO, not L^∞ → L^∞. The loss is up to log(scale ratio) =
     log(TL^{k-l}), which is **T-dependent**.
2. No local primitive can beat this.
   - A bounded primitive g (|g| ≤ Ca own) forces the coarse current at every scale ℓ to be O(a/ℓ).
   - For rough w the coarse current at level m is Q^{(l+1→m)}dφ = d ev φ, where Q_lw = dφ.
   - So bounded primitives exist iff the **rough potential φ has bounded oscillation**.
   - φ = Δ^{-1}D(w) - h_l(w), where D(w) := d*Q_strw is local in w. It vanishes identically only if Q_str maps co-closed
     forms to co-closed ones. My symbol argument says it does not: V = Σ_μ(U_{X,μ} - U_{X-e_μ,μ}) has curl
     ∂_μ∂_ν(ψ_μ - ψ_ν) ≠ 0.
   - **Probe P2 confirms D ≢ 0 (|d*Q_strw|/|Q_strw| = 0.18-0.28; Part 9).**
3. If D ≢ 0, then φ = (degree-0 CZ)(envelopes) is BMO but not bounded, and (RP)-sup fails by the logarithm.
   **(RP)-BMO** (mean oscillation of g^c on boxes of side ≥ ρ_l, ≤ Cρ_l||w^c||_∞) is PLAUSIBLE: the lattice CZ
   L^∞ → BMO bound is uniform in the torus. It would suffice for route (A)'s X_s part, by a BMO version of Theorem 6.8.
   G enters only modulo constants and co-exact 2-forms, and the kernel dB'_l is exponentially decaying with zero mean,
   hence in H¹.
4. **Recommendation: drop route (A).** Route (B) below needs neither (RP) nor BMO.

**(SB): same analytic class (Gram inverse plus Hodge projector, CZ type); also unnecessary for X_s (Part 6).**

---

# Part 6. Do the walls merge? Yes for the X_s outputs: one lemma, LRL. Statement and consequences

**Route (B) closed for X_s modulo LRL (a) (ARGUED, unwritten).**
- By Lemma 6.6 (applied to w = d*g, any primitive; the identity is algebraic), κ_{k-1}r_{k-1}(x(w))(X) = ⟨w, B'_l⟩, with
  B' the source-free response to the data δ_{(X,·)}. The pairing is invariant under B'_l ↦ B'_l + dλ_l for **any** level-l
  function λ_l, not only composite gauges, because d*w = 0.
- So replace B'_l by its level-l Coulomb representative A := d*Δ_l^{-1}f_l(B') + (mean of B'_l). The mean pairs to zero
  with w.
- A is co-closed. Let z ∈ C_{l+1} be its **flux coarse-graining**: s³-normalised face fluxes of A through the coarse faces.
  It is co-closed exactly (flux conservation) and local.
- Then Q_l^Tz = Q_str^Tz ∈ S_l, so ⟨w, Q_l^Tz⟩ = 0.
- Q_str^T(s³·) is a convex combination of neighbouring coarse values (13.3 (iii)'s weights), so
  |A - Q_l^Tz| ≤ C·L·|∇A| locally.
- Count in own units, with |w| = a and |∇A| ≲ L^{-2(k-l)}·(1 + d)^{-5} per coarse cell of L^{4(k-l)} links:
  |r_{k-1}(X)| ≲ aL^{4(k-l)}·L·L^{-2(k-l)} = L·L^{2(k-l)}a = L·L^{-(α+θ)(k-l)}N.
- This is better than the target L^{-α(k-l)}N by L^{1-θ(k-l)}. With Part 5's transport remark, **the X_s part of
  (G♯-rough) follows**.

**SPD + LRL (a) give the X_s response to the BCH₂ rows without (SB) or (G♯-rough) (ARGUED, unwritten).**
- For a co-closed R^B_l (13.7's scope), ⟨R^B_l, B'_l⟩ = ⟨R^B_l, A⟩.
- Telescope with nested flux coarse-grainings z_m of A (all co-closed, so Q^T = Q_str^T and the funnel term drops):
  ⟨R, A⟩ = ⟨R, A - Q_str^Tz_{l+1}⟩ + Σ_{m=l+1}^{k-1}⟨Q_str^{(l→m)}R, z_m - Q_str^Tz_{m+1}⟩ + ⟨Q_str^{(l→k)}R, z_k⟩.
- With SPD (|Q_str^{(l→m)}R| ≤ CκL^{-3(k-l)}η² own), z_m ≈ s_m³A, |∇z_m| ≲ s_m⁴L^{-2(k-l)}, and L^{4(k-m)} level-m links
  per coarse cell, **each term is ≲ L^{1-(k-l)}η², independently of m**. The top term is ≤ CL^{-(k-l)}η² (SPD at m = k).
- Total per row ≲ (k - l)L^{1-(k-l)}η², summable over l: **||r(x(ΣR^B))||_{X_s} ≤ Cη², uniform in k, T.**
- Only the curvature outputs still need more (below).

**The lemma (LRL: weighted lattice Coulomb-Schauder reconstruction).** Fix d = 4, L ≥ 3 odd, α ∈ (0, 1), κ_± and
0 < m' < m_*'. Distances d(·,·) are coarse ℓ¹ torus distances. Campanato seminorms are in coarse units over boxes of side
ρ ∈ [ρ_l, 1], as in §7.2.

- **LRL (a) (single level).** There is C_a = C_a(L, α, m') such that for all k ≥ 1, T ≥ 1, X_0, 0 ≤ l < k and every exact
  level-l 2-form F with Φ_{m'}(F) := sup_z e^{m'd(z,X_0)}(|F^c(z)| + sup_{B∋z}ρ_B^{-α}Osc_2(F^c; B)) < ∞, the Coulomb
  potential A := d*Δ_l^{-1}F on the level-l torus obeys, for every level-l link b,
  **|∇^cA^c(b)| + sup_{B∋b, B⊂B_1(b)}ρ_B^{-α}Osc_2(∇^cA^c; B) ≤ C_a(1 + d(b, X_0))^{-5}Φ_{m'}(F).**
  - The decay exponent 5 uses ∫F = 0 (F exact): Δ^{-1}F ~ |z|^{-3}, d* gives one more power, ∇ another.
  - It is **polynomial, not exponential**. A Coulomb gauge is inadmissible in e^{m d} norms with m > 0, which is why (b)
    needs a local gauge.
  - Input for B': Proposition W / BL-4 (all [f_j]_{α,m'}), proven.
- **LRL (b) (composite slice, the data map).** There are a linear projection P_♯ onto a slice S_♯ and a constant C_b, with
  P_♯ commuting with coarse translations and P_♯x - x a composite gauge direction trivial at level k. C_b =
  C_b(L, α, κ_±, m, m') for 0 ≤ m < m' < m_*'. For all k ≥ 1, T ≥ 3, X_0 and every B_k, the source-free minimiser y(B_k)
  obeys
  **max_j[||(P_♯y)^c_j||_{∞,m} + ||∇^c(P_♯y)^c_j||_{∞,m} + [∇^c(P_♯y)^c_j]_{α,m} + L^{k-1-j}||r^c_j||_{∞,m}] ≤ C_b||B_k||_{D,m}.**
  - Intended construction: S_tent's tents patching box-local Coulomb gauges. The patching error dχ·(λ-differences) is
    bounded by 13.12; the interior C^{1,α} step is LES-div (Lemma 3.2''), plus a box Gaffney inequality. LRL (a) is its
    CZ core.
- **Quantifier warning (fix B5').** (b) must be stated for the data map, not, as §12.2's LR-grad, for every configuration
  with ||x||_{inv,m} on the right. Counterexample:
  - take r_{j-1} = dψ with ψ a level-j checkerboard of amplitude a, and all f = 0;
  - since Q_{j-1}x_{j-1} - x_j = dψ is gauge-invariant and Q preserves gradient-Hölder bounds up to constants, every
    gauge representative has [∇^cx^c_{j-1 or j}]_α ≳ L^{α(k-j)}L^{2(k-j)}a;
  - but ||x||_inv ≈ L^{2(k-j)}a.
  For residual-type sources use x = y - τ and BL-3 (α ≤ θ), as Corollary FP does for potentials.

**What LRL closes and what it does not (all ARGUED from here).**

| target | closed by | remaining |
|---|---|---|
| gradient half of (G♯_0-field^∇)_m, data + residual sources (lane B's (LEG_w)) | LRL (b) + BL-3/Theorem W | none beyond LRL (b) |
| X_s part of (G♯-rough), m = 0 | LRL (a) + duality + flux approximant + transport (Part 5) | none beyond LRL (a) |
| X_s part of H-lin_inv's BCH₂ response, m = 0 | LRL (a) + SPD (telescoping above) | co-closed part only (13.7 scope) |
| curvature outputs f_j, [f_j]_α of (G♯-rough) / BCH₂ response | **not** closed | dual responses to localized divergence-form sources: (G♯_0-lev0)/(G♯-up), OPEN |
| (RP) sup form | not needed | expected false (log) |

**Verdict on item 5: the walls merge for the X_s outputs and for the gradient half, into LRL. LRL (a) is the shared
analytic core, a lattice CZ/Schauder estimate, uniform in mesh and torus. They do not merge for the curvature outputs.**

---

# Part 7. Step 3 (§13.8-13.13)

**Lemma TS: CONFIRMED** (it is REVIEW_BFT_A_S2's derivation; ba3 R3 2.3e-14).

**Proposition W: CONFIRMED given the package (constants crude).**
- Theorem 6.8 (a)/(b) are quoted correctly.
- Lemma 6.7 summation: Σ_{n∈Z}e^{-μ|n-t|} ≤ coth(μ/2). It is periodic and convex between integers, so the maximum is at
  integer t ✓, and S(μ) = coth⁴ ✓.
- J_0 = -κ_{k-1}(Q_str^{(n)})^Tr_{k-1} by J-str (b) and Lemma 2.4 ✓; the convex-combination form gives e^{5m} ✓.
- Weighted LES, weighted BL-C and the upper levels are all local within bounded coarse distance ✓.
- e^{17m} ≤ e^{20m} ✓.
- **Note:** S(μ) and M_f blow up as μ = m' - m → 0, so G_D(m) is uniform in k, T, X_0 but not in μ. This is stated
  correctly.

**Theorem W: CONFIRMED** (BL-3 with e^{8m}; G_R(m) as displayed).

**Lemma Λ: CONFIRMED, C_Λ = 10, k-free.**
- Λ_i's endpoints are level-0 roots spaced L^ie_ν (nesting, L odd) ✓.
- The one-step loop is the ruled surface γ × [0, L], with ≤ 2L(L-1) level-i plaquettes, each assembled into a square of side
  L^i of flux ≤ L^{2i}s_0 ✓. This needs the return path to be γ + Le_μ, which holds for the c26 template
  (`axial(cY, yL, sig)` is the translate).
- Telescoping with |Q^{(i+1→k)}v| ≤ 5L^{k-1-i}||v|| (BL-2 (b) in own units) ✓.
- 10L(L-1)L^{k-1}(L^k - 1)/(L - 1) ≤ 10n² ✓; localisation in B(X) ∪ B(X + e_μ) ✓ (nested blocks).

**Lemma LR-pot: CONFIRMED** (I checked every constant).
- P∘P = P: λ vanishes at roots because χ_X(c_Y) = δ_XY and λ_X(c_X) = 0 ✓.
- First sum: the strip has ≤ 3n plaquettes ✓.
- Second sum: Σ_X dχ_X = 0 and Σ|dχ_X| ≤ 2/n ✓. The loop has length ≤ 12n and lies within n of c_X; the cone fill is
  36n² ✓; Λ enters through ≤ 4 segments ✓.
- 75 + 8; 155/8/40; ×5 → 775/40/205 ✓; c_0 = 20 is crude but fine.
- Scope: T ≥ 3. ba3 R5 tests k = 1 only, so the j ≥ 1 telescoping is untested (it is a one-line identity).

**Corollary FP: CONFIRMED** (1083 = ⌈775 + 205·L/(L-1)⌉ at L = 3). It is the potential half for data + residual sources
in a linear, covariant slice. The heading's "(G♯_0-field^∇)_m" must keep "potential half" attached (it does).

**LR-grad (13.13): OPEN, and as stated FALSE (Part 6, fix B5').** The diagnosis that S_tent loses n^{1-α} on gradients
is consistent with Lemma AX (ARGUED).

---

# Part 8. Code review of ba3_rough.py

- R1's w is j minus its least-squares projection onto span Q_1^T[d_2^*(2-forms), constants], which is the correct S_1.
  R1c's comparison uses the correct BR-1 data shift and sources.
- R3 compares full configuration vectors from CG runs started at 0. This is fine: both runs see the same normal operator,
  and TS is an identity of the energy up to a constant.
- R4's Λ uses roots nX + (n-1)/2, consistent with the c26 template ✓.
- R5's tent_lambda implements the 24-order axial average and the tents ✓, k = 1 only.
- R2 uses su(2) ≅ (R³, ×), adequate.
- **No test touches SPD's cancellation, Proposition W's weights, or anything k-uniform.** This is disclosed (l.1181-1182).
- The script writes no files. The criteria file predates it.

---

# Part 9. ba3 rerun and reviewer probe (numeric lock)

**Run record.**
- Lock acquired 07:02:25Z (load 3.51, 46% free) after waiting for another holder. Released 07:02:46Z by one `rmdir`; no
  trap.
- nice 10; OMP/OPENBLAS/MKL/VECLIB threads 1; PYTHONDONTWRITEBYTECODE=1; python3 without -I; no timeout.
- Afterwards: no process left, no `__pycache__` in checks/, and the lock directory is gone (all verified).

**ba3 rerun** (run from checks/, output to the scratchpad; checks/ba3_out.txt untouched).
- 16.5 s, peak RSS 0.72 GB.
- **Output byte-identical to checks/ba3_out.txt** apart from the timing/RSS lines (diff empty).
- R0, R1a-c, R2, R3, R4, R5a-c: all PASS reproduced.

**Reviewer probe `rev3_probe.py`** (4.5 s, 0.47 GB; criteria in its docstring, written before the run).

| probe | result |
|---|---|
| **P1** (pre-stated criterion ≤ 1e-12): tent formula for (Q^{(0→2)})^Tu on co-closed level-2 u (k = 2, T = 2, s = 9), i.e. BR-2 (iii) and SPD's U | rel **6.0e-14**; equality max\|J\|s³ = max\|u\| to **2.2e-16**: **PASS**. On non-co-closed u the formula fails (rel 1.0), as it should (Lemma 2.4 needs co-closedness). |
| **P2**: Lemma 2.4 sanity, Q_str^T = Q^T on co-closed inputs | 1.3e-14 |
| **P2**: does Q_str preserve co-closedness? | **No**: \|d*Q_strw\|/\|Q_strw\| = 0.18, 0.28, 0.28 (T = 2, 3, 4). So D(w) ≢ 0 and the rough potential φ is non-local, confirming the structural step of Part 5. |
| **P3**: rough w, Hodge primitive, sup\|g\|/sup\|w\| | random w: 0.32, 0.28, 0.38; designed w = P_R sign(P_RK): **1.16, 1.21, 1.47** at fine sides 6, 9, 12. osc φ/sup\|w\| (designed): 0.14, 0.36, 0.35. |

Reading of P3 (informational, not pre-registered):
- The designed ratio grows by 27% when the side doubles. That is consistent with the predicted CZ logarithm but too short
  a range to separate log growth from saturation.
- The designed w is a heuristic, not the true maximiser of the LP.
- **(RP)-sup's failure remains ARGUED.** A decisive test is the LP max_{w∈R, |w|≤1} g(b_0) at sides 6 to 24 (or a 2D
  analogue with the same alias structure). It is not needed if route (A) is dropped.

**SPD itself (the cancellation B(ū, v̄) = 0 and the boundary count)** is not tested numerically. That would need the
nonabelian S4' second-order form, which no check in this directory implements. P1 covers SPD's carrier formula and pairing
identity only.

---

# Binding fixes for the next lane-A session

- **P1' (provenance).** In §12.3 l.943, "stated before the proofs are written, after exploratory reasoning" reads
  "stated after the outcomes were known (BR-2 (iii) already asserts BA3-F4; the ba3 criteria file carries §13's final
  constants 10, 75, 155, 8, 40); not pre-registered". Correct the 13.4 correction's "≈06:43" to "≤ 06:42:14Z".
- **B1' (none needed for RS/BR-1/BR-2/CR-1/TS/Λ/LR-pot/FP).** They are CONFIRMED as written.
- **B2' (SPD label).** In the §15 table, "Proposition SPD (W2)" reads "SPD: carrier bound for Q_str^{(l→m)}R^B_l
  (PROVEN-HERE); (W2) ⟸ SPD + (SB), (SB) OPEN". §11's (W2) wording stays as the definition.
- **B3' (CR-1 scope).** Add "source in E_src's sign convention is -s^C; BL-5 (a) applied componentwise in an
  orthonormal basis of su(N) at the trivial background".
- **B4' (13.7 gap).** Add Gap 3: the level-0 rough piece of R^B_0 (outside (G♯-rough)'s 1 ≤ l ≤ k - 1); it is a
  (G♯_0-lev0) instance.
- **B5' (LR-grad quantifiers).** §12.2 l.940-941 and 13.13: LR-grad with ||x||_{inv,m} on the right is false (Part 6
  counterexample). Restate as LRL (b) for the data map; residual-type sources via BL-3.
- **B6' (route choice).** Record that (RP)-sup is expected false (CZ log, T-dependent; Part 5), that the X_s part of
  (G♯-rough) and of the BCH₂ response reduce to LRL (a) via route (B) and the telescoping of Part 6 (ARGUED), and that
  the curvature outputs remain tied to (G♯_0-lev0)/(G♯-up).
- **B7' (transport remark).** Record that all residuals of x(w) are transports of r_{k-1}(x(w)) plus -w/κ_{l-1} (J-str
  argument on the source-free levels). Then Theorem 6.8 (b)'s G-sum is never needed for rough sources.

# Strategic verdict

Session 3 is solid and mostly correct:
- the exact rough reduction (BR-1, with BA3-F4 an honest negative);
- the commutator row identified as residual type (CR-1);
- a correct carrier-decay bound (SPD);
- the first configuration-level results at m > 0 (Λ with a k-free constant, LR-pot and FP in a linear covariant slice),
  plus the weighted gauge-invariant data map (Proposition W, Theorem W).

The two weak points are labels: SPD is not (W2), and LR-grad is quantified wrongly. **The highest-value next step is
LRL**, the lattice Coulomb-Schauder lemma:
- (a), a single-level CZ/Schauder estimate with polynomial decay, closes the X_s outputs of (G♯-rough) and of the BCH₂
  rows without (RP) or (SB);
- (b), a composite local slice for the data map with e^{O(m)} weights, closes the gradient half of (G♯_0-field^∇)_m,
  i.e. lane B's (LEG_w), and the gauge-variant components BFT-A-F2 needs.

After LRL, the remaining linear wall is the curvature outputs for localized divergence-form sources ((G♯_0-lev0),
(G♯-up)), which is where the level-0 image J lands. Abandon (RP) in sup form.

## Tally

- CONFIRMED:
  - §11 (all fixes; B7 independently);
  - Lemma RS; BR-1; BR-2 (i)-(iii); the 13.4 reduction and route (A) as an implication;
  - CR-1 (exact); SPD as a carrier bound;
  - 13.7's implication (weights);
  - Lemma TS; Proposition W; Theorem W; Lemma Λ (C_Λ = 10); Lemma LR-pot; Corollary FP.
- CONFIRMED-WITH-FIX: CR-1 scope (sign convention, componentwise su(N)); 13.7 (missing level-0 rough piece).
- WRONG / mislabelled: §15 "SPD (W2) PROVEN" (it is the carrier bound only); LR-grad as stated (false for general
  configurations).
- OPEN, as the file says: (G♯-rough) curvature outputs; (SB); (RP); LR-grad. New reviewer routes (ARGUED): the X_s parts
  via LRL (a).
- Provenance: file order CONFIRMED (boundaries 79088 / 85494 / 93716); epistemic pre-statement NOT established (BR-2
  (iii) and the criteria constants).
