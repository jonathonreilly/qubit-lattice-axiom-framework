# the-record-gas-chessboard-threshold: derivation attempt 1 of 2

Worker `w-jonathonsmac4f50-j2e73` (claude-opus-5-5), unit `J-derive-the-record-gas-chessboard-threshold-a1`.

**Provenance.** No earlier attempt at this problem is on `ai/probes`. The plan is my own:
- reflection positivity through planes of sites;
- chessboard estimates on `2×2×2` blocks;
- a Peierls sum;
- content factors bounded through block 81's bond identity.

**Sources.** Block 81, PR #8626, note
`ADMISSIBILITY_RULE_THE_RECORD_GAS_NEVER_MAKES_THE_CHESSBOARD_…_2026-09-22.md`, gives:
- the static law with vacancies;
- the scale `c = g·c₀`, with `c₀ = 6/(p + q + 4r)`;
- the matrix `M = c₀ω = J + 6λ₁P₁ + 6λ₂P₂`, with `λ₁ = (p − q)/(p + q + 4r)` and `λ₂ = (p + q − 2r)/(p + q + 4r)`;
- T1, the bond identity;
- the executed chessboard below `c₀`.

The scan `X:record-gas-chessboard-onset` is queued in `probes/tasks/refill_20260923_scans.json`, over `g ∈ [0.30, 0.50]`, and has no logs yet.

**The object.** On the torus `T_L = (Z/2L)³`, an arrangement `η` is a set of recorded sites. Each record carries a content in the six-axis menu. The weight is

  `z^{|η|} Π_{recorded bonds} g·M(s_x, s_y)`,

and a bond with an empty end weighs 1. Summing the contents gives the occupancy law

  `P(η) ∝ ζ^{|η|} g^{B(η)} W(η)`,

where:
- `ζ = 6z` is the activity of a record summed over its six contents;
- `B(η)` is the number of recorded bonds (both ends recorded);
- `W(η) = Z₀(η)/6^{|η|}`, with `Z₀(η) = Σ_contents Π_{recorded bonds} M`, is the weight over free.

Write `ε(x) = (−1)^{x₁+x₂+x₃}` and `S = Σ_x ε(x) n(x)`, the staggered count. The chessboards are `n = (1 ± ε)/2`, with structure factor `S²/N = N/4`, where `N = (2L)³`.

## 1. Statement attempted

**(a) What contents do.**
1. For every arrangement, `W(η) ≤ Λ^{c(η)}`. Here `Λ = max M = 6·max(p,q,r)/(p+q+4r)` and `c(η)` is the cycle rank of the recorded-bond graph. `W = 1` on forests. So contents can raise the weight of a cluster only through its cycles, by at most `Λ` each.
2. On the line `p + q = 2r` (so `λ₂ = 0`; this includes `(3,1,2)` and `(1,3,2)`), `W(η) ≥ 1` for every arrangement of `Z³`, and adding a recorded bond never lowers `W`. **Contents hurt the chessboard there:** relative to the content-less gas they reward exactly what the chessboard lacks, recorded bonds.
3. Off that line the sign of `W − 1` is not proved. Block 81 T2 finds it `≥ 0` on every window enumerated.

**(b) A proof with an explicit `g*`.** Take activity `ζ = g^{−3}` (the content-less half-filling point) and `g < g*(p,q,r)`. Then, uniformly in `L`:
- `E[S²]/N ≥ (N/4)(1 − 4ε − 2δ − o_L(1))`, with `4ε + 2δ < 1`: the gas makes the chessboard, with long-range staggered order;
- `g* = 8.0·10⁻¹⁰` without contents. There the weight is particle-hole symmetric at `ζ = g^{−3}`, so the density is exactly `1/2`;
- `g* = 5.2·10⁻¹⁰` at `(3,1,2)`, `6.1·10⁻¹⁰` at `(5,2,4)`, `1.9·10⁻¹⁰` at `(12,1,2)`.

The proof uses three ASSUMED standard results: the chessboard estimate, a torus separation lemma, and a count of connected sets. Against the scan window `0.30–0.50` and the content-less comparator `0.41`, the argument sits about nine orders of magnitude low. §3 says where the loss is.

**(c) A structural fact the proof needs.** The static law with vacancies is reflection positive through planes of *sites* at **every** `g ≥ 0`, including the excluded scales `g < 1`. Reflection positivity through planes *between* sites fails for `g < 1`: the occupancy block of the bond kernel, `[[1,1],[1,g]]`, has determinant `g − 1 < 0`. So the range `g ≥ 1` that block 81 cites from block 39 T5 is the range for bond-plane reflections. Through site planes the law is reflection positive at every scale. This is used here, not adopted.

## 2. Steps

**S1 (PROVED; CHECKED `E2`). The bond factor.** By block 81 T1, adding a recorded bond between recorded `x, y` multiplies `Z₀` by

  `Σ_s Π M · M(s_x,s_y) / Σ_s Π M = E_μ[M(s_x, s_y)]`,

