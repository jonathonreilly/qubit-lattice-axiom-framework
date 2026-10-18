**Referee record: GEN-1, GEN-2, LOCK-1.** Same-family referee (Claude Opus 5.5, not independent). I ran three spot checks, each under 40 MB, in `chirality_ex/ref_GENLOCK_sf/` (`chk_gen1_n.py`, `chk_fold.py`). The repo was read only, using `origin/main` at fa841753c1.

---

## GEN-1: CONFIRMED WITH CORRECTIONS (same-family referee)

**Correct fixed reading:** GEN-CONE(n). Every count is ≤ 8: literal rows n = 0, two-sided rows n = **1** (not 2), all one-loop terms n_all = 8.

**Key findings**
1. **a3(ii), the twist argument, is sound.**
   - At each corner, Z₂³ acts through the central element (−1)^F. So each corner's anomaly is the 48-Weyl anomaly pulled back along a group homomorphism, and that anomaly is trivial (`GEN1/REPORT.md:34-37`).
   - It is conditional on recalled values: Ω₅^{Spin-Z₄} = Z₁₆ (Tachikawa–Yonekura; García-Etxebarria–Montero; Hsieh), and the vanishing anomaly of the Spin(10) 16 on Spin×_{Z₂}Spin(10) manifolds (García-Etxebarria–Montero 2018; Wang–Wen–Witten). I recall the same values; neither was fetched.
   - Scope: it covers Z₂³ only. It does not cover point-group anomalies or anomalies of the full Z³ translations.
   - The extension to X2 holds, because each X2 corner carries one full 16 (32 modes per site; `combos/X2/COMBO_REPORT.md:252`).
2. **No texture escape: true, but the stated reason is slightly off** (`REPORT.md:55`).
   - The real reason: X2′'s observable speeds are mass-basis diagonals of κ(H_u+H_d), so they are fixed by masses and CKM alone (C3 check, 1e-47). OBS-3's escape needed kinetic terms that are diagonal in the corner basis (`OBS3/REPORT.md:76-87`), which X2′ does not have.
   - "A zero needs a permutation CKM" is right only for a zero of the whole Q flavour pattern ([H_u,H_d] = 0). For the clean rows, a zero is one real equation, and PDG data violate it: the spread is 7.5e-5·κ.
   - The case of flavour-dependent vertex symbols is excluded by defining zeros as "kernel-independent", not by a proof.
3. **The n count is wrong under variant B.**
   - "H_u alone leaves ×1e11–1e12" (`REPORT.md:64`, `assembly.out:10`) comes from fixing that coefficient at −κ (`gen1_assembly.py:139`).
   - With the coefficient free, H_u alone at 0.9997·(−κ) brings the worst ratio to ≤ 4e-34, and H_d alone at −3320·(−κ) works too (my check).
   - So the two-sided count is **n = 1**. TESTS.md:716 ("2 covariant counterterms") and GEN-2's comparator "GEN-1's n = 2" both become 1. The tuning figure of about 3e-16 is unchanged.
4. **The clean-row count understates what the data require.**
   - After the per-field counterterms, the three neutrino eigenstates still differ in speed by about 1e-7. Heavy rows remain too: s at 2e-5, b and t at about 1e-2 (`assembly.out:15`).
   - Neutrino-oscillation and neutral-meson Lorentz-violation bounds (recalled) would force at least H_e on L. All of this stays within n_all ≤ 8, so the reading is unaffected.
5. **The variant-A loophole should not be credited.** Its n = 0 needs the d quark to be subluminal by 0.6–8.7e-7. That gives nucleons isotropic c-coefficients of order 1e-7, far above the clock-comparison bounds (about 1e-11, recalled). Treat variant A as "no pass".
6. **Comparator overclaim (`REPORT.md:77` against `:84`).**
   - "Class S: not needed" is literally true, but side finding 2 shows that an on-site, flavour-dependent energy offset (a dimension-3 term) is allowed by every symmetry of X2′.
   - That is the same structure CLS-1 priced at ×4e42 without Θ (`CLS1/REPORT.md:98,107`).
   - So X2′ still needs Θ, or tuning of about 1e-40. The supervisor reading should add this price.

**Strongest correct statement:** Putting 3×16 at Γ as an internal label frees CKM, keeps tree-level ΔF = 2 at the SM's, and removes the first-order strain channel. Z₁₆ forces ν_R, and the mixed Z₂³ anomaly vanishes, given the recalled bordism values. The price has two parts:
- one-loop flavour-pattern Lorentz violation at 1e14–1e15 × the clean rows, removed by 1 (clean rows) to 8 (all one-loop terms) flavour-covariant counterterms, each tuned to about 3e-16 and needed again at every loop order;
- a dimension-3 flavour-offset structure that needs Θ, exactly as in CLS-1.

---

## LOCK-1: CONFIRMED WITH CORRECTIONS (same-family referee)

**Correct fixed reading:** LOCK-MIXED, for the record gas. The family inventory needs correcting (item 2).

