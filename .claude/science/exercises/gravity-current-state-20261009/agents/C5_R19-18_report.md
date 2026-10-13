# C5 round 19, probe R19-18: breaking the E1/E2 tie by observation (worker report)

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-13, 05:45Z to about 06:06Z. No repository file was edited.

**Scratch:** `scratchpad/C5/R19-18/`. OMP_NUM_THREADS=2; every run is under 1 min. SHA-256 prefixes (script / output):
- `scripts/r1918_lift.py` / `.out` (233b04eccc9c / ce9fcb429ba1), section [L]: sympy derivation of the FRW lifts of E2's friction stress, the TT equation in FRW, and the Lemma F0 sink.
- `scripts/r1918_obs.py` / `.out` (52b1234596e5 / a17b0aa2ab37), sections [S1]–[S3], [B1]–[B2], [G1]–[G3], [M1]: sirens, a toy siren Fisher, the P-r14a variant, the L1 background fitted to DESI DR2 + compressed CMB, growth, ISW, and the fixed-reference lift.
- `scripts/r1918_forecast.py` / `.out` (72dec9f9e4ac / 1169d87a508d), section [F]: mock-data (Asimov) sensitivity of BAO + CMB to the L1 sink.
- `rerun/`: the archived R12-7, R14-2 and R19-8 runners (6 scripts). **All 6 rerun with exit 0, and their outputs are identical to the archived `.out` files except for runtime lines** (checked: `rerun/summary.txt`).
- No downloads and no web fetches. All literature and data values are **RECALLED** and labelled.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `rR12-7:n` = `P/agents/C5_R12-7_report.md:n`, `vR12-7:n` = `P/agents/C5_R12-7_referee_verdict.md:n`, `refR12-7:n` = `P/agents/C5_R12-7_referee.md:n` (and so on); `O:n`, `L:n`, `F:n` = line n of `r1918_obs.out`, `r1918_lift.out`, `r1918_forecast.out`.

**What I read.**
- In full: AX; `TESTS:2302-2372` (C5 method, round 1); the R19-18 item `TESTS:7954-7985`.
- Set-A entries and verdicts: R6-4 `TESTS:3143-3165, 3409-3418`; R12-7 `TESTS:4527-4560`; R13-6 `TESTS:4682-4733`; R14-2 `TESTS:4817-4832, 4891-4897`; R16-4 `TESTS:5108-5125, 5286-5290, 5433-5437`; R16-14 `TESTS:5630-5684, 5875-5887, 5998-6006`; R18-7 `TESTS:6713-6748, 6898-6916, 7020-7028`; R19-8 `TESTS:7450-7469, 7611-7626, 7753-7764`.
- Reports and verdicts: `rR12-7` and `vR12-7` (full); `rR14-2` and `vR14-2` (full); `rR19-8` and `vR19-8` (full); `vR16-14` (full); `refR12-7:147-160`; `rR16-4:305-315`; `rR19-2:39-40, 149-164` (lift A, Lemma F0); `vR19-2:7`.
- Runners: all of `P/scripts/C5/R12-7`, `R14-2`, `R19-8` (rerun).

**Labels.** **proved** (derived here under stated hypotheses); **checked** (a number or identity in my `.out` files); **suggested** (argued, not proved); **reading** (interpretation); **comparator** (literature or data; all RECALLED here).

**Order rule.** Linear in γ for every E2-specific effect, except where the exact exponential is printed. Linear perturbation theory. The background is exact in the stated lift (ODE). Sub-horizon growth is quasi-static.

---

## Reading against the FIXED readings (`TESTS:7982-7984`)

**Worker reading: OPEN.** The registered class ("E2 with γ in the drag-allowed range", `TESTS:7967`) runs from γ → 0 up to the R14-2 ceiling. That ceiling is 0.016–0.024 H₀ (signed timing) or 0.032–0.047 H₀ (conservative envelope) (`vR14-2:3`, labelled suggested in strong field). The class splits:

