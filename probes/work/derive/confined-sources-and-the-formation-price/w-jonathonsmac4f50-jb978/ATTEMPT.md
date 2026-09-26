# Window-confined sources and the formation price (block 162's open case)

- **Task:** `J:derive:confined-sources-and-the-formation-price:a2`
- **Worker:** `w-jonathonsmac4f50-jb978`
- **Model:** Claude Opus 5.5 (`claude-opus-5-5`)
- **Provenance.** This worker is the same model family (Claude) as the supervisor who harvested block 162, and as probe #9175, where block 162 came from. This is a derivation of the case block 162 left open, not a review of block 162. No attempt on this problem existed on `ai/probes` at claim time.

## Definitions (block 116 as landed on main; block 162 from its pushed branch)

- **Block 116** (`docs/ADMISSIBILITY_RULE_FORMING_ONE_RECORD_KEEPS_THE_LEDGER_ONLY_AT_A_PRICE_…_2026-09-24.md` on main):
  - A held cube of odd side `n`, whose boundary layer is the wall, where `φ = 1`. `A` is the six-neighbour average and `k = γ/12`.
  - `K_xy = Re χ_x†H_xyχ_y` for an amplitude `χ` and a Hermitian `H`. Then `e = K1`.
  - Amplitude sourcing: `((1 − A) + kK)ψ = k e`, with `φ = 1 − ψ` and `ψ = 0` on the wall.
  - `g = (1 − A)⁻¹` inside, with zero wall values.
  - Bodies at rest: `K = diag(m)`. No sign is imposed on `m`.
  - T1(b): a record at rest at `y` keeps the ledger `Λ = Σ eφ` iff its bare energy is `E' = Λ/(1 − kΛ g_yy)`. It is a positive record energy exactly when `0 < kΛ g_yy < 1`.
- **Block 162** (branch `physics-loop/admissibility-induced-law-block162-…-20260926`):
  - The window is `B_R(y)`: coordinate (sup-norm) distance at most `R` from `y`.
  - A rule of radius `R` reads the amplitude and the pre-event rates in the window.
  - The source `s = Kφ` is point-equivalent iff `s − Qδ_y = (1 − A)f` with `f` finitely supported. Block 162's T4(b) and T4(d) read this on `ℤ³`, through moments of discrete harmonic polynomials.
  - Block 162's cage uses signed rest energies, "as block 116's witness allows". Block 116's moving witness has `H_xx = μσ₃`, which has a negative eigenvalue.
- **Notation.**
  - For a held box `Ω`: `I` is its interior, and `∂` is the set of wall points adjacent to `I`. Edge and corner wall points are adjacent to nothing inside and play no role.
  - `G = g = (1 − A_I)⁻¹`, where `A_I` is `A` restricted to `I`.
  - "Window data" means `K` on `B_R(y)` together with `φ` (equivalently the rates `φ²`) on `B_R(y)`.

## (1) Exact statement attempted

Block 162 asks: for a source confined to the window that is not point-equivalent, can two held boxes give identical window data and different prices? The answer found here has five parts.

- **(A) Yes, for every `R ≥ 1`.**
  - Let the two boxes share the wall plane at distance `R + 1` from `y`.
  - Let `s = ε((1 − A)δ_{f₀})|_I`, with `f₀ = y − R e₁` the site next to that plane.
  - Then `s` is supported in `B_R(y)`, has `Q = ε/6`, and is not point-equivalent.
  - Its field is `ψ = kεδ_{f₀}` in every such box.
  - So the window data agree while `g_yy`, and with it the price `Q/(1 − kQ g_yy)`, differs.
  - This is exact for `R = 1`, `ε = 1`, `γ = 1` in the cubes of side 5 and 7, and proved for every `R`.
- **(B) Nested boxes.** Take `Ω₁ ⊂ Ω₂`, let `S` be the wall points they share, and let `c = H₁ᵀs` be the outer flux.
  - Identical window data hold iff `c` vanishes off `S`.
  - Then `Q = Σ_S c`.
  - Consequently, strict nesting (`S = ∅`) forces `s = (1 − A)(G₁s)`: a point-equivalent source with `Q = 0`.
  - A nonzero nonnegative source never gives identical window data in two different nested boxes.
