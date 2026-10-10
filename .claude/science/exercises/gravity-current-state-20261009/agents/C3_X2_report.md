# C3 lane X2: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. Codex sol referee: pending if the verdict is a FAIL or no-go.

**Verdict (worker):** FAIL against the fixed reading, bounded to the models tested. Every model has Re G_T(0) != 0, or n <= 1, or both. The two FR3 gases have a stationary law that is exactly independent of the metric. So their configurational TT stress has Re G_T(0) = 0 and Im G_T identically 0, but its noise is white, S(0) > 0, giving n_S = 0. The activity (traffic) stresses have an exact instantaneous response, Re G_T(0) = -0.0700 (swap gas) and -0.1000 (wind gas) per site, and S(0) > 0. E2's frozen dilution has Re G_T(0) = +0.09 to +0.19 per site. B2's predicted FAIL holds, but its predicted route (n = 1 through FDT) does not occur: FDT's conditions fail for both gases, and the measured Im G_T is identically zero. Needs the codex sol referee before it is recorded.

**Plain summary:** A gravitational-wave-like stretch of space was made to change how fast records hop along each axis. For FR3's swap and wind gases, and for E2's diluted grid, I measured two things separately: how the shear stress responds to the stretch, and how much it jitters at low frequency. In both gases the stretch leaves the long-run statistics exactly unchanged. So a stress built from the configuration has no response at all (no stiffness, no friction), but it still jitters with flat (white) noise down to the lowest frequency; for the swap gas that noise is 0.00668 per site, computed exactly. If the stress is instead the hop traffic itself, it follows the stretch instantly, which is a nonzero static stiffness (-0.070 and -0.100 per site), and the diluted grid keeps its known stiffness (+0.09 to +0.19 per site). Every model therefore fails the fixed reading. The cause is noise without dissipation, not the n = 1 friction that B2 predicted from the fluctuation-dissipation theorem; that theorem does not apply here, and the measured dissipative response is exactly zero.

# X2: response of a classical record gas (Campaign C3, lane X)

**Worker:** Claude Opus 5.5 (max effort).
**Pre-registration:** `PREREG.md`, stamped Sat Oct 10 00:59:14 UTC 2026, before any computation.
**Work done:** 00:59Z to 01:19Z.
**Fixed readings (TESTS.md, C3, X2; not changed):**
- **PASS:** some model has Re G_T(0) = 0, with S and Im G_T both vanishing as ω^n, n ≥ 3, untuned.
- **FAIL:** every model tested has Re G_T(0) ≠ 0 or n ≤ 1.
- **INCONCLUSIVE:** otherwise.

## Verdict: FAIL (bounded to the models tested; needs the codex sol referee)

Every tested model (dynamics + coupling + stress definition) fails at least one fixed criterion:
- either Re G_T(0) ≠ 0;
- or S(ω → 0) > 0, i.e. n_S = 0.

Most fail both. B2's predicted FAIL holds, but **not by B2's predicted route**:
- the gases show **noise without dissipation**: Im G_T is identically 0 (EXACT), not ∝ ω;
- FDT does not apply, because its conditions fail (section 3).

This confirms and sharpens referee item 13: S(0) > 0 is not n = 1, and here Im G_T ≡ 0.

## 1. What I read (in full)

