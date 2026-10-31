# s4 criteria (lane F, session 4). Written BEFORE checks/s4_sf.py exists. Not edited after the script exists.

Targets: SF.md §12 (pre-stated 05:20 UTC): Lemma HALO, Lemma SH, Theorem CE-Q-col constants, RATE-Q, RT-1 norm thresholds,
SN-1 display, Lemma TILT, Proposition RES. Labels: EVIDENTIAL (could fail if the derivation is wrong), LOW-POWER (a theorem or
construction-level identity; informational), ARITHMETIC (reproduces numbers; non-evidential). OVERALL = PASS iff every criterion
below passes. A negative control is expected to FIND a violation; it passes iff it does.

## A. Lemma HALO (EVIDENTIAL). Tori of cubes in d = 2 (side 64) and d = 3 (side 36), ℓ^∞ index distance with wrap-around.
Random Q-cubes (density chosen so that several classes occur), each with a random halo length ℓ ∈ {1, 2, 3, 4}; halo = cubes within
ℓ - 1 of q(y); R = union of halos; classes = components of R under "index distance ≤ 7"; W = R̄^{(2)}, U = R̄^{(7)}, U^+ = R̄^{(8)}.
At least 30 random trials per dimension.
- A1 (HALO (a)): for every cube c whose 1-neighbourhood misses R (a small single-cube X) and every Q-site y: dist(q(y), c^{(1)}) ≥ ℓ_y.
  Also for every small 2^d-box X. PASS iff 0 violations.
- A2 (HALO (b)): for every class α, every Q-site y of another class with q(y) ∉ U_α^+: dist(q(y), U_α^+) ≥ max(1, ℓ_y - 1) and ≥ ℓ_y/2.
  PASS iff 0 violations.
- A3 (HALO (c)): for every class α and every Q-site y of another class with q(y) ∈ U_α^+: dist(q(y), W_α) ≥ ℓ_y + 5. PASS iff 0
  violations AND at least one such (α, y) pair occurs (non-vacuous).
- A4 (HALO (d)): |W_α| ≤ Σ_{y∈Q_α}(2ℓ_y + 3)^d, |U_α| ≤ Σ(2ℓ_y + 13)^d, |U_α^+| ≤ Σ(2ℓ_y + 15)^d, U_α connected under ℓ^∞-adjacency.
  PASS iff 0 violations.
- A5 (HALO (e)): every 2^d-box X with X^+ ∩ R ≠ ∅ lies in W_α for exactly one α. PASS iff 0 violations.
- A6 (non-vacuity): the number of (α, y) pairs tested in A2 with ℓ_y ≥ 2 is ≥ 50 (both dimensions together).
- A7 (NEGATIVE CONTROL, power): the stronger statement "dist(q(y), U_α^+) ≥ ℓ_y" (what a 2 log 2 halo would need) is VIOLATED at least
  once in the A2 population. PASS iff ≥ 1 violation is found.

## B. Lemma SH (EVIDENTIAL, moderate power). Exact formula Γ_j = exp(2κ̂(2ℓ_j+13)⁴ + w_8(2ℓ_j+15)⁴ + 2h_0(2ℓ_j+3)⁴),
ℓ_j = ⌈4(j+1)log 2/(μM)⌉, κ̂ = κ_c - κ_0 - κ̃_0 - 2, on the grid κ_c ∈ {810, 1478.5, 2500, 10000}, μM ∈ {μM_W3(κ_c), 2μM_W3,
10μM_W3} (μM_W3 := the smallest μM allowed by (M-W3) with M solved from it at μ = m_1 = 4.83e-11), p ∈ {2, 2.5, 5, 50},
h_0 ∈ {0, 1}; j from 0 to J := 3⌈μM/(4 log 2)⌉ + 10 (so ℓ_j ≥ 2 occurs).
- B1: the pointwise inequality log Γ_j - log Γ_0 ≤ (4^j - 1)p²/32 holds at every grid point and every j ≤ J. PASS iff 0 violations.
- B2: Σ_{j=0}^{J}Γ_je^{-4^jp²/16} ≤ 2Γ_0e^{-p²/16} at every grid point. PASS iff 0 violations.
- B3 (non-vacuity): at every grid point some j ≤ J has ℓ_j ≥ 2, and max_j(log Γ_j - log Γ_0) > 0 somewhere on the grid.

