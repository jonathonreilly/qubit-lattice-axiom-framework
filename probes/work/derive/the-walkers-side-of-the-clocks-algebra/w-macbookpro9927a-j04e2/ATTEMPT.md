# The walker's side of the clock algebra

Task `J:derive:the-walkers-side-of-the-clocks-algebra:a1`, worker `w-macbookpro9927a-j04e2`, model claude-opus-5-5.
Checker: `check.py` in this directory. It is exact over Q(i), with sparse matrices on the 6^3 torus; it takes about 1 s and reports `TOTAL: PASS=5 FAIL=0`.

**Sources.** Read as landed on `origin/main` at `25b8c1874f`:
- block 112 (`..._THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_...`), T1;
- block 136 (`..._TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_...`), for the densities and T1/T2;
- block 138 (`..._THE_SYMMETRIC_MOMENTUM_IS_THE_TWO_STEP_MOMENTUM_PLUS_HALF_THE_CURL_OF_THE_SPIN_...`);
- blocks 54 and 137.

Conventions are block 136's:
- `(T_a psi)(x) = psi(x + e_a)`, `S_a = (T_a - T_a^-1)/(2i)`, `C_a = (T_a + T_a^-1)/2`, `H = sum_a sigma_a S_a` and `P_j = S_j C_j`.
- The densities are `e(x) = Re psi^dag(x)(H psi)(x)` (block 137's `e_x`) and its body-diagonal average `e' = C1C2C3 e`.
- The momenta are `P''_j = phi_j^T pi_j` and `Q_j = C1C2C3 Q^b_j`, with `P^B = (P'' + Q)/2 = P'' + (1/2) curl(sigma/2)` (block 138).

**Related prior work, disclosed.**
- I refereed block 112 T1's source attempt: the constraint-algebra a2, whose bond field `xi` is used here.
- My #8921 and #9204 treated the member–walker identity.
- None of these computed the walker's own bracket.
- There are no earlier attempts on this problem.

## 1. Statement attempted

**The walks with a lapse.**
- `H[N] = sum_x N_x e_x`. This is the arithmetic mean of the lapse on each bond, the task's literal walk.
- `H_G[N] = sqrt(N) H sqrt(N)`. This is the geometric mean, block 60's premise.
- `H'[N] = sum_x N_x e'_x`. This couples the lapse to the averaged density, which is the one block 136's `P^B` belongs to.

**The question.** Does `i[H[M], H[N]] = c sum_{x,j} xi_j(x) P^B_j(x)` hold, with block 112's `xi_j(x) = N_{x+e_j} M_x - N_x M_{x+e_j}` and `c = K/(4 alpha)`? Exactly for every pair of lapses, or to which order in the departures `M = 1 + m`, `N = 1 + n`?

## 2. Steps

**Step 1. The first order is a divergence test. PROVED.**
- Both sides are antisymmetric and bilinear for the arithmetic rule. Write `B(M,N)` for their difference.
- Then `B(1 + m, 1 + n) = B(1, n - m) + B(m, n)`.
- **The left side's first order.** `B(1, g)` contains `i[H, sum_x g_x e_x] = sum_x g_x (de_x/dt)`.
- **The right side's first order.** `c sum_{x,j}(g_{x+e_j} - g_x) P^B_j(x) = -c sum_x g_x (div P^B)_x`.
- So first-order closure for every `g` means `de_x/dt = -c div P^B` as operators, at every site: `P^B` must be a current of the density the lapse couples to.
- The geometric rule agrees with the arithmetic one at first order, since `sqrt((1 + n_x)(1 + n_y)) = 1 + (n_x + n_y)/2 + O(n^2)`.

**Step 2. With the averaged density: closure at first order iff `K/(4 alpha) = 1`. CHECKED X2.**
- Block 136 T1 and T2 state `de'/dt = -div P''` and `div Q = div P''` for every state. As operator identities they give

  `i[H, sum g e'] = sum_{x,j}(g_{x+e_j} - g_x) P^B_j(x)`.

- X2 verifies this exactly on the 6^3 torus for a generic rational `g`. It also validates my constructions of `P''`, `Q` and `e'`.
- So `B'(1, g) = 0` iff `c = 1`, that is `alpha = K/4`.

**Step 3. With block 137's density: no normalization closes even the first order. CHECKED X3.**
- `i[H, sum_x g_x e_x]` is not `c` times `sum grad g . P^B` for any `c`, including `c = 0`. The landed `P^B` is the current of `e' = C1C2C3 e`, not of `e`.
- This holds for the arithmetic rule and, by Step 1, the geometric rule.
- What would close the first order for `e` is any placement whose divergence is `-de/dt`. That is not the landed `P^B`.

**Step 4. Exact closure fails. The averaged density's obstruction has lowest order two. CHECKED X4.**
- **The witness.** Take delta lapses `M = delta_u` and `N = delta_{u + 2e_1}`, two steps apart along an axis.
  - Then `xi(M, N) = 0` on every bond, so the right side vanishes.
  - But `i[H[M], H[N]]` has 4 nonzero entries, and `i[H'[M], H'[N]]` has 48.
- **The order.** The bracket is bilinear, so this is `B(m, n)` at `m = delta_u`, `n = delta_v`: the second-order term in the departures.
- **A side fact.** On a face diagonal, `u` and `u + e_1 + e_2`, the two paths give `sigma_1 sigma_2` and `sigma_2 sigma_1`, which cancel. There the bracket is `0`.

**Step 5. The obstruction's form on a straight two-step path. CHECKED X5.**
- Along any axis, `<x|H[m]|x + e_a> = (1/2)(m_x + m_{x+e_a})(-i sigma_a/2)`. The only two-step path from `x` to `x + 2e_a` passes through `x + e_a`.
- So, for the arithmetic rule,

  `<x| i[H[m], H[n]] |x + 2e_a> = -(i/16)[(m0 n1 - m1 n0) + (m1 n2 - m2 n1) + (m0 n2 - m2 n0)]`

  times the coin identity.
- X5 verifies this at every site and on every axis for generic rational `m`, `n`.
- The first two brackets are the two bonds' `xi`. The third, `(m0 n2 - m2 n0)`, couples second neighbours, and no nearest-bond `xi` can produce it. This is the three-site term the supervisor anticipated, now exact.
- The averaged walk smears the same structure over body diagonals.

## 3. Result

**A counterexample to exact closure, and the first order split by density.**
- **Lapse coupled to block 137's `e`** (arithmetic or geometric bond mean): the walker's bracket misses `c sum xi.P^B` already at first order, for every normalization.
- **Lapse coupled to block 136's averaged `e' = C1C2C3 e`:**
  - it matches at first order exactly iff `K/(4 alpha) = 1` (`alpha = K/4`, the same condition again);
  - it fails at second order, witnessed by delta lapses two steps apart.
- **The supervisor's prior.** "Exact closure below one in ten" is confirmed. "Closure at first order with `alpha = K/4`" holds only when the lapse couples to the averaged density.

## 4. What would finish or extend it

1. A lapse placement that makes the second order close, perhaps a smeared `xi` or a second-neighbour term in the member's relabellings. Alternatively, a proof that no nearest-bond `xi` can.
2. The same computation with the member's own lapse timing (block 112's face means) carried to the walker.
3. The geometric rule beyond first order: `H_G` is not bilinear in the lapses.
