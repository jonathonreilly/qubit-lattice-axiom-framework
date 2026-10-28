# REVIEW_X7: independent hostile review of session 7 of the YM4D existence lane (§16 and the [RX56-fix] changes)

Reviewer: an independent agent. It wrote none of the reviewed text.

Inputs:
- EXISTENCE.md, byte-identical to EXISTENCE_session7_snapshot.md (`cmp` empty).
  - `diff session6 session7` read in full (614 lines).
  - §12.1-12.2 (l.1331-1390), §14.2 insertions, §15.2-15.7 changed lines and §16 (l.2486-2813) read by offset.
- LOG.md session 7 (l.351-421); REVIEW_X5_X6.md (all).
- checks: x6_criteria.md, x6_sig_free.py, x6_out.txt, x6_time.txt, x6_posthoc_linear.py, x6_posthoc_out.txt,
  x6_posthoc_time.txt.
- Read-only layer 1: ../ym4d-proof/FLOW.md §0, §1, §7-§10 (Theorems F-flow and F-tune); ../ym4d-proof/PLD.md §14.1
  (PLD-AF, (W-F3)) and l.240-246.
- One web search (bibliographic only): Magnen-Rivasseau-Sénéor, CMP 155 (1993) 325-383 (open preprint mp_arc 92-38).

Line numbers are EXISTENCE.md lines unless marked. No file other than this one was edited.

**Re-run conditions.** Under the numeric lock (`until mkdir …/scratchpad/locks/numeric`; acquired 00:50:54 UTC after waiting for another holder; `rmdir` exactly once at 01:05:04 UTC, no trap). nice 10, OMP/OpenBLAS/MKL/vecLib threads 1, `python3` without -I, no `timeout`. Load 3.3 before, 4.2 max, so below 8; 38% of memory free. Output: scratchpad `rerun_x7/`.

**Bottom line.**
- **All 12 RX56 fixes are applied correctly.** §12.1 matches REVIEW_X5_X6 §(7)'s text word for word. Two stale
  sentences around it remain (cosmetic, (1)).
- **Theorem SIG-FREE is CORRECT on a fixed spatial torus** (re-derived, including the closed form c_*(3,1) = 1.929·10⁻⁴).
  One remark is wrong: the single-mode constant c_* tends to 0, not to the continuum integral, as T_m → ∞ (l.2636-2638).
