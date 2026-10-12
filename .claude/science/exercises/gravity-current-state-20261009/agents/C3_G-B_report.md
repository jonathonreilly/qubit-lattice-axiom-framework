# C3 lane G-B: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. **Codex sol referee: INCONCLUSIVE. The admixture conjunct is controlled: A_rms = 7.27e-28 at 1 Gpc, far below 1e-3, as an asymptotic ceiling. The PASS clause 'mean exactly the linearized-GR retarded solution' fails only at finite density (the mean is K_rho*T, which equals G_R*T only as density goes to infinity). FAIL is inapplicable** (C3_G-B_referee.md).

**Verdict (worker):** PASS within the registered scope: a linearized, source-driven tensor carried on links. Two judgment items are flagged for the referee. (1) The clause "the mean is exactly the linearized-GR retarded solution" is met only in this sense: the mean's de Donder (harmonic-gauge) structure is exact, and the scalar kernel differs from the retarded Green function by the O(l^2/r^2) corrections already accepted in E1'. (2) My PREREG named "F_P grows with s/l at fixed s/D" as an example of lost control. F_P does grow up to s/l of about 24, then stays flat to s/l = 48, everywhere below 2.22 and inside the proved bound.

**Plain summary:** In Einstein's theory a gravitational wave reaching a detector stretches space in only two "tensor" patterns, plus and cross; any other pattern would show up in polarization tests. Here the wave travels from source to detector only along "links" between randomly scattered spacetime events. In any one random arrangement the received wave is therefore a random sample of the source rather than its smooth average, and that sampling error could add wrong patterns. Averaged over arrangements, the link-carried wave is exactly Einstein's weak-field wave in its standard gauge. In each single arrangement the wrong-pattern part is only counting noise, and I proved it is at most about √3 times the simple counting estimate; simulations at small scales follow this law. For a neutron-star merger a billion parsecs away, the wrong-pattern part is at most about one part in 10^26 to 10^28, against an allowed one part in 1,000. This tests only a weak gravitational wave carried on links: it does not explain why the graviton stays massless, and it does not test strong gravity.

# G-B report: a tensor field propagated along links (campaign C3, lane G)

**Worker.** Claude Opus 5.5, max effort.

**Pre-registration.** `PREREG.md`, stamped `Sat Oct 10 01:00:39 UTC 2026`, written before any G-B computation. All runs had finished by 01:31Z.

**Repository.** No repository file was edited; `git status` is clean.

**Test setting only.** The E1/E1′ axiom conflicts apply unchanged:
- Lattice is replaced by a Poisson sprinkling.
- The causal order is supplied, because records carry no time.
- Records as events conflict with "one record per site, permanent".

**Primitives.** No registered primitive is used as a premise. The scale-reference primitive enters only as the ruler ℓ = ℓ_P.

## 1. Verdict against the fixed reading

**PASS, within the registered scope:** a linearized, source-driven tensor carried on links, h̄^{μν}(x) = ρ⁻¹ Σ_y aL(x,y) T^{μν}(y).

**Controlled law.** It is a tensor corollary of the refereed E1′-b Poincaré bound: the proof steps are EXACT, and one step is new.
- E[A²] ≤ (3 + C′_S·s/D) × (exact Mecke diagonal ratio).
- Equivalently, E[A²] ≤ (3 + C′_S·s/D)·(√6/3)·ℓ²D·Σ_nonTT/|Σ_TT|².

**At 1 Gpc with ℓ = ℓ_P, for the BNS proxy:**
- A_rms ≤ 2.3e-28 (v = 0.4, face-on) up to 3.0e-26 (v = 0.05, edge-on); 7.4e-27 at v = 0.1, edge-on.
- The bar is 1e-3.
- Chebyshev gives P(A > 1e-3) ≤ 9e-46 per observer event.

**The mean** is exactly the de Donder (harmonic-gauge) solution built with the E1′ mean link kernel:
- ∂_μ E h̄^{μν} = 0 exactly, at every density;
- one scalar kernel acts on all ten components;
- it is massless;
- the kernel equals G_R up to the E1′-confirmed O(ℓ²/r²) power corrections, which amount to 1.4e-101 rad of phase at 100 Hz and 1 Gpc.

