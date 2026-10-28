# q1 criteria (lane G session 1; written BEFORE checks/q1_sq_lin.py exists; not to be edited after the script is written)

Purpose: numeric verification of the linear square-function estimate (SQ-lin) of SQ.md (deviation sources) and of its
one-dimensional ingredients, across depths. L = 3 (h = 1) unless stated; L = 5 informational in part A.

Definitions (as in SQ.md §2-§3; restated so that the check is self-contained).
- n := L^j. T_n(u) := #{(a, b) ∈ [0, n)² : a + b = u} (the discrete triangle, support [0, 2n - 2], peak n at u = n - 1).
- Box functionals φ_{j,X} := n^{-1/2}(1_{[n(X+1), n(X+2))} - 1_{[nX, n(X+1))}) (the gradient of the normalised block mean).
- Triangle functionals ψ_{j,X} := n^{-3/2}(T_n(· - n(X+1)) - T_n(· - nX)) (the gradient of the normalised in-plane average).
- Edge functionals χ_{j,s} := n^{-3/2}T_n(· - ns), s ∈ {0, …, h - 1} (lower layer) and their mirror images (upper layer).
- On the interval of N_0 := 2L^J sites (box family) or N_0 - 1 plaquette positions (triangle and edge families), levels
  j = 0, …, J - 1, all functionals of the family whose support lies in the interval. The frame operator is S := Σ φφ^T over
  the family; λ(J) := its largest eigenvalue (Lanczos, matrix-free, relative tolerance 1e-10).
- Proven bounds of SQ.md §3 (L = 3 values): β_M = 4 + 8/(√L - 1) = 14.93; β_A = 10 + 6/(√L - 1) + 14/(L^{3/2} - 1) = 21.53;
  β_E (one layer) = min(h, 3) + (h(h + 1)/2 + h)/(L^{3/2} - 1) = 1.477; both layers together ≤ 2β_E.

## A (1D, exact Bessel constants across depths)
J = 1, …, 9 at L = 3 (N_0 up to 39366); J = 1, …, 5 at L = 5 (informational).
- **A1** λ_box(J) ≤ β_M, λ_tri(J) ≤ β_A, λ_edge(J) ≤ 2β_E for every J (L = 3 and L = 5, each with its own L in the bounds).
- **A2** depth-uniformity (L = 3): for each family, λ(9) ≤ 1.05·λ(6) + 1e-6.
- A3 (info) the table λ(J) per family; the ratio of λ to the proven bound.

## B (4D cone boxes, depths k = 2, 3): the deviation square function
Cone box of a level-k plaquette P in the (0,1) plane: level-j extents (2L^{k-j}, 2L^{k-j}, L^{k-j}, L^{k-j}). Per 2-form
component (αβ) (six of them): in-plane directions α, β carry plaquette base positions [0, N - 1), transverse directions
carry [0, N), N the level-j extent. One-step maps per direction (level j → j + 1): in-plane A[X, s] = L^{-1}T_L(s - LX);
transverse M[X, s] = L^{-1}·1{s ∈ [LX, LX + L)}; interpolation (level j + 1 → j): in-plane J_0[x, X] = L^{-1} for
x ∈ [LX + h, LX + h + L - 1] and 0 elsewhere (clamped to zero outside the hull of centres); transverse J_1 = linear hats
between the centres LX + h, constant extension outside the hull. Q_2 := A ⊗ A ⊗ M ⊗ M and I_2 := J_0 ⊗ J_0 ⊗ J_1 ⊗ J_1 (in the
component's direction order). Chain of curvatures F_{j+1} := Q_2F_j - dr_j (dr_j the lattice curl of a level-(j + 1) link
field r_j on the box links), deviations **D_j := F_j - I_2F_{j+1}**, j = 0, …, k - 2.
Ratios: R_D := Σ_jΣ_comp||D_j||² / (||F_0||² + Σ_{j ≤ k-2}||r_j||²); R_F := Σ_{j ≤ k-2}Σ_comp||F_j||² / ||F_0||² (the
curvature-source sum, which SQ.md §2 recalls is k-fold lossy).
Families: B-rand (seeds 1-2): F_0 iid N(0,1) in every component, r ≡ 0; B-exact (seeds 3-4): F_0 = dB_0 with B_0 iid N(0,1),
r ≡ 0; B-res (seeds 5-6): F_0 = dB_0 as B-exact and r_j iid N(0,1); B-smooth (one sample): F_0 = dB_0 with B_0 the lowest
non-constant cosine mode of the box in each link direction (smooth at the top scale), r ≡ 0; B-adv: the largest eigenvalue of
the map F_0 ↦ (D_j)_j (r ≡ 0), per component, by Lanczos (relative tolerance 1e-6).
- **B1** R_D ≤ 34200 for every sample without residuals and R_D ≤ 34200 for B-res (the bound proven in SQ.md §4 is
  Σ||D||² ≤ 34200||F_0||² + 1010Σ||r||²); the B-adv eigenvalue ≤ 11400 per component (the main-term constant of SQ.md §4).
- **B2** B-smooth contrast: R_F(k = 3)/R_F(k = 2) ≥ 1.4 while R_D(k = 3) ≤ 1.5·R_D(k = 2) + 0.05.
- **B3** consistency of the implementation with the exact identities used in SQ.md: (a) Q_2 maps a constant 2-form c to L²c
  on every component (to 1e-12 relative); (b) for F_0 = dB_0, F_1 = Q_2F_0 equals d(Q_strB_0) computed directly from the
  straight average of LINEAR_PACKAGE §1.2 (to 1e-10 relative, k = 2); (c) I_2Q_2 reproduces constants on the interior
  (positions inside the hull of centres in the in-plane directions) to 1e-12.
- B4 (info) all ratios per family and depth; the B-adv eigenvalues for k = 2 and 3.

OVERALL PASS iff A1, A2, B1, B2, B3 all PASS. Resources: numeric lock (mkdir/rmdir exactly once), nice 10, BLAS/OMP threads 1,
load < 8, ≥ 25% free memory (memory_pressure), peak RSS < 1 GB, python3 without -I, no `timeout`. Timestamps recorded in
checks/q1_time.txt; output in checks/q1_out.txt.
