# C5 R19-21 report: the state-tied subtraction across cosmic history. Do (S\*) and (S\*\*) survive the electroweak crossover and a thermal plasma?

**Author and provenance.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. Run 2026-10-13, 06:10Z to about 06:45Z. I edited no repository file and downloaded nothing.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `S/` = `scratchpad/C5/R19-21/` (this folder; scripts and `.out` in `S/run/`, archived-runner copies in `S/arch/`, rechecks in `S/recheck/`).

**Machine use.** `OMP_NUM_THREADS=2`; load 6 to 9 from other jobs; every run under 10 s.

**What I read.** `AX` in full. `P/TESTS.md`: the C5 method (`:2302-2319`); my item (`:8144-8173`); the R14-3 entry and verdict (`:4830-4844`, `:4915-4923`); R17-7 (`:6020-6047`, worker `:6129-6140`, verdict `:6297-6312`); R18-2 (`:6475-6500`, `:6614-6625`, verdict `:6806-6815`); R17-11's verdict (`:6590-6600`); R19-11 (`:7628-7651`, `:7811-7822`, verdict `:7986-7994`); R19-15 (verdict `:7995-8006`); R19-17 (`:8117-8130`); R19-19 (`:8008-8046`, worker `:8131-8142`). `P/agents/`: `C5_R19-19_report.md` in full (its §3.6 is the item-10 risk sent to its referee, `scratchpad/C5/ref_R19-19/REFEREE_PROMPT.md` item 4; that referee had not returned when I finished); `C5_R19-15_report.md` and its verdict in full; `C5_R19-17_report.md` in full; `C5_R19-11_report.md:1-276` and its verdict; `C5_R17-7_referee_verdict.md` in full; `C4_W2_report.md:191`; `C5_R19-20_report.md:231` (the coordinator's addendum request); `P/PRICE_NOTE.md:20-24`.

**Runners rechecked before use (checked; `S/recheck/recheck_summary.out`).** Copies in `S/arch/`, rerun there:
- R19-11 `twfit.py` and `fitres.py` (root-0 dense): identical.
- R19-15 `r1915_b_cubic.py` and `r1915_d_hartree.py`: identical.
- R19-19 `r1919_bounds.py`: identical.
- R14-3 `calib.py`: identical.
- R16-13 `validate.py` (NN μ_E = +1.9703886419e-3, the Dirac Ξ control): identical except its `elapsed` line.
- My scripts also reproduce R19-11's sums (Σnma = 4.3952e-17, Σn(ma)² = 6.0061e-34, scalar 2.4771e-34, vector 1.4247e-34), R19-19's Δμ (−4.6999e-19, −1.2040e-19; twisted −4.3803e-36, +2.3013e-39) and R19-20's naive-Wilson dρ/dm = −1.767029.

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics run here) / suggested (argued, not proved) / reading (interpretation) / comparator (outside reference) / RECALLED (from memory).

---

## 0. In plain words

1. **R19-19's number is right, and the problem is wider (checked from refereed coefficients).**
   - On R19-11's root edges, the symmetric phase gives Δμ = −4.70e-19 (E_g) and −1.20e-19 (T₂g) per cell. Both are tachyonic. Under the canonical reading, |m_g|/H ≈ 1.5e24 at T_c.
   - The cause is general. On the lattice the vacuum's shear stiffness depends on the particle masses (R19-11's slopes c₁, c₂). The actual state is almost never the lowest state, and anything that shifts a mass seen by the lattice-scale modes leaves an unsubtracted shear.
   - Four channels were computed:
     - **(V)** the Higgs vev shift. This is x = 0 above T_c, and a thermal shift of v(T) below T_c, all the way down to BBN.
     - **(F)** thermal Higgs fluctuations dressing the lattice sea. This is a cross term.
     - **(Q)** the plasma quasiparticles' own lattice shear.
     - **today's matter**, which shifts the Higgs vev through the Higgs–nucleon coupling.
   - (V) and (F) give |m_g| ≫ H at every temperature from 1 MeV to about 1e15 GeV (`r1921_history.out`, `r1921_bbn_signs.out`).
