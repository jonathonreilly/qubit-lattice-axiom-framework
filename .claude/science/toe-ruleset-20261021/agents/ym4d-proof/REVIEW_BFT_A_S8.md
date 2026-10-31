# REVIEW_BFT_A_S8: hostile line-by-line review of BFT lane A, session 8 (BFT_A.md §38-§40 with §36-§37, BFT_A_LOG session 8, checks/ba8*)

Reviewer: independent session (did not write BFT_A). Date 2026-10-28 (UTC). Files read: REVIEW_BFT_A_S7.md (all, binding);
REVIEW_BFT_B_S8.md (all, including "Cross-lane GE-T adjudication"); BFT_A.md l.20, l.472, l.500-505, l.512-527, l.655,
l.659-660, l.928-939, l.1077-1106, l.1150-1151, l.1197, l.1471, l.2389, l.2441-2449, l.2474-2477, l.2516-2517,
l.3027-3047, l.3260-3744 (§36-§40 in full); BFT_A_LOG.md session 8 (l.218-256); BFT_B.md §15.0-15.1 (l.2014-2060),
§16.1-16.2 (l.2143-2163), l.94-98, l.410-420, l.2288-2300 (stopped at the end of lane B session 8; BFT_B.md's session 9 was
not read); SF.md l.780-790, l.840-858; HANDOFF.md; checks/ba8_criteria.md, ba8_fun.py (all), ba8_out_E1.txt,
ba8_out_E2.txt, ba8_err_{E1,E2}.txt, ba8_time.txt; checks/ba5_y.py l.14-100, l.158-220; checks/c26_led.py l.55-100. Only
this file was written in the repo. Reviewer scripts and outputs:
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-yang-mills-proof-df9972/a931aaa3-5369-4512-9e8d-b8590010706c/scratchpad/revA8/`
(rev8_exact.py, rev8_psi.py). **No numeric lock was taken and no floating-point job was run**: every number I produce is
exact rational arithmetic in plain python (no numpy, no BLAS), or arithmetic on ba8's printed values. See S8-17 for what
that leaves unchecked.

Verdict vocabulary: CONFIRMED / CONFIRMED-WITH-FIX / NARROWED / WRONG / NOT-VERIFIED. ARGUED marks reasoning of mine that
is not a written proof. Nothing below counts in PROOF's tally. REVIEW_BFT_B_S8's precision for lane A is labelled P8-a
there; it is separate from the P8-n fixes below, and I endorse it.

## Bottom line

- **Provenance: CONFIRMED.** Byte boundaries are exact (305985 B ends §35 at l.3266; 315783 B ends §36.4 at l.3368;
  351969 B is the file). Birth unchanged, so every edit was an append. Criteria (11:24:37Z) precede the script (11:25:56Z)
  and hold no session-8 constant. One undisclosed deviation: criteria pre-register E1b at (k, T) = (2, 2), the script runs
  it at (3, 1) (P8-1). **Honest reading of the disclosure (l.3276-3283): the session pre-disclosed the whole session-8
  story**, including the funnel mechanism, the tents at level-k roots and the corrected projection. So BA8-F3 and BA8-F4
  carry no pre-registration weight, exactly as the (c) marks say, and "F3 OCCURS" is confirmation of a held hypothesis.
- **[RBA7-fix] P7-1..P7-8: all eight applied faithfully** (§37, l.3373-3441).
- **Lemma DF: CONFIRMED.** **Theorem PW-cc: CONFIRMED, and its uniformity in k and T holds.** I traced C_cc's every
  ingredient. The usual failure mode (a constant built from a Green's function degrading as m' → 0 or T → ∞) does not bite:
  m' := m_*'/3 is **pinned before the estimate** (l.1471), S(m') = coth⁴(m'/2) is a Z⁴ sum that dominates the torus sum for
  every T (l.2389), G_D(m') = e^{20m'}G_D♭ is k,T-uniform (Proposition W, l.928-931), and κ_± are standing parameters of
  Setting LIN (l.20, l.472). Every exponent re-done.
- **Proposition RF: CONFIRMED (exact).** **Proposition TE: identity CONFIRMED, size CONFIRMED.** **Lemma RC: CONFIRMED.**
  **Theorem PW-E: CONFIRMED as an implication**, with the label correction that one of its other inputs is itself ARGUED.
- **THE CENTRAL FINDING (S8-7). The refutation of (GE-T) does not need the Coulomb stand-in at all, and the route the
  session uses to it is wrong.** §38.8's tent bullet routes the tent coefficient through "ψ_u(X) ≈ … is the level-0 spike a
  of 38.4 (measured a = −0.0022 …; ARGUED identification)" (l.3582-3585). That identification is not available: ψ_u(X) =
  (h^{(0→k)}u)(c_X) and sp_0 are different functionals, and ba8's own output separates them (at the non-level-k root
  S_C0 has sp_0 = 0 with φ_1 = −0.002619, CG has sp_0 = −0.0017 with φ_1 = −0.000713). Worse, a was measured at a level-k
  root in two representatives that are not S_E, and lane B's **PROVEN** 16.2 Step 1 (BFT_B l.2162) forces sp_0(Π_Ex; c_X) to
  be a partition-of-unity remainder, not a.
  - But ψ_u(X) is a linear functional of the given u, with no representative in it. **I computed it exactly.** For
    u := ⅛d*δ_p (p the (0,1)-plaquette based at c_X + (1,0,0,0)) — co-closed, admissible for (GE-T) with R = 1 —
    φ_1 = −1/432, φ_2 = −17/104976, **same sign**, φ_2/φ_1 = 17/243, and ψ_u(X) = **−65/26244** at k = 2. The tent then
    carries 8|ψ_u|L^{3(k−l)} = (130/6561)L^{3(k−l)} = 0.019814·L^{3(k−l)} against (GE-T)'s C_GTL^{−3l}R = C_GTL^{−3l}:
    **(GE-T) of §36.0 is FALSE by a factor ≍ L^{3k}**, with no numerics beyond exact rationals and no stand-in —
    modulo the two routine estimates named in S8-7 (the exact value is at k = 2; the k → ∞ statement needs the
    same-sign pattern of the higher funnel terms, which is exact at i = 1 and geometric above it).
  - The mechanism, stated correctly: Λ ∈ Λ_* vanishes at the level-k roots (16.1 (c), BFT_B l.2150) while h^{(0→k)}u does
    not, and Ξ_fullψ̃_u is **not** in 𝒢_0 (it moves the data), so S_E has nothing with which to absorb ψ_u and TE forces it
    out as a tent. The representative u⃗^♮ − Ξψ̃_u = u⃗ has no tent, so the failure is a property of **S_E**, not of the
    orbit. That is the lead's reading, now with a proof of the S_E half.
  - The session reached the right magnitude (0.0176 against my 0.0198) by a route that does not support it.
- **The stand-in transport (S8-8): NARROWED, and SOUND IN SUBSTANCE.** For the *spike* half (non-level-k roots) the stand-in
  is load-bearing and §38.5 justifies it in one clause ("plus terms smooth at Z", l.3523-3525) with no size estimate. The
  estimate exists and I supply it: by 16.1 (a), (b) and 16.2 Step 1, d*(Π_Ex)_0 at an interior site equals
  d*d[Σ_Xχ^5_X(λ^E_X − λ^E_{X_0})], every term of which carries at least one difference of χ^5, and Σ_Xdχ^5_X = d(1) = 0
  kills the leading term. So S_E's level-0 field has **no point divergence** at a non-level-k root. REVIEW_BFT_B_S8 reaches
  the same conclusion independently with its R_x identity. What §38.5/§38.8 omit, and should not: the transported number is
  representative-**sensitive** (ε(C0) = −0.002619 against ε(CG) = −0.000713, a factor 3.7).
- **Therefore the one-slice decision is well founded** — for the tent reason, which is now essentially provable, rather
  than for the measured-spike reason. See the explicit verdict at the end.
- **Nothing in §38 closes the factor k or (PW-ii), and PW-E is nowhere used as if it had content** (grep over the lane
  files: every occurrence labels it an implication or empty). But §40's Corollary PW-SR row understates the damage:
  Proposition SR, as an implication of (PW-ℓ¹) in S_E, is now **vacuous**, not merely short of (PW-ii) (S8-12).
- **Nothing labelled PROVEN depends on Proposition TE's size statement or on Proposition FS.** Checked item by item
  (S8-6, S8-9). The PROVEN labels are clean on that axis.
- **ba8: verdicts match the pre-registered criteria, with no post-hoc reinterpretation.** I re-derived both deciding
  verdicts exactly. Three disclosure fixes: the "F6-test YES" lines at three print-floor offsets are not reported (P8-5);
  §38.5's "ε = 0 … exactly" is not what the output says, though it is true (P8-4, and my exact computation proves the zero
  pattern); E4 is uninformative and sits where it reads as evidence (P8-6).

---

# Part 1. Provenance (priority 1)

**Filesystem record** (BFT_A_LOG l.223-241, times UTC): start stat 11:21:54Z, BFT_A.md born 05:39:32Z, modified 10:26:38Z,
size 305985, `ls checks | grep -c ^ba8` = 0. §36 at 11:23:19Z (size 315783). ba8_criteria.md 11:24:37Z. ba8_fun.py
11:25:56Z. Run 11:27:02Z-11:28:51Z. §37 11:35:55Z. §38 11:38:50Z. §39-§40 11:39:34Z. Final size 351969, birth unchanged.

**S8-1 Provenance: CONFIRMED-WITH-FIX.**
1. **Byte boundaries are exact.** The first 305985 bytes end at §35's last line (l.3266, "…Lemma GE, Lemma TD."); the first
   315783 bytes end at §36.4's last line (l.3368, "…No constant derived in this session appears in them."); 351969 is the
   whole file (l.3744). So §36 and §37-§40 were appends, and nothing above was rewritten.
2. **§36 is statements only** (l.3271-3368). No proof, no constant with session content, no forward reference. The
   provenance paragraph names the stat it was logged against and says corrections go into later sections as dated notes
   (l.3284-3285) — which is what §38's four precisions do (l.3452-3463).
3. **The disclosure is unusually complete, and it costs the session its pre-registration.** l.3281-3283 discloses, before
   the first edit, "a mechanism by which the funnel h of Q (BL-2 (b)) could put level-independent values on the links at a
   root next to p, together with its consequence for the S_E representative (tents at level-k roots) and a corrected
   projection". That is the entire session-8 result. The (c) marks on BA8-F3 and BA8-F4 (l.3353-3355) are therefore
   correct and the session says they carry no pre-registration weight (l.3283, l.3712-3713). I record the consequence
   plainly: **ba8 E2/E3 confirm a hypothesis the session already held; they are not a blind test of it.** The session is
   honest about this; a reader of §40 alone would not know it.
4. **Criteria before script, no session-8 constant.** ba8_criteria.md's numbers are 1e-9, 1e-10, 4, 2, 0.5, L² = 9, and the
   p_ref (8,8,8,8) taken from REVIEW_BFT_A_S7's D2 (l.20). None is derived in session 8. The one within-run comparator,
   "2 max|Y_2(C0; p_ref)| L^4" (l.22), is a **rule** fixed before the run, not a constant: that is legitimate
   pre-registration, and it is what screens out the three spurious large ρ values (S8-14).
5. **The sign error of §36.0's Π^♯ is recorded in the criteria file, before any script** (ba8_criteria.md l.6-8) and then
   as §38 precision 1 (l.3453-3456). Correctly handled.
6. **One deviation (P8-1).** ba8_criteria.md l.13 pre-registers E1b "on random chains (k = 2, T = 2)"; ba8_fun.py l.146
   runs E1b at `b5.Chain(3, 1)`. §38.1 reports the actual setting ("ba8 E1b, k = 3, T = 1", l.3479), so nothing is
   misreported, but the deviation from the pre-registered plan is not disclosed. Immaterial (an exactness test), but it is
   exactly the kind of drift the criteria rule exists to catch.
7. **Run protocol matches the brief**: one acquisition, one rmdir, nice 10, threads 1, no pkill, post-run pgrep and pycache
   checks logged with commands (BFT_A_LOG l.234-237; ba8_time.txt). ba8_err_{E1,E2}.txt are `time -l` records, 102 MB and
   297 MB, 0.7 s and 108 s: inside the budget.

# Part 2. [RBA7-fix] items (§37)

**S8-2: CONFIRMED.** All eight fixes are applied and are faithful to REVIEW_BFT_A_S7's text.

- **P7-1** (l.3377-3379): the dated line is there and says the two phrases were forward references at 10:17:18Z.
- **P7-2** (l.3381-3386): "Per R̃_c = R_c" is stated with the reason (local polynomial formulas in x and r(x) on the
  periodic lift). The optional part is taken, and the session upgrades the conclusion to "**Proposition NC, Corollary NC
  and Corollary WR (b) hold for every T ≥ 1 with C_NC itself**". That upgrade is licensed by S7 Part 2 (the overlap count
  already absorbs the wrap), and it is a real strengthening.
- **P7-3** (l.3388-3397): all three parts — v_k = 0 in 33.2's identity; Λ_0/const → Λ_* in Lemma CD (ii); CD (i) trivial
  and not using (GI).
- **P7-4** (l.3399-3407): the OB conclusion is weakened exactly as S7 required, with the recursion
  C_L := 1 + 18(L − 1), the impossibility of (ND) for ρ > 8C_L(k − m)N_BL³/c_0, and the replacement of §35's "grow with the
  box". BA7-F2 "does not occur (ARGUED)" is explicitly kept only in the weaker form. Typo: "8N_bCL³/c_0" (l.3403) should be
  N_B, and the C there is S7's unnamed constant from "no b_m of sup ≤ Cσ_m" (P8-9, cosmetic).
- **P7-5** (l.3409-3416): both dual forms recorded verbatim, §35's two sentences replaced, and the funnel split with the
  sign-convention clash against S7 noted. Lane A's own convention Q = Q_str − d∘h is the one ba8 E1a verifies to 2.6e-15
  (ba8_out_E1.txt l.1-2), so the file's convention is the right one to keep.
- **P7-6** (l.3418-3425), **P7-7** (l.3427-3434), **P7-8** (l.3436-3441): applied. P7-7 (c) cites REVIEW_BFT_B_S6's
  verdicts at second hand and says so ("I have not read REVIEW_BFT_B_S6 myself", l.3431-3432). Acceptable and honestly
  flagged; the verdicts match what S7 Part 6 reported.

# Part 3. Lemma DF and Theorem PW-cc (priority 2)

**S8-3 Lemma DF (38.1, l.3465-3479): CONFIRMED.** Every step re-done.
- (i) ⟨j, d ev^{(l)}θ⟩ = ⟨ev^{(l)T}d*j, θ⟩ ✓; with θ = Λ(Y), ⟨j, (Π_EY)_l⟩ = ⟨j, Y_l⟩ + ⟨Γ_E^TD(j), Y_0⟩ = ⟨S^E_0(j), Y⟩ ✓
  (Γ_E reads Y_0 only; ev^{(0)} = 1).
- (ii) BL-1 (ii) plus the induction Q^{(0→k)}Y_0 = Y_k + Σ_{i<k}Q^{(i+1→k)}r_i(Y) ✓. **The identity needs Y_k = 0** and says
  so (l.3471) — consistent with [RBA7-fix] P7-3.
- (iii) **This is the load-bearing new step and it is right.** d*Q^T = ev^Td* (BL-2 (c)) gives d*(Q^{(0→l)})^Tj = D(j);
  Γ_E(dλ) = −λ + I_χλ (BFT_B 16.1 (a), l.2144-2146) gives d*Γ_E^T = −1 + I_χ^T, hence d*Γ_E^TD(j) = −D(j) + I_χ^TD(j);
  I_χ^TD(j) is supported on the level-k roots with total ΣD(j) = 0, so b_k(j) exists on the connected coarse torus and
  ev^{(k)T}d*b_k(j) = −I_χ^TD(j). The three divergences cancel ✓.
- (iv) ℓ¹-ℓ^∞ duality with j = sign ✓, so 𝒟_l(Y) = ||(Π_EY)_l||_1 ✓.
- **What ba8 E1b does and does not test.** It tests only the chain push-downs of (ii) (ba8_fun.py l.145-159); the Γ_E step
  (i) is not in code. §39 does not claim otherwise, and §38.1's parenthetical is accurate. No fix.

**S8-4 Theorem PW-cc (38.2, l.3481-3501): CONFIRMED, and uniform in k and T.**

*Arithmetic (re-done).*
- Level-0 term: c := (Q^{(0→l)})^Tj is co-closed (BL-2 (c)), (Q^{(a→b)})^T = (Q_str^{(a→b)})^T on co-closed currents,
  |Q_str^Tj| ≤ L^{−3}||j||_∞ per step (L terms of weight L^{−4}) ✓, so ||c||_∞ ≤ L^{−3l}||j||_∞; co-closedness kills ⟨c, dλ⟩,
  so |⟨c, Y^p_0⟩| ≤ L^{−3l}||j||_∞𝒩(Y^p) ≤ C_YNL^{−3l}n = C_YNL^{k−3l} with n = L^k ✓.
- Top residual: r_{k−1}(Y^p)(b) = ⟨δ_p, dY^{(b)}_0⟩ = n^{−2}f_0(Y^{(b)})(p), |f_0| ≤ G_D(m')κ_-^{−1}e^{−m'd(p,b)} (28.5 step 3,
  l.2474-2475), 4 level-k links per coarse site ⇒ ||r_{k−1}||_1 ≤ 4n^{−2}G_D(m')S(m')/κ_- ✓.
- Lower residuals: from κ_iQ_i^Tr_i = κ_{i−1}r_{i−1}, iterating upward gives κ_ir_i = κ_{k−1}(Q^{(i+1→k)})^Tr_{k−1} ✓.
  Co-closedness **propagates** down the chain (d*Q^Tv = ev^Td*v = 0), so Q^T = Q_str^T at every step ✓, and
  ||Q_str^Tu||_1 ≤ L||u||_1 (L⁵ pairs of weight L^{−4}) ⇒ ||r_i||_1 ≤ κ̂L^{k−1−i}||r_{k−1}||_1 ✓.
- Residual terms: L^{−3(l−m−1)}·L^{k−1−m}·L^{−2k} = L^{2m+2−k−3l} ✓; Σ_{m<l} ≤ AL^{−k−l}/(1 − L^{−2}) and
  L^{−k−l} = L^{k−3l}L^{−2(k−l)} ≤ L^{k−3l}L^{−2} (since l ≤ k − 1) ⇒ ≤ (A/(L² − 1))L^{k−3l} ✓. This matches C_cc's second
  term exactly, A := 4κ̂G_D(m')S(m')/κ_-.
- ℓ¹ form: max{⟨j, x_l⟩ : d*j = 0, ||j||_∞ ≤ 1} = min_θ||x_l + dθ||_1 is the right LP dual pair ✓; 𝒩_l is invariant under
  composite gauge directions ✓ (Ξ adds d ev^{(l)}λ).

*Uniformity in k and T — the thing I was asked to break, and could not.*
- **m' is pinned, not chased.** l.1471 fixes m' := m_*'/3 once and for all, before the estimate, with m_*' the exponential
  rate of N2-exp'/Theorem 6.8 (a) (l.659-660). So **nothing in C_cc takes m' → 0.**
- **S(m') is a Z⁴ sum.** S(μ) := Σ_{X∈Z⁴}e^{−μ|X|_1} = ((1 + e^{−μ})/(1 − e^{−μ}))⁴ = coth⁴(μ/2) (l.2389, l.1077). It
  dominates the torus sum Σ_be^{−m'd(p,b)} for every T, so it is T-uniform and k-independent (the coarse lattice does not
  depend on k).
- **G_D(m') = e^{20m'}G_D♭** (l.1097) with G_D♭ BL-4's constant, and Proposition W is stated and proven "uniformly in
  k ≥ 1, T ≥ 1, X_0" (l.928-931, l.1076-1098).
- **κ̂ and κ_- are standing parameters.** κ_j ∈ [κ_-, κ_+] is a hypothesis of the composite problem (l.20) and
  κ̂ := κ_+/κ_- (l.472): neither depends on k or T.
- **C_YN** is Theorem YH's 𝒩* constant, 2(1728C_0'L^c + 4C_FP(m')C_N(c)S(m')) (l.2449); large (it carries L^c) but k,T-uniform.
So C_cc is k- and T-uniform. The claim stands as written.

*Two precisions (P8-2).*
- (a) The top-residual step writes r_{k−1}(Y^p)(b) as an **equality**, which is right only because Y^p's only source is
  G_0 = δ_p with no level-0 current: Lemma TOPD's second term sup|j_0|𝒩(Y^{(b)}) (l.2474) is absent. Say so in one clause;
  it is tighter than 28.5 step 3 and a reader will otherwise look for the missing term.
- (b) C_cc should be listed with its full dependence (C_YN, G_D(m'), S(m'), κ̂, κ_-, L), and the statement at l.3321-3322
  ("depending only on C_YN and the constants of Proposition W") should add κ_± and L. Cosmetic.

*Independent sanity note.* For l = 0, PW-cc **is** Theorem YH's 𝒩* with no residual term, as l.3499-3500 says. That is a
genuine consistency check, and it means PW-cc's new content is the residual chain, i.e. the second term of C_cc. That term
is where I looked hardest and it holds.

# Part 4. RF, TE, FS, and the stand-in transport (priority 1 — the central question)

**S8-5 Proposition RF (38.3, l.3503-3507): CONFIRMED (exact).**
- I re-derived Q^{(0→l)} = Q_str^{(0→l)} − d∘h^{(0→l)} from Q_i = Q_{str,i} − d∘h_i together with root covariance Qd = d ev:
  expanding the product, every term that has passed a d through a later Q becomes d ev, which gives
  h^{(0→l)} = Σ_{i<l}ev^{(i+1→l)}h_iQ_str^{(0→i)} = Φ_l ✓. Applying d*/8 at Z with (d*df)(Z) = 8f(Z) − Σ_{±μ}f(Z ± e_μ)
  reproduces RF verbatim ✓.
- **The code tests the stated identity, not a weaker one.** ba8_fun.py l.163-168 builds
  `-P + nb/8 + div(qstr_to(X0,l))/8 - Σ div(q_to(r_i, i+1, l))/8` with `div` = d* in the §23.1 convention
  (div(grad f) = 8f − Σ_{±μ}f, from ba5_y.py l.64-69) and the full Q (not Q_str) in the residual terms ✓. Exactness
  1.98e-15 / 3.57e-15 (ba8_out_E1.txt l.5-6).
- **Constructive note (P8-3 part): RF does more work than §38.5 claims.** With sp_0 ≡ 0 at Z, RF gives
  sp_l(Z) = −Φ_l(Z) + (neighbour average of Φ_l) + (Q_str and residual terms), and Φ_l = Σ_{i<l}φ_{i+1} is a **convergent**
  series, so sp_l(Z) → −Φ_∞(x_0)(Z) ≠ 0. *That* is why the spike is level-independent — not "two measurements agree". The
  session's own numbers fit it: Ξσ puts σ(Z) = Φ_2(Y_0)(Z) on sp_0, and the printed sp_0(C0#) = −0.0028 against
  ε = φ_1 = −0.002619 gives φ_2(Z) = −1.81e-4, i.e. **6.9%** of φ_1; my exact operator ratio for a source dipole is
  φ_2/φ_1 = **17/243 = 0.0700** (rev8_psi.py). sp_1 = 0.003189 and sp_2 = 0.002843 then bracket −Φ_∞ ≈ 0.0028 from above,
  decreasing. Put this argument in the file; it is stronger than what is there and it is almost free.

**S8-6 Proposition TE (38.4, l.3509-3520): identity CONFIRMED; size CONFIRMED.**
- Identity: Λ(x_0 + dμ) = Λ(x_0) − μ + I_χμ (16.1 (a)) gives (Π_E(x + Ξ_fullμ))_j = (Π_Ex)_j + d ev^{(j)}I_χμ, and
  I_χ(aδ_{c_X}) = aχ^5_X ✓.
- Size: in coarse coordinates ∫|∂_μ(Π_νσ_5(|t_ν|))|d⁴t = (2∫_0^1|σ_5'|)(∫_{−1}^1σ_5)³ = 2·1 = 2, so
  Σ_{level-l μ-links}|Δχ^5_X| = h^{−3}·2 = 2L^{3(k−l)} and ×4 directions = 8L^{3(k−l)} ✓. REVIEW_BFT_B_S8 (f) makes this an
  exact identity rather than a Riemann sum; adopt that (its P8-a).
- **Nothing labelled PROVEN depends on TE's size statement.** Checked: Lemma DF, PW-cc, RF and Lemma RC are independent of
  it; PW-E's inputs are (GE-T), YH's decomposition and EP-rec (l.3459-3462), not TE. The size statement feeds only
  §38.8's ARGUED refutation and Lemma RC's ARGUED *Reading*. The PROVEN labels are clean on this axis.

**S8-7 §38.8's tent leg (l.3581-3592): the conclusion is CONFIRMED and strengthened; the route as written is NARROWED and
should be withdrawn. This is the most important item in the review.**

*What is wrong with the route.*
- l.3582-3585 reads: "ψ_u(X) ≈ φ_1(g_0)(c_X) **is the level-0 spike a of 38.4** up to the Z'' contribution (measured
  a = −0.0022 at k = 2, T = 2, offset (1,0,0,0); ARGUED identification)".
- ψ_u(X) = (h^{(0→k)}u)(c_X) is the **funnel**, a weighted line-integral functional of u. a = sp_0 is the **divergence** of a
  chosen representative. They are different linear functionals, and **ba8's own output separates them**: at the
  non-level-k root Z, S_C0 has sp_0 = 0 with φ_1 = −0.002619, while CG has sp_0 = −0.0017 with φ_1 = −0.000713
  (ba8_out_E2.txt l.17, l.14, l.23). φ_1 moves by +0.0019 when sp_0 moves by −0.0017: slope ≈ −1.1. So the "≈" hides an
  O(1) multiple of the representative's own spike, i.e. the identification is not a small error, it is a change of object.
- And the number quoted, a = −0.0022, was measured at a **level-k** root in CG and S_C0, neither of which is S_E. Lane B's
  **PROVEN** 16.2 Step 1 (BFT_B l.2162: d*a_X = 0 at every site of Ñ_X all of whose 2d links lie in Ñ_X, c_X **included**,
  since the pin λ(c_X) = 0 only fixes the additive constant) forces sp_0(Π_Ex; c_X) to be the partition-of-unity remainder,
  which carries at least one difference of χ^5 and is therefore O(n^{−3}) — **not** a. So the one number the tent leg quotes
  is, for S_E, the wrong number, and it is the number that vanishes as k grows.

*Why the conclusion survives, exactly and with no stand-in.*
- ψ_u(X) contains no representative and needs no measurement. Take **u := ⅛d*δ_p**, p the (0,1)-plaquette based at
  z_0 := c_X + (1,0,0,0). Then u is co-closed (checked), supported within ℓ^∞ distance 1 of z_0, and
  |u(b)| ≤ (1 + |b − z_0|_∞)^{−3} with equality at distance 1: **admissible for (GE-T) with R = 1** (§36.0 l.3310-3312 with
  §38 precision 2).
- For such a u, λ^E_X(u) = 0 for every box that contains supp u in its interior: by 16.2 Step 0 (BFT_B l.2161) a_X is the
  ℓ²(Ñ_X) component of x_0 orthogonal to the gradients, and ⟨u, dν|_{Ñ_X}⟩ = ⟨d*_{Ñ_X}u, ν⟩ = 0 because d*u = 0 and u
  vanishes near ∂Ñ_X; the pin fixes the constant to 0. supp u is at distance ≥ n − 2 from ∂Ñ_X for every X within coarse
  distance 1. So **Π_Eu⃗ = u⃗ in the whole neighbourhood of supp u**, and nothing is available to cancel the tent.
- Exact values (plain python, Fractions, no numpy; rev8_psi.py; the h weights re-implemented from c26_led.axial and
  cross-checked by the identity h_0(dλ) = (mean of λ over the L⁴ offsets) − λ(root), which holds **exactly**):

  | offset o of p from c_X | φ_1 | φ_2 | φ_2/φ_1 | ψ_u(X) at k = 2 |
  |---|---|---|---|---|
  | (0,0,0,0), (−1,0,0,0), (0,0,1,0), (1,1,0,0) | 0 | 0 | — | **0 exactly** |
  | (1,0,0,0) | −1/54 | −17/13122 | +17/243 | −130/6561 |
  | (0,1,0,0) | +1/54 | +17/13122 | +17/243 | +130/6561 |

  (unnormalised u = d*δ_p; divide by 8 for the admissible u). The two terms have the **same sign**, so they add: there is no
  cancellation, and with the ratio 17/243 the tail is a 0.5% correction. For the admissible u, ψ_u(X) = **−65/26244**.
- Tent ℓ¹ at level l = 8|ψ_u|L^{3(k−l)} = (130/6561)L^{3(k−l)} = 0.019814·L^{3(k−l)}. (GE-T) with R = 1 allows
  C_GTL^{−3l}. So (GE-T) requires **C_GT ≥ 0.0198·L^{3k}**: **(GE-T) of §36.0 is FALSE, by a factor ≍ L^{3k}.**
- Two steps remain estimates, and I label them: (i) ||(Π_Eu⃗)_l||_1 ≲ L^{−3l} (that is (GE-T) without the ♮ term; the boxes
  whose boundary passes through supp u contribute a boundary **dipole** — the cut source has zero total — at distance 2n,
  so λ^E_X = O(n^{−3}) and its tent contributes O(n^{−4}) fine, i.e. O(L^{−3l}) in level-l ℓ¹, exactly at the allowed scale;
  REVIEW_BFT_B_S8's probe R3 supports the same conclusion numerically); (ii) that the φ_{i+1} for i ≥ 2 do not reverse
  φ_1 + φ_2 (same sign and down by 17/243 at i = 1). Both are routine; neither involves a stand-in.
- **The mechanism, stated correctly.** Λ ∈ Λ_* vanishes at the level-k roots (16.1 (c)) while h^{(0→k)}u does not, and
  Ξ_fullψ̃_u is not in 𝒢_0 (it moves the data from Q_str^{(0→k)}u to Q^{(0→k)}u). So S_E has no gauge with which to absorb
  ψ_u, and TE forces it out as a tent. By the same token the representative u⃗^♮ − Ξψ̃_u = u⃗ (data unchanged) carries **no**
  tent: the failure is a property of **S_E**, not of the orbit. That is precisely the lead's reading, and the S_E half of it
  is now proved rather than measured.
- The session reached a magnitude 0.0176 where I get 0.0198. The agreement is a coincidence of two different
  normalisations, not a validation of the route.

**S8-8 §38.5's spike leg and the S_C0 → S_E transport: NARROWED (sound in substance, under-argued as written).**
- The transport is the clause at l.3523-3525: "S_C0; and, ARGUED, S_E, whose level-0 field near a non-level-k root is a
  tent-weighted sum of box-Coulomb fields a_X, d*a_X = 0 in the box interiors, plus terms smooth at Z". There is no size
  estimate and no statement of how the omitted terms behave as k grows. This clause carries lead decision D1, so it needs
  more than one line.
- **The estimate exists; here it is.** By Σ_Xχ^5_X = 1 (16.1 (b)),
  Λ(x) − λ^E_{X_0}(x) = Σ_Xχ^5_X(λ^E_X − λ^E_{X_0}), so at any interior level-0 site z

      d*(Π_Ex)_0(z) = d*a_{X_0}(z) + d*d[Σ_Xχ^5_X(λ^E_X − λ^E_{X_0})](z),

  and the first term vanishes by 16.2 Step 1 while d*d(λ^E_X − λ^E_{X_0}) = 0 there too (both box potentials have the same
  divergence −d*x_0). So every surviving term carries at least one **difference of χ^5**, each costing 1/n
  (|σ_5'| ≤ 15/8, 16.1 (b)), and Σ_Xdχ^5_X = d(1) = 0 kills the leading one, leaving only differences λ^E_X − λ^E_{X'}.
  Conclusion: **S_E's level-0 field has no point divergence at a non-level-k root**; it differs from S_C0's by a gauge that
  is smooth on scale n. REVIEW_BFT_B_S8 reaches the same conclusion independently with its shift-corrected R_x identity,
  which is the same computation. Two independent derivations of the same missing step is good news for the claim and bad
  news for the file, which contains neither.
- **What §38.5 and §38.8 omit and should not: the transported number is representative-sensitive.** ε(C0) = −0.002619
  against ε(CG) = −0.000713 (ba8_out_E2.txt l.23) — a factor 3.7 — and the session's own CG row shows a representative can
  sit most of the way to cancelling ε. Reporting only the C0 value, with "smooth at Z" as the bridge, makes the inference
  look more robust than it is. With the estimate above it **is** robust; without it, it is not.
- **k-independence of the spike** rests on two points, (k, T) = (3, 1) and (2, 2), which differ in **both** k and T
  (l.3527-3528). The agreement to three figures (0.00319 both times) shows the spike is set by the local geometry, which is
  the right conclusion; but the clean argument is RF plus the convergence of Φ_l (S8-5), and that is what should be written.
- Verdict: the ARGUED label is **correct**; the justification must be replaced (P8-3).

**S8-9 Proposition FS (38.5, l.3522-3535): CONFIRMED as ARGUED, with three overstatements to fix.**
- The exponent arithmetic is right. A point divergence 8·sp_l at Z forces Σ|Y_l| ≥ 8|sp_l| ≈ 0.023, against (PW-i)'s
  C_PL^{k−3l}; this fails once L^{3l−k} > C_P/0.023, i.e. for l > k/3 + (1/3)log_L(C_P/0.023) = k/3 + O(1) ✓ (l.3531,
  l.3533-3534). Such roots exist for every l < k, so the quantifier over p is satisfied.
- (a) "those four other offsets … give ε = 0 and sp = 0 **exactly**" (l.3530-3531): the script prints ε to six decimals
  (ba8_fun.py l.220), so the data support only |ε| ≤ 5e-7. The claim is nevertheless **true**: my exact computation gives
  ψ_u = 0 exactly at (0,0,0,0), (−1,0,0,0), (0,0,1,0), (1,1,0,0) and ±1/54 at (1,0,0,0), (0,1,0,0), (1,−1,0,0) — the same
  zero pattern as E3, now exact for the source functional. Cite an exact computation, not the print (P8-4).
- (b) The F4 criterion ("BA8-F4 occurs iff |eps| <= 1e-10 for every o", ba8_criteria.md l.29-30) **cannot be evaluated** at
  six printed decimals. It does not matter for the verdict (one offset gives 2.6e-3 ≫ 1e-10, so F4 cannot occur whatever
  the others are), but criterion and instrument disagree and that should be said (P8-4).
- (c) "level-independent to 11%" is a two-point statement; replace by RF + Φ-convergence (S8-5).

# Part 5. Lemma RC and Theorem PW-E

**S8-10 Lemma RC (38.6, l.3537-3552): CONFIRMED.** Every clause re-done.
- Precision 1's sign is right: with Π^♯ = Π_E + Ξσ, f^♯ − f^E = +n²⟨S, Ξσ⟩ = +n²⟨D(S), σ⟩ ✓ (and §36.0's original sign was
  wrong, as the criteria file already recorded).
- σ(y) ∈ Λ_* ✓ (the code zeroes σ at the level-k roots **after** the level loop, ba8_fun.py l.109-110, matching §36.0's
  "1 ≤ l(z) ≤ k − 1"; the nested-roots overwrite in l.105-108 correctly leaves Φ_{l(z)} at the top level of z).
- Idempotence, Π^♯x − x ∈ 𝒢_0, and S^♯ ∩ 𝒢_0 = {0} ✓. I also checked the clause the proof leaves implicit:
  Ker Π^♯ = 𝒢_0 (if x ∈ 𝒢_0 then Π_Ex = 0 by 16.1 (e) and Π^♯x = Ξσ(0) = 0), so chains = S^♯ ⊕ 𝒢_0 and S^♯ is a genuine
  slice. Translation covariance and reach ≤ 6 ✓.
- *Identity.* The step the text compresses is fine: Y^p's **own** source j_p = d*δ_p is composite-co-closed, so the
  S'-constrained solve returns Π_{S'}Y^p for any S' with S' ∩ 𝒢_0 = {0}; the response identity then holds for an
  **arbitrary** source S ✓.
- *Reading, l.3548-3552.* The arithmetic is right: n²σ_{l(Z)} = L^{2k}·L^{−3(k−l(Z))}η² = L^{3l(Z)−k}η², up to L^{2k−3}η² at
  l(Z) = k − 1 ✓. But the step from "the **difference** f^♯ − f^E can reach L^{2k−3}η²" to "the **Γ_E-response** carries
  terms up to L^{2k−3}η²" (l.3601, l.3742) needs f^♯ to be bounded, i.e. (PW-ℓ¹) in S^♯, which is unproven (only ba8's
  k ≤ 3 ratios support it). The ARGUED label currently covers only the D(R)-size step; extend it (P8-7).
- Two further precisions (P8-7): (i) §38.8's "a representative of the orbit, **not yet a slice** compatible with
  configurations" (l.3595-3596) is wrong as phrased — Lemma RC proves S^♯ **is** a slice; what it is not is
  𝔐^∇-compatible. (ii) §40's Lemma RC row cites "ba8 E2 (F6 does not occur)" (l.3702), but ba8's C0# is
  S_C0 + Ξσ(S_C0-field) (ba8_fun.py l.210), **not** Π^♯ = Π_E + Ξσ∘Π_E. Lemma RC needs no numerics; what ba8 tests is σ's
  cancellation mechanism in the C0-based variant. Say which.

**S8-11 Theorem PW-E (38.7, l.3554-3578): CONFIRMED as an implication, with one label correction.**
- 𝒮_l is a 𝒢_0-invariant seminorm on chains ✓ (38.6's Λ(y + Ξν) = Λ(y) − ν for ν ∈ Λ_*).
- The data split Z' ≡ Z'' + Ξ_fullψ̃ is right: β = β_str + dψ and Ξ_full ψ̃ moves the data by exactly d ev^{(k)}ψ̃ = dψ while
  leaving the residual sources (it is a pure gauge), so uniqueness modulo 𝒢_0 identifies the two problems ✓. Hence
  Y^p ≡ g^♮ + Z'' + Σ_qG_e(q)Y^q with g^♮ = u⃗^♮ for u = g_0 ✓ — and this is exactly where the tent enters Y^p.
- Unit conversions: a coarse cell holds 4L^{4(k−l)} level-l links, own units are L^{−(k−l)}× coarse, so the cell's
  contribution is 4L^{3(k−l)}× the coarse sup, and L^{3(k−l)}n^{−2} = L^{k−3l} ✓.
- Bootstrap: M := sup_p𝒮_l(Y^p) ≤ A + ½M with Σ_q|G_e(q)| ≤ ½ (U4') and M < ∞ at fixed (k, T) ⇒ M ≤ 2A ✓, with A free of p ✓.
- Case B: R = Tn/2 < 4L^cn for T < 8L^c ✓. T ≤ 4: the periodisation step is right and worth one written line —
  ||descent of Σ_γΠ_EY^{p+γ}_{T'}||_{1,T} = c^{−4}||Σ_γ…||_{1,T'} ≤ c^{−4}·c^4||Π_EY^p||_{1,T'} by translation invariance,
  and L^{k−3l} does not depend on T ✓.
- **Label correction (P8-8).** Precision 3 (l.3459-3462) lists among PW-E's inputs "the weighted reach c_r = 24 is ARGUED
  in REVIEW_BFT_B_S5 RS5-4 (a)". So PW-E is an implication **with an ARGUED input**, not a clean implication. The
  precision discloses it; §40's row (l.3703) should too. Low stakes, since the hypothesis is false anyway.
- **Not used downstream as if it had content: CONFIRMED.** Grep over the lane files gives BFT_A l.3340 ("conditional"),
  l.3596 ("as an implication"), l.3703, l.3744 ("an implication with a hypothesis expected false"), BFT_A_LOG l.248,
  HANDOFF l.117 ("PW-E is empty for S_E") and RTARGET l.906 (same). No occurrence treats it as content. **No quiet use.**

# Part 6. What §38 does not close

**S8-12 Proposition SR does not use PW-E, but §40's PW-SR row understates the damage: CONFIRMED-WITH-FIX.**
- SR (33.7, l.3027-3047) takes (PW-ℓ¹) as a hypothesis directly, via Lemma GE (b); PW-E appears nowhere in it. So the
  specific worry "is SR quietly using PW-E?" is answered: **no**.
- But SR's own scope paragraph already said "the contraction argument uses Φ_E away from the fixed point and needs
  (PW-ℓ¹) in S_E" (l.3046-3047). Session 8 says (PW-i) in S_E is expected FALSE. So **SR, as an implication of (PW-ℓ¹) in
  S_E, is now vacuous**, not merely short of (PW-ii). §38.9 (l.3616-3620) and §40's row (l.3707) discuss only (PW-ii);
  §40's Net (l.3724-3728) does say the Γ_E formulation is in question, so nothing is hidden, but the row as written will
  mislead (P8-6).
- What survives is a template, and it should be stated as one: 38.7's proof uses only 𝒢_0-invariance of 𝒮_l plus the YH
  decomposition, so **(GE-T)_P ⇒ (PW-i)_P ⇒ SR_P for any 𝒢_0-invariant linear representative map P**, and Lemma RC supplies
  one such P. REVIEW_BFT_B_S8 makes the same point about PW-E. Recording it converts a dead theorem into a live one.
- §38.8's "at a fixed point (PW-ℓ¹) may be used in the top-anchored representative" (l.3599-3600) is sound in its logic
  (at a critical point the rows are composite-co-closed by Lemma CD (i), so the pairing is representative-independent), but
  "may be used" reads as a licence: (PW-ℓ¹) in S^♯ is itself unproven. Soften it (P8-6).

**S8-13 The factor k in (NC-Γ) and (PW-ii): nothing in §38 closes them, and nothing appears to. CONFIRMED.**
- §38.9 is honest and correct: without (PW-ii) the interpolation term loses the s-gain, the level sum stops being
  geometric, and the factor k returns; (PW-ii) was not attempted; and (PW-ii)'s symmetric part contains d*Y_l, which is the
  spike functional of §36.0, so it fails in S_E for the same reason as (PW-i) (l.3616-3620).
- §40's Net states "The factor k of (NC-Γ) is not removed in session 8" (l.3724). I found no item in §38 phrased so as to
  suggest otherwise, and no constant in §38 that would feed a k-uniform (NC-Γ).
- The restated (NC-Γ) of lead decision D1 (composite-co-closed sources plus a remainder bound) has **no written remainder
  bound anywhere in §38**; Lemma RC's *Reading* says the remainder can reach L^{2k−3}η² (ARGUED). That is the gap D1
  creates, and §40 does not list it as an open item in those words. It should (P8-6).

# Part 7. Check ba8

**Script review (ba8_fun.py).**
- `coulomb0` (l.119-130) is S_C0 as defined: with mask = 0 at the level-k roots, the CG system
  mask·d*(Y_0 + d(mask·λ)) = 0 imposes d*(Y_0 + dλ) = 0 at every non-level-k-root site with λ = 0 at the level-k roots ✓.
  Residuals 7e-14 to 1e-13 (ba8_out_E2.txt), tolerance 1e-13 ✓.
- `xi` (l.113-117) builds Ξ over levels 0..k−1 only, i.e. **not** Ξ_full ✓ — the data are untouched, as 𝒢_0 requires.
- `Phi` (l.77-82), `sigma` (l.104-111), `hfun` (l.43-48) and the HT template (l.32-40, 24 orders × L⁴ offsets, weight
  1/(24L⁴)) match §36.0's definitions ✓. I re-implemented HT from c26_led.axial and cross-checked it by the exact identity
  h_0(dλ) = (mean of λ over the L⁴ offsets) − λ(root), which holds **exactly** in Fractions (rev8_exact.py). So the code's
  funnel is the object §36.0 names.
- `report`'s `isite` test (l.185) correctly restricts sp_l to sites that are level-l roots; Z = (4,4,4,4) is a level-2 but
  not level-3 root at k = 3 (off(2) = 4, off(3) = 13), so l(Z) = 2 < k ✓, and at k = 2 (7,7,7,7) has l = 1 while (4,4,4,4)
  is the level-k root ✓. The geometry claimed in §38.4-38.5 is the geometry the code uses.

**S8-14 ba8's verdicts match the pre-registered criteria, with no post-hoc reinterpretation: CONFIRMED.** Re-derived
exactly (rev8_exact.py, Fractions on the printed values):
- ρ = 0.2303/0.0287 = 8.0244 (printed 8.022 at full precision); **ρ ≥ 4 ✓ and 0.2303 ≥ 2·0.0822 = 0.1644 ✓ ⇒ F3 OCCURS**,
  as reported (§39 l.3660).
- 0.0000 > 0.5·0.2303 = 0.11515 is **false ⇒ F6 does not occur**, as reported (§39 l.3661).
- Every derived number in §38.4-38.5 and §39 checks: sp_1 = 0.0287/9 = 0.003189, sp_2 = 0.2303/81 = 0.002843, level drop
  10.8% ("11%" ✓); sp_1/(−ε) = 1.2176 and sp_2/(−ε) = 1.0856 ("within 25%" ✓); 8|sp_2| = 0.02275 ("≈ 0.023" ✓);
  8|a| = 0.0176 ("≈ 0.018" ✓); the l = 2 ratios 0.8656 / 0.4449 / 0.2716 ✓ (l.3534-3535); k = 2 T = 2 C0 sp_1 = 0.003189,
  identical to the k = 3 value ✓ (l.3528); CG's Σ_lsp_l = 0 to 4e-16 ✓ (l.3673).
- The criteria's a-priori factor rule is the right one and was not bent: "a level-independent spike gives rho ~ L² = 9;
  PW's scaling gives rho ~ 1" (ba8_criteria.md l.23), measured 8.02. And the **second** clause of F3 is what makes the test
  meaningful: ρ is 25.95, 67.62 and 9.22 at three of the symmetric offsets, where both spikes are at the print floor, and
  only the size clause screens those out. Good criteria design, written before the script.

**S8-15 Disclosure gap in §39: CONFIRMED-WITH-FIX.** The output prints "F6-test YES" at o = (0,0,0,0), (−1,0,0,0) and
(1,1,0,0) (ba8_out_E2.txt l.12, l.37, l.59), where both |sp_2| values are at the print floor. The criterion scopes F6 to
"that o", the F3 offset (ba8_criteria.md l.24), so the reported verdict is **right**; but three "YES" lines in the stored
output that the file never mentions is exactly what a hostile reader looks for. Disclose them as print-floor artefacts
(P8-5).

**S8-16 ba8 E4 is uninformative and is placed where it reads as support: CONFIRMED-WITH-FIX.** A random co-closed j is
essentially orthogonal to Y^p, so |⟨j, Y^p_l⟩|/(L^{k−3l}||j||_∞) = 0.0010-0.0052 is two to three orders below the quantity
PW-cc bounds, which is the **sup** over co-closed j, i.e. 𝒩_l — of the order of the 0.25-0.87 ratios in the same table.
E4 therefore carries no information about C_cc, and placing it immediately after the bold "**BA8-F2 does not occur**"
(l.3499) invites the reading that it is evidence. §40 is correct ("BA8-F2 does not occur (proof)", l.3711). Also
ba8_criteria.md l.32 asks for "3 random co-closed level-l j … l = 0, 1, 2" and the script uses one j per level
(ba8_fun.py l.223-226): a plan/script mismatch in an informational item (P8-6).

**S8-17 Reproducibility, and what this review did not check: NOT-VERIFIED (stated, not a defect of the session).**
- ba8_fun.py's `sys.path.insert` (l.13-14) and ba5_y.py's (l.14-15) point at `/Users/jonreilly/Projects/Physics/…`, so the
  stored scripts cannot be run from this worktree without editing the path.
- Following the brief ("prefer not to run numerics at all unless your result genuinely depends on one"), I took **no**
  numeric lock and ran **no** floating-point job. My findings rest on algebra, on exact rational arithmetic, and on
  arithmetic applied to ba8's printed values.
- **So, unlike REVIEW_BFT_A_S7, this review does not independently reproduce ba8's floating-point outputs.** The E1
  exactness figures (2.6e-15 … 4.6e-15) and the E2 table are taken as reported; what I verified independently is that the
  code computes the identities the file states (S8-5, Part 7), that the verdicts follow from the criteria (S8-14), and the
  exact rational facts of S8-7 and S8-9. A future reviewer who wants the floating-point half reproduced should fix the
  import path first.

# Part 8. Requirement table MR (§38.10)

**S8-18 CONFIRMED as a read-only survey, honestly marked.** Four rows spot-checked against their sources:
- m_Y ≤ ln2/(16·260) = 1.666e-4 ✓ (l.3623).
- **BFT-3** (BFT_B l.94-97): (H-𝔊_w)_k returns m_0 = m/4 for n ≤ 4, with no threshold on m_0 ✓. The row's caveat — that
  (H-𝔊_w)_k is itself a weighted (NC-E)-type statement, open independently of the rate — is correct and important.
- **RATE-m** (BFT_B l.2291-2294): "R_W(s̄) ≤ max(16, 18 + (2/m)log(C_Ws̄))" and "κ_L ≥ m/8 for R ≥ R_0(m, C_W')" quoted
  verbatim ✓. Quibble: "≳ 10⁴ coarse units" is a lower bound; R_0 ≈ (4/m)log(2^{44}C_W') is nearer 10⁶ at m_Y. Harmless.
- **BB-mix** (BFT_B l.415-417): K < e^{−m_0}/c_an with c_an = 80e ✓, and M_c ≥ 8(m_0 + log 80e)/m follows from
  K = e^{−κ_LM_c} with κ_L ≥ m/8 ✓.
- **SF CE-exp** (SF l.781-785): μM_min = 1539.5 at μ = m_1 = 4.83e-11 ✓. I note the condition is
  μM ≥ 3κ' + 4 log M + 8, not μM ≥ const, so M_min ∝ 1/μ only up to the log term — and at the **larger** rate m_Y the
  requirement is **smaller** (≈ 1479), so the "MEETS" verdict is conservative ✓.
- The CE-exp-𝒞 row's "NOT DETERMINED (open in SF)" is right: SF l.850-858 records (L-loc)_k as OPEN and (CE-col) as a new
  open name, with the rate loss blocking iteration.
- The verdict paragraph (l.3636-3640) draws the right conclusion and relocates the m > 0 problem to the weighted (NC-E),
  which is consistent with every row. No inflation found.

---

# Binding fixes

- **P8-1** (§39 Order, l.3647-3649, and ba8_criteria.md l.13): record that E1b was run at (k, T) = (3, 1), not the
  pre-registered (2, 2). One dated line; nothing is invalidated.
- **P8-2** (38.2, l.3487-3489 and l.3321-3322): state that the top-residual **equality** holds because Y^p's only source is
  G_0 = δ_p with no level-0 current, so Lemma TOPD's second term is absent; and list C_cc's full dependence
  (C_YN, G_D(m'), S(m'), κ̂, κ_-, L). Add the one line that makes the uniformity claim checkable: m' := m_*'/3 is fixed at
  l.1471 and S(m') = coth⁴(m'/2) is a Z⁴ sum, so neither degrades as T → ∞ or as k grows.
- **P8-3** (38.5, l.3523-3528): replace the transport clause by the estimate of S8-8 — d*(Π_Ex)_0 at an interior site is
  d*d[Σ_Xχ^5_X(λ^E_X − λ^E_{X_0})], every term carrying a difference of χ^5 (cost 1/n, |σ_5'| ≤ 15/8), with
  Σ_Xdχ^5_X = 0 killing the leading term, so S_E has **no point divergence** at a non-level-k root (16.1 (a), (b), 16.2
  Step 1, all PROVEN in lane B). Report ε(CG) = −0.000713 beside ε(C0) = −0.002619 and say that the transported quantity is
  representative-sensitive by a factor 3.7. Replace "level-independent to 11%" by the RF argument: sp_l → −Φ_∞ with
  Φ_l = Σ_{i<l}φ_{i+1} convergent (measured φ_2/φ_1 = 6.9%; exact operator ratio 17/243).
- **P8-4** (38.5, l.3530-3531, and §39's E3 row): "ε = 0 … exactly" is not supported by a six-decimal print. Cite instead
  the exact statement: for u = d*δ_p the funnel ψ_u(c_X) is **0 exactly** at the offsets (0,0,0,0), (−1,0,0,0), (0,0,1,0),
  (1,1,0,0) and ±1/54 at (1,0,0,0), (0,1,0,0), (1,−1,0,0). Also record that the F4 criterion's 1e-10 threshold cannot be
  read off the printed output, and that the verdict does not depend on it.
- **P8-5** (§39, l.3661): disclose the three "F6-test YES" lines at the symmetric offsets (ba8_out_E2.txt l.12, l.37,
  l.59) as print-floor artefacts, and state that the criterion scopes F6 to the F3 offset.
- **P8-6** (§38.9, §40 rows at l.3702, l.3703, l.3707, and §38.8 l.3599-3600): (i) state that Proposition SR, as an
  implication of (PW-ℓ¹) **in S_E**, is now vacuous, and record the surviving template (GE-T)_P ⇒ (PW-i)_P ⇒ SR_P for any
  𝒢_0-invariant linear P, with Lemma RC's Π^♯ as one such P; (ii) soften "at a fixed point (PW-ℓ¹) may be used in the
  top-anchored representative" to note that (PW-ℓ¹) in S^♯ is itself unproven; (iii) add to the open list that lead
  decision D1's remainder bound for composite-co-closed (NC-Γ) is not written anywhere in §38; (iv) note E4 is
  informational only and used one j per level, not three.
- **P8-7** (38.6 *Reading*, l.3548-3552, and l.3595-3596, l.3601, l.3742): (i) the step from "the difference f^♯ − f^E can
  reach L^{2k−3}η²" to "the Γ_E-response carries terms up to L^{2k−3}η²" needs f^♯ bounded, i.e. (PW-ℓ¹) in S^♯, which is
  unproven; extend the ARGUED label to cover it. (ii) "not yet a slice compatible with configurations" should read "a
  slice (Lemma RC) that is not 𝔐^∇-compatible for configurations". (iii) §40's Lemma RC row should not cite ba8 E2 as
  support for Π^♯: ba8's C0# is S_C0 + Ξσ(S_C0-field), not Π_E + Ξσ∘Π_E.
- **P8-8** (§40 l.3703): PW-E is an implication **one of whose other inputs is ARGUED** (EP-rec's weighted reach c_r = 24,
  §38 precision 3). Say so in the row, as the precision already does.
- **P8-9 (THE BIG ONE)** (38.8 first bullet, l.3582-3585): **withdraw the identification of ψ_u(X) with the level-0 spike
  a** and replace the tent bullet by the stand-in-free argument of S8-7: for u := ⅛d*δ_p with p the (0,1)-plaquette at
  c_X + (1,0,0,0) — co-closed, admissible with R = 1 — λ^E_X(u) = 0 for every box containing supp u in its interior
  (16.2 Step 0), so Π_Eu⃗ = u⃗ near supp u; TE then gives Π_Eu⃗^♮ = u⃗ + ψ_u(X)Ξχ^5_X with ψ_u(X) = −65/26244 **exactly** at
  k = 2 (φ_1 = −1/432, φ_2 = −17/104976, same sign, ratio 17/243); the tent carries (130/6561)L^{3(k−l)} against (GE-T)'s
  C_GTL^{−3l}, so **(GE-T) is false by a factor ≍ L^{3k}**. Keep ARGUED only on the two routine estimates named in S8-7.
  State the mechanism as it is: Λ ∈ Λ_* cannot see ψ_u at the level-k roots, and Ξ_fullψ̃_u is not a gauge of the problem,
  so the obstruction belongs to **S_E** and not to the orbit. Also fix the cosmetic typo "8N_bCL³/c_0" → N_B at l.3403.

# Independent tally of what session 8 adds

**Added, and standing after review:**
1. **Lemma DF** — the dual form of (PW-i) with the exact push-down, and 𝒟_l(Y) = ||(Π_EY)_l||_1. CONFIRMED. Its (iii)
   (co-closedness of c_0(j)) is the new algebra and it is correct. PROOF candidate.
2. **Theorem PW-cc** — the co-closed half of the dual (PW-i), every level, k- and T-uniform. CONFIRMED, uniformity traced
   to its roots. This is the session's one unconditional positive theorem, and it is the right one: by Lemma GE (c) it says
   the Γ_E-response to a co-closed single-level source is the gauge-invariant one and is O(1). PROOF candidate with P8-2.
3. **Proposition RF** — the root-funnel identity. CONFIRMED, exact, and it carries more weight than the file uses (S8-5).
   PROOF candidate.
4. **Proposition TE (identity)** — Π_E(x + Ξ_full(aδ_{c_X})) = Π_Ex + aΞχ^5_X. CONFIRMED; the size is 8L^{3(k−l)} and is
   exact (lane B (f)). PROOF candidate.
5. **Lemma RC** — the funnel-corrected projection Π^♯ and the exact response difference. CONFIRMED; it also establishes
   that a top-anchored **slice** exists (not merely a representative). PROOF candidate with P8-7.
6. **Theorem PW-E** — (GE-T) ⇒ (PW-i)_{Γ_E}, uniform in k and T. CONFIRMED as an implication; vacuous for S_E; valuable
   only as the template of S8-12. Not a PROOF candidate.
7. **Proposition FS and §38.8** — ARGUED, correctly labelled, conclusion right. **The tent half is upgraded by this review
   from ARGUED to essentially proven** (S8-7, P8-9); the spike half stays ARGUED but now has a written transport estimate
   (S8-8, P8-3).
8. **Requirement table MR** — a correct read-only survey. Its real content is the negative one: m_Y's smallness costs
   constants, and the m > 0 gap is the weighted (NC-E), not the rate. CONFIRMED.

**Not added, despite appearances:** nothing. I found no item in §38 that closes the factor k, (PW-ii), (NC-Γ), or D1's
remainder bound while appearing to. The session's self-assessment in §40 is, on this axis, accurate — which is worth
saying explicitly after a session whose headline is a refutation.

**Net direction.** Session 8 converts lane A's position from "(PW-ℓ¹) is a plausible wall" (REVIEW_BFT_A_S7's reading) to
"(PW-ℓ¹) is false in the slice both lanes agreed to use, and the co-closed half is a theorem". That is real progress and it
is correctly signed.

# Verdict on the stand-in transport, and therefore on the one-slice decision

**The refutation does not depend on the stand-in. Reported loudly, as asked.**

1. **The tent half needs no stand-in and no measurement.** The tent coefficient in (GE-T) is ψ_u(X) = (h^{(0→k)}u)(c_X), a
   linear functional of the **given** u, with no representative in it. I computed it exactly for an admissible u and got
   −65/26244 at k = 2, built from same-sign terms φ_1 = −1/432 and φ_2 = −17/104976 with ratio 17/243. Combined with
   Proposition TE (exact), the exact tent size 8L^{3(k−l)}, and λ^E_X(u) = 0 (an immediate consequence of lane B's PROVEN
   16.2 Step 0), this gives **(GE-T) false by a factor ≍ L^{3k}**, with two routine estimates remaining. The Coulomb
   stand-in plays no part in it.
2. **The spike half does rest on the stand-in, and the transport is valid — but the file does not contain the argument.**
   "Plus terms smooth at Z" is not an estimate, and the quantity being transported moves by a factor 3.7 between the
   session's own two representatives. The correct argument is the partition-of-unity one (S8-8): d*a_X = 0 at every
   interior site of Ñ_X (16.2 Step 1, PROVEN), so the only non-co-closed part of S_E's level-0 field carries a difference
   of χ^5, and Σ_Xdχ^5_X = 0 removes the leading term. S_E therefore has **no point divergence** at a non-level-k root and
   lies in S_C0's class. REVIEW_BFT_B_S8 derived the same thing independently. So the transport is sound in substance and
   under-argued in the file; it must be written (P8-3).
3. **Therefore the one-slice decision is well founded.** (PW-i) for S_E fails and PW-E is empty for S_E, for a reason that
   does not reduce to a measurement on a different operator. The lead should however know that the file's **stated**
   reason for the tent half is not a reason, and that the fix makes the case stronger, not weaker.
4. **What the refutation does and does not reach.** It refutes **(GE-T)** outright. It does **not** refute (PW-i) for Y^p
   directly: there the tent coefficient is ψ_{g_0}(X) for the YH piece g_0, which is not explicitly known, and the
   no-cancellation step against Z'' and the bootstrap sum is unwritten. At k ≤ 3 the measured effect is a factor ≈ 2
   (0.866 against 0.445), not L^{2k}. So "(PW-i)_{Γ_E} expected FALSE" remains **ARGUED**, as the session says, and the
   direct S_E run at (T, k) = (5, 2) that both lane B's review and §39 identify is still the check that would settle it.
   My work removes the stand-in from the (GE-T) half only.

# The biggest live wall in lane A

**A representative map that is top-anchored for Y^p and 𝔐^∇-compatible for configurations — and the quantitative evidence
is that no partial funnel correction can be both.** §38.8's tension paragraph (l.3605-3613) states the dilemma; the exact
ratio of S8-7 sharpens it into a dichotomy:

- The **full** correction is Lemma RC's σ(z) = Φ_{l(z)}(x_0)(z). It kills the spike (ba8 C0#: sp_2 → 0.0000), but for a
  configuration with ||∇^cx^c_0||_∞ ≤ η it places a level-0 **point** gradient ≍ L^{2l(Z)}η, which 𝔐^∇ forbids for l(Z)
  near k (l.3607-3608).
- The **partial** correction the session floats — "Moving only φ_1 to level 0 costs ≍ L²η (allowed) and appears to remove
  the dominant part of Y^p's spike" (l.3608-3610) — **does not restore a k-uniform (PW-i)**. It leaves
  Φ_∞ − φ_1 = Σ_{i≥1}φ_{i+1}, which with the exact ratio 17/243 is ≈ 7.5% of φ_1: still nonzero, still level-independent
  in own units, still k-independent. So (PW-i) still fails, merely at l > k/3 + (1/3)log_L(13·C_P/0.023). **Every finite
  truncation of the funnel leaves a level-independent remainder.** (ARGUED, reviewer: it uses the ratio at i = 1 and the
  geometric pattern above it.)
- The two halves have very different prices, and that is the one piece of good news. The level-k **tents** can be removed
  by a gauge that is smooth on scale n: Ξψ̃_u with ψ̃_u an extension of a level-k function costs a coarse gradient
  ≍ Φ_k ≍ L^{2k}η/n² = η, which 𝔐^∇ allows. The intermediate **spikes** cannot, because the level-l roots are only L^l
  apart and the cancelling correction must be point-like at them. (ARGUED, reviewer.)

**So the wall is specifically the intermediate-root spikes, and the live questions, in order:**
1. Does the contraction's linear solve have to meet non-composite-co-closed sources at all? §38.8's alternative
   ("a contraction that only meets composite-co-closed sources up to ∇𝔉-multiplied remainders", l.3612-3613) is "Not
   attempted" and is the only route that sidesteps the dichotomy. Lead decision D1 already points there; **the remainder
   bound it needs is written nowhere**, and Lemma RC's *Reading* says the remainder can reach L^{2k−3}η². That bound is the
   single highest-value missing object in lane A.
2. (PW-ii), which was not attempted and which §38.9 shows fails in S_E by the same mechanism. Without it SR gives the
   factor k back even if (PW-i) were available.
3. A direct S_E measurement at (T, k) = (5, 2) — the one check that moves "(PW-i)_{Γ_E} expected FALSE" from ARGUED to
   measured. Both reviews now ask for it; it needs its own long locked slot.
4. The weighted (NC-E) behind (H-𝔊_w)_k and (W-lin-Π)_m, which §38.10's survey correctly identifies as the real m > 0 gap.

**One cheap target worth a session.** PW-cc covers co-closed single-level sources at every level, k- and T-uniformly. The
dual form (P7-5) says the whole remaining problem is the **non**-co-closed part, i.e. Γ_E^TD(j). Lemma DF already writes
that part as an exact push-down with a co-closed c_0(j) plus residual pairings, and Lemma TD supplies the pairing device
S7 Part 4 recommended. Pushing Lemma DF's decomposition against PW-cc, level by level, with the funnel part paired through
TD, is the one route in §38 that is both written down and untried.
