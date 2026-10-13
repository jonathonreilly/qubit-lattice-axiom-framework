# C5 R19-27 report: V1's enthalpy gap. Does a growing-spacing lattice have a receiver for the vacuum enthalpy mismatch, or is V1 excluded by history?

- **Worker:** Claude Opus 5.5 (Claude Code agent; same model family as the supervisor and every C5 worker). Started 06:41Z, report about 07:25Z, 2026-10-13. Unrefereed. No repository file was edited. Nothing was downloaded.
- **Item:** `TESTS:8436-8460` (FIXED readings `:8456-8459`; expectation `:8460`).
- **Paths.** `TESTS` = `.claude/science/exercises/gravity-current-state-20261009/TESTS.md`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`. `rX` / `vX` / `fX` = `agents/C5_X_report.md` / `agents/C5_X_referee_verdict.md` / `agents/C5_X_referee.md` (full referee text) in that packet. `S/` = `scratchpad/C5/R19-27/` (scripts and `.out` in `S/scripts/`; runner rechecks in `S/recheck/`).
- **Machine use.** `OMP_NUM_THREADS=2`. Every run took under 70 s; most under 2 s.
- **Labels.** proved (a complete short argument under the stated hypotheses; unrefereed) / checked (sympy or numerics run here) / suggested / reading / comparator. RECALLED = from memory, not verified this run.

---

## 0. Reading against the FIXED readings: **V1-RECEIVER (worker)**, in a stated class 𝒱_ct, with the caveats in §6

**The class 𝒱_ct (stated before the title).**
- R19-17's class 𝒱: V1 with comoving frame fields X^I, H-cov, constant physical masses, linear FRW perturbations with cold dust (`rR19-17:14-19`; refereed conditional, `vR19-17:1-9`).
- (S_ad) for the lowest state (P-r1914a / P-r1917a). N_red and W1 as registered.
- R19-21's Born–Oppenheimer hypothesis BO: lattice-scale modes see the IR fields (Higgs condensate, thermal fluctuations) as local backgrounds (`rR19-21:120-128`).
- R19-21's H-cov dilation: the sea at a new spacing is the same law (`rR19-21:216`).
- **The added completion datum (priced, P-R19-27a).** The Higgs-sector counterterms are local terms of the law, written per site. They are fixed numbers in lattice units, so H-cov dilation carries them with the sea. They are polynomial of degree ≤ 4 in the Higgs field (the renormalizable basis). Their logarithmic part follows the line of constant physics (LCP): v, m_H, λ₃ and λ₄ stay fixed in physical units as the spacing grows.

**What is shown.**
- **(i) Lemma E (proved; checked).** For any isotropic H-cov vacuum term −∫√−g F(n, φ) with site density n, the metric stress is T = −F g + n∂_nF h. So ρ = F, p = n∂_nF − F, and **W = n∂_nF** (`S/scripts/r1927_identities.out:1,3`).
- **(ii) Lemma X0 (proved; checked).** u^μ∂_μX^I = 0, so the lattice frame (reading W or A) can take only the momentum leg of an enthalpy, never the energy leg Wθ (`:2`).
- **(iii) Lemma D (proved; checked).** On V1, ρ̇ + 3HW = F_φφ̇ identically (`:4`). The energy leg of any H-cov enthalpy is received by that term's own drift with the site density.
- **(iv) Corollary (proved, from E and D).** On V1 a state-dependent enthalpy is exactly a drift of the effective potential:

  ΔW(φ) = n∂_n[F(n, φ) − F(n, v)] = −(1/3) ∂_{ln a}ΔV(φ).

  A "pure pressure" with fixed energy cannot persist on V1: ρ̇_state = −3HW_state.
- **(v) Theorem R (proved under 𝒱_ct; checked).**
  - The sea's mass-dependence splits into powers ε_k(mℓ)^k/ℓ⁴ ∝ n^{(4−k)/3}.
  - A per-site counterterm with fixed lattice-unit coefficient c_k has the same n-scaling, so its own pressure cancels the sea's term by term: W_k = ((4−k)/3)(ε_k + c_k)m^k n^{(4−k)/3}.
  - The constancy of v, m_H, λ₃ and λ₄ for all n forces c_k = −ε_k for k = 1, 2, 3 (the powers n^{(4−k)/3} are linearly independent) and fixes the φ⁴ log n term.
  - Hence ΔW_state(φ) = O(φ⁵ℓ) for every state in BO: symmetric phase, thermal, and matter-shifted.
  - The registered mismatch (R19-21: ΔW = 3.04e-17 per cell = 2.7e106 ρ_Λ) is the **Lorentz-invariant counterterm** value. With per-site counterterms it is 0 through k = 3. Even without the log-level LCP it is only the electroweak-scale m⁴/(24π²) per Dirac field (`r1927_lcp_enthalpy.out:28-30`).
- **(vi) No signalling (proved by reduction to R19-17's class).**
  - Under 𝒱_ct the state-dependent vacuum is −ΔV_phys(φ)g, which is Lorentz-invariant and conserved with φ's own stress.
  - Its force on the lattice is zero (`r1927_identities.out:5`), so R19-17's Corollary B condition F_I = 0 is unchanged (`rR19-17:122-128`).
  - The linear gravitating equations are GR plus standard fields. The Lemma-S jump is the GR control (`fR19-17:29`, counted once).
- **(vii) The Lorentz-invariant counterterm scheme is not admissible on V1 (checked arithmetic; bounds RECALLED; a no-go-type statement that needs a referee if recorded).**
  - Fixed physical-unit counterterms cancel the Wilson Higgs tadpole at one instant only. The vev then drifts by |d ln v/d ln a| = 2.1e51 per e-fold at ℓ = ℓ_P, and 1.2e3 at ℓ = (1 TeV)⁻¹ (`r1927_lcp_enthalpy.out:31-33`).
  - Clock-level stability needs ℓ > 1.9e-16 m (`:34`), which is excluded by collider resolution (RECALLED).
  - So the LI scheme violates 𝒱's own constant-mass hypothesis. It lies outside 𝒱, and within 𝒱 the per-site scheme is forced.

**Against the readings (`TESTS:8456-8459`).**
- **V1-RECEIVER:**
  - **"a stated V1 mechanism":** the per-site (H-cov-dilated) counterterms. Their pressure is the receiver, and V1's site-density dependence is what makes it work.
  - **"absorbs the enthalpy mismatch":** it cancels exactly, power by power (k ≤ 3), and the log term is fixed by the LCP.
  - **"no number":** no number beyond the Higgs-sector counterterms. Those are needed in any arena, and R19-20 already lists them as a matter-sector tuning missing from the bill (`rR19-20:231`); count them once there.
  - **"no signalling":** (vi).
  - **"Checked":** the sympy identities, the D1 root-edge sums and the NN Hartree thermal channel (§3).
- **V1-EXCLUDED:** not met. The class 𝒱_ct leaves no Planckian mismatch.
- **OPEN:** the reading if a referee rules that the per-site counterterm is a restatement that "removes" rather than "absorbs" the mismatch. See §6.

**Against the expectation (`TESTS:8460`).**
- "V1-RECEIVER": **borne out.**
- "under reading A: the frame's zero-inertia constraint becomes a carrier": **not borne out as a mechanism.**
  - The frame cannot take the energy leg Wθ (Lemma X0).
  - Under reading A it can absorb the momentum leg of an LI-scheme enthalpy, by compressing the lattice: δn = −9c₁δm n̄^{2/3}/(4A) (`r1927_identities.out:8`). That is harmless (δn/n ~ (mℓ)(δv/v)), but it leaves the energy leg to the potential's drift.
  - The working receiver is the counterterm, under either reading W or A.

---

## 1. Plain words

- **Where the gap came from.** The lattice's lowest state pushes outward differently from how it weighs. When the Higgs field changes (before the electroweak crossover, in hot plasma, near matter), the push changes by a Planck-sized amount. Earlier probes (R19-20, R19-21) assumed that the corrections which keep the Higgs field's energy sensible are fixed in ordinary physical units. With that assumption the extra push is left over, and on a stretching lattice nothing soaks it up.
- **What a stretching lattice changes.** On V1 the number of sites is fixed and they spread apart. For anything whose energy is "so much per site", the pressure is exactly how its energy changes as the sites spread. So the leftover push is the rate at which the Higgs field's energy curve drifts as the universe expands. A push with no drift is impossible.
- **Why the drift is already excluded.** If the corrections were fixed in physical units while the lattice stretched, they would stop matching the lattice's own contributions within about 1e-33 s at Planck spacing. The Higgs field would then be thrown far from its observed value. Particle masses would drift, which atomic clocks forbid, at any lattice spacing small enough to escape colliders. So on V1 the corrections must be written per site, as fixed numbers in lattice units, just like the lattice's own contributions they cancel.
- **What happens then.** Written per site, each correction carries exactly the opposite push to the piece of the lattice sea it cancels. The Planck-sized push disappears for every state: hot, symmetric, or near matter. What is left is ordinary electroweak physics, which gravitates as in GR.
- **What it costs.** No new number. The corrections were needed anyway. The law must be written per site, and its logarithmic running must track the growing spacing. That second requirement is forced for other reasons too: without it the fine-structure constant and the proton mass would drift with the expansion.

---

## 2. Hypotheses, class and exclusions (stated before titles)

- **𝒱** (`rR19-17:14-19`; `vR19-17:3,5`): V1, comoving X^I, the law diffeomorphism-invariant as a functional of (g, X, fields), constant physical masses, linear FRW + cold dust. This item extends 𝒱 with Higgs–Yukawa content.
- **BO and H-cov dilation:** as R19-21 (`rR19-21:120-128,216`). ε(n, m) = n^{4/3}e(m n^{−1/3}) per field, with e(μ) the lattice-unit cell energy.
- **Counterterm forms compared.**
  - **(LI):** ∫√−g V_ct(φ), fixed in physical units. This is the implicit form behind "to first order the total energy is stationary, so ΔW appears as a pure pressure" (`rR19-21:230-231`).
  - **(site):** ∫√−g Σ_k c_k n^{(4−k)/3}m(φ)^k, with c_k fixed lattice-unit numbers (k ≤ 3, plus a φ⁴ log n term for k = 4).
- **LCP (Higgs sector):** v, m_H, λ₃ and λ₄ are fixed in physical units as n changes.
- **Excluded or not covered:**
  - the anisotropic (shear, T₂g) vacuum response. Lemma E is isotropic, so R19-21's shear channels are untouched;
  - gauge-field and fermion thermal cross terms beyond R19-21's argument;
  - the non-perturbative crossover;
  - nonlinear Bianchi;
  - site creation (the removed hypothesis is "site creation as the only receiver").

---

## 3. Results

### 3(a) Can the lattice frame or the spacing evolution absorb an isotropic enthalpy, and at what cost?

**Lemma E (stress of an isotropic H-cov term; proved, checked).**
- Take Γ = −∫√−g F(n, φ), with n = √det b and b^{IJ} = g^{μν}∂_μX^I∂_νX^J.
- Then δn/δg^{μν} = ½ n (b⁻¹)_{IJ}∂_μX^I∂_νX^J = ½ n h_μν, so T_μν = −F g_μν + n∂_nF h_μν.
- Checked at a random Lorentzian point by finite-difference metric variation: residual 2.5e-9 on a scale of 18. Also checked: ρ = F, p = n∂_nF − F, W = n∂_nF to 9 digits, and h = g + uu (`r1927_identities.out:1-3`).
- **This generalizes R19-21's p = (e − me′)/3** (`rR19-21:216`). Each power μ^k carries W_k = ((4−k)/3)ρ_k (`r1927_lcp_enthalpy.out:7`); R19-21's twisted dW/dm² = (2/3)e₂ is the k = 2 case.

**Lemma X0 (the frame cannot take the energy leg; proved, checked).**
- u ∝ ε^{μνρσ}∂_νX^1∂_ρX^2∂_σX^3 gives u^μ∂_μX^I = 0 (`r1927_identities.out:2`).
- Lemma N's source term E_I∇^νX^I (`rR19-17:115-117`; `fR19-17:21`) therefore has no u-component.
- The frame, under either reading W or A, can receive only spatial (momentum) legs D_iW + W a_i. It can never receive the energy leg Wθ = 3HW that an isotropic enthalpy carries in an expanding universe.
- **This is (d-i)'s structure seen from V1.** In C-box-E the energy leg goes to site creation (`vR17-11:5-15`). On V1 there is no creation, and the frame cannot take it.

**Lemma D (the energy leg on V1 is the term's own drift; proved, sympy).**
- With n = n₀a⁻³: ρ̇ + 3H(ρ + p) − F_φφ̇ = 0 identically (`r1927_identities.out:4`).
- So any H-cov isotropic vacuum term is conserved on V1 (with φ on shell). Its enthalpy is paid by ρ̇ = −3HW.
- **Corollary (proved).** For the state-dependent part ΔF = F(n, φ) − F(n, v): ΔW = n∂_nΔF = −(1/3)∂_{ln a}ΔF.
- R19-21's "pure pressure" (Δρ = 0, ΔW ≠ 0; `rR19-21:230-231`) holds on V1 at one instant only. The next instant the state-dependent energy has drifted by −3HΔW dt.

**Force on the lattice (proved, sympy; static, flat, 1D strain).**
- E_1 = d/dx[F_n] (`r1927_identities.out:5-7`).
  - LCP form F₀(n) + ΔV(φ): E_1 = 0.
  - LI form F₀(n) + c₁n m(φ) + V_ct(φ): E_1 = c₁m′φ′ = ∂_xW_state.
- Under reading W that force breaks Bianchi at linear order around inhomogeneous matter (Corollary B, `rR19-17:122-128`).
- Under reading A, F_I = 0 is solved by a lattice compression δn = −9c₁δm n̄^{2/3}/(4A) (`:8`), of relative size (mℓ)(δv/v). That is negligible, but it handles only the momentum leg.

**Theorem R (per-site counterterms remove the state-dependent enthalpy; proved under 𝒱_ct).**
- Write F(n, φ) = ε(n, m(φ)) + C(n, φ) + V_phys-like terms, with C local and polynomial of degree ≤ 4 in φ.
- The sea's φ-dependence is Σ_{k=1}^{3} ε_k n^{(4−k)/3}m^k − (1/8π²)m⁴ log(m n^{−1/3}) + O(m⁵n^{−1/3}). The m⁴ log comparator is RECALLED; it is checked approximately below.
- Require v, m_H, λ₃ and λ₄ to be n-independent. The coefficients of the Taylor polynomial at v are then n-independent. The functions n^{(4−k)/3} (k = 1, 2, 3) and log n are linearly independent, so each sea term must be cancelled by a counterterm with the same n-power: c_k = −ε_k, plus a λ-running term ∝ φ⁴ log n.
- That is exactly the per-site form with fixed lattice-unit numbers. F(n, φ) − F(n, v) is then n-independent up to O(φ⁵ℓ). By Lemma E, ΔW_state = O(φ⁵ℓ) ~ v⁴(vℓ).
- **Thermal and BO states.** The counterterm is an operator. ⟨c₂n^{2/3}y²|φ|²⟩ cancels the sea's ⟨ε₂n^{2/3}y²|φ|²⟩ in any state, so R19-21's channel F has no Planckian isotropic enthalpy either.

**Numerical checks (checked).**
- **D1 root edge, Taylor coefficients** (`r1927_lcp_enthalpy.out:3-6`):
  - e₀ = −3.2055621 and ε₁ = −0.6923204 reproduce R19-21's values;
  - ε₂ = −0.55873 and ε₃ = +0.130947 are stable over N = 64–128.
  - W vanishes for |k| < b_f, so the IR is pure Dirac and ε₁₋₃ are IR-finite.
- **Finite-difference enthalpy in n, computed from lattice sums at μ = m n^{−1/3}** (`:10-19`):
  - The LI scheme gives W_LI = ε₁m + (2/3)ε₂m² + (1/3)ε₃m³ + O(m⁴) (`:15-18`), with ρ_state ≈ O(m⁴) at the tuning instant: the "pure pressure".
  - The per-site scheme leaves W_site/W_LI = −5.3e-7 at mℓ₀ = 0.05, scaling as m^{3.2} (expected μ³ × log).
- **The remainder is CW-like** (`r1927_cw_fit.out:1-3`): the fitted log coefficient is A = −0.0128 to −0.0136, against the continuum −1/(8π²) = −0.01267 (RECALLED). It agrees to 1–7%, not converged in N. This is an approximate check only.
  - The remainder's n-scaling is n⁰ up to the log, so its enthalpy is m⁴/(24π²) per Dirac field (log level). The per-site W at mℓ₀ = 0.05 (+1.9e-8) is consistent with this to within the IR resolution.
- **NN λφ⁴ at O(λ), thermal cross channel (isotropic analogue of R19-21's F)** (`r1927_nn_thermal_enthalpy.out:3-10`):
  - LI scheme: W_x = (λ/6)G_th g_vac(0)/ℓ², matched to 1e-4–5e-3. At T_c with ℓ = ℓ_P and λ = 1 that is 5.3e29 ρ_rad(T_c).
  - Per-site scheme: residual ratio 3e-5 to 4e-3, scaling as (mℓ)^{2.4}. That is the log running of the mass, which LI-type terms and the LCP remove.

**Answer to (a).**
- **The lattice frame (W or A):** no, for the energy leg (Lemma X0). Under A it takes the momentum leg at negligible cost.
- **The spacing evolution:** it always carries the energy leg, through the term's own drift (Lemma D). That drift is a drift of the effective potential, so it is observable unless the state-dependent W vanishes.
- **What works:** per-site counterterms. They are forced in 𝒱 by constant masses (Theorem R), and make the state-dependent W vanish with no new number and no signalling.

### 3(b) Sizes against bounds

**Per-site scheme, LCP imposed:** ΔW_state = 0 through k = 3 and at the log level. The residual is ~v⁴(vℓ).

**Per-site scheme, LCP imposed only to the precision allowed by drift bounds.** By the Corollary, |ΔW| ≤ (1/3)|∂_{ln a}ΔV|.
- **Symmetric phase.** ΔV_EW = λv⁴/4 ≈ 1.2e8 GeV⁴ ≈ 5e-3 ρ_rad(T_c). With |d ln v/d ln a| ≲ 5e-4 (a BBN-level 1% over about 20 e-folds, RECALLED), ΔW ≲ 1e5 GeV⁴ ≈ 4e-6 ρ_rad(T_c) (arithmetic).
- **Today, in matter.** ΔW ≲ f_N ρ_m |d ln v/d ln a| ≈ 0.3 × 1.4e-6 ρ_m ≈ 4e-7 ρ_m, using the clock bound |μ̇/μ| ≲ 1e-16/yr over H₀ (RECALLED). Compare R19-21's LI value of 2.1e50 ρ_m (`rR19-21:228`).
- **If the log-level LCP is dropped** (bare dimensionless couplings fixed in lattice units):
  - W₄ = Σn m⁴/(24π²) = 1.1e7 GeV⁴ = 5e-4 ρ_rad(T_c) (`r1927_lcp_enthalpy.out:29-30`). That is gravitationally harmless.
  - But the same choice makes couplings drift, which observation already excludes (suggested): the proton mass is lattice-native through Λ_QCD ∝ 1/ℓ (counted once with G0-c, `rR19-14:70-74`), and α runs by ~α|b|/2π per e-fold, ~1e-13/yr against ~1e-17/yr (RECALLED).

**LI scheme (for comparison; it is outside 𝒱).**
- R19-21's numbers stand, counted once (`rR19-21:223-228`).
- The decisive bound is the vev drift, 2.1e51 per e-fold at ℓ_P (`r1927_lcp_enthalpy.out:31`). With ℓ = ℓ_P and H₀ ≈ 1.2e-61 t_P⁻¹, the tadpole stays cancelled to m_H²v accuracy for only about 1e10 t_P ≈ 5e-34 s (arithmetic).

### 3(c) Prices (named, none adopted)

- **P-R19-27a (new): per-site counterterms and the Higgs-sector LCP on V1.**
  - Wording: "The law's Higgs-sector counterterms are per-site terms with fixed lattice-unit coefficients, and its logarithmic running follows the line of constant physics in the local spacing."
  - **0 new numbers.** The counterterm values are R19-20's suggested missing matter-sector tuning (`rR19-20:231`), counted once there. Under the counting rule (`TESTS:5700`) the basis is one counterterm per Higgs-potential power k = 1–3, shared by all species, plus the λ₄ running fixed by its β-function. Twisted edges need only k = 2.
  - Enforced or stipulated: stipulated as law data. The form (per site) is enforced within 𝒱 by constant masses (Theorem R). Its radiative stability is that of the SM Higgs counterterms, with no new instability.
  - Text touched:
    - `AX:57-58` ("one fixed … rule": the rule is fixed as a functional of the local spacing);
    - `AX:189-190` (scale reference; counted once with P-r1914c, of which the log-level LCP is the dimensionless-coupling extension).
- **Inherited, counted once:**
  - P-r1914a / P-r1917a ((S_ad));
  - P-r1917b (H-cov);
  - P-r1917c (frame law W or A; Theorem R works under both);
  - P-r1914c;
  - N_red;
  - W1;
  - P93.
- **No axiom text changes.**

---

## 4. Prior art (each counted once)

- **R19-21 §3.5** (`rR19-21:214-235`; worker, referee running) and **R19-20 row 3** (`rR19-20:231`): ΔW = (4e − me′)/3, the D1 value, "(d-i) absorbs it; on V1 nothing does" (`TESTS:8429`, `:8263`).
  - Reproduced: ε₁ = −0.6923204 and ΔW = 3.043e-17.
  - New here: the counterterm form decides it. On V1 the LI form is inadmissible, and the per-site form cancels it.
- **R19-21's own NN mechanism model already uses the per-site form.** Its mass counterterm is an on-site law datum fixed in lattice units, m_b² = m_p² − (λ/2)G_vac(0; m_p) (`scripts/C5/R19-21/r1921_nn_thermal.py:3`). The LI form enters only through the enthalpy addendum's "the total energy is stationary" step (`rR19-21:230-231`).
- **R19-20's "Planckian Higgs tadpole"** (`rR19-20:231`; `rR19-21:195-197`): the same counterterm, priced there as missing from the bill. Here its V1 form is fixed.
- **R17-11 and its verdict** (`vR17-11:5-23,44-45`): Q = ∇(Wh) with energy leg Wθ received by creation, and the free spatial trace as a postulate. Lemma X0 shows why V1's frame cannot replace creation as receiver of Wθ.
- **R19-14 and its verdict** (`rR19-14:85-90,121`; `fR19-14:11`): the V1 vacuum fluid is separately conserved, and "the receiver of W is e₀'s own drift". Lemma D generalizes that to state-dependent terms. G0-c is counted once for the LCP's mass side.
- **R19-17 and its verdict** (`rR19-17:115-133`; `fR19-17:21,29,31`): Lemma N, Corollary B, readings W and A, and the linear GR control.
- **R12-2, R11-3:** not re-derived (V1 SOURCED; L-CR).
- **Comparators (RECALLED):**
  - the Coleman–Weinberg potential with a cutoff;
  - lattice "lines of constant physics" (bare couplings tuned with the spacing; critical-mass tuning for Wilson fermions);
  - the thermodynamic identity p = n²∂_n(ε/n);
  - atomic-clock and BBN bounds on varying constants;
  - collider resolution of contact interactions.

## 5. Archived runners rechecked (before relying on them)

- All 17 archived runners of R19-14 (2), R19-17 (7), R19-21 (4) and R17-11 (4) were copied to `S/recheck/` and rerun there.
- **All reproduce their stored outputs** (`S/recheck/recheck_summary.out`). The only differences are two elapsed-time labels in `r1917_dynamic_lump.out` (lines 3 and 14).
- **Archive defect (report to the coordinator).** `scripts/C5/R19-21/r1921_enthalpy.py:9` imports `dirac` from `../arch/R18-5`, a path that does not exist in the archive. The file lives at `scripts/C5/R18-5/dirac.py`.
  - I reproduced the run by copying `scripts/C5/R18-5/*.py` to `S/recheck/arch/R18-5/`. These copies are identical to R19-21's own `arch` copies (`dirac.py` and `sublum.py` diff clean).
  - This is the same kind of fix as the R17-7 import repair (`TESTS:6625`).

## 6. Scope and strong words

- **"proved"** is used for:
  - Lemma E;
  - Lemma X0;
  - Lemma D and its Corollary;
  - the force-on-lattice expressions;
  - Theorem R (under 𝒱_ct: BO, H-cov dilation, renormalizable local counterterms, LCP).

  All are short and unrefereed.
- **"checked"** is used for:
  - the sympy and numeric identity checks;
  - the D1 sums and the finite-difference enthalpies;
  - the NN Hartree thermal cross channel;
  - the CW log, approximately (to 1–7%, not converged).
- **The literal question for a referee: "absorbs" versus "does not arise".** The per-site counterterm is a stress term whose pressure equals −ΔW_sea power by power. I read that as absorbing, on the letter. A referee may instead read Theorem R as showing that the registered mismatch presupposed an inadmissible LI scheme. Then the honest summary is "V1 has no enthalpy gap in 𝒱_ct", and the literal reading might be judged OPEN, with no V1-EXCLUDED content.
- **"no number"** means no number beyond the Higgs-sector counterterms that any arena needs (R19-20's suggested missing tuning). It does not mean that the Higgs sector is untuned.
- **"forced"** (per-site form) means: within H-cov local polynomial counterterms, given constant v, m_H, λ₃ and λ₄. Non-local or clock-dependent counterterms are outside the class. An extra dilaton-like field that tracks n is not considered.
- **"excluded" (LI scheme)** rests on BO, the D1 ε₁, and RECALLED clock and collider bounds. It is a no-go-type statement: it needs the referee before being recorded as one.
- **Not covered:**
  - the shear and T₂g channels (Lemma E is isotropic; R19-21's (S_loc) or per-link counterterms would be needed; suggested);
  - full SM gauge and Yukawa operator mixing in the LCP;
  - nonlinear Bianchi;
  - the non-perturbative crossover;
  - order-2 state dependence. The induced-G piece linear in mℓ shifts G by ~mℓ ~ 1e-17 between phases (suggested; far below BBN's ΔG/G).
- **Side remark for R19-20 and R19-21's referees (suggested).** The one-point enthalpy mismatch depends on the counterterm scheme in C-box-E too. With per-site counterterms the state-dependent W vanishes there as well, so (d-i) would be needed only for the lowest state's W₀ (R17-11's original role).

## 7. For a referee (optional; no FAIL claimed, but §0(vii) is no-go-type)

1. Lemma E and Theorem R: is the linear-independence step (n^{(4−k)/3}, log n) sound for the stated counterterm class? Is the LCP (constant v, m_H, λ₃, λ₄) a fair reading of 𝒱's constant-mass hypothesis?
2. Is "per-site counterterm" an admissible completion of 𝒱, or a restatement (literal-first)?
3. The LI-scheme exclusion: the vev-drift arithmetic, and the collider and clock inputs (RECALLED).
4. Whether "absorbs" is met (§6).

## 8. Files (`S/`)

- `scripts/r1927_identities.py` → `.out`: Lemma E (numeric metric variation), Lemma X0, Lemma D (sympy), force on the lattice, reading-A compression.
- `scripts/r1927_lcp_enthalpy.py` → `.out`: D1 root-edge ε₁–ε₃; finite-difference enthalpy in n for the sea, LI and per-site schemes; the remainder; physical sizes; LI vev drift.
- `scripts/r1927_cw_fit.py` → `.out`: the CW-log coefficient of the per-site remainder (N = 128–256).
- `scripts/r1927_nn_thermal_enthalpy.py` → `.out`: the NN λφ⁴ O(λ) thermal cross-channel enthalpy in both schemes.
- `recheck/run_rechecks.py` → `recheck_summary.out`, with the copies, `.rerun` files, `stored/` originals and `arch/R18-5` (the path fix).
