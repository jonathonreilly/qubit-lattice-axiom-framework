# lightcone-long-range-order — attempt a4 (route (ii))

Worker `w-jonathonsmac4f50-j539b` (model claude-opus-5). Check script: `check.py` in this directory. The graph and form identities are
exact; the energy threshold is evaluated with explicit margins; there is one numerical cross-check, labelled; it runs in under 1 s.

**Disclosure.** Attempt a5 of this problem, printed at claim time, is by the same model family. It closes the gap by route (i): the
layer swap with halves `A | B` is a reflection whose crossing edges are the vertical edges. This attempt deliberately takes the task's
route (ii) and does not use that reflection. What it adds is a second, independent argument for long-range order at large `β`, and a
precise account of what route (ii) needs.

## 1. The statement attempted

**Objects (GIVEN).** These are as in the task:

- `Γ_L` (`L` even): two copies of `(Z/L)³` with edges `(x,0)–(y,1)` for `y − x ∈ N7`;
- `μ_L`: the sphere (`n = 3`) Heisenberg ferromagnet on `Γ_L`;
- `π_L`: the layer-0 marginal of `μ_L`, the stationary law of the light-cone formation law;
- `A, B`: the classes of the bipartition (layer × spatial parity);
- `σ_x = s_{(x,0)} + s_{(x,1)}`;
- `m₀ = (1/N) Σ_x s_{(x,0)}`, with `N = L³`.

**Claim.** For every even `L` and every `β > 0`,

`⟨|m₀|²⟩_{π_L} ≥ ¼ [2 + 2 e_v − (6/β) G_L]`.

Here `G_L = (1/N) Σ_{k≠0} 1/E(k)`, and `e_v = ⟨s_{(x,0)}·s_{(x,1)}⟩ ≥ 7e − 6`. The average edge correlation satisfies
`e ≥ max_δ [cos 2δ + (2/(7β)) log((1 − cos δ)/2)]`.

With `G_L ≤ I₀ + (3/(4L)) S₂(L/2) + π²/(16L)` and `I₀ ≤ 0.255485`, the right side is positive for every `β ≥ 7` in infinite volume,
and at `β = 10` on tori of side 24, 48, 100. **Threshold proved: long-range order of `π` for `β ≥ 7` on large tori.** This is about ten
times attempt a5's `0.593`, by a route that does not use the rung reflection.

## 2. Steps

**S1 (GIVEN; refereed).** The reflections `θ_P` (a bond plane composed with the layer swap) are reflection-positive for `μ_L`. Their
crossing edges are exactly `{u, θ_P u}`, and they map `A` onto `A`. This is round 1's step 6, which the round-1 referee report on
`lightcone-formation:a2` says holds.

**S2 (PROVED; CHECKED G1).** Gaussian domination on the layer-symmetric class `𝓢 = {h : h(x,0) = h(x,1) for all x}`.

- *The reflection inequality.* For `θ_P` and any `h`, `Z(h)² ≤ Z(h⁺) Z(h⁻)`, where `h⁺` is `h` on one half and `h∘θ_P` on the other.
  The proof is the Taylor expansion of the crossing factors and Cauchy–Schwarz, as in a5's S5(a).
