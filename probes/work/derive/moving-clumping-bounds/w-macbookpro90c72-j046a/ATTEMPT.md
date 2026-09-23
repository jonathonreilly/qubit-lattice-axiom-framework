# J:derive:moving-clumping-bounds:a2 — a sharp one-site bound below; above, an explicit clumping region for every (p, q, r) through site-plane reflection positivity

**Provenance.**
- Worker `w-macbookpro90c72-j046a`, model `claude-opus-5-5`, one session.
- The claim printed one prior attempt, a1 (`w-jonathonsmac4f50-j6200`, `claude-opus-5`: the same family, an earlier model, another machine, unrefereed). a1 left (a) unfinished and used the bound `(M − m)/(M + m)` for (b).
- I formed my plan before reading a1: a sharp total-variation bound for Dobrushin, and a chessboard/Peierls argument for (a). I then read a1 and take a different route on both parts.
- Definitions come from the owner's reading as the task states it (block 39's law with vacancies).
- Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**The law.**
- Each site of `Z³` is empty or holds one record, whose content `a` is one of `±e₁, ±e₂, ±e₃`.
- The weight is `z^N Π_bonds W`, with `W(a, b) = cω(a, b)` between two records (`ω = p, q, r` for equal, opposite, orthogonal contents) and `W = 1` if an end is empty.
- Constants: `T = p + q + 4r`, `c₀ = 6/T`, `ω* = max(p, q, r)`, `t = T/ω* ∈ [1, 6]`.
- **Clumping** means two translation-invariant Gibbs states of different density at one fugacity.

**Claims.**

**(b) BELOW (exact).**
1. **The one-site bound.** For distributions `P ∝ f` and `P′ ∝ fh` with `h ∈ [m, M]`:

   `sup_f TV(P, P′) = (√M − √m)/(√M + √m) = tanh(¼ log(M/m))`,

   and the supremum is attained. a1's bound `(M − m)/(M + m)` is strictly larger.
2. **Dobrushin at every fugacity.**
   - A site's conditional law, over 7 states, changes under a change `b → b′` of one neighbour by the factor `h(a) = W(a, b′)/W(a, b)`. The fugacity and the other five neighbours enter only through `f`.
   - So the law is unique at every fugacity when `R_max < (7/5)² = 49/25`, where `R_max` is the largest spread `max h/min h` over all neighbour changes (`6 tanh(¼ log R) < 1`).
3. **Exact windows.**
   - Content-less records: `25/49 < cw < 49/25`, i.e. `c/c₀` up to `1.96`.
   - `(9,8,8)`: `25/392 < c < 49/225`, i.e. `c/c₀ ∈ (0.52, 1.78)`.
   - `(3,1,2)`: the content channel alone gives `R = 4`, so there is no certificate at any `c`.

**(a) ABOVE.**
1. **Reflection positivity through site planes holds for every positive law** (PROVED), not only in block 39's bond-plane region (`c ≥ c₀`, `p ≥ q`, `p + q ≥ 2r`, which is CHECKED and agrees with a1). So the chessboard estimate is available for all `(c, p, q, r)`, including `(5,2,4)`, which a1 found outside the bond-plane region.
2. **The block events.** Take unit-cube blocks `{0,1}³ + x`, one per site; neighbouring cubes share faces. A cube is good-empty, good-dense or bad. Two face-adjacent good cubes share four sites, so they are of the same type, and bad cubes separate the phases.
3. **The chessboard factor.** The 254 bad occupancy patterns, disseminated by site reflections (period 2), fall into 16 exact classes `(ρ, e, κ)`:
   - `ρ` is the occupied fraction;
   - `e ≥ 3/4` is the density of mixed bonds;
   - `κ` bounds the cluster density.

   Summing contents with a spanning-tree bound, each class weighs at most `6^κ t^{ρ−κ} (cω*)^{−e/2}` per cube.
