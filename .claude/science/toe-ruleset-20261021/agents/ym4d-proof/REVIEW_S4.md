# REVIEW_S4: independent hostile review of PROOF_session4_snapshot.md

Reviewer: an independent agent that did not write the proof. Inputs: the session-4 snapshot (byte-identical to
PROOF.md when read), the session-3 snapshot, REVIEW_S3.md, LOG.md, and checks c13-c15, all re-run. PROOF.md and the
snapshots were not edited.

**Bottom line.** All 30 PROVEN-HERE items survive. Two of the six new items need scope fixes: E8*-sup/E8*-k for
N ≥ 13, and the wording of E8*-ob. No PROVEN-HERE argument uses an IMPORTED-NOT-YET-REVERIFIED lemma. The odd branch
rule is correct, and the 3τ_N/4 numbers are right. The c15 "decision" for E7.2 is not justified by the evidence
offered. Strategically, the lane is producing reductions to open estimates that restate Balaban's own content, and
it has read none of his papers. That is the main risk.

## [R3-fix] audit

All eight fixes are applied.

**Fix 1: the 3τ_N/4 numbers. CORRECT.** I re-derived them by hand.
- Definitions: τ_N = min(1, 2 sin(π/N)), x = 2 arcsin(3τ_N/8), b_0 = 11N/(48π²), so 4N b_0 = 0.09287 N².
- N ≤ 6: 3x² = 1.7733. The products are 0.659 (N = 2), 1.482 (3), 2.635 (4), 4.117 (5) and 5.929 (6).
- N = 7: x = 0.6628, giving 6.000. N = 10 gives 6.096.
- N → ∞: 3·(9π²/4N²)·44N²/(48π²) = 6.1875.
- The SU(2) ratio is 4/0.659 = 6.07.
- t = 3τ_N/4 is admissible in the conditional lemma for N = 3..6, since 0.75 < 2 sin(π/N).
- Conclusion: E7.0 is dense, and so fails in the AF window, exactly for N = 2, 3, 4. This matches c13(R). The t = 1
  values 1.222, 2.750 and 4.889 are also re-derived.

**Fix 4: the single extension S4'' with the odd branch rule. CORRECT: well defined, measurable and
reflection-covariant.**
- Well defined: off the closed branch set B = {eigenvalue −1} the principal log is Borel and continuous; on B it is
  0; B is invariant under inversion and conjugation.
- Odd and covariant: off B, log Z⁻¹ = −log Z (phases stay in (−π, π)) and log(WZW⁻¹) = W log(Z) W⁻¹; on B both are
  trivial. Π_0 is linear and commutes with both.
- Reversal (re-derived): with U'(b) = S e^{X̄}, the reversed link uses S T⁻¹ = S Z⁻¹ S⁻¹, so X̄(−b) = −S X̄ S⁻¹ and
  U'(−b) = e^{−X̄} S⁻¹ = U'(b)⁻¹, using exactly the two identities: everywhere. Gauge covariance (Z ↦ g Z g⁻¹ preserves
  B) and permutation covariance hold.
- On D'_N the logs are already traceless (L1b), so X̄ := avg Π_0 log Z globally equals S4' there.
- What it does not do. It does not make S4'' continuous. The "Price" paragraph states this correctly: consistency
  still needs E8*.
- The reason given for rejecting "link := 1" (w_0 → 0 at β = 0) is sound.

