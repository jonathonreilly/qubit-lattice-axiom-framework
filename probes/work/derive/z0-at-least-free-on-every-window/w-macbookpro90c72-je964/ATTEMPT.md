# J:derive:z0-at-least-free-on-every-window:a1: every arrangement weighs at least its records placed apart, on every window, at every triple

**Provenance.**
- Worker `w-macbookpro90c72-je964`, model `claude-opus-5-5`, one session. Unit a1; no prior attempt files exist on the branch.
- **Plan, formed before reading block 81's note and harvest #8627:**
  - split each content into an axis and a sign;
  - expand the three-axis part in `Z3` characters;
  - for negative `λ₂`, write the bond weight as a mixture of the free weight and the proper-colouring weight, and bound proper colourings of bipartite graphs;
  - run an exact search on the windows as a check.
- **Setting.** Block 81's notation, read on its PR branch: `M = c₀ω = J + 6λ₁P₁ + 6λ₂P₂`, `Z₀(η) = Σ_contents Π_bonds M(s_x, s_y)`, "free" `= 6^{|η|}`. Also T1 and T2 of #8626, and #8627's expansion into leafless edge sets.
- Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**(a) Theorem (PROVED; CHECKED A–E).**
- **Statement.** Let `η` be any finite arrangement of `Z³`, with recorded bonds `E` (the lattice bonds inside `η`). Let `(p, q, r) ≥ 0` with `T = p + q + 4r > 0`. At the neutral scale,

  `Z₀(η) ≥ 6^{|η|}`,

  with equality exactly when `η` has no cycle, or when `p = q = r` (then `M ≡ 1` and every arrangement weighs `6^{|η|}`).
- **Scope.** The proof uses only that the bond graph is bipartite. So it holds on every finite window, on every periodic window with even sides, and on every finite bipartite graph. It fails on odd rings (G).
- **Consequences.**
  - Block 81 T2 holds on every window. At every `g ≥ 1` the weight over free is `g^{|bonds|}Z₀/6^{|η|} ≥ 1`, so a chessboard (no bonds, weight `z^{|η|}6^{|η|}`) is a least-weighted arrangement of its record number on every window.
  - The grand sum at `c = g·c₀`, `g ≥ 1`, satisfies `Ξ = Σ_η z^{|η|}g^{|bonds|}Z₀(η) ≥ (1 + 6z)^N` on every window of `N` sites: the gas at an allowed scale is never lighter than independent placement.

**(b) Block 81 T1's bond factor.** Adding a lattice bond `xy` multiplies `Z₀` by `1 + 3t₁λ₁ + 2t₂λ₂`.
- **PROVED ≥ 1** for `λ₂ ≥ 0` (every `λ₁`) and for `λ₁ = 0` (every `λ₂`).
- **CHECKED exactly** on every bond set of the cube at triples with `λ₂ < 0 < λ₁`: the factor is ≥ 1, and equal to 1 exactly when `x` and `y` were in different components.
- **Not proved** in that region. At `(100, 1, 51)`, `t₂ > 0` while `λ₂ < 0` (F2), so no term-by-term argument can give the sign.

## 2. Steps

**Notation.**
- `n = |η|`. `U` and `V` are the even and odd sites; every bond joins `U` to `V`.
- `λ₁ = (p − q)/T`, `λ₂ = (p + q − 2r)/T`. Non-negative weights are equivalent to `λ₂ ∈ [−1/2, 1]` and `|λ₁| ≤ (1 + 2λ₂)/3`.
- `Z₀/6ⁿ` is the average of `Π M` over independent uniform contents.

**S1: axes and signs (PROVED; CHECKED A1–A3, D1).**
- **Split.** Write `s = σe_a` with sign `σ = ±1` and axis `a ∈ {1, 2, 3}`. Uniform contents are independent uniform axes and signs. The pair weight is:
  - `R = 6r/T = 1 − λ₂` for different axes;
  - `A + Bσσ'` for the same axis, with `A = 3(p + q)/T = 1 + 2λ₂` and `B = 3(p − q)/T = 3λ₁`.
- **The sign sum.** For fixed axes let `S(a)` be the bonds with equal axes. Then

  `E_σ Π_{S(a)} (A + Bσ_xσ_y) = Σ_{F ⊆ S(a), every degree even} A^{|S|−|F|} B^{|F|}`,

  since expanding the product and averaging leaves only those `F` in which every site carries an even power of its sign.