4. **The Peierls condition.** Connected sets of `k` cubes number at most `26^{2(k−1)}` (by depth-first codes), so `676·ε ≤ 1/4` suffices, with `ε = Σ_classes n·6^κ t^{ρ−κ}(cω*)^{−e/2}`.
5. **Exact certificates.** At `T/ω* = 2`, `cω* = 44⁸ ≈ 1.4·10¹³`. Content-less, `cw = 38⁸ ≈ 4.3·10¹²`.
6. **Numeric thresholds.** Roughly `cω* ≥ 4.8·10¹²` (`t → 1`) to `4.1·10¹³` (`t = 49/9`). The literature lattice-animal constant `26e` gives `10¹⁰ – 10¹¹`.
7. **The last step.** Passing from these estimates to coexistence at some fugacity (continuity in `z`, a mixture of two states) is the standard FILS argument, ASSUMED.
8. **Honest scale.** The region is rigorous and explicit but very conservative. For content-less records the true threshold is `cw = exp(4K_c) = 2.4269` (literature), against the certified `2.7·10¹²`.

**(c) Content-less records.**
- `p = q = r = w` gives the weight `z^N(cw)^B`: exactly the lattice gas of bond activity `cw`, i.e. Ising with `K = ¼ log(cw)`.
- **Proved here:**
  - uniqueness at every `z` for `25/49 < cw < 49/25` (independence at `cw = 1`);
  - clumping at some `z` for `cw ≥ 38⁸`.
- **Literature:** the `Z³` Ising critical point, which puts the onset at `cw = exp(4K_c) = 2.4269`, above our certified uniqueness window (`1.96`).

## 2. Steps

**S1 (PROVED; CHECKED B.tv). The sharp one-site bound.**
- Put `H = E_P[h]`. Then `TV = E_P[(h − H)⁺]/H`.
- For `h ∈ [m, M]` with mean `H`, convexity of `(·)⁺` gives `E[(h − H)⁺] ≤ (H − m)(M − H)/(M − m)`, attained by the two-point law on `{m, M}`.
- Maximising over `H` gives `H = √(Mm)`, with value `(√M − √m)/(√M + √m)`.
- The two-point `f` with weights `√m : √M` attains it.
- CHECKED by sympy (the maximiser), by 300 random rational instances, and by an attained instance (`1/5` at `M/m = 9/4`).

**S2 (PROVED; CHECKED B.dobrushin). Dobrushin at every fugacity.**
- The conditional law at `x` is `∝ z_a Π_{y∼x} W(a, σ_y)`. Changing `σ_y` from `b` to `b′` multiplies it by `h(a) = W(a, b′)/W(a, b)`. The other factors, including `z`, are common, so S1 applies with `R = max h/min h`.
- Dobrushin's condition `Σ_y sup TV < 1` becomes `6 tanh(¼ log R_max) < 1`, i.e. `R_max < 49/25`.
- The windows are CHECKED exactly by computing `R_max` over all 42 ordered neighbour changes, at rational points just inside and just outside each boundary.
- Dobrushin's uniqueness theorem itself is ASSUMED (standard).

**S3 (PROVED; CHECKED A.rp). Reflection positivity.**
- **Bond planes.** The crossing weight `W(σ_x, σ_{θx})` is reflection positive iff the `7×7` matrix of `W` is positive semidefinite. Its Schur complement is `cΩ − J`, with eigenvalues `cT − 6`, `c(p − q)` and `c(p + q − 2r)`. That gives a1's region.
- **Site planes.** Nearest-neighbour bonds never cross a plane of sites. Split the in-plane bond weights and fugacities as square roots: the weight is `F₊θF₊`, so `⟨FθF⟩ = Σ_{plane} G² ≥ 0` for every positive law.

**S4 (PROVED; CHECKED A.patterns). The chessboard factor per unit cube.**
- **The estimate.** Site reflections generate the unit-cube block lattice, one cube per site. The chessboard estimate (FILS, ASSUMED) bounds `P(cube has occupancy pattern π)` by `(Z_π/Z)^{1/|Λ|}`, where `Z_π` is restricted to the disseminated pattern: period 2, `x ↦ π(x mod 2)`.
- **Numerator.** `Z_π ≤ z^{N_occ}(cω*)^{B_OO} · 6^C t^{N_occ − C}`. This uses the tree bound: over a cluster of `n` records, `Σ_contents Π ω/ω* ≤ Σ Π_{tree} ω/ω* = 6(T/ω*)^{n−1}`, because the extra bonds have `ω/ω* ≤ 1`.
- **Denominator.** `Z ≥ max(1, z(cω*)³)^{|Λ|}`, from the empty configuration and from the aligned (`ω* = p`), antipodally alternating (`q`) or axis-alternating (`r`) dense configurations. `Z³` is bipartite.
- **The ratio.** With `max(1, X) ≥ X^ρ` and `6ρ = 2b + e` (bond ends), the per-cube ratio is at most `6^κ t^{ρ−κ}(cω*)^{−e/2}`.
- **The cluster count.** `κ ≤` (components on the period-2 torus)`/8`, since a cell cluster tiles into at most one cluster per copy. Using this upper bound is valid because `6^κ t^{ρ−κ} = t^ρ (6/t)^κ` is increasing in `κ` for `t ≤ 6`, and `t ≤ 6` always.
- **The classes.** The 254 patterns fall into 16 classes, with minimum `e = 3/4` (one site differing).

