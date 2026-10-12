# C5 round 16, probe R16-4: set A, route E1 — does anything observable remember the start? (worker report)

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker.
- **Not refereed.**
- Run 2026-10-12, 22:31Z to about 22:58Z.
- No repository file was edited.

**Scratch:** `scratchpad/C5/R16-4/`.
- `r164_checks.py` and `r164_checks.out` (sections [1]–[10]) hold every number below. Runtime is about 3 s with OMP_NUM_THREADS=2.
- SHA-256: script `2de95dd2…2ec5bb`, output `01ec13be…8d2e12c`.
- No downloads and no web fetches. Comparators come via earlier referees or are RECALLED.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `vR13-6` = `P/agents/C5_R13-6_referee_verdict.md` (and so on); `R13-6:n` = `P/agents/C5_R13-6_report.md:n` (and so on).
- `vR15-2` = `scratchpad/C5/ref_R15-2/REFEREE_VERDICT.md`. It appeared while I worked: **R15-2 CONFIRMED WITH CORRECTIONS, OPEN**.
- `out:[n]` = section n of `r164_checks.out`.

**What I read.**
- In full:
  - `AX`;
  - `TESTS:2302-2320` (C5 method), `TESTS:4561-4572` (round-13 rules), `TESTS:4682-4692, 4726-4733` (R13-6), `TESTS:4891-4897` (R14-2), `TESTS:4939-4951` (R15-2), and `TESTS:5037-5162` (round 16; R16-4 at `:5108-5126`);
  - `SUMMARY.md:534-675` (§§21–25);
  - `C5_S17_synthesis.md` §1 and §5;
  - `C5_R13-6_report.md`, `vR13-6`, and `C5_R13-6_referee.md:195-235`;
  - `C5_R14-2_report.md`, `vR14-2`, and `C5_R14-2_referee.md`;
  - `C5_R15-2_report.md` and `vR15-2`;
  - `vR11-5`, and `C5_R11-5_report.md:100-288`;
  - `vR12-4`.
- Grep only: `C5_S14_synthesis.md`, for set A and E1.

**Labels.**
- **proved:** derived here under the stated hypotheses.
- **checked:** a number in `r164_checks.out`.
- **suggested:** argued, not proved.
- **reading:** an interpretation.
- **comparator:** literature, via an earlier referee or RECALLED.

**Subtraction rule (`TESTS:4566`).** Each section of the output prints its subtraction.
- Initial-state differences are measured against the vacuum-start value of the same observable, at the same t.
- The meter domination bound subtracts the steady-state (vacuum) second moments.
- Energies, variances and envelopes are positive, so nothing is subtracted from them.
- The matter initial-record term is measured against Ψ₁(∞) = 0.

**Order rule.** Exactness holds at these orders:
- TT free-data conservation: linear order in G, on Minkowski space, with matter absorption of gravitational waves neglected;
- the meter bounds: Gaussian order (second order in the matter–meter coupling);
- PPN and bath friction: second order in the metric noise.

**New round-16 rules (`TESTS:5039`).**
- *Whole-zone v_max:* not applicable. Set A is a continuum. G_R is untouched, so free TT data propagate at exactly c.
- *Self-force on a moving compact body:* the initial-state terms add **no** velocity-proportional self-force at linear order (§3.5, proved). The repaired gain's residual is unchanged (`vR14-2:7`).
- *Ward:* only the **standard** linearized Bianchi identity is used (R15-2 Lemma B, `vR15-2:11`). No deformed identity is used.

---

## Reading against the FIXED readings (`TESTS:5122-5125`)

**Worker reading, primary class 𝒢(1, 1/ℓ): STATE-DEPENDENT.** The class is defined in §2. Because the observable's difference is never washed out, a **referee is required**. Until the referee rules, the recorded reading is OPEN.
- **The observable is the near-cone budget,** the gravitating gravitational-wave (GW) energy density at t − t₀ = t_H, against ρ_Λ.
- **Two states in the class:** the vacuum start and a start with one quantum-equivalent of free TT wave per mode for k ≤ 1/ℓ. Their budgets differ by Δρ = ħc/(4π²ℓ⁴):
  - 2.4e3 ρ_Λ at ℓ = 5e-6 m;
  - 1.5e6 ρ_Λ at ℓ = 1e-6 m;
  - 5.9e19 ρ_Λ at ℓ = 4e-10 m.

  The difference is the same at t_H as at t₀, and at every time (Lemma T: proved; checked out:[2], [5]).
