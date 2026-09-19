# static-formation-singularity: derivation attempt 3 of 3

Worker `w-jonathonsmac4f50-ja5a1` (claude-opus-5), unit `J-derive-static-formation-singularity-a3`.

**Sources and provenance**
- **The objects** are the six-axis rule and the formation laws of blocks 05, 08, 09, 14 and 16 (PRs #8149, #8138, #8139, #8148, #8150), restated in `check.py`'s docstring:
  - `K(s,t) = p, q, r` for equal, antipodal and orthogonal values, at `(3,1,2)`;
  - the static law on a window: `∏_edges K / Z`;
  - a formation law in an order: each site is drawn given its earlier neighbours with probability `∏K(s,u_i)/N(u)`.
- **Monotone order:** the earlier neighbours of `x` are its predecessors `x − e_j`. By block 05 every monotone order gives the same law.
- **The GIVEN** is round 1's `static-law-in-the-hull`: `a1` is by claude-opus-5, my model family, and was refereed by grok and claude-opus-5.
- I use its quantities `Z`, `D_σ`, `N_k` and the separator `1[constant]`, and recompute each of them.

## 1. Statements

**(a) m disjoint plaquettes.** Let `W_m` be a window that is a disjoint union of `m` plaquettes (4-cycles). Let `ν` be any law in the convex hull of adapted formation laws on `W_m`, where the order may depend on the values already formed. Then

`TV(static_{W_m}, ν) ≥ max(81/3464 − 9/416, 1 − A^m − B^m)`,

- `A = (26/25)^{−9/400} (1 + (1/25)(9/416))`;
- `B = (24/25)^{−9/400} (1 − (1/25)(81/3464))`;
- `A, B < 1` exactly, with `A ≈ e^{−1.75·10⁻⁵}` and `B ≈ e^{−1.73·10⁻⁵}`.

The bound tends to 1 and exceeds `1/2` from `m = 80237`.

**(b) Relative entropy and singularity on Z² and Z³.** Take the six-axis rule at `(3,1,2)`, let `μ` be any static Gibbs measure and `ν` any monotone-order formation law in infinite volume, i.e. any space-time law of the level automaton. With `Λ_n` the cube of side `n`:
- **Z²:** `liminf_n |Λ_n|^{−1} H(μ_{Λ_n} | ν_{Λ_n}) ≥ c₂/3`, with `c₂ = 19/4604256`. Numerically `c₂/3 ≈ 1.38·10⁻⁶`.
- **Z³:** the same quantity is `≥ c₃/4`, with `c₃ = (1/986)²·(4/28561)`. Numerically `c₃/4 ≈ 3.6·10⁻¹¹`.
- **In both:** `μ ⊥ ν`.

**(c) The observable.**
- **The 2×2 window.** `μ/ν = 864 N(σ₁₀, σ₀₁)/20784`, where `N` is 26, 24 or 22 as the anti-diagonal pair is equal, orthogonal or antipodal. So the total-variation-optimal event is `{σ₁₀ = σ₀₁}`, the two predecessors of the last site being equal.
  - `TV = 455/31176 = μ(σ₁₀ = σ₀₁) − ν(σ₁₀ = σ₀₁) = 169/866 − 13/72`.
  - That is 8.3 times the difference in the plaquette four-point indicator (all four equal), `81/3464` against `9/416`.
  - The expected number of equal nearest-neighbour pairs is `1.01155` against exactly 1.
- **The 2×2×2 window.**
  - `μ/ν = 10368 Q/Z`, with `Q` the product of the normalisers of the four sites that have at least two predecessors, and `Z = 6982520832`.
  - `TV = 1182193085/23402354976 ≈ 0.0505`.
  - Constant indicator: `0.000457` against `0.000292`.
  - Equality of one face-diagonal pair: `0.1975` against `0.1806`.
- **Answer.** The most discriminating local observables are the two-point functions of the pairs that share a common successor: the anti-diagonal in 2D and the face-diagonals in 3D. These are exactly where the formation law's extra normaliser terms live. The four-point function is weaker.

## 2. Steps

**S1 (PROVED; CHECKED `A1`). The plaquette constants.**
- Static: `P(constant) = 6p⁴/Z = 81/3464`, with `Z = 20784`.
- Fixed order `o`: `P_o(constant) = 6p⁴/D_o`, with `D_o = ∏N_{k_x}`, `N₀ = 6` and `N_k = p^k + q^k + 4r^k`. Over the 24 orders `D_o ∈ {22464, 24336}`, so `π_f = 6p⁴/22464 = 9/416`.

**S2 (PROVED). Adaptive orders cannot raise a single plaquette's constancy.**
- Given the first value `a`, the probability of ending constant is the product along the all-`a` path of `p^{k}/N_k`, where `k` counts the formed neighbours.
- On that path the history is determined, so an adaptive rule is a mixture of fixed orders there. Hence `P(constant) ≤ π_f`.
- For `θ ≥ 1` this gives `E[θ^{f}] = 1 + (θ − 1)P(f = 1) ≤ 1 + (θ − 1)π_f`.

**S3 (PROVED). A dynamic-programming product lemma.**
- On `W_m` let `V(S)` be the supremum over adaptive continuations of `E[∏_i θ^{f_i}]` from a partial state `S`, with `f_i = 1[plaquette i constant]` and `θ ≥ 1`. Then `V(S) = ∏_i V_i(S_i)`, where `V_i` is the single-plaquette supremum.
- **Proof.** Induction on the number of unformed sites. Suppose the next site is in plaquette `j`. Its draw depends only on plaquette `j`'s formed sites. So `E[V(S')] = ∏_{i≠j} V_i(S_i) · E[V_j(S'_j)] ≤ ∏_i V_i(S_i)`, and a policy attaining `V_j` attains equality.
- Hence every adapted law, and every mixture of them, has `E_ν[θ^C] ≤ (1 + (θ − 1)π_f)^m`, where `C` is the number of constant plaquettes.
- The static law on `W_m` is a product, so `C ~ Bin(m, π_s)`.

**S4 (PROVED; CHECKED `A1`). The Chernoff bounds.**
- Set `τ = 9/400`, `θ = 26/25` and `θ' = 24/25`.
- By Markov's inequality:
  - `ν(C ≥ mτ) ≤ [θ^{−τ}(1 + (θ−1)π_f)]^m = A^m`;
  - `μ(C < mτ) ≤ [θ'^{−τ}(1 − (1−θ')π_s)]^m = B^m`.
- `A^{400} < 1` and `B^{400} < 1` are checked in exact rational arithmetic.
- So `TV ≥ μ(C ≥ mτ) − ν(C ≥ mτ) ≥ 1 − A^m − B^m`.
- For `m = 1`, `TV ≥ π_s − π_f` directly.

**S5 (PROVED; CHECKED `B1`, `B2`). Markov structures.**
- `μ` is nearest-neighbour Markov: for finite `B`, `μ(σ_B | σ_{B^c}) = γ_B(σ_B | σ_{∂B})` with `γ ∝ ∏K`.
- `ν` is the space-time law of a positive-rate automaton. By Bayes, its conditional of a finite set `I` given everything else is the normalised product of the kernels that involve `I`.
- The kernel of `x` involves `{x} ∪ pred(x)`. So when the sites of `I` are pairwise non-adjacent in `NN ∪ {pairs of predecessors of a common site}`, both conditionals factorise over `I`:
  - in 2D those pairs are the anti-diagonals, `e₁ − e₂`;
  - in 3D they are the face-diagonals, `e_i − e_j`.
- **The single-site formation conditional** is `ν(s|b) ∝ ∏_{NN} K(s,·) · g(s)`:
  - 2D: `g(s) = 1/(N(s,b₅)N(s,b₆))` over the two anti-diagonal neighbours. The factorisation is checked;
  - 3D: `g(s) = ∏_j 1/N(s,a_j,b_j)` over the six face-diagonal neighbours.

**S6 (PROVED). The chain rule.**
- For a box `Λ` and the interior part `I` of a colour class (`(x₁ − x₂) mod 3` in 2D, `(x₁ + 2x₂ + 3x₃) mod 4` in 3D, both independent in the union graph):

  `H(μ_Λ | ν_Λ) = H(μ_{Λ∖I} | ν_{Λ∖I}) + E_μ[H(μ_{I|Λ∖I} | ν_{I|Λ∖I})] ≥ Σ_{y∈I} E_μ[D(γ_y(·|∂y) ‖ ν_y(·|∂'y))]`.
- This uses S5: the conditionals given `Λ∖I` equal the specifications, because the neighbourhoods lie in `Λ∖I`.
- The single-site divergence is `D = log E_γ g − E_γ log g`, and `D ≥ Var_γ(g)/(2 g_max²)` because `(−log)'' ≥ 1/g_max²` on `[g_min, g_max]`.

**S7 (CHECKED `B1`). Z².** The exact minimum of `Var_γ(g)/(2g_max²)` over all `6⁶` boundaries is `c₂ = 19/4604256 > 0`. With density `1/3` this gives `h ≥ c₂/3`.

**S8 (CHECKED `B2`). Z³.**
- `g` is constant on exactly 600 face-diagonal boundaries: 216 in which all three pairs are antipodal and 384 in which all three are orthogonal. So no uniform single-site bound exists.
- None of the 600 has `a₁ = b₁`, where `a₁ = σ_{y+e₁−e₂}` and `b₁ = σ_{y+e₁−e₃}`.
- On `{a₁ = b₁}`: `D ≥ γ_min (g_max − g_min)²/(4g_max²) ≥ (1/986)·(4/28561)`, using `Var ≥ γ_min(g_max − g_min)²/2`.
- **Finite energy.** `μ(a₁ = b₁) ≥ min γ = 1/986`: condition on everything but `y + e₁ − e₂`, whose nearest neighbours exclude `y + e₁ − e₃`.
- So `E_μ D_y ≥ c₃`, and with density `1/4`, `h ≥ c₃/4`.
- **Blocks.** For a block `{y, y + e₁ − e₂}` with `y ∈ 4Z³`:
  - The chain rule gives `D_block ≥ E_{σ_u∼μ(·|rest)} D_y ≥ (1/986)·min_{a₁=b₁} D_y ≥ c₃`, uniformly in the rest.
  - This holds because `u` and `y` are not nearest neighbours, so under `μ` they are conditionally independent given the rest.

**S9 (PROVED). Mutual singularity without an outside theorem.**
- Let `S_n = Σ_{y∈I_n} log(γ_y/ν_y)(σ_y | ·)`, summing over sites in 2D and over blocks in 3D.
- Given `σ_{Λ_n∖I_n}`, the terms are independent under both `μ` and `ν`, and bounded by some `L`. Their conditional means are:
  - under `μ`, at least `c`, where `c = c₂` in 2D and `c = c₃` in 3D;
  - under `ν`, at most `0`.
- **Chebyshev.** `μ(S_n ≤ |I_n|c/2) ≤ 4L²/(|I_n| c²)`, and the same bound holds for `ν(S_n ≥ |I_n|c/2)`.
- **Borel–Cantelli.** Since `Σ_n 1/|I_n| < ∞` for `d ≥ 2`, the event "eventually `S_n > |I_n|c/2`" has `μ`-probability 1 and `ν`-probability 0.

**S10 (CHECKED `C1`, `C2`). The window observables.** The ratio identities, the exact TVs and the tabulated values.

## 3. Where the route stops

Nothing in (a)–(c) is left open. Two limits of scope:
- **The constants are far from sharp.**
  - (a): the rate `1.7·10⁻⁵` per plaquette comes from the small gap `π_s − π_f`.
  - (b): the constants come from worst-case boundaries (2D) and finite-energy factors (3D).
- **(a) covers disjoint cycles only.** For connected windows the static marginals do not factorise.

## 4. What would sharpen it

- For (a): count many disjoint anti-diagonal pairs instead of plaquettes. By C1 they carry the likelihood ratio, and the DP lemma extends to any statistic that a single plaquette's order controls.
- For (b): use `μ`'s actual boundary distribution in place of the worst case. The Z³ bound is set by the 600 symmetric boundaries.
