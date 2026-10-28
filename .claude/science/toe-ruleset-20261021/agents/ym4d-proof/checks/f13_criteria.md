# f13 criteria (lane C, session 10; written before any f13 script)

Pre-statement: FLOW.md §73 (T1)-(T7) and its "Check f13" paragraph. This file fixes the computations, thresholds and
verdict lines before any f13 script exists. No constant derived in session 10 appears here; reference values are
from session 9 (checks/f12_out.txt) and from closed forms (c_g = 1/(96π²), L = 3, s = 4).

Run conditions: one NUMERIC LOCK acquisition per official run, released once with rmdir (no trap); nice 10; all BLAS
threads = 1; plain python3; no `timeout`; load < 8 and memory free ≥ 35% checked inside the lock before starting; job
< 20 min, peak RSS < 1 GB (measured by /usr/bin/time -l). A run that starts outside these conditions is VOID and is
re-run, and the void output is set aside unused.

## Part A: Lemma FINE-IR (fine scalar polarisation, x_0(q) = [ε²]τ log Δ_U/(q²/2))
Method: x_0(q) = (16 sin²(q/2)/q²)·J(q), J(q) = ∫∫_0^∞ ds dt s t e^{-8τ}·½[I_0(2τ) − I_2(2τ)]·½[I_0(2R) − cos(2ψ)I_2(2R)]·I_0(2τ)²,
τ = s + t, R² = s² + t² + 2st cos q, cos 2ψ = ((s² + t²)cos q + 2st)/R² (the symmetrised form of FLOW §74), by the trapezoidal
rule in u = log s, v = log t with scaled Bessel functions.
- A1 (step control): halving the log-step changes x_0(q) by ≤ 1e-10 relative at every q used. Verdict line.
- A2 (symmetrisation identity): at q = 0.3 and q = 0.6, the unsymmetrised form (1/(2q²))[∫W/λ − ∫Σ²/(λλ_q)] (each piece by
  its own proper-time representation) agrees with x_0(q) to ≤ 1e-9 relative. Two verdict lines.
- A3 (log slope, S10-F1): the slope −Δx_0/Δlog q between q = 1e-3 and q = 1e-2 equals 2c_g to ≤ 1e-3 relative. Verdict line.
- Reported: a_0 from a fit of x_0(q) − 2c_g log(1/q) in {1, q² log q, q²} on q ∈ [1e-3, 0.05], and its change under the
  window [2e-3, 0.1].

## Part B: (VC)/(UIR) for the scalar proxy (L = 3, s = 4)
Y_n(P) := x_n(P) − 2c_g log(1/P), evaluated exactly as Y_n(P) = x_0(P/ℓ) − 2ℓ²h_n(P/ℓ)/P² − 2c_g log(1/P), ℓ = 3^n, with h_n
from the f12 functions UNCHANGED (h_of_p, p = 0 integrand subtracted pointwise), x_0 from Part A.
n = 1..5; P-grid {0.05, 0.1, 0.2, 0.4, 0.8, 1.6, 2.4}.
- B1 (step control): for n = 1..4, K grid 12⁴ vs 16⁴ (proper-time step h_u = 0.3) changes Y_n(P) by ≤ 1e-9 at every P; for
  n = 5, h_u = 0.15 vs 0.1 at K grid 12⁴ changes Y_5(P) by ≤ 1e-9 at every P (REVIEW_FLOW_S9 §9: h_u ≤ 0.15 at n ≥ 5).
  Verdict lines (one per n).
- B2 (S10-F2): with Δ_n := max_P |Y_n(P) − Y_{n−1}(P)|, the ratios Δ_n/Δ_{n−1} for n = 3, 4, 5 are each ≤ 0.2. Three verdict
  lines. Reported: Δ_n, the ratios, and the P at which the max is attained.
- B3 (uniformity in P, S10-F2): for n = 3, 4, 5, |Y_n(P) − Y_{n−1}(P)| at P = 0.05 is ≤ 2·|Y_n(P) − Y_{n−1}(P)| at P = 0.4
  (no growth toward small P beyond a factor 2). Three verdict lines.
- Reported: Y_n(P) at all grid points; Y_n(0.05) against a_0 − ρ_n with ρ_n from checks/f12_out.txt (n ≤ 4) and with a_0
  from Part A.

## Part C: the vector bordered identity (finite-dimensional; SU(2), root sector at Cartan backgrounds)
Torus 6 × 6 × 3 × 3 (periodic), ℓ = 3 (n = 1; level lattice 2 × 2 × 1 × 1), Wilson action S = Σ_P(1 − ½Re tr U_P),
exponential chart U_b → U_be^{X_b}; H = root block of the Hessian of S (central finite differences of the analytic gradient,
symmetrised); D_U the covariant gradient (D_Uλ)_b = Ad(U_b^{-1})λ(x) − λ(x + μ); Δ_U = D_U^TD_U; M = derivative of the
straight-path decimation 𝔪(U)_{(X,μ)} = U_{ℓX,μ}U_{ℓX+e_μ,μ}U_{ℓX+2e_μ,μ}; 𝒞 = 1; ι, E', Ã, Δ', K_F, X, b, δ, g as in §73 (T4).
Backgrounds: U^flat = constant Cartan links exp(iσ_3θ_μ) with twists θ_μ chosen so that no root-sector zero mode exists; U^pw =
U^flat·exp(iσ_3 ε cos(p x_2 + ϑ)) on the 1-links, ε = 1e-3, p ∈ {2π/6, 4π/6}, ϑ = 0.3.
- C1: (T4) det identity log det Ã = log det K_F − log det 𝒞 + log det X + log det(δ + b^TX^{-1}b), relative error ≤ 1e-9 at
  U^flat and at U^pw (p = 2π/6). Two verdict lines.
- C2: ghost Jacobi log det Δ' = log det Δ_U + log det g, ≤ 1e-10 relative at U^pw. Verdict line.
- C3: M D_U = D_ℓ^{𝔪(U)}ι^T, max abs entry ≤ 1e-12 at U^pw. Verdict line.
- C4: at U^flat, max|δ| ≤ 1e-7 and max|b − D_ℓg| ≤ 1e-7. Two verdict lines.
- C5 (S10-F4): ||E_U||_F/ε at p = 4π/6 over the same at p = 2π/6 equals 3 within 1e-3 relative. Verdict line.
- C6: (T5) on the chain Λ_0 ⊃ Λ_1 (level-1 sites) ⊃ Λ_2 (one of them): log det(Δ_U|_{Λ_0∖Λ_2}) = Σ of the two step terms,
  ≤ 1e-10 relative at U^pw. Verdict line.
- Reported: max|E_U − E^formula| with E^formula_b = ½[Ad(U_b^{-1})λ(x) + λ(x + μ), ∇_bS]-type (the §79 (a) formula, sign and
  normalisation as derived there) — reported only; the sizes of δ, η at U^pw for both p.

## Output
Every verdict line is "[PASS]" or "[FAIL]" with the measured number and its threshold. Total line: number of PASS / total.
