# REVIEW_S5_S6: independent hostile review of sessions 5 and 6

Reviewer: an independent agent that did not write the proof.

Inputs:
- PROOF.md, which is byte-identical to PROOF_session6_snapshot.md (checked with `cmp`).
- `diff PROOF_session4_snapshot.md PROOF_session6_snapshot.md`.
- LOG.md, sessions 5-6.
- REVIEW_S4.md.
- literature/NOTES.md §1-10.
- Checks c16, c17, c18 and c18b, all re-run.
- Primary sources:
  - CMP 109: text extraction, plus page images of PDF pp. 11, 12, 18 and 19 rendered for this review;
  - Dimock arXiv:1212.5562, 1304.0705, 2009.01156 and 2204.07201;
  - Dimock's Rome lectures;
  - BFKT arXiv:1609.00968.

PROOF.md, LOG.md, the snapshots and the checks were not edited.

**Bottom line.**
- All 9 new PROVEN-HERE items survive. None is WRONG.
- Five need substantive fixes (L4a-Π also has a typo):
  - A1: the sharpness wording;
  - A2: the scope of its E8* corollary;
  - A1-NA(1): the proof of (c), and the branch convention;
  - A1-NA(k): it is proven for S4' iterates, not for Balaban's M^k;
  - LF-count: the interpretation.
- The arithmetic of LF-count is right.
- Its interpretation has three problems:
  - it mixes coupling normalisations, off by a factor 2N;
  - it states a conditional ("every small-field threshold") as fact;
  - LOG overstates it as an "iff".
- Two non-PROVEN statements are wrong:
  - the claim that our torus satisfies CMP 109's side 2L^m;
  - the "iff" in LOG.
- One narrowing is a GAP: "(1.2) is exactly L1e's hypothesis". L1e is proven for S4/S4' only, and Balaban's (0.4)
  pairs independently.
- Every citation spot-checked (17) is accurate. Nothing is fabricated.
- No PROVEN-HERE argument uses an IMPORTED-NOT-YET-REVERIFIED lemma as a premise.
- c18b's post-hoc status is honestly disclosed. However, neither c18 nor c18b tests A1-NA(1) in its own regime near
  the extremal constant.

## [R4-fix] audit

All six REVIEW_S4 fixes are applied:
- E8*-sup and E8*-k: domain τ_N/2, the c → 2c alternative C_1 = L² + 8cA_L, and the condition t ≤ C_1τ_N/2. Re-checked:
  sin(π/N) < 1/45.39 ⇔ N ≥ 143, so "N ≳ 140" is right.
- E8*-ob scope.
- L9a bounded-measurable scope.
- H1: SU(2) only.
- c15 downgraded, with the poor b²/j³ fit reported (j = 1, 3) and the bookkeeping-identity wording.
- FILS [v-R4] pp. 1-34; Dimock 2009.01156 confirmed.

## (1) New PROVEN-HERE items (30 → 39)

**Inequality (B) [S5] (PROOF.md l.1138): CONFIRMED.**
- ||1 - U||²_HS = 2N - 2 Re tr U, and HS ≥ op. This is elementary.
- Counting it as a PROVEN item is bookkeeping, as the tally says.

**Lemma E8\*\*-dens [S5] (l.1120-1137): CONFIRMED.**
- n_ℓ = d|Λ_m| = d(4L^{M+m})^d = d2^d n_c, with n_c = (2L^{M+m})^d (E8*-red l.1061).
- The bound is pointwise: on the event, Π_C w_C ≤ ω^{n_c}, and Haar mass is 1. Cell disjointness is not even needed.
- Gibbs case: by (B), bad ⇒ s(V_P) ≥ η²/(2N), so ω = e^{-aη²/(2N)}. Correct.
- Note: it is a reduction to a hypothesis (D_m) with a K-uniform C_+, which is where all the difficulty sits. The text
  says so (l.1326-1328).

**Lemma A1 [S5] (l.1139-1166): CONFIRMED-WITH-FIX.**
- (i) Re-derived. Pair link 2 at y + Le_μ, link 3 at y + Le_ν and link 4 at y, all with the same σ. The axial legs at
  c_{X+μ}, c_{X+μ+ν}, c_{X+ν} and c_X cancel pairwise in the linear sum. What remains is ∂sq_y. Averaging over σ is
  then trivial.
