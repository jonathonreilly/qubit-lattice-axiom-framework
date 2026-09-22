# pinned-loop-expansion, attempt 2 of 4: the occupied set at c₀ is Bernoulli occupancy decorated by a gas of leafless subgraphs

Worker `w-jonathonsmac4f50-ja55c` (`claude-opus-5-5`), unit `J-derive-pinned-loop-expansion:a2`.

**Provenance.** There were no prior attempts. The definitions come from the unit's statement, blocks 39–40 (PRs #8530,
#8546, both by the same model family as me), and block 39's T5 spectrum. The Kotecký–Preiss criterion is a classical import and
is marked ASSUMED where it is used.

## 1. What is claimed

**Setting.**
- Contents are the six axes `±e_i`. The pair weights are `ω = p, q, r` for equal, opposite and orthogonal contents, and
  `S = p + q + 4r`.
- At the pinned scale `c₀ = 6/S`, the record–record weight is `W = c₀ω = 6K₁`, where `K₁ = ω/S` is symmetric and doubly
  stochastic.
- The eigenvalues of `K₁` are `1`, then `l₁ = (p−q)/S` three times (odd modes) and `l₂ = (p+q−2r)/S` twice (even traceless
  modes).
- The occupied set `A` has law `μ(A) ∝ (6z)^{|A|} Φ(A)`, with `Φ(A) = E_s[Π_{e∈E(A)} 6K₁(s_e)]` over independent uniform
  contents. For an edge set `H`, write `w(H) = E_s[Π_{e∈H} (6K₁(s_e) − 1)]` and `ρ₀ = 6z/(1+6z)`.

> **(a) The expansion (exact).** `Φ(A) = Σ_{H ⊆ E(A) leafless} w(H)`, where the sum runs over edge sets with every degree ≥ 2
> (∅ included). The weight factorises over connected components:
> - A component with no branch vertex is an `n`-cycle, with `w = tr K₁ⁿ − 1 = 3l₁ⁿ + 2l₂ⁿ`. So a unicyclic set gets
>   `1 + 3l₁ⁿ + 2l₂ⁿ`.
> - A component with branch vertices (degree ≥ 3) splits into strands of lengths `L` between them, and
>   `w = E_{branch contents}[Π_strands (6K₁^L − 1)(s_u, s_v)]`. This is the transfer of `K₁` along strands, contracted at the
>   branch vertices.
> - In the eigenbasis each strand carries one mode (`l₁^L` or `l₂^L`) and each branch vertex a fusion tensor. For three modes
>   the fusion weights are `F_VVE = 6`, `F_EEE = 2` and `F_VVV = F_VEE = 0`.
> - **Two cycles sharing edges** form a theta graph with strands `a, b, c`:
>   `Φ = 1 + Σ_{its 3 cycles}(3l₁ⁿ + 2l₂ⁿ) + 6(l₁^{a+b}l₂^c + l₁^{a+c}l₂^b + l₁^{b+c}l₂^a) + 2l₂^{a+b+c}`.
>
> **(b) The density.** The grand partition function on any finite graph is
> `Ξ = (1+6z)^N Σ_{H leafless} w(H) ρ₀^{|V(H)|}`. So the occupied set is independent Bernoulli(`ρ₀`) occupancy, decorated by a
> polymer gas of connected leafless edge sets, each with activity `w(γ)ρ₀^{|V(γ)|}`, where vertex-disjoint polymers are
> compatible. Consequences:
> - `⟨n_x⟩ = ρ₀ + (1−ρ₀)·P(x ∈ V(H))`, exactly.
> - On `Z³`, `⟨n_x⟩ = ρ₀ + 12(3l₁⁴ + 2l₂⁴)ρ₀⁴ + O(ρ₀⁵)`, and the nearest-neighbour covariance begins
>   `4(3l₁⁴ + 2l₂⁴)ρ₀⁴`. Plaquettes lead, and the correction is positive, a first sign of clumping.
> - The activities obey `|w(γ)| ≤ 5^{#strands} λ^{|E(γ)|}`, with `λ = max(|l₁|, |l₂|)`.
> - With the Kotecký–Preiss criterion (**ASSUMED**), the density is analytic in `z`, so there is no clumping transition,
>   for **every** `z` when `λ ≤ 0.0024`, and for small `z` when `λ ρ₀^{1/3} ≤ 0.0029`.
>
> **(c)** Not attempted, beyond the limit `p → ∞` (`l₁, l₂ → 1`). There `μ(A) → z^{|A|} 6^{|E(A)| + c(A)}`, with `c` the
> number of occupied clusters: a lattice gas with bond attraction `log 6` and a cluster-count factor. That is the model a
> chessboard or contour argument would have to control.
>
> **(d)** On the line `(p,1,2)`, where `p ≥ 3` is needed for a positive semidefinite rule, `λ ≥ 1/6`. The proved region
> therefore reaches only densities `ρ₀ ≤ 5·10⁻⁶` at `p = 3` and `≤ 7·10⁻⁷` at `p = 6`. That is orders of magnitude from the
> executed onsets (densities `0.1–0.7` at `p = 6–16`), so this attempt does not locate them.

