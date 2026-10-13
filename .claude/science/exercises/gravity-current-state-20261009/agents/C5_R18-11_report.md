# C5 round 18, probe R18-11: set A's E1 + N in Poisson gauge, gauge-invariant noise at O(G²) (worker report)

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-13, 03:09Z to about 03:40Z. No repository file was edited.

**Scratch:** `scratchpad/C5/R18-11/`. Runtimes are each under 25 s with OMP_NUM_THREADS=2. SHA-256 prefixes in brackets.
- `r1811_modes.py` / `.out` [ff9737aa… / 064b384c…]: sections [1]–[4]. Sympy, exact second-order Einstein tensor per frame mode. Covers the Poisson-gauge and harmonic-gauge laws, the channels ρ, T_⊥, V and TT, and the insertion weight a.
- `r1811_insertions.py` / `.out` [7d965961… / 5b419664…]: section [8], which insertions are independent of the readout gauge. It imports `r1811_modes_lib.py` [b8bb0418…], a non-printing copy of the definitions in `r1811_modes.py`.
- `r1811_pin.py` / `.out` [e857e99d… / 524cf202…]: section [9], R18-7's Π acting on the homogeneous mode, and [9b], the linear constraint at k = 0.
- `r1811_budget.py` / `.out` [3e7c204c… / 04ddb388…]: sections [5]–[7b], spectral averages, the budget and Mercury.
- `rerun/`: copies of the archived R18-7, R16-14, R15-2, R16-4 and R13-6 runners, rerun here. **All are byte-identical** with the archived `.out` files, except `r187_ll.out`, whose two differing lines are wall-clock runtimes (`rerun/rerun_summary.txt`).
- No downloads and no web fetches. Literature is labelled RECALLED.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `R18-7:n` = `P/agents/C5_R18-7_report.md:n` (and so on); `vR15-2` = `P/agents/C5_R15-2_referee_verdict.md` (and so on); `vR18-7` = `scratchpad/C5/ref_R18-7/REFEREE_VERDICT.md` (it appeared during this run; CONFIRMED WITH CORRECTIONS); `modes:n`, `ins:n`, `pin:n`, `bud:n` = line n of my `.out` files.

**What I read.** `AX` in full. `TESTS:2302-2320` (C5 method). The set-A entries and verdicts: R6-4 `TESTS:3143-3175, 3409-3418`; R13-6 `TESTS:4682-4692, 4728-4732`; R15-2 `TESTS:4939-4951, 5177-5183`; R16-4 `TESTS:5108-5125, 5286-5297, 5433-5436`; R16-14 `TESTS:5630-5653, 5875-5886, 6000-6006`; R18-6 `TESTS:6684-6711, 6826-6843`; R18-7 `TESTS:6713-6736, 6898-6916`; R18-11 `TESTS:6918-6942`. Also `R18-7` in full, `vR18-7` in full, `R18-6:84-143`, `R15-2` in full, `vR15-2` in full, `C5_R15-2_referee.md` in full, and `vR16-14:11-23`, `vR16-4:11-19`.

**Labels.** **proved** (derived here under stated hypotheses); **checked** (a number or identity in my `.out` files); **suggested** (argued, not proved); **reading** (interpretation); **comparator** (literature, RECALLED or via an earlier referee).

**Order rule.** First order in G·noise for the metric. O(G·noise²) for the mean source. Gaussian order for CP.

**Subtraction rule.** None. Every mean is the phase average of an exact second-order expansion (`modes:1-34`).

---

## Reading against the FIXED readings (`TESTS:6938-6941`)

**Worker reading: OPEN.** NOISE-SAFE is not met. A **NOISE-OVERSHOOT candidate** is proved and checked in the class stated below. Recording it needs a referee.

- **NOISE-SAFE is not met (proved, checked).**
  - Exactly one insertion makes the O(G·noise²) mean source independent of the readout gauge: **a = 2**, the record J^{μν} = √−g T^{μν} (Theorem G, §4).
  - At a = 2 the active density never vanishes. It is
    - **exactly −4u₁** per mode, if the S/V noise is stationary with its energy already present (reading (U)); or
    - **at most −(1 + ⟨x²⟩)u₁ − 2r u₁ − u_V**, if the noise switches on from zero under R18-7's Π (reading (P)), for anticorrelated T_⊥ (q = −r ≤ 0).
  - Here u₁ is R15-2's ρ-channel field energy, u_V the V-channel field energy, r ≥ 0 the T_⊥ noise fraction, and x = ω/ck.
  - Over R15-2's least-decoherence window, u₁/ρ_Λ ≥ 1.171 (`bud:67`). So |ρ_act| > ρ_Λ everywhere, by ×1.17 at the window's corner up to ×1e19.