- (ii) Schur test re-derived. The row sum is L^{-d}·L^d·L² = L². For the column sum: given a fine plaquette p, each
  (a, b) ∈ [0, L-1]² fixes a unique y. That gives L² triples, so the column sum is L^{2-d}. Hence ||M||² ≤ L^{4-d}.
- The Dimock cross-check is verified: 2009.01156 eq. (7), p.2, gives e_k = L^{k/2}e_0, so e_k² = L^k e_0².
- **Fix (l.1143, "equality attained by the constant mode").** A constant F is closed, but on the torus it is not in
  Ran d for real A, because its total flux through a coordinate 2-torus is nonzero.
  - For real A: "the constant L^{4-d} is the supremum over torus sizes, approached by long-wavelength modes; equality is
    attained for compact U(1) with a quantised constant flux inside the principal branch".
  - The same caveat applies to "equal action at every level" (l.1158): it holds for the quadratic action only. c18b
    shows that the cos-action ratio of that mode is 0.81.

**Proposition A2 [S5] (l.1167-1189): CONFIRMED-WITH-FIX.**
- Re-derived:
  - ||C|| ≤ β^{-1}‖M_R‖² ≤ β^{-1};
  - det(1 - 2sC)^{-1/2} ≤ 2^{r/2} at s = β/4;
  - Markov gives e^{-β|R|η²/4}2^{r/2};
  - n_pc = C(4,2)·2² = 24, so 2^{12} = 4096.
- The "one family" restriction is not used; the bound holds for any disjoint cells.
- **Fix (l.1173, "Through E8*-red(ii) this gives E8* at every depth").** E8* and E8*-red(ii) are statements about the
  compact S4''/S4' steps and their domain events. In the noncompact Gaussian model the averaging is linear and has no
  domain.
  - Either define E8* for the model through the compact embedding U = e^{iA}, and check that the domain events of the
    compact steps are controlled by the linear F^(m) (they are while every flux is in the principal branch, which is
    itself an E8*-type event);
  - or restrict the claim to "E8** (in the |F^(m)_P| ≥ η form) at every depth".
- The E8** half stands as written. The badness notion is compatible: ||1 - e^{iF}|| ≤ |F|.

**Lemma L4a-Π [S6] (l.661-710): CONFIRMED-WITH-FIX (typo only).**
- Every step re-derived:
  - midpoint covariance Π̃(εp) = ε_με_νΠ̃(p);
  - reality plus evenness;
  - A_μν = aδ_μν;
  - Q_μν = cp_μp_ν (μ ≠ ν) and Q_μμ = bp_μ² + eΣ_{κ≠μ}p_κ²;
  - (G) in the form Σ_νΠ̃_μν s_ν = 0, with the phase e^{ip_μ/2} factored out. This is correct. Derivation:
    Σ_ν Π̂_μν(e^{ip_ν} - 1) = ie^{ip_μ/2}Σ_ν Π̃_μν s_ν;
  - order p gives a = 0; order p³ gives b = 0 and c = -e;
  - β = -∂_1∂_2Π̃_12(0) = Σ(z_1 + ½)(z_2 - ½)Π_12, which equals CMP 109 (1.22).
- The scalar (δ_ab) form of Π is justified by CMP 109 (1.21), as transcribed in NOTES §9.4. The lemma should cite it.
- **Fix (l.702).** The uncentred transform is Π̂_12 = e^{**+**}i(p_1 - p_2)/2 Π̃_12, not e^{-i(p_1-p_2)/2}. This is
  harmless, because Π̃_12 = O(p²) either way.
- Scope is stated correctly: the algebra only. Nothing about β_j for the actual RG step.

**Lemma B-avg [S6] (l.233-238): CONFIRMED.**
- Conjugation identity: log(TS^{-1}) = S log(S^{-1}T)S^{-1}.
- Verified against the page-image transcription of (0.4):
  - G(y,x) holds one contour per order of the nonzero coordinates;
  - so a uniform average over the d! orders σ equals a uniform average over the distinct contours (multiplicity
    d!/k!).