- **Axioms and registry:**
  - `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines);
  - `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`.
- **Packet:**
  - `TESTS.md`: the rules, E2/E3 and their results, all of Campaign C3;
  - `SUMMARY.md` (all);
  - `agents/B2_report.md`: §1 (blocks, c1, c2) and §5 (T-3);
  - `agents/B_referee.md`: items 13, 17, 18 and ranked test 4.
- **FR3 code and record:**
  - `scratchpad/test_FR3/fr3_lg.c` and `run_all.sh`;
  - the FR3 entry and referee corrections in the candidate pack's `TEST_LOG.md`.
- **E2 code and output:** `scripts/E23/e23_core.py`, `E2_1_nn.out`.
- **No downloads.** No repository file was edited.

## 2. Setting and hypotheses (as pre-registered; test setting only)

**Models.** Each runs on a torus L³ in continuous time.
- **M1: swap gas** (FR3 mode 0, SSEP).
  - Each record tries a hop at rate 1/6 per direction; the hop succeeds only into an empty site.
  - Densities ρ = 0.3 (FR3's) and 0.1.
- **M2: wind gas** (FR3 mode 1). The record's content is its direction of travel.
  - Streaming along e_d at rate 1: into an empty site the record moves; into an occupied site the two contents are exchanged.
  - Bond collisions at γ = 1: an opposite pair goes to a random opposite pair; any other occupied pair is exchanged with probability ½.
  - ρ = 0.3.
- **M3: E2's frozen dilution (nn).**
  - Free scalar on the present sites; m² = 1 and 0.04; quantum ground state.
  - p = 1, 0.9, 0.5; L = 8 and 10.
- **M3b: the M1 swap gas living on E2's frozen dilution** (p = 0.7, L = 16).
  - Added after pre-registration, as the other reading of "frozen dilution with hop rates".
  - It only adds a model, so it is conservative for a FAIL.

**Coupling (fixed by the task).**
- The metric is g = exp(h), with h = ε(t)ĥ.
  - E_g: ĥ = diag(1,−1,0)/√2.
  - T_2g: ĥ = (E_xy + E_yx)/√2.
- Every hop or stream rate along axis e, and in M3 every nn coupling, is multiplied by c_e = e·g⁻¹·e.
- M2 variant: collisions on e-bonds are scaled by c_e as well.

**T_2g is vacuous for six-axis hops** (EXACT).
- c_x = c_y = cosh(ε/√2) is even in ε, so there is no linear coupling.
- The xy stress of axis hops is identically 0.
- So T_2g cannot pass a model. FR3 already found the × polarisation absent.

**Stress observables** (per site, T = Σ ĥ_ij T_ij):
- **S1, activity count** (B2's "activity anisotropy"): hop events along e per unit time, weighted e_ie_j, as a counting process.
- **S2, activity intensity:** Σ_e c_e(t)·r₀·B_e, the conditional intensity of S1.
  - M1: B_e is the number of bonds along e with exactly one end occupied, and r₀ = 1/6.
  - M2: B_e = n_e, the number of records with content ±e, and r₀ = 1.
- **S3, rate-stripped:** r₀·B_e.
  - For diagonal h this equals traffic × (proper step)², since c_e·g_ee = 1.
  - For M2, S3 is the content (momentum-flux) stress, so S3 = S4.
- **M3:** T = ∂H/∂ε.

**Hypotheses.**
- **H1:** the metric acts only through rates. The gas has no Hamiltonian, so its stress is supplied by definition, not derived.
- **H2:** zero momentum; finite periodic boxes.
- **H3:** linear response about the h = 0 stationary state.

## 3. Method

**Simulator:** `x2gas.c`, built from `fr3_lg.c`, modes 0 and 1.
- Exact continuous time: exponential waiting times, with Lewis–Shedler thinning for the time-dependent rates, c_max = e^{|ε|/√2}.
- Incremental counters for B_e and n_e, checked against a full recount at the end of every run: 0 mismatches over 212 runs.
- The initial state is drawn from the stationary law (Lemma A below).

**Response by direct perturbation.**
- h(t) = ε·cos(ωt), with ω ∈ {0, 0.003, 0.01, 0.03, 0.1, 0.3, 1}.
- Antithetic ±ε runs share seeds, with ε = 0.2. Linearity check at ε = 0.1 (ω = 0 and 0.03).
- G′ and G″ are projections onto cos and sin over whole periods, with bin-average (sinc) corrections.
- L = 16, T = 4000, 4 seeds. 16 seeds at ω = 0.003 and 0.03.

**Noise.**
- Stationary runs at h = 0:
  - L = 16, 24, 32 with T = 4000 (4, 4 and 2 seeds);
  - L = 16 with T = 40000 (4 seeds) and L = 24 with T = 40000 (2 seeds);
  - M3b on 4 dilution realisations.
- S(ω) = |∫X e^{iωt}|²/(VT) for the extensive E_g stress, using periodograms, Welch averages over segments of 4000, and batch means S_τ = Var(∫_block X)/(Vτ) as a direct S(0) estimator.
- Every number is reported **per realisation**.

**Exact checks.**
- `x2_exact_small.py`: full generators on L = 3 with N = 2. It checks stationarity and reversibility under anisotropic rates, solves for π, and gives the Kipnis–Varadhan S(0).
- `x2_ssep_exact_S0.py`: S3(0) for M1 by SSEP two-particle duality.
- `x2_m3_frozen_dilution.py`: E₀(ε) by finite differences (d = 0.02) at fixed realisations.

**FDT conditions** were checked before any use. No FDT was invoked.

## 4. Exact structure

**Lemma A: the stationary law does not see the metric.** EXACT, CHECKED.
- **M1 and M3b:** the rate factor c_e multiplies both directions of every bond. The generator stays symmetric, so the uniform law on configurations (fixed N) is stationary for every c and every time-dependent c(t).
- **M2:** for each content d, streaming is a TASEP for d-records that swaps with any non-d site.
  - The inflow to a configuration counts "non-d then d" boundaries along e_d; the outflow counts "d then non-d" boundaries.
  - These are equal on every ring, so the uniform law is invariant for **any** per-direction rates, including c_{+x} ≠ c_{−x}.
  - Collisions are doubly stochastic among opposite pairs, and symmetric swaps.
- **Consequence:** starting stationary, the law is the same at every time, for any h(t). So **every state-function stress has exactly zero response**, at all ω and all orders.
- **Exact generator check (L = 3, N = 2):**
  - inflow minus outflow ≤ 1.3e-15 at every state, for 4 rate settings (isotropic; E_g d = 0.3; collisions scaled; random c_{±e});
  - in the largest closed class (378 states), the solved π equals uniform to 3e-14, and ⟨q⟩ = 0 to 1e-15;
  - swap gas: ⟨B_x − B_y⟩_π = 1e-17 under anisotropy.
- The same argument covers FR3's vacancy crystal: Metropolis rates times a symmetric c_e keep detailed balance with the same Gibbs law. That model was not simulated (ARGUED from the lemma).

**Lemma B: activity stresses have a pure contact response.** EXACT, CHECKED.
- ⟨S1(t)⟩ = ⟨S2(t)⟩ = Σ_e ĥ_ee·c_e(t)·r₀⟨B_e⟩_π/V.
- So G_T(ω) = −r₀⟨B_e⟩/V for every ω. It is real and constant, and Im G_T ≡ 0.
- M1: −(1/6)·2N(V−N)/(V(V−1)) = **−0.070023** at ρ = 0.3, V = 4096.
- M2: −N/(3V) = **−0.100016**.

**Lemma C: zero-frequency noise is strictly positive.** EXACT; standard Markov-chain CLT (Kipnis–Varadhan), so COMPARATOR as to provenance.
- **State functions:** for a finite irreducible chain with stationary law π and any non-constant state function T,
  S_T(0) = 2⟨T, (−Q)⁻¹T⟩_π = Σ π(η)·k(η→η′)·(u(η′) − u(η))² > 0, where −Qu = T − ⟨T⟩.
  - Reversibility is not needed.
- **Counting stresses:** S1 is not a coboundary. One record hopping +x then −x closes a loop with net TT count 2. Hence S1(0) > 0.
- **Conserved stresses:** a conserved stress (the swap gas's inert labels) gives an atom at ω = 0. By the pre-registered convention (B2's "frozen dilution has n = 0") that counts as S not vanishing.
- **Exact small values:** S_q(0) = 24.0 (wind gas, L = 3); S(0) = 1.055 (swap gas, L = 3).

**Exact S3(0) for M1, per site, thermodynamic limit.** EXACT.
- Duality gives S3(0) = 8·r₀²·ρ²(1−ρ)²·ΔG.
- ΔG = 0.682054 is the occupation-time difference of the two-particle relative walk. It is the same to 1e-6 at L = 16, 24, 32 and 48.
- S3(0) = **0.006684** at ρ = 0.3 and **0.001228** at ρ = 0.1.

## 5. FDT conditions (checked; FDT not invoked)

| Model | (i) detailed balance at h = 0 | (ii) h enters as a potential, k_h(η→η′)/k_h(η′→η) = k₀-ratio·e^{βhΔB} | FDT usable? |
|---|---|---|---|
| M1, M3b | yes (generator symmetric; max\|Q−Qᵀ\| = 0) | **no**: the ratio is h-independent, so the perturbation is purely kinetic ("frenetic") | **no** |
| M2 | **no** (TASEP streaming has no reverse move; max\|Q−Qᵀ\| = 2.0–2.6 with π uniform and unique in its class) | no | **no** |
| M3 | Hamiltonian ground state | yes | yes (T = 0 quantum FDT); not needed, since Re G_T(0) was computed directly |

**What was measured instead:** S(0) > 0 together with G_T ≡ 0 (S3), or G_T a real constant (S1, S2).
- That is an infinite effective temperature: noise with no dissipation.
- B2's "n = 1 from shot noise" assumes an FDT that fails here.

## 6. Results

### 6a. Response G_T(ω), E_g, per site; mean ± s.e. over seeds

**M1, swap gas (ρ = 0.3, L = 16, ε = ±0.2).**
- Exact contact at finite ε: −0.07026 at ω = 0 (factor sinh(a)/a) and −0.07019 for ω > 0 (factor 2I₁(a)/a), with a = ε/√2.

| ω | S1 G′ | S1 G″ | S2 G′ | S2 G″ | S3 G′ | S3 G″ |
|---|---|---|---|---|---|---|
| 0 | −0.07024 ± 9e-5 | 0 | −0.07022 ± 5e-5 | 0 | +4e-5 ± 6e-5 | 0 |
| 0.003 (16 seeds) | −0.07019 ± 1.1e-4 | −3e-5 ± 7e-5 | −0.07013 ± 3e-5 | −4e-5 ± 2e-5 | +4e-5 ± 3e-5 | −4e-5 ± 2e-5 |
| 0.03 (16 seeds) | −0.07013 ± 5e-5 | −2e-5 ± 6e-5 | −0.07018 ± 2e-5 | −1e-5 ± 1e-5 | +1e-5 ± 2e-5 | −1e-5 ± 1e-5 |
| 0.1 | −0.07012 ± 9e-5 | +1.3e-4 ± 5e-5 | −0.07013 ± 5e-5 | +3e-5 ± 2e-5 | +5e-5 ± 5e-5 | +3e-5 ± 3e-5 |
| 1.0 | −0.07025 ± 1.0e-4 | +6e-5 ± 4e-5 | −0.07022 ± 3e-5 | +2e-5 ± 4e-5 | −2e-5 ± 3e-5 | +3e-5 ± 4e-5 |

**M2, wind gas (ρ = 0.3, γ = 1, L = 16).**
- Exact contact: −0.10036 at ω = 0, −0.10029 for ω > 0.

| ω | S1 G′ | S2 G′ | S2 G″ | S3 = S4 G′ | S3 G″ |
|---|---|---|---|---|---|
| 0 | −0.10034 ± 4e-4 | −0.10038 ± 4.6e-4 | 0 | −2e-5 ± 4.5e-4 | 0 |
| 0.003 (16 seeds) | −0.09949 ± 4.4e-4 | −0.09959 ± 3.9e-4 | +3.8e-4 ± 3.9e-4 | +6.2e-4 ± 3.8e-4 | +3.9e-4 ± 3.9e-4 |
| 0.03 (16 seeds) | −0.09978 ± 2.6e-4 | −0.09989 ± 2.1e-4 | −3e-5 ± 1.8e-4 | +3.5e-4 ± 2.1e-4 | −4e-5 ± 1.8e-4 |
| 1.0 | −0.10032 ± 2.6e-4 | −0.10031 ± 1.5e-4 | −1e-5 ± 2.7e-4 | −1e-5 ± 1.5e-4 | −1e-5 ± 2.7e-4 |

**Also checked:**
- Linearity: ε = 0.1 agrees with ε = 0.2.
- M2 with collisions scaled by c_e: unchanged.
- M3b (dilution p = 0.7, two realisations): S1/S2 G′ = −0.0340/−0.0341 and −0.0330/−0.0332, against exact −0.03402 and −0.03316; S3 is within ±2e-4.
- **Every S3 entry is within ±2e-4 of 0** (M2 ≤ 6e-4), i.e. ≤ 0.6 % of the contact term. A few 4-seed entries sit at 2–4 nominal σ with only 3 degrees of freedom; the 16-seed entries are at ≤ 1.7σ.
- **All G″ are 0 within errors** at every ω, consistent with Im G_T ≡ 0 (Lemmas A and B).

### 6b. Noise S(ω → 0) at h = 0, E_g, per site, per realisation

**M1, S3** (exact 0.006684):
- L = 16, T = 4e4, batch means τ = 100: 0.00690, 0.00665, 0.00697, 0.00676.
- Welch lowest band ω ∈ [0.0015, 0.005): 0.0061, 0.0077, 0.0070, 0.0058.
- L = 24, τ = 100: 0.0065, 0.0070, 0.0067, 0.0054.
- L = 32: 0.0086, 0.0094.
- ρ = 0.1, τ = 100: 0.0012, 0.0017 (exact 0.001228).

**M1, S1:** τ = 100 gives 0.081, 0.086, 0.074, 0.073.
- That matches the exact shot part 0.0700 plus about 0.0067 from S3.

**M2, S3 = S4** (content stress):
- L = 16, T = 4e4, τ = 100: 0.544, 0.466, 0.522, 0.467.
- Welch lowest band: 0.61, 0.45, 0.56, 0.46.
- L = 24, τ = 100: 0.458, 0.542.
- L = 32: 0.59, 0.47.

**M2, S1:** 0.647, 0.579, 0.593, 0.578.
- That matches the shot part 0.100 plus about 0.5 from S3.

**M3b, S2** (4 dilution realisations): 0.005–0.009.

**Log-slopes between the two lowest Welch bands** (ω ≈ 0.0027 → 0.0087), per seed:
- M1 S3: +0.07, −0.09, +0.07, +0.36.
- M2 S3: −0.19, +0.15, −0.25, +0.02.
- So the spectrum is white: n_S = 0, read directly from resolved plateaus with no extrapolation.
- The per-site plateau agrees across L = 16, 24 and 32, so the noise is extensive (CHECKED).

### 6c. M3: E2's frozen dilution, Re G_T(0) = d²E₀/dε² per present site, per realisation (CHECKED)

- **Crystal (validation):** E_g = +0.16770 (m² = 1) and +0.17739 (m² = 0.04). These equal E2's values to 5 digits. T_2g = +0.18319, which is E2's −0.18319 with the sign flipped because e·g⁻¹·e gives cosh where E2's 1/(e·g·e) gives 1/cosh. It is nonzero either way.
- **p = 0.9, m² = 1:** E_g = +0.1567, +0.1560, +0.1539, +0.1559; T_2g ≈ +0.171 to +0.173.
- **p = 0.5, m² = 1:** E_g = +0.1013, +0.0959, +0.0989, +0.0984; T_2g ≈ +0.118 to +0.121.
- **L = 10:** p = 0.9 gives +0.157 and +0.154; p = 0.5 gives +0.091 and +0.090.
- **Gap:** the stress is quadratic in φ, so Im G_T = S_dyn = 0 below the two-phonon threshold 2m (EXACT). The threshold is 2.0 for m² = 1 and 0.4 for m² = 0.04.
- **Static disorder:** each realisation carries a frozen static E_g stress (E′ = ±1e-4 to 1e-2 per site, white across realisations; E2 refereed sd·√N = 0.086 at p = 0.5). That is an ω = 0 atom.

## 7. Mapping onto the fixed reading

| Model / stress | Re G_T(0) | Im G_T | n_S | Fails on |
|---|---|---|---|---|
| M1 S1, S2 | −0.0702 (EXACT −0.0700) | ≡ 0 | 0 | both |
| M1 S3 | 0 (EXACT) | ≡ 0 | 0 (S(0) = 0.006684, EXACT) | n ≤ 1 |
| M2 S1, S2 | −0.1003 (EXACT −0.1000) | ≡ 0 | 0 | both |
| M2 S3 = S4 | 0 (EXACT) | ≡ 0 | 0 (S(0) ≈ 0.5) | n ≤ 1 |
| M3 (scalar) | +0.09 to +0.17 (E_g); +0.11 to +0.19 (T_2g) | 0 below 2m | ω = 0 atom | Re G_T(0) ≠ 0 |
| M3b S1, S2 / S3 | −0.034 / 0 | ≡ 0 | 0 | both / n ≤ 1 |

T_2g is vacuous for M1, M2 and M3b (no coupling, stress ≡ 0), and E_g decides.

**Every tested model fails, so the reading is FAIL.**
- The FAIL does not depend on the stress definition.
- Without the traffic contact term (which a referee may regard as a coordinate artifact), the noise criterion alone fails every gas model.

## 8. Strongest correct statement

**What holds.** Under B2's T-3 coupling (hop rates × e·g⁻¹·e):
- the swap and wind gases, and the swap gas on a frozen dilution, are exactly shape-blind in their statistics: no static stiffness and no viscosity of any configurational stress;
- they fail on noise: white zero-momentum TT stress noise, S(0) > 0;
- traffic-type stresses add an instantaneous static response;
- E2's frozen dilution keeps its static stiffness.

**General part (Lemma C).** Any classical finite-state Markov substrate has S_T(0) > 0 for every non-constant, non-conserved state-function stress at finite volume.
- So n ≥ 3 can only arise from stresses whose per-volume S(0) vanishes in the infinite-volume limit (ARGUED; not seen in any local stress here).

**What it does not show.**
- Other couplings: potential-type couplings, rates not of the form e·g⁻¹·e, or coupling through record formation.
- Nonzero momentum.
- Quantum or coherent substrates (B2's C).
- That every classical spatial record substrate fails; B2's "decides D" wording is broader than this test.
- A stress of the form T = dF/dt (a time derivative of a state function) would have Re G_T ≡ 0 and S_T = ω²S_F, i.e. n = 2, which sits between the readings (ARGUED). It was not pre-registered and is not a natural stress (its time integral is bounded, so it carries no net momentum flux). A stress set identically to 0 would pass only vacuously (no coupling), and was not tested.

## 9. What a referee should re-check

1. **The stress definitions,** and treating each (dynamics, coupling, stress) as a separate model.
   - Is the traffic contact term (S1/S2) a genuine mass, or the tensor transformation of an isotropic activity? The verdict holds either way, via S3.
2. **Lemma A for the wind gas:** the boundary-counting argument, with fr3_lg.c's rule (exchange into occupied sites), and the exact L = 3 check.
3. **Thinning, the antithetic estimator and the finite-ε factors** (sinh(a)/a; 2I₁(a)/a).
4. **The duality formula** S3(0) = 8·r₀²·ρ²(1−ρ)²·ΔG with ΔG = 0.682054, against simulation (0.00682 vs 0.006684).
5. **FDT inapplicability:** the perturbation is kinetic, not potential (M1), and M2 is not reversible.
6. **M3:** the e·g⁻¹·e versus 1/(e·g·e) sign flip in T_2g. Also whether the ω = 0 atom convention, taken from B2, is acceptable; M3 fails on Re G_T(0) ≠ 0 regardless.
7. **Whether c1's bridge Π = 16πG·G_T applies** to a medium with no Hamiltonian. H1: the stress is supplied by definition, and no action-reaction is derived.
8. **M3b was added after pre-registration.** It only adds models, so it cannot by itself create a FAIL.

## 10. Files (absolute paths)

Scratch: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/X2/`