- **This holds under both budget premises.** These are free gravitational waves, the component that gravitates in every budget premise used so far (premise (i), `C5_R11-5_report.md:245`).
- **The same reading holds for every class whose TT bound reaches ρ_Λ.** The condition is n_b·k_c⁴ ≥ 6.6e17 m⁻⁴. Examples:
  - one quantum per mode down to a wavelength of 0.22 mm;
  - a thermal (Planck) TT state at T ≥ 28.9 K (out:[5c,d]);
  - a classical (Rayleigh–Jeans) thermal TT state cut at 1/ℓ, at T ≥ 1.1e-3 K (ℓ = 1 µm) or T ≥ 0.14 K (ℓ = 5 µm). At the CMB's 2.73 K this gives 19 to 3.8e13 ρ_Λ (out:[5f]).

  For a classical metric, Rayleigh–Jeans is the natural "thermal" state.

**Small classes: OPEN, not WASHED-OUT.** Take n_b·k_c⁴ < 6.6e17 m⁻⁴ for the TT data and n_b < 1/8 for the meters. Then every listed difference at t_H is below its comparator:
- lab decoherence, budget, and drag: proved or checked;
- PPN second order and the record-growth slope: suggested only.

The FIXED WASHED-OUT reading needs "with proof, checked" for every observable. The second-order PPN coefficient is still power counting (`vR15-2:19`; `C5_R15-2_report.md:202-210`), so the reading stays OPEN. Nothing washes out the TT sector: the differences are small only because the class is small.

**Against the expectation (`TESTS:5126`).** The expectation was "WASHED-OUT, with only an unobservable logarithmic dependence left by the J₀ channel."
- The J₀ channel does forget, as t^{−1/2} in amplitude (§3.3).
- The logarithm belongs to the start **time** t₀ (Var h ∝ ln 8Ω(t − t₀)), not to the start **state**.
- What does not forget is the metric's own free TT data. E1 keeps G_R undamped (`R13-6:448`), so free-wave energy per mode is exactly conserved, as in linearized GR.

---

## 0. In plain words

- **The start-time universe remembers its initial gravitational waves exactly.** E1 does not damp gravitational waves; that is the difference from the leaky route, E2.
  - Any gravitational waves present at the start are still there today, with the same energy, mode by mode.
  - So late-time observations depend on the initial state as much as that state's wave content is large.
- **A modest initial wave content is already observable through the energy budget.** Take one quantum's worth of wave energy per mode, at every wavelength the record smearing can resolve. That alone exceeds the dark-energy density by 2.4e3 at ℓ = 5 µm, and by up to 6e19 at ℓ = 0.4 nm. A thermal bath of initial waves warmer than about 29 K does the same. For a classical, equipartition bath cut at the smearing scale, about 1 mK is enough at ℓ = 1 µm.
- **Everything else forgets, or barely matters.**
  - A disturbance in the record stream reaches the metric only through the J₀ kernel. It fades as one over the square root of the time since: by today, to about 1e-32 of its energy at micrometre scales.
  - An excited meter changes every listed observable by at most a fixed multiple of the vacuum prediction, and that multiple depends only on how excited the meter is. The lab tests have 9 or more decades of margin, so even 1e8 quanta per meter mode is invisible there.
  - Drag on the double pulsar does not depend on the start at all, at linear order.
- **What this means for the axiom question.** E1 must name its initial wave state. "No waves at the start" (h_TT = ḣ_TT = 0) is the only choice that keeps the metric a readout of records alone (`AX:82-83`); any other choice needs an initial record of the wave state. So the datum is not unobservable. Whether fixing it "privileges a state" (`AX:94`) remains the owner's question, now sharper.
- **The leaky route gives no relief here.** At the friction the double pulsar allows, E2 also keeps 95–98% of any initial wave energy at t_H (out:[10]).

