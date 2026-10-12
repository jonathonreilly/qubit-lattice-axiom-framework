# Lane RD (campaign C4), probe D2: numerics on gapless-dressed bands. Report

**Provenance.** Worker: Claude Opus 5.5 (same model family as the supervisor). Ran 16:23Z to about 16:55Z on 2026-10-11. Not refereed. No repository files were edited.

**Scratch folder:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/D2/`

| Script | Output | What it does |
|---|---|---|
| `d2_common.py` | (library) | Bands, mediators, vertex \|M_q\|² = g²(2\|sin q/2\|)^{2a}, one-loop root solver (bracketed Newton), face and SLAC-fit measures |
| `d2_test.py` | (console) | Calibration: exact SLAC gives exponent 1.000, slope ratio 1.000, fit error 3e-16; smooth bands give exponent 2.000 |
| `d2_scan1d.py` | `d2_scan1d_N1024.out` | 1D one-loop scan: band {TB, KG} × sound speed {1.5, 1.0, 0.4} × vertex power a {0, ¼, ½, 1} × g² {0.05, 0.3, 1}; bare-propagator (BW1) and self-consistent (SC) |
| `d2_scan_summary.py` | `d2_scan_summary.out` | Summary of the scan over converged runs |
| `d2_rs1d.py` | `d2_rs1d.out` | 1D second-order Rayleigh–Schrödinger (RS), continuous k at the face, q-grids up to 2^20 |
| `d2_rs2d.py` | `d2_rs2d.out` | 2D RS, face centre (π,0) and corner (π,π), q-grids up to 512² |
| `d2_rs3d.py` | `d2_rs3d.out` | 3D RS, face centre, q-grids up to 96³ (includes the QED-like marginal power a = −½) |
| `d2_ed1d.py` | `d2_ed1d_Mconv.out`, `d2_ed1d_main.out` | Exact diagonalization, one electron + acoustic phonons, N = 8–24 sites, phonon number ≤ M (M-converged), twisted boundary for continuous K |
| `d2_scba1d.py` | `d2_scba1d.out` | Self-consistent Born (non-crossing) on the real axis, 1D, η = 0.01 |
| `d2_super1d.py` | `d2_super1d.out` | Supersonic (Cherenkov) regime, generic band: face bound state, Z, rounding |
| `d2_super1d_b.py` | `d2_super1d_b.out` | Supersonic regime with two degenerate Cherenkov minimisers: exact threshold Λ-cusp at the face, and what the dressed state does |
| `d2_q4_sc.py`, `d2_q4_bare.py` | `d2_q4_sc.out`, `d2_q4_bare.out` | Self-consistent check of the degenerate-minimiser cusp; SLAC-fit comparators |
| `d2_fermisea.py` | `d2_fermisea.out` | Impurity band + Fermi sea, density vertex (onsite and nearest-neighbour), 1D and 2D: decay rate Γ at the face |

Units: TB band ε = 1 − cos k (v_max = 1); KG band ε = √(m² + 4 sin²(k/2)), m = 0.5; flat-bottom band "Q4" ε = (1 − cos k)² (trig degree 2, v_max = 2.6); mediator ω = 2c\|sin(q/2)\| (per axis, ω = c\|2 sin(q/2)\| in d > 1). Vertex power a = ½ is the nearest-neighbour strain vertex n_i(u_{i+1} − u_i); a = −½ has the photon-emission power counting (no gauge structure). "Face" = k = π (1D), (π,0) or (π,π) (2D), (π,0,0) (3D).

## Reading against the FIXED lines

**PASS is not met.** No computed case gives a dressed band equal to SLAC on an open set including the face with a finite residue. Nothing came close: see (ii) and (iv).

**FAIL (bounded) is supported, CHECKED numerically, pending the codex sol referee.** In every class computed, one of the FAIL alternatives holds:
1. **Subsonic matter + gapless acoustic/photon-like mediator (1D, 2D, 3D; a from −½ to 1; one-loop BW1, self-consistent one-loop, RS, SCBA, and exact 1D ED):** the dressed face is a **smooth maximum**. The face exponent is 2.000 and the face curvature is N-stable. There is no cusp at all, so the dressed face differs from SLAC (whose face has a Λ-kink of slope βπ/E(π)).
2. **Supersonic (Cherenkov) matter:** the face state is a phonon-dominated bound state below the one-phonon threshold. With a generic band it is smooth at the face. With two degenerate Cherenkov minimisers, the threshold has an **exact Λ-cusp at the face**, and the dressed band follows it with rounding length ℓ ∝ g⁴ and **Z(π) ∝ ℓ**. The cusp becomes exact only as the residue vanishes. Even the limiting cusp (the threshold itself) is not SLAC.
3. **Fermi sea, density vertex (1D, 2D):** the face state has a finite decay rate Γ(π) > 0, stable in N and broadening. There is no real-axis pole at the face, so the residue of a sharp band there is zero.
4. **Marginal infrared powers** (d + 2a = 2: 1D strain vertex a = ½, 2D a = 0, 3D a = −½): Z → 0 everywhere in the band, including the face, logarithmically at one loop. In exact 1D ED it falls as a power law N^{−γ} with γ ∝ g². **IR-relevant powers** (d + 2a < 2): Z → 0 as a power of N.

**Scope.** The FAIL holds for the classes listed, at the orders computed, in the one-particle sector. It is numerical (CHECKED), not proved. See "Limits".

## (i) Band shape near the zone face

The local exponent p is of D(δ) = E(face) − E(face − δ). Calibration: SLAC gives p = 1.000; a smooth maximum gives 2.000. C(δ) = 2D(δ)/δ². If a cusp formed, C at fixed small δ would grow ∝ N; for a smooth face it converges.

| Method / class | p at small δ | C vs N (fixed δ) | Verdict |
|---|---|---|---|
| 1D one-loop scan, 144 runs (BW1 + SC, all bands, c, a, g²; N = 1024), 109 converged | 2.000 at δ = 1 and 4 grid steps in all 109 converged runs; 1.995–2.001 at 16 steps; 1.92–2.03 at 64 steps (δ ≈ 0.39, quartic terms) | — | smooth |
| 1D RS, TB c = 1.5, g² = 0.3, N = 2^12 → 2^20 | dressing part Σ(π) − Σ(π−δ): p = 2.000 (a ≥ ¼) | a = ½: 0.91507 → 0.91511 → 0.91512; a = 1: 0.67570 (all N); a = ¼: 1.0344 → 1.0374 | smooth, N-stable |
| 1D RS, a = 0 (IR-relevant) | 2.000 | 1.378 → 1.535 → 1.692 (grows like log N) | no cusp; whole band shape renormalises with the IR cutoff (Z → 0) |
| 2D RS face (π,0), c = 2, N = 64 → 512 | 2.000 | a = ½: 0.96284 (all N); a = 0: 0.98701 → 0.98733; a = −½: 1.0073 → 1.0196 (log drift) | smooth |
| 2D RS corner (π,π) | 2.000 | a = ½: 1.80154 → 1.80156; a = 0: 1.9307 → 1.9314 | smooth |
| 3D RS face, c = 2, N = 24 → 96 | 2.000 | a = −½ (QED-like): 0.99669 → 0.99685; a = 0, ½: N-stable to 5 digits | smooth |
| 1D exact ED, TB c = 1.5, a = ½, g² = 0.3 / 1.0, N = 8 → 24 (M-converged to 4–6 digits at N = 12) | 2.000 | 0.9001, 0.9067, 0.9100, 0.9119, 0.9132 (increments 0.0066 → 0.0013, converging); g² = 1: 0.7174 → 0.7435 (converging) | smooth |
| 1D ED, a = 1 and a = ¼; KG c = 1 | 2.000 | 0.5092 → 0.5116; 0.8218 → 0.8944 (slowing); KG 0.2139 → 0.2873 (converged by N = 16) | smooth |
| 1D SCBA (non-crossing), TB c = 1.5, a = ½, N = 64/128, η = 0.01 | 1.996–1.998 at the first steps (one g² = 1 row has ω-grid jitter 1.58/2.46) | — | smooth |

**Supersonic, generic band** (TB, c = 0.4; `d2_super1d.out`). The one-phonon threshold has a unique minimiser at the face (electron at the band bottom plus a zone-boundary phonon). It is smooth. The bound state below it is smooth: the chord slope s(δ)/s_th scales linearly in δ for every g². Z(π) = 0.114, 0.023, 2.5e-3, 2.8e-4, 2.6e-5 for g² = 0.3, 0.1, 0.03, 0.01, 0.003, so Z ∝ g⁴ at weak coupling.

**Supersonic, degenerate minimisers: the one SLAC-like feature found** (Q4 band; `d2_super1d_b.out`, `d2_q4_sc.out`). At K = π the threshold min_k[ε(k) + 2c\|cos(k/2)\|] has two minimisers ±k*: k* = 0.457 at c = 0.4, 0.751 at c = 1.0. The two Cherenkov branches exchange at the face, so the threshold has an exact Λ-cusp there, with slope \|ε′(k*)\| = 0.091 (c = 0.4) and 0.367 (c = 1.0). The dressed bound state (BW1, q-grid 32768, K continuous) follows it, rounded on a length ℓ:

| c | g² | gap to threshold at π | Z(π) | ℓ = s_th / C | Z(π)/ℓ | s(δ)/s_th at δ = 1e-3, 1e-2, 1e-1 |
|---|---|---|---|---|---|---|
| 1.0 | 0.3 | 8.4e-2 | 5.2e-2 | 1.4e-1 | 0.37 | 0.003, 0.035, 0.33 |
| 1.0 | 0.1 | 1.6e-2 | 1.3e-2 | 3.0e-2 | 0.43 | 0.017, 0.16, 0.80 |
| 1.0 | 0.03 | 1.7e-3 | 1.6e-3 | 3.1e-3 | 0.51 | 0.16, 0.73, 1.05 |
| 1.0 | 0.01 | 1.9e-4 | 1.8e-4 | 3.5e-4 | 0.51 | 0.70, 0.96, 1.08 |
| 0.4 | 0.03 | 1.6e-3 | 8.9e-4 | 1.2e-2 | 0.074 | 0.042, 0.36, 1.01 |
| 0.4 | 0.01 | 1.9e-4 | 1.2e-4 | 1.4e-3 | 0.082 | 0.31, 0.86, 1.12 |
| 0.4 | 0.003 | 1.7e-5 | 1.1e-5 | 1.5e-4 | 0.073 | 0.86, 0.99, 1.14 |

- The gap, ℓ and Z(π) all scale as g⁴ (successive ratios 8–11 per factor 3.3 in g²).
- So Z(π)/ℓ is constant: **the cusp sharpens only as fast as the face residue vanishes.**
- The self-consistent one-loop (N = 2048, c = 1; `d2_q4_sc.out`) agrees with BW1:

  | g² | Z(π) | gap | chord slopes at 1, 4, 16, 64 grid steps (s_th = 0.37) |
  |---|---|---|---|
  | 0.1 | 1.46e-2 | 3.0e-3 | 0.018, 0.070, 0.212, 0.382 |
  | 0.03 | 1.65e-3 | 1.7e-3 | 0.151, 0.289, 0.363, 0.430 |
  | 0.01 | 1.85e-4 | 1.9e-4 | 0.328, 0.361, 0.382, 0.434 |

  BW1 gave Z(π) = 1.57e-3 and 1.82e-4 at g² = 0.03 and 0.01. As g² → 0 the SC SLAC-fit errors converge to the threshold's (0.0043, 0.0146, 0.0334).
- In the window near the face the state is phonon-dominated throughout: Z(π − 0.2) = 4.8e-3.
- The SCBA with η = 0.01 cannot resolve this bound state (gap < η); its Q4 row in `d2_scba1d.out` is not usable.

**ED supersonic note.** At N ≤ 24 the ED face curvature for c = 0.4, g² = 0.05 is negative: −0.83 at N = 8, −0.24 at N = 24, at δ = 0.005. That is a finite-size effect: with q = π on the grid, "electron at k − π plus phonon π" makes the face a local minimum. It moves toward the thermodynamic (positive) value as N grows. Z(π) = 0.011 → 0.0085.

## (ii) Deviation from the best-fit SLAC form E² = m₀² + βk² on windows [π − w, π]

Max \|E − E_fit\| divided by the full-zone bandwidth. N = 1024 unless stated. The slope ratio is the one-sided face chord slope divided by SLAC's face slope βπ/E(π): it is 1 for SLAC and → 0 for a smooth face (0.007–0.009 at this grid).

| Band | w = π/4 | w = π/2 | w = π | slope ratio |
|---|---|---|---|---|
| exact SLAC (comparator) | 3e-16 | 3e-16 | 5e-16 | 1.000 |
| bare TB | 0.0257 | 0.0771 | 0.0869 | 0.008 |
| bare KG (m = 0.5) | 0.0177 | 0.0755 | 0.2272 | 0.007 |
| dressed KG, best case per window over converged runs | 0.0122 (c = 0.4, a = 1, g² = 0.3, BW1) | 0.0602 (same) | 0.2067 (c = 1.5, a = ¼, g² = 0.3, SC) | ≤ 0.016 (all 109 converged runs) |
| dressed TB, best case (indicative: energy zero fixed at the bare bottom) | 0.0161 | 0.0406 | 0.0741 | ≤ 0.016 |

The degenerate-minimiser case uses N = 2048 and windows π/8, π/4, π/2:

| Band | w = π/8 | w = π/4 | w = π/2 | slope ratio |
|---|---|---|---|---|
| bare Q4 | 0.0125 | 0.0406 | 0.0705 | 0.003–0.008 |
| Q4 threshold, c = 1 (exact Λ-cusp, Z = 0) | 0.0043 | 0.0146 | 0.0335 | 0.51–0.73 |
| Q4 dressed SC, c = 1, g² = 0.1 | 0.0085 | 0.0194 | 0.0386 | about 0.03–0.05 (one-step chord 0.018) |

**Dressing improves the SLAC fit by at most a factor of about 1.5 (KG) or 1.9 (TB, indicative) on any window.** It is often worse, and it never trends toward zero. The face slope ratio stays at the trivial grid value for every quasiparticle band. Only the Z = 0 threshold carries a real face slope, and that slope is 51–73% of SLAC's, not 100%.

SC runs with a ≤ ¼ at strong coupling did not converge in 150 iterations: the IR-divergent shift grows with each iteration. Where E crosses zero, the E² fit is meaningless (fit errors > 1 in the .out). The summary excludes these runs.

## (iii) Residue Z at the face

| Class | Z(face) vs N | Reading |
|---|---|---|
| 1D, a = 1 (IR-irrelevant), RS | 0.6356 at N = 2^12, 2^16 and 2^20 | finite |
| 1D, a = ½ (NN strain vertex; marginal), RS | 0.611, 0.570, 0.534; 1/Z − 1 grows by 0.117 per factor 16 in N | → 0 logarithmically (one loop) |
| 1D, a = ½, exact ED (M-converged) | g² = 0.3: 0.757, 0.742, 0.731, 0.724, 0.718 (N = 8–24): power law with γ ≈ 0.05. g² = 1: 0.505 → 0.425, γ ≈ 0.155. γ ∝ g² | → 0 as N^{−γ} (orthogonality); Z(0) also falls (0.952 → 0.914) |
| 1D, a = ¼, RS / ED | RS 0.247, 0.080, 0.022 (1/Z ∝ N^{1/2}); ED 0.523 → 0.371 | → 0 (power) |
| 1D, a = 0, RS | 0.021, 1.4e-3, 1e-4 (1/Z ∝ N) | → 0 (power) |
| 2D face, a = ½ / 0 / −½, RS | 0.9447 → 0.9441 / 0.9436 → 0.9220 (log) / 0.847 → 0.416 (1/Z − 1 ∝ N) | finite / → 0 log / → 0 power |
| 3D face, a = ½ / 0 / −½ (QED-like), RS | 0.9718 → 0.9717 / 0.9842 → 0.9837 / 0.9873, 0.9848, 0.9823 (1/Z − 1: +0.0026 per doubling) | finite / finite / → 0 log (infraparticle) |
| supersonic generic, 1D | Z(π) ∝ g⁴ (1.1e-1 to 2.6e-5) | finite but small (gapped bound state, smooth face) |
| supersonic degenerate, 1D | Z(π) ∝ ℓ ∝ g⁴ | finite only while the cusp is rounded |
| Fermi sea, 1D, onsite U = 1 / NN V = 1 | Γ(π) = 0.0877 / 0.265 (N = 512–2048, η = 0.01–0.02, stable to 3 digits) | no real-axis pole at the face |
| Fermi sea, 2D, onsite U = 1 | Γ(π,0) = 0.0525, Γ(π,π) = 0.139, Γ(π/2,0) = 0.015, Γ(π/8,0) = 0.001 (N = 32–64, η = 0.04–0.08; the last is at the broadening level) | no real-axis pole at the face |

**Marginality line.** These numbers match C1's power counting: Z → 0 exactly when d + 2a ≤ 2 (log at equality, power below). The nearest-neighbour strain vertex in 1D and the photon power in 3D both sit on the marginal line.

## (iv) Does any coupling or dispersion choice drive the face toward SLAC?

The scan is `d2_scan1d_N1024.out`, summarised in `d2_scan_summary.out`. Across all 109 converged runs (of 144), the face exponent at one grid step is 2.000 in every run, and the slope ratio lies in −0.0007 to 0.016 (SLAC: 1).

Best SLAC-fit error per window; the bare value is in parentheses. "Converged" means SC residual < 1e-9 and E > 0 on the whole zone.

| band, c, mode | converged / total | best w = π/4 | best w = π/2 | best w = π |
|---|---|---|---|---|
| KG, 1.5, BW1 | 12/12 | 0.0164 (0.0177) | 0.0724 (0.0755) | 0.2115 (0.2272) |
| KG, 1.5, SC | 7/12 | 0.0172 | 0.0743 | 0.2067 |
| KG, 1.0, BW1 | 10/12 | 0.0163 | 0.0726 | 0.2134 |
| KG, 1.0, SC | 5/12 | 0.0164 | 0.0724 | 0.2109 |
| KG, 0.4, BW1 | 8/12 | 0.0122 | 0.0602 | 0.2766 |
| KG, 0.4, SC | 2/12 | 0.0160 | 0.0688 | 0.2507 |

TB rows are indicative only. Dressing makes E(0) < 0, so a fit with the bare energy zero is ill-posed on the w = π window. Best values over all converged TB runs, bare in parentheses: 0.0161 (0.0257), 0.0406 (0.0771), 0.0741 (0.0869).

SC iterations did not converge in 150 steps in some cases: a ≤ ¼ at strong coupling, where the IR-divergent shift keeps growing, and several supersonic cases. Those runs are listed in the .out with their residuals and excluded here.

**No subsonic quasiparticle case moves the face toward SLAC.**
- The face exponent stays 2.000 and the slope ratio stays at its grid value. This holds for every sound speed, vertex power and coupling scanned, in d = 1, 2 and 3, and in the exact 1D ED.
- Coupling only rescales the band. It lowers E(π) and flattens the top, which can shrink the windowed C⁰ error by up to about 1.5× (KG) or 1.9× (TB, indicative). It does not create a one-sided slope.

**The only route to a face cusp found is a branch exchange at the face** (degenerate Cherenkov minimisers, supersonic regime).
- It gives an exact Λ-cusp only on the Z = 0 threshold.
- The cusp is not SLAC-shaped: the slope ratio is 0.51–0.73, and the SLAC-fit error is 0.4–3.4% of the bandwidth.
- On the quasiparticle, the cusp is rounded on ℓ ∝ Z(π).

## Mechanism (SUGGESTED; consistent with every run)

- **Subsonic case.** On shell, the soft-emission singularity sits in λ − E(k), which is pinned at 0. Its coefficient depends on k analytically through v(k) while \|v\| < c. Inversion plus periodicity make E even about the face. So nothing selects a one-sided slope. The dressing part Σ(π) − Σ(π − δ) itself has p = 2.000 in the RS runs for d = 1, 2, 3.
- **A face kink needs two branches crossing exactly at the face.** Examples are the Cherenkov branches here, or the band touching in C1's two-band construction.
- **Coupling hybridises the crossing branches.** That rounds the cusp on a length set by the binding gap, and the weight of the bare particle in the rounded state goes to zero with that length.
- **Combined with B2:** a gapped simple root is analytic, and a threshold-touching quasiparticle is analytic at the face unless branches cross. Then "exact cusp" and "finite residue" exclude each other in all the classes computed.

## Against the supervisor expectation

| Expectation | Outcome |
|---|---|
| Soft-emission threshold gives a cusp of the wrong form | Partly. For subsonic matter there is **no cusp at all** (smooth maximum, exponent 2). A cusp appears only from a branch exchange at the face (supersonic, degenerate minimisers). It is exact only on the Z = 0 threshold, and its slope is 51–73% of SLAC's. |
| Branch-point power law set by the coupling | Not seen at the face. The coupling-dependent power laws are in Z(N) (γ ∝ g² in 1D ED) and in the spectral edge, not in E(k) near the face. |
| Vanishing residue (infrared catastrophe) | Confirmed on the marginal line d + 2a = 2 (log at one loop, power law in exact 1D ED) and below it. Confirmed for the Fermi sea as a finite face decay rate. Not universal: for IR-irrelevant vertices (1D a = 1, 2D/3D a ≥ 0) Z(face) is finite, but then the face is smooth. |
| FAIL (bounded) | D2 supports FAIL (bounded, checked). |

## Labels

**CHECKED (numerical, same-family, unrefereed):**
- face exponent 2.000 and N-stable face curvature in every subsonic class (1D/2D/3D RS, 1D BW1/SC scan, 1D SCBA, 1D exact ED);
- the Z(N) scalings in table (iii);
- the Fermi-sea face decay rates;
- the supersonic generic smooth face with Z ∝ g⁴;
- the degenerate-minimiser threshold Λ-cusp, with ℓ ∝ g⁴ and Z(π)/ℓ constant (BW1, confirmed by SC at three couplings);
- the SLAC-fit errors and slope ratios in (ii);
- the M-convergence of the ED.

**SUGGESTED:**
- the mechanism paragraph (no one-sided slope without a branch crossing; hybridisation trades cusp sharpness for residue);
- 2D/3D degenerate-threshold analogues: there the threshold density of states is a step or √, so in 3D the bound state may merge with the continuum, making Z = 0 exactly at the cusp. Not computed.

**READING:** the FAIL support, bounded to the classes and orders below.

**COMPARATORS:**
- exact SLAC band (calibration);
- C1's d + 2a = 2 power counting;
- orthogonality catastrophe / mobile-impurity edge physics (Anderson; Imambekov–Glazman) for the 1D power-law Z;
- Fermi-polaron damping for the sea.

**PROVED:** nothing new.

## Limits (what this does not establish)

- **One-particle sector only.** There is no pair creation for the KG band and no back-reaction on the mediator.
- **Fermi sea only to second order** (one bubble, bare impurity propagator), and at half filling only.
- **Vertex corrections and ladders** are included only through the exact 1D ED, at N ≤ 24. ED cannot resolve thermodynamic non-analyticity below δ ≈ 2π/N; it shows only that the face curvature converges rather than growing ∝ N.
- **2D and 3D are second-order RS only** (subsonic), and only on lines through the face and corner.
- **a = −½ uses photon power counting without gauge structure** (no transverse projector, no diamagnetic term). A real lattice-gauge computation is not done.
- **The degenerate-minimiser cusp is computed in 1D only**, at one loop (BW1, plus SC at three couplings).
- **Not covered:**
  - mediators with non-analytic (SLAC-like) dispersion;
  - multi-band matter with symmetry-protected face crossings (C1's two-band route);
  - strong coupling beyond g² = 1;
  - T > 0.