- **Every such `F` has an even number of bonds.** Each bond has exactly one end in `U`, so `|F| = Σ_{x∈U} deg_F(x)`, a sum of even numbers. So every term is ≥ 0, and the `F = ∅` term is `A^{|S(a)|}`:

  `Z₀/6ⁿ = Φ(λ₂) + R_η`, where `Φ(λ) = E_a Π_bonds [(1 − λ) + 3λ[a_x = a_y]]` and `R_η ≥ 0`.
- **When `R_η = 0`.** Exactly when `λ₁ = 0` or `η` is acyclic. If `η` has a cycle `C`, the assignment with all axes equal contributes `A^{|E|−|C|}B^{|C|} > 0`.
- Flipping every sign on `U` gives `Z₀(p, q, r) = Z₀(q, p, r)`.
- **Result.** A `λ₁` of either sign never lowers an arrangement. The question reduces to `Φ(λ₂)`, the three-state average of the axes.
- #8627's leafless expansion carries negative weights for thetas (`6l₁^{a+b}l₂^c` with `c` odd). Here they are regrouped into a sum with no negative terms.

**S2: `λ₂ ≥ 0` (PROVED; CHECKED B).**
- With `ω = e^{2πi/3}`, `3[a = a'] − 1 = ω^{a−a'} + ω^{a'−a}`.
- Expanding the product and averaging over the axes gives

  `Φ(λ) = Σ_{F⊆E} N₃(F) λ^{|F|}`,

  where `N₃(F) ≥ 0` is the number of nowhere-zero `Z₃` flows on `F`; it equals 2 on a cycle.
- So `Φ ≥ 1`, and `Φ > 1` when `λ > 0` and `η` has a cycle. This is the three-axis part of #8627's expansion; the theta term `2l₂^{a+b+c}` is `N₃(θ) = 2`.

**S3: `λ₂ < 0` (PROVED; CHECKED C1–C4).**
- **Mixture.** With `θ = −2λ₂ ∈ (0, 1]`, `(1 − λ₂) + 3λ₂[a = a'] = (1 − θ) + θ·(3/2)[a ≠ a']`. Expanding over bonds:

  `Φ(λ₂) = Σ_{F⊆E} (1 − θ)^{|E∖F|} θ^{|F|} Ψ(F)`, with `Ψ(F) = (3/2)^{|F|} hom((η, F), K₃)/3ⁿ`.

  Here `hom(H, K₃)` counts the colourings of `H` by the three axes with different axes on every bond.
- **Lemma K.** Every finite bipartite `H` with `n` sites and `e` bonds has `hom(H, K₃) ≥ 3ⁿ(2/3)^e`, with equality iff `H` is a forest.
- **Proof of Lemma K.**
  1. Add the bonds one at a time, starting from no bonds (`3ⁿ` colourings). Adding `uv`, with `u ∈ U` and `v ∈ V`, multiplies the count by `Pr[a_u ≠ a_v]` under the uniform proper colouring of the current graph.
  2. **Kempe map.** Take a colouring with `a_u = a_v = 0`. Let `K` be `v`'s component among the sites coloured 0 or 1, and swap 0 and 1 on `K`. The result is proper and has `a_v = 1`.
  3. `u ∉ K`: colours alternate along any path in `K`, and every `u–v` path has odd length, so `u` would carry colour 1.
  4. `K` is recovered from the image, so the map is injective. Hence `N(0,0) ≤ N(0,1)`, and by symmetry among the axes `Pr[a_u = a_v] = 3N(0,0)/(3N(0,0) + 6N(0,1)) ≤ 1/3`.
  5. **Strictness.** If `u` and `v` are already joined, the colouring `U ↦ 0`, `V ↦ 1` has `u` in `v`'s chain, so it is not an image and the inequality is strict.
- **Conclusion.** `Ψ(F) ≥ 1` for every `F`, so `Φ(λ₂) ≥ Σ_F (1 − θ)^{|E∖F|}θ^{|F|} = 1`.
- **Strict when `η` has a cycle `C`:**
  - for `θ < 1`, the term `F = C` has a positive coefficient and `Ψ(C) = 1 + 2^{1−|C|} > 1`;
  - for `θ = 1` (`p = q = 0`), `Φ = Ψ(E) > 1` by Lemma K's strictness.
- Lemma K is the case of target `K₃` of Sidorenko's inequality for bipartite graphs. The proof here is self-contained.

**S4: assembly (PROVED).**
- `Z₀/6ⁿ ≥ Φ(λ₂) ≥ 1`.
- **Equality.** If `η` has a cycle, either `λ₂ ≠ 0` and `Φ > 1` (S2, S3), or `λ₂ = 0 ≠ λ₁` and `R_η > 0` (S1). The only remaining case is `λ₁ = λ₂ = 0`, that is `p = q = r`.

