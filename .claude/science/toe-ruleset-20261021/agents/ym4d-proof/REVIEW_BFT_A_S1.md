# REVIEW_BFT_A_S1: hostile line-by-line review of BFT lane A, session 1 (BFT_A.md, BFT_A_LOG.md, checks/ba1_*)

Reviewer: independent session (did not write BFT_A). Date 2026-10-28 (UTC). Files read: BFT_A.md (all, l.1-329),
BFT_A_LOG.md (all), checks/ba1_criteria.md, ba1_cz.py, ba1_out.txt, ba1_time.txt; REVIEW_S22.md Part 4-5 and fixes
(l.299-499); PROOF.md TOWER-VAR/COMP/COMP-F1 (l.6290-6368), NA-IFT/B-NA-red/(FP♯') (l.3164-3192), NA-alg (l.2995-3010),
Setting N5-bg/N5-cov/Lemma AX (l.5255-5300), (R♯_ω) (l.3505-3520); RTARGET §33-37 (l.572-667); LINEAR_PACKAGE §1-§3
(l.49-204) and headings of §4-§10. Only this file was written in the repo; my scripts and outputs are in the session
scratchpad (`.../scratchpad/revbftA1/`: criteria.md written before r1.py; r1_out.txt; ba1_rerun_out.txt; lock_record.txt).

Verdict vocabulary: CONFIRMED / CONFIRMED-WITH-FIX / GAP / WRONG. Nothing below is counted in PROOF's tally.

## Bottom line

- **Provenance:** filesystem times are consistent with the log; the ba1 pre-registration is real (criteria born 29 s
  before the script, 66 s before the output) and ba1 reproduces bit-identically. Every *ordering* claim inside BFT_A.md
  (§1 "written before §2-§3", §2 "composed before the proofs", "Failure modes ... (pre-stated)", §5 "written after
  §3-§4") is unverifiable or false at file level. The whole file was written in one go after ba1 ran. The false-timestamp
  first draft and the pre-correction text cannot be recovered.
- **BA-2 (COMP-F2): CONFIRMED, and stronger than stated.** The lift also lies outside every *Hölder* curvature ball at
  θ_w = 0, by a factor L^{αk}, so BA-2's "sup norm escape" is no escape in BFT's own norm. The cure, centring at the trivial
  chain, works only on 𝒞_glob, which is a strict subclass of BFT's data class.
- **BA-4/BA-5: CONFIRMED** (algebra re-derived; numerics r1-R1 show the average is O(t³) and r1-R2 that X_0 - Ȳ = O(y³)).
  BA-4's Remark is **WRONG**: pairing the legs is *not* needed for the constant-field cancellation, and unpaired legs
  cancel too (r1-R1u).
- **BA-6: sizes CONFIRMED; the 𝒴^∇ bookkeeping has a GAP.** Two remainder terms are plain level-l currents that 𝒴^∇ has
  no slot for: (∂ρ^{(2)})^Tr_l (and the same structure in (COMM): [A^T, χ]A). In plain-current units they are O(η²)
  *per level*, with no decay, so BFT-A-F2 can come back through them. Separately, (H-lin^∇) with sup-only residual-type
  sources cannot give [∇^cx^c]_α unless α ≤ θ. Fix below.
- **BA-7/BA-8: CONFIRMED** given the Green bounds, which are standard. I re-verified them numerically (r1-R3: uniform
  constants; tail coefficients decrease with N) and sketch the dyadic proof. ba1's A3 does not test the tail.
- **BA-9: CONFIRMED as an implication**, with one ARGUED step: restriction preserves the per-level slice. **Theorem BA:
  CONFIRMED as an implication on 𝒞_glob.** It is B-NA-red re-instantiated in 𝔐^∇ plus BA-9, not BFT-0/1/2 on BFT's class.
  §5 "Net" overstates this.
- **Strategic:** yes, the trivial-background linear estimate is a symbol statement and the right next attack. It is not
  "explicit Fourier and done", though: the norm pair must be fixed first, and it needs a translation-invariant composite
  gauge and LED-unif-type uniformity. Outline in Part 7, including an exact reduction of (G♯-res) by completing the square.

---

# Part 1. Provenance audit

**Filesystem record (APFS birth | modification, local EDT = UTC-4, converted to UTC):**

| file | born (UTC) | modified (UTC) | size |
|---|---|---|---|
| checks/ba1_criteria.md | 04:47:36 | 04:47:36 | 2299 |
| checks/ba1_cz.py | 04:48:06 | 04:48:13 | 4719 |
| checks/ba1_out.txt | 04:48:43 | 04:48:44 | 2878 |
| checks/ba1_time.txt | 04:48:44 | 04:48:44 | 225 |
| BFT_B.md (lane B) | 04:53:54 | 04:53:54 | 10787 |
| BFT_A.md | 04:55:24 | 04:56:30 | 34584 |
| BFT_A_LOG.md | 04:56:48 | 04:56:48 | 1810 |

**What can be trusted.**
1. ba1's pre-registration. The criteria file was born before the script, and the script before the output (APFS birth
   times). The criteria text says "04:48"; the true time is 04:47:36, a harmless rounding. No ba1-named files exist in the
   scratchpad, and the output file's birth time equals the run time. A deleted earlier run cannot be excluded by
   filesystem evidence (a re-created file gets a new birth time). The thresholds are loose (A2: 15%/25%; A3: 1.2, met at
   1.15 by K11), but none of them is post-hoc in the file record.
2. ba1's numbers. My re-run under the lock (05:07:13-05:07:27Z) is **byte-identical** to checks/ba1_out.txt except for
   the timing lines (diff empty; 1.2 s, 0.67 GB).
3. The log's stated sequence (reads to ≈04:47, ba1 at 04:48:43, BFT_A written ≈04:55, corrections 04:56) matches the
   times. BFT_A.md was born 04:55:24 and last modified 04:56:30. The log's "BFT_B.md did not exist at 04:47" is
   consistent with BFT_B's birth at 04:53:54.

**What cannot be trusted.**
1. **Every within-file ordering claim of BFT_A.md.** BFT_A.md was created at 04:55:24 *after* ba1's output (04:48:43),
   and §1-§5 came in essentially one write (66 s of later edits).
   - **BFT_A.md l.18**, "§1 ... (definitions; written before §2-§3)", is a file-order claim contradicted by the log's own
     "ONE write (§1 ... §5)". It must be relabelled "composed before §2-§3 in reasoning; not a file-order fact".
   - **l.48** ("composed before the proofs ... in reasoning") is correctly disclaimed but untestable.
   - **l.93**, "Failure modes to watch (pre-stated)", is **false as a provenance label**. BFT-A-F1..F5 were written in the
     same write as the verdicts on them and after ba1. Read "stated with the results; not pre-registered".
   - **l.292** "(written after §3-§4)" is the same kind of claim and is unverifiable.
2. **The first draft.** The log (l.11-13) says a first draft carried timestamps "04:53-05:05" and "from 05:05". Those
   were wall-clock *future* times when written (≈04:55). It also carried content later corrected in place: C_ρ, BA-8's
   y = 0 term, BA-12's Taylor constant, and the [A^T, χ]A term. Nothing is tracked or snapshotted, so neither the false
   timestamps nor the pre-correction mathematics can be inspected. I take the corrected file as the only object. The
   episode means the session's self-reported timings are reliable only where the filesystem confirms them (the table
   above).