- **Pre-registration:** `PREREG.md`.
- **Simulators:** `x2gas.c` (+ binary `x2gas`) and `x2gas_dil.c` (+ `x2gas_dil`).
- **Job lists:** `run_all.sh`, `jobs_noise.txt`, `jobs_resp.txt`, `jobs_more.txt`, `jobs_long.txt`, `jobs_dil.txt`.
- **Analysis:** `x2_analyze.py` → `x2_analyze.out`; `x2_long.py` → `x2_long.out`.
- **Exact checks:** `x2_exact_small.py` → `x2_exact_small.out`; `x2_ssep_exact_S0.py` → `x2_ssep_exact_S0.out`.
- **Frozen dilution:** `x2_m3_frozen_dilution.py` → `x2_m3_frozen_dilution.out`; `x2_m3b_dil_gas.py` → `x2_m3b_dil_gas.out`.
- **Data:**
  - `data/noise/`, `data/long/` (plain text);
  - `data/resp/`, `data/dil/` (gzipped; the loaders read .gz);
  - consistency logs: `data/stderr*.log`.
- Every run is deterministic from its seed and the job lists; the whole set takes about 2 minutes on 4 cores.

---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** True

**Corrected verdict:** FAIL, bounded to the models tested and still pending the codex sol referee (C3 rules). The tested models are M1 swap gas, M2 wind gas, M3 frozen-dilution scalar and M3b swap gas on dilution, each with stresses S1–S4, under B2's T-3 coupling (hop rates times e·g⁻¹·e), at k = 0, in linear response about h = 0, on finite tori.

