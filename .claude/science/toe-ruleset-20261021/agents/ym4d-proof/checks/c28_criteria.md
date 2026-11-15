# c28 criteria: N2-exp (exponential locality) and IT' (composite slice) — written BEFORE checks/c28_exp.py

Session 13, 2026-10-27. Targets: RTARGET.md §24-25. The proof chain being checked is PROOF.md L5 [S13]
(Lemmas EXP-id, EXP-real, EXP-strip, Theorem N2-exp; Lemma IT-line, Proposition PG^{(k)}). The explicit strip width
η_* = η_*(κ, κ̂, L) is computed by the arithmetic of Lemma EXP-strip (re-implemented in the script exactly as written in
PROOF): η_*(1, 1, 3) ≈ 0.0110 (r_0 = 0.55), η_*(0.25, 1, 3) ≈ 0.0076 (r_0 = 0.35), η_*(4, 1, 3) ≈ 0.0118 (r_0 = 0.65).
Disclosure: these three numbers were computed (scratch arithmetic of the bound chain) before this file was written;
no kernel, symbol or singularity numerics of session 13 had been run. The session-12 review's measured r-kernel ratio
(≈ 0.30 per coarse unit, T = 32) was known.

Notation (as in PROOF): β_μ := aδ_μ + φR_μ, a := κΠ_αδ_α, Ψ := 1 - Σ_μφ_μR_μ/β_μ, Σ := Σ_μΔ_μ/β_μ, Z_μ the K ≠ 0 alias
sum, R_μ = A_μ + κZ_μ, all with the K = 0 alias at p (Re p ∈ [-π, π]^4). d = 4, L = 3 throughout.

## Part A: exact identities (d = 4; T ∈ {8, 12}; k ∈ {1, 2, 3}; κ ≡ 1 and κ = (0.5, 1, 2)[:k])
- A1. On p ≠ 0: max|𝓡̂_c26 - (-aν̄_ν/(β_μβ_νΨ))| ≤ 1e-9·max|𝓡̂_c26| (𝓡̂_c26 := c26 R_symbol with c26 P_symbol).
- A2. Same with -φν̄_ν/(β_μβ_νΣ).
- A3. max|aΣ - φΨ| ≤ 1e-12·max|φ|.
- A4. B_k-form of r: for 3 random coarse 1-forms b̂, c26 r_from_b equals the PROOF b-formula to ≤ 1e-9 (relative).
- A5. f_0, K = 0 alias term, as a map of b̂ (u = (0,0,0,0) and u = (1,2,0,1) mod n): the c26-form
  -κe^{ip·u/n}[ν^{(n)}_ρW_σr̂_σ - ν^{(n)}_σW_ρr̂_ρ]/φ (p ≠ 0) equals the PROOF analytic formula to ≤ 1e-9 (relative).
- A6 (informational). Ψ at the smallest grid momentum, and the PROOF formulas evaluated at p = 0 (finite; Ψ(0) = 1).

## Part B: strip inequalities at complex points (n = 3, 9, 27, i.e. k = 1, 2, 3; κ ∈ {1, 0.25, 4}, κ constant)
Points: 150 random x ∈ [-π, π]^4 plus x = 0, the corner (π, π, π, π), (π, 0, 0, 0), (r_0, 0, 0, 0), (r_0, r_0, 0, 0)/√2;
for each, 4 values of y with |y_α| ≤ η_* (two random, two with every |y_α| = η_*). Alias sums exact (finite K-sums).
For n = 27 only 40 random x (cost). Each sub-check PASS iff it holds at every point:
- B1. |Z_μ(z) - Z_μ(x)| ≤ c_Z and Z_μ(x) ≤ 1/9.
- B2. |β_μ(z) - β_μ(x)| ≤ ρ_β β_μ(x), and β_μ(x) ≥ b_* := min(κ, 24/π²).
- B3. For |x| ≤ r_0: Ψ(x) ≥ Ψ_U and |Ψ(z) - Ψ(x)| ≤ e_Ψ.
- B4. For |x| ≥ r_0: Re Σ(z) ≥ (ψ(x)/min_μβ_μ(x))·br_V.
- B5. β_μ(x) ≤ Γ β_ν(x) for all μ, ν.

