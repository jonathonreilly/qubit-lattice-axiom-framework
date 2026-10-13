# C5 round 19, probe R19-2: set A's a = 2 record noise in FRW (worker report)

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-13, 03:50Z to about 04:35Z. No repository file was edited.

**Conditionality.** At launch, R18-11's referee was still running. During the run, its verdict appeared at `scratchpad/C5/ref_R18-11/REFEREE_VERDICT.md` (call it vR18-11). It reads **CONFIRMED WITH CORRECTIONS**:
- Theorem G is confirmed for the coarse-grained mean in the C_w density family (`vR18-11:3`).
- Lemma P is confirmed, and homogeneous pressure is called a completion datum (`vR18-11:5`).
- The precondition of R19-2 (`TESTS:7186`) is therefore met. The verdict was not yet recorded in TESTS.md when I read it, so everything below stays conditional on that recording.

**Scratch:** `scratchpad/C5/R19-2/`. Each runtime is under 13 s with OMP_NUM_THREADS=2. SHA-256 prefixes are in brackets.
- `r192_modes.py` / `.out` [9cb8850738b7 / 874526110eee], section [A]. An independent sympy computation of the per-mode O(G·noise²) mean source over all six channel variables. It uses the exact second-order inverse metric, avoiding the runner slip noted in `vR18-11` item 6 of the long form.
- `r192_split.py` / `.out` [3df4b0faac7a / 7bb36f489144], section [B]. The least-decoherence split for every channel, and the identity.
- `r192_frw.py` / `.out` [c5211eb2eb15 / dbe2cf5bbd55], section [C]. The FRW homogeneous mode under lifts A and B.
- `r192_budget.py` / `.out` [4d2754403a76 / 7d673efb55fd], section [D]. Budgets, matches, Mercury and precision.
- No downloads and no web fetches. Literature and cosmological parameters are labelled RECALLED.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `rR18-11:n` = `P/agents/C5_R18-11_report.md:n` (and so on); `vR15-2` = `P/agents/C5_R15-2_referee_verdict.md`; `vR18-11` = `scratchpad/C5/ref_R18-11/REFEREE_VERDICT.md`.
- `A:n`, `B:n`, `C:n`, `D:n` = line n of `r192_modes.out`, `r192_split.out`, `r192_frw.out`, `r192_budget.out`.

**Read.**
- AX in full.
- TESTS:2302-2320 (the C5 method); the round 17-19 rules (`TESTS:5688-5706, 6395-6406, 7117-7136`); R19-2 (`TESTS:7186-7216`); the R18-7, R18-11 and R18-6 entries (`TESTS:6682-6760, 6918-6956, 7020-7044`).
- The S26 synthesis's set-A lines (`S26:91-92, 175-187, 342-357, 514-517`).
- R18-11 in full, vR18-11 (both files), R18-7 §§3-7 and vR18-7, R15-2 in full, `r152_checks.py`, the R18-11 runners, and R13-6:300-331.

**Labels.** proved / checked / suggested / reading / comparator. **Order.** O(G·noise²) mean source, Gaussian noise, first iteration on a fixed FRW background. **Subtraction.** None. Every mean is a phase average of an exact second-order expansion.

---

## Reading against the FIXED readings (`TESTS:7207-7211`)

**Worker reading: OPEN.** NOISE-OVERSHOOT-FRW is refuted for the registered channel set (a checked counterexample). NOISE-IS-Λ is not met in the registered construction. Two candidates are offered for the referee:
- a **NEITHER** candidate (τ_c variant, all four channels);
- a **NOISE-IS-Λ candidate in a new completion** (outside the registered window).

