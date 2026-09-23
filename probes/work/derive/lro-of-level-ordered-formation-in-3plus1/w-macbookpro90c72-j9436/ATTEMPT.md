# J:derive:lro-of-level-ordered-formation-in-3plus1:a1 — the level-ordered law is a reversible diamond-lattice chain followed by an inversion; each named route fails at an identified exact step

**Provenance.**
- Worker `w-macbookpro90c72-j9436`, model `claude-opus-5-5`, one session. The claim printed no prior attempts.
- The law is the one the scans execute: `probes/lib/formation_levelplane.py`, `dim = 3`, menu `sphere`, non-symmetric neighbourhood. Its docstring identifies it with the campaign's level-ordered formation law.
- The light-cone law, and its proof of long-range order, come from harvest issues #8463 (a5) and #8631, which the task names as its setting, and from `probes/work/derive/lightcone-long-range-order/`. I formed the plan below (diamond structure plus inversion) before reading the light-cone attempt files, then read them to match their steps.
- Executed plateau values come from the committed logs of `X:formation-3plus1-finite-size`.
- Every clause is supplied; nothing is adopted.

## 1. The statement attempted

**Objects.**
- **Torus and records.** The torus is `(Z/L)³`, with `N = L³` sites. The records are `s = (s_x) ∈ (S²)^N`. `λ` is the product of the normalized surface measures.
- **Functions.** `Z(q) = sinh q / q`, so `∫ e^{q u·r} dr/(4π) = Z(|q|)`. `A = (log Z)' = coth q − 1/q`, the Langevin function.
- **Sums.** Backward: `S_x(s) = Σ_{d ∈ N4} s_{x−d}`, with `N4 = {0, e₁, e₂, e₃}`. Forward: `S^f_x(s) = Σ_{d ∈ N4} s_{x+d}`.
- **The level-ordered law.** `K(r | s) = Π_x e^{β r_x·S_x(s)} / Z(β|S_x(s)|)`, a density with respect to `λ`. In the code, `np.roll(s, 1, axis=j)` is `s_{x−e_j}`.
- **The light-cone law.** The same, with `N7 = {0, ±e_j}` in place of `N4`.
- **Inversion.** `(ιs)_x = s_{−x}`. The mirror law is `K^ι = ιKι`, whose stencil is `−N4`.
- **The doubled graph.** `Γ_L` has vertices `(x, a)`, `a ∈ {0, 1}`, and edges `(y, 0)–(x, 1)` with `x − y ∈ N4`. `Γ^lc_L` is the same with `N7` (the graph of #8463/#8631).
- **The Gibbs measure.** `G_L(s, r) ∝ e^{β B(r, s)}` with `B(r, s) = Σ_x r_x·S_x(s)`: the Heisenberg model on `Γ_L`.
- **Its layer marginal.** `ρ_L(s) = 𝒵⁻¹ Π_x Z(β|S_x(s)|)`, the layer-0 marginal of `G_L`.
- **The reversible neighbour.** `Q` = `K` followed by `ι`, i.e. `Q(r | s) = K(ιr | s)`.
- **Stationary law.** `π_L` is the stationary law of `K`.
- **Long-range order.** `⟨|m|²⟩_{π_L} ≥ c > 0` uniformly in `L`, where `m = N⁻¹ Σ_x s_x`.

**Task (a).** A proof route for long-range order of `π_L` (comparison with the light-cone law, a coupling to a reversible law, a contour argument in level time, or the linear theory's `1/L`), or an exact reason each route fails.

**Obtained (PARTIAL).** No proof of long-range order. The following is new and exact.

1. **(A) `Γ_L` is the diamond lattice.** It is a spanning subgraph of `Γ^lc_L`, and the level-ordered histories live on the hypercubic `Z⁴`.
2. **(B) `K` is `Q` followed by `ι`, with `Q` reversible for `ρ_L`.**
   - One step of `K` maps `ρ_L` to its mirror image: `ρ_L K = ι_*ρ_L`.
   - The alternating law (`K`, then `K^ι`) equals `Q∘Q`. It is local and reversible for `ρ_L`.
3. **(C) For every `β > 0` and `L ≥ 3`, `ι_*ρ_L ≠ ρ_L`.** Hence:
   - `K` has no inversion-symmetric stationary law;
   - `π_L ≠ ρ_L`;
   - `K` is not reversible: an explicit 3-cycle has ratio `e^β`.
   The two laws `ρ_L` and `ι_*ρ_L` agree through order `β²` and differ at order `β⁴`.
4. **(D) Each of the four routes fails at an identified exact step** (section 3).

## 2. Steps

### Part A: the diamond lattice

**S1 (PROVED; CHECKED G.diamond, G.spacetime).**
- **The diamond.** `Γ_L` is 4-regular. Map it to `R³` by the integer map `A e_j = v₀ − v_j`, with `v₀ = (1,1,1)`, `v₁ = (1,−1,−1)`, `v₂ = (−1,1,−1)`, `v₃ = (−1,−1,1)`:
  - `(y, 0)` goes to `A y`;
  - `(x, 1)` goes to `A x − v₀`;
  - the four bond vectors (bottom minus top) are exactly `v₀, …, v₃`, with `|v_i|² = 3` and `v_i·v_j = −1` for `i ≠ j`;
  - `A(Z³)` is the FCC lattice spanned by `(0,2,2), (2,0,2), (2,2,0)`.

  This is the diamond structure (FCC plus FCC shifted by `(1,1,1)`, tetrahedral bonds). On the tori `L = 4` and `6`, the girth is 6 at a vertex of each layer. `Γ^lc` is 7-regular with girth 4.
- **The staggered bilayer.** `(x, a) ↦ (x, a + |x| mod 2)` maps `Γ_L` onto a bilayer that keeps all vertical bonds. In layer `a` it keeps only the bonds `{y, y + e_j}` with `|y| ≡ a`. For `Γ^lc`, the same map gives the full bilayer (#8631). Each bond of `Z³` appears in `Γ^lc` in both layers, and in `Γ_L` in one layer.
- **Inclusion.** `E(Γ_L) ⊂ E(Γ^lc_L)`, since `N4 ⊂ N7`.
- **Space-time.** `(t, x) ↦ (t − |x|, x)` sends the predecessors `(−1, 0)` and `(−1, −e_j)` to the four negative unit vectors of `Z⁴`. So the bonds of a level-ordered history are the nearest-neighbour bonds of `Z⁴`.

### Part B: `K` is a reversible chain followed by an inversion

**S2 (PROVED; CHECKED R.bilinear).**
- **The identity.** `B(ιa, ιb) = B(b, a)`. Both sides equal `Σ_{d ∈ N4} Σ_{u + v = −d} a_u·b_v`.
- **The forward form.** `B(r, s) = Σ_y s_y·S^f_y(r)`, by relabelling `y = x − d`.
- **The check.** Both are checked exactly on random rational records (rational points of `S²`) for `L = 3, 4, 5`.

**S3 (PROVED). The marginals, and reversibility of `Q`.**
- Since `∫ e^{β r·S} dr/(4π) = Z(β|S|)`, we have `ρ_L(s) K(r | s) = 𝒵⁻¹ e^{βB(r, s)}`.
- Integrating out `s` with S2's forward form gives the `r`-marginal `𝒵⁻¹ Π_y Z(β|S^f_y(r)|)`. Also `S_x(ιr) = S^f_{−x}(r)`. So the `r`-marginal is `ρ_L(ιr)`, i.e. `ρ_L K = ι_*ρ_L`.
- `ρ_L(s) Q(r | s) = 𝒵⁻¹ e^{βB(ιr, s)}`. By S2 with `a = s`, `b = ιr`, we get `B(ιr, s) = B(ιs, r)`. So `ρ_L(s) Q(r | s) = ρ_L(r) Q(s | r)`: **`Q` is reversible for `ρ_L`**.
- `K = Q∘ι`, since `ι² = 1`.
- `Q∘Q = K ι K ι = K (ιKι) = K` followed by `K^ι`. This is the alternating law, which is local. It is reversible for `ρ_L` because `Q` is.

**S4 (PROVED). Uniqueness (Doeblin).**
- Every factor of `K(r | s)` is at least `e^{−4β}/Z(4β)`. So `K(· | s) ≥ c λ` with `c = (e^{−4β}/Z(4β))^N > 0`, uniformly in `s`. The same bound holds for `Q`.
- Write `K = cλ + (1 − c)R` with `R` a Markov kernel. Then `‖μK − νK‖_TV ≤ (1 − c)‖μ − ν‖_TV`.
- So `K` has exactly one stationary law `π_L`, and `Q` has exactly one, which by S3 is `ρ_L`.

### Part C: `ρ_L` is not inversion-symmetric

**S5 (PROVED; CHECKED M.counts, M.ratio, M.lazarevic). `ι_*ρ_L ≠ ρ_L` for every `β > 0` and `L ≥ 3`.**
- **The configuration.** Let `s_F` have records `−e_z` on `F = {0, −e₁, −e₂}` and `e_z` elsewhere.
- **Backward tetrahedra.** `T_x = x − N4` meets `F` for the ten sites
  `x ∈ {0} ∪ {e₁, e₂, e₃, −e₁, e₂ − e₁, e₃ − e₁, −e₂, e₁ − e₂, e₃ − e₂}`.
  - `T₀` contains all of `F`, so `|S|² = 4`.
  - The nine others contain one flipped record each, so `|S|² = 4`.
  - Result: `{4: 10, 16: N − 10}`.
- **Forward tetrahedra.** `x + N4` meets `F` for `x ∈ {−e₁, −e₂, −e₁−e₂}`, each containing two flipped records (`|S|² = 0`), and for six others, each containing one (`|S|² = 4`).
  - Result: `{0: 3, 4: 6, 16: N − 9}`.
- **Validity for all `L ≥ 3`.** Every site involved (the tetrahedra's base points and members) has entries in `{−2, …, 1}`. So for `L ≥ 5` nothing wraps and the counts are those of `Z³`. The counts are CHECKED exactly for `L = 3, …, 8`, which covers the small tori where wrapping could occur.
- **The ratio.** `ρ_L(ιs)/ρ_L(s) = Π_y Z(β|S^f_y(s)|) / Π_x Z(β|S_x(s)|)`, since `S_x(ιs) = S^f_{−x}(s)`. At `s_F`, with `u = 2β`, this equals

  `Z(0)³ Z(2β)⁶ Z(4β)^{N−9} / (Z(2β)^{10} Z(4β)^{N−10}) = Z(4β)/Z(2β)⁴ = u³ cosh u / sinh³ u`.
- **Why the ratio is below 1.** From `sinh 3x = 3 sinh x + 4 sinh³ x`:

  `sinh³ x − x³ cosh x = Σ_{n odd} [(3ⁿ − 3)/4 − n(n−1)(n−2)] xⁿ/n!`.
  - The bracket is 0 for `n = 3, 5`, and positive for `n = 7` (`546 − 210`).
  - Induction for odd `n ≥ 7`: `(3^{n+2} − 3)/4 = 9(3ⁿ − 3)/4 + 6 ≥ 9n(n−1)(n−2) + 6`, and `9n(n−1)(n−2) + 6 − (n+2)(n+1)n = 8n³ − 30n² + 16n + 6`. At `n = 7 + m` this has coefficients `8, 138, 772, 1392`, all positive.
  - So every coefficient is `≥ 0` and the `n = 7` coefficient is `> 0`. Hence `x³ cosh x < sinh³ x` for `x > 0` (Lazarević's inequality, re-proved here), and the ratio is `< 1` for every `β > 0`.
- **Conclusion.** Both densities are continuous and they differ at `s_F`, so `ι_*ρ_L ≠ ρ_L` as measures.
- **`L = 2` is excluded.** There `ι` is the identity and `−N4 ≡ N4`, and the law is reversible (CHECKED R.cycle).

**S6 (PROVED). Consequences.**
- **No inversion-symmetric stationary law.** Suppose `πK = π` and `ι_*π = π`. Then `πQ = ι_*(πK) = π`, so `π = ρ_L` by S4. Then `ι_*ρ_L = ρ_L`, contradicting S5. So `K` has no inversion-symmetric stationary law, and in particular `π_L ≠ ι_*π_L`.
- **`π_L ≠ ρ_L`.** `ρ_L K = ι_*ρ_L ≠ ρ_L`.
- **The magnetization sees nothing at one step.** `|m|` is inversion-invariant, and every translation-invariant two-point function is too, since `⟨s₀·s_r⟩ = ⟨s_{−r}·s₀⟩`. So one step of `K` from `ρ_L` leaves the law of `|m|` unchanged. The asymmetry lives in three-point and higher correlations.

**S7 (PROVED; CHECKED R.cycle). `K` is not reversible for any measure.**
- **Kolmogorov's criterion for densities.** If `K` were reversible for some law `m`, then `m` would have the continuous positive density `h = ∫ m(ds′) k(· | s′)`. Detailed balance `h(s) k(r | s) = h(r) k(s | r)` would hold everywhere, by continuity. Multiplying it around a 3-cycle cancels `h`, and cancels the normalizers `Z` too (each configuration is the source once on each side).
- **What remains.** `exp(β Σ_i [B(s_{i+1}, s_i) − B(s_i, s_{i+1})]) = 1` would be required.
- **The cycle.** Take: all `e_z`; `e_x` at 0; `e_y` at `e₁`. The sum is exactly 1 for `L = 3, …, 6`, so the ratio is `e^β ≠ 1`.
- **Controls.** The sum is 0 for the light-cone stencil, and for `L = 2`.

**S8 (PROVED; CHECKED M.gauss). The asymmetry is non-Gaussian.**
- **Order `β²` agrees.** `Σ_x |S_x|² = Σ_x |S^f_x|²` for every configuration. Both count each nearest-neighbour pair and each pair `{y, y + e_i − e_j}` once. Checked exactly on random rational records.
- **Order `β⁴` differs.** Since `log Z(q) = q²/6 − q⁴/180 + …`, the Gaussian parts of `log ρ_L` and `log ι_*ρ_L` coincide. The quartic tetrahedral invariant differs: `Σ|S|⁴` differs by `192` at `s_F`. So `log(ρ_L(ιs_F)/ρ_L(s_F)) = −16β⁴/15 + O(β⁶)`, a sympy series check.

### Part D: the ingredients of the route obstructions

**S9 (CHECKED C.aff, C.reflections; the necessary condition PROVED). Reflections.**
- **The candidate maps.** `Aff(N) = {(M, δ) : M ∈ GL(3, Z), MN + δ = N}` has 24 elements for `N4` (the permutations of the tetrahedron) and 48 for `N7` (signed permutations).
  - The maps are `(x, a) ↦ (Mx + c_a, a)` with `(M, c₁ − c₀) ∈ Aff`, and `(x, a) ↦ (Mx + c_a, 1 − a)` with `(−M, c₀ − c₁) ∈ Aff`, for `c₀ ∈ (Z/L)³`. All are automorphisms (CHECKED).
  - For `N4` they are all the affine automorphisms of the torus graph. An automorphism preserves or swaps the layers, `0 ∈ N4` forces `δ ∈ N4`, and `M e_j + δ ∈ N4` fixes `M` mod `L`.
- **The necessary condition.** For a fixed-point-free involution `θ` with halves `Λ± = θΛ∓`, the crossing weight is `exp(Σ_{u,w ∈ Λ+} J_{uw} s_u·s_{θw})` with `J_{uw} = β·1[{u, θw} ∈ E]`. Reflection positivity by the standard criterion needs `J` positive semidefinite.
  - A zero diagonal entry forces a zero row. So every endpoint of a crossing edge must carry a mirror edge `{v, θv}`.
  - Therefore every edge with an endpoint off the mirror edges lies inside one half.
  - Therefore no connected component of the graph of those edges may be `θ`-invariant.
- **Results.**
  - `Γ^lc_L`: 7 of 621 (`L = 4`) and 10 of 1392 (`L = 6`) fixed-point-free involutions pass. All of them are admissible in the strict sense of #8631 (only mirror pairs cross): the bond planes times the layer swap, and the layer swap. Their mirror pairs cover every edge.
  - `Γ_L`: 0 of 191 (`L = 4`) and 0 of 475 (`L = 6`) pass even the necessary condition.
  - The remaining involutions of `Γ_L` (73 at `L = 4`, 145 at `L = 6`) fix vertices, i.e. reflect through sites.
- **Crystallographic consistency.** The diamond lattice has no mirror plane that bisects a bond. Its mirrors `{110}` contain atoms, and the plane through the midpoint of a `[111]` bond would exchange the stacking positions `A ↔ C`.

**S10 (PROVED; CHECKED K.concave). The one-record update is not monotone in the `z`-order.**
- `A'' = 2(k³ cosh k − sinh³ k)/(k³ sinh³ k) < 0` by S5's inequality, so `A` is strictly concave with `A(0) = 0`. Hence `A(λq) > λA(q)` for `λ ∈ (0, 1)`.
- **The example.**
  - Predecessors `u, u, u, u` with `u = (4/5, 0, 3/5)` give mean `z` of the new record `(3/5)A(4β)`.
  - Predecessors `u, u, w, w` with `w = (−4/5, 0, 3/5)` have the same `z`-components, but give `A(12β/5)`, which is larger.
- So no coupling preserves the order of `z`-components. The same holds for the light-cone kernel.

**S11 (PROVED; CHECKED L.fcc). The linear theory is the lazy FCC walk, and it is inversion-symmetric.**
- **The identity.** `1 − |φ(k)|² = (3/4)(1 − λ_FCC(k))`, where `φ = (1 + Σ_j e^{ik_j})/4` and `λ_FCC` is the characteristic function of the 12 vectors `±e_j, ±(e_i − e_j)`. Equivalently `N4 − N4` is `0` four times plus the FCC shell: the two-step walk of the diamond.
- **Symmetry.** The linear stationary covariance `σ²/(1 − |φ|²)` is even in `k`, so the linear stationary law is inversion-symmetric.
- **The alternating linear law has the same covariance.** Two steps give `C = |φ|⁴ C + σ²(1 + |φ|²)`, hence `C = σ²/(1 − |φ|²)`. So the linear theory cannot tell `K` from `Q∘Q`.
- **The infinite-volume variance.** Per transverse component the linear variance is `σ² W_L`, with `W_L → (4/3)G_FCC(0) = 12Γ(1/3)⁶/(2^{14/3}π⁴) = 1.792882`. Watson's FCC integral is ASSUMED here; it is used only in the printed notes.
- **Notes (floating point).** `L(W_∞ − W_L) = 1.461, 1.460, 1.459` at `L = 16, 32, 64`, so the linear `1/L` law is `W_L ≈ W_∞ − 1.4595/L`.

**S12 (PROVED). The zero-noise law does not erode tilted islands.**
- **Set-up.** As `β → ∞`, `K` concentrates on `Φ(s)_x = S_x/|S_x|`. Every constant configuration is a fixed point, a continuum `S²`. Start with records `e_z`, except `u = (sin α, 0, cos α)`, `0 < α < π/2`, on a finite nonempty `F`.
- **Invariant.** Every later record is `(sin α_x, 0, cos α_x)` with `α_x ∈ [0, α]`.
  - `S_x` has `z`-component `≥ 4 cos α > 0`, so it is never zero.
  - Its angle lies in `[0, α]`, since that cone is convex.
  - The angle is positive iff some predecessor is tilted.
- **Growth.** So `D_{t+1} = {x : T_x ∩ D_t ≠ ∅} ⊇ D_t ∪ (D_t + e_j)` for `j = 1, 2, 3`: the tilted set never shrinks. On `Z³` it grows forever; on the torus it fills all sites within `3L` levels.
- **Consequence.** No tilted island is eroded in finite time, which is Toom's hypothesis for stability.

**S13 (PROVED; CHECKED T.twist). A twist has no positive wall cost.**
- **The history.** Take the static history `s_x = u_{x₁}` on a ring of unit vectors in the `xz`-plane, with `c_x = u_{x₁}·u_{x₁−1}`. Then `s_x·S_x = 3 + c_x` and `|S_x|² = 10 + 6c_x`. These are checked exactly on a rational ring with `u_{k+4} = −u_k` at `L = 8`, where `m = 0` exactly.
- **The bound.** Its per-site log density relative to the aligned history is `ℓ_x = β(c_x − 1) + log Z(4β) − log Z(β|S_x|)`. Since `A ∈ [0, 1)` and `0 ≤ 4 − |S_x| = 6(1 − c_x)/(4 + |S_x|) ≤ (3/2)(1 − c_x)`:

  `−β(1 − c_x) ≤ ℓ_x ≤ (β/2)(1 − c_x)`.
- **The uniform ring.** For the ring at angles `2πk/L`, a level costs at most `β L³ (1 − cos(2π/L)) ≤ 2π²βL`, and `m = 0` at every level.

## 3. The routes, and the first failing step of each

**(i) Comparison with the light-cone law.** The light-cone proof (#8463, #8631) has two ingredients:
- S1 there: `π^lc` equals the layer marginal of the doubled-graph Gibbs measure (reversibility);
- S2–S5 there: bond-cutting reflections give Gaussian domination.

Each fails here, exactly:
1. **First failing step: the identification of the stationary law with the layer marginal.** For the level-ordered law, the doubled-graph Gibbs measure is the diamond-lattice Heisenberg model. Its layer marginal `ρ_L` is not stationary (`ρ_L K = ι_*ρ_L ≠ ρ_L`, S3 and S5), and no reversible measure exists (S7).
2. **The reflections fail even for the reversible neighbour.** For `Q`, whose stationary law is `ρ_L`, no affine reflection of `Γ_L` has halves with a positive semidefinite crossing matrix (S9). So Gaussian domination is not available for `ρ_L` by the light-cone mechanism either.
3. **A direct comparison points the wrong way, or does not exist.**
   - `Γ_L` is a spanning subgraph of `Γ^lc_L` (S1). A coupling-monotone comparison, where one is available at all (Griffiths/Ginibre for the Ising and plane-rotator analogues; none is available in general for O(3)), bounds the level-ordered order from above by the light-cone order, never from below.
   - The one-record update is not monotone in the `z`-order (S10), so no such coupling exists for the sphere law.

**(ii) A coupling to a reversible law.**
- The reversible law built from the same kernel is `Q` (`K` followed by `ι`), and its local version is the alternating law `Q∘Q`. Both have the explicit stationary law `ρ_L` (S3).
- A coupling of `K` with `Q` agrees step by step iff `ι` acts trivially on the state.
- **First failing step: the inversion symmetry of the stationary state.** `K` has no inversion-symmetric stationary law (S6), and the difference is certified for every `β > 0` (S5).
- The obstruction is invisible to the linear theory and to every two-point function (S6, S8, S11). It first enters at order `β⁴` of the local weights.

**(iii) A contour argument in level time.**
- **First failing step: erosion.**
  - For the sphere menu, the zero-noise law has a continuum of fixed points.
  - Tilted islands are never eroded; they spread (S12).
  - So Toom's eroder hypothesis fails.
- **Peierls.** A twist through angle `π` over a half-period costs at most `2π²β/L` per unit of wall area per level (S13). No positive surface constant separates the ordered states.
- The obstruction is the continuous symmetry. It holds in the same form for the light-cone law, whose order is proved by spin-wave control (the infrared bound), not by contours.

**(iv) The linear theory's `1/L`.**
- The linear theory is exact for the Gaussian gain-one law:
  - it is the lazy FCC walk;
  - its transverse variance is `σ²W_L`, with `W_L = W_∞ − 1.4595/L + …` (S11, notes);
  - hence the plateau law `m(L) = m_∞ + b/L`.
- **First failing step: the infrared bound for the nonlinear law.** Turning this into a bound on `π_L` needs `Ŝ(k) ≤ C_β/(1 − |φ(k)|²)` for all `k`, with `C_β W_∞ < 1` (the sum rule then gives `⟨|m|²⟩ ≥ 1 − C_β W_L`). Its only standard source is Gaussian domination, which S9 excludes for `Γ_L`.
- **The linear theory cannot see the obstruction.** It is inversion-symmetric (S11), while the nonlinear law is not (S6).
- **Executed data (not claims).**
  - The low-`k` ratio of the committed finite-size logs is `1.00 ± 0.01` at `L = 96` (β = 2, 3): at long wavelengths the executed structure factor matches the bare linear one.
  - The executed plateaus lie below the linear prediction `1 − σ²W_∞`: `0.732` against `0.804` at `β = 2`, and `0.835` against `0.863` at `β = 3`. The executed slopes are about `0.19` and `0.12`, against the linear `σ² × 1.4595 = 0.160` and `0.111`.
  - So a constant `C_β` that makes the sum-rule bound true must exceed the linear value. The excess is carried by the non-Gaussian fluctuations at larger `k`.

**ASSUMED.**
- Watson's closed form for the FCC Green function. It is used only in the notes and in the value 1.792882, not in any claim.
- The identification of the executed law with the campaign's level-ordered law, as stated in the scan code's docstring.

## 4. What would finish it

1. **A non-reflection infrared bound for `π_L`.** A bound `Ŝ(k) ≤ C_β/(1 − |φ(k)|²)` with `C_β W_∞ < 1` would, with the sum rule, give long-range order. The executed low-`k` ratio (`≈ 1`) suggests the bound holds at long wavelengths with the bare constant.
2. **Via the diamond model.** Prove long-range order for `ρ_L` (the diamond-lattice Heisenberg marginal: the alternating law's stationary state). Then control `π_L − ρ_L` at large `β`. By S8 the difference starts at the quartic tetrahedral invariant, so a low-temperature expansion around `ρ_L` is the natural tool. The diamond lattice has no bond-bisecting mirror (S9), so the first half needs a method other than reflection positivity as well.
3. **Reflections through sites.** `Γ_L` has 73 (`L = 4`) and 145 (`L = 6`) affine involutions with fixed vertices (diagonal mirrors). They give reflection positivity through sites. Whether chessboard estimates from them control spin waves is open.
4. **The space-time specification.** By S1, the level-ordered histories are Gibbs for the O(3)-invariant finite-range specification on `Z⁴`: the nearest-neighbour Heisenberg bonds plus the corner terms `−log Z(β|S_e|)` over the four backward neighbours. A low-temperature renormalization or spin-wave method on `Z⁴`, which need not use reflections, would give long-range order of the space-time law and hence of `π_L`.

## 5. Running it

```
python3 probes/work/derive/lro-of-level-ordered-formation-in-3plus1/w-macbookpro90c72-j9436/check.py
```

The run takes about 2 s. It checks 13 exact facts, using Fractions, integer graph enumeration with numpy/scipy, and sympy identities. The two `note` lines are floating-point lattice sums and are not claims.
