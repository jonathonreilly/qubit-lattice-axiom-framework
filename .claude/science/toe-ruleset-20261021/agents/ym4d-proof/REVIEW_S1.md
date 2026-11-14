# REVIEW_S1: independent hostile review of PROOF_session1_snapshot.md

Reviewer: independent agent (did not write the proof). Inputs: the snapshot, LOG.md, checks/*.py (re-run 2026-10-26).
PROOF.md was not read or edited.

**Bottom line.** 10 of the 13 PROVEN-HERE items survive as proven. Four of those 10 need written fixes.
- L8b survives only in a narrowed form: translations and coordinate reflections, not the full hypercubic group.
- L7.0 has a real gap: tuning uniform in K.
- L7c inherits that gap.
- No PROVEN-HERE step relies on an IMPORTED-NOT-YET-REVERIFIED lemma.
- I found no fabricated citation.

## (1) PROVEN-HERE items

**L0: CORRECT.** The axial paths stay inside the block, and nested centres are fine for L odd. Cosmetic fix: (iii) should say D_N for N ≥ 6.

**L1a: CORRECT.** Z_y → g(c_Y) Z_y g(c_Y)^†, and the principal log is a spectral function, so it commutes with the conjugation. Re-derived.

**L1b: CORRECT-WITH-FIXES.**
- The bound ||Z−1|| < 2 sin(π/N) gives |θ_j| < 2π/N, so |Σθ| < 2π and Σθ = 0. Correct.
- Fix: the bound ||Z−1|| < 1 gives |θ| < π/3 ≤ 2π/N for every **N ≤ 6**, not only N ≤ 5. LOG says the argument fails for N ≥ 7, so the snapshot and LOG disagree. Align them.
- Note: D_N shrinks like 1/N, so later "uniform in N" claims must keep track of it.

**L1c: CORRECT.**
- BCH re-derived. In fact the second-order commutators cancel, so log U′ = avg log T_y + O(t³).
- The O(t²) constant depends on L through the path lengths. Fine, because uniformity is not claimed.
- See (5): c1(d) tests a different identity from the one stated.

**L3s: CORRECT as a theorem about the stated operator. It is a faithful analogue of Balaban's operator but strictly weaker.**

I re-derived every inequality:
- **(i)** The axial paths to x and x+e_μ differ by one μ-step and then run parallel, so the loop is a ladder of ≤ (d−1)r lassoed plaquettes inside B. This gives A_max ≤ (d−1)rεF ≤ (d−1)F/2. The gauge is consistent with Q: Q_Aφ = Q_0ψ with ψ_y = P(c→y)φ_y.
- **(ii)** Step 1: (x−y)² − x²/2 + y² = (x/√2 − √2y)² ≥ 0. Step 2: the Neumann λ₁ = (4/ε²)sin²(π/2n) ≥ 4. Step 3 is correct. So H_A ≥ min(2,a) − 9F².
- **(iii)** The kinetic cross term is −2cosh(t)Re z with |t| ≤ 1, and cosh s − 1 ≤ (cosh 1/2)s² gives the 1.543dμ² loss. Block part: |s_±| ≤ e^{μ/2} − 1, and the Cauchy-Schwarz steps are correct. (CT) forces η ≤ 1/2. The numerical-range bound and the conjugation identity are correct.
- **Uniformity.** The constants really are independent of ε = 1/n, T, N and the background, given F. The proof uses only unitarity, and the Poincaré constant is n-independent.

Required fixes (scope and labelling, not logic):
- (a) It is **not** Balaban's Q_k. Balaban iterates the averaging, and the transports of the iterate differ from the direct axial P(c→y). "Uniform in the number of RG steps" holds only in the sense n = L^k, for the direct average. Rename it, or close R3.1, which is an unproven obligation: "θ ≤ C_path F" is asserted, not shown.
- (b) Scalar, fundamental representation, no gauge fixing, 0-forms. The 1-form Hodge-Poincaré inequality (L3g(a)) is the real analogue and is open.
- (c) The bounds are on L² operator norms of block-localised pieces. The pointwise kernel follows as |G(x,y)| ≤ (2/m) ε⁻⁴ e^{−μρ}, which is not uniform, and the derivative/Hölder bounds that Balaban needs are absent.
- (d) The hypothesis F (max over all fine intra-block plaquettes in physical units) holds only for smooth backgrounds, i.e. Balaban's minimisers U(V). Typical Wilson configurations have F ~ g/ε² → ∞. So *applying* L3s needs L2 and L1d (both IMPORTED-NOT-YET-REVERIFIED). This is legitimate as a hypothesis, but the text should say so.
- (e) The result needs F < 1/3 (for a = 1), which is a quantitative small-field condition in physical units.

**L4c: CORRECT.**
- Induction: g_j ≤ g_0 gives β_j ∈ [β/2, 3β/2], and the comparison sums follow.
- Fix: "a convergence proof *must* produce geometric decay" is heuristic, because O(g²) errors could telescope or cancel. Soften it.
- Related: L4a writes 1/g_{k+1}² = 1/g_k² + β_k with k = "steps". If k counts coarse-graining steps, the sign is wrong (g must grow toward the IR). L4c is consistent only with resolution indexing. Fix L4a's indexing.

**L7.0 (tuning exists): GAP.**
- What is correct: for each fixed K, continuity in β, the Laplace concentration on flat configurations, and w̃ = 0 there.
  - Wording fix: the loops T_{c_X}⁻¹T_y and the coarse plaquette loops are null-homotopic (zero winding). That is what kills torus holonomy, including when M = 0. "Lies in a contractible union" fails when the coarse torus has side ≤ 2.
- **Missing step.** The IVT gives w* ∈ (0, w̃_0(K)), where w̃_0(K) is the β = 0 value. At β = 0 the links are i.i.d. Haar. ζ = 1 requires about L^{4K} of the Z_y, many with disjoint supports, to lie in a fixed ball. So w̃_0(K) → 0 super-exponentially in K.
  - Even sup_β E_{K,β}[w̃] ≥ c > 0 uniformly in K is unproven. It is essentially a large-field suppression statement (L6/E8).
  - So a fixed w* for all K, which the continuum limit, RC, L7c and LOG decision 1 all need, is **not** proven.
- Secondary fix: for N ≥ 13, the thresholds ‖Z−1‖ ≤ 1/2 or 3/4 do not imply D_N, so V⁽⁰⁾ may leave SU(N). Scale the thresholds with D_N.

**L7a: CORRECT (vacuous).** The limit depends on the arbitrary off-D extension.

**L7c: GAP (inherits L7.0) + fix.**
- w̃ is a function of the fine field, not of V⁽⁰⁾. Only E_K[w(V⁽⁰⁾_p)] ≥ w* holds (w ≥ w̃ ≥ 0), and that inequality passes to the limit because w is continuous.
- "= w*" is wrong. "≥" is right, given uniform tuning.

**L8a: CORRECT (vacuous).**

**L8b: WRONG as stated.**
- S4 fixes the path order "coordinate 1, then 2, 3, 4". An axis permutation maps complete-axial paths to paths with a different order, so V⁽ᵐ⁾[RU] ≠ R V⁽ᵐ⁾[U]. Invariance of the torus measure therefore does not transfer.
- What survives: resolution-m translations (they preserve every finer grid) and coordinate reflections through block-aligned planes (L9a′).
- Fix: either restrict the claim to that subgroup, or symmetrise the averaging over the 24 orders (averaging the logs over all orders keeps L1a/L1b).

**L8c: CORRECT-WITH-FIXES.** The argument (positive-half measurability via L0(i), covariance via L9a′, closedness under weak limits of a continuous bilinear) is right. Two fixes:
- (a) The fine torus has side L^{K+M}, which is **odd**. A reflection through a block-boundary link plane therefore fixes a *site* plane antipodally: it is a mixed reflection, not the pure link reflection that L9a re-derives. RP still holds (gauge-fix the crossing links, condition on the fixed-plane variables, and get a sum of |·|²), but L9a must be extended to state this.
- (b) The measurable extension off D must be chosen θ-covariant.

**L9a′: CORRECT.**
- Re-derived the reversal: T̃_ref = T_{c_X}⁻¹ and T_{c_X}T_y⁻¹ = T_{c_X} Z_y⁻¹ T_{c_X}⁻¹. Then log(Z⁻¹) = −log Z on D, which gives U′⁻¹.
- Order preservation under coordinate reflections is correct. Induction over the levels holds, because block-boundary planes at resolution m are boundaries at every finer level.

**Imported-lemma leakage:** none inside any PROVEN-HERE argument. L3s's *applicability* (fix d) and L7.0's *usefulness* depend on L2, L1d and L6.

## (2) IMPORTED-AND-REVERIFIED

- **L4b (b0): genuine, for the continuum coefficient.** I re-derived (1/2)[4·(1/12)(−C_A) + 2C_A] + C_A/12 = 11C_A/12 and the heat-kernel sign, giving d(1/g²)/d ln μ = 2·11N/48π². The step load-bearing for the RG, Balaban's lattice β_k → 2b0 ln L, is not reverified (correctly flagged).
- **L9a (Wilson RP): genuine.** The OS argument is correct for both link and site reflection. Gap: the odd-torus mixed reflection actually used (see L8c).

## (3) Structural finding

- **Compactness: correct.** These are weak limits of laws on products of compact groups, tested against the local continuous block observables O_m (Prokhorov on the torus; Tychonoff plus Kolmogorov in infinite volume).
- **It is not existence of the theory.** Without E8, the per-m limits need not be consistent (A_*ν_{m+1} ≠ ν_m), mass can sit on the arbitrary off-D extension, and non-triviality fails with the L7.0 gap.
- **"IR strong coupling is not an obstruction to existence" is overstated.** OS existence needs OS1 on R⁴, and route γ1 needs uniqueness, i.e. IR control. It is true only for limit points of block laws.
- **"Euclidean invariance is the hard core"** is reasonable, and R9.1 is correctly scoped.
- **Balaban's restriction (small coupling at the stopping scale, not small volume)** is plausible and partly confirmed. Dimock II, for the scalar model, gives bounds "uniform in the ultraviolet cutoff N and with bulk dependence on the volume parameter M". It is unconfirmed for the gauge papers, so keep the "pending" tag.

## (4) Citations

- **Confirmed by me (web):**
  - Balaban CMP 95:17–40, 96:223–250, 109:249–301, 116:1–22;
  - Balaban CMP 99:75–102 and 102:277–309: **upgrade from [m]**;
  - Osterwalder-Seiler, Ann. Phys. 110 (1978) 440, via a citing paper: **upgrade**;
  - Abbott NPB 185 (1981) 189–203; Vassilevich Phys. Rept. 388:279–360;
  - Dimock 1108.1335, 1212.5562 and 1304.0705 (the quotes are accurate);
  - Cao-Chatterjee 2111.12813 ("to appear in CMP"; I did not confirm "2024");
  - arXiv:2606.19362, which exists as described and is correctly not imported.
- **Not checked by me, but consistent with my knowledge:** Balaban CMP 98:17–51, 99:389–434, 119:243–285, 122:175–202 and 355–392; MRS CMP 155:325–383; Lüscher JHEP 08 (2010) 071 (add the exact reference).
- **Suspicious or fabricated:** none found. No Balaban paper body has been read, so every exact-statement paraphrase remains unverified.

## (5) Checks (re-run: laptop, BLAS = 1, nice 10, load about 2, 37% free RAM)

- **c1: 12/12, 3 s.** (a), (b), (c) and (f) test the exact identities of L1a, L1b and L9a′ on one link (L = 3).
  - (d) compares log U′ with avg log T_y, not with the stated line integrals. Those differ at O(t²), which is why the ratio is about 4.
  - So the LOG's "second order, better than the claim" is a misreading, though the lemma still holds.
  - (e) is a diagnostic.
- **c2: 4/4, 30 s.** Exact algebra downstream of the imported a2 formula, plus lattice diagnostics. It does not test Balaban's β_k.
- **c3: 5/5, 5 s.** Consistency instances for SU(2), n ≤ 3. The n = 1 case is trivial and the large-field cases are vacuous. Uniformity in n rests on the proof alone, which holds up.
- **c4: 4/4, < 1 s.** It tests the positivity mechanism (Z2 in 2D, crossing-kernel PSD), not 4D SU(N) Wilson RP and not the odd-torus reflection.

All outputs reproduce the stored c*_out.txt values.
