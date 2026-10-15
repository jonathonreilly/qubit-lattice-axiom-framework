# CKM versus corner protection in X2: a supervisor synthesis (2026-10-15, written 15:2x–15:32Z; header time corrected from a typed-ahead 15:40Z)

**Status.** This is my own synthesis of refereed campaign results, written for panel E. It adds no new computation.

**Labels.**
- **Proved-by-cited:** the premise is a refereed result, and I state exactly what it covers.
- **Reading:** my interpretation.

## The chain

1. **With exact unit translations, CKM is a permutation.** (Proved-by-cited: OBS-4 S1 and the NFC lemma, confirmed by OBS-4's referee for definite-momentum D3 content.)
   - X2 puts each generation's whole 16 at one hw1 corner. That includes Q, which carries both u_L and d_L.
   - A Yukawa between corners c and c′ needs a scalar of momentum Q_c + Q_c′. The k = 0 Higgs therefore gives corner-diagonal M_u and M_d.
   - Both left rotations are then monomial, so |V_CKM| is a permutation matrix.
   - **Consequence:** the observed CKM needs a condensate at momenta K ∈ hw2, which breaks unit translations spontaneously at some scale v_T.

2. **If v_T is at the electroweak scale (doublet carriers), there is a FCNC failure in the benchmark.**
   - **Proved-by-cited:** OBS-4 and its referee, D3 benchmark, degenerate heavy H/A.
   - The mass-basis couplings are large: |Ŷ_uc| ≈ 0.66.
   - ΔF = 2 needs M* ≈ 1.3–7.9e3 TeV untuned.
   - Exact translations remove the ordinary decoupling term, so the carriers come out naturally at the TeV scale.
   - **Not established:** a universal ceiling, coverage of D6, general non-degenerate potentials.

3. **If v_T is high (singlet condensate S_K, "class S"), the light generations mix with each other.**
   - **Proved-by-cited:** CLS-1 and its referee.
   - The light–light density and kinetic operators ψ_c†ψ_c′S_K carry the same translation charge as the CKM Yukawa ψ_cψ_c′H₀S_K. They are permitted by Spin(10), G_SM, cubic symmetry and the condensate pattern.
   - Their coefficients are independent of the Yukawa coefficient, but nothing protects them. At natural size they exceed neutrino Lorentz-violation bounds by about 1e26 (dimension 4) and about 1e42 (dimension 3, unless a lattice CPT Θ is imposed).
   - A one-loop toy regenerates them, with a spread of about 2.9e-2.

4. **v_T cannot sit far below 1/a without losing the Yukawas** (reading, from the CLS-1 and OBS-4 sizes).
   - The off-diagonal Yukawa is a dimension-5 term, y_off ≈ g·f·a.
   - For B-gen's up sector, y_off ≈ y_t/3 ≈ 0.33. With g ≤ 4π that needs f·a ≳ 0.026.
   - A texture that keeps the up sector nearly diagonal and puts CKM in the down sector (OBS-2's branch B) needs only y_off ≈ y_b/3 ≈ 0.008, so f·a ≳ 6e-4.
   - That re-opens OBS-2's one-loop Lorentz-violation residual (×1e14, unless OBS-3's escape applies). And light–light mixing at ε ≈ g′f ≈ 1e15 GeV still needs tuning of about 1e-25.

5. **Reading.** Every realisation of the observed CKM in X2 tested so far pays one of two prices:
   - (a) electroweak-scale carriers that fail ΔF = 2 in the benchmark; or
   - (b) lattice-scale translation breaking, whose unprotected light–light operators need Θ plus tuning at about 1e-25 to 1e-27.

   This is a structural tension between "generations = corners protected by exact translations" and "the generations mix". It is not a proved no-go:
   - the coefficients in (b) are natural, not forced;
   - the benchmark in (a) is not universal;
   - a symmetry that forbids the light–light operators while allowing the Yukawa has not been excluded.

   The referee called "any symmetry removing it also removes the Yukawa" too strong.

## Questions this hands the panel

- Is there a symmetry, or a field assignment, under which light–light operators of K-charge are forbidden but the Yukawa is allowed? For example, S_K carrying a charge that only the H₀-Yukawa combination can neutralise: H₀ carries hypercharge, and so does the Yukawa product.
- Should generations be decoupled from corners, with corners giving something other than flavour?
- Or does this count as a price route 2 pays, beside SMG and the 16 modes per site?

## Why no flavour symmetry can forbid the light–light mixing in class S (reading; self-corrected before the panel)

**A first idea, withdrawn.** I first proposed a U(1)_S under which S_K is charged and only the Yukawa is neutral. It fails.
- Uniform corner charges force q_S = 0 once the diagonal Yukawas are allowed: 2q_c + q_H = 0, so q_c is uniform.
- Putting the diagonal masses on a k = 0 spurion S_0 with the same charge makes S_K·S_0† neutral, and that product carries momentum K. So the mixing returns at second order, ε ≈ g′f_K·f_0·a, and B-gen needs f_0 ≈ f_K.

**The general point.** The Yukawa matrix is itself the spurion. Any kinetic operator ψ†_c(YY†)_cc′ψ_c′ is neutral under every flavour symmetry the Yukawas respect.
- CKM ≠ permutation forces off-diagonal (YY†)_cc′. These are OBS-3's L-words.
- In class S the translation breaking sits at the lattice scale, so the loop that generates this operator is a lattice-scale loop. It is Lorentz-violating at O(1) × y²/16π².
- This is CLS-1's one-loop toy, with spread about 2.9e-2 after the referee's correction.
- In the doublet (D3) case, by contrast, the breaking is at the electroweak scale. Continuum loops there carry Lorentz violation only at about (v·a)². That case fails on FCNC instead.

**Reading.** The tension is between where the generation mixing is generated and where Lorentz invariance is emergent.
- CKM needs corner-changing spurions.
- At the electroweak scale they bring light carriers, which give FCNC.
- At the lattice scale they feed lattice-scale loops, which give Lorentz violation with no symmetry to stop them.
- A way out would need the corner-changing spurion to live at an intermediate scale where both are small. OBS-4 and CLS-1's sizes suggest no such window for B-gen: the top-sector off-diagonal needs f·a ≳ 0.026. For down-sector-only textures it is also unlikely, with f·a ≳ 6e-4 and a one-loop residual of order (y_b/3)²/16π², about 4e-7 ≫ 1e-28. This is a test the panel can pre-register.
