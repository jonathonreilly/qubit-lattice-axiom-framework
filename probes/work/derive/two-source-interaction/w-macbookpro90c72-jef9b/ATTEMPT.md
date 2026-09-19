# two-source-interaction, attempt 5 (worker w-macbookpro90c72-jef9b, model grok-4.6)

Own plan: the Newtonian coefficient of the linear light-cone covariance, from `E=|k|²+O(k⁴)` and `FT(1/k²)=1/(4πr)`. a1–a4 (same family) treated FDR and finite-L pins; this is the continuum `1/r` prefactor.

Light-cone: `φ=1-E/7`, `E=2∑_j(1-\cos k_j)`, stationary covariance `C=σ²/(1-φ²)=7σ²/(2E(1-E/14))`, static response `χ=1/(1-φ)=7/E`.

## (1) The statement attempted

**Statement (PARTIAL).** (a) Naive FDR fails: `χ/C=1+φ`, identically, not a real constant. (b) Linear mean field about a persistent source is `χ(k) h(k)`; real-space `~ (7/(4π r)) h` at long distance. (c) The equal-time kernel itself is Coulomb with coefficient **`7σ²/(8π r)`**, because `E=|k|²+O(k⁴)` (Hessian `2I`) so `C∼7σ²/(2k²)` and `∫ d³k/(2π)³ e^{ikx}/k²=1/(4π|x|)`. Like pins: interaction `∼ -a b C(r)` attractive when `C>0`. (d) Massless torus: like-pin energy IR-divergent; superposition holds linearly. Sphere `1/β` and nonlinear 1/r not proved. Gaussian conditioning on large L not re-run (a2).

## (2) Steps

**Step 1 — `χ/C=1+φ` (PROVED; CHECKED N1a, N2).** Algebra: `1-φ²=(1-φ)(1+φ)`, `C=σ²/(1-φ²)`, `χ=1/(1-φ)`, ratio `1+φ`. Sampled on `L=4` modes.

**Step 2 — `E=|k|²+O(k⁴)` (PROVED; CHECKED N1c,e).** Hessian of `E` at 0 is `2I`. Axis series `E(k,0,0)=k²+O(k⁴)`.

**Step 3 — coefficient `7σ²/(8π r)` (PROVED; CHECKED N1d).** `7/2 × 1/(4π)=7/(8π)`. Standard Fourier of the Laplacian Green function on `R³` ASSUMED at the usual scope (`-Δ(1/|x|)=4πδ`).

## (3) Where the route stops

Linear continuum only. Nonlinear sphere pins and the reversible `π∝∏ Z` interaction of a4/a1 (six-axis) are other routes. First missing step for a theorem of Newton’s law: a remainder `C(x)=7σ²/(8π|x|)+O(1/|x|³)` on `Z³` with an explicit constant, plus unlike-pin energy matching `+7σ² a b/(8π r)`.

## (4) What would finish it

Watson lemma for the lattice Green function of `E(k)` vs `k²`, and the two-pin log-weight `(1/2) v^T K^{-1} v` expanded as in the compute task, checked on `L=8..32` FFTs.
