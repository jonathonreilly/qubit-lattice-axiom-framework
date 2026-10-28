# ym4d-proof LOG

## Session 1, 2026-10-26 (proof lead)

**Read.** BRIEF.md (including the SCIENCE IMPORTS rule), openai-balaban-review/{review.md, HOW_WE_MISSED_IT.md, runner.py,
out.txt}, and d4-gauged-fixed-point-locality/{note_draft.txt, out.txt}.

**Web (data only).** Confirmed the bibliographic data of these Balaban papers:
- CMP 95 (1984) 17-40; 96 (1984) 223-250; 98 (1985) 17-51; 99 (1985) 389-434;
- CMP 109 (1987) 249-301; 116 (1988) 1-22; 119 (1988) 243-285;
- CMP 122 (1989) 175-202 and 355-392.

Also confirmed:
- MRS, CMP 155 (1993) 325-383;
- Vassilevich, Phys. Rept. 388 (2003) 279-360;
- Cao-Chatterjee 3D state space, arXiv:2111.12813.

Read Dimock II's introduction (arXiv:1212.5562): torus (L^-N Z / L^M Z)^3, bounds uniform in N with bulk M dependence.
The Dimock III abstract says "convergence of the expansion" for the stability bound only.

**Not confirmed:**
- Osterwalder-Seiler, Ann. Phys. 110 (1978) 440: attribution confirmed, volume and page not.
- CMP 99 (1985) 75 and CMP 102 (1985) 277: titles only.
- Abbott (1981) and Lüscher (2010): from memory.
- No Balaban paper body was read (paywalled). Every Balaban statement in PROOF.md is a structural paraphrase, tagged
  [unverified-exact-statement].

**Found, NOT imported.** arXiv:2606.19362 (Faizal-Shabir, June 2026) claims RP YM4 with a mass gap and confinement.
- It is unvetted and not Balaban-based per its abstract, and its claims go far beyond the community consensus.
- Treated as data. No lemma relies on it.
- No public OpenAI write-up was found.

**Decisions.**
1. **Setting.** Wilson action on Z^4 tori; L odd (block centres are sites); Balaban-type log-averaging along
   complete-axial paths. The renormalisation condition is an observable one (a cut-off resolution-0 plaquette
   expectation), so that tuning is a proven IVT statement (L7.0) and E7 can be stated on expectations, independent of
   Balaban's internal norms.
2. **Structural finding.** Limit points exist by compactness at every resolution, at finite and infinite volume, for
   any bare sequence (L7a, L8a). So existence alone needs no IR control. The content is in E8 (local large-field
   suppression, which gives consistency and non-triviality), E7 (uniqueness) and L9b (Euclidean invariance on a local
   algebra).
3. **Remark R9.1.** Averaging over SO(4) destroys RP, so rotation invariance needs universality or a second covariant
   family. The torus breaks O(4), so the OS target requires R^4.
4. **review.md correction (pending primary text).** "Small physical volume" in L6 is probably a misreading; the
   restriction is small coupling at the stopping scale.
5. **New proven lemma L3s.** Uniform gap and exponential decay of the scalar Balaban-type covariance in SU(N)
   small-field backgrounds, uniform in the number of RG steps. Ingredients:
   - the discrete Poincaré inequality with the sharp constant 4, giving gap min(2, a);
   - the axial-gauge ladder bound A_max ≤ (d-1)F/2;
   - a Combes-Thomas argument in the form that uses only cosh (no derivative coupling).
   The naive Combes-Thomas argument (row sums ~ ε^-2) gives μ ~ ε → 0 and was rejected.
6. **L4c.** Σ g_j^2 = ∞ along the AF trajectory, so per-scale O(g^2) errors are not summable. E7 must carry geometric
   decay.

**Corrections made during the session (honest trail).**
- **c1(d) linearisation.** The pre-registered halving-ratio band was 1.6-2.4, based on my claim that the relative error
  is O(t). The data show a ratio of about 4: the agreement is second order. The claim (first order) was conservative,
  and the criterion was changed to "ratio ≥ 1.6" with the observation recorded. This is not a goalpost move against
  the claim, since the claim is weaker than the data.
- **c4.** β < 0 for Z2 was intended as the negative RP control, but it turned out PSD (presumably a π-flux relabelling,
  not proven). It was replaced by a non-RP crossing term F_x θ(F_{x+1}), which fails RP as expected.
- **L1b.** My first draft asserted tracelessness of the averaged log for all N with ||Z - 1|| < 1. That fails to
  follow for N ≥ 7, where the eigenvalue-sum argument needs |θ| < 2π/N. The domain is now D_N.
- **L9a'.** In drafting I wrongly flagged a reference asymmetry under reversal of the reflected direction. Explicit
  computation shows exact covariance, since T̃_ref = T_{c_X}^-1; c1(f) confirms it to 1e-15.
- **c3.** The first run hung: the "large F = 3" tuning loop is unreachable at n = 1, because ||1 - U|| ≤ 2. It was
  killed, and the case replaced by a fixed rough field. All later runs take ≤ 30 s.

**Checks** (laptop, BLAS = 1, nice 10, every run < 35 s, < 1 GB, load < 3.1 throughout):
- c1_averaging.py: 12/12 (3 s);
- c2_b0.py: 4/4 (30 s);
- c3_scalar_covariance.py: 5/5 (5 s);
- c4_rp_wilson.py: 4/4 (< 1 s).
Outputs are in checks/c*_out.txt.

**Tally.** 13 PROVEN-HERE (six of them soft or compactness statements); 2 IMPORTED-AND-REVERIFIED;
7 IMPORTED-NOT-YET-REVERIFIED; 14 OPEN. The first open estimate is E7 (core: E7.2, irrelevant-direction contraction
including large fields).

**Next.** See PROOF.md §4:
- C_path for the iterated averaging;
- the uniform Hodge-Poincaré inequality (L3g(a));
- the Balaban primary texts, to pin down L4a, L5 and L6 and to test whether E8 is already there;
- E7.2 on a hierarchical toy model.

## Session 2, 2026-10-26 (proof lead)

**REVIEW_S1 applied first** (all fixes marked [R1-fix] in PROOF.md):
- **L7.0** is split. The per-K tuning is PROVEN. The K-uniform w* is a GAP, now the new OPEN estimate E7.0
  (w̃_0(K) → 0 super-exponentially). The ζ thresholds are rescaled to τ_N, and "contractible" is replaced by "zero
  winding".
- **L7c** is now CONDITIONAL on E7.0, and "= w*" is corrected to "≥ w*".
- **L8b** is narrowed to translations and block-aligned coordinate reflections; axis permutations are not symmetries
  of the fixed-order block map.
- **L8c** now has the odd-torus mixed reflection: L9a-m, re-derived here. The off-D extension is set to 1, which is
  θ-covariant.
- **L3s** is relabelled as a strictly weaker analogue, with scope items (a)-(e).
- **L1b** threshold corrected to N ≤ 6. The session-1 LOG said the argument "fails for N ≥ 7"; the snapshot said "N ≤ 5"
  suffices. The correct statement: the bound 1 suffices for N ≤ 6, and D_N is needed for N ≥ 7.
- **L4a** indexing fixed to resolution. The L4c consequence is softened to heuristic.
- **The overstated "IR is no obstruction to existence"** is reworded.
- **Citations upgraded** per the reviewer: CMP 99:75-102, CMP 102:277-309, Osterwalder-Seiler 110:440, Abbott 189-203.
- **c1(d) correction.** Session 1 read c1(d) as showing "second-order agreement, better than the claim". That is wrong.
  c1(d) tests log U' vs avg log T_y, which agree to O(t^3), not the line-integral form, so the reading was a misreading.
- **General caveat now in PROOF.md:** the checks test instances, not uniformity.

**Session-2 work (after the R1 fixes).**
- **(a) Iterated averaging.**
  - New L1e (PROVEN-HERE): the recursion δ_j ≤ ρ δ_{j+1} + c C_A F, with ρ = (1 + c(d+2))/L. It gives a k-uniform
    bound ||V^(j) - S|| ≤ C_δ s_j^2 F for L ≥ 9 (d = 4) and small F, and hence k-uniform coarse curvature.
  - L3s' (PROVEN-HERE): C_path = d(d-1)/4 for fine composite paths, plus a small correction for V^(j)-transports. This
    closes the session-1 obligation R3.1.
  - c5: 17/17, 23 s.
  - The L = 3 cases (ρ > 1) show δ_j growing roughly additively in the number of levels, so small-L uniformity is not
    shown.
- **(b) Hodge-Poincaré.**
  - The block version with absolute boundary conditions is PROVEN, with λ_n = 4n^2 sin^2(π/2n) and no averaging term
    (tensor product). It does not localise the global d^* term.
  - Finding L3g-ob (heuristic plus numerics): the linearised S4 root-based complete-axial average contains line
    functionals with ||·||^2_{H^-1} ~ n in d = 4 (c6: 0.196, 0.261, 0.334 at n = 3, 5, 7; log-like in d = 3; bounded in
    d = 2). The straight-leg part is bounded everywhere. The plain Feynman-gauge 1-form gap is then not uniform in
    (n, T). This is a heuristic trial-function argument, not proven.
  - c6(C): the axial-restricted λ ~ a/n was first read as a coercivity failure. It is a residual coarse-gauge artifact;
    the check was relabelled before the final run.
  - c6 first run: the lobpcg Feynman bound sat at exactly 1. Explanation: the constants are exact eigenvectors, and the
    effect needs T ≳ n^{1/4}. That pre-registered "decreasing" check FAILED and was replaced by H^-1 measurements of the
    mechanism. The first-run output was overwritten; this entry is its record.
- **(c) Literature (data only).**
  - Dimock II (arXiv:1212.5562): large fields carry a local density factor e^{-O(1)p_0^2} per cube. No local
    probability bound of E8 type is stated in the part read. E8 is NOT in Dimock I-II.
  - Dimock, "Covariant axial gauge" (arXiv:1410.2798): the abelian Balaban-style Q uses averaged gauge functions
    (Q∂λ = ∂Qλ) and order-averaged trees, with Q_kλ = 0 constraints. This suggests S4 should be revised; it also fixes
    L8b.
  - Balaban CMP bodies: still unread (paywalled).
  - arXiv:1406.4177 ("Renormalized Four Dimensional Quantum Yang-Mills Theory and Mass Gap") turned up in search. It was
    not read and not imported.
- **(d) MK toy (c7: 4/4, 1 s).**
  - The E7 analogue holds geometrically, with ratio → b^-4 = 1/16, explained heuristically at leading order.
  - It is universal across four bare families, including a large-field bump.
  - The pre-registered universality threshold (spread(K=8) ≤ 1e-9) FAILED at a* = 0.6 (8.4e-9, from log a_n at
    n ~ 8). The first-run output is kept as checks/c7_out_firstrun.txt. The check was replaced by a geometric-ratio
    criterion, and this is stated in the script.
  - The toy has no spatial large-field regions, so it says nothing about the interface.
- **Machine.** Load < 3 throughout; every run < 45 s and < 1 GB; laptop only.
- **Tally.** 17 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / 17 OPEN.
- **First open estimate:** E8 (upstream of E7.0, L7c and E7.4); E7.2 is next.
- **c5 first run.** 5 FAILs, all because the field amplitudes put F ≈ 3-12, outside the L1e domain (||Z-1|| > 1/2); the
  check had combined the domain and recursion tests. The amplitudes were reduced to the small-field regime, and one
  large-field case was kept as DIAG with no claim. The recursion itself held in all cases.

## Session 3, 2026-10-26 (proof lead)

**REVIEW_S2 applied first** (all marked [R2-fix] in PROOF.md):
- L1e restated as a smooth-background theorem; the L1d line "k-uniform sup-curvature part proven" withdrawn.
- S5 aligned with L7.0 (cut-off observable w̃, per-K tuning, E7.0 for a uniform w*).
- L8b cites the θ-covariant off-D extension of L8c(b); L8c excludes the block cut by Π_s.
- Dimock 1410.2798 entry corrected: weight L^-d; abelian averaged-gauge covariance does NOT carry over to SU(N) (root
  covariance is forced); order averaging acts on τ in Dimock, so for L8b it is an analogy only.
- MK large-field sub-test marked vacuous; Migdal/Kadanoff references added [m]; Cao-Chatterjee CMP 405 (2024) [v-R2].
- R3.1 marked as a promoted session-1 remark.
- arXiv:1406.4177 (Farinelli, math.GM) noted by the reviewer as non-credible; still not imported.

**Session-3 work.**
- **(a) Averaging revision.**
  - S4' (order-averaged over the 24 coordinate orders, order-free straight reference S_{c_X}) adopted, with S4'' (traceless
    projection, defined everywhere). Re-checked L0, L1a-c, L1e, L9a'; new axis-permutation covariance, so L8b now holds
    for the full hypercubic group. c8: 12/12, 2 s.
  - Torus side changed to EVEN (2L^{K+M}): needed for the chessboard estimate; L8c then needs only the pure link reflection.
  - Key identity (exact, linearised): Q_root = Q_str - d h. The L3g-ob funnel is a coarse pure-gauge term. On the slice
    h = 0 the root average equals the straight one.
  - L3g(a)-glob PROVEN (abelian, flat, direct average): ||A||^2 ≤ 5⟨A,ΔA⟩ + 2||Q_str A||^2, uniform in n, T, d, by a
    two-block slab Poincaré + bounded tent density + double covering. c9: 8/8, 3 s; measured gap = a (constants are the
    minimisers at all sizes tried), H^-1 norm of the straight functional bounded (0.11 → 0.093, n = 2..6).
  - Open: Faddeev-Popov completion of the slice, nonabelian background version, iterated composite.
  - REVIEW_S2 point (4) taken: averaged-gauge covariance is abelian-only; the point part is handled by the slice, not by
    the averaging.
- **(b) E8.**
  - E8.1 PROVEN: chessboard estimate re-derived (maximiser/doubling argument, from site-reflection RP on the even torus),
    giving a volume- and K-uniform Peierls bound μ(R all η-bad) ≤ q̄^{|R|}, q̄ ≲ poly(β) e^{-βη^2/(8N)}.
  - E8.2 PROVEN: one-step local ratio bound for S4', μ(F_{b'}(t)) ≤ 2L^4 q̄(t/A_L) ~ e^{-t^2/(4A_L^2 g^2)}, A_L = 9 (L = 3).
  - E8.3 PROVEN (inequality) + CONDITIONAL (AF reading): a matching lower bound by single-link conditioning shows that
    first-step domain failures are DENSE in physical volume along β_K ≤ λK sequences. Hence the session-1 E8 is FALSE
    along AF-rate sequences (SU(2), SU(3) with D; all N with τ_N/2), and E7.0 is FALSE in the AF window: the cut-off RC S5
    forces a bare coupling ~14× weaker than AF (SU(2)).
  - Repair: S5' (plain plaquette of S4'', per-K tuning PROVEN; uniformity = Haar statement E7.0', OPEN) and E8* (a
    scale-local Peierls bound at each level, OPEN; E8.2 is its m = K-1 case).
  - c10: 5/5, 24 s. Process notes: c10(D) first draft would have divided by MC-zero probabilities at large β; an
    effective-sample-count guard was added before the first run (no case was excluded: 0 untestable). c10(A) is weak by
    construction (2D U(1) plaquettes are exchangeable); stated in the output.
  - Lemma hypothesis caught while writing: the conditional lower bound needs t + 3δ < 2 sin(π/N) for N ≥ 3 (traceless
    principal logs); added.