3. **Influence of BFT_B.** BFT_B.md existed from 04:53:54, 90 s before BFT_A.md was written. The log does not say whether
   it was read. BFT_A cites BFT_B only by ownership (l.3-4) and in "FOR OTHER FILES" (l.328), so independence of lane A
   from lane B is unestablished but immaterial to the mathematics.
4. **Statements fitted to ba1.** BA-7 was written after A1-A3 were known. Its mathematics is independent of the numbers
   (verified below), so this does not affect correctness, but ba1 cannot count as a test of a pre-stated BA-7.

**Provenance verdict: ACCEPTABLE WITH RELABELLING (binding fix F1).** The ba1 evidence is sound. The file's internal
pre-statement claims carry no weight and two of them (l.18, l.93) must be corrected.

---

# Part 2. BA-2 / COMP-F2 (l.54-57, 105-118): CONFIRMED, strengthened; cure CONFIRMED-WITH-SCOPE

**Proof check.**
- U0/TOWER-VAR (b) puts V_{k,P}'s holonomy on one level-0 corner plaquette (PROOF l.6303-6305).
- d(U_p, U^lift_p) ≤ Σ_b|X_b| holds by bi-invariance, replacing factors one at a time. Inverted links are fine:
  d(A^{-1}, B^{-1}) = d(A, B).
- The reverse triangle step gives Σ_b|X_b| ≥ ε_P - δ.
- Gauge independence: the argument uses only the two plaquette values, both conjugation-invariant, so it holds for every
  representative of either field (also when only Z, not Z^lift, is re-gauged). Correct.