- *The class is closed.* If `h ∈ 𝓢`, then `h^± ∈ 𝓢` (CHECKED G1: every plane and direction, `L = 4, 6`).
- *The maximizer.* Take the supremum of `Z` over `𝓢` with `h(u₀) = 0`; it is attained by the same coercivity as a5's S5(b). Among the
  maximizers in `𝓢` choose one with the fewest nonzero-gradient edges. The counting argument (a5's S5(c)) runs inside `𝓢`: every
  crossing edge of every `θ_P` has zero gradient. These are all the non-vertical edges.
- *Constancy.* So the field is constant on `A` and on `B`. Since `(x,0)` and `(x,1)` lie in different classes (CHECKED G1), layer
  symmetry forces the two constants to agree. The field is constant and `Z(h) ≤ Z(0)` on `𝓢`.

**S3 (PROVED; CHECKED Q1).** For `h ∈ 𝓢` with value `h(x)` at `x`:

- `Σ_{edges} (s_u − s_v)·(h_u − h_v) = (h, −Δσ)`;
- `Σ_{edges} |h_u − h_v|² = 2(h, −Δh)`, where `−Δ` is the `Z³` Laplacian with symbol `E(k)`. The self-edges contribute nothing, and
  each nearest-neighbour pair occurs twice, once from each layer.

Expanding `Z(εh) ≤ Z(0)` to order `ε²` (the first order vanishes by rotation invariance) gives `⟨(σ^α, −Δφ)²⟩ ≤ (2/β)(φ, −Δφ)`. By real
and imaginary parts, `⟨|σ̂^α(k)|²⟩ ≤ 2N/(βE(k))` for `k ≠ 0`, and summing `α = 1, 2, 3` gives `⟨|σ̂(k)|²⟩ ≤ 6N/(βE(k))`.

*CHECKED:* both identities exactly on 10 random integer configurations of `Γ₄`.

**S4 (PROVED) The energy bound.** Let the a priori measure `μ₀` be the product of normalized uniform laws on `S²`, so `Z(0) = 1`.
Write `F(β) = log Z(β)` with `Z(β) = ∫ exp(β Σ_{edges} s_u·s_v) dμ₀`.

- *Convexity.* `F` is convex (`F'' = Var ≥ 0`) with `F(0) = 0`, so `F(β) ≤ β F'(β) = β ⟨Σ s_u·s_v⟩_β`.
- *A cap configuration.* Let `C_δ` be the cap of half-angle `δ` around a fixed direction. On `C_δ^V` every edge has `s_u·s_v ≥ cos 2δ`,
  and `μ₀(C_δ) = (1 − cos δ)/2`. So `F(β) ≥ |V| log((1 − cos δ)/2) + β|E| cos 2δ`.
- *Result.* With `|V| = 2N` and `|E| = 7N`: `e = ⟨Σ s·s⟩/|E| ≥ cos 2δ + (2/(7β)) log((1 − cos δ)/2)` for every `δ ∈ (0, π/2]`.

*CHECKED (E1):* the cap area, and the convexity inequality on the Ising analogue of `Γ` in one dimension (numerical, 40 digits).

**S5 (PROVED).** By translation invariance each of the seven edge types has a single correlation. The vertical type is `e_v`, and each
of the six others is at most 1. So `7e ≤ e_v + 6`, i.e. `e_v ≥ 7e − 6`.

**S6 (PROVED).**

- *Sum rule.* By Parseval for `σ`, `Σ_k |σ̂(k)|² = N Σ_x |σ_x|²`. So `⟨|σ̂(0)|²⟩ ≥ N² ⟨|σ_x|²⟩ − (6N/β) Σ_{k≠0} 1/E(k)`.
- *Exchangeability.* `σ̂(0) = M₀ + M₁`, and the layer swap is an automorphism (plain symmetry; no reflection positivity is used here). So
  `⟨|M₀ + M₁|²⟩ ≤ 4⟨|M₀|²⟩`, and `⟨|m₀|²⟩_{π_L} ≥ ¼ [⟨|σ_x|²⟩ − (6/β) G_L]`.
- *The vertical correlation.* `⟨|σ_x|²⟩ = 2 + 2e_v`.

**S7 (CHECKED E1) The threshold.**

- *`G_L`.* `G_L ≤ I₀ + (3/(4L)) S₂(L/2) + π²/(16L)` (a5's S8: monotone cells for interior points, the planes and axes bounded directly).
- *`I₀`.* `I₀ ≤ 0.255485`, from 800 exact terms of the cubic-walk return series and a5's rigorous Bessel tail. The return counts come
  from the recurrence, checked against the closed form for `n ≤ 20`.
- *Evaluation.* Maximizing over a grid of `δ`, with a margin of `10⁻⁹`, the bound is:

| `β` | 6 | 7 | 8 | 10 | 20 |
|---|---|---|---|---|---|
| bound on `⟨|m₀|²⟩` (infinite volume) | −0.0835 | 0.0491 | 0.1512 | 0.2986 | 0.6145 |

At `β = 10` on tori it is `0.2796` (`L = 24`), `0.2867` (`L = 48`) and `0.2916` (`L = 100`). The first positive value on the grid of
halves is at `β = 7`.

## 3. Route (ii) as posed, and route (iii)

- **Route (ii) alone does not close.** The layer-symmetric infrared bound together with the exchangeability of the layers leaves the
  sum rule open by the term `2 + 2e_v`, the vertical-edge correlation. Nothing in the symmetric sector bounds it: the self-edges carry
  zero gradient for every `h ∈ 𝓢`.
- **The missing input.** A lower bound on `e_v`. S4–S5 supply it from the energy alone. The cost is a threshold near `7` instead of a5's
  `0.593`. At large `β`, `e_v ≥ 1 − (2/β)(1 + log 28β) + …` (δ² ≈ 1/(7β)), so the bound tends to `1` like `1 − O(log β/β)`.
- **Route (iii).** Not attempted.

## 4. What would sharpen it

- A better vertical correlation bound, e.g. from the conditional law of `s_{(x,1)}` given layer 0 (a von Mises–Fisher law with mean
  direction along `S_x`), would lower the threshold.
- The rung reflection of a5 gives the sharp infrared route.
- The two routes agree on the conclusion (order at large `β`), which is the point of this attempt.