- **NOISE-OVERSHOOT candidate (worker; a referee is required).** The class 𝒜₂ is:
  - the insertion family J^{μν} = (−g)^{1−a/4}T^{μν} restricted to its readout-gauge-independent member a = 2;
  - Minkowski background, O(G·noise²), static to stationary S/V noise with any temporal spectrum;
  - T_⊥ anticorrelated with ρ, as at R15-2's least-decoherence split (q = −r, r ∈ [0, 1]); V noise u_V ≥ 0. Reading (U) needs none of these: it is exactly −4u₁ for any q, r and u_V. Reading (P) needs q ≤ 0 mode by mode. That holds for x < 1 at least decoherence (`R15-2:125`) and hence in the τ_c variant. In the strict variant the far-off-cone (x > 1) modes have g₁₁ < 0, so q > 0 there, and the (P) bound is not established for them;
  - γ = 1 (no γ-trade); TT budgeted separately;
  - energy readings (U) or (P) in flat space.

  Over the whole window ℓ ∈ [4e-10, 5e-6] m, with τ strict or τ_c up to the ceiling 1.49e-3 m/c, |ρ_act| > ρ_Λ for every member. The class has one member. That is the honest scope: every other a is readout-gauge dependent (§4).
- **Why only a candidate.**
  1. The class is narrow. For a ≠ 2 the active density depends on the readout gauge, on the far-off-cone and IR noise spectrum, and on r. Zeros exist at tuned, non-natural a (§6).
  2. Under the FRW-attractor reading of (P), which is suggested only (FRW is excluded by the item), the noise tends to w = −1 with |ρ_act| = (2/3)(1 + ⟨x²⟩ + 2r + u_V/u₁)u₁. That is below ρ_Λ in a corner ℓ ≳ 4.6e-6 m at the τ_c ceiling if r ≈ u_V ≈ 0 (§7).
  3. The window's top corner has only a 17% margin. It rests on R15-2's u₁ (confirmed, `vR15-2:17`), R14-2's τ_c ceiling (suggested) and R6-4's 5e-6 m endpoint.

| Probe (`TESTS:6933-6937`) | Result | Label |
|---|---|---|
| (a) Poisson-gauge O(G²) construction | E1 + N_c with the record inserted in Poisson coordinates. The per-mode mean source is computed for all channels (`modes:36-56`). Static ρ-only reproduces R18-7 in both gauges (`modes:21-22`). | proved (construction); checked |
| (b) active density vs a; gauge invariance; vanishing a; natural? | Formulas in §6. Gauge-independent iff a = 2 (Theorem G). The a = 4 zero is a static-(U) statement. Zeros elsewhere are tuned and gauge-dependent. | proved; checked |
| (c) budget vs ρ_Λ over R15-2's window | a = 2: \|ρ_act\| ≥ 1.17 ρ_Λ (P) or ≥ 4.68 ρ_Λ (U) at the corner, up to 1e19. Mercury fails for ℓ ≲ 2.5–2.7e-8 m (strict). | checked (`bud:59-74`) |
| (d) CP and well-posedness | CP at Gaussian order: a record-controlled instrument (R18-7 §5, `vR18-7:11`). Elliptic plus wave at each order with Π. The homogeneous mode needs (P), or FRW for (U). | proved by citation and structure; suggested for globality |
| (e) prices | P-r1811a (a = 2), P-r1811b (energy history), P-r15c becomes necessary, Π's homogeneous-pressure freedom | named |

---

## 0. In plain words

