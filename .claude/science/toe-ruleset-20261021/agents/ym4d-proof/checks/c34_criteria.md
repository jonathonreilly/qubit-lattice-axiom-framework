# c34 criteria (written BEFORE checks/c34_n5triv.py; session 18, 2026-10-27, after PROOF.md's [S18] N5-triv block)

Purpose: instances of the elementary constants and the abstract lemma behind Theorem N5-triv (PROOF.md [S18]): the slice
weight vector w (Lemma N5-sl), the block Neumann gap and the residual-group operator (Lemma N5-coer step 1), and Lemma CT.
It does NOT test the full per-level operator O_i (that would need the chain energy E_i; Theorem N5-triv's other inputs
are ledger theorems with their own checks). Three parts, each its own job (`python3 c34_n5triv.py A|B|C`), one job at a
time, nice 10, OPENBLAS/OMP/MKL/vecLib threads 1, no `timeout`. No tolerance beyond those written here.

## Part A: the slice weight vector (d = 4, L = 3)
w(b) := (1/(24·81))·Σ_{σ, y∈B} (signed number of times the complete-axial path P^σ(c → y) traverses b), c the block centre.
- **A1:** ||w||_2 ≥ (L - 1)/(8L) = 1/12. **A2:** Σ_b|w(b)| ≤ 2(L - 1) = 4. **A3:** max_b|w(b)| ≤ 1. **A4:** every b with
  w(b) ≠ 0 has both ends in B. **A5 (informational):** print ||w||², Σ|w|, w(b_0) for b_0 = (c, c + e_1).
- PASS iff A1-A4.

## Part B: Neumann gap and the residual-group operator (d = 4, L = 3, fine torus (Z/6)⁴, 16 blocks)
- **B1:** the second-smallest eigenvalue of the graph Laplacian of the grid {0,1,2}⁴ equals 2(1 - cos(π/3)) = 1 to 1e-10.
- **B2:** with Δ_0 the torus scalar Laplacian and P_res the orthogonal projector onto Λ_res = {λ : λ(c_X) = 0, Σ_{B(X)}λ = 0},
  the smallest eigenvalue of P_resΔ_0P_res restricted to Λ_res (dense, via an orthonormal basis of Λ_res) is ≥ 1 - 1e-10.
- **B3:** for 5 random λ ∈ Λ_res (seed 0): ||P_resΔ_0λ||² ≥ (1 - 1e-10)·||dλ||², and h(dλ) = 0 to 1e-12 (h the slice
  functional with Part A's w on every block).
- PASS iff B1-B3.

## Part C: Lemma CT on random instances
Grid Z/40 (d = 1, ℓ¹ metric on the cycle) and (Z/12)² (d = 2). K := γ_0·1 + V with V symmetric, V(x, y) = u_{xy}e^{-μd(x,y)}
for d ≤ 4 (0 otherwise), u iid uniform in [-1, 1], scaled so that λ_min(K) ≥ γ_0/2 (γ := λ_min(K)); μ = 1, γ_0 ∈ {0.5, 1, 2};
seeds 0-3. For each instance take the largest m on the grid {0.01, 0.02, …, 1.0} with D_m(|K|) ≤ γ/2.
- **C1:** if such m exists: max_{x,y}|K^{-1}(x, y)|e^{md(x,y)} ≤ 2/γ.
- **C2:** same m: max|K^{-1/2}(x, y)|e^{md(x,y)} ≤ 2/√γ (K^{-1/2} by eigendecomposition).
- **C3:** for t ∈ {0.5, 2, 10}: max|(K + t)^{-1}(x, y)|e^{md(x,y)} ≤ 2/(γ + t).
- **C4 (power):** an m was found in at least 20 of the 24 instances.
- PASS iff C1-C4 (no float tolerance: the bounds are not expected to be tight).
