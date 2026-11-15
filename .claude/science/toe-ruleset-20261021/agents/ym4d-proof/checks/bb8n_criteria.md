# bb8n criteria (lane B session 8; written after BFT_B §24 (11:12:37 UTC) and before checks/bb8n_lip.py)

Tests Theorem N2-loc (b), (c) (BFT_B §24.2) in the d = 2 SU(2) model of bb7n (its chain code is reused unchanged: the script
executes bb7n_chain.py's definitions up to its first test). Top torus side 12, DD8, depth 3 (levels k, k-1, k-2, k-3).
Top field: bb7n's construction (seeded Gaussian log, own) scaled by bisection so that f_k = 0.1000 (and 0.0500 for the scaling
test). F_j(p) := log hol(∂p) based at the first corner, coarse units (× 9^m at level k - m). Distances: ℓ^∞ coarse distance of
the first corners; offsets δ ∈ {(1,0), (0,1), (1,1), (2,1), (3,0), (3,3), (9,0), (9,4), (27,0), (27,27)} in level-j fine steps,
those with |δ|_∞ ≤ 3^m only (coarse distance ≤ 1). Transport τ(p, p'): the chain's links along axis 0 then axis 1.

- L-a (N2L-F1, Lipschitz): Lip_m := max over p and offsets of |F_j(p) - Ad_τF_j(p')|/(|p - p'|f_k), m = 1, 2, 3.
  PASS iff Lip_3 ≤ 1.25·max(Lip_1, Lip_2).
- L-b (gauge invariance of the covariant difference): under a Haar-random level-k gauge the field |F_j(p) - Ad_τF_j(p')| is
  unchanged to 1e-10 (all m, all offsets). PASS required.
- L-c (defects): D_m := max over level-(k-m+1) links of |d_j|_own/(ρ_{j+1}⁴f_k²), ρ_{j+1} = 3^{-(m-1)}, m = 1, 2, 3. PASS iff
  D_3 ≤ 2·max(D_1, D_2) and, at m = 1, 2, 3, the ratio D_m(f_k = 0.05)/D_m(f_k = 0.10) ∈ [0.5, 2] (second order in f).
- C (control): in the Haar-random gauge the non-covariant ratio max|F_j(p) - F_j(p')|/(|p - p'|f_k) ≥ 5·max_m Lip_m (PASS =
  the control behaves as predicted).
Resources: expected < 300 MB, < 3 min.