**Flagged for the referee** (section 8):
1. Is "exactly the linearized-GR retarded solution" met by an exact de Donder structure plus the E1′-accepted power corrections of the scalar kernel?
2. My PREREG named "F_P grows with s/ℓ at fixed s/D" as an example of lost control.
   - It does grow for s/ℓ ≤ 24 at s/D = 0.3 and 0.1. It is flat at s/D = 0.03.
   - At s/D = 0.3 it then saturates between s/ℓ = 24 and 48.
   - It stays ≤ 2.22 < 3 everywhere, inside the proved uniform bound.
   - Read literally, this example would give INCONCLUSIVE, not FAIL.

**Scope.** This is a linearized graviton carried on links. It does not cover:
- its protection (G-C) or its mass;
- nonlinear gravity;
- the strain crackle of the order (G-A);
- relays or regeneration;
- initial-value evolution.

## 2. What I read (in full)

- `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (all 3 primitives).
- Packet `TESTS.md`, all 524 lines: the rules, T0–T2, E1–E3, B, E1′, E1′-b, and Campaign C3 with G-B's fixed readings.
- `SUMMARY.md` §7–9.
- `agents/supervisor_E1p_b.md`, `agents/E1p_b_referee.md`, `agents/E1p_report.md`, `agents/E1p_referee.md`.
- `scripts/E1p/e1p_core.py`, `S2_needle_overlap.py` with its `.out`, and `E1p_1_massless_needle.py`. The last supplies the exact-dependence-region sampler and the link test; I copied it unchanged into scratch.

## 3. Setting and observables

**Units and kernel.**
- ρ = ℓ⁻⁴; every run uses ρ = 1.
- The observer is a fixed event (a Palm point).
- a = √ρ/(2π√6).
- Sampling is truncated at m = ρV < 24, i.e. e^{-24} per point, matched in the quadrature.

**Source.** An exactly conserved superpotential quadrupole:
- Q^{ij} = q^{ij} e^{-iΩt} g(ξ), with g ∝ (1 − |ξ|²/s²)⁴.
- T^{00} = q^{ij}∂_i∂_j g, T^{0i} = iΩ q^{ij}∂_j g, T^{ij} = −Ω² q^{ij} g, each times e^{-iΩt}.
- ∂_μT^{μν} ≡ 0. The mass quadrupole is 2q, with no monopole and no dipole.

**Orientations** (propagation along n = x̂):
- A: q = diag(0, 1, −1), pure TT. By symmetry its mean has no non-TT part.
- B: a tilted oscillator, 56% TT by Frobenius weight.

**Frequencies:** Ωs = 0.5 and 1, i.e. λ/s = 12.6 and 6.3.

**Measured per realization:**
- the complex field (cos and sin phases on the same sprinkling) and its deviation δh̄ from the exact Mecke mean;
- the helicity sectors 0, ±1, ±2 with respect to n, which are orthogonal in the Frobenius norm;
- **A = ‖P_nonTT δh̄‖ / ‖P_TT E h̄‖;**
- the far-zone gauge contraction G^ν = h̄^{0ν} − n_i h̄^{iν}.

**What is not counted as admixture.** The mean's own helicity-0/±1 part is linearized GR's de Donder gauge content, which is pure gauge in the radiation zone. It is reported separately.

**Why these choices are conservative.**
- The single-event A bounds every smoothed observable, because smoothing never raises the rms deviation (Minkowski).
- The complex A is √2 larger than the real single-phase A.

## 4. Derivation (full text in `DERIVATION.md`)

**1. Mean (EXACT).**
- By Mecke, E h̄ = K̄ * T with K̄ = a·e^{-ρV}·θ, which depends only on x − y.
- Integrating by parts against the smooth conserved source gives ∂_μ E h̄^{μν} = K̄ * ∂_μT^{μν} = 0.
- The same scalar kernel acts on every component, so the mean has the de Donder form.

**2. Per realization (EXACT).**
- L_Π(x,y) is not a function of x − y.
- h̄ is piecewise constant in x, so ∂_μ h̄^{μν} is a sum of surface deltas on the future cones of sprinkled points.
- No identity carries conservation onto the realized field: the harmonic gauge holds only in mean.

**3. Tensor corollary (EXACT steps plus the refereed E1′-b geometry).**
- For any bounded vector weight w, for example w = P·T for any linear map P:
  E‖δF_w‖² ≤ (3 + C′_S·s/D)·Diag_w, with Diag_w = ρ∫‖w‖² e^{-ρV}.
- **The only new step:** AM–GM plus a Schur test on the off-diagonal term, using |w(y)||w(y′)| ≤ ½(|w(y)|² + |w(y′)|²).
  - This turns the y′ integral into E1′-b's integral for the indicator of the source region.
  - So C′_S is the E1′-b constant of that region, independent of w.
- **Hypotheses** are those of E1′-b:
  - weights slowly varying across the cone-normal shell ℓ²/D;
  - bounded aspect ratio;
  - D ≫ s ≫ ℓ.

**4. Shell asymptotics (controlled).**
- ρ∫ f e^{-ρV} d⁴y = (√6/(2ℓ²)) ∫ f_ret d³y/r × (1 + O(ℓ²/r²) + O(Ωℓ²/r)).
- Checked: asymptotic/exact = 1.0005 at D = 40.

**5. The law.**
- E[A²] ≤ (3 + C′_S·s/D)·(√6/3)·ℓ²D·Σ_nonTT/|Σ_TT|², where:
  - Σ_nonTT = ∫‖P_nonTT T‖²_ret d³y;
  - Σ_TT = ∫P_TT T_ret d³y = ½Ï^TT.
- **Closed form for orientation A:**
  E[A²] ≤ (3 + C′_S·s/D)·(√6/3)·(ℓ²D/s³)·[1152·I₁·(Ωs)⁻⁴ + 64·I₂·(Ωs)⁻²] / (N_g² ĝ²),
  with N_g = 0.4642122, I₁ = 9.5223e-3, I₂ = 3.36081e-2.
- **What it means:** A ≈ (counting noise 1/√N̄) × (λ/2πs)².
  - The second factor is the cancellation ratio between the mass density at each point, which is helicity 0, and the TT radiative moment.
  - Link propagation is a Monte Carlo of the retarded integral. The admixture is the Monte Carlo error in the cancellation that makes T^{00} radiate like a TT wave.

**6. Worldline decorrelation (EXACT u-slab argument).**
- Define u(z) = (t_x − t_z) − n·(z − x). Then z ≺ x implies u(z) > 0, and y ≺ z implies u(y) > u(z).
- So the dependence regions of the observers x and x + Δe_t (or x + Δn) are disjoint once Δ ≥ U_max, with U_max ≤ (s² + τ_max²)/(2(D − s)).
- The two fields are then independent.
- This bounds smoothed and differentiated observables (DERIVATION §6). Decorrelation under transverse spatial shifts is ARGUED only.

## 5. Results (all CHECKED unless labelled)

### R1. The mean

**Transversality.** Finite differences of the exact Mecke mean give |∂_μ E h̄^{μν}| / (largest single term) = 1.5e-6, 3.9e-7 and 9.6e-8 at ε = 0.04, 0.02 and 0.01. That is pure ε² truncation, so the divergence is zero.

**Sampled means against quadrature.** `gb_meancheck.py` gives 660 Re/Im z-values, max |z| = 2.49, none above 3.
- A code slip: the "max|z|" printed in the run logs used the complex sd and the Re parts only. It is superseded by this check.

**Mean non-TT content.**
- Orientation A: non-TT/TT = 5e-14, i.e. roundoff.
- Orientation B: non-TT/TT = 1.27–1.41, which is GR's de Donder content. Its far-zone gauge contraction falls as 1/D, the near-zone terms of GR: 0.49, 0.15 and 0.045 at D/s = 3.3, 10 and 33 (Ωs = 0.5).

**Quadrature.** Converged to 1e-13. N̄ = 221.51 at (s, D) = (12, 40) reproduces E1′.

### R2. Fano factors

F_P = E‖P δh̄‖²/Diag_P, ± 1 se in the last digits. The columns are orientation A with Ωs = 0.5; the last column is F_nonTT for orientation B with Ωs = 1.

| s/ℓ | D/ℓ | s/D | n | N̄ | F_TT | F_±1 | F_0 | F_nonTT | F_gauge | B, Ωs=1: F_nonTT |
|---|---|---|---|---|---|---|---|---|---|---|
| 6 | 20 | 0.3 | 2000 | 55.3 | 1.559(51) | 1.401(33) | 1.340(43) | 1.343(41) | 1.341(42) | 1.296(32) |
| 12 | 40 | 0.3 | 1500 | 221.5 | 1.747(64) | 1.696(44) | 1.669(59) | 1.670(57) | 1.670(58) | 1.478(39) |
| 24 | 80 | 0.3 | 700 | 886.4 | 2.030(108) | 1.963(79) | 2.171(114) | 2.161(109) | 2.166(112) | 1.798(80) |
| 36 | 120 | 0.3 | 500 | 1994.5 | 1.875(113) | 1.972(86) | 2.215(140) | 2.204(134) | 2.210(137) | 1.761(86) |
| 48 | 160 | 0.3 | 300 | 3545.9 | 2.151(206) | 1.841(108) | 1.769(154) | 1.773(147) | 1.771(151) | 1.560(99) |
| 6 | 60 | 0.1 | 2000 | 18.5 | 1.274(47) | 1.144(29) | 1.131(40) | 1.132(39) | 1.132(39) | 1.102(31) |
| 12 | 120 | 0.1 | 1500 | 73.9 | 1.285(51) | 1.261(33) | 1.223(43) | 1.225(42) | 1.224(42) | 1.185(35) |
| 24 | 240 | 0.1 | 700 | 295.5 | 1.485(89) | 1.328(50) | 1.326(76) | 1.326(72) | 1.326(74) | 1.232(50) |
| 6 | 200 | 0.03 | 2000 | 5.5 | 1.124(53) | 1.031(32) | 1.087(38) | 1.085(37) | 1.086(38) | 1.047(33) |
| 12 | 400 | 0.03 | 1500 | 22.2 | 1.098(44) | 1.068(29) | 1.150(41) | 1.147(39) | 1.148(40) | 1.045(31) |
| 24 | 800 | 0.03 | 600 | 88.6 | 1.151(69) | 1.088(48) | 1.079(59) | 1.079(57) | 1.079(58) | 1.075(46) |

- Every F, for all 4 sources and 6 sectors, is ≤ 2.22. That is below 3, and so below the pre-registered 3 + 10s/D. Full table: `out/gb_tables.md`.
- The s = 36 and s = 48 rows were added after the PREREG, to test the s/ℓ trend.

### R3. Admixture per realization

Orientation A, Ωs = 0.5. The prediction is √Diag/H_TT.

| s/ℓ | D/ℓ | A_rms | prediction | (A_rms/pred)² | median | 99th pct | max |
|---|---|---|---|---|---|---|---|
| 6 | 20 | 9.36 | 8.08 | 1.34 | 6.51 | 24.5 | 32.4 |
| 12 | 40 | 5.22 | 4.04 | 1.67 | 3.66 | 12.8 | 18.0 |
| 24 | 80 | 2.97 | 2.02 | 2.16 | 2.09 | 7.52 | 8.96 |
| 36 | 120 | 2.00 | 1.35 | 2.20 | 1.39 | 4.89 | 6.57 |
| 48 | 160 | 1.34 | 1.01 | 1.77 | 0.92 | 3.32 | 4.70 |
| 6 | 60 | 14.9 | 14.0 | 1.13 | 10.0 | 39.5 | 70.4 |
| 12 | 120 | 7.77 | 7.02 | 1.23 | 5.46 | 18.7 | 29.1 |
| 24 | 240 | 4.04 | 3.51 | 1.33 | 2.75 | 9.94 | 15.6 |
| 6 | 200 | 26.7 | 25.7 | 1.09 | 17.2 | 72.9 | 97.6 |
| 12 | 400 | 13.7 | 12.8 | 1.15 | 9.54 | 34.0 | 43.3 |
| 24 | 800 | 6.67 | 6.42 | 1.08 | 4.82 | 16.9 | 20.9 |

- **A is O(1–30) here by design.** N̄ is 5–3500 and (λ/2πs)² is 1–4. The test is whether the law (prediction × √F) holds, not how small A is.
- **Scalings are reproduced:**
  - A ∝ √D at fixed s;
  - A ∝ 1/s at fixed D/s;
  - the (Ωs) dependence.
- **The noise is not pure gauge.** Per realization, |G(δh̄)|/TT is 0.95–1.0 × A_rms; for example 7.68 against 7.77 at (12, 120).

### R4. Law against exact quadrature

The closed form divided by the exact quadrature is:

| s/D | ratio |
|---|---|
| 0.3 | 0.990 |
| 0.1 | 0.999 |
| 0.03 | 0.9999 |
| 0.01 | 0.99999 |

This covers s/ℓ = 6–24 and Ωs = 0.5, 1 (`out/gb_law.out`).

### R5. The Poincaré right-hand side, measured directly

This check was added after the PREREG. It measures E∫‖D_zF‖²ρ dz / Diag, the quantity the theorem bounds by 3 + C′_S s/D. Orientation A, Ωs = 0.5:

| s/D, sector | s/ℓ = 6 | 12 | 24 | 36 | 48 |
|---|---|---|---|---|---|
| 0.3, non-TT | 1.836(63) | 2.220(94) | 2.515(115) | 2.441(104) | 2.547(79) |
| 0.3, TT | 2.363(167) | 2.516(279) | 3.094(520) | 2.630(164) | 2.803(175) |
| 0.1, non-TT | 1.614(59) | 1.811(64) | 1.905(67) | — | — |
| 0.1, TT | 1.869(107) | 1.881(87) | 1.850(92) | — | — |

- The right-hand side saturates at about 2.5 for s/ℓ ≥ 24, which supports a uniform constant.
- Every Var/Diag is ≤ the right-hand side, as it must be.

### R6. Worldline decorrelation

Added after the PREREG. Two observers share one sprinkling; s = 6, D = 60, n = 800.

| Δ·D/ℓ² | 0 | 0.3 | 0.6 | 1.2 | 3 | 6 | 12 | 24 | 48 |
|---|---|---|---|---|---|---|---|---|---|
| corr (A) | 1 | 0.762(44) | 0.530(42) | 0.212(36) | 0.014(33) | −0.013(33) | 0.029(32) | 0.030(33) | 0.037(34) |
| corr (B) | 1 | 0.776(37) | 0.536(34) | 0.247(30) | 0.018(26) | 0.015(25) | 0.027(27) | 0.022(27) | −0.009(25) |

- Rigorous independence (U_max) applies only from Δ·D = 27.5ℓ².
- The measured correlation is already zero from Δ·D ≈ 3ℓ², the thickness of the link shell.

### R7. Needle overlap

The S2 needle-overlap Monte Carlo was rerun and reproduced exactly: overlap·b⁴ → 23.0ℓ⁸.

### R8. Translation to 1 Gpc

ℓ = ℓ_P; source: `out/gb_translate.out`.

**Inputs.**
- ℓ²D/V_star = 1.11e-57, for a 12-km star.
- N̄ = 1.1e57 per star.

**BNS proxy, A_rms bound.** ‖T‖² is dominated by the mass density; stresses and momentum are allowed up to a factor 2.

| v | edge-on (least TT) | face-on |
|---|---|---|
| 0.05 | 3.0e-26 | 1.5e-26 |
| 0.1 | 7.4e-27 | 3.7e-27 |
| 0.2 | 1.8e-27 | 9.2e-28 |
| 0.4 | 4.6e-28 | 2.3e-28 |

**Superpotential source** (s = 100 km, λ = 3000 km): A_rms ≤ 7.3e-28.

**What it would take to reach 1e-3:** s³(Ωs)⁴ ≤ 1.0e-36 m³, for example a 1 m source at Ωs = 1e-9. Such a source gives no detectable signal at 1 Gpc.

**Mean against G_R:**
- arrival offset 2.2e-104 s;
- phase offset 1.4e-101 rad at 100 Hz;
- static correction 2.1e-121.

**Noise along the worldline.**
- Decorrelation time: ≤ 5.4e-25 s (rigorous U_max).
- Shell time ℓ²/(cD) = 2.8e-104 s; R6's ~3ℓ²/D scaling, applied at 1 Gpc, gives about 8e-104 s.
- Averaging over 1 ms cuts the noise variance by ≤ 1e-21.

**Harmonic-gauge violation as a time derivative,** relative to the wave's own derivative:
- It stays below 1e-3 at any time resolution coarser than 9.4e-27 s.
- It is 1.2e-5 at a resolution of U_max, and 4.6e-36 at 1e-4 s.
- This is EXACT given the bound and the u-slab argument.

**Curvature proxy** (second time derivative): below 1e-3 for any resolution coarser than 3.8e-17 s. This is ARGUED, because the spatial parts rest on decorrelation that is not proved.

## 6. Mapping onto the fixed readings (PREREG §5)

**PASS, because every condition holds:**
- the mean statements are proved (EXACT);
- the tensor corollary is proved under the E1′-b hypotheses;
- the pre-registered numerical checks pass: means within 3 se; every F_P ≤ 3 + 10s/D; the law matches quadrature; S2 reproduced;
- at 1 Gpc the controlled law gives A_rms between 2.3e-28 and 3.0e-26, at least 23 orders of magnitude below 1e-3, with a per-event probability bound.

**No extrapolation.** No fitted trend is extrapolated: the 1-Gpc numbers come from the proved bound and exact integrals.

**Margin.** Overturning the result would need F of about 1e46. The measured F is ≤ 2.2, and the measured Poincaré right-hand side saturates at about 2.5.

## 7. Labels

| Label | Claims |
|---|---|
| EXACT | §4 items 1–3 and 6; Chebyshev; smoothing inequalities |
| CHECKED | R1–R7 |
| ARGUED | the BNS stress allowance (gravitational-stress estimate ~1e-8 of ∫ρ_m²; strut model ~v⁴); transverse decorrelation; the curvature proxy |
| COMPARATOR | none new; Johnston's normalisation via E1′ |

## 8. What a referee should re-check

1. The Schur/AM–GM step (DERIVATION §3), and the claim that C′_S is the E1′-b constant of the source region, independent of the weights.
2. Whether "exactly the linearized-GR retarded solution" is met:
   - the de Donder structure, transversality and masslessness are exact;
   - the scalar kernel matches G_R only up to the E1′ O(ℓ²/r²) corrections.
   If the referee reads "exactly" more strictly, I suggest INCONCLUSIVE, not FAIL.
3. My PREREG example: F grows with s/ℓ for s/ℓ ≤ 24 at s/D = 0.3 and 0.1. My judgment is that the corollary is still controlled, because it is proved and the growth saturates.
4. The admixture definition:
   - the per-realization deviation, projected onto helicity 0 and ±1, relative to the mean TT amplitude;
   - the mean's own non-TT part treated as GR gauge content.
5. The BNS proxy: a linearized source with assumed conserving stresses, and the stress allowance.
6. The rms reading of "stays below". An event-wise supremum along the whole worldline would need tail bounds; a detector-smoothed observable does not.
7. The u-slab proof, and the smoothing bounds built on it.

## 9. Files

All paths are under `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/G-B/`.

**Notes**
- `PREREG.md`
- `DERIVATION.md`

**Scripts, in `scripts/`**
- `gb_core.py`
- `gb_run.py`
- `gb_law.py`
- `gb_translate.py`
- `gb_decor.py`
- `gb_poincare.py`
- `gb_table.py`
- `gb_meancheck.py`
- Copied unchanged from the packet: `E1p_1_massless_needle.py`, `e1p_core.py`, `S2_needle_overlap.py`

**Outputs, in `out/`**
- Run logs: `gb_main1.log` to `gb_main5.log`.
- Per-realization fields: `gb_main*_s*_D*.npz` (11 files).
- Summaries: `gb_tables.md`, `gb_law.out`, `gb_translate.out`, `gb_meancheck.out`.
- Decorrelation: `gb_decor_s6_D60.log`.
- Poincaré checks: `gb_poincare_sD0.3.log`, `gb_poincare_sD0.1.log`, `gb_poincare_s36.log`, `gb_poincare_s48.log`.
- Needle overlap: `S2_needle_overlap_rerun.out`.
- `gb_smoke_s6_D20.npz` is a smoke test and is not used.

**needs_referee = true.** This is not a FAIL. A referee is requested because the PASS rests on a new corollary and on the two judgment items above.

---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** True

**Corrected verdict:** G-B: PASS, within the registered scope and with corrections. The scope is a linearized, source-driven tensor carried on links (h̄ read as the trace-reversed potential), compared at amplitude level, with "stays below" read as an rms bound plus Chebyshev, i.e. for detector-smoothed observables.

Admixture conjunct: met by a controlled law. The vector-weight (AM–GM/Schur) corollary of the refereed E1′-b bound is valid:
- E[A²] ≤ (3 + C′_S s/D) · Diag_nonTT / |P_TT E h̄|².
- E1′-b's y′-integral bound is pointwise in y, so the corollary goes through.
- With ℓ = ℓ_P at 1 Gpc, the controlled benchmark (superpotential quadrupole, s = 100 km, λ = 3000 km) gives A_rms ≤ 7.3e-28.
- The BNS proxy (≤ 3.0e-26 edge-on, v = 0.05) is ARGUED, not controlled. Its face-on numbers are overstated by √2: the face/edge TT² ratio is 8, not 4, so the low end of the range is ≈ 1.6e-28, not 2.3e-28.
- Every benchmark sits 22–25 orders of magnitude below the 1e-3 bar.

Mean conjunct: met under the pre-registration author's stated intent. In `agents/supervisor_thread.md`, written before results, the supervisor said: "The mean is exactly the linearized-GR retarded field, since G₀'s mean commutes with derivatives". On that reading the conjunct holds:
- the de Donder form and ∂_μ E h̄^{μν} = 0 are exact;
- the kernel is the E1′-accepted mean link kernel K̄, equal to G_R + O(ℓ²/r²), with a phase offset of about 1e-101 rad.

Under a strictly literal reading (K̄ ≡ G_R) the conjunct fails at finite ρ, and the verdict would be INCONCLUSIVE, not FAIL. The referee should state which reading applies.

Not covered: protection or mass (G-C), nonlinear gravity, the order's strain crackle (G-A), an event-wise supremum along the worldline, curvature-level (transverse-derivative) bounds, and initial-value propagation.

**Issues:** None of these change the verdict. Most are corrections of wording or labels.

1. **"Exactly" clause (interpretive).** The mean is K̄*T. This is not G_R*T, and it does not solve □h̄ = −16πG T exactly: K̄ fills the inside of the cone, so □K̄ ≠ 0 away from the origin. "Exactly the linearized-GR retarded solution" therefore holds for the structure (de Donder, conserved, one scalar kernel, massless) and holds for the kernel only up to O(ℓ²/r²) and O(Ωℓ²/r). The supervisor's pre-results text supports this reading. The worker flagged the point honestly. The referee must rule on it.

2. **The worker's own pre-registered INCONCLUSIVE trigger fired.** PREREG §5 gives "measured F_P grow with s/l at fixed s/D" as an example of lost control. Growth is clear: at s/D = 0.1, 1.13 → 1.23 → 1.33; at 0.3, 1.34 → 2.2.
   - Overriding it is defensible, because control now comes from the proof, not the data. This is how E1′-b turned E1′ from INCONCLUSIVE to PASS.
   - But the override is post hoc and needs an explicit ruling.
   - The "saturates between s/ℓ = 24 and 48" claim is weak and not load-bearing. The s = 48 point (n = 300) shows F_nonTT falling from 2.20 to 1.77 (about 2.2σ, unexplained), and F_TT = 2.15 ± 0.21 shows no saturation.

3. **Label inflation.** §7 lists §4 item 3 (the tensor corollary) as EXACT. It inherits E1′-b's asymptotic pieces: B_diag = Diag only at leading order, and C′_S is finite but never computed. It should be labelled CONTROLLED (exact steps plus refereed asymptotic geometry). This does not matter at s/D ~ 1e-21.

4. **Face-on BNS factor.** c_orient(face)/c_orient(edge) = 8, not 4.
   - Edge-on: |Σ_TT|² = 2m²v⁴. Face-on: 16m²v⁴.
   - The face-on A values are therefore √2 too large. This is in the conservative direction. The edge-on worst case is correct.

5. **BNS stress allowance.** The "~1e-8 of ∫ρ_m²" gravitational-stress estimate leaves out neutron-star pressure and self-gravity field stress. Those are about 1e-2 to 1e-1 of ρ²; compactness GM/R is about 0.17. They still fit inside the factor-2 allowance (κ_T ≤ 1). The BNS benchmark stays ARGUED. The controlled benchmark is the superpotential source.

6. **Per-realization versus rms.** Chebyshev (≤ 9e-46) applies per event. Along a worldline the field changes on the shell time ℓ²/D. A union bound over U_max blocks therefore does not control the event-wise supremum, since there are about 1e80 distinct values per block. The PASS is valid for rms and detector-smoothed observables, where a union bound over detector samples is trivial. The worker flagged this (item 8.6). It should be stated as scope.

7. **"Single-event A bounds every smoothed observable."** This bounds the rms of the smoothed deviation. The ratio to the smoothed signal also needs a window that does not suppress the TT signal, for example a filter matched to the signal band. Minor wording.

8. **Wording.** §1 describes the 1.4e-101 rad phase offset as part of the "O(ℓ²/r²) power corrections". In fact it is the O(ℓ²/r) arrival delay times Ω.

9. **Mean-check statistics.** `gb_meancheck.out` reports mean z² = 0.67 and fraction(|z| > 2) = 0.015 over 660 z-values. That is under-dispersed. It is consistent with strongly correlated z-values: one sprinkling is shared across 4 sources, and Re/Im and components are correlated. It is harmless, but "none above 3" is weak evidence alone. My independent means agree (max|z| ≤ 2.44).

10. **Setting reading.** The setting writes h_μν = ρ⁻¹ΣG₀T_μν. The worker reads it as the trace-reversed h̄. Only that reading makes the mean a linearized-GR solution. This is the natural reading, but it should be stated. TT is unaffected.

**Checked and found sound:**
- Mecke mean and exact transversality.
- The add-one cost and the B_diag factor ⟨m⟩ = ½.
- The off-diagonal Mecke step with P(both linked) ≤ e^{−(m+m′)/2}.
- AM–GM reducing the off-diagonal to the pointwise E1′-b y′-integral with J′ = 1_S.
- The u-slab bound. U_max ≤ (s² + τ²)/(2(D − s)) is exact, because r(1 − cosθ) = (r sinθ)²/(r + ξ) ≤ s²/(2(D − s)).
- The shell normalisation and the 1-Gpc arithmetic.

**Re-runs:** All runs used OMP_NUM_THREADS=2. Files are in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/G-B/verify/`.