2. **The plasma's own physical shear does not dominate (checked).**
   - The quasiparticles' lattice shear is 0.206(Ta)⁶ per massless bosonic degree of freedom (analytic; numerics 0.19–0.20). That gives m_g²/H² ≈ 2.5e-6 at 1e16 GeV, and it falls as (Ta)². Count once with C4 W2 (`C4_W2_report.md:191`).
   - The dominant thermal piece is the cross term (F): the thermal ⟨|φ|²⟩ changes the masses that the lattice-scale sea sees.
   - The mechanism is checked in the NN λφ⁴ model by direct strain-flow Hessians. A fixed lowest-state subtraction leaves exactly (λ/4)G_th(0)G_vac″ plus the quasiparticle term. The cross term is tachyonic in E_g, zero in T₂g (Liouville), and scales as T² rather than T⁶.
3. **Every fixed-state subtraction fails under the canonical reading (worker; suggested in parts).** This covers (S\*), (S\*\*), "the instantaneous law's lowest state" (the law is fixed, so this is the same clause) and R19-17's (S_ad) (tied to the adiabatic lowest state).
   - At the root edges, both Wilson and twisted edges have a tachyonic row with |m_g|/H between 1e15 and 1e24 somewhere in [1 MeV, 1e12 GeV].
   - On free edges the sign is a law choice, with two exceptions:
     - The mass-even part flips sign at T ≈ 0.5–0.6 TeV: Δμ ∝ R₂(⟨|φ|²⟩_T − v²). So it is tachyonic on one side whatever the sign of R₂.
     - A Wilson-type law with c₁ < 0 < R₂ stays massive (r → 0, not excluded by present data). But today's intergalactic matter then gives it |m_g| ≈ 1.4e-9 eV. That is above the 100 Hz GW frequency (4.1e-13 eV) and 1e14 times the RECALLED LVK bound.
   - Avoiding all of this needs a mass-blind law: |c₁| ≲ 3e-49 and |c₂| ≲ 2e-32 of natural size for history, and 8e-29 and 4e-12 for today's IGM. In absolute terms that is |Δμ| ≲ 1.6e-67 at T_c, the item's ~1e-67 tuning.