## 2. The steps

1. **PROVED + CHECKED (A1).** `K₁` commutes with the axis permutations and with the sign flips. The odd functions (a sign on one
   axis) give eigenvalue `(p−q)/S`, and the even traceless axis functions give `(p+q−2r)/S`, as in block 39's T5. Checked
   symbolically. A fully occupied cycle has `Φ = tr K₁ⁿ`.
2. **PROVED + CHECKED (A2): leaves vanish.**
   - Expand `Π_e 6K₁ = Π_e (1 + (6K₁ − 1))` over subsets `H`. This gives `Φ(A) = Σ_{H ⊆ E(A)} w(H)`.
   - If `v` is a leaf of `H`, integrating `s_v` first gives `E_{s_v}[6K₁(s_v, s_u) − 1] = 0`, because `K₁` is doubly
     stochastic. So only leafless `H` survive.
   - A forest has only `H = ∅`, so `Φ = 1` and occupancy is independent with density `6z/(1+6z)`. Checked on a path, a star
     and a comb at three weight triples.
3. **PROVED + CHECKED (A3, A4): the component rule.**
   - Integrate out the degree-2 vertices of a strand of length `L` (uniform average over its `L − 1` inner contents). With
     `J` the all-ones matrix, this gives `6^{1−L}((6K₁ − J)^L)(s_u, s_v) = 6((K₁ − J/6)^L)(s_u, s_v) = 6K₁^L(s_u, s_v) − 1`.
     The last step holds because `K₁` fixes constants, so `(K₁ − J/6)^L = K₁^L − J/6`.
   - What remains is the expectation over branch-vertex contents. A branch-free component is a cycle:
     `6^{−n} tr((6K₁ − J)ⁿ) = tr((K₁ − J/6)ⁿ) = tr K₁ⁿ − 1`.
   - *Spectral form.* `6K₁^L − 1 = Σ_{m=1}^5 λ_m^L ψ_m ⊗ ψ_m`, with `ψ_m` orthonormal for the uniform content (checked).
   - *The theta graph.* Two degree-3 branch vertices give `Σ_{m₁m₂m₃} λ^a λ^b λ^c E[ψ_{m₁}ψ_{m₂}ψ_{m₃}]²`. Grouping by modes
     gives the fusion weights `F_VVE = 6`, `F_EEE = 2`, `F_VVV = F_VEE = 0`; odd cubes vanish by `s ↦ −s`.
   - **CHECKED exactly** against brute-force content sums: thetas `(1,3,3)` (the domino on `Z³`), `(2,2,2)`, `(1,2,2)`,
     `(1,2,4)`, `(3,3,3)`; and the general rule on `C₄`, the domino, the `2×4` ladder and the cube (175 leafless edge sets).
     All at `(p,q,r) = (3,1,2), (5,1,1), (7,2,1)`.
4. **PROVED + CHECKED (B1–B3): the polymer representation.**
   - Swap sums: `Ξ = Σ_A (6z)^{|A|} Σ_{H ⊆ E(A)} w(H) = Σ_H w(H) Σ_{A ⊇ V(H)} (6z)^{|A|}`. Every `H ⊆ E(G)` with
     `V(H) ⊆ A` lies in `E(A)`, so this is `Σ_H w(H)(6z)^{|V(H)|}(1+6z)^{N−|V(H)|}`.
   - Per site, `⟨n_x⟩ = E_H[1_{x∈V(H)} + ρ₀ 1_{x∉V(H)}]` under the signed polymer measure.
   - **CHECKED exactly** on the cube window: the identity in `z`; the density series, with `ρ₀⁴` coefficient `3w₄` (three
     faces per vertex) and nothing at orders 2–3; and the nearest-neighbour covariance series, with `ρ₀⁴` coefficient `2w₄`
     and nothing below. On `Z³` the counts are 12 plaquettes per site and 4 per edge.