**Key findings**
1. **The record gas Monte Carlo checks out.**
   - The classification is consistent: 147 peaks at (π,π,π), 54 at the smallest k, and 5 frozen domains (`runs/archive.out`).
   - Exact enumeration agrees with the MC (`validate2.out`).
   - g_N(1/2) sits between 0.41 and 0.42, matching e^{−4K_c} = 0.412 (`runs/F4.out`).
   - The hard-core edge of about 0.21 matches the literature value ρ_c ≈ 0.214 (recalled).
   - The g_N values are brackets from noisy Binder curves; the L = 24 points are non-monotone (`F2.out`, `F4.out`).
   - Block 117's g ≤ 9/62500 is verified on main (`…NINE_OVER_62500…md`, T5).
2. **"Only landed family that orders matter" is not supported** (`REPORT.md:7`, TESTS.md:765). The PREREG prior-art list (`PREREG.md:14-18`) misses landed admissibility notes on period-2 bond structure:
   - `…BOND_RATES_ALTERNATE_ON_THEIR_OWN_BELOW_A_THRESHOLD_STIFFNESS…2026-09-22.md` (T3): the filled sea makes the uniform bond rates unstable to alternation below κ = χ/12. This is within a supplied ansatz only.
   - `…TWO_INSTABILITIES_OF_THE_UNIFORM_BOND_RATES…`: the alternation breaks translation below a threshold set by α+2β.
   - `…WHAT_CAN_GAP_THE_WALK…` (T2/T3): every rest energy main gives the walker comes from a chessboard, axis stripes, or alternating bonds.
   - `…A_CHESSBOARD_RECORD_BACKGROUND_IS_FELT_ONLY_AS_A_REST_MASS…` (T1): a chessboard gaps the free walk.
   - With all three axes alternating, the remaining translations are 2Z³, which folds all 8 corners (index 0; my check).
   - These are conditional supplied models, but they are in scope ("admissibility rules"). Main's preferred values are safe only for the record gas (TESTS.md:768); for bond rates, I did not find where main's coefficients sit relative to the threshold.
3. **The supervisor reading (TESTS.md:771) gets the index assignment right.**
   - Walker chirality is (−1)^{hw} (`chk_fold.py`). So Γ carries +3 per component and (π,π,π) carries −3.
   - Only (π,π,π) folds onto Γ under FCC, so the folded index is 0.
   - The staggered ψ†ψ mass is a Spin(10), Z₄^F and gauge singlet, and a free walker plus mε has min|E| = m exactly.
4. **The reading's conclusion is overclaimed.**
   - What is lost is the symmetry protection: L1 and L2 no longer hold.
   - With an SMG-gapped hw3 mirror, mixing at the level of a bilinear term produces no gap, because the mirror's propagator vanishes at zero energy (CLS-1; `GEN2/REPORT.md:57-58`). A gap needs V ≳ Δ or non-perturbative effects, so it is OPEN.
   - The light 3×16 carries no internal anomaly, so nothing forbids an eventual gap either.
   - "Survive at g ≥ 1" means only "no folding". Main defines no coupling between records and fermions.

**Strongest correct statement:** The landed record gas locks into a period-2 chessboard only for g < g_N(ρ) and ρ ≳ 0.21. It is liquid or clumped (period 1) at main's g = 1 and through the RP range, and no odd period appears. Main's bond-rate notes contain a conditional period-2 instability. A chessboard removes X2′'s protection by symmetry; it does not prove that the light sector gaps.

---

## GEN-2: CONFIRMED WITH CORRECTIONS (same-family referee; symmetry level)

**Correct fixed reading:** DIR-PRICE, at symmetry level. It is conditional on c1 (no three-orientation cell law has been built; `REPORT.md:27`) and c5 (heavy flavon, spectrum not computed). The PRICE trigger, "n exceeds GEN-1's", is suggested, not proved.

**Key findings**
1. **Circulant ⇒ trivial CKM is correct.** Circulants are diagonalised together by the 3×3 discrete Fourier transform (`symm.out:2-4`), and the E part is orthogonal to the circulants, so the first-order Eg response vanishes (`symm.out:5-6`).
   - Sharper version: full O_h invariance gives Y = a·1 + b·J, which has a degenerate pair, so the masses fail before CKM does. Non-degenerate circulants need O broken to T or C3. Realistic masses plus CKM need Eg.
   - A tree-level Eg strain channel is symmetry-allowed (proved). Its size is not computed.
2. **"n ≥ 7" is overclaimed** (TESTS.md:746; `REPORT.md:47`).
   - Proved: 5 A1g speed structures per field (`symm.out:1`), and an Eg condensate allows first-order Eg speed couplings for every field, the photon included.
   - Not proved:
     - that each coupling exceeds its bound (sizes not computed);
     - "non-covariant": for a spontaneous flavon, the counterterm λ_f Φ_E·T_E is cubic-invariant;
     - the base value 2, which should be GEN-1's 1.
   - Defensible: n > GEN-1's (suggested, high confidence; the photon's Eg anisotropy alone would need it).
3. **c6 is correct for simple-cubic crystals.** LOCK-1's correction stands: a chessboard (FCC) folds only (π,π,π), with the same folded index of 0.

**Strongest correct statement:** If generations are rod orientations, real CKM forces an Eg order. That order makes tree-level strain couplings and first-order anisotropic speed terms for every field symmetry-allowed. These are prices GEN-1 does not pay, so the internal label is the better placement at symmetry level; the sizes are not computed.