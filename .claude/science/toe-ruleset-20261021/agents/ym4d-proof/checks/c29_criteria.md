# c29 criteria (written BEFORE checks/c29_su2_contraction.py; session 14, 2026-10-27)

Purpose: instances for the session-14 targets (RTARGET §27-31). Not a proof of anything. Four parts, each run as its own
job (`python3 -I c29_su2_contraction.py A|B|C|D`), one job at a time.

## Part A: fine sources enter the linear chain as effective coarse data (Lemma SRC-id, linear)
Setting: c26's Chain (Setting SC, S4' root averages, LSMR) on the cases (d, T, k, κ) = (4, 3, 1, (1)), (4, 2, 2, (1, 1)),
(2, 5, 2, (1, 1)), (2, 5, 3, (0.5, 2, 1)). A fine source j := d*ω (ω a random fine 2-form, fixed seed), so j is
co-closed with zero mean; random coarse data B_k. The chain with source is the critical point of E - ⟨j, B_0⟩, solved by
MINRES on the normal equations MᵀMx = Mᵀb + (j, 0, …, 0).
- V1 (validity): the normal-equation residual ≤ 1e-8 relative, in every case.
- A1: r_{k-1}(source j, data B_k) equals r_{k-1}(no source, data B_k - Q^{(k)}Δ^{-1}j), with Q^{(k)} the chain's own
  composite root map and Δ^{-1} the fine Hodge inverse (FFT, zero mode removed): relative max error ≤ 1e-6.
- A2: dB_0 equals dΔ^{-1}(j - κ_0Q_0ᵀr_0) (Q_0 the level-0 root map), and r_0 = (κ_{k-1}/κ_0)(Q^ᵀ)^{k-1}r_{k-1}:
  relative max error ≤ 1e-6.
- A3 (algebra): at 200 random complex points z (|Im z_α| ≤ 0.05) and n ∈ {3, 9, 27}, the identity
  a·Σ_ν ν̄_ν W̄_ν ĵ_ν/β_ν = ΠD̄·[Σ_ν ν̄^{(n)}_ν ĵ_ν - φ Σ_ν ν̄^{(n)}_ν R_ν ĵ_ν/β_ν] for random complex ĵ, with every block
  continued analytically (W̄_ν := ΠD̄·D̄_ν, D̄ the continuation of the conjugate on the real axis): relative error ≤ 1e-10.
- Informational: on a T = 64 coarse grid near p = 0, the size of the K = 0 composite symbol ĵ ↦ r̂ (SRC-id formula) vs
  the size of its 1/φ input ĝ.
PASS iff V1, A1, A2, A3.

