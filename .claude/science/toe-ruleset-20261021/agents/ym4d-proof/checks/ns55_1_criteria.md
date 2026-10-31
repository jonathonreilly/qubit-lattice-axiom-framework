# ns55_1 — criteria (written before the script; NSL55.md, Opus 5.5, claude-opus-5-5)

Written (UTC) 2026-10-29, before `ns55_1_witness.py` exists.

## What is checked
NSL55 §1 claims an explicit witness that the depth-k elliptic slice is not preserved under restriction to depth j < k:
for constant data B_k = h·τ·e_1 the depth-k slice critical point has level-0 component y = c·e_1 + dν
(c = L^{-k}hτ, ν = -c(z_1 - I_k z_1)), and Λ^{(j)}(y) = -c·(1 - I_j)(I_k[z_1]), which reduces (tensor-product tents) to the
1D function ψ := (1 - I_j)(I_k[z_1]) on a level-k cell. The claim is ψ ≢ 0, with the closed form
ψ(c_X + e_1) = n_k[p(1/n_k) - p(n_j/n_k)p(1/n_j)] < 0, p(t) = 10t³ - 15t⁴ + 6t⁵, n_i = L^i.
The 4D -> 1D reduction and the box-Coulomb formula λ_X(c e_1 + dν) = -c(z_1 - c_{X,1}) - ν + ν(c_X) are proved in the text,
not by this check. This check verifies only the exact 1D interpolation arithmetic.

## Method
Exact `fractions.Fraction` arithmetic, plain python (`python3 -I`), no floats in any verdict.
On one level-k cell, m = 0..n_k: g(m) := n_k p(m/n_k) (= I_k[z_1] - c_X); for the level-j cell [a, a + n_j] containing m
(a = n_j·floor(m/n_j), s = m - a): I_j g(m) := g(a)(1 - p(s/n_j)) + g(a + n_j)p(s/n_j); ψ(m) := g(m) - I_j g(m).
Cases (L, j, k): (3,1,2), (3,1,3), (3,2,3), (5,1,2), (7,1,2), (3,1,4).

## PASS / FAIL (pre-registered)
- C1 (control): ψ(m) = 0 at every level-j root m ∈ n_j·Z ∩ [0, n_k]. FAIL if any nonzero.
- C2 (control): tent partition of unity σ_5(t) + σ_5(1 - t) = 1, i.e. p(t) + p(1 - t) = 1, at every sample t = s/n_j and
  t = m/n_k used. FAIL if any violation.
- C3 (claim): ψ(1) ≠ 0, ψ(1) equals the closed form exactly, and ψ(1) < 0. FAIL if any of the three fails in any case.
- C4 (claim, reported): the number of m in [0, n_k] with ψ(m) ≠ 0 is ≥ 1 in every case.
- C5 (designed-FAIL control): with the linear profile p_lin(t) = t in place of p (hat tents, which reproduce linear
  functions) the same code must give ψ_lin ≡ 0 in every case. FAIL of the CHECK if ψ_lin has any nonzero value (that
  would mean the code, not the tents, produces the nonvanishing).
- C6 (informational, decides nothing): dimension count rank Λ^{(i)} ∝ N_0 - N_i with N_i = (T L^{k-i})^4 for T = 3:
  print N_0 - N_j and N_0 - N_k to record the direction of the inequality (GV55 §3.3 states it reversed).
- Overall verdict PASS iff C1, C2, C3, C4, C5 all hold in every case.
