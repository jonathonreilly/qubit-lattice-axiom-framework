# C5 R19-11 report: one law for every SM mass — does the SM cone root have a massless limit valid for all species at once?

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. 2026-10-13, 04:47Z to about 05:30Z. No repository file was edited. No downloads, no web lookups.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `S/` = `.../scratchpad/C5/R19-11/`. My scripts and `.out` files are in `S/run/`. `S/arch9`, `S/arch18`, `S/arch18_13`, `S/arch16_10`, `S/arch13`, `S/arch17_4`, `S/arch17_12` hold unmodified copies of `P/scripts/C5/{R18-9, R18-5, R18-13, R16-10, R17-13, R17-4, R17-12}/`, including the root `.npy` files.
- Every run used `OMP_NUM_THREADS=2` and ran under 10 minutes (longest about 380 s, `mscan_d_root0_GL6_16.out`, two masses). Machine load was 3–10 from other jobs; I ran at most three of my jobs at once. I stopped one of my own runs (`refine0.py` at GL(8,20)) before it started computing, because its 3D arrays would have needed several GB on a shared 16 GB machine; the refinement was done at GL(5,12) instead.

**Read.**
- `AX`, in full.
- `P/TESTS.md`: the C5 method and readings (`:2302-2319`); the R16-2 entry, worker line and verdict (`:5065-5085`, `:5210-5221`, `:5422-5426`); R16-3 (`:5087-5106`, `:5359-5368`, `:5427-5431`); R16-10 (`:5449-5476`, `:5563-5572`, `:5890-5893`); R17-13 (`:6365-6383`, `:6654-6662`, `:6802-6805`); R18-9 (`:6847-6869`, verdict `:7284-7299`); R18-13 (`:7061-7091`, verdict `:7505-7516`); the rules at the heads of rounds 17–19 (`:5688-5706`, `:6395-6406`, `:7117-7131`); my item `:7628-7651`; C4 lane RP (`:1822-1849`, result `:1902-1913`).
- `P/agents/`: `C5_R18-9_report.md` and `C5_R18-9_referee_verdict.md` (`vR18-9`); `C5_R18-13_report.md` and `C5_R18-13_referee_verdict.md` (`vR18-13`); `C5_R16-10_report.md` and `C5_R16-10_referee_verdict.md` (`vR16-10`); grep hits in `C5_R17-13_report.md` (`:230`, m-transfer), `C5_R16-13_referee_verdict.md` (`:23`), `C5_R14-3_referee_verdict.md` (`:18`), `C5_R16-3_report.md` (`:276`), `C5_R9-9_report.md` (`:120`, `:185-186`), `C5_R8-5_report.md` (`:261`), `C5_R7-4_report.md` (`:46`); `PRICE_NOTE.md` (`:22`, `:162`).
- Overlap: R19-12 (pre-registered 04:54Z, running) recomputes the charge block on the R18-9/R18-13 root edges (`TESTS:7673-7703`). Nothing here drafts it. Note for it: the m → 0⁺ root found here has different Dirac and scalar edges (§3.2).

**Runners rechecked before use (checked).**
- `lib9.phot_quad` (R18-9, unmodified) at the root photon edge, N = 224, returns R18-9's printed coefficients to every printed digit: T (2.002586e-1, 1.157162, −3.85e-7), E (1.966943e-1, 1.117700, −3.59e-7), μ_E 2.850892e-2 (`run/phq_N224.out` vs `arch9/solve4k_N224.out:1`).
- R18-13's `dface.xi_dirac` at vR18-9's retuned root, m = 0.01, GL(4,10), reproduces `arch18_13/dface_refroot_m0.01.out` to all printed digits (T₂g 1.98456394e-3, E_g 1.32143598e-4, face1 1.12353749e-3, face2 2.12323533e-3; `run/test_d.out`).
- R17-4's off-axis scalar evaluator at the same root reproduces `arch18_13/scal_offaxis_refroot.out` (E_g −3.621562e-4, T₂g −6.277494e-4, face1 −4.576449e-4, d1 −2.909043e-5; `run/mscan_s.out`, m = 0.01 line).
- R18-13's `vwface.xi_geo` own-direction derivatives at the new stencil value equal R18-13's N = 224 Jacobian to 1e-9 (0.139704009, 0.289279709, 0.578571421; `run/photface0_N224.out` vs `arch18_13/photface_N224.out:1`).
- The GL(4,10) and GL(6,16) Dirac rows at m = 0.04 agree to 7e-11 per field (`run/mscan_d_GL4_10.out:2`, `run/mscan_d_GL6_16.out:2`).

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator. Numbers from memory are labelled RECALLED.

---

## 0. In plain words

1. **Every row has a finite massless limit, and none has a log at the order that matters (proved for the axial and shear rows; checked for all six).**
   - Scalars (Higgs edge) and the vector μ_E row: analytic in m². The archived Schwinger forms decay like e^{−t b²} because the edges are exact continuum inside their boxes (Lemma B).
   - Wilson-Dirac rows: analytic in m, **not in m²**. The Wilson mass M = m + ΣW breaks m → −m, so every Dirac row has a linear term (Lemma A). This is the linear drift already seen for single rows (`vR16-13:23`; `C5_R17-13_report.md:230`), now measured for all six rows at the SM root.
   - No m ln m term in any row (fits bound it at ≤ 3e-7 against linear terms of 1e-3). An apparent m² ln m term in the Dirac face rows traces to the off-axis evaluator's quadrature near k = 0 (§3.1). It would be harmless anyway (about 1e-33 at SM masses).
2. **The m → 0⁺ root exists (checked).** With R18-9's photon edge and stencil family, and every mass at 0⁺:
   - (b_s, b_f, r, a) = (2.590035, 0.915439, 0.568281, −0.176177) (§3.2);
   - transversal (σ_min 6.6e-4); r < 1/√3 with margin 0.0091, so it is still subluminal; the photon edge is unchanged inside R18-9's window;
   - the two off-axis rows are paid by R18-13's own-direction data at (w_d, w_o) = (−1.17171, −0.19557). A direct N = 224 re-evaluation leaves face totals −1.7e-6 and −4.1e-7, the same grid artefact R18-13 had.
   - Relative to the m = 0.01 root, the knobs move by (+0.064, +0.0063, +0.0127, −8e-5). That is not small: the Dirac mass enters linearly.