---

## 1. Prior art (each counted once)

1. **R13-6 and its verdict.**
   - The model: the start state "meters in vacuum, h = ḣ = 0, couplings switched on" (`R13-6:148-151, 247`).
   - The explicit network starts in its steady state, with Γ_min ≤ 1/t_H (`R13-6:240-245`).
   - Finite-start corrections to the lab kernels are ≤ 1/(Ωt_H) (`R13-6:265`).
   - The metric is a linear functional of the records since t₀ (`R13-6:442`).
   - The verdict confirms Lemma D, Lemma S and the finite-start Var h. The exact J₀ output has a white-noise ḣ term that needs a regulator (`vR13-6:3-31`).
2. **R14-2 and its verdict.**
   - E1 and E2 are tied (`vR14-2:11-13`).
   - The initial-state question is posed at `C5_R14-2_report.md:268-273` (the "AX:94" row; readout holds "given the fixed initial h = ḣ = 0").
   - The residual drag with V_CMB included, and the τ_c ceiling of 1.49e-3 m (`vR14-2:7`).
   - P-r14b: stationary E2 needs a history much longer than t_H (`C5_R14-2_report.md:244`).
3. **R15-2 and its verdict.**
   - Lemma A, refereed: for k ≠ 0, only TT keeps the light-cone pole, and S/V are instantaneous constraints (`vR15-2:5`). **Used here: TT carries the only free initial data.**
   - Lemma B, refereed: the finite-start defect is repaired by B, which decays because the first moment is zero (`vR15-2:11`).
   - The leading-log TT weight of ¼ is refereed. The finite constant c₁ is not, because the worker omitted the f(t)J₀(0) term in K′ (`vR15-2:13`). **My runner includes that term** (out:[2], K′(0) = 0).
   - Exact irrational CP is not proved (`vR15-2:15`).
4. **R12-4:** a start time is a temporal boundary, not a privileged site (`vR12-4:15`).
5. **R11-5:** the test list (`C5_R11-5_report.md:213-236`); a finite frame age is allowed as a price (`vR11-5:18`).
6. **Lemma S** (`vR13-6:17-25`): Ĥ ↔ θJ₀, and Ĥ² = G_R.
7. **Repository grep** of `P/agents/`, `P/TESTS.md` and `P/SUMMARY.md`:
   - for "initial state", "initial-state", "attractor", "washed", "initial condition", "privileged state";
   - hits: only the R14-2 row above, the S17 and round-16 item text, and R15-2's Lemma B and B term.
   - There is no prior computation of initial-state dependence in E1.
   - `docs/` was not grepped.

## 2. Hypotheses and the class (stated before any title)

**H1 (model).** Per frame mode k, Ω = c|k|, preferred CMB frame:
- R13-6's linearized E1 model (`R13-6:144-157`) with the repaired gain F = e^{−k²ℓ²/2}(1 − 4iωτ)(1 − iωτ)^{−4} (P-r13b; τ = ℓ/c strict, or τ_c).
- R15-2's refereed channel split (`vR15-2:5`): two TT polarizations with a cone pole, and S/V constraint channels with none.
- The TT metric is h = h_free + G_R·J.
- The metric record noise is h_noise = K ⋆ ξ, with K = f ⋆ J₀(Ω·) and f(t) = e^{−x}x²(4 − x)/(2τ), x = t/τ.
- **Bandwidth regulator for ḣ:** the gain itself. K(0) = K′(0) = 0, with K′ = f(t)J₀(0) − f ⋆ J₁ as corrected by `vR15-2:13` (out:[2]).

**H2 (meters).** The explicit finite network of `R13-6:240-245`:
- a stable linear Gaussian network with smallest damping Γ_min ∈ (0, 1/t_H];
- its "vacuum" is its steady state.