5. **PROVED + CHECKED (B4, B5): the activity and counting bounds.**
   - Each strand kernel has entries `|6K₁^L − 1| ≤ λ^L Σ_m |ψ_m(a)ψ_m(b)| ≤ 5λ^L`, since `Σ_{m≥1} ψ_m(a)² = 5`. Checked for
     `L ≤ 6`. So `|w(γ)| ≤ 5^{#strands}λ^{|E|} ≤ (5λ)^{|E|}`.
   - Leafless graphs on `Z³` have `|V| ≥ |E|/3` (maximum degree 6).
   - Connected edge sets with `n` edges through a vertex number at most `36ⁿ`: an Euler tour of the doubled edge set is a
     closed walk of length `2n` with at most 6 choices per step. Exact counts for `n = 1..4` are `6, 45, 380, 3402`.
6. **ASSUMED (Kotecký–Preiss), then CHECKED arithmetic (B6).**
   - With `a(γ) = |V(γ)|/4`, compatibility failure means sharing a vertex. So it suffices that
     `Σ_{γ∋v}|ζ(γ)|e^{|V(γ)|/4} ≤ 1/4`, and this is at most `Σ_{n≥4} xⁿ = x⁴/(1−x)`.
   - This holds for `x ≤ 57/100`.
   - *All `z`* (`|ρ₀| ≤ 1`): `x = 180λe^{1/4}` gives `λ ≤ 0.00246`.
   - *Small `z`:* `x = 180λ(ρ₀e^{1/4})^{1/3}` gives `λρ₀^{1/3} ≤ 0.00291`.
   - The cluster expansion then converges uniformly in a complex neighbourhood, so the pressure and the density are analytic
     in `z`.
7. **PROVED + CHECKED (C0): the `p → ∞` limit.** `W → 6δ(s,s')`, so `Φ(A) → 6^{|E(A)|}·6^{c(A)−|A|}`.
8. **CHECKED (D1): the line `(p,1,2)`.** `l₁ = (p−1)/(p+9)` and `l₂ = (p−3)/(p+9)`, with the region's density thresholds as
   stated.

## 3. Where this stops

- **(c) is not attempted.** The first open step is a chessboard estimate for the law with vacancies at `c₀`: reflection
  positivity holds by block 39's T5, but its degenerate direction at `c₀` (the null vector of the bond kernel) is exactly the
  one the estimate must avoid. After that comes a Peierls count for the limiting gas `z^{|A|}6^{|E|+c}`, carried to large but
  finite `p`.
- **(b)'s region is crude.** The `36ⁿ` count and `|V| ≥ |E|/3` waste a lot: cycles have `|V| = |E|`, and polygons grow like
  `μⁿ` with `μ ≈ 4.7`, not `36ⁿ`. A polymer count by excess `|E| − |V|` would move the region by orders of magnitude, but not,
  it seems, to the executed onsets.
- **What is proved about clumping is only its absence**, in the region. The sign of the leading density correction (positive,
  plaquette-driven) is a tendency, not an onset.
- **Only the six-axis menu is treated.** The sphere menu's version (modes `ℓ ≥ 1`, eigenvalues `a_ℓ/a₀`) follows the same
  pattern with infinitely many modes. It is not done here.

## 4. What would finish it

1. A sharper polymer count (by excess), which gives an explicit analyticity line `ρ₀ < f(λ)` to set against the executed onsets.
2. (c): the chessboard estimate at `c₀` and the Peierls argument for `z^{|A|}6^{|E|+c}`, then perturbation to finite `p`.
3. The density-density correlation beyond leading order: its decay rate `ξ⁻¹ ≥ −log(C λ ρ₀^{…})` from the cluster
   expansion's tree bounds.
4. A referee from another model family.

## 5. Running it

```
python3 probes/work/derive/pinned-loop-expansion/w-jonathonsmac4f50-ja55c/check.py
```

It needs sympy and has 13 checks, all exact (`fractions`, `sympy`); the only floats are printed decimals. It runs in about 45
seconds, most of it the cube window's brute-force content sums. `loopexp.py` beside it holds the elimination and strand code.
