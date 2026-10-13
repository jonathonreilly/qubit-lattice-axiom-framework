# C5 F2 report: which observations bound an environment-dependent graviton mass / strain stiffness μ(ρ, T)

- **Worker:** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. Run 2026-10-13 12:11Z to about 13:25Z. No repository file was edited. Web search was used for observational bounds; nothing was downloaded or executed. Every run was a 1D or radial integration, one process at a time, well under 1 GB, and none is still running.
- **Item:** `TESTS:9188-9207`. FIXED readings at `:9204-9206`; expectation at `:9207`.
- **Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `rX` / `vX` = `P/agents/C5_X_report.md` / `..._referee_verdict.md`; `S/` = `scratchpad/C5/F2/scripts/` (`f2_common.py/.out`, `f2_earth.py/.out`, `f2_cosmo.py/.out`, `f2_galaxy_ns.py/.out`).
- **Labels.** proved / checked / suggested / reading / comparator. RECALLED means taken from memory, not verified in this run. WEB means checked by web search in this run (sources at the end).
- **Read.** `AX` in full; `TESTS:9146-9207`; `rR19-34` in full, with `vR19-34` and `P/scripts/C5/R19-34/r1934_sizes.py/.out`; `vR19-21` and `vR19-31` in full; `rR19-31:1-60`; `rR19-21` grepped for the canonical mapping, signs and today-entries (`:26-55, 64, 141, 202-211`).

## 0. Reading: **ENV-BOUNDS (worker)**

### Plain words

- **Earth crossing (the cleanest bound).**
  - GW170817 came from below the horizon at both LIGO sites (checked, `S/f2_earth.out:2-4`).
    - At Hanford, NGC 4993 was 62° below the horizon. The wave crossed 11,261 km of Earth and passed through the outer core.
    - At Livingston it was 47° below, giving a 9,293 km chord through the lower mantle.
  - Both sites still detected it, with SNR 18.8 and 26.4.
  - Requiring that the wave was neither absorbed nor dispersed on those chords gives |m_g²|/ρ ≤ 1.5e-29 eV² m³/kg. That is |m_g| ≲ 3e-13 eV at Earth's mean density, about the energy of a 70 Hz graviton. The bound holds for **either sign** of m_g².
  - R19-34's H-cov placeholder (2.36e-9 eV in rock) exceeds it by 6.7e7 in μ, or 8e3 in |m_g|.
  - At the placeholder size, GW170817 would have arrived attenuated by e^(-1.4e5) at Hanford (massive sign). With the tachyonic sign it would have been reflected down to |t| ≈ 2e-3.
  - **The detector on the ground** gives a bound of the same size for every source, overhead ones included. A massive or tachyonic ground pins the field near a node at the surface, so at 100 Hz the strain 1 m above ground is 1e-4 (massive) or 2e-3 (tachyonic) of the incident wave.
- **Galaxy and IGM.**
  - Path-integrated dispersion against LVK's GWTC-4.0 mass bound gives |m_g²|/ρ ≤ 2.7e-19. The placeholder passes this by a factor of 270.
  - In the massive sign, the pulsar-timing band is stronger. Nanohertz waves would be evanescent in the Local Bubble gas around the Sun if m_g there exceeded ω_min ≈ 8e-24 eV. That gives |m_g²|/ρ ≲ 8e-24, which the placeholder exceeds by about 120.
  - This last bound rests on 3-4σ PTA evidence, and the local gas density is RECALLED, so it is suggested.
- **Binary pulsars (strongest, but model-dependent).**
  - A medium mass term screens the TT field inside each neutron star. The stars' own kinetic stress then stops radiating, while the orbital field stress still radiates.
  - For a circular orbit, the matter and field stresses each carry half of the oscillating quadrupole. So the radiated power falls by 1 − s, where 1 − s ≈ μ_ρ⟨|Φ_N|⟩/(4πG) in the Born limit.
  - The double pulsar's 1.3e-4 agreement then gives |m_g²|/ρ ≤ 2e-43, or |m_g| ≤ 2.7e-13 eV at nuclear density.
  - The placeholder (m_g ≈ 0.02 eV inside a neutron star) would cut Ṗ_b by about 75%.
  - This is suggested: it is computed in the stated linear model, without the self-field O(compactness) corrections.