The exact s₀ = 0 limit is treated separately, as suggested only.

**H3 (start).** As R13-6 at t₀, with R15-2's initial constraint record B for matter present at t₀ (P-r15a). Matter states are outside the class.

**The class 𝒢(n_b, k_c).**
- It is a product over normal modes of Gaussian states, each thermal, squeezed or displaced, or a mixture of these.
- In each mode, the excess energy over the vacuum start is at most n_b quanta-equivalent, n_b·ħΩ_mode:
  - for the free TT data (h_TT(t₀), ḣ_TT(t₀)) of every mode with |k| ≤ k_c, both polarizations;
  - for every internal meter mode.
- **The S/V metric has no free data.** It is fixed by the constraints at t₀ (`vR15-2:5,11`).
- **Primary bound:** n_b = 1 and k_c = 1/ℓ. These are the modes to which matter couples through the spatial smearing ½h_μν(g⋆T^{μν}) (`R13-6:146`).
- **Why the product restriction:** correlated multimode squeezing or displacement can concentrate many modes' energy into one collective mode. Per-mode bounds then fail to control local second moments (out:[1], [4]).

**Excluded realizations.**
- E2.
- Non-Gaussian initial states.
- Correlated multimode initial states (bounded separately, §3.4).
- Matter initial states.
- Cosmic expansion (§6).
- Nonlinear gravity, beyond the second-order estimates.