For every gas model the failing leg that holds up is the noise.
- The configurational (rate-stripped) stress has Re G_T(0) = 0 and Im G_T ≡ 0 at all ω, both exact by Lemma A.
- Its zero-frequency noise is white and strictly positive, so n_S = 0:
  - M1: S(0) = 0.006684 per site (exact);
  - M2: S(0) ≈ 0.5 per site.
- So the gases show noise without dissipation. Reading the reading's n as the common exponent (min of n_S and n_Im), this gives n ≤ 1 and FAIL.

The activity stresses (S1, S2) also fail on Re G_T(0) ≠ 0, but that leg is weaker.
- In E_g, Re G_T(0) is exactly −P, where P = r₀⟨B_e⟩/V is the isotropic traffic. This is because S2 = P·(g⁻¹)_ij for diagonal h.
- In T_2g the same stress gives 0. So part of the E_g value is a tensor (index-placement) term, and part is a real cubic anisotropy. Either way it fails, but noise is the leg to cite.

M3 fails on Re G_T(0) ≠ 0.
- Its E_g values are +0.09 to +0.17 and its T_2g values +0.11 to +0.19.
- This is a genuine shear stiffness: with g = exp(h), det g = 1 exactly, so an energy that depends only on the volume would give zero.

Not established by this test: B2's "decides D" (that no classical spatial record substrate can carry the geometry); other couplings; k ≠ 0; quantum substrates.