- **(C) Finite exact chart,** for `R = 1`, cubes of side 5 and 7, and `y` at distance `≥ 2` from every wall. Among all 269 pairs with different `g_yy`:
  - a window-identical source with `Q ≠ 0` exists iff the two boxes share a wall plane at distance `R + 1 = 2` from `y`;
  - no pair has a nonzero nonnegative window-identical source.
- **(D) Far windows,** for `R = 1`, with `y` at distance `≥ 3` from every wall, in cubes of side 7, 9 and 11 (11628 pairs of distinct relative boxes). Identical window data give identical prices in every pair.
  - For each non-congruent pair, the only window-identical source is the trivial `(1 − A)δ_y`, which has `Q = 0`.
  - Every pair with a larger kernel is congruent under a symmetry fixing `y`, so its `g_yy` is equal.

## (2) Steps

### Step 1 — reduction (PROVED)

*Claim.* Take a window-confined amplitude, with `K` supported in `W × W`, `W = B_R(y)`, and a static solution in each box. Then the following hold.
- The window data coincide iff the two effective sources are the same `s` (supported in `W`) and `(G₁ − G₂)s = 0` on `W`.
- The prices are `E'_i = Q/(1 − kQ g_i(y,y))`, with `Q = Σ s`.
- When both are defined, `E'_1 = E'_2` iff `Q = 0` or `g_1(y,y) = g_2(y,y)`.

*Proof.*
- `Λ = eᵀφ = (K1)ᵀφ = 1ᵀKφ = Σ s = Q`, since `K` is symmetric.
- The law reads `(1 − A)ψ = k(e − Kψ) = kKφ = ks` inside, with `ψ = 0` on the wall. So `ψ_i = kG_is` in box `i`.
- Suppose the window data coincide. Then `s_1 = Kφ_1 = Kφ_2 = s_2` on `W`, and both sources vanish off `W`. Also `kG_1s = ψ_1 = ψ_2 = kG_2s` on `W`.
- Conversely, suppose `s` is given and `(G₁ − G₂)s = 0` on `W`. Let `φ = 1 − kG₁s` on `W`, with `φ > 0`, and take bodies at rest `m = s/φ` on `W`. Then `ψ_i = kG_is` solves law `i`, because `Kφ_i = Kφ = s`. It is the solution when the operator is nonsingular.
- Block 116 T1(b) gives `E'_i`. Finally, `Q/(1 − kQg₁) = Q/(1 − kQg₂)` with both denominators nonzero iff `Q = 0` or `g₁ = g₂`. ∎

### Step 2 — the construction for every R (PROVED; CHECKED for R = 1)

*Construction.*
- Fix `R ≥ 1` and `ε > 0`. Put `f₀ = y − Re₁` and `b₀ = y − (R + 1)e₁`.
- Let `Ω` be any held box whose interior contains `B_R(y)` and whose wall contains `b₀`. Then `b₀` lies on `Ω`'s low `x`-face.
- Define `s = ε[δ_{f₀} − (1/6)(δ_{f₀+e₁} + δ_{f₀±e₂} + δ_{f₀±e₃})]`. This is `ε(1 − A)δ_{f₀}` with the wall term at `b₀` dropped.

*Claims.*
- (a) `supp s ⊂ B_R(y)`. The coordinate offsets from `y` are at most `R` in `x`, and at most `1 ≤ R` in `y` and `z`.
- (b) `Q = ε(1 − 5/6) = ε/6`.
- (c) `G_Ω s = εδ_{f₀}` in every such box. Because `δ_{f₀}` vanishes on the wall, `(1 − A_I)δ_{f₀} = ((1 − A)δ_{f₀})|_I = s/ε`.
- (d) Take bodies at rest `m(f₀) = ε/(1 − kε)` and `m = −ε/6` at the five other sites. With `kε < 1`, `ψ = kεδ_{f₀}` solves the law, and `φ = 1 − kεδ_{f₀} > 0`.
- (e) Uniqueness holds whenever `kε/6 < λ_min(1 − A_I)`.
  - For symmetric matrices, `vᵀ(X + Y)v ≥ (λ_min X + λ_min Y)|v|²`, so `λ_min((1 − A_I) + kK) ≥ λ_min(1 − A_I) − kε/6`.
  - `λ_min(1 − A_I) = 1 − (1/3)Σ_i cos(π/(L_i + 1))`, where `L_i` is the interior length along axis `i`. The products `Π_i sin(πj_ix_i/(L_i + 1))`, `1 ≤ j_i ≤ L_i`, vanish on the wall, satisfy `A·v = (1/3)Σ cos(πj_i/(L_i + 1))·v`, and there are `|I|` of them, independent. So they form an eigenbasis.
  - The same condition gives a positive record energy. `kQ g_yy ≤ kε/(6λ_min) < 1`, since `g_yy ≤ λ_max(g) = 1/λ_min(1 − A_I)`, and `Q > 0`.