- **Conceptually SIG-FREE is the expected statement about a free field.** In the free model g_0 is the coupling at
  *every* scale. So "g_0 → 0 ⇒ trivial" says only that a Gaussian field whose amplitude goes to 0 is trivial, and
  "g_0 fixed ⇒ non-trivial" says only that the free Maxwell field is non-trivial. In SU(N) Yang-Mills g_0 → 0 is forced
  (layer 1's own Theorem F-tune), and the analogue of the free model's g_0 is the coupling g_m at the observation scale,
  which is produced by the running. The free model cannot speak to whether the running produces that signal.
  - **What SIG-FREE does say about the interacting case is limited and real.** Bounded kernel noise multiplies the
    cross-plane signal by e^{-λ²N_j} and never removes it, for every κ. So the soft machinery is not itself an
    obstruction (reading (c) excluded at the free level).
  - **"(b) is right" is an accurate diagnosis of REVIEW_X5_X6's example.** The "sharper form" ("the decisive parameter
    is the fine coupling g_0") is free-model-only and must say so.
  - **"(a) EXCLUDED" overclaims.** If σ_i ∝ g_0 → 0, the fixed algebra is trivial, and the K-dependent normalisation
    f(·/g_0) restores the g_0 = 1 model exactly. Lemma SIG-1 excludes (a) only when g_0²/σ² → 0 (§2).
- **Lemma RC is correct and compatible with asymptotic freedom.** It is an IVT existence statement per K and does not
  forbid g_0^{RC}(K) → 0. Two texts around it are not compatible with layer 1:
  - The DAG item "(RC) ⇒ liminf g_0 > 0" (l.663, l.2754) is true **only in the free model**. Read for SU(N), it
    contradicts FLOW Theorem F-tune, 1/g_0² ≥ 1/g² + β_-K log L - R → ∞.
  - The "proposed reading" (l.2691-2698) misdescribes layer 1. FLOW's bare coupling *is* the finest term of the chain's
    own effective sequence, fixed by a renormalisation condition (g_K = g, F-tune). It is not a point picked by hand
    from a bracket.
- **Corollary SEP is CORRECT and important.** The soft one-point bounds are saturated by kernel noise.
  - "PLD-AF is the upper half of (F)'s self-consistency" and "(H-sig^♭) is the lower half" are an analogy. Label them
    ARGUED.
  - (H-sig^♭) is a *two-point* lower bound. It is not the lower half of (F); FLOW's F-flow supplies (F)'s lower half
    conditionally, and that gives no correlation lower bound.
- **Proposition SIG-RED: the inequality is CORRECT. Two readings are WRONG.**
  - "In REVIEW_X5_X6's example (TRACK) holds" is false: TRACK's threshold s_0 is 0 there, so TRACK fails.
  - "In the free model it is never the part that fails" is false: for small κ, TRACK fails while (H-sig^S) holds.
  - SIG-RED is a lossy sufficient condition.
  - (H-sig^♭) is well posed only once g_m is fixed (for (H-sig^♭_ren)). It is a known-hard, open statement: the
    non-triviality half of the continuum problem (§5).
- **x6: honestly recorded.** C INCONCLUSIVE (2.4 SE < 5, pre-registered); post-hoc 6.2 SE labelled. Re-run
  identical (deterministic seeds; only wall times differ).
- **Tally: 49 / 1 / 3 / 5 / 12 stands.** No counted item is demoted. ARGUED is 20 (+1: the two-halves reading, now
  labelled).

---

## (1) RX56 fixes

| Fix | Where (session-7 lines) | Verdict |
|---|---|---|
| 1 X-KER^S (iv) framing + free rank-one remark | l.2231-2233, 2255-2261 | CONFIRMED |
| 2 (H-sig^S) OPEN; tally OPEN 12 | l.91-92, 655-658, 2262-2265, 2432-2434, table l.2451, l.2480-2482 | CONFIRMED. §15.6 (I) (l.2418) writes "H^S_ω may be CΩ" without naming (H-sig^S); acceptable, since "Not delivered" names it. |
| 3 "unconditioned free noncompact analogue" | l.84-86, 1912-1913, 1939-1940, 2023-2024, LOG l.276 | CONFIRMED. Pre-stated l.1808-1809 and l.1821 are left alone, as instructed. |
| 4 flat background / SU(2) scope | l.6-7, 93-95, 2169-2170, 2422-2423, 2457-2461, LOG l.320-322 | CONFIRMED |
| 5 GS (iv) 0.0453 / 0.0020 (L = 3); A1 imported | l.1886-1890, 1902-1904, LOG l.272 | CONFIRMED (0.0453² = 0.002052) |
| 6 H-lin^S ⇐ (NA-R2^bg); NA-R2 restricted to SU(2) | l.97, 653, 2182-2186, 2320-2324, 2331, 2450, 2469; LOG l.331 | CONFIRMED |
| 7 H-cont^S-red n := max | l.2278-2282 | CONFIRMED |
| 8 ASSEMBLY (I) | l.2411-2420 | CONFIRMED |
| 9 hypothesis table | l.2440-2451 | CONFIRMED-WITH-FIX: the (F) row's added sentence "§16 shows that the *lower* half of this self-consistency is what non-triviality needs" must be relabelled. See (4). |
| 10 x5 b ≈ 4.1; E1/E2 recorded | l.2348-2366, LOG l.339 | CONFIRMED. "About a quarter" (4.1/15 = 0.27) is right. |
| 11 cosmetic | l.1848-1850; LOG l.201, 216 | CONFIRMED |
| 12 §12.1 word for word; §12.2 retired | l.1331-1371, 1382-1383 | CONFIRMED. The three passages are REVIEW_X5_X6 §(7)'s text verbatim: the inserted soft sentence, the PLD parenthesis and the "not established" list. |

**Cosmetic leftovers (not binding for science):**
- l.1376, in the "changes" paragraph under §12.1, still says "the missing free-field instance of (PLD^mod_dis) is
  stated". Add "[superseded in session 7 by the RX56 parenthesis]".
- l.9, the header, still says "§0-§14 are unchanged except the session-6 lines". It should mention the session-7 fixes in
  §12 and §14.

---

## (2) Theorem SIG-FREE, Lemma SIG-0, Lemma SIG-1

### Lemma SIG-0 (l.2531-2548): CONFIRMED-WITH-FIX (scope of (iv))
- (i)-(iii) re-derived: θ-invariance gives E θ(F)^* = conj(E F); X-KER^S (i) does the rest. The polarisation step in (ii)
  is right.
- **Fix: (iv) is a noncompact statement.** "f(x) ↦ f(x/λ)" has no meaning for SU(N)-valued soft variables. For SU(N),
  read it as "multiplication of an algebra element by a K-independent constant". Add "(noncompact model; for SU(N): a
  constant multiple)" at l.2538.