**Issues:** The verdict holds up. I found no error that would flip it. Corrections and caveats:

1. **The S1/S2 "mass" leg is partly bookkeeping.**
   - For diagonal h, S2 has T_ee = c_e·r₀·B_e/V = P·(g⁻¹)_ee. That is exactly an isotropic traffic tensor with upper indices, so Re G_T(0) in E_g equals −P (−0.0700 for M1, −0.1000 for M2).
   - It is not purely a pressure artifact. Axis hops have no xy component, so T_2g gives 0 for the same stress, and the E_g/T_2g split (−P against 0) is a real cubic anisotropy.
   - Still, the §7 entries "fails on both" should be read with the noise leg as the decisive one. This answers the worker's own referee question 1.

2. **What "n" means.** Im G_T ≡ 0 (no power law at all) while S(0) > 0 (n_S = 0). FAIL follows only if the reading's n is taken as the common exponent of S and Im G_T, as the PASS clause's "both" implies. The report should say this explicitly. I agree with that reading.

3. **Overclaim in §8.** "Exactly shape-blind in their statistics" is too broad. Only the one-time stationary law is metric-blind. Two-time correlations at h ≠ 0 depend on the rates. The response statements (no static stiffness, no viscosity of configurational stresses, in linear response about h = 0) are correct.