where `μ` is the current joint law of the two contents, a probability measure. So the factor is at most `max M = Λ`. If `x` and `y` lie in different components, the two contents are independent and uniform, and the factor is `(1/36)ΣM = 1`, since the rows of `M` sum to 6. Build the bond graph one bond at a time: only cycle-closing bonds can cost more than 1. Hence `W ≤ Λ^{c(η)}`, and `W = 1` on forests. (`E2.1` checks `M = J + 6λ₁P₁ + 6λ₂P₂` with `P₁ = s·s'/2` and `P₂ = (s·s')²/2 − 1/6`, and `max M = Λ`, at seven triples.)

**S2 (PROVED; CHECKED `E4`). Contents hurt on `p + q = 2r`.** There `λ₂ = 0` and `M(s, s') = 1 + 3λ₁ s·s'`.

Take `λ₁ ≥ 0` first. Then

  `W(η) = E_unif[Π_b (1 + 3λ₁ s_x·s_y)] = Σ_{F ⊂ bonds} (3λ₁)^{|F|} E[Π_{b∈F} s_x·s_y]`.

Expanding each `s_x·s_y = Σ_i s_{x,i} s_{y,i}`, each term is a product over sites of single-site monomial means `E[s_{i₁}⋯s_{i_m}]`. Under the uniform six-axis law these are `≥ 0`: a monomial is `1/3` if all its indices agree and `m` is even (`≥ 2`), `1` if `m = 0`, and `0` otherwise (`E4.4`). So `W ≥` the `F = ∅` term, which is 1.

The same expansion with an extra factor `s_x·s_y` shows `E_η[s_x·s_y] ≥ 0`. So adding a bond multiplies `W` by `1 + 3λ₁E_η[s_x·s_y] ≥ 1`.

For `λ₁ < 0`, the lattice is bipartite, and `s → −s` on one sublattice preserves the uniform law and sends `λ₁ → −λ₁`. `E4.1`–`E4.2` confirm both statements on every arrangement of the `2×2×2` cube with at most 6 records, at `(3,1,2)` and `(1,3,2)`. `E4.3` confirms `W ≤ Λ^{c}` at four triples.

**S3 (PROVED; CHECKED `E3`). Reflection positivity through site planes, at every `g`.**

*The involution.* Let `θ` be the reflection `x₁ → 2m − x₁` of `T_L`. It fixes the two site planes `x₁ ≡ m` and `x₁ ≡ m + L`. Let it act on configurations by moving positions and leaving contents unchanged: `(θξ)_x = ξ_{θx}`. This is a symmetry of the weight, because `ω`, and so `M`, depends only on whether two contents are equal, opposite or orthogonal, never on the bond's direction.

*The factorisation.* Let `T_±` be the closed halves, which share the planes. Put into `F(ξ|T_+)`:
- the site weights of `T_+`, with a square root on plane sites;
- the bond weights of `T_+`, with a square root on bonds inside the planes.

All of these weights are `≥ 0`. Then `w(ξ) = F(ξ|T_+) F(θ(ξ|T_−))`, and for every `f` of `ξ|T_+`,

  `⟨f θf⟩ = Σ_{ξ_plane} (Σ_{ξ_{T_+∖plane}} f F)² ≥ 0`.

`E3.1` checks this exactly on the ring `Z/4`: every Gram block at fixed plane configuration has rank one with a nonnegative diagonal, at `g = 1/4, 1/100, 1, 4`. `E3.2` checks the failure for bond planes.

**S4 (ASSUMED; standard). The chessboard estimate.** Let the measure be reflection positive with respect to the reflections in all planes `x_i = m`, `m ∈ Z`. For events `A_t` determined by the configuration on the unit block `{0,1}³ + t` (`N` blocks, overlapping on faces):

  `P(∩_t A_t) ≤ Π_t (Z(A_t everywhere)/Z)^{1/N}`.

Here "`A` everywhere" means every block carries the reflected image of `A`. The right-hand side is subadditive in `A`. References: Fröhlich–Israel–Lieb–Simon 1978; Shlosman 1986; Biskup 2009, lecture notes on reflection positivity.

**S5 (PROVED from S1, S3, S4; CHECKED `E1`, `E5`). The block bound.**
- For an occupancy pattern `A` of `{0,1}³` with `n` records and `b` recorded bonds, "`A` everywhere" is the 2-periodic extension of `A`. It has `Nn/8` records and `Nb/4` recorded bonds, because each bond of the block appears twice per period cell.
- Its contents sum to `ζ^{Nn/8} g^{Nb/4} W(η_A)`, with `W ≤ Λ^{Nb/4}` by S1.
- `Z ≥ 2ζ^{N/2}`, from the two chessboards, which have no recorded bond.

Hence

  `ρ(A) := (Z(A everywhere)/Z)^{1/N} ≤ ζ^{(n−4)/8} (gΛ)^{b/4}`.

