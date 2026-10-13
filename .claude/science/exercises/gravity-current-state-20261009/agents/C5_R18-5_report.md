# C5 R18-5 report: does the Dirac vertex V0 pass the forward test, and can SM content sit on one cone under conserved vertices?

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. 2026-10-13, 02:18Z to 03:00Z. No repository file was edited. No downloads and no web lookups.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`.
- `S/` = `.../scratchpad/C5/R18-5/`. Scripts and `.out` files are in `S/scripts/`.
- Every run used `OMP_NUM_THREADS=2`. The longest single run was 504 s (`smsolve_UD_A.out`). Machine load was about 4–7 from other jobs.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `P/TESTS.md`:
  - C5 method and readings (`:2302-2319`);
  - round-17 rules (`:5685-5713`) and round-18 rules (`:6392-6406`);
  - verdicts R16-13 (`:6146-6156`), R17-9 and the R17-12 worker line (`:6580-6612`);
  - my item (`:6629-6653`), with its R17-13 worker line (`:6654-6663`).
- `P/agents/`:
  - `C5_R17-12_report.md` (all), and its referee verdict, which appeared while I ran: `scratchpad/C5/ref_R17-12/REFEREE_VERDICT.md` (`vR17-12`), **CONFIRMED WITH CORRECTIONS**, Lemma F confirmed (`vR17-12:5`);
  - `C5_R17-13_report.md` (§§0–1, the rows table), and its verdict `ref_R17-13/REFEREE_VERDICT.md` (`vR17-13`), **ZEROED**, with the four-row SM problem OPEN (`vR17-13:3,17`);
  - `C5_R16-13_report.md:1-200` and verdict (`vR16-13`);
  - `C5_R17-9_referee_verdict.md` (`vR17-9`) and `C5_R17-9_report.md:24-35,101,225-227,239,281`;
  - `C5_R17-4_report.md:1-60,100-140` and verdict (`vR17-4`);
  - `C5_S23_synthesis.md` §1.3 (`:171-220`) and §1.8 (`:344-371`).
- R13-5's W1 hypotheses enter only as R17-12 imports them (`rR17-12:70-74`, confirmed in `vR17-12:5`).

**Runners rechecked before use (checked).**
- `P/scripts/C5/R17-12/*.py` were copied unmodified into `S/scripts/`. These include R16-13's `dirac.py`, `dfam.py`, `content3.py` and `content4.py`, R17-12's `r1712_lib.py`, `photon.py` and `zz.py`.
- **V0 on D1(1.4, 0.3), m = 0.01:** (Ξ_T2g, Ξ_Eg, μ_E) = (+5.4601e-3, +2.8291e-3, −2.9186e-2). This equals the R16-13 referee's independent values (`vR16-13:7-13`). Source: `xiud_laws_m0.01.out:1`.
- **V0 at R17-13's zero D1(0.916719, 0.559627):** (+4.3474e-3, +1.2469e-3, −1.7230e-2) and μ_T2 = +9.2e-11. These are R17-13's numbers (`rR17-13:221`). Source: `xiud_laws_m0.01.out:4`.
- **One bug of my own, fixed before use.** My `phot()` first passed the stencil weight positionally into R17-12's `xi(..., shifts=...)` argument. It was fixed to `lam=` before any VWa run. The VW0 runs were unaffected.

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **V0 fails the forward test (proved; checked).**
   - On the positive band, V0's forward stress is s_is_j/E.
   - Lemma F requires p_ip_j/E, with p = ∇(E²/2) = s s′ + M W′.
   - The two agree only inside the Dirac box. Outside it the mismatch is O(1): 1.5–1.9 against a scale of 0.76–0.99 on three D1 laws (`fwd_cov.out:12-61`).
   - **In the mirror boxes (s′ = −1, W′ = 0) V0's forward momentum flux has the wrong sign.** There p = −s along that axis.
   - The Wilson mass enters the required value through M W′. V0 leaves it out.
2. **V0 passes covariance (proved; checked). Lemma M's zero does not apply to Dirac pairs (proved).**
   - V0 is covariant under the spin-½ lift of C₂ₓ, C₂ᵧ and C₄z to rounding (`fwd_cov.out:64`).
   - Its T₂g pair weight at the face K = (π, K_y, 0) is nonzero.
   - That is allowed for spinors. C₂ᵧ covariance at the fixed point requires only S†AS = −A for the pair matrix A. Because S² = −1, S⊗S has a −1 eigenspace on the pair labels, so A ≠ 0 is allowed (Lemma M′, §3.2).
   - Lemma M's zero is forced only for scalar legs (`vR17-4:7`: "single … scalar pair amplitude").
3. **The replacement vertex (proved; checked).**
   - The vertex is **UD: T_ij = ½(p_j ∂_ih + p_i ∂_jh)**, i.e. G_T2g = (½p_ys′_x, ½p_xs′_y, 0, ½(p_yW′_x + p_xW′_y)) on (α_x, α_y, α_z, β). It couples the Wilson mass through β and through M in p.
   - **Uniqueness (Lemma D).** In the family 𝔇 of stresses ½(a_j∂_ih + a_i∂_jh) with one covariant vector field a, Lemma F forces a = p.
   - **The vielbein family has no conserved member (Lemma D₀).** No member of V0's own family ½(a_jα_i + a_iα_j) passes Lemma F on any D1 edge.
   - **UD and SF share the first-order map (proved).** UD is the operator generator of the stipulated SF strain flow dk/de = ½h·p, so its forward block equals SF's first-order mode-energy shift.
   - **Outside 𝔇 the pair block is free (proved; checked).** V0* = V0 + h(pp − ss)/E² passes Lemma F, keeps V0's q = 0 pair block, and gives very different Ξ (§3.3).
4. **Conserved Dirac signs (checked).** Comparing UD with V0 on D1 at m = 0.01 (`ud_grid.out`, 32 laws; `xiud_laws_m0.01.out`):
   - UD lowers Ξ_T2g on all 8 laws of `xiud_laws_m0.01.out`. It lowers Ξ_Eg on large boxes and raises it on small ones (D1(0.3, 0.5): −2.31e-3 → −0.99e-3).
   - On small Dirac boxes (b_f ≤ 0.3) Ξ_T2g turns negative.
   - The birefringence Ξ_T2g − Ξ_Eg ranges over [−5.2e-4, +2.4e-3] under UD, against V0's minimum of +2.57e-3. **R16-13's birefringence obstruction (`rR16-13:200`) belongs to V0.**
   - μ_E and μ_T2 are unchanged: they come from SF and do not depend on the vertex (`vR17-13:11`).
5. **SM-count zero under (U, UD, VW) (checked; worker). Knobs counted.**
   - **Content.**
     - 4 real scalars on one Higgs edge G_w(2.361986, 0.134479), U vertex;
     - 22.5 Dirac fields on D1(0.167717, 0.484515), UD vertex;
     - 12 vectors on γGw(1.271203, 0.259986), VW with a **signed** two-offset stencil a = −0.122745 (weights 1.122745 at z ± ½ and −0.122745 at z ± 3/2; λ = 0.0045 < ¼).
     - Common matter mass m = 0.01.
   - **Totals** (Ξ_T2g, Ξ_Eg, μ_E):
     - +4.5e-14, −7.5e-14, −6.6e-15 at photon grid N = 96 (`refine_C96.out`);
     - +1.6e-6, +3.9e-6, +1.6e-8 at N = 160 after one Newton step;
     - +8.2e-6, +7.8e-6 at N = 192 (`newton_hi.out`).
     - The content contributions per row are about ±2e-2 (`final_check.out`).
   - **Transversal.** det J = 3.4e-3 in the knobs (b_g, a, w_s).
   - **Subluminal on every edge.** Dirac by Lemma V1 (r = 0.4845 < 1/√3; sampled v_max 0.99996). Photon d′ ∈ [0, 1], so v_max = 1, reached in the box. Scalar v_max 0.999997.
   - **Tunings: 3, one of them a non-shape placement datum** (the VW stencil, P-R17-12b with signed weights) **and two edge shapes.**
   - **Left unpaid:** μ_T2 = +9.11e-2 (R17-13's row; not a FIXED row here).
   - **The signed stencil was needed in the search.** With nonnegative stencils (VW0) under UD, two solves stopped at bounds with Ξ_T2g = −7.6e-3 (`smsolve_UD_A.out`, `_B.out`).
6. **Against the FIXED readings (`TESTS:6650-6652`):**
   - **V0-FAILS (worker; referee required):** met through Lemma F, with UD as the replacement.
   - **SM-LIFTED-CONSERVED (worker; checked):** met on the letter, with the scope conditions in §4.
   - **Expectation (`TESTS:6653`):** V0-FAILS as expected. "The SM solve then stays OPEN" is refuted in-sample: a root exists, but it uses a signed placement stencil.

---

## 1. Class, hypotheses, stipulations and exclusions (stated before any title)

**Setting (`TESTS:6637`).**
- **Dirac edges.** 4-component Wilson-Dirac D1(b, r) (R14-1; `dirac.py`): h = Σs(k_j)α_j + Mβ, M = m + ΣW(k_j), W′ = r√(1 − s′²), r ≤ 1/√3 (Lemma V1, `rR16-13:176`).
- **Scalar.** The U vertex on one Higgs edge G_w(b_s, w_s), in class 𝒮.
- **Vectors.** VW (R17-12) on γGw(b_γ, w_γ) photons with d′ ∈ [0, 1].
- **Fixed elements.**
  - SM counts 4 + 22.5 + 12.
  - Axial q = qẑ, one loop, m = 0.01.
  - The supplied zero-point vacuum / filled sea, with an ultralocal seagull.
  - SF for every shear row (stipulated, P-R16-13a).
- **Excluded (`TESTS:6638`):** VU, VM, the M vertex, pairing, superluminal edges.

**W1 hypotheses for the Dirac field (imported, as R17-12 did).**
- (W1-s) is the scattering-channel Ward identity, with a kernel C¹ near the diagonal.
- (H-sym) is a symmetric T^{μν}.
- (H-E) is F⁰⁰(k, k) = E δ_λλ′.
- The positive band is two-fold degenerate, and Lemma F's proof (`rR17-12:108-116`, confirmed `vR17-12:5`) holds for any basis of it.
- **Holes.** The antiparticle at −k has forward value −P₋ΓP₋. So the requirement is P₋ΓP₋ = −E v_iv_j P₋. T⁰⁰ = h satisfies (H-E) for both.
- **Not new.** R16-13 already assumed "standard first-order W1" for fermions (`rR16-13:89`). The forward test therefore uses R16-13's own setting.

**Families (stated before results).**
- **𝒞 (Clifford-linear):** Γ_e = G_e(k)·γ, with γ = (α_x, α_y, α_z, β) and G real. This is Theorem DT's family with k_z-dependence allowed. It contains V0, UD and V0*.
- **𝔇₀ (vielbein, one vector):** T_ij = ½(a_jα_i + a_iα_j). V0 is a = s.
- **𝔇 (strain-flow, one vector):** T_ij = ½(a_j∂_ih + a_i∂_jh). UD is a = p.

**Placement of UD's k_z-dependence (stated law datum).**
- UD depends on k_z through M.
- For the pair (k − q/2, k + q/2) I use the **midpoint** prescription G(k).
- The leg-average ½(G(k − q/2) + G(k + q/2)) differs at O(q²). §3.4 gives the sensitivity.

**Ξ for k_z-dependent G (proved here; checked).** With g = c·G, g₁ = c′·G, g₂ = c″·G (′ = ∂_z) and t₀ = (N_c/2)(|G|² − g²/E²):

  α = ¼⟨t₀E″/(2E²) + (N_c/2)[|G|²(|c′|² − E′²) + g g₂ − g₁² − g²(EE″ − E′²)/E²]/E³⟩,  β = −⟨t₀/(4E³)⟩.

- **Derivation.** Expand t and 1/(E₊ + E₋) to O(u²) with u = q/2, using ĉ₋·ĉ₊ = 1 − 2u²(|c′|² − E′²)/E² + O(u⁴).
- **Reduces to Theorem DT.** For g₁ = g₂ = 0 and k_z-independent |G|, two periodic integrations by parts give `rR16-13:138-160` exactly.
- **Evaluation.** Ξ_X = Ξ_V0 [R16-13 closed form, `dfam.py`] + ⟨integrand_X − integrand_V0⟩. The difference vanishes identically where |k_x|, |k_y| < b, so the m = 0.01 box is never sampled.
- **Checks.**
  - The V0 pointwise form equals the closed form to 1e-9 (`xiud_validate.out:2`).
  - A direct finite-q midpoint grid agrees with the pointwise formula at m = 0.3, for UD and V0*:
    - D1(1.4, 0.3): UD +4.3205e-3 (N = 96) against +4.3264e-3 (GL);
    - at the root's Dirac law D1(0.16772, 0.48451): UD T₂g −8.42118e-4 (N = 128) against −8.42102e-4, and E_g −7.56965e-4 against −7.56948e-4 (`validate_root_law.out`).

**Round-18 head rules (`TESTS:6403-6406`).**
- **Locality of vertices.**
  - The Dirac vertices V0, UD and V0* do **not** have the scalar Lemma-M zero. That zero is not implied for spin-½ legs (Lemma M′).
  - They satisfy the spinor covariance condition exactly, and their kernels are absolutely summable: smooth periodic symbols, with E ≥ m > 0 on V0*'s support.
  - VW passes the face test (`rR17-12:186`) and U passes (`vR17-4:7`).
- **Whole-zone v_max** (§0.5), gauge field included.
- **Counting.** Counterterm basis is per edge: one Higgs edge, one Dirac edge shared by the 22.5 fields, one photon edge.
- **No CONFLICT is claimed,** so no certificate is required.

## 2. Prior art (each counted once)

- **R17-12 + vR17-12.** Lemma F (confirmed, necessary-order); VW; Lemma X within 𝔐; Lemma I (stencils W1-invisible, conditional on an exact completion); signed stencils not searched (`rR17-12:252`). Suggested follow-up: apply Lemma F to V0 (`rR17-12:332`). This item is that follow-up.
- **R16-13 + vR16-13.** V0 and SF as stipulations; the Wilson-coupled variant "G_β ∝ R_xR_y … coded but not run" (`rR16-13:87`); Theorem DT; Lemma V1; birefringence ≥ +2.6e-3 per field on V0 (`rR16-13:200`).
- **R17-9 + vR17-9.** The VM root (void under vR17-12); the sampled inequalities (`rR17-9:225-227`), which were computed with V0.
- **R17-4 + vR17-4.** Lemma M, scoped to a single scalar amplitude.
- **R17-13 + vR17-13.** μ_T2 depends on the band and SF only; ZEROED at D1(0.916719, 0.559627); the four-row SM problem OPEN.
- **R13-5.** W1 hypotheses, and the pair stress as a law datum (C3, `rR17-12:166`).
- **Grep.** I searched `P/agents/*.md` for Dirac forward values, "Lemma F" and Wilson-stress coupling. The only hits are R17-12's suggestion and R16-13's unrun `lamW` variant. No Dirac forward test or strain-flow Dirac vertex exists in the packet.

---

## 3. Results

### 3.1 (a) Lemma F for V0

**Corollary DF (proved).**
- For Γ = G·γ: P₊γ_aP₊ = ĉ_aP₊ and P₋γ_aP₋ = −ĉ_aP₋. So P₊ΓP₊ = (c·G/E)P₊ and P₋ΓP₋ = −(c·G/E)P₋.
- Lemma F then requires exactly **c·G_e = e:(p⊗p)**, i.e. p_xp_y for T₂g and ½(p_x² − p_y²) for E_g.
- V0 has c·G = s_xs_y (and ½(s_x² − s_y²)).
- So V0 passes iff s_xs_y = p_xp_y, with p_j = s_js′_j + MW′_j.
- On D1, p_j = s_j iff |k_j| < b (where s′ = 1 and W′ = 0), or at isolated points.
- In the mirror box |k_j| > π − b, s′ = −1 and W′ = 0, so p_j = −s_j. **V0's forward T_xy has the opposite sign to the required one whenever exactly one of k_x, k_y is in a mirror box.** ∎

**Checked** (`fwd_cov.out`; 300 random k per region; operator 2-norm, both bands):

| law (m = 0.01) | V0 off box: T₂g / E_g / T_xx (scale) | UD, V0* (all) |
|---|---|---|
| D1(1.4, 0.3) | 1.86 (0.99) / 0.72 (0.71) / 1.43 (1.43) | ≤ 4.8e-16 |
| D1(1.313475, 0.572783) (vR16-13 root) | 1.78 (0.88) / 0.71 (0.65) / 1.33 (1.30) | ≤ 5.4e-16 |
| D1(0.916719, 0.559627) (R17-13 zero) | 1.48 (0.76) / 0.63 (0.57) / 1.15 (1.13) | ≤ 4.7e-16 |

Inside the box, all three vertices pass to ≤ 2.4e-16.

**Lemma D₀ (proved): no member of V0's family 𝔇₀ passes Lemma F on a D1 edge.**
1. The diagonal entries give a_is_i/E = p_i²/E, so a_i = p_i²/s_i.
2. The T₂g entry then needs ½(p_y²s_x/s_y + p_x²s_y/s_x) = p_xp_y, i.e. (p_ys_x − p_xs_y)² = 0, i.e. p_x/s_x = p_y/s_y.
3. That fails at any k with |k_x| < b (ratio 1) and k_y in the Wilson region (ratio s′_y + MW′_y/s_y ≠ 1). ∎

**Lemma D (proved): in 𝔇, Lemma F forces a = p, which is UD.**
1. P₊∂_ihP₊ = v_iP₊ (Hellmann–Feynman), and P₋∂_ihP₋ = −v_iP₋.
2. The diagonal T_ii gives a_iv_i = Ev_i², so a_i = Ev_i = p_i on {v_i ≠ 0}.
3. On D1, {p_i = 0} has empty interior: p_i is affine in M with slope W′_i > 0 on (b, π − b), and equals k_i on the box. Continuity of a gives a = p everywhere.
4. The off-diagonal components then hold: ½(p_yv_x + p_xv_y) = Ev_xv_y. ∎

**UD written out.**
- T₂g: G = (½p_ys′_x, ½p_xs′_y, 0, ½(p_yW′_x + p_xW′_y)).
- E_g: G = (½p_xs′_x, −½p_ys′_y, 0, ½(p_xW′_x − p_yW′_y)).
- **The Wilson mass is coupled** through the β entry and through M inside p.
- In the box UD = V0 identically, since s = k, s′ = 1 and W′ = 0 there.

**UD is SF's operator (proved).**
- SF maps h(k) → h(k + ½h·p), so δh = ½h_ij p_j ∂_ih = ½h_ij(UD)_ij.
- Its first-order energy shift ½h_ijp_ip_j/E equals ½h_ij times UD's forward value.
- **Not shown:** that SF's second-order shear equals UD's static q⁰ response with some seagull. So "UD and SF are one vertex" is suggested beyond first order, not proved.

### 3.2 Covariance; Lemma M′ (proved; checked)

**Lemma M′.**
- **Setting.** Spin-½ site fields, ψ(r) → Sψ(Rr), with S the spin lift of a proper rotation R in the stabilizer of h_xy's plaquette centre. At q = 0, covariance of T_xy reads S Γ(k) S† = −Γ(Rk).
- **At the face.** At K = (π, K_y, 0), Rk ≡ k for C₂ᵧ. So S A S† = −A for the pair block A = P₊ΓP₋, and S commutes with h(K).
- **Spinors.** S = −iΣ_y has S² = −1 and eigenvalues ±i. The condition says A maps each S-eigenspace into the other. Nonzero A is allowed.
- **Pair labels.** S⊗S has eigenvalues +1 (×8) and −1 (×8) (`fwd_cov.out:82`).
- **Scalars.** For scalar legs S = 1, so A = −A = 0. That is Lemma M. ∎

**Checked.**
- **Covariance.** V0, UD and V0* are covariant under C₂ᵧ, C₂ₓ and C₄z for both TT components to ≤ 1.2e-15 (`fwd_cov.out:64-66`). The band satisfies S h(k) S† = h(Rk) to 7e-16.
- **Face weights.**
  - The face pair weights are nonzero: V0 4.5e-2 to 0.96, UD 4.5e-2 to 0.32, over K_y ∈ {0.3, 0.8, 1.5, 2.5}.
  - ‖S†AS + A‖ = 0 exactly for all three (`fwd_cov.out:69-81`).

**Reading.**
- V0's failure is Lemma F, not covariance.
- The round-18 locality rule's "Lemma-M zero" is a scalar-leg statement. For Dirac vertices the right test is Lemma M′, which V0, UD and V0* pass.
- **Not examined:** the analogous statement for photon legs. VW has the zero anyway.

### 3.3 (b) Signs and sizes, conserved Dirac versus V0 (checked)

Per Dirac field, m = 0.01, GL(4,10). The GL(3,8) → (4,10) change is ≤ 9e-8 (`xiud_laws_m0.01.out`). μ is the same for all vertices (SF).

| D1(b, r) | V0 (T₂g, E_g) | UD (T₂g, E_g) | V0* (T₂g, E_g) | μ_E | μ_T2 |
|---|---|---|---|---|---|
| (1.4, 0.3) | +5.460e-3, +2.829e-3 | +4.676e-3, +2.287e-3 | −8.950e-3, +1.741e-3 | −2.919e-2 | −1.2e-6 |
| (1.313475, 0.572783) | +5.511e-3, +2.801e-3 | +4.312e-3, +1.994e-3 | −8.041e-3, +1.225e-3 | −2.690e-2 | −3.5e-5 |
| (0.916719, 0.559627) | +4.347e-3, +1.247e-3 | +2.026e-3, +1.670e-4 | −6.540e-3, −1.593e-3 | −1.723e-2 | +9e-11 |
| (0.6, 0.5) | +2.837e-3, −6.04e-4 | +5.72e-4, −7.96e-4 | −6.262e-3, −3.607e-3 | −1.069e-2 | +5.1e-4 |
| (0.3, 0.5) | +1.075e-3, −2.308e-3 | −4.25e-4, −9.90e-4 | −5.459e-3, −4.718e-3 | −3.08e-3 | +3.0e-3 |

**32-law grid**, b_f ∈ [0.15, 1.4], r ∈ [0.1, 1/√3] (`ud_grid.out:33`):

| vertex | birefringence Ξ_T2g − Ξ_Eg | Ξ_T2g |
|---|---|---|
| UD | [−5.2e-4, +2.40e-3] | [−1.01e-3, +4.81e-3] |
| V0 | ≥ +2.57e-3 | — |
| V0* | ≤ +3.8e-4 | — |

**Reading.**
- **The Wilson coupling does not flip UD's signs on large boxes (b_f ≥ 0.9; 5 laws in `xiud_laws_m0.01.out`).** It shrinks both rows there.
- **On small boxes (b_f ≤ 0.3) UD's T₂g is negative,** and its birefringence reaches either sign.
- **The pair block matters at O(1).** V0* has V0's q = 0 pair block and a corrected forward block, and its T₂g changes sign on every law. Outside 𝔇 the conserved Dirac Ξ is therefore not fixed by W1 at O(q).

### 3.4 Placement sensitivity of UD (checked)

Midpoint against leg-average prescription, direct grids N = 96 and 128 at m = 0.3 (`presc.out`):
- D1(1.4, 0.3): Δα = +1.0e-6 (T₂g) and +1.7e-7 (E_g).
- D1(0.9167, 0.5596): +1.89e-4 and +6.0e-5, against Ξ ≈ 2e-3.

It is a law datum of the same kind as VW's stencil. **Suggested:** Lemma I's superpotential construction (ΔT^{xy} = D_z²Y) applies, which would make it W1-invisible. Not proved for the Dirac field.

### 3.5 (c) The SM-count solve under (U, UD, VW)

**Knobs.**
- Seven continuous knobs: (b_γ, w_γ) photon, (b_f, r) Dirac, (b_s, w_s) scalar, and a = VW's two-offset stencil weight. P = (1 − a)cos(s/2) + a·cos(3s/2), λ = ¼ + 2a.
- **All are law data.** Six are edge shapes and one is a placement datum (P-R17-12b).
- UD has no knob, since it is unique in 𝔇. The midpoint prescription is a fixed declared choice.

**Rows.** The FIXED rows Ξ_T2g, Ξ_Eg, μ_E. μ_T2 is reported.

**Runs** (`smsolve_ud.py`; local least squares from stated starts; 480–500 s wall-clock guard):

| run | stencil | end point | totals (T₂g, E_g, μ_E) | at bounds |
|---|---|---|---|---|
| A, B | VW0 (a = 0) | both reach the same point: b_γ = 0.15, b_s = 3.0, r = 1/√3 cap | (−7.6e-3, +2.6e-3, −7e-4) | yes |
| **C** | **signed a ∈ [−0.6, 1]** | **root (N = 48)** | **(+4.5e-12, −1.6e-12, +5.6e-12)** | **none** |
| D | signed | second root: γGw(1.341, 0.183), a = −0.1248, D1(0.109, 0.459), G_w(2.603, 0.067) | 1e-11 at N = 48 | none |

Root D was not grid-checked: its photon turn is about 1.4 steps at N = 48.

**Root C, resolved (checked).**

*Grid.*
- At C's N = 48 knobs, the 12-vector part moves by (+5.3e-4, +1.3e-3) between N = 48 and N = 64. From N = 64 to N = 128 it is stable to 4e-5 (`res_check_C.out`).
- **Re-solve at N = 96** in (b_γ, a, w_s), with Dirac GL(4,10): totals (+4.5e-14, −7.5e-14, −6.6e-15) and det J = 3.4e-3 (`refine_C96.out`).
- **At N = 160** the drift was (+6.1e-5, +7.6e-5). After one Newton step with that J: (+1.6e-6, +3.9e-6, +1.6e-8). At N = 192: (+8.2e-6, +7.8e-6) (`newton_hi.out`).
- **Reading.** The residual is photon-grid-limited at ~1e-5, against row contributions of ~2e-2. Since the root is transversal, it persists with knob shifts of ~1e-3 (suggested from J; checked at N = 160 by the Newton step).

*Other quadratures.*
- Dirac GL(5,12) − GL(4,10): (−2e-8, −8e-8, −4.3e-6) for 22.5 fields.
- Scalar n = 2¹⁶ against 2¹⁴: below 3e-14.

**At m = 0.001 (checked).** Re-solved at N = 96 from the stepped root, in the same three knobs (`refine_C96_m0.001.out`):
- (b_γ, a, w_s) = (1.268947, −0.122515, 0.261845), with the Dirac and scalar boxes unchanged;
- totals (−7.3e-14, +5.0e-14, +1.0e-13), det J = 3.6e-3, μ_T2 = +8.86e-2.
- The root persists at the lighter mass with separately tuned knobs (as `vR16-13:23,29` note for R16-13's root).
- It was not grid-checked beyond N = 96.

**Record at the stepped root** (`final_check.out`):

| species (count) | Ξ_T2g | Ξ_Eg | μ_E | μ_T2 |
|---|---|---|---|---|
| real scalar, U, G_w(2.361986, 0.134479) (×4) | −5.467e-4 | −3.838e-4 | +4.605e-3 | 0 |
| Dirac, UD, D1(0.167717, 0.484515) (×22.5) | −7.883e-4 | −1.0504e-3 | −4.746e-4 | +4.049e-3 |
| vector, VW a = −0.122745, γGw(1.271203, 0.259986), N = 160 (×12) | +1.6605e-3 | +2.0978e-3 | −6.452e-4 | 0 |
| **total** | **+1.6e-6** | **+3.9e-6** | **+1.6e-8** | **+9.11e-2** |

**How the root works (reading).**
- The μ_E row (SF, vertex-independent) forces a small Dirac box. Large boxes have μ_E^F ≈ −1e-2 to −3e-2 per field, which 4 scalars and 12 vectors cannot offset (R17-13's shortfall, `vR17-13:15`).
- On small boxes, UD's Dirac fields have both Ξ rows negative with a small birefringence.
- The photons must then add positive T₂g and E_g in nearly equal amounts.
- VW0 photons with positive T₂g have E_g − T₂g ≥ ~4e-3 per vector (`rR17-12:246-248`). The signed stencil lowers E_g faster than T₂g (G_E/G_T ≈ 2–3, `scan_parts.out`), which closes the gap.
- Both roots land at λ ≈ 0 (C: 0.0045; D: 0.0004), i.e. a stencil with nearly zero second moment. Suggested coincidence; not analysed.

### 3.6 (d) Prices and the bill (named, not adopted)

- **P-R18-5a (correction, no new price).**
  - The Dirac TT stress must have Lemma-F forward values p_ip_j/E, under W1 hypotheses R16-13 already assumed.
  - V0 is excluded. So is V0's family 𝔇₀ (Lemma D₀).
  - Every Dirac Ξ number since R16-13 is an integral of a vertex that is not the TT part of any symmetric, O(q)-conserved stress with ∫T⁰⁰ = H. That covers rR16-13 §3.3, R17-9's rows (already void by VM) and R17-12's solves.
  - **Unaffected:** μ_E and μ_T2 (SF), hence R17-13's ZEROED.
- **P-R18-5b (Dirac pair block as law datum).**
  - Within 𝒞, Lemma F fixes only c·G. G_⊥ (the q = 0 pair block) is free: this is R13-5's C3 for fermions.
  - Restricting to 𝔇, which forces UD, is a stipulation. It is motivated by agreement with SF's first-order map, not derived from one lattice action.
  - Source/action gate `AX:187`; dynamics downstream `AX:114-130`.
- **P-R18-5c (Dirac O(q²) placement).** The midpoint versus leg-average choice for UD's k_z-dependence is a law datum. It moves Ξ by up to ~10% per field on some laws (§3.4).
- **Used, not new.**
  - P-R17-12b with **signed** weights (λ < ¼). Signed stencils satisfy every stated requirement: P(0) = 1, so the forward value is unchanged; the stencil is symmetric, so covariant; it is antiperiodic, so continuous; and it is finite-range.
  - SF (P-R16-13a).
  - The VW photon (P-R17-12a/b).
  - One Higgs edge in 𝒮.
- **Bill (reading, conditional; per-edge counterterm basis).**
  - The axis cone (E_g, T₂g) plus the E_g shear are 3 rows, paid by 3 tunings: two edge shapes and one placement-datum tuning (the stencil, a non-shape knob of about 1e-12 at the root precision).
  - This matches S23's count (`S23:344-371`): these rows are already counted, so the total does not change.
  - What changes is the payment. One of the three is a placement datum, not a shape, and no pairing is used.
  - **μ_T2 (+9.11e-2) stays unpaid.** P-R17-13a needs one more Dirac-shape tuning, but on D1 the μ_T2 zero sits near b_f ≈ 0.92 (`vR17-13:17`), where μ_E^F is far more negative. The four-row question stays OPEN.
- **No axiom text changes.** No sizes at a = ℓ_P are quoted (`AX:189-190`).

---

## 4. Against the FIXED readings (`TESTS:6650-6652`)

**V0-FAILS: worker reading MET (referee required).**
- V0 violates Lemma F (Corollary DF, proved; checked to O(1), with the wrong sign in the mirror boxes).
- It does **not** violate covariance (Lemma M′).
- **Replacement vertex: UD**, unique in 𝔇 (Lemma D). It couples the Wilson mass. Outside 𝔇 the pair block is a law datum (P-R18-5b).

**SM-LIFTED-CONSERVED: worker reading MET on the letter (checked), with scope.** The clause, part by part:

| clause | status |
|---|---|
| explicit SM-count content | 4 + 22.5 + 12, knobs in §3.5 |
| conserved vertices | U by definition (`rR17-12:93`); VW (`vR17-12:15`); UD (Lemma D; checked ≤ 5e-16). In every case **at O(q) only**: no exact W1 completion is built for any vertex (`vR17-12:5,19`) |
| covariant | checked |
| local | U and VW finite or absolutely summable; UD absolutely summable |
| every edge subluminal | Lemma V1; photon d′ ≤ 1; scalar in 𝒮 |
| one Higgs edge | yes |
| Ξ_Eg = Ξ_T2g = μ_E = 0 at a common light mass | m = 0.01, to 1e-13 at N = 96 and to the ~1e-5 photon-grid limit at N = 160–192 |
| knobs counted | 3 tunings |

**Scope conditions** (each should be checked by the referee):
1. The VW stencil is **signed** (λ = 0.0045). R17-12 did not search signed stencils (`rR17-12:252`). With nonnegative stencils no root was found.
2. UD rests on the 𝔇 restriction. SF is stipulated.
3. μ_T2 = +9.11e-2 is unpaid. It is not a FIXED row of R18-5.
4. Only axial rows and one loop. The masses are m = 0.01, grid-checked to N = 192, and m = 0.001, re-solved at N = 96 only, with w_s retuned 0.134 → 0.262. Off-axis rows (face1/K₆) for vectors and Dirac fields were not computed.
5. The Dirac box is small (b_f = 0.168) and the photon turn is narrow (w = 0.26). Resolved at N ≥ 96 as stated.
6. "Common light mass" follows R17-9/R17-12's convention: matter at m = 0.01, photon μ_E with a 1e-3 regulator.

**Expectation (`TESTS:6653`).**
- V0-FAILS: **as expected.** The Wilson mass must couple.
- "Changes the Dirac signs": **partly.** Small boxes only; on large boxes the magnitudes shrink.
- "The SM solve then stays OPEN": **refuted in-sample.** A transversal root exists, and it uses a signed placement stencil.

## 5. Strong-word check

- **"Proved"** is used for:
  - Corollary DF;
  - Lemmas D₀, D and M′;
  - the Ξ expansion for k_z-dependent G;
  - UD as SF's first-order operator.
- **"Checked"** is used for every number.
- **"Excluded"** for V0 means: fails the necessary O(q) forward condition under (W1-s), (H-sym), (H-E). It is not excluded as a pair-block datum (V0* keeps V0's pair block legally).
- **"Unique"** for UD means within 𝔇 only.
- **"Root"** means local least squares from stated starts, transversal, grid-checked to N = 192 at C. It is not a claim about the whole solution set. The second root D is at N = 48 only.
- **Not claimed:**
  - exact W1 completion of any vertex;
  - equality of SF's second-order shear with UD's static response;
  - the μ_T2 row;
  - off-axis rows;
  - m = 0.001 beyond N = 96;
  - uniqueness of the root;
  - Lemma I for the Dirac placement.

## 6. For the referee

1. **Corollary DF and the hole sign.** The forward requirement is P₋ΓP₋ = −Ev_iv_jP₋.
2. **Lemma M′.** Is Lemma M's zero really absent for spin-½ legs? I use S⊗S's −1 eigenspace.
3. **Lemma D / D₀,** and whether 𝔇 (one vector a for all components) is the right Dirac analogue of 𝔐₁.
4. **The Ξ expansion for k_z-dependent G** (§1), and the difference method around R16-13's closed form.
5. **The root.** Reproduce it from `S/scripts/smroot_C160.npy` with `final_check.py`, preferably with an independent photon evaluator at N ≥ 160.
6. **Whether signed VW stencils (λ < ¼) are in-setting** under `TESTS:6647` ("VW stencils as declared extra knobs").

## 7. Files (`S/scripts/`)

- **Forward and covariance tests:** `fwd_cov.{py,out}` (Lemma F forward test; spinor covariance; face pair weights; S⊗S spectrum).
- **Ξ evaluator:** `xiud.py` (Ξ for k_z-dependent Clifford-linear vertices: pointwise, difference and brute force).
- **Validation and sizes:**
  - `xiud_validate.out`;
  - `xiud_laws_m0.01.out`;
  - `ud_grid.{py,out}`;
  - `presc.{py,out}`;
  - `validate_root_law.out`.
- **Solves and resolution:**
  - `smud_lib.py`; `smsolve_ud.py` → `smsolve_UD_A.out`, `smsolve_UD_B.out`, `smsolve_UDa_C.out`, `smsolve_UDa_D.out`; `smroot_{A,B,C,D}.npy`;
  - `res_check.{py}` → `res_check_C.out`;
  - `refine.py` → `refine_C96.out`, `smroot_C96.npy`; `refine_m.py` → `refine_C96_m0.001.out`, `smroot_C96m001.npy`;
  - `newton_hi.{py,out}` → `smroot_C160.npy`;
  - `final_check.{py,out}`;
  - `scan_parts.out`.
- **Written, not run:** `smsolve_mix.py` (the Dirac pair-block knob u).
- **Copied unmodified from `P/scripts/C5/R17-12/`:** `dirac.py`, `dfam.py`, `sublum.py`, `content3.py`, `content4.py`, `zz.py`, `photon.py`, `r1712_lib.py`, `r161_laws.py` and the other R17-12 scripts.
