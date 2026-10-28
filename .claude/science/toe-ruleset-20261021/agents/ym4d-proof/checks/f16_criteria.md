# f16 criteria (session 13, lane C; written before any f16 script)

Statements tested: FLOW.md §103 (X2) Lemma Cartan-𝔪, (X3) Lemma Cartan-T, (X4) Proposition SLICE-U, (X5) Proposition VC-T1 /
Lemma P-poles. Conventions of §103: U_b = exp(a_bH_1), H_1 = i diag(h); root (i, j), q = h_i − h_j; fluctuation U_b → U_b expm(X_b),
X_b = φ_be_{ij} − φ̄_be_{ji}; (D_Uω)_{x,μ} = e^{−iqa_{x,μ}}ω(x) − ω(x + e_μ); blocks {LX..LX + L − 1}, roots c_X = LX + 1, L = 3; S4'
contours T^σ_y = P^σ(c_X → y)S_yP^σ(c_Y → y + 3e_μ)^†, 24 orders, 81 offsets, uniform weights. Chain map 𝔪 = W_♮∘M̄ (M̄ the mean
of the T^σ_y; W_♮ = polar part for SU(2), maximiser of Re tr(V^{-1}M) over SU(3)); S4' map 𝔪^{S4'} = S_c exp(avg log(S_c^{-1}T)).
Every verdict line is PASS/FAIL against the threshold stated here; thresholds are not changed after the run.

## Part A (4D, fine torus 9⁴, coarse 3⁴; Cartan plane wave a_{x,1} = ε cos(p x_2 + ϑ), p = 2π/9, ϑ = 0.4)
Groups: SU(2), h = (1/2, −1/2), root (1,2); SU(3), h = (0.7, −0.2, −0.5), roots (1,2) (q = 0.9, h̄ = 0.25) and (1,3) (q = 1.2,
h̄ = 0.1). Base amplitude ε = 0.25 (domain: the largest |eigen-angle| of S_c^{-1}T^σ_y is printed and must be < π/3).
- A1a: 𝔪^{S4'}(U) = exp((Q_root a)H_1) (max entry error) ≤ 1e-12, and the coarse angle equals ε_1cos(3pX_2 + ϑ_1) on direction-1
  links (ε_1 = ε sin(3p/2)/sin(p/2), ϑ_1 = ϑ + p), 0 on the other directions, ≤ 1e-12.
- A1b: chain 𝔪(U): max |off-diagonal| ≤ 1e-13; oddness max|φ(−ε) + φ(ε)| ≤ 1e-12·max|φ(ε)|; deviation dev(ε) := max|φ(ε) −
  h·(Q_root a)| has ratio dev(ε)/dev(ε/2) in [7, 9].
- A2: closed forms (X3) (a) (chain) and (b) (S4') against central differences (t = ±1e-5) of the nonlinear maps along
  U_b expm(tX_b), random complex φ on all fine links (seeded), E_α-coefficient of log(V_0^{-1}V(t)): relative ℓ² error ≤ 1e-7, each
  group/root/map.
- A2c (control): the chain map with N_T/avg N̄_T replaced by 1 (T = avg_Tξ_T): relative error ≥ 1e-3.
- A3a: covariance T(U)D_Uω = D_{U'}ev ω (closed forms, random ω): relative ≤ 1e-12, both maps.
- A3b: r(ε) := ||T_chain φ − T_S4' φ||/||T_chain φ||; ratio r(ε)/r(ε/2) in [3, 5].

## Part B (SU(2), q = 1, chain map, Π = 1, κ = 1)
Levels: bottom b on torus (27, 27, 18, 18) → level n−1 (9, 9, 6, 6) → level n (3, 3, 2, 2). Bottom background a_{X,1} = ε cos(P_bX_2 + 0.3),
P_b = 2π/27 (level-n momentum 2π/3 along e_2), other directions 0; levels n−1, n carry the exact Cartan images (coarse angle θ' =
2 arg avg_Te^{iθ_T/2}). Slice: h_U(φ)(X) = −avg_{σ,y}e^{iqθ_P}ξ_P(φ), P = P^σ(c_X → c_X + y); Q_k := T_k + D^{(k+1)}(U)h_{U,k}; ev = value at
the root. s_i := A^{(i)}A^{(i)*}, A^{(1)} = T_{n−1}, A^{(2)} = T_{n−1}T_b; P := 1 − D_nΔ^+D_n^*. Coefficients [ε], [ε²] from central
differences at δ = 0.02 and 0.04, Richardson-combined (error O(δ⁴)). "Sector norm" := operator norm after projecting both sides
onto the level-n momentum sectors (K_1, K_3, K_4) ≠ (0, 0, 0) (the background preserves these sectors).
- B1: at ε = 0.04: ||A^{(2)} − (Q_{n−1}Q_b − D_nh^{(2)})|| / ||A^{(2)}|| ≤ 1e-11 (h^{(2)} = ev h_b + h_{n−1}Q_b); ||P(A^{(i)} − Q^{(i)})|| /
  ||A^{(i)}|| ≤ 1e-11 (i = 1, 2); ||T_kD^{(k)}ω − D^{(k+1)}ev ω|| / ||T_kD^{(k)}ω|| ≤ 1e-12 (k = b, n−1; random ω).
- B2: c_r(i) := sector norm of [ε^r](P s_i P); c_r(2)/c_r(1) ≤ 0.25 for r = 1 and r = 2 (theory: ≈ L^{-2} up to a factor
  (1 + O(L^{-1}))). q_r(i) := ||[ε^r]Q^{(i)}|| (full operator norm); q_r(2)/q_r(1) ≤ 0.6 for r = 1, 2 (theory ≈ L^{-1}(1 + ρ)).
- B3 (control, the U = 1 bookkeeping): ℒ^{(i)} := [ε]P (1 − P^0) s_i^0 (1 − P^0) [ε]P (superscript 0: ε = 0). On the sectors:
  λ_min(ℒ^{(i)} − (1/8)P^0D_1D_1^*P^0) ≥ −1e-10 (i = 1, 2), D_1 := [ε]D_n; and ||ℒ^{(2)}|| / ||ℒ^{(1)}|| ≥ 0.5.
- B4: λ̃(K)λ̃(K+P)[ε]P(K+P ← K) from the finite differences against the closed form of Lemma P-poles (first-order perturbation
  in symbols), max over all level-n K on the sectors: ≤ 1e-7 (absolute; entries O(1)).

Diagnostics printed (no verdict): c_0(i); the termwise first-order piece ||[ε]P (1 − P^0)s_i^0P^0||; ||[ε]Q'^{(i)}|| with the U = 1
pairing Q'^{(i)} := A^{(i)} + D_n(1)h^{(i)}(1); timings; peak RSS.

Run conditions: one NUMERIC LOCK acquisition per run, nice 10, all BLAS threads 1, plain python3 (no -I), no `timeout`; start only
if load < 8 and memory free ≥ 35% (checked inside the lock); job < 20 min, peak RSS < 1 GB.
