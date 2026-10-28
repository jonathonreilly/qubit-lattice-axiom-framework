# Check s1 (lane F, SF.md): pre-registered criteria (written before any s1 script)

Purpose: numerical sanity checks of SF.md's Lemmas SF-DC (and the (OP-loc) failure), SF-J, SF-cut, SF-geo, and the arithmetic
of Corollary CE^+, Lemma SF-blk and Proposition SF-V (V7). A check does not prove a lemma; the proofs are in SF.md §3.
Runner: checks/s1_sf.py, output checks/s1_out.txt, record checks/s1_time.txt. Numeric lock, nice 10, BLAS threads 1.
Expected runtime < 5 min, peak RSS < 1 GB.

## A. SF-DC dependence sets (d = 2 scalar model of Theorem RW's setting)
[Revision 01:49 UTC, before any s1 script existed (disclosed in SF_LOG): the first version (2 × 2-block boxes, R = 2, m² = 1)
made Ω(𝒴^+) the whole 12 × 12 torus, so A2 was vacuous and A6 impossible. Revised model below; A0-A6 otherwise unchanged
except A6's distance (5 → 2 blocks, the largest available on this torus).]
Model: coarse torus 12 × 12 blocks, L = 3 (36 × 36 sites, one real component per site); K = -Δ + m² + E, m² = 4, Δ the
nearest-neighbour Laplacian, E a fixed-seed random real symmetric perturbation with entries only between sites whose blocks are at
coarse ℓ^∞ distance ≤ 1 (r_K = 1), scaled so that ||E|| ≤ 0.3. Boxes: R = 1, every box a single block (144 boxes);
Ω_□ = sites in blocks at coarse distance ≤ R from □. 𝒴 = {block (0,0), block (6,6)} (two linked components, since linking is
distance ≤ R + r_K = 2 blocks), s = 0.5 on 𝒴, 0 elsewhere. K^{-1}(s; t) := P(t)(1 - R(s; t))^{-1} as in Theorem RW, t ∈ {0, 1, 10}.
- A0: N_0(|R(s; t)|) < 1 at each t (else A is INCONCLUSIVE, not FAIL).
- A1 (SF-DC (a)): for every column y in a box □' ∉ 𝒴, max_{x∉Ω_{□'}}|K^{-1}(s;t)(x,y)| ≤ 1e-12·max|K^{-1}(s;t)|.
- A2 (SF-DC (b)): for every column y in a box of component 𝒴_α, max_{x∉Ω(𝒴_α^+)}|entry| ≤ 1e-12·max|K^{-1}|.
- A3 (non-vacuity): for some column y ∈ 𝒴, some x ∈ Ω(𝒴_α^+) ∖ Ω_{□(y)} has |entry| ≥ 1e-8·max|K^{-1}| (the reach beyond Ω_{□'} is real).
- A4 (square root, quadrature): 𝒞(1) := (2/π)∫_0^∞(K + u²)^{-1}du by Gauss-Legendre on u = tan(θ), ≥ 200 nodes, agrees with K^{-1/2}
  (eigendecomposition) to relative max-entry error ≤ 1e-6.
- A5 (SF-DC (c)): 𝒞(s) by the same quadrature of K^{-1}(s; u²): for every link x and column y outside the predicted dependence set
  D(x) (∪ x's own block), |𝒞(s)(x, y)| ≤ 1e-10·max|𝒞(s)|.
- A6 ((OP-loc) failure, SF.md §3.3): add to K one symmetric entry ε_lr = 1e-3 between a site z ∈ Ω_{box(0,0)} and a site w at
  coarse distance ≥ 2 blocks from Ω(𝒴^+) (and keep K positive); then for some y ∈ box (0,0), |K^{-1}(s; 0)(x, y)| ≥ 1e-10·max for
  some x ∉ Ω(𝒴^+) (the dependence set is no longer bounded).

## B. SF-J (Haar Jacobian)
For N = 2, 3, 4, 200 fixed-seed random complex A ∈ sl(N, C) rescaled to ||A||_op uniform in (0, π/2]:
- B1: det f(ad A) on sl(N, C) (matrix of ad A in a basis of sl, f(z) = (1 - e^{-z})/z by eigendecomposition or series) equals
  Π_{a<b}(sinh(w_ab)/w_ab)², w_ab = (λ_a - λ_b)/2, to relative error ≤ 1e-9.
- B2: |L(A)| ≤ (N/9)|A|²_HS, L(A) := Σ_{a≠b}Log(sinh(z_ab/2)/(z_ab/2)).
- B3: |L(A) - (N/12)tr(A²)| ≤ (N/270)|A|⁴_HS.
- B4: scalar: |Log(sinh(w)/w)| ≤ (2/9)|w|² on a polar grid of |w| ≤ π/2 (≥ 10⁴ points).
- B5: Haar SU(2): 2·10⁵ fixed-seed Haar samples (normalised Gaussian quaternions); the empirical CDF of θ = |eigen-angle| ∈ [0, π]
  differs from the CDF of the density (2/π)sin²θ (= 4πθ²j(θ) normalised, j = (sin θ/θ)²) by ≤ 0.01 in sup norm.

## C. SF-cut tail bound
- C1: for n = 12 (N = 2) and n = 32 (N = 3) and p on a grid of [0.5, 20] (≥ 200 points): P(χ²_n > p²) ≤ 2^{n/2}e^{-p²/4}
  (scipy.stats.chi2.sf).

## D. SF-geo combinatorics
- D1: the reflected 4-bit Gray code XOR-translated by each of the 16 vertices v of {0,1}⁴ is a sequence of 16 distinct vertices
  starting at v with consecutive Hamming distance 1 (path length 15).
- D2: for each of the 80 offsets e ∈ {-1,0,1}⁴ ∖ {0}, the closed cubes [0,1]⁴ and e + [0,1]⁴ intersect and the intersection
  contains a vertex of [0,1]⁴.

## E. Arithmetic (reproduce SF.md's numbers)
κ_0 := 16 log 12800, K_0 := e^{κ_0}/6400, L = 3.
- E1: 273(3κ_0 + 3 + 16 log 2) within 0.1% of 1.2779·10⁵.
- E2: (κ_0L + 1)/(L - 1) within 0.5 of 227.5; (κ_0L + 1 + log(16L⁴K_0))/(L - 1) within 0.5 of 302.4.
- E3: 1.2779·10⁵/(4.83·10⁻¹¹) within 1% of 2.65·10¹⁵; (3·1.7·10¹² + 1)·3 within 1% of 1.53·10¹³; (2.65·10¹⁵)⁴ within 2% of 4.9·10⁶¹.
- E4: 2arcsin(x/2)/x ≤ 1.0107 on (0, ½] (grid) (SF-thr).

## Overall
PASS iff every criterion above passes (A0 INCONCLUSIVE makes A INCONCLUSIVE and OVERALL INCONCLUSIVE). Failures are recorded as
FAIL; criteria are not edited after the script exists.
