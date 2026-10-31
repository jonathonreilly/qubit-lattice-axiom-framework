# f7 criteria (FLOW.md §29 target S4-2; written before checks/f7_cov_chain.py exists; append-only from now on; its stat is
# copied into FLOW_LOG.md before the script is created)

Purpose: the cheap check proposed in REVIEW_FLOW_S3 §6.3 (2): the composite-covariance term of the UNIFORM scalar U(1) chain
at fixed L = 3, levels n = 1..4 (ℓ = 3, 9, 27, 81), where the composite covariance is diagonal on level-n sites. It tests the
closed form of FLOW §30 Proposition COV-sc (written 03:46 UTC, before this file) by an independent route. It says nothing
about the SU(N) gauge chain (Lemma COV-str (iv): that chain has a non-contracting sector the scalar chain lacks).

Object. FLOW §30 Proposition COV-sc's setting: fine Z⁴; level-k sites L^kZ⁴, L = 3; covariant averages with the 24 axial
orders run on fine links; κ_j = sL^{2j}; 𝒞_n(A)(c, c) = Σ_{j=1}^nκ_j^{-1}Σ_{y_j∈B(c)}Π_{k=j}^{n−1}L^{-8}|w_k(y_k)|²;
Γ^cov_n = Σ_c log 𝒞_n(c, c). c_n := coefficient of ε² per fine site for the constant field F_12 = ε.
Brute route (the script): for every actual level-k site y_k of one level-n block (absolute fine coordinates; k = 1..n−1) and
every one of the 24 orders, the path phase is accumulated LINK BY LINK from a gauge field A_μ(x) given as a function on
fine links (traversing x → x + e_μ adds A_μ(x); x → x − e_μ adds −A_μ(x − e_μ)); the phase is linear in ε, so φ_σ := phase/ε
is computed at ε = 1. Second derivative at ε = 0 analytically: ∂²_ε|w_k|² = −2Var_σ(φ_σ); ∂_ε of everything vanishes at
0. Then c_n = ½(∂²_ε𝒞_n(c, c))/𝒞_n^0(c, c)/L^{4n}, with the chain sums done by explicit ancestor maps over all y_j ∈ B(c)
(no use of the factorisation or of the closed-form variance). Closed form: c_n = c_∞[1 − L^{-2(n−1)}(1 + L^{-2n})/(1 + L^{-2})],
c_∞ = −(L² − 1)/(576(L⁴ + L² + 1)).

Pre-registered criteria (validation):
- (P1) n = 1: |c_1| ≤ 1e-15 (the composite covariance has no background dependence at n = 1).
- (P4) gauge and position independence (n = 3): the brute c_3 with the gauge A_1(x) = −εx_2 (A_2 = 0), and with the gauge
  A_2 = εx_1 on the block centred at the level-3 site 27·(1, −2, 0, 3), each equal the reference c_3 to 1e-12 relative.
- (P5) s-independence (n = 3): s ∈ {0.25, 1, 4} give the same c_3 to 1e-12 relative.
Pre-registered criteria (the claim):
- (P2) |c_n^brute − c_n^closed| ≤ 1e-10·|c_∞| for n = 2, 3, 4.
- (P3) n = 2 reproduces f6's stored ℓ = 9 value: |c_2^brute − (−0.00013717)| ≤ 1e-8.
Pre-registered criterion (falsification of S4-F1 in this instance; a log ℓ would give increments c_{n+1} − c_n of fixed size):
- (F7) |c_4^brute − c_3^brute| ≤ 0.2·|c_3^brute − c_2^brute|, and |c_4^brute| ≤ |c_∞|(1 + 1e-10).
Informational: the finite-ε route (exact complex means |w_k|², log 𝒞_n(ε) at ε = 2e-4 and 1e-4, Richardson-combined
second difference) for n = 2, 3, 4; wall times; peak memory.
Reading rule (fixed now): any FAIL is reported as a FAIL. A PASS of (P2)/(F7) confirms Proposition COV-sc's algebra and the
bounded, geometrically convergent c_n in THIS scalar instance only; (U-IR)(c), (s2) for SU(N) remain OPEN whatever f7 gives.
Limits: NUMERIC LOCK; nice 10; 1 thread; expected wall time < 1 min, peak < 300 MB; a run over 20 min is aborted and reported.
Outcome in checks/f7_out.txt, checks/f7_time.txt.