## C. Constants (ARITHMETIC). κ_0 = 16 log 12800, K_0 = e^{κ_0}/6400, C_K = 32eK_0, a' = log(2·624²), κ̃_0 = 16a',
K̃_0 = e^{κ̃_0}/624², B̃ = 625C_Ke^{κ̃_0}K̃_0, C̃_1 = 2κ̃_0B̃, w_8 = Σ_{n≥1}(2n+1)⁴e^{-8n}, L = 3.
- C1: κ̃_0 ∈ [217.04, 217.05]; log B̃ ∈ [574.6, 574.8]; log C̃_1 ∈ [580.7, 580.8].
- C2: CE-col rate threshold κ_c^* = (6κ_0 + 6κ̃_0 + 10 + 64 log 2 + 1296w_8)/2 ∈ [1149.9, 1150.0].
- C3: CE-col d ≥ 1 norm threshold in SF's displayed form (§10.3: log[16L⁴K_0·2^{16}e^{r}C̃_1·2^{16}e^{1296w_8}] -
  (κ(L-1) - κ_0L - 1) ≤ 0, r = κ_c - κ_0 - 2κ̃_0 - 3, κ = r - 16 log 2): first κ_c with log ratio ≤ 0 lies in [1850, 1858]
  (the reviewer's ≈ 1854), and the log ratio at κ_c = 1149.92 lies in [703, 704.2].
- C4: the same with the next stage's input rate κ_in := κ_c + 16 log 2 + 1296w_8 in place of κ in the exponent (exponent
  (κ - κ_0)L - 1 - κ_in): report the threshold (no pass band; ARITHMETIC record); PASS iff it is finite and > C3's threshold.
- C5: CE-Q-col rate threshold κ_c^{Q*} = (6κ_0 + 9κ̃_0 + 16 + 64 log 2 + 1296w_8)/2 ∈ [1478.4, 1478.7]; report the CE-Q-col norm
  thresholds (both forms, H''_0-dominated, factor 2 of Ĥ_0 included).
- C6 (SN-1): e^{0.0151515…}/(1 - (e^{1/120} - 1) - (e^{0.0151515…} - 1)) ∈ [1.0398, 1.0399], and the rounded display
  e^{0.0152}/0.9762 > 1.04.
- C7: Σ_{j≥1}e^{-(4^j - 1)/8} ≤ 1.
- C8: p_0 (smallest p with M⁴η̂ ≤ 1/32, N = 3, n = 32, h_0 = 0, M = M_W3, κ_c = 1478.5) for CE-Q-col is smaller than the session-3
  CE-Q p_0 computed with η̂_3 = e^{274κ̂_3}·4Γ_32^{n/2}e^{-p²/16}, Γ_3 = exp(546·15⁴κ̂_3 + 17⁴w_8), κ̂_3 = κ_c - κ_0, at the same κ_c and M.

## D. Lemma TILT and Proposition RES (EVIDENTIAL).
- D1 (TILT): 20 random symmetric K ≥ 0 in dimension 6 with ||K|| ≤ 1 (spectra random in [0, 1], some with eigenvalues ≥ 0.99), θ ∈
  {0, 0.3, 0.6, 0.9}, E = {⟨v,Kv⟩ ≥ s}, s ∈ {0, 2, 8}: Monte Carlo (2·10⁵ standard Gaussian samples per K) estimate of
  ∫_Ee^{θ⟨v,Kv⟩/2}dγ plus 4 standard errors is ≤ exp((1+θ)tr K/(2(1-θ)))·e^{-(1-θ)s/4}. PASS iff 0 violations. Report the max ratio.
- D2 (RES witness): SU(2), d = 2 periodic 4×4 sites, blocks of side 2 with centres c_X at the even-even sites, random background
  U_b = exp(0.2·random su(2)); h(A)(X) := (1/4)Σ_{y∈B(X)}ℓ_{P(c_X→y)}(A) with the axial path "axis 0 then axis 1" (NA-FP's ℓ_P);
  λ ∈ Λ (λ(c_X) = 0), A(λ)_b := log(e^{λ(x)}U_be^{-λ(y)}U_b^{-1}). Starting from 5 random λ_0 ∈ Λ of sup-size 0.3, a Gauss-Newton
  projection onto {h(A(λ)) = 0}. PASS iff for at least 3 of 5 starts: converged |h(A(λ))|_∞ ≤ 1e-10, max_b|A(λ)_b| ≥ 0.1,
  max_b||A_b||_op < π, the reconstruction max_b||e^{A_b}U_b - g(x)U_bg(y)^{-1}|| ≤ 1e-10 and the plaquette spectrum unchanged
  (max_p | ||1 - (e^AU)_p||_op - ||1 - U_p||_op | ≤ 1e-10). (The plaquette identity is construction-level; the evidential part is
  the existence of non-small zeros of h∘A away from λ = 0.)
- D3 (control): for 5 random A in ker h (linear projection) with max_b|A_b| = the D2 witness's value, the max plaquette-norm change
  is ≥ 1e-3 in every case (typical slice directions do move plaquettes; the D2 witnesses are special).

Lock: the mandated mkdir loop; nice 10; OMP/OPENBLAS/MKL/VECLIB threads 1; python3 without -I; no `timeout`; exactly one rmdir.
Criteria are not edited after the script exists.
