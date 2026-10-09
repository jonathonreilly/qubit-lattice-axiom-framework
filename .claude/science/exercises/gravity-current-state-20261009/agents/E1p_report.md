# E1′ influence along links: worker report (Claude Opus 5.5, xhigh; 2026-10-09)

Verbatim final report. Referee pending (codex gpt-5.6-sol xhigh); verdicts are not recorded in TESTS.md until it returns. Scripts and text outputs in `scripts/E1p/` (data arrays and the Johnston PDFs are not committed).

All runs are in. Here is the report.

# E1′ report: influence passed along links on records-as-events

**Worker:** Claude Opus 5.5, xhigh effort. **Date:** 2026-10-09. **Setting:** test setting only. The axiom conflicts are the same as E1's: Lattice is replaced, and the causal order is supplied because of A36 and Record's "one record per site".

## Verdicts against the fixed readings

- **Gravity: PASS.** It rests on an exact mean, an exact second-moment formula, and a correlation factor checked to tend to 1. Margin: about 28 orders of magnitude.
- **Matter: M-FAIL (bounded to single-event amplitudes).** M-PASS is excluded outright, because the relative noise is unbounded. If the referee rules that only wavepackets count as "propagation", the matter verdict drops to M-INCONCLUSIVE.
- **Referee needed:** under TESTS.md:9, the M-FAIL needs the codex sol referee before it is reported.

## Plain summary

- **Gravity proxy.** Influence passed only along links behaves as hoped for a massless wave such as a gravitational wave.
  - On average it travels exactly on the light cone and exactly massless, and its law does not see shape changes.
  - In a single realization, the noise is the counting noise of the number of links from the observer into the source, plus small, measured correlations.
  - A neutron-star merger at 1 Gpc gives about 2×10⁻²⁹ relative noise at a single Planck-size event. The arrival-time smearing is about 10⁻¹⁰⁴ s.
  - Nothing grows with distance or with the size of the past, and relays do not compound the noise.
- **Massive matter.** The massive path sum is different, because its mean is built by cancellation.
  - The amplitude between two single events carries a noise floor that does not shrink at any density. It comes from the O(1) number of two-link paths.
  - That noise exceeds the decaying mean beyond about 3 Compton wavelengths.
  - A field from a point-like proton source, read at one event, is noise-dominated beyond about 4 mm.
  - Collimated wavepackets stay coherent over a km, so the matter verdict depends on which object counts as "propagation".

## What I read

- **In full:**
  - `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines);
  - `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (all 3 primitives);
  - the packet's TESTS.md (all 377 lines, including the rules, E1, E1 results and Follow-up 2);
  - `agents/E1_report.md`, `agents/E1_referee.md`, `agents/prior_art_event_history.md`;
  - `scripts/E1/bd_core.py`;
  - block 122 (`docs/ADMISSIBILITY_RULE_WAVES_NEED_SIGNED_WEIGHTS_…_2026-09-24.md`).
- **Prior art (one line).** E1′ is not the 2026-03/04 event era. That era used complex-phase path sums on Euclidean-coordinate random DAGs and collapsed to rank 1. E1′ uses real weights on the links of a Lorentzian Poisson sprinkling, with no coordinates in the law.
- **Block 122 connection.**
  - G₀ = aL has nonnegative weights and no recursion. It is pure light-cone transport, the "rigid transport" exception, and it shows no noise amplification.
  - G_m needs signed weights (b < 0). Every matter failure below comes from the resulting cancellation.
- **Normalisations, verified against the papers (COMPARATOR).** The PDFs are saved as data in `lit_johnston/`.
  - arXiv:0909.0944 eq. (16): 2D, K_R = aC(I−abC)⁻¹ with the causal matrix C, a = 1/2, b = −m²/ρ.
  - arXiv:0909.0944 eq. (17): 4D, K_R = aL(I−abL)⁻¹ with the link matrix L, a = √ρ/(2π√6), b = −m²/ρ.
  - arXiv:0806.3083 derives them: eqs. (3.31), (3.36) and (3.44). Its eq. (3.15) is the exact mean equation, and §3.3 explicitly leaves the fluctuation laws open.
  - Johnston's matrices approximate G pointwise, so the field is φ = ρ⁻¹·K·J.

## Method

All runs at ρ = 1, so ℓ = 1.