| γ sub-range (ohmic) | Strongest siren forecast (both lifts) | L1 background + growth | Current data | Reading on the sub-range |
|---|---|---|---|---|
| γ ≤ 0.024 H₀ (the whole signed-timing range) | ≤ 1.9σ (optimistic ET-like toy, `O:14`); ≤ 1.4σ (RECALLED ET σ(Ξ₀) = 0.8%, `O:8`); ≤ 1.2σ (LISA-like toy, `O:22`) | DESI DR2 + CMB: Δχ² = −0.46 to −0.56, i.e. no penalty (`O:37`); Asimov Δχ² ≤ 1.83 even with BAO errors ÷3 (`F:4`); Δfσ8/fσ8 ≤ 1.1% (`O:45`, interpolated) | nothing: GW170817 ratio−1 ≤ 1.2e-4; GWTC-3 bounds γ < 1.35 H₀ (`O:9`) | **TIE-HOLDS** (checked, against stated toy and RECALLED forecasts) |
| 0.026 ≤ γ < 0.039 H₀ | 2–3σ (optimistic toy); 1.5–2.3σ (RECALLED ET) | no current penalty; ≤ 2.2σ Asimov with BAO ÷3 (`F:4`, interpolated ∝ g_L²) | nothing | neither |
| 0.039 ≤ γ ≤ 0.047 H₀ (top of the conservative envelope only) | 3.0–3.7σ (optimistic toy only); 2.3–2.8σ (RECALLED ET); ≤ 2.4σ (LISA toy) | Δχ² = −0.43 now (`O:37`); Asimov 1.41 (DR2), 3.59 (÷2), 7.07 (÷3) at 0.047 (`F:2-4`); Δfσ8/fσ8 ≈ +1.5–2.2% (`O:46, 48`) | nothing | **TIE-BROKEN by forecast**, only under the optimistic ET-like toy (suggested: toy) |

- **Why not TIE-BROKEN for the class.**
  - No stated datum excludes any drag-allowed γ under either consistent lift (checked).
  - Detectability at ≥ 3σ is reached only in the top sliver of the *conservative* drag envelope, and only by my optimistic toy. It is not reached by the RECALLED ET figure (2.8σ at most) or by LISA.
  - Every E2-specific signal is ∝ γ, and nothing bounds γ from below. So E2 approaches E1 observationally as γ → 0 (proved for the stated observables: §5, §4).
- **Why not TIE-HOLDS for the class.** At γ ≥ 0.039 H₀ the siren signal is above an (optimistic) forecast's 3σ line.
- **Threshold convention (stated here, not registered):** "detectable" means ≥ 3σ expected significance against Ξ = 1, and "below sensitivity" means < 2σ. With a 2σ "detectable" convention, TIE-BROKEN would extend down to γ ≥ 0.026 H₀ (toy) or 0.034 H₀ (RECALLED ET) (`O:8, 15`). The class reading stays OPEN under either convention.

**Against the expectation (`TESTS:7985`).**
- **Confirmed: the size.** d_L^GW/d_L^EM − 1 = 0.44–1.30% at z = 1 and Ξ₀ − 1 = 0.76–2.26% across the four drag ceilings (`O:3-6`). E1 has no such signal (`rR14-2:193`).
- **Confirmed: the siren signal is lift-independent.** L0 and L1 give the same Ξ(z), up to a mass-type term m² = 4γH (harmonic) or γH (synchronous) that shifts the speed by ~1e-42 at 100 Hz (`L:9-10`).
- **Refuted: "TIE-BROKEN under L1".**
  - L1's background adds no decisive channel: it is mildly favoured, not excluded, by DESI DR2 + CMB (`O:35-37`). Its Asimov significance is 1.2σ at DR2 precision (`F:2`).
  - "Within ET/LISA reach" holds only marginally, at the top of the conservative envelope (above).

---

## 0. In plain words

- **The question.** E2 says gravitational waves lose energy slowly to a hidden sink tied to the cosmic rest frame. E1 says they don't, but the record process had a start. Can any telescope tell which is true?
- **The clean signal is in gravitational-wave "standard sirens".**
  - Friction makes a distant merger look fainter in gravitational waves than in light. The two distance estimates then disagree by a factor exp(γ × travel time / 2). E1 predicts exact agreement.
  - The binary-pulsar brake caps γ at about 2–5% of the Hubble rate. The mismatch is then at most about 1% at redshift 1, and at most 2.3% for very distant sources.
  - Today's data are 30–80 times too coarse to see it (GWTC-3: γ < 1.35 H₀).
  - Next-generation detectors (Einstein Telescope with about a thousand neutron-star mergers with flashes, or LISA) reach about 1% precision. They could see the effect at about 3σ, but only if γ sits at the very top of the brake-allowed range.
- **If the friction also slows or speeds the expansion itself (L1),** it acts like a small extra component of the universe. That component has negative energy and positive pressure for the gauge E2's law fixes.
  - The expansion rate shifts by under 1%. After refitting matter density and the Hubble constant, current baryon-acoustic and CMB data cannot tell; they even mildly like it.
  - Structure grows about 2% faster. That is below today's precision.