- (f) The window data are the same in every such box: the rest energies `m`, and `φ = 1 − kεδ_{f₀}` on `W`.

*The pair for every R.* In coordinates relative to `y`:
- `Ω₁` is the cube `[−R−1, R+1]³` (side `2R + 3`, `y` at the centre);
- `Ω₂` is the cube `[−R−1, R+3] × [−R−2, R+2]²` (side `2R + 5`).

Both contain `b₀` on their low `x`-face and are nested (`Ω₁ ⊂ Ω₂`). Step 4 shows `g₂(y,y) > g₁(y,y)`, so the prices differ (Step 1, `Q ≠ 0`).

*CHECKED (X1–X6).* The instance `R = 1`, `ε = 1`, `γ = 1`, cubes of side 5 (`y = (2,2,2)`) and 7 (`y = (2,3,3)`), with exact rational elimination:
- the static solution is `ψ = kδ_{f₀}` in both boxes (every pivot nonzero, so it is unique);
- the window data agree exactly, and `Q = 1/6`;
- `g_yy = 22/17` against `34706593/25555530`;
- the prices are `102/601` against `306666360/1805291567`;
- the support and charge of the construction are checked for `R = 1, …, 5`.

### Step 3 — the source is not point-equivalent (PROVED; CHECKED X5)

- `P(x) = x₁ − y₁` is discrete harmonic on `ℤ³`: `AP = P`.
- For finitely supported `h`, `Σ P·(1 − A)h = Σ h·(1 − A)P = 0`. The swap is a finite sum, since `A` is symmetric on finitely supported functions.
- `Σ P(s − Qδ_y) = ε[−R + (R − 1)/6 + 4R/6] = −ε(R + 1)/6 ≠ 0`.
- So `s − Qδ_y ≠ (1 − A)f` for every finitely supported `f`. This is block 162's T4(d) test, using the linear harmonic polynomial.
- For `R = 1` the moment is `−1/3` (X5).

### Step 4 — Gram identity for nested boxes (PROVED; CHECKED G1–G3)

*Setting.* Let `Ω₁ ⊂ Ω₂` be held boxes, so `I₁ ⊂ I₂` and `∂₁ ⊂ I₂ ∪ ∂₂`. Let `S = ∂₁ ∩ ∂₂` and `T = ∂₁ \ S ⊂ I₂`.

*Harmonic measure.*
- Define `H₁(z, b) = (1/6)Σ_{x∈I₁, x∼b} g₁(z, x)` for `z ∈ I₁` and `b ∈ ∂₁`.
- For `v` on `∂₁`, `h = H₁v` is the unique function with `h = v` on `∂₁` and `(1 − A)h = 0` on `I₁`.
  - Proof: `(1 − A_{I₁})h = A_∂v`, where `(A_∂v)(x) = (1/6)Σ_{b∼x} v(b)`, so `h = g₁A_∂v = H₁v`.
  - Uniqueness follows from `λ_min(1 − A_{I₁}) > 0` (Step 2(e)).
- With `v ≡ 1`, every row of `H₁` sums to `1`.

*Lemma G.* On `I₁ × I₁`, `G₂ − G₁ = H₁ΓH₁ᵀ`, where `Γ(b, b') = g₂(b, b')` for `b, b' ∈ ∂₁`, and `g₂ = 0` whenever an argument lies on `∂₂`.

