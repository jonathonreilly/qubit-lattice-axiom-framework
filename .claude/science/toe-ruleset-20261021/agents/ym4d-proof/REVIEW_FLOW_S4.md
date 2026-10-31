# REVIEW_FLOW_S4: hostile review of lane C session 4 (FLOW.md §29-§34 and the [RFL3-fix] edits)

Reviewer: an independent agent. I wrote none of FLOW.md, FLOW_LOG.md or checks/f6c*, f7*. This file is the only one I
edited. No commits, PRs or pushes.

Inputs (read-only, by offset):
- FLOW.md §0 (l.36-42), §4 FR-2 block (l.196-215), §15 (l.570-590), §16 (l.594-684, U-tad, U-dec, U-pair, U-red),
  §18 (l.752-822), §19A row (l.868-874), §23 end (l.1099-1108), §25-§28 (l.1240-1366), §29-§34 (l.1368-1638) in full.
- FLOW_LOG.md, the session-4 entries (l.118-165).
- REVIEW_FLOW_S3.md, all of it (format; fixes S3-1..S3-7).
- HIST.md: grep of every `g_{k+1}` (l.190, 235, 244, 247, 253-254, 299, 349, 767).
- PROOF.md, current bytes: L4b (l.1205-1226), Prop. LF-count (l.4144-4172), Setting N5-0 (l.5110-5130).
- agents/ym4d-existence/EXISTENCE.md §14 (l.1869-2010): Lemma GS-1, Lemma GS-2, Theorem GS.
- checks: f6_criteria.md (A1 append boundary), f6c_closed.py, f6c_out.txt, f7_criteria.md, f7_cov_chain.py, f7_out.txt.
  BSD `stat` (TZ=UTC) of all of them.