- **A version of the lift that measures friction against a fixed reference** blows up in the early universe. It is not a sensible lift.
- **So there is no tie-breaker today.** A future one exists only if γ is near its upper limit. If γ is small, E2 and E1 make the same predictions for every quantity tested here, because every E2-specific effect is proportional to γ.

---

## 1. Prior art (each counted once)

1. **R12-7 / vR12-7.**
   - The E2-h law (□ − γu·∂)h̄ = −16πGJ (`rR12-7:67`); the causal telegraph kernel (`rR12-7:113`).
   - The sirens: d_L^GW/d_L^EM = exp(γ t_lb/2) (`rR12-7:131`). Lu et al.'s 2.98 H₀ is a fixed-distance benchmark; the EM-counterpart scale is about 62 H₀ (`vR12-7:11`).
   - GWTC-3 Ξ₀ = 1.2 ± 0.7 (comparator via `vR12-7:11`).
2. **R14-2 / vR14-2.**
   - The drag ceilings: 0.032–0.047 H₀ conservative, 0.016–0.024 H₀ signed (`vR14-2:3`).
   - P-r14a, the zero-integral kernel, with 31.7 H₀ (signed) or 62 H₀ (conservative) at ω_c = 3000 rad/s (`vR14-2:5`).
   - The siren row: E1 ratio exactly 1; E2 ≤ 1.0083 at z = 1 at 0.03 H₀ (`rR14-2:193`). My `O:3-6` reproduce it: 0.00881 at 0.032 H₀ scales to 0.0083 at 0.03 H₀.
   - The tie, with no cost metric (`vR14-2:11`).
3. **R16-14 / vR16-14.** The observational tie at PPN order; E2 lacks a field-level sink (`vR16-14:19`).
4. **R19-8 / vR19-8.**
   - E2 + N_c stipulable at weak field; the per-mode noise is |R| × E1's.
   - **The FRW lift is not constructed** (`vR19-8:15,17`). The worker named it law data, P-r198a, with a suggested O(γ/H) = 2–5% change in the expansion law (`rR19-8:57, 257`; `P/scripts/C5/R19-8/r198_sink.out:29`).
   - The near-cone noise difference E2/E1 = 1.034–1.053 (stationary) or 0.954–0.984 (t_H history) (`r198_sink.out:22-27`). The split sink is ≤ 5.6e-7 ρ_Λ (`r198_sink.out:28`).