**Other fixes.**
- Fixes 2, 3, 5, 6, 7: applied verbatim (the E8 reading of g, the coarse exact form with FP condition, E7.0' as a
  sufficient condition, E7.0'-AF opened, ζ_1 of largest modulus, the c11 depth limitation).
- Fix 8: FILS cited; first runs kept for c13, c14, c15.

## (1) New PROVEN-HERE items (24 → 30)

**E8*-sup: CORRECT-WITH-FIXES.**
- Re-derived: ribbon ||Z − 1|| ≤ A_L η; c = 4 arcsin(1/4) = 1.0107 (θ/(2 sin(θ/2)) is increasing);
  ||U' − S|| ≤ c A_L η; the straight square gives ||1 − S_p|| ≤ L² η; telescoping gives 4c A_L η. C_1 = 45.39 (d = 4),
  33.26 (d = 3).
- **Fix (domain for N ≥ 13).** The proof asserts "every step is in D', S4'' = S4'" from ||Z − 1|| ≤ 1/2.
  - This holds only while 1/2 < 2 sin(π/N), i.e. N ≤ 12.
  - Counterexample at N = 13: the central element e^{2πi/13}·1 has ||Z − 1|| = 0.479 ≤ 1/2. Its principal log has
    trace 2πi, so it is not traceless and S4'' ≠ S4'.
  - This is the same N ≥ 13 trap that R1 fixed for L7.0.
  - Repair: require A_L η ≤ τ_N/2. Alternatively, keep 1/2 and use ||Π_0 X|| ≤ 2||X||, which replaces c by 2c in C_1.

**E8*-k: CORRECT-WITH-FIXES.** It inherits the N ≥ 13 fix.
- The domain chain is correct: A_L C_1^j η_0 = t C_1^{j−k} ≤ t/C_1 < 1/2.
- L0 nesting keeps every region inside the fine region of b. That region has 2L^{d(k+1)} fine sites.
- Distinct cells for disjoint regions is correct.
- The bound is uniform in K and M, as claimed.
- The usefulness window k ≲ log β/(2 log C_1) is right, and so is the conclusion that it covers a vanishing fraction
  of the levels along AF-rate sequences.

**E8*-ob (constant flux): CORRECT as a statement. The headline wording is overbroad.**
- Re-derived.
  - The fields are abelian. Log Z is the enclosed (1,2)-flux, inside the principal branch while L^{2k−2} A_L η < π/3.
  - For contractible loops in constant field strength, the flux depends only on the shape. So X̄ depends only on μ.
  - In a coarse plaquette the averaged logs cancel in pairs. The coarse flux is L² × the fine flux.
  - The total flux is still one quantum (consistent). Induct.
  - c13(B): 9.00 and 80.48 = sin(81η/2)/sin(η/2). Correct.
- What it shows: any **sup-to-sup** bound has constant ≥ L^{2k}.
- What it does not show: "no deterministic induction goes deeper". Inductions on other quantities are not excluded,
  for example L²-type norms or level-wise probabilistic re-seeding.
- Fix: say "no induction through the fine-plaquette sup".
- The energy-entropy paragraph is correctly labelled heuristic.

**E8*-red (coarse chessboard): CORRECT.**
- Geometry.
  - The boundaries of F_s cells lie between level-m sites. These are resolution-m block boundaries, hence fine link
    planes (L odd).
  - Reflection x ↦ 2t + 3 − x maps cells of F_s to cells of F_s.
  - There are 2L^{M+m} cells per direction (even). The antipodal shift 2L^{M+m} sites is even, so it maps boundaries
    to boundaries. That is exactly why 4L^{K+M} is needed; the S3 convention 2L^{K+M} would fail.
  - Run doubling works with L^{M+m} slabs per half (an odd number is fine).
- Positivity and covariance.
  - Cell events contain no crossing links.
  - By L0 they are measurable functions of positive-half fine links.
  - θ-covariance holds at every finer level, because a level-m block boundary is a level-j boundary for all j > m.
    This uses the odd rule above.
- (ii) Union over ≤ 2L^d lower corners. For r links, the pigeonhole bound gives ≥ r/2^d cells in one family. The
  bound (2L^d)^r q̄_m^{r/2^d} is correct.
- One thing to state explicitly: the extension of L9a to bounded measurable gauge-invariant F. The Osterwalder-Seiler
  argument does cover it, but L9a's REVERIFIED scope should name it.
- Hostile note: E8** is not easier than E8*. It is a global constrained-free-energy bound of UV-stability type, as
  the text concedes. The reduction is real but transfers all of the difficulty.

**H0: CORRECT.**
- Straight legs cross exactly one face, at the position of their own line.
- Axial paths stay inside their block, so they never use face links.
- Distinct coarse links own distinct faces.
- On the centre line the paths are straight and backtrack, so Z ≡ 1.

**H1 (the first Haar step of E7.0'): CORRECT.**
- Re-derived: given G, Z = S⁻¹ α u_ℓ β is conditionally Haar; Π_0 log is odd, so E[Π_0 log Z | G] = 0; cross-line terms
  vanish; Jensen within a line gives m_N L^{−2(d−1)}; m_2 = (4/π)∫θ² sin²θ = 2π²/3 − 1 = 5.580; the W_b are disjoint
  straight products, hence i.i.d. Haar, so E tr W_p = 0.
- Numbers: L = 5 gives 0.158, L = 7 gives 0.4905, L = 3 is vacuous (2321 > 729).
- Scope: "useful for L ≥ 5" is for SU(2) only. For larger N it needs larger L, because m_N grows (m_N ≤ Nπ²).
- c14 bounds reproduced (0.199, 0.551, 0.214, 1.240).

**Interface bond-moving mechanism (c15): not a PROVEN-HERE item, and correctly labelled a finite diagnostic.**
- The 0.5266 match is exact but near-tautological. The synthetic parent recomputes the same MK slot arithmetic on the
  same children as the c11 RRSS node. It confirms the bookkeeping more than it explains the mechanism.
- The stated leading-order law b²/j³ fits poorly:
  - j = 1: predicted 4, measured 1.12.
  - j = 3: predicted 0.148, measured 0.21.
  - Only the qualitative ordering (H2) is supported.
- The corner prediction H4 (1.1201 > 1) is a genuine pre-registered success.
- The H1 tolerance FAIL is honestly kept.

## (2) "E7.2 needs a geometry-weighted norm": NOT JUSTIFIED as stated

- **Self-undermining.** Decision (1) rests on the j = 1 corners (ratio > 1). Decision (3) declares j = 1
  non-contraction an MK artefact with no 4D counterpart. Without it, the only 4D input is the heuristic counting:
  - face rate L⁻¹, bulk rate L⁻²;
  - both are < 1, so a **uniform** per-block contraction at the slowest rate L⁻¹ is not excluded by the document's
    own argument.
- **Moot in the target setting.**
  - In 4D the bare action is homogeneous, so deterministic interfaces do not occur. Interfaces arise from random
    large-field regions, which the R-operation handles (L5).
  - Balaban-type polymer norms are already geometry-weighted (e^{κ|X|}, localised by polymer).
- Downgrade to: "toy-informed design note: the contraction constant should be the face rate, or weighted by type".
- H6 (no compounding beyond the volume fraction) is the useful finding. It is toy-only.

## (3) Citations

- **FILS: confirmed.** J. Fröhlich, R. Israel, E. H. Lieb, B. Simon, "Phase transitions and reflection positivity. I.
  General theory and long range lattice models", Commun. Math. Phys. 62 (1978) 1–34. IHES preprint P/78/224. Upgrade
  the tag from [m] to [v-R4].
  - Nothing rests on it: the special case is re-derived.
  - Seiler, LNP 159 (1982) is the natural gauge-theory reference for link/site RP [m].
- **Dimock arXiv:2009.01156: confirmed.** "Ultraviolet Stability for QED in d=3", J. Dimock, math-ph, v1 2 Sep 2020,
  revised 27 Jul 2021. The abstract matches the proof's paraphrase: Balaban's RG, weak coupling, a UV stability bound
  in a fixed finite volume.
  - No journal reference is listed on arXiv.
  - It is abelian and d = 3, so at best an analogy for E8**. It is not imported, which is correct.
- No fabricated references. The Project Euclid bot block was not bypassed, which is correct.

## (4) Checks re-run

Laptop, OMP/OpenBLAS/MKL/vecLib threads = 1, nice 10, load 1.7-2.1, 37% free memory.

| Check | Result | Time | Peak RSS | vs stored |
|---|---|---|---|---|
| c13 | 6/6 PASS | 2.6 s | 74 MB | identical |
| c14 | 12/12 PASS | 30.8 s | 86 MB | identical except one timestamp (17 s vs 18 s) |
| c15 | 5 PASS / 3 FAIL (H1, H6, H6', as stored) | 5.0 s | 264 MB | identical |

Caveats: c13(A) ratios (0.46, 0.19) are far from the constants; sharpness is c13(B). c14's H1c bounds are vacuous
(negative) at every tested size, so the useful regime L ≥ 5, d = 4 is untested. c15's c = 0 nan rows are benign
(response identically 0; disclosed).

## (5) Strategy

**Blocking imports for pure YM4.**
- L6 (UV stability) and L5 (the large-field R-operation): E8** is essentially their localised form.
- L2 and L3g (background field and fluctuation propagator): any multiscale step beyond fixed depth, and E7.
- L1d (regularity spaces): every iterated averaging bound.
- L4a (AF rate): the E8.3/E7.0 falsifications and E7.0'-AF.
- F1 (Wilson-fermion RP) is not blocking for pure YM.

So 6 of the 7 imports block, and together they are Balaban's programme.

**Converging or circling? Mostly circling, with real but peripheral gains.**
- Every PROVEN-HERE item is one of three kinds:
  - soft (compactness, per-K IVT);
  - first-step or fixed-depth (E8.1-E8.3, E8*-k, H1);
  - a reduction of a hard estimate to a new OPEN one (E8*-red → E8**, H1 → E7.0'-TV).
- OPEN grew 18 → 21. The "first open estimate" moved E8 → E8* → E8**, each time to a restatement of
  Balaban-type large-field and UV stability.
- The genuinely valuable outputs are negative results: E8/E7.0 false in the AF window, E8*-ob sharpness. These
  constrain which statements to import; they do not replace the imports.
- No Balaban body has been read in four sessions. The 7 imports are marked [unverified-exact-statement], so the lane
  cannot even confirm that E8** is a corollary of L5/L6.
- **Recommendation.** Before any new reduction, obtain CMP 109/116/122 (and 95/96/98/99/102), via a library, a
  Springer preview or the IHES preprints, and do a line-level comparison of E8** against L5/L6. Next-session item 1(i),
  the U(1) Gaussian analogue, is worth doing. Item 5 (the E7.2 norm) should be dropped per (2).

## Required fixes

1. E8*-sup/E8*-k: domain A_L η ≤ τ_N/2 (or c → 2c) for N ≥ 13.
2. E8*-ob: "no sup-to-sup induction", not "no deterministic induction".
3. E8*-red: state the L9a bounded-measurable extension explicitly in L9a's REVERIFIED scope.
4. H1: "useful for L ≥ 5" is SU(2)-only.
5. c15/E7.2: downgrade the "decision" to a design note. Report the poor b²/j³ fit (j = 1, 3). Call the 0.5266 match
   a bookkeeping identity.
6. FILS: change [m] to [v-R4] with pages 1–34. Dimock 2009.01156: change [v-abs] to confirmed.

**Count: 30/30 PROVEN-HERE survive** (fixes 1-4 are scope or wording). The tally is otherwise accurate: 2
IMPORTED-AND-REVERIFIED, 7 IMPORTED-NOT-YET-REVERIFIED, 21 OPEN.
