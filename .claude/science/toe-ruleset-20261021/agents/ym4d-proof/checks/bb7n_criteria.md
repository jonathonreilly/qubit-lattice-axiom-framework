# bb7n criteria (lane B session 7; written after BFT_B §21 and Step 1, before checks/bb7n_chain.py exists)

Model: d = 2, SU(2) (unit quaternions), L = 3, ternary DD8 weights, roots at block corners (fine site 3X; bb5 convention).
R^{ax} exactly as Construction GC (§18.0): for each level-(j+1) site X, the axial gauge g^X of the stencil (tree from X: axis 0
first, then axis 1; g^X(X) = 1), A^X := log of the stencil field in that gauge, s^X := S_1A^X + dμ(A^X) on the fine links with tail
in X (μ(A^X) = 0 on X's own sites; on a face neighbour X' it is Σ_iΦ_0(z' - i)∫_{a(i→X')}A^X), R^{ax}(Z)(b) := exp(s^X(b))·Z(X, X').
Top: coarse side 12, V = exp(b), b iid Gaussian scaled so that f_k ≈ 0.10 ("a") and ≈ 0.20 ("2a"); depths k = 1, 2, 3 (level-0 side
324 at k = 3). f_j := max over level-j plaquettes of 9^{k-j}|log hol(∂p)| (coarse units). Linear reference: the same construction
applied componentwise to the Lie-algebra field b (A^X := b + dψ_X, exp/log omitted), f^lin_j its coarse curvature sup.
Thresholds are float precision (exactness checks) or the predictions of Theorem N2 (bounded, depth-uniform ratios; deviation
from the linear chain of relative order f_k).
- L0 structure (linear construction): max|Q_ax R b - b| ≤ 1e-12·max|b| and max|R(dν) - dC_0ν| ≤ 1e-12·max|ν| (Lemma GC-lin).
  PASS required.
- N-a depth uniformity (amplitude a): R_k := max_j f_j/f_k for k = 1, 2, 3: R_3 ≤ 1.15·max(R_1, R_2). PASS required.
- N-b closeness to the linear chain (amplitude a, k = 3): max_j |f_j - f^lin_j·(f_k/f^lin_k)|/f_k ≤ 0.25. PASS required.
- N-c exact covariance: for a Haar-random level-k gauge h, the plaquette-wise |log hol| profiles of chain(V^h) and chain(V) agree
  at every level to ≤ 1e-10 (k = 2). PASS required.
- N-d control (global-log refinement, no frames): the linear construction applied to log(V^h) (principal log of the gauged links)
  gives a curvature profile differing from chain(V)'s by ≥ 0.1·f_k at some level (k = 2). PASS required (= the control fails as
  predicted).
- N-e informational: f_j/f_k profiles for a and 2a, f^lin ratios, max axial stencil size a_{j+1}/(ρ_{j+1}f_{j+1}).
Resources: vectorised over blocks; expected < 1 GB, < 5 min.
