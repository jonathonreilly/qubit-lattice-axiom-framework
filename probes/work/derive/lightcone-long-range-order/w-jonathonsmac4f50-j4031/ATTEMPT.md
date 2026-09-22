# lightcone-long-range-order, attempt 1 of 5 (round 2): the slab halves are what make the layer swap reflection positive

Worker `w-jonathonsmac4f50-j4031` (`claude-opus-5-5`), unit `J-derive-lightcone-long-range-order:a1`.

**Provenance, in order.**
1. **My own plan, before reading the priors.** Route (i) with the layer swap as the reflection. I first took the two *layers* as its
   halves, and found that choice is not reflection positive (step 5).
2. **Then I read the priors.** Attempt a5 (`w-jonathonsmac4f50-ja59c`) and `w-macbookpro90c72-j451b` both use a different pair of
   halves. Their slabs `{(x, a) : a = parity(x)}` turn `Γ` into the ordinary bilayer torus.
3. **Consequence.** The route below is theirs. What I add:
   - an exact re-check with my own code;
   - the threshold constants by a method different from a3's;
   - the no-go for the layer halves, which is new and explains why the slab halves are necessary.

All of these workers, and a3 and a4, are the same model family as me (Claude). A referee from another family is needed.

## 1. What is claimed

**Setting (GIVEN, round 1).**
- `Γ_L` has vertices `(x, a)`, with `x ∈ (Z/L)³` and `a ∈ {0, 1}`. Its edges are `(x,0)–(y,1)` with `y − x ∈ N7 = {0, ±e_j}`.
- `μ_L` is the sphere Heisenberg ferromagnet on `Γ_L`, and `π_L` is its layer-0 marginal, the light-cone formation law's
  stationary law.
- Write `m₀ = (1/N)Σ_x s_{(x,0)}`, `E(k) = 6 − 2Σcos k_j`, `G_L = (1/N)Σ_{k≠0} 1/E(k)` and `H_L = (1/N)Σ_k 1/(E(k) + 2)`.

> **Claim.** For every even `L` and every `β > 0`:
>
> `⟨|m₀|²⟩_{π_L} ≥ 1 − (3/(2β))(G_L + H_L)`.
>
> Hence `π` has long-range order for `β > β₀ = (3/2)(I₀ + I₂) = 0.590494` (on all sufficiently large even tori), where
> `I₀ = ∫d³k/(2π)³ 1/E = W/6` and `I₂ = ∫ 1/(E+2) = 0.1409314881127…`.
>
> **No-go (new, exact).** Take the swap `(x, a) ↦ (x, 1 − a)` with the two layers as halves. It is **not** reflection positive
> for any `β > 0`. The same swap with the slab halves is.

## 2. The steps

1. **CHECKED, exact (E1): the relabelling.** `f(x, a) = (x, a ⊕ parity(x))` maps `Γ_L` isomorphically onto the bilayer torus: two
   copies of `(Z/L)³` with their nearest-neighbour edges, and one rung `(x,0)–(x,1)` per site.
   - The stencil's self-edge `(x,0)–(x,1)` joins equal parities, so it becomes a rung.
   - A shifted edge `(x,0)–(x±e_j,1)` joins opposite parities, so both ends land in the same slab.
   - Checked edge by edge for `L = 4` (448 edges) and `L = 6` (1512).
2. **PROVED + CHECKED (E2): the spectrum.** The bilayer Laplacian is (slab Laplacian) ⊗ 1 + 1 ⊗ (rung Laplacian), with eigenvalues
   `E(k)` and `E(k) + 2`. Since `E(k + (π,π,π)) = 12 − E(k)` (symbolic), this is the given `{E, 14 − E}`.
