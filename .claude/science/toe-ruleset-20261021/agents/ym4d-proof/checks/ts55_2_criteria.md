# ts55_2 — criteria (pre-registered before any script exists)

Written by the TSE55 worker (claude-opus-5-5); UTC stamp in the record line below. Script to be written AFTER this file:
`checks/ts55_2_gauss.py`. Exact rational arithmetic only (fractions.Fraction); no floats, no numpy.

## What is tested
Proposition GT of TSE55 §3.2 (the per-level one-loop terms of Proposition B's telescoping sum add up to the running-coupling
bubble) on random toy multiscale Gaussian models, by a computation path that does NOT use the per-level closed formula:
- Model: n = 6 "plaquette" coordinates, levels i = 0,1,2,3 (3 = top), independent Z_i ~ N(0, I_{r_i}/u_i) (r_i ∈ {2,3,4},
  rational u_i), F := Σ_i M_iZ_i with random integer matrices M_i (6 × r_i, entries in [−3, 3]); colour multiplicity c_col = 3
  (independent identical copies). Weights w_f ≥ 0 on coordinates {0,1,2}, w_g ≥ 0 on {3,4,5} (disjoint supports), random
  integers in [0, 4], not all zero. Observables Q_w := Σ_colΣ_p w(p)F_p². Filtration 𝔉_i := σ(Z_i, …, Z_3).
- Path (P): per level i < 3, the conditional covariance Cov(E[Q_f|𝔉_i], E[Q_g|𝔉_i] | 𝔉_{i+1}) is computed by writing both
  conditional expectations as explicit polynomials in the Gaussian coordinates and evaluating ALL second and fourth moments by
  brute-force enumeration of Wick pairings (Isserlis), then averaging over 𝔉_{i+1} the same way; the top term
  Cov(E[Q_f|𝔉_3], E[Q_g|𝔉_3]) likewise. Sum = TEL.
- Closed forms: TOTAL := 2c_colΣ_{p,q}w_f(p)w_g(q)A(p,q)², A := Σ_iM_iM_iᵀ/u_i; and the per-level formula of TSE55 §3.2,
  Λ_i := c_colΣ_{p,q}w_fw_g[4A_{>i}(p,q)a_i(p,q) + 2a_i(p,q)²] (i < 3), Λ_3 := 2c_colΣw_fw_ga_3², a_i := M_iM_iᵀ/u_i,
  A_{>i} := Σ_{j>i}a_j.

## Gates
- **G1.** For each of 12 random models (fixed seeds 1..12): TEL = TOTAL exactly AND for each level the brute-force per-level
  value equals Λ_i exactly. PASS iff all 12 × (1 + 4) equalities hold.
- **G1-F (control, must FAIL):** replacing 4 by 2 in the cross term of Λ_i must break Σ_iΛ_i = TOTAL in ≥ 10 of the 12 models.
- **G2-F (control, must FAIL):** dropping the top term Λ_3 must break the equality in ≥ 10 of the 12 models.
- **G3 (u-scaling and the "fine share").** For each model, set all u_i := u (uniform) for u ∈ {3, 7}. With the split level k = 2,
  define TREE_k := 2c_colΣw_fw_g(A_{≥k})² (covariance of the level-k images in the Gaussian model) and FINE_k := TOTAL − TREE_k.
  PASS iff u²·FINE_k is the same rational at u = 3 and u = 7 (u-independent) in all 12 models, AND FINE_k ≠ 0 in ≥ 10 of them.
  (This is the toy instance of TSE55 finding §4.2: the part of the one-loop bubble not carried by the level-k images scales
  exactly like the leading term, so it is not suppressed by any power of the coupling.)

## Verdict rule
ts55_2 PASS iff G1 PASS, G1-F and G2-F fail as stated, and G3 PASS. Otherwise FAIL, recorded as such.

## What this check cannot decide
Proposition GT is an identity about Gaussian measures; the check tests that identity and its factor structure (4 vs 2, top
term) on toy models. It says nothing about whether Yang–Mills' per-level covariances are close to their Gaussian values (that is
the named input (PL-1L)), nor about the lane chain's actual slices 𝔎_i.

## Record
- criteria file completed 2026-10-29T06:08:21Z (date -u); no script for ts55_2 exists at this time.