### Lemma SIG-1 (l.2564-2584): CONFIRMED (mathematics); the reading at l.2582-2584 OVERCLAIMS
- **Re-derived:**
  - ∂_e h = E[f(x + η)⟨Σ^{-1}e, η⟩], and E|N(0, s²)| = (2/π)^{1/2}s.
  - |∇h| = max over unit e of |∂_e h|, so there is no dimension factor.
  - Gaussian Poincaré with ||S|| ≤ g_0² (A1).
  - Sharpness at f = sign: (2/π)arcsin(s²/(s² + τ²)) / ((2/π)s²/τ²) → 1, as in x6 B1.
- **The reading is too broad.** "No normalisation of the observables prevents E[F | fine field] from becoming constant"
  holds only when g_0²/σ²_{j-1} → 0, which is the lemma's own hypothesis. Counter-case inside Theorem SIG-FREE (i):
  - Take σ_i(K) = g_0(K)/√κ with g_0 → 0, i.e. the constant-coupling free chain at a vanishing coupling.
  - The rescaling A ↦ A/g_0 maps it exactly to the g_0 = 1 chain.
  - The fixed algebra is trivial (SIG-FREE (i)), but the K-dependent observables f(Y/g_0) have the K-independent,
    non-trivial OS form of the g_0 = 1 model.
  - There, reading (a) is exactly right. In the free model g_0 is a pure field normalisation, and the only invariant is
    the ratio g_0/σ.
- **Fix (binding).**
  - At l.2582-2584 and l.2659-2660, write "if g_0²/σ²_{j-1} → 0, no normalisation …; if σ ∝ g_0, triviality of the fixed
    algebra is a normalisation artefact (reading (a))".
  - At §0 l.101-103, replace "whatever the kernel couplings and κ" by "for the K-independent algebra, given bounded
    noise; up to K-dependent normalisations the invariant is g_0/σ".

### Theorem SIG-FREE (l.2586-2638): CONFIRMED-WITH-FIX
- **(i)** Re-derived.
  - Var f_η(D) ≤ Λ² tr Cov D ≤ Λ²|X|g_0².
  - The tightness and Lipschitz-approximation step: ||F - F_ε||_{L²} ≤ ε + 2||f||_∞ε^{1/2}, uniformly in K.
  - The O(m/K) rate from the two halves of (F).
  - Scope: the curvature algebra only (torus holonomies excluded). So "H^S_ω = CΩ" means "the curvature-algebra OS space
    is CΩ", and the noncompact RP/OS structure is not re-derived (said at l.2588-2590). Add "(curvature algebra)" to the
    displayed conclusion at l.2591.
- **(ii)** Re-derived.
  - E e^{iλ(Y - Y_θ)} = e^{-λ²(v - c)} and |E e^{iλY}|² = e^{-λ²v}.
  - Independence of η, η_θ and B_0 (ancestors of positive-side variables are positive-side).
  - The k_0-summed lattice Green function, and the bound G_{N_0}(n) ≥ e^{-En}/(2 sinh E) for 0 ≤ n ≤ N_0. Check:
    cosh(a - b) ≥ e^{-b}sinh a.
  - Positivity of every k_s term; the four-mode limit.
  - Reviewer evaluation: c_*(3,1) = (4/27)(2π/3)·0.46774·(0.051561)²/2 = 1.9292·10⁻⁴. This matches x6 A's single-mode
    continuum value 1.92887·10⁻⁴, and the code's single-mode routine implements the same expression.
  - liminf_K c_K ≥ g_*²c_* follows because c_K ≥ g_0(K)²a_K with a_K → c_*.
- **WRONG remark (l.2636-2638).** "c_* tends (T_m → ∞) to the m-independent continuum integral" is false. By its
  definition c_*(T, t_b) ∝ T^{-3}·q ∝ T^{-4} → 0. It is a single-mode lower bound.
  - What tends to the continuum integral is the *full* mode sum c_∞(T, t_b) (x6 A3 at T = 3), a Riemann sum.
  - So the explicit K-uniform bound of (ii) is a **fixed-torus** bound. On the infinite-volume side the lane needs the
    full sum, which is positive termwise, so the conclusion survives.
  - **Fix (binding):** "the full mode sum, not c_*, tends to the continuum integral; c_* → 0 as T_m → ∞".