- So (0.4) is S4' with independent pairing, as stated.

**Lemma A1-NA(1) [S6] (l.1199-1261): CONFIRMED-WITH-FIX.**
- Re-derived:
  - (BCH) with 9s². Submultiplicativity of HS gives |Y - Σx| ≤ e^s - 1 - s ≤ s². Then |log(1+Y) - Y| ≤ 2|Y|² ≤ 8s².
    The power series is the principal log because ||Y||_op ≤ ½.
  - Axial gauge on the 2L × 2L × L^{d-2} box: ≤ (d-1)·2L conjugated plaquettes per link. The telescoping is
    unitarily invariant in HS. The log bound holds in HS once each eigenvalue distance is ≤ ½.
  - |Z_y| ≤ (d+2)L links.
  - Λ_P = avg_y Σ_{sq_y}(da)_p, because A1(i) is a scalar-coefficient linear identity and so holds for su(N)-valued a.
  - The row/column Schur restriction to R.
  - n_W ≤ 4·C(d,2).
  - C_6 = L^{4-d} + 2C_4²n_W, from (1+φ)u² + (1+1/φ)v² with φ ≤ 1.
  - The step-6 sandwich.
- The proof also holds for (0.4), because the path counts and the linearisation are the same.
- **Fix 1 (l.1250, proof of (c)).** "Contrapositive of (b) together with the lower bound of step 6" does not prove the
  first alternative. Step 6's lower bound needs every |θ_j| ≤ φ, which fails exactly when |X_p| > φ_0.
  - Correct argument: t ↦ 1 - cos√t is concave on [0, π²]. So with Σθ_j² > φ_0² (φ_0 ≤ π) the minimum of Σ(1 - cos θ_j)
    is at a vertex: N s(U_p) ≥ 1 - cos φ_0 ≥ (φ_0²/2)(1 - φ_0²/12).
  - The SU(N) constraint Σθ_j = 0 only shrinks the feasible set. The claimed bound is therefore true; insert this
    argument.
- **Fix 2 (l.1203, branch convention).** "X_p = log U_p (principal)" must use arg ∈ (-π, π], not the S4'' odd branch
  rule. Under the odd rule, a plaquette with eigenvalue -1 gets X_p = 0. It would then satisfy φ_R ≤ φ_0 while
  s(U_p) ≥ 2/N, which breaks (b) and (c).
- **Fix 3.** State the norm conversion used in A1-NA(k). c_N = c√N, because |log V|_HS ≤ √N||log V||_op ≤ c√N||1 - V||_op
  for ||1 - V||_op ≤ ½. Also add the hypothesis "level-m torus side ≥ 3 coarse sites" so that W_P does not wrap. S4
  [S4] gives side ≥ 4, so this holds; c18's coarse side 2 violates it, which is harmless for a check.

**Corollary A1-NA(k) [S6] (l.1270-1290): CONFIRMED-WITH-FIX (scope).**
- Re-derived. L1e(b) gives the level-(j+1) plaquettes φ_{j+1} = c_N(1 + 4C_δ)F L^{-2(j+1)} ≤ φ_0 when F ≤ F_1. The
  product of steps from i = j+1 ≥ 1 is bounded by exp(C_6c_N(1 + 4C_δ)F/(L² - 1)).
- The "wall for fluctuating fields" (l.1285) is right: g_j ~ n^{-1/2} under (0.31), so Σg_j = ∞.
- **Fix (l.1271, l.1281-1284, l.1706, l.14).** The corollary is proven for **S4' iterates**. Two of its readings go
  further:
  - "Balaban's background domain (1.2)";
  - the minimiser reading A_coarse(V) ≤ e^{C_7F}A(U_k(V)).
- Those readings apply it to V = M^k(U_k(V)) with Balaban's M, i.e. (0.4) with independent pairing. L1e is not proven
  for (0.4).
  - The ribbon step (l.284-289) uses that γ + s_je_μ is the translate of the SAME-order path. With σ ≠ σ' the loop is
    the ribbon times a loop formed by two axial paths with the same endpoints.
  - That is still bounded, with C_A replaced by roughly 2C_A, but it is not written.