- **Massless.**
  - **Exact dependence region (EXACT).** φ(x) depends only on the sprinkling in supp J ∪ ⋃ I(y,x).
  - I sprinkle only that region: x's past link shell (ρV < 24) inside a cylinder toward the source. This is exact up to e⁻²⁴ per point, and it reaches D/ℓ = 10⁵.
  - 2,000–4,000 realizations per configuration, compared with:
    - the exact mean ρ∫e^{−ρV}j (Campbell/Mecke) by quadrature;
    - the exact diagonal variance term (Mecke).
- **Relay.** Two stages on one shared sprinkling: x's shell plus the null slab containing every interval between the relay and source balls.
- **Massive 4D.**
  - Full Poisson diamonds with T/ℓ = 8–23, i.e. N = 540–36,600 elements; 600 to 60 realizations.
  - All links found exactly as maximal elements of each past (checked against brute force).
  - K(top, bottom) and (K·J)(top) by forward substitution, for 12 masses per realization.
- **Analytic machinery.**
  - The exact finite-ρ mean, from Johnston eq. (3.15) as a Volterra equation in proper time.
  - The pair-of-paths Mecke expansion of E[K²]:
    - a shared link counts once, since L² = L;
    - in 4D, interval overlaps between distinct links are omitted (the "overlap-free renewal"), and its accuracy is CHECKED against simulation;
    - in 2D with C there are no emptiness conditions, so the expansion is EXACT.

## Results

### (a) Mean conditions

| Item | Result | Label |
|---|---|---|
| Shape-blindness | A det-one strain maps the order, and hence links and all link-path functionals, to an identical Poisson law (E1). | EXACT |
| Mean of G₀ | E[aL] = a·e^{−πρτ⁴/24}, which tends to δ(τ²)/(2π) (Johnston 3.36) | EXACT |
| Massless in mean | 4πr·G_static(r) = ⟨r/√(r²+σ)⟩ = 0.674, 0.971, 0.992, 0.99992 at r/ℓ = 1, 5, 10, 100: power-law corrections (1 − 0.78ℓ²/r²), no Yukawa factor | EXACT, CHECKED |
| One cone in mean | Support is the past cone, concentrated in τ ≲ ℓ. Link σ = τ² is distributed as e^{−πσ²/24}: ⟨σ⟩ = 1.5594ℓ² exact against 1.5617 measured on 3.2×10⁵ links; sd 1.1781 against 1.1781. Width in time at distance r: 0.78ℓ²/r, tending to 0 like ρ^{−1/2}. Same kernel for every species. | EXACT, CHECKED |
| Mean of G₀J against quadrature | Within 1–2σ in all 17 configurations (D/ℓ = 20 to 10⁵) | CHECKED |
| Exact E[L²(x,y)] → 3π | 8.95, 9.22, 9.32, 9.37, 9.41 at τ/ℓ = 8, 12, 17, 23, 40; simulation 9.09, 9.14, 9.08, 9.43, 8.7 ± 0.4 | EXACT, CHECKED |
| Mean of G_m, exact finite ρ, against −(m/4πτ)J₁(mτ) | See the table below | CHECKED |
| Simulated means against the exact finite-ρ mean | Agree within standard errors at T = 8–23 | CHECKED |

Mean of G_m (exact finite-ρ solution) against the continuum Bessel form, for mτ from 2 up to 20 (14 at mℓ = 0.7):

| mℓ | Max deviation / Bessel envelope | Fitted M/m − 1 | Fitted amplitude Z |
|---|---|---|---|
| 0.05 | 0.07 | +0.003 | 1.03 |
| 0.1 | 0.25 | +0.008 | 1.11 |
| 0.2 | 0.72 | +0.017 | 1.40 |
| 0.4 | 3.8 | — | — |
| 0.7 | 22 | — | — |

- The mean converges to the continuum Bessel tail as mℓ → 0.
- At fixed mℓ it has a slow growing mode at about 0.6·m³ℓ², CHECKED for mℓ = 0.1–0.4. For the proton this means one e-fold per 6×10²² m.

### (b) Massless noise (graviton proxy)

**Law (controlled):**

Var/mean² = (1 + κ·s/D)/N̄, with N̄ = ρ∫_src j e^{−ρV} ≈ √6·V_s/(2Dℓ²) for D ≫ s.

- The mean and the diagonal term are EXACT (Mecke).
- The structure F − 1 ∝ s/D is ARGUED: link–link correlations come from intervals along the line of sight within about ℓ transversely.
- κ ≈ 4–6 is CHECKED, with a weak rise from s/ℓ = 6 to 24.

