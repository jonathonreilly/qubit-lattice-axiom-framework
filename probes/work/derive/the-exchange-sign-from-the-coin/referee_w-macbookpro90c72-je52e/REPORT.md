# Referee report: the exchange sign from the coin, attempt 1

- **Author:** `w-macbookpro90c72-j3430` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-je52e` (`grok-4.6`). Different model family.
- **Checks:** own Gaussian-integer walk and own one-site algebra. The author's script is not called.

## The statement that survives

The Record axiom gives exclusion, not an exchange sign. Both the symmetric and the antisymmetric hard-core sectors are closed under the two-record walk, carry one record per site, and are invisible to readouts that see only content. No involution of `ℂ²`, linear or antilinear, makes all three Pauli matrices odd: the linear solutions are zero, and the antilinear ones are `c σ₂ K`, which square to `−|c|²`. A graded record needs at least `ℂ⁴`. The graded composite of two Clifford presentations is `Cl(6,0)`, real rank 64, whose two sitewise complex units anticommute; the complex composite `M₂(ℂ) ⊗ M₂(ℂ)` does not. Neither composite is named by the one-site sentences.

Under exclusion the sectors agree at orders 2 and 3 on `Z²` and `Z³`. They differ at order 4 by `−8` per plaquette: `−8` per site on `Z²` and `−24` per site on `Z³`. Coin-summed, a pair exchanges with amplitude `−2` if the records are neighbours, `−1` on a face diagonal, and `0` at distance 2 on a line. On a ring the difference vanishes below order `N`, equals `128`, `−1248`, `7680` for `tr(P (2H)ᴺ)` at `N = 4, 6, 8`, and is absent for every order on odd rings: on 5 and 7 sites the unitary `U = (σ₁⊗σ₁)(G⊗G)J` preserves the walk and flips the exchange.

## Steps

**1.** `α(x) = σ₂ x̄ σ₂` fixes `1` and `iσ_a`, negates `σ_a` and `i`, and is multiplicative on the generators. A pure state `(1 + u·σ)/2` has even part `1/2` and odd part `u·σ/2`.

**2.** The linear intertwiner `Γσ_a = −σ_a Γ` is only `Γ = 0`. The antilinear ones are multiples of `σ₂ K`, and `(σ₂ K)² = −1`.

**3.** `Γ = 1⊗σ₃` and `e_a = σ_a⊗σ₁` on `ℂ⁴` satisfy `Γ² = 1`, `Γ e_a = −e_a Γ`, and `e_a² = 1`. The pseudoscalar squares to `−1`.

**4.** Six tensor Majoranas on three qubits square to `1`, anticommute, and their 64 ordered products are distinct matrices.

**5.** An exact enumeration of hard-core paths gives zero exchange at orders 2 and 3, and `tr(P (2H)⁴) = −128` per site on `Z²` and `−384` per site on `Z³`. Dividing by `16` is `−8` and `−24`. The six neighbour separations contribute `−32` each, the twelve face diagonals `−16`, and the six distance-2 axis separations `0`.

**6.** On rings of 4, 6 and 8 the exchange trace of `(2H)^k` is zero for `k < N` and `128`, `−1248`, `7680` at `k = N`. At `N = 4` the hard-core second moment is `2/3`, and the two sector fourth moments are `5/6` and `7/6`.

**7.** On rings of 5 and 7, the same `U` satisfies `UH = HU` and `UP = −PU`.

The absolute fourth moments `9135/496` and `9183/496` on the 3-torus of side 5 were not rebuilt. A 4-hop exchange cannot wind on that torus, so the per-site difference is the local one, `−24`, and the sectors differ.

## Verdict

The counterexample survives. The axioms as stated do not choose the exchange sign. It is a conditional, first visible in the fourth moment of a localised pair.
