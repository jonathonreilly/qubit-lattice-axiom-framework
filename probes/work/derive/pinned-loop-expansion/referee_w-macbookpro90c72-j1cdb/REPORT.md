# Referee report: J:derive:pinned-loop-expansion:a4

- **Author:** `w-jonathonsmac4f50-ja002` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-j1cdb` (`grok-4.6`). Different model family.
- **Target:** part (c) of the pinned-scale task, read as a no-go. The attempt does not claim coexistence. Parts (a) and (b) stay with attempt a2.
- **Checks:** own weight matrices, own content elimination, own torus and cube graphs. The author's `check.py` is not called.

## The statement that survives

At `c₀ = 6/S`, `W_eq = 6p/S` lies in `[6 l₁, 6)`. At the balance point `z_t = W_eq⁻³` every configuration weighs

`W_eq^{−|∂A|/2} · Π_{E(A)} (W/W_eq)`,

with `|∂A|` the number of record–vacancy bonds. Each of those bonds therefore weighs more than `6^{−1/2}` for every finite triple with `q + 4r > 0`. Sending `l₁ → 1` does not open a small parameter for density contours: the weights tend to the fixed positive values below, and the occupied-set law tends to one model,

`μ_∞(A) ∝ 6^{c(A) − |∂A|/2}`

at `z = 1/216`. That is the 3D Ising lattice gas at `J = (log 6)/4`, `h = 0`, with neighbouring records forced to agree and one of six contents on each occupied cluster. The cycle rank is supermodular, so this limit law is FKG. The 2×2×2 chessboard's single-configuration bad sum is at least `8/√6 > 3` for every such triple, and the event-form floor tends to `0.003963`.

## Steps

**1. Cap.** Each row of `W = 6 K₁` sums to 6, so no entry exceeds 6 when `p` is the largest pair weight. `W_eq − 6 l₁ = 6q/S` and `6 − W_eq = 6(q+4r)/S`. `W_eq ≥ 1` when `p ≥ q` and `p ≥ r`, because that forces `5p ≥ q + 4r`. Checked at the six listed triples and as rational identities.

**2. Balance-point energy.** On the `L = 3` torus the edge list has `3N` edges, each vertex has six neighbours, and each undirected edge is stored once. The handshaking `6|A| = 2|E(A)| + |∂A|` was checked on 52 subsets, including empty, full, a singleton and a half-space. Then `z_t^{|A|} W_eq^{|E(A)|} = W_eq^{−|∂A|/2}`. Squared weights match on the empty state, both aligned ground states, a content defect, a vacancy, an aligned domino, a misaligned domino, a single record, and twelve further configurations, at `(16,1,2)`, `(5,1,1)` and `(3,1,2)`. Weight 1 occurs exactly on the empty state and the fully occupied aligned states. The extra bulk factor at a general `z` is `(z/z_t)^{|A|}` and does not change the bond energies.

**3. Limit law.** With `K₁ = I`, content elimination gives `Φ = 6^{β₁}` on all 256 subsets of the open 2×2×2 and all 512 subsets of the 3×3×1. The bond identity `2|∂A| = 3N − Σ σ_i σ_j` is the same handshaking (`Σ σσ = |E| − 2|∂A|`) and was checked on the same `L = 3` subsets. At `z = 1/216` the prefactor `z^{|A|} 6^{|E|}` equals `6^{−|∂A|/2}`; the cluster factor `6^{c(A)}` is the content count already in `Φ`. The coupling is `J = (log 6)/4` because each disagreeing bond contributes `6^{−1/2} = e^{−2J}`.

**4. No small parameter.** On `(p,1,2)`, `W_eq = 6p/(p+9) = 6 − 54/(p+9)`. The limits are `6^{−1/2}`, `1/36`, `1/216`, `1/1296`, and `0` for the opposite and orthogonal ratios `q/p`, `r/p`. A domino summed on contents weighs `36 z_t²` because `Σ W = 36`. The open cube has 12 edges and is connected, so `β₁ = 5` and `z_t⁸ 6⁸ Φ → 6^{−11}`. At `p = 10⁶` the same cube, summed by elimination, is within `10^{−3}` of that value. Misaligned bonds are the only energies that grow.

**5. Supermodularity.** Adding `v` changes `β₁` by `(neighbours of v in A) − (components those neighbours meet)`. That increment does not fall when `A` grows: an added `u` adjacent to `v` raises it by the number of merged `v`-touching components, and an `u` not adjacent to `v` raises it by `j − 1` when it touches `j ≥ 1` of them. Every mixed second difference was recomputed on the 2×2×2, 3×3×1, 2×2×3 and 4×3×1 windows (no violations). The local increment matches the table on every site of the cube. Holley's inequality, which turns the lattice condition into stochastic monotonicity, stays assumed.

**6. Finite `p`.** Log-supermodularity of `Φ` was recomputed on the 2×2×2 at `(3,1,2)`, `(16,1,2)`, `(5,1,1)`, `(7,2,1)` and `(2,1,2)`, and on the 3×3×1 at the first three. No violation, including the triple `(2,1,2)` outside the positive-semidefinite regime. The same second differences on the 2×2×3 and the 4×3×1 at `(3,1,2)` were recomputed separately (0 violations). Those two windows are not repeated in `check.py`. This remains a check, not a proof.

**7. Kernel.** The 7×7 bond matrix (1 against an empty end, `W` between records) has determinant 0 and all 127 principal minors nonnegative at `(3,1,2)`, `(16,1,2)` and `(5,1,1)`. Reflection positivity for site-only bond-plane reflections, and the Fröhlich–Israel–Lieb–Simon chessboard estimate, stay assumed.

**8. Disseminated weight.** On eight explicit blocks, at `z = 1/50` and at `z_t`, for `(16,1,2)` and `(5,1,1)`, the weight of the folded configuration on the `4³` torus is `w(b)⁸`. At `z_t` that block weight is the internal balance-point weight. The cube is 3-regular, so the exponent `3n/2` is the degree-3 form of step 2. Crossing bonds join a site to a mirror of itself.

**9. Single-configuration bound.** The empty block and the six aligned full blocks are exactly the weight-1 blocks. Grouping the cube by occupied set puts at least 7 into the even part and at least 48 into the odd part (one record, six contents, eight sites), so `Z_cube − 7 ≥ 48 W_eq^{−3/2}`. Since `W_eq < 6` this exceeds `8/√6`. The four printed bad sums match to the cent: `110226.56`, `128.00`, `29.29`, `22.57`. The limit sum, split into rational and `√6` parts, is exactly `152/9 + 136 √6 / 27`. One decimal slip: `8/√6 = 3.2659…`, which prints as `3.27` but is not strictly above `3.27`. Vacuity near the two ground states (`Z^{1/n}` near 1) is unaffected.

**10. Event form.** The `4³` torus is bipartite, so the 32 even sites form an independent set, four in each 2×2×2 block of the tiling. Configurations supported on those sites, with at least one record in every block, weigh `((1+6z_t)⁴ − 1)^n` and are entirely bad. The comparison `Z ≤ Z_cube^n` is the assumed chessboard bound. Given it, the floor `((1+6z_t)⁴ − 1)/Z_cube` matches `0.00053`, `0.00367`, `0.00418`, `0.00398`, and the limit is `0.003963`, which prints as `0.00396`.

**11. Heuristics.** `e^{−4J} = 1/6` is exact. The balance line with dilute density `6z/(1+6z)` meets densities `0.1, 0.3, 0.5, 0.7` at `p = 15.32, 6.04, 3.91, 2.66`, the printed `15.3, 6.0, 3.9, 2.7`. The literature onset `e^{4K_c} = 2.427` is not used. These lines are not part of the claim.

## Verdict

The no-go survives. Large `l₁` makes content disorder costly and does not make a density contour cost more than `(log 6)/2` per record–vacancy bond. An explicit coexistence region still needs a contour estimate for the fixed limit model at per-plaquette weight `6^{−1/2}`. The attempt already says that, and does not claim the estimate.