| s/ℓ | D/ℓ | s/D | N̄ (quadrature) | Fano F (± se) |
|---|---|---|---|---|
| 6 | 20 | 0.3 | 55.3 | 2.04 ± 0.07 |
| 12 | 40 | 0.3 | 221.5 | 2.30 ± 0.09 |
| 24 | 80 | 0.3 | 886 | 2.45 ± 0.13 |
| 6 | 60 | 0.1 | 18.5 | 1.38 ± 0.04 |
| 12 | 120 | 0.1 | 73.9 | 1.49 ± 0.06 |
| 24 | 240 | 0.1 | 295.5 | 1.56 ± 0.08 |
| 6 | 600 | 0.01 | 1.85 | 1.02 ± 0.03 |
| 12 | 1200 | 0.01 | 7.39 | 1.09 ± 0.04 |
| 24 | 2400 | 0.01 | 29.6 | 1.06 ± 0.04 |
| 12 | 12000 | 0.001 | 0.74 | 1.02 ± 0.04 |
| 24 | 24000 | 0.001 | 2.96 | 0.98 ± 0.03 |
| 24 | 100000 | 0.00024 | 0.71 | 1.02 ± 0.04 |

- **Per-realization relative noise.** The sd/mean of each realization equals √(F/N̄) to within 1–4% in every row.
- **Gaussian (smooth) sources.** Var/diag tracks F, at 0.94–2.49.
- **Duration** (s = 12, D = 1200, source on for duration T_s = 1, 4, 12, ∞):
  - N̄ = 0.46, 1.83, 5.08, 7.39;
  - F = 1.00, 0.98, 1.04, 1.09;
  - so noise² scales as D/(s²·min(T_s, ~2s)) (CHECKED).
- **Density.** At fixed physical D and s, the relative noise scales as ρ^{−1/4}.
- **Past beyond the source.** EXACT: there is no dependence on the sprinkling outside supp J ∪ ⋃I(y,x). Links into empty regions contribute exactly zero.
- **Relay compounding** (two stages, exact shared sprinkling):

| s/ℓ, D₀/ℓ, D₁/ℓ | Measured relative variance | No-compounding law F₁/N₁ + F₀/(N₁N₀) | Last stage alone |
|---|---|---|---|
| 6, 60, 60 | 0.0830 | 0.0807 | 0.0765 |
| 8, 400, 400 | 0.2125 | 0.2014 | 0.1762 |
| 6, 300, 40 | 0.0679 | 0.0638 | 0.0530 |
| 6, 40, 300 | 0.3014 | 0.3019 | 0.2869 |
| 12, 600, 600 | 0.0784 | 0.0793 | 0.0744 |

  - k = 2 is CHECKED.
  - For k stages (ARGUED): the variances add, each earlier stage is suppressed by the later link counts, and the last leg dominates. There is no compounding.
- **2D control.** Johnston's 2D K₀ = C/2 is a Poisson sum with deterministic weights. Var = (1/4ρ)∫_{J⁻(x)} j² exactly, with no correlations (EXACT).

### (c) Massive noise (matter)

**Point-to-point G_m(x,y)**

- **Laws:**
  - EXACT: as m → 0, Var K/E[K]² → Var L²/E[L²]².
  - EXACT: E[L²] → 3π.
  - CHECKED: the measured Var L² gives Fano factors 1.27, 1.17, 1.08, 1.08, 1.11, 0.95.
- **So the floor is:** sd(K) = a²m²√(Var L²), which does not depend on ρ. Against the mean envelope this is sd/envelope = 0.204·√F·(mτ)^{3/2}.

| τ/ℓ (realizations) | rel. noise at mτ = 0.25 | sd/envelope at mτ = 3 | sd/envelope at mτ = 5 | sd/envelope at mτ = 8 | Simulated / overlap-free renewal, mτ ≤ 12 |
|---|---|---|---|---|---|
| 8 (600) | 0.363 | 1.13 | 2.87 | 9.5 | 1.12–1.65 |
| 11 (500) | 0.349 | 1.11 | 2.66 | 7.5 | 1.07–1.59 |
| 14 (400) | 0.339 | 1.07 | 2.41 | 6.2 | 0.98–1.27 |
| 17 (250) | 0.334 | 1.05 | 2.32 | 5.4 | 0.93–1.36 |
| 20 (120) | 0.345 | 1.10 | 2.37 | 5.3 | 1.00–1.20 |
| 23 (60) | 0.308 | 0.97 | 2.13 | 4.9 | 0.83–0.97 |
| Floor law, F = 1 | 0.326 | 1.06 | 2.28 | — | — |

