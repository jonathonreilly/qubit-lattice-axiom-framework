# C5 round 14, probe R14-2: set A, start time (E1) against GW friction (E2), with the drag fixed (worker report)

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-12, 21:13Z to about 21:35Z. No repository file was edited.

**Scratch:** `scratchpad/C5/R14-2/`.
- `scripts/r142_checks.py` and `scripts/r142_checks.out` hold every number below. Runtime about 20 s with OMP_NUM_THREADS=2.
- SHA-256: script `9cefedc40af59a5f886004ff1b3623208ee5f3b824c4f7451500b38ece007e62`, output `6d7066ea948a2c4d63c15e8c526aea2ce3e6438850084d9f9b5ea23461059240` (recompute with `shasum -a 256`).
- No downloads. Two web lookups (abstract of arXiv:2112.06795; a search on the pulsar PPN bounds). Everything else is via earlier referees or RECALLED.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `vR13-6` = `P/agents/C5_R13-6_referee_verdict.md`, `refR13-6` = `P/agents/C5_R13-6_referee.md` (and so on); `out:N` = line N of `scripts/r142_checks.out`.

**What I read.** In full: `AX`; `TESTS:2302-2320` (C5 method); `TESTS:4779-4847` (round 14); the set-A entries `TESTS:3143-3180, 3409-3418, 3468-3481, 3559-3573, 3707-3738, 3909-3915, 3984-3998, 4218-4243, 4287-4296, 4325, 4438-4445, 4449-4462, 4518-4526, 4529-4560, 4682-4692, 4728-4732`; `C5_R13-6_report.md`, `vR13-6`, `refR13-6`; `C5_R12-7_report.md`, `vR12-7`, `refR12-7`; `vR11-5` and `C5_R11-5_report.md:225-236`; `vR6-4:17-19`. Scripts: `scripts/C5/R13-6/r136_checks.py` ([4], [6], [10], [11]); `scripts/C5/R12-7/r127_checks.py` ([4], [5], [9]) and its output.

**Labels.** **proved** (derived here under stated hypotheses); **checked** (a number in `r142_checks.out`); **suggested** (argued, not proved); **reading** (interpretation); **comparator** (literature: web-checked this run, via an earlier referee, or RECALLED).

**Subtraction rule.** Every rate, energy and spectral density below is positive, so the subtraction is none. The drag is the odd-in-ω part of the response. The even part exerts no force on a symmetric body and is not subtracted. Each script section prints its subtraction.