- Further caveat: Balaban's |·| uses the normalised trace (tr 1 = 1). Then "exactly L1e's hypothesis" holds only up to
  the √N norm conversion.
- Either re-prove L1e for (0.4) or keep the reading restricted to S4'. Both are needed for decision 4 (l.1758) anyway.

**Proposition LF-count [S6] (l.1292-1328): CONFIRMED-WITH-FIX.** The arithmetic is right; the interpretation has one
WRONG number and two over-statements. See (5) below.

**Not a PROVEN item, GAP: L1d [S6] narrowing (l.240-250, header l.14).**
- "L1d(i) ... is now covered on Balaban's own domain ... That is exactly L1e's hypothesis F ≤ F_0." This inherits the
  A1-NA(k) scope problem: L1e is for S4/S4', not (0.4).
- Fix: "covered for S4' iterates, up to the √N norm conversion; for (0.4), L1e needs the two-axial-path ribbon variant
  (OPEN, easy)".

**Not a PROVEN item, WRONG (minor): L4a-form hypothesis check (l.653).**
- The text says "Its hypotheses do hold in our setting where they can be checked: ... torus side 2L^m". That is false.
  - Since session 4 our fine side is 4L^{K+M}, i.e. unit-lattice side 4L^M.
  - 4L^M ≠ 2L^m for odd L.
- Fix: "Balaban's torus has side 2L^m; ours 4L^M. Whether his proofs are side-agnostic is [unverified]". Also: "L odd >
  11", where our L1e needs L ≥ 9 and the checks use L = 3.

## (2) Citations and transcriptions

17 spot-checks against the primary text. All are accurate in content and page.

| # | Claim in PROOF.md / NOTES | Source location | Verdict |
|---|---|---|---|
| 1 | "simplifying assumption that integrals are restricted to small fields" | CMP 109 p.250 | exact |
| 2 | "(in fact they are dimension-independent)" | CMP 109 p.250 | exact |
| 3 | "L is an odd, positive integer > 11" | CMP 109 p.251 | exact |
| 4 | "all results of the paper [12] are valid"; "not interesting enough" | CMP 109 p.254 | exact |
| 5 | Theorem 1, no asymptotic freedom assumed | CMP 109 p.259 | exact |
| 6 | d = 3: g_k² = g²L^kε | CMP 109 p.259 (image) | exact |
| 7 | Theorem 2, SU(2), 0 < β ≤ β', (0.31) | CMP 109 p.259 (image) | exact; log(L^kε)^{-1} = (K-k)log L is correct |
| 8 | "A proof ... will be given in a separate paper"; "superficial" | CMP 109 p.259-260 | exact |
| 9 | (1.2); "By Proposition 2 [12] ... < 2ε_0" | CMP 109 p.260 (image) | exact |
| 10 | (1.18), with no power of g | CMP 109 p.263 | exact |
| 11 | Theorem 3 constants | CMP 109 p.264 | exact |
| 12 | (2.9), fixed ε_1, alternative g_k/γ_k ε_1 | CMP 109 p.266 (image) | exact |
| 13 | "In the next paper we will construct such localizations" | CMP 109 p.298 | exact |
| 14 | "This difficult step is not necessary for this model" | Dimock II p.31, Remark 3 | exact |
| 15 | Lemma 13 eq. (166) (p.24); Lemma 20 (p.35) | Dimock III | correct pages and equations |
| 16 | Lemma 23 eq. (471), p.64; "There are no marginal terms" | Dimock QED p.64; overview p.13 | correct |
| 17 | Rome p.39 (224)-(228), "bounded uniformly in N for n_0 ≥ 7"; BFKT p.4, "routine" | Rome lectures; BFKT | exact |

- (2.10), p.267 (image), confirms that the fluctuation action is (1/2g_k²)⟨H_1B', Δ_1H_1B'⟩ with B' unscaled. So
  "the excluded fluctuations cost ~ε_1²/g_k²" (l.763) is right **in Balaban's normalisation**.
- No fabricated or misattributed claim found.
- The OSTI 120:575-612 vs 122:355-392 discrepancy is correctly left unresolved.

## (3) Status labels

