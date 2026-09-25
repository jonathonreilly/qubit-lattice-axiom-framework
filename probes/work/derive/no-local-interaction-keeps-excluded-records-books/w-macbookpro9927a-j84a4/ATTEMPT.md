# No local interaction keeps two excluded records' energy current

Task `J:derive:no-local-interaction-keeps-excluded-records-books:a2`, worker `w-macbookpro9927a-j84a4`, model claude-opus-5-5.
Checker: `check.py` in this directory. It is exact (sympy rationals, Gaussian rationals and symbols), takes about 130 s, and reports `TOTAL: PASS=7 FAIL=0`.

**Sources.** Read as landed on `origin/main` at `25b8c1874f2ea657653dbb298bf383c18d81e0b5`:
- block 143 (`ADMISSIBILITY_RULE_EXACT_BOOKS_NEED_RECORDS_THAT_NEVER_SCATTER_OR_BIND_...`), the supervisor's derivation along this problem's suggested route;
- block 137 (`..._KEEPS_THE_BOOKS_ONLY_AT_LEADING_ORDER_...`);
- block 140 (`..._EXACT_BOOST_CHARGE_...`);
- block 141 (`..._NO_POSSIBILITY_SHIFT_AMONG_NEIGHBOURS_...`);
- block 121 (`..._THE_SOURCE_IS_THE_COMPRESSED_DENSITY_...`).

PRs #9174, #9197, #9203 and #9205 are closed, and their notes are on main. Landed block 143 states its T3 and T5 only as conditional implications. It names an unresolved "analytic bridge":
- wave operators, RAGE time averages, a local-current decomposition and shell kernels, for T3;
- a determinant boundary identity and complex threshold bounds, including cones, for T5.

This attempt proves the no-go without T3's hypotheses. It derives T5's determinant identity, and replaces the threshold hypothesis by bounded spectral densities, which it proves from T6.

**Related prior work, disclosed.**
- #9249 is my first-order books identity for the long-range pull on the full space. Its remark R1 excluded exclusion.
- Today I released the excluded-record-interactions recovery unit, with route notes in my journal.
- I have made no earlier attempt at this problem.

## 1. Statement attempted

**Setting.** These are supplied clauses; nothing is adopted and no gravitational claim is made.