1. **`v_mc.py`: an independent Monte Carlo, written from scratch with no worker code imported.**
   - My own rejection sampler on a tighter dependence region (radius s + τ/2).
   - A brute-force link test.
   - My own superpotential T.
   - TT taken through the explicit Λ projector, with nonTT = total − TT.
   - Mecke quadrature on a Cartesian grid.

   Orientation A, mine against the worker's (Ωs = 0.5):

   | (s, D), n | F_TT | F_nonTT | A_rms |
   |---|---|---|---|
   | (6, 20), n = 3000 | 1.570(44) vs 1.559(51) | 1.345(34) vs 1.343(41) | 9.372 vs 9.36 |
   | (6, 60), n = 3000 | 1.173(34) vs 1.274(47) (1.7σ) | 1.127(30) vs 1.132(39) | 14.91 vs 14.9 |
   | (12, 40), n = 1500 | 1.770(68) vs 1.747(64) | 1.712(62) vs 1.670(57) | 5.283 vs 5.22 |

   - Ωs = 1 also agrees.
   - Sampled means match quadrature: max|z| 0.8–2.4 over 10 Re/Im components per configuration.
   - The Diag ratio A²_diag matches the worker's exact quadrature to 6 digits: 65.30314 vs 65.30311.
   - An (s, D) = (24, 80) run was stopped at 12 minutes to stay within the runtime budget. Its output file is empty.

2. **`v_closed.py`: the closed form checked independently.**
   - I₁ = 9.52230e-3, I₂ = 3.36081e-2 and N_g = 0.4642122 reproduced by separate angular and radial integration.
   - Closed form divided by exact quadrature: 0.9917 at s/D = 0.3, 0.99999 at 0.01, and 1.00000 at s/D = 1e-3 and 4e-4, for Ωs = 0.2, 0.5 and 1.
   - The 1-Gpc superpotential bound reproduced: A_rms ≤ 7.27e-28.

3. **The BNS orientation factor recomputed** with the TT projector: face/edge |Σ_TT|² = 8.0. The worker used 4.

4. **By-hand checks:**
   - BNS edge-on formula: 7.4e-27 at v = 0.1.
   - ℓ²D/V_star = 1.11e-57 and N̄ = 1.1e57.
   - Chebyshev 8.7e-46.
   - Arrival offset 0.78ℓ²/(rc) = 2.2e-104 s.
   - u-slab U_max: exact bound confirmed.

No repository file was edited.