## Part C: decay rates (κ ≡ 1)
Kernels (max over entries, along the axis X = (x, 0, 0, 0)):
- 𝓡 (F ↦ r) at T ∈ {16, 24, 32}, k ∈ {1, 2, 3};
- B_k ↦ r, and B_k ↦ f_0 at the fine offsets u = (0, 0, 0, 0) and u = (1, 0, 0, 0), at T ∈ {16, 24}, k ∈ {1, 2};
- informational: the session-12 F-representative 𝒦̂_u + Π_coex at u = (1, 0, 0, 0), T ∈ {16, 24}, k = 1.
Rate m_meas: least-squares slope of -log max|K(x e_1)| over x ∈ [4, T/2 - 4], using only points with value
> 1e-12·max|K|.
- C1. Every m_meas of 𝓡 and of the two B_k-kernels is ≥ η_*(1, 1, 3) (the proven rate).
- C2. k-stability: for each (kernel, T), max/min of m_meas over k ≤ 1.10.
- C3. T-stability (𝓡): max/min of m_meas over T ∈ {16, 24, 32} at each k ≤ 1.10.
- C4. Singularity prediction (k = 1, n = 3, κ = 1): the smallest Im w > 0 with Ψ = 0 or some β_μ = 0 at
  z = (w, p_2, p_3, p_4), p_2..p_4 ∈ {0, π/2, π} (all sorted combinations), Re w ∈ [-π, π], found by a grid on
  (Re w, Im w) ∈ [-π, π] × (0, 3] (step 0.05) and Newton refinement. C4 PASS iff |m_meas(𝓡, k = 1, T = 32) /
  m_sing - 1| ≤ 0.15.
- C5 (informational). The f_0 representative 𝒦̂_u + Π_coex: its fitted log-log slope and exponential rate, and
  whether a power law fits better (no PASS/FAIL).

## Part D: IT' (d = 4, L = 3, k = 2, n = 9, coarse T = 2, fine side 18)
Q^{(1)} := Q_str - dh (the L3g(a)-slice identity, PROVEN and checked exactly in c8); h at each level computed directly
from the axial S4' paths (24 orders σ). Test fields: 5 random; one supported on the axial lines through the block
centres; one on the central 3^4 fine sub-block; one constant on the whole fine lattice.
- D1. h^{(2)} by the recursion h^{(2)} = Mh^{(1)} + h(Q^{(1)}A) equals the unrolled formula of Lemma IT-line to ≤ 1e-12.
- D2. h^{(2)}(dλ) = Mλ - λ(c_X) for 3 random λ, ≤ 1e-12.
- D3. Q^{(1)}(Q^{(1)}A) = Q_str^{(9)}A - dh^{(2)}A, ≤ 1e-12.
- D4. |h^{(2)}(A)(X)|² ≤ (4L²/(L-1))Σ_{b∈B(X)}|a_b|² for every X and every test field (lattice units): max ratio ≤ 1.

(Two phrasing slips in Part C/D were tidied at 16:52 UTC, before any c28 script existed.)

Result: each part PASS iff every non-informational criterion in it holds. Resources: one job, nice 10,
OPENBLAS/OMP/MKL threads = 1, load < 8, ≥ 25% free memory before start, peak < 1.5 GB (Part C at T = 32 computes one
kernel entry at a time); peak memory and time reported. No criterion is edited after a run; later changes go in an
addendum with time stamps.

## Addendum (written 16:52 UTC, BEFORE any c28 script existed)
- **C-window.** The fit window x ∈ [4, T/2 - 4] has a single point at T = 16. It is replaced by x ∈ [3, T/2 - 2]
  (T = 16: 4 points). Images at T - x bias the last points by ≲ e^{-4m}; this is accepted.
- **C4 denominator.** "Ψ = 0 or some β_μ = 0" is imprecise: a zero of β_μ alone is cancelled (Ψ has a pole there and
  β_μβ_νΨ stays finite for ν ≠ μ). The singular set of 𝓡̂ (entries ν ≠ μ) lies in the zero set of
  Den := Ψ·Π_ρβ_ρ = Π_ρβ_ρ - Σ_ρφ_ρR_ρΠ_{σ≠ρ}β_σ. C4 searches the zeros of Den, with the same grid, combinations and
  tolerance.
- **Part A, Z_μ.** On the real grid Z_μ is computed by an independent factorised Laplace quadrature of the K ≠ 0 sum
  (not by c26's G); Part B uses exact finite alias sums. Informational: Laplace vs exact Z at 20 real points, n = 9.