*Proof.*
- Fix `z ∈ I₁`. `F = g₂(·, z) − g₁(·, z)`, with `g₁ = 0` on `∂₁`, satisfies `(1 − A)F = δ_z − δ_z = 0` on `I₁`, and `F = g₂(·, z)` on `∂₁`. So `F = Σ_b H₁(·, b)g₂(b, z)`.
- For `b ∈ S`, `g₂(b, ·) = 0`.
- For `b ∈ T`, `g₂(b, ·)` is harmonic on `I₁`, because `b ∉ I₁`. So `g₂(b, z) = Σ_{b'} H₁(z, b')g₂(b, b')`.
- `g₂` is symmetric. Combining gives the identity. ∎

*Positivity.*
- `Γ_T` (on `T × T`) is a principal submatrix of `g₂ = (1 − A_{I₂})⁻¹`, which is positive definite. So `Γ_T` is positive definite.
- `g₁ > 0` entrywise: `g₁ = Σ_m A_{I₁}^m`, and `I₁` is connected. Hence `H₁(z, b) > 0` for every `z ∈ I₁` and `b ∈ ∂₁`.
- Corollary: `g₂(y,y) − g₁(y,y) = H₁(y,·)_Tᵀ Γ_T H₁(y,·)_T > 0` whenever `T ≠ ∅`. This is the strict inequality used in Step 2. It re-proves, by a different route, block 162 T2's growth of `g_yy` with the box.

*CHECKED.*
- G1: the identity holds exactly for side 5 inside side 7 (a shared face, 9 shared wall points) and for side 5 centred inside side 9 (strict nesting).
- G2: for the Step 2 source, `c = H₁ᵀs = (1/6)δ_{b₀}`, and `(G₂ − G₁)s = 0` on all of `I₁`.
- G3: `Γ` is positive definite in the strict pair, by exact elimination with every pivot positive.

### Step 5 — the nested theorem (PROVED)

Let `Ω₁ ⊂ Ω₂`, let `s` be supported in `W ⊂ I₁`, let `c = H₁ᵀs` (a function on `∂₁`), and let `u₁ = G₁s`.

- **(a) Identical window data iff the flux stays on shared walls.** `(G₂ − G₁)s = 0` on `W` ⇔ `c|_T = 0` ⇔ `(G₂ − G₁)s = 0` on all of `I₁`.
  - (⇒) Because `supp s ⊂ W`, `0 = sᵀ(G₂ − G₁)s = cᵀΓc = c_Tᵀ Γ_T c_T`. `Γ` vanishes on `S`, and `Γ_T` is positive definite, so `c_T = 0`.
  - (⇐) `(G₂ − G₁)s = H₁Γ_{·T}c_T = 0`.
- **(b) The charge sits on shared walls.** `Q = Σ_{b∈S} c(b)`, because `Σ_b c(b) = Σ_z s(z)Σ_b H₁(z, b) = Σ s`.
- **(c) The flux as the outer derivative.** `c(b) = (1/6)Σ_{x∈I₁, x∼b} u₁(x)`. Extending `u₁` by zero, `(1 − A)u₁ = s − c` on `ℤ³`: inside `I₁` it is `s`, at `b ∈ ∂₁` it is `−c(b)`, and elsewhere it is `0`.
- **Corollary 1 (strict nesting, `S = ∅`).** Identical window data force `c = 0`. Then `s = (1 − A)u₁` with `u₁` finitely supported: point-equivalent with `Q = 0` and `f = u₁`, and both prices are `0`. A window-confined source that is not point-equivalent never gives identical window data in strictly nested boxes.
- **Corollary 2 (nonnegative sources).** Suppose `s ≥ 0`, `s ≠ 0`, and `Ω₁ ≠ Ω₂`.
  - Then `u₁ > 0` on `I₁`, so `c > 0` on all of `∂₁`.
  - `T ≠ ∅`. If every face point of `Ω₁` lay on `∂₂`, each face of `Ω₁` would lie in the corresponding face plane of `Ω₂`, giving `Ω₁ = Ω₂`.
  - So by (a), the window data never coincide.
- **Corollary 3.** Every nested coincidence with `Q ≠ 0` has its outer flux on shared wall points. The Step 2 source is the case `c = (ε/6)δ_{b₀}`.

### Step 6 — finite chart near the walls (CHECKED C1, P1)

*Scope.* `R = 1`, `y` at distance `≥ 2` from every wall, cubes of side 5 and 7 (28 placements, exact window blocks of `G`). All 269 pairs of distinct relative boxes with different `g_yy`, nested and non-nested.