- No PROVEN-HERE item takes an IMPORTED-NOT-YET-REVERIFIED lemma as a premise.
  - LF-count takes (0.31) (L4a-flow) as a hypothesis of a conditional statement. That is legitimate.
  - The A1-NA(k) minimiser reading is labelled conditional on L2.
- **Violation (l.767; also l.1707).** "This includes every small-field threshold ε_1" is stated as fact in L5 [S6] and
  in the tally. It rests on two things:
  - β' ≈ the perturbative rate, labelled [inference] only at l.1307, and an L4a-flow / L4b identification that is not
    re-verified;
  - the unquantified "ε_1 sufficiently small".
  Tag it [inference] at both places.
- The tally counts (B) and B-avg as items "for bookkeeping". Of the 9 new items, 6 are substantive: A1, A2, E8**-dens,
  L4a-Π, A1-NA(1) and A1-NA(k). LF-count is arithmetic.

## (4) Checks re-run

Setup: laptop, nice 10, OMP/OpenBLAS/MKL/vecLib threads = 1, load 2.3-2.8, 34% free memory, sequential runs. Outputs
are in the scratchpad `rerun_s56/`.

| Check | Result | Time | Peak RSS | vs stored |
|---|---|---|---|---|
| c16 | 11/11 PASS | 3.1 s | 68 MB | identical |
| c17 | 8/8 PASS | 0.5 s | 39 MB | identical except the runtime line |
| c18 | 6 PASS / 2 FAIL | 11.5 s | 423 MB | identical to c18_out_firstrun.txt except the runtime line |
| c18b | 1/1 PASS | 6.4 s | 424 MB | identical except the runtime line |

- **c16.** A genuine test of A1(i) (an identity, to 1e-14) and of ||M||² = L^{4-d} exactly, for one plane. The random
  fields (ratios 0.001-0.06) and the d = 2 two-step run (0.09) are far from extremal. Pre-registered, first run.
- **c17.** Part A tests the Fourier algebra on abelian loop-squared functionals, for which (G) holds by construction. It
  cannot test whether the RG-generated Π satisfies (H) and (G), which is not claimed. Part B is a correct test of the
  conjugation identity and of the second-order pairing difference (ratio 3.96).
- **c18.**
  - Criterion (ii) FAILED as pre-registered. The FAIL is kept, the first-run file equals the stored output, and the
    "ill-posed" explanation is right: seed 2 changes sign between t = 0.04 and 0.08.
  - The data are consistent with an O(φ) non-abelian correction (the cubic f^{abc} term). But the lemma claims an upper
    bound, not a rate, so (ii) never tested the lemma.
  - Criterion (i) is vacuous: R ≤ 0.043 against a bound of 1.
  - So c18 does not test the load-bearing step: the leading constant 1 plus C_6φ near the extremal mode. This is
    disclosed (l.1262-1263).
  - φ is the op norm θ/2, while the lemma uses HS (√2 larger for SU(2)). This is minor.
- **c18b.** The post-hoc status is honestly disclosed in the docstring, PROOF.md and LOG. However:
  - (a) The configuration is **outside the lemma's hypothesis**. The coarse plaquette angle is π/2: 9 × 0.1745 per
    eigen-angle. The BCH condition s_P ≤ ¼ at the coarse level needs φ ≲ 1/(4·L²·const), far below the fine 0.17.
  - (b) R(0) = 0.81 < 1 is the cos nonlinearity at angle π/2, not a near-extremal ratio.
  - (c) The PASS criterion "C < 10" is effectively unfalsifiable.
  - Fix l.1265: "outside the small-φ regime of A1-NA(1); not a test of the lemma".
- **Missing check (binding).** Test A1-NA(1) in its regime: small φ, near-extremal, coarse side ≥ 3. A d = 2 or d = 3
  SU(2) run with a small constant τ_3 flux plus a non-abelian perturbation, L = 3, coarse side 3-4, is cheap. In d = 2
  the target ratio is L² + O(φ); in d = 3 it is L + O(φ). Pre-register R ≤ L^{4-d}(1 + Cφ) with C reported.

## (5) Proposition LF-count: arithmetic and inference

