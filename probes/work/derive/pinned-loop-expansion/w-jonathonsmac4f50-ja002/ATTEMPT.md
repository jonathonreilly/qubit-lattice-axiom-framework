# pinned-loop-expansion, attempt 4 of 4: part (c) at the pinned scale — large `l₁` supplies no small parameter

Worker `w-jonathonsmac4f50-ja002` (`claude-opus-5-5`), unit `J-derive-pinned-loop-expansion:a4`.

**Provenance.**
- The only prior deliverable is attempt a2 (`w-jonathonsmac4f50-ja55c`). I wrote it in this same session, with the same model
  family. It is not refereed, so it does not count as an independent prior result. It did (a) and (b) and left (c) unattempted.
- This attempt therefore takes the other route, part (c). The only thing it uses from a2 is the `p → ∞` form of the law, and
  that is re-checked here (A3).
- Definitions come from the task statement and from block 39 (PR #8530: T5, and the executed calibration line), which I read
  on its branch for this attempt, and from block 40 (PR #8546).
- The chessboard estimate and the FKG inequality are classical theorems. They are listed under ASSUMED where used.

## 1. What is claimed

**Setting.**
- Six-axis menu at `c₀ = 6/S`, with `S = p + q + 4r`. Then `W = c₀ω = 6K₁` and `W_eq = 6p/S`.
- A configuration (occupied set `A`, contents `s`) weighs `z^{|A|} Π_{E(A)} W(s_e)`. A bond with an empty end weighs 1.
- Throughout, `p > q` and `p > r`, so that `W_eq` is the unique largest entry. This is the regime of (c).
- The **balance point** is `z_t = W_eq⁻³`. There the empty configuration and the fully occupied aligned configuration both
  weigh 1 per site.
- `∂A` is the set of record–vacancy bonds. `c(A)` and `β₁(A) = |E(A)| − |A| + c(A)` are the component count and the cycle rank
  of the induced graph.

> **(c1) The balance-point energy (exact).** On any graph with every site of degree 6 (the `L³` torus, `L ≥ 3`, or `Z³` with
> `A` finite), every configuration weighs
> `z_t^{|A|} Π_{E(A)} W = W_eq^{−|∂A|/2} · Π_{e∈E(A)} (W(s_e)/W_eq)`,
> so the weight is `e^{−E}` with non-negative bond energies:
> - `(log W_eq)/2` per record–vacancy bond;
> - `log(W_eq/W)` per record–record bond (0 if aligned, `log(p/q)` if opposite, `log(p/r)` if orthogonal).
>
> `E = 0` exactly for the empty configuration and for the fully occupied aligned configurations. At any other `z`, the weight
> is multiplied by the bulk factor `(z/z_t)^{|A|}`, and the bond energies are unchanged.
>
> **(c2) No small parameter from `l₁ → 1` (the no-go).**
> - At `c₀` the rows of `W` sum to 6, so `W_eq = 6 − 6(q+4r)/S < 6`, and `W_eq ≥ 6l₁`.
> - Hence, **for every weight triple and every `z`**, each record–vacancy bond costs `(log W_eq)/2 < (log 6)/2`. The weight of a
>   density contour is at least `6^{−1/2} = 0.408` per unit of boundary.
> - As `l₁ → 1` (that is, `q, r ≪ p`), only misaligned record–record bonds become costly. Density excitations tend to fixed
>   positive weights: a single record in the empty phase `1/36`, a vacancy in the dense phase `1/216`, a domino `1/1296`, a
>   unit-cube cluster `6⁻¹¹`.
> - The law tends, on every finite window, to one fixed model:
>   `μ_∞(A) ∝ (6z)^{|A|} 6^{β₁(A)} = z^{|A|} 6^{|E(A)|+c(A)}`. At `z = 1/216` this is `μ_∞(A) ∝ 6^{c(A) − |∂A|/2}`: the 3D Ising
>   lattice gas at `J = (log 6)/4 = 0.448`, `h = 0`, with neighbouring records forced to agree and one of six contents per
>   occupied cluster.
> - So an "explicit region at large `l₁`" cannot come from `l₁` being large. It needs a contour estimate for this fixed model, at
>   per-plaquette weight `6^{−1/2}`, and none is supplied here.
>
> **(c3) FKG in the limit (exact).** `β₁` is supermodular on subsets of any finite graph. Therefore `μ_∞` satisfies the FKG
> lattice condition for every `z`. The same condition holds at finite `p` on every window tested (checked, not proved).
>
> **(c4) The chessboard at `c₀`.**
> - Site-only bond-plane reflections are reflection positive at `c₀` (block 39 T5, re-checked). A 2×2×2 block `b` then has
>   disseminated weight `w(b) = e^{−E_int(b)}` at `z_t`.
> - The single-configuration sum of the bad blocks is `Z_cube − 7 ≥ 48W_eq^{−3/2} > 8/√6 = 3.27` for **every** triple. It tends
>   to `152/9 + 136√6/27 − 7 = 22.227` as `l₁ → 1`.
> - The event-form parameter `ε = (Z(all blocks bad)/Z)^{1/n}` is at least `((1+6z_t)⁴ − 1)/Z_cube`. This tends to `0.00396`
>   as `l₁ → 1`, so it does not vanish either.
>
> **(d)** Heuristic only (D2). The balance line reaches densities 0.1, 0.3, 0.5, 0.7 on `(p,1,2)` at `p = 15.3, 6.0, 3.9, 2.7`.
> The executed onsets are above 16, 8–12, 6–8, and below 6: the same trend, at larger `p`. The dilute side's six-fold entropy
> pushes coexistence above the balance line, which is the direction of the gap.

## 2. The steps

1. **PROVED + CHECKED (A1): the cap.**
   - `W = c₀ω` and `c₀ = 6/S`, so row sums are `6(p + q + 4r)/S = 6`. Every entry is positive, so none exceeds 6.
   - `W_eq = 6p/S = 6 − 6(q+4r)/S`, and `W_eq ≥ 6(p−q)/S = 6l₁`.
   - `W_eq ≥ 1` iff `5p ≥ q + 4r`, which holds when `p ≥ q, r`.
   - Checked at six triples.
2. **PROVED + CHECKED (A2): the energy identity.**
   - Count record endpoints of bonds: `6|A| = 2|E(A)| + |∂A|`.
   - So `z_t^{|A|} W_eq^{|E(A)|} = W_eq^{−3|A| + |E(A)|} = W_eq^{−|∂A|/2}`. Multiply by `Π(W/W_eq)`.
   - Every factor is at most 1 (`W_eq ≥ 1` is the largest entry), so `E ≥ 0`.
   - `E = 0` forces `∂A = ∅` and all record–record bonds aligned. On a connected graph that means `A = ∅`, or `A` = everything
     with one content.
   - For general `z` the extra factor is `(z/z_t)^{|A|}`.
   - Checked exactly (squared, to stay rational) on 120 configurations of the 3³ torus at three triples, including both ground
     states.
3. **PROVED + CHECKED (A3): the limit law.**
   - `l₁ → 1` iff `(2q + 4r)/S → 0` iff `K₁ → I`.
   - `Φ(A) = E_s[Π 6K₁(s_e)]` is a polynomial in the entries of `K₁`. So on every finite window it converges to
     `Φ_∞(A) = 6^{|E(A)|} P(s constant on each component) = 6^{|E(A)| + c(A) − |A|} = 6^{β₁(A)}`.
   - `z_t = W_eq⁻³ → 1/216`.
   - At `z = 1/216`, step 2's count gives `z^{|A|} 6^{|E(A)|} 6^{c(A)} = 6^{c(A) − |∂A|/2}`.
   - With `σ = 2n − 1`, `|∂A| = (3N − Σ_bonds σ_xσ_y)/2`. So `6^{−|∂A|/2} = const · exp((log 6)/4 · Σσσ)`: the Ising weight at
     `J = (log 6)/4`, `h = 0`.
   - Checked: `Φ_∞ = 6^{β₁}` on all 768 subsets of the 2×2×2 and 3×3×1 windows, and the torus identities on 60 random sets.
4. **PROVED + CHECKED (A4): no small parameter.**
   - By steps 1–2, every record–vacancy bond costs `(log W_eq)/2 < (log 6)/2`, whatever the triple and whatever `z`.
   - The limits `W_eq^{−1/2} → 6^{−1/2}`, `6z_t → 1/36`, `W_eq⁻³ → 1/216` and `36z_t² → 1/1296` (the domino: `Σ_{s,s'} W = 36`)
     are checked symbolically on `(p,1,2)`.
   - The cube cluster `z_t⁸ 6⁸ Φ(cube) → 6⁻¹¹` is checked exactly at `K₁ = I`, and at `p = 10⁶` to within 10⁻³.
   - `W_opp/W_eq = q/p → 0` and `W_perp/W_eq = r/p → 0`. These are the only energies that grow.
5. **PROVED + CHECKED (A5): `β₁` is supermodular.**
   - Adding a vertex `v ∉ A` adds `k` edges (its neighbours in `A`) and one vertex. It changes the component count by `1 − m`,
     where `m` is the number of components of `A` that `v` touches. So `Δ_vβ₁(A) = k − m`.
   - Now add a vertex `u ∉ A ∪ {v}` to `A`, and let `j` be the number of `v`-touching components adjacent to `u`.
     - If `u ~ v`: `k` rises by 1, and `m` becomes `m − j + 1` (those `j` merge with `u` into one `v`-touching component). So
       `k − m` rises by `j ≥ 0`.
     - If `u ≁ v`: `k` is unchanged, and `m` falls by `j − 1` when `j ≥ 1` and is unchanged when `j = 0`. So `k − m` does not
       fall.
   - Hence increments are non-decreasing in `A`. Telescoping over `A∖B` gives
     `β₁(A∪B) + β₁(A∩B) ≥ β₁(A) + β₁(B)`.
   - `|A∪B| + |A∩B| = |A| + |B|`, so `μ_∞(A∪B)μ_∞(A∩B) ≥ μ_∞(A)μ_∞(B)`: the FKG lattice condition.
   - Checked: every mixed second difference on the 2×2×2, 3×3×1, 2×2×3 and 4×3×1 windows.
   - **ASSUMED** (FKG theorem; Holley's inequality). The occupied set is positively associated and stochastically increasing in
     `z`, so empty and full boundary conditions give the extremal states.
6. **CHECKED, NOT PROVED (A6): FKG at finite `p`.**
   - `Φ` is log-supermodular (every mixed second difference of `log Φ` is ≥ 0) on these windows and triples:
     - 2×2×2 at `(3,1,2), (16,1,2), (5,1,1), (7,2,1), (2,1,2)`;
     - 3×3×1 at the first three;
     - 4×3×1 and 2×2×3 at `(3,1,2)`.
   - `(2,1,2)` lies outside the positive semidefinite rule.
   - The local condition to prove: for `v ≁ w`, the functions `g_v(s) = E_t[Π_{u∈N(v)∩A} W(t, s_u)]` and `g_w` are positively
     correlated under the content law tilted by `Π_{E(A)} W`. There is an analogous condition for `v ~ w`.
7. **CHECKED (B0) + ASSUMED (the chessboard estimate).**
   - The 7-state bond kernel is positive semidefinite at `c₀`: all 127 principal minors ≥ 0 at three triples, and singular.
   - `W` depends only on the relation of the two contents and not on the bond direction. So the reflection acting on sites
     only, with contents untouched, is a symmetry. Its crossing factor is the kernel itself, and block 39 T5's argument gives
     reflection positivity for every `z`.
   - **ASSUMED:** the chessboard estimate of Fröhlich–Israel–Lieb–Simon for 2×2×2 blocks on `L³` tori with `4 | L`:
     `P(∩_t θ_t E_t) ≤ Π_t (Z(E_t disseminated)/Z)^{1/n}`.
8. **PROVED + CHECKED (B1): the disseminated weight.**
   - In the disseminated configuration every crossing bond joins a site to its own mirror copy, so it is never excited.
   - Every site of a 2×2×2 block lies on three faces, and each face bond is shared by two blocks. So
     `w(b) = Π (zW_eq^{3/2})^{n} Π_{12 internal} W`, and at `z_t` this is `e^{−E_int(b)}` (the cube graph is 3-regular, as in
     step 2).
   - Checked against the whole 4³ torus: 24 random blocks at `z = 1/50` and at `z_t`, two triples.
9. **PROVED + CHECKED (B2): the single-configuration form is vacuous.**
   - The seven good blocks (empty; six aligned dense) have `w = 1`. The ground states give `Z^{1/n} ≥ 1`.
   - With that normalisation the bound `P(bad) ≤ Σ_bad w(b)/Z^{1/n}` reads `P(bad) ≤ Σ_bad w(b) = Z_cube − 7`.
   - The 48 single-record blocks alone contribute `48W_eq^{−3/2} > 8/√6`.
   - Values: `110226.56` at `(3,1,2)`, `128.00` at `(16,1,2)`, `29.29` at `(100,1,2)`, `22.57` at `(1000,1,1)`, with the exact
     limit `152/9 + 136√6/27 − 7` (limit model `z^{|A|}6^{|E|+c}`).
   - So this form proves nothing unless `Z^{1/n} > 3.27` per block. The two ground states give 1, and the leading excitations
     add only about `6z_t = 1/36` per site (heuristic).
10. **PROVED + CHECKED (B3): the event form stays away from 0.**
    - Put records only on even sites (4 per block, pairwise non-adjacent), at least one per block. Every such block is bad, and
      no bond is formed. So `Z(all bad) ≥ ((1+6z_t)⁴ − 1)^n`.
    - By the single-configuration chessboard estimate, `weight(σ) ≤ Π_t w(σ_t)`, so `Z ≤ Z_cube^n`.
    - Hence `ε ≥ ((1+6z_t)⁴ − 1)/Z_cube`. This is `0.00053, 0.00367, 0.00418, 0.00398` at the four triples, with limit
      `((37/36)⁴ − 1)/(152/9 + 136√6/27) = 0.00396`.
    - This does not by itself defeat a Peierls count (it depends on the count). It shows that the chessboard's parameter, like
      the contour weights of step 4, has a positive limit as `l₁ → 1`.
11. **HEURISTIC (D1, D2), not claimed.**
    - The limit model's binding, bond weight 6, is far above block 39's calibrated content-less onset, `e^{4K_c} = 2.427`. There
      `K_c = 0.2216544` is a literature value, cited and not used.
    - The low-temperature variable is `u = e^{−4J} = 1/6`.
    - At `z_t` the dilute side leads by about `5z_t` per site (single records `6z_t`, against vacancies `z_t`). So coexistence
      lies above the balance line; this is the direction of the gap to the executed onsets. Its size is not derived.

## 3. Where this stops

- **The first failing step of (c) as posed** is "take `l₁` large enough that contour activities fall below a Peierls
  threshold". At `c₀` no density contour costs more than `(log 6)/2` per record–vacancy bond, for any triple (steps 1, 2, 4).
  The chessboard parameter has a positive limit (step 10).
- Large `l₁` does make *content* disorder costly (`log(p/q)`, `log(p/r)`). But the dense/dilute question is about density, and
  it tends to the fixed model `μ_∞`.
- **What is not shown:** that coexistence fails. The limit model may well coexist. Heuristically, bond weight 6 is far into the
  condensed range of the content-less gas. But a proof must beat the six-fold cluster entropy at fixed per-plaquette weight
  `6^{−1/2}`.
- **Not shown either:** that every chessboard or Pirogov–Sinai argument fails for the limit model. Step 9 rules out only the
  single-configuration form. Step 10 only bounds the event form from below.
- **FKG at finite `p` (step 6) is checked on windows only.**

## 4. What would finish it

1. **A contour estimate for the fixed model** `μ_∞ ∝ 6^{c(A) − |∂A|/2}` at `z` near `1/216`. For example, a Pirogov–Sinai
   analysis with a sharp count of 3D contours at weight `6^{−1/2}` per plaquette: exact enumeration of small contours plus a
   rigorous tail bound. Or a non-perturbative argument built on step 5's FKG property.
2. **Stability for large finite `p`.** There misaligned bonds cost `log(p/q)`, `log(p/r)` → ∞, which is a genuine small
   parameter, but only for the content order.
3. **A proof of step 6** (FKG at finite `p`), through the correlation inequality stated there.
4. **A reading with a real large parameter.** For the sphere menu at `c₀`, `W_eq = β e^{β}/sinh β = 2β/(1 − e^{−2β})` is
   unbounded. There large `β` does raise the density-contour cost, but the dense phase then has a continuous symmetry.
5. **A referee from another model family.**

## 5. Running it

```
python3 probes/work/derive/pinned-loop-expansion/w-jonathonsmac4f50-ja002/check.py
```

- It needs sympy and has 12 lines: 10 exact checks and 2 labelled heuristics.
- Everything is exact (`fractions`, `sympy`). The only floats are printed decimals and the heuristic lines' displays.
- It runs in about 80 seconds, most of it the 2×2×3 window's 4096 content sums in A6.
- `loopexp.py` beside it (copied from a2) holds the brute-force content sum `phi_brute`.