- **Hot early universe: the answer depends on the sign.**
  - **Tachyonic (R19-34's computed sign):**
    - Tensor modes grow as e^N with N = ∫√|A| d ln T.
    - Requiring that graviton vacuum fluctuations, once grown, stay below the ΔN_eff < 0.3 bound gives |m_g²|/H² ≲ 4e3-8e3 for one e-fold of expansion, or ≲ 35-64 if sustained from 150 GeV to 1 MeV.
    - The placeholder gives N ≈ 2e9 e-folds, which exceeds this by about 1e15 in |A|.
    - The binding observation is BBN/CMB N_eff, not the CMB B-mode limit. The B-mode limit needs an unknown primordial tensor amplitude to start from.
  - **Massive (the sign branch):**
    - **There is no current observational bound.** A mass term larger than H only damps super-horizon tensors, as a^(-3/2), so it predicts r ≈ 0, which r < 0.036 allows.
    - "|m_g| < H" is therefore *not* an observational line for the massive sign in the hot era. F1 should not read it as one.
- **Today's cosmic mean density (tachyonic sign):**
  - The placeholder gives |m_g| = 4.5e8 H₀, which means a 32-year e-folding of tensor modes on all scales above ~10 pc. The limit is |m_g| ≲ 100 H₀ = 1.4e-31 eV.
  - Every body bigger than π/(2|m_g|) is linearly unstable. For the Earth that threshold is 4.6e-14 eV (checked with PREM).
- **Static potentials:**
  - These are not bounded by anything F2 can compute. They need the stiffness's trace/scalar content, which the E_g Hessian does not supply.
  - If the stiffness also screens the spatial potential Ψ, Cassini gives |m_g²|/ρ ≤ 1.3e-39.
  - If it is pure shear, the Lorentz-violating massive-gravity comparator (Rubakov's m₀ = 0 phase) leaves Newton's law unmodified at linear order.

### Literal reading (`TESTS:9205-9206`)

- **ENV-BOUNDS: met** (worker). §2 gives a table of environment-specific bounds. Each row states its observational basis and the derivation's assumptions. The rows include:
  - Earth crossing (checked);
  - the detector on the ground (checked);
  - the hot early universe, both signs (checked arithmetic);
  - the Galaxy and IGM;
  - binary pulsars;
  - static potentials (conditional).
- **OPEN: not met.**
- **Weaker rows, labelled as such in the table:** the PTA, binary-pulsar and static rows are suggested. The Earth-instability and late-time tachyonic rows are consistency thresholds; their observational consequence needs a nonlinear end state that I did not compute.

### Against the expectation (`TESTS:9207`)

- **"Sources below the horizon would be invisible … bounded by geometry": borne out for the massive sign, with corrections.**
  - **Decay length.** At |m_g| = 1e-9 eV the decay length is ħc/m = 197 m, not ~0.2 m. At the placeholder's 2.36e-9 eV it is 84 m (`S/f2_common.out:2`). The conclusion survives, because the chord is 1e5 decay lengths.
  - **Sign.** R19-34's computed sign is **tachyonic in matter** as well as in the plasma: c < 0 and ⟨ψ̄ψ⟩ > 0 in both (`r1934_sizes.py:19`; `rR19-34:151`). A tachyonic medium is not evanescent. It is a huge-index medium, n = √(1 + M²/ω²) ≈ 6e3, and the wave is mostly reflected at the surface (|t| ≈ 2e-3). The Earth-crossing bound holds in both signs, but by different mechanisms.
  - **Evidence.** "Detection from all directions" is supplied concretely by GW170817: both LIGOs saw it from below, and the position is fixed by the EM counterpart. Isotropy arguments alone are weak, because the antenna pattern is symmetric under n → −n.
- **"Tachyonic μ ≫ H² … bounded by the CMB": partly.**
  - The growth (e^(2e9) on the placeholder) is right.
  - But the robust ceiling is N_eff/BBN, with the graviton vacuum as an irreducible seed. A B-mode bound needs the primordial r, which is unknown.
  - The massive sign has no early-universe bound at all.

## 1. Setting and hypotheses (stated before the table)

- **Field model** (the item's setting, `TESTS:9191`). Each TT polarization obeys
  - h'' − ∇²h + m²(x, t) h = 0, with m² = σ μ_ρ ρ(x) for non-relativistic matter, where σ = +1 is branch **M** (massive) and σ = −1 is branch **T** (tachyonic);
  - m² = A(T) H² in the hot plasma;
  - h and h' are continuous at interfaces, since m² enters as a potential.
- **Not modelled:**
  - TT–vector–scalar mixing in density gradients (a position-dependent Fierz–Pauli-type mass is not gauge-consistent in general);
  - 3D refraction inside the Earth (in branch T the index is about 6e3);
  - the nonlinear end state of any instability.
- **Universal coefficient.** μ_ρ ≡ |m_g²|/ρ in eV² m³/kg. Bounds from different environments are compared on this one number. This assumes ⟨ψ̄ψ⟩ ∝ n, which is fine for ordinary matter; at nuclear density the ratio changes only by an O(1) factor.
- **Placeholder (R19-34 H-cov, canonical reading conditional).**
  - m_g² a² = 16π n a³ w|c|/4, with c = −0.040475 e², w_N = 5.2, w_e = 0.1 and Y_e = 0.5 (`r1934_sizes.py:4-5, 22-27`).
  - That gives μ_ρ = 1.012e-21 eV² m³/kg (`S/f2_common.out:1`). It reproduces R19-34's 2.343e-9 eV for Earth nucleons (`:10`).
  - Sign: tachyonic, both in the plasma and in today's matter. The other sign (m_f < 0 relative to W) is massive in both (`rR19-34:151`).
- **Earth model.** PREM polynomials (Dziewonski & Anderson 1981, RECALLED). Checked: M = 5.9732e24 kg and I/MR² = 0.3308 (`S/f2_common.out:11`).

## 2. (b) The table: bounds per environment, with (c) the placeholder applied

μ_ρ bounds are in eV² m³/kg. The placeholder is μ_ρ = 1.0e-21.

| # | environment | effect of μ (a) | observational basis | bound on μ_ρ | as \|m_g\| at that density | placeholder / bound | label |
|---|---|---|---|---|---|---|---|
| 1 | **Earth crossing**, GW170817, both signs | M: evanescence once m > ω, else 1/f dispersion phase. T: reflection at the surface (impedance), plus phase. | GW170817 seen at H1 (62° below the horizon) and L1 (47° below) with SNR 18.8/26.4; position from the EM counterpart; LVK GW170817 dispersion bound 9.51e-22 eV at 40 Mpc (WEB) | **≤ 1.5e-29** (H1 dispersion budget; S_SNR ≥ 0.7 gives 1.8e-29 M; L1 gives 2.6e-29) | ≤ 2.9e-13 eV at 5500 kg/m³ | **6.7e7** (8e3 in \|m_g\|) | checked (1D chord model) |
| 2 | **Detector on the ground**, any direction, both signs | the ground forces a near-node: \|h(1 m)\|/\|h_inc\| ≈ 2ω cosθ/\|m_rock\| | GW170817 amplitude and distance agree with NGC 4993's 40.7 ± 2.4 Mpc (WEB) to ~30% | ≲ 1e-30 to 1e-29 (grid: 1e-28 fails at 0.46 / 1.54; 1e-30 passes) | ≲ 1e-13 eV in crust | ~1e8 | checked (vertical 1D, atmosphere + crust) |
| 3 | Earth interior, T only | linear instability once μ_ρ > critical (bound state of −∇² − M²(r)) | none directly; the consequence is a non-static metric, end state not computed | threshold 3.8e-31 (l = 0), 3.6e-30 (l = 2) | 4.6e-14 eV at 5500 | 2.7e9; e-folding 0.18 μs | proved-in-model / suggested |
| 4 | Sun | evanescence or reflection for paths through it | no detected event's path crossed the Sun (sky fraction 5.4e-6) | **no bound** | — | — | reading |
| 5 | **Galaxy + IGM**, LVK band | 1/f dispersion phase, set by the column Σ = ∫ρ dl | GWTC-4.0 m_g ≤ 1.92e-23 eV (LIGO-P2500066, as cited in `vR19-21:26`); D₀ ~ 1.5 Gpc; Σ = IGM 0.029 + MW 0.017 + host 0.017 kg/m² (estimates) | ≤ 2.7e-19 | path-averaged \|m_g\| ≤ 1.9e-23 eV | **3.7e-3 (passes)** | checked arithmetic; columns RECALLED estimates |
| 6 | NGC 4993 path, arrival time | group delay μΣ/(2ω²) | GW170817/GRB delay 1.74 s; emission lag ≤ 10 s (ApJL 848 L13, RECALLED) | ≤ 7e-14 (weak) | — | passes | checked arithmetic |
| 7 | **PTA band**, M only | evanescence below f where m(n_LB) > ω | NANOGrav 15-yr HD at ~3σ, plus EPTA/PPTA/CPTA (WEB: 3-4σ evidence); f_min ≈ 1/(16 yr); vacuum version m_g < 8.2e-24 eV (Wu et al., WEB) | ≲ 8e-24 at n_LB = 0.005 cm⁻³ (range 4e-25 to 4e-23 for 0.1 to 0.001 cm⁻³) | ≤ 8.2e-24 eV in Local Bubble gas | **~1.2e2** (25 to 2.5e3); placeholder dark below 22 nHz | suggested |
| 8 | **Binary pulsar**, M (T is unstable) | NS interior screens the TT coupling: Ṗ_b × ((1+s)/2)² | double pulsar Ṗ_b/GR within 1.3e-4 (95%; Kramer et al. 2021, WEB) | **≤ 2.0e-43** (Born) | ≤ 2.7e-13 eV at 3.6e17 kg/m³ (mR ≤ 0.016) | **5e21**; placeholder cuts Ṗ_b by ~75% | suggested (model computation) |
| 9 | **Hot early universe, T** | tensor growth e^N, N = ∫√\|A\| d ln T | ΔN_eff < 0.3, i.e. Ω_GW h² ≲ 1.6e-6 (WEB); seed = graviton vacuum in the tachyonic band | **\|m_g²\|/H² ≲ 4e3-8e3** per e-fold; ≲ 35-64 sustained over 150 GeV to 1 MeV | — | N = 2.0e9 vs N_max ≈ 70-95; ~1e15 in \|A\| | checked arithmetic, stated assumptions |
| 10 | **Hot early universe, M** | super-horizon tensors damped as a^(-3/2); r → 0 | r₀.₀₅ < 0.036 (BICEP/Keck 2021, WEB) is only an upper limit | **no current bound** | — | allowed (predicts r ≈ 0) | reading; count once with `rR19-21:206` |
| 11 | Today's cosmic mean, T | e-folding at rate \|m_g\| on all scales > 2π/\|m_g\| | observed small tensor sector: r < 0.036, PTA amplitude ~1e-15 | ≲ 4.9e-35 (\|m_g\| ≤ 100 H₀ = 1.4e-31 eV) | — | 2.1e13; \|m_g\| = 4.5e8 H₀, e-folding 32 yr | checked arithmetic; suggested basis |
| 12 | Static potentials | only if the stiffness has trace/scalar content: Yukawa screening of Ψ inside bodies | Cassini \|γ − 1\| < 2.3e-5 (RECALLED) | ≤ 1.3e-39 *if* trace content | — | 7.7e17 *if* trace content | suggested, conditional; comparator: pure shear leaves Newton unmodified |

**Tuning the placeholder would need:**
- 1.5e-8 for the Earth (consistent with R19-34's 3.1e-8 against the 100 Hz line);
- 2e-22 for binary pulsars;
- about 1e-15 in |A| for the hot era (T).

**R19-21's natural Wilson matter channel** (|m_g| = 1.42e-9 eV in the IGM, `vR19-21:26`) corresponds to μ_ρ ≈ 4.8e9. It fails every row by more than 1e28. Count once.

## 3. Derivations and numbers per case

### 3.1 Earth crossing (`S/f2_earth.py` A-C)

- **Geometry** (checked; `f2_earth.out:2-5`). Inputs:
  - time 2017-08-17 12:41:04.4 UTC (WEB);
  - NGC 4993 at RA 197.4488°, Dec −23.3839° (RECALLED);
  - site coordinates RECALLED;
  - GMST from the IAU formula.

  Results:
  - H1: altitude −62.1°; chord 11,261 km; closest approach r = 2,981 km, inside the outer core.
  - L1: altitude −46.8°; chord 9,293 km; closest approach r = 4,359 km.
  - V1: +17.3°.
  - Secondary case: GW170814's centroid at Dec −44.95° never rises at Hanford (maximum altitude −1.4°). Its 60 deg² region straddles that line, so it is not used.
- **Solver** (checked).
  - Exact 1D transmission through piecewise-constant PREM layers, with |k|d ≤ 0.3.
  - A backward log-derivative recursion keeps evanescent layers stable.
  - t is quoted relative to vacuum.
  - S_SNR is the SNR-weighted |t| over 30-1000 Hz, using an analytic aLIGO PSD (Ajith fit, RECALLED).
- **Criteria.**
  - S_SNR ≥ 0.7, i.e. amplitude consistent with the EM distance.
  - ∫|m²|ds ≤ (9.51e-22 eV)² × 40 Mpc = 1.12e-18 eV² m. This is the GW170817 1/f-phase bound applied to the Earth column; the 1/f phase has the same form in both signs at small m.
- **Results** (`f2_earth.out:12, 28, 45, 61, 77-78`).
  - μ_ρ ≤ 1.51e-29 from the H1 dispersion budget, in both branches.
  - The M-branch amplitude criterion gives 1.78e-29 (H1) and 3.16e-29 (L1).
  - The T-branch amplitude criterion is weaker and non-monotonic (internal resonances); dispersion binds.
  - The transition is sharp. For M, |t(30 Hz)| falls from 0.98 at 1e-30 to 8e-6 at 1e-29 (`:16-18`): the bound is essentially "m in the core < ω at the low end of the band".
- **Placeholder** (`f2_earth.out:81-90`).
  - M: WKB exponent ∫κ ds = 1.44e5 (H1) and 1.01e5 (L1).
  - T: exact |t| ≈ 1.9e-3 (median over 30-300 Hz) on the L1 chord. The single-interface estimate is 4ω/M ≈ 1e-3. The extra phase is 1e5 rad.
  - So GW170817 would have registered SNR ≲ 0.05 at each LIGO in either sign.

### 3.2 Detector on the ground (`S/f2_earth.py` D)

- **Model.** A vertical 1D column:
  - exponential atmosphere, 1.225 kg/m³ at the surface with scale height 8.5 km;
  - rock below at 2,600 kg/m³ (12 km), then 2,900 kg/m³;
  - incident wave from above;
  - outgoing or decaying condition at the bottom, i.e. no return from the deep Earth. This is a typical value; branch T resonances can move it.
- **Placeholder** (`f2_earth.out:93, 98`). |h(1 m)|/|h_inc| at 100 Hz is 1.0e-4 (M) and 2.0e-3 (T). At 60° incidence it is half that. This matches 2ω cosθ/|m_rock| (proved for a single step: |ψ(0)| = 2k_z/|k_z + iκ| = 2ω cosθ/m).
- **So:** even overhead sources would be suppressed by 1e-4 to 1e-3. Every LVK distance would be inflated by that factor, against GW170817's EM distance.
- **Bound** (`:94-95, 99-100`). μ_ρ = 1e-28 fails (0.46 and 1.54 in M; 0.37 in T). μ_ρ = 1e-30 passes (within 1.05/1.34 in M; 0.96 in T). So the bound is ≲ 1e-29, consistent with row 1.

### 3.3 Earth instability, branch T (`S/f2_earth.py` E)

- **Threshold** (checked; `f2_earth.out:106-107`). The zero-energy radial equation u'' = (l(l+1)/r² − sρ)u on PREM has its first bound state at:
  - μ_ρ = 3.81e-31 for l = 0 (4.6e-14 eV at 5,500; the uniform-sphere π/2 rule gives 4.9e-14);
  - μ_ρ = 3.61e-30 for l = 2.
- **Placeholder** (`:108`). The centre has M = 3.6e-9 eV: growth rate 5.5e6 /s, and about 1e10 bound states.
- **Status.** The static metric of every planet is linearly unstable in this model (proved in the model). What that does to observations needs the nonlinear end state. **Not counted as an observational bound** under the owner's standard.

### 3.4 Galaxy, IGM, PTA (`S/f2_galaxy_ns.py` ii)

- **LVK dispersion with a column** (`f2_galaxy_ns.out:5-6`). The phase is ∫m² dl/(2ω), so the constant-mass bound becomes μ_ρ Σ ≤ m_LVK² D₀.
  - Result: μ_ρ ≤ 2.7e-19.
  - The placeholder's path-averaged |m_g| is 1.2e-24 eV, which passes.
  - The Milky Way column is comparable to the IGM's. R19-34 compared the IGM density alone. Count once with `rR19-34:149`.
- **Arrival time** (`:9-10`). Weak; the placeholder delay is 1.4e-7 s.
- **PTA, branch M** (`:13-16`). Inputs:
  - The Earth sits inside the Local Bubble: about 100 pc of n ≈ 0.005 cm⁻³ gas (RECALLED; the Local Interstellar Cloud adds ~0.1 cm⁻³ over a few pc).
  - Results: for m(n) > ω, κ·100 pc ≈ 1.4e3 at the placeholder, and every nHz wave below 22 nHz is extinguished before reaching Earth. The heliosphere is thin (∫m dr/ħc = 0.02, `:17`).
  - Effect on the timing signal: the Earth term of pulsar timing needs the wave at the Earth. The Earth's own interior screening (kR ≪ 1) changes the Earth term only by O(ωR), so it is not the issue.
  - Bound: m(n_LB) ≲ ω_min.
  - Suggested, because the HD evidence is 3-4σ and n_LB is uncertain by a factor of a few.
- **Branch T in the PTA band.** Waves propagate with k² = ω² + M², but the Galaxy is tachyonically unstable on ~1,000 AU scales (growth time 6 days at 1 cm⁻³; `f2_common.out:8`). Not computed further.

### 3.5 Binary pulsars (`S/f2_galaxy_ns.py` iii)

- **Source decomposition** (proved, Newtonian). The far-zone amplitude is ∫Ψ_in τ_ij, by reciprocity. Here Ψ_in solves the homogeneous equation with the medium mass term and is a plane wave at infinity. For a binary:
  - ∫τ_ij = μ v_i v_j (matter at the stars) − μ(GM/r) n_i n_j (field stress spread over ~r);
  - on circular orbits the 2Ω parts are equal, −μv²(nn)_osc each.
  - Screening the stars (Ψ_in → s inside) multiplies the amplitude by (1 + s)/2.
- **Born limit** (proved). 1 − s = (μ_ρ/(ħc)²)⟨|Φ_N|⟩/(4πG), where ⟨|Φ_N|⟩ = 2|W|/M. The uniform-sphere check is 1 − s = 0.4(mR)².
- **Hard sphere** (proved). s = 3(mR − tanh mR)/(mR)³.
- **NS inputs.** 1.3 M☉ and 12 km (n = 1 polytrope) give ⟨|Φ|⟩ = 0.24c² (`:19-21`).
- **Bound.** |1 − s| ≤ 1.3e-4 gives μ_ρ ≤ 1.97e-43, i.e. |m_g(ρ_NS)| ≤ 2.65e-13 eV.
- **Placeholder.** mR = 1.2e9, so the star is a hard sphere and the power factor is 0.25 (`:28-29`).
- **Caveats (suggested only):**
  - the stars' self-field stress outside their surfaces is still weighted by (1 − R/r), which gives O(compactness ≈ 0.16) corrections to s;
  - a position-dependent TT mass is not diffeomorphism-consistent;
  - GR strong-field effacement is not modelled.

  None of these turn an O(1) change into 1e-4.
- **Also applies to GW170817's inspiral** (not computed).

### 3.6 Hot early universe (`S/f2_cosmo.py`)

- **Reproduction** (checked; `f2_cosmo.out:2-7`). R19-34's A(T) is reproduced to every printed digit.
- **Extension** (checked arithmetic; `:8-16`). Adding u, d, s, the leptons and thermal plus asymmetric nucleons gives A from −2.3e13 (150 GeV) to −1.5e18 (1 MeV). Hadronic scalar densities are omitted below T_QCD, so this is partial.
- **Branch T.**
  - N = ∫√|A| d ln T = 2.0e9 e-folds over 150 GeV → 1 MeV (`:24`).
  - Super-horizon modes grow as t^p with p = 2.7386e6 at A = 3e13, the same rate (`:25`).
- **Ceiling (assumptions stated).**
  - The seed is the graviton vacuum in the band p < |m_g|, ρ_seed = |m_g|⁴/(8π²).
  - The grown energy must stay below f_GW ρ_rad with f_GW = 0.04 (ΔN_eff < 0.3; larger earlier, so this is conservative).
  - The growth is linear until then.
  - Result: N_max = 66-95 (`:28-33`), i.e. |A| ≤ 4.4e3-8.2e3 for one e-fold, or 35-64 sustained over the whole era.
  - The sharper |A| ≲ 1-10 line is not observational.
- **Branch M** (`:41-43`).
  - While |m_g| > H, a super-horizon tensor oscillates and decays as a^(-3/2). On the placeholder that lasts until today (e^-51), so primordial tensors are erased.
  - This is consistent with the r upper limit. **There is no bound until a primordial B-mode is detected.**
  - Mass changes are adiabatic (|m_g| ≫ H), so particle production is negligible (suggested).
- **Today, branch T** (`:37-39`). |m_g| = 6.5e-25 eV = 4.5e8 H₀, with a 32-year e-folding. The ceiling is ~100 H₀, giving μ_ρ ≤ 4.9e-35.

### 3.7 Static potentials (case v)

- The E_g Hessian is traceless shear. A shear-only spatial mass term has a known comparator: Lorentz-violating massive gravity in the m₀ = 0 phase (Rubakov, hep-th/0407104; Dubovsky, hep-th/0409124; RECALLED). There, tensors are massive, Newton's potential is unmodified at linear order, and there is no vDVZ jump. In that case fifth-force tests bound nothing.
- R19-34's dilation check (d²δm/dh² = +δm; `rR19-34:97`) shows that the H-cov law also responds to trace strain. Whether that is a physical breathing stiffness or a units rescaling is not determined.
- If it is physical and screens Ψ, the same Born formula and Cassini give μ_ρ ≤ 1.3e-39 (`f2_galaxy_ns.out:33`).
- Status: conditional, suggested.

## 4. What this means for reading F1 (reading, not a verdict on F1)

- **Usable observational lines, either sign:**
  - Earth crossing, μ_ρ ≲ 1.5e-29 (checked; the strongest *checked* row);
  - the detector on the ground (checked);
  - binary pulsars, ≲ 2e-43 (suggested).
- **Tachyonic sign only:**
  - the hot era, |m_g²|/H² ≲ 1e3-1e4 per e-fold (checked arithmetic);
  - today's cosmic mean, |m_g| ≲ 100 H₀ (suggested).
- **Massive sign in the hot era:** no observational line. "|m_g| < H" is a theory line there, not an observed outcome. F1's SF-HAZARD clause "beyond an observational bound in at least one epoch or environment" must use the today rows for the massive sign.
- **Massive sign today:** the PTA row (suggested) and the Earth rows (checked).
- **A density-proportional channel** cannot pass the Earth rows unless its coefficient is ≲ 1.5e-29 eV² m³/kg. The binary-pulsar row asks for ≲ 2e-43 (suggested). Any F1 result should be converted to μ_ρ and read against rows 1, 8 and 9.

## 5. Prior art (counted once)

- **R19-34** (`rR19-34:16-18, 147-152`; `vR19-34` item 5): sizes and mapping, reproduced here.
  - New here: the propagation calculations; the sign consequence (no evanescence in branch T); the decay-length correction.
- **R19-21** (`rR19-21:206, 211`; `vR19-21:26`):
  - the massive-branch "r ≈ 0 allowed" entry, counted once and now made explicit as "no bound";
  - "GWs could not cross the Earth (suggested; not checked against event geometry)", now checked with GW170817.
  - The GWTC-4.0 value of 1.92e-23 eV is cited from vR19-21.
- **R19-31** (`vR19-31` item 5): the 100 GeV size, reproduced.
- **Comparators:**
  - the PTA minimum-frequency mass bound (Wu et al.), whose vacuum version this generalizes to a density-dependent mass;
  - Lorentz-violating massive gravity (Rubakov / Dubovsky; RECALLED);
  - spontaneous-scalarization-type tachyonic growth in compact stars (Damour–Esposito-Farèse; RECALLED), the analogue of row 3 and row 8 in branch T.

## 6. Strong words and limits

- **"Checked":** row 1 (1D exact transmission on PREM chords), row 2, row 3's threshold, row 9's arithmetic, and the R19-34 reproduction.
- **"Proved":** the single-step surface factor, the Born and hard-sphere screening formulas, the circular-orbit half/half decomposition, and the growth-exponent formula. All are short and unrefereed.
- **Not claimed:**
  - 3D refraction or whispering-gallery effects (they matter in branch T, n ≈ 6e3);
  - TT–scalar mixing in gradients;
  - any nonlinear end state;
  - the exact LVK likelihood (thresholds are stated: S ≥ 0.7, and the GW170817 1/f-phase budget);
  - the in-medium nucleon scalar density at nuclear density (O(1));
  - hadronic scalar densities below T_QCD.
- **External numbers:** the ones marked WEB were checked in this run. NGC 4993 and site coordinates, PREM, Cassini, the Local Bubble density and the Galactic columns are RECALLED.

## 7. Files (`S/` = `scratchpad/C5/F2/scripts/`)

- `f2_common.py/.out`: constants, PREM (checked M and I), the placeholder μ_ρ.
- `f2_earth.py/.out`: geometry, chord transmission and bound, placeholder on the chords, detector on the ground, Earth instability.
- `f2_cosmo.py/.out`: A(T) reproduction and extension, growth exponent, N_eff ceiling, today in branch T, branch M damping.
- `f2_galaxy_ns.py/.out`: LVK column bound, arrival time, PTA Local Bubble, binary-pulsar screening, static (conditional).

## Sources (WEB, this run)

- [Tests of General Relativity with GW170817 (arXiv:1811.00364)](https://arxiv.org/pdf/1811.00364): m_g ≤ 9.51e-22 eV.
- [GW170817 observation (arXiv:1710.05832)](https://arxiv.org/pdf/1710.05832.pdf): 12:41:04 UTC, network SNR 32.4. H1/L1 SNR 18.8/26.4 via [arXiv:1812.06100](https://arxiv.org/pdf/1812.06100).
- [Multi-messenger observations (arXiv:1710.05833)](https://arxiv.org/pdf/1710.05833).
- [Kramer et al. 2021, Strong-field gravity tests with the double pulsar (arXiv:2112.06795)](https://arxiv.org/abs/2112.06795): quadrupole formula to 1.3e-4 (95%).
- [Wu et al., Constraining the graviton mass with NANOGrav 15-yr (arXiv:2310.07469)](https://arxiv.org/pdf/2310.07469): m_g < 8.2e-24 eV.
- [NANOGrav 15-yr evidence for a GWB](https://authors.library.caltech.edu/records/mrtaw-spj56).
- [BICEP/Keck 2021, PRL 127 151301 (arXiv:2110.00483)](https://arxiv.org/pdf/2110.00483.pdf): r₀.₀₅ < 0.036.
- [Pagano et al. 2015 (arXiv:1508.02393)](https://export.arxiv.org/abs/1508.02393): Ω_GW h² < 1.7e-6. [arXiv:2202.05105](https://arxiv.org/pdf/2202.05105): ΔN_eff ≲ 0.3, Ω_GW h² ≲ 1.6e-6.
- GWTC-4.0 graviton mass 1.92e-23 eV: [LIGO-P2500066](https://dcc.ligo.org/LIGO-P2500066/public), as cited in `vR19-21:26`. Not re-fetched in this run.
