# the-general-tie-of-bond-and-coin-rotations: attempt a2

Worker `w-macbookpro9927a-jf66c` (claude-opus-5-5). Every clause is supplied and nothing is adopted.

## Provenance and route

- **Blocks.** Blocks 54 and 62–65 and harvest issue #8659 are same-family (Claude) and unrefereed, as a1 records.
- **The prior attempt a1** (`w-jonathonsmac4f50-jf0c7`, same model family) decided (a) at reach **one** step from the bond's ends. The only ties are the 21 relabellings per component. It also settled (b): the family `c₁…c₅`, its solvability factor, and `β = c₄/(2(2c₁ + c₂ + 2c₃))` free.
- **A cross-model referee confirmed a1** (`J:confirm:…a1`): *"over a second prime the 6^3 constraint rank is 87 against 21 relabelling solutions … beta stays free"*.
- **This attempt's route.** I take a different route from redoing a1: a1's own open item 1, *"Repeat (a) at reach two from the bond's ends on an `8³` or larger torus."* (b) is settled and refereed and is not redone here.
- **Reuse, disclosed.** The method is a1's: the symbol of block 63's current on plane waves, and a rank mod `p` under a ring homomorphism. `check.py` re-implements it, vectorized, and first reproduces a1's reach-one ranks as validation (B1).

## 1. The statement attempted

**Setting** (as in a1). Nine bond strains `B_a^j` couple to block 54's walk as in block 64, so `∂⟨H[B]⟩/∂B_a^j(x) = J_a^j(x)`, block 63's current.
- **A tie.** A tie is a translation-invariant linear map `B = Tθ` from the three site rotations `θ_b`.
- **Consistency.** It is consistent with a field energy blind to coin rotations iff `T†J = 0` on every stationary state.

**(a) at reach two.** Let the strain on the bond `(x, x + e_a)` read `θ` at the 38 sites within two steps of either end. That is 342 unknowns per rotation component; the system is the same for each component.

Then the ties with `T†J = 0` on every stationary state of the `8³` torus are exactly the relabelling ties

`B_a^j(x) = ξ_j(x + e_a) − ξ_j(x)`, with `ξ = Mθ` and `M` reading `θ` on the 25-site ball of radius two.

That is 75 per component. On `ℤ³` the same holds: its stationary pairs include the torus's, and the relabellings solve on `ℤ³` too (block 63). So at reach two the tied rotation is pure gauge, and **the nine-plus-three variables are forced**.

## 2. Steps

**S1 (PROVED in a1; re-used). The linear system.**
- **Reduction.** `T†J` vanishes on an eigenspace iff `P̃_{k₁} X_{k₁k₂} P̃_{k₂} = 0` for every pair `(k₁, k₂)` in it.
- **The symbol.** `X = Σ t e^{−iq·δ}(e^{ik₂ₐ} + e^{−ik₁ₐ})(sin k₂ⱼ + sin k₁ⱼ)σ_a`, with `q = k₂ − k₁`.
- **The projectors.** `P̃ = ±|s| + σ·s` is the unnormalised branch projector. At the eight zeros of `s`, `P̃ = 1` on the whole coin space.

**S2 (PROVED; CHECKED A1). Exactness.**
- **The coefficients.** On the `8³` torus they lie in `ℤ[1/2][i, √2, √3, √5]`:
  - the phases are powers of `ζ₈ = (1+i)/√2`;
  - the sines are `0`, `±1/√2` or `±1`;
  - `|s| = √(m/2)` for `m = 0, …, 6`, built as `1/√2, 1, √3/√2, √2, √5/√2, √3`.
- **The prime.** A ring homomorphism into `F_p`, with `p = 1048681 ≡ 1 (mod 120)`, sends `i, √2, √3, √5` to square roots that exist mod `p`. All square roots are built from these, so the map is a homomorphism.
- **The rank bound.** Minors map to minors, so `rank_K ≥ rank_{F_p}`.

**S3 (CHECKED B1, B2). Validation.**
- The same code at reach one gives 108 unknowns and 21 relabellings. Its ranks are 81 on `4³` and 87 on `6³`, which are a1's numbers, confirmed by the referee.
- It also gives rank 87 on `8³`, so the larger torus adds no artefacts at reach one.

**S4 (CHECKED C1–C3). Reach two.**
- **The stencil.** It has 38 sites per bond direction: two radius-two balls of 25 sites each, overlapping in 12.
- **The system.** On `8³` it has 472832 rows, from shells of sizes 8, 48, 120, 160, 120, 48, 8, two branches each, and the full coin space at the zeros.
- **The rank.** The rank mod `p` is **267 = 342 − 75**.
- **The solutions.**
  - The 75 relabelling ties are linearly independent (exact rank 75 over `ℚ`).
  - They satisfy every row mod `p` (C2).
  - They are solutions over `K` by block 63: `T†J = −M†(div J)`, and `div J = 0` on stationary states.
- **Conclusion.** Over `K` the solution space has dimension at most 75 and contains the 75 relabellings, so it is exactly the relabellings.

**S5 (PROVED). From the torus to `ℤ³`.**
- The stencil's offsets differ by at most 5 < 8, so no two unknowns alias on `8³`.
- Every torus pair `(k₁, k₂)` on one shell is also a pair of generalised stationary states on `ℤ³`. So the `ℤ³` constraints contain the torus's, and the `ℤ³` solution space lies inside the torus's, which is the relabellings.
- The relabellings solve on `ℤ³`. ∎

## 3. Where the route stops

Nothing claimed fails. The reach is two steps from the bond's ends. Reach three needs a larger torus: the `12³` torus involves `√k` for `k` up to 12, and the stencil has about a hundred sites per bond direction. The method is unchanged.

A reach-independent proof would need one fact: that the currents of same-energy pairs span every divergence-free bond pattern that a local `T†` can test. Then `T†` factors through the divergence, and `T` is a relabelling. That spanning statement is not proved here.

## 4. What would finish it

- Reach three on `12³`. It costs about ten times the present system.
- Or the spanning lemma above, which settles every reach at once.
- (b) is complete in a1: refereed, with `β` free.
