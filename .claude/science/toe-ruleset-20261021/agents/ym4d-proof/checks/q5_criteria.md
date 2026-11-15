# q5 criteria (lane G session 4; written 2026-10-28 before checks/q5_lattice_ids.py exists)

Purpose: exact or elementary lattice identities used by SQ.md §15 (session 4): Lemma TPL, Lemma BIA, Lemma WB, Lemma NREFL,
Lemma GARSIA. Identity and scaling checks only; no estimate of a minimiser is tested.

Conventions: SU(2); u_{μν}(x) := traceless part of (U(p) - U(p)^†)/2, U(p) := U(x,μ)U(x+e_μ,ν)U(x+e_ν,μ)^†U(x,ν)^†;
straight covariant operators with transports Ad_{U(x,λ)} along the links at the base point: ∇_λ, D_1 (1-forms → 2-forms),
D_2 (2-forms → 3-forms), adjoints by transposition in an orthonormal real basis of su(2); ∇*∇ := Σ_λ∇_λ^T∇_λ on each
plaquette orientation class. K := ∇*∇ - D_1D_1^T - D_2^TD_2 (a matrix). Random small fields: U(b) = exp(η·X_b), X_b with
i.i.d. Gaussian coefficients normalised to |X_b|_op = 1·uniform(0.3, 1), η ∈ {0.04, 0.02, 0.01}; η_P := max_p||1 - U(p)||_op.
Torus side 3 for the operator checks (dimension 1458 for 2-forms).

- **T1 (TPL, 1D kernels, exact integer arithmetic).** For L = 3 and m = 1, 2, 3: the m-fold composition of the in-plane 1D
  kernel A[X, s] = L⁻¹T_L(s - LX) equals L^{-m}T_{L^m}(s - L^mX); its column sums on a periodic line of L^{m+2} sites equal 1
  exactly; the transverse kernel's column sums equal L^{-m} exactly; max entry of the in-plane kernel = 1, transverse = L^{-m}.
- **T2 (dQ_str = Q_2d, 4D).** On a 4D region 2L × 2L × L × L (L = 3), for 5 random real 1-forms a and all six plaquette
  orientations of the coarse plaquette at the origin block: |(dQ_stra)(q) - Σ_pw(q;p)(da)(p)| ≤ 1e-12, with w = L⁻⁴·T_L·T_L
  (in-plane) × 1 (transverse in the block), Q_str := L⁻³Σ_{transverse offsets}Σ_{i<L} (straight lines from the block face).
- **W1 (abelian identity).** At U ≡ 1: max|K_{ij}| ≤ 1e-12.
- **W2 (covariance; K vanishes on pure gauge).** For U(x, y) = g(x)g(y)^† with Haar-random g: max|K_{ij}| ≤ 1e-11.
- **W3 (zeroth-order, plaquette-controlled).** For random small fields: R_K := ||K||_op/η_P satisfies R_K ≤ 200 at every η,
  and max/min of R_K over the three η values ≤ 2; and ||K||_op changes by ≤ 1e-9 relative under a Haar-random gauge
  transformation of the field.
- **B1 (Bianchi defect quadratic).** For random small fields: R_B := max_c|(D_2u)(c)|/(max_{faces f of c}||1 - U(f)||)² ≤ 50 at
  every η, max/min over η ≤ 3; and R_B is gauge invariant (≤ 1e-9 relative change under a Haar-random gauge).
- **R1 (NREFL).** Box (4, 4, 2, 2) inside the torus (8, 8, 4, 4), random small field on the box, reflected as in §15.1:
  (a) max over crossing plaquettes ||1 - U(p)|| ≤ 1e-14; (b) on box links the torus gradient of Σ_ps(U(p)) equals the box
  (free-boundary) gradient to ≤ 1e-13; (c) on every torus link | |grad_𝕋(b)| - |grad_box(preimage of b)| | ≤ 1e-13 (0 on
  crossing links); (d) |Σ_𝕋|u|² - 16Σ_box|u|²| ≤ 1e-12·(1 + Σ_box|u|²).
- **G1 (GARSIA).** Ternary tree of depth 10 (uniform measure on 3^10 leaves); nonnegative adapted increments a_t (node
  values) of three kinds (i.i.d. uniform scaled; a single heavy path ("tower"); a random sparse heavy set). β := max over
  nodes of E[Σ_{s ≥ t}a_s | node] computed exactly. For λβ ∈ {0.25, 0.5, 0.9}: E[e^{λA}] ≤ (1 - λβ)⁻¹ (1 + 1e-12).

PASS = all of T1, T2, W1, W2, W3, B1, R1, G1. Resources: < 5 min, < 500 MB; under the numeric lock; nice 10, threads 1.