- **C1.** An exact kernel vector of `(G₁ − G₂)_W` with `Q ≠ 0` exists in exactly the 146 pairs that share a wall plane at distance 2 from `y`. It exists in none of the other 123.
- **P1.** Each pair has an exact rational `z > 0` with `z ⊥ ker(G₁ − G₂)_W`. For `s ≥ 0` in the kernel, `0 = zᵀs` forces `s = 0`. So nonnegative window sources never coincide, in the non-nested pairs as well.

### Step 7 — far windows (CHECKED F1, F2)

*Scope.* `R = 1`, `y` at distance `≥ 3` from every wall, cubes of side 7, 9 and 11 (153 placements, 11628 pairs of distinct relative boxes). The window blocks of `G = 6M⁻¹`, with `M = 6(1 − A)` an integer matrix, are computed modulo the prime `p = 2147483629`. `M` is invertible mod `p`, so these blocks are the reductions of the rational blocks.

- **F1.**
  - `dim ker_ℚ D ≤ dim ker_p D`, for `D = (G₁ − G₂)_W`.
  - `t = (1 − A)δ_y` is always in `ker_ℚ D`, because `G_it = δ_y` when all neighbours of `y` are interior.
  - 10785 pairs have `dim ker_p = 1`. There the only window-identical sources are the multiples of `t`: point-equivalent, `Q = 0`, price `0` in both boxes.
  - The other 843 pairs all have equal `g_yy` mod `p`.
- **F2.** Every pair with equal `g_yy` mod `p` is congruent by a reflection or permutation fixing `y`, so `g_yy` is equal exactly. Pairs with unequal residues have unequal rationals.
- **Conclusion.** In every one of the 11628 pairs, identical window data give identical prices.

## (3) Where it stops

The HIT is Step 2 with Steps 1 and 3: an exact counterexample for every `R`. The remaining items are the limits of the positive side.

- **Non-nested pairs in general.**
  - Lemma G applies to each box against the intersection box `Ω₀ = Ω₁ ∩ Ω₂`, whose interior contains `W`. It gives `G₁ − G₂ = H₀(Γ₁ − Γ₂)H₀ᵀ` on `I₀`, by the same proof.
  - But `Γ₁ − Γ₂` is indefinite, so Step 5's argument stops at the first step: `sᵀ(G₁ − G₂)s = 0` no longer forces `c₀` onto a subset.
  - For non-nested pairs there is only the finite chart (Step 6).
- **The far regime** (Step 7) is a finite survey for `R = 1`, not a theorem.
- **Nonnegative sources** in non-nested boxes are covered only by the chart (Step 6).
- **Not treated:** crowds of records, and the delayed law (block 57).

## (4) What would finish it

- **(i) Characterisation.** Prove, for every `R` and every pair of held boxes, that a window-identical source with `Q ≠ 0` exists iff the boxes share a wall plane at distance `R + 1` from `y`. This is C1's pattern.
  - The route is Step 5(c) with a Cauchy-continuation argument on the faces of `Ω₀` that are not shared. On such a face, `c = 0` and `u = 0` determine `u` layer by layer. The function then vanishes outside the "shadow" of `W` on the shared faces.
  - The non-nested case needs a replacement for the positivity of `Γ_T`.
- **(ii) Nonnegative sources in general.** Prove Corollary 2 for non-nested pairs, for example through (i), or through a sign argument on `Γ₁ − Γ₂` restricted to the flux of a positive source.
- **(iii) The far statement in general.** For `W` at distance `≥ R + 2` from every wall of both boxes, show that identical window data force point-equivalence, or congruence of the two boxes.

## ASSUMED

Nothing outside the notes is used without proof. The facts used are re-proved at the scope used:
- Rayleigh-quotient eigenvalue bounds (Step 2(e));
- the sine eigenbasis (Step 2(e));
- summation by parts against a harmonic polynomial (Step 3);
- positivity of the Green's function on a connected interior (Step 4).

The modular-rank inequality is the elementary fact that a minor nonzero mod `p` is nonzero over `ℚ`.

## Reproduce

```bash
python3 probes/work/derive/confined-sources-and-the-formation-price/w-jonathonsmac4f50-jb978/check.py
```

The run takes about 3 minutes. `--skip-F` omits the far survey, which takes about 140 s.