3. **PROVED + CHECKED (E3): reflection positivity and Gaussian domination.**
   - *The family.* Bond planes in each spatial direction (acting on both slabs) and the plane between the slabs.
   - *Mirror pairs.* Each reflection swaps its halves with no fixed vertex, and each crossing edge is a mirror pair `{u, θu}`
     (checked on `L = 4`). So the crossing factor `Π e^{β s_u·s_{θu}}` expands with nonnegative coefficients in products
     `g(s_u)ḡ(s_{θu})`, and `E[F·θF] ≥ 0`.
   - *Coverage.* Every edge crosses some reflection of the family (checked).
   - *Domination.* Block 19's G2 argument (maximiser with the most zero-gradient edges) then gives `Z(h) ≤ Z(0)` for every
     gradient twist.
   - *Infrared bound.* On the two branches: `⟨|Ŝ^e_±(k)|²⟩ ≤ 1/(β λ_±(k))`, with `λ_+ = E`, `λ_− = E + 2`.
4. **PROVED + CHECKED (E4): the sum rule and the one-layer reduction.**
   - Summing over both branches, `Σ_{k,±,e}⟨|Ŝ^e_±(k)|²⟩ = 2N`. So `⟨|M|²⟩/(2N) ≥ 2N − (3N/β)(G_L + H_L)`, with `M = M₀ + M₁`.
   - The layer swap is an automorphism of `Γ` (`N7 = −N7`), so `⟨|m₀|²⟩ = ⟨|m₁|²⟩`. Together with `|a + b|² ≤ 2|a|² + 2|b|²`
     (symbolic), this gives `⟨|M/(2N)|²⟩ ≤ ⟨|m₀|²⟩`.
   - As `L → ∞`, `G_L → I₀` and `H_L → I₂`.
5. **PROVED + CHECKED (E5): the no-go for the layer halves.**
   - With the layers as halves every edge crosses, and the crossing factor is `exp(β⟨s₀, M s₁⟩)` with `M = I + A_nn`, the
     7-stencil matrix. Its eigenvalue at `k = (π,π,π)` is `1 − 6 = −5`.
   - For two configurations `s, s'` with `d = s − s'`, the 2×2 principal minor of the kernel is
     `e^{2β⟨s,Ms'⟩}(e^{β⟨d,Md⟩} − 1)`.
   - The staggered `d = 2(−1)^{|x|}e_z` on a 2×2×2 cube gives `⟨d, Md⟩ = 32 − 96 = −64` (exact), so the minor is negative for every
     `β > 0`. Test functions concentrating near `s` and `s'` then make `E[F·θF] < 0`.
6. **NUMERIC (N1): the constants.**
   - `I₀` and `I₂` come from quadrature of `∫₀^∞ e^{−(6 or 8)t} I_0(2t)³ dt` at 30 digits.
   - `I₀` agrees with `W/6`, where `W = √6/(32π³)Γ(1/24)Γ(5/24)Γ(7/24)Γ(11/24)`, to `3·10⁻¹⁹`.
   - `I₂ = 0.140931488112717092`, and `β₀ = 0.590493746957070142`, agreeing with a3.

## 3. Where this stops

- **Everything but the no-go is a re-derivation** of a5's result by the slab route of j451b. Its value is the independent code and
  the independent constant, not a new idea.
- **The threshold `0.5905` is the Gaussian-domination constant**, which is not sharp. The executed `|m| = 0.76` at `β = 1` is far
  above the bound, `⟨|m₀|²⟩ ≥ 0.337` at `L = 100` (a5's table).
- **Only the sphere menu is treated**, as the unit asks.

## 4. What would finish it

1. A referee from another family on the slab relabelling and the reflection family. That is the whole proof; the rest is block 19.
2. A sharper threshold, if wanted. For example, bound the antisymmetric branch (gap 2) through the rung energy instead of its
   infrared bound.

## 5. Running it

```
python3 probes/work/derive/lightcone-long-range-order/w-jonathonsmac4f50-j4031/check.py
```

It uses sympy and mpmath, has 6 checks, and runs in about a second. E1–E5 are exact; N1 is labelled `NUMERIC`.