**Arithmetic: CORRECT.**
- N_k = (L^kε)^{-4}M^{-4}|T| = L^{4(K-k)}M^{-4}|T|.
- w_k ≥ e^{-a/g_k²} ≥ e^{-a/g²}L^{-aβ'n} with n = K - k. So C_K ≥ e^{-a/g²}Σ_{n=0}^K L^{(4-aβ')n}, which diverges for
  aβ' ≤ 4: geometrically for aβ' < 4, linearly for aβ' = 4.
- The converse, with β, is right.
- d = 3: g_k² = g²L^kε (CMP 109 p.259, image) gives L^{3n}e^{-aL^n/g²}, which converges double-exponentially.
- The instanton product is aβ' = 8π²·11N/(24π²) = 11N/3. Its normalisation is consistent.

**Inference: CONFIRMED-WITH-FIX.**
- **WRONG as stated (LOG l.368): "diverges iff aβ' ≤ 4".** Only "if" is proven. Convergence is proven for aβ > 4. For
  aβ ≤ 4 < aβ' the proposition is silent unless the actual rate is known. PROOF.md's claim is stated correctly.
- **WRONG numbers (l.1307-1308): normalisation mixing.** CMP 109's action is (1/g_k²)Σ[1 - Re tr U] with tr 1 = 1
  (NOTES §9.1). So 1/g_B² = 2N/g_std², and (0.31)'s perturbative β' is β'_B ≈ 2N·2b_0 = 4Nb_0 = 0.0929N², not 2b_0.
  The same 4Nb_0 appears in the R3 numbers.
  - The cost a = ½||Δ||ε_1² (l.1305) is in Balaban's normalisation, since it comes from (2.10).
  - So the threshold is a_B > 4/(4Nb_0) = 43.1/N²: 10.8 for SU(2), 4.8 for SU(3).
  - The text says "a > 86/N, i.e. a > 43 for SU(2)", which is a factor 2N too strict.
  - With ||Δ|| ≈ 16, divergence needs ε_1 ≲ 1.16 (SU(2)) or 0.77 (SU(3)), and the bound falls like 1/N.
  - So the qualitative conclusion survives only in the sense "for ε_1 sufficiently small", which is what Balaban
    assumes. "Incompatible with a small-field threshold" is not shown for O(1) thresholds. At large N the per-bond
    "cheapest configuration" estimate also ignores the N² fluctuation entropy.
  - Redo l.1305-1311 in one normalisation, stating the dependence on ||Δ^{(k)}||.
- **Over-statement (l.767, l.1707): "every small-field threshold".** Divergence along the true flow needs the true rate.
  (0.31) supplies only some β' ≥ the true rate. So the unconditional form requires L4a-flow plus the perturbative
  identification, neither re-verified. Restate it as: "for every ε_1 below an explicit bound, conditional on the
  one-loop rate [inference]".
- **The substance holds.** Even granting the fixes, the inference "unrenormalised per-level large-field bounds cannot be
  summed in 4D at small-field thresholds, so large-field contributions must themselves be renormalised" is sound. It
  matches three sources:
  - the CMP 122 I abstract [read-abs]: R removes "the main obstacle";
  - Dimock II p.31 Remark 3;
  - the Rome p.39 contrast, whose convergence comes from the geometric e_k.
- **The "[heuristic] dense" paragraph (l.1312-1314).** It is fair at fine scales in physical units. Per level-k lattice
  cell the excursions are rare (density e^{-a/g_k²}). So an isolated-cube model is locally reasonable.

## (6) Strategy

**Progress.** Sessions 5-6 are better than "circling". A1, A2, A1-NA(1) and A1-NA(k) are real tree-level theorems.
L4a-Π re-verifies the β-definition algebra. Reading CMP 109 removed two false beliefs:
- "β_j → 2b_0 ln L is in CMP 109";
- "CMP 109 proves Theorem 3": it defers the localisation to CMP 116.

But no IMPORTED item moved. The quantitative content of UV stability, L5 and L6, is untouched.