4. **A state-tracking variant works, by construction (checked in one model; suggested for the SM).**
   - **(S_loc):** subtract the lowest state's LV strain response (the shear and LV speed rows) of the law re-evaluated at the actual state's local IR mean fields (Higgs condensate, thermal ⟨|φ|²⟩, …).
   - In the NN model it leaves only the quasiparticle term, with m_g²/H² ∝ (Ta)² (≈ 4e-6 at Ta = 0.0125, and ~4e-36 at T_c).
   - **Bianchi.** By Noether (R19-17's Lemma N extended to scalar backgrounds Φ), the shear piece's Φ-force is O(strain²). At linear order Bianchi therefore reduces to R19-17's lattice-frame condition: automatic under its reading A, and failing at O((Ta)²) for hot matter under reading W (`C5_R19-17_report.md:34,157`).
   - The isotropic enthalpy cannot be state-tracked without a carrier (vR17-7 item 3). It needs (d-i).
5. **Addendum on the one-point enthalpy mismatch (R19-20 item 3; coordinator request; checked on the root edge).**
   - On the D1 root edge, dρ/dm = −0.69232 per 4-component field (naive Wilson: −1.767) and dp/dm = 0 at m = 0 (scaling).
   - Symmetric phase: ΔW = +3.0e-17 per cell = 2.7e106 ρ_Λ, which is 2.9e49 × ρ_rad(T_c). With twisted mass: 2.4e89 ρ_Λ, which is 2.6e32 × ρ_rad.
   - At BBN (electrons only): 7.5e48 × ρ_rad. In matter today: 2.1e50 × ρ_matter, independent of density.
   - (d-i) absorbs it within R17-11's class. (S\*), (S\*\*) and (S_ad) do not. On V1 nothing registered does.
6. **Reading: HISTORY-SAFE on the letter, narrowly, for (S_loc) + (d-i) in C-box-E.** It holds by construction and is checked at O(λ) in one model.
   - The HISTORY-CONFLICT content holds for every fixed-state version (worker, conditional on the canonical reading). It goes to a referee.
   - If the referee holds that (S_loc)'s all-orders definition (a UV/IR split) is not stated sharply enough, the literal reading is **OPEN**.

---

## 1. Class, hypotheses, exclusions (stated before any title)

- **Rows and normalization.**
  - μ_E and μ_T2 are the uniform-strain Hessians of the lattice sea (Lemma H, vR19-15 item 1).
  - **Canonical reading:** m_g²a² = 16πμ. This is conditional: it is a graviton mass only for a supplied dynamical metric with a stationary background and kinetic normalization (`PRICE_NOTE.md:22`; vR19-11 item 4).
  - The alternative "μ is not a mass" reading gives no tensor consequences (§3.4).
- **Edges and coefficients (refereed, R19-11 + verdict).** Wilson-Dirac per field:
  - μ_E: c₁ = +1.06932e-2, c₂ = +6.6e-3;
  - μ_T2: c₁ = +2.73929e-3, c₂ = +2.19e-3 (`C5_R19-11_report.md:139-140`).
  - Twisted per field (`twfit.out`): μ_E c₂ = +8.5643e-3; μ_T2 c₂ = −3.8315e-6.
  - Scalar edge: μ_E c₂ = −1.3608e-3. Vector edge: μ_E c₂ = −2.9932e-3. μ_T2 = 0 for both (Liouville).
  - SM masses and bookkeeping as R19-11 (RECALLED there); a = ℓ_P, M_P = 1.22089e19 GeV.
- **Thermal inputs (RECALLED, labelled):**
  - T_c = 159.5 GeV (crossover; used only as a switch point);
  - Higgs thermal mass² ≈ 0.4T²;
  - g\*(T) step approximation;
  - H²a² = (8π/3)(π²/30)g\*(Ta)⁴.
  - Below T_c, v(T) comes from linear response to free relativistic species. This is valid for |δx| ≪ 1 and crude within ×2 near T_c; free quarks below the QCD crossover are unphysical, so BBN is also given electrons-only.
- **Matter channel inputs (RECALLED):**
  - δv/v = −f_N ρ/(v²m_H²) with f_N = 0.30;
  - Ω_b h² = 0.0224; ISM n_H ≈ 1 cm⁻³; Earth 5.5 g/cm³;
  - LVK graviton-mass bound ≈ 1.3e-23 eV.
- **Model for the mechanism check.**
  - NN lattice scalar with on-site (λ/4!)φ⁴ at first order (Hartree), in a thermal state, with R19-15's SF flow.
  - The mass counterterm is a law datum fixed in the lowest state (as `r1915_d_hartree.py`).
- **Excluded or not computed:**
  - the non-perturbative crossover region itself;
  - QCD-era hadronic shifts;
  - gauge and fermion thermal cross terms (argued small, §3.1);
  - two-loop thermal terms;
  - nonlinear Bianchi;
  - V1 site creation;
  - the root-edge off-axis rows (only μ is treated; the speed rows' thermal analogues are not computed).

## 2. Prior art (each counted once)

- **R19-19 §3.6** (`C5_R19-19_report.md:239-252`): the symmetric-phase Δμ, its tachyonic sign at the root edges, the ~1e-67 requirement. This report reproduces it and extends it.
- **R19-11 P-R19-11a** (`C5_R19-11_report.md:231-234`): "any change of the spectrum detunes" the shear; "the electroweak transition, the QCD transition and thermal masses are such changes … not computed". The channels below are that statement, computed.
- **R19-15 §0.5 / §3.4** (`C5_R19-15_report.md:63-66,291-293`): (S\*) covers the lowest state only.
- **vR19-15 item 4:** (S\*) is "a stipulated renormalization/source definition".
- **C4 W2** (`C4_W2_report.md:191`): thermal quasiparticle shear ~H²(Ta)². My channel Q is the same order, here with an exact coefficient.
- **R19-17** (`C5_R19-17_report.md:115-133,147-162`): Lemma N, readings W and A, and hot matter F_I ≠ 0 at O((ℓp)²).
- **vR17-7 item 3** (`C5_R17-7_referee_verdict.md:44-50`): a varying algebraic C(x) with separately conserved T is excluded, but a local exchange sector can carry ∂C.
- **R17-11 verdict** (`TESTS:6590-6600`): (d-i) cancels W exactly in its class; moving bodies and anisotropic responses lie outside.
- **R19-20 item 3** (`C5_R19-20_report.md:231`): the one-point enthalpy mismatch (naive-Wilson illustration).
- **R18-2:** the electroweak vacuum under (S); not used beyond counting.
- **Comparators (RECALLED):**
  - solid inflation (Endlich–Nicolis–Wang): a medium's shear modulus gives tensor modes a mass that Stückelberg/phonon fields cannot remove, because their displacements are not TT;
  - Rubakov/Dubovsky LV massive gravity;
  - Weinberg's neutrino free-streaming damping (an LI O(H²) plasma effect);
  - BICEP/Keck r < 0.036;
  - SM thermal masses and Higgs–nucleon coupling;
  - the LVK m_g bound.

---

## 3. Results

### 3.1 (a) Size and sign of Δμ, by channel

**Why channels exist (proved under a stated hypothesis).**
- **Hypothesis BO (Born–Oppenheimer).** Lattice-scale modes, with k ~ 1/a, see the slowly varying IR fields (the Higgs condensate, thermal fluctuations with k ~ T ≪ 1/a) as local backgrounds.
- Write the lattice sea's shear as μ_UV(m_s(φ)). For mass-even terms with m_s² = κ_s|φ|²:

  μ_UV = c + R₂·|φ|²/v²,  R₂ = Σ_s n_s c₂,s (m_s a)².

  The Wilson linear term adds c₁Σn_s m_s a·(φ_∥/v).
- So Δμ = μ_state − μ_lowest = c₁Σnma·(x − 1) + R₂(⟨|φ|²⟩_T − v²)/v², with x = v(T)/v.
- This is the Taylor statement plus BO. **Checked** for the scalar-quartic piece in the model (below). For Yukawa and gauge couplings it is the same diagram topology and is **suggested**, not checked.

**Mechanism check (checked; `r1921_nn_thermal.out`).** NN scalar, m_p = 0.5, T = 0.3 and 0.15, N = 32 and 40, direct SF-flow finite-difference Hessians of the O(λ) free energy:
- The fixed lowest-state subtraction leaves H_full − μ_vac(m_p) = μ_th,free + (λ/4)G_th(0)[G_vac″ + G_th″]. The difference from this prediction is −2.5e-9 at λ = 0.02 and −6.3e-10 at λ = 0.01: ratio 4, i.e. O(λ²). Both N agree.
- Identity ∂μ_vac/∂m² = G_vac″/2: −8.302661e-4 against −8.302669e-4 (N = 32).
- T₂g: every term vanishes to ≤ 2e-12 (Liouville, separable band).
- G_vac″ < 0 (−1.66e-3 at m = 0.5; −2.03e-3 at m = 0.02). So the thermal cross term is **tachyonic** in E_g in this model.
- **Scaling (Lemma-H formula on a graded GL grid, validated by reproducing NN μ_E = +1.970388642e-3):**
  - G_th(0) → T²/12 (mass-suppressed once T ≲ m);
  - μ_th,free/T⁶ → 0.19–0.20. Analytic massless value: (1/8)(4/15)·Γ(6)ζ(6)/(2π²) = 0.206;
  - the cross term ∝ T².
- **Hence (proved from the checked pieces):** for the fixed subtraction, m_g²/H² = 0.38 λG_vac″/(g\*(Ta)²). That is −4e28 at Ta = 1.3e-17 (λ = 1, g\* = 106.75).

**SM root edges (checked arithmetic on refereed coefficients; `r1921_history.out`; the channel formulas are proved under BO).** m_g²/H² = 16πΔμ/(Ha)²; sign + is massive, − is tachyonic.

| T (GeV) | V Wilson μ_E | V Wilson μ_T2 | V twisted μ_E | V twisted μ_T2 | F (twisted c₂) μ_E | F (twisted c₂) μ_T2 | Q |
|---|---|---|---|---|---|---|---|
| 1e16 | −1.8e-7 | −4.6e-8 | −1.7e-24 | +8.7e-28 | +5.2e2 | −0.28 | 2.5e-6 |
| 1e12 | −1.8e9 | −4.6e8 | −1.7e-8 | +8.7e-12 | +5.2e10 | −2.8e7 | 2.5e-14 |
| 1e4 | −1.8e41 | −4.6e40 | −1.7e24 | +8.7e20 | +5.2e26 | −2.8e23 | 2.5e-30 |
| 170 | −2.4e48 | −6.1e47 | −2.2e31 | +1.2e28 | +2.0e30 | −1.1e27 | 7e-34 |
| 100 | −1.9e48 | −4.8e47 | −3.3e31 | +1.7e28 | +3.4e30 | −1.8e27 | 2.5e-34 |
| 10 | −2.8e47 | −7.2e46 | −5.2e30 | +2.7e27 | +1.1e28 | −6.0e24 | 2.5e-36 |
| 1 | −3.6e48 | −9.2e47 | −6.7e31 | +3.5e28 | 0 (Boltzmann) | 0 | 2.5e-38 |
| 1e-3 (BBN, electrons only) | −7.0e47 | −1.8e47 | −1.3e31 | +6.8e27 | 0 | 0 | — |

- **(i) Answered: size and sign.**
  - R19-19's Δμ is reproduced exactly: −4.70e-19 and −1.20e-19, |m_g|/H ≈ 1.5e24 at T_c.
  - It is tachyonic in both rows wherever the V channel dominates. On Wilson edges that is everywhere below ~3e11 GeV, because the F channel (sign of R₂) wins only above T* ≈ 3e11 GeV (table: V wins at 1e11, F at 1e12).
  - **Below T_c the mismatch does not switch off.** The thermal shift of v(T) from the remaining relativistic species keeps |m_g| ≫ H down to BBN: 1e47–1e48 (Wilson), 1e31 (twisted).
- **Sign structure (proved, mean field).** The mass-even part is Δμ_even = R₂(⟨|φ|²⟩_T − v²)/v².
  - Above T_c, ⟨|φ|²⟩_T ≈ 4⟨δφ₁²⟩ ≈ T²/3 (reduced by the thermal mass).
  - Below T_c it is ≈ v(T)² < v².
  - So Δμ_even changes sign at T ≈ 0.5–0.6 TeV (`r1921_bbn_signs.out`: +0.135 at 600 GeV, −0.36 at 450 GeV). It is tachyonic on one side of that temperature for either sign of R₂.
  - Twisted root edges: μ_E is tachyonic below about 0.5 TeV; μ_T2 is tachyonic above it.
- **Gauge and fermion thermal cross terms (suggested).**
  - A uniform gauge background is pure gauge, so ∂²μ/∂A² = 0 at q = 0. The leading gauge cross term is O(e²T⁴) ~ H²M_P², an LI-scale effect.
  - Thermal fermions enter through ⟨ψ̄ψ⟩_th ∝ m_f(T), which is 0 in the symmetric phase.
  - So F is carried by the Higgs fluctuations. Not computed beyond this argument.

### 3.2 (b) Which dominates, and the m_g² history

- **(ii) Answered: no (checked).** The quasiparticle shear is ≤ 2.5e-6 H² at 1e16 GeV, and it falls as (Ta)². The LI part of the plasma's TT response (neutrino free-streaming, O(H²)) is ordinary GR physics, untouched by any clause.
- The dominant pieces are V (at T ≲ 3e11 GeV on Wilson edges, and everywhere below about 0.5 TeV on twisted ones) and F (at high T).
- **The history under fixed (S\*\*) and the canonical reading:** |m_g| ≫ H from at least 1e15 GeV down to BBN. The Wilson V channel drops below H only above ~2e14 GeV, but the F channel keeps μ_E above H up to ~1e17 GeV (|m_g|²/H² = 5e2 at 1e16 GeV, falling as T⁻²).

### 3.3 (c) A state-tracking variant: Bianchi and carrier

**Variants examined.**
- **"The instantaneous law's lowest state."** In the SM-root setting the law is fixed and only the state changes, so this is (S\*\*) itself (proved, by definition). The same holds for R19-14's and R19-17's (S_ad) on a fixed-content lattice: it tracks the lattice's adiabatic vacuum, which has ⟨φ⟩ = v and no thermal ⟨|φ|²⟩. So the V, F and matter channels remain (proved, by definition).
- **(S_loc) [new]:** "the LV part (shear and O(q²) LV rows) of the strain response of the law's lowest state, evaluated with the actual state's local IR mean fields Φ(x) as backgrounds, does not gravitate". The isotropic part stays (S): a fixed e₀.
  - **Number-free:** the backgrounds are state functionals, e.g. ⟨φ²⟩_state − ⟨φ²⟩_vac.
  - **Local.**
  - **Non-signalling at linear order (suggested):** it depends on Φ at the same point, with no global variable, so there is no R15-1 channel.

**What (S_loc) removes (checked in the model).**
- In the NN model at O(λ), (S_loc) subtracts μ_vac(m_eff) with m_eff² = m_p² + (λ/2)G_th(0). The residual is μ_th,free + (λ/4)G_th(0)G_th″ (prediction met to O(λ²); `r1921_nn_thermal.out`).
- That residual is positive, ∝ T⁶, and gives m_g²/H² ∝ (Ta)²: 4e-6 at Ta = 0.0125, extrapolating to ~4e-36 at T_c.
- For the SM, it removes the V, F and matter channels by construction (suggested; it rests on BO).

**Bianchi (proved, structural; standard Noether).**
- Take Γ_sub[g, X; Φ], diffeomorphism-invariant in (g, lattice frame X^I, scalar backgrounds Φ). Then ∇_μT_sub^{μν} = (E_I∇^νX^I + E_Φ∇^νΦ)/√−g.
- For the shear piece, Γ_shear = −∫√−g ½μ(Φ)σ_IJσ^IJ, so E_Φ = −√−g ½μ′(Φ)σ² = O(σ²), which is second order.
- So at linear order about FRW, Bianchi for T_grav reduces to R19-17's lattice-frame condition:
  - automatic under reading A (the counterterm action is added; X's equation balances);
  - under reading W it needs F_I = 0, which fails at O((Ta)²) for radiation (`C5_R19-17_report.md:34,157`; count once).
- So (S_loc) keeps linear Bianchi only with R19-17's reading A, whose zero-inertia frame constraint is untested (inherited).
- **The isotropic part cannot be state-tracked this way.** Its E_Φ is zeroth order: the Planckian Higgs tadpole ∂ε/∂φ. A state-dependent isotropic subtraction is vR17-7's varying C(x), excluded without a carrier.
  - (d-i) is the registered carrier (C-box-E).
  - On V1 no carrier is registered. Reading A there would remove the subtracted piece's φ-dependence from the Higgs dynamics, which is R19-20's "Planckian Higgs tadpole" (suggested; not analyzed).
- **Scope of the definition (suggested).** At O(λ), the background is unambiguous (the thermal tadpole). To all orders, (S_loc) needs a BO split of UV and IR sectors at a scale T ≪ Λ_s ≪ 1/a. Its residual ambiguity is not estimated here.

### 3.4 (d) Observational consequences, by version

| version | early universe (canonical reading) | today (canonical reading) | status |
|---|---|---|---|
| (S\*), (S\*\*), instantaneous-law, (S_ad); root edges (Wilson or twisted) | tachyonic tensor modes with rate ≫ H in some window: 1e15–1e24 e-folds per Hubble time at T_c (Wilson), 1e15 (twisted). FRW and BBN cannot survive | IGM: Wilson μ_E tachyonic, \|m_g\| = 1.4e-9 eV (rate ~2e6 s⁻¹); twisted μ_E tachyonic at 6.1e-18 eV | excluded (worker; conditional) |
| same, free edges, even part (any R₂ ≠ 0) | tachyonic on one side of ~0.5 TeV | tachyonic in matter if R₂ > 0; massive m_g ≈ 6e-18 eV (4.7e5 × the LVK bound) if R₂ < 0 | excluded (worker; conditional) |
| same, Wilson-type law with c₁ < 0 < R₂ in both rows | massive throughout, m_g ≫ H, so primordial tensors are erased: predicts r ≈ 0 (allowed by r < 0.036, RECALLED) | massive m_g ≈ 1.4e-9 eV in the IGM, above ω(100 Hz) = 4.1e-13 eV: 100 Hz GWs would be evanescent, against LVK detections | early-universe letter not excluded; excluded today (worker; conditional) |
| mass-blind law | safe if \|c₁\| ≲ 3e-49 and \|c₂\| ≲ 2e-32 of natural size (history), 8e-29 and 4e-12 (IGM) | same | a tuning (`r1921_history.out` (e)) |
| (S_loc) + (d-i), C-box-E | GR plus LI plasma physics, plus m_g² ≲ 1e-5 H² (≈ 2.5e-6 H² at 1e16 GeV, falling as (Ta)²). Primordial r, BBN and the GW background are unaltered | the matter channel is removed by construction | HISTORY-SAFE on the letter (worker) |
| any version, "μ is not a mass" reading (no dynamical metric supplied, `PRICE_NOTE.md:22`) | no tensor-mode consequence | none | no conflict |

- **Strength of the today-entries.** Linear response in δv. The IGM dominates the path, so the path-averaged m_g² applies. The LVK dispersion bound tests ω² = k² + m_g² along the path. Inside the Earth the same channel gives |m_g| ≈ 5 MeV (Wilson) or 0.02 eV (twisted). That suggests GWs could not cross the Earth, which seems inconsistent with all-sky detections (suggested; not checked against event geometry).
- **Solid-EFT comparator (RECALLED).** A dynamical lattice frame does not remove the TT mass, because frame displacements carry no TT strain. So R19-17's frame does not rescue the fixed versions.

### 3.5 Addendum: the one-point enthalpy mismatch (R19-20 item 3, coordinator request; `r1921_enthalpy.out`, `r1921_bbn_signs.out`)

- **Scaling (proved under H-cov dilation, i.e. the same law at a new spacing, as R19-17's p = ρ/3).** p = (e − me′)/3, so W = (4e − me′)/3, dW/dm|₀ = e′(0) and dp/dm|₀ = 0.
- **Checked:**
  - Naive Wilson: e′(0) = −1.767029, reproducing R19-20.
  - **D1 root edge (b_f, r) = (0.915438682, 0.568280847):** e′(0) = −2⟨W_tot/E⟩ = −0.6923204 per 4-component field, stable over N = 64, 96, 128; a finite-difference check agrees.
  - Twisted: dW/dm² = (2/3)e₂ = −0.45026.
- **Sizes:**

| state | ΔW per cell (D1, Wilson-type) | (twisted) | against |
|---|---|---|---|
| symmetric phase | +3.04e-17 = 2.7e106 ρ_Λ | +2.7e-34 = 2.4e89 ρ_Λ | ρ_rad(T_c) = 9.1e56 ρ_Λ: ratios 2.9e49 and 2.6e32 |
| T = 1e16 GeV | same | same | ratios 1.9e-6 and 1.7e-23 (they cross 1 near 4e14 GeV for D1) |
| BBN (electrons only) | | | ratios 7.5e48 and 1.3e32 × ρ_rad |
| matter today (IGM or Earth) | | | 2.1e50 × ρ_matter (D1) and 3.8e33 (twisted), independent of density |

- **Reading.**
  - To first order the total energy is stationary (the vacuum sector sits at its minimum). So ΔW appears as a pure pressure of size ΔW. Without exchange its conservation fails.
  - (d-i)'s Q = ∇(W h) cancels it exactly in R17-11's class (`TESTS:6590-6600`; moving bodies are outside that class).
  - (S\*), (S\*\*) and (S_ad) do not cancel it (proved for (S\*) and (S\*\*) by definition; suggested for (S_ad)).
  - A state-tracking isotropic subtraction needs a carrier (vR17-7).
  - Count once with R17-11 and R19-20. The new parts are the root-edge value (about 2.6× smaller than naive Wilson) and the BBN and matter channels.

### 3.6 (e) Prices (named, not adopted)

- **P-R19-21a (new): (S_loc).** "The LV strain response (shear and O(q²) LV rows) of the law's lowest state, evaluated at the actual state's local IR mean fields, does not gravitate."
  - It replaces (S\*\*)'s fixed-state reference for the LV parts only. 0 numbers, 1 clause.
  - It is state-dependent: one answer per state. AX:94 ("A law privileges no states", `AX:94`) is counted once with (S).
  - Gates: source/action `AX:187`; R19-17's reading A (P-r1917c), inherited; the BO-split definition beyond O(λ) (open).
- **P-R19-21b (alternative): a mass-blind gravity block.** c₁ and c₂ (and c₃ for Wilson) of both shear rows vanish to the precisions above. It contains R19-11's P-R19-11b, with tighter targets. It is a tuning: unstable at higher loops, suggested by R19-15's O(λ²) detuning.
- **Inherited, counted once:** (d-i) (R17-11) for the isotropic enthalpy; the canonical-mass conditional; P-R19-19a.
- **No axiom text changes.**

---

## 4. Against the FIXED readings (`TESTS:8167-8172`)

| reading | clause | status |
|---|---|---|
| **HISTORY-SAFE** | a stated version | (S_loc) + (d-i), C-box-E (§3.3, §3.6) |
| | every pre-crossover effect below bounds | by construction for the V, F, matter and enthalpy channels; the residual quasiparticle term is checked: m_g²/H² ≤ 2.5e-6, ∝ (Ta)² |
| | without a new number | met (0 numbers) |
| | checked | at O(λ) in the NN λφ⁴ model (direct flows, two N); the SM channels from refereed coefficients; the SM-level BO step is suggested |
| **HISTORY-CONFLICT** | refereed; every stated version excluded or ~1e-67 tuning | **not met**: (S_loc) escapes. Worker content shows it for every fixed-state version on root edges and on even-part laws. The Wilson c₁ < 0 < R₂ subfamily escapes the early-universe letter (r → 0) and fails only through today's matter channel. All of it is conditional on the canonical reading. Needs a referee |
| **OPEN** | otherwise | the reading if (S_loc)'s definition beyond O(λ), or its reliance on R19-17's reading A, is judged insufficient |

**Worker reading: HISTORY-SAFE on the letter, narrowly, by construction, for (S_loc) + (d-i) in C-box-E.**
- Literal first (`TESTS:7124`).
- No fixed-state clause qualifies.
- On V1, where (d-i) cannot be posed, no stated version handles the enthalpy channel. There the reading would be OPEN, with HISTORY-CONFLICT content.

**Against the expectation (`TESTS:8173`).**
- "HISTORY-CONFLICT for fixed (S\*\*) under the canonical-mass reading": **holds**, and extends to (S\*), (S_ad), the instantaneous-law variant, and today's matter.
- "A state-tracking variant could be HISTORY-SAFE": **holds**, with refinements:
  - the shear needs no carrier at linear order (E_Φ = O(σ²)); the frame enters only through R19-17's force balance;
  - the isotropic enthalpy does need one, namely (d-i).
- "The thermal μ_th is likely the dominant physical piece": **does not hold**.
  - The quasiparticle shear is ~H²(Ta)², negligible.
  - The dominant thermal piece is the cross term, in which the plasma's ⟨|φ|²⟩ re-masses the lattice-scale sea.

## 5. Strong-word check

- **"Proved"** is used for:
  - the channel formulas under hypothesis BO (a Taylor expansion);
  - the even-part sign flip (mean field);
  - "(S\*\*) = instantaneous-law variant" and "(S_ad) misses the channels" (by definition);
  - the Noether structure with E_Φ = O(σ²);
  - the dilation scaling p = (e − me′)/3.

  All are short and unrefereed.
- **"Checked"** is used for:
  - the NN Hartree flows (two N; O(λ²) differences scale by 4);
  - the scaling coefficients;
  - the D1 enthalpy slope;
  - the arithmetic on refereed R19-11 coefficients;
  - the archived-runner reruns.
- **"Excluded"** always means under the canonical-mass reading, which is conditional (`PRICE_NOTE.md:22`; vR19-11 item 4), with RECALLED bounds.
- **"Every fixed-state version"** means (S\*), (S\*\*), the instantaneous-law variant and (S_ad), on laws with natural-size mass slopes.
- **"By construction"** means that (S_loc), like (S\*), is a stipulated subtraction, not a mechanism (vR19-15 item 4 precedent).
- **Not claimed:**
  - the crossover's non-perturbative profile;
  - QCD-era numbers;
  - the gauge and fermion cross terms (argued only);
  - the speed rows' thermal analogues;
  - nonlinear Bianchi;
  - (S_loc)'s all-orders definition;
  - the Earth-crossing GW claim.

## 6. For the referee

1. The NN mechanism check (`r1921_nn_thermal.py`): the fixed-subtraction residual (λ/4)G_th G_vac″, its sign, its T² scaling, and the (S_loc) residual.
2. Hypothesis BO and the channel formulas. Is the Higgs-fluctuation cross term with R19-11's c₂ the right leading thermal term? Are the gauge cross terms O(e²T⁴)?
3. The even-part sign flip near 0.5 TeV, and the claim that only the Wilson c₁ < 0 < R₂ subfamily escapes the early-universe letter.
4. Today's matter channel (f_N, the IGM path average, the LVK bound): does it close that escape?
5. (S_loc): does its Bianchi structure (E_Φ = O(σ²); R19-17's reading A) and its O(λ) definition suffice for HISTORY-SAFE "checked"? Or is the reading OPEN?
6. The enthalpy addendum: is the D1 slope −0.6923 right, and is the (d-i) absorption in scope?

## 7. Files (`S/`)

- `run/r1921_nn_thermal.py` → `.out`: the mechanism check (direct flows, Part 1) and the Lemma-H scaling (Part 2).
- `run/r1921_history.py` → `.out`: the SM-root channels V, F and Q against H(T); today's matter channel; the mass-blind targets.
- `run/r1921_bbn_signs.py` → `.out`: BBN (with and without free quarks; electrons only is the quoted line) and the even-part sign flip.
- `run/r1921_enthalpy.py` → `.out`: the one-point enthalpy on the D1 root edge, plus the naive-Wilson control.
- `recheck/run_rechecks.py` → `recheck_summary.out`; `arch/` holds copies of the R19-11, R19-15, R19-19, R14-3, R16-13 and R18-5 (D1 class) runners.