- **Two records** of block 54's walk on `Z^d`, `d = 2` or `3`. The symbol is `h(k) = sum_a sin k_a sigma_a` with `eps = |sin k|`, and `H2 = H(x)1 + 1(x)H`. The records are exchange-symmetric or antisymmetric.
- **One record per site** (block 78's compression; blocks 121 and 137). `P` removes the coincident coin states: the singlet for antisymmetric pairs and three states for symmetric pairs (block 143 T4).
- **The interaction.** `V` is any bounded, Hermitian, translation-invariant interaction acting within a fixed relative distance `R`, on the excluded space. `H' = P H2 P + V`.
- **The placement** (block 143's class).
  - The energy densities are local. Away from coincidence the current is the additive one-body current: the member's density `e_x = (Pi_x H + H Pi_x)/2` of block 137, plus any bounded translation-covariant one-body placement change of finite range.
  - A bounded remainder has finite relative support.
  - The total current is `J' = i[H', D']`.

**Claim.** `[H', J'] != 0`. No such interaction and placement keeps the total energy current, on `Z^3` or on `Z^2`, for either exchange sign.

**Imports.** The following standard theorems are assumed; they are named here and not re-proved.
- **I1:** the spectral theorem.
- **I2:** Fatou and de la Vallee Poussin. The Borel transform of a finite complex measure has finite boundary values at Lebesgue-almost every point, and `(F(E+i0) - F(E-i0))/(2 pi i)` is the density of its absolutely continuous part almost everywhere.
- **I3:** the coarea formula.
- **I4:** the Morse lemma.
- **I5:** M. Riesz's theorem: the Cauchy transform maps `L^p(R)` into `H^p` of the upper half-plane, for `1 < p < oo`. Also Hoelder's inequality.
- **I6:** Paley-Wiener: the boundary values of `H^2` of the upper and of the lower half-plane intersect only in `0`.
- **I7:** the direct-integral (fiber) decomposition of translation-invariant operators.
- **I8:** the identity theorem for real-analytic functions.

**Landed exact inputs** (block 143):
- **T1:** for almost every `(K, E)`, the total two-step momentum `g = sin K cos 2q` is constant on no shell component.
- **T4:** the removed states exist in every fiber.
- **T6:** at `tan K0 = (5/6, 18/5)` (plane) and `(5/6, 18/5, 1/2)` (space), every stationary point of every band function away from cones is nondegenerate, and the cone tilts are below one.
  - By continuity in `K`, this persists on a neighbourhood `U` of `K0`. The note states this, and it follows from the inverse function theorem.

## 2. Steps

**S0. Fibers. PROVED.**
- **The fiber space.** At total wave vector `K`, the pair lives on `L^2(T^d_q)(x)C^4`, or its exchange subspace. The free generator `h0` is multiplication by `h(K/2+q)(x)1 + 1(x)h(K/2-q)`. `g` is multiplication by the scalar `g(K,q)`, and `[h0, g] = 0` (block 140 T1).
- **Extending past the removed states.** Let `Pi0 = 1 - P`, of finite rank. Give the removed states an energy `lambda` outside `sigma(h0)`: `h'' = h' (+) lambda Pi0`. Also set `j'' = j' (+) mu Pi0`.
  - Then `[h', j'] = 0` iff `[h'', j''] = 0`.
- **Finite rank.** `h'' - h0 = F1 = A W A*`, where `W` is a Hermitian `r x r` matrix. The columns `a_i` of `A` have finite relative support, so they are trigonometric polynomials in `q`.
- **The current.** Away from coincidence the current is additive and one-body. Every two-body term (from `V`, the exclusion and the placement) acts within a finite relative distance. So

  `j'' = g + i[h0, m] + F2`,

  with `m` the fiber symbol of the one-body placement change and `F2 = A2 W2 A2'*` of finite rank with trigonometric-polynomial columns. This is block 143 T3's step 3, which is algebraic.

**S1. Lemma L0: a kept current has no one-body placement current. PROVED; CHECKED C4.**
- **Separating terms.** In `[h'', j''] = 0` every term is of finite rank except `i[h0, [h0, m]]`: `F1`, `F2` are finite rank and the other factors are bounded.
- **A multiplication operator of finite rank.** `i[h0, [h0, m]]` is multiplication by a bounded matrix function. Being equal to a finite-rank operator, it is compact, and a compact multiplication operator on `L^2(T^d)(x)C^4` is zero. So `[h0(q), [h0(q), m(q)]] = 0` almost everywhere.
- **The split (C4).** `[h0,[h0,m]] = [h1,[h1,f1]](x)1 + 1(x)[h2,[h2,f2]]`. Both terms are traceless, so each vanishes.
- **The one-body identity (C4).** `[h.s,[h.s,f.s]] = 4(|h|^2 f - (h.f)h).s`. This is zero iff `f` is parallel to `h`, iff `[h, f] = 0`.
- **Conclusion.** `i[h0, m] = 0` and `j'' = g + F2`.
- **Remark.** Far apart, each record must keep its own current. So a placement with `[h, f] != 0` already loses the books with no collision at all.

**S2. The resolvent identity. PROVED; CHECKED C1.**
- **Definitions.** Let `R0 = (h0 - z)^{-1}`, `R'' = (h'' - z)^{-1}` and `T(z) = F1 - F1 R'' F1`, for `z` not real.
- **Derivation.**
  - `R'' = R0 - R0 T R0`.
  - `[j'', R''] = 0` gives `[g, R''] = -[F2, R'']`.
  - `[g, R''] = -R0[g, T]R0`, since `g` commutes with `R0`.
  - Hence `[g, T(z)] = (h0 - z)[F2, R''](h0 - z)`.
- **The right side.** Using `(h0 - z)R'' = 1 - F1 R''` and `R''(h0 - z) = 1 - R'' F1`, it equals

  `(h0 - z) F2 (1 - R'' F1) - (1 - F1 R'') F2 (h0 - z)`.

  All kernels here are continuous functions of `(q', q)`: finite sums of trigonometric polynomials times finitely many scalars `<phi|R''(z)|psi>`.
- **On the shell.** Sandwich between band eigenvectors, `<u_b(q')|` on the left and `|u_a(q)>` on the right, with `E_b(q') = E_a(q) = E` and `z = E + i eta`. The `F2` terms cancel, and

  `(g(q') - g(q)) T_ba(z; q', q) = i eta <u_b(q')| (F2 R'' F1 - F1 R'' F2)(q', q) |u_a(q)>`.  (*)
- **Check C1.** It verifies the operator identity at two generic `z`, and the sandwich form (*) on a degenerate eigenspace, exactly.

**S3. A kept current makes the pair transparent at almost every energy. PROVED, given I1, I2, T1 and I8.**
- **The right side of (*) vanishes.** It contains finitely many scalars `i eta <phi|R''(E + i eta)|psi>`. By I1, each tends to `-<phi| 1_{E}(h'') |psi>`, which is `0` unless `E` is an eigenvalue of `h''`. There are at most countably many eigenvalues.
- **The left side converges.** By I2, `T(E + i0)` exists for almost every `E`: its kernel is `A (W - W Q''(E+i0) W) A*` with `Q'' = A* R'' A`.
- **So** for almost every `E`, `(g(q') - g(q)) t_ba(q', q) = 0` for all shell points, where `t = T(E + i0)`.
- **Density.** For almost every `(K, E)` (T1), `g` is non-constant on each shell component.
  - By I8, `g` is then non-constant on every open subset of a component.
  - So `{g(q') != g(q)}` is dense in each product of shells.
- **Conclusion.** `t_ba` is continuous there (trigonometric polynomials with fixed coefficients, and continuous band vectors away from cones). So it vanishes on the whole shell: the on-shell T-matrix is zero.
- **What is not used.** This step needs no wave operators, RAGE, time averages or analyticity in the channel. The forward direction is included by continuity.

**S4. The determinant is real on the continuum. PROVED, given I2 and I3; CHECKED C2 and C3.**
- **The determinant.** `Delta(z) = det(1 + W Q0(z))`, with `Q0 = A* R0 A`.
  - `T = A W (1 + Q0 W)^{-1} A*` (push-through), and `det(1 + W Q0) det(1 - W Q'') = 1` (C2).
  - So where the boundary values exist, `Delta(E + i0)` is nonzero and `M = W(1 + Q0(E+i0) W)^{-1}` is defined.
- **The density matrix.** Let `Gamma(E) = (Q0(E+i0) - Q0(E-i0))/(2 pi i)`. It is the density matrix of `<a_i| dE_{h0} |a_j>` (I2).
  - At regular `E`, `Gamma = R* R`, where `R` restricts `c -> sum c_i a_i` to the shell with measure `dsigma/|grad E_a|` (I3).
- **Transparency gives `Gamma M Gamma = 0`.** S3 says `R M R* = 0`, so `Gamma M Gamma = R*(R M R*)R = 0`.
  - Then `X = Gamma^{1/2} M Gamma^{1/2}` satisfies `Gamma^{1/2} X Gamma^{1/2} = 0` and `X = Pr X Pr`, with `Pr` the projector onto the range of `Gamma`. `Gamma^{1/2}` is invertible on that range, so `X = 0`.
- **Sylvester (C3).** `det(1 + W(Q0+ - 2 pi i Gamma)) = det(1 + W Q0+) det(1 - 2 pi i X)`. So `Delta(E - i0) = Delta(E + i0)`.
- **Reality.** `Delta(z-bar) = conj Delta(z)`, since `W` is Hermitian and `Q0(z-bar) = Q0(z)*`. Hence `Delta(E + i0)` is real for almost every `E`.

**S5. Lemma D: bounded spectral densities near `K0`. PROVED, given I3, I4 and T6.**
- **The claim.** For `K` in `U` and bounded weights `phi`, the push-forward of `phi dq` under each band function `E_a(K, .)` has a density in `L^oo` (on `Z^3`) or in every `L^p`, `p < oo` (on `Z^2`).
- **Reduction.** It suffices that `|{q : e < E_a(q) < e + delta}| <= C delta` uniformly in `e` (`d = 3`), or `<= C delta (1 + log(1/delta))` near saddle values (`d = 2`).
- **Cover.** Cover `T^d` by finitely many open sets. There are finitely many stationary points and cones for `K` in `U`.
  - **(i) Regular sets**, where `|grad E_a| >= c > 0`. In flow-box coordinates with `E_a` as one coordinate (bounded Jacobian), the volume is `<= C delta`.
  - **(ii) Nondegenerate stationary points (T6).**
    - By I4, `E_a = tau + sum eps_i y_i^2`, with a bounded Jacobian.
    - In `d = 3`, signature `(+++)` gives a spherical shell of volume `(4 pi/3)((u+delta)^{3/2} - u^{3/2}) <= C delta`. Signature `(++-)` gives, for each `y_3`, an annulus of area `pi delta`, so volume `<= 2 r pi delta`. The other signatures follow by sign.
    - In `d = 2`, extrema give area `pi delta`. At saddles the density is `int dy_2 / sqrt(w + y_2^2) = O(log(1/|w|))`, which lies in every `L^p`.
  - **(iii) Cones.** Near a cone of record 1, with `K/2 + q0` in `{0, pi}^d` and `q = q0 + rho theta`:
    - `E_a = s1 omega + psi`, where `omega = |sin(rho theta)|` and `d omega / d rho = 1 + O(rho^2)`.
    - `psi` is the other record's energy. It is smooth near `q0`, with `|grad psi(q0)| = t < 1` (T6; C6).
    - So `|d E_a / d rho| >= (1 - t)/4` for `rho < r`, with the sign of `s1`.
    - Along each ray `{e < E_a < e + delta}` is then an interval of length `<= 4 delta/(1 - t)`, and the volume is `<= C delta`.
    - The coin projectors are discontinuous at the cone but bounded, which is all that is used.
- **Conclusion.** The entries `Q0_ij` are Cauchy transforms of densities in `L^1` intersected with every `L^p`. They are therefore in `H^p(C+)` for every `1 < p < oo` (I5), with `|Q0_ij(z)| <= C/|z|` at large `|z|`.

**S6. `Delta = 1`. PROVED, given I5 and I6.**
- **`Delta - 1` is in `H^2`.** `Delta - 1` is a sum of products of `k <= r` entries of `W Q0`. Take each entry in `H^{2r}`.
  - By Hoelder, each product lies in `H^{2r/k}`. On bounded `|x|` this is locally in `L^2`, uniformly in `y`; at large `|x|` it is `O(|z|^{-k})`.
  - So `Delta - 1` is in `H^2(C+)`. By `Delta(z-bar) = conj Delta(z)`, it is also in `H^2(C-)`.
- **Equal boundary values.** By S4 the two boundary functions agree almost everywhere. By I6 their common value is `0`, so `Delta = 1` on both half-planes.

**S7. The contradiction. PROVED; T4.**
- `lambda` is not in `sigma(h0)`, and `h'' Pi0 = lambda Pi0` with `Pi0 != 0` (T4). So `h'' - lambda` is not injective.
- Since `h'' - lambda = (h0 - lambda)(1 + R0(lambda) F1)`, we get `Delta(lambda) = det(1 + R0(lambda) F1) = 0` (Sylvester). This contradicts `Delta = 1`.
- So `[h''(K), j''(K)] != 0` for almost every `K` in `U`, a set of positive measure. By I7, `[H', J'] != 0`.
- The argument holds on `Z^3` and on `Z^2`, for either exchange sign.

**S8. Consistency. CHECKED C7.**
- **The line.** On `Z` each shell is two points carrying one value of `g`. S3's density step has nothing to act on, which matches block 137's kept current on the infinite line.
- **Free records.** For free (non-excluded) records the same chain shows that a kept current forces transparency and `Delta = 1` (block 143 T5(ii)).
  - It does not forbid all interactions. For example `h'' = U h0 U*`, with `U - 1` of finite rank commuting past `g`, keeps `j'' = U g U*` and has `Delta = 1`.
- **Placements outside the class.** A placement whose current is not finite-rank off the free one is not covered. S1 shows that one-body changes are forced to vanish anyway.

## 3. First unresolved step

None within the stated class.

What is taken from outside:
- the named standard theorems I1-I8;
- block 143's exact results T1, T4 and T6.

What is not covered:
- interactions of infinite range;
- placements with non-local currents;
- more than two records.

## 4. What would finish or extend it

1. A referee's line check of S2-S6 and Lemma D (S5), especially the flow-box and cone volume bounds, and the `H^2` membership of `Delta - 1`.
2. The same chain for `N > 2` records (clusters) and for exponentially decaying interactions. In the latter case `F1` is trace class rather than finite rank, which needs Fredholm determinants.
3. Long-range pulls (#9249's setting) with exclusion, where `F1` is not trace class.
