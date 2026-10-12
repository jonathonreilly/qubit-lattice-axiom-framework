# C5 R15-4 report: a regular P-T reader (transitions, lumpy universe, DESI-like evolving w)

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-12, 22:04Z to 22:45Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R15-4/`. Scripts and outputs are in `S/scripts/`. Each runs in under 2 min at `OMP_NUM_THREADS=2`.
- `r154_reader.py/.out`: the reader designs, the step-response formula, the R14-5 runner cases, the R13-3 S1/S2 transition grid, and the positivity facts.
- `r154_lagfree_scan.py/.out`: exact-constraint designs with and without lag-free conditions, plus positivity.
- `r154_bbn.py/.out` and `r154_bbn_diag.py/.out`: the reader through e⁺e⁻ annihilation, which happens during BBN.
- `r154_desi.py/.out`: (c) constant w; tracking of the DESI DR2 CPL; the inverse problem; g/H².
- `r154_nogo.py/.out`: an LP check of the positivity no-go (Lemma N+).
- `r154_lumpy.py/.out`: (b) sympy identities, a T³ curvature-average check, and backreaction magnitudes.
- `r154_nnls.py/.out`: a nonlinear constrained-fit reader as an escape test.
- `r154_p2_random.py/.out`: Lemma P2 on random 𝓗₄ histories, plus a phantom control.

**Read.**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (`AX`); `TESTS.md:2302-2320` (C5 method); `:4860-4988` (round 14 items 4–5 and their verdict lines; round 15 items 1–4; my item is `:4969-4988`); `agents/C5_R14-5_report.md`; `agents/C5_R14-5_referee_verdict.md` (`vR14-5`); `scripts/C5/R14-5/r145_homog.py/.out`; `scripts/C5/R13-3/r133_transition.py` and `r133_de_encoder.py`.
- In part: `TESTS.md:4615-4733` (R13-3 registration and result); `agents/C5_R13-3_report.md:225-266`; `C5_R13-3_referee_verdict.md:59`; `agents/C5_R12-2_report.md:1-80, 120-240` (Rule P `:179-190`, Lemma G `:192`, Lemma K `:198`).
- The Λ entries R5-3, R10-4, R11-3 and R12-2 were read through the R14-5 report's prior-art list (`C5_R14-5_report.md:113-148`), not line by line.

**Labels.** proved / checked (sympy or numerics run here) / suggested / reading / comparator.
- A comparator is **V** if fetched this run. That covers DESI DR2 w₀w_a from arXiv:2503.14738 v3, Table 5 and Eqs. 25–28: DESI+CMB (−0.42 ± 0.21, −1.75 ± 0.58); +Pantheon+ (−0.838 ± 0.055, −0.62 +0.22/−0.19); +Union3 (−0.667 ± 0.088, −1.09 +0.31/−0.27); +DESY5 (−0.752 ± 0.057, −0.86 +0.23/−0.20).
- Otherwise a comparator is **RECALLED**.

**Subtraction rule.**
- ε := ρ̂/ρ_nc − 1, where ρ_nc is the exact non-vacuum content (radiation + dust + released latent heat, plus e±/ν where present).
- Λ̃ := λ + κρ_v = θ²/3 − 𝓔_nc (R14-5's definition, `C5_R14-5_report.md:24`).
- "Vacuum" means any part of ρ_tot that is constant in time.
- For CPL dark energy (DE), ρ_nc includes all of ρ_DE, because CPL has no constant part (ρ_DE → 0 at both a → 0 and a → ∞ for all four DESI sets).
- Nothing else is subtracted.

---

## 0. Verdict against the FIXED readings (`TESTS:4984-4988`)

**Worker reading: FAIL, bounded to a stated class (test (c)), for the referee. Tests (a) and (b) PASS inside that class.**

**What is built (§2).** A regular reader that annihilates constants exactly. It is a causal **linear** filter with M = 2 first-order registers on the history of E := −dρ_tot/du (u = ln a). Inside the R14-5 model, E is exactly the clock law's own global number, κE = 2S(t) (proved, §4).
- It is real and bounded for every history with finite energy density and finite first derivative.
- It is exact for any radiation + dust mixture: G(3) = G(4) = 1.
- It has **ρ̂ ≥ 0 for every history in the class 𝓗₄** (proved, Lemma P2). 𝓗₄ is any mixture of components with −1 ≤ w ≤ 1/3 plus any number of nonnegative vacuum-to-content releases of any size and width. The clamp P-r13d is not needed.

**(a) PASS (proved; checked).**
- **Bound.** Through S1/S2 transitions of every width, including an exact step: ε ∈ [−α_r, +0.8α_r] for D1 and [−α_r, +2.48α_r] for R*. Here α_r is the released-heat fraction still present. The relaxation is exponential, e^{−(β₁−4)τ}.
- **The five R14-5 runner cases with D1.** min ρ̂/ρ_nc = 0.986–0.999, against Prony's −3.43 / −482 / −34.3.
- **EW and QCD.** Both residuals are ≤ 9e-5 by T = 1 MeV.
- **Limit.** The reader is exact only on exponential content. Through e⁺e⁻ annihilation, which is itself in the BBN window, it errs by an equivalent ΔN_eff of +0.43 (D1) or +0.16 (R*) at T ≈ 0.07 MeV. Against the ~0.3 BBN scale (RECALLED) that is marginal for R* and in tension for D1.

**(b) PASS (proved; checked in linear theory).**
- In the R14-5 model the Hamiltonian density 𝓔(x) = κT_nn − R/2 + σ²/2 is **uniform on each CMC slice** (proved). A reader on 𝓔, or equivalently on S(t), therefore needs no slice average: P-r13b is no longer needed.
- It gives Λ̃ = R̂[𝓔_nc] − 𝓔_nc exactly. Λ̃ is the reader error on content that now includes the backreaction terms.
- Numbers: Λ̃/Λ_obs = −2.3e-8 (D1) and −1.1e-7 (R*), against +9.9e-7 for R14-5's ⟨ρ⟩-reader. This is linear theory with recalled inputs.
- The exact identity Q̃ = 𝓔_nc + σ² + (κ/2)(ρ+3p)_nc closes the positivity gap the referee found (`vR14-5:62`). Lapse positivity reduces to one global inequality, 𝓔_nc > 0, plus the strong energy condition (SEC) pointwise.

**(c) FAIL in class 𝓡⁺ (proved; checked).** 𝓡⁺ is the set of causal, linear, u-translation-invariant readers of E that are exact for dust and nonnegative on reheating histories. The model needs the last property: ρ̂ < 0 means H² < 0.
- Lemma N+: every reader in 𝓡⁺ has G(x) ≤ x(4−x)/3 for 0 < x < 3, and **G(x) ≤ 0 for every phantom x < 0**.
- DESI CPL is phantom at z ≳ 0.4 in all four DR2 sets, so no reader in 𝓡⁺ tracks it.
- Checked:
  - for D1, R* and the non-positive D3, the tracking residual after the one unobservable renormalization is 3–43% in H(z) and 2–52% in D_M at DESI redshifts;
  - Lemma N0 (any reader continuous at constants, nonlinear readers included) has a dead band near w = −1, and a nonlinear fit shows it at 1+w ≲ 0.01.

**(d) Residual and tuning.**
- The vacuum's part of Λ̃ is **exactly zero** for every constant and every number of transitions, with no tuned number (proved).
- What remains is content-reading error: transition transients (bounded, decaying), e⁺e⁻ (above), backreaction (≤ 1e-7 Λ_obs), and DE misreading. The last is of order Λ_obs, and it is where (c) fails.

**The escape, and what it costs (c2: checked, reading).** The observed DE in this model is R̂[true DE], not the true DE.
- For each DESI DR2 set there is a true DE history with **E_true ≥ 0 everywhere**, i.e. never phantom, whose reading is *exactly* DESI's phantom-crossing CPL. That holds for D1, R* and D3.
- So the apparent phantom crossing comes out naturally from a vacuum-blind reader acting on ordinary non-phantom dark energy.
- The cost: Λ̃ ≠ 0 relative to the true content, and the E-fluid is active today, with g/H² = −0.3 to −1.1 at z = 0 for R*. That brings back R14-5's instantaneous-response price at late times, and its horizon-scale perturbation effects are not computed.

**Why FAIL and not INCONCLUSIVE.** The FIXED FAIL reading asks for a no-go in a stated class showing that no causal regular reader annihilates constants while tracking the stated content. Lemma N+ is that, for 𝓡⁺ and DESI-like (phantom-crossing) content, and N0 gives a general dead band near w = −1.
- Outside 𝓡⁺ the item stays INCONCLUSIVE. That covers nonlinear or non-time-invariant readers, and readers allowed to go negative after reheating.
- A naive nonnegative constrained fit (NNLS) was tried and fails worse (§4.4), but that is not a no-go.

---

## 1. In plain words

- **What was broken.** R14-5's expansion rule worked out the "real" (diluting) energy from the slope, curvature and higher wiggles of the energy history at one instant. At a phase transition those wiggles become enormous, and the rule returned nonsense: negative energy, an imaginary expansion rate.
- **The fix.** Read only the slope (how fast the total energy is dropping, which is exactly the pressure-plus-energy of the real stuff), and average it over the recent past with fixed weights.
  - Two memory registers per site are enough. Each one leaks at its own rate and is fed by the slope.
  - A constant (any vacuum, of any size) has zero slope, so it is never seen.
  - The weights are chosen so that radiation and ordinary matter are read exactly.
  - Because the rule only adds up past slopes, it can never blow up. With the two-register weights it can be proved never to go negative, whatever the phase transitions do.
- **Lumpy universe.** In R14-5's clock model one combination, energy density minus spatial curvature plus shear, is automatically the same at every site at a given grid time. A rule that reads that combination needs no averaging over the universe, and it reads the "backreaction" of galaxies along with the matter. What leaks through is about one part in ten million of the observed dark energy.
- **Where it breaks: evolving dark energy.** A rule blind to constants is almost blind to anything that changes slowly.
  - Dark energy that is nearly a constant is mostly not read.
  - Dark energy that grows (phantom) is read with the wrong sign. That is a theorem for every rule of this kind that can never go negative.
  - DESI's best fits have a phantom past, so such a rule cannot reproduce "the content" as the item asked.
- **The twist.** Run backwards, the same rule turns perfectly ordinary dark energy (never phantom) into exactly the phantom-crossing curve DESI reports. The dark energy we infer would be the rule's reading of the true dark energy. The price is that the grid's global clock sector is still active today, not only during early-universe transitions.

---

## 2. Hypotheses and classes (stated before titles)

- **H-model.** R14-5's class 𝒵 (`C5_R14-5_report.md:34-41,161-174`):
  - a smooth continuum CMC lattice time;
  - E_ni = 0, E^TL = 0, E_nn = λ(t);
  - conserved total stress;
  - H-vac-Λ;
  - sites created at the uniform rate θ(t);
  - lapse law −D²N + Q̃N = S(t) with ⟨N⟩ = 1;
  - g = −(2/3)(θ̇ + S).
  - **Not assumed proved:** CMC foliation existence (H-CMC-exist, `vR14-5:64-66`). Positivity uses the maximum principle given existence.
- **H-clock.** u = ln a = (1/3) ln(site count). Because creation is uniform, each site's own count gives the same u (R14-5 site rule, `:167`).
- **Reader class 𝓛 (built).** ρ̂(u) = ∫₀^∞ K(s)E(u−s)ds, with K(s) = Σ_j k_j e^{−β_j s} and β_j > 4. Its state-space form is y_j′ = E − β_j y_j and ρ̂ = Σ k_j y_j. Creation law: θ²/3 = κρ̂.
  - Response to a component ρ ∝ e^{−xu}: G(x) := ρ̂/ρ = Σ_j k_j x/(β_j − x). Always G(0) = 0 (constants annihilated).
- **Class 𝓡⁺ (for the no-go).** Any causal, linear, u-translation-invariant reader of E, with:
  - (i) G(3) = 1;
  - (ii) ρ̂ ≥ 0 on reheating histories. A reheating history has all content created as radiation from a vacuum at one instant.
  - **Why (ii) is required, not chosen (reading).** In this model the hot universe starts as exactly such a history, and ρ̂ < 0 means H² < 0, which contradicts c = θ ≥ 0 (P-arrow, `C5_R14-5_report.md:337`).
  - u-translation invariance is the reading of `AX:94-95` ("a law privileges no states"). A u-dependent kernel would privilege epochs.
- **Content classes.**
  - 𝓗₄: mixtures of components with 0 ≤ x_i ≤ 4 and nonnegative densities, plus any nonnegative releases into such components.
  - S1/S2 sectors of R13-3 (`C5_R13-3_report.md:231-235`).
  - e⁺e⁻ thermodynamics with instant ν decoupling.
  - CPL with the four DESI DR2 (w₀, w_a).
- **Excluded:**
  - the Z³ construction (S1/S3/S4 carried);
  - inhomogeneous bubble dynamics;
  - nonlinear backreaction;
  - inflation;
  - perturbations of the active g ≠ 0 sector today;
  - nonlinear readers, except the one NNLS test.

---

## 3. Prior art (each counted once)

1. **R12-2 Rule P (Prony)** (`C5_R12-2_report.md:179-190`) [ref]. It is exact for N constant-w components, but nonlinear and instantaneous: it uses m₁…m_{2N}.
2. **R13-3 (d)/(e)** (`C5_R13-3_report.md:228-266`; verdict `:59`) [ref].
   - Prony leaks ∝ α/W and goes negative for α/W ≳ 10.
   - The CPL is not reconstructed for N ≤ 5.
   - The referee notes that the transition runner misclassifies complex roots.
3. **R14-5 and verdict** [ref]:
   - Lemma C, and the CMC necessity (`vR14-5:5-27`);
   - the Prony transition law gives H² < 0 (`vR14-5:41-43`);
   - the positivity bound drops ⟨R⟩ and ⟨σ²⟩ (`vR14-5:55-63`);
   - lumpy Λ̃ = ½⟨R⟩ − ½⟨σ²⟩ (`C5_R14-5_report.md:257`).
   - **This run builds the regularized reader R14-5 left as P-r13d.**
4. **Comparators.**
   - DESI DR2 w₀w_a (V, above).
   - RECALLED: BBN/CMB ΔN_eff ≲ 0.3; the BBKS transfer function; Planck-like Ω_m = 0.31, h = 0.677, n_s = 0.965, σ₈ = 0.81; DESI DR2 effective redshifts 0.295–2.33; Buchert-type backreaction of order 1e-5–1e-6.
   - The linear "fixed-node Prony" and state-space realizations are standard signal-processing constructions (RECALLED). I found no repository precedent: a grep of `P/` for "regularized reader", "linear filter" and "register" returned only R13-3/R14-5's "pre-filter" mentions (`C5_R13-3_report.md:251`).

---

## 4. Results

### 4.1 The reader and its exact properties (proved; checked `r154_reader.out:1-27`)

**Exactness.** G(x) = 1 for x ∈ {3, 4} fixes k for two registers.
- D1: β = (6, 8), k = (−2, 5).
- R*: β = (20, 24), k = (−136, 175).
- D3 (5 registers) and D5 (lag-free, G′(4) = 1/4) are comparators.

**Annihilation.** ρ̂ depends only on E = −dρ_tot/du. A vacuum, constant between transitions, contributes nothing (proved). At a transition the vacuum drop and the latent heat cancel in ρ_tot, so E = 3(ρ+p)_nc at all times (proved: total energy conservation and (ρ+p)_vac = 0).

**Step response (proved; checked to 9 digits, `r154_reader.out` Part 4).** Latent heat Δ released at u_T into a sector of rate x_s gives, for τ = u − u_T > 0:
- ρ̂ − ρ_nc = −Δ_s(u)(1 − G_τ(x_s)), with G_τ(x) = Σ k_j x(1 − e^{−(β_j−x)τ})/(β_j − x).
- A release of any width W is this step response convolved with s′ ≥ 0, so the bound is independent of W. Prony's α/W blow-up is absent.
- D1: 1 − G_τ(4) = −4e^{−2τ} + 5e^{−4τ} ∈ [−0.8, 1], and 1 − G_τ(3) = −2e^{−3τ} + 3e^{−5τ} ∈ [−0.20, 1] (`r154_reader.out` Part 5).

**Lemma P2, positivity (proved).** Let k₁ ≤ 0 ≤ k₂ and β₁ < β₂ in a two-register reader exact at x = 4, and write H(t) := ∫₀ᵗK e^{4s}ds.
- Then H(t) = ¼ + c₁y^{p₁} − (¼ + c₁)y^{p₂}, with c₁ = −k₁/(β₁−4) ≥ 0, y = e^{−t} and p₂ > p₁. Since y^{p₂} ≤ y^{p₁}, H(t) ≥ ¼(1 − y^{p₁}) ≥ 0.
- Layer-cake: for a history with E(u′)e^{4u′} nondecreasing (class 𝓗₄), r(s) := E(u−s)e^{−4s}/E(u) is nonincreasing. Then ρ̂ = 4E(u)∫dμ_r(t)H(t) ≥ 0.
- **Hence ρ̂ ≥ 0 for every 𝓗₄ history, including any number of transitions of any α and W, and reheating.**
- Checked:
  - min H = 0 for D1, R* and D5; D2 and D3 violate it (min ρ̂/ρ_nc down to −7.1, `r154_reader.out` Part 3);
  - on 30 random 𝓗₄ histories per reader (1–3 components with x ∈ [0, 4]; 1–5 releases of size 0.01–30, any sector, widths 1e-3–0.5 or exact steps; reheating starts), min ρ̂/ρ_nc = +7.7e-5 (D1) and +2.0e-4 (R*). A control with a dominant phantom component (outside 𝓗₄) goes to −0.27 and −0.80, as Lemma N+ predicts (`r154_p2_random.out`).

**Regular g (proved).** dρ̂/du = K(0)E − Σk_jβ_jy_j is bounded by const·E. So g = −(1/3)(dρ̂/du + E) (κ = 1, homogeneous) is finite through steps.
- The peak |g/H²| for an α = 0.5 step is 7.7 (D1) and 64 (R*).
- Prony: about 1e3, with singular points (`r145_homog.out`).
- Between transitions g decays as e^{−(β₁−4)τ}. It is exponentially small, not identically zero; that is the referee's g ≡ 0 caveat (`vR14-5:24`). A compactly supported kernel would make it exactly zero after the memory, at the cost of infinite-dimensional state.

**No feedback instability (proved, homogeneous).** dρ_nc/du = −E is independent of H, so ρ̂(u) is a fixed functional of the content history in u. H only maps u to t.

### 4.2 (a) EW- and QCD-like transitions (checked; `r154_reader.out` Parts 2–3)

**R14-5 runner cases, reader D1** (rv0 = 5; latent heat into radiation):

| Δ (α) | W | min ρ̂/ρ_nc (Prony R14-5) | max\|ε\| | Λ̃/ρ_nc at end of R14-5 span | λ_end vs −ρ_v,final | max\|g/H²\| |
|---|---|---|---|---|---|---|
| 0.01 (0.0095) | 0.15 | **0.9989** (0.716) | 7.7e-3 | 5.5e-7 | −4.990000 = −4.990000 | 0.048 |
| 0.05 (0.048) | 0.3 | **0.9989** (−3.43) | 4.2e-2 | 8.8e-8 | −4.950000 = −4.950000 | 0.16 |
| 0.3 (0.29) | 0.3 | **0.9935** (−482) | 0.19 | 5.2e-7 (1.7e-13 with +5 e-folds) | −4.700000 = −4.700000 | 0.76 |
| 0.7 (0.67) | 0.3 | **0.9858** (−34.3) | 0.31 | 1.2e-6 | −4.300000 = −4.300000 | 1.45 |
| 0.01 | 0.02 | **0.9939** (0.334) | 7.4e-3 | 2.7e-5 | −4.990000 = −4.990000 | 0.12 |
| 0.7 | 0 (exact step) | **0.603** | 0.40 | 2.6e-3 (2.1e-9 with +5 e-folds) | −4.299999 = −4.300000 | 10.6 |

- The control is unchanged: unimodular (g ≡ 0) gives Λ_eff = −Δ, which is Lemma PT.
- The λ column is an identity once ρ̂ = ρ_nc (`vR14-5:39`). The content is the relaxation, which is analytic, Σc_je^{−(β_j−4)τ}, and not floating-point closure.

**R13-3 grid, S1 and S2** (α = 0.01, 0.1, 0.5; W = 0.3, 0.05, 0.005, 0):
- **D1:** min ρ̂/ρ_nc ≥ 0.676 in every row, with peak |ε| ≤ 0.32, and |ε| < 1e-6 after 4.4–6.9 e-folds.
- **R*:** min ρ̂/ρ_nc ≥ 0.744, peak |ε| ≤ 0.82 (over-read), and |ε| < 1e-6 after 0.8–4.9 e-folds.
- Compare R13-3's Prony (`C5_R13-3_report.md:241-247`): S1 α = 0.1, W = 0.005 gave ε = −1.73 / −2.29, and S1 α = 0.5, W = 0.05 gave −58.
- D2 and D3 (flatter G, not positive) go negative: down to −7.1.

**EW and QCD (proved bound, inputs RECALLED).** Worst case under D1, α·|1 − G_τ(4)| at T = 1 MeV:
- EW (α = 5.1e-3): 8e-13.
- QCD (α ≤ 0.5): 8.9e-5.
- Both are below the ΔN_eff-scale |δH²/H²| ≲ 0.04. For R* the relaxation is faster (e^{−16τ}).

**e⁺e⁻ annihilation, inside BBN (checked, `r154_bbn.out`; T_γ/T_ν = 1.40101 against (11/4)^{1/3}).** The content is not a sum of x = 3, 4 exponentials: the comoving γe energy rises by about 20%. Peak equivalent ΔN_eff := ε·ρ_tot/ρ_1ν in T ∈ [1, 0.07] MeV:

| reader | positive (P2) | ε range in BBN window | ΔN_eff equivalent |
|---|---|---|---|
| D1 | yes | [−0.006, +0.058] | [−0.04, **+0.43**] (at 0.07 MeV) |
| D5 (lag-free) | yes | [−0.003, +0.046] | [−0.02, +0.34] |
| two registers β = (10, 12) | yes | [−0.003, +0.033] | [−0.02, +0.24] |
| **R*** β = (20, 24) | yes | [−0.002, +0.021] | [−0.01, **+0.16**] |
| two registers β = (40, 48) | yes | [−0.002, +0.018] | [−0.01, +0.13] |

- At T = 1–0.2 MeV (n/p freeze-out) every positive reader has |ΔN_eff| ≤ 0.04. The excess sits at the deuterium bottleneck.
- **Reading.** R* is within the ~0.3 scale. D1 is in tension at about the 2σ scale. A proper BBN network run is needed (not done).
- The fast lag-free 3-register designs are not positive, and their ±5% results carry cancellation and interpolation error, so they are not used. The β → ∞ limit of a local-exponential reader errs by at most 0.7% (`r154_bbn_diag.out`).

### 4.3 (b) The lumpy universe (proved; checked `r154_lumpy.out`)

**Identities (sympy, all residuals 0; from H-model alone).**
- **A1. Uniform Hamiltonian density.** 𝓔(x) := κT_nn^tot − ½R + ½σ² = θ²/3 − λ(t), which is uniform on each CMC slice.
- **A2.** Λ̃ = θ²/3 − 𝓔_nc, with 𝓔_nc := 𝓔 − κρ_v = κρ_nc − ½R + ½σ². Pointwise, and uniform.
- **A3, the exact lapse coefficient.** Q̃ = 𝓔_nc(t) + σ²(x) + (κ/2)(ρ+3p)_nc(x) = (3κ/2)(ρ+p)_nc − ½R + (3/2)σ². No terms are dropped. This corrects `C5_R14-5_report.md:204-205`; the referee's form is `vR14-5:58-60`.
- **A4.** d𝓔/dt = −(2/3)θS, i.e. **κE_𝓔 := −d𝓔/du = 2S(t) = 2⟨Q̃N⟩**. Homogeneously S = (3κ/2)(ρ+p)_nc and g = −2Ḣ − κ(ρ+p)_nc, which matches `r145_homog.py:7`.

**Consequences:**
- **The reader's input is the clock law's own global number** S(t) (`C5_R14-5_report.md:172-174`). Equivalently, it is the locally measurable 𝓔(x), which A1 guarantees is uniform.
  - So the creation law is H² = (1/3)∫K(s)·2S(u−s)ds. It needs no slice average of ρ_tot.
  - **P-r13b (global reader) is no longer needed.** Lemma A (a per-site reader missing collapsed mass, `C5_R13-3_report.md:177-181`) does not arise: inside a halo the larger ρ is compensated pointwise by R, and 𝓔 is the same.
- **Λ̃ in a lumpy universe is the reader error** on 𝓔_nc = κ⟨ρ_nc⟩ + B, with B := −½⟨R⟩ + ½⟨σ²⟩. It is not ½⟨R⟩ − ½⟨σ²⟩.
- **Lapse positivity, corrected Lemma P (proved, given H-CMC-exist).** N > 0 if 𝓔_nc(t) > 0 and (ρ+3p)_nc ≥ 0 pointwise.
  - With smooth DE w ≥ −1: Q̃ ≥ κρ̄_m − ½⟨R⟩ + (3κ/2)(1+w)ρ_DE ≥ 0 whenever ⟨R⟩ ≤ 2κρ̄_m.
  - This is one global inequality: no recollapse, satisfied with a margin of about 5e5 (⟨R⟩/H₀² = 4e-6 against 6Ω_m = 1.9). It replaces the dropped terms of `vR14-5:62`.
- **Checked on a random T³ field.** ⟨R⟩_vol = 2⟨e^{−Ψ}|∇Ψ|²⟩/⟨e^{−3Ψ}⟩ = 0.71476524 on both sides. ⟨R⟩ > 0 while min R = −267, so R is not ≥ 0 pointwise.

**Magnitudes (linear theory; comparator inputs RECALLED).**
- ⟨R⟩/H₀² = 4.1e-6 and ⟨σ²⟩/H₀² = 2.1e-9 (suggested normalization).
- R14-5's ⟨ρ⟩-reader: Λ̃/Λ_obs = +9.9e-7.
- 𝓔-reader: R̂[B]/B = 1.02 (D1) and 1.11 (R*), so Λ̃/Λ_obs = **−2.3e-8 (D1), −1.1e-7 (R*)**.
- Nonlinear halos are not included. They plausibly add an O(1) factor to ⟨|∇Φ|²⟩ (suggested).

### 4.4 (c) DESI-like evolving w (proved no-go; checked `r154_desi.out`, `r154_nogo.out`, `r154_nnls.out`)

**Lemma N0, a dead band (proved; any reader).** Let a reader satisfy R̂[const] = 0 and be continuous at constant histories in sup-norm of E over a finite memory window [u−Σ, u]. Then R̂[Ae^{−xu}] → 0 as x → 0, while the content stays A e^{−xu}.
- Quantitatively, with |R̂| ≤ L sup|E|: the read fraction is ≤ L|x|e^{|x|Σ}.
- Exact tracking of all w ≠ −1 content is therefore impossible for any regular reader. "Convergent to the w ≠ −1 content" can hold only pointwise, along a sequence of readers whose regularity constants diverge.
- Checked for a nonlinear fit: the DE read fraction falls to 0.60 at 1+w = 0.01 and 0.18 at 0.003 (`r154_nnls.out` (iv)).

**Lemma N+, positivity against tracking (proved; for 𝓡⁺).**
- Positivity on reheating histories ⇔ H(t) = ∫₀ᵗKe^{4s} ≥ 0 for all t. For ⇐ use layer-cake; for ⇒, a reheating at u − t₀ gives ρ̂ = 4Δe^{−4t₀}H(t₀).
- Integration by parts gives F(x) := ∫Ke^{xs} = (4−x)L_H(4−x), where L_H(p) = ∫He^{−ps} is nonincreasing in p because H ≥ 0. Dust exactness gives L_H(1) = 1/3.
- Hence **G(x) ≤ x(4−x)/3 on (0, 3)**, and **G(x) = x(4−x)L_H(4−x) ≤ 0 for x < 0**.
- Consequences:
  - Constant-w DE is read at most at 0.19 (w = −0.95), 0.37 (−0.9) and 0.81 (−0.75).
  - **Every phantom component is read with nonpositive density.**
  - Exact tracking within δ needs w ≥ −1 + (2 − √(1+3δ))/3, i.e. w ≥ −2/3 for δ = 0.
- LP check (40 rates, 1500 positivity points): sup G approaches the bound from below as the coefficient cap grows, and the transition sensitivity T_K diverges (24 → 250). For phantom x, sup G ≤ −1e-4 (`r154_nogo.out`).

**(c1) Tracking the DESI CPL as the true content.** R̂[ρ_DE]/ρ_DE at z = 0 / 1 / 2:

| set | D1 | R* | D3 (not in 𝓡⁺) |
|---|---|---|---|
| DESI+CMB | 0.43 / −0.29 / −0.48 | 1.00 / −0.40 / −0.93 | 4.18 / −0.17 / −3.64 |
| +Pantheon+ | 0.10 / −0.14 / −0.22 | 0.30 / −0.20 / −0.38 | 1.80 / −0.22 / −1.13 |
| +Union3 | 0.23 / −0.21 / −0.33 | 0.59 / −0.29 / −0.60 | 3.04 / −0.19 / −2.03 |
| +DESY5 | 0.17 / −0.18 / −0.28 | 0.45 / −0.25 / −0.49 | 2.47 / −0.21 / −1.57 |

- **Raw Λ̃(z = 0)** in units of 3H₀²/κ, where Λ_obs ≈ 0.69 in these units: −0.39 to −0.62 for D1, −0.003 to −0.48 for R*, +0.55 to +2.2 for D3.
- **After the one unobservable renormalization**, which keeps H₀ and flatness: |δH/H| reaches 34–43% (D1), 24–26% (R*) and 14–15% (D3) at z ≈ 0.5–0.9, against DESI's percent-level BAO (RECALLED).
- **The model's effective w** is far from the input. For R* and DESY5, w_eff(z = 0) = −1.72 against the input −0.75.
- **(c1) fails for every reader built** (checked), and for every reader in 𝓡⁺ because of the phantom past (proved).

**(c2) The inverse problem: which true DE does the reader turn into DESI's curve? (checked).** Solve R̂[E_true] = ρ_CPL. The inverse system is minimum-phase; its residual is ≤ 4e-7 of Ω_DE.

| set | min/max E_true (z < 3), R* | all z: E_true ≥ 0 (never phantom)? | g/H² at z = 0 / 0.5 / 1, R* (c2 picture) |
|---|---|---|---|
| DESI+CMB | +0.49 / +1.89 | **yes** (also D1, D3) | −0.31 / −0.94 / −0.70 |
| +Pantheon+ | +0.79 / +1.49 | **yes** | −1.09 / −0.88 / −0.51 |
| +Union3 | +0.64 / +1.63 | **yes** | −0.77 / −0.91 / −0.58 |
| +DESY5 | +0.71 / +1.55 | **yes** | −0.93 / −0.89 / −0.55 |

- **Reading:**
  - The model reproduces each DESI DR2 background expansion exactly from a true dark energy that is never phantom.
  - The read DE starts at zero and rises (an effective phantom phase), then falls, because a constant-blind reader sees only the decaying part.
  - The true DE has decreased by about 1.7–1.9 ρ_c0 since z = 3 (R*), or 3.1–3.5 (D1). Its constant part is invisible.
- **The cost:**
  - Λ̃ ≠ 0 relative to that true content.
  - g/H² is O(1) today, so the E-fluid's instantaneous pressure response δp_E = −gδN (`C5_R14-5_report.md:296`) acts now.
  - Horizon-scale growth, ISW and lensing corrections O[(g/H² + ġ/H³)(aH/k)²] (`vR14-5:73-77`) are not computed.

**A nonlinear escape attempt (checked, `r154_nnls.out`).** The reader is a nonnegative exponential fit with a free constant and phantom nodes allowed. It is positive by construction but ill-conditioned:
- errors of 2–10% on pure radiation + dust;
- an over-read by up to ×770 after an α = 0.5 step;
- DESI CPL errors of O(1–10).

As built it is not a viable escape. It is not a no-go either.

### 4.5 (d) Residual Λ̃ and tuning

- **The vacuum's part.** Λ̃ = θ²/3 − 𝓔_nc contains no ρ_v (A2). The reader reads only E (or S), which contains no ρ_v. So **the residual from any constant vacuum, through any number of transitions, is exactly zero** (proved). No parameter is set against ρ_v.
- **Reader constants.** β_j and k_j are law constants:
  - k is fixed by exactness at w = 0 and 1/3, which is structural;
  - β is a design choice constrained by BBN (R* over D1). That is a choice, not a fine-tuning (reading). R* sits within an order-one window: β ≳ 10–20 for BBN, with T_K growing in β.
- **Remaining Λ̃, all from content-reading error:**
  - transitions: transient and bounded;
  - e⁺e⁻: ε ≤ 0.021 (R*);
  - lumpy: ≤ 1.1e-7 Λ_obs;
  - DE: O(Λ_obs) when the DE is near −1 or phantom (Lemmas N0, N+).

---

## 5. Kill round on my own construction

- **K1, "this is just fixed-node Prony".** Yes in spirit. Its instantaneous form would be ρ̂ = (7/12)m₁ − (1/12)m₂ (exact at x = 3, 4; derived here). Replacing m₂ by a fading memory integral is what removes the α/W blow-up and the H² < 0 points. **Survives as a construction.**
- **K2, positivity only on 𝓗₄.** Phantom content (x < 0) or stiff content (x > 4) leaves 𝓗₄.
  - In the observed history, phantom DE is subdominant: min ρ̂_tot over z < 3 is ≥ 0.38 ρ_c0 in every (c1) row.
  - Stiff epochs: β > x keeps the registers finite. Positivity there is not proved.
- **K3, BBN.** D1 is in tension (+0.43). **R* survives at +0.16** (equivalent at T = 0.07 MeV; marginal; no network run).
- **K4, lapse positivity and CMC existence.** A3 removes the dropped-term gap. Existence of the CMC foliation through collapse is still assumed (R15-1's item; not addressed).
- **K5, the active g today.** Any DE misreading makes g ≠ 0 at late times (c1: g/H² = −1.7 to −1.95 at z = 0 for R*; c2: −0.3 to −1.1). R14-5 had hoped g ≈ 0 between early transitions; that does not hold once DE is evolving. **Named as a price, P-r15b.**
- **K6, inflation (suggested, not computed).** A slow-roll inflaton has x = 2ε. It is read at G(2ε) ≈ 2ε∫K, so its energy barely drives expansion in this model. Inflation's dynamics would need re-derivation.
- **K7, reheating start.** ρ̂ = 0 right after reheating (H(0) = 0), so creation pauses briefly (c = 0, compatible with c ≥ 0) and then catches up. It never goes negative (P2).

---

## 6. Prices (named, none adopted)

| # | Price | Axiom text touched | What it buys | Status |
|---|---|---|---|---|
| P-r15a (P-r13d built) | **Register reader.** A fixed causal linear filter with two leaky registers per site on S(t), equivalently on the local 𝓔(x), with constants (β, k) | `AX:57` (law constants of the one rule); `AX:116-123` (dynamics content not in the axioms); `AX:94-95` (u-translation invariance, reading) | Regular, real, nonnegative reading through any 𝓗₄ history; exact for radiation and dust | built; proved and checked |
| dropped | P-r13b (global ⟨ρ_tot⟩ reader). 𝓔 is uniform by A1, and S(t) is already P-r14a's global number | — | — | not needed |
| P-T | Temporal vacuum reference (only time variation is read) | `AX:186-187` | Λ̃_vac = 0 exactly | carried |
| P-r14a, P-arrow, P-vac | As in R14-5 (`C5_R14-5_report.md:333-338`) | as recorded | — | carried |
| **P-r15b (new)** | **Slow-content degravitation.** Every positive reader under-reads near-Λ DE (N0, N+) and reads phantom DE with the wrong sign. The observed DE is R̂[true DE], and the E-fluid stays active today (g/H² of order 1) | `AX:186-187` (source/action); `AX:57` (instantaneous response, via P-r14a) | Reproduces DESI's phantom-crossing background from a never-phantom true DE (c2) | new; costs are unquantified at the perturbation level |
| S1, S3, S4, S6 | Unchanged | as recorded | — | carried |

---

## 7. Notes for the referee

1. **Lemma P2 and the layer-cake step:**
   - the H(t) ≥ ¼(1 − y^{p₁}) argument;
   - the representation r(s) = ∫_{(s,∞]}dμ;
   - the class 𝓗₄ (whether E e^{4u} is nondecreasing for every 0 ≤ x_i ≤ 4 mixture with nonnegative releases: d(Ee^{4u})/du = e^{4u}[Σx_i(4−x_i)ρ_i + 4·release] ≥ 0).
2. **Lemma N+:** the equivalence "positive on reheating ⇔ H ≥ 0"; the integration by parts F(x) = (4−x)L_H(4−x) (boundary terms need H bounded and x < 4); the monotonicity of L_H. Also whether "positive on reheating" is really forced in 𝒵. My argument: ρ̂ < 0 gives H² < 0 (`C5_R14-5_report.md:163`), and the hot universe starts from a vacuum decay.
3. **A1–A4:** that E_nn(x) = λ(t) holds pointwise (`C5_R14-5_report.md:97,161`). Then 𝓔 is uniform, so the reader is local and P-r13b is dropped. Also the identity κE_𝓔 = 2S.
4. **The e⁺e⁻ numbers** (instant ν decoupling; the "equivalent ΔN_eff" mapping is a reading, not a BBN network).
5. **The FAIL scope:** N+ covers linear, time-invariant, positive readers only. N0 covers any continuous reader, but only near w = −1. A positive nonlinear reader that tracks a phantom past is not excluded.

**Strong-word check:**
- "Exactly zero" applies to the vacuum's contribution only.
- "Never negative" applies to class 𝓗₄ with P2 readers.
- "Exact" for radiation and dust means constant-x components.
- "Exactly DESI's curve" (c2) is the background only.
- "FAIL" is bounded to 𝓡⁺ for test (c).
- "PASS" for (a) and (b) is within 𝒵, with H-CMC-exist assumed, and with the e⁺e⁻ caveat.

**What would change the picture:**
- a positive nonlinear reader that tracks phantom-crossing histories (escapes N+);
- a BBN network run with R*;
- the late-time perturbations of the g ≠ 0 sector in the (c2) picture (ISW and large-scale growth);
- an inflation calculation under constant-blind reading.

## 8. Files

- Report: `S/R15-4_report.md`.
- Scripts and outputs: `S/scripts/`, namely `r154_reader.py/.out`, `r154_lagfree_scan.py/.out`, `r154_bbn.py/.out`, `r154_bbn_diag.py/.out`, `r154_desi.py/.out`, `r154_nogo.py/.out`, `r154_lumpy.py/.out`, `r154_nnls.py/.out`, `r154_p2_random.py/.out`.