**Strengthening (record it).** l.115-116 say (CL-1) "holds in the undecayed sup norm (θ_w = 0)". BFT's 𝔐 (REVIEW_S22
l.392-397) is a *Hölder* (X_c-type) curvature norm, and the plain sup-curvature norm is excluded. At the lift, the level-0
own-unit curvature (the θ_w = 0 normalisation) is a spike of height ε_P on one plaquette of coarse diameter L^{-k}, and
zero on its neighbours. Its Hölder/Campanato seminorm, with distances in coarse units at the smallest scale ρ = L^{-k},
is therefore ≥ cε·L^{αk}. (In coarse-unit values, θ_w = 2, the spike is L^{2k}ε, which is BA-2's own bound.)
- So **Z^lift is outside every BFT-admissible 𝔐-ball even at θ_w = 0**, by L^{αk}.
- COMP centred at the lift fails in every norm BFT allows, not only in decaying ones.
- l.113-117 should say this, and the "(CL-1) holds at θ_w = 0" clause should be restricted to the excluded sup norm.

**The cure (C-glob), l.117-118: CONFIRMED-WITH-SCOPE.** Centring at the trivial chain in a global small gauge is
B-NA-red's setting (PROOF l.3178-3180) and is coherent. But 𝒞_glob(ε) = {||B_k||_D ≤ ε in one global gauge} is a
**strict subclass** of BFT's data class (curvature ≤ ε, every torus side ≥ T_0):
- on a coarse torus of side T, a field of curvature ε generically needs potentials of size ~ min(εT, O(1)) in every gauge;
- non-trivial bundles and flux sectors admit no small global gauge at all once εT² ≳ 2π (abelian intuition: quantised
  flux).
So the cure covers BFT only together with the outside-𝒞_glob reduction (BA-11/12 + (UHL) + (SL-cov), OPEN). The
"smooth lift" alternative is ARGUED (l.255-256), not constructed.

---

# Part 3. BA-3 (l.58-59, 120-127): CONFIRMED

- Plaquette: (dx)_p is the difference of two own-differences of parallel links, so |(dx)_p| ≤ 2L^{-2(k-j)}||∇^cx^c_j||.
  The unit conversion ∇^cx^c_j = L^{2(k-j)}·(own difference) is right.
- |q_p| ≤ 9s² is quoted correctly from PROOF l.3512 (A1-NA(1), S6; not re-verified here).
- Soft part:
  - |r_j| own ≤ L^{-2(k-1-j)}η is correct.
  - The commutator s_{j+1}|r_j| ≤ L³L^{-3(k-j)}η² ≤ L²L^{-2(k-j)}η² holds for k - j ≥ 1, with equality at k - j = 1. Fine.
  - BCH₂ is ≤ ½p_L(p_L - 1)s², and l.125 writes ·2s², which overcounts by 2. Harmless.
- θ_w = 2 for BFT-1 follows. Note that BFT-1's "Hölder form" needs the Hölder algebra for q_p, which is ARGUED (table
  l.226).

---

# Part 4. BA-4 / BA-5: CONFIRMED (BA-4's Remark WRONG)

**BA-4 algebra (l.130-138), re-derived block by block.** Word w·s·w̄, where w̄ is w reversed and negated:
- (w, w̄) = ½[D, -D] = 0;
- (w̄, w̄) = -Q_w;
- (s, s) = 0;
- (w, s) + (s, w̄) = [D, Lx̄_μ], linear in d.

L odd and c_X the block centre give avg_yd = 0. Structurally, T = P·S·P^{-1} for a direction-constant field, so
log T = Ad_P(Ltx̄_μ) and the second order is [log P, Ltx̄_μ] at first order in log P, i.e. Lt²[D, x̄_μ]. This is a second,
shorter proof.

The general bound uses |[A, B]| ≤ 2|A||B|: per pair the difference is ≤ 2δ(2|x̄| + δ), giving ½p_L(p_L - 1)δ(2|x̄| + δ).
CONFIRMED.