1. **The attractor (probe a): proved under one stated FRW lift, refuted as lift-independent.**
   - Lift A: the homogeneous mode of K is pressureless in the cosmic frame, which is the k = 0 content of R18-7's Π. Here the noise sector obeys ρ_n(t) = −a⁻³∫_{t₀}^{t} p_tot d(a³) exactly. With stationary noise, ρ_n → −p_s, w → −1, and the remainder is p_s(a_on/a)³ (checked to 1e-9, `C:7-13`).
   - The covariant lift B, K = ∇^μV^ν + ∇^νV^μ (the curved-space form of R18-7's own formula), gives p_K = 2HV ≠ 0 (`C:1-5`).
     - Today ρ_n = −4.96 U_IR with w = −1.23 (`C:17`), not w = −1.
     - In de Sitter it has a growing mode e^{0.79Ht} (`C:20`).
   - So **the FRW homogeneous pressure of Π is load-bearing law data** (price P-r192a). It extends vR18-11's "homogeneous pressure remains a completion datum" (`vR18-11:5`).
2. **R18-11's u₁-sized FRW Λ omitted a same-order channel (checked).**
   - At its least-decoherence floor, the quasi-static TT noise carries field stress of size u₀ per polarization. That is the same universal ħ|F|²/4 per mode as every instantaneous channel.
   - It has the opposite pressure sign (`B:16`). R18-11 excluded TT (`rR18-11:114`), and so did its referee (`vR18-11:6-13`).
   - With all four registered channels (`TESTS:7194`) at the **complete** least-decoherence split (K_ρρ at its floor and K_⊥⊥ minimal), **the a = 2 mean source vanishes identically on every spacelike mode**: τ₀₀ = τ_kk = 0 for all x = ω/ck < 1 (`B:11`). It vanishes only at a = 2 (`B:10,12`).
   - On timelike modes it is (τ₀₀, τ_kk) = (4, −4)u per mode (`B:26`).
   - In reading (U), ρ_act = 0 on every mode.
3. **NOISE-OVERSHOOT-FRW is refuted (checked counterexample).**
   - Setting: lift A, complete split, the τ_c ceiling, every ℓ in the window.
   - The bulk vanishes. The timelike modes give ρ_n = 5.9e-8 ρ_Λ (`D:8-11`).
   - The near-cone TT radiation under R15-2's bounded reading gives −1.2e-5 ρ_Λ at the corner (`D:17`).
   - So |ρ_act| = 2|ρ_n| ≪ ρ_Λ there.
   - The overshoot survives in two places:
     - R18-11's TT-omitted channel set, where ρ_n = u₀/(1 − r) ≥ 1.17 ρ_Λ (`D:34-35`). The setting does not allow that set.
     - The literal free-r family with r away from ½, where |ρ_n| = |2r − 1|/(1 − r)·u₀ (`B:19`). For example r → 0 gives −u₀.
   - It fails at r* and at R15-2's printed p₂ = Δ. So it is not a property of the registered class.
4. **NOISE-IS-Λ is not met in the registered construction.**
   - At the principled split (complete), in R15-2's τ_c window, cτ ∈ [lower(ℓ), 1.49e-3] m (`rR15-2:218-224`):
     - with the floor kept up to the cone, ρ_n = (4/3)U_IR ≤ 1.3e-3 ρ_Λ (`D:18`);
     - under R15-2's bounded near-cone reading, ρ_n ≈ −ρ_GW/3 < 0 (`D:17-20`).
   - Neither matches.
   - A match inside the window needs one of:
     - a chosen S-block pressure fraction r ≠ r*. At the corner r = 0.6496, set to 0.3% for a 2% ρ_Λ; elsewhere r − ½ ≈ ρ_Λ/(4u₀), down to 4e-13 (`D:36-41`);
     - the γ-trade, e.g. γ_TT = 0.573 at the corner (`D:43-45`).
   - That is the **NEITHER candidate**. It covers the τ_c variant only. In the strict variant (cτ = ℓ) the near-cone band carries O(1) of the spectrum, and its split is a reading (`vR18-11:6-13`; `rR15-2:126-127`). So NEITHER is not established over the whole window. Hence OPEN.
5. **NOISE-IS-Λ candidate in a new completion (P-r192c: the floor kept up to the cone, with the TT-matched regulator).**
   - ρ_n = (4/3)·11ħc/(96π³(cτ)⁴) with w = −1. This does not depend on ℓ for ℓ ≪ cτ.
   - It equals ρ_Λ at **cτ = 2.32e-5 m** (`D:7-11`). That fixes cτ to ¼ of ρ_Λ's relative error (`D:52`).
   - This cτ lies below R15-2's registered τ_c window, whose lower end is ≥ 1.21e-4 m (`D:12`). It is above the strict variant (cτ = ℓ ≤ 5e-6 m).
   - Mercury is passed with margin 7.8e11 (`D:47`).
   - The completion carries a log-divergent near-cone ρ-noise variance and K_⊥⊥, regulated like TT's ln(ckt). It is a new completion, so it is priced, not adopted.

| Probe (`TESTS:7201-7206`) | Result | Label |
|---|---|---|
| (a) FRW Π, homogeneous mode, attractor, remainder | ρ_n = −a⁻³∫p_tot d(a³) for any conserving lift. Lift A gives R18-11's equation (if ρ̇_s = 0) and w → −1, with remainder p_s(a_on/a)³ (negative dust). Lift B gives no w = −1 attractor. | proved; checked `C:1-23` |
| (b) late-time ρ_noise in all channels vs (ℓ, τ) | Bulk: (2r − 1)/(1 − r)·u₀ (x → 0); 0 at r*; 2⟨x²⟩u₀ at R15-2's printed p₂ = Δ. Timelike: +(4/3)U_IR. Near cone: reading (0 at the floor; ≈ −ρ_GW/3 if bounded). u_V = 2u₀ at the floor. | checked `B:8-33`, `D:4-41` |
| (c) where ρ_noise = ρ_Λ; window; R6-4; Mercury | See §4. Under the registered split there is no in-window match without a chosen r or the γ-trade. The new completion gives cτ = 2.32e-5 m, below the registered τ_c window. Mercury passes at any match. | checked `D:7-52` |
| (d) prediction or tuning | The corner fit of r needs 0.3%. Elsewhere r is tuned to ρ_Λ/u₀ (to 4e-13). The new completion is a one-parameter fit of cτ (¼ of ρ_Λ's error), with ℓ unfixed. No prediction. | checked |
| (e) prices | P-r192a (FRW lift of Π), P-r192b (the complete split), P-r192c (near-cone split); P145, P146 and P-r15c carried | named |

---

## 0. In plain words

- **The question.** R18-11 found that at the one gauge-independent insertion (a = 2) the record noise has negative pressure. It suggested that in an expanding universe this settles into a positive cosmological constant of size about u₁/3, which could be the dark energy.
- **What the expanding universe does (proved).** Total energy is conserved, so negative pressure pumps energy in as space grows: ρ̇ = −3H(ρ + p).
  - If the bookkeeping term Π adds energy only, the noise ends with density exactly −p: a cosmological constant.
  - Π's curved-space form is not unique. Its most direct covariant version adds pressure of its own, and then the end state differs and is not constant.
  - So "how Π behaves in an expanding universe" is a rule that must be chosen.
- **The surprise.** R18-11 counted three of the four noise channels. The fourth, the slowly varying part of the gravitational-wave channel, carries an equal amount of field stress with the opposite sign.
  - When every channel is recorded as gently as possible, the four contributions cancel exactly for every slowly varying mode.
  - The large ħ/(ℓ³τ) noise energy then exerts no net pressure.
- **What is left.** Only modes that vary faster than light can cross their wavelength contribute: the near-cone and timelike modes. Their pressure scales as ħc/(cτ)⁴, independent of ℓ.
  - If the light-cone band is also recorded at the floor, the leftover is a small positive Λ that equals the observed value when the gain time is cτ ≈ 23 µm. That sits just below the gain times R15-2 allowed.
  - If the light-cone band is recorded the way R15-2 actually chose, real gravitational waves dominate the leftover, and the Λ comes out negative.
- **So:**
  - the record noise does not overshoot the dark energy once all channels are counted;
  - it can be the dark energy only with a fitted parameter or with a new rule for the light-cone band;
  - the deciding datum is how the noise is recorded near the light cone.

---

## 1. Prior art (each counted once)

1. **R18-11 and vR18-11.**
   - Theorem G and Lemma P (confirmed, `vR18-11:3,5`).
   - The (P) formula with "TT excluded" (`vR18-11:6-13`; `rR18-11:114,166-187`).
   - The FRW suggestion ρ = (1 + ⟨x²⟩ + 2r + u_V/u₁)u₁/3 (`rR18-11:211-216`) and its rho-only corner value 0.78064 (`vR18-11:15`).
   - The per-mode table (`rR18-11:166-171`), which I recomputed independently: 10 of 10 entries agree, and j_y and t_× equal j_x and t₊ (`A:43-44`).
2. **R15-2 and vR15-2.**
   - Lemma A's exchange kernel (`rR15-2:103-110`).
   - The least-decoherence trade-off K = P⁻¹/4 + GPG (`r152_checks.py:261-275`).
   - The S-block correlated optimum, with p₂ free and "finite K_⊥⊥" (`rR15-2:125-127`). The printed choice is p₂ = Δ (`r152_checks.py:268`).
   - The TT floor S_h = 8πGħ|F|²e(s)/(c²|Ω² − ω²|) with e → 1 off the cone (`rR15-2:120`; `rR13-6:201`).
   - u₁ = ħI_F/(32π^{3/2}ℓ³τ), confirmed (`vR15-2:17`); recomputed as 1.170953060 ρ_Λ at the corner (`D:1`).
   - The τ_c window lower ends (`rR15-2:218-224`) and ρ_GW (`rR15-2:196`).
3. **R18-7 and vR18-7.** Π, K = i(p^αD^β + p^βD^α)/p² − ip^αp^β(p·D)/p⁴ (`rR18-7:144-146`). It is causal and not spatially local (`vR18-7:3`).
4. **R16-14 and vR16-14.** The Mercury bound 9.286e-15 kg/m³ (`vR16-14:11`, as recomputed in `vR18-11:13`).
5. **R14-2 (suggested).** The τ_c ceiling 1.49e-3 m. **R6-4.** The ℓ window endpoints.
6. **Comparators (RECALLED).**
   - FRW continuity ρ̇ + 3H(ρ + p) = 0.
   - Isaacson averaging.
   - ΛCDM parameters H₀ = 67.7, Ω_m = 0.31, Ω_r = 9.1e-5, Ω_Λ = 0.69.
   - Gravitational vacuum-energy pinning in FRW, Ford-type, not used.
7. **Repository grep.**
   - `P/agents/` and `P/TESTS.md` for "quasi-static TT", "TT field energy", "FRW" + "Π", "pressureless", "complete split", "K_pp": no derivation of the quasi-static TT stress in the budget or of an FRW lift of Π.
   - R13-6's "quasi-static TT" (`rR13-6:322-327`) counts only ⟨ḣ²⟩ for ω < 0.5ck, not the gradient stress.
   - R15-2's ⟨h²⟩_TT counts only the on-cone part (`r152_checks.py:245-249`, |F(ck)|²).
   - `docs/` was not grepped.

## 2. Hypotheses: class ℱ₁₉ (stated before any title)

- **H1.** E1 + N_c at a = 2 (P145): R15-2's channels ρ, T_⊥, V (two components) and TT (two polarizations); the repaired gain F = e^{−k²ℓ²/2}F_t(ωτ) common to all channels (Lemma CU); P76; P88 extended.
- **H2.** Least-decoherence split per channel, as R15-2's K = P⁻¹/4 + GPG (16πG = ħ = 1).
  - The 1×1 channels (V, TT) sit at P = 1/(2|G|).
  - The S block sits on R15-2's K_ρρ-floor family (p₁ = p₂γ² + Δ, q = −p₂γ), with p₂ either free (literal), at R15-2's printed Δ, or at the K_⊥⊥ minimizer p₂* (the "complete split", P-r192b).
  - TT has e(s) = 1 off the cone (τ_c variant, ε = 1).
- **H3.** Spatially flat FRW (matter, radiation, Λ; RECALLED) as a fixed background. The noise is stationary in **proper** units in the cosmic frame. Its statistics are isotropic and homogeneous in that frame: invariance of the ensemble, not covariance.
- **H4.** Short-wave locality. Since ℓ, cτ ≪ c/H, the coarse-grained per-mode source is the Minkowski one. Corrections are O(Hτ) ≲ 1e-29 and O((Hℓ/c)²) ≲ 1e-64 (suggested; scale separation, not computed).
- **H5.** The FRW Π is a causal conserving completion with zero homogeneous data before t₀. Its homogeneous mode is specified by a lift: A (pressureless in the cosmic frame) or B (covariant ∇V + ∇V).
- **Excluded.** E2; strong field; a ≠ 2 (except to show uniqueness of the zero); the γ-trade (price only); non-Gaussian noise; backreaction beyond first iteration.

---

## 3. Probe (a): the FRW homogeneous mode

- **Lemma F0 (proved).**
  - The O(G) metric closes on FRW, and the O(G·noise²) law must satisfy Bianchi. So the homogeneous mean of the noise sector (source s plus completion K) is covariantly conserved, provided background matter and radiation are conserved separately (H5): d(a³ρ_n)/dt = −p_tot d(a³)/dt.
  - Hence ρ_n(t) = −a⁻³∫_{t₀}^{t} p_tot d(a³) + ρ_n(t₀)(a₀/a)³ exactly. Zero start gives ρ_n(t₀) = 0 (Lemma P as H → 0).
  - **Late-time density = minus the late-time total homogeneous pressure, whenever that pressure tends to a constant.**
- **Lift A (proved; checked `C:7-13`).**
  - p_K = 0, so p_tot = p_s. Then ρ̇_K + 3Hρ_K = −ρ̇_s − 3H(ρ_s + p_s). This is R18-11's equation (`rR18-11:212`) iff ρ̇_s = 0, i.e. H3's proper-unit stationarity.
  - Solution: ρ_n = −p_s[1 − (a_on/a)³] + O(Hτ). The numeric ΛCDM integration matches to 1e-9 for a_on ≤ 1e-3.
  - w_n = −1/(1 − (a_on/a)³) → −1.
  - **Remainder:** p_s(a_on/a)³. For p_s < 0 it is negative dust whose ratio to matter, |p_s|/ρ_m(a_on), is fixed at switch-on.
- **Lift B (proved; checked `C:1-5, 15-23`).**
  - K^{μν} = ∇^μV^ν + ∇^νV^μ with V = (V(t), 0) gives ρ_K = −2V̇ and p_K = 2HV. It reduces to R18-7's k = 0 content (K^{ij} = 0) only when H = 0.
  - Conservation becomes −2V̈ − 6HV̇ + 6H²V = −D_s. In constant-ε eras it tracks ρ_n = ρ_s + (ρ_s + p_s)ε/(1 − ε), which differs by era.
  - Integrated over ΛCDM from a_on = 1e-3: ρ_n = −2.34ρ_s − 3.31p_s today, with w_n ≠ −1.
  - De Sitter has a growing mode e^{0.791Ht}, excited by a zero start.
  - **So the w → −1 attractor is lift-dependent, and so are its sign and size.**
- **Comoving-unit noise (proved, one line).** If ℓ and τ scale with a, then p_s ∝ a⁻⁴. Lemma F0 then gives ρ_n ∝ a⁻³ (dust-like, set at switch-on) and no Λ. The attractor needs proper-unit stationarity (H3).

## 4. Probe (b): the late-time ρ_noise in all channels

**Coefficients (checked `A:1-44`).**
- My independent per-mode table equals R18-11's in all 10 entries.
- Both V components and both TT polarizations contribute equally, with no cross terms.
- At a = 2:
  - ρ²: τ₀₀ = x² − 3, τ_kk = −(1 + x²);
  - ρT_⊥: −2 and +2;
  - each j: +4 and −4;
  - each t: 4(1 + x²)/(1 − x²)² and 4(3 − x²)/(1 − x²)² (units π/k²).

**Least-decoherence powers (checked `B:1-6`; numeric two-stage optimisation agrees with the closed forms).**
- V: P_j = 1/4 per component, so **u_V = 2u₀** at the floor (`B:15,21`). This is not small, as R18-11's FRW corner had assumed.
- TT: P_t = |1 − x²|/4 per polarization.
- **Normalization cross-checks (checked by hand).**
  - The TT/S floor ratio here, S_h/S_Ψ = (16π)²P_t/((4π)²(1 − x²)²P_ρ), tends to 4 as x → 0 with P_ρ at the 1×1 floor. That equals the x → 0 ratio of R15-2's own stated floors: 8πGħ/(k²(1 − x²)) over the quasi-static 4πGħ/(2k²) (`rR15-2:120, 227`).
  - For V, R15-2's "32πG" response (`rR15-2:123`) and its matrix ρρ entry ½ (`r152_checks.py:263`) are both twice the potential normalization (16πG for S_a; 4πG for Ψ). So the one convention covers all channels, and u_V = 2u₀ follows.
- S block: K_ρρ floor |g₁₁|, Δ = 1/|1 − x²|. K_⊥⊥ is minimized at p₂* = |1 − x²|, giving p₁ = 2/|1 − x²| and q = ∓1, i.e. r* = (1 − x²)²/2 (→ ½ quasi-statically). R15-2's printed p₂ = Δ equals p₂* only at x = 0.

**Theorem I₀ (inertness) (checked, exact rational identity `B:8-16`).** At a = 2, with all four channels at the complete least-decoherence split, the per-mode mean source of every spacelike mode (x < 1) vanishes: τ₀₀ = τ_kk = 0. Channel by channel, in units of u₀:

| | τ₀₀ | τ_kk |
|---|---|---|
| ρ | −2(3 − x²)/(1 − x²) | −2(1 + x²)/(1 − x²) |
| T_⊥ | +2 | −2 |
| V (2) | +2 | −2 |
| TT (2) | +2(1 + x²)/(1 − x²) | +2(3 − x²)/(1 − x²) |
| **sum** | **0** | **0** |

- The rows are `B:13-16` rewritten with (x − 1)(x + 1) = −(1 − x²). At x = 0 the rows are (−6, −2), (2, −2), (2, −2) and (2, 6).
- For general a the totals are −(a − 2)(3x² + 5)/(x² − 1) and −(a − 2)(4x⁴ + 7x² − 3)/(x² − 1), so the zero is at a = 2 only (`B:10-12`). The gauge-independent insertion (Theorem G) is also the one at which least-decoherence noise is gravitationally inert on spacelike modes.
- Timelike modes give (4, −4) (`B:26`). So (U) ρ_act = 0 on every mode.
- The structural reason is not identified (suggested: the floor makes the metric-noise covariance equal |G|, propagator-like).
- **Scope:**
  - Gaussian noise, O(G·noise²), Poisson law (gauge-free at a = 2 by Theorem G);
  - x ≠ 1;
  - TT at e = 1;
  - the S block at p₂*.
- **Control.** R18-11's channel set (TT omitted) gives ρ_n = u₀/(1 − r) under lift A. That is exactly R18-11's FRW formula with u₁ = u₀/(1 − r) and u_V = 2u₀ (`B:20-21`). It is the same component and the same normalization.
- **Literal (R15-2 as written, r free).** At x → 0, τ_kk = 3(2r − 1)/(r − 1)·u₀, so lift A gives ρ_n = (2r − 1)/(1 − r)·u₀: zero at r = ½, negative below it, positive above it (`B:19`).
- **R15-2's printed p₂ = Δ.** τ_kk = −6x² − 13x⁴ + …, so ρ_n = 2⟨x²⟩u₀ + O(x⁴) with ⟨x²⟩ = 2(17/21)(ℓ/cτ)² (exact, `D:24-26`). Near the cone this choice is (1 − x²)⁻³ singular (`B:17`). That is why R15-2 interpolates there (reading).
- **The matrix-|G| S choice** (K = |G_S|, not at the K_ρρ floor) gives τ_kk = +2.2u₀ at x = 0 (`B:35-40`). This illustrates that the sign is split-dependent.

**ρ_n(ℓ, τ) under lift A, by component (checked `D:4-41`).**
- **Bulk (x < 1):** as above.
- **Timelike floor:** (4/3)U_IR with U_IR = (ħ/4)∫_{|ω|>ck} e^{−k²ℓ²}|F_t|² d³k dω/(2π)⁴. That is 11ħc/(96π³(cτ)⁴) for ℓ ≪ cτ (closed form checked to 2e-6, `D:6`).
- **Near-cone band:** a reading.
  - At the floor (P-r192c), the TT log is cancelled by the ρ-channel's near-cone floor noise.
  - Under R15-2's bounded interpolation, TT's on-shell radiation pressure is left over: ρ_n ⊃ −ρ_GW/3. This dominates (4/3)U_IR by about ×200 through ln(ck t_H) (`D:17-22`). The bounded S-block band terms (no log) are not computed (suggested to be subdominant by that log).

## 5. Probe (c): where ρ_noise = ρ_Λ (thresholds recomputed by bisection; `D:7-41`)

| Split / near-cone | ρ_n at the corner (5e-6 m, 1.49e-3 m) | In-window match? |
|---|---|---|
| R18-11's set (TT omitted), floors | ≥ 1.171 ρ_Λ | none (match at ℓ = 5.27e-6 m, just outside); excluded by the setting |
| complete split, floor to the cone (P-r192c) | +5.9e-8 ρ_Λ | none in the registered window; ℓ-independent match at cτ = 2.32e-5 m < lower(ℓ) ≥ 1.21e-4 m |
| complete split, R15-2's bounded near-cone | −1.2e-5 ρ_Λ (negative) | none (wrong sign at every cτ ≥ lower(ℓ)) |
| R15-2 printed p₂ = Δ (bulk), any near-cone | +4.3e-5 ρ_Λ (bulk) | bulk match curve at cτ = 1.2e-3 to 5.2e-5 m, below lower(ℓ) at every ℓ by ×1.3 to ×2.3; at the ceiling ℓ = 2.1e-10 m (below the window) |
| literal r free, TT included | (2r − 1)/(1 − r)·1.171 ρ_Λ | yes, with r = 0.6496 at the corner (a fit); r − ½ ≈ 7e-3 at ℓ = 1e-6, 2e-9 at 1e-8, ≈ 4e-13 at 4e-10 (tuning) |
| γ-trade (price only) | (4γ_S + 2γ_V − 6γ_TT)u₀/3 | yes with an imbalance tuned to ρ_Λ/u₀; e.g. γ_TT = 0.573 at the corner |

- **Mercury** (`D:47-50`).
  - At any FRW match, |ρ_act| = 2ρ_Λ = 1.2e-26 kg/m³, with margin 7.8e11.
  - In flat (P) at the complete split, |ρ_act| ≤ 1e-33 kg/m³ at the ceiling.
  - R18-11's a = 2 local exclusion (ℓ ≲ 2.5e-8 m strict, `vR18-11:13`) rests on the TT-omitted value. At the complete split with the floor kept up to the cone, the strict-variant crossing is ℓ < 1.94e-8 m (checked; near-cone reading). Under the bounded reading it is not computed.
- **R6-4 lab bounds.** K_ρρ stays at its floor in every row except the γ-trade. So R6-4's mass-density margins are unchanged (suggested: R6-4's bounds concern K_ρρ).
  - Choosing r ≠ r* raises K_⊥⊥ (pressure-superposition decoherence), for example from 1.000 to 1.099 (x = 0, r = 0.65, from K_⊥⊥ = (p₂ + 1)(1/(4p₂) + 1/4) with p₂ = r/(1 − r)). It is not bounded by R6-4's mass-density tests.

## 6. Probe (d): prediction or tuning

- **No prediction.**
  - The registered construction needs a chosen r. That is an O(1) fit at the corner (0.3% on r for 2% on ρ_Λ), and a tuning to ρ_Λ/u₀ elsewhere, down to 4e-13 at ℓ = 4e-10 m.
  - The new completion P-r192c fixes only cτ: δ(cτ)/cτ = ¼ δρ_Λ/ρ_Λ. It leaves ℓ free and cancels nothing large. That is a one-parameter fit, not a tuned cancellation.
  - cτ ≈ 23 µm is the familiar ρ_Λ^{−1/4} length, about 0.1 mm divided by numerical factors. Read as a coincidence of scales, not an explanation.
- **Enforced vs stipulated (Λ-mechanism rule).**
  - **Enforced:** w = −1, given lift A (Lemma F0); the bulk zero, given a = 2 and the complete split (Theorem I₀ (inertness)).
  - **Stipulated:**
    - lift A (P-r192a);
    - the complete split (P-r192b);
    - the near-cone split (P-r192c), which sets the sign and size;
    - cτ (and r, if it is not at r*).
  - "No number" is distinct from "forced by the four texts": no Λ value here is forced by AX.
- **Radiative stability.** Not applicable at this order (tree-level noise stress). It is not computed.

## 7. Probe (e): prices (named, not adopted)

- **P-r192a (FRW lift of Π).** "The homogeneous mode of the conserving completion carries energy only, in the cosmic frame." This is load-bearing: lift B differs in sign and in w (`C:17-20`). *Axiom text:* AX:185 (dynamics), AX:187 (source/observable).
- **P-r192b (complete least-decoherence split).** "Each record channel minimizes the whole matter-decoherence matrix lexicographically: mass density first, then pressure." It fixes R15-2's free p₂ at p₂* (r* = (1 − x²)²/2) with no number. *Axiom text:* AX:82-83 (Record readout), AX:60-61 (Admissibility distribution) as R6-4's record-precision prices.
- **P-r192c (near-cone record split).** Either the floor is kept up to the cone with a TT-matched regulator (log-divergent ρ-noise variance and K_⊥⊥ near the cone), or R15-2's bounded interpolation is used. This is the deciding datum for the sign and size of the noise Λ. *Axiom text:* same as P-r192b.
- **Carried.** P145 (a = 2); P146 (energy history; (P) is used, and (U) cannot be posed in FRW without K, since ρ_s + p_s ≠ 0 in general); P76; P88 extended; P138 (Π); P-r15c (the γ-trade, named only).
- **v_max (whole zone).**
  - TT propagates at c.
  - S and V are constraint channels, instantaneous in the Poisson-gauge readout but non-propagating, and the mean is causal by Lemma CU (`rR15-2:128-131`).
  - Π is causal but not spatially local (`vR18-7:3`).
  - Inherited unchanged; matter is not modified here.
- **Counts.** Three new stipulated sentences (P-r192a/b/c) and one fitted number (cτ, or r). The basis is one sentence per completion piece, not per channel.

## 8. Corrections to earlier records (worker)

- **R18-11 (`rR18-11:27-43, 184, 211-216`) and vR18-11 item 3.**
  - The (P) value −(1 + ⟨x²⟩)u₁ + 2⟨q⟩u₁ − u_V omits the quasi-static TT stress. At the floor that stress is +2(3 − x²)/(1 − x²)·u₀ in τ_kk.
  - With TT included, the flat (P) active density is 3(1 − 2r)/(1 − r)·u₀ (x → 0) and exactly 0 at the complete split (spacelike modes). (U) is exactly 0, not −4u₁.
  - The NOISE-OVERSHOOT candidate and the Mercury crossing at 2.5e-8 m therefore belong to the TT-omitted set only.
- **R18-11's FRW suggestion (`rR18-11:213-215`).** With u_V at its floor (2u₀) the TT-omitted value is ≥ u₀, matching ρ_Λ only at ℓ = 5.27e-6 m (outside). With TT included it is r-dependent and zero at r*. The "3.65 µm" match assumed u_V ≈ 0, which the floor does not give.
- **R18-11's "ρ_GW ≲ ρ_Λ/12 at the ceiling" (`rR18-11:217`).** R15-2's 12.3 is a window factor in cτ. The exact value at the corner ceiling is ρ_GW = 3.6e-5 ρ_Λ (`D:17`).
- **R15-2's TT ⟨h²⟩ (`rR15-2:208`) and R13-6's quasi-static TT term.** Both count only on-cone or ḣ² content. The quasi-static TT metric noise at the floor is comparable to the S channel's (S_h/S_Ψ = 4/(1 − x²)). This does not affect the PPN margin.

## 9. Strong words checked

- **"Vanishes identically."** Per mode, exact rational identity, at a = 2, complete split, x < 1, Gaussian, O(G·noise²), Poisson law (gauge-free at a = 2). It is not claimed at x = 1 or for p₂ ≠ p₂*.
- **"Refuted" (NOISE-OVERSHOOT-FRW).** By a counterexample in the registered channel set (complete split, lift A, τ_c ceiling). It is checked under the floor-to-cone reading.
  - Under R15-2's bounded reading, the TT part is checked (−1.2e-5 ρ_Λ).
  - The bounded S-block band terms are suggested to be O(ħc/(cτ)⁴) ≈ 1e-5 ρ_Λ at the ceiling, with no log factor.
  - It is not a claim about every lift or every split. With r far from ½ the bulk is u₀-sized.
- **"Exact" (lift A).** Given the lift and H3-H4. The ΛCDM background is RECALLED.
- **"No in-window match."** For the complete split, τ_c variant, cτ ∈ [lower(ℓ), 1.49e-3] m with R15-2's lower(ℓ), under the two near-cone readings considered. It is not established for the strict variant or for other near-cone interpolations.
- **Numbers.** ρ_Λ uses the referee's constants (H = 67.7 km/s/Mpc; RECALLED).

## 10. What would decide it

1. **A referee** of Theorem I₀ (inertness), of Lemma F0 with the lift-dependence, and of the NEITHER candidate. Theorem I₀ alone changes the reading of R18-11's overshoot.
2. **The near-cone record split (P-r192c).** Can the floor be kept up to the cone with a regulator matched to TT's ln(ckt), and what does that cost in K_⊥⊥ and ρ-noise variance? This decides the sign of the noise Λ.
3. **The owner's choice of FRW lift** (P-r192a), and whether the complete split (P-r192b) is the intended reading of "least decoherence".
4. **Whether R15-2's τ_c lower end survives** under P-r192c. If it does not, the ℓ-independent match at cτ ≈ 23 µm enters the window and becomes the NOISE-IS-Λ test proper.