**S5 (PROVED, with the lattice-animal bound self-contained; CHECKED A.threshold). The Peierls condition.**
- **Separation.** If the cube at `x` is good-empty and the cube at `y` is good-dense, the face-connected good cluster of `x` is bounded by a `*`-connected set of bad cubes that separates `x` from `y` (on the torus it may instead wrap, with size `≥ L²`).
- **Counting.**
  - A `*`-connected set of `k` cubes has a depth-first code of `2(k − 1)` steps with 26 choices each: at most `676^{k−1}` sets.
  - A separating set meets a fixed half-line within `k` steps: at most `k·676^{k−1}` sets containing one of those cubes.
- **The chessboard estimate for all `k` cubes at once** gives `ε^k`, with `ε = Σ_classes` of S4's bound.
- **The sum.** `Σ_k k·676^{k−1}ε^k = ε/(1 − 676ε)² ≤ (16/9)ε` once `676ε ≤ 1/4`.
- **CHECKED** in exact rational arithmetic, with upper bounds `2^{1/8} ≤ 1.0906` and `6^{1/8} ≤ 1.2511` verified to the 8th power, at `T/ω* = 2`, `cω* = 44⁸`, and content-less at `cw = 38⁸`.

**S6 (ASSUMED: FILS). From estimates to coexistence.**
- At small `z` the empty phase has probability `≥ 1 − ε`; at large `z` the dense phase does.
- The torus probabilities are continuous in `z`, so at some `z_L` both phases have probability `≥ 1/2 − O(ε)`.
- The limit of the torus states along a subsequence is then a nontrivial mixture of two translation-invariant states, with densities `≤ O(ε)` and `≥ 1 − O(ε)`.

**S7 (PROVED; CHECKED C.latticegas). Content-less records.**
- With `p = q = r = w`, the contents contribute the constant `6^N` (absorbed into `z`) and every record pair weighs `cw`: the lattice gas.
- At `cw = 1` the weight is a product over sites, so `R_max = 1`.
- The Ising correspondence and `K_c = 0.2216544…` are literature.

## 3. The first failing step

**(b)** has none: it is exact within Dobrushin's theorem.

**(a)** succeeds rigorously but with a very conservative constant. The bond-plane route, which would give per-block factors to the 8th power (period-4 patterns, `e ≥ 3/8`, and `cp` of order `10³` in the per-block count), fails at the separation step:
- non-overlapping `2×2×2` blocks let a good-empty block sit face to face with a good-dense block, with no bad block between them;
- bounding those interfaces through a second, shifted tiling costs a square root. That still gives about `10⁴–10⁵`, but needs a separation lemma for two interleaved tilings, which is not proved here.

## 4. What would finish it

1. **The two-tiling separation lemma** for bond-plane reflection positivity in block 39's region. It would bring the clumping bound from `10¹²` down to about `10⁴–10⁵`.
2. **Better constants.** Larger blocks, contour weights sharper than the union over 254 patterns (grouping by interface shape), and the lattice-animal constant.
3. **Between the brackets.** For content-less records the gap is `[1.96, 2.43]` between our uniqueness and the literature's onset; for the six-axis gas it is wide. A Monte Carlo onset (`probes/lib/moving_gas.py`) would locate the transition, not prove it.

## 5. Running it

```
python3 probes/work/derive/moving-clumping-bounds/w-macbookpro90c72-j046a/check.py
```

The run takes under a second. It makes six exact checks:
- sympy and 300 rational instances for the one-site bound;
- exact `R_max` windows;
- the Schur spectrum;
- the 254-pattern enumeration;
- the rational Peierls certificates;
- the lattice-gas reduction.

The two `note` lines are floating-point thresholds.
