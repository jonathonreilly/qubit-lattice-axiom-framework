# Referee: neutral moving-records law at large beta, attempt 1

Attempt `w-macbookpro9927a-ja869` (Claude). The kernel, the occupation bound, the cube census and the Peierls arithmetic are rebuilt here. The attempt's script is not imported.

The question in the task is whether the vacancy law orders at `c = c₀(β)`. Block 126 as landed (T4, open item N1.3) leaves that open and uses `M_L² = ⟨(N⁻¹ Σ_x σ_x)²⟩` as the torus diagnostic. The attempt answers a stated partial of that question for the two-valued menu, not an infrared bound and not the sphere.

## Verdicts

**Step 1 (neutral kernel) — holds.** At `c = 1/cosh β`, `c e^{±β} = 1 ± tanh β`, so `B = 1 + t σσ'` with `σ ∈ {−1,0,1}` and `t = tanh β`. Averaging the other end over `{±1}` returns weight 1, the empty weight. Also `1 − tanh β = 2/(e^{2β}+1)`.

**Step 2 (reflection positivity) — holds.** No nearest-neighbour bond crosses from one open half to the other. Bonds and sites in the fixed planes are split by positive square roots (`1 − t > 0`). For `F` supported on one half, `Z E[F θF]` is a sum of squares. On the 8-ring at `t = 1/3`, `z = 5/2`, the joint law of a mirror pair is symmetric and positive semidefinite.

**Step 3 (no order for `z < 1/320`) — holds.** Given the occupied set, a cluster flip leaves the neutral weight fixed, so `⟨σ_0 σ_x | O⟩ = 0` unless `0` and `x` are in the same cluster. Checked on two clusters: the cross term is 0 and the bonded pair has correlation `t`. For every neighbourhood, `S ≤ (1+t)⁶ + (1−t)⁶` coefficient-wise and the right-hand side is at most 64, so `P(occupied | rest) ≤ 64z`. Sequential sampling dominates the occupied set by Bernoulli(`64z`). Self-avoiding paths in `Z³` are at most `6·5^{n−1}`; the partial sum of order `N` equals `6p²(1−(5p)^N)/(1−5p)`, hence `Σ_x P(0↔x) ≤ p + 6p²/(1−5p)` for `p < 1/5`, that is `z < 1/320`. Thus `M_L² → 0` and the structure factor stays bounded, uniformly in `β`, `k` and even `L`. At `z = 1/400` the sum is `116/125`.

**Step 4 (chessboard ratios) — holds.** There are `3⁸ − 2 = 6559` bad patterns. A fully occupied bad cube has at least 3 opposite edges. The ratio identity `w_τ/w₊ = z^{−V}((1−t)/(1+t))^{2m}(1+t)^{−2k}` is the edge product, and dropping `(1+t)^{−k/4} ≤ 1` gives `P(σ = σ^τ)^{1/N} ≤ A^V U^m`. On both the `4³` and the `6³` tori, each of the 12 cube edges occurs twice per `2×2×2` cell. The pattern polynomial has 42 monomials, beginning `16A + 16U³ + 48AU² + 56A² + 30U⁴`.

**Step 5 (chessboard estimate) — assumed, and the deduction from it holds.** A1 is the standard estimate for reflections through planes of sites, with `2×2×2` blocks indexed by every site (they share faces) and exponent `1/N`. Subadditivity `𝔷(E ∪ E′) ≤ 𝔷(E) + 𝔷(E′)` is the union bound over assignments, using A1 on mixed patterns. It applies to the 6559 bad patterns, so `n` distinct cubes are all bad with probability at most `ε^n`. A1 is not proved in the attempt; nothing later treats it as proved.

**Step 6 (Peierls bound, given A2) — holds.** Opposite good cubes force every nearest-neighbour cube path to hit a bad cube. The count `26^{2(n−1)} = 676^{n−1}` bounds the star-connected `n`-sets through one cube. The finite sums `Σ_{n=1}^N 2n q^{n−1}` and `Σ_{n=L}^N q^{n−1}` match the stated closed forms, so the infinite sums are `2ε/(1−q)²` and `ε q^{L−1}/(1−q)` when `q < 1`. On the 8-torus every star-connected 3-set has `ℓ_∞` diameter at most 2, which is the size bound used to keep a separator of size `n < L` off the periodic cut. A2 itself is not proved.

**Step 7 (the corner) — holds.** `P(10^{−5}, 10^{−2}) = 1763606212274367599564337682401600001 / 10^{40} = 1.763606·10^{−4} ≤ 1/2704`. Then `q = 676P = 0.119220 ≤ 1/4`, and `1 − 2[2P + 2P/(1−q)²] = 0.998385 > 998/1000`. So `⟨σ_0 σ_x⟩ ≥ 0.998 − δ_L` with `δ_L → 0`, and `liminf M_L² ≥ 0.998`, for `z ≥ 10^{40}` and `1 − tanh β ≤ 10^{−8}` (`β ≥ log(2·10^8 − 1)/2 = 9.55691`). The attempt's `0.998` and the logged `0.996` are both below this value. A vacancy makes its cube bad, so the density is at least `1 − ε` once A1 is granted.

## What stays open

A1 and A2 are not discharged. The sphere menu is not reached. The two-valued window `1/320 ≤ z < 10^{40}` is open, and no `4³` table is computed. The constants are not sharp: the polynomial, not the quoted corner, is the region.

## Result

HIT: confirmed. At the two-valued neutral scale the kernel is `1 + tanh(β) σσ'`. There is no long-range order for `z < 1/320`. Granting the chessboard estimate and torus separation, `z ≥ 10^{40}` and `1 − tanh β ≤ 10^{−8}` give `⟨σ_0 σ_x⟩ ≥ 0.998 − δ_L`.