4. **The T_2g channel.** For a gas stress, T_2g passes vacuously (no linear coupling, S ≡ 0). It counts as no pass only because the convention "a model must pass every channel it couples to" was pre-registered (PREREG stamped 00:59:14Z, before the code at 01:01Z). That convention is physically sensible but should be stated as load-bearing. There is also an inconsistency: the M3 T_2g value comes entirely from the second-order cosh term, while for the gases T_2g is declared vacuous. It does not affect the verdict.

5. **M3 is not a classical record gas.** It is a T = 0 quantum ground state. Its "ω = 0 atom" is the realization-to-realization spread of the static stress, not noise within one realization; within a realization the connected S is zero below 2m. This does not matter, because Re G_T(0) ≠ 0 decides M3.

6. **Minor numerical points.**
   - The M1 S3 noise at L = 32 (0.0086 and 0.0094, from T = 4000 with 2 seeds) sits about 1.3σ and 1.8σ above the exact value. "The plateau agrees across L = 16, 24, 32" is loose for L = 32. My own L = 16 and L = 24 long runs agree with the exact value.
   - "S1 noise = shot part + S3" is only approximate: the cross term between the count fluctuations and the intensity need not vanish. The worker does say "about".
   - A few 4-seed G″ entries sit at 2–3σ. They are harmless given the exact zero.