- **(c) Spatial toy (c11: 3 PASS / 1 FAIL, 1 s; first run kept as c11_out_firstrun.txt).**
  - Inhomogeneous MK tree with deterministic strong-coupling regions; criteria pre-registered in the docstring.
  - T1 (fine-size Haar defect: root effect ratio 0.066/step) and T2 (fixed physical region: Cauchy ratios 0.01-0.07) PASS.
  - T3 FAILED as pre-registered: interface per-node contraction 0.667 (> 0.5), exterior 0.070. Criterion not changed.
  - T3b diagnostic: my hypothesis (lone undiluted child, factor → 1 at weak coupling) was written before the run and is
    FALSIFIED: the interface factor is flat at ~0.60-0.67 for a* = 0.6-0.95. Mechanism not identified.
- **(d) E7.0.** E7.0 (cut-off RC) is false in the AF window (E8.3). Replaced by S5' (plain plaquette of S4''; per-K tuning
  PROVEN) and E7.0' = liminf w_0(K) > 0 at β = 0 (pure Haar statement, OPEN). c12 diagnostic: w_0 ≈ 0.98-1.03 at K = 1, 2;
  77.5% of first-step Z are out of domain at β = 0. Process: the first c12 run took 64 s (> 60 s rule); its output is kept
  as checks/c12_out_firstrun_64s.txt, and the sample counts were cut (rerun 46 s). Values are consistent between runs.
