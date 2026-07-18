# Block09 plan — matrix-fiber trace-norm lemma and the fiber feed

Date: 2026-07-18. Ninth block. Takes block08's named-open matrix-fiber
item via one sharp new lemma plus an n_f-scaled feed.

## Supervisor ground truth (pre-worker/lens, sympy session)

- PAIR LEMMA (EXACT IDENTITY, new): for x != y and any fiber matrix k,
  || sum_ab k_ab c^dag_{xa} c_{yb} + h.c. || = ||k||_S1 (trace norm).
  Verified on 7 instances incl. non-normal ([[2,1],[0,1]]: both sides
  sqrt(10); identity fiber: both 2; rank-1: sigma). Proof route: SVD
  k = U Sigma V^dag; particle-conserving mode rotations preserve CAR;
  T becomes sum_i sigma_i (hop_i + h.c.) on DISJOINT mode pairs;
  commuting Hermitian pieces, each spectrum {-sigma_i, 0, sigma_i};
  joint spectrum = sums; norm = sum sigma_i.
- ON-SITE BOUND: for Hermitian fiber k, ||h_x|| = max(sum lambda^+,
  sum lambda^-) <= ||k||_S1, strict at diag(1,-1) (1 < 2), saturated
  at diag(1,2) (3 = 3).
- S1 <= n_f * op-norm (n_f singular values each <= sigma_max);
  equality at k = identity (n_f vs 1: strictness of op-norm alone).
- FEED: any supplied matrix-kernel bound ||k_xy||_op <= K e^{-eta r}
  gives ||h_xy|| = ||k_xy||_S1 <= n_f K e^{-eta r}; every block08 step
  multiplies by n_f: kappa_bar_fiber = n_f * kappa_bar_scalar
  (envelope 585 n_f K at x = 1/2). n_f = 1 recovers block08 exactly.
  n_f is geometry (fixed across backgrounds) so uniformity carries.
- Sharper remark: if sum_y ||k_xy||_S1-type data is supplied directly,
  use it; the n_f factor is only for op-norm-supplied kernels.

## Scope honesty

The CT note's kernel carries no fiber vocabulary (checked: no
internal/color/spinor lines) — its case is the scalar n_f = 1
instance. Block09 is forward-compatible generality for supplied
matrix kernels; no gauge-theory fiber content is claimed from the CT
note itself.

## Cluster discipline

PR #10. B08's evaluator file did NOT list matrix fibers as
outside-toolkit (only the PR BODY sentence did) — the evaluator must
record this discrepancy and the correction: the SVD/mode-rotation
argument is elementary exact algebra, within toolkit.