**BA-4's Remark (l.139-141) is WRONG.** "for unpaired legs Q_w + Q_w̄' ≠ 0" is true per contour, but irrelevant after the
average:
- for a direction-constant field Q_w = ½Σ_{ν before ν' in σ}d_νd_ν'[x̄_ν, x̄_ν'], and avg_y d_νd_ν' = 0 for ν ≠ ν'
  (independent symmetric coordinates of the block), so each leg's second order averages to zero on its own;
- the cross term is ½[D, -D'] with D' = D (same displacement).

So the S4' pairing is **not** load-bearing for the constant-field second-order cancellation. Measured (r1-R1u, SU(2) and
SU(3), all σ, a fixed 5-of-24 subset of σ' per σ): the unpaired average residual equals the paired one, 3.727e-2·t² →
3.727e-3·t² (ratio 1000 between t = 1e-2 and 1e-3, i.e. O(t³)). The per-contour maximum is O(t²) (13.4). The pairing may
matter for the *oscillation* term or beyond second order (c17(B)'s ratio 3.96 is for general fields). Delete or narrow
the Remark.

**r1-R1 (paired), with my own pre-registered criterion.**
- Measured: average residual/t² = 3.73e-2 (SU(2)) and 1.91e-2 (SU(3)) at t = 1e-2, against per-contour 8.0 and 4.1. The
  residual ratio between t = 1e-2 and 1e-3 is 999.9, i.e. residual ∝ t³.
- **My criterion recorded FAIL.** I pre-registered the ratio window [50, 200], which was my error: O(t³) gives 1000, not
  ~100. The other two sub-criteria passed (average ≤ 0.02 × per-contour; per-contour ratio 100.6, 100.9, i.e. O(t²)).
- I record the FAIL as written. The measurement supports BA-4 (second order cancels; the third order survives, as
  ½[log P, [log P, ·]] with avg d⊗d ≠ 0 predicts).

**BA-5 (l.143-150): CONFIRMED.**
- e^{-Ȳ}Σw_je^{Y_j} = 1 + ½Σw(Y - Ȳ)² + O(y³) with Hermitian second order, so M = e^{Ȳ}(1 + H_2 + R_3) is polar to
  O(y³).
- The SU(N) correction: write W = Ue^{-iφ/N}e^{iA}, A Hermitian traceless. Stationarity at A = 0 needs
  sin(φ/N)·tr(AP) = 0, so with φ = O(y³) and P - 1 = O(y²) the maximiser moves by O(y⁵). BA-5's "phase e^{-i arg det/N}"
  step is therefore right to the order needed. (The phrase "differs from the U(N) polar factor by the phase" is exact only
  if P ∝ 1; harmless.)
- r1-R2 PASS (SU(3), 8 contours, 6 seeds; stationarity residual ≤ 6.5e-16): max|X_0 - Ȳ|/y³ = 0.01707 at y = 0.02,
  0.01, 0.005 (constant), and /y² halves with y. So the empirical c_pol ≈ 0.017 on this sample, against NA-alg's 9.2y²
  envelope. Record c_pol as uncomputed, with the measurement as a diagnostic only.

---

# Part 5. BA-6 (l.65-68, 152-169) and (COMM) (l.238-247): sizes CONFIRMED; GAP in the 𝒴^∇ representation

**Sizes, re-derived.**
- δ ≤ 5L·L^{-2(k-l)}η: the ℓ¹ diameter of N(X, μ) is 3(L - 1) + (2L - 1) ≈ 5L - 4.
- s_l ≤ L^{-(k-l)}η, so ½p(p - 1)δ(2s + δ) ≈ 5Lp(p - 1)L^{-3(k-l)}η².
- The commutator ½[x_{l+1}, r_l] is ≤ L³L^{-3(k-l)}η².
- C_6 = 5Lp_L(p_L - 1) + L³ = 1677 at L = 3. Correct.
- Residual-type weight: ω_lL^{2(k-1-l)}κC_6L^{-3(k-l)}η² = κC_6L^{-2}L^{-(1-θ)(k-l)}η². Correct.
- In X_c (δ ≤ 2s): O(1)·L^{θ(k-l)}η² per level, or Ω = k at θ = 0. Correct as an *upper* bound.

**The (CL-2) Lipschitz form (marked ARGUED at l.221-222) follows by polarisation.** BCH₂ is a quadratic form vanishing on
the linear space of direction-constant fields after the S4' average. Its polarisation B(u, v) therefore vanishes on pairs
of constant fields. With u = ū + δu, v = v̄ + δv: |avg B(u, v)| ≤ p_L²(|ū|δ_v + δ_u|v̄| + δ_uδ_v). Since both x and x - x'
carry ∇-control in 𝔐^∇, the difference bound has the same L^{-3(k-l)} decay. This settles the soft-BCH₂ row of
(H-rem^∇) in Lipschitz form at second order. Write it in.

**Attainment in X_c (l.163-165), ARGUED: keep it ARGUED, and qualify it.** The proposed rough configuration x = dλ is pure
gauge at linear order:
- under an *exact* slice with elliptic gauge condition, such configurations are removed;
- in the Feynman-term setting (B-NA-red: the contraction ball is all of X_c), they remain in the ball.
State that the X_c failure is a failure of the *bound* in the Feynman setting, not a proven lower bound on C_2.

**GAP 1: plain level-l currents (l ≥ 1) have no slot in 𝒴^∇ (l.41-43).**
- Two terms are claimed to decay "geometrically":
  - κ(∂ρ^{(2)}/∂x)^Tr_l (table l.229, own size ≤ 2κp_LL²L^{-3(k-l)}η²);
  - the (COMM) term [A^T, χ]A (l.244: CL³L^{-3(k-l)}η/ℓ own).
- Both are **level-l currents that are neither divergence-form G_l nor residual-type**. For example (Q^Tχ - χQ^T)s(b) =
  Σ_cw(b, c)(χ(m_c) - χ(m_b))s(c) is not in Ran Q^T in general.
- In the plain-current coarse units BFT_A itself uses (l.32: j^c = L^{3(k-l)}j), their sizes are 2κp_LL²η² and
  CL³η/ℓ: **O(1) per level, no decay**. Summed against a level-uniform plain-current response, that is Ω = k again:
  BFT-A-F2 re-enters through these two rows.
- The table's "geometric" (l.229) is a statement relative to κQ^Tr_l in own units, not in 𝒴^∇.
- **Fix (binding F3):** add a plain level-l current component to 𝒴^∇ with the weight the linear response actually needs,
  and prove (H-lin^∇) on it. Power count [ARGUED]:
  - with no stiffness of its own at the level-l own scale, the local response to a level-l plain current j is
    ∇x_l ~ j (own);
  - so the 𝔐^∇ components need ω_lL^{(2+α)(k-l)}||j_l||_own (the extra α from [∇^cx^c]_α at the own scale);
  - the two terms then contribute L^{(θ+α-1)(k-l)}, bounded iff **θ + α ≤ 1**.
- Alternatively, prove the representation BFT_A proposes, (Q_x - Q)^Tκr_l. The route: (∂ρ^{(2)})^Tr = B(x, ·)^Tr pairs to
  ≤ p²δ_x|r||ū| with constant fields ū, so it is a divergence of a local field plus a decaying part. The gradient
  (longitudinal) part must be absorbed by the Ward identity of the gauge-invariant functional. ARGUED.

**GAP 2: residual-type sources with sup-only norm cannot give [∇^cx^c_{l+1}]_α unless α ≤ θ.**
- x_{l+1} has no stiffness term of its own. It enters only κ_l||Qx_l - x_{l+1}||² (a mass in own units),
  κ_{l+1}||Qx_{l+1} - x_{l+2}||² (averages only) and the fixing.
- So in the directions with Qx_{l+1} = 0 the response to a rough residual-type source is algebraic:
  x_{l+1} ≈ Qx_l - s_l/κ_l. A level-(l+1)-scale checkerboard s_l is reproduced unsmoothed.
- Then ||∇^cx^c_{l+1}|| ≈ L^{2(k-1-l)}|s_l| is fine, but [∇^cx^c_{l+1}]_α at the own scale is ≈ L^{(2+α)(k-1-l)}|s_l|.
  Against the 𝒴^∇ norm ω_lL^{2(k-1-l)}|s_l| this is a loss of L^{α(k-1-l)-θ(k-l)}.
- **(H-lin^∇) as stated (l.38-43, 207-208) is therefore false for α > θ** [ARGUED from the structure of the chain energy;
  no explicit computation].
- **Fix (binding F4):** either impose α ≤ θ, or add [s^c_l]-Hölder/∇ components to 𝒴^∇. The actual remainder s_l =
  κρ^{(2)}_l has them with decay: its level-(l+1) difference is ≲ p²L^{-(1+α)(k-l)}η² in the weighted units, using
  [∇^cx^c]_α.
- With F3, the admissible window is **α ≤ θ ≤ 1 - α (so α ≤ 1/2)**, or the Hölder-source variant with θ < 1 only.
- BA-6's "θ up to 1" (l.168) must be narrowed accordingly.

---

# Part 6. BA-7 / BA-8 and the imported Green bounds: CONFIRMED (given the bounds); the bounds are standard

**BA-7 (l.171-181).**
- Σ_yK = 0 gives the difference form, and the triangle inequality gives A_α.
- The shell count is ≤ 216j³: the true count is 64j³ + 16j ≤ 80j³.
- Σ_{j≤N/2}j^{α-1} ≤ 1 + (N/2)^α/α, so A_α ≤ 216C_K(N^{-α} + 2^{-α}/α). Correct.
- The scale-by-scale reading (radius ≍ L^j contributes L^{-α(k-j)}) is correct.

Caveats to add:
1. BA-7 bounds **sup of the output only**. 𝔐^∇ needs Hölder (and ∇-Hölder) outputs, i.e. a lattice Schauder/CZ-Hölder
   estimate. That needs |∇K(y)| ≤ C|y|^{-5} as a further imported bound.
2. ba1's "exact norm bound" (criteria l.15) is an upper bound for the operator norm, not the norm.
3. The Campanato ⇒ pointwise-Hölder step (l.179-180) is the lattice Campanato theorem (dyadic telescoping of box means;
   the smallest box is a single plaquette). Standard, as stated.

**BA-8 (l.182-185).** Σ_{|y|_∞≤N}|y|^{-3} ≤ 216N (+1 for y = 0, absorbed since the true shell constant is 80), and
j^c = N³j, F^c = N²F. Correct. Add the scope sentence: for a plain current spread over T coarse units, the bare
|x|^{-3} kernel gives a response growing **linearly in T** (Σ_R R³·R^{-3}). So G♯_0-plain is not a "long-range
correction": it *requires* the chain's screening, and BA-8 is meaningless beyond one coarse unit without it. Similarly,
BA-7 beyond one coarse unit gives log T without screening (G0-F3).

**The imported bounds (l.171), named precisely:**
- (G1) |∇_a∇_bG(y)| ≤ C|y|^{-4}, y ≠ 0, on Z⁴ and on mean-zero tori (|y| the torus distance), for the lattice Green
  function of -Δ;
- (G2) |∇_aG(y)| ≤ C|y|^{-3};
- (G3, needed for the Hölder version) |∇³G(y)| ≤ C|y|^{-5}.

These are standard lattice potential theory. On Z⁴ they follow from the asymptotic expansion of the simple-random-walk
Green function and its difference estimates (Lawler-Limic, *Random Walk: A Modern Introduction*, CUP 2010, Ch. 4; also
Uchiyama, Proc. LMS 1998). I did not check theorem numbers; cite the chapter, not a theorem number.

**Re-verification route (self-contained):**
- The symbols ν_aν̄_b/φ (degree 0), ν_a/φ (degree -1) and ν_aν_bν_c/φ (degree 1) are smooth on T⁴ \ {0}, and Mikhlin
  type at 0 (|∂^βm| ≤ C|p|^{s-|β|}).
- Split m = Σ_jm·ψ(2^jp), a smooth dyadic partition. Integrating by parts M times gives
  |K_j(y)| ≤ C_M2^{-(4+s)j}min(1, (2^{-j}|y|)^{-M}), and summing over j gives C|y|^{-4-s}.
- On the torus the p-sum is a Riemann sum: dyadic pieces with 2^j ≪ N differ from the Z⁴ ones by rapidly decaying
  images (Poisson summation), and the shell |p| ≲ 1/N, with p = 0 removed, contributes ≤ CN^{-4-s} ≤ C|y|^{-4-s} for
  |y| ≤ N/2.

**Numerical re-verification (r1-R3, my criterion; N = 24, 36, 54, 72):**
- the global constants C3 = max|y|³|∇_1G| = 0.17349-0.17350 and ba1's C_K(K12) = 0.4311 are **N-independent** (attained
  near the origin);
- the tail coefficients over N/8 ≤ |y| ≤ N/2 *decrease*: T3 = 0.134, 0.082, 0.068, 0.062; T4(K12) = 0.250, 0.187, 0.155,
  0.137.
- My pre-registered criterion (≤ 15% variation, 36 → 72) **FAILS** for T3, T4 (24%, 27%). The direction is benign: the
  tail coefficients approach their asymptotic angular maximum from above, and the uniform bound holds with the global
  constant.
- Consequence for ba1: **A3 does not test the tail.** max_{y≠0}|y|⁴|K| is attained at |y| = O(1) for K12 (exactly
  0.431125 at every N ≥ 9), so A3 would pass even if the tail coefficient grew like log N up to the near-field value.
  Read A3 as "the near-field constant is stable", and cite r1-R3 or the dyadic proof for the tail.

**ba1 A2 reading.** A_{0.5}(K11) = 1.28, 1.36, 1.41, 1.47 still rises. Fitting A(∞) - cN^{-1/2} to N = 27, 36, 54 gives
increment ratio 0.85 against the predicted 0.84, and A(∞) ≈ 1.74, about 18% above A(54). That is consistent with BA-7's
uniform bound (216C_K/(α2^α) ≈ 0.31·216 ≈ 70 ≫ 1.74), but "depth-uniform" was observed only through a 15% window. Fine
as informational.

---

# Part 7. BA-9, Theorem BA, BA-10/11/12

**BA-9 (l.75-80, 187-203): CONFIRMED as an implication.**
- Unit scaling between depths: potentials L^{-(k-j)}; gradients and residual weights L^{-2(k-j)}; Hölder seminorms a
  further L^{-α(k-j)}. So ||x_{<j}||_{𝔐_j} ≤ L^{-(k-j)}||x||_{𝔐_k} holds.
- The envelope step (ii) needs (FP♯') at depth j for *every* W near U_j (so that Feynman terms vanish along Z_j(W)). That
  is in the hypotheses; say it.
- "The per-level covariant slice is a product of per-level conditions, so restriction preserves it" (l.190) is
  **ARGUED**: the residual groups at level j - 1 are tied to level-j gauges at roots (g_{j-1}(c_X) = g_j(X)), with g_j
  free at depth k and trivial at depth j. Write the slice and check this.

Consequences to record:
1. BFT-0's second bullet (REVIEW_S22 l.407-408: "each U_j is the unique critical point of F_j(·, U_{j+1})", F_j built on
   PROOF's E_j^br) is obtained **only in Balaban's convention** (E^cb replaces E^br). Every downstream lemma proved for
   E^br (BR1, HG1, CURV1_1, LOC_1, HG-ind) must be re-proved for E^cb or shown to coincide with it. That coincidence
   holds only at fixed level (l.199-203). BFT-A-F5 does not occur; correct.
2. "BA-2: the composite component is not near the lift in 𝔐" (l.201) is right, and by Part 2 also in Hölder at θ_w = 0.

**Theorem BA (l.89-91, 205-230): CONFIRMED as an implication on 𝒞_glob.**
- The constants match NA-IFT (PROOF l.3167-3168).
- The enlarged uniqueness ball r_u = min(ρ_0, 1/(4GC)) - s is right: Lip(Φ) = ½ - GCs < 1 there, and uniqueness needs
  no self-map.
- But it is **B-NA-red (PROOF l.3177-3190) re-instantiated** in (𝔐^∇, 𝒴^∇), plus BA-3 (BFT-1), BA-9 (identification)
  and BA-10. Say so.

Corrections:
- (i) §5 "Net" (l.312) "BFT-0/1/2 are reduced to one linear estimate ..." must read "**on 𝒞_glob**". For BFT's class
  (curvature-small data on every torus), add (G♯-patch) ⇐ (COMM) + (UHL) + (SL-cov) + the smooth lift, all OPEN or
  ARGUED.
- (ii) (H-lin^∇)'s sub-items need F3/F4 (Part 5) added.
- (iii) BFT-2 on the complex ball needs the holomorphic continuation of NA-alg's maximiser and of (H-rem^∇). These are
  hypotheses here, and BA-10 is fine as an implication.

**BA-11 (PAR): CONFIRMED** (algebra checked: 𝓛Par = 1 + E, ||E|| ≤ ½, right inverse, finite dimension). The Campanato
remark (l.236-237) holds at scales ≤ one coarse unit ≤ the patch side ℓ.

**BA-12 (CEN1): CONFIRMED** for the affine, direction-constant case (straight leg: Lχ(m_c)x̄_μ after the y-average; legs:
-L∂_μχ·D with avg D = 0). The general crude constant was not checked.

**(COMM) "holds in (𝔐^∇, 𝒴^∇)" (l.246-247): GAP**, by Part 5 GAP 1. The [A^T, χ]A term is a plain level-l current with
no 𝒴^∇ slot and O(1)/ℓ per level in plain units. Lemma AX's L^{k(1-α)} gradient loss (l.252-253) is CONFIRMED: complete
axial gauge gives ∇A ~ Σ over ℓL^k plaquette moves of F-differences, so ∇^cA^c ≲ ℓL^{k(1-α)}[F^c]_α. (UHL) is the
right missing object.

---

# Part 8. Strategic: is (H-lin^∇) at the trivial background a symbol computation? YES in principle; the next attack

At the trivial background every chain operator commutes with coarse translations. The per-level structure is explicit:
Q_root = Q_str - d∘h (LINEAR_PACKAGE §1.2), and straight averages compose exactly (IT-str, Lemma 2.4). The data map
already reduced to closed-form symbols (LED-dual/LED-symb, P̂ = β/φ, R_μ = A_μ + κZ_μ), and uniformity in k and the fine
offset u is LED-unif (Prop 3.7). So (H-lin^∇) at 1 is a statement about the same symbol family. Proof outline:

1. **Gauge.** Use the per-level root slice h(x_l) = 0, in which Q_root = Q_str, with a translation-invariant Feynman term
   on each residual group. Every operator is then Bloch-diagonal: coarse momentum p ∈ (2π/T)Z⁴ plus a level-l offset
   index. This is a choice available on 𝒞_glob and is the main design decision. Check (FP♯') for it (PG^{(k)}/Prop 6.3).
2. **Configuration recursion.** B_l = H_l(B_{l+1}) + (source terms), where H_l is the one-step minimiser map of the
   sub-chain below l + 1. Its effective bottom energy is E_l = (κ/2)⟨r, P^{(l)}r⟩ (LED-dual at depth l), so H_l has an
   explicit Bloch symbol of the LED-symb type with n → L^l.
3. **Residual-type sources (G♯-res) reduce exactly.** (κ_l/2)||Qx_l - x_{l+1}||² - ⟨s_l, Qx_l - x_{l+1}⟩ =
   (κ_l/2)||Qx_l - x_{l+1} - s_l/κ_l||² - const. Substituting x'_{l+1} = x_{l+1} + s_l/κ_l turns s_l into:
   - a residual-type source κ_{l+1}Qs_l/κ_l at level l + 1, smaller in 𝒴 weight by κ̂L^{-1-θ} (geometric if
     κ̂ < L^{1+θ});
   - a Feynman/slice source Γ^TΓs_l/κ_l;
   - an explicit rough shift -s_l/κ_l of x_{l+1}.

   At the top the cascade is a data shift. So (G♯-res) for X_s follows from Theorem 6.8 + N2-exp. For 𝔐^∇ the explicit
   shift is exactly what forces F4 (α ≤ θ, or Hölder sources). This replaces BFT_A's "[ARGUED] REC/KF applies formally"
   (l.262) with an algebraic reduction; the slice inhomogeneity h(s_l) is ARGUED.
4. **Kernel bounds uniform in k.**
   - Each response symbol (to x^c_j, ∇^cx^c_j, r, f_0) is of homogeneous type a ≥ 0 at p = 0 and C^M elsewhere,
     uniformly in the offset. Type a > 0 gives ℓ¹ kernels (Lemma WA).
   - The degree-0 parts (Π_ex, the ∇-of-potential maps) are lattice CZ operators: kernel bounds (G1)/(G3) by the dyadic
     proof of Part 6, giving sup→sup with log (COMP-F1) but Hölder→Hölder bounded.
   - The **new** work is LED-unif's uniformity-in-u argument carried to one more derivative (∇x) and to intermediate
     levels.
5. **Screening (G0-F3, G♯_0-plain).** Beyond one coarse unit, the coarse field is pinned by the data, so the responses at
   coarse momentum are analytic in a strip. That gives exponential decay (the N2-exp mechanism) and removes the long-range
   Π_ex and |x|^{-3} tails. This is a symbol statement too, and it is where BA-7/BA-8's one-coarse-unit restriction is
   lifted.
6. **Schauder at fine scales.** Use LES-div (Lemma 3.2'') locally for C^{0,α} → C^{1,α} at level 0. For soft levels, use
   Part 5's power counts (F3/F4).

**Verdict.** This is the shortest credible path to BFT-0/1/2 **on 𝒞_glob** and should be lane A's next target. It is not
a few lines of Fourier analysis: steps 1, 4 and 5 are each LED-unif-sized. It must start from the corrected pair (F3, F4),
or the estimate being proved is false (Part 5 GAP 2). It says nothing about BFT outside 𝒞_glob, where (UHL) and (SL-cov)
remain.

---

# Binding fixes for the next lane-A session

- **F1 (provenance).** Relabel BFT_A.md l.18 ("written before §2-§3"), l.93 ("pre-stated"), l.292 ("written after"): all
  are "composed in one write after ba1; not file-order facts". Record in the log that the first draft is unrecoverable.
- **F2 (BA-2).** Add the Hölder strengthening (Part 2): the lift is outside every BFT-admissible ball at θ_w = 0 by
  L^{αk}. Restrict "(CL-1) holds at θ_w = 0" to the excluded sup norm. State that (C-glob) covers a strict subclass of
  BFT's data.
- **F3 (𝒴^∇ plain level-l currents).** Add a component for plain level-l currents with weight ω_lL^{(2+α)(k-l)} (own
  sup), or prove the divergence/Ward representation of (∂ρ^{(2)})^Tr_l and [A^T, χ]A. Change table l.229 and l.244-247
  from "geometric"/"holds" to "size proven; 𝒴^∇ representation OPEN; O(η²) per level in plain-current units".
- **F4 (residual-type sources).** Impose α ≤ θ (with F3: α ≤ θ ≤ 1 - α), or add Hölder/∇ of s_l to 𝒴^∇. Narrow BA-6's
  "θ up to 1" (l.168). Restate (H-lin^∇) accordingly; as written it is false for α > θ [ARGUED].
- **F5 (BA-4 Remark).** Delete or narrow l.139-141: the pairing is not needed for the constant-field cancellation (r1-R1u).
- **F6 (BA-6).** Write the polarisation proof of the Lipschitz form (Part 5). Keep X_c attainment ARGUED, and note that the
  rough example is pure gauge at linear order (it is in the ball only in the Feynman setting).
- **F7 (BA-7/8).** Name (G1)-(G3) as above, with the dyadic proof or the Lawler-Limic Ch. 4 citation. Add that Hölder
  outputs need (G3). Read ba1 A3 as near-field only. Add BA-8's linear-in-T statement for bare kernels beyond one coarse
  unit.
- **F8 (Theorem BA / Net).** "BFT-0/1/2 on 𝒞_glob", identified as B-NA-red in 𝔐^∇ + BA-3 + BA-9. Mark the slice-
  restriction step of BA-9 ARGUED. List E^cb ≠ E^br as a downstream re-proof obligation.

## Tally

- CONFIRMED: BA-1, BA-3, BA-4 (body), BA-5, BA-7, BA-8 (given G1/G2), BA-9 (implication; one ARGUED step), BA-10, BA-11,
  BA-12 (affine case).
- CONFIRMED-WITH-FIX: BA-2 (stronger than stated), BA-6 (sizes), Theorem BA (scope).
- WRONG: BA-4 Remark.
- GAP: 𝒴^∇ representation of two remainder/commutator rows (F3); (H-lin^∇) in the stated pair for α > θ (F4); (COMM) as
  stated.
- Checks: ba1 re-run identical (A1-A3 PASS reproduced). Mine (r1): R1 FAIL by my own miscalibrated ratio window
  (measurement supports BA-4); R1u informational (refutes the Remark); R2 PASS; R3 FAIL by my convergence window (benign
  direction; uniform bound supported).
- Lock: acquired 05:07:13Z (load 1.90, 45% free), released 05:07:27Z by one rmdir. nice 10, thread variables 1, python3
  without -I, no timeout, no process left.