3. **The massless-limit law does not meet ONE-LAW's comparators at the SM masses (checked numbers, reading conversions).** All of the residual comes from the Dirac sea's linear terms, 96% from the top quark (Σ n_i m_i a = 4.40e-17 for the 22.5 Dirac fields; top alone 4.24e-17).
   - **Speed rows** (E_g, T₂g, face1, face2): Δc_g = 8πΞ ≈ 1.9e-19 to 2.4e-18. That is 290× or more below the GW170817 band. But T₂g, face1 and face2 are 6–9× **above** the R16-2 photon comparator 2.66e-19. E_g is just below it (0.7×).
   - **Shear rows** (μ_E, μ_T2): residuals +4.7e-19 and +1.2e-19 per cell. Read as a graviton mass (R9-9's normalization, with PRICE_NOTE's caveat), that is m_g ≈ 5e-9 M_P ≈ 6e10 GeV. GW170817 needs |μ| ≲ 3e-98. The residual is about 1e79 too large.
   - The pre-registered expectation fails twice: the Dirac corrections are O(m a) ≈ 1e-17, not (m a)² ≈ 1e-34; and the shear rows' comparator is about 1e-98, not 1e-15.
4. **But one law does serve every SM mass at once (proved, given the checked root and Jacobian).** The rows are sums over species. Near the 0⁺ root they are smooth in the knobs and analytic in every mass (one massive-vector piece is assumed C¹), and the Jacobian is invertible. So the implicit-function theorem gives a law, within about 1e-17 of the 0⁺ root in every knob, whose six totals vanish exactly at the actual SM spectrum. A scaled SM-like spectrum (top at m a = 2e-3) shows this numerically: the root exists, and its knob shift matches the linear IFT prediction to 0.2%. No extra knob is needed; the count stays 6 equality tunings plus the photon window.
   - The catch is what that law must know. Its knobs encode the SM masses (Σ n_i m_i, Σ n_i m_i², …) to the shear rows' precision. Any change of the spectrum detunes the shear rows at O(c₁ Σ n_i Δm_i a). Switching the whole spectrum on or off is ≈ 5e-19. The electroweak transition, which switches all these masses on, is such a change (suggested; the history is not computed).
   - A law that is blind to the masses instead needs extra conditions: the Dirac edge's shear coefficients of m¹ through m⁵ (10), the scalar and vector μ_E coefficients of m² and m⁴ (4), and, for the R16-2 comparator, the linear terms of three speed rows (3). That makes about 14–17 more (suggested count). This is C4 lane RP's mass-relation problem (`TESTS:1902-1913`) on the SM root's edges.
5. **What works, partly: a twisted-mass Dirac edge (checked; a priced law datum).**
   - Put the Dirac mass orthogonal to the Wilson term (i m βγ₅). Every Dirac row is then even in m (proved by inspection), and the 0⁺ root is unchanged.
   - The speed residuals fall to Δc ≈ 1e-35 (axial) and ≲ 1e-34 (face), below both comparators.
   - The shear residuals fall from about 1e-19 to about 4e-36. That is still about 1e62 above the GW comparator.
   - So the speed half of ONE-LAW can be had at the price of a twisted mass. The shear half is not reached in these families. Even with the twisted mass, a mass-blind law needs about 8 extra conditions (the m² and m⁴ coefficients of the Dirac, scalar and vector shear rows; suggested count). Otherwise the law must be tuned against the spectrum (item 4).