7. **Lemma C wording.** The general statement needs "non-constant on the irreducible closed class". Positivity per site in the infinite-volume limit is shown only for the tested stresses: exactly for M1, numerically for M2. The worker labels the general part ARGUED, which is right.

8. **Provenance and scope.**
   - This check is same-family (Claude Opus 5.5, like the worker). Under the C3 rules the FAIL still needs the codex sol referee before it is recorded.
   - The scope is bounded to the T-3 coupling, k = 0 and linear response, as the worker states.

**Re-runs:** All checks are in /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/X2/verify/. No repository file was edited.

1. **Worker's exact scripts, re-run.** x2_exact_small.py and x2_ssep_exact_S0.py give output byte-identical to the worker's x2_exact_small.out and x2_ssep_exact_S0.out.

2. **lemmaA_local.py: Lemma A, checked independently.** Written from FR3's rule text, not from the worker's code. It tests inflow = outflow at random states, enumerating every one-bond predecessor.
   - Wind gas, L = 4 and 5, ρ = 0.4 and 0.7, random per-direction rates (c₊ₑ ≠ c₋ₑ) and per-axis collision rates: relative mismatch ≤ 2.3e-15.
   - Swap gas, symmetric anisotropic rates, on the torus and on a p = 0.7 dilution: mismatch 0.
   - Control (asymmetric rates on a dilution): mismatch 0.16–0.24, so the test can detect a failure. Asymmetric rates on the full torus are also stationary, by the ring argument.
   - The first run gave a false mismatch from a numpy bool-addition bug in my own script. After fixing it, everything matches.

