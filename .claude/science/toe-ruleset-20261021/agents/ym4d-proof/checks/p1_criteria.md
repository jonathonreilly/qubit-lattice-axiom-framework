# p1 criteria (written 2026-10-27, before checks/p1_pld.py exists)

Tests PLD.md §7 (Proposition PLD-lin: the linearised soft chain, uniform in depth) and the elementary inequalities of
Lemma HS. d = 4, L = 3, real abelian (one component), each level in its own units, periodic tori. No SU(N) content.

**G (validity of the operators; must PASS for A-C to count).** For the straight average Q_str (one step), its adjoint, the
exterior derivative d (1-forms -> 2-forms, 6 components μ<ν) and its adjoint: dot tests |<Mx, y> - <x, M^T y>| <= 1e-10 *
|x||y| on 3 random pairs each, at coarse side T = 2 (fine side 6). Also Q_root (S4' contours, 24 orders, 81 start points)
reproduces a pure gauge: Q_root(dλ) = d(λ at roots) to <= 1e-12 * |dλ| on 3 random λ.

**A (Schur bound, PLD.md §7 (2)).** λ_max(Q_str Q_str^T) <= L^{-2}(1 + 1e-12) at T = 2 and T = 3 (exact dense
eigenvalues of the coarse-link Gram matrix). Informational: the ratio λ_max / L^{-2} (expected 1: constant fields).

**B (identity, PLD.md §7 (1)).** On 5 random real 1-forms A at T = 2: max |d Q_root A - d Q_str A| <= 1e-12 * max|A|, and
max |Q_root A - (Q_str A - d h(A))| <= 1e-12 * max|A| with h the slice functional (order- and start-point average of the
axial path integrals from the root).

**C (noise covariance, PLD.md §7 (2), (4)).** With unit noise at every level (s_i = 1), the level-k curvature covariance
of the noise part, Σ_k := Σ_{m=0}^{k-1} (d Q_str^m)(d Q_str^m)^T on level-k plaquettes, obeys
λ_max(Σ_k) <= 16 Σ_{m<k} L^{-2m} (1 + 1e-10), for (T, k) in {(2,1), (2,2), (2,3), (3,1), (3,2)} (exact Gram matrices,
columns computed as A_m(A_m^T e_P)). Also λ_max(d d^T) <= 16 (1 + 1e-12) at T = 2, 3.
Informational (not PASS criteria): λ_max(Σ_k) for each k; the increments λ_max(Σ_{k+1}) - λ_max(Σ_k); the ratio to the crude
additive bound 16k (the recursion of EXISTENCE §13.6 form).

**D (Lemma HS one-coordinate constant).** For c in {0, 0.25, 1, 3}: (2π)^{-1/2} ∫ exp(-ξ²/4 + c|ξ|) dξ <= 2√2 e^{c²}
(trapezoid on [-80, 80], step 1e-4; PASS if the ratio <= 1 + 1e-9 for every c). Informational: the ratios.

**E (||1 - e^X||_HS <= ||X||_HS).** 2000 random X in su(2) and 2000 in su(3) with spectral radius uniform in (0, π]: the
inequality holds for all, to 1e-12. Informational: max ratio.

**F (informational only, PLD.md §5.3).** The exponent of the m-th term of Corollary PLD-fin, κ c_1^{2m} (1/g² + β m log L)
/(256 N), N = 2, κ = 1, g² = 0.5, β = 11N/(48π²) (one-loop, [inference]), for m = 0..40: printed, to show it tends to 0.

Run discipline: numeric lock, nice 10, OPENBLAS/OMP/MKL threads = 1, load < 8, >= 25% memory free, peak < 1 GB;
`python3` (user-site numpy; no `-I`, disclosed); no external files read. A FAIL is recorded as a FAIL; criteria are not
edited after the run.