- **(iii)** Correct. §0 l.101 ("CΩ iff g_0 → 0") should read "iff liminf_j g_0(K_j) = 0" (cosmetic).

### The conceptual point (priority 2)
- **What the free model is.** In the free model the coupling does not run, so g_0 is simultaneously the bare coupling
  and the coupling at the observation scale.
  - SIG-FREE (i) is the statement that a Gaussian field whose amplitude vanishes is trivial. It is expected, and it is
    REVIEW_X5_X6's computation, extended.
  - SIG-FREE (ii) is the statement that the free Maxwell field (block flux variance ∝ g_0², scale-invariant in d = 4) has
    a non-zero cross-plane correlation that bounded kernel noise does not destroy.
- **The interacting case.** In SU(N) the bare coupling must go to 0 (FLOW F-tune: 1/g_0² ≥ 1/g² + β_-K log L - R), and
  the signal at resolution m must be of order g_m because of the running.
  - The free model's g_0 corresponds to g_m, not to the SU(N) bare coupling.
  - Hence SIG-FREE says **nothing** about whether the interacting theory is non-trivial.
  - Its interacting content is negative-space only:
    - (c) the soft layer is not the obstruction, for every κ and bounded noise;
    - Lemma SIG-1's mechanism: a soft observable at scale m is blind if the fine-field signal at that scale is
      o(N_j^{1/2}).
- **"Reading (b) is right": ACCURATE for the example.** The example inserted a running coupling into a model that cannot
  run, and the free model is not self-consistent with β_- > 0.
- **The "sharper form" (l.2662-2663, §0 l.100, LOG finding 2) is free-model-specific.** Add after "the bare coupling of
  the fine measure": "(free model only; in SU(N) the bare coupling → 0 necessarily, and the decisive quantity is the
  noise-free signal at the observation scale, (H-sig^♭))". SIG-RED already says this; the headline must as well.

---

## (3) Lemma RC and the proposed reading (priority 3)

### Lemma RC (l.2675-2690): CONFIRMED (as an existence statement), with one hypothesis made explicit
- **The proof is checked:**
  - continuity in g_0 by dominated convergence on a compact space;
  - g_0 → ∞: the density → 1;
  - g_0 → 0 on a finite lattice: the complement of {all plaquettes within δ of 1} has action ≥ c(δ) > 0, so its
    probability → 0;
  - sup Φ_ref over the shrinking sets → 0 by compactness;
  - IVT.
- **The hypothesis to make explicit.** The proof uses continuity of X-S4c's block map on the **whole** configuration
  space, not only on small fields. State this at l.2676 with its source line in X-S4c.
- **Not given:** uniqueness, monotonicity, and that g_0^{RC}(K) lies in FLOW's admissible range (0, γ]. Say so.
- **Compatibility with AF: YES.** RC is an existence statement for each K. It does not forbid g_0^{RC}(K) → 0, and in
  SU(N) one expects 1/g_0^{RC}(K)² ≈ β_0'K log L + O(log K) (not proven).
- **The free-model remark (l.2688-2690) is correct.** ||Π_exψ||² ∈ (0, 1] by A1, and it is bounded below by the
  zero-separation single-mode term.

### Incompatibilities with the layer-1 flow (FLOW.md, read-only): GAP (binding)
- **"(RC) ⇒ liminf g_0 > 0".**
  - Where: §6 l.663 and §16.4 item 4, l.2754 ("[Lemma RC + remark]").
  - Problem: it is true only in the free model, but the §6 line is ambiguous.
  - For SU(N) it is **incompatible with FLOW Theorem F-tune**, whose tuned bare coupling satisfies 1/g_0² ≥ 1/g² +
    β_-K log L - R, so g_0 → 0.
  - **Fix:** write "free model: (RC) ⇒ liminf g_0 > 0; SU(N): (RC) is expected to give g_0 → 0 (AF), and nothing here
    bounds it below".