3. **indep.c + indep_analyze.py: my own simulator.** M1 is run in the stirring (bond) representation and X is integrated exactly in time. 60 runs; the end-of-run recount matched in 60/60.
   - **M1 S3 noise S(0), h = 0, ρ = 0.3:**
     - L = 16, 16 seeds, T = 4e4: 0.00657 ± 0.00012 (τ = 100), 0.00655 ± 0.00026 (τ = 400);
     - L = 24, 4 seeds: 0.00654 to 0.00681;
     - worker's exact value: 0.006684.
   - **M2 S3 noise S(0):** 0.475 ± 0.016 (τ = 100) and 0.494 ± 0.023 (τ = 400), against the worker's ≈ 0.5.
   - **Static response at ε = ±0.4** (twice the worker's ε, which also tests beyond linear order):

     | | S3 response (Lemma A: 0) | S2 measured | S2 exact contact × sinh(a)/a |
     |---|---|---|---|
     | M1 | +1.0e-5 ± 0.9e-5 | −0.070948 ± 9e-6 | −0.070961 |
     | M2 | +2e-5 ± 4e-5 | −0.101314 ± 3.4e-5 | −0.101355 |

4. **m3_crystal_ksum.py: M3 crystal by a momentum sum.**
   - E_g: +0.16770 (m² = 1) and +0.17739 (m² = 0.04, L = 8; +0.17749 at L = 32 and 64).
   - T_2g with cosh weights: +0.18319 and +0.19819.
   - These match the worker's values and E2's.

5. **Analytic re-derivation.**
   - SSEP duality: under the Bernoulli law, Cov(η_a·η_b, P_x − P_y) = κ·[1 if b − a = ±e_x, −1 if ±e_y, else 0], with κ = ρ²(1−ρ)². The relative coordinate is a walk at rate 1/3 per direction with 0 excluded. This gives S3(0) = 8·r₀²·κ·ΔG, confirming the worker's formula.
   - S2 = P·(g⁻¹)_ij exactly in E_g, so its contact term is exactly −P.
   - Lemma C's Dirichlet-form positivity holds without reversibility.
   - FDT conditions: M1's perturbation is purely kinetic, and M2 is not reversible (Q is not symmetric while π is uniform). FDT therefore does not apply, as the worker says.