**Observables** (R11-5/R13-6's list, `TESTS:5114`): lab decoherence (Cs-133 at 70 s, LPF, torsion), the near-cone budget, PPN-type terms, the double-pulsar drag, and record growth. All are evaluated at t − t₀ = t_H.

---

## 3. Lemmas

### 3.1 Lemma L: superposition (proved)

H1–H2 are linear, with Gaussian noise that is independent of the initial state. So, for any two initial states, the difference at time t:
- in means is Φ(t)δm₀;
- in covariances is Φ(t)δV₀Φ(t)ᵀ.

Here Φ is the homogeneous propagator of (TT metric, meter, classical post-filter). There are no cross terms between the initial state and the later noise. Every initial-state memory is a property of Φ.

### 3.2 Lemma T: the free TT data are an exact memory (proved; checked out:[2])

In E1 the h-equation is □h = source with **G_R untouched** (`R13-6:448`; `vR14-2:11`). Three facts follow.
- J is a functional of matter's stress and the record noise. It does not depend on h_free, because the meters read matter, not the metric.
- So Φ restricted to the TT free data is the undamped rotation (h, ḣ/Ω) ↦ R(Ω(t − t₀))(h, ḣ/Ω).
- For every realization, the free-wave energy per mode is constant, and its phase advances at Ω.

Hence, for every observable that is a mode-diagonal functional of the TT energy, E_state(t) − E_vac(t) = E_init,exc for all t ≥ t₀, at linear order in G.

| Check (Ω = 1, τ = 0.2, 8000 paths) | t = 20 | t = 100 | t = 399 |
|---|---|---|---|
| ⟨E⟩_vac (the exact value is ¼∫₀ᵗ(K² + K′²): 1.868, 2.230, 2.539) | 1.841 ± 0.022 | 2.219 ± 0.026 | 2.568 ± 0.030 |
| thermal − vacuum (initial excess 1) | 0.983 ± 0.024 | 1.009 ± 0.026 | 0.989 ± 0.028 |
| displaced − vacuum (initial 0.5) | 0.517 ± 0.017 | 0.500 ± 0.016 | 0.472 ± 0.016 |

The vacuum content grows like ln t. The excess does not move.

**No attractor.**
- A squeezed initial state also keeps its quadrature angle, which rotates at Ω, mode by mode.
- Band-averaged observables lose that phase as 1/(Δω·t), but never the energy (suggested; elementary).
- Only matter absorption of GWs could damp the free data, and it is negligibly small (suggested).

### 3.3 Lemma J: record-current perturbations fade as t^{−1/2} (proved; checked out:[3])

A perturbation δI of the homodyne current reaches h through G_R·R = Ĥ/√2 (`R13-6:192-197`), times the gain. So δh = (K ⋆ δI)/√2.

For a pulse:
- t·(K² + K′²) → (2/π)|F_t(Ω)|². The check gives 0.89245 at t = 1e4/Ω, against 0.89246 predicted, with |F_t|² = 1.402 at Ωτ = 0.2.
- The pulse energy left at t is ≈ |F|²/(πΩt).
- At t_H this is 4.9e-33 for k = 1/µm, 7.3e-16 for k = 1/AU, and 1.5e-7 for k = 1/kpc (out:[3]).

**Scope.** This attractor covers the record-current sector only.

A perturbation of the classical post-filter's internal state at t₀ is different. It is a fictitious pre-t₀ record history entering a chain that starts with h = ḣ = 0, and it leaves a free wave. By Lemma L it is the same as nonzero TT data, so Lemma T applies (proved).

### 3.4 Lemma M: meter domination (proved under H2 for product states; checked out:[1], [4])

Take an internal meter state with covariance V₀ and mean m₀, against the steady state V_ss (= vacuum). Let y be any output functional at time t. Then:
1. **Covariance:** c_tᵀ(V₀ − V_ss)c_t ≤ Λ(n_b)·c_tᵀV_ss c_t, with **Λ(n) = 2n + 2√(n(n+1))**, the pure-squeeze worst case. Thermal states give 2n and displaced states 4n.
   - Sampled supremum: 4.8248 at n = 1, against the formula's 4.8284 (out:[1]).
   - On 200 random passive 4-mode networks, the worst ratio is 0.835 ≤ 1 (out:[4]).
2. **Mean:** (c_t·m₀)² ≤ (Σ_j 4|α_j|²)·c_tᵀV_ss c_t. This is set by the **total** displaced quanta, not the per-mode bound (out:[4]: the ratio to 4n_b reaches 1.52).
   - Means enter only first-moment (deterministic-force) observables and mode-diagonal energies.
   - They do not enter decoherence functionals, which depend on covariances.
3. **The vacuum internal part is at most the vacuum total.**
   - The steady state at t₀ is independent of inputs after t₀.
   - Hence Var y = Var y_int + Var y_rest ≥ Var y_int.
   - The same holds for any positive quadratic observable Q: lab decoherence functionals, ⟨ḣ²⟩ (the budget), ⟨h²⟩ (PPN).

   **So |Q_state − Q_vac| ≤ max(Λ(n_b), 1)·Q_vac** for the covariance part.
4. **Decay.** c_tᵀV_ss c_t = |Φ(t)ᵀc|²/2 falls as e^{−2Γ_min(t − t₀)}. R13-6's explicit model needs Γ_min ≤ 1/t_H for its ε ln t growth (`R13-6:240-245`).

   **So the slowest meter modes are not washed out at t_H. The bound above is what holds.**
5. **The exact s₀ = 0 limit** (an arcsine continuum of undamped modes, `R13-6:226-229`) never forgets the occupations of its internal modes (suggested; realization-dependent). There is no steady state to dominate by (Theorem U), so the bound is stated only for H2.

### 3.5 Drag: state-independent at linear order (proved)

Lemma D's self-force is the odd-in-ω part of the body's **own** mean response, F·G_R acting on its own ρ (`R13-6:358-366`; `vR13-6:3-7`). Initial data add a homogeneous solution that does not depend on the body's velocity. Two consequences:
- Γ_drag is the same for every state in the class.
- With the repaired gain it is 2.3e-28 s⁻¹ (strict, ℓ = 5e-6 m), against the bound of 6.1e-21 (`vR14-2:7`; `C5_R14-2_report.md:173`).

**Second order: friction from the initial GW bath (suggested).**
- Take a geometric momentum-transfer cross-section 4π(GM/c²)². This gives Γ ≤ 3.2e-41 s⁻¹ × (ρ_init/ρ_Λ) (out:[9]).
- It is below the bound unless ρ_init ≳ 1e19 ρ_Λ, and a Coulomb-type logarithm could lower that to about 1e18.
- The budget constraint is far stronger than this.

### 3.6 The matter initial record B (outside the class; refereed lemma, rechecked)

- Ψ₁(∞) = ∫t f = 5e-14 τ, which is zero to quadrature precision.
- |Ψ₁(s) − Ψ₁(∞)| = 2.8e-2, 9.1e-6 and 1.4e-13 at s = 10τ, 20τ and 40τ (out:[8]).
- So B, which `vR15-2:11` confirmed, is gone within about 40τ ≤ 2e-10 s of t₀ (τ ≤ 5 ps).

Its one-shot decoherence at t₀ (P-r15a) is a matter-state datum, not in the class.

---

## 4. Probe (a): vacuum start against the worst state in 𝒢(n_b, k_c), at t − t₀ = t_H

| Observable | TT free data (Lemma T) | Meter (Lemma M) | Comparator | At n_b = 1, k_c = 1/ℓ | Label |
|---|---|---|---|---|---|
| **Near-cone budget** (gravitating GW energy) | **Δρ = n_b ħc k_c⁴/(4π²), constant in t.** k_c = 1/ℓ, n_b = 1: 2.43e3 (5e-6 m), 1.52e6 (1e-6 m), 1.52e14 (1e-8 m), 9.5e16 (2e-9 m), 5.93e19 (4e-10 m) × ρ_Λ. Threshold n_b* = 4.1e-4 to 1.7e-20 (out:[5a]). | ≤ max(Λ(n_b), 1)·ρ_rec(t_H). Below the comparator for n_b < 1/8 (Λ = 1), given ρ_rec ≤ ρ_Λ. Above that, realization-dependent. | ρ_Λ = 5.27e-10 J/m³ | **TT: exceeds by ×2.4e3 to ×5.9e19 (FAIL of washing out)** | TT: proved + checked. Meter: proved bound, ρ_rec ≤ ρ_Λ premise-laden (`vR15-2:17`) |
| Lab decoherence (Cs-133 70 s, LPF, torsion) | Cs dephasing ≤ 3.4e-56 (ℓ = 4e-10 m) per 70 s, via (mv²/ħ)²⟨h²⟩(ℓ/c). LPF tidal √S_a ≤ 1.8e-49 m s⁻²/√Hz at 1 mHz (out:[6]). | ≤ Λ(n_b) × the vacuum prediction. The vacuum is ≥ 9 decades below the comparators (`R13-6:344`; `vR11-5:12`, conditional scope). Below the comparator for n_b < 2.5e8 (out:[6]). | Panda et al. 70 s; 1.74e-15 m s⁻²/√Hz; torsion σ_a² (via `vR11-5:12`) | below by ≥ 9 decades (meter) and ≥ 30 decades (TT) | meter: proved bound on inherited margins; TT: suggested estimate |
| PPN-type, first order | 0: free waves are homogeneous, not body-centred 1/r terms | 0: the mean field is F·G_R⟨T⟩, independent of the meter state | α̂₂ < 1.6e-9, \|α̂₁\| ≲ 4e-5 (via `C5_R14-2_report.md:191`) | 0 | proved (linear) |
| PPN-type, second order | Fluid: 1.6e-33·ρ_init/ρ_crit at 1 AU, giving 6.6e-14 at ℓ = 4e-10 m. ⟨h_ijh_ij⟩_init = 16n_bℓ_P²k_c²/π = 8.3e-51 (out:[7]). | ≤ Λ × the vacuum's ⟨h²⟩ term | as above | below by ≥ 4 decades | suggested (power counting, as `vR15-2:19`) |
| Double-pulsar drag | 0 at linear order (§3.5); bath friction ≤ 3.2e-41(ρ_init/ρ_Λ) s⁻¹ | 0 at linear order | 6.1e-21 s⁻¹ (`vR13-6:7`) | linear: 0. Bath: ≤ 1.9e-21 at 4e-10 m (geometric; log caveat) | linear proved; bath suggested |
| Record growth (slope dE/d ln T at t_H) | identical: the excess is constant (Lemma T; out:[2]) | the excess is ≤ Λ·ρ_rec and decays as e^{−2Γ_min t}; slope change suggested ≤ Λ·O(Γ_min t_H) | the budget itself | 0 (TT) | TT proved; meter suggested |

**The record's own wave content, for scale.**
- Formula: n_rec(k) ≈ ε|F|²·[ln(Ωt_H) + O(1)]/(2π), about 11–12.5·ε|F|² quanta per mode at t_H (out:[5e]).
- It uses the refereed ¼ weight; the O(1) constant is unrefereed (`vR15-2:13`).
- In the strict variant, n_rec(1/ℓ) is a factor of about 3–4 below the TT threshold n_b*(1/ℓ) (out:[5e]). So an initial wave state comparable to what the records themselves make by t_H already reaches the comparator.

**Classical thermal TT states** (k_BT per mode and polarization, cut at 1/ℓ). These reach ρ_Λ already at T_RJ* = 7e-14 K (4e-10 m), 1.1e-9 K (1e-8 m), 1.1e-3 K (1e-6 m) and 0.14 K (5e-6 m) (out:[5f]).

**The τ_c variant.**
- Choosing k_c = 1/(cτ_c) instead raises the thresholds to n_b* = 1.4e2 to 3.2e6 (out:[5b]).
- But modes between 1/(cτ_c) and 1/ℓ still couple to matter: the coupling is spatially smeared only (`R13-6:146`).
- So the reading for 𝒢(1, 1/ℓ) holds in both variants.

## 5. Probes (b) and (c): attractor and permanent memory

| Sector | Attractor? | Rate | Label |
|---|---|---|---|
| TT free data (h_TT, ḣ_TT at t₀) | **none** | energy exactly conserved; phase rotates at Ω | proved, checked [2] |
| Record current / meter output perturbations | yes | amplitude ∝ \|F(Ω)\|(πΩt/2)^{−1/2}; energy ∝ \|F\|²/(πΩt) | proved, checked [3] |
| Classical post-filter state | none (it is equivalent to TT data) | — | proved (Lemma L) |
| Internal meter modes (H2) | yes, exponential | e^{−Γ_j(t − t₀)}, with the slowest Γ_min ≤ 1/t_H by construction, so **not attracted within t_H** | proved, checked [4] |
| Internal meter modes (exact s₀ = 0) | none for the undamped modes | — | suggested |
| S/V constraint channels | no free data | — | refereed Lemma A (`vR15-2:5`) |
| Matter initial record B | yes | ∝ s³e^{−s/τ}; gone in about 40τ | proved (`vR15-2:11`), checked [8] |

**(c) The quantity with an O(1) memory of the start at every time** is the free TT wave content: its energy per mode exactly, and for displaced states the whole phase-coherent waveform. In the exact s₀ = 0 limit, the undamped meter-mode occupations also qualify (suggested).

**The logarithm the item expected is a start-time effect.** Vacuum-start Var h ∝ ln 8Ω(t − t₀), with the referee's form at `vR13-6:27`. So two vacuum starts that differ in t₀ by Δ differ at time t by a fractional amount ≈ Δ/[(t − t₀)·L], and this decays.

## 6. Probe (d): prices (named, not adopted)

- **P-r16a (new). A law-supplied initial TT datum.**
  - E1's late-time universe depends permanently, mode by mode, on the TT free data at t₀ (Lemma T). So the law must state them.
  - **The minimal choice** is h_TT = ḣ_TT = 0, R13-6's choice.
    - *Reading:* it is the unique TT datum that keeps the metric a readout of record content alone (`AX:82-83`; `R13-6:442`; `C5_R14-2_report.md:268`).
    - Any nonzero datum needs an initial TT record at t₀, an analogue of P-r15a. That record is observable through the budget once n_b·k_c⁴ ≳ 6.6e17 m⁻⁴.
  - *Axiom text:* the open gate `AX:185-186` (record-production dynamics, arrow) gains an initial condition as well as a time origin.
  - Under `AX:92` ("A state is a configuration of records"), the state at t₀ is the empty record configuration, plus B under P-r15a. The owner question at `AX:94` is therefore: **does a law that says "no non-record metric content at the first instant" privilege the empty configuration?** It is no longer about an unobservable datum.
- **P-r16b (class restriction, conditional).**
  - The meter bound uses product initial states.
  - Correlated multimode states can concentrate energy: Λ grows like 4N·n_b over N correlated modes (out:[1]).
  - If such starts are allowed, the meter sector needs a total-energy bound instead.
- **Carried over:** P-r11a, P-r13a, P-r13b, P-r15a (`vR15-2:11`), P-r1, P-r11b, and the remainder of R14-2's list (`C5_R14-2_report.md:252-271`).
- **Cosmic expansion (outside the setting; RECALLED).** Occupation numbers of free comoving modes are adiabatic invariants. A class defined by n_b per mode today therefore gives the same ρ_init today. A class defined at t₀ in physical k is diluted by expansion. In that case the reading depends on the expansion history between t₀ and today.

## 7. E1 against E2 on this question (reading; E2 is outside the setting)

E2's friction damps TT energy at rate γ. At the drag-allowed γ = 0.016–0.047 H₀ (`vR14-2:3`), it keeps 95.6–98.5% of the initial TT energy at t_H (out:[10]).

So **on a history of about t_H neither route forgets the initial wave state.** E2's "no distinguished state" needs P-r14b (a history far longer than t_H) for this sector too. The initial-state question does not separate the routes observationally.

## 8. Strong words checked

- **"Exact memory":** linear order in G, on Minkowski space, with the record not reading h (H1). Matter absorption of GWs is neglected (suggested to be negligible).
- **"STATE-DEPENDENT":** a worker reading. It holds for the stated primary class 𝒢(1, 1/ℓ) and for any class with n_b·k_c⁴ ≥ 6.6e17 m⁻⁴. The observable is the budget, under the Isaacson premise for free waves; the comparator is ρ_Λ, as in R11-5, R13-6, R14-2 and R15-2. **A referee is required.**
- **"Below the comparator" (lab):** rests on R6-4's inherited margins (`R13-6:344`, conditional scope `vR11-5:12`). Λ(n) is checked by sampling (out:[1]) and by its closed form.
- **"Not washed out at t_H" (meters):** holds for H2's Γ_min ≤ 1/t_H. A realization whose low-frequency response is carried by fast modes would forget faster; only the bound is claimed.
- **"t^{−1/2}":** an asymptotic of the J₀ tail with the gain included, checked from t = 10 to 1e4.
- **"Unique record-compatible datum":** a reading of `AX:82-83`, not a theorem.

## 9. What would decide it

1. **A referee of Lemma T and of the budget comparison.** In particular: whether "near-cone budget against ρ_Λ" is an admissible observational comparator for free initial waves; whether k_c = 1/ℓ is the right class edge; and whether matter absorption is negligible.
2. **The owner's choice of initial-state class.**
   - If the law fixes h_TT = ḣ_TT = 0 (P-r16a, minimal), the question becomes the `AX:94` reading alone.
   - If any Gaussian TT start with one quantum per resolvable mode is "reasonable", E1 is STATE-DEPENDENT.
3. **The second-order PPN coefficient** (as R15-2). It is needed only to turn the small-class OPEN into WASHED-OUT.
4. **For the meters, a concrete QMFS realization** of g = √2FĤ. This would replace Lemma M's bound with numbers.

**Sources.**
- Via earlier referees: double-pulsar bound 6.1e-21 s⁻¹ (`vR13-6:7`); α̂₁ and α̂₂ (`C5_R14-2_report.md:191`); the lab comparators (`vR11-5:12`).
- RECALLED:
  - ρ_crit, ρ_Λ = 0.69ρ_crit and t_H, as R13-6;
  - Ω_GW–S_h relation;
  - LPF test-mass separation 0.376 m;
  - Cs-133 mass;
  - adiabatic invariance of mode occupations;
  - the Planck energy density.