- **The "proposed reading" (l.2691-2698).**
  - What it says: "let the Wilson bare coupling be fixed by (RC), not identified with the finest term of the (F)
    bracket … a bracket with β_- < β_+ is too coarse for the bare coupling". That misdescribes layer 1:
    - In FLOW the sequence (g_k) is *the chain's own effective-coupling sequence*: "a deterministic function of (g_0, K,
      L, N, κ)" (FLOW §1), with g_0 the bare coupling at level 0.
    - Theorem F-tune fixes g_0 by the renormalisation condition g_K = g.
    - Corollary F-ll pins the sequence to the one-loop line within R + O(log). The two-loop matching the lane worries
      about is automatic.
    - The bracket β_± bounds the *actual* sequence. It is not a menu from which to pick a bare rate.
  - What survives: the one-loop mismatch mechanism (β ≠ β_1 ⇒ g̃_m → 0 or strong coupling) applies only to a bare
    coupling chosen by hand. Its β < β_1 half is P/PLD.md (W-F3) (cited). Its β > β_1 half is the only addition.
  - **Fix:** replace the proposed reading with "Layer 1 already fixes the bare coupling by a renormalisation condition
    (FLOW Theorem F-tune, g_K = g). (RC) is an alternative condition at a noise-free reference observable. The
    REVIEW_X5_X6 example is the free model run with that tuned SU(N) sequence, which the free model cannot sustain." Drop
    LOG "Next" item "Propose (RC) to layer 1".

---

## (4) Corollary SEP and the two-halves reading (priority 4)

- **Corollary SEP (l.2640-2653): CONFIRMED.**
  - (a) Re-derived. The lower bound E|dB_j|² ≥ N_j ≥ 4g²_{j-1}/κ is pure noise. The upper bound is g_0² + 4.35 max
    g_i²/κ ≤ β̂(1 + 4.35/κ)g_j², using the indexing of (F) with g_K = g.
  - (b), (c) are cited results; triviality is SIG-FREE (i).
  - **It is important.** Every one-point bound in ASSEMBLY (II)-(III) can be carried by kernel noise alone.
- **Scope fix.** It is a counter-model in the free class. So the correct claim is "no implication that uses only these
  properties (model-independently)". Some SU(N)-specific argument might still exist. Add this at l.2648-2649.
- **A stronger abstract fact, which the lane may add.** A θ-invariant measure that is a product across the plane is RP
  with H = CΩ and has arbitrary one-point marginals. So no one-point statement of any kind implies (H-sig^S) abstractly.
  This also settles "either direction" for the implication from one-point to two-point (l.2752) at the abstract level.
- **"PLD-AF = upper half of (F)'s self-consistency": a fair ANALOGY, not a theorem.**
  - PLD-AF is a one-point upper bound with a log loss, relative to the nominal sequence: E s ≤ Cg_k² log(1/g_k).
  - The one-point *lower* counterpart (E s ≥ c g̃_k²) is already in P/PLD.md (W-F3), as an ARGUED perturbative input.
  - (H-sig^♭) is a two-point lower bound, strictly stronger than any one-point lower bound (product-measure model above).
  - (F)'s own lower half (β_-) is supplied, conditionally, by FLOW Theorem F-flow, and gives no correlation lower bound.
- **Fix (binding).**
  - At l.2742-2747, in the table row (F) (l.2446, "§16 shows that the lower half …"), and in §16.6 T20, write: "ARGUED
    (analogy): PLD-AF is a one-point upper comparison with the nominal coupling; (H-sig^♭) is a two-point lower
    comparison; neither is a half of (F), whose two halves FLOW F-flow supplies conditionally".
  - ARGUED +1 = 20.

---

## (5) Proposition SIG-RED, (H-sig^♭), (TRACK) (priority 5)

- **The inequality (l.2705-2713): CONFIRMED.** It follows from the split Cov(θ(F̃ - Φ)^*, F̃) + Cov(θΦ^*, F̃ - Φ),
  θ-invariance, and Var E[F - Φ | U_0] ≤ Var(F - Φ) for Φ U_0-measurable.
- **Well-posedness:**
  - **(H-sig^♭) with a free choice of Φ_K is well posed** but is only meaningful through TRACK, which ties Φ_K to F.
    With Φ_K := F∘𝒮^♭ it is a definite statement. It also needs:
    - the skeleton's support to lie in the open positive half (true for block-local maps; say so);
    - a measurable selection of the mode (stated).
  - **(H-sig^♭_ren) is not well posed as written.** g_m is undefined: (F) only brackets it. Fix g_m as FLOW's effective
    sequence at the tuned g_0 (F-tune), or by (RC) at each scale.
  - **(TRACK) is well posed.** Its threshold is s_0.
