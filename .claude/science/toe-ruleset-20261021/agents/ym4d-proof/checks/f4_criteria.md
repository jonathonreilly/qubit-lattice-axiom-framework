# f4 criteria (written 2026-10-27 23:08 UTC [file mtime], before checks/f4_flow_shoot.py)

Purpose. Arithmetic check of Theorem F-flow / F-tune (FLOW.md §8-§9) on synthetic admissible step data. It checks the
written constants and the shooting argument, not any physics input.

Synthetic data. N = 3, L = 3, β_0' = 11N²/(12π²). One-loop numbers b_k = β_0' log L + d_k with d_k := A L^{-2k}cos(1.3k) +
A'·(cos(0.7(k+1)) - cos(0.7k)) (so the partial sums of d_k are bounded; R := sup_{j≤n}|Σ_{k=j}^{n-1}d_k| computed
exactly on the range used, A = 2, A' = 0.5). Remainder ρ_k(g_0, …, g_k) := C_ρ g_k² sin(5k + 17g_0) (continuous in g_0,
|ρ_k| ≤ C_ρg_k², not monotone), C_ρ = 3; δβ_k := g_k⁶cos(k). γ chosen with (C_ρ + 1)γ² = ½β_0' log L (δβ absorbed by
C_ρ → C_ρ + 1, since g⁶ ≤ g² for g ≤ 1). u_{k+1} = u_k - b_k - ρ_k - δβ_k.

Pre-registered criteria:
- (A) (F-3): for 50 values of g_0 on a grid in (0, γ] and K = 200, on every run's admissible prefix (g_0, …, g_{n-1} ≤ γ),
  β_-(n - j) log L - R ≤ u_j - u_n ≤ β_+(n - j) log L + R for all j ≤ n: zero violations.
- (B) (F-4): for K ∈ {10, 100, 1000} and g ∈ {g_1, g_1/2, g_1/10}, the scan-plus-bisection of FLOW §9 finds g_0 ∈ (0, γ]
  with |u_K - g^{-2}| ≤ 1e-9·g^{-2} and max_k g_k ≤ γ: 9/9.
- (C) the two-sided tuned bounds of (F-4) hold for those 9 runs at every k: zero violations.
- (D) informational: g_0(K, g)^{-2}/(β_0' K log L) for K = 1000 (→ 1 slowly).

Outcome in checks/f4_out.txt, checks/f4_time.txt. A FAIL is reported as a FAIL.