6. **Against the FIXED readings: OPEN.**
   - ONE-LAW fails on its comparator clause (shear rows by about 79 decades; three speed rows by 6–9× against R16-2's comparator).
   - MASS-OBSTRUCTED fails on both of its clauses: nothing diverges or is non-analytic in the mass (proved for the axial and shear rows, checked for the face rows), and a single law does serve all SM masses (item 4).
   - The obstruction that exists is one of size and mass-dependence, not of analyticity.

---

## 1. Class, hypotheses, stipulations, exclusions (stated before any title)

**Setting (`TESTS:7636-7640`).**
- **Content and vertices:** R18-9/R18-13's.
  - 4 real scalars, U vertex, on one Higgs edge G_w(b_s, fr = 1).
  - 22.5 Dirac fields, UD vertex (midpoint prescription), on one D1(b_f, r) edge.
  - 12 vectors, VWa stencil a, on the photon edge γG_w(2.9435, 0.198093). This is fixed inside R18-9's window; the window selection is unchanged.
  - Off-axis: VWa-geo with own-direction data (w_d, w_o) (R18-13); the UD midpoint extension (R18-13 `dface`); the scalar E1 extension (R17-4).
- **Rows:** Ξ_T2g, Ξ_Eg, μ_E, μ_T2, face1, face2 (totals). Body follows (Lemma C of R18-13, `vR18-13:3`).
- **Masses.**
  - A common m → 0⁺ (Dirac m = 0 exactly; scalars m = 1e-5, which is 0⁺ to 1e-14 by Lemma B; vector μ_E at 1e-5 instead of the archived 1e-3 regulator).
  - Then the SM spectrum as perturbations, a = ℓ_P (`AX:189-190` scale reference; the reading m a = m/M_P with M_P = 1.22089e19 GeV, RECALLED).
  - SM masses (GeV, RECALLED): t 172.69, b 4.18, c 1.27, s 0.0934, d 0.00467, u 0.00216 (each ×3 colours); τ 1.77686, μ 0.10566, e 0.000511; ν ≈ 0 (3 × ½ Dirac); H 125.25, W 80.377, Z 91.1876.
- **Mass bookkeeping in the 4 + 22.5 + 12 count.** The count is the unbroken-phase one. For the residuals I use the broken phase:
  - W±, Z as 2 transverse polarizations on the vector edge;
  - their longitudinal modes as Goldstones on the scalar edge, with masses m_W, m_W, m_Z in Feynman–'t Hooft gauge (massless in Landau gauge; both shown);
  - the Higgs at m_H.
  - This is a stated choice (suggested); it moves only O((m a)²) terms that are 18 decades below every number that decides the reading.
- **Physics, as R18-9/R18-13:** one loop, supplied zero-point vacuum and filled sea, ultralocal seagull, SF strain flow for the shear rows (P-R16-13a). "Conserved" is the O(q) forward convention (`vR18-9:21`; `vR18-13:11`).
- **Excluded:** pairing; superluminal edges; M; V0 (as a vertex choice); two loops; interactions; thermal masses; running.
- **Hypotheses carried, not derived:** everything R18-9 and R18-13 stipulate (SF, the 𝔇 restriction for UD, the midpoint prescription, signed stencils, VWa-geo, own-direction data, the photon window). No exact W1.
- **Not computed:** the Ξ and face rows of a massive vector (the archived vector evaluator is massless). See §3.3 for why this cannot change the reading.

**Round 17–19 head rules.**
- **v_max:** D1 r ≤ 1/√3 gives v_max ≤ 1 (Lemma V1, `vR18-9:15`). G_w scalar and γG_w photon have d′ ∈ [0, 1]. Edges are R18-9's families with new parameters; the photon edge is unchanged.
- **Counterterm basis:** per law datum (`vR18-9:17`).
- **Locality:** unchanged from R18-9/R18-13.
- **Literal first:** readings are reported on the registered text (§4).
- **Signs of law data:** signed stencils and own-direction weights, as registered before (`vR18-5:16`).
- **Thresholds recomputed:** the comparator thresholds below are recomputed in the script (`run/fitres.py`), not quoted.
- **Exhaustive forks:** §4 lists the NEITHER outcome explicitly.

## 2. Prior art (each counted once)

- **R18-9 + vR18-9.** The axial four-row root at m = 0.01 and a separately retuned m = 0.001 root; "one law valid at both masses" not established (`vR18-9:23`). I start from vR18-9's retuned root.
- **R18-13 + vR18-13.** Two off-axis rows; Lemma O (linear, triangular, det E0T0/16 > 0); Lemma S; 7 continuous knobs; "one law at both masses" not established (`vR18-13:13`).
- **R16-10 + vR16-10.** Theorem L: finite (m, λ) → 0 limit of the matter speed, no divergent IR log, with m² log m not excluded (`vR16-10:3`). Its linear-in-m drift at the Dirac zero, "from the Wilson term" (`C5_R16-10_report.md:161`). Its top-quark matter-speed residual ≈ 1.3e-21 (`:203`).
- **R16-13 verdict.** "Fixed-law mass drift is linear—not O(m²)—because M = m + ΣW" (`C5_R16-13_referee_verdict.md:23`).
- **R17-13.** m-transfer for μ_T2: real-analytic in m through 0, residual ≈ 2.6e-3·m per field (`C5_R17-13_report.md:230`). Reproduced here: 2.74e-3 at the 0⁺ root (§3.1).
- **R14-3 verdict.** μ_E analytic in m² under a single-zero gapped hypothesis; a common massless tuning leaves O((m a)²) per-species residuals and exact roots stay weakly mass-dependent (`C5_R14-3_referee_verdict.md:18`). Lemma B is that statement for the root's edges and rows.
- **R16-3.** Ξ analytic in m², and the conversion c_T² − 1 = 16πΞ at a = ℓ_P with the GW170817 band (`C5_R16-3_report.md:276`, from `C5_R9-9_report.md:120,185-186`).
- **R16-2 + verdict.** Per-species residuals; the comparator ε* = 2.66e-19 (`C5_R8-5_report.md:261`).
- **C4 lane RP (refereed FAIL, bounded).** For free lattice species the shear response is F(M) = c₀ + c₂M² + c₄M⁴ + M⁶[(384π²)⁻¹ln M + c₆]. Cancelling to the P0 level at physical masses needs R0 plus the mass relations R2, R4 and R6 (`TESTS:1902-1913`). The extra-condition count in §3.4 is this structure on the SM root, with the Wilson-Dirac odd orders added.
- **PRICE_NOTE.** P0's shear target, 5.7e-99 of natural size (`PRICE_NOTE.md:162`). A shear response is a graviton mass only for a supplied dynamical metric with stationary background and kinetic normalization (`:22`).
- **Grep** (`P/agents/*.md`, `TESTS.md`, `SUMMARY.md`) for "m → 0⁺ root", "one law", "SM spectrum", "Σ n m", "electroweak" with "shear". Besides the items above there is no SM-spectrum residual of the gravity-block rows and no massless-limit root.

---

## 3. Results

### 3.1 (a) Massless limits and leading corrections

**Lemma A (Wilson-Dirac rows: finite at m = 0, real-analytic in m, odd terms allowed). Proved for the axial and shear rows under the archived representations.**
- **Inputs.**
  - D1(b, r) with b < π/2. S = SymS(b) has S = k, S′ = 1, S″ = 0 on |k| ≤ b (`arch18/sublum.py:49-58`).
  - W′ = 2r√(st(1 − st)) with st = sstep((|k| − b)/w) = 0 on |k| ≤ b (`arch18/dirac.py:36-37`). So W = W′ = W″ = 0 in the box, and W ≥ 0.
- **Support.** In `dfam.evaluate` (`arch18/dfam.py:57-85`), each integrand carries a factor that vanishes in the box coordinate:
  - the a-term carries cp2 − 1 at k_z, and the s-term carries A_zz at k_z;
  - μ_E carries H_xx − H_yy (H_jj = 1 in the box), and μ_T2 carries H_xy = W′_xW′_y.
  - UD − V0 vanishes where |k_x|, |k_y| < b (`arch18/xiud.py:12`). Directly: with W′ = 0 and S′ = 1, p_i = S_i, so GU = G0.
  - So every integrand is supported on sets where some coordinate has |k_j| ≥ b.
- **The bound.** There, at real m ≥ 0, E² = ΣS_l² + (m + ΣW_l)² ≥ S(k_j)² + W(k_j)² ≥ c_b², with c_b = min(b, W_π) > 0. The reasons:
  - S is concave on [b, π − b] (S″ = −2 sstep′/w ≤ 0), so S ≥ b there;
  - on [π − b, π], W = W_π > 0.
- **Conclusion.** For |m| < ρ, with ρ small enough that |2mΣW + m²| < c_b²/2 (ΣW ≤ 3W_π), Re E² ≥ c_b²/2. So E = √E² is holomorphic, and the integrands are holomorphic and uniformly bounded. Each row is real-analytic in m on (−ρ, ρ), m = 0 included.
- **Nothing forces odd coefficients to vanish.** m → −m is not a symmetry, since M = m + W with W ≥ 0. ∎
- **Off-axis Dirac rows** (`dface`, pointwise over all terms) are not covered by this support argument. They are checked below.

**Lemma B (scalar U rows and the vector μ_E: analytic in m²). Proved under R14-3's Schwinger representation.**
- **The forms.** Ξ_v = (32Γ(5/2))⁻¹∫dt t^{3/2}e^{−tm²}W_v(t)J(t), with J = 2tF₂ − E₀. And μ_E = (12Γ(3/2))⁻¹∫dt t^{1/2}e^{−tm²}E₀(3F₂² − F₄E₀) (`arch18/zz.py:58-92`).
- **The family.** G_w has h = k in the box, h′ ∈ [0, 1] and g = h² ≥ b² outside the box.
- **J decays.** Its box part is exactly −(b/π)e^{−tb²}, since ∫_{−b}^{b}(2tk² − 1)e^{−tk²}dk = −2be^{−tb²}. Its outside part is ≤ (1 + 2t·max f²)e^{−tb²}.
- **3F₂² − F₄E₀ decays.** Write E₀, F₂, F₄ as the full Gaussian moments G₀, G₀/2t, 3G₀/4t² plus remainders bounded by poly(t)e^{−tb²}. The Gaussian parts cancel identically.
- **Conclusion.** W_v is polynomially bounded. So both t-integrals converge absolutely and uniformly for Re m² > −b² + ε, and both rows are holomorphic in m². There are no odd powers and no logs. ∎
- **Scope.** This also covers the photon edge's μ_E (2 × the scalar formula on γG_w, b_γ = 2.9435). It does not cover the off-axis scalar evaluator, which is checked.

**Checked coefficients at the m → 0⁺ root law.** The law is the GL(4,10) root `root0_m0.npy`; the final root differs by 5e-5 in b_s and ≤ 8e-7 elsewhere, which moves these coefficients by ≲ 1e-4 relative. Sources (`run/mscan_d_root0_dense_GL4_10.out` 14 masses in [0, 2.5e-3]; `run/mscan_s_root0.out` 10 masses in [1e-5, 0.04]; `run/vmu.out`). Fits: `run/fitres_root0_dense.out`, `run/mlogm_dense.out`. Per field:

| row | Dirac c₀ (m = 0) | Dirac c₁ (m¹) | Dirac c₂ | scalar c₀ | scalar c₂ (m²) | vector c₀ | vector c₂ |
|---|---|---|---|---|---|---|---|
| Ξ_T2g | +2.036920e-3 | −1.44595e-3 | −6.6e-4 | −6.36802e-4 | +1.05e-4 | (a-dep.) | not computed |
| Ξ_Eg | +1.821548e-4 | −1.67037e-4 | +7.2e-6 | −3.67723e-4 | +6.7e-5 | (a-dep.) | not computed |
| μ_E | −1.718337e-2 | +1.06932e-2 | +6.6e-3 | +1.112970e-2 | −1.361e-3 | +2.850892e-2 | −2.993e-3 |
| μ_T2 | 0 (root) | +2.73929e-3 | +2.19e-3 | 0 (S1) | 0 | 0 (S1) | 0 |
| face1 | +1.190214e-3 | −1.6914e-3 | −4e-3 | −4.64672e-4 | +8.1e-5 | +2.18190e-1 at w = 0 | not computed |
| face2 | +2.195877e-3 | −2.1447e-3 | +7e-3 | −6.36802e-4 | +1.02e-4 | +1.09244e-1 at w = 0 | not computed |

- **Dirac, axial and shear rows.**
  - Linear term: present in every row (checked).
  - m ln m: |e| ≤ 1.2e-11. m² ln m: |d| ≤ 1.5e-8. Both consistent with zero, as Lemma A requires.
  - Fit residuals 4e-17 to 5e-15.
- **Dirac face rows.**
  - c₁ is stable across fits to 2e-3 relative.
  - An m ln m term is bounded by |e| ≤ 3e-7 (fit noise 1e-11).
  - An m² ln m term with d ≈ −3e-4 (face1) and +6e-4 (face2) lowers the fit residual from 1.1e-11 to 4e-12. I attribute it to quadrature (checked indication, not proof). The `dface` evaluator integrates every term pointwise, including the continuum box where the integrand only cancels after integration. Its axial T₂g differs from the support-free dfam+UD value by 2.9e-8 at GL(4,10) and 3e-9 at GL(6,16), and with the twisted mass (below) its m-dependence shows the same non-constant (row − row₀)/m² while the support-free axial rows are clean m². The term is not established either way. Its size at SM masses is ≲ 1e-33. The linear coefficients are unaffected: dface's axial T₂g slope equals dfam's to 3.5e-4 relative.
- **Scalars.** c₁ ≤ 3e-8 (noise level 3e-11 in the row values); m ln m |e| ≤ 5e-8. Clean m² behaviour, e.g. μ_E steps ratio 4.00 per halving.
- **Quadrature check of the Dirac slopes.** GL(6,16) at m = 0 and 1e-4: §3.2 note.
- **Vectors.** Massless in the archived Ξ/face evaluator, so m-independent. The vector μ_E is clean m² (c₂ = −2.993e-3 per vector). The archived 1e-3 regulator shifts it by −3.0e-9 per vector.

**Answer to (a).** Every row has a finite m → 0⁺ limit (checked; proved for the axial and shear rows). Scalar and vector-μ rows are analytic in m². Dirac rows are analytic in m with nonzero linear terms of 1.7e-4 to 1.1e-2 per field. There is no m log m. A Theorem-L-type IR log does not arise, because every axial and shear Dirac integrand vanishes identically in the continuum box (Lemma A). That is stronger than Theorem L's exclusion of divergent logs for the matter speed (`vR16-10:3`).

### 3.2 (b) The root at m = 0⁺ (checked)

**Axial solve.** Knobs (b_s, b_f, r, a), as R18-9. Photon coefficients recomputed at N = 224 (`run/phq_N224.npy`). Newton at Dirac GL(4,10) (`run/root0_m0.out`), then refinement at GL(5,12) with a frozen GL(4,10) Jacobian (`run/refine0.out`), then the vector-μ regulator removed (`run/final0.out`):

| stage | (b_s, b_f, r, a) | max \|rows\| | det J; σ_min |
|---|---|---|---|
| start: vR18-9's m = 0.01 root | (2.526104, 0.909104, 0.555604, −0.176095) | at m = 0⁺: 2.4e-3 (μ_E), 5.7e-4 (μ_T2) | |
| m = 0⁺, GL(4,10) | (2.5900891, 0.9154380, 0.5682803, −0.1761772) | 6e-11 (GL(4,10)); 1.9e-6 at GL(5,12) | −3.538e-4; 6.6e-4 |
| m = 0⁺, GL(5,12) refined | (2.5900361, 0.9154387, 0.5682809, −0.1761772) | 3e-11 at GL(5,12) | |
| **m = 0⁺, vector μ at 0⁺ (final)** | **(2.590034773, 0.915438682, 0.568280847, −0.176177232)** | 1.0e-10 at GL(5,12) (1.9e-6 at GL(4,10): quadrature) | −3.5382e-4; 6.596e-4 |

- **Removing the archived photon regulator.** Moving the vector μ_E from the 1e-3 regulator to 0⁺ shifts the μ_E total by +3.6e-8. That moves b_s by −1.4e-6 and the rest by ≤ 2e-8 (`run/final0.out`).

- **Subluminal.** r = 0.56828 < 1/√3 = 0.57735, margin 0.0091 (it was 0.0218 at m = 0.01), so v_max ≤ 1 by Lemma V1. Scalar and photon d′ ∈ [0, 1]. The photon edge is R18-9's point 2.9435, so the 0⁺ root sits inside R18-9's window at that point (the window's ends at 0⁺ are not recomputed).
- **The knobs' uncertainty is in b_s.** As in R18-9, b_s is the weakly controlled direction (σ_min 6.6e-4). The quadrature change GL(4,10) → (5,12) moves b_s by 5e-5 and the rest by ≤ 8e-7.
- **Off-axis rows at the 0⁺ root** (`run/fsolve0.out`, `run/photdirect0.out`). Per field:
  - scalar (m = 1e-5): face1 −4.64672e-4, face2 −6.36802e-4;
  - Dirac (m = 0, GL(4,10)): face1 +1.190214e-3, face2 +2.195877e-3;
  - vector (VWa-geo at a = −0.1761772, N = 224, w = 0): face1 +0.21819, face2 +0.10924.
  - Totals at w = 0: face1 +2.6432, face2 +1.3578.
  - Lemma O's triangular Jacobian (det 11.639, equal to R18-13's) gives **(w_d, w_o) = (−1.171715, −0.195566)**, against (−1.171554, −0.195418) at m = 0.01.
  - Direct N = 224 re-evaluation at these data: face totals −1.7e-6 and −4.1e-7. That is R18-13's w-quadratic grid artefact (−1.7e-6, −4.0e-7 there).
- **Existence of the six-row root at 0⁺** follows from the axial root plus Lemma O. The face block is linear in (w_d, w_o) with positive determinant, and (w_d, w_o) do not enter the axial rows (`vR18-13:7`). So the off-axis part costs nothing new at 0⁺.
- **GL(6,16) check of the Dirac rows at the 0⁺ law** (`run/slope616.out`). The linear coefficients over [0, 1e-4] at GL(6,16) equal the GL(4,10) ones to ≤ 4.3e-5 relative (T₂g −1.44601e-3, E_g −1.67029e-4, μ_E +1.06936e-2, μ_T2 +2.73951e-3, face1 −1.69199e-3, face2 −2.14374e-3). The m = 0 values move by ≤ 5e-8 per field, which is the quadrature effect the refinement absorbs.

**Answer to (b).** A transversal, subluminal m → 0⁺ root of all six rows exists in R18-9/R18-13's families, with the same 6 equality tunings plus the photon window (checked). It is not R18-9's root: r moves by +0.0127 and b_s by +0.064, because the Dirac rows are linear in m.

### 3.3 (c) Residual rows at the SM masses, a = ℓ_P

**Residual of the 0⁺ law at the SM spectrum.**
- R_row = Σ_species n_s[row_s(m_s a) − row_s(0)] = c₁^D·Σn_im_ia + c₂^D·Σn_i(m_ia)² + c₂^S·Σ(m a)²_scalar + c₂^V·Σ(m a)²_vector + …, with the coefficients of §3.1.
- Σ_Dirac n_im_ia = 4.395e-17, of which the top is 4.24e-17. Σ_Dirac n_i(m_ia)² = 6.0e-34. Scalar edge Σ(m a)² = 2.48e-34 (Feynman) or 1.05e-34 (Landau). Vectors 1.42e-34 (`run/fitres_root0_dense.out`).
- The series converges: the masses are 15 decades inside the analyticity radius (Lemmas A, B).
- **Conversions (reading).**
  - Speed rows: c_T² − 1 = (2/M²)Ξ = 16πΞ at a = ℓ_P, so Δc = 8πΞ (`C5_R9-9_report.md:120,185-186`; used at `C5_R16-3_report.md:276`).
  - Shear rows: the same prefactor on the q = 0 term, m_g²a² = 16πμ (R9-9's "TT mass² = 2Π(0,0)/M²", with μ in Π(0,0)'s place). This is a graviton mass only for a supplied dynamical metric with stationary background and kinetic normalization (`PRICE_NOTE.md:22`).
  - Normalization caveat: the Dirac evaluator's e:e convention differs from the scalar's; R18-9's totals use one common convention (`C5_R18-13_report.md:90-93`). An O(1) factor in the conversion moves nothing below by more than its own size.
- **Comparators (recomputed in `run/fitres.py`).**
  - GW170817: −3e-15 ≤ Δc/c ≤ 7e-16 (RECALLED; `C5_R7-4_report.md:46`), i.e. |Ξ| ≤ 2.8e-17.
  - The R16-2 photon comparator 2.66e-19 (`C5_R8-5_report.md:261`), i.e. |Ξ| ≤ 1.06e-20.
  - For shear rows at f = 100 Hz (ω a = 2π·100 Hz·5.391e-44 s = 3.39e-41; RECALLED t_P): Δc = 8πμ/(ωa)², so |μ| ≤ 3.2e-98.

| row | residual (totals; Dirac part) | as Δc or m_g | vs GW170817 | vs R16-2's 2.66e-19 |
|---|---|---|---|---|
| Ξ_T2g | −6.36e-20 | Δc = 1.60e-18 | 440× below | **6.0× above** |
| Ξ_Eg | −7.34e-21 | 1.85e-19 | 3800× below | 0.70× (below) |
| face1 | −7.43e-20 | 1.87e-18 | 370× below | **7.0× above** |
| face2 | −9.43e-20 | 2.37e-18 | 300× below | **8.9× above** |
| μ_E | +4.70e-19 (scalar −3.4e-37, vector −4.3e-37) | m_g a = 4.9e-9 (m_g ≈ 5.9e10 GeV); Δc(100 Hz) ≈ 1e64 | **1.5e79× above** (needs ≤ 3.2e-98) | — |
| μ_T2 | +1.20e-19 | m_g a = 2.5e-9; Δc(100 Hz) ≈ 3e63 | **3.8e78× above** | — |

- **Heaviest species alone (top, m a = 1.4145e-17, ×3 colours):** Ξ_T2g −6.14e-20 (Δc 1.5e-18); μ_E +4.54e-19; μ_T2 +1.16e-19.
- **Massive-vector Ξ and face rows were not computed.** They cannot change the table's verdicts:
  - the failures are carried by the Dirac terms, which are computed;
  - an O((m_V a)²) term (suggested; Lemma B's argument applies to the vector μ row, and the stencils act at O(q²) in the IR, so an m⁴ ln m term is possible) is ≲ 1e-34 × O(1), about 14 decades below the smallest speed comparator (Δc ≤ 2.66e-19).
- **The physical-spectrum law (proved, given the checked inputs).** Let R(x; m⃗) be the six totals as functions of the six knobs x = (b_s, b_f, r, a, w_d, w_o) and the species masses m⃗, with the photon edge fixed.
  - At (x₀, 0⃗), R = 0 (checked).
  - ∂_xR is block-triangular and invertible: the axial 4×4 block has σ_min 6.6e-4 (checked); the face 2×2 block has det 11.64 (Lemma O); (w_d, w_o) do not enter the axial rows.
  - R is C^∞ in x (x enters through C^∞ sstep shapes and affine stencils) and analytic in the Dirac and scalar masses (Lemmas A, B), and in the vector masses for μ_E. For the massive-vector Ξ and face rows only C¹ is needed; that is assumed (suggested).
  - The implicit-function theorem gives a unique C^∞ x(m⃗) with R(x(m⃗); m⃗) = 0, and x(m⃗_SM) − x₀ = −(∂_xR)⁻¹R(x₀; m⃗_SM) + O(m²), of size ≲ 7e-16 per knob (|R| ≤ 4.7e-19, ‖J⁻¹‖ ≤ 1/σ_min); the checked linear scaling below gives about 1e-17.
  - So **one set of knobs zeroes all six rows at the true SM spectrum** at one loop. In double precision it is indistinguishable from the 0⁺ root.
  - **Checked on a scaled spectrum** (`run/spectrum.py` → `run/spectrum_2e-3.out`). SM-like counts and mass ratios (Dirac t, b, c, τ with the lighter Dirac fields at 0; H, W, W, Z on the scalar edge; W, W, Z in the vector μ_E), scaled so that the top has m a = 2e-3:
    - the 0⁺ law's residual there equals c₁·Σn_im_ia to ≤ 0.4% (e.g. μ_E +6.647e-5 vs +6.640e-5);
    - Newton with the frozen 0⁺ Jacobian converges to 2e-9 at the spectrum root (2.588309, 0.915264, 0.567928, −0.176175), which is subluminal;
    - the knob shift (−1.7258e-3, −1.7430e-4, −3.5256e-4, +2.282e-6) matches the linear prediction −J⁻¹R (−1.7290e-3, −1.7437e-4, −3.5273e-4, +2.283e-6) to 0.2%.
  - Scaling that shift linearly to the physical Σn_im_ia = 4.40e-17 gives Δb_s ≈ −1.2e-17 and Δr ≈ −2.5e-18.
  - The precision this law must hold is set by the shear rows: the shear totals must vanish to about 3e-98, so the knobs must be fixed to about 1e-98–1e-99 (the largest singular value of J is 19.3). That is P0's level (`PRICE_NOTE.md:162`), not a new order of fine-tuning. But the knobs now carry the SM masses' sums.

**Answer to (c).** The massless-limit law leaves speed residuals Δc ≈ 2e-19 to 2e-18 (inside GW170817, outside R16-2's comparator for three rows). It leaves shear residuals of about 1e-19 per cell, which the GW comparator excludes by about 79 decades. The law that serves the SM masses is the spectrum-tuned one (IFT), not the m → 0⁺ one.

### 3.4 (d) Prices and the bill (named, not adopted)

- **Used, not new:** everything in R18-9/R18-13's bill (P-R17-12b signed stencil, P-R18-5b/c, SF, P-R17-13a, P-R18-9a photon window, P-R18-13a/b own-direction data and VWa-geo).
- **P-R19-11a (new, reading): a spectrum-tuned gravity block.**
  - The six gravity-block knobs are fixed at the physical mass spectrum (the IFT root of §3.3), not at m → 0⁺.
  - No new count. But the law then encodes Σ n_i m_i^k of the SM to the shear rows' precision. Any change of the spectrum detunes μ_E and μ_T2 at O(c₁ΣΔm a) ≈ 1e-19, which is a graviton mass of about 1e10 GeV in the reading of §3.3.
  - The electroweak transition (all SM masses switching on), the QCD transition and thermal masses are such changes. Whether the detuning before or during them is observable is not computed (suggested).
  - Gates: source/action `AX:187`; dynamics downstream `AX:114-130`.
- **P-R19-11b (new, suggested count): a mass-blind gravity block.**
  - Zero the mass coefficients per edge instead. Each c_k must vanish separately, because the SM sums Σn_im_i^k are all nonzero.
  - Dirac edge, both shear rows, k = 1, …, 5: 10 conditions. The k = 6 term is 2.5e-101·c₆, below 3.2e-98.
  - Scalar-edge and vector-edge μ_E, k = 2, 4: 4 conditions. m⁶ ≈ 1e-102 passes.
  - The three speed rows' Dirac c₁, if R16-2's comparator is imposed: 3 conditions.
  - That is about 14–17 extra equality conditions, assuming generic nonzero coefficients and no logs below sixth order. The declared families have no spare knobs for them (not tested).
  - This is C4 RP's R2/R4/R6 structure (`TESTS:1902-1913`), with the Wilson-Dirac odd orders added.
- **P-R19-11c (new; constructive for the speed rows): a twisted-mass Dirac edge.**
  - Put the Dirac mass in the Clifford direction orthogonal to the Wilson term: h = α·S + βW + i m βγ₅ (the twisted-mass construction of Frezzotti and Rossi, RECALLED). Then c = (S_x, S_y, S_z, W_tot, m) and E² = S² + W_tot² + m².
  - **Every Dirac row is then even in m** (proved by inspection). m enters only as a constant fifth component of c, and every pair weight depends on c through |c|², c·c′ and c·G with G₅ = 0. This holds for all six rows in the Clifford-linear representations used here.
  - **Checked** for the four axial and shear rows with an independent re-implementation (`run/twisted.py`). At m = 0 it reproduces the archived rows exactly; |c₁| is at print-precision noise; c₂ is (−1.79e-3, −7.09e-4, +8.56e-3, −3.8e-6) per field (`run/twfit.out`).
  - **The 0⁺ root is unchanged**, because the rows coincide at m = 0.
  - **Residuals at the SM spectrum become O((m a)²).**
    - Speed rows: Δc = 2.7e-35 (T₂g) and 1.1e-35 (E_g). That is below both GW170817 and R16-2's comparator by 16 decades or more.
    - Face rows: a twisted version of R18-13's `dface` (`run/dface_tw.py`, patched in memory) reproduces the archived rows exactly at m = 0. For m ∈ [5e-4, 4e-3], |row − row₀|/m² ≤ 7e-3 per field (`run/dface_tw.out`), with the quadrature caveat above. So the twisted face residuals are ≲ 7e-3 × Σn_i(m_ia)² = 7e-3 × 6.0e-34 ≈ 4e-36, i.e. Δc ≲ 1.1e-34 (checked to that bound).
    - Shear rows: μ_E ≈ +4.4e-36 and μ_T2 ≈ −2.3e-39. That is still 1e62 and 7e58 above the GW comparator.
  - **The price.** A mass term twisted against the Wilson term breaks parity (and flavour, if twisted per doublet with τ₃) at O(a) on the lattice. A per-flavour twist phase would also feed arg det M, i.e. the strong-CP θ̄ gate (`AX:179`). Twisting within doublets cancels that phase (RECALLED, suggested).
  - Gates: source/action `AX:187`; dynamics downstream `AX:114-130`.
- **Bill (reading, per-datum basis).**
  - At one loop, for the SM spectrum: unchanged at **6 equality tunings + 1 photon-window selection** (P-R19-11a), now tuned against the spectrum.
  - Or **6 + 1 + about 14–17** for a mass-blind law (P-R19-11b).
  - Or **6 + 1 + about 8** for a mass-blind law with a twisted-mass Dirac edge (P-R19-11b with P-R19-11c): the m² and m⁴ coefficients of the Dirac μ_E and μ_T2 and of the scalar and vector μ_E. Odd orders vanish identically; the speed rows need nothing.
  - Unpaid as before: the LV tadpole, CC, exact W1, the charge block (R19-12, running), radiative stability, two loops.
- **No axiom text changes.**

---

## 4. Against the FIXED readings (`TESTS:7647-7650`)

| reading | clause | status |
|---|---|---|
| **ONE-LAW** | a massless-limit root exists | **met** (checked; §3.2), with the six rows, transversal, subluminal |
| | residuals at SM masses below the GW170817 comparator | **not met** for μ_E and μ_T2 (≈ 1e79 above, under the graviton-mass reading of the shear rows, `PRICE_NOTE.md:22`). Met for the four speed rows (≥ 300× below) |
| | below the R16-2 photon comparator | **not met** for Ξ_T2g, face1, face2 (6.0×, 7.0×, 8.9× above); met for Ξ_Eg (0.70×) |
| **MASS-OBSTRUCTED** | some row diverges or is non-analytic as m → 0 | **not met.** No row diverges. Scalar and vector-μ rows are analytic in m² (Lemma B), and Dirac rows are analytic in m (Lemma A, checked for the face rows). If "non-analytic" were read as "not analytic in m²", the Dirac rows' odd terms would qualify, but see the next clause |
| | so that no single law serves all SM masses | **false at one loop.** The IFT law of §3.3 serves the whole SM spectrum with the same knob count |
| **OPEN** | otherwise | **This is the reading.** |

**Worker reading: OPEN** (literal first, `TESTS:7124`). NEITHER branch, stated explicitly: the massless-limit law exists but fails the comparators; the spectrum-tuned law exists but is not a massless-limit law.

**With the twisted-mass completion P-R19-11c** (a new, priced completion, not the registered setting): the speed-row clauses of ONE-LAW are met (Δc ≈ 1e-35 for E_g and T₂g; ≲ 1e-34 for the face rows). The shear-row clause still fails by about 1e62. The reading stays OPEN.

**Expectation (`TESTS:7651`).** "ONE-LAW … corrections ~(m·a)² ≲ 1e-34" was wrong twice:
- the Wilson-Dirac rows are not even in m, so the corrections are O(m a) ≈ 1e-17 × c₁ (as `vR16-13:23` and `C5_R17-13_report.md:230` had found for single rows);
- the shear rows' comparator is about 1e-98, not 1e-15.

The feared IR logs are absent: Lemma A, Lemma B, and fits.

**Removed hypothesis (fixed finite m):** removed. The 0⁺ root exists and differs from the m = 0.01 root at O(m).

**The verdicts' open item "one law at both masses"** (`vR18-9:23`; `vR18-13:13`). A law tuned at one common mass does not zero the rows at another, because the drift is linear in m (Δr = +0.0127 from m = 0.01 to 0⁺; μ_T2 per field moves by −2.55e-5 at fixed law, `run/mscan_d_GL4_10.out`). The question is replaced by two existence results:
- the m → 0⁺ law exists (§3.2);
- the spectrum-tuned law exists (§3.3).

## 5. Strong-word check

- **"Proved"** is used for:
  - Lemma A, for the axial and shear Dirac rows, under the archived dfam/xiud representations and D1's box exactness;
  - Lemma B, under R14-3's Schwinger forms for G_w edges;
  - the IFT statement, given the checked root and Jacobian and assuming C¹ massive-vector Ξ and face rows;
  - the six-row-root existence from the axial root plus Lemma O (R18-13's refereed lemma).

  Each is a short argument from stated definitions. All are unrefereed.
- **"Checked"** means numerics here: coefficients, the 0⁺ root, the off-axis solve, the direct re-evaluation, the scaled-spectrum root, and the reproduction of archived values.
- **"No log"** is proved for the axial and shear rows (Lemmas A and B) and checked by fits for the face rows (m ln m ≤ 3e-7). An m² ln m term in the Dirac face rows is not excluded (fit-level, harmless).
- **"Exists"** for the 0⁺ root means a transversal Newton root to 3e-11 at GL(5,12), quadrature-stable to ~2e-6 in totals. It does not mean a Newton–Kantorovich certificate.
- **"1e79 above"** depends on reading μ as a graviton mass² with R9-9's prefactor. That is a reading, conditional on PRICE_NOTE:22's supplied metric. Under a prefactor change of up to 10× it remains at least 1e78.
- **"6–9× above R16-2's comparator"** carries the O(1) normalization caveat of §3.3. A factor-4 normalization change would still leave T₂g (4e-19) and face2 (6e-19) above.
- **Twisted mass.**
  - "Even in m" is proved by inspection of the representation.
  - The twisted c₂ values come from my re-implementation of R16-13's and R18-5's formulas with a fifth constant Clifford component. That re-implementation agrees with the archived code exactly at m = 0, but it was not validated against a brute-force finite-q grid at m ≠ 0. So these values are checked only in that limited sense.
  - Twisted face rows were computed only with the patched `dface`, and are bounded rather than fitted.
- **Not claimed:**
  - any exact-W1 statement;
  - SF derived;
  - massive-vector Ξ and face values;
  - the photon window recomputed at 0⁺;
  - anything about two loops, running masses, thermal masses or cosmological history;
  - that P-R19-11b's count is minimal.

## 6. For the referee

1. **Lemma A's support claim**, especially that the UD − V0 pointwise difference and every dfam integrand vanish where the relevant coordinates lie in the D1 box, and the complex-m lower bound |m|² ≥ S(k_j)² + W(k_j)².
2. **Lemma B's decay** of J and 3F₂² − F₄E₀ for G_w edges.
3. **The 0⁺ root.** Reproduce it from `run/root0_final.npy` (or `root0_refined.npy`) at converged Dirac quadrature, and the off-axis solve (`run/fsolve0.out`). Also the scaled-spectrum root (`run/spectrum_2e-3.out`), which is the numerical face of the IFT claim.
4. **The reading.** Whether ONE-LAW's comparator clause applies to the shear rows through the graviton-mass conversion. If the shear rows are judged only against P0's 5.7e-99 of natural size (`PRICE_NOTE.md:162`), the verdict is the same: 4.7e-19 against natural sizes of about 1e-2. Also whether the IFT law defeats MASS-OBSTRUCTED's "no single law" clause.
5. **The Dirac face rows' possible m² ln m term** (`run/mlogm_dense.out`, `run/fitres_root0_dense.out`).

## 7. Files (`S/run/`)

- **Rechecks:** `phq.py` → `phq_N224.out`, `phq_N224.npy`; `test_d.out`.
- **(a) Mass scans:**
  - `mscan_s.py` → `mscan_s.out` (R18-9 root), `mscan_s_root0.out`;
  - `mscan_d.py` → `mscan_d_GL4_10.out`, `mscan_d_GL6_16.out` (one mass; run stopped), `mscan_d_root0_GL4_10.out`, `mscan_d_root0_dense_GL4_10.out`, `mscan_d_root0_GL6_16.out`;
  - `vmu.py` → `vmu.out`.
- **Fits and residuals:** `fitres.py` → `fitres_R18-9root.out`, `fitres_root0.out`, `fitres_root0_dense.out`; `mlogm.py` → `mlogm_root0.out`, `mlogm_dense.out`.
- **(b) Root:** `root0.py` → `root0_m0.out`, `root0_m0.npy`; `refine0.py` → `refine0.out`, `root0_refined.npy`; `final0.py` → `final0.out`, `root0_final.npy`.
- **(b) Off-axis:** `photface0.py` → `photface0_N224.out`, `.npy`; `fsolve0.py` → `fsolve0.out`; `photdirect0.py` → `photdirect0.out`.
- **Quadrature check of slopes:** `slope616.py` → `slope616.out`.
- **Twisted mass (P-R19-11c):** `twisted.py` → `twisted.out`; `twfit.py` → `twfit.out`; `dface_tw.py` → `dface_tw.out`.
- **Scaled-spectrum IFT demonstration:** `spectrum.py` → `spectrum_2e-3.out`.
