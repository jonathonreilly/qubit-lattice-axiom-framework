# C5 R19-31 report: gauge and Yukawa thermal masses against (S_loc)

- **Worker:** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. Run 2026-10-13, 07:09Z to about 07:38Z. No repository file was edited. Nothing was downloaded.
- **Item:** `TESTS:8614-8630` (FIXED readings `:8626-8629`, expectation `:8630`).
- **Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `TESTS` = `P/TESTS.md`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`. `rX` / `vX` = `P/agents/C5_X_report.md` / `P/agents/C5_X_referee_verdict.md`. `S/` = `scratchpad/C5/R19-31/` (scripts and `.out` in `S/scripts/`).
- **Machine use.** `OMP_NUM_THREADS=2`. Every run took under 25 s.
- **Labels.** proved (complete short argument under stated hypotheses; unrefereed) / checked (numerics run here) / suggested / reading / comparator. RECALLED = from memory, not verified this run.
- **Read.** `AX` in full. `TESTS:8140-8173` (R19-21 item), `:8419-8435` (R19-21 worker summary), `:8545-8572` (referee records, R19-21 at `:8548-8558`), `:8614-8630` (this item). `rR19-21` in full; `vR19-21` in full; `rR19-17` in full and `vR19-17`; `vR17-11`; `vR11-3` and `rR11-3:1-40`; `rR19-27:1-80` (scratch, worker, unrefereed). Runners reused: `P/scripts/C5/R19-21/r1921_nn_thermal.py` (grid and Hessian method copied, not imported) and `r1921_history.py` (read for the channel definitions).

---

## 0. Reading against the FIXED readings: **OPEN (worker)**, with GAUGE-CANCELS content at the g²T² level

**Plain words.**
- Hot gauge bosons and fermions do get thermal masses of order g²T². But those masses belong to the soft plasma modes. The lattice-scale modes that carry the grid's shear see something else.
- At one loop, the part of the hot state's free energy that mixes plasma and lattice-scale physics is exactly: (number of soft thermal particles) × (the vacuum self-energy of a soft particle, on its mass shell). This is a standard identity.
- For a soft photon or gluon, that vacuum self-energy has no mass term at any strain, because the strained lattice law is still gauge invariant. For a soft massless fermion with chiral protection there is also no mass term. So hot gauge bosons and chiral fermions produce no g²T² grid cross term at all. Their thermal masses cancel between the boson sea and the fermion sea of lattice-scale modes (proved, with a continuum comparator, and checked on the lattice for the Ward part).
- The g²T² cross terms that do exist come through the Higgs: the plasma's ⟨φ†φ⟩ ≈ T²/12 per component multiplies the strain dependence of the Higgs mass's lattice-scale gauge and Yukawa loops. That is R19-21's F channel, whose R₂ already contains the W, Z, top and Higgs edges (`P/scripts/C5/R19-21/r1921_history.py:12,28-29`).
- (S_loc) removes this Higgs-channel g²T² term exactly at one loop, provided its "local effective mass" is the background-field mass. That is the mass the Higgs background gives the lattice-scale gauge bosons (m_A² = 2e²⟨|φ|²⟩ on three Landau modes). It is not the Debye mass. Subtracting at the Debye mass leaves an O(e²T²) residue (checked in lattice scalar QED).
- **What is left after (S_loc) is not O(T⁶).**
  - **Main residue: O(g²T⁴) in lattice units.** Under strain, the soft particles' radiatively corrected light cones move off the strained metric. These are the speed rows' thermal analogues, which the R19-21 referee listed as uncomputed.
  - **Size.** Estimated |m_g²/H²| ≈ 2e-3 (Higgs channel, computed coefficient) to ≈ 4e-2 (with the fermion speed rows bracketed, not computed). The value is constant through the radiation era. So |m_g| < H, below R19-21's bound line, but up to about 1e4 times its T⁶ estimate at 1e16 GeV.
  - **A second channel, on Wilson-type edges only.** Below the crossover, the soft massive fermions' scalar density ⟨ψ̄ψ⟩_th ≈ m_f T²/6 multiplies the strain Hessian of the Wilson additive mass (−0.062 e², checked). That gives m_g²/H² ≈ −5e13 at 100 GeV (tachyonic), and |m_g| ≈ 3e-9 eV inside the Earth today.
  - (S_loc) removes this second channel only if ψ̄ψ is among its "local IR mean fields". R19-21's list ends in "…" (`rR19-21:45,178`).

**Why OPEN, literally (`TESTS:8626-8629`, literal-first).**
- GAUGE-CANCELS requires the residue to be "O(g⁴) or O(T⁶)". The residue found is O(g²T⁴), estimated below R19-21's bound line. The Wilson-edge ψ̄ψ channel is removed only under an unstated choice of background list.
- GAUGE-RESIDUE requires "a g²T² cross term that (S_loc) leaves". With the background-field (S_loc) none is left at O(g²T²). The ψ̄ψ channel scales as g² m_f T², and it is left only if ψ̄ψ is not a background.
- So neither literal reading is met. What is met:
  - the g²T² cancellation itself (proved; checked in U(1));
  - the absence of any gauge-boson Debye/HTL g²T² cross term (proved; Ward part checked).
- **Two conditions would turn this into GAUGE-CANCELS as worded:**
  - (i) D1∞'s on-shell speed condition (`TESTS:8483`) is imposed on every uniformly strained law, not only at h = 0;
  - (ii) ψ̄ψ is included in (S_loc)'s backgrounds, or the edges are twisted/chirally protected.

  The residue would then be O(g⁴T⁴) and O(T⁶) (§2.4).

**Against the expectation (`TESTS:8630`).**
- "GAUGE-CANCELS for the Debye (electric) part, because it is a local mass": the outcome holds, but **not for the stated reason.**
  - The Debye part produces no cross term to cancel: the vacuum polarization is massless at every strain.
  - Subtracting "at the Debye mass" would itself create an O(e²T²) error (§2.2, checked).
- "OPEN for the magnetic/HTL nonlocal part": **not borne out as stated.**
  - The static magnetic part vanishes identically on the lattice (checked to 1e-13).
  - The nonlocal HTL structure affects only soft modes, at O(g²T⁴) and beyond.
  - The OPEN content sits instead in the O(g²T⁴) speed-row residue and in the Wilson ψ̄ψ channel.

---

## 1. Class, hypotheses, exclusions (stated before any title)

- **Model (the item's setting, `TESTS:8619-8621`).**
  - **Arena:** Z³ × ℝ (continuous time), lattice units a = 1.
  - **Gauge field:** a noncompact U(1) at O(e²), i.e. the Wilson action at quadratic order. Its O(e²) self-interaction, a photon–photon "Hartree" with (UV) × ⟨F²⟩_th ~ T⁴, is not computed.
  - **Matter:** an NN complex scalar with mass m (the comparator, carrying the Higgs channel), and a Wilson–Dirac fermion with r = 1 and bare m = 0.
  - **Gauge:** Feynman gauge in the loops. The Landau gauge is used for the background-field (CW) vacuum.
- **Strain: H-cov E_g** (as in `rR19-17:16,90-91`). Cell lengths are ℓ = (e^h, e^{−h}, 1).
  - Scalar hopping is c_i = 1/ℓ_i². The photon variables are a_i = θ_i/ℓ_i, so the photon dispersion is Ω² = Σ4sin²(q_i/2)/ℓ_i².
  - The Wilson term is (r/ℓ_i)(1 − cos p_i). This is a law datum and a stated choice.
  - Minimal coupling is p_i → p_i + ℓ_i a_i.
  - **Normalization (proved for soft modes).** H-cov acts on soft momenta as k_x → e^{−h}k_x; R19-21's SF flow acts as k_x → e^{t/2}k_x. So t = −2h, and μ_SF = μ_Hcov/4. All sizes in §2.5 are converted.
- **Counterterms.**
  - The scalar mass, fermion critical mass and speed counterterms are law data, fixed at h = 0 in the lowest state, as in `r1921_nn_thermal.py:3`.
  - Under strain, the speed counterterms scale like the tree action (H-cov).
  - Per-site counterterms (R19-27 form) are invariant under traceless strain at fixed site density (§3).
- **(S_loc)**, as in `rR19-21:178-186` and P-R19-21a (`rR19-21:239-242`). I use its **background-field form**:
  - Φ = ⟨φ†φ⟩_state;
  - "the law's lowest state at background Φ" is the one-loop effective potential's vacuum, in which the Higgs background gives the lattice-scale gauge modes m_A² = 2e²Φ (Landau gauge, 3 modes).
- **Canonical reading** (conditional, `PRICE_NOTE.md:22`): m_g²a² = 16πμ, with R19-21's bound line 16π|μ| < (Ha)² (`r1921_history.py:14-15`).
- **Not computed:**
  - non-abelian vertices: suggested to follow the same identity, since the BRST/lattice gauge invariance keeps gluons massless at every strain;
  - two loops and n² terms, apart from scaling arguments;
  - the fermion speed-row strain Hessians, which are bracketed in §2.5;
  - the off-diagonal (T₂g) strain, which needs a non-NN stencil (`rR19-17:86`);
  - nonperturbative magnetic screening (g²T): suggested to be O(g⁶T⁴).

## 2. Results

### 2.1 (a) The lattice photon's one-loop thermal self-energy (checked; `S/scripts/r1931_photon_thermal.out`)

- **Electric (Debye) part.** Π₀₀(0, k → 0) = e²χ(T), where χ = ∂²P/∂μ² (a uniform static A₀ is a chemical potential; proved).
  - Complex NN scalar (m = 0): m_D²/(e²T²/3) = 1.0489, 1.0103, 1.0024 and 1.0005 at T = 0.2, 0.1, 0.05 and 0.025 (`:3-6`).
  - Wilson fermion: 0.9602 → 0.9989 (`:3-6`).
  - So the continuum value e²T²/3 is approached at O(T²).
- **Magnetic part.** Π_ii(0, k → 0) = 0.
  - **Proved:** a uniform static a_i shifts every lattice momentum by ℓ_i a_i, so the Brillouin-zone sum is a-independent. This holds at every strain, and to all orders for U(1).
  - **Checked:** S − L = 1e-13 for massive scalars, at h = 0 and at h = 0.05. For the massless case it is 3e-8, the grid's IR limit (`:8-13`).
- **Hard (lattice-scale) photons see the background-field mass, not the Debye mass** (checked, `:16-18`).
  - For thermal scalars with m_s = 1 and T = 0.25: the on-shell Π_th(Ω_q, q) = 2.87e-4 to 2.91e-4 for q = 0.5 to 3.0.
  - The seagull alone, 2e²⟨cos p_x n/ε⟩ ≈ 2e²Φ, is 3.00e-4. The Debye mass is m_D² = 2.22e-3.
  - So the lattice-scale photon's thermal shift is ≈ m_A² = 2e²Φ, with a q-dependent paramagnetic correction of 1–4%.
  - **Comparator (continuum scalar QED, RECALLED):** m_A² = 2e²·T²/12 = e²T²/6 = m_D²/2 = m_∞², the asymptotic mass.

### 2.2 (b) The grid cross term with and without (S_loc)

**Lemma I (proved: standard; the frequency integral with one thermal line puts that line on shell).** At O(e²), the part of the free energy linear in thermal occupations is

  X(h) = Σ_p (n_p/ε_p)[Σ_os(p; h) − Σ_ct] + Σ_k (n_k/Ω_k) Π_os^T(k; h) + (fermions: Σ_p 4n_F/(2E)·ūΣ_os u/2 …),

i.e. soft density × the on-shell **vacuum** self-energy of the soft particle.
- "UV modes see thermal masses" is the same integral, split by partial fractions into "boson sea" and "fermion/scalar sea" pieces.
- The split is not separately physical: only the sum enters the free energy.
- **Comparator check (continuum QED, RECALLED HTL values).**
  - A hard photon's m_∞² = e²T²/6 shifts the photon sea by +e²T²/(12ω).
  - The n_F part of the hard fermion's m_∞² = e²T²/12 shifts the Dirac sea by −e²T²/(12ω).
  - They cancel exactly, as Lemma I requires for a massless chiral fermion.

**Lemma W (proved).** These on-shell self-energies are protected at zero momentum, at every strain:
- A soft photon's Π_os^T has no k⁰ term, because the strained (H-cov) law is gauge invariant.
  - Checked: Π_ii(0) = 2e-13 at h = 0 and ±0.02 (`r1931_sqed_cross.out:27-31`). On shell, Π_os^T ∝ k² (`:28-32`).
- A soft fermion's ūΣu at p → 0 is δm(h)·ūu.
  - For a massless Wilson spinor, ūu ∝ M(p) ~ rp²/2, which gives T⁴.
  - In the broken phase, ūu = 2m_f, which gives the ψ̄ψ channel (§2.3).
- The soft charged scalar's Σ_os(0; h) is not protected. This is the Higgs channel: a g²T² cross term.

**Lemma C (proved: Γ⁽²⁾(P = 0) = V_eff″).** In the background-field vacuum, dE_vac/dΦ = Σ(P = 0; h).
- In lattice scalar QED at m = 0 this is 3e²G_γ(h), with G_γ = ⟨1/(2Ω)⟩. This is the same in Feynman and Landau gauge, and checked as 4G_γ − G_s → 3G_γ.
- So (S_loc) in background-field form subtracts Φ·∂²_hΣ(0; h), and the Higgs-channel g²T² term cancels.
- The remaining difference is Φ·∂²_h[Σ_os(rest) − Σ(0)] = O(e²m²)·Φ.

**Checks (lattice scalar QED, per e², H-cov; `r1931_sqed_cross.out`, `r1931_mcheck.out`).**

| quantity | value | where |
|---|---|---|
| ∂²_hΣ(P = 0), Feynman | −0.53181 | `sqed:5` |
| ∂²_hΣ_os(rest), gauge-invariant | −0.53236 (m = 0.1) | `sqed:5` |
| (S_loc)-CW coefficient 3G_γ″ | −0.53154 | `sqed:5` |
| gap os − CW | −0.082·m², at m = 0.2, 0.1, 0.05 (exactly ∝ m²) | `mcheck:1-3` |
| fixed-subtraction cross term / Φ | −0.606, −0.553, −0.539, −0.535 at T = 0.2 … 0.025 (→ −0.532 + O(T²)) | `sqed:22-25` |
| (S_loc) residue | −1.66e-4, −7.4e-6, −2.9e-7, −5.7e-9 at T = 0.2, 0.1, 0.05, 0.025 | `sqed:22-25` |
| Debye-prescription residue (photon sea's 2 transverse modes at m_D²) | +0.0153T², +0.0163T², … | `sqed:22-25` |

- **The residue scales as T⁴ (proved and checked).**
  - Its massless-gas coefficient is (Σ_iκ_ii″)·π²T⁴/90 = −0.0860 e²T⁴ (H-cov), stable for m = 0.2, 0.1, 0.05 (`mcheck:1-3`).
  - Here κ_ii(h) is the on-shell O(p²) coefficient [Σ_os(p) − Σ_os(0)]/p̂_i². It is obtained by D_space(p) − D_time(Ω_p), which cancels the LI threshold logarithm.
  - Values: κ₀ = −0.0760 e² (h = 0: isotropic, absorbed by the speed counterterm); ∂_hκ_xx = −0.196 e²; ∂²_hκ = (−0.413, −0.413, +0.042) e² (`sqed:7-17`).
- **The Debye prescription fails (checked; proved for m = 0).** The residue after subtracting the photon sea at m_D² approaches −(T²/12)G_γ″ = +0.0148 e²T² for m → 0. The table's +0.0153 at T = 0.2 matches. This is an O(e²T²) error, of opposite sign to the cross term.
- **Photon channel: Π_os^T/k̂² at h = 0 is −1.93e-3 e², isotropic** (`sqed:30`).
  - Under strain it is birefringent at O(e²h): (x, z) and (y, z) split by 1.0e-4 at |h| = 0.02, each ±5.1e-5 about the h = 0 value (`sqed:28,32`).
  - Its thermal cross term after the h = 0 counterterm is −8.88e-4 e²T⁴, with clean T⁴ scaling (`sqed:35-38`).

### 2.3 Wilson-fermion channel (checked; `r1931_wilson_mass.out`)

- **The one-loop additive mass is δm = +0.37435 e²** (H-cov, r = 1).
  - r → 0 gives exactly 0, the chiral control (`:1`).
  - ∂²_hδm = −0.0622 e², stable under the step size (`:7`).
- **A fixed critical-mass counterterm cancels only δm(0).** Under strain, every soft Wilson fermion's mass shifts by (∂²_hδm/2)h².
- **Cross term = ⟨ψ̄ψ⟩_th·∂²_hδm** (Lemma I + W):
  - massless Wilson soft fermions: −0.0355 e²T⁴ (`:9-11`);
  - massive fermions: ⟨ψ̄ψ⟩_th → m_f T²/6, which gives a g² m_f T² term (`:12-17`).
- **Twisted edges (suggested).** At maximal twist an untwisted mass shift enters the soft energy quadratically, so this channel is O(h⁴), or O(g²(m_f a)²(Ta)²) through multiplicative renormalization.
- **Is it in (S_loc)?**
  - Only if ⟨ψ̄ψ⟩ is one of its "local IR mean fields". Then Lemma C's argument applies with dE_vac/d(ψ̄ψ) = δm(h).
  - R19-21's definition names "Higgs condensate, thermal ⟨|φ|²⟩, …" (`rR19-21:45`).

### 2.4 (c) Scaling in g and T (proved from Lemmas I, W and C; checked where marked)

| channel | fixed (S\*\*) | (S_loc), background-field, {φ†φ} | (S_loc) + {ψ̄ψ} | (S_loc) + D1∞ at every strain |
|---|---|---|---|---|
| soft charged scalars (Higgs): ⟨φ†φ⟩ × ∂²Σ_H | g²(Ta)², checked U(1) | O(g²m²)·Φ = O(g⁴(Ta)⁴), checked | same | same |
| same, speed rows | g²(Ta)⁴ | g²(Ta)⁴: −0.086 e² per complex scalar, checked | same | 0 at this order |
| soft gauge bosons (Debye/HTL) | g²(Ta)⁴ (Ward), checked U(1) | same | same | 0 at this order |
| soft chiral fermions | g²(Ta)⁴ (suggested; Wilson r-term checked −0.0355) | same | 0 | speed part 0 |
| soft massive Wilson fermions (broken phase) | g²(m_f a)(Ta)², checked coefficient | **same** | 0 | same as left |
| quasiparticles' own LV (R19-21 Q) | (Ta)⁶ | (Ta)⁶ | (Ta)⁶ | (Ta)⁶ |

- No g²T² term arises from gauge-boson or chiral-fermion thermal masses at n-linear order (Lemmas I and W).
- **Beyond one loop (suggested).**
  - Lemma I holds order by order for the n-linear terms: n × the all-orders on-shell vacuum self-energy. So the g²T² channel stays the Higgs one.
  - The n² terms (soft–soft) are LI in the strained metric up to O(g²(Ta)⁶) or O(g³(Ta)⁴)·LV.

### 2.5 (d) Sizes through SM history (`r1931_sizes.out`; canonical reading conditional; SM mapping an ESTIMATE)

- **Fixed (S\*\*), Higgs channel:** this is R19-21's F channel, unchanged; it is not recomputed here.
  - My U(1) coefficient gives −0.133 e²Φ per complex scalar (SF), consistent in size with R19-21's F column (~1e30 at T_c).
  - This upgrades R19-21's BO step for gauge species (`rR19-21:128`, "suggested") to checked at one loop in a U(1) lattice model.
- **(S_loc) residue, O(g²T⁴).** It is T-independent in the radiation era (g\* = 106.75). Mapping uses lattice-scale couplings g² ≈ 0.25, g′² ≈ 0.2, g_s² ≈ 0.3 (RECALLED).

| piece | m_g²/H² | status |
|---|---|---|
| Higgs doublet, scalar speed rows | −1.7e-3 | computed coefficient, SM mapping |
| gauge-boson channel | ≈ −2.8e-3 | coefficient from the scalar loop, multiplicities guessed |
| fermion speed rows | ≈ −3e-2 | **bracket only**, not computed |
| rough total | ≈ −4e-2 (\|m_g\|/H ≈ 0.2) | estimate |
| R19-21's T⁶ term, for comparison | 2.5e-6 at 1e16 GeV; 4e-36 at T_c | `rR19-21:35` |

  - |m_g| < H, so the bound line is met (estimate).
  - **Consequence (suggested).** A tachyonic m_g² = −εH² grows superhorizon tensors by e^{εN}. Over 55 e-folds of radiation: ×1.1 for ε = 1.7e-3, ×8 for ε = 0.038 (`sizes:8-9`).
  - That does not conflict with r < 0.036 (RECALLED), but it would alter the mapping from r to the inflation scale if ε ≳ 0.01.
- **CW gap (O(g⁴)):** m_g²/H² ≈ −6e-5 (`sizes:12`).
- **Wilson ψ̄ψ channel** (Wilson-type edges; not removed by (S_loc) unless ψ̄ψ is a background), quarks t, b, c with C_F g_s² (`sizes:14-19`):
  - m_g²/H² ≈ −3e13 (150 GeV), −5e13 (100 GeV), −7e13 (50 GeV), −4e14 (10 GeV), −7e15 (1 GeV). Tachyonic, with masses at their T = 0 values (crude near T_c).
  - **Today** (path-averaged, σ-term weight ≈ 13 per nucleon, RECALLED):
    - IGM: |m_g| ≈ 8e-25 eV, below LVK's 1.92e-23 eV.
    - Earth: ≈ 3e-9 eV, above the 4.1e-13 eV energy of a 100 Hz GW.
  - This is the same kind of conflict as R19-21's natural-Wilson matter channel (`vR19-21:26`).
  - Under the "μ is not a mass" reading there is no tensor consequence. The rest-mass–shear coupling, Planckian per particle: ½|∂²_hδm| ≈ 0.031 e²/a per unit h², H-cov, remains a law-level fact of Wilson edges with fixed counterterms.

## 3. Recheck of R19-27's claim (worker, unrefereed; `rR19-27:16-36`)

- **Lemma E's power counting checks** (proved; trivial). For F = c n^{(4−k)/3}m^k, n∂_nF = ((4−k)/3)F.
- **Scope (proved).** R19-27's per-site counterterms depend on the site density n and the Higgs field only. Traceless E_g strain at fixed n leaves them unchanged.
  - So they cannot absorb any shear-row cross term: neither the Higgs g²T² channel, nor the speed-row residue, nor the Wilson ψ̄ψ channel.
  - Theorem R (if confirmed) acts on the isotropic enthalpy channel only. It does not change any number in this report.
- I did not rerun R19-27's numerics.

## 4. Prior art (each counted once)

- **rR19-21** §3.1: BO, the F channel and the "gauge cross term O(e²T⁴)" argument (`:120-128,163-166`).
  - The gauge-boson part of that argument holds, for a different reason (Lemma W, not "pure gauge").
  - The "Higgs-only, T⁶ residue" claim does not hold: the residue is O(g²T⁴), and Wilson edges add ψ̄ψ.
- **vR19-21** item 2 (`:15-20`) and TESTS `:8556`: the g²T² objection, answered in §0 and §2.4. Item 5 (`:28-30`): cone rows uncomputed. §2.2's speed-row residue is their thermal analogue.
- **rR19-17** Lemma N and H-cov (`:61-68,115-133`): the strain definition and the Bianchi structure. Not re-derived.
- **vR17-11 / vR11-3:** the enthalpy and tadpole channels. These are isotropic and not touched here.
- **R11-3's edge coefficients** enter only through R19-21's R₂ (`r1921_history.py:4-6`).
- **R19-24 D1∞** (`TESTS:8483,8569-8570`): the speed counterterms. Here they are fixed at h = 0.
- **Comparators (RECALLED):**
  - HTL / asymptotic masses (m_D² = e²T²/3, m_∞,γ² = m_D²/2, m_f² = e²T²/8);
  - the one-loop pressure's n-linear terms vanishing after on-shell renormalization in the continuum;
  - the anisotropic-lattice renormalized anisotropy (O(g²)) and the anisotropy dependence of the critical mass in lattice QCD;
  - the nucleon σ-term.

## 5. Against the FIXED readings (`TESTS:8626-8629`)

| reading | clause | status |
|---|---|---|
| **GAUGE-CANCELS** | (S_loc) removes the g²T² cross term at one loop | **met** for the background-field (S_loc) (Lemma C; U(1) T² coefficient matched to O(e²m²), checked). There is no gauge-boson/HTL g²T² term to remove (Lemmas I and W) |
| | residue O(g⁴) or O(T⁶) and below bounds | **not met as worded.** The residue is O(g²T⁴) (speed rows; −0.086 e² per complex scalar, checked; SM ≈ −2e-3 to −4e-2 H², estimated; below the \|m_g\| < H line). The O(g⁴) part (CW gap) is checked |
| | as checked | U(1) lattice scalar QED plus the Wilson additive mass. SM fermion speed rows and non-abelian vertices are not computed |
| **GAUGE-RESIDUE** | a g²T² term that (S_loc) leaves | **not met** for background-field (S_loc). The Wilson-edge ψ̄ψ channel (g² m_f T², m_g²/H² ≈ −5e13 at 100 GeV) is left only if ψ̄ψ is not a background. Twisted edges: suggested O(h⁴) |
| **OPEN** | otherwise | **the reading** |

## 6. Strong-word check

- **"Proved":**
  - Lemma I (standard identity);
  - Lemma W (Ward identity at every strain; magnetic zero by momentum shift);
  - Lemma C (Γ⁽²⁾(0) = V″);
  - t = −2h for soft modes;
  - the Debye-prescription mismatch at m = 0;
  - the R19-27 scope statement.

  All are short and unrefereed.
- **"Checked":** the numerics in §2.1–2.3. One model (U(1), NN complex scalar, Wilson fermion), the H-cov strain, the GL grid with 144 nodes per axis, finite-difference Hessians with step 0.02 (fermion: 0.02 and 0.04 agree to 0.1%).
- **"Exactly":** used for the CW identity (a symbolic identity) and for the gap's ∝ m² scaling (three masses). Nothing else.
- **"No g²T² cross term" from gauge bosons and chiral fermions:** at n-linear order, all orders in the vacuum self-energy. The n² terms are argued, not computed.
- **The SM sizes in §2.5 are estimates:** coupling mapping RECALLED, fermion speed rows bracketed, multiplicities rough. Every "excluded" or "tachyonic" is under the canonical reading.
- **Not claimed:**
  - any non-abelian or two-loop number;
  - the T₂g rows;
  - the sign of the fermion speed-row residue;
  - that (S_loc) is defined beyond its stated backgrounds.

## 7. Prices (named, not adopted)

- **P-R19-31a.** (S_loc)'s "local effective mass" is the background-field (effective-potential) mass at Φ = ⟨φ†φ⟩. It is not the Debye/HTL mass. This is a definitional sharpening of P-R19-21a, with 0 numbers.
- **P-R19-31b.** For Wilson-type edges, (S_loc)'s backgrounds include ⟨ψ̄ψ⟩. The alternative is twisted or chirally protected edges.
- **P-R19-31c.** D1∞'s on-shell speed conditions hold on every uniformly strained law. This is a law-level clause: speed counterterms as functions of the uniform strain. Without it, the O(g²T⁴) residue remains, at ≈ 1e-3–1e-1 H² (estimate).

## 8. Files (`S/scripts/`)

- `r1931_photon_thermal.py/.out`: (a) Debye (scalar and Wilson fermion), the magnetic zero, and the hard-photon on-shell thermal self-energy.
- `r1931_sqed_cross.py/.out`: (b) Σ(0; h) in Feynman, on-shell and CW forms; on-shell κ(h) by D_space − D_time; the fixed, (S_loc) and Debye-prescription cross terms against T; the photon channel.
- `r1931_mcheck.py/.out`: the CW gap ∝ m², and the massless-limit residue coefficient.
- `r1931_wilson_mass.py/.out`: the Wilson additive mass δm(h), ∂²_hδm, the r = 0 control, and the ⟨ψ̄ψ⟩_th cross terms.
- `r1931_sizes.py/.out`: (d) SM-history sizes (estimates), and today's matter for the Wilson ψ̄ψ channel.