- **WRONG readings (binding fixes).**
  - **l.2719-2721, "In REVIEW_X5_X6's example (TRACK) holds".** There s_0 = 0, because the signal → 0, while the left
    side of TRACK is ≈ Λ²|X|N_j, which does not vanish. A strict "< 0" fails, so TRACK **fails**. What holds is the
    tracking *estimate* sd(F - Φ)² ≤ Λ²|X|N_j. Rewrite as "the tracking estimate holds; (H-sig^♭) fails; so the
    degeneracy originates in the Wilson half".
  - **l.2672-2673, "in the free model it is never the part that fails".** This is false. For F = e^{iλY} the left side of
    TRACK is ≈ λ²N_j^{1/2}v^{1/2} and s_0 ≈ λ²c. The ratio does not depend on λ, so TRACK fails whenever
    N_j^{1/2}v^{1/2} ≳ c, i.e. for small κ. Meanwhile (H-sig^S) holds for every κ (SIG-FREE (ii)). Write "SIG-RED is
    lossy: in the free model TRACK needs κ ≥ κ_0(F), although (H-sig^S) holds for all κ".
- **Is (H-sig^♭) known-hard? YES.** It is the non-triviality part of the continuum problem itself: a K-uniform lower bound
  on a connected two-point function of noise-free block observables at a fixed physical scale, across a plane. What is
  known rigorously for 4D non-abelian lattice YM (reviewer's knowledge, open-access sources):
  - **Balaban's renormalisation-group programme** (CMP, 1983-1989) gives UV stability, i.e. upper and lower bounds on
    *partition functions* and effective actions in finite volume. It gives no lower bound on correlations.
  - **Magnen-Rivasseau-Sénéor** (CMP 155 (1993) 325-383; preprint mp_arc 92-38) construct SU(2) YM₄ Schwinger functions
    with a fixed infrared cutoff, in a regularised axial gauge, with Slavnov identities checked non-perturbatively.
    Lifting the infrared cutoff and the full OS axioms are left open. That gives gauge-fixed, IR-cut-off Schwinger
    functions, not the Wilson-lattice block correlations of (H-sig^♭).
  - **Non-triviality (dim > 1, and non-Gaussianity) of a 4D YM continuum limit is not proven in any setting known to the
    reviewer.** It is part of the Clay problem statement.
  - **The plausible route** is the lane's own: a two-sided small-field Gaussian comparison with o(g_m⁴) error, i.e.
    Balaban's finite-volume control extended to correlation functions. On a fixed torus, flat non-trivial connections
    (torons) complicate the small-field expansion.
  - **Verdict:** (H-sig^♭) is correctly OPEN. It is the substance, and it is at least as hard as extending Balaban's
    finite-volume method to correlation lower bounds. No layer-1 hypothesis supplies it; the lane's statement at
    l.2735-2736 is accurate.

---

## (6) Check x6

- **Pre-registration order** (local EDT mtimes): criteria 20:19:58 < script 20:21:58 < out 20:31:57 < post-hoc
  script 20:32:28 < post-hoc out 20:42:48. §16.0 is stamped 00:18 UTC = 20:18 EDT. **Consistent.**
- **A: PASS, honest.**
  - A2's FFT and the transfer formula are two genuinely different codes, agreeing to 8·10⁻¹⁶ and 4·10⁻¹⁵. Both rely on
    ψ_P, which is built from the tent profile of GS-2 (a).
  - The convergence (c(r) - c_∞)/c_∞ ≈ 9^{-r} matches L^{-2r}.
- **B: PASS, honest.**
  - B1 uses the exact Gaussian identities (cos, sin, the arcsin form for sign) plus quadrature for the indicator.
    Maximum ratio 0.9999: the bound is sharp.
  - B2's shapes are right (the cube faces in directions 1-3; Bianchi dim 5).
- **C: INCONCLUSIVE, honestly recorded.**
  - The criteria rule is "PASS iff |z| ≤ 4 in both cases and C1 closed form > 5 SE". C1's closed/SE = 2.4, so C is
    INCONCLUSIVE. The script prints "FAIL", and the lane explains why.
  - **Design note.** With λ = v^{-1/2}, Q ≈ c/(e·v) ≈ 2.7·10⁻⁴ against a per-sample sd ≈ 0.023 (SE·√40000), so 40000 samples could
    not reach 5 SE. A pre-run power estimate would have shown it.
  - C2 cannot discriminate either (SE ≫ closed form).
  - So C gives **no independent evidence** for SIG-FREE's OS quantity beyond the variance term (E e^{iλY} matches to
    4·10⁻⁴). The lane's l.2780-2781 says this.
