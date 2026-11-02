# h2_55_c — obstruction examples (pre-registered in HINT2_55's PRE-STATED as h2_55_c; criteria written 2026-10-29T03:46Z,
# before any h2_55_c script)

Owner: HINT2_55.md (claude-opus-5-5). Exact sympy only; no floats. nice 10.
Purpose: (1) wrapped-normal monotonicity — for a centred Gaussian X of variance v, the bounded compact observables
B(X) = 2(1 − cos X) and Ψ(X) = 2·dist(X, 2πZ)² have expectations strictly increasing in v (so, within Gaussian laws, the
literal bounded observable inherits KLM monotonicity from Var X; Codex's compound-Poisson obstruction needs non-Gaussian
noise); (2) the scalar-GFF identification example is A7 of h2_55_a (not repeated).

## Gates
- **C1** E[cos X] = e^{−v/2} for X ~ N(0, v) (sympy integral), hence d/dv E[B] = e^{−v/2} > 0.
- **C2** ∫_{−π}^{π} y² dy/(2π) = π²/3 and, for symbolic integer n ≥ 1, ∫_{−π}^{π} y² cos(n y) dy = 4π(−1)^n/n².
- **C3** With the wrapped-normal Fourier series p^{wrap}_v(y) = (2π)^{−1}(1 + 2Σ_{n≥1}e^{−n²v/2}cos ny) (Poisson summation,
  IMPORTED-standard), C2 gives E[dist(X, 2πZ)²] = π²/3 + 4Σ_{n≥1}(−1)^n e^{−n²v/2}/n², and term-wise
  d/dv = 2Σ_{n≥1}(−1)^{n+1}e^{−n²v/2}; the terms e^{−n²v/2} are strictly decreasing in n for v > 0 (ratio of consecutive terms
  e^{−(2n+1)v/2} < 1, checked symbolically), so the alternating sum is ≥ e^{−v/2} − e^{−2v} > 0.
- **C4** (cross-check of C3's series at one point, exact) the n-sum of the derivative's first two terms
  e^{−v/2} − e^{−2v} is > 0 for v = 1/10, 1, 10 (sympy decides the sign exactly).
## Designed-FAIL controls
- **C1-F** a wrong Gaussian characteristic function e^{−v} (missing ½) must disagree with the C1 integral.
- **C2-F** the claim ∫y²cos(ny) = 4π/n² (no (−1)^n) must fail at n = 1.
PASS = all gates hold and both controls fire.