## Part B: target D's sector bounds at complex points (Lemma EXP-strip')
For (κ, κ̂) ∈ {(1, 1), (0.25, 1), (4, 1)} with κ_i ≡ κ, and (1, 16) with k = 2, (κ_0, κ_1) = (1/16, 1) (κ̂ = 16), and
k ∈ {1, 2, 3} (n = 3, 9, 27; k = 2 only for κ̂ = 16): take (η, r_0) := the proof's values (η'_*, r_0) (computed by the
script from the proof's formulas, verbatim arithmetic). Sample x: 120 uniform points of Q = [-π, π]⁴ (40 at k = 3),
plus 0, (π, π, π, π), (π, 0, 0, 0), (r_0, 0, 0, 0), (r_0, r_0, 0, 0)/√2. For each x, four y with |y_α| ≤ η (two uniform,
two at the corners ±η). Check every inequality of the lemma with its constant (ratio ≤ 1, or ≥ 1 for lower bounds):
- B1: |Re δ(z_α) - δ(x_α)| ≤ c_η, |Im δ(z_α)| ≤ sinh η·min(1/3, |x_α|/6);
- B2: Re φ_α(z) - φ_α(x) ∈ [-c_φ, 0], |Im φ_α(z)| ≤ σ_φ√φ_α(x); |Re Δ_α(z) - Δ_α(x)| ≤ 2c_η, |Im Δ_α(z)| ≤ 2 sinh η √Δ_α(x);
- B3: |arg(aδ_μ(z)/aδ_μ(x))| ≤ θ_a and m_- ≤ |aδ_μ(z)/aδ_μ(x)| ≤ m_+;
- B4: |Re R_μ(z) - R_μ(x)| ≤ e_RR, |Im R_μ(z)| ≤ e_RI;
- B5: (1 - ρ_R)β_μ(x) ≤ Re β_μ(z) ≤ (1 + ρ_R+)β_μ(x), |Im β_μ(z)| ≤ ρ_Iβ_μ(x);
- B6: for |x| ≤ r_0: |Ψ(z)| ≥ Ψ_L; for |x| ≥ r_0: Re Σ(z) ≥ (ψ(x)/min_ν β_ν(x))·br'_V and Re φ(z) ≥ ψ_0/2.
PASS iff every check holds at every sample (a float tie at a sharp point counts as a FAIL; it is reported as such).

## Part C: SU(2) contraction instance (B-NA's second-order structure and the decay of the non-abelian response)
Model: c22's (SU(2) unit quaternions, d = 4, L = 3, κ = 1, E = Σ_p(1 - Re U_p) + κΣ_c(|M̄_c| - ⟨V_c, M̄_c⟩), the S4'
contours of c22), with coarse side NC as stated. Minimiser: c22's Riemannian Barzilai-Borwein descent, stopped at
|g| ≤ 1e-9·|g_0| (12000 iterations max; otherwise NOT CONVERGED). Residual ρ_c := log(V_c^{-1}M̄_c/|M̄_c|) (half-angle
vector; invariant under the fine gauge transformations that fix V). Linear prediction: c26's Chain(d = 4, T = NC, k = 1,
κ = (1)) by LSMR, componentwise on the three su(2) components (same S4' template).
- C-V1 (validity): every minimisation CONVERGED.
- C-V2 (validity, the linear prediction is the t → 0 limit): D(0.025) ≤ 0.05, where D(t) := ||ρ(t)/t - r_lin||_2/||r_lin||_2.
- C1 (NC = 3, data V_t = exp(t·X), X a fixed random smooth coarse su(2) field, t ∈ {0.025, 0.05, 0.1, 0.2, 0.3}): the
  least-squares slope p of log D(t) against log t over the five t is ≥ 0.8 (the non-linear part is O(t²) in ρ, i.e. D =
  O(t) or smaller), and D(0.1) ≤ 0.1. Informational: D(t)/t, E(t)/t² vs the linear energy.
- C2 (NC = 4, background t = 0.2, a localised data change at the coarse link c_0 = (0, μ = 0) in colour direction e_1,
  amplitude s = 0.01, symmetric difference): δρ := (ρ(+s) - ρ(-s))/(2s); δr_lin := the linear kernel (LSMR, data e_1 at
  c_0); Δ := δρ - δr_lin (the non-abelian part of the response). Profiles by the periodic ℓ^∞ distance d ∈ {0, 1, 2}
  between the base sites of c and c_0: A(d) := max_{c at distance d}|Δ_c|, A_lin(d) likewise for δr_lin. Rates
  m_NA := ln(A(0)/A(2))/2, m_lin := ln(A_lin(0)/A_lin(2))/2.
  - C2-V (validity, the linear kernel decays on this torus): m_lin ≥ 0.5.
  - C2a: max|Δ| ≤ 0.5·max|δr_lin| (perturbative at t = 0.2).
  - C2b: m_NA ≥ 0.5·m_lin.
PASS (findings) reported per criterion; Part C is VALID iff C-V1, C-V2 and C2-V hold.

## Part D: covariant Faddeev-Popov identities (Proposition NA-FP), NC = 3, at the t = 0.2 minimiser U* of Part C's C1
(recomputed in Part D with the same seed and stopping rule)
Conventions: (D_Uλ)_b := Ad(U_b)λ(y) - λ(x) for b = (x → y); Λ := {λ : λ(c_X) = 0}; h_U(A)(X) := average over the 24
orders σ and the 81 sites y ∈ B(X) of the transported path functional ℓ_{P^σ(c_X→y)}(A) (PROOF L5 [S14]); M_Uλ(X) := the same
average of Ad(T^σ(c_X ← y))λ(y). Tangent vectors in c22's left trivialisation (U_b → e^{A_b}U_b), where the gauge orbit
direction of λ is -D_Uλ.
- D1: max_X|h_U(D_Uλ)(X) - (M_Uλ(X) - λ(c_X))| ≤ 1e-12·max|D_Uλ| for 3 random λ (any λ, not only Λ), at U* and at a
  random non-critical U.
- D2: at U*, for 3 random λ ∈ Λ, ξ := D_Uλ: R(ξ) := |H_Uξ|/|ξ| ≤ 1e-4·median_v |H_Uv|/|v| over 3 random v, with
  H_Uξ := (g(e^{hξ}U) - g(e^{-hξ}U))/(2h), h = 1e-4.
- D3 (control, the identity needs criticality): at the start configuration U^0 (non-critical), R(ξ) ≥ 1e-2·median_v.
PASS iff D1, D2, D3.

## Resources and rules
One job at a time, nice 10, OPENBLAS/OMP/MKL/VECLIB threads 1, `uptime` load < 8 and memory_pressure free ≥ 25% before
each job; peak RSS < 1.5 GB (reported). A pre-run smoke test of the evaluator at NC = 4 (one energy/gradient
evaluation, timing, memory) is allowed and is disclosed in checks/c29_time.txt; it changes no criterion. No criterion
is edited after any run; post-run diagnostics are labelled as such.