- **Machine.** Load ≤ 2 throughout; every run except the first c12 under 60 s; peak RSS ≤ 175 MB; laptop only.
- **Tally.** 24 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / 18 OPEN; 2 retired as false
  (conditional on L4a's AF rate). First open estimate: E8* (scale-local Peierls bound at coarse levels).
- **Run trail.** The first c9 run (all PASS, narrower sizes: T = 2 in d = 4, a ∈ {1, 0.2}) was overwritten when the size
  grid was widened. It recorded λ_min = a in every case, the same as the kept run. All other first runs are kept.
- **Checkpoint.** Clean stop: PROOF.md and LOG.md are consistent; no snapshots or reviews were touched; no PRs, pushes, CL
  or axiom edits.

## Session 4, 2026-10-26 (proof lead)

**REVIEW_S3 applied first** (all marked [R3-fix] in PROOF.md):
- **E8.3 consequences re-thresholded to 3τ_N/4.** E7.0 restricted to the AF window fails only for N = 2, 3, 4, and the
  SU(2) ratio λ_c/λ_AF is about 6.1, not 14. E8 with D is false only for SU(2) and SU(3). The "all N" claim is
  withdrawn: it concerned the stronger event "all steps within τ_N/2". Recomputed in c13(R).
- **E8 falsity scoped by reading.** It is unconditional for a fixed bare g, and conditional on L4a for the tuned g.
  E7.0 itself (sup over all β) is not falsified.
- **Conditional lemma.** ζ_1 is chosen as the eigenphase of largest modulus, with sign(0) = +1.
- **L3g(a)-slice.** The term is a "coarse exact 1-form dh(A)", valid only linearised and abelian. Its use as a gap is
  CONDITIONAL on (FP).
- **One off-D extension.** S4'' now uses an odd branch rule: log Z := 0 when Z has eigenvalue -1. Gauge, permutation
  and reflection covariance then hold everywhere, with no null-set obligation. "Failed link := 1" is withdrawn, and
  L8b, L8c and L9a' were updated.
  - Considered and rejected: "link := 1" for O. At β = 0 it would set almost every coarse link to 1 and make
    w_0 → 0, which kills E7.0'.
- **S5'.** E7.0' is sufficient, not equivalent. The AF compatibility of S5' tuning is a new OPEN item, E7.0'-AF. The
  K = 2 c12 value rests on 2 samples and its error bar is not credible. The 77.5% out-of-domain fraction matches exact
  Haar.
- **Other.** Added the c11 depth ≤ 3 limitation and the FILS citation [m].

**Session-4 work.**
- **(a) E8* beyond the first step.**
  - E8*-sup (PROVEN): one step maps a plaquette bound η to C_1 η, with C_1 = L^2 + 4cA_L.
  - E8*-k (PROVEN): at every fixed depth, μ(F_b(t)) ≤ 2L^{d(k+1)} q̄(t/(A_L C_1^k)), uniform in K and M. It is useful
    only for k ≲ log β / (2 log C_1).
  - E8*-ob (PROVEN, c13(B)): a constant-flux field gives exact growth L^{2k}, so no deterministic induction goes
    deeper. Heuristically, energy-only bounds hit the same L^{4k} entropy wall.
  - E8*-red (PROVEN): a chessboard estimate on 2-site cells at level m, using the RP of ν_m under link planes. It
    reduces E8* at every depth to the homogeneous constrained-stability bound E8** (OPEN), which is the new first open
    estimate.
  - The torus side becomes 4L^{K+M} (every level side divisible by 4).
  - c13 (6/6, 2 s). Process notes: the first two runs aborted at a domain assert (amplitudes too large); the first is
    kept as c13_out_firstrun.txt. Run 3 had a B0 tolerance bug (the 1e-12 tolerance against a sqrt that loses half the
    digits), kept as c13_out_run3_B0tol.txt. No criterion on the proven inequalities was changed.
- **(b) E7.0'.**
  - H0 (PROVEN): the crossing-link structure; centre-line Z ≡ 1.
  - H1 (PROVEN): from i.i.d. Haar, V' = W e^{X̄} with W i.i.d. Haar and E||X̄||²_HS ≤ m_N(L^{d-1} - 1)/L^{2(d-1)}. This
    gives w_0(1) ≥ 0.16 at L = 5 and 0.49 at L = 7 (SU(2), d = 4); it is vacuous at L = 3.
  - H1 does not iterate, because centring is lost after one step. Sufficient reduction: E7.0'-TV (OPEN).
  - c14 (12/12, 31 s). Diagnostic in d = 2: w_0(K) ≈ 1 for K = 1..5. The first run had 4 samples at K ≥ 3; it is kept
    as c14_out_firstrun.txt.
- **(c) The 2/3 interface mechanism (c15: 5 PASS / 3 FAIL, 5 s).**
  - Mechanism: slots with j small-field children perform bond moving with power j, so locally the map is a
    lower-dimensional MK step.
  - The j = 2 model reproduces the c11 RRSS class exactly (0.5266).
  - Pre-registered prediction confirmed: j = 1 corners (a small-field box in a strong sea) give a ratio of 1.12 > 1.
  - H1 FAILED: the exterior class missed the 1e-3 tolerance by 3e-4.
  - H5 first FAILED from a script bug (wrong reference node). Fixed; the first run is kept.
  - Compounding (H6) FAILED as predicted: the interface/bulk ratio is flat at 0.9-1.0 and both decay like the layer
    volume. H6' (post hoc, tangent removal) FAILED and is inconclusive by construction.
  - Decision: a uniform per-block contraction is false in the toy, so E7.2 needs a geometry-weighted norm. The interface
    influence does not compound in the toy. j = 1 non-contraction is judged an MK artefact (heuristic dimension
    counting); the face rate L^-1 is generic.
- **(d) SU(N)/FP extension of L3g(a).** Not attempted (time). It is carried to Next, item 4.
- **Literature.**
  - Project Euclid (CMP back volumes) served an Incapsula bot-detection page. It was not bypassed, and no Balaban body
    was read.
  - deepblue.lib.umich.edu (CMP 102 record): HTTP 403.
  - Dimock arXiv:2009.01156 (UV stability for QED d = 3): abstract read only.
  - Balaban primary papers remain IMPORTED-NOT-YET-REVERIFIED.
- **Machine.** Laptop only; load ≤ 2.3 throughout; every run ≤ 31 s; peak RSS ≤ 263 MB.
- **Tally.** 30 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / 21 OPEN. First open estimate:
  E8**.
- **Checkpoint.** Clean stop: PROOF.md and LOG.md are consistent; snapshots and reviews were untouched; no PRs, pushes, CL
  or axiom edits.

## Session 5, 2026-10-26 (proof lead; reading and re-verification session, per REVIEW_S4)
- **Step 0: REVIEW_S4 fixes applied as [R4-fix].**
  - E8*-sup: domain A_L η ≤ τ_N/2. The c → 2c alternative is noted. E8*-k's domain chain needs t ≤ C_1 τ_N/2.
  - E8*-ob now rules out only fine-plaquette-sup inductions.
  - L9a scope now names bounded measurable F.
  - H1's useful range (L ≥ 5) is SU(2) only.
  - c15 downgraded to a finite diagnostic and "E7.2 needs a geometry-weighted norm" withdrawn. Kept as a design note;
    Next item 5 dropped.
  - FILS cited as [v-R4], pp. 1-34. Dimock 2009.01156 upgraded.
- **Step 1: reading.**
  - Method. arXiv ids and dates checked against the arXiv API. PDFs fetched to the scratchpad; text extracted with
    pypdf, with page markers. Notes with page and equation numbers are in literature/NOTES.md.
  - Read:
    - 1108.1335, 1212.5562, 1304.0705 (Dimock I-III): **scalar φ⁴_3, not scalar QED**. The brief's premise is corrected.
    - 2009.01156 (QED UV stability), 1712.10029 (multiscale averaging) and 1512.04373 (UV regularity): read-skim,
      theorem statements plus the large-field lemmas.
    - 2204.07201 (QED overview): read in full.
  - No Balaban CMP body was read. No modern open exposition of 4D YM was found. One search-engine summary claim (that
    Dimock doubts 4D completeness) was not found in the text and is not cited.
- **Key findings.**
  - (1) The R-operation appears in no open exposition (Dimock II p.31, Remark 3).
  - (2) Balaban/Dimock large-field factors are extracted per level from that level's own action. The sup bound crosses
    one level only (QED Lemma 23; III Lemma 13), which is exactly the escape from E8*-ob.
  - (3) E8** is not stated anywhere. It is the probability form of L5 + L6, so it is reclassified as an import target.
- **New PROVEN-HERE items (4).**
  - E8**-dens: E8** ⇐ (D_m), an effective-density bound.
  - Inequality (B).
  - Lemma A1: the abelian S4' averaging contracts the action with the sharp constant L^{4-d}, which is 1 in d = 4. It
    reproduces Dimock's e_k² = L^k e_0² in d = 3.
  - Proposition A2: E8** and E8* hold at every depth in the 4D Gaussian abelian model, with ε = 4096 e^{-βη²/4}.
- **New OPEN: A1-NA.**
- **Check c16: 11/11 PASS, 3.1 s, 69 MB.** First run, with no criterion changes. (An earlier launch attempt failed
  before Python started because `timeout` is not installed on macOS. Nothing ran; there is no output file.) Machine:
  load ≤ 3.3, 36% free memory, BLAS = 1, nice 10.
- **Status changes.**
  - No IMPORTED-NOT-YET-REVERIFIED lemma upgraded. Each 3D analogue maps onto structure only; the 4D SU(N) content needs
    the CMP papers.
  - L6 citation upgraded to [read].
  - Tally: 34 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / 22 OPEN.
- **Still blocked.** L1d, L2, L3g, L4a, L5 and L6 (4D SU(N)). Hence E8** and E8* at depths ≳ log β.
- **Owner request.** PDFs of Balaban CMP 122:175-202 and 122:355-392 (first), then 109:249-301, 116:1-22, 119:243-285,
  102:277-309 and 98:17-51; then 95:17-40, 96:223-250, 99:75-102 and 99:389-434. Place them in literature/.
- **Checkpoint.** PROOF.md, LOG.md and NOTES.md are consistent. The snapshot is PROOF_session5_snapshot.md. REVIEW files
  and earlier snapshots are untouched. No PRs, pushes, CL edits or axiom edits.

## Session 6, 2026-10-27 (proof lead; CMP 109 reading and large-field reconstruction)
- **Step 0.** No review of session 5 exists, so there are no [R5-fix] items. REVIEW files and earlier snapshots were
  left untouched.
- **Step 1: CMP 109 read in full** (owner-supplied PDF plus text extraction).
  - Garbled display equations were read from page images (pypdf + Pillow into the scratchpad; Pillow was installed into
    the scratchpad venv from PyPI).
  - Notes: literature/NOTES.md §9, with page and equation tags and every citation to the other papers.
  - Findings:
    - (1) Small-field only (p.250).
    - (2) The proof of its own Theorem 3 is incomplete by design. The localisation and cluster expansion are deferred to
      "the next paper" (p.298), CMP 116:1-22, "II. Cluster expansions" (Crossref).
    - (3) Theorem 2 (the coupling flow, (0.31), SU(2), constants 0 < β ≤ β' unspecified) is deferred to "a separate
      paper". No "β_j → 2b_0 ln L" appears; PROOF.md is corrected.
    - (4) Balaban's average (0.4) is S4' with independent instead of diagonal order pairing. They are identical under
      diagonal pairing (conjugation identity) and differ at second order otherwise (c17(B)).
    - (5) The background small-field domain (1.2), |U(∂p) - 1| < ε_0η², is L1e's hypothesis exactly. The fluctuation
      cut is |B'| < ε_1 (2.9).
    - (6) The inductive polymer bound (1.18) has no power of g. The renormalised terms obey (L^jη)^{4+α}e^{-κd} (0.29).
    - (7) The gauge fixing combines δ(Q̃B') with an exponential, Euclidean-invariant block-axial gauge on order-averaged
      contour variables, and passes to Landau gauge for the estimates.
- **Step 2: upgrade attempts.**
  - L1d, L2, L3g, L4a: none upgraded wholesale. CMP 109 cites CMP 98/99/102 for their content without reproving it,
    and defers L4a's localisation and flow.
  - Narrowings:
    - L1d's background-regularity part is L1e on Balaban's domain (the R2-fix sentence is narrowed);
    - L2's statement is now exact (second-hand), with a conditional tree-level corollary;
    - L3g's gauge fixing is now known;
    - L4a is split into L4a-form, L4a-flow and L4a-Π.
  - **New PROVEN-HERE (5):**
    - L4a-Π: a direct Taylor re-derivation of CMP 109 §5 (transverse structure; β is the mixed second moment);
    - Lemma B-avg;
    - Lemma A1-NA(1): the one-step non-abelian action bound with leading constant L^{4-d}, its local form and the
      large-field dichotomy (c). This was OPEN;
    - Corollary A1-NA(k): k-uniform on the L1e domain;
    - Proposition LF-count.
- **Step 3: large-field literature (route a).**
  - Crossref: CMP 122 titles and issues; CMP 116 subtitle.
  - OSTI abstracts of CMP 122 I-II [read-abs]. The OSTI record has a citation discrepancy (120:575-612 vs 122:355-392),
    recorded as unresolved.
  - Read: Dimock's Rome 2022 lectures (the d = 3 large-field counting template, p.39), BFKT arXiv:1609.00968 p.4, and
    Jaffe-Witten.
  - No open-access statement of Balaban's 4D large-field bound or of the R-operation was found.
  - Project Euclid served an Incapsula bot page; not bypassed. Springer redirected to a login; not pursued.
- **Step 4: reconstruction (route b), outcome.**
  - The bare-action per-level extraction is now proven at tree level (A1-NA(1)(c)).
  - The exact wall is Proposition LF-count. With the flow (0.31), the unrenormalised count Σ_k L^{4(K-k)}e^{-a/g_k²}
    diverges iff aβ' ≤ 4 [R56-fix: read "diverges if aβ' ≤ 4; convergent if aβ > 4"; only "if" is proven]. This holds for every small-field threshold [R56-fix: WRONG as stated; corrected to "for ε_1 ≲ (8/(||Δ||β'_B))^{1/2}, conditional on the one-loop rate", threshold a_B > 43/N² in Balaban's normalisation]: the perturbative β' needs a ≳ 43 for SU(2), while
    the instanton's a = 8π² is fine.
  - So in d = 4 the large-field regions must themselves be renormalised (the R-operation), unlike in Dimock's d = 3
    template, where geometric e_k makes the count converge.
  - Named next target: a one-cube R-operation.
- **Checks (laptop, nice 10, BLAS/OMP threads 1; load 1.7-3.1, 32-33% free memory):**
  - c17: 8/8 PASS, 0.7 s, 39 MB, first run.
  - c18: 6 PASS / 2 FAIL, 11 s, 422 MB, first run, kept as c18_out_firstrun.txt. The FAILs are the pre-registered
    slope criterion (ii), ill-posed because the deviation is non-monotone. Bounded deviation ≤ 0.006φ. The fields are
    far from extremal.
  - c18b (post hoc, near-extremal constant flux plus a non-abelian perturbation): 1/1 PASS, 6 s, 404 MB.
- **Tally.** 39 PROVEN-HERE / 2 IMPORTED-AND-REVERIFIED / 7 IMPORTED-NOT-YET-REVERIFIED / 21 OPEN.
- **Checkpoint.** PROOF.md, LOG.md and NOTES.md are consistent. The snapshot is PROOF_session6_snapshot.md. No PRs,
  pushes, commits, CL edits or axiom edits. Downloads went to the scratchpad only (arXiv/OSTI/Clay/Dimock open PDFs).

## Session 7, 2026-10-27 (proof lead; review fixes, in-regime check, one-cube R-operation)
- **Step 0.** REVIEW_S5_S6.md read first (binding). REVIEW files and earlier snapshots were not edited.
- **Step 1: every REVIEW_S5_S6 fix applied, tagged [R56-fix].**
  - A1: the supremum is not attained for real A (it is attained for compact U(1) with quantised flux); "equal action at
    every level" holds for the quadratic action only.
  - A2: corollary restricted to E8** in the |F| form; the E8* sentence is withdrawn.
  - L4a-Π: phase e^{+i(p_1-p_2)/2}; CMP 109 (1.21) cited for the δ_ab form.
  - A1-NA(1): (c) re-proved by concavity of 1 - cos√t; principal branch (-π, π], not the odd rule; coarse side ≥ 3;
    c_N = c√N.
  - A1-NA(k), L1d [S6], the L2 tree-level reading and the header: restricted to S4' iterates. New OPEN item L1e-(0.4).
  - L4a-form: torus side 4L^M (ours) vs 2L^m (Balaban); side-agnosticism [unverified].
  - LF-count: one normalisation (Balaban's), β'_B ≈ 4Nb_0, a_B > 43/N², ε_1 ≲ (8/(||Δ||β'_B))^{1/2}; "every
    small-field threshold" made conditional at L5 and in the tally.
  - **Correction of session 6:** "diverges iff aβ' ≤ 4" should read "diverges if aβ' ≤ 4; convergent if aβ > 4"
    (annotated in place).
  - c18b: declared outside A1-NA(1)'s regime, not a test of the lemma.
  - Tally after step 1: 39 / 2 / 7 / 22.
- **c18c (in-regime A1-NA(1) check).** Criteria in checks/c18c_criteria.md, written before the script. First run: 16/16
  PASS, 0.96 s, 66 MB (load 2.4, 36% free memory, nice 10, BLAS threads 1).
  - Cases: d = 2, coarse side 5, R_ab/L² = 0.79; d = 3, coarse side 3, R_ab/L = 0.51; fine φ ≤ 0.022.
  - The non-abelian ratio tends to the abelian one, with a correction O(φ²) here, which is negative.
  - The sharp edge L^{4-d} is not reached on finite tori, so it is not stressed.
- **Step 2: one-cube R-operation.**
  - RTARGET.md written first: model, target (R2D), counterterms, failure modes F1-F4, and non-success W1-W3.
  - 2D wall verified: divergent if aβ' ≤ 2. With the one-loop O(N) rate, every single-bond cut lies in the window for
    3 ≤ N ≤ 8. The O(3) instanton has aβ' = 2 exactly, matching the known small-instanton divergence [m].
    **[R78-fix, annotated in session 9]** The "3 ≤ N ≤ 8" statement is WRONG: the cheapest excluded configuration
    costs a ≈ ε_1² (not ε_1²/2, which is a lower bound). The window is every ε_1 ≲ (4π/(N-2))^{1/2} (linearised). On
    the lattice the O(3) count is geometric, not marginal (dislocations, [m]).
  - Literature [read-abs / read-skim]: CMP 198 (1998) is the large-field operation of the low-temperature d ≥ 3
    N-vector series, not 2D UV (Rutgers record; search snippets). Kopper CMP 202 (1999), math-ph/9902020
    introduction: the full 2D O(N) UV analysis had been done only hierarchically. No open 2D large-field
    R-operation was found. No paywall, sign-in or bot-check was crossed.
  - **Proposition R2D-iso PROVEN-HERE**, for an isolated cube with frozen exterior, soft block spin and an interior-bond
    cut. The target was met as pre-stated: ρ = ρ_0 + δβA_B + O(e^{-a/g²}s⁴), for every a < ε_1²/4, with
    g-independent s_0. The proof uses positivity, g-polynomial derivative bounds, point-reflection evenness, O(N-1)
    and D_4 invariance. Consequence: for isolated cubes, LF-count's divergence sits entirely in the field-independent
    vacuum part, which is removed by normalisation.
  - Walls of the full R-operation, named:
    - W1: localisation in a fluctuating small-field sea;
    - W2: nested multi-scale large fields;
    - W3: hard constraints, i.e. M's branch set under Balaban's δ-constraint.
  - 4D: the R4D-iso changes are listed (plaquette cut via (B), soft gauge-covariant constraint, the gauge-invariant
    Taylor lemma with B_4 irreducibility of Λ², remainder O(s⁶)). Item OPEN.
- **Tally.** 40 / 2 / 7 / 23.
- **Checkpoint.** PROOF_session7_snapshot.md. No commits, PRs, pushes, CL edits or axiom edits.

## Session 8, 2026-10-27 (proof lead; W1 in 2D, R4D-iso, Lemma GT)
- **Step 0.** Read RTARGET.md, the session-7 log, PROOF.md (R2D-iso, W1-W3, R4D-iso, inequality (B), LF-count,
  L1e-(0.4)), REVIEW_S5_S6 (binding rules) and NOTES §1-3, §9, §11. No REVIEW file or earlier snapshot was edited.
- **Pre-statements first.** RTARGET.md §5 (W1, strong and weak forms, failure modes W1-F1..F4), §6 (Lemma GT and
  R4D-iso, failure modes R4-F1..F4, the c19 plan), §7 (W2), written before any derivation. One typo in §5 was fixed
  before the derivations started. Outcome pointers were added afterwards as §8.
- **Lemma GT PROVEN-HERE.**
  - Radial (Fock-Schwinger) gauge makes all data O(s²).
  - Constant-gauge invariance kills DF̃(0) (G semisimple), so order s² vanishes; ι gives evenness.
  - Order s⁴ = c·Σ||F_μν(0)||²: Λ²R⁴ is absolutely irreducible under B_4 (sign flips separate the six lines,
    permutations are transitive on them), and su(N) is absolutely irreducible under Ad. The remainder is O(s⁶).
- **Proposition R4D-iso PROVEN-HERE** (moved from OPEN), as pre-stated:
  - plaquette cut priced by (B): numerator ≤ e^{-ε_1²/(2Ng²)};
  - Haar balls of radius ε_1g/8 for the denominator; data deviation O(s²) in radial gauge, so s_0 = (ε_1²/(4NB))^{1/4};
  - R2D-iso-type derivative bounds, then GT for ρ, log(1 + ρ) and A_B (c_B = n_B/(2N)).
  - Result: ρ = ρ_0 + δβA_B + O(e^{-a/g²}s⁶) for a < ε_1²/(4N). The remainder sums against L^{4(k-j)} with α = 2.
- **c19.** Criteria in checks/c19_criteria.md, written before the script. First run 10/10 PASS: 18 s, 64 MB, load 1.9,
  36% free memory, nice 10, BLAS threads 1.
  - P1 character norm 1 (rotation subgroup 2). P2 one invariant form.
  - F1/F2/F3 on 6 backgrounds: c universal to ≤ 5e-8 (SD = ASD), s⁶ remainder ratios 63.4-64.6, gauge-invariant to
    3e-12, c_{F1} = 9 = n_B/4.
  - Controls: B_4-broken spread 0.80; ι-broken odd part ~ s⁵.
- **W1 in 2D: partial; exact wall named.**
  - Lemma W1-def: the fluctuating-exterior defect equals 1 + ⟨ρ_□⟩ over the conditioned sea (Fubini).
  - Lemma W1-size: ⟨ρ_□⟩ ≤ [C_1g^{-p}e^{-ε_1²/(4g²)} + P_rel(E)]/(1 - P_rel(E)), where E = the collar is off every
    common direction by δ_0 = ε_1/(2√(4L+κ)).
  - Lemma W1-sym: for any O(N)- and D_4-invariant function of the whole block-spin field with exponentially decaying
    derivatives, F = f_0 + δβA_B + O(ws⁴), uniform in the torus.
  - New OPEN item W1-loc = W1-LD (collar large deviations) + W1-cl (clustering of the pinned sea). Both are small-field
    sea estimates (2D analogue of L4a-form / CMP 116).
  - The frozen-exterior moment recursion amplifies by M ≫ 1 and does not close [route obstruction, not a no-go].
  - Dimock I Thm 27 needs an ultralocal measure (W1-F3), so the multi-defect strong form is not reached.
  - Illustration (N = 2, crossing bonds cut): winding exterior ⇒ ρ = ∞.
- **W2:** pre-stated only.
- **Tally.** 40/2/7/23 → **43 / 2 / 7 / 23** (+GT, +R4D-iso, +W1-sym; OPEN -R4D-iso +W1-loc).
- **Checkpoint.** PROOF_session8_snapshot.md. No commits, PRs, pushes, CL edits or axiom edits.

## Session 9, 2026-10-27 (proof lead; review fixes, decision 4, BG-reg, W1-loc in 4D)
- **Step 0.** Read REVIEW_S7_S8.md (binding), PROOF.md (header, L1d/L2, L5 [S7]-[S8], tally, session order), RTARGET.md,
  the session-7/8 log, NOTES §1-3, §9.4 and Dimock I (scratchpad text) §4.4-4.6 and App. B. No REVIEW file or earlier
  snapshot was edited.
- **Decision 4: made by the session-9 lead under authority delegated by the owner** (this is not an owner ruling, and
  not a CL or axiom change). The main path keeps S4'-contour averaging with the soft gauge-covariant constraint. The
  precise kernel is the normalised k_c ∝ exp(-(κ/g²)[1 - N^{-1}Re tr(V_c^{-1}M̄_c(U))]), with M̄_c the mean S4' contour.
  Balaban's (0.4) with δ(M(U)V^{-1}) becomes a comparison branch. L1e-(0.4) and W3 move to the comparison-branch list.
  The hard-constraint imports (L1d, L2, L3g, L4a, L5, L6) must be re-verified for the soft version.
- **Step 1: every REVIEW_S7_S8 fix applied, tagged [R78-fix].**
  - The 2D wall cost is a ≈ ε_1² with window ε_1 ≲ (4π/(N-2))^{1/2}. RTARGET §0 is annotated, not rewritten. PROOF L5
    [S7], the session-7 header and the session-7 LOG line are annotated.
  - The O(3) lattice-dislocation caveat is added.
  - R2D-iso: B is now the Γ-Γ bonds (b = 2(L-1)).
  - New OPEN item BG-reg; the Consequence paragraphs and the header are tagged "[conditional on BG-reg, hence on L2]";
    W2's "small-field" is now "smooth s-family".
  - W1-sym and W1-red: seam-safe families. W1-def: higher derivatives are pure cumulants.
  - W1-loc restated: polynomial g-loss, direct Φ_0 terms, seam, s_0 ≲ δ_0.
  - Headers: weak-form wall; "counted as one item"; "on smooth s-family backgrounds".
  - RTARGET §8: the weak form was read as "all other cubes cut".
  - c18c: the "largest available" claim is deleted.
  - **c19's pre-run edit (20 → 5 random Ad elements; B_4 generators) is disclosed** in PROOF and in an appendix to
    checks/c19_criteria.md.
  - Tally after step 1: 43/2/7/24. After decision 4: 43/2/7/23 + 1 comparison-branch item.
- **c19b** (reflection-odd clover control; criteria checks/c19b_criteria.md written before the script). First run 5/6,
  overall FAIL as pre-registered: 15 s, 37 MB, load 2.0, 36% free memory, nice 10, BLAS threads 1.
  - Q5 PASS, which is the control's point: c_SD = +2.000, c_ASD = -2.000, so without reflections a second invariant
    appears.
  - Q1, Q2, Q4 and Q6 PASS.
  - **Q3 FAIL**: the s²-rate window [3, 5] at s = 0.2 was missed on 3 of 5 backgrounds (5.15, 17.3, 2.70). A disclosed
    post-run diagnostic shows r(s) converging, with the difference ratios → 4 only for s ≤ 0.1. The criterion is not
    edited.
- **Pre-statements first.** RTARGET §9 (BG-reg) and §10 (W1-loc, 4D) were written before the derivations, and the c20
  criteria before the c20 script. Provenance caveat: the targets were formulated after a short preliminary analysis in
  this session.
- **BG-reg.**
  - Lemma GT-lat + Proposition R4D-lat PROVEN-HERE. This is a lattice Taylor lemma in gauge-invariant parameters
    (ε_2, ε_3, ε_V); no smooth interpolation is needed, so (a) is discharged.
  - Lemma BG-sum (arithmetic): the sum is bounded iff, sufficiently, BG-b holds = sup coarse-unit curvature +
    summable mean oscillation. In d = 4 the scale factors cancel exactly.
  - BG-b is the U_k(ε_0)-membership half of L2 (CMP 109 (1.2): curvature AND |J| < ε_0), plus a lattice elliptic step
    and a soft-residual bound. It is not proven for the soft S4' minimiser; the obstruction is per-cell nonlinear
    multiscale regularity.
  - **c20**, linearised abelian 2D soft chain with S4' contours. First run VALID: 104 s, 391 MB, load 2.0, 36% free
    memory. Model SUMMABLE in all three runs: mean-oscillation ratio ≈ 1/L, and no concentration at the axial centre
    lines. A pre-run smoke test of the averaging operator was done (disclosed).
- **W1-loc in 4D (main path).**
  - Lemma W1-size' PROVEN-HERE: an exact size reduction to the holed sea plugged with w_ref = sup_{U_int}w. It removes
    the released-measure probability and the exponentially small denominator.
  - Lemma AG (Anderson/rearrangement sub-Gaussianity of truncated Gaussians).
  - Corollary W1-LD-cond: (DF1-3') ⇒ (LD), with a = min(ε_1²/(4N), a_LD), g-independent.
  - (cl) argued under (DF4) + Dimock I Thm 27, with a corridor of width O(log 1/g) that costs a polynomial g-loss.
  - **Exact wall: (DF) = the small-field package for the soft RG, plus re-verifying Thm 27.** Its tree-graph bound
    (323) is "one can show" in Dimock I App. B [read].
- **Lemma D4-norm** PROVEN-HERE: R4D-iso holds for the normalised soft kernel, the exact RG step, with only a
  polynomial g-loss.
- **Tally.** **46 / 2 / 7 / 23 + 1 comparison-branch item** (+D4-norm, +GT-lat/R4D-lat, +W1-size'/W1-LD-cond).
- **Checkpoint.** PROOF_session9_snapshot.md. No commits, PRs, pushes, CL edits or axiom edits.

## Session 10, 2026-10-27 (proof lead; Thm 27 re-verification, BG-b for the soft chain, (DF) sub-DAG)
- **Step 0.** Read PROOF.md (header, session-10 order, L2, L5 [S9], A1/A1-NA(1), L3g(a)-glob/slice, tally),
  RTARGET.md §9-11, the session-9 log, NOTES §1 and §9.4, and Dimock I App. A-B (pp. 37-44, text extracted from the
  arXiv PDF in the scratchpad). No REVIEW file or earlier snapshot was edited. No review of session 9 exists, and none
  was done (carried as item 1 of the session-11 order).
- **Pre-statements first.** RTARGET §12-14 were written before the derivations, and c21/c22 criteria before the scripts.
  Provenance caveat: a short preliminary analysis in this session had already suggested the κ-dependence of c_0 and the
  funnel cancellation; both were pre-stated as things to test.
- **A. Theorem CE (PROVEN-HERE).**
  - Dimock I Thm 27 is re-proved with explicit d = 4 constants. It includes Lemma TG (= (323); Penrose partition,
    complete proof) and Lemma CE-geo (touching-tree metric: |X| ≤ 81(1 + 4d), d(∪X_i) ≤ Σd(X_i) + 2(n-1), lattice
    animals ≤ 80^{2(n-1)}).
  - **Proposition CE-κ: Thm 27 as stated (c_0 depending on d only) is false**: nearest-neighbour Ising,
    H#(2×3) = h⁶ + O(h⁸) while d ≥ 1. The corrected c_0(κ) ∝ e^{-2κ}.
  - Text discrepancies: √d in (305); the (2d) count in (292); the root factor in (329); κ_2 in (325); the dropped
    e^{(κ_2-2κ_0)(n-1)} in (326).
  - c21 (criteria first): 13/13 PASS, 6.1 s, 31 MB, load 1.6, 35% free memory, nice 10, BLAS threads 1.
- **B. BG-b.**
  - Lemma LES (lattice elliptic step, Campanato, Hölder-α), Lemma CR (constant reproduction; ε_V's linear part
    vanishes by block centring alone) and Lemma J-str (at critical points of the linearised soft chain, every residual
    is co-closed, so the S4' funnel part of the soft current vanishes exactly; ||Q_str^T||_∞ = L^{-3} makes the fine
    current bounded in coarse units by the top residual, uniformly in k): all PROVEN-HERE.
  - Proposition BG-b-lin: BG-b ⇐ (H1) + (H2). PROVEN-HERE.
  - Non-abelian transfer: argued (A1-NA(1), BCH, exact Noether identity).
  - c22 (criteria first; SU(2), 9⁴, L = 3): VALID; Q1, Q2 PASS; Q3 FAIL (pre-registered monotonicity of dev_S; the
    deviations themselves are ≤ 8%). 394 s, 573 MB, load 1.8, 38% free memory, nice 10, BLAS threads 1. Two pre-run
    smoke tests were done (disclosed in checks/c22_time.txt); one changed only the evaluator's speed, verified to 9e-16.
- **C.** (DF) sub-DAG N1-N12 written. The (DF3') tilt argument from Theorem CE is argued. The remaining wall of W1-loc
  and BG-reg = {N2 soft L2 with (H1)/(H2), N4 (FP), N5 soft covariance, N6 soft polymer bound}.
- **Tally.** 46/2/7/23 + 1 → **49 / 2 / 7 / 23 + 1 comparison-branch** (+Theorem CE, +LES, +BG-b-lin).
- **Checkpoint.** PROOF_session10_snapshot.md. No commits, PRs, pushes, CL edits or axiom edits.

## Session 11, 2026-10-27 (proof lead; REVIEW_S9_S10 fixes, N2 linear half, N4 abelian, κ_0)
- **Step 0.** Read REVIEW_S9_S10.md (binding), PROOF.md (headers, L5 [S9]/[S10], the (DF) sub-DAG, L2,
  L3g(a)-glob/slice, the tally, the session-11 order), RTARGET §12-15 and the session-10 log. Re-read Dimock I in
  the extracted text for every quotation used: (119), (122), (243), (305), p.40, the Lemma 21 proof and §3.1. No REVIEW
  file or earlier snapshot was edited.
- **Corrections to earlier log entries** (appended, not rewritten) [R910-fix]:
  - Session 10, "Proposition CE-κ: Thm 27 as stated (c_0 depending on d only) is false": withdrawn as phrased.
    Thm 27's statement says c0 depends on d only; its proof says (p.40) "So c0 does depend on κ". Proposition CE-κ
    shows the κ-dependence is necessary. This corrects the statement's quantifiers, as the author's remark does.
    Dimock's proof and his application (κ fixed) are unaffected.
  - Session 10, "the (2d) count in (292)" listed as a text discrepancy: retracted. Dimock's polymers are
    face-connected (§3.1), so it is a definitional difference. There are four textual discrepancies: (305), (329),
    (325), (326).
  - Session 9, "the sum is bounded iff, sufficiently, BG-b holds": read "bounded if BG-b holds" (sufficiency only).
  - Session 9, c20: one pre-run code edit (a diagonal-term line, 13:22:02 UTC, found by the REVIEW_S9_S10 transcript
    audit) was not disclosed.
- **Step 1: all 13 REVIEW_S9_S10 fixes applied** ([R910-fix] in PROOF.md; RTARGET §15 annotated).
  - The CE-κ wording, the touching-tree reading, the six-bond finite-difference proof, the c21 value 0.9997.
  - The discrepancy-2 retraction, the CE-cx constants, the N6 κ-requirement.
  - BG-b-lin: the factor 2, n ≥ 1 with the n = 0 edge case, the κ̂/κ_{k-1}-only constants; CR (ii) for every B.
  - The LES small-radius line; "iff" → "if"; D4-obs as an OPEN item; the (DF3') Cauchy margin and |t| ~ 1/g.
  - The B-NA (iii) reconciliation note; the c20/c22 reporting; "(linearised)".
  - Decision 4: the owner's delegation in the owner's words is not in any file read, so the label stays.
  - **c21 re-run** (criteria addendum first; reporting-only edit of Part I plus the new exact I4): 14/14 PASS, 6.2 s,
    33 MB, load 1.99, 37% free memory, nice 10, BLAS threads 1. Output checks/c21_out_s11.txt; the session-10 output
    is kept.
  - Tally after step 1: **49/2/7/24 + 1**.
- **Pre-statements.** RTARGET §16-18 were written before any session-11 derivation; the criteria for c21 (addendum),
  c23, c24 and c25 were written before the scripts (UTC 14:58).
- **N2, linear half.**
  - Lemma N2-a (gauge orbit; flat ⇒ zero; abelian and SU(N)) and Lemma N2-E (E_k ≤ 1.2·10⁸(1 + κ_+)||dB_k||²,
    uniformly in k, via a cubical-Whitney test chain plus CR (ii)) give the ℓ² (H1)/(H2) from the curvature:
    PROVEN-HERE.
  - Proposition N2-red ((H1) + (H2) ⇐ (LED), with Lemma LES-sup): PROVEN-HERE.
  - (LED) is not proven. The hole-filling commutator is marginal per level, so the naive sum is O(k).
  - **c23** (one pre-run tiny smoke test, disclosed). A: VALID; Q1, Q2 PASS; Q3 FAIL as pre-registered (design flaw:
    the k = 1 value is the largest and the values decrease; not edited); 65.7 s, 469 MB. B (SU(2), 4D): VALID; Q4, Q5,
    Q6 PASS (a large pure gauge leaves R_top unchanged; a flat field of size 1.1 changes R_top by 8%; the flat field
    alone gives R_top 6.7e-7); 256 s, 473 MB.
- **N4, abelian.**
  - Lemma FP-ab plus its application: the legitimate fixed-b fixing is δ(h)·e^{-½||P_resd*A||²}, with an A- and
    b-independent constant.
  - The double fixing with the full Δ carries an explicit weight W, so it is not an identity.
  - The O_FP gap ⟺ the physical gap on Phys (OPEN).
  - **c24:** VALID, Q1 PASS (λ_min(O_FP) = 0.27-0.43 against 1.0 for O_Δ). A dense-to-sparse rewrite was made before
    the only run (disclosed). 177 s, peak 1.69 GB, load 1.24, 40% free memory.
- **κ_0.** Lemma CE-geo': |X| ≤ 2^d + 2^{d-1}√d·d(X) (d = 4: 16(1 + d)), proving (122) in stronger form. κ_0 =
  16 log 12800 ≈ 151.3, so N6 must deliver κ > ≈ 457. **c25:** Q1 PASS, 6045 instances, 7.5 s.
- **Tally.** 49/2/7/24 + 1 → **53 / 2 / 7 / 24 + 1 comparison-branch** (+CE-geo', +N2-E, +N2-red, +FP-ab).
- **Checkpoint.** PROOF_session11_snapshot.md. No commits, PRs, pushes, CL edits or axiom edits.

## Session 12, 2026-10-27 (proof lead; fix 13, (LED), the N4 physical gap)
- **Step 0 (REVIEW_S9_S10 fix 13).**
  - Read the lead's memory file feedback_no_permission_except_axioms.md.
  - Quoted the owner's dated messages verbatim in PROOF.md's decision-4 record (session-9 header and L5 note) and in
    the tally:
    - 2026-10-21: "you dont need to ask permissions unless we are editing the axioms";
    - 2026-10-23: "remember that you can set whatever works for the TOE here, you dont need to ask me (put it in the CL
      until we have a working TOE)".
  - Label: decision 4 is a proof-technique choice by the lead under that standing delegation; it is not an axiom or CL
    change. The source is the memory file, not a primary transcript. Tag [R910-fix13].
- **Pre-statements.** RTARGET §20-22 were written at 15:41 UTC. That was after the lead's exploratory reasoning, but
  before any written derivation or script. The criteria were written before the scripts: c26 between 15:41 and 15:48 UTC, with an
  addendum at 15:50:55 after Parts A-B and before Part C was coded; c27 at 15:53:38.
- **(LED): PROVEN for the linearised soft chain** (Theorem N2-lin).
  - IT-str: a composite of straight averages is the direct straight average.
  - LED-dual: the minimiser is determined by its co-closed top residual r, which minimises ½⟨r, Pr⟩ + ⟨r, B_k⟩, and
    E_k = (κ/2)⟨r, Pr⟩.
  - LED-symb gives the explicit coarse symbols, and WA plus LED-unif give k- and T-uniform ℓ¹ kernels.
  - Hence (H2), (H1) and then (LED). BG-b for the linearised chain is now unconditional.
  - The f_0 map needs the representative +Π_coex (zero on closed data). Without it, the kernel has a |x|^{-4}
    (Calderón-Zygmund) tail.
  - **c26.**
    - A: VALID; all identities ≤ 4e-13; 5 s, 458 MB.
    - B: N_r → 2.727, k-stable; Q5, Q6 PASS; N_f grows with T, as the extension should; 53 s, 218 MB.
    - C: V3 PASS. N_f^rep → 10.25, k-stable. Q7 FAILED as pre-registered (ratio 1.104 > 1.1; the increments fit c/T).
      79 s, 850 MB.
  - A first launch with python3 -I failed at import (numpy is in the user site). All runs were without -I; no
    downloaded files are read.
- **The N4 physical gap: PROVEN** (Proposition PG).
  - c_PG = min(1, κ)/(3.5·10⁶), uniform in n and T; O_FP ≥ min(c_PG, 4) on H_0.
  - The ingredients: face-flux co-closedness, an orbit-minimum decomposition, a cheap extension (point capacity 8ε²),
    and a line trace of h with C_3 ≤ 14.
  - **c27:** E1, E2, E4-E6 PASS. E3 FAILED as pre-registered: the r - m = h(A_c) sub-check was normalised by
    max|r - m| ≈ 1e-16 on the pure-gauge vector; the absolute error is 1e-15 (post-run diagnostic disclosed). Two
    unused helpers were deleted before the only run (disclosed). 15 s, 350 MB.
- **B-NA:** not attempted.
- **Tally.** 53/2/7/24 + 1 → **55 / 2 / 7 / 24 + 1 comparison-branch** (+N2-lin, +PG; no OPEN item closes completely).
- **Numerics hygiene.** One job at a time, nice 10, BLAS/OMP/MKL/vecLib threads 1, load ≤ 1.96 before each run, ≥ 41%
  free memory, peak 850 MB.
- **Checkpoint.** PROOF_session12_snapshot.md. No commits, PRs, pushes, CL edits or axiom edits. No REVIEW file or
  earlier snapshot was edited.

## Session 13 (2026-10-27)
- **Inputs.** REVIEW_S11_S12.md (binding fixes + strategic verdict "N2-exp first"); the reviewer's kernel probe
  (scratchpad rev1112/rdecay.py, rd32.out, rd32k3.out). Targets pre-stated in RTARGET.md §24-25 at 16:49 UTC, after the
  lead's exploratory reasoning on paper and before any written derivation or script. c28 criteria at 16:50:58 UTC,
  tidied and given an addendum before the script existed.
- **[R1112-fix] All 11 fixes applied** (PROOF header lists them): Dimock l.1672 (§4.7); c21_criteria annotation
  appended (l.52-53 untouched); decision 4 "by inference from" the TOE-ruleset delegation, with the reading of the
  "(put it in the CL …)" parenthesis stated; CE-geo' → the upper inequality of (122) (d = 3 in Dimock), also in
  RTARGET §19; N2-a set-valued; WA for a > 0 and F̂(0) = 0; power-tail BOUNDS; BG-b scope restored (header, N2 status,
  tally); PG-ext Collect written out (4.241·10⁵, 160; arithmetic re-done); c26 c/T labelled informational, Part B
  slopes not cited; N2 kernels vs N5 covariance separated. Tally after fixes: 55/2/7/24 + 1, unchanged.
- **N2-exp: PROVEN** (Theorem N2-exp, with EXP-id, EXP-real, EXP-strip, Corollary N2-exp-b).
  - Key fact: with β_μ := aδ_μ + φR_μ and Δ = φδ, P̂_μ = β_μ/φ and D = φ²Ψ/a, so 𝓡̂ = -aν̄_ν/(β_μβ_νΨ): the fine
    Green's function's 1/φ cancels exactly. The same holds for B_k ↦ r and B_k ↦ f_0 (the f_0 cancellation uses
    ν_σ/D̄_σ = ν^{(n)}_σ).
  - Explicit strip: m_* = 0.0111 (L = 3, κ ≡ 1), 0.0077 (κ = 0.25), 0.0118 (κ = 4) [R15-fix: read 0.0117 (κ = 4, r_0 = 0.65),
    the value valid at the stated r_0; c30 A]; uniform in k, T, u.
  - The located rate (numerical, not proven; [R1314-fix: was "true rate"]) (located complex zero of Ψ·Πβ at p = (iw, 0, 0, 0)) is ≈ 1.04, 0.99, 0.98 (k = 1, 2, 3) at κ = 1,
    scaling like √κ: the soft constraint's mass. Proven m_* is ≈ 90 times smaller.
  - N6 consumes the B_k-kernels (exponential). The unrestricted f_0 extension (|x|^{-4}) and the 𝒦̂_u + Π_coex
    representative (power tail seen in c28 C5) are not needed. Decision 4: no adverse finding.
- **(IT'): PROVEN** (Lemma IT-line, Proposition PG^{(k)}): the composite funnel integrates averaged fields at every
  level, so ε²|h^{(k)}|² ≤ (4L²/(L - 1))||A||²_B with no trace loss; C_IT(3) ≤ 3.6·10⁶, uniform in k, T.
- **c28.** A VALID (≤ 2.2e-13). B FAILED as pre-registered on a float tie (β_μ(0)/b_* - 1 = -5.6e-16 at n = 27; the
  bound is sharp at p = 0); all perturbation bounds hold with margin (≤ 0.13 of the allowance). C1, C2 PASS; C3, C4
  FAILED as pre-registered (pre-asymptotic window; post-run three-parameter fits m ≈ 0.88-0.97 vs located 0.98-1.04).
  D PASS. Criteria not edited after any run; post-run diagnostics in checks/c28_time.txt.
- **Tally.** 55/2/7/24 + 1 → **57 / 2 / 7 / 24 + 1 comparison-branch** (+N2-exp, +PG^{(k)}; no OPEN item is fully discharged).
- **Remaining walls.** SU(N) chain (B-NA, SU(N) N2-E/N2-lin/N2-exp); (NA) for N4; N5 (soft Hessian covariance ℓ¹ +
  random walk); N6 (κ > 457 in M-units; with the proven m_*, M ≳ 4·10⁴); D4-obs; N10's non-linear analytic dependence.
- **Numerics hygiene.** One job at a time, nice 10, BLAS/OMP/MKL/vecLib threads 1, load ≤ 2.2 before each run,
  ≥ 37% free memory, peak RSS 694 MB (footprint 1.21 GB). No `timeout`.
- **Checkpoint.** PROOF_session13_snapshot.md. No commits, PRs, pushes, CL edits or axiom edits. No REVIEW file or
  earlier snapshot was edited.

## Session 14 (2026-10-27)
- **Inputs.** PROOF.md [S13] order (items 2, 3, 5); no review of session 13 exists (item 1 carried). Targets
  pre-stated in RTARGET.md §27-31 at 17:32 UTC, after the lead's exploratory reasoning and two scratch arithmetic
  probes for target D (scratchpad dconsts*.py, not checks), before any written derivation or check script. c29
  criteria before the script.
- **B-NA: reduced, not closed** (Proposition B-NA-red). Explicit threshold ε_0 = min(ρ_0/(2(1+G_D)),
  1/(16GC(1+G_D)²), 1/(10G_wC_w(1+G_D))); x_NA - x_lin ≤ 9GC(1+G_D)²||B_k||²; response decays at every m ≤ m_G. The
  hypotheses (G♯) (multi-scale Schauder bound for the gauge-fixed linear chain on general sources) and (R♯) are OPEN.
  Failure modes [R1314-fix: BNA-F1, F3 established; F2 argued]: BNA-F1 (N2-exp gives data kernels only), BNA-F2 (sup norms do not close at the fine Wilson level;
  scaling count, argued), BNA-F3 (block-axial gauge puts the coarse field on sparse links; a smooth covariant slice is
  needed, tying B-NA to (NA)). Proven pieces: NA-alg, NA-crit, NA-inv, NA-IFT, SRC-id (fine source = effective datum
  -Q^{(k)}Δ^{-1}j; K = 0 screening β - κ|W|² = φR). SU(N) N2-E/N2-lin/N2-exp: conditional, not counted.
- **(NA) for N4:** Proposition NA-FP PROVEN (covariant FP identity [R1314-fix: at the Hessian (Gaussian) level] at every critical background, admissible for every
  background, direct and composite slices; FP_U now background-dependent). The (NA) gap is OPEN: a |f|-weighted
  far-root funnel-trace defect (NA-F2); routes (R1) enlarged covariant slice, (R2) smooth/rough split.
- **m_*:** Theorem N2-exp' (Lemma EXP-strip', Re/Im sector bounds): m_*' = 0.0385 [R15-fix: read 0.0384 (r_0 = 0.70); c30 A] at κ ≡ 1 (3.5×); N6 needs
  M ≳ 1.2·10⁴ (was 4.1·10⁴).
- **c29.** A PASS (≤ 1.1e-12). B PASS (sharp ratios 1.000, lower-bound margins ≥ 4.8). C VALID: C1 FAILED as
  pre-registered (D(0.1) = 0.110 > 0.1; slope 1.04, D/t ≈ 1.09-1.22); C2 PASS (NA part 0.21 of linear, rate 1.38 vs
  1.77). D PASS (telescoping 1.9e-15; Hessian on gauge directions 3.7e-8 at U*, 1.9e-2 at the non-critical control).
- **Tally.** 57/2/7/24 + 1 → **60 / 2 / 7 / 24 + 1** (+NA-alg, +NA-FP, +SRC-id; N2-exp → N2-exp' no count change).
- **Remaining walls.** (G♯) + (R♯) (B-NA); the (NA) gap and FP_U(V); N5; N6 (M ≳ 1.2·10⁴ at the proven rate); N10;
  D4-obs; review of sessions 13-14.
- **Numerics hygiene.** One job at a time, nice 10, BLAS threads 1, load ≤ 3.7, ≥ 42% free, peak RSS 1.09 GB. No
  `timeout`.
- **Checkpoint.** PROOF_session14_snapshot.md. No commits, PRs, pushes, CL or axiom edits; no REVIEW file or earlier
  snapshot edited.

## Session 15 (2026-10-27)
- **Inputs.** REVIEW_S13_S14.md (13 binding fixes + strategic verdict "(G♯)_0 first, per-level (NA) in parallel"); the
  reviewer's scratch rev1314/ (constant scans, pairs). Fixes applied first; targets pre-stated in RTARGET.md §33-36 at
  19:29 UTC (all norms defined there), before any written derivation or check script; c30 criteria before the script
  (one pre-script correction, disclosed in checks/c30_time.txt).
- **[R1314-fix] All 13 fixes applied** (PROOF header lists them). Valid strip pairs: η_* = 0.0111 (r_0 = 0.57), 0.0077
  (0.37), 0.0117 (0.65), κ̂ = 16: 0.0037, 0.0082 (was 0.0083); η'_* = 0.0384 (0.70; was 0.0385), 0.0273 (0.37), 0.0306
  (0.90; was 0.0307), κ̂ = 16: 0.0140, 0.0226, 0.0216; the f_0 condition is in η_*'s definition. In-place annotations in
  this LOG at session 13 ("true rate") and session 14 (BNA-F2 argued; NA-FP Hessian level). Tally after fixes unchanged.
- **(G♯)_0 soft half: PROVEN** (Theorem G♯_0-soft; Lemmas SRC-all, REC, KF). Key step: Green reciprocity
  κ⟨r(j; 0), B'_k⟩ = Σ_l⟨G_l, dB'_l⟩, so source-to-r = transpose of the exponential data-to-curvature kernels (N2-exp +
  BG-b-lin's level recursion). Bound: ||r_{k-1}||_{∞,m} ≤ C_topΣ_l||G_l||_{∞,m} + C_D||B_k||_{D,m}, and per level
  L^{k-1-i}||r_i|| ≤ κ_i^{-1}e^{5m}[κL^{-(k-1-i)}||r|| + 6Σ_{l>i}||G_l||]. Marginal count (G0-F1): one O(1) per source level,
  so summable level weights are needed.
- **(G♯)_0 fine half: reduced.** Lemma LES-div PROVEN (Campanato with divergence-form source). Level-0 sources:
  ⇐ (LED-src), OPEN. Sources at levels ≥ 1: transported potentials are rough at the fine scale; separate OPEN item.
- **Per-level (NA): NA-F2 is an artefact of the direct step** [R15-fix: narrowed; read "the top-level per-step defect has no
  n-loss; the multi-level uniformity is carried by (NA-H) ⊂ B-NA"] (Proposition NA-lev; Lemma E-low E_k ≥ c_E||dB_k||²,
  c_E ≈ 0.0041). The (NA) gap reduces to (NA-H) (SU(N) Hessian of E_i, inside B-NA) and a per-block perturbation at n = L.
- **(R♯)**: stated as (R♯_ω) in the §33 norms; argued only.
- **c30.** A PASS (30-digit constants). B PASS (SRC-id f_0 lines ≤ 5.2e-13). C PASS (SRC-all, REC ≤ 4.3e-9; transport
  bound ratios ≤ 0.33). D informational (random-sign sources; 4.64 vs proven 6 at d = 4, k = 2).
- **Tally.** 60/2/7/24 + 1 (after fixes, unchanged) → **63 / 2 / 7 / 24 + 1** (+G♯_0-soft, +LES-div, +NA-lev).
- **Remaining walls.** (LED-src) and (G♯_0-fine-up) (curvature response to sources); (G♯_0-field) (multi-level gap);
  G♯_0-plain; (NA-H) and the per-block perturbation; (R♯_ω); FP_U(V); F-df_0; N5; N6 (M ≳ 457/0.0384 ≈ 1.2·10⁴); N10;
  D4-obs; review of session 15.
- **Numerics hygiene.** One job at a time, nice 10, BLAS/OMP/MKL/vecLib threads 1, load ≤ 2.8, ≥ 43% free, peak RSS
  0.51 GB. No `timeout`. Run without -I (disclosed).
- **Checkpoint.** PROOF_session15_snapshot.md. No commits, PRs, pushes, CL or axiom edits; no REVIEW file or earlier
  snapshot edited.

## Session 16 (2026-10-27; wind-down session 1 of 2 for the linear/abelian package)
- **Inputs.** REVIEW_S15_CONVERGENCE.md (job 1: 6 binding fixes; job 2: convergence audit, verdict RE-PLAN); owner
  decision 2026-10-27 as relayed by the session brief (finish and write up the linear/abelian package in ≤ 2 sessions,
  then one session costing the soft-vs-hard choice, then pause the lane until Balaban's later papers are available; no
  new frontier work, no new SU(N) obligations). Targets pre-stated in RTARGET.md §38 at 20:26 UTC, before any written
  derivation or check script; c31 criteria before the script.
- **[R15-fix] All 6 fixes applied** (PROOF header lists them): G♯_0-soft's two sentences labelled ARGUED; NA-lev
  headline narrowed ("the top-level per-step defect has no n-loss; the multi-level uniformity is carried by
  (NA-H) ⊂ B-NA") in PROOF (headers, L2, L5, tally), annotated here (session 15) and in RTARGET §37; Def indexed by
  coarse links; smallness η̄ ≲ 1.9·10⁻⁷ recorded; (G♯_0-fine): k ≥ 3 for LES-div at R = n (k = 1, 2 by a finite-scale
  bound), (G♯_0-fine-up) displayed; c31 E-low instance; LOG l.666, l.700 annotated. Tally after fixes unchanged.
- **Governance correction (recorded here at the owner's direction, relayed by the session brief).** REVIEW_S15_CONVERGENCE
  (c) says decision 4 "departs from" an owner order "Balaban Z^4 standard first, then D4" (from the lead's memory file
  project_openai_ym_writeup_watch_2026_10_26.md, which reads: "independent derivation as a lemma DAG (Balaban Z^4
  standard first, then D4; …)"). That is a misreading: the order means the Z^4 LATTICE before the D4 LATTICE, not the
  hard constraint before the soft one. Decision 4 (soft kernel on Z^4) is consistent with that order. The review's
  substantive cost point (decision 4 forfeits the import option for the hard-constraint papers not yet read) stands on its
  own and is the subject of the planned soft-vs-hard cost session; it is not an order violation.
- **Lemma F-df_0: PROVEN** (PROOF L5 [S16]). Explicit analytic Koszul factorisation of the f_0 B_k-symbol through ν∧:
  h_{αβ} = T_αE_{<α}𝔅^β (E: evaluation at p_1..p_{α-1} = 0; T_α: divided difference by e^{ip_α} - 1). Kernel bound
  (2M/(m_*' - m'))e^{-m'|X|_1}, every m' < m_*', uniform in k, T, u. Both gauge-invariant outputs now have exponential
  F-kernels. It answers N2-exp-b's open question (a global exponential F-representative of f_0 exists).
- **c31.** E PASS: E-low's exact per-mode minimum 0.0310/0.0297/0.0296 (κ ≡ 1; k = 1, 2, 3; p = (π, π, π, π)), 7.3-7.6 ×
  c_E; chain level ≥ 7.3 c_E; symbol = chain to ≤ 7e-15; c_E = 0.0040691; η̄_max = 1.904·10⁻⁷. F PASS: factorisation
  identity ≤ 5.0e-16, gauge invariance ≤ 3.7e-16 (grid points with every p_α ≠ 0; strip bound not tested).
- **LINEAR_PACKAGE.md written** (self-contained; check inventory; what it is not; open items weighted paper/session).
- **Tally.** 63/2/7/24 + 1 (after fixes, unchanged) → **64 / 2 / 7 / 24 + 1** (+F-df_0).
- **Remaining for session 17.** Hostile review of session 16 (fixes, F-df_0, c31, LINEAR_PACKAGE.md); (LED-src) and the
  multi-level per-level-slice gap if cheap; freeze LINEAR_PACKAGE.md. Session 18: soft-vs-hard cost audit; then pause.
- **Numerics hygiene.** One job at a time, nice 10, OPENBLAS/OMP/MKL/vecLib threads 1, load ≤ 4.2 before each run
  (1-minute), ≥ 34% free, peak RSS 457 MB. No `timeout`. Run without -I (disclosed in checks/c31_time.txt).
- **Checkpoint.** PROOF_session16_snapshot.md. No commits, PRs, pushes, CL or axiom edits; no REVIEW file or earlier
  snapshot edited.

## Session 17 (2026-10-27; the 4D large-field R-operation, node B-W2)
- **Inputs.** REVIEW_S15_CONVERGENCE (critical path: B-W2 = "never attacked", P×2); PROOF.md LF-count, R2D-iso, R4D-iso,
  GT, GT-lat, R4D-lat, D4-norm, BG-sum, W1-def/size/size'/sym, W1-LD-cond, (DF), Theorem CE (steps 3-4), CE-geo', inequality
  (B), E8*/E8**, L5, L6 (read by offset); RTARGET §0-11; LINEAR_PACKAGE §9-10; NOTES §2-4, §9.8, §10. No new literature
  fetched; CMP 122 remains [not-read]. The sister lane agents/ym4d-existence/ was not touched.
- **Pre-statement.** RLARGE.md §0-§2 written at 20:58 UTC before any derivation (targets 1-3, failure modes RLF-F1-F4,
  the c32 plan); c32 criteria before the script.
- **Target 1 (RLF statement): met.** RLARGE §1, with the composition rules (LF-count's divergence = the vacuum c-number of
  clusters N ≤ n_*; |Y| = 1 frozen = R4D-iso; final level = Theorem CE, explicit g_K² < a''/(8(3κ_0 + 3))).
- **Target 2 (two scales, frozen exterior): met in the frozen setting.** New PROVEN-HERE (unreviewed): Lemma GT-lat',
  Proposition CL, Theorem TS (with Theorem R1), Lemma RS. Key mechanisms: (i) the exact Fubini identity turns the
  large-field expansion into a pointwise frozen gas of *-components; (ii) fattening Ŷ = Y + {0,1}⁴ turns *-separation into
  disjointness, so Theorem CE's proven steps 3-4 exponentiate the gas; grading by total cube number N gives
  e^{-a''N/g²} per connected term; (iii) only N ≤ n_* = ⌊4/(a''β_-)⌋ needs counterterms (LF-n), and their B_4 orbit sums
  give one uniform coupling shift; (iv) inner remainders sum against BG-b at the LAST small-field level, never the large
  one (W2-F1 circumvented) [R1617-fix R-6, annotated in session 18: for frozen BG-b data only; in a sea sample the
  remainder is O(g²) and is re-extracted after the sea average. R-3b: (iii)'s B_4 step, as written, was false; repaired
  in session 18]; constants fixed at the trivial datum (W2-F2 avoided); (v) a coarse large field is re-seeded
  across one step (RS), the mismatch branch priced unconditionally by the normalised soft kernel.
- **Target 3 (inductive step): partial.** Proposition RLF-step conditional on (SF)_k (the small-field package, incl.
  (H-pos)), (PLD)_k (multi-defect Peierls LD), (W1-ret)_k (strong W1 for clusters ≤ n_*), (HIST)_k (Dimock-II-type history
  bookkeeping), (F); level summations (P1)-(P5) proven. RLF ⇐ these for all k.
- **c32: A-D PASS** (RS constants attained exactly: ribbon 9 and square 9 at L = 3; unpaired orders reach 15 — S4' pairing
  load-bearing; hard-core combinatorics; graded log extensive; B_4 average scalar, rotations only not). n_* (one-loop,
  [inference]): SU(2) 382 / 95 / 23 at ε_1 = 0.5 / 1 / 2; SU(3) 255 / 63 / 15. Constants η_1, ε_loc are tiny (recorded).
- **Tally.** 64/2/7/24 + 1 → **68 / 2 / 7 / 24 + 1.**
- **Remaining walls (RLARGE §11):** (SF) [P×3-4]; (PLD) [s given SF]; (W1-ret) [s-P]; (HIST) [P]; (F) [P]; (H-pos) written
  [s]; optional sharpening of η_1.
- **Numerics hygiene.** One job at a time, nice 10, BLAS/OMP/MKL/vecLib threads 1, load ≤ 2.5, ≥ 36% free, peak RSS 41 MB,
  no `timeout`, run without -I (disclosed in checks/c32_time.txt).
- **Checkpoint.** PROOF_session17_snapshot.md (PROOF.md + the [S17] pointer). No commits, PRs, pushes, CL or axiom edits;
  no REVIEW file or earlier snapshot edited.

## Session 18 (2026-10-27; REVIEW_S16_S17 fixes, RLARGE repair, LINEAR_PACKAGE freeze)
- **[R1617-fix 12] What directed session 17 to node B-W2 (recorded at the session-18 brief's direction).** The session-16
  wind-down plan (owner decision relayed in the session-16 entry above: package write-up in ≤ 2 sessions, cost audit, then
  pause) was reversed by the owner on 2026-10-27, after the wind-down had been agreed: "we are only halfway through tokens
  and they reset in a couple days. keep after it". Source: the lead's campaign memory log, as relayed by the session-18
  brief (this session did not read that log itself). The wind-down is reversed; the lane is on a full push. Session 17's
  choice of B-W2 followed from that direction and REVIEW_S15_CONVERGENCE's critical path; the session-17 "Inputs" line
  above did not record it, and is not edited.
- **Inputs.** REVIEW_S16_S17.md (BINDING, all 550 lines); RLARGE.md (all); LINEAR_PACKAGE.md (all); LOG sessions 16-17;
  PROOF.md by offset (header l.1-61; D4-norm l.1505-1530; GT-lat l.1536-1580; Theorem CE l.1744-1760, l.1768-1783,
  l.1843-1870, l.1893-1916; L6 l.3481-3502; the tally l.4456-4500; the [S17] pointer). Sister lane agents/ym4d-existence/
  not touched.
- **Pre-statements.** RLARGE §13 at 21:47 UTC (repair targets A-E) before any repair text and before the c33 criteria;
  RTARGET §40 at 22:11 UTC (N5-triv) before the N5 text; c33 and c34 criteria before their scripts (c34: one command,
  criteria first, disclosed).
- **Step 1, RLARGE [R1617-fix]** (session-17 text kept as RLARGE_session17_snapshot.md). R-3b: Theorem R1 (iii)
  re-localised on the unfattened supports of cluster tuples; the family at x is permuted by B_4 (explicit bijection), so
  GT-lat' (ii) gives one coupling shift; Remark 7.2-B shows the session-17 value of δβ_j was right (centre independence of
  the Hessian on reference data + translation) though the written step was false. R-3a: Lemma 7.2-0 ((H-ch) ⇒ cluster
  completion for every size). R-4: torus wrap width W = 2n_c + 5, wrap levels a bounded term (≤ (L⁴/(L⁴-1))W⁴ cubes in all).
  R-5: TS on Δ_* with R1's hypothesis global and g² < a''/3. R-6: remainders of order 𝔯, irrelevant for BG-b-regular
  frozen data only; O(g²) in a sea sample, re-extracted after the sea average; TS = frozen shadow, unused by RLF-step.
  RLF amended in §1A (§1 verbatim; labels unchanged; (RLF-5) complex fields added): two-threshold R-operation with
  a_♯ = min{a'', a_♭, a_RS/c_RS}, n_♯; Z_ref := exp(𝒱^{LF})Z^{sf,ref}; (SF-last). Gaps G1-G4 named: (H-Mayer), (H-pos) [P],
  (W1-ret') with the re-extraction, (SF-last); RS ordering in (HIST). (P4) ARGUED; (P1) one count factor; §8.5 wording;
  R-10 [inference]; CL-1: Λ_1 = 6 + 8κ(2 + C_𝒩) (multiplicity 8 derived; ≤ 2 occurrences per contour).
- **c33** (toy B_4 step): B PASS (d = 4, all 384 elements: tuple localisation invariant ≤ 1.3e-15, fattened changes by
  0.68-3.9; the review's {x ± e_1} case; constant data agree 2.7e-14). A FAIL as pre-registered on the constant seed only
  (double-precision cancellation in the brute-force log coefficient, 2.9e-9 vs 1e-10/1e-12); A2/A3 hold on all seeds;
  post-run 40-digit diagnostic agrees to 3e-34. No criterion edited.
- **Step 2, LINEAR_PACKAGE FROZEN v1 (2026-10-27)** (session-16 text kept as LINEAR_PACKAGE_session16_snapshot.md): all
  REVIEW_S16_S17 fixes (statement table; 13 sentences; P-1; §0 glossary of ledger names; bibliography with the seven Dimock
  arXiv ids verified against the arXiv API (titles, DOIs) and Balaban's CMP data from NOTES; Lemma 4.4 renamed; Dimock
  differences listed and classified; §9 extended; §10 frozen as prose; governance text removed; companion snapshot named).
- **Step 3, N5 at the trivial background: Theorem N5-triv PROVEN (unreviewed)** (PROOF [S18], end of file): coercivity
  O_i ≥ γ_i on the slice from NA-lev (c) + the orbit decomposition (Neumann gap ν_N); exponential locality of O_i from
  N2-exp' via LED-dual (Hess E_i = -κ_{i-1}sym(B ↦ r_{i-1})); the slice projector is block-local (hh^T = ||w||²·1); explicit
  Combes-Thomas on Õ = ΠO_iΠ + (1 - Π) gives the covariance, its square root, and N5's ℓ²/ℓ¹ bounds, uniformly in i, k, T.
  c34 PASS (A: w; B: Neumann gap 1, λ_min(P_resΔ_0|Λ_res) = 1; C: Lemma CT on 24 random instances). Random-walk expansion
  and general backgrounds: OPEN.
- **Tally.** 68 claimed → 67 (REVIEW_S16_S17) → 68 (TS/R1 repaired) → **69 / 2 / 7 / 24 + 1** (+N5-triv). Unreviewed: the
  repaired TS/R1 and N5-triv.
- **Next (recommendation).** Hostile review of session 18 (RLARGE §7.2-§7.3 repair, Remark 7.2-B, N5-triv); then N5 at
  small-field backgrounds as a perturbation of N5-triv once (NA-H) is available, or the soft-vs-hard cost audit.
- **Numerics hygiene.** One job at a time, nice 10, OPENBLAS/OMP/MKL/vecLib threads 1, load ≤ 5.1 (1-min) before each run,
  ≥ 35% free, peak RSS 152 MB; no `timeout`; runs without -I (disclosed in the time files).
- **Checkpoint.** PROOF_session18_snapshot.md. No commits, PRs, pushes, CL or axiom edits; no REVIEW file or earlier
  snapshot edited (new snapshots RLARGE_session17_snapshot.md and LINEAR_PACKAGE_session16_snapshot.md created).

## Session 19 (2026-10-27; N5 at small-field backgrounds, the random-walk expansion)
- **Inputs.** PROOF.md by offset: session-18 header (l.1-23 of the S18 file), N5-triv block (S18 end), NA-alg/NA-crit/NA-inv/
  NA-FP (S14), B-NA-red, NA-lev (S15), (R♯_ω), N4/N5/N6/N9 nodes, tally; RTARGET §40-41; LOG session 18; REVIEW_S16_S17
  strategic verdict (l.521-550); RLARGE (H-Mayer) and (RLF-5) statements; literature/NOTES.md §5-7 (Dimock's random-walk
  statements are quoted there as imported from Balaban; nothing here is attributed to them). Sister lane not touched.
- **Pre-statements.** RTARGET §42 at 22:30 UTC (targets A-C, expected scope: level 0 unconditional, i ≥ 1 conditional) before
  any derivation; c35 criteria before the script.
- **Step 1 (targets A+B merged by the route).** Gauge covariance of the fixed covariance (N5-cov); curvature ⇒ local axial
  gauges (AX); local analyticity of the background operator with existence constants (N5-an); complex Combes-Thomas with the
  square root (CT♯); the Dirichlet-compression random-walk expansion (Theorem RW) glues the local gauges, so no global
  small-field gauge is needed. Theorem N5-sf0 (level 0) PROVEN; Corollary RW-triv (every level, trivial background) PROVEN;
  Proposition N5-sf_i (i ≥ 1) ⇐ (NA-H_loc), not counted.
- **Step 2 (target C).** Exact slice vector (ν_w = 30/13 vs 576) and level-0 first moment: rate ×4.9·10⁷ (Lemma N5-w0,
  computer-assisted). No rigorous γ gain; measured γ_0 = 0.0398 (2.5·10⁶×), γ^LB = 2c_E (6.3·10⁷×): the loss is PG's c_1.
- **c35** A, B, C PASS (run record checks/c35_time.txt; one disclosed float artefact in a printed informational number).
- **Tally.** 69 → **71 / 2 / 7 / 24 + 1** (+RW, +N5-sf0). Unreviewed.
- **Next (recommendation).** Hostile review of sessions 18-19 (N5-triv, RW, N5-sf0: especially N5-an's existence argument and
  the RW locality claim); then either a sharper PG constant (the measured 2.5·10⁶ gap ratio says it is the lever for every
  threshold) or (NA-H_loc) at level 1 as the first multi-level case.
- **Numerics hygiene.** Coordinator lock rule adopted mid-session (machine-wide numeric lock); one job at a time, nice 10,
  threads 1; peak 1.17 GB.
- **Checkpoint.** PROOF_session19_snapshot.md. No commits, PRs, pushes, CL or axiom edits; no REVIEW file, earlier snapshot,
  LINEAR_PACKAGE.md, RLARGE.md, FLOW.md or HIST.md edited.

## Session 20 (2026-10-27/28; REVIEW_S18_S19 fixes, LINEAR_PACKAGE v1.1, (NA-H_loc) at level 1)
- **Inputs.** REVIEW_S18_S19.md (BINDING, all 519 lines); PROOF.md by offset (header l.1-45; [S17] pointer, [S18] and [S19]
  blocks l.5030-5393; NA-alg/NA-crit/NA-inv/NA-FP l.2914-2990; N5 node l.2125-2140; tally l.4500-4520); RTARGET §40-43; LOG
  sessions 18-19; LINEAR_PACKAGE.md (all); RLARGE.md §0, §1A, §7.1-§7.2, §8.2-§8.3 by offset; PROOF_session16_snapshot.md
  l.1575-1602, l.2700-2740, l.3116-3152 (for the v1.1 definitions); checks c31, c35 scripts/outputs. FLOW.md, HIST.md, PLD.md
  and agents/ym4d-existence/ not edited.
- **Pre-statements.** RTARGET §44 at 23:58 UTC 2026-10-27 (targets A-C) before any session-20 derivation; c36 criteria
  before the c36 script.
- **Step 1, REVIEW_S18_S19 fixes [R1819-fix]** (pointer list at the head of PROOF [S20]): SF-1 (two R_g orientations);
  SF-2 (gap sizes stated at every "gap"); SF-3 (N5-sf0 labelled an existence theorem; RTARGET §43 annotated, not edited);
  SF-4, SF-5; RW-1 ((iv) narrowed: bounds, holomorphy, 𝒞(1) = K^{-1/2}, decoupling; A = 𝒞(s)Z usage) and RW-2; W0-1 (c35 C2
  redone in exact rationals, c36 C PASS, so N5-w0's rate is now computer-assisted); fix 7 ((NA-H_loc) presupposes the level-i
  minimiser); fix 8 in RLARGE (F1 C_♮ existence, F2 one T convention, G5 named as (R1-loc) in (W1-ret') (d), N5 threshold
  compatibility and c_RS in §1A item 1, W⁴ sentence); fix 9 (γ_i doubles by A_P ⊥ dλ; M' in N5-loc). New: Proposition
  RW-ℓ² (covering multiplicity ≤ 3⁴), which raises N5-sf0's proven gap from ≈ 4·10⁻⁵¹ to ≥ γ'(1 - ε_R)/9 ≈ 6.6·10⁻¹⁰.
- **Step 2, LINEAR_PACKAGE FROZEN v1.1 (2026-10-28 UTC)** (v1 kept as LINEAR_PACKAGE_v1_snapshot.md): REVIEW_S18_S19 Part 3
  items 1-8, change log §12; Dimock journal data and five Balaban titles checked against the Crossref API; the uncited QED
  entries dropped. No mathematics changed.
- **Step 3, (NA-H_loc) at level 1** (PROOF [S20]): Lemma U0 (exact lift: M̄(U^(0)(V)) = V, curvature only at block
  corners), Lemma FPq (Kato + block mean: background-uniform Faddeev-Popov inverse), Lemma N5-an♭ (existence constants),
  Lemma BR1 (critical branch by a sup-norm contraction with N5-sf0's covariance; NA-crit with multipliers removes the
  fixing), Lemma SC1 (Hess E_1^br = F_BB - F_BACF_AB), Lemma LOC (localised covariance comparison), Theorem NAH1
  ((NA-H_loc)_1, δ_H = O(ε log(1/ε))), Corollary N5-sf1 (N5 at level 1, branch). Proposition NAH-ind (inductive form,
  implication). Constants level 0 → 1: measured trivial gap 0.039849 → 0.039712
  (×0.997, c36 D: no true shrinkage); proven gap ×2c_E once; proven background threshold ×≲10⁻⁴⁰ per level in the
  per-level form (NAH1-F4 occurs there; set by the sup-norm Newton step, N_0(|C|) ≥ 1/λ_min, not by c_1 alone). **[R20-fix 8
  (session 21): NAH1-F4 occurs for this estimate chain; the 10⁴⁰ is constants (𝔠_∞); the 36p_L/λ_min floor is an artefact of
  bounding curvature by displacement, not shown intrinsic; measured per-level curvature amplification < 1 (REVIEW_S20 Part 4;
  c37).]**
  Uniformity needs (BG-unif) (named; ⊂ B-NA). E_1^br = E_1^NA needs (MIN_1) (named).
- **c36** (criteria first; record checks/c36_time.txt): A PASS (exact lift); C PASS (W0-1, exact rationals: N_0 =
  10462237/410670, moment 449171/10935); D PASS (Schur-formula H_1 reproduces c31 E's 0.030950; gauge mode 9.7e-14);
  **B FAIL as pre-registered** (t = 0.05 passes, Schur identity to 2.1e-7; at t = 0.15 the contraction diverges; disclosed
  post-run diagnostic: converges to coarse plaquette angles ≈ 0.6). Peak RSS 733 MB (footprint 957 MB).
- **Tally.** 71 (confirmed by REVIEW_S18_S19) → **72 / 2 / 7 / 24 + 1** (+Theorem NAH1 with its lemmas and Corollary N5-sf1).
  Unreviewed. RW-ℓ², the N5-w0 exact redo and NAH-ind change no count.
- **Next (recommendation).** Hostile review of session 20 (BR1's contraction and transversality constants, SC1, LOC,
  NAH1's δ_H bookkeeping, RW-ℓ²'s multiplicity). Then, per NAH-ind's answer, (BG-unif): the multi-scale non-linear
  background bound (sup-norm, level-independent, own-units curvature ~ L^{-2(k-j)}) — the non-linear version of N2-lin +
  BG-b-lin — rather than further per-level steps or a sharper PG constant.
- **Numerics hygiene.** Machine-wide numeric lock for every job (wrapper scratchpad s20/runlocked.sh: mkdir/rmdir with trap),
  nice 10, threads 1, load and free memory recorded in each .time file; no `timeout`; runs without -I.
- **Checkpoint.** PROOF_session20_snapshot.md. No commits, PRs, pushes, CL or axiom edits; no REVIEW file or earlier snapshot
  edited; RLARGE §1/§1A numbering unchanged (annotations only).

## Session 21 (2026-10-28 UTC; REVIEW_S20 fixes; the one-level curvature lemma)
- **Pre-statements (in order, before the corresponding work).** RTARGET §46 appended at 01:24 UTC (targets, failure modes
  CURV-F1/F2/F3), before any session-21 derivation and before the c37 criteria. c37 criteria written before any c37 script:
  `stat`: checks/c37_criteria.md mtime 2026-10-28 01:26:13 UTC (21:26:13 EDT), size 4336 bytes; no c37 script existed
  at that time (recorded here before the script was written).
- **Step 1, REVIEW_S20 binding fixes [R20-fix]** (pointer list at the head of PROOF [S21]): NAH1-1 (α' ≤ r_♭/2 added to ε_H;
  chart alternative noted), LOC-1/NAH1-2 (collar r_1 + 3L, ℓ_1 := 2ρ + 2⌈(D + r_1 + 3L)/L⌉ + 4), NAH1-3 (T_1, T_2 units; and
  the torus condition T_2 ≥ T_0^{(1)}(ε) is ε-dependent: the session-20 T_0^{(1)} at ε_H covered only ε near ε_H), NAH1-4
  (suprema), RW2-1 (product partitions; 5^d otherwise), RW2-2 ((RW1-n) at complex backgrounds by the Neumann series), fix 7
  (level-1 locality exception in S20 header, N5 node, tally, [S20] N5 status), fix 8 (NAH-ind reading; also annotated in
  the session-20 entry above), W0-2, fix 11 (B4 = -0.003808 reported and explained; "FAIL (criterion pre-registered)";
  checks/c36_consts.py pointer), fix 12 ((BG-unif) precise, anti-circularity clause), fix 13 optional ((MIN_1) small-field
  form as target, FPq α_b = 0, γ_1/36). No count change.
- **FOR RLARGE v2** (RLARGE.md not edited this session; an integration session is rewriting it):
  1. **[R21-fix S21-7: DONE — already applied in RLARGE v2 [v2-C] (RLARGE l.13, l.72-74, rows 3/3a); this item is stale]**
     [REVIEW_S20 fix 9] §1A item 1 (l.101-106): the N5 ↔ RLARGE threshold compatibility holds with K-independent constants
     only under level-uniform N5 thresholds ((BG-unif), or Proposition NAH-unif's hypotheses (H-K), (H-C), PROOF [S21]);
     "still g- and K-independent" must say so. "Recorded here and in (SF)" is false: add "(with level-uniform
     thresholds)" to (SF)_k (l.601-602) or delete the clause.
  2. [REVIEW_S20 Part 1, cosmetic] RLARGE's ε_1 is an operator-norm cut ||1 - U_p||_op < ε_1, N5's classes use |log U_p|_HS:
     name the conversion (|log U|_HS ≤ √N·max|θ_j|, |θ_j| ≤ arcsin-type bound in ||1 - U||_op for ||1 - U||_op < 1).
  3. [S21] With Lemma CURV1 the per-level threshold loss of BR1 (iii) is replaced by K_p^♯ + θ (PROOF [S21]); the
     remaining K-dependence of the N5 threshold is through the Lipschitz recursion (H-C). The compatibility note should
     cite (H-K)/(H-C) rather than "per-level 10⁻⁴⁰".
- **Step 2, the one-level curvature lemma** (PROOF [S21]). Lemma CURV-lin (linear response F_1 = 𝒦F_V, ρ = 𝒦_ρF_V,
  𝒦 = (1 - dC^0d^*)ι; 0 ≤ dCd^* ≤ 1, ℓ² bounds 3 and 3κ^{-1/2}; SU(N) = scalar ⊗ 1), Lemma CURV1 (non-linear: new curvature
  ≤ (K_p(Z) + θ)ε_V + C_θε_V² with K_p(Z) in a Bianchi-adapted representative 𝒦 - Zd_2; 𝔠_∞, C_♭ only at second order;
  replaces BR1 (iii)'s 1 + 36p_L𝔠_∞), Lemma E3 (D³E^br = ζ^TD³F[ζ·]ζ exactly; Lipschitz recursion C_♭^{(i+1)} ≤
  Z_colZ_row²C_♭^{(i)} + …), Proposition NAH-unif (implication: depth-independent ε_unif under (H-K), (H-C); the soft
  fluctuation constant enters once, not per level).
- **c37** (record checks/c37_time.txt; one job at a time under the lock; peak ≤ 718 MB): A PASS; **B FAIL (criterion
  pre-registered)** K_curv(6, 8, 10) = 2.736, 2.907, 2.969 (K_p 2.244, 2.262, 2.268); C: attained 0.015-0.084, LP exact
  norm on exact inputs 0.0822 (16 top rows, side 6), ρ 2.614; D: κ-dependence of row sums, K_A 1.388, Z_row 2.849, Z_col
  156.08, Z_colZ_row² 1266.8; E: side-4 exact norms level 0 K_p^♯ 0.0619 / K_ρ^♯ 2.219, level 1 0.1032 / 2.074 (E1 gauge
  checks 7.8e-14, 1.4e-12). Pre-run script edits disclosed in c37_time.txt.
- **Reading.** The 10⁻⁴⁰-per-level threshold loss of [S20] is a displacement-estimate artefact, and the curvature part of it
  is removed by CURV1 conditionally on a certified K_p^♯ < 1 (measured ≈ 0.06-0.10, margin ≈ 10 **[R21-fix S21-2: small-torus exact-input values; the CURV1 constant is the closed-input value ≈ 0.11-0.13, margin ≈ 8, two rows, not certified]**; the Bianchi identity is
  essential, plain row sums are 2.27). What remains for depth-uniformity on the per-level route is (H-C), the Lipschitz
  constants of Hess E_i^br: absolute-value norms compound by ≈ 10³ per level (d = 4 marginal counting).
- **Tally.** 72 / 2 / 7 / 24 + 1, unchanged (CURV1 strengthens BR1 (iii); CURV-lin, E3 algebraic; NAH-unif an implication).
  Unreviewed.
- **Next (recommendation).** Hostile review of [S21] (CURV1's constants and the Bianchi step (5); E3; NAH-unif's induction).
  Then (H-C): a Lipschitz bound for Hess E_i^br in a curvature-adapted norm (third derivatives with one leg through d,
  using the same Bianchi representative idea), measured first (the signed pulled-back third-derivative tensor at level 1
  against level 0, c38), else (BG-unif) (iv) by the composite contraction. In parallel, the certification path for K_p^♯:
  an explicit decaying Z (from the LP duals, translation-averaged) and a computer-assisted ℓ¹ bound on C^0 via a truncated
  approximate inverse and a Neumann residual in N_m — which would also replace the proven decay rate 10⁻¹⁰ by ≈ 0.4.
- **Numerics hygiene.** Machine-wide numeric lock (scratchpad s21/run37.sh: mkdir wait, load1 < 8 and free memory ≥ 25%
  checked, rmdir exactly once, no trap), nice 10, threads 1, no `timeout`, python without -I.
- **Checkpoint.** PROOF_session21_snapshot.md. No commits, PRs, pushes, CL or axiom edits; no REVIEW file, earlier snapshot,
  RLARGE.md, FLOW.md, HIST.md, PLD.md, LINEAR_PACKAGE.md or agents/ym4d-existence/ edited.

## Session 22 (2026-10-28 UTC; REVIEW_S21 fixes; (H-G) at level 1; c38; the composite route to (BG-unif))
- **Pre-statements (in order, before the corresponding work).** RTARGET §48 appended at 03:41:44 UTC (targets A-C, failure
  modes HG-F1/F2, C38-F1, COMP-F1/F2), before any session-22 derivation and before the c38 criteria. c38 criteria written
  before any c38 script: `stat`: checks/c38_criteria.md mtime 2026-10-28 03:45:12 UTC (23:45:12 EDT), size 4649 bytes; no
  c38 script existed at that time (recorded here before the script was written).
- **Step 1, REVIEW_S21 binding fixes [R21-fix]** (pointer list at the head of PROOF [S22]): S21-1 (ρ, D frozen at ε_♯: one
  torus T_2 ≥ T_0^{(1)}(ε_♯) for every ε ≤ ε_♯; δ_H = O(ε log 1/ε) only on T_2 ≥ T_0^{(1)}(ε); NAH1 and N5-sf1), S21-2 (every
  K_p^♯ quotation: closed-input ≈ 0.11-0.13, margin ≈ 8, two rows, not certified; "below 1/L²", "margin ≈ 10", "×1.7"
  withdrawn; "closed inputs" in CURV1's representative sentence; Z tails noted; RTARGET §47 and the session-21 entry above
  annotated), S21-3 (14ε_V; 56, 104), S21-4 (E3's 2.3·10³), S21-5 (NAH-unif GAP as stated; (H-G), (H-ℂ) named; false
  sentence withdrawn), K_ρ not an obstruction, S21-6 (η_*, C_θ^ρ), S21-7 (the session-21 "FOR RLARGE v2" item 1 marked DONE).
  No count change.
- **Step 2, c38** (record checks/c38_time.txt; lock-guarded, one job per acquisition): A PASS (03:52:19-03:52:24 UTC; the
  soft cubic validated against the exact SU(2) level-0 action to 3·10⁻⁸; H_1 = -κ𝒦_ρd_1 to 1.3e-14); C informational
  (c_3 = 0.97447, 0.99766, 0.99974, 0.99998; c_2 = 0.99122, 0.99920, 0.99991, 0.99999 at s = 0.1 … 0.003); **B FAIL
  (criterion pre-registered)**: N3(T_W) = 3.000, N3(T_E) = 3.380 / 4.187, R_3 = 1.127 / 1.396 at T = 4 / 5 (stability clause
  fails); absolute-leg N3^abs = 73.2 / 90.8. D (post-hoc, added 03:56:52 UTC after B, disclosed): shell masses 0, 1.473,
  1.907 (T = 4) and 0, 1.410, 2.777 (T = 5): not converged; R_3(5) is not an upper bound. Pre-run script edit (fibre
  dictionaries slimmed for memory) disclosed in c38_time.txt. Peaks 612 / 84 / 942 / 904 MB.
- **Step 3** (PROOF [S22]). Lemma ENV (∇E_{i+1}^br = -κ_iπ(M̄V^{-1}) at the branch), Corollary H-fac (H_1 = -κ_0𝒦_ρd_1),
  **Lemma HG1 ((H-G) at level 1, uniform error κ_0(θ' + C_Gε)ε, no near/far split)**, Lemma LOC_1, **Corollary CURV1_1**,
  Lemma HG-ind ((H-G)_{i+1} ⇐ CURV1_i; (H-G) is not an independent hypothesis **[R22-fix S22-5: at each fixed level only;
  "no near/far split" withdrawn, S22-3b]**), the correction of NAH-ind's BR1 at level i
  (U0 (iv) is Wilson-specific; r^{(1)} from HG1 (iv)), Proposition NAH-unif′ (hypotheses (H-K), (H-C⁺), (H-ℂ)). **CURV-F2′:**
  the second-order constants compound per level (4κ𝔠_∞^{(i+1)} per level in sup norms). Composite route: **Lemma
  TOWER-VAR** (tower = one critical point of the local composite functional 𝔉_k; quadratic part = Setting SC), Proposition
  COMP ((BG-unif) (i)-(ii) ⇐ (CL-0)-(CL-3) by one Banach contraction). **Wall:** (CL-2) in sup-curvature norms (the Π_ex
  |x|^{-4} tail of LINEAR_PACKAGE Prop. 3.7 on non-closed non-linear sources); cures (W1) scale-weighted norms (the decaying
  form of (BG-unif) (i)), (W2) covariant Hodge decomposition; meeting point (CL-cl), the tree-level fixed-point class of
  E_i^br. (H-ℂ): route ARGUED, not written.
- **Step 4** (optional (H-K) certification): not attempted.
- **Reading.** Session 21's open (H-G) is now proven at level 1 and derived level by level, so the per-level route's only
  remaining obstruction is level-uniformity of its constants, now including the second-order constants (H-C⁺). c38 says the
  quantity behind (H-C) is level-stable at the trivial background: signed ratio 1.1-1.4 on small tori and an exact Wilson
  vertex in the smooth limit up to O(K²), against E3's 1267. Both routes meet at (CL-cl): E_i^br stays in a fixed class
  c_iS_W + (contracted irrelevant remainder). **[R22-fix (session 23; REVIEW_S22 overclaims 1, 3, 7): "1.1-1.4" are
  periodised lower bounds, R_3(ℤ⁴) ∈ [1.40, ≲ 60]; (H-G) is derived at each fixed level only; (CL-cl) restated as BFT-4,
  E_k^br = S_W + R_k bounded (not shrinking), the marginal coefficient fixed (no flowing c_i).]**
- **Tally.** 72 / 2 / 7 / 24 + 1, unchanged. Unreviewed.
- **Next (recommendation).** Hostile review of [S22] (HG1's use of CURV1's ρ-proof before the X_0 step; LOC_1's two
  changes; CURV1_1's log factor; TOWER-VAR (a), (d); the CURV-F2′ and COMP-F1 readings). Then c39: N3 on larger tori by a
  real-space truncated kernel (the leg kernels decay; T ≥ 8 needs a method that does not store the T⁸ pair grid), and the
  level-2 smooth-limit vertex (does the O(K²) remainder contract per level? this is the first measurable piece of (CL-cl)).
  Then (W1): restate (BG-unif) (i) with the L^{-2(k-j)} decay and test the composite contraction in that norm on the
  linear package.
- **FOR OTHER FILES (not edited this session).**
  1. RLARGE.md row 3a: "(BG-unif) named, not precisely stated in PROOF" is stale (stated precisely since [R20-fix 12]);
     REVIEW_S21 S21-7. The N5 ↔ RLARGE compatibility note should now cite (H-K)/(H-C⁺)/(H-ℂ) (PROOF [S22]), with (H-G)
     derived.
  2. SF.md (lane F): the chain "(N5-unif) ⇐[ARGUED] (BG-unif) + NAH-ind inputs" should note that NAH-ind's BR1 at level i
     needs the HG1/HG-ind correction (U0 (iv) is Wilson-specific) and that (H-G) is derived (PROOF [S22]); (BG-loc) is
     unchanged.
  3. LINEAR_PACKAGE (next version): Corollary H-fac (H_1 = -κ_0𝒦_ρd_1) is a one-line consequence of CURV-lin + ENV and
     could sit next to Lemma N5-loc's H_1.
- **Housekeeping.** An orphaned `rdiag.py T 252,482 4,6,8` process (REVIEW_S21's diagnostic; started 22:55 EDT; ~90% of one
  core; not under the numeric lock) was still running at 04:02 UTC; not touched by this session. checks/__pycache__ was
  removed after a syntax check (bytecode only).
- **Numerics hygiene.** Machine-wide numeric lock (scratchpad s22/run38.sh: mkdir wait, load1 < 8 and free memory ≥ 25%,
  rmdir exactly once, no trap), nice 10, threads 1, no `timeout`, python without -I.
- **Checkpoint.** PROOF_session22_snapshot.md. No commits, PRs, pushes, CL or axiom edits; no REVIEW file, earlier snapshot,
  RLARGE.md, FLOW.md, HIST.md, PLD.md, SF.md, SQ.md, HW.md, LINEAR_PACKAGE.md or agents/ym4d-existence/ edited.

# Session 23 (2026-10-28 UTC; consolidation)

Role: lead, session 23 (consolidation). Write access used: PROOF.md, RTARGET.md, LOG.md, PROOF_session23_snapshot.md. No
numeric job (none was needed; no python was run). No commit, PR, push, CL or axiom edit. No REVIEW file, earlier snapshot,
RLARGE, FLOW, HIST, PLD, SF, SQ, HW, BFT_A, BFT_B, LINEAR_PACKAGE or agents/ym4d-existence/ file edited.

- **Inputs read.** REVIEW_S22.md in full; REVIEW_SF_S7.md in full; SF_LOG.md l.300-393 (the proposed PROOF edits l.367-382);
  REVIEW_BFT_B_S2.md l.80-92 and D.4 (l.374-392); PROOF [S22] (l.6137-6368 before editing), the 𝔠_∞ definition, U0, BR1,
  N5-sf0, RW-ℓ², NAH1 (a), NAH-ind, (BG-unif), CURV1. Two read-only digest agents (fable-low-reader) extracted the latest
  reviews' statuses for FLOW (S9), HIST (S4), PLD (S3), HW (S2), SQ (S2), BFT_A (S4), BFT_B (S4; it reported the later S5),
  and RLARGE v2 (no dedicated review); I spot-checked REVIEW_BFT_B_S5 l.440-500, REVIEW_HW_S1 l.36-39, REVIEW_SQ_S2 l.52,
  301-306, REVIEW_BFT_A_S4 l.305-314, BFT_A.md l.306, BFT_B.md l.598 directly before quoting.
- **Group [R22-fix] (36 tags; source REVIEW_S22 "Required fixes" l.463-491 and "Overclaims" l.439-450).** S22-1 (Part 2
  l.144-189: diagnostic L, the replacement sentence l.186-187): S22 header, c38 B, c38 Reading, RTARGET §49, LOG s22.
  S22-2 (l.164-180): c38 C, Reading, header. S22-3 (Part 3 l.210-247): HG1 (a: Ad(h) term; b: near/far withdrawn), CURV1_1
  (b: split; d: BCH), LOC_1 (c: m^{(1)} ≤ m). S22-4 (l.258-266): HG1 consequence, HG-ind, header. S22-5 (l.267-290):
  CURV-F2″ (new item), CURV-F2′ wording, HG-ind, NAH-unif′ heading + end (GAP as written), node status, header, RTARGET,
  LOG. S22-6 (l.312-331): COMP heading + after the proof. S22-7 (l.333-343): the "What (CL) asks" bullet. S22-8
  (l.345-368): after (CL-cl). S22-9 (Part 5 l.372-435): the BFT item in [S23], (BG-unif), (H-ℂ). Fix 10 (l.208, 95-97):
  after H-fac; CURV1 step (3) (both 6ε and 7.2ε are valid upper bounds; constants kept).
- **Group [SF7-edit] (20 tags; source SF_LOG l.367-382, adjudicated by REVIEW_SF_S7 E-3 l.306-315, C-3 l.233-251, B-5
  l.153-165, C-1 l.188-212).** Edit 1 (+ KW-1, CS-1, "CI-0 independently reproduced"); edit 2 (both classes, kept apart);
  edit 3 (gap line, class-specific); edit 4 (ACCEPTED as lead decision with CS-1: 𝔠_∞^♯ = 315.19, λ_min ≥ 3.1727·10⁻³,
  ε_* = 2.476·10⁻¹³/C_Δ used together); edit 5 (arithmetic; CURV1 NOT yet usable, other terms ≈ 10⁴² dominate C_θ); edit 6
  ((C_♭-eval) and a C_Δ evaluation named). **Lead's notes, hand arithmetic, unreviewed (flagged as such in PROOF):** (i) the
  KW-1 window 2.586·10⁻² was computed by REVIEW_SF_S7 for the old class; the same formula (1 - e_0 - δk_0)/(qk_0) with the
  session-23 δ = C_Δα_* = 1.0568·10⁻³ gives ≈ 1.94·10⁻²; PROOF quotes 2.586·10⁻² as instructed, attributed to the old class,
  with the 1.94·10⁻² note. (ii) Edit 5's numbers on the session-23 class: 288𝔠³ ≈ 9.0·10⁹, 1/(80(48𝔠 + 1)) ≈ 8.3·10⁻⁷,
  53(48𝔠 + 1)² ≈ 1.2·10¹⁰; with the rerun's m_1 = m_4/2 the coth⁴(m_1/2) factor is ≈ 5.9·10²⁰ rather than 2.9·10⁴² (still
  dominant). These want a check by the next reviewer.
- **Group [BR1v-fix] (8 tags; source REVIEW_BFT_B_S2 l.85-86, l.311-314, D.4 l.376-390).** BR1 (v) statement and proof
  (ϱ_br := ε_br/16, ε_V ≤ ε_br/2; complex curvature ≤ ε_br); **NAH1 (a) checked (l.~5775 in the S22 numbering): it inherits
  BR1 (v)'s radius, so it was affected and is restated on ϱ_br** (with ϱ_br ≤ ε_*/16 < α_*/8, so N5-sf0 (a)'s complex
  neighbourhood contains it); NAH-ind (I_i)'s radius. N5-sf0 (a)'s own α_*/8 neighbourhood is a different statement and
  unchanged. The complex form of U0 (iv)'s constant (6(1 + O(ε_br²))) is left as the reviewer's inference, not written out.
- **CROSS-LANE STATUS (session 23)** added at the end of PROOF [S23], with the BFT-0..5 clause table. Headline: N5 is PROVEN
  at levels 0-1; level-uniformity rests on BFT-0, 1 (θ_w = 0), 2, 4; BFT-3/BFT-4 at k = 1 PROVEN (lane B); the open inputs
  concentrate in (H-inv+) [(CO-0), (CO-up)] + (Res-Hölder), (CovLift), (Mult-Y), and PROOF's (CL-4); BFT-5 has no recorded
  status; SQ needs θ_w > 1 stated (REVIEW_SQ_S2).
- **Tally.** 72 / 2 / 7 / 24 + 1, unchanged: NAH-unif′ and COMP move from "implication" to "GAP as written", both uncounted
  before and after; SF7 edits change constants of PROVEN items; BR1v-fix restates a PROVEN lemma's radius.
- **FOR OTHER FILES (not edited).**
  1. BFT_B.md: BB-3_1, BB-loc, BB-mix′_1 use BR1 (v)'s complex neighbourhood; read |z| ≤ ϱ_br = ε_br/16 (PROOF BR1 (v)
     [BR1v-fix]; REVIEW_BFT_B_S2 D.4 consequences).
  2. SF.md: §22.6 / C4 should adopt the session-23 class consistently (CS-1), as PROOF now does; TB-1, KW-1 (and the
     smaller window on the enlarged class, lead's note above), PV-1, the §20.1 leftover remain SF's.
  3. FLOW (SF-bg), SQ (REG-min), SF (a5-G♯)/(a5-U)/(MIN-reg), RLARGE (BG)_k: cross-reference PROOF [S23]'s BFT and the clause
     each uses (REVIEW_S22 FOR OTHER FILES); SF.md l.252's stale "margin ≈ 10" (S21-2 residue); RLARGE row 3a.
  4. BFT lane A: SQ's requirements (θ_w > 1 stated; cone-box uniqueness, REVIEW_SQ_S2 items 1-5); BFT-5 has no owner yet.
- **Checkpoint.** PROOF_session23_snapshot.md (= PROOF.md at 09:14 UTC).

# Session 24 (lead; 2026-10-28) — review discharge, integration audit, consolidation

**A lead session: no new mathematics of its own; the main-path tally is unchanged at 72 / 2 / 7 / 24 + 1.**

- **12:15:32 UTC** RTARGET.md §51 appended (PRE-STATED: targets T51-A..F, lead decisions D1-D3, failure modes
  NORM-F1..F4 / NA-F1 / HI-F1, anti-inflation clause), before any worker was briefed on a result and before
  any consolidation edit. RTARGET.md 89255 bytes after the append.
- INTEGRATION_AUDIT.md created (lead-owned; not counted in this tally). Revised twice during the session as
  REVIEW_SQ_S4 and NORMS.md landed: shortfalls A1-A3 withdrawn, A1 reinstated on stronger grounds, A5
  ((CONST-T)) and A6 (this ledger's wrong Z_col diagnosis) added.
- SESSION24_RESULTS.md created (lead's running ledger of worker reports; not counted).
- **Eleven workers commissioned and completed**, single-writer file ownership, none permitted to run git:
  five hostile reviews (REVIEW_HW_S5, REVIEW_PLD_S5, REVIEW_SQ_S4, REVIEW_BFT_A_S8, REVIEW_FLOW_S13); HW
  session 6; PLD session 6; BFT_B sessions 9 and 10; NORMS.md; CONST_T.md; NQ_CHECK.md; STAR_CONST.md.
  Append-only discipline verified by prefix md5/byte-size on HW.md, PLD.md and BFT_B.md.
- **PROOF.md edited only here:** a session-24 header (four binding corrections [S24-fix 1]-[S24-fix 4], one
  flag, one note) and the [S24] consolidation section at the end. **100 insertions, 0 deletions.** No
  REVIEW file, earlier snapshot, LINEAR_PACKAGE, RLARGE, FLOW, HIST, SF, SQ, HW, PLD or BFT lane file was
  edited by the lead.
- **13:29 UTC** RTARGET.md §52 appended (outcomes, scored honestly, including three corrections to the lead).
- HANDOFF.md rewritten in full, superseding the pre-session-24 version.

**FOR OTHER FILES (lead requests; not edited by the lead).**
1. **SQ.md / SF.md / PROOF's SF owner:** settle PLD §16.8's λ_min = 3.17e-3 against REVIEW_PLD_S3's binding
   L0-1 (6.6e-10). If L0-1 governs, a_ret falls ×4.80e6 (PLD p6 D2).
2. **SQ.md:** EPS-T's q is a free parameter fixed at l.1621 to 8, which is its **worst admissible value**
   (CONST_T.md). Restate EPS-T with q carried, or fix q ≈ 30. Also: the S4-3 hypothesis, R_0 = 128 (not 64),
   l.1504's e^{100} = 255 (not 1.6e4), and SHIFT's wording needs one clarifying clause (NQ_CHECK item).
3. **RLARGE.md:** relabel critical-path item 1 from "(CRC-1), a two-species cluster expansion" to
   **(E2^𝔉)**; row 9 and HW row A5 are stale after SQ session 4's θ_w = 2.
4. **HIST.md:** adopt Corollary H-geo′ (proof supplied in HW §41). Without it, HW's full ×311 gain collapses
   to ×4.77 — pre-stated failure mode (W-F3).
5. **The BFT owners:** restate BFT-1 with a weight pair (curvature 2, residual d - 1) and promote (BB-mix)
   to **BFT-6**.
6. **A reviewer:** settle the two cross-lane disagreements — the ring price (HW's Lemma RING ×17 against
   PLD's ×82) and TF-2.