**Order rule.** All drag statements are at first order in γ (or in the gain's odd part), at Newtonian mean-field order, for v ≪ c. The budget is at second order in the matter–meter coupling (Gaussian), with R11-5's normalization.

---

## Reading against the FIXED readings (`TESTS:4829-4832`)

| Route | Worker reading | Why |
|---|---|---|
| **E1** (start time; gain repaired by P-r13b) | **OPEN** | Every stated observational test passes on a stated region (table §4.2), including the double-pulsar drag with the CMB velocity included. VIABLE is not reached, for four reasons:<br>(1) the spin-2 conserved-noise assembly is not built, so the budget's tensor weights are assumed O(1);<br>(2) PPN α₁, α₂ hold at linear order only, and no nonlinear completion exists;<br>(3) CP and ḣ regularity in the exact irrational limit are conditional (`vR13-6:27-31`);<br>(4) the budget passes only under the Isaacson premise. |
| **E2** (GW friction; same gain repair; ohmic friction kept, or repaired) | **OPEN** | **Not EXCLUDED.** The E2-h self-drag bounds γ ≲ 0.032–0.047 H₀ (checked; strong-field use suggested), and the class is non-empty below that. At γ ≲ 0.03 H₀ every stated test passes on the same footing as E1. VIABLE is not reached: E2 has E1's four gaps, plus no gravitating sink completion and no derivable PPN (`vR12-7:7,11`). |

**Answer to the owner's question 1 (reading).** Once both routes carry the same gain repair, and E2's friction obeys the drag bound, the two cannot be told apart by any stated test or by the near-cone budget.
- The budget differs by ≤ 8% in the strict variant and by about 1% in the τ_c variant (checked, out:72-80).
- At the drag-allowed ohmic γ, E2's damping time 2/γ is about 45–70 t_H. Its stationarity therefore needs a record history of tens of Hubble times. On a 1 t_H history E2 is E1 plus a few-percent friction (suggested).
- E2 stays a genuinely different law within the observed age only with a new repair (P-r14a below). That repair costs a frame time scale and a budget about 3× worse.
- **On the stated tests the two routes tie. E2 carries strictly more prices.**

---

## 0. In plain words

- **The friction route has the same braking problem as the start-time route, in a second form.**
  - E2's friction acts on the whole metric, including the Newtonian potential. A moving neutron star then drags its own potential behind it, which slowly brakes the star relative to the cosmic frame.
  - In the double pulsar both stars are braked. The orbit shrinks faster than radiation alone would make it.
  - The measured shrinkage agrees with Einstein's prediction to 1.3e-4. So the friction rate must be below about 3–5% of the Hubble rate.
- **That small friction is allowed, but it changes what E2 is.**
  - At 3% of the Hubble rate the friction needs about 70 Hubble times to settle. Within the universe's actual age it hardly acts.
  - So E2's claim to "no start time" holds only if records have been forming for dozens of ages of the universe. Otherwise E2 behaves like E1.
  - E2's distinctive prediction, gravitational waves fading with distance, shrinks to ≤ 1% at redshift 1. That is far below current sensitivity.
- **The brake can be removed the same way as E1's.**
  - Make the friction's memory average to zero. It then acts on fast waves but not on slowly moving stars.
  - The cost is a new time scale, about 1–3 ms, at which the friction turns on.
  - With that repair E2 can damp faster than the Hubble rate, so it is truly stationary today. Its energy dump (the sink) then grows, and the energy budget gets about 3× harder.
- **The energy budget is the same for both routes.** E1's growing record content at age t_H equals E2's stationary content at friction γ when t_H ≈ 0.56/γ. Earlier tables made E2 look about 2× worse; that came only from different bookkeeping conventions.
- **One correction to E1 (shared by E2).** The leftover brake from the repaired gain depends on the stars' speed through the cosmic frame (about 370 km/s), not only on their orbital speed. Including it tightens R13-6's τ_c ceiling from 2.4 mm to about 1.5 mm. The τ_c window then closes near ℓ ≈ 1.5e-9 m, not 4.3e-10 m.

---

## 1. Prior art (each counted once)

1. **R13-6 and its referee** (`vR13-6:3-44`; `refR13-6:36-131, 197-262`).
   - Lemma D: the gain's first moment gives a self-drag −(4πG/3)δ∫ρ²v. The literal F_u is EXCLUDED.
   - P-r13b (zero first moment) repairs it. The residual is profile-dependent, and the τ_c ceiling of 7.9 ps is profile- and orbit-model-dependent (`vR13-6:15`).
   - The E2-h drag Γ = 2γ|U|/(3Mc²) is confirmed. "Common-mode" is wrong, the bound is γ ≲ 0.03–0.04 H₀, and the status is suggested (`vR13-6:33-37`; `refR13-6:235-258`).
   - Unequal stars need the mass-weighted Γ_eff (`refR13-6:84-90`).
2. **R12-7 and its referee** (`vR12-7:3-17`).
   - E2-h is a causal, boost-stable telegraph law. The Lamb-string sink is a toy, with no gravitating completion. PPN is unclosed.
   - Lu et al.'s 2.98 H₀ is a fixed-distance benchmark; GW170817's EM counterpart gives about 62 H₀.
   - The budget optimum over γ ≤ H₀ is near 0.037–0.040 H₀ (`refR12-7:147-160`).
   - The drag formula is at `C5_R12-7_report.md:145`.
3. **R11-5** (`vR11-5:5-22`): Lemma C; the PPN and window scope; the premise-(ii) roots; the secular log of about 50–53 (`vR11-5:15`).
4. **R12-4** (`TESTS:4518-4526`): Theorem U, so a stationary model needs an undamped-pole escape. E2 is that escape.
5. **R6-4** (`vR6-4:7,19`): the lab window 4e-10 to 5e-6 m, and the record-reading prices on all four axioms.
6. **Repository grep** (this run) of `P/agents/`, `P/TESTS.md` and `P/SUMMARY.md` for "superohmic", "inerter", "zero-mean friction", "zero-integral", "high-pass" and "T_eq": **no hits**. `docs/` was not grepped.

## 2. Hypotheses (class ℰ₁₂, stated before any title)

- **H1.** Linearized Gaussian CQ gravity, mean GR coupling, preferred CMB frame, matter sourced through a frame-tied causal gain F = e^{−k²ℓ²/2}F_t(ω). Newtonian mean field for the drag. Symmetric bodies; v ≪ c.
- **H2 (E1).** As R13-6, E1-H1–H5 (`C5_R13-6_report.md:144-157`), with P-r13b: F_t = (1 − 4ix)(1 − ix)^{−4}, x = ωτ. Here τ = ℓ/c (strict) or τ_c (variant).
- **H3 (E2).** As R12-7, E-H1–H5 (`C5_R12-7_report.md:64-72`): (□ − γ(ω)u·∂)h̄ = −16πG J. The same P-r13b gain. Friction is either ohmic (γ constant) or **zero-integral (§3.4)**.
- **H4 (equal terms).** Both routes use the single-port saturated meter.
  - E1: Ĥ = (Ω² − ω²)^{−1/2}.
  - E2: Ĥ_γ = (Ω² − ω² − iγω)^{−1/2} (§4.3).
  - Both use the same ε profile, the same Isaacson premise and the same O(1) tensor weights.
- **Excluded realizations:** E2-TT (acausal, `vR12-7:9`); quantum FDT sinks; dynamical frames; nonlinear or strong-field completions; Lorentz-covariant gains (no Lemma-D drag, but they fail R8-3).

---

## 3. Probe (a): E2's self-drag, its bound, and its removal

### 3.1 The formula (proved in the linear model; checked out:3-5)

The setup is G_γ = 1/(k² − ω²/c² − iγω/c²) and a source moving uniformly, so ω = k·v. Then Im[k²G] = γω/(c²k²) + O(γ²), and the self-force F = −4πG∫d³k/(2π)³ k Im[k²G]|ρ̃|²/k² gives

  F = −(2γ|U|/(3c²)) v,  Γ_E2 = 2γ|U|/(3Mc²),

using ⟨k̂_ik̂_j⟩ = δ_ij/3 and 2|U| = ∫d³k/(2π)³ 4πG|ρ̃|²/k².
- An exact quadrature with the full propagator matches the first-order formula to 1e-6 (γ = 1e-4) and 1.2e-4 (γ = 1e-3) (out:3-4).
- The polytrope quadrature gives 0.08233 against 0.08234 (out:39).
- This agrees with `C5_R12-7_report.md:145` and `refR13-6:239-247`.

### 3.2 Each star, and the double-pulsar bound (checked out:8-20)

| R, model | Γ_A/γ | Γ_B/γ | Γ_eff/γ | γ_max |
|---|---|---|---|---|
| 11 km uniform / n=1 polytrope / LP binding | 0.072 / 0.090 / 0.079 | 0.067 / 0.084 / 0.073 | 0.069 / 0.087 / 0.076 | 0.040 / 0.032 / 0.037 H₀ |
| 12 km | 0.066 / 0.082 / 0.072 | 0.062 / 0.077 / 0.067 | 0.064 / 0.080 / 0.069 | 0.044 / 0.035 / 0.040 H₀ |
| 13 km | 0.061 / 0.076 / 0.066 | 0.057 / 0.071 / 0.061 | 0.059 / 0.073 / 0.063 | 0.047 / 0.038 / 0.044 H₀ |

- **Inputs.**
  - m_A = 1.338, m_B = 1.249 M_☉, P_b = 8834.535 s, |Ṗ_GR| = 1.2478e-12 (RECALLED, Kramer et al. 2021).
  - Agreement 1.3e-4 at 95% (comparator, web-checked abstract of arXiv:2112.06795). So Γ_eff < 6.12e-21 s⁻¹.
  - Γ_eff = (Γ_A m_B + Γ_B m_A)/M.
  - "LP binding" is the Lattimer–Prakash binding-energy fit 0.6β/(1 − β/2) (RECALLED). It is a strong-field proxy only.
- **At γ = H₀:** Ṗ_b/P_b = −(3.9 to 5.7)e-19 s⁻¹ against an allowed 1.84e-20, which violates the bound by ×21–31.
- **Bound: γ ≲ 0.032–0.047 H₀ across the structure models** (checked arithmetic). R13-6's worker estimate was 0.03 H₀ and its referee's 0.03–0.04 H₀.
- **Label of the bound: suggested.** E2-h has no strong-field completion, and Newtonian |U| applied to a neutron star is an uncontrolled extrapolation (`refR13-6:114-117`; `refR12-7:138-145`).
- A RECALLED one-sided reading of Kramer et al. (ratio 0.999963(63)) would tighten it about ×2. That reading is not used here.

**Orbital mapping (checked by direct integration, out:24-32).**
- With linear drag on absolute velocities, Ṗ_b/P_b = −3Γ_eff to 0.25%, for:
  - zero or nonzero CM velocity V;
  - e = 0.088;
  - unequal Γ, mass-weighted as the referee stated.
- The CM velocity drops out for linear drag.

**Companion term (proved in the linear model; out:21).**
- The friction-corrected companion field is the frame dipole δΦ₂ = (Gm₂γ/2c²)(v₂·r̂). Fourier inversion with ∫e^{ik·r}/k⁴ = −r/8π gives it, matching `C5_R12-7_report.md:141`.
- Orbit-averaged, it gives dE/|E| = +2γ(m_Am_B/M²)w²/c² = +2.2e-6 γ. That is an anti-drag about 6e4 times smaller than the self-drag, so it is negligible.

### 3.3 The gain's Lemma-D drag in E2

- E2 carries the same F_u (`C5_R12-7_report.md:67`). At first order the two odd parts add: Im[k²G_γF] = Im F + γω/(c²k²) (proved).
- So literal E2 is excluded by Lemma D exactly as E1 is (`refR13-6:260-262`). It needs P-r13b too.
- The residual of the repaired gain is identical in the two routes (§4.1).

### 3.4 Removing E2's drag "the same way" (proved: passivity and causality of the kernel; checked: poles, drag)

**The analogue of P-r13b.** Lemma D's drag is the first moment of the gain's impulse response. E2's drag is the **zeroth moment of the friction memory kernel**, γ(ω → 0). So set:

  K(t) = γ₀[δ(t) − ω_c e^{−ω_c t}]θ(t),  γ(ω) = γ₀(−iω)/(ω_c − iω),  Re γ = γ₀ω²/(ω² + ω_c²).

| Property | Result | Label |
|---|---|---|
| ∫K = 0 | −2e-16 (out:36) | proved; checked |
| Passive (Re γ ≥ 0 for all real ω) | yes (out:36) | proved |
| Rest-frame poles | max Im ω = −5e-16 over k ∈ [1e-4, 1e4], γ₀ ∈ [1e-3, 10], ω_c ∈ [1e-2, 1e2] (out:37) | checked |
| Boosted frames, β < 0.999 | 6000 random samples, max Im ω′ = −2e-13: no growing mode (out:38) | checked |
| Static limit, Newton | G(0, k) = 1/k² unchanged | proved |
| Near-cone record modes (ω ≥ 6e13 s⁻¹) | 1 − γ/γ₀ ≤ 3e-22 for ω_c ≤ 1e3, so E2's regulator is unchanged (out:47-48) | checked |

**The double-pulsar drag with the zero-integral kernel** (exact polytrope quadrature as a function of speed, orbit-averaged with V_CMB = 370 km/s; out:40-46):

| ω_c [rad/s] | 0 (ohmic) | 30 | 100 | 300 | 1000 | 3000 |
|---|---|---|---|---|---|---|
| allowed γ₀ | 0.035 H₀ | 0.059 H₀ | 0.15 H₀ | 0.73 H₀ | 7 H₀ | 62 H₀ |

- **The drag is removable.** ω_c ≳ 330 rad/s allows γ₀ = H₀. ω_c ≳ 500 rad/s allows γ₀ ≳ 2 H₀, so the damping time 2/γ₀ is shorter than t_H (interpolated).
- **Costs (named as price P-r14a, not adopted):**
  1. **A new frame time 1/ω_c ≈ 1–3 ms.** The friction kernel is signed, an "extrapolating" sink coupling. A passive realization is suggested: an inerter in series with the Lamb string, giving ω_c = Z/b (comparator, RECALLED: Smith 2002 inerter; Brune positive-real synthesis).
  2. **LIGO-band damping becomes frequency-dependent:** γ(f)/γ₀ = 0.016, 0.28 and 0.98 at 20 Hz, 100 Hz and 1 kHz for ω_c = 1e3 (out:48). That is a new predicted waveform distortion (suggested). The siren test now bounds γ(f_LIGO), not γ₀.
  3. **The budget gets worse** through the sink (γ₀/3H)ρ_GW: ×3 at γ₀ = 7 H₀ (out:72-80, last column). The τ_c lower end rises ×1.3–1.5.
- The repair is **not needed for any stated test**. The ohmic γ ≈ 0.03 H₀ sits at R12-7's budget optimum (`refR12-7:153-157`).
- What the repair buys is **stationarity within the observed age** (§4.4).
- **A second option, not developed (suggested only):** a Lorentz-invariant near-cone filter of the friction, f(s) = m/√(m² + s). It is passive, since Re f ≥ 0 on both sides of the cone. A Lorentzian m²/(m² + s) is not passive: it anti-damps a massive mode at rate γ/2. The residual drag is then about γGM/(c²ℓ_f) times a logarithm.

---

## 4. Probe (b): both routes on equal terms

### 4.1 A shared correction: the gain's residual drag depends on the CMB velocity (checked out:28-32, 51-54)

- R13-6's repaired gain leaves a cubic odd part, 20x³. The force is then −MΓ₃|u|²u on the **absolute** frame velocity u = V + w.
- Orbit-averaging gives Γ_eq = Γ₃(V² + V_∥² + w²), not Γ₃w². This is checked by integration: 0.994–1.000 of the prediction (out:28-31).
- R13-6 used v = 300 km/s (`C5_R13-6_report.md:396`; `vR13-6:15` flagged the dependence). With V = 370 km/s:
  - **strict τ = ℓ/c, ℓ = 5e-6 m:** Γ_eq = 2.3e-28 s⁻¹ (×3.8 over V = 0), still 7 decades below 6.1e-21. Pass in both routes;
  - **τ_c ceiling:** τ_c < 5.0e-12 s (cτ_c < 1.49e-3 m) with V in the orbital plane, and 5.8e-12 s (1.74e-3 m) with V normal. R13-6 had 7.9e-12 s (2.4e-3 m). At R13-6's ceiling the drag is 2.46e-20 s⁻¹, ×4 over the bound (out:53);
  - **the τ_c window** therefore closes at ℓ ≈ 1–2e-9 m (out:98-101), not at about 4.3e-10 m (`C5_R13-6_report.md:416`). It is open at ℓ ≥ 2e-9 m: about a factor 1.8 at 1e-8 m and 7–8.6 at 1e-6 to 5e-6 m (out:77-80, 99-101).
- Label: checked arithmetic within the smooth-polytrope, weak-field model; suggested as a bound (`vR13-6:15`). **This applies identically to E1 and E2.**

### 4.2 Every stated test, side by side

The tests are the union of `TESTS:4232-4237` (R11-5), `TESTS:4532-4537` (R12-7), `TESTS:4687` (R13-6) and R14-2(a). E2 is at γ ≤ 0.03 H₀ (ohmic) unless marked.

| Test | E1 (repaired) | E2 (repaired gain; ohmic γ ≤ 0.03 H₀) | Label |
|---|---|---|---|
| Cs-133 (70 s), LPF, corrected torsion | R6-4's window; finite-start corrections ≤ 1e-15 (`C5_R13-6_report.md:344`) | R6-4's window; lab kernels change ≤ 4e-85 (`C5_R12-7_report.md:138`) | checked (inheritance), scope `vR11-5:12` |
| Cassini γ | γ = 1, linear static | γ = 1 (G_γ(0, k) = 1/k²) | proved, linear |
| GW170817 c_T | c_T = c; repaired gain lag-free at first order | Δv/c = γ²/8ω² ≈ 1e-45 at 100 Hz | checked (`r127` [2]); comparator via `vR12-7:11` |
| Double-pulsar GW power at the source | unchanged (G_R) | ≤ γ/Ω ≈ 4.6e-17 | checked (`r127` [3]) |
| **Double-pulsar drag from the gain (Lemma D)** | literal: FAIL; repaired: 2.3e-28 vs 6.1e-21 | same | proved + checked (§4.1) |
| **Double-pulsar drag from the regulator** | none (G_R untouched) | Γ_eff = (0.059–0.087)γ; pass for γ ≲ 0.032–0.047 H₀ | checked; strong-field use suggested (§3.2) |
| Orbital aberration (Laplace) | removed at first order by P-r13b | same, plus a companion frame dipole +2e-6γ | checked/proved (§3.2) |
| PPN α₁, α₂ (comparator: α̂₁ = −0.4^{+3.7}_{−3.1}e-5, α̂₂ < 1.6e-9, 95%; web-checked search, Shao & Wex 2012, Shao et al. 2013) | zero frame displacement at first order; even term ≲ 1e-41 at 1 AU | frame dipole ≤ 2e-20 of Newton at 1 AU (0.03 × R12-7's 6.8e-19), not of PPN form | linear order only for **both**; no nonlinear theory in either (`vR12-7:11`) |
| Noise-fed second order | ≲ 4e-65 vs α̂₂ (`C5_R13-6_report.md:348`) | same noise; a homogeneous fluid at rest plus 1% sink | suggested (power counting), both |
| Standard sirens | ratio exactly 1 | ≤ 1.0083 (z = 1), ≤ 1.014 (z ≫ 1) at 0.03 H₀; ≤ 1.012 / 1.021 at 0.045 H₀ (out:84-85), against Ξ₀ = 1.2 ± 0.7 (comparator via `vR12-7:11`) | checked: pass; E2's signature is now below current sensitivity |
| Vacuum photons; near-cone matter heating | strict: R11-5's bounds (ℓ ≳ 0.5–1.7e-8 m; heating crossover about 4.2e-8 m, `C5_R11-5_report.md:225-233`); τ_c: cut | identical (the same ε profile and gain) | suggested (inherited) |
| BMV falsifier (R4-4 Lemma N) | zero entanglement predicted | zero entanglement predicted | proved within each model |
| Near-cone budget | §4.3 | §4.3 | suggested (premises) |

**Reading.** Every row is a pass or a tie. The only E2-specific row, the regulator drag, is satisfied by the parameter restriction.

### 4.3 The near-cone budget on equal terms (checked out:57-81, 89-95)

**E2's single-port factor (checked out:58-63).**
- Ĥ_γ = (Ω² − ω² − iγω)^{−1/2} ↔ θ(t)e^{−γt/2}J₀(Ω′t), with Ω′ = √(Ω² − γ²/4).
- The Laplace identity matches to 6 digits at four frequencies. The branch points sit at −iγ/2 ± Ω′, in the lower half-plane. So Ĥ_γ and 1/Ĥ_γ are both causal.
- This makes E2's meter exactly saturated and stationary, replacing R12-7's unsaturated bank (X ≤ 2.47).
- Its memory is about 2/γ. That is **70 t_H at γ = 0.03 H₀**, longer than E1's age-long J₀ memory.
- The referee's ḣ caveat (`vR13-6:27-31`) applies equally: the impulse response also jumps at t = 0.

**Content equivalence (checked out:64-68).**
- E2's stationary Var h = ½∫₀^∞e^{−γt}J₀² equals E1's finite-age ½∫₀^T J₀² at **T_eq = e^{−γ_E}/γ = 0.561/γ**, to 1e-3 or better (γ = 1e-2 down to 3e-4).
- Both equal ln(8/γ)/(2π) asymptotically.
- With the ε profile, E2's secular slope is ε/(2π) per ln(1/γ), the same coefficient as E1's per ln T. The constant equals the forced part ln(1/ε)/(4π) up to O(ε ln ε) (out:89-95). The forced part is the same in both routes.

**Strict variant (τ = ℓ/c): ε needed for ρ_GW (+ sink) < ρ_Λ** (R11-5 normalization; O(1) tensor weights; Isaacson premise; out:69-75):

| ℓ [m] | E1 (age t_H) | E2, γ = 0.03 H₀ | E2, γ = H₀ (drag-excluded unless repaired) | E2, R12-7's form | E2 repaired, γ₀ = 7 H₀ |
|---|---|---|---|---|---|
| 1e-8 | 1.23e-16 | 1.14e-16 | 9.4e-17 | 4.9e-17 | 4.1e-17 |
| 2e-7 | 1.63e-11 | 1.53e-11 | 1.24e-11 | 8.1e-12 | 5.3e-12 |
| 1e-6 | 9.3e-9 | 8.8e-9 | 7.1e-9 | 5.2e-9 | 3.0e-9 |
| 5e-6 | 5.4e-6 | 5.1e-6 | 4.1e-6 | 3.3e-6 | 1.7e-6 |

- **On one convention, E1 and the drag-allowed E2 differ by ≤ 8%.**
- R12-7's form used L = ln(2ω/γ) with no ε inside the logarithm, while R13-6 followed `vR11-5:15`. That convention difference, about ×1.2–2.3, is the whole of the apparent gap between the two earlier tables.
- **Correction (suggested level):** R12-7's E2 ε limits (`C5_R12-7_report.md:37`) are 1.5–2.3× stricter than E2's equal-terms values at γ = 0.03 H₀.

**τ_c variant (ε = 1, repaired gain with n = 4): lower ends of cτ_c (out:76-80):**

| ℓ [m] | E1 | E2, 0.03 H₀ | E2, H₀ | E2 repaired, 7 H₀ | drag ceiling, CMB velocity included (§4.1) |
|---|---|---|---|---|---|
| 4e-10 | 2.43e-3 | 2.44e-3 | 2.67e-3 | 3.63e-3 | 1.49e-3 (closed) |
| 1e-8 | 8.3e-4 | 8.3e-4 | 9.1e-4 | 1.24e-3 | 1.49e-3 |
| 1e-6 | 2.09e-4 | 2.11e-4 | 2.28e-4 | 2.99e-4 | 1.49e-3 |
| 5e-6 | 1.74e-4 | 1.76e-4 | 1.87e-4 | 2.38e-4 | 1.49e-3 |

**Stated parameter regions where every stated test passes** (on the premises above; checked arithmetic, suggested status):
- **E1:** ℓ ∈ [about 2e-9, 5e-6] m with cτ_c ∈ [lower end(ℓ), 1.49e-3 m]. Or the strict variant with ε(ℓ) as tabulated.
- **E2:** the same, plus 0 < γ ≲ 0.032–0.047 H₀ (ohmic). Or γ₀ up to 7 H₀ with ω_c = 1e3 s⁻¹ (P-r14a), with the ε and τ_c entries of the repaired columns.

### 4.4 Stationarity at the drag-allowed friction (reading, suggested)

- R12-7 framed E2's gain over E1 as "stationarity, not an axiom-text saving" (`C5_R12-7_report.md:154`).
- At ohmic γ ≤ 0.047 H₀, the damping time 2/γ is ≥ 43 t_H (70 t_H at 0.03 H₀; out:86).
  - Stationary E2 therefore presupposes a record history of tens of Hubble times. This is named as price **P-r14b**: an eternal or ≫ t_H-old record process.
  - On a record history of about t_H (records forming since the hot big bang), friction removes ≤ γt_H ≈ 3–5% of the content by today. E2's state is then E1's finite-start state with small damping. Its finiteness comes from the finite history, not from the friction (suggested).
- Only the repaired E2 (P-r14a, γ₀ ≳ 2 H₀) is stationary within the observed age.

---

## 5. Probe (c): the price lists side by side, against the axiom text

**Shared by both routes** (named, not adopted):
- P-r1 (preferred frame);
- P-r11b (driven meters; energy input to record production);
- P-r13b (a zero-first-moment, signed gain, forced by Lemma D);
- P-r13c (τ_c ≈ 0.6–5 ps, optional) or P-r9b′ (ε suppression, strict variant);
- P-r3 (R6-4's P-i1 to P-i5);
- P-r4 (vacuum photons);
- R6-4 (iii)'s changes to Lattice, Qubit, Admissibility and Record plus a source/readout/permanence bridge (`vR6-4:19`);
- the unbuilt spin-2 conserved-noise assembly.

| Axiom text | E1 (start time) | E2 (friction) |
|---|---|---|
| **Lattice**, "No site is privileged" (`AX:37-41`) | P-r11a: a time origin t₀ is a temporal boundary, not a privileged site (`vR12-4:15`) | no time origin |
| **Qubit** (`AX:45-53`) | R6-4 (iii) only | R6-4 (iii) only |
| **Admissibility**, translation- and cubic-rotation-covariant (`AX:57-61`) | frame-tied gain (P-r1) | frame-tied gain plus a frame-tied **dissipative metric law** that breaks the gauge invariance of the h-equation (P-r12a′) |
| **Record**, "Records form", permanent (`AX:77-80`) | records form from t₀; the metric is a functional of records since t₀ | records form always; the metric is a **leaky** functional of permanent records |
| **"Readout … by record content alone"** (`AX:82-83`) | holds given the fixed initial h = ḣ = 0 and vacuum meters (reading) | holds **only because** the sink is noiseless and outgoing-only. Its state is then a deterministic functional of record history. A noisy (FDT) sink would put non-record randomness into the metric (reading) |
| **"A law privileges no states"** (`AX:94-95`) | the law fixes a distinguished initial state at t₀. Whether an initial condition counts as a privileged state is an owner question (reading) | no distinguished state at stationarity (unique attractor). Needs P-r14b (≫ t_H history) unless repaired |
| **Open gates: arrow, record-production dynamics, time metric** (`AX:185-186`) | P-r13a: a half-retarded J₀ meter channel, memory = age | P-r12b: a noiseless T = 0 outgoing-only gravitating sink with frame recoil (an **arrow** at the sink boundary), no field-level completion (`vR12-7:7`); P-r12c: meter memory about 2/γ (70 t_H at 0.03 H₀); and either the restriction γ ≲ 0.03–0.047 H₀ plus P-r14b, or **P-r14a** (zero-integral friction kernel, new frame time 1/ω_c ≈ 1–3 ms, frequency-dependent GW damping, about ×3 budget) |
| **Count of route-specific prices** | 2 (P-r11a, P-r13a) | 3 (P-r12a′, P-r12b, P-r12c) + 1 (P-r14a or P-r14b) |

**Reading.** E2 removes the time origin (P-r11a) but adds a dissipative metric law, a gravitating hidden sink with an arrow, and a longer meter memory. At drag-allowed γ it also adds either a history of tens of Hubble times or a new frame time scale. **On the axiom text, E1 is the cheaper route by count.** Whether AX:94 makes E1's initial state a price is the one owner question that could reverse this.

---

## 6. Strong words checked

- **"Removable"** (E2 drag): the leading term is removed exactly by ∫K = 0. The residual is the full quadrature, not a Taylor estimate (out:40-46). The bound uses smooth n = 1 polytropes at 12 km and a weak field.
- **"Passive", "causal":**
  - Re γ ≥ 0 is proved.
  - Poles in the rest frame and boosted frames are checked by sampling, not proved for all parameters.
  - The principal part is the wave operator, so the front speed is c (suggested; Gavassino-type all-frame stability, RECALLED via `C5_R12-7_report.md:116`).
- **"Tie" / "same footing"**: on the listed tests, at the stated orders, under the shared premises. Untested sectors (spin-2 assembly, nonlinear PPN, sink stress tensor) could split the routes.
- **"≤ 8%"**: the strict-variant ε tables on one L convention, at γ = 0.03–0.045 H₀ (out:72-75).
- **"γ ≲ 0.032–0.047 H₀"**: a structure-model range with all of the 1.3e-4 attributed to drag. Strong-field use is suggested only.
- **"Closes near 1–2e-9 m"**: within the smooth-polytrope τ_c ceiling and the worst-case V orientation. With V normal to the orbit the closure moves slightly lower (out:98).
- **"OPEN"** for both routes is a worker reading. No no-go is claimed, so no referee is mandatory. A referee is recommended for §3.2 (the bound), §3.4 (the repair) and §4.1 (the τ_c correction).

## 7. What would decide it

1. **The spin-2 conserved-noise assembly** for either route. It is the same object for both, with Ĥ or Ĥ_γ. It fixes the tensor weights and decides the budget for both at once.
2. **The owner's reading of `AX:94-95`** for E1's initial state. That is the only axiom-text item that could reverse "E1 cheaper".
3. **For E2 only:** a field-level gravitating sink (action plus stress tensor) and a nonlinear frame theory giving PPN α₁, α₂. Without them E2 cannot reach VIABLE, whatever γ is.
4. **A realistic neutron-star (crust/envelope) drag calculation** with the true orientation of V_CMB relative to J0737's orbit. It fixes the τ_c ceiling for both routes and E2's γ bound.
5. **If P-r14a is pursued:** a waveform-level siren test of frequency-dependent damping γ(f) ∝ f² below ω_c.

**Sources.**
- Web-checked this run:
  - [arXiv:2112.06795](https://arxiv.org/abs/2112.06795) (abstract: 1.3e-4 at 95%);
  - search results for [Shao & Wex 2012, arXiv:1209.5171](https://arxiv.org/pdf/1209.5171) (α̂₁) and [Shao et al. 2013, arXiv:1307.2552](https://ar5iv.arxiv.org/html/1307.2552) (α̂₂ < 1.6e-9).
- Via earlier referees: Lu et al. [arXiv:1803.11397](https://arxiv.org/abs/1803.11397) (β < 6.75e-4 Mpc⁻¹, fixed-distance; `vR12-7:11`); GW170817 [arXiv:1710.05834](https://arxiv.org/abs/1710.05834); GWTC-3 Ξ₀ [arXiv:2203.09238](https://arxiv.org/abs/2203.09238).
- RECALLED:
  - Kramer et al. 2021 masses, P_b and Ṗ_GR (and the 0.999963(63) ratio, not used);
  - the Lattimer–Prakash binding-energy fit;
  - Smith 2002 inerter; Brune positive-real synthesis; Gavassino 2021;
  - the solar CMB speed of 369.8 km/s;
  - ρ_crit, ρ_Λ and t_H as in R11-5.
