# C3 lane X1: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. Codex sol referee: pending if the verdict is a FAIL or no-go.

**Verdict (worker):** FAIL (bounded to the tested implementation). Every direct nonzero-k TT stiffness spectrum is flat (white) and at or above 1e-3, for both kernels and for the fermion seas. K1 scalar (B1 c5's setting): S_TT ≈ 3.6e-3 from qR = 0.18 to 1.41. K2 scalar: about 2.1e-3 to 2.6e-3. Spinless fermion sea: 7.1e-2 on K1 and 3.8e-2 on K2. Frame-sensitive Dirac sea on K1: 1.4e-2. The verdict is the same whether S is read as a power or as an amplitude, so it is decisive under the pre-registered rule. The PASS bar of 5e-11 is missed by at least 7.6 decades. A FAIL needs the codex sol referee.

**Plain summary:** I put a scalar field and two kinds of fermion sea on a random 4D point set, which has no repeating pattern and no shear stiffness on average. I then measured how the vacuum's resistance to shear varies from patch to patch, and computed the spectrum of that variation directly at nonzero wavevector. The referee had asked for this in place of B1 c5's whole-box total. The spectrum is flat (white) in every case tested: two coupling kernels, a scalar, a spinless fermion sea, a Dirac sea coupled to the local frame, and both random and fixed point counts. It stays flat from the coupling range out to the longest wavelengths reached, at 2e-3 to 8e-2 per site, which is at least 7.6 decades above the pass bar of 5e-11. A second calculation that never splits the stiffness into patches (the response to real long strain waves) gives the same spectrum to within 0.1-4%. B1 c5's box total also equals the nonzero-k level, so its estimator was not misleading. Against the fixed reading this is a FAIL, bounded to this implementation (a frozen Euclidean Poisson set, free fields, two smooth kernels, up to about 4100 points), and it goes to the codex sol referee.

# X1: TT stiffness noise spectra at nonzero k on a 4D random lattice (Campaign C3, lane X)

- **Worker:** Claude Opus 5.5, max effort. Ran 2026-10-10 from 00:51Z to about 02:00Z.
- **Pre-registration:** `PREREG.md`, stamped `Sat Oct 10 00:56:09 UTC 2026`, written before any X1 computation.
- **Status: test setting only.**
  - A 4D Euclidean Poisson point set replaces Lattice's Z³.
  - No axiom or registered primitive is used as a premise. I checked the registry: scale reference, kinetic isotropy and realized state are not invoked.
  - Nothing here is a framework claim.
- **Referee:** the codex sol referee is required, because the verdict is a FAIL.

## Verdict against the fixed reading (TESTS.md, Campaign C3, X1, unchanged)

**FAIL, bounded to the tested implementation (CHECKED).** Every direct nonzero-k TT stiffness spectrum is flat and at or above 1e-3, for both kernels and for the fermions.

| Matter, kernel | S_TT in the window qR ≤ 1.5 (power) | √S (amplitude) | low-q log-slope p | smallest qR reached |
|---|---|---|---|---|
| Scalar S0 (B1 c5's functional), K1 (c5's kernel) | 3.6e-3 | 0.060 | −0.03 ± 0.08 (8 points) | 0.18 |
| Scalar S0, K2 (second kernel) | 2.1e-3 (rod 5³×24, 42 realizations); 2.6e-3 (rod 5³×32, 9 realizations) | 0.046; 0.051 | +0.18 ± 0.22; −0.58 ± 0.42 | 0.47 |
| Spinless fermion sea F1, K1 | 7.1e-2 | 0.27 | −0.03 ± 0.07 | 0.18 |
| Spinless fermion sea F1, K2 | 3.8e-2; 4.1e-2 | 0.19; 0.20 | −0.20 ± 0.21; −0.08 ± 0.48 | 0.47 |
| Frame-sensitive Dirac sea F2 (vierbein), K1 | 1.4e-2 | 0.12 | +0.13 ± 0.19 | 0.47 |

- **PASS** needs S_TT(k → 0) → 0, or ≤ 5e-11.
  - No case falls toward small q. No slope reaches p ≥ 1, and no spectrum drops by 4× across its window.
  - The smallest level, K2 scalar at 2.1e-3, misses 5e-11 by 7.6 decades as a power and by 9.0 decades as an amplitude (arithmetic).
- **FAIL** needs "flat and ≥ 1e-3 in the direct k-spectra, for both kernels and for the fermion."
  - Every case meets it, whether S is read as a power or as an amplitude.
  - So the verdict is decisive under the pre-registered rule.

## 1. What I read (in full, nothing truncated)

- **Foundations:**
  - `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines);
  - `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`.
- **Packet:**
  - `TESTS.md`: the rules, every section, and Campaign C3 with X1's fixed readings;
  - `SUMMARY.md`: all of it.
- **The referee's request and its context:**
  - `agents/B_referee.md`: item 6, "a total box stiffness estimator, not a direct measurement of the nonzero-k structure factor", and ranked test 3;
  - `agents/B1_report.md` §2.9: c5, plus c3's A ≲ 5e-11 LIGO bar, which is the source of the PASS threshold.
- **Code:**
  - `scripts/B1/B1_c5_euclid4d_noise.py` and `B1_c5b_euclid4d_noise_more.py`, with their `.out` files;
  - `scripts/E23/e23_core.py`.

## 2. Setting and hypotheses

- **H1. Substrate.**
  - A quenched 4D Euclidean Poisson set of density 1 in periodic boxes, which is O(4)/SL(4)-invariant in law.
  - **Cubes:** L⁴ with L = 4–7, as in c5.
  - **Rods:** Lp³ × Lz with Lp = 4 or 5 and Lz = 12–64. A rod reaches small nonzero q = 2πm/Lz along e3 at an affordable N (≤ 4200).
  - **Ensembles:** Poisson-N, and fixed-N (binomial).
- **H2. Kernels.** Weights are set on pairs chosen by current proper distance, with s = DᵀgD and g = exp(t h). Both kernels have w, w′ and w″ → 0 at the cutoff, so no pair-switching terms appear.
  - **K1** (c5): w = (1 − s/R²)⁴, R = 1.8.
  - **K2:** w = exp(−s/2σ²)(1 − s/Rc²)⁴, σ = 0.8, Rc = 2.4.
- **H3. Matter (free fields, vacuum functionals).**
  - **S0:** Σ½√(λ+1), c5's functional. It is the zero-point energy of a 4+1 Hamiltonian living on the 4D set.
  - **S1 (secondary):** ½Tr log(L+1), the 4D Euclidean scalar effective action.
  - **F1:** the spinless sea of H = L_g, −TΣlog(1+e^{−(λ−μ)/T}), following the packet's E23 convention.
  - **F2:** −log det(D + 1) = −Tr log(B†B + 1) for a naive Euclidean Dirac operator. D = Σ w(s) γ·d (|I⟩⟨J| − |J⟩⟨I|), with d = e·D and vierbein e = exp(t h/2). Through the vierbein, F2 is frame-sensitive.
- **H4. TT channel.** The constant traceless strains are h1 = diag(1,−1,0,0)/√2 (E-type) and h2 = (e0e1 + e1e0)/√2 (T-type). Wavevectors q run along e3, so they are transverse to both strains. The cubes also give the in-plane q.
- **H5. Units.** Per-site stiffness in lattice units, with tr h² = 1 and density 1. These are c5's units, so white noise of per-site amplitude a gives S = a², and c5's sd·√N = 0.06 corresponds to S = 3.6e-3.

## 3. Method

1. **Exact local density.**
   - The second derivative is E″ = Tr(f′(L)L₂) + Tr(L₁Φ), with Φ = V(F∘A₁)Vᵀ (Daleckii–Krein) and A₁ = VᵀL₁V.
   - The local density is κ_i = Σ_j [f′(L)_ij(L₂)_ij + Φ_ij(L₁)_ij]. Then Σκ_i = E″ (EXACT).
   - Any other local decomposition differs by a lattice divergence, which changes S only at O(q²) (ARGUED). Check 3 confirms this.
2. **Direct spectrum.**
   - Per realization, S(q) = (1/N)|Σ_i κ_i e^{−iq·x_i}|².
   - It is averaged over realizations, with h1 and h2 pooled (they are equivalent in law). Errors are the spread over realizations and directions.
3. **Decomposition-free k-resolved response.**
   - The strain field is t·φ_a(z)·h, with φ_a = cos or sin of k_m z, k_m = 2πm/Lz and m = 1, 2, 3. It is coupled through each pair's midpoint.
   - The exact bilinear response E_ab gives the amplitudes at k1 ± k2 without any local decomposition:
     - E_c1c2 ∓ E_s1s2 give Re κ̃(k1 ± k2);
     - −(E_s1c2 + E_c1s2) gives Im κ̃(k1 + k2);
     - E_c1s2 − E_s1c2 gives Im κ̃(k1 − k2).
   - These identities are EXACT for a local density; the corrections are O(k²) (ARGUED).
   - E_ab is the graviton–graviton scattering kernel Π(k1, k2) of the induced quadratic action.
4. **Windowed check, real space, within each realization.** Sum κ over slabs of length ℓ, then take V(ℓ) = Var over slabs / ⟨N_slab⟩. Flat V(ℓ) means white noise; V falling with ℓ would mean hyperuniform noise.
5. **The q = 0 box estimator,** exactly as in c5: sd(E″/N)·√N.
6. **Fixed-N against Poisson-N,** at q ≠ 0 and at q = 0.

## 4. Validation (CHECKED)

Outputs are in `out/validate.out` and `out/dirac_validate.out`.

- **Exact identity.** Σκ_i equals the eigenbasis total to about 1e-8 relative.
- **Finite differences.** Analytic E″ matches central finite differences, with pairs recomputed in proper distance, to 4e-7 – 1.6e-5 relative. This holds for S0 and F1 on K1 and K2.
- **Agreement with the packet's code.** `x1_core` reproduces the packet's `e23_core.derivs` (c5's code path) to every printed digit.
- **k-resolved response.** E_aa, and a polarization combination, match finite differences of the energy under a modulated metric to about 1e-6.
- **Dirac.**
  - The sparse block assembly matches an explicit loop.
  - b(v)†b(v) = |v|² holds.
  - Σκ equals the eigenbasis total.
  - Finite differences agree to about 5e-6.

## 5. Results

### 5.1 K1 scalar S0: the TT channel along the rod (q ∥ e3), S in units of 1e-3

**Rod 4³×64, Poisson, 20 realizations:**

| q | 0.098 | 0.196 | 0.295 | 0.393 | 0.491 | 0.589 | 0.687 | 0.785 |
|---|---|---|---|---|---|---|---|---|
| qR | 0.18 | 0.35 | 0.53 | 0.71 | 0.88 | 1.06 | 1.24 | 1.41 |
| S (×1e-3) | 3.64±0.47 | 4.36±0.86 | 2.95±0.37 | 4.06±0.73 | 3.10±0.49 | 2.90±0.45 | 3.72±0.56 | 3.94±0.67 |

The slope is −0.03 ± 0.08 and S(q_min)/median = 0.99.

**Other rods (q = 0.196, 0.393, 0.589, 0.785 unless stated):**
- **Rod 4³×32, Poisson, 90 realizations:** 3.66, 4.10, 3.53, 3.37 (each about ±0.3); p = −0.06 ± 0.08.
- **Rod 4³×32, fixed-N, 90 realizations:** 3.60, 3.75, 3.87, 3.56; p = +0.01 ± 0.07.
- **Wider rod 5³×24, Poisson, 14 realizations** (q = 0.262, 0.524, 0.785): 4.96, 3.86, 4.05; p = −0.18 ± 0.22.
- **S1 (Euclidean log det, secondary), rod 4³×32, 30 realizations:** 3.20, 4.00, 3.32, 3.34; p = +0.01 ± 0.13.

**Over the full axis range** (up to qR = 5.65) the spectrum stays flat, falling mildly at the largest q. The per-realization ratio S(low-q window)/S(qR 3–6) is 1.1–1.3.

### 5.2 K2 scalar S0 (S in units of 1e-3)

- **Rod 5³×24, Poisson, 42 realizations:** q = 0.262 and 0.524 give 1.94±0.22 and 2.20±0.23; p = +0.18 ± 0.22.
- **Rod 5³×24, fixed-N, 14 realizations:** 2.02 and 2.28; p = +0.18 ± 0.39.
- **Rod 5³×32, Poisson, 9 realizations:** q = 0.196, 0.393, 0.589 give 3.66, 1.73, 2.33; p = −0.58 ± 0.42; ratio 1.57.
  - This is flat only through the pre-registered 2σ clause, on a noisy 3-point window.
- **Cubes:** S(2π/L) in the TT channel is 2.1e-3 at L = 5 and 1.9e-3 at L = 6.
- **Lowest values seen:** the per-direction values stay at or above 1.7e-3 in the windows with 42 realizations. The lowest single point is h1 at q = 0.393 in the 9-realization rod, 9.6e-4, which is noise-dominated.

### 5.3 Fermion seas (S in units of 1e-2)

**F1 on K1** (one shared μ = 3.6164, T = 0.2892):
- **Rod 4³×64, Poisson, 20 realizations:** window mean 7.11; the 8 points lie in 5.7–7.6; p = −0.03 ± 0.07.
- **Rod 4³×32, Poisson, 90 realizations:** 8.41, 7.68, 6.80, 8.04; p = −0.08 ± 0.09.
- **Rod 4³×32, fixed-N with the shared pilot, 30 realizations:** 7.09, 7.04, 6.82, 7.23; p = 0.00 ± 0.12.
- **Wider rod 5³×24, 14 realizations:** 8.06, 6.39, 7.69.

**F1 on K2** (μ = 3.7161, T = 0.2653):
- **Rod 5³×24, Poisson, 42 realizations:** 4.02, 3.49; p = −0.20 ± 0.21.
- **Rod 5³×24, fixed-N, 14 realizations:** 2.96, 4.58; p = +0.63 ± 0.40. This passes "flat" only through the 2σ clause.
- **Rod 5³×32, 9 realizations:** 4.95, 2.87, 4.40.

**F2, the Dirac sea on K1:**
- **Rod 4³×24, Poisson, 22 realizations:** q = 0.262, 0.524, 0.785 give 1.28±0.19, 1.60±0.25, 1.44±0.21; p = +0.13 ± 0.19.
- **Rod 4³×24, fixed-N, 12 realizations:** 1.31, 1.08, 1.03; p = −0.21 ± 0.32.
- **Rod 5³×12, 12 realizations:** 1.36 at q = 0.524.
- **Cubes, TT channel at q = 2π/L:** 1.36 and 1.40 (L = 4, Poisson and fixed), 1.49 (L = 5), 1.67 (L = 6).

### 5.4 The decomposition-free response against the density spectrum (h1)

Each row gives the ratio S_resp/S_dens at q = 0.196·j, with j = 1–6 on the K1 rods and q = 0.262·j on the K2 rod. The last column is the per-realization correlation of the complex amplitudes.

| Case | j=1 | 2 | 3 | 4 | 5 | 6 | correlation |
|---|---|---|---|---|---|---|---|
| K1 S0, rod 4³×32 Poisson (90 realizations) | 1.001 | 1.003 | 1.004 | 1.010 | 1.019 | 1.027 | ≥ 0.999 |
| K1 S0, fixed-N (90 realizations) | 1.000 | 1.002 | 1.005 | 1.010 | 1.016 | 1.029 | ≥ 0.999 |
| K2 S0, rod 5³×24 (42 realizations) | 1.001 | 1.003 | 1.012 | 1.019 | 1.035 | 1.040 | ≥ 0.997 |
| F1 on K1 (90 realizations) | 1.000 | 1.003 | 1.001 | 1.003 | 1.010 | 1.012 | ≥ 0.995 |
| F1 on K2 (42 realizations) | 0.999 | 1.000 | 0.995 | 1.011 | 1.004 | 1.009 | ≥ 0.985 |
| S1, rod 4³×32 (30 realizations) | 0.999 | 1.001 | 1.004 | 1.011 | 1.016 | 1.027 | ≥ 0.999 |

For example, the raw K1 values at q = 0.196 are 3.549e-3 by response and 3.544e-3 by density. The deviation grows like q², as expected for nonlocal corrections. **So the repaired estimator is independent of how the stiffness is split into patches (CHECKED).**

### 5.5 Windowed real-space noise, per realization then averaged: V(ℓ)

- **K1 S0, rod 4³×64,** at ℓ = 1, 2, 4, 8, 16, 32: 3.21, 3.40, 3.42, 3.50, 3.96, 3.66 (×1e-3).
- **K2 S0, rod 5³×24,** at ℓ = 1.5, 3, 6, 12: 1.96, 2.10, 2.09, 2.05 (×1e-3).
- **F1 on K1, rod 4³×64:** 6.68, 6.95, 6.96, 7.06, 7.42, 8.65 (×1e-2).
- **F1 on K2:** 3.58, 3.76, 3.74, 4.27 (×1e-2).
- **F2, rod 4³×24:** 1.50, 1.42, 1.40, 1.63 (×1e-2).
- **S1:** 2.98, 3.23, 3.32, 3.69, 3.54 (×1e-3).

V(ℓ) does not fall as ℓ grows in any case, so the noise is white per realization (CHECKED).

### 5.6 Noise per realization

Each realization's own low-q window mean S:

| Case | Range | At or above 1e-3 |
|---|---|---|
| K1 S0, rod 4³×64 | 1.86e-3 – 5.69e-3 | 20 of 20 |
| K1 S0, rod 4³×32 | 1.08e-3 – 7.47e-3 | 90 of 90 |
| K2 S0 | 4.1e-4 – 4.95e-3 | only 4 samples per realization |
| F1 on K1 | 3.3e-2 – 1.15e-1 | all |
| F2 | 4.4e-3 – 2.8e-2 | all |

- The ratio of the observed realization-to-realization scatter to the χ² expectation for independent Gaussian white samples is 0.79–1.19 in every case.
- **So no realization is quiet.** The spread is exactly the sampling noise of white noise (CHECKED).
- The table is `out/perreal_final.out`.

### 5.7 Fixed-N against Poisson-N

Each row gives the S level in the q ≠ 0 window, then S_box(0) for h1 and h2.

| Case | Window S: Poisson / fixed | S_box(0): Poisson (h1, h2) | S_box(0): fixed (h1, h2) |
|---|---|---|---|
| K1 S0, rod 4³×32 | 3.66e-3 / 3.70e-3 | 4.2e-3, 2.6e-3 | 4.4e-3, 3.4e-3 |
| K2 S0, rod 5³×24 | 2.07e-3 / 2.15e-3 | 1.5e-3, 2.4e-3 | 2.0e-3, 1.3e-3 |
| F1 on K1, shared μ and T | 7.73e-2 / 7.05e-2 (1.6σ) | 9.9e-2, 6.9e-2 | 1.15e-1, 8.1e-2 |
| F1 on K2 | 3.75e-2 / 3.77e-2 | — | — |
| F2 | 1.44e-2 / 1.14e-2 | 1.2e-2, 1.4e-2 | 4.2e-2, 1.3e-2 (12 realizations) |

- **K1 cubes, sd·√N:** Poisson 0.051–0.073 and fixed-N 0.059–0.069, for L = 4–7. This matches c5's 0.043–0.079.
- **Isotropy:** S(2π/L) is 2.6–4.7e-3 in the TT channel and 3.2–4.1e-3 in-plane.
- **Conclusion:**
  - The two ensembles agree at q ≠ 0 and at q = 0, so there is no zero-frequency atom.
  - The c5 whole-box total equals the nonzero-k level. Item 6's estimator concern is resolved for this implementation (CHECKED).

### 5.8 Side observations (not part of the reading)

- **Scalar means vanish.** The mean per-site TT stiffness is consistent with 0, for example −0.00006 ± 0.00020 on the K1 rod 4³×64. The mean diagonal response at k = 0.196 is −0.00009 ± 0.00015, so there is no mean mass (CHECKED; as in c5).
- **The Dirac E-type mean is a finite-size effect.**
  - At box width 4 it is nonzero: +0.0034 ± 0.0006 on the rod, and +0.0024 ± 0.0010 and +0.0030 ± 0.0011 on the cubes.
  - At width 5 it is consistent with zero: +0.0004 ± 0.0006 on the cube and +0.0003 ± 0.0005 on the rod. At width 6, from 8 realizations, it is −0.0014 ± 0.0010.
  - So it comes from the periodic torus (CHECKED), and it vanishes in infinite volume by SL(4) invariance of the law (EXACT, given H1).
  - The Dirac noise level is unchanged by width.

## 6. Scope: what this does and does not establish

- **Established (CHECKED), for this implementation.** In a frozen 4D Euclidean Poisson set with these kernels and free functionals, the local TT stiffness is white noise. Its level is 2e-3 to 8e-2 per site, and it holds from the coupling range down to qR = 0.18 (K1) or 0.47 (K2 and F2), with no sign of falling as k → 0.
- **Not established:**
  - other finite-valency constructions: Delaunay or Voronoi (Christ–Friedberg–Lee) weights, k-nearest-neighbour graphs;
  - relaxed (force-balanced), hyperuniform, annealed or dynamical substrates;
  - Lorentzian sprinklings;
  - interacting fields;
  - wavelengths beyond the measured window, since no extrapolation was made.
- **Not attempted:** the translation into physical graviton noise, which needs a self-energy map (B1 c3's toy and the B referee's caveat).

## 7. Deviations from the pre-registration (all logged)

1. **Fermion pilot.**
   - At first each run drew its own pilot. As a result, the K1 4³×32 fixed-N run used μ = 3.399, T = 0.279. It is reported separately: S = 6.4e-2, flat.
   - From 01:08Z there was one shared pilot per kernel, and a clean fixed-N run (`K1_rod32_Fshared`) was added.
2. **Secondary functional.** S1 was added at 01:15Z. It is not used in the verdict.
3. **Shared CPU (load average up to 28).** The first launch was aborted; its partial files are in `out/aborted/` and are not used. Run sizes were cut:
   - the K1 4³×64 fixed-N run stopped at 2 realizations;
   - the K1 4³×64 Poisson run was capped at 20;
   - one K2 run was capped at 14;
   - F2 was run on K1 only.
4. **Added after a nonzero mean appeared:** the Dirac finite-size check (cubes L = 5–6, rod of width 5).
5. **Midpoint coupling** was my choice for the k-resolved strain. Any local rule differs only at O(k).

## 8. What a referee should re-check

1. **Validation.** Re-run `x1_validate.py` and `x1_dirac.py validate`: the exact identity, the finite differences, and agreement with `e23_core`.
2. **The k-resolved identities and table 5.4.** This is the decomposition-free core of the estimator repair.
3. **Normalisation.** Check that S = (1/N)|Σκe^{−iqx}|² equals c5's (sd·√N)², and that the 1e-3 and 5e-11 bars hold whether S is read as a power or as an amplitude.
4. **Rod width.**
   - Width 4 for K1 and 5 for K2, against kernel ranges of 1.8 and 2.4.
   - Levels at width 5 and in cubes agree within about 20%: 4.3e-3 against 3.6e-3 for K1 S0.
5. **The "flat" rule on the 2–3-point windows** for K2 and F2. Two noisy windows pass "flat" only through the 2σ clause: K2 rod 5³×32 and F1 on K2 with fixed-N.
6. **The fermion parameters.** F1 and S0 are Hamiltonian objects (4+1 dimensions) living on the 4D set, as in c5 and E23. S1 and F2 are the 4D Euclidean objects.
7. **The naive Dirac operator.** B†B has near-zero modes (about 1e-8), no doubler analysis was done, and m² = 1. Is "the fermion" covered by F1 on both kernels plus F2 on K1 only?
8. **Scope** (§6).

## 9. Files

All are under `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/X1/`:

- **Pre-registration:** `PREREG.md`.
- **Code:**
  - `x1_core.py`: the local density and k-resolved response;
  - `x1_validate.py`;
  - `x1_run.py`;
  - `x1_run_logdet.py`;
  - `x1_dirac.py`: F2, including its validation;
  - `x1_analyze.py`;
  - `x1_blocks.py`;
  - `x1_perreal.py`;
  - `x1_dirac_fs.py`;
  - `lane*.sh`.
- **Outputs:**
  - `out/analysis_final.out`: every spectrum, every k-resolved table, the cubes;
  - `out/blocks_final.out`;
  - `out/perreal_final.out`;
  - `out/dirac_finite_size.out`;
  - `out/validate.out`;
  - `out/dirac_validate.out`;
  - `out/fermion_params_K1.json` and `out/fermion_params_K2.json`;
  - per-run `out/*.log` and `out/*.pkl`, holding the positions and per-site κ for every realization.

No repository file was edited.

---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** True

**Corrected verdict:** I could not refute it. The verdict is FAIL against the fixed X1 reading, unchanged, bounded to the tested implementation. That implementation is a quenched 4D Euclidean Poisson set with kernels K1 and K2 and the free functionals S0 and F1 (both kernels) and F2 (K1 only).

- Every direct nonzero-k TT stiffness spectrum is flat and at or above 1e-3. This holds for both kernels and for the fermion sea, whether S is read as a power or as an amplitude. The lowest case, K2 scalar, gives S = 2.1e-3, about 7.6 decades above the 5e-11 PASS bar.
- My independent checks reproduce the levels and the flatness:
  - an independent finite-difference code with a different local coupling rule;
  - fresh realizations from my own sampler;
  - an independent full 4x4 Dirac construction.
- Under the TESTS.md rule, every FAIL needs the codex gpt-5.6-sol referee before it is recorded. Until then this is "FAIL (bounded), adversarial check supports, codex referee pending".
- It is not a class-wide exclusion of finite-valency constructions.
- Two side claims need correcting; neither touches the reading (see issues).

**Issues:** The verdict holds. Below are what I confirmed, the corrections to side claims, and the scope limits I would add.

**Confirmed (none overturns the verdict)**
1. **Fixed readings.** They are quoted exactly. PREREG.md is stamped 00:56:09Z, after the C3 pre-registration at 00:47Z.
2. **FAIL conditions, checked against analysis_final.out:**
   - K1 S0: flat over qR 0.18–1.41, 8 points, p = −0.03 ± 0.08, S = 3.6e-3.
   - K2 S0: S = 1.94e-3 and 2.20e-3 at 42 realizations, p = +0.18 ± 0.22.
   - F1 on K1: 7.1e-2.
   - F1 on K2: 3.8e-2.
   - F2: 1.4e-2.
3. **Normalisation.** S = (1/N)|Σκ e^{-iqz}|² equals c5's (sd·√N)². For example, sd·√N = 0.0646 gives S_box = 4.17e-3.
4. **Arithmetic.** log10(2.1e-3/5e-11) = 7.6 and log10(0.046/5e-11) = 9.0.

**Corrections to side claims**
- **(a) §5.7, "the ensembles agree at q = 0, so there is no zero-frequency atom".** This does not hold for F2.
  - Fixed-N S_box(0) for h1 is 4.2e-2, against 1.2e-2 for Poisson-N. That is sd·√N of about 0.21 in both independent fixed-N seed sets (5 and 7 realizations), against 0.10–0.12 for Poisson.
  - The variance ratio is about 3.5 with 11 and 21 degrees of freedom, so p ≈ 0.01.
  - The claim holds for S0 and F1 only. For F2 it should read "q = 0 excess under fixed-N, 12 realizations, unresolved".
  - The excess goes in the direction opposite to PASS, so the verdict is unaffected.
- **(b) §5.6, "the scatter/χ² ratio is 0.79–1.19 in every case".** analysis_final.out also shows 0.60 (K2 S0, rod 5³×32) and 0.71 (F1 on K1, fixed-N with the shared pilot). The range is 0.60–1.19.

**Nuance on the decomposition-free claim**
- The averaged spectra are independent of the coupling rule. I confirmed this with a third rule, the endpoint average.
- Per realization, the more nonlocal F1 on K2 shows 5–15% amplitude differences at q = 0.52. For example, in r = 0, |κ̃|²/N is 6.1e-4 by finite differences and 1.3e-3 by density.

**Scope limits to state**
1. **The K2 flat rule rests on a short window.**
   - The 42-realization window has 2 points, spanning a factor 2 in q.
   - It excludes a q² falloff at more than 5σ, but it cannot exclude a weak falloff with p ≈ 0.5.
   - It meets the pre-registered "flat" rule. It is the thinnest leg of the FAIL.
2. **Fermion coverage.**
   - The frame-sensitive fermion F2 was run on K1 only.
   - "The fermion" is met through F1, the pre-registered E23-convention spinless sea, on both kernels.
   - On K2, only the 4+1 Hamiltonian-type functionals S0 and F1 were tested. The Euclidean S1 and F2 were not.
3. **Interaction.** The B referee's ranked test 3 also asked for "one interaction". That is not part of X1's fixed reading, and it was not done.
4. **Mean F2 stiffness.** At width 4 it is nonzero: +0.0034 ± 0.0006.
   - The worker attributes this to the torus. That is plausible, since the mean vanishes by SL(4) invariance of the law in infinite volume.
   - At width 6 the evidence is thin (8 realizations).
   - This is outside the reading.
5. **Referee.** The codex referee has not yet run, and it is required before this FAIL is recorded.

**Re-runs:** All runs used OMP_NUM_THREADS=2, and each stayed under 10 minutes. Outputs are in /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/X1/verify/.

**1. Worker validations re-run** (`validate_rerun.out`, `dirac_validate_rerun.out`)
- I re-ran `x1_validate.py` and `x1_dirac.py validate`.
- The output is identical to the worker's `out/validate.out` and `out/dirac_validate.out`. That covers Σκ against the eigenbasis total, the finite-difference checks, agreement with the packet's `e23_core`, and the Dirac block assembly.

**2. Independent finite-difference k-resolved stiffness** (`fd_kspec.py`)
- **Method.**
  - My own Laplacian and energy, with no worker code.
  - Pairs are recomputed by proper distance.
  - The strain is coupled by the endpoint average (φ(z_i) + φ(z_j))/2, not the worker's midpoint rule.
  - κ̃(2k) comes from E''[cos] − E''[sin] and E''[cos(·−π/4)] − E''[sin(·−π/4)]. This uses no local density.
- **Worker's K1 rod 4³×32 realizations** (30, h1; `fdA_K1rod32_worker.out`). Finite difference against the worker's density:

  | Functional | q = 0.393 | q = 0.785 |
  |---|---|---|
  | S0 | 3.52e-3 against 3.51e-3 | 3.51e-3 against 3.47e-3 |
  | F1 | 8.6e-2 against 8.6e-2 | 8.8e-2 against 8.8e-2 |

  Per realization, the complex amplitudes agree to about 1–3%.
- **Fresh realizations from my own Poisson sampler** (`fdB_K1rod32_fresh.out`, 30 realizations):

  | Functional | q = 0.393 | q = 0.785 |
  |---|---|---|
  | S0 | 4.7e-3 ± 0.7e-3 | 2.8e-3 ± 0.5e-3 |
  | F1 | 1.00e-1 ± 0.16e-1 | 6.5e-2 ± 1.1e-2 |

  All are flat and at or above 1e-3.
- **Worker's K2 rod 5³×24 realizations** (12, h1; `fdC_K2rod24_worker.out`). Finite difference against the worker's density:

  | Functional | q = 0.524 | q = 1.047 |
  |---|---|---|
  | S0 | 2.92e-3 ± 0.32e-3 against 2.91e-3 | 1.63e-3 against 1.59e-3 |
  | F1 | 2.42e-2 against 2.43e-2 | 1.90e-2 against 1.76e-2 |

**3. Independent Dirac check** (`fd_dirac.py`, `fdD_dirac_rod24.out`)
- **Method.**
  - The full 4x4 Euclidean gamma construction, not the worker's chiral B†B route.
  - W = −log|det(D + 1)| via slogdet.
  - A modulated vierbein with the endpoint coupling.
- **Constant-strain totals** match the worker to 1e-5. Examples are −1.35896 against −1.35894, and +3.85782 against +3.85782; the cube cases also match.
- **κ̃(q = 0.524) on rod 4³×24 realizations 0–2** agrees within 2–8%. |κ̃|²/N is:
  - 3.6e-3 against 3.8e-3;
  - 6.5e-3 against 6.4e-3;
  - 3.54e-2 against 3.50e-2.

**4. Re-analysis of all saved pkl files** (`reanalyze.py`)
- **h1–h2 correlation.** The correlation of the spectra is at most 0.07, so pooling the two directions is fine.
- **Intercept fit.** S = a + b·q² was fitted over qR ≤ 2. In every case a is at or above 1e-3 at more than 5σ, and b is consistent with 0:

  | Case | a | Realizations |
  |---|---|---|
  | K1 S0 | 3.60e-3 ± 0.13e-3 | 210 |
  | K2 S0 | 2.07e-3 ± 0.19e-3 | 56 |
  | F1 on K1 | 7.9e-2 ± 0.4e-2 | — |
  | F1 on K2 | 3.8e-2 ± 0.35e-2 | — |
  | F2 | 1.38e-2 ± 0.16e-2 | — |

**5. F2 per-realization q = 0 totals**
- This check found correction (a).
- Fixed-N gives sd·√N = 0.220 for the 5-realization seed set and 0.213 for the 7-realization set. Poisson gives 0.118 and 0.102.