**Next target: the "one-cube R-operation" (Next item 2). CONDITIONAL GO, redirected.**
1. **Smaller testbed first.**
   - Balaban states that CMP 109's results hold for the 2D nonlinear chiral models, and were obtained there first
     (p.260).
   - He treats the large-field R-operation for N-vector models in CMP 198 (1998) 493-534.
   - The d = 2 analogue of LF-count diverges too: N_k ∝ L^{2(K-k)}, so the condition is aβ' ≤ 2. The wall is
     therefore present there.
   - Do the one-cube construction for a 2D asymptotically free σ/chiral model before 4D SU(N), and add CMP 198 to the
     owner request.
2. **Pre-state the target inequality before deriving.**
   - Name the counterterms subtracted inside the cube: the vacuum energy E^{(j)}(1) / log Z^{(j)}(1) and β_jA.
   - State the claimed bound on the field-dependent remainder: (L^kε)^{4+α}·w_k with w_k ≤ e^{-a/g_k²}.
   - State why the constant part may be moved into the vacuum energy uniformly in K.
   - A failure with the exact wall named is a valid outcome, as stated.
3. **CMP 122 remains decisive.** Keep the owner request first. A reconstruction that later disagrees with CMP 122 costs
   more than waiting.
4. **Fix before building on it:**
   - L1e for (0.4), or decision 4 (adopt (0.4) vs S4'). The A1-NA(k) minimiser reading depends on it.
   - The A1-NA(1) regime check from (4).

## Required fixes (binding for session 7)

1. **A1-NA(1)(c), l.1250.** Replace "contrapositive ... lower bound of step 6" with the concavity argument (1 - cos√t
   is concave; vertex minimum; Σθ_j = 0 only shrinks the set).
2. **A1-NA(1), l.1203.** X_p uses the principal log with arg ∈ (-π, π], not the odd branch rule. Add the coarse-side ≥ 3
   hypothesis and the c_N = c√N conversion.
3. **A1-NA(k), l.1271/1281-1284, header l.14, tally l.1706; L1d [S6], l.240-250.** Restrict to S4' iterates. Mark "=
   Balaban's domain (1.2)" and the minimiser reading as needing L1e for (0.4) (new OPEN, easy) and the √N norm
   conversion.
4. **LF-count, l.1305-1311.** Use one normalisation: β'_B ≈ 4Nb_0 and a_B > 43/N². Restate "incompatible with a
   small-field threshold" as "for ε_1 ≲ (8/(||Δ||β'_B))^{1/2}". Tag "every small-field threshold" [inference,
   conditional on the one-loop rate] at l.767 and l.1707. In the next LOG entry, correct LOG l.368's "iff" to "if
   (aβ' ≤ 4); convergent if aβ > 4".
5. **A2, l.1173.** Restrict the corollary to E8** in the |F| form, or define E8* for the Gaussian model through the
   compact embedding and prove the domain control.
6. **A1, l.1143 and l.1158.** Replace "equality attained by the constant mode" with "supremum approached by
   long-wavelength modes; attained for compact U(1) with quantised flux". "Equal action at every level" holds for the
   quadratic action only.
7. **L4a-Π, l.702.** The phase is e^{+i(p_1-p_2)/2}. Cite CMP 109 (1.21) for the δ_ab form of Π.
8. **L4a-form, l.653.** The torus side is 4L^M (ours) vs 2L^m (Balaban), not "holds". Side-agnosticism is [unverified].
9. **c18b, l.1264-1269.** State that it lies outside A1-NA(1)'s small-φ regime (coarse angle π/2) and is not a test of
   the lemma. Add the pre-registered in-regime check of (4) as c19.

**Count: 39/39 PROVEN-HERE survive.** The 30 items from sessions 1-4 were not re-reviewed. Of the 9 new items:
- 3 are CONFIRMED: (B), E8**-dens and B-avg. (B) and B-avg are trivial.
- 6 are CONFIRMED-WITH-FIX: A1, A2, L4a-Π (typo only), A1-NA(1), A1-NA(k) and LF-count.
- 0 are GAP and 0 are WRONG.

Non-item statements: 1 GAP (the L1d [S6] narrowing) and 2 WRONG (l.653 torus side; LOG l.368 "iff"). The l.1307 numbers
are WRONG by a factor 2N, within LF-count.

**Corrected tally.** 39 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / **22** OPEN. The
added OPEN item is L1e for Balaban's (0.4) independent pairing, needed by the A1-NA(k) minimiser reading and by
decision 4.
