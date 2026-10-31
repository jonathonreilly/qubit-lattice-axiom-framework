# c20 criteria (written BEFORE c20_bg_regularity.py; session 9, 2026-10-27)

Purpose: a model diagnostic for BG-b (RTARGET §9, failure mode BG-F3). The level-summed R4D-lat remainder is bounded
uniformly in the number of levels iff (sufficient form) Σ_j A_j < ∞, where A_j is the mean oscillation of the
background curvature, in coarse (level-n) units, over the level-j cubes (PROOF.md, Lemma BG-sum). Question: is the
background produced by the S4' contour family with the soft constraint regular enough, or does the axial concentration
of the S4' contours (the adjoint Q^T puts O(1) weight on the axial legs through block centres) make it too rough?
This is a diagnostic of a LINEARISED ABELIAN 2D model. It tests instances, not a theorem, and it is not evidence about
the non-abelian 4D minimiser beyond plausibility.

Model (d = 2, abelian, linearised; L odd, n levels, coarse torus side T_c):
- Level-i lattice: torus side T_c L^{n-i}; link variables B_i (real); B_0 = fine field; B_n given (iid N(0,1) per
  coarse link, fixed seed). Plaquette field dB_i.
- Q^{(i)}: the linearisation of S4' (L1c) from level i to level i+1: the coarse link (X, X + e_μ) gets the average over
  the d! = 2 coordinate orders σ and the L² sites y of the block of the line integral of the contour
  P^σ(c_X → y)·S_y·P^σ(c_Y → y + L e_μ)^{-1} (S_y: L straight steps in direction μ).
- Background = the tree-level soft-constraint chain minimiser: minimise ½||dB_0||² + Σ_{i=0}^{n-1} (κ_i/2)
  ||Q^{(i)}B_i - B_{i+1}||² over B_0, …, B_{n-1}, with κ_i = κ L^{-2i} (the constraint/action ratio is level-independent,
  as in the marginal 4D scaling). Gauge zero modes are removed with a Tikhonov term (τ/2)||B_0||², τ = 1e-9
  (reported: the change of the curvature fields under τ → τ/10 must be ≤ 1e-5 relative, else the run is invalid).
- Coarse-unit curvature at level j: f_j := L^{2(n-j)}·dB_j.
- Level-j cubes: the L×L blocks of level-j sites aligned with the level-(j+1) blocks; window W = the (L+2)×(L+2)
  level-j plaquettes around it (cube + one-layer collar). osc(W) := max_W f_j - min_W f_j.
  A_j := mean over level-j cubes of osc; G_j := max over cubes; S_j := mean of max_W |f_j|.
Runs: (L, n, T_c, κ) ∈ {(3, 4, 4, 1), (3, 4, 4, 10), (5, 3, 2, 1)}.
Controls (synthetic fields f on the same level-j lattices, same statistics):
- C1 smooth: f = sin(2πx_1/T) cos(2πx_2/T) sampled at plaquette centres (T = physical torus side). Expected summable.
- C2 multi-level jumps: f = Σ_{i=1}^{n} L^{-(n-i)}·(±1, iid per level-i block) (piecewise constant on blocks of every
  level, jumps ∝ the block size). Expected summable (A_j ≈ c(n-j)L^{-(n-j)}).
- C3 rough: f_j iid N(0,1) per level-j plaquette at every j. Expected NOT summable.
Classification of a sequence (A_j), j = 0..n-1, by the ratios r_j := A_j / A_{j+1} for j = 0..n-2:
- SUMMABLE iff max_j r_j ≤ 0.7 (geometric decay towards the fine levels);
- NOT-SUMMABLE iff r_0 ≥ 0.9 (no decay at the finest pair);
- otherwise UNDECIDED.
Pass criteria (diagnostic validity, not a theorem):
- V1. τ-stability: as above, for every run.
- V2. Controls classify as expected: C1 SUMMABLE, C2 SUMMABLE, C3 NOT-SUMMABLE, for every (L, n, T_c).
- V3. The model runs are classified (SUMMABLE, NOT-SUMMABLE or UNDECIDED) and the classification is REPORTED; any
  classification is an outcome. SUMMABLE supports BG-b for this averaging in this model; NOT-SUMMABLE is evidence for
  BG-F3; UNDECIDED decides nothing.
Informational: G_j (max oscillation; Hölder needs G_j → 0), S_j, the location of the largest oscillations relative to
the block-centre axes, and the ratio sup|f_0| / max|dB_n|.
Resource rules: one job, nice 10, OPENBLAS/OMP/MKL threads = 1, load < 8 and ≥ 25% free memory before start; peak memory
reported. Result: VALID iff V1 and V2 hold; the model classification is the finding. No criterion is edited after the
run.