- **The question.** R18-7 found that the record noise's static "weight" (its active gravitating density) vanishes if the noise enters with weight a = 4. Does that survive a gauge-proper treatment with time-dependent noise?
- **What "gauge" means here.** In ordinary GR, the choice of coordinates is pure bookkeeping. In set A it is not. The record is a fixed field written on the background frame. To insert it into the curved spacetime you must say at which points it sits, and that is a coordinate choice. Different choices are different laws, and they differ exactly at the order asked about.
- **One insertion is gauge-independent.** If the record is read as the density √−g T^{μν} (a = 2), the choice of coordinates drops out of the averaged source. This follows from the record's own conservation. For R18-7's a = 4, harmonic and Poisson coordinates give different answers as soon as the noise changes in time (checked).
- **The energy books.** E1's noise starts from nothing at t₀. Exact energy conservation, which R18-7's Π enforces, then pins the noise's averaged energy density at zero forever. What remains is its averaged pressure, and that pressure is negative.
- **The result at a = 2.**
  - If the noise is taken as always present, its active density is exactly −4u₁, independent of frequency content, pressure noise and gravitomagnetic noise.
  - If it switches on from zero, it is at least u₁ in size, and negative.
  - Either way it is larger than the dark-energy density everywhere in R15-2's window. So R15-2's overshoot returns as a set A wall at the one gauge-independent insertion, unless the S/V channels are under-recorded (the γ-trade, P-r15c) or something is tuned.
- **A twist (suggested).** The sign is negative, which is Λ-like. In an expanding universe the switched-on noise would settle to an exact cosmological constant of size about u₁/3. At ℓ ≈ 3.7 µm with the longest allowed gain time, that equals the observed ρ_Λ. That is a lead, not a result: FRW is not built here.

---

## 1. Prior art (each counted once)

1. **R18-7 and its referee.**
   - The E1 + N_c law: source (−g)J + Λ, causal conserving Π, readout □h = −16πGτ_rec (`R18-7:128-151`).
   - Static (2a − 7)|u₁| energy and (2a − 8)|u₁| active density (`R18-7:219-226`; `TESTS:6912`).
   - Caveat: harmonic gauge conflicts with P-r15b; no gauge-invariant time-dependent result (`R18-7:40-44`; `TESTS:6913`).
   - The referee confirms the (2a − 8) result only for the "homogeneous static scalar channel". It does not settle T_⊥, V, TT, time dependence or FRW. Π is nonlocal (`vR18-7:3, 20, 26`).
2. **R15-2 and its referee.**
   - Lemma A: only TT has the cone pole (`vR15-2:5`).
   - P-r15b: the record is held in Poisson gauge (`R15-2:133-135`).
   - Anticorrelated T_⊥ at least decoherence, P_ρ⊥ = −P_⊥⊥g₁₂/g₁₁ (`R15-2:125`); K_⊥⊥ diverges near the cone; bounded interpolation is a reading (`R15-2:126-127`).
   - |u₁| = ħI_F/(32π^{3/2}ℓ³τ) with I_F = 21/32, confirmed; premise (iii) open (`vR15-2:17`).
   - γ-trade window (`R15-2:245`, suggested).
3. **R18-6** (set A part, worker): N's source carries the record noise, which (S) cannot subtract. Noise injection needs a conserved partner, P-r186c (`R18-6:112-116, 139-140, 177`).
4. **R16-14 and its verdict**: Mercury's active-density bound |ρ_act| < 9.29e-15 kg/m³ (`vR16-14:11`); N does not establish premise (iii) (`vR16-14:15`).
5. **R16-4 and its verdict**: free-data memory; P88; the AX:94 question (`vR16-4:17-19`).
6. **R13-6**: the repaired gain P-r13b; the finite start (`TESTS:4728-4732`).
7. **R6-4**: the ℓ window 4e-10 to 5e-6 m (`TESTS:3410`).
8. **Comparators (RECALLED).**
   - Second-order Poisson-gauge perturbation theory (Matarrese–Mollerach–Bruni 1998).
   - The Isaacson / Green–Wald averaging logic (Green–Wald needs the weak energy condition, which the zero-mean record noise violates).
   - The Tolman–Komar identity √−g R⁰₀ = −∂_i(√γγ^{ij}∂_jN) for static metrics.
   - Lie derivatives of tensor densities.
   - Buchert-type averaging.
9. **Repository grep** of `P/agents/` and `P/TESTS.md` for "tensor density", "√−g T", "pinned", "homogeneous mode", "weight-1": no derivation of readout-gauge dependence or of homogeneous-energy pinning. `docs/` was not grepped.

## 2. Hypotheses: class 𝒫₁₁ (stated before any title)