With `ζ = g^{−3}` define

  `ε(g) := Σ_{A ∉ {chessboards}} g^{−3(n−4)/8}(gΛ)^{b/4}`,

a sum over the 254 bad patterns (`E1`). Then `P(block bad) ≤ ε`, and `P(k given blocks all bad) ≤ ε^k`.

The leading terms are `g^{3/8}` from the 8 one-vacancy patterns (`n = 3`, `b = 0`) and `g^{3/8}Λ^{3/4}` from the 8 one-extra-record patterns (`n = 5`, `b = 3`). No bad pattern costs less than `g^{3/8}` (`E1.3`).

**S6 (ASSUMED; standard). Separation and counting.** Blocks `u` and `v` whose index difference is a unit vector share 4 sites, 2 even and 2 odd. So two such good blocks are in the same phase: the phase propagates along face-adjacent good blocks (PROVED).

If `B_u` is even-good and `B_v` is odd-good, the bad blocks separate `u` from `v` in the face-adjacency graph. The torus separation lemma (Deuschel–Pisztora 1996 Lemma 2.1 on `Z^d`; the torus form as in Fröhlich–Israel–Lieb–Simon §5) then gives a `*`-connected set of bad blocks (26-adjacency) that does one of three things:
- encloses `u`: it has at least 6 blocks and meets the `e₁`-ray from `u` within its own size;
- encloses `v`, in the same way;
- wraps the torus, with at least `2L` blocks.

The number of `*`-connected sets of `k` blocks that contain a given block is at most `(26e)^k` (Klarner, Kesten).

**S7 (PROVED from S5, S6; CHECKED `E6`). Long-range order.** Set `x = 26e·ε`. Then

  `P(B_u, B_v good in different phases) ≤ δ + w_L`,

where `δ = 2Σ_{k≥6} k x^k = 2x⁶(6 − 5x)/(1 − x)²` and `w_L = N x^{2L}/(1 − x) → 0`.

Write `S = (1/8)Σ_B m(B)`, where `m(B) = Σ_{y∈B} ε(y)n(y) ∈ [−4, 4]`, `m = ±4` on the two good phases, and each site lies in 8 blocks. Then

  `E[m(B)m(B')] ≥ 16(1 − 2(2ε + δ + w_L))`,

and so

  `E[S²] ≥ (N²/4)(1 − 4ε − 2δ − 2w_L)`.

`E6` finds, by rational bisection on `t` with `g = t⁸` and exact arithmetic (with `e < 2.7183` and a rational upper bound on `Λ^{1/4}`), the `g*` of §1(b). At each, `x = 0.507` and `4ε + 2δ < 1`.

**S8 (PROVED; CHECKED `E7`). Half filling for the comparator.** At `ζ = g^{−3}`, every site has 6 bonds, so `ζ^{N} g^{B} = g^{Σ_b (n_x n_y − (n_x + n_y)/2)}`. This is invariant under `n → 1 − n`. So the content-less gas is at exact half filling, and its `g* = 8.0·10⁻¹⁰` is a statement at half filling.

With contents, `W` breaks this symmetry. S7 holds at `ζ = g^{−3}`, where the density lies within `ε` of `1/2`. That the canonical half-filled law, or the grand-canonical one tuned to density `1/2`, also orders is **not proved here**.

## 3. Where the argument loses, and what would finish it

- **The two losses are both geometric.**
  1. A point defect (one vacancy or one extra record) costs `ζ^{−1} = g³` in weight, but the chessboard estimate spreads it over the 8 blocks sharing the site, which leaves `g^{3/8}` per block.
  2. The contour entropy of `*`-connected block sets is `26e ≈ 70.7` per block.

  So `g^{3/8} ≈ 1/(70.7·(8 + 8Λ^{3/4}))`, which is `g ≈ 10⁻⁹`.

- **Contents.** They change `g*` only through `Λ^{3/4}` in the second family (`8.0 → 5.2·10⁻¹⁰` at `(3,1,2)`). In this argument they cost at most `Λ` per cycle-closing bond.

- **A direct Peierls argument would do better.** Use plaquette contours (like bonds) with a translation map inside the contour, whose weight `W` is preserved exactly by translation. Then each like bond costs `g^{1/2}` (`g^{1/2}Λ` if it closes a cycle), and the entropy is about `12e` per plaquette. That should bring `g*` near `10⁻³/Λ²`. The price is Dobrushin's thick-contour geometry for the shift. Neither version approaches `0.3–0.5`.

- **Towards the scan's window.** It needs either a comparison with the content-less antiferromagnetic gas (whose threshold `0.41` is itself numerical), or a rigorous expansion at the true threshold. On `p + q = 2r`, S2 shows that contents only add weight to bonded arrangements. So any such comparison can at best reproduce the content-less threshold, never improve on it.

- **The open item from the task.** Whether contents can *help* off the line `p + q = 2r` (a factor `< 1` for some arrangement) remains open, as in block 81.

`SUMMARY: PROVED` modulo S4 and S6 (see `check.py`).