- **Post-hoc: correctly labelled.**
  - It is ψ-free and noise-free, and it resolves c at 6.2 SE, with z = +0.26 against the r = 1 closed form.
  - It validates ψ_P at r = 1 by an independent route.
  - It does not test the noise's non-crossing, which is structural.
- **The C code is correct as read:**
  - the plaquette Y = B_1(x) + B_2(x + e_1) - B_1(x + e_2) - B_2(x);
  - the reflection pair (p + 1, p - 2) about the coarse plane p, i.e. t_b = 1;
  - the averaging Q_str = L^{-4}ΣΣ;
  - the delta-method SE.
- **Re-run (reviewer, under the mandatory lock):** `x6_out.txt` is identical except the three wall-time fields: A, B and C/D numbers agree digit for digit, including the C1 MC Q = 3.256207e-04 ± 1.14e-04 and "C: FAIL / OVERALL: FAIL" (= INCONCLUSIVE under the criteria). The run took 562 s with a 414 MB peak. `x6_posthoc_out.txt` is identical except wall time (c = 2.967292e-04 ± 4.79e-05, 6.2 SE); it took 288 s with a 31 MB peak.

---

## (7) Verdicts and corrected tally

| Item | Verdict |
|---|---|
| RX56 fixes 1-8, 10-12 | CONFIRMED |
| RX56 fix 9 (table (F) row's new "lower half" sentence) | CONFIRMED-WITH-FIX (relabel ARGUED, (4)) |
| Cosmetic: l.1376, l.9 | stale; annotate |
| Lemma SIG-0 | CONFIRMED; (iv) noncompact-only |
| Lemma SIG-1 | CONFIRMED (mathematics); reading overclaims (σ ∝ g_0 case) |
| Theorem SIG-FREE (i)-(iii) | CONFIRMED (fixed torus; curvature algebra); remark l.2636-2638 WRONG (c_* → 0 as T → ∞) |
| T17 (a) EXCLUDED | GAP: excluded only when g_0²/σ² → 0 |
| T17 (b) | ACCURATE for the example; "sharper form" free-model-only |
| T17 (c) EXCLUDED at the free level | CONFIRMED |
| Corollary SEP | CONFIRMED; scope "model-independently" |
| Lemma RC | CONFIRMED (needs global continuity of X-S4c stated); compatible with AF |
| "(RC) ⇒ liminf g_0 > 0" in the DAG | GAP: free model only; for SU(N) contradicts FLOW F-tune if unqualified |
| "Proposed reading" (l.2691-2698) | GAP: misdescribes FLOW (the bare coupling is already tuned by g_K = g) |
| PLD-AF / (H-sig^♭) "halves" | ARGUED analogy, not a theorem; relabel |
| Proposition SIG-RED (inequality) | CONFIRMED |
| SIG-RED readings ("TRACK holds" in the example; "never fails" in the free model) | WRONG; fix wording |
| (H-sig^♭_ren) | not well posed until g_m is fixed |
| (H-sig^♭), (TRACK) OPEN | CONFIRMED; (H-sig^♭) known-hard |
| x6 A, B PASS; C INCONCLUSIVE; post-hoc | honest; re-run identical (deterministic seeds; only wall times differ) |

**Tally.**
- **Claimed:** PROVEN-HERE 49 / IMPORTED-AND-REVERIFIED 1 / IMPORTED-NOT-YET-REVERIFIED 3 / HYPOTHESIS-NEW 5 / OPEN 12.
- **Corrected: 49 / 1 / 3 / 5 / 12 (unchanged).** The three new counted items (SIG-1 + SIG-0, SIG-FREE + SEP, SIG-RED + RC)
  are mathematically correct. The errors are in readings and remarks. ARGUED is **20** (+1: the two-halves reading,
  previously asserted without a label).
- **Bookkeeping note.** Lemma RC has nothing to do with SIG-RED. Bundling it there is cosmetic, but list it with
  SIG-FREE.
- **Substance:**
  - SIG-FREE and SIG-1 are free-model facts.
  - SEP is a clean separation result (one-point bounds are blind to non-triviality).
  - SIG-RED is a reduction whose Wilson half is the open problem.
  - None of the three adds information about the Wilson measure.

---

## Binding fixes for session 8

1. **l.2636-2638:** c_* → 0 as T_m → ∞. The full mode sum, not c_*, tends to the continuum integral. The explicit bound
   of SIG-FREE (ii) is fixed-torus.
2. **Reading (a):** at l.2582-2584, l.2659-2661, §16.6 T17 and §0 l.101-103, restrict "(a) EXCLUDED" to g_0²/σ² → 0, and
   add the σ ∝ g_0 case (a pure normalisation artefact). In the free model the invariant is g_0/σ.
3. **The free-model-only qualifier:** "(free model only; in SU(N) g_0 → 0 necessarily and the decisive quantity is the
   noise-free signal at the observation scale, (H-sig^♭))". Add it at l.2662-2663, §0 l.100 and LOG finding 2.
