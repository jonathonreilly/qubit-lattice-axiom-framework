# REVIEW_BFT_A_S4: hostile line-by-line review of BFT lane A, session 4 (BFT_A.md §16-§20, BFT_A_LOG session 4, checks/ba4*, ba4b*, ba4c*)

Reviewer: independent session (did not write BFT_A). Date 2026-10-28 (UTC). Files read: REVIEW_BFT_A_S3.md (Bottom line,
Part 6); BFT_A.md l.869-942 (§12 statements) and l.1226-1673 (§16-§20 in full); BFT_A_LOG.md session 4; checks/ba4_criteria.md,
ba4_lrl.py, ba4_out_*.txt, ba4b_criteria.md, ba4b_diag.py, ba4b_out.txt, ba4c_profile.py, ba4c_out.txt; checks/ba2_lin.py
l.1-140 and checks/c26_led.py l.26-128 (chain, Q template). Only this file was written in the repo. Reviewer scripts and
outputs: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revbftA4/`
(rev4_probe.py, rev4_rp.py, rev4_synth.py and their *_out.txt).

Verdict vocabulary: CONFIRMED / CONFIRMED-WITH-FIX / GAP / WRONG. ARGUED marks reasoning of mine that is not a written
proof. Nothing below counts in PROOF's tally.

## Bottom line

- **Provenance: file order CONFIRMED. The order of the epistemic steps is as disclosed.** The ba4 criteria were registered
  before the script ran. All §18 proofs, and §19's "tori too small" reading, were written after T2 FAILED.
- **Lemma TK, LRL (a), Lemma FC: CONFIRMED-WITH-FIX** (two constant/scope slips, fixes T1-T2; neither touches a downstream
  use).
- **The review's Part 6 T-logarithm is real; Lemma TOP's repair is CONFIRMED-WITH-FIX** (fix T3: the composed-tent barycentre
  claim needs its one-line proof).
- **Theorem XR, Theorem XB, Corollary HX: CONFIRMED-WITH-FIX.**
- **ba4 T2 FAIL: NOT a counterexample. It is a pre-asymptotic L¹ trend below a T-independent ceiling (decisive evidence,
  T ≤ 12, Part 3).**
  - I re-implemented the k = 1 chain matrix-free. It reproduces ba4/ba4b to every printed digit at T ≤ 6, and I took it to
    T = 12 (M = 36).
  - The pointwise weighted envelope max(1 + s)⁵|∇A| is exactly T-flat (5.76 at s = 3, for every T = 4..12). The far shells
    do not grow. So Σ|∇A| ≤ 2157 for every T, a fixed ceiling, while W(12) = 8.6.
  - Running in the same code, the genuinely logarithmic quantity (the bare (RP) primitive) is a control: it has constant
    doubling increments. B(T) does not: its local log-slope falls from 1.57 to 1.07.
  - On the RP-designed family, Q_XR saturates outright (0.2315, 0.2312 at T = 8, 10).
  - Still, no finite-T numerics proves uniformity. Theorem XR stands on its proof, which I checked line by line.
- **Proposition CO: CONFIRMED as bookkeeping. (CO-0) is a new kind of problem, not the (RP) logarithm.**
  - The bare piece n²dΔ^{-1}w grows like log T.
  - The screened f_0 does not. A rigorous dual upper bound, over all rough w, is 3.59, 3.98, 4.38, 4.52, 4.57 at
    T = 3..10 (k = 1).
  - So any proof must keep J_0's two terms together (fix T5).
  - (CO-up) is mostly bookkeeping once (CO-0) is in hand (ARGUED, fix T6).
- **LRL (b): OPEN.** Its precise needs are listed in Part 6.
- **ba4, ba4b, ba4c re-runs under the lock (07:51:35-07:53:53Z): output identical to the stored files apart from timing.**

---

# Part 1. Provenance

**Filesystem record (stat, local EDT = UTC-4; quoted here in UTC):**

| file | born | modified | size |
|---|---|---|---|
| BFT_A.md | 05:39:32 | 07:41:05 | 164731 |
| BFT_A_LOG.md | 04:56:48 | 07:41:27 | 11541 |
| checks/ba4_criteria.md | 07:21:53 | 07:21:53 | 3577 |
| checks/ba4_lrl.py | 07:24:02 | 07:24:25 | 13532 |
| checks/ba4_out_D3.txt / D1a / D1b / D2 | 07:24:45 / 07:26:52 / 07:26:54 / 07:26:56 | 07:26:52 / 07:26:54 / 07:26:56 / 07:27:00 | - |
| checks/ba4b_criteria.md, ba4b_diag.py | 07:32:32 (both) | 07:32:32 | 1335, 1495 |
| checks/ba4b_out.txt | 07:32:44 | 07:32:46 | 643 |
| checks/ba4c_profile.py / ba4c_out.txt | 07:33:54 / 07:34:03 | 07:33:54 / 07:34:05 | - |

**Confirmed.**
1. **Byte boundaries.**
   - The first 121185 bytes of BFT_A.md end exactly at §15's last line ("…Lemma Λ, Theorem W.").
   - The first 129454 bytes end exactly at §16.5's last line ("…numbers fixed in the criteria file."). §17's separator
     follows.
   - The birth time is unchanged, so the file was appended to, consistent with the logged stats.
2. **Order:** §16 < ba4 criteria < script < ba4 run < §17 < §18 < §19/§20. The ba4 criteria contain only a-priori trend
   thresholds and no §18 constant (I checked: none of 648, 6⁵, 25⁵, C_F = 4, 108 or 18 appears).
3. **Labelling:** ba4b is labelled post-hoc in its first line; ba4c has no criterion. Both are labelled honestly in §19.

**Epistemic order (P1'').**
- §16 discloses that the LRL (a) route, Part 6's duality chain and the T-log were already sketched. F1-F4 are marked (c)
  correctly.
- BA4-F5..F7 carry pre-registration weight. **BA4-F7 ("ratios grow with T") OCCURRED for Q_XR.** §20 says so; good.
- Every §18 proof, including Theorem XR's "PROVEN-HERE" heading, was written after T2 FAILED. So was §19's "Reading" (the
  bulk at d ≈ 2-8 has not been contained). That reading was an assertion when it was written: ba4c did not discriminate a
  tail from a logarithm. It is now partly supported, and partly corrected, by Part 3 (fix T4).
- The ba4b criteria and script share the same second (07:32:32Z). "Criteria first in the command" cannot be checked from
  the filesystem, and it does not matter: ba4b is post-hoc either way.
- "Dated correction to 18.2 (ii) (session 4, ≤ 07:45Z)" (l.1572): the log puts it at 07:40:45Z. It should cite that time
  (fix P2'').

# Part 2. Lemma TK, LRL (a), Lemma FC (§18.1-18.3)

**Lemma TK: CONFIRMED-WITH-FIX.**
- Littlewood-Paley pieces, finite Poisson summation, and dropping p = 0 (σ_j(0) = 0): ✓.
- Only 2^j ≤ M/π occur ✓.
- Image bound |z + nM|_∞ ≥ max(|n|_∞M/2, |z|_∞) for |z|_∞ ≤ M/2 ✓.
- The 6 + 5 split, Σ_{n≠0}|n|^{-5} < ∞ in Z⁴ ✓, (2^{j+1}/M)⁵ ≤ (2/π)⁵ ✓.
- j-sums need a + 2 > 0 and a < 4 ✓.
- **T1 (scope slip).** §16.1 claims second-difference bounds for every 0 ≤ a < 4. The proof (l.1408-1409) gives them only
  for a > 0, since the second-difference symbol has order a - 2, which must exceed -2. At a = 0 (K_0) the 6 + 5 split
  gives an extra log r.
  - Fix: restrict the second-difference claim to a > 0; or split 11 = (11 - s) + s with 4 < s < 5, which covers a > s - 7.
  - Nothing downstream uses D²K_0 (LRL (a) uses |K_0|, |DK_0|, |K_1|, |DK_1| only).
- (K0-box): telescoping a forward difference ✓; q³(1 + h)^{-3} < 64 for q ≤ 4h + 1 ✓.

**LRL (a): CONFIRMED-WITH-FIX.**
- (i) The three-way split I/II/III using Σ_yK_0 = 0 ✓.
  - I: ℓ^∞ shell count 64t³ + 16t ≤ 216t³ ✓; Σt^{α-1} ≤ 2n^α/α ✓.
  - II: via K0-box ✓.
  - III: the dipole subtraction on Y_0 = {d ≤ D/2} uses Σ_yH(y) = 0 ✓. Path at ℓ^∞ ≥ RD/8 (ℓ^∞ ≥ ℓ¹/4 in d = 4) ✓.
    Lattice path length ≤ Rd(y) ✓; the complement is exponentially small ✓.
- (ii) Hölder: the N_2 split, the mean-value bound with ℓ¹ path ≤ 4h, and Σ_{t≥2h}t^{α-2} ✓. The wrap correction of l.1572 ✓.
- (iii) companion: A^c = R^{-1}K_1 * H ✓, near region ≤ 216C_Ke^{4m'} ✓.
- **T2 (false intermediate inequality, harmless).** (Σ1) l.1383 says the count of v ∈ Z⁴ with |v|_1 = t is
  ≤ 3(t + 3)³.
  - The true count is (8/3)t(2t² + 1), which exceeds 3(t + 3)³ for t ≥ 15 (18040 > 17496).
  - Replace it with ≤ 6(t + 1)³. Then 6(t + 1)³ ≤ 6R³(1 + t/R)³ ≤ 81R³(1 + t/R)³, so the stated 648R⁴ survives (the true
    value is ≤ 48R⁴).
- Numerics agree. ba4 T1/T3 PASS. My T ≤ 12 envelope (Part 3) is T-flat on the data response.

**Lemma FC: CONFIRMED.**
- (i) block flux conservation ✓.
- (ii) the tent weights sum to 1 ✓, the distance is ≤ 4L ✓, D_ρz_m ≤ s⁴max|∇A| ✓, C_F = 4 ✓.
- Measured ratio 0.15-0.16 (reproduced).

# Part 3. Theorem XR and the ba4 T2 FAIL (decisive item)

**Proof check: CONFIRMED-WITH-FIX (T2 only).**
- Step 1, transport: the induction for d*r_i = 0, and the i ≤ l - 1 formula (B7' precision) ✓. Exponents: the transported
  r_{k-1} gives L^{-(k-1-i)}; the w-part gives L^{2(k-l)}L^{-(l-1-i)}; Σ ≤ 3/2 ✓.
- Step 2, duality: ✓; S2 holds at 1e-11, reproduced.
- Step 3: w ⊥ Q_l^T(C_{l+1}) and 𝔽A co-closed. Constants cancel (Q^T𝔽c = c) ✓.
- Step 4: Prop W at (m, m') = (m_*'/3, 2m_*'/3), with the e^{4m'} corner shift ✓.
- Step 5: region factor 6⁵ ✓ and (Σ1) ✓; the exponent bookkeeping gives L^{2(k-l)}a ✓. The identity
  L^{2(k-l)}sup|w| = L^{-(α+θ)(k-l)}N_l(w) holds ✓.
- The only T-dependence anywhere is Σ_b(1 + d(b))^{-5}, which converges in d = 4. The logic is sound. A counterexample
  would have to break LRL (a)'s uniform envelope.

**Numerics: my own test, under the lock.**
- **Method.** The script is rev4_probe.py. It uses the same model as ba2_lin.SChain(4, T, 1, (1,)) (c26 axial template;
  datum at coarse link (0, 0)).
  - Q and Q^T are applied matrix-free as strided slices of the level-0 field (459 template entries per direction).
  - CG solves to residual ≤ 1e-11.
  - P_S is done by CG on coarse co-closed fields.
- **Validation:** B(T), W(T) and Q_XR for the XR-designed family equal ba4/ba4b at every printed digit for T = 2..6
  (e.g. B(5) = 1.45127, Q_XR(5) = 0.3254).
- **Resources:** peak 0.69 GB at T = 12. Every run took ≤ 60 s. Load 2.0-6.4 and ≥ 38% free at each acquisition.

| T | 4 | 5 | 6 | 8 | 10 | 12 |
|---|---|---|---|---|---|---|
| B(T) (bounds Q_XR on all of R_0) | 1.103 | 1.451 | 1.737 | 2.140 | 2.412 | 2.607 |
| dual upper bound ‖P_R B'_0‖_1/L² | 1.097 | - | 1.744 | 2.154 | 2.429 | - |
| W(T) = Σ\|∇A\|/L² | 3.915 | 4.969 | 5.862 | 7.113 | 7.966 | 8.575 |
| Q_XR, XR-designed w | 0.254 | 0.325 | 0.379 | 0.450 | 0.497 | - |
| Q_XR, RP-designed w (my design) | 0.199 | - | 0.223 | 0.2315 | 0.2312 | - |
| max_s (1 + s)⁵·shellmax\|∇A\| | 5.80 | 5.77 | 5.76 | 5.76 | 5.76 | 5.76 |
| outermost-shells value of the same | 3.34 | 3.77 | 4.67 | 4.88 | 4.44 | 4.42 |

**Discrimination (pre-asymptotic tail vs logarithm).**
1. **The pointwise envelope is T-independent.** Its sup is 5.76, attained at the same shell s = 3 for every T. The
   antipodal shells stay at ≤ 4.9.
   - A log T in Σ|∇A| would need a d^{-4} far field. Then (1 + s)⁵·max at the antipodal shell s ≈ 2T would grow linearly
     in T. It does not.
   - At a fixed position, the axial and diagonal profiles converge as T grows: the diagonal value at x = 9 is 1.68 (T = 10)
     and 1.35 (T = 12), decreasing toward a flat infinite-volume d^{-5} profile.
   - With envelope E = 5.76: W(T) ≤ 16E·Σ_{v∈Z⁴}(1 + ⌊|v|_1/3⌋)^{-5}/9 = 2157 for every T. This is a fixed ceiling, finite
     because Σ(1 + d)^{-5} converges in d = 4. That is the content of Theorem XR's Step 5.
2. **A logarithmic control in the same code.**
   - The bare (RP) quantity (rev4_rp.py) behaves as a logarithm should:
     - lower bound: designed |g(p)|/sup|w| = 1.44, 1.61, 1.75, 1.87, 1.94 at T = 4, 6, 8, 10, 12; doubling increments
       0.31, 0.33, 0.33;
     - rigorous upper bound ‖P_R y‖_1 = 4.33, 5.22, 5.83, 6.30, 6.67; local slope T·dQ/dT = 2.13, 2.09, 2.07, constant.
   - B(T) does not: its doubling increments are 1.03, 1.04, 0.96, 0.87 (3→6, 4→8, 5→10, 6→12), and its local slope
     T·dB/dT is 1.57 (T ≈ 5), 1.41 (7), 1.22 (9), 1.07 (11), falling.
3. **The per-shell sums converge in T.** Shell 7 is 0.516, 0.595, 0.609 at T = 8, 10, 12; shells 0-4 are identical to
   4 digits from T = 6 on. W grows by filling shells whose sums decay only slowly, roughly like s^{-1.2} to s^{-2} at
   s = 6..11. That is why the approach is slow: the asymptotic tail is c/T.
4. **A synthetic control with the same dipole structure** (F = d(Gaussian·e_0), width 1 coarse unit, R = 1, rev4_synth.py).
   - Increments: 22.5, 13.9, 9.7, 12.7, 7.9 for T = 12→16→20→24→32→40.
   - This matches c/T (predicted ratios 0.60, 0.67, 1.25, 0.60) and not log T (0.78, 0.82, 1.58, 0.78). Smaller T are
     irregular.
   - So a provably convergent source also looks non-saturated at T ≲ 10.

**T2 verdict.**
- **Not a counterexample to Theorem XR. The FAIL is finite-size.**
- Precisely: Q_XR ≤ B(T) and B(T) ≲ W(T) both sit under a T-independent ceiling, fixed by a T-independent pointwise
  envelope. The rise is shell filling with a c/T tail. On the RP-designed family Q_XR has saturated by T = 8.
- Caveats:
  - ba4's T2 remains FAIL as pre-registered. My tests are post-hoc reviewer tests with no pre-registration weight.
  - Everything is at k = 1, l = 0, L = 3, κ = 1.
  - The XR-designed Q_XR still rises at T = 10, though more slowly (+0.071, +0.047).
  - T-uniformity is proved by the argument, not by the trend.
- **Fix T4:** §19's "Reading" (l.1618-1622) and §20's BA4-F7 line should read: "the L¹ quantities rise by shell filling
  below a T-independent ceiling; the pointwise envelope is T-flat to T = 12 (REVIEW_BFT_A_S4 Part 3); T2 stays FAIL as
  registered". They should not say "the bulk at d ≈ 2-8 is not yet contained": at T = 12, shells 8-11 still carry
  0.49, 0.42, 0.34, 0.27.

**Side finding (ba4 RP numbers).** My RP-designed values (1.05, 1.18, 1.44, 1.55 at T = 2..5) differ from ba4's
(1.152, 1.375, 1.503, 1.513) and from rev3 P3, while the XR design matches to all digits.
- Likely cause (consistent with, not proven by, this): P_R y has entries that vanish by symmetry, and np.sign of roundoff
  noise picks different w.
- Fix T7: threshold sign() at 1e-12·max in future designs. Every such design is only a lower bound.

# Part 4. Theorem XB, Lemma TOP, Corollary HX (§18.5-18.6)

**Part 6's top-term logarithm: CONFIRMED real.** |z_k| ≈ s³ρ_l|A^c| ~ (1 + d)^{-4}. Summed over the 4T⁴ coarse links,
this gives log T, so REVIEW_BFT_A_S3's "(SPD at m = k)" step was wrong. Credit to session 4.

**Lemma TOP: CONFIRMED-WITH-FIX.**
- A = Π_ccA_loc = A_loc + du_0 ✓ (A_loc - B'_l is a gradient; FP gives |A^c_loc| ≤ C_Pe^{-m'd} for T ≥ 3).
- dψ = (A - A_loc) * ϑ ✓. (P1)-(P3) follow from ||Dϑ||_1 ≤ 2/R and ||D²ϑ||_1 ≤ 4/R² ✓.
- ⟨R, dψ⟩ = 0 (R co-closed) ✓. The telescoping ⟨V_k, dφ_k⟩ = Σ_m⟨V_m, e_m⟩ ✓.
- e_m kills affine ψ: block averages hit the centres, and Q^T acts on constants by L^{-3} ✓. Σ|c| ≤ 3L^{2(m-l)} ✓.
  Exponent -(k - l) ✓.
- The T ≤ 2 branch ✓ (≤ 64 coarse links; the harmonic mean is T^{-4}e_μ, because coarse means agree across levels).
- **T3 (unproven claim):** (c) needs "the two probability averages have the same barycentre" for the composed
  Q_str^{(l→k)} (convolved tents, transversally uniform). That is true if s²Q_str^{(l→k)}dψ = 𝔽dψ for every quadratic ψ.
  Add that identity, which is one line by induction on the levels (each one-step tent is symmetric about the face). The
  18s⁵ constant is then generous.

**Theorem XB: CONFIRMED.**
- The telescoping in Step 3 is pure algebra (V_{m+1} = Q_strV_m).
- Exponent: -3(k - l) + 4(m - l) - 2(k - l) + 4(k - m) = -(k - l) ✓.
- Step 1: weights L^{-(k-1-i)} with multiplicity k - 1 - i, and Σjj3^{-j} = 3/4 ✓.
- Assembly: Σ(j + 1)L^{-j} ≤ 5/4 ✓.
- Scope: co-closed R_l only. It needs no (SB), (W2) or (G♯-rough) ✓. It is not tested numerically.

**Corollary HX: CONFIRMED (scope as stated).**
- C_0 = 112p_L²L² = 2·8·7 ✓.
- Commutator rows via CR-1 ✓; residual sources via BL-1 and BL-3 ✓.
- It covers the X_s outputs only, at m = 0, at the trivial background, and only the co-closed BCH₂ part (13.7's scope).
  The non-co-closed part of R^B_l is not covered and must stay listed as open.

# Part 5. Proposition CO (§18.7): verified; how hard (CO-0) and (CO-up) are

**The reduction: CONFIRMED.**
- J_0 = j_0 - κ_0Q_str^T r_0, with r_0 from XB Step 1, gives J_0 = -κ_{k-1}(Q_str^{(0→k)})^Tr_{k-1} + Σ_l(Q_str^{(0→l)})^Tj_l ✓.
- f_0 = n²dΔ_0^{-1}J_0, because an exact 2-form F satisfies F = dΔ^{-1}d*F ✓.
- f_j = 𝒜f_0 - R_j with sup|R^c_j| ≤ 4‖r‖_{X_s,Σ} ✓ (exponents checked).

**(CO-0) is not the (RP) logarithm (reviewer numerics, k = 1, rev4_rp.py).**
- The bare piece n²dΔ^{-1}w grows like log T (Part 3, control 2).
- The chain's f_0 for the same designed w is flat: 1.13, 1.32, 1.34, 1.35, 1.35, 1.32 at T = 3, 4, 6, 8, 10, 12.
- Against the f_0-adversarial design (w = P_R sign(P_R y_p), y_p := H^{-1}d*δ_p, so that f_0(p) = ⟨w, y_p⟩):
  - designed ratio 1.17-1.27 at T = 3..10;
  - **rigorous upper bound over all rough w, ‖P_R y_p‖_1 = 3.59, 3.98, 4.38, 4.52, 4.57 (T = 3, 4, 6, 8, 10), saturating**
    (increments 0.39, 0.40, 0.14, 0.05).
- **So screening cancels the CZ logarithm.** The two terms of J_0 each carry log T separately, and their sum does not.
- **Fix T5:** Proposition CO must not suggest estimating the two terms of J_0 separately. (CO-0) is false by that route.
- **Route (ARGUED):** XR's duality, with B' replaced by the dual response y_p to the plaquette source d*δ_p, at the
  relevant level l: f_0(p) = ⟨w, (y_p)_l⟩. Then Π_cc, flux coarse-graining, FC (ii) and LRL (a) apply verbatim.
  - **The new input is a weighted curvature bound for the response to a localized level-0 divergence-form source.** It
    should be uniform in T and k, including Hölder at boxes down to ρ_0 near the source.
  - That is a localized (G♯_0-lev0) instance, the same analytic class as Proposition W but with a fine-scale source.
  - Estimated hardness: medium-hard. Prop W's machinery plus one source-scale Schauder step.
  - Caution: d*δ_p ∈ C_0 itself has a rough part, so the argument must not become circular. Use the explicit local Green
    structure of y_p within one coarse unit.

**(CO-up): mostly bookkeeping after (CO-0) (ARGUED).**
- [𝒜f_0]_α ≤ C[f_0]_α, because 𝒜 is a probability average and boxes satisfy ρ ≥ ρ_j ≥ ρ_0.
- [R_j]_α needs Hölder, not sup, control of the residual tent images. The naive bound Osc ≤ 2sup loses L^{α(k-j)}.
  - The transported parts are tent-Lipschitz at their own scale.
  - The explicit w-parts are BR-2 (i)-type explicit computations.
- **Fix T6:** "(CO-up) = (G♯-up) instance, OPEN" should read "(CO-up) ⟸ (CO-0) + a residual-Hölder lemma for
  L^{2(k-j)}Σ𝒬dr_i (OPEN, expected explicit)".
- The "iff" in Proposition CO is vacuous for (CO-up), which is the target restated. Say so.

# Part 6. LRL (b), the gradient half: OPEN. What it needs, precisely

1. **A slice construction.** A linear projection P_♯, commuting with coarse translations. P_♯x - x must be a composite
   gauge direction (one λ_0 pushed up by ev^{(j)}) trivial at level k.
   - Box-local Coulomb gauges, patched by S_tent's tents. A global Coulomb gauge is excluded at m > 0 by its polynomial
     tails.
2. **Interior C^{1,α} control from the curvature.** On each box of coarse side ~1, at every level j:
   [∇^cx^c_j]_α ≲ ||f_j||_∞ + [f_j]_α + lower order.
   - This is LES-div (Lemma 3.2'') plus a box Gaffney/Schauder estimate: a boundary version of LRL (a) with Campanato down
     to ρ_j, uniform in k.
3. **Patching.** Transition functions between neighbouring box gauges are harmonic on overlaps (both co-closed with the
   same curvature). The error dχ·(λ_X - λ_Y) needs C^{1,α} control of those transitions, which 13.12 supplies only at the
   potential level.
4. **Level consistency.** x_j = Qx_{j-1} - r_{j-1} in the slice. Gradient-Hölder bounds of x_j need Hölder bounds on the
   data-map residuals r_{j-1}.
   - This is exactly why the quantifier is for the data map (B5' counterexample).
   - It also needs Q to preserve gradient-Hölder bounds, uniformly in k.
5. **Weights.** Everything at e^{md}, 0 ≤ m < m' < m_*', with Prop W as the input.
- Residual sources enter through x = y - τ (BL-3, α ≤ θ), as in FP. No ||x||_{inv,m} may appear on the right.

# Part 7. Re-run of ba4 under the mandatory lock

Lock acquired 07:51:35Z (load 6.36 < 8, 42% free) and released by one rmdir at 07:53:53Z. Settings: nice 10,
OMP/OPENBLAS/MKL/VECLIB threads 1, PYTHONDONTWRITEBYTECODE=1, python3 without -I, no timeout, no trap.
- ba4 D3, D1a, D1b, D2, ba4b and ba4c are all **identical to the stored outputs** once the timing/RSS fields are stripped.
- Peak RSS 0.33-0.70 GB.
- Afterwards: no process left, no lock directory, no __pycache__ in checks/.
- My own probes ran in six further acquisitions (07:47:30-08:02:25Z), each with one rmdir and the same settings. Peak
  0.88 GB.

# Binding fixes

- **P2''** l.1572: "≤ 07:45Z" reads "07:40:45Z". Add to §19 that its "Reading" was written after T2 FAILED.
- **T1** Lemma TK (§16.1, l.1408): claim second-difference bounds only for a > 0, or redo the split (4 < s < 5).
- **T2** (Σ1) l.1383: "≤ 3(t + 3)³" reads "≤ 6(t + 1)³" (false for t ≥ 15 as written; 648R⁴ survives).
- **T3** Lemma TOP (c): prove the barycentre identity s²Q_str^{(l→k)}dψ = 𝔽dψ for quadratic ψ.
- **T4** §19 Reading / §20 BA4-F7: replace "tori too small / bulk not contained" with Part 3's evidence. T2 stays FAIL as
  registered; T-uniformity rests on the proof and the T-flat envelope.
- **T5** Proposition CO: (CO-0) must treat J_0 as a whole. The separate estimate carries log T (numerics, Part 5). State
  the duality route with y_p as the intended proof.
- **T6** (CO-up) restated as (CO-0) + a residual-Hölder lemma. Note that "iff" is vacuous there.
- **T7** Designs: threshold sign() (symmetry zeros). Report designed ratios as lower bounds, and ‖P_R ·‖_1 as the rigorous
  upper bounds.
- **Scope lines (§20):** XR/XB/HX hold at m = 0, at the trivial background, for co-closed BCH₂ rows. The numerics are at
  k = 1 only.

# Strategic verdict

- **Lane A's X_s outputs at m = 0 are closed modulo these fixes.**
  - LRL (a) is a sound single-level CZ/Schauder core.
  - Theorem XR delivers the X_s part of (G♯-rough) at every level, with an extra gain.
  - Theorem XB, with Lemma TOP, handles the BCH₂ X_s response without (SB).
  - The T2 FAIL that threatened this is a finite-torus effect, not a counterexample.
- **The live walls are now three:**
  1. **(CO-0)**, the level-0 curvature. Numerically it is T-uniform at k = 1 because of chain screening. It is provable
     only by keeping J_0 whole, via duality with a localized-source response.
  2. **LRL (b)**, the gradient half.
  3. **The non-co-closed BCH₂ remainder**, plus everything at m > 0 and at nontrivial background.
- **Recommended next session:** prove the weighted curvature bound for the response to d*δ_p at level 0, uniform in k and
  T. Then run XR's duality for (CO-0). Pre-register a k = 2 test of ‖P_R y_p‖_1 and of B(T) at T ≤ 10.