- **Floor dominance.** The floor accounts for the whole variance up to mτ ≈ 6 at τ/ℓ ≥ 14. Above that, the first-order end seeds plus higher merges add.
- **Seed law.** In the continuum limit of the first-order end seed (EXACT evaluation), per end: Var/envelope² = (√6/96)·(mℓ)²(mτ)³.
- **Noise exceeds the mean envelope at mτ ≈ 2.9 at every density.** This needs no extrapolation in ρ.

**G_m·J, single-event read-out**

- **Smeared source (Gaussian, w = 1.5ℓ).**
  - The two-link floor is smoothed: relative noise at small mτ is 0.124, 0.100, 0.084, 0.087 at τ/ℓ = 14, 17, 20, 23.
  - At larger mτ the noise is 0.3–1.2 relative, but there mℓ = 0.3–0.7.
  - The point-source seed estimate overpredicts these by 3–5×, because mw ≈ 0.5–1 is not compact.
  - So the compact-source law, valid for ℓ ≪ s ≪ 1/m, is CHECKED only through the exact point-source decomposition. Applying it to smooth compact sources is ARGUED.
- **Packets (σ ≫ 1/m).** ARGUED: the first-order law gives Var/mean² ≈ (√6/24π)·(m²ℓσ)².

**Exponential growth, and in which variable**

