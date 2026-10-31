# bb2 criteria (BFT lane B session 2; written 2026-10-28 ≈05:50 UTC, before checks/bb2_symbol.py exists)

Target: BFT_B.md §5.1 Theorem BB-4♮ (a)-(c) at k = 1, quadratic part, trivial background, d = 4, L = 3, abelian fibre model of
c37/bb1 (one colour). Object: the level-1 Hessian symbol H_1(K) (4×4, coarse momentum K) computed exactly as in bb1_decay.py
`hats` (x = -Cg[:, :6], H_1 = -κ(Qx)d1), at off-grid momenta K = t·n. Wilson symbol H_W(K) := d1c(K)^†d1c(K).
Directions n ∈ {(1,0,0,0), (1,1,0,0)/√2, (1,1,1,1)/2, (1,2,0,3)/√14}; t ∈ {0.4, 0.2, 0.1, 0.05, 0.025}; complex128 throughout.
Transverse unit vectors e: two orthonormal vectors orthogonal to d0c(K) (Gram-Schmidt from the real basis).

- **B2-1 (gauge invariance).** max over (t, n) of ||H_1(K)d0c(K)|| / (||H_1(K)||·||d0c(K)||) ≤ 1e-8.
- **B2-2 (marginal coefficient c_1 = 1, F-tree).** β(t, n, e) := Re(e^†H_1e)/Re(e^†H_We). PASS iff |β(0.025, n, e) - 1| ≤ 1e-3
  for all (n, e), and for every (n, e) with |β(0.05) - 1| > 1e-9 the ratio |β(0.05) - 1|/|β(0.025) - 1| lies in [2.5, 6]
  (O(t²) approach).
- **B2-3 (irrelevance of the remainder, O(p⁴) with c_1 := 1 fixed, not fitted).** ρ(t) := max_n ||H_1(tn) - H_W(tn)||_2 / t⁴.
  PASS iff ρ(0.05)/ρ(0.1) ∈ [0.8, 1.25] and ρ(0.025)/ρ(0.05) ∈ [0.8, 1.25].
- **Informational (no verdict).** κ = 0.25 and 4: β(0.025) range and the ρ ratios; Hermiticity defect max||H_1 - H_1^†||/||H_1||.

Runner: numeric lock (`until mkdir …/locks/numeric`), load1 < 8, nice 10, thread variables 1, PYTHONDONTWRITEBYTECODE=1,
/usr/bin/time -l, python3 without -I, no `timeout`, `rmdir` exactly once, no trap. Budget < 20 min, < 1 GB.