5. **R19-2 / vR19-2.** Lemma F0, ρ = −a⁻³∫p_tot d(a³), with lift A (Π's k = 0 part pressureless in the cosmic frame) (`rR19-2:39, 149-153`). The lift dependence is confirmed (`vR19-2:7`). I use lift A (P-r192a) for the k = 0 sink.
6. **R16-4.** At the drag-allowed γ, E2 keeps 95.6–98.5% of initial TT energy at t_H (`rR16-4:311`).
7. **Repository grep** of `P/agents/`, `P/TESTS.md`, `P/SUMMARY.md` for "Belgacem", "Xi_0"/"Ξ₀" and "DESI":
   - the only DESI number used before is 10³Ω_K = 2.3 ± 1.1 (`TESTS:2993`);
   - no repository Ξ-forecast or FRW friction-lift computation exists.
   - `docs/` was not grepped.
8. **Comparators (all RECALLED).**
   - Belgacem, Dirian, Foffa, Maggiore 2018 (the Ξ₀, n parametrisation; ET with about 10³ BNS plus counterparts gives σ(Ξ₀) ≈ 0.8%).
   - Belgacem et al. (LISA CosWG) 2019 (σ(Ξ₀) ≈ 1–4%, depending on the MBHB population).
   - DESI DR2 BAO (arXiv:2503.14738, Table IV values typed in `r1918_obs.py`).
   - Planck 2018: 100θ_* = 1.04110 ± 0.00031, ω_m = 0.1430 ± 0.0011, r_d = 147.09 Mpc, r_* = 144.43 Mpc, z_* = 1089.92.
   - The lensing-scatter fit 0.066[(1 − (1+z)^−0.25)/0.25]^1.8.
   - The ISW detection significance of about 4–5σ.

## 2. Hypotheses: class ℰ₂^FRW (stated before any title)

- **H1.** E2-h as in R12-7/R14-2/R19-8: friction γ u·∂ on the gothic metric perturbation in harmonic gauge, which is E2's law gauge (`rR19-8:33`). Ohmic, 0 < γ ≤ γ_max with γ_max ∈ [0.016, 0.047] H₀. P-r14a only in §5.3.
- **H2.** A flat ΛCDM background with Planck-like early-universe physics: r_d and r_* fixed, since every lift changes H by ≤ 3e-6 at z > 10 (`O:30`).
- **H3.** Π's homogeneous mode is pressureless (lift A, P-r192a). Any friction pressure is completed by an energy-only sink obeying Lemma F0.
- **H4.** The sink is smooth on sub-horizon scales. The friction is negligible on quasi-static potentials (§4.3).
- **H5.** The EM sector is untouched: photons do not feel the friction, so d_L^EM is the background's.
- **Excluded:** strong field, dynamical frames, quantum or thermal sinks, lift B (`rR19-2:40`), and non-linear structure.

## 3. The lifts (stated) and which are consistent

**Consistency criteria (reading):**
- (C1) on sub-Hubble scales the lift reduces to the refereed Minkowski E2 law;
- (C2) the total effective source is conserved, via Π lift A;
- (C3) observables do not depend on the arbitrary normalisation of comoving coordinates (a → λa);
- (C4) it is local and causal in the cosmic frame;
- (C5) it is finite toward the past without new start data.

| Lift | Homogeneous friction stress (`L:1-6`) | C1–C5 | Status |
|---|---|---|---|
| **L0**: friction on the deviation from the FRW background in the cosmic frame | X̃_{k=0} ≡ 0 | all hold | consistent (proved, by definition) |
| **L1-H**: friction on the full gothic metric, local reference (a = N = 1 at each epoch), harmonic slicing N ∝ a³ (E2's law gauge) | ρ_X = 0, **p_X = γH/(4πG)**, so κ_p = 1 | all hold | consistent (proved; checked `L:2,5`) |
| **L1-S**: the same in the synchronous slicing | ρ_X = −3γH/(16πG), p_X = γH/(16πG), so κ_p = 1/4 | all hold, but the slicing is not E2's law gauge | consistent as a different law datum (proved; checked `L:3`) |
| **L1-M**: friction against a fixed global reference η (a_ref, C) | p_X = (γH/4πG)(a_ref/a)⁶/C | fails C3 and C5 | **not consistent** (proved `L:6`). Taken literally with a_ref = a₀, |p_X| < 1% ρ_crit needs γ < 2.1e-16 H₀ (CMB) and < 5.6e-39 H₀ (BBN) (checked `O:55-57`) |

- **The general L1 family.** Under lift A, only κ_p matters. ρ_X is redistributed between X̃ and Π's sink, which leaves p_tot unchanged (proved: Lemma F0, `rR19-2:149`). So the background depends on one number, **g_L ≡ κ_p γ/H₀**.
- **The sink under L1 (proved, `L:11-13`).**
  - In the matter era: ρ_s/ρ_crit = −(4/3)κ_p γ/H and p_X/ρ_crit = (2/3)κ_p γ/H, so w_sink = −1/2.
  - For κ_p > 0 the sink has **negative energy and violates the NEC** (ρ_s + p_X < 0): it is phantom-like.
  - In the radiation era it is negligible: |Ω_s| ~ g_L/E.
  - This is a property of the lift, not a proved inconsistency (reading). The sink is a Π bookkeeping term with no dynamics of its own, so there is no ghost to exhibit.
- **The TT sector is the same in every lift (proved, `L:7-10`).**
  - Cosmic-time friction γḣ gives h'' + (2 + ν)ℋh' + k²h = 0 with **ν = γ/H**.
  - The gothic lifts add a mass term m² = 4γH (L1-H) or γH (L1-S). That shifts the speed by 2γH/ω² ≈ 1e-42 at 100 Hz (γ = 0.047 H₀). This is negligible for c_T, LISA and LIGO dispersion (suggested size, from the formula).

## 4. Probe (a): background and growth under L1 (L0 has none)

### 4.1 H(z) and distances (checked `O:29-43`, `F:1-4`)

- **At fixed (Ω_m, h) = (0.3153, 0.6736), g_L = +0.047:**
  - Ω_s/E² = −4.5% (z = 0), −3.3% (z = 1), −0.8% (z = 5), −3e-6 (z = 1089);
  - ΔH/H = −0.73%, −0.91%, −0.76% and −0.34% at z = 0.5, 1, 2, 5;
  - w_DE,eff(0) = −1.020.
  - g_L = −0.047 mirrors this, with w_DE,eff(0) = −0.979 (`O:30-31`).
  - **Correction to R19-8's suggested "2–5% change in the expansion law" (`rR19-8:57`).** 2–5% is the size of Ω_s/E². The change in H(z) is ≤ 0.9%, and most of it is absorbed by refitting (Ω_m, h).
- **Fit to DESI DR2 BAO + compressed CMB (all RECALLED), profiled over (h, ω_m).**
  - ΛCDM gives χ²_min = 13.11 for 15 numbers and 2 parameters, at Ω_m = 0.2976 and h = 0.689 (`O:33`). This is a sanity check on the recalled DR2 table.
  - Δχ²(g_L) is ≤ 0 across 0 < g_L ≤ 0.06: −0.46, −0.56, −0.59, −0.43 at 0.016, 0.024, 0.032, 0.047 (`O:35, 37`).
  - Best fit g_L = +0.031 (Δχ² = −0.59, not significant). The 95% interval is g_L ∈ [−0.048, +0.108] (`O:36`).
  - With errors ×1.5 the interval is [−0.046, +0.144] (`O:41`).
  - BAO alone: Δχ² = +0.66 at 0.047 (`O:43`).
- **Expected sensitivity (Asimov, independent of DR2's actual scatter; `F:2-4`).**
  - At g_L = 0.047: Δχ² = 1.41 (DR2 errors), 3.59 (÷2), 7.07 (÷3).
  - At g_L = 0.024: 0.37, 0.93, 1.83.
  - The ÷2 and ÷3 scalings are my assumptions, not RECALLED forecasts.
- **Consequence for L1-H (κ_p = 1).**
  - Current BAO + CMB data exclude no drag-allowed γ.
  - Their 95% bound, γ < 0.108 H₀, is weaker than the drag ceiling.
  - For L1-S (κ_p = 1/4) the bound is 4× weaker still.
  - A κ_p < 0 lift is bounded at |κ_p|γ < 0.048 H₀, comparable to the conservative ceiling and not below it.

### 4.2 Growth fσ8 and ISW (checked `O:44-53`)

- **L1, same early normalisation, fixed parameters.** At g_L = +0.047, Δ(fσ8)/fσ8 = +1.6% to +2.25% for 0 ≤ z ≤ 1.5, and σ8(0) is +1.5% (`O:46`). At each model's own BAO + CMB best fit it is +1.5% to +2.0% (`O:48`). At g_L = 0.016 it is ≤ +0.76% (`O:45`).
- **Against data (comparator, RECALLED, rough).** Current fσ8 points carry 5–10% each; the aggregate σ8 or S8 constraints are at about 2–3%. A +1.5–2% shift is not detectable now, and is at most marginal (about 1–2σ) for Stage-IV aggregates (suggested).
  - Its sign is +σ8, which pulls away from the low-S8 weak-lensing values. That is a weak-lensing-tension comparator only (RECALLED).
- **ISW (proxy: the late potential-decay fraction 1 − D/a at z = 0).** It changes by −3.6% at g_L = +0.047 (`O:46`). Against an ISW detection of about 4–5σ total (RECALLED), that shifts the significance by ≤ 0.2σ: undetectable (suggested).

### 4.3 Friction on scalar potentials (L0 and L1; checked `O:49-53`)

- **Sub-horizon (quasi-static).** From (□ − γu·∂)h̄₀₀, the relative correction is (γ/H)|1 − f|(aH/k)² = 2.6e-5, 1.0e-6 and 6.5e-8 at k = 0.01, 0.05 and 0.2 h/Mpc for γ = 0.047 H₀. **Under L0, growth is E1's to ≤ 3e-5** (checked, at the estimate's order).
- **Horizon scale (k ~ aH).** The correction is O(γ/H) ≤ 4.7% on the ISW modes, which shifts the ISW significance by ≤ 0.25σ (suggested).
- The matter self-drag of R14-2, Γ = 2γ|U|/(3Mc²), is ~γ·1e-6 for galaxies. It is negligible for structure (`rR12-7:145`; suggested).

## 5. Probe (b): d_L^GW / d_L^EM under both lifts

### 5.1 The prediction (proved `L:8`; checked `O:2-12`)

- **The formula.** Ξ(z) ≡ d_L^GW/d_L^EM = exp(γ t_lb(z)/2) in both L0 and L1. It is frequency-independent for ohmic γ.
  - H₀t_lb = 0.0097, 0.093, 0.359, 0.548, 0.725 and 0.870 at z = 0.0098, 0.1, 0.5, 1, 2, 5; H₀t₀ = 0.950 (`O:2`).
- **The ratio − 1 at the four ceilings:**

| γ/H₀ | z = 0.0098 | 0.1 | 0.5 | 1 | 2 | 5 | Ξ₀ − 1 | n (Belgacem fit, z ≤ 5) |
|---|---|---|---|---|---|---|---|---|
| 0.016 | 8e-5 | 7.4e-4 | 2.9e-3 | 4.4e-3 | 5.8e-3 | 7.0e-3 | 0.0076 | 1.295 |
| 0.024 | 1.2e-4 | 1.1e-3 | 4.3e-3 | 6.6e-3 | 8.7e-3 | 1.05e-2 | 0.0115 | 1.293 |
| 0.032 | 1.6e-4 | 1.5e-3 | 5.8e-3 | 8.8e-3 | 1.17e-2 | 1.40e-2 | 0.0153 | 1.292 |
| 0.047 | 2.3e-4 | 2.2e-3 | 8.5e-3 | 1.30e-2 | 1.72e-2 | 2.07e-2 | 0.0226 | 1.290 |

- **The E2 signature (proved; checked).** A positive Ξ₀ − 1 = γt₀/2. The small-z slope is n = 1/(H₀t₀) = 1.05, and the best Belgacem-form fit gives n ≈ 1.29, with residual ≤ 7.5e-4 (`O:3-10`).
- **Mode check (checked `O:11-12`).** Integrating h'' + (2ℋ + aγ)h' + k²h = 0 through ΛCDM from z = 1, with k = 400 H₀, gives an amplitude ratio of 0.987232 against exp(−γt_lb/2) = 0.987207 at γ = 0.047 H₀ (2.5e-5 relative).
- **E1:** Ξ ≡ 1, since its readout is G_R (`rR14-2:193`).
- **The noise-sector difference between E1 and E2** in the background is ≤ 5% of ρ_GW/3 ≈ 6e-7 ρ_Λ (`r198_sink.out:28`). It is unobservable.

### 5.2 Against data and forecasts

- **Current data (comparator).**
  - GW170817: ratio − 1 = 2.3e-4 at γ = 0.047 H₀ (`O:9`), against a counterpart-distance precision of order 10% (RECALLED).
  - GWTC-3 dark sirens: Ξ₀ = 1.2 ± 0.7 gives γ < 1.35 H₀ (68%) (`O:9`), 29–84× above the drag ceilings.
  - **No current datum sees E2's siren signal.**
- **Forecasts (RECALLED, plus a toy to calibrate them).**
  - RECALLED ET, σ(Ξ₀) = 0.8% applied to Ξ₀ = e^{γt₀/2}, gives σ(γ/H₀) = 0.0168. The ceilings then sit at 2.8σ (0.047), 1.9σ (0.032), 1.4σ (0.024) and 1.0σ (0.016) (`O:8`).
  - **Toy Fisher** (suggested; my parametrisation: volume-weighted z < 2, instrumental 5% + 5%z plus RECALLED lensing scatter, the EM cosmology fixed by CMB + BAO; `O:13-23`):
    - ET-like, 1000 events: σ(γ/H₀) = 0.0129, so 3.7/2.5/1.9/1.2σ at the four ceilings. The 2σ line is at 0.026 H₀ and the 3σ line at 0.039 H₀.
    - ET-like, 300 events, or 1000 events with doubled instrumental error: σ = 0.024–0.025, ≤ 2.0σ.
    - LISA-like, 30 or 100 MBHB: σ = 0.036 or 0.020, ≤ 1.3σ or ≤ 2.4σ.
  - The toy's ET optimum (σ(Ξ₀) ≈ 0.6%) is close to the RECALLED 0.8%. This is consistency of scale, not a forecast.
  - **LISA cannot reach 3σ** anywhere in the drag-allowed range (`O:20-23`).

### 5.3 The P-r14a variant (zero-integral kernel; checked `O:24-28`, consequences suggested)

- **Frequency-dependent friction, Re γ(ω) = γ₀ω²/(ω² + ω_c²), along the path.** For each parameter set, the d_L ratio at f = 30/300/1000 Hz:

| (γ₀, ω_c) | z = 0.0098 | z = 0.1 | z = 0.5 | LISA (1 mHz, z = 3) |
|---|---|---|---|---|
| 7 H₀, 1e3 rad/s (R14-2 example) | 1.001/1.027/1.034 | 1.012/1.296/1.375 | 1.066/2.86/3.44 | ratio − 1 = 4.3e-10 |
| 31.7 H₀, 3e3 rad/s (signed ceiling) | 1.001/1.045/1.134 | 1.006/1.56/3.39 | 1.034/8.2/136 | ratio − 1 = 2.2e-10 |
| 62 H₀, 3e3 rad/s (conservative ceiling) | 1.001/1.090/1.279 | 1.013/2.40/10.9 | 1.068/61/1.5e4 | ratio − 1 = 4.2e-10 |
| 1 H₀, 330 rad/s | 1.001/1.005/1.005 | 1.012/1.046/1.048 | 1.060/1.19/1.20 | ratio − 1 = 5.6e-10 |

- **Consequences (suggested).**
  - These are O(1)-to-huge **frequency-dependent amplitude deficits inside the LVK band** for BBH at z ≳ 0.1. That is a distinct E2 signature; E1 has none.
  - It is plausibly already excluded near the ceiling parameters by LVK waveform-consistency or population analyses. I computed no such likelihood, so I make no exclusion claim.
  - GW170817 alone does not exclude these parameters (≤ 1.28 at 1 kHz, z = 0.0098).
  - The P-r14a family also extends continuously to γ₀ → 0. There, as in the ohmic case, it ties with E1.

## 6. Probe (c): bounds on γ

| Source | Bound | Below R14-2's drag bound? | Label |
|---|---|---|---|
| GW170817 + EM | ~62 H₀ (`vR12-7:11`) | no | comparator |
| GWTC-3 dark sirens (Ξ₀ = 1.2 ± 0.7) | γ < 1.35 H₀, 68% (`O:9`) | no (29–84× weaker) | comparator + checked arithmetic |
| DESI DR2 + CMB, L1-H (κ_p = 1) | γ < 0.108 H₀, 95% (`O:36`) | no | checked, on RECALLED data with a compressed CMB |
| DESI DR2 + CMB, κ_p = −1 lift | γ < 0.048 H₀ | comparable to the conservative ceiling, not below it | checked |
| ET-like toy (1000 BNS + counterparts), if Ξ = 1 is observed | 2σ: γ < 0.026 H₀ | below the conservative envelope (0.032–0.047); **not** below the signed one (0.016–0.024) | suggested (toy) |
| RECALLED ET σ(Ξ₀) = 0.8% | 2σ: γ < 0.034 H₀ | partly below the conservative envelope only | comparator-based |
| LISA-like toy | 2σ: γ < 0.039–0.072 H₀ | no | suggested |
| BAO ÷3 (Asimov), κ_p = 1 | 2σ: g_L ≲ 0.036 (`F:4`, interpolated) | partly, conservative only | suggested |

**Answer.**
- No current datum bounds γ below the drag bound under any consistent lift.
- Third-generation sirens could push it below the conservative envelope, but not below the signed-timing envelope.

## 7. Probe (d): is the tie broken?

- **E2 does predict signals E1 does not (proved within ℰ₂^FRW).**
  - In both lifts: Ξ(z) = e^{γt_lb/2} > 1, frequency-independent, n ≈ 1.05–1.29.
  - In L1: a phantom-side (κ_p > 0) sink in H(z) and +1.5–2.2% in fσ8 at the ceiling.
  - In P-r14a: an LVK-band frequency-dependent amplitude deficit.
- **Observability.**
  - None is excluded by current data at any drag-allowed γ (checked).
  - Only the siren channel can reach ≥ 3σ, and only for 0.039 ≤ γ ≤ 0.047 H₀ under an optimistic ET-like toy (suggested). That range lies above the signed-timing drag ceiling (`vR14-2:3`).
- **Structural point (proved for the listed observables).**
  - Every E2-specific observable is linear in γ, and no theory input bounds γ from below.
  - R12-7's budget optimum, γ ≈ 0.037–0.040 H₀ (`refR12-7:155-157`), is not a selection: it relaxes the ε limits by only about 26%. If γ were pinned there anyway, it would lie above the signed drag estimate and give 2.9–3.1σ in the optimistic toy.
  - So observation can confirm E2 only if γ is near its ceiling. It can never exclude E2 as a class; it can only lower the ceiling. A significant **Ξ₀ < 1** would exclude ohmic E2 for every γ > 0, and E1 with it.
- **Tie-break statement (reading).** The E1/E2 tie is **observationally breakable in principle**, through sirens. **In practice it holds** for γ ≤ 0.024 H₀ against every stated forecast, and is **broken only by an optimistic forecast in the top ~20% of the conservative envelope**. Hence OPEN.

## 8. Prices (named, not adopted)

- **P-r1918a (refines P-r198a): the FRW lift of the friction is L0.** Friction acts on the deviation from the FRW background. The cost is a background split in the cosmic frame (reading). *Axiom text:* AX:185-186 (dynamics, time metric), AX:187 (source/observable).
- **P-r1918b (the alternative to P-r1918a): L1-H.** Friction on the homogeneous gothic mode with a local reference. It costs a negative-energy, NEC-violating Π sink (κ_p = 1), whose size is fixed by γ (no new number). *Axiom text:* as P-r1918a, plus P-r192a (lift A).
- **No price for L1-M:** it is not a consistent lift (§3).
- **Carried, unchanged:** P-r1, P-r12a′, P-r12c, P-r13b, P-r14a or P-r14b, P-r192a/b, P-r198b/c, P76/P88 (`rR19-8:256-265`).
- **Count against E1:** E2 adds P-r1918a or P-r1918b. No cost metric orders the lists (`vR14-2:11`).

## 9. Remarks on earlier records (worker)

- **`rR19-8:57, 257` and `r198_sink.out:29`** ("O(γ/H) = 2–5% in the expansion law"):
  - 2–5% is the size of the sink's density parameter for κ_p = 1.
  - H(z) moves by ≤ 0.9%, and after refitting (Ω_m, h) the effect is invisible to DESI DR2 + CMB (§4.1).
  - The "possible new test of γ, comparable to or tighter than the double-pulsar drag" (`rR19-8:293`) is **not realised** for κ_p = 1 with current data: it gives 0.108 H₀ against the drag's 0.016–0.047 H₀.
- **`rR14-2:46`** ("E2's siren signature ≤ 1% at z = 1, far below current sensitivity"): confirmed. It is not far below 3G sensitivity at the conservative ceiling (§5.2).
- **The TESTS expectation's** "≈ γ/(2H₀) × O(1) ~ 1–2% at z ~ 1": the O(1) is H₀t_lb(1) = 0.548, which gives 0.44–1.30% at z = 1. 1–2% is the z ≫ 1 value (Ξ₀ − 1 = 0.76–2.26%).

## 10. Strong words checked

- **"Consistent" lift:** against C1–C5 as stated in §3. These are my criteria, not registered ones.
- **"Excluded" (L1-M):** under its literal reading with a_ref = a₀; its failure of C3 is proved.
- **"Lift-independent" (sirens):** to O(γH/ω²) ≈ 1e-42 in speed. The amplitude law is the same in L0, L1-H and L1-S.
- **"Detectable":** ≥ 3σ expected significance under a stated toy or a RECALLED forecast. All forecasts are RECALLED or toys, and none is a survey-grade Fisher matrix.
- **"No current exclusion":** the DESI DR2 table and the Planck compressed numbers are RECALLED. The likelihood is compressed: θ_* and an ω_m prior, with r_d and r_* fixed.
  - Robustness: errors ×1.5 change Δχ² at the ceilings by ≤ 0.6, with no sign change (`O:42`).
  - The Asimov result (`F:2-4`) does not depend on DR2's central values.
- **"Proved: E2 → E1 as γ → 0":** only for the observables computed here (Ξ, H(z), fσ8, ISW proxy, quasi-static potentials). The law is not the same: the start time against P-r14b, the sink, and stationarity all remain (`rR14-2:244`).
- **"NEC-violating sink":** for κ_p > 0, by Lemma F0 under lift A. It is not shown to be inconsistent.
- **"OPEN"** is a worker reading. No FAIL or no-go is claimed, so a referee is not mandatory. One is recommended for §3 (the κ_p derivation and the L1-M exclusion), §4.1 (the compressed likelihood) and §5.2 (the forecast mapping).

## 11. What would decide it

1. **A survey-grade 3G siren forecast** for the specific shape Ξ = e^{γt_lb/2} (not a Ξ₀ with free n). It should cover ET + CE bright sirens, plus spectral or dark sirens and LISA MBHB, with H₀ and Ω_m marginalised. If σ(γ/H₀) ≲ 0.008, every one of the four drag ceilings (down to 0.016 H₀) would be testable at ≥ 2σ, though γ below the ceiling still would not.
2. **A tighter, strong-field drag bound** (`rR14-2:295`). If it lands at the signed estimate (≤ 0.024 H₀), every stated forecast puts E2's siren signal below 2σ, and the reading moves to TIE-HOLDS for the class.
3. **The owner's choice of FRW lift** (P-r1918a or b). It decides whether the background channel exists at all; that channel is currently non-decisive.
4. **For P-r14a only:** an LVK waveform or population likelihood for frequency-dependent amplitude damping. At its ceilings the predicted deficits are O(1) at 300 Hz for z ≳ 0.1, and are likely testable now.

**Sources (all RECALLED; no web access this run):**
- Belgacem, Dirian, Foffa, Maggiore, PRD 97, 104066 and PRD 98, 023510 (2018);
- Belgacem et al. (LISA CosWG), JCAP 07 (2019) 024;
- Mancarella et al. 2022, arXiv:2203.09238 (via `vR12-7:11`);
- DESI DR2 BAO, arXiv:2503.14738;
- Planck 2018 VI;
- the lensing-scatter fit as used in LISA/ET siren forecasts;
- Planck/ISW cross-correlation significance.
