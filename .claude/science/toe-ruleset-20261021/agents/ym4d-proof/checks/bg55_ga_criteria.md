# bg55_ga — criteria (pre-registered; written 2026-10-29T01:05Z, BEFORE any script exists)

Owner: BGT55 worker (claude-opus-5-5). Script to be written AFTER this file: `checks/bg55_ga.py`; output
`checks/bg55_ga_out.txt`. Exact arithmetic only (python ints / fractions.Fraction; no floats, no numpy, no BLAS).
`python3 -I`, single thread. No criterion may be edited after the script runs; any amendment is appended and dated.

## What is tested
The exact linear algebra of the gauge-aligned transfer (BGT55 Theorem GA): for an invertible T with T Xi_1 = Xi_Z A,
(a) E_T := T^T H_Z T - H_1 annihilates Ran Xi_1 on both sides; (b) T^T maps cc_Z sources (Xi_Z^T S = 0 on Lambda_0)
to cc_1 sources; (c)-(e) solutions of H_1 u + E_T u = T^T S give solutions x = T u of H_Z x = S; and at a pure gauge
T = M_G gives E_T = 0 exactly (Lemma CONJ + gauge invariance).

## Models
- M1: d = 2, L = 3, depth k = 1, coarse side T = 2 (level-0 torus side 6, level-1 side 2), fibre = su(2) adjoint = R^3
  with the cross product, kappa_0 = 2. Data level fixed: x_1 = 0.
- M2: d = 2, L = 3, depth k = 2, coarse side T = 1 (level-0 side 9, level-1 side 3, level-2 side 1), kappa_0 = 2,
  kappa_1 = 3, x_2 = 0.
- Roots at block centres. Root map Q_l = Q_ax (root-to-root straight line sum; root covariant Q d = d ev). Lane A's
  S4' contour average is NOT used (the theorem under test is Q-independent algebra).
- Lambda_0 = level-0 R^3-valued functions vanishing at the level-k roots. Xi_1 lam = (d ev^(l) lam)_{l<k}.
- Covariant objects at a background chain Z = (Z_0, ..., Z_{k-1}) of SO(3) link matrices:
  (d_Z lam)(b) = Ad_{Z(b)} lam(y') - lam(y); Q_ax^Z with transports to the base root along the straight row;
  Xi_Z lam = (d_{Z_l} ev^(l) lam)_l; H^cov_Z = d_Z^T d_Z (level 0, on 2-forms) + sum_l kappa_l (Q^Z_l x_l - x_{l+1})^T(...).
- Backgrounds (pseudo-random, fixed seeds, entries from the 24-element octahedral rotation group = signed permutation
  matrices with det +1, so all arithmetic is integer):
  (PG) pure gauge Z_l(b) = G(y) G(y')^{-1} with G on level-0 sites, level-l sites identified with their level-0 roots;
  (CV) curved: every link of every level an independent random octahedral rotation.
- H_Z := H^cov_Z at PG; at CV, H_Z := P_Z^T H^cov_Z P_Z with P_Z := 1 - Xi_Z P'_Z, P'_Z the covariant spanning-tree
  left inverse of Xi_Z (artificial, gauge-degenerate by construction; NOT a true critical-point Hessian).
- Alignments: T_G := M_G (pointwise Ad_G at base sites) at PG; T_N := 1 + (Xi_Z - Xi_1) P with P the flat spanning-tree
  left inverse of Xi_1 (P Xi_1 = 1 on Lambda_0), at PG and CV.

## PASS criteria (each must hold exactly)
- A1 (implementation, Lemma CONJ): at PG, d_Z M_G = M_G d on functions at every level, and H^cov_Z = M_G H_1 M_G^T.
- A2: H_Z Xi_Z = 0 at PG and at CV (both models).
- A3: T_G Xi_1 = Xi_Z M_G^fn at PG; T_N Xi_1 = Xi_Z at PG and CV.
- A4 (GA (a)): E_T Xi_1 = 0 and Xi_1^T E_T = 0 for every (model, background, T) pair.
- A5 (GA (b)): for 6 pseudo-random S in cc_Z (S := H_Z x, x a random integer chain), Xi_1^T T^T S = 0 exactly.
- A6 (pure-gauge exactness): E_{T_G} = 0 exactly at PG (both models).
- A7 (GA (c)-(e), M1 only, PG and CV): T_N invertible (exact rank = dim X); for 3 random S in cc_Z the exact solution u
  of the augmented system [H_1 + E_T ; P] u = [T^T S ; 0] exists and x := T_N u satisfies H_Z x = S exactly.

## Controls (each MUST FIRE; a control that does not fire voids the weight of the PASS it guards)
- C1 (guards A2/A4 non-vacuity): at CV, H^cov_Z Xi_Z != 0 (the covariant quadratic form is not gauge-degenerate at a
  curved background — the B1/B2 defects are real in the model).
- C2 (guards A6): at PG, E_{T_N} != 0 (the naive alignment is not exact at a pure gauge).
- C3 (guards A4): the unaligned difference E_1 := H_Z - H_1 has E_1 Xi_1 != 0 (PG and CV).
- C4 (HR-1 reproduced): at PG, H_Z - H_1 != 0 while every level-0 plaquette holonomy is the identity.
- C5 (guards A5): a random non-cc_Z vector S_bad has Xi_1^T T_N^T S_bad != 0.
- C6 (guards A3/A4): with P~ := 2P (not a left inverse), T~ := 1 + (Xi_Z - Xi_1) P~ has T~ Xi_1 != Xi_Z and
  E_{T~} Xi_1 != 0.

## Informational (no verdict weight)
- I1 (M1): rank(H_Z) at PG and CV, compared with dim X - dim Lambda_0.

## What this check cannot decide (stated before running)
Nothing analytic: no size, no k- or T-uniformity, no d = 4 arithmetic, nothing about the true Hessian at a critical
background (CV's H_Z is artificial), nothing about lane A's S4' map, nothing about the norms. It can catch a wrong
transpose/sign/side in Theorem GA's statement, a wrong claim that M_G aligns and intertwines, and implementation errors.
