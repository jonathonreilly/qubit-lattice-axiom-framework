# Check x6 criteria (session 7; written 2026-10-28 before checks/x6_sig_free.py and before the §16 derivations)

Model: the free Gaussian soft chain of EXISTENCE §14.1 (noncompact abelian, d = 4, L = 3), fine coupling g_0,
straight averaging (Lemma GS-1: gauge-invariant content of the soft chain = straight chain), white kernel noise of
variance σ² per link. Lattice Maxwell curvature F = dA has covariance g_0²Π_ex; the F_12 symbol is
(k̂_1² + k̂_2²)/k̂², k̂_μ² = 4 sin²(k_μ/2). Reflection: time reflection x_0 ↦ -1 - x_0 about a fine-link mid-plane, which is
a block-boundary plane at every resolution; pullback convention ΘF = F∘θ, OS form ⟨F, G⟩ = E[conj(ΘF)G].

Geometry: block side ℓ = 3^r fine units (r = number of averaging steps between fine and observable resolution);
spatial torus of 3 blocks per direction (n_s = 3ℓ); P a 12-plane block plaquette whose base block occupies fine times
[ℓ, 2ℓ) (distance one block side from the plane, so its continuum support is at positive distance); composite test
form ψ_P = ℓ^{-4}Σ_{y∈B(P)}1_{Sq_y} (X-CONT-G (i)). c(r) := ⟨θψ_P, Π_exψ_P⟩ (unit coupling) is the cross-plane covariance
Cov(D(θP), D(P)) of the fine-field block flux.

## A. Cross-plane covariance of a block flux (exact)
- A1: c(r) for r = 1, 2, 3, 4 from the spatial-momentum / transfer-matrix formula with infinite time (time propagator
  e^{-E|n|}/(2 sinh E), cosh E = 1 + ω̂²/2).
- A2 (independent route): c(r) for r = 1, 2 from a full 4D FFT on a periodic lattice n_s³ × N_0 (N_0 = 16ℓ), against the
  transfer formula with the periodic-time propagator for the same N_0.
- A3: the continuum value c_∞ (sum over physical momenta q = 2πn/3, n ∈ Z³, of the continuum expression; truncated with
  the remaining tail bounded by the script).
- A4: the single-mode lower bound (the n = (±1, 0, 0) and (0, ±1, 0) terms) at each r and in the continuum.
- **PASS (A)** iff: every c(r) > 0; A2 agreement ≤ 1e-9 relative; every c(r) ≥ its single-mode term (A4); and
  |c(4) - c_∞|/c_∞ ≤ 0.05. Expected: c(r) converges to c_∞ > 0, monotonically or not (not part of the criterion).
- **FAIL** if any c(r) ≤ 0, A2 disagrees, or c(4) is not within 5% of c_∞.

## B. Signal-to-noise bound (any lemma of §16.2 of the form Var E[f(D + η) | D] ≤ (2/π)||f||²_∞·s²/τ²)
- B1: scalar case D ~ N(0, s²), η ~ N(0, τ²) independent; f ∈ {cos(λx), sin(λx), sign(x), 1[x > a]} over a grid of
  s/τ ∈ [0.01, 3], λ ∈ [0.1, 30], a ∈ [-2, 2] (in units of τ); Var computed by numerical quadrature of exact Gaussian
  integrals. **PASS (B1)** iff every ratio Var / bound ≤ 1 + 1e-9. Report the maximum ratio (sharpness, informational).
- B2: c(X) := smallest eigenvalue of P_X d d^* P_X on V_X = range(P_X d) for X ∈ {one plaquette, two plaquettes sharing a
  link (same plane), two plaquettes sharing a link (different planes), a 2×2 planar square, the six faces of a 3-cube},
  on a periodic 4⁴ lattice. **PASS (B2)** iff every c(X) > 1e-9, and c = 4 for one plaquette (to 1e-12); dim V_X = 5 for
  the cube faces (Bianchi).

## C. Monte Carlo of the free soft chain (independent of the ψ formula)
- Fine lattice 9³ × 54, one straight averaging step (coarse 3³ × 18), coarse white noise σ² per link. Fine field
  sampled in Feynman gauge by FFT (variance g_0²/k̂² per component, k ≠ 0); coarse field B_1 = Q_strA + ξ with
  Q_strA(X, μ) = L^{-4}Σ_{y∈LX+box_L}Σ_{j<L}A(y + je_μ, μ); Y = dB_1(P) for coarse 12-plaquettes at coarse time block b,
  Y_θ the reflected partner; averages over all 27 spatial positions and the 18 reflection planes (fine planes at
  multiples of 3).
- Cases: C1 g_0 = 1, σ² = 0.05 (constant-coupling regime, κ = 20); C2 g_0 = 0.05, σ² = 0.05 (signal ≪ noise, the
  (F)-mismatch regime). λ := v^{-1/2} with v the exact variance of Y below (rule fixed here, before any number is
  known; it maximises the leading term c/(e·v)).
- Estimate Q := E[e^{iλ(Y - Y_θ)}] - |E e^{iλY}|² (the OS connected quantity ||[F] - ω(F)Ω||²); 40000 independent
  samples; SE from per-sample means. (Amended before the script existed: σ², λ rule and sample size; the first draft
  had σ² = 1/4, λ = 1.5, 20000 samples and a 10 SE resolution threshold, chosen without an estimate of c.)
- Closed form for comparison: e^{-λ²(v - c)} - e^{-λ²v}, v = g_0²⟨ψ, Π_exψ⟩ + 4σ², c = g_0²⟨θψ, Π_exψ⟩ with the
  periodic-time lattice (computed by the A2 FFT route at r = 1, N_0 = 54).
- **PASS (C)** iff |MC - closed form| ≤ 4 SE in both cases, and in C1 the closed form is > 5 SE above 0 (the effect is
  resolved; if it is not, C is INCONCLUSIVE for C1, not a pass). In C2 the closed form is expected to be below the SE (informational).

## D. Informational
- The exact OS connected quantity sup_λ [e^{-λ²v}(e^{λ²c} - 1)] for an (F)-type sequence (g_0² = 1/(1/g² + β K log L),
  noise at resolution m from Theorem GS) versus K, and for constant couplings; expected → 0 like m/K versus a positive
  K-independent value. No pass/fail.

Resources: numeric lock, nice 10, BLAS threads 1, load < 8, memory ≥ 25% free; python3 without -I (user-site numpy);
the script reads no external files.