Numerics:
- One NUMERIC LOCK acquisition, 04:06:00-04:06:06 UTC, released once. nice 10, 1 thread, load 4.97, memory free 43%.
- f6c and f7 were re-run unchanged, with stdout sent to the scratchpad. Nothing in checks/ was written.
- Separately, an exact-rational check of Prop. COV-sc's summation, no lock (< 0.1 s, no floats).
- Everything is in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revflow4/`.

Line numbers are FLOW.md lines as of this review.

---

## Bottom line

- **The [RFL3-fix] edits are correct and complete.** S3-1..S3-7 are applied and tagged, with one leftover from S3-2: the
  F-mono "Reading" sentence (l.1266) still carries the old index, "(1 + Rg_{k+1}²)^{p/2}" (fix S4-1).
  - The S3-4 pointers match the current PROOF bytes. PROOF.md was modified again at 03:55 UTC, after the session's
    03:38 check, and I re-verified the pointers after that change. My own S3 replacement numbers were wrong. Session 4
    found this, logged it before editing (FLOW_LOG 03:38) and used verified lines instead. That is the honest outcome.
  - The post-hoc f6 amendment A1 is correctly labelled. It sits after byte 5282, so the original criteria bytes are
    untouched (I checked the boundary). Its header time is corrected by a second appended line.
- **Lemma COV-str (i)-(iv): CONFIRMED** as mathematics, with two minor scope notes (fix S4-2).
- **The verdict on obstruction (iv) is the main finding.** (iv) is true, but **it is not an obstruction to UNIV for
  SU(N). It is an artefact of stating (U-IR)(c) on Γ^cov_n alone, over all directions.**
  - The undamped pure-gauge noise lives exactly on the coarse-gauge directions D_{B_n}Λ_n.
  - Those directions are not removed by any slice: FP-ab, NA-FP and PG^{(k)} fix only the residual group, and its
    algebra has ev λ = 0, so it does not reach them.
  - They are removed instead by an exact Gaussian identity, against the coarse-gauge zero modes of the Wilson Hessian
    inside Γ^{W0}_n (part of (a4)). After that, B_n depends on 𝒞_n **only through the transverse compression
    P_⊥𝒞_nP_⊥**. There, GS-1 and GS-2 give n-uniform L^{-2(n−j)} damping at the trivial background.
  - (U-IR)(c) on all directions is probably not the right hypothesis. It may even be false, since the gauge block of
    Γ^cov_n alone has an effective correlation length that grows like √n [inference]. Restate it as (COV-⊥) and add the
    cancellation lemma (COV-GI) (§2 below).
- **Prop. COV-sc: CONFIRMED.** I re-derived it, and the exact-rational identity holds for L ∈ {3, 5, 7, 9}, n = 1..8.
  - The f7 re-run is byte-identical to the stored output, apart from timing. The brute route equals the closed form to
    0.0e+00 at n = 2, 3, 4, and the finite-ε route agrees to ≤ 3.1e-11.
- **Lemma TOW: CONFIRMED.** Non-uniformity in k is harmless for UNIV-1L, because F-tel is an exact identity at each
  fixed n and no per-step constant of TOW enters any bound. There are two wording notes (fix S4-3).
- **Corrected tally: 27 PROVEN-HERE (claimed 27).** It is unchanged. But §30's "Reading" of (iv), the bracketed
  inference under (COV-NA), §33's "new obstruction identified", §31's UNIV hypothesis list and §34's OPEN line must be
  reframed (fix S4-4).

---

## 1. Priority 1: the [RFL3-fix] edits

| Fix | Where | Verdict |
|---|---|---|
| S3-1 | l.1104-1108, l.1340-1342 | APPLIED. Both sentences are struck and replaced with the FT-1 condition. §31 (l.1578-1582) later discharges FT-1 by Lemma TOW, so "UNIV conditional on (U-IR) + upstream" is now correct for the stated reason. |
| S3-2 (F-mono) | l.1252-1260, l.1269-1283 | APPLIED. The clause is struck. The correct clause is g_{k+1}^{-p} ≤ g_k^{-p}(1 + Rg_k²)^{p/2}, with the other direction via β_+ log L + R. **Leftover:** l.1266 still says "(resp. (1 + Rg_{k+1}²)^{p/2})". It must be (1 + Rg_k²)^{p/2} (fix S4-1). |
| S3-2 (H1-H5) | l.1272-1278 | APPLIED and CORRECT. I re-grepped HIST: the uses are at l.190, 235, 244-247, 253-254, 349 and 767, and the table matches them. Each is covered by the corrected clause or by (⋆). H3 is flagged for HIST's owner in FLOW_LOG l.135-139. **(minor)** For H4: F-mono's own hypothesis g_0, …, g_k ≤ γ already gives g_k ≤ γ. If γ ≤ min{1, √κ}, the √2 loss is not needed. Say which applies. |
| S3-3 (f6 A1) | l.1311-1317; f6_criteria.md bytes 5283-7295 | APPLIED. It is labelled POST-HOC, and the original FAILs stand. Provenance: the A1 append ran 03:42:34-42; f6c_closed.py was born 03:43:17; f6c_out.txt at 03:52:43. **(minor)** A1-cov's 1e-8 tolerance against 8-decimal printing tests only about 4 significant digits of c^cov. That is acceptable, because the closed form is independently confirmed (REVIEW_FLOW_S3 §6.3, and f7 P3). |
| S3-4 | l.41-42, l.576, l.587, l.872, l.1324-1327 | APPLIED. Verified against current PROOF bytes: L4b is l.1207-1225 (continuum normalisation at l.1216-1217); LF-count is l.4144-4172 (l.4151 "Let g_k obey…", l.4153 "Conversely…"); β'_B is at l.4162. **Recommendation:** PROOF.md is live, and these pointers have now moved twice. Cite by anchor ("Prop. LF-count, β'_B line") plus the line number as of a date. |
| S3-5 | l.1122 | APPLIED (infinite volume and twisted tori). |
| S3-6 | l.789-797, l.1343 | APPLIED. (a1)-longitudinal is merged into (a4); the requirement is in integrated form; (a2)'s needs are recorded, with the (iv) consequence. |
| S3-7 | l.201-215, l.1177, l.1201, l.1332 | APPLIED. One residue: the "FR-2 timestamps" line says the minutes are unrecoverable. That is honest and acceptable. |
| Tally 26 → 24 | l.1351-1355 | APPLIED. |

## 2. Priority 2: Lemma COV-str and the (iv) verdict

### 2.1 Checks of (i)-(iv)

**(i) CONFIRMED.**
- Set Z = 0 at X = 0. Since h̃(0; M) = 0 and ∂_Zh̃(0; M) = 0 for all M, every M-derivative of h̃ and of ∂_Zh̃ vanishes
  there.
- That kills ∂_Mh̃, ∂²_Mh̃, ∂_Z∂_Mh̃ and ∂_Zh̃·D²Z.
- Sign: linearising B_{k+1}e^{X_{k+1}} = W_♮(M̄(B_ke^{X_k}))e^{−Z} gives Z = T_kX_k − X_{k+1}.
- **(minor, S4-2a)** f contains only h = k̃ − d. For N ≥ 3, the V-independent terms κd(M̄_c(U_k)) are also part of the
  order-u intermediate exponent. Their Hessian at a background near 1 is O(|background|⁴), because d = O(y⁶) (§3.1).
  So they do not touch the F² coefficient. State this in one line.

**(ii) CONFIRMED.**
- The chain form is triangular with Π_{k+1} > 0, so it is nondegenerate.
- The envelope identity holds at the joint minimum X = 0.
- So 𝒞_n = κ^{-1}Σ_jA_jΠ_j^{-1}A_j^T.

**(iii) CONFIRMED** (geometric range sum r_1Σ_{m≥0}L^{-m} = r_1L/(L − 1), doubled by A_jΠ^{-1}A^T).
- **(minor, S4-2b)** "for every U_0 near 1" is not an n-uniform neighbourhood. For a constant-F background the level-k
  curvature in level units is L^{2k}F. So B_k stays in W_♮'s analyticity domain only for |F| ≲ L^{-2n}.
- This is harmless for β, which is a second derivative at F = 0 at each n. It matters for any non-perturbative use.
  Say "for U_0 in a neighbourhood 𝒰_n of 1".

**(iv) CONFIRMED.**
- Root covariance gives Q_kd_k = d_{k+1}ev_k, and ev^{(n−j)}δ_x^{(j)} = δ_x^{(n)} for odd L (nested sites).
- ||u||² = ||v||² = 8. Cauchy-Schwarz gives ||A_j^Tv||² ≥ ||v||⁴/||u||² = ||v||². Summing over j = 1..n gives
  ⟨v, 𝒞_nv⟩ ≥ (n/κ)||v||².
- So λ_min(𝒞_n^{-1}) ≤ κ/n.

### 2.2 The key question: does (iv) affect the one-loop coefficient?

**Verdict: no, not by itself. (iv) is an artefact of where the split B_n = −β[Γ^{W0}_n∘Φ_0] − β[Γ^cov_n] places the
coarse-gauge sector.** The argument follows.

**(1) Where the undamped noise goes.**
- Gauge covariance of the composite average holds at every background: A_j(B)D_{B_j} = D_{B_n}ev^{(n−j)}. FLOW states
  this at l.1509, and it is the derivative at g = 1 of 𝔪(B^g) = 𝔪(B)^{ev g}.
- So the pure-gauge part of the level-j noise lands exactly in the level-n coarse-gauge directions G_n := D_{B_n}Λ_n.
- The orthogonal projector P_⊥ = P_⊥(B_n) onto ker D^*_{B_n} kills it exactly, at every background.
- (iv)'s test vector v = d_nδ_x lies in G_n, so P_⊥v = 0.
- This is the 𝒞_n-level form of EXISTENCE Lemma GS-1. There, the root chain equals the straight chain plus dλ_n, the
  gauge-invariant content is the straight chain's, and only the gauge-variant root-representative variance diverges
  (Theorem GS (iv)).

**(2) Who else sees G_n. This is an exact Gaussian identity, and it is the new input.**
- In Γ^{W0}_n the fine fluctuation X_0 is on the composite slice. That slice fixes only the residual group
  G_res^{(n)}, whose algebra has λ = 0 at the level-n sites and zero block means.
- The fine coarse-gauge directions Jμ = D_{U_0}λ_μ (ev λ_μ = μ ∈ Λ_n) are therefore **not** gauge-fixed by FP-ab,
  NA-FP or PG^{(k)}. They must not be: V is the external field.
- At a critical point U_0 of 𝒯_0 (for example a constant Cartan field), H_WJ = 0, and D𝔪Jμ = D_{B_n}μ. These are
  exactly the "coarse-gauge modes … which carry only the IR term" of (a4) (l.786-787).
- Write exp(−Γ^{W0}_n − Γ^cov_n) ∝ Δ_FP∫_{slice}dX e^{−½⟨X, H_WX⟩}p_{𝒞_n}(D𝔪X), with p_𝒞 the N(0, 𝒞) density.
- Split X = Jμ + X' and integrate μ flat. The quotient-marginal formula
  ∫dμ p_𝒞(y + D_{B_n}μ) = det(D^*_{B_n}D_{B_n})^{-1/2}p_{P_⊥𝒞P_⊥}(P_⊥y) then gives, exactly:

  **Γ^{W0}_n + Γ^cov_n = ½log det_{X'}(H_W + D𝔪^TP_⊥(P_⊥𝒞_nP_⊥)^+P_⊥D𝔪) + ½log det_{ker D^*}(P_⊥𝒞_nP_⊥)
  + ½log det(D^*_{B_n}D_{B_n}) − log|Jac_J(U_0)| − log Δ_FP(U_0) + const.**   (COV-GI)

  Here P_⊥(P_⊥𝒞P_⊥)^+P_⊥ = 𝒞^{-1} − 𝒞^{-1}D(D^*𝒞^{-1}D)^{-1}D^*𝒞^{-1}. That is the inverse-compression identity which
  Lemma U-T⊥ step (2) already uses: U-T⊥ is the Γ^{W0}-side half of this identity.
- **All 𝒞_n-dependence of B_n is through P_⊥𝒞_nP_⊥.** The undamped share cancels exactly between Γ^cov_n's gauge
  block (≈ +½log(n/κ) per coarse-gauge direction) and Γ^{W0}_n's coarse-gauge block (≈ +½log(κ/n)).
- (COV-GI) is my derivation. It is not in FLOW, and it is not checked numerically. It is standard Gaussian algebra; I
  give it session-scale credibility, not PROVEN status.

**(3) The transverse sector is damped.**
- Each T_k(B) maps D_{B_k}Λ into D_{B_{k+1}}Λ, so P_⊥^{(k+1)}T_kP_G^{(k)} = 0. Hence P_⊥A_j|_⊥ is the product of the
  one-step transverse compressions, exactly.
- At the trivial background this is P_⊥Q_str^{n−j}P_⊥ (GS-1). Its noise covariance is ≤ σ²L^{-2(n−j)} at every
  coarse momentum (GS-2 (e)).
- So κ^{-1}P_⊥ ≤ P_⊥𝒞_nP_⊥ ≤ κ^{-1}C_LP_⊥, n-uniformly. The bracketed L^{-2j} mechanism of §18 (l.757-759) is
  **true on the transverse sector**. It is false only on G_n, where it is not needed.
- In the Cartan sector D_{B} = d does not depend on the background. There δT_k annihilates d exactly, so the
  background never converts gauge noise into transverse noise.
- Prop. COV-sc's mechanism (shares L^{-2(n−j)}, sensitivity L^{4k}, normalisation L^{-4n}) is the scalar model of
  exactly this transverse sector.

**(4) Why (U-IR)(c) on all directions is the wrong hypothesis [inference, not proven].**
- At the trivial background, the level-j gauge noise at level n has covariance ≈ D(G_j(0) + L^{-2(n−j)}Δ_n^{-1})D^*.
  This uses the 4D on-site Green's function G(0) and G_j(L^{n−j}r) ≈ L^{-2(n−j)}G_n(r).
- So 𝒞_n|_{G_n} ≈ κ^{-1}(c_0 + nG(0)p²) at coarse momentum p. The n-growth is p²-weighted. It is what (iv) sees at
  p ~ 1, and it gives 𝒞_n^{-1} on G_n a correlation length ~√n.
- In root sectors the background enters G_j(0) through a charged covariant Laplacian. The diagonal of such a
  Green's function is non-analytic in a constant field in 4D (|F|-type behaviour).
- So β[Γ^cov_n] alone may grow with n, plausibly like log n, while the sum (COV-GI) does not.
- The bracket at l.1509-1511 ("a background-independent log n per direction") is therefore unsupported: the growth is
  p-dependent and its coefficient is background-dependent. Its conclusion "not decoupled exactly" is true for 𝒞_n,
  but false for B_n.

**(5) What (COV-GI) moves elsewhere. These are real, but they are not obstructions.**
- (a) The explicit 𝒞-independent level-n terms ½log det(D^*_{B_n}D_{B_n}) and −log|Jac_J| are each IR-log singular in
  root sectors. They must be kept together; their low-momentum parts cancel.
  - A clean IR-safe form writes P_⊥𝒞P_⊥ through the block-curvature covariance:
    ½log det_⊥(P_⊥𝒞P_⊥) = ½log det_{Ran d_B}(d_B𝒞_nd_B^T) − ½log det_⊥(d_B^Td_B).
  - d_B𝒞_nd_B^T is local (finite range) and n-uniform, by Theorem GS (ii) at the trivial point.
- (b) At the tower U_0 = Φ_0(V), H_WJ = O(∇𝒯_0) = O(r), because ∇_{U_0}Ψ vanishes on V = 𝔪(U_0). So the corrections
  are r-pairings of Lemma U-pair type (β = 0 given its hypotheses (b)-(e)) plus O(r²) terms (symbols O(p⁴)).
- (c) The transverse damping at nontrivial root-sector backgrounds, to second order in F, is OPEN. It is now of
  scalar (COV-sc) type, not of the (iv) type.

**Answers to the specific questions.**
- Should (COV-NA) be stated on the gauge-invariant sector? **Yes.** Replace it with (COV-⊥): β of
  ½log det_{Ran d_B}(d_B𝒞_nd_B^T) relative to the 𝒞-independent determinants is bounded uniformly in n and converges
  geometrically. Add (COV-GI) as a lemma.
- Do FP-ab, NA-FP and PG^{(k)} project out exactly the undamped directions? **No.** They fix G_res^{(n)}, whose
  algebra has ev λ = 0. The undamped directions are the complementary coarse-gauge directions, ev λ ≠ 0. They are
  removed by the flat integral over the Wilson zero modes (COV-GI), not by a slice.
- **Real obstruction or artefact? Artefact,** for the n-growth found in (iv). What remains for SU(N) is (COV-⊥),
  together with (COV-GI)'s bookkeeping.

## 3. Priority 3: Proposition COV-sc and f7

**Re-derivation.**
- Diagonality: unique ancestors give A_j(c, y) = Π_kQ_k(y_{k+1}, y_k), and A_jA_j^† is diagonal.
- |w_k|² = cos²(Fd_1d_2/2): the 12 + 12 coordinate orders split the phase by the rectangle flux Fd_1d_2. This is exact
  in F.
- N_k = 1 − F²L^{4k}μ_2²/4 + O(F⁴), with μ_2 = (L² − 1)/12.
- The weights κ_j^{-1}L^{-4(n−j)} ∝ L^{2j}L^{-4n}.
- Hence c_n = −(μ_2²/4)Σ_{i=1}^{n−1}x^iΣ_{m=1}^ix^{2m}/Σ_{i=0}^{n−1}x^i, with x = L^{-2}.
- The sum gives x/(1 − x) − x³/(1 − x³) = x(1 + x)/(1 − x³), so c_∞ = −(μ_2²/4)x³/(1 − x³) = −(L² − 1)/(576(L⁴ + L² + 1)).

**Exact-rational check** (`revflow4/closed_check.py`).
- The direct double sum equals the closed form exactly, for L = 3, 5, 7, 9 and n = 1..8.
- At n = 2 it equals REVIEW_FLOW_S3's f6 form at L_2 = L (L = 3, 5).
- At L = 3: c_∞ = −1/6552, c_2 = −1.3717421e-4, c_3 = −1.5092699e-4, c_4 = −1.5243670e-4.
- The bounds hold: |c_n| ≤ |c_∞| and |c_n − c_∞| ≤ |c_∞|L^{-2(n−1)}, with monotone increase.
- **CONFIRMED.**

**f7 provenance.** f7_criteria.md was born 03:48:00 (birth = mtime). f7_cov_chain.py was born 03:49:19 (birth = mtime).
The smoke test ran at 03:51:57, after the final script bytes, and the official run at 03:52:43. **Criteria predate the
script.**

**f7 independence.**
- The brute route computes path phases link by link and walks explicit ancestor chains. It does not use the
  factorisation over offsets or the closed-form variance.
- It does use the diagonal formula from proof step (1). That step is structural and correct, but f7 does not test it
  independently.
- P4's second gauge (A_1 = −x_2) and the displaced block are genuine tests.

**Re-run (under the lock).**
- All criteria PASS, and the output is identical to the stored file apart from timing lines.
- The brute route equals the closed form to 0.0e+00 at n = 2, 3, 4. The finite-ε route agrees to −8.0e-12 / +1.4e-14 /
  +3.1e-11.
- Increment ratio 0.1098; |c_4|/|c_∞| = 0.998765.
- Wall time 5.1 s, peak RSS 361 MB. The criteria's "< 300 MB" was an estimate, as FLOW_LOG says.

**f6c re-run:** byte-identical to checks/f6c_out.txt (A1-cov, A1-G, A1-H PASS; A1-G' NOT EVALUATED).

**Scope.** In view of §2, COV-sc is the scalar model of the **transverse** sector only. That is the correct reading.

## 4. Priority 4: Lemma TOW (FT-1)

**Step-by-step checks.**
- **Step (1):** CONFIRMED. On Σ_lin the dP_resd* compression vanishes, because ⟨Y, dP_resd*X⟩ = ⟨P_resd*Y, P_resd*X⟩ = 0.
  Phys ⊥ dΛ_res, and O is block diagonal on ker h = Phys ⊕ dΛ_res.
- **Step (2):** CONFIRMED.
  - The count is right: #blocks + dim Λ_res = dim Λ'.
  - Injectivity holds: Mλ = 0 and λ ∈ Λ' give λ ∈ Λ_res, and then Tλ = 0 gives λ = 0.
  - d is injective on Λ'.
- **Step (3): CONFIRMED-WITH-WORDING.** The induction needs only "𝒯_k(U) = 0 ⇒ U flat", which is what it proves.
  - The direction comes from a zero of a minimum of nonnegative terms, with the minimum attained: the composite of a
    flat U' is M̄(U'), which is unitary and flat.
  - "Vanishes exactly on flat configurations" (both directions) is not needed and not shown. Write "only on".
  - The flat configurations U with M̄(U) = 1 are 1^g with g constant on the level-(k+1) sites, which is the G_res-orbit
    of 1. ✓.
- **Steps (4)-(5): CONFIRMED.** The value-function derivatives are D² = ∇²F[Y'²], D³ = ∇³F[Y'³] and
  D⁴ = ∇⁴F[Y'⁴] + 3∇³F[(D²X*, 0), Y', Y'].
  - The 6∇³F term combines with 3∇²F[(D²X*)²] = −3∇³F[…] through the derivative of stationarity.
  - The induction closes at order 4.
- **Step (6):** CONFIRMED given the cited upstream items.
- **Step (7):** CONFIRMED. The Taylor data need only the formal implicit-function computation at 1. The
  T-dependence of the chart radius is irrelevant.

**Is non-uniformity in k harmless for UNIV? Yes.**
- B_n = Σ_{k<n}b_k is an exact identity at each n. Each b_k = −β[Γ_k] needs only some exponential decay rate.
- UNIV bounds B_n through the composite route (U-red), never through per-step constants.
- F-rem's |ρ_k| bound comes from (SF-g), not from TOW.
- **Caveat for the record:** any future per-step statement must not use TOW's constants. That includes rates of
  b_k → b_∞ taken from the per-step route, or analyticity domains uniform in k.

**Verdict: CONFIRMED (counted).** Fix S4-3: write "only on" in step (3), and add the caveat to "What is not claimed"
(l.1573).

## 5. Priority 5: the UNIV hypothesis list

§31 (l.1578-1582) and §33 (l.1620-1622) list (a2), (a3), (a4), (b), (c)-for-SU(N) = (COV-NA), plus (U-IR-s).

Discharged items:
- (a1⊥), (U-loc) (session 3);
- FT-1 (TOW);
- (c) in the scalar instance (COV-sc).

These are correctly recorded.

**Corrected list (binding, fix S4-4):**
- **(a2)** The IR-term vertices, now of the transverse inverse compression D𝔪^TP_⊥(P_⊥𝒞_nP_⊥)^+P_⊥D𝔪, not of
  D𝔪^T𝒞_n^{-1}D𝔪.
  - This removes S3-6(3)'s demand for n-uniform locality of 𝒞_n^{-1}, which (iv) shows is impossible.
  - It is replaced by n-uniform bounds on P_⊥𝒞_nP_⊥, which do hold at the trivial point (§2 (3)).
- **(a3)** Residual-slice modification: unchanged.
- **(a4')** = (a4) minus its coarse-gauge-mode block. That block is absorbed by (COV-GI). What remains:
  - the transverse-longitudinal cross entries;
  - the residual-slice longitudinal entries;
  - the 𝒞-independent level-n determinants of (COV-GI), taken together for IR safety.
- **(b)** Unchanged.
- **(COV-GI)** The exact identity of §2 (2). Needed at Cartan constant backgrounds, with the r-corrections by
  U-pair. Session-scale Gaussian algebra.
- **(c⊥) = (COV-⊥) for SU(N)** Replaces (c) and (COV-NA). It is PROVEN in the scalar instance (as a model).
- **(U-IR-s)** (s1), and (s2) restated for (c⊥).

## 6. Verdicts per item (session 4)

| Item | Verdict | Fix |
|---|---|---|
| [RFL3-fix] set S3-1..S3-7 | CONFIRMED; one leftover index (l.1266) | S4-1 |
| S3-4 pointers | CONFIRMED against current PROOF bytes | anchor names (rec.) |
| f6 amendment A1 | CONFIRMED (post-hoc, labelled, append-only, boundary at byte 5282) | — |
| Lemma COV-str (i)-(iii) | CONFIRMED | S4-2 (d-terms; n-dependent neighbourhood) |
| Lemma COV-str (iv) | CONFIRMED as a statement about 𝒞_n | — |
| Reading of (iv) as an obstruction (l.1439-1443, l.1607-1612, S4-F3 "first half observed") | **WRONG emphasis**: the sector cancels exactly in B_n (COV-GI); it is not an obstruction to UNIV | S4-4 |
| (COV-NA) and its bracket (l.1506-1511) | Wrong target: stated on Γ^cov alone; the bracket's "background-independent log n per direction" is unsupported | S4-4 |
| Share identity S_j (l.1501-1503) | CONFIRMED (M^T𝒞^{-1}M ≤ 1 from MM^T ≤ 𝒞; Σtr S_j = dim) | — |
| Proposition COV-sc | CONFIRMED (exact rationals; f7) | — |
| Lemma TOW | CONFIRMED | S4-3 |
| f6c, f7 re-runs | identical | — |

**Corrected tally: 27 PROVEN-HERE (claimed 27).** That is 24 + COV-str (with (iv)) + COV-sc + TOW. Unchanged:
- GAP: UNIV-rate.
- WRONG as stated: F-split, and the session-3 sentence.
- IMPORTED-AND-REVERIFIED: L4b.

## 7. Binding fixes for the next lane-C session

1. **S4-1.** At l.1266, replace "(1 + Rg_{k+1}²)^{p/2}" with "(1 + Rg_k²)^{p/2}". In the H4 row, say whether
   γ ≤ min{1, √κ} makes the √2 loss unnecessary.
2. **S4-2.** In COV-str (i), add one line: for N ≥ 3 the κd(M̄) terms have Hessian O(|bg|⁴), so they do not affect the
   F² coefficient. In (iii), replace "every U_0 near 1" with a neighbourhood 𝒰_n, and note it shrinks like L^{-2n} in
   curvature.
3. **S4-3.** In TOW (3), replace "vanishes exactly on" with "vanishes only on". Under "What is not claimed", add: no
   per-step rate or bound may be taken from TOW's constants.
4. **S4-4 (main).**
   - Annotate §30's Reading, §33's S4-2 bullet and S4-F3: (iv) is a fact about 𝒞_n on G_n, and the sector cancels in B_n.
   - Strike the l.1509-1511 bracket.
   - Replace (COV-NA) with (COV-GI) + (COV-⊥).
   - Restate (a2) and (a4) per §5.
   - Update §31's "Consequence" and §34's OPEN line accordingly.
   - Keep "(c) on Γ^cov_n alone" only as a remark: possibly false (√n correlation length in G_n) [inference].

## 8. Next target (recommendation)

1. **Prove (COV-GI)** at constant Cartan backgrounds. Include:
   - the quotient-marginal step;
   - the Jacobian of J against the residual slice;
   - D_{B_n}'s constant zero mode in the Cartan sector;
   - the O(r) corrections via U-pair.

   Session-scale.
2. **(COV-⊥) in the Cartan sector.** D = d there does not depend on the background, and δT_k annihilates d. The
   transverse chain is then a COV-sc-type problem with cos-weights and |M̄| weights. Target: a closed form or a
   geometric bound.
3. **Check f8, criteria first.** A small-torus U(1) gauge chain (d = 4 if memory allows, otherwise d = 2 as a
   structural test), n = 1..3:
   - (A) verify (COV-GI) numerically;
   - (B) show that the F² coefficient of Γ^cov_n alone and of the (COV-GI) sum behave differently in n.

   This tests §2 (4)'s inference.
4. Then the root sectors, and (a2) in its transverse form.