- **H1.** E1 as R13-6/R15-2/R18-7:
  - Minkowski background with the CMB frame;
  - repaired gain F = e^{−k²ℓ²/2}(1 − 4iωτ)(1 − iωτ)^{−4};
  - channel meters at the least-decoherence split;
  - finite start with B (P76); zero free data (P88, extended);
  - the record J (matter plus noise) flat-conserved.
- **H2.** The law is G_μν[g] = 8πG T^eff_μν in coordinates satisfying the readout gauge C (Poisson, P-r15b; harmonic for comparison). T^eff is the inserted record plus Π's completion K.
- **H3.** Insertion families:
  - C_w: J^{μν} = (−g)^{w/2}T^{μν}, with a = 4 − 2w (R18-7's a);
  - M_w: J^μ_ν = (−g)^{w/2}T^μ_ν;
  - L_w: J_μν = (−g)^{w/2}T_μν.
- **H4.** The noise is homogeneous and stationary in the frame and Gaussian. Per frame mode p = (ω, 0, 0, k), the channels are ρ, T_⊥ (S), j (V) and t₊ (TT), with relative statistics q = ⟨ρT_⊥⟩/⟨ρ²⟩ = −r and r = ⟨T_⊥²⟩/⟨ρ²⟩ (`R15-2:125`, static relation).
- **H5.** Active density = the source of the long-wave tidal field: ρ_act = τ_00 + τ_kk, where τ_μν = ⟨T^(2)_μν⟩ − ⟨G^(2)_μν[h₁,h₁]⟩/8πG is the coarse-grained second-order source. This equals R₀₀ of the long-wave metric over 4πG.
- **Excluded:** E2; strong field; FRW (used only in a labelled suggestion); TT beyond its off-shell per-mode coefficients (its on-shell Isaacson part is R15-2's TT budget); non-Gaussian noise.

---

## 3. Probe (a): the construction in Poisson gauge

**Linear order (checked, `modes:1-8`).** In Poisson gauge, ds² = −(1+2Φ)dt² + 2S_x dx dt + [(1−2Ψ)δ + h^TT]dx². For one mode:
- Ψ = −4πρ/k² and Φ = −4π[(1 − 2x²)ρ + T_⊥]/k² (instantaneous);
- S_x = −16πj/k² (instantaneous);
- h₊ = 16πt₊/(k² − ω²) (the only cone pole).

All 14 nontrivial linear equations hold, and the harmonic solution h̄ = 16πJ/(k² − ω²) satisfies G⁽¹⁾ = 8πJ in all 16 components. The two are the same physical O(G) field, as Lemma A requires (`vR15-2:5`).

**Second order.**
- G⁽¹⁾[h₂] = 8πG(T⁽²⁾ + K) − G⁽²⁾[h₁, h₁]. In Poisson gauge the S/V parts of h₂ are elliptic and the TT part is a wave equation.
- Solvability needs ∂^μ(source)_μν = 0 (linearized Bianchi). R18-7's Π supplies it. Π acts on the source, so it does not depend on the gauge formulation (proved).
- The coarse-grained mean τ_μν (H5) per mode is in `modes:10-18` (full forms) and `modes:36-56` (coefficients). Mean momentum ⟨τ_0i⟩ cancels between ±ω and over directions (proved, from an even spectrum and isotropy).

**Validation (checked, `modes:21-22`).** Static, ρ-only: τ_00/u₁ = 2a − 7, τ_kk/u₁ = −1, sum 2a − 8, in **both** the Poisson and harmonic laws. This reproduces R18-7 exactly. Here u₁ is the per-mode ⟨|∇Ψ|²⟩/8πG = πρ²/k².

## 4. Probe (b), first part: is it gauge-invariant? Theorem G

- **For a fixed law, the active density is an observable (proved, sketch).** The long-wave source is unchanged by short-wave coordinate changes whose mean effect is constant or linear in t. G⁽¹⁾ of a homogeneous tensor that is constant or linear in t has zero 00 component and zero spatial trace. This is the Isaacson argument.
- **But the law itself depends on the readout gauge.** Moving from harmonic to Poisson coordinates by ξ (linear in the noise) re-inserts the record at shifted points. The two laws' sources differ by −L_ξ𝔍 for the density 𝔍 that the insertion defines.
- **Theorem G (proved).** For a contravariant density of weight w, homogeneity and the record's flat conservation ∂_λ𝔍^{λν} = 0 give

  ⟨L_ξ𝔍^{μν}⟩ = −⟨(∂·ξ)𝔍^{μν}⟩ + ⟨ξ^μ∂_λ𝔍^{λν}⟩ + ⟨ξ^ν∂_λ𝔍^{μλ}⟩ + w⟨(∂·ξ)𝔍^{μν}⟩ = (w − 1)⟨(∂·ξ)𝔍^{μν}⟩.

  So the mean source is independent of the readout gauge for every ξ iff w = 1, that is **a = 2: the record is √−g T^{μν}**.
- **Checked (`modes:33-34`; `ins:1-6`).**
  - C family, Poisson minus harmonic, ρ channel: Δτ_00 = 2x²(a − 2)u₁ and Δτ_kk = 2x⁴(a − 2)u₁; they vanish only at a = 2 (w = 1).
  - The mixed (M_w) and covariant (L_w) families have Δ ≠ 0 for every w, with cone poles 1/(k² − ω²) and V-channel terms (`ins:7-18`).
  - So within the three power families, **a = 2 is the unique gauge-independent insertion**.
- **Consequence for R18-7's a = 4.** Its static zero is gauge-independent only because harmonic and Poisson coincide at O(G) for static fields. For time-dependent noise, a = 4 gives different active densities in the two laws: Δ = 2x²·2 + 2x⁴·2 per u₁. So the a = 4 statement is a harmonic-gauge statement, as the item expected (`TESTS:6942`).
- **IR robustness.** Only a = 2 has no x⁴ term in τ_kk; the coefficient there is 2(a − 2) (`modes:47`). Under R15-2's quasi-static weight, ⟨x⁴⟩ diverges in the IR (∝ 1/u_min, `bud:2-3`) from far-off-cone (ω ≫ ck) long-wavelength noise. So for a ≠ 2 the active density depends on the unspecified far-off-cone spectrum. At a = 2 it does not (proved from the coefficients; checked).

## 5. The energy books: Lemma P (homogeneous energy is pinned)

- **Lemma P (proved; checked `pin:1-3`).** On a Minkowski background, any O(G²) law that closes satisfies the linearized Bianchi identity. Its coarse-grained source τ is therefore flat-conserved. For the homogeneous, isotropic mean, ∂_t⟨τ_00⟩ = −∂_i⟨τ_0i⟩ = 0. So the noise's mean energy density keeps its t₀ value.
  - E1's noise starts at zero (f(0) = f′(0) = 0, J_n(t₀) = 0; `R15-2:146`). With zero homogeneous data (P88 extended), **⟨τ_00⟩ = 0 at all times**.
  - This holds for any causal conserving completion that vanishes before t₀.
  - R18-7's explicit Π does it by K⁰⁰ = −[S⁰⁰(t) − S⁰⁰(t₀)], with K^{ij} = 0 on the k = 0 mode (`pin:2`).
  - The linear Hamiltonian constraint has no k = 0 content: G⁽¹⁾₀₀ = 0 for any homogeneous h(t) (checked `pin:8`). So a nonzero homogeneous ⟨τ_00⟩ cannot be posed on Minkowski at this order anyway.
- **Two readings follow:**
  - **(P) (default; zero data):** ρ_act = τ_kk, the trace of the mean spatial stress of noise plus field.
  - **(U) (stationary S/V noise already present):** ρ_act = τ_00 + τ_kk. This is R18-7's static setting. It needs an extra homogeneous energy datum at t₀ of size ~u₁, plus an FRW or local posing (price P-r1811b).
- **Π's freedom (reading).** A constant homogeneous pressure is conserved. So a completion could add any homogeneous K^{ij}(t) and shift ρ_act. R18-7's Π adds none. Choosing one to cancel ρ_act is a tuning of size u₁ to relative precision ρ_Λ/u₁ (1e-19 to 0.85).

## 6. Probe (b), second part: the active density as a function of a

**Per mode, Poisson law, C family, in units of the per-mode u₁ (checked `modes:37-51`):**

| channel | τ_00 | τ_kk |
|---|---|---|
| ρ | 2a(1+x²) − 7 − 3x² | (1+x²)(2(a−2)x² − 1) |
| T_⊥ (q, r) | −a q | [(a−2)(x²+2) + 2] q − (a−2) r |
| V | +u_V | −u_V |
| TT (off-shell) | 4π(1+x²)t₊²/(k²(1−x²)²) | −4π(x²−3)t₊²/(k²(1−x²)²) |

**(U) ρ_act = τ_00 + τ_kk (proved from the table):**
- ρ channel: 2a(1+x²)² − 4(2 + 2x² + x⁴).
- T_⊥ channel: (a−2)[(1+x²)q − r], which is −r(a−2)(2 + x²) with q = −r.
- V channel: **0**.
- **At a = 2 the total is exactly −4u₁** for every x, every (q, r) and every u_V (checked `bud:18-44`, all weights).
- Zeros: per mode a*(x) = 2 + 2/(1+x²)². Statically a = 4 (R18-7). With T_⊥, statically a = (4 − 2r)/(1 − r): 4, 4.67 and 6 at r = 0, ¼ and ½ (`bud:56`).
- Spectrum-averaged a*: 2.51 strict (cone-regulated weight); 3.80–3.86 at cτ/ℓ = 10; 3.9999 at the ceiling (`bud:47-55`).
- The time-dependent residual of a = 4 is (8⟨x²⟩ + 4⟨x⁴⟩)u₁: 1.5–1.9e-4 u₁ at the ceiling, 33–55 u₁ strict (`bud:48-55`).

**(P) ρ_act = τ_kk:**
- Quasi-static: ρ_act/u₁ = −1 − r(3a − 4) − u_V/u₁ + O(x²) (proved).
- **At a = 2:** −(1 + ⟨x²⟩)u₁ + 2⟨q⟩u₁ − u_V. With q = −r ≤ 0 that is −2.62u₁ − … strict and −1.00u₁ − … at the ceiling, with R15-2's weight (`bud:18-44`). If the far-off-cone modes carry q > 0 (least decoherence at x > 1), the strict-variant (P) value is not bounded by −u₁. The τ_c variant (⟨x²⟩ ≈ 2e-5, `bud:10-13`) is unaffected.
- Zeros exist only for:
  - a < 4/3 with a tuned r = (1 + u_V/u₁)/(4 − 3a) (static); or
  - a > 2 through the IR-sensitive x⁴ term, at spectrum-dependent a* (2.44–2.46 strict, 9.5–13 at cτ/ℓ = 10, about 2.4e4 at the ceiling, cone-regulated weight; `bud:48-55`).

**Which a vanishes, and is it natural? (reading on proved formulas).**
- The only a fixed by a principle (readout-gauge independence, Theorem G) is a = 2, and it never vanishes.
- Every zero needs at least one of: a ≠ 2, which makes the law gauge-dependent; a tuned T_⊥ fraction r; or a spectrum-specific a* that varies with ℓ across the window.
- The cancellation must hold to ρ_Λ/u₁, which is 1e-19 to 0.85 across the window.
- **No natural a works.**
- Is ⟨T_eff⁰⁰ + 3p⟩ gauge-invariant? As an observable for a fixed law, yes. As a property of "the noise" independent of the law's readout gauge, only at a = 2.

## 7. Probe (c): the budget

All values at γ = 1. Here u₁/ρ_Λ is as confirmed in `vR15-2:17`, recomputed in `bud:59-67`.

| ℓ [m] | u₁/ρ_Λ, strict | u₁/ρ_Λ, τ_c ceiling | a = 2 (U) \|ρ_act\|/ρ_Λ (ceiling) | a = 2 (P) ≥ (ceiling) |
|---|---|---|---|---|
| 4e-10 | 8.5e18 | 2.3e12 | 9.1e12 | 2.3e12 |
| 1e-8 | 2.2e13 | 1.5e8 | 5.9e8 | 1.5e8 |
| 1e-6 | 2.2e5 | 146 | 586 | 146 |
| 5e-6 | 349 | 1.171 | 4.68 | 1.171 |

- **R15-2's overshoot returns at a = 2 (checked).** The ×1e12 at 4e-10 m (τ_c) and ×1e19 (strict) are back as active density, not only as energy. The worst-case margin is ×1.17 at the window's top corner in (P), ×4.68 in (U).
- **Mercury (checked `bud:72-74`).** At a = 2 the local active density violates |ρ_act| < 9.29e-15 kg/m³ for ℓ < 2.5e-8 m (P) or 2.7e-8 m (U) in the strict variant, and for ℓ < 4.5–7.2e-10 m at the ceiling. This is a local, cosmology-free exclusion of the lower window at a = 2.
- **Escape by price.** The γ-trade (P-r15c) needs γ_{S,V} ≤ ρ_Λ/(4u₁): 1.1e-13 at 4e-10 m and 0.21 at 5e-6 m, ceiling (U) (`bud:70`). Whether R6-4's lab bounds allow that is R15-2's suggested window (ℓ ≳ 5e-8 m, τ_c).
- **The sign is negative** (a repulsive, Λ-like source), in both readings at a = 2.
- **Suggested, FRW (excluded by the item; not built).**
  - If K obeys covariant conservation with zero pressure at k = 0, then ρ̇_K + 3Hρ_K = −3H(ρ_s + p_s). The total tends to ρ = −p_s, p = p_s: exactly w = −1, with the (a⁻³)-decaying remainder gone by today.
  - At a = 2, ρ_noise → (1 + ⟨x²⟩ + 2r + u_V/u₁)u₁/3 > 0, a positive cosmological constant set by (ℓ, τ).
  - It equals ρ_Λ at ℓ = 3.65e-6 m at the ceiling (ρ-only). The strict variant would need 1.6e-5 m, outside the window (`bud:68-69`).
  - Under this reading |ρ_act| = 2ρ_noise is below ρ_Λ only for ℓ ≳ 4.6e-6 m at the ceiling, and only if r and u_V are small.
  - This is a lead for set A (the record noise as the dark energy), not a result.
- **TT (suggested).** Under (P), the secular TT energy is also pinned: K absorbs it, leaving active ρ_GW. At the ceiling ρ_GW ≲ ρ_Λ/12 (from R15-2's window factor, `R15-2:222`). It cannot offset the S/V term.

## 8. Probe (d): CP and well-posedness

- **CP (proved by citation).** At a = 2 the meter measures √−g[h]T^{μν}, where h is a function of past records. That is an adaptive Gaussian instrument whose strength is controlled by records, followed by record-controlled feedback. The Kraus form U_rA_r is CP for any classical record dependence (`vR18-7:11`; R18-7 toy [7], rerun identical). This holds for finite rational networks; the exact irrational limit stays conditional, as in `vR15-2:15`.
- **Well-posedness (proved, structure).** At each order:
  - Φ, Ψ, S solve elliptic equations with a source known at the same time, and h^TT solves a retarded wave equation;
  - Π (causal, retarded) makes the source conserved, so the constraints are consistent;
  - the free data are P76 plus P88 extended, now to the TT modes only, since Poisson gauge has no residual gauge waves. That is a simplification relative to R18-7's harmonic extension.
- **Caveats.**
  - Under (P) the homogeneous mode is perturbative on Minkowski. Under (U) it is not (§5).
  - The homogeneous pressure drives h₂ ~ 8πG p_s t². Over t_H that is O(u₁/ρ_crit) ≫ 1 in most of the window, so a global treatment needs FRW (suggested). The local Mercury statement is unaffected.
  - Elliptic, instantaneous potentials inserted into the law could in principle allow Lemma-S-type signalling for a ≠ 2, since the insertion is then physical rather than gauge. At a = 2 the mean is gauge-free. Fluctuation-level no-signalling is not computed (open).

## 9. Probe (e): prices (named, not adopted)

- **P-r1811a (insertion a = 2).** One sentence: "The record is the conserved tensor density √−g T^{μν}." It replaces P-r18-7c's a = 4 and makes P-r18-7b (the readout gauge) irrelevant at O(G·noise²) for the mean. *Axiom text:* `AX:82-83` (readout), `AX:187` (source/observable gate).
- **P-r1811b (energy history of the S/V noise).** (P), zero homogeneous energy at t₀, is the default under P88. (U) needs a pre-loaded homogeneous energy datum, which raises the AX:94 privileged-state question (`vR16-4:17`). *Axiom text:* `AX:92-95`, `AX:185`.
- **P-r15c (γ-trade) becomes necessary**, not optional, for the budget at a = 2: γ_{S,V} ≤ ρ_Λ/(4u₁) in (U), or ≤ ρ_Λ/((1 + ⟨x²⟩ + 2r)u₁ + u_V) in (P).
- **The alternative to the price is a tuning:**
  - a ≠ 2 with a tuned (a, r) or a spectrum-tuned a* (each is gauge-dependent); or
  - a homogeneous pressure added to Π.

  Any of these must cancel to precision ρ_Λ/u₁.
- **Carried:** P65, P76, P88, P107, P-r15b (now immaterial at a = 2), P-r18-7a (Π), P-r186c.

## 10. Corrections and refinements to earlier records (worker)

- **R18-7 / `TESTS:6912`.** "(2a − 8)|u₁|, which vanishes only at a = 4" holds in reading (U), static, ρ-only. It fails in each of these four cases:
  1. **Time dependence:** a*(x) = 2 + 2/(1+x²)² (`bud:47-55`).
  2. **T_⊥ noise:** a* = (4 − 2r)/(1 − r).
  3. **Readout gauge:** a = 4 differs between harmonic and Poisson by 2x²(a − 2) (`modes:33`).
  4. **E1's zero-energy start (P):** ρ_act = −u₁ − r(3a − 4)u₁ − u_V + O(x²) for every a.

  This sharpens `vR18-7:20`.
- **R18-7 §7 ("premise (iii) quantitatively no").** At the gauge-independent insertion it is quantitatively **yes**: |ρ_act| ≥ u₁.
- **R18-6 set A (`R18-6:112-116`).** Confirmed and made quantitative: the noise's active density at a = 2 is −4u₁ (U) or ≤ −u₁ (P). (S) cannot remove it, because it is not p = −ρ in flat space.
- **R15-2 (`R15-2:242`, sign "suggested").**
  - The S channel's static mean energy density, insertion included, is (2a − 7)u₁: negative for a < 3.5 (−3u₁ at a = 2), +u₁ at a = 4 (`modes:21`).
  - The V channel's energy is +u_V (`modes:40`). It has ρ + 3p = 0 in (U), with p = −ρ/3.

## 11. Strong words checked

- **"Unique gauge-independent insertion."** Within the C, M and L power families with real density weight, for the coarse-grained mean at O(G·noise²), comparing Poisson and harmonic readouts. The identity in Theorem G covers any pair of readout gauges for the C family. Insertions that are nonlinear in h, or that use derivatives, are not covered.
- **"Exactly −4u₁."** Per mode, reading (U), a = 2, any ω/k, any in-phase T_⊥ and V content; TT excluded. Here u₁ is the ρ-channel field energy of that mode. It is exact at O(G·noise²).
- **"Pinned."** Minkowski background, homogeneous isotropic mean, any causal conserving completion vanishing before t₀, noise zero at t₀.
- **"Exceeds ρ_Λ over the whole window."** At a = 2, γ = 1, R15-2's window with the 1.49e-3 m ceiling. In (U), unconditionally (×4.68 minimum). In (P), for q ≤ 0, which covers the τ_c variant; the strict variant's far-off-cone modes are an exception. The margin is ×1.17 at one corner in (P), using R15-2's quasi-static weight; the exact ρρ floor only increases u₁ (`bud:4, 12`). It does not hold under the suggested FRW-attractor reading near the corner.
- **"No natural a."** Natural means fixed by a stated principle. Tuned zeros exist.
- **IR statements.** Under R15-2's weight extended to ω ≫ ck. The far-off-cone spectrum is a reading (`R15-2:126-127`).

## 12. What would decide it

1. **A referee of Theorem G and Lemma P**, and of the class 𝒜₂ NOISE-OVERSHOOT candidate.
2. **The owner's choice of insertion.** Is a = 2 (gauge-independent) the intended reading of P107? If a = 4 is kept, P-r18-7b/P-r15b become physical law data that change the time-dependent active density.
3. **An FRW version of Π.** Does the switched-on noise become an exact w = −1 component of size −p_s? If so, the "overshoot" turns into a prediction, ρ_Λ ≈ (1 + …)u₁/3, which fixes ℓ³τ.
4. **The S-block least-decoherence optimum** (r(ω, k)) and the V-channel energy u_V/u₁, to turn the (P) bound into a number.

**Sources (RECALLED):**
- Matarrese, Mollerach & Bruni 1998 (second-order Poisson gauge);
- Isaacson 1968; Green & Wald 2011 (averaged backreaction, under the weak energy condition);
- Tolman/Komar mass for static metrics;
- Lie derivatives of tensor densities;
- Buchert 2000/2001 (averaged expansion).

Via earlier referees: |u₁| and I_F (`vR15-2:17`); the Mercury bound (`vR16-14:11`); CP of record-controlled instruments (`vR18-7:11`).