4. **"(RC) ⇒ liminf g_0 > 0":** prefix "free model:" at l.663 and l.2754; add "SU(N): (RC) is expected to give g_0 → 0 (AF)".
5. **Replace the "proposed reading" (l.2691-2698)** with the text in (3). Drop "Propose (RC) to layer 1" from LOG Next.
   Credit P/PLD.md (W-F3) for the β < β_1 half of the one-loop mechanism.
6. **Lemma RC:** state that X-S4c's map is used as continuous on the whole configuration space (with its source line).
   Add "uniqueness and g_0^{RC} ∈ (0, γ] not given".
7. **The two-halves reading:** relabel ARGUED (analogy) at l.2742-2747, the table row (F) and §16.6 T20. ARGUED 20.
8. **SIG-RED readings:** at l.2719-2721, "the tracking estimate holds; (H-sig^♭) fails" (TRACK itself fails, s_0 = 0).
   At l.2672-2673, "SIG-RED is lossy: TRACK needs κ ≥ κ_0(F) in the free model".
9. **(H-sig^♭_ren):** fix g_m, either as FLOW's tuned effective sequence or by (RC) per scale.
10. **SEP:** "model-independently". Optionally add the product-measure remark (no one-point statement implies (H-sig^S)
    abstractly).
11. **Scope tags:** SIG-0 (iv) is "noncompact"; the conclusion of SIG-FREE (i) is "(curvature algebra)"; at §0 l.101,
    "liminf_j g_0(K_j) = 0".
12. **Cosmetic:** l.1376 and l.9 are stale.

---

## Strategic verdict: non-triviality for the interacting theory

- **What session 7 established.**
  - The free-model degeneracy was a modelling mismatch: a running coupling inserted into a model that cannot run. It is
    not a defect of soft variables.
  - Kernel noise never crosses the plane and never removes a cross-plane signal; it only damps it. In this sense soft
    variables are a *safe* observable algebra for non-triviality.
  - One-point bounds of every kind (AF-type, PLD, non-Haar) are blind to dim H^S_ω.
  - These are clarifying results, and they close the question REVIEW_X5_X6 raised.
- **What it did not establish, and cannot by these methods.** For SU(N), dim H^S_ω > 1 is exactly (H-sig^♭): the Wilson
  measure has a K-uniform connected two-point function at a fixed physical scale. With the bare coupling tuned by FLOW's
  F-tune (g_0 → 0), the cross-plane signal must be produced by the running. No soft-variable, kernel or one-point
  argument can supply it.
  - This is the non-triviality half of the Yang-Mills existence problem.
  - It is not supplied by Balaban's UV-stability results (bounds on partition functions and effective actions) or by
    Magnen-Rivasseau-Sénéor (IR-cut-off, gauge-fixed).
- **Honest status.** The conditional existence statement of §15.6 still produces, at best, a reflection-positive limit
  whose Hilbert space may be CΩ. The §12.1 sentence "a Hilbert space of dimension greater than one … not established" is
  exactly right and must stay.
- **Next target, in order:**
  1. State (H-sig^♭_ren) with g_m fixed by F-tune.
  2. Attempt the one route that could deliver it: a two-sided small-field Gaussian comparison for block curvatures at
     fixed separation on a fixed torus, with error o(g_m²) at two points. This is the "two-sided W-AF2". First decide
     whether layer 1's (SF)_k package (an analytic polymer representation of the effective action) gives a *lower*
     bound once the large-field contribution is bounded by RLF. Reading the effective-action Hessian u_m as the
     fluctuation scale is exactly the step that needs a lower bound.
  3. Treat (TRACK) as secondary: it fails only at small κ, and κ is a free parameter.
- **What not to do.** Do not count further free-model facts or one-point bounds as progress on non-triviality.