**S5: the windows (CHECKED D, E).** Exact search, as the task asks, at triples with `λ₁ < 0` or `λ₂ < 0`: `(1,2,5)`, `(3,1,4)`, `(1,5,1)`, `(1,1,100)`, the last with `λ₂ = −99/201`.
- **Direct windows.** Every arrangement of `2×2×2`, `2×3` and `3×3` at all four triples, and of `2×2×3` at the first two. Equality holds exactly for the `188, 56, 415, 2466` acyclic arrangements, block 81's counts.
- **`2×3×3`.** All `262143` arrangements through their leafless cores. There are `675` classes up to the 48 lattice symmetries, and the core reduction is checked exactly on every `2×2×3` arrangement. Every class weighs strictly more than free; the smallest excess is `8.2·10⁻⁹` at `(3,1,4)`.
- **`3×3×3`.**
  - At `λ₁ = 0`, the case S1 reduces to, exact for the full window, the 27 windows with one vacancy, and 36 random arrangements, at `λ₂ = −1/3` and `−99/201`.
  - The full window at `(1,2,5)` in float64 (control): `2.3242`.

**S6: block 81 T1's factor (PROVED in two regions; CHECKED F).**
- **`λ₂ ≥ 0`.**
  1. Flipping the signs on `V` changes `λ₁` to `−λ₁` and leaves `Z₀` and the factor unchanged, so take `λ₁ ≥ 0`.
  2. The contents form the group `Z₂ × Z₃`, and `M(s, s') = Σ_χ λ_χ χ(s)χ̄(s')` with coefficients `1, λ₁ (×3), λ₂ (×2)`, all ≥ 0.
  3. Expanding gives every pair correlation `E[χ(s_x)χ̄(s_y)] ≥ 0` (Griffiths' first inequality in Ginibre's form). So `t₁, t₂ ≥ 0` and the factor is ≥ 1.
- **`λ₁ = 0`, `λ₂ < 0`.**
  1. By S3's expansion, the axis law is a mixture over `F` of uniform proper colourings of `(η, F)`.
  2. In each of these, `Pr[a_x = a_y] ≤ 1/3` by the Kempe map. So `2t₂λ₂ ≥ 0`.
- **`λ₂ < 0 < |λ₁|`.**
  - **Checked.** On every bond set of the cube and every added bond at `(5,1,4)` and `(100,1,51)`, the factor is ≥ 1, and equal to 1 iff the ends were in different components.
  - **Not proved.**
  - **The obstacle.** With `α = Pr[same axis]` and `ρ = Pr[same sign | same axis]`, the factor minus 1 is `3λ₁α(2ρ − 1) + 3λ₂(α − 1/3)`. The first term is ≥ 0 by the sign argument of S1. The second can be negative: F2 gives `t₂ = 3.55·10⁻³ > 0` with `λ₂ = −1/305`.

**S7: odd rings (CHECKED G).** Bipartiteness is used. A three-site ring, a periodic window of side 3, weighs `1 + 3λ₁³ + 2λ₂³ = 71/72` of free at `(1,3,2)`.

## 3. The first failing step

- **(a):** none; the statement is proved on every window.
- **(b):** the sign of `3t₁λ₁ + 2t₂λ₂` where `λ₂ < 0` and `λ₁ ≠ 0`. Neither tool applies:
  - the Kempe map on axes changes the `λ₁` weights on bonds leaving the chain;
  - Griffiths' inequality needs every channel ferromagnetic, and the `λ₂` channel is not.

## 4. What would finish it

1. **The bond factor where `λ₂ < 0 < |λ₁|`.** Candidates:
   - a move that recolours the axes along a Kempe chain and carries the sign clusters with it;
   - an inequality `t₂ ≤ c·t₁` that holds on bipartite graphs.
2. **Periodic windows of odd side.** An odd ring falls below free whenever `3λ₁ⁿ + 2λ₂ⁿ < 0`. Which arrangements do so there is not examined.

## 5. Running it

```
python3 probes/work/derive/z0-at-least-free-on-every-window/w-macbookpro90c72-je964/check.py
```

The run takes about 20 s and peaks near 250 MB. It prints exact checks A1–A3, B, C1–C4, D1–D3, E1, F1, F2 and G, one float control (E2), then the SUMMARY and HIT lines.

Standard mathematics used, none as authority:
- Kempe chains;
- `Z₃` characters and flows;
- Griffiths' first inequality in Ginibre's form;
- Sidorenko's inequality, named for comparison only.
