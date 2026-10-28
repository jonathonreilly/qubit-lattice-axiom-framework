# bb8w criteria (lane B session 8; written after BFT_B §24 (11:12:37 UTC) and before checks/bb8w_nf.py)

Tests Theorem N1-loc (BFT_B §24.2) in d = 2, SU(2) (quaternions as in bb6n). One box Ñ (own side S = 4n + 1, coarse half-width
2, centre c), n ∈ {3, 9, 27}. Field: a fixed smooth coarse su(2)-valued 1-form profile a(x) on [-2, 2]² (non-commuting
components, amplitude ε = 0.2), U(b) := exp(a(midpoint of b)/n) (own). Box normal form by the linearised Coulomb iteration
g ← exp(ξ)g, ξ := the pinned Neumann solution of d*dξ = d*w (sparse LU), until max|d*w| < 1e-12 (the normal-form equation of
Lemma NF-crit); w := log U^g, w^c := n·w; ∇^cw^c := n × (fine difference of w^c between parallel links along each axis).
Region N' := coarse half-width 3/2 around c (and the whole box, informational).

- W0: convergence max|d*w| < 1e-12 within 60 iterations for every n; w(c-pinned) normalised g(c) = 1. PASS required.
- W1 (N1L-F1): A1 := sup_{N'}|w^c|, A2 := sup_{N'}|∇^cw^c|, A3 := the pointwise Hölder proxy max|∇^cw^c(b) - ∇^cw^c(b')|/
  (δ/n)^{1/4} over parallel pairs at fine distances δ ∈ {1, 2, 4, …} with δ/n ≤ 1, both in N'. PASS iff for each of A1, A2, A3 the
  n = 27 value ≤ 1.25·max(n = 3 value, n = 9 value).
- W2 (informational): ratio (A1 + A2 + A3)/(f_0 + [F_0]_Lip-proxy) per n; the same quantities on all of Ñ; |w - a_lin|/|w| where
  a_lin is the abelian box-Coulomb potential of log U (componentwise linear projection).
Resources: expected < 300 MB, < 3 min.