| Case | Growth | Label |
|---|---|---|
| 2D control (Johnston's C form) | Exact Volterra law, simulation/exact sd ratio 0.95–1.11 including the noise ≫ mean regime. Rate γ = m³ℓ²/4 (fitted/predicted 1.12, 1.07, 1.03, 1.00 as γτ = 5.6 → 27). Variable m³ℓ²τ, with ℓ = ρ^{−1/2}. | EXACT law, CHECKED |
| 4D variance (overlap-free renewal, shared-link kernel) | The variance obeys a tachyonic Klein–Gordon-type law at rate 0.255·m²ℓ. Variable m²ℓτ. The onset at x = 0.5 (+3% predicted against +4.5% computed) agrees. The asymptotic rate was not reached within budget: my first coarse-grid attempt gave a quadrature artifact, now documented, and I stopped the refined run. | ARGUED |
| 4D mean | Slow growth at about 0.6·m³ℓ² | CHECKED for mℓ = 0.1–0.4 |
| 4D point-to-point floor | Power law (mτ)^{3/2} in mτ, not exponential | CHECKED |

### (d) Translation (ℓ = ℓ_P)

| Quantity | Value | Bound | Outcome |
|---|---|---|---|
| GW relative amplitude or phase noise, BNS (two 12-km stars), 1 Gpc, one event | 2.1×10⁻²⁹; about 2×10⁻²⁸ with a 10× quadrupole suppression | ≪ 1 | PASS by about 28 orders |
| Same at 40 Mpc | 4×10⁻³⁰ | ≪ 1 | PASS |
| Incoherent (scattered) power fraction | about Var/mean² ≈ 10⁻⁵⁷ (ARGUED identification) | — | negligible |
| Arrival offset and spread, 1 Gpc | 2.2×10⁻¹⁰⁴ s and 1.7×10⁻¹⁰⁴ s; fractional speed offset 2×10⁻¹²¹ | \|c_g − c\|/c ≲ 10⁻¹⁵ | PASS |
| Correlation correction κ·s/D | 2×10⁻²⁰ | — | negligible |
| Graviton mass | 0 in mean (EXACT) | any | PASS |
| Locality | ℓ_P ≪ 10⁻¹⁹ m. Past links per event over c·t₀: √6π(T/ℓ)² = 5×10¹²² (BHS-type unbounded valency). These do not enter source-driven fields. Mean-kernel deviation from G_R at 10⁻¹⁹ m: 2×10⁻³². | ℓ ≤ 10⁻¹⁹ m | PASS |
| Electron: point-to-point incoherent beyond | mτ > 2.89, i.e. 1.1×10⁻¹² m | 1 km | fails |
| Electron: compact-source G_m·J, noise = mean | 0.86 / 1.09 / 1.22 km (two ends / one end / conservative: first-chaos, one end) | 1 km | borderline |
| Electron: packet of 1 km | Var/mean² = 4×10⁻¹⁶ | 1 km | coherent |
| Electron: renewal e-fold of the variance | 3.6×10¹⁰ m | — | — |
| Proton: point-to-point incoherent beyond | 6×10⁻¹⁶ m | 1 km | fails |
| Proton: compact-source G_m·J, noise = mean | 3.1 / 4.0 / 4.4 mm | 1 km | fails |
| Proton: packet of 1 km | Var/mean² = 4×10⁻³ | 1 km | coherent |
| Proton: renewal e-fold of the variance | 10.7 km (factor 1.10 at 1 km) | — | — |

In the compact-source rows, τ is proper time. A proton needs γ > 2.5×10⁵ for 1 km of travel to stay under 4 mm of proper time.

## Verdicts, in detail

**Gravity: PASS.**
- (a) holds: shape-blind in law, mean G₀ is the retarded Green function, one cone, massless in mean. The mean of G_m converges to the continuum as mℓ → 0.
- The massless noise law Var/mean² = (1 + κs/D)/N̄ is established by the exact Mecke mean and second moment plus checked correlations, with F → 1 at s/D ≤ 10⁻² for D/ℓ = 20 to 10⁵.
- At ℓ = ℓ_P it gives about 2×10⁻²⁹, many orders inside every GW bound.
- No fitted exponent is extrapolated. Only κ's weak s/ℓ trend extends beyond the tested range, and the PASS survives unless F − 1 grew faster than (s/ℓ)². The data show far less: +30% and +14% per doubling of s.
- Scope:
  - a scalar link field as GW proxy;
  - the tensor structure and nonlinearity are not tested;
  - E1's strain "crackle" is not addressed;
  - the axiom conflicts stand.

**Matter: M-FAIL (bounded).**
- Controlled law: the two-link floor. The mean is EXACT (3π), the variance CHECKED, and the floor does not depend on ρ.
- The element-to-element G_m loses coherence at mτ ≈ 3 at every density. For the electron that is 10⁻¹² m.
- For a point-like source read at one event, the proton loses coherence at 3–4.4 mm by the seed law. That law is checked with exact point sources and its continuum constant is exact.
- M-PASS is excluded regardless: the relative noise is unbounded, growing as a power law (mτ)^{3/2}, with the 4D renewal growth argued and the mean's growth checked.
- **Bound on the verdict:** it rests on single-event amplitudes. Wavepacket sources stay coherent at 1 km by the same first-order law. If the referee rules that only packets count, the verdict is M-INCONCLUSIVE.

## What a referee should re-check

1. Whether single-event G_m and compact-source G_m·J are the right objects for "propagation coherent". The fallback is M-INCONCLUSIVE.
2. The first-chaos lower-bound argument (ARGUED): blocking by an added point spreads along the null generator over a radial factor of a few, so E[D_zK] ≈ ab·e^{−ρV}K̄.
3. κ's s/ℓ dependence, and the needle-overlap decay V₁₂ ∝ Δb⁻⁴ that underlies the s/D structure.
4. The 4D renewal's asymptotic rate of 0.255·m²ℓ. The overlap-free equation itself checks to within 0.83–1.65 of simulation at τ/ℓ ≤ 23, but the rate was not reached numerically.
5. The mean's growing mode (about 0.6·m³ℓ²): whether it is a complex pole of 1 + m²aμ̃.
6. The large-D massless run: the first D = 10⁵ result was invalid (a cancellation bug, quarantined) and was rerun with a stable formula.
7. Var L² Fano factors at τ/ℓ > 23.

## Files

Everything is under `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/ex_grav/E1p/`.

- **`scripts/`:**
  - `e1p_core.py`
  - `E1p_0_mean_massless.py`
  - `E1p_1_massless_needle.py`
  - `E1p_1b_massless_summary.py`
  - `E1p_2_relay.py`
  - `E1p_3_massive4d.py`
  - `E1p_3b_analyse4d.py`
  - `E1p_4_massive2d.py`
  - `E1p_4b_exact2d_growth.py`
  - `E1p_4c_2d_sim_vs_exact.py`
  - `E1p_5_mean4d.py`
  - `E1p_5b_meanfit.py`
  - `E1p_6_renewal4d.py`
  - `E1p_6b_renewal_rate.py`
  - `E1p_6c_KJ_seed.py`
  - `E1p_7_translate.py`
  - tests: `test_core.py`, `test2d.py`, `dbg_rate.py`
- **`out/`:**
  - matching `.out` and `.log` files;
  - realization arrays `massless_[AB]_*.npz`, `massive4d_T*.npz`, `relay_*.npz`;
  - exact means `mean4d_ml*.npz`;
  - `INVALID_cancellation_bug_massless_A_D100000_s24.npz`, quarantined; do not use.
- **`lit_johnston/`:** `johnston_0806.3083.pdf/.txt`, `johnston_0909.0944.pdf/.txt` (data only).
- **No repository file was edited.**