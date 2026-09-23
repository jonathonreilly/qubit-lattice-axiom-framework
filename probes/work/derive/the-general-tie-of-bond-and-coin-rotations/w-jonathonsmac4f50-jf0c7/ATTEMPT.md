# The general tie of bond and coin rotations — attempt 1

Worker `w-jonathonsmac4f50-jf0c7`, model `claude-opus-5-5`. Task `J:derive:the-general-tie-of-bond-and-coin-rotations:a1`.

**Provenance.** Blocks 54 and 62 to 65 were written by the same model family (Claude Opus). So was the attempt behind harvest issue #8659, which this problem builds on (`one-set-of-variables...:a2`, another worker). All are open and unrefereed. I restate what I use. The referee should come from another family. There were no prior attempts on this problem at claim time.

**Scope.** This works within the supplied clauses of blocks 54 and 62 to 65. Nothing is adopted. The parked decisions are untouched. No gravitational claim is made. Part (a) is exact on finite tori. Part (b) is in block 64's continuum symbols, as block 64 T2 to T4 are.

## 1. The exact statement attempted

**Setting.**
- **Strain and current.** Nine bond strains `B_a^j` couple to block 54's walk as in block 64: `H[B] = H + Σ σ_a (1/2){C_a[B_a^j], S_j}`. So `∂⟨H[B]⟩/∂B_a^j(x) = J_a^j(x)`, block 63's bond current.
- **A tie.** Three site rotations `θ_b` are tied to the strains by a local linear map `B = Tθ`, translation-invariant. The strain on the bond `(x, x + e_a)` reads `θ` at the 12 sites within one step of either end of the bond.
- **The consistency test.** A field energy blind to coin rotations has consistent static equations for the tied variables iff `T†J = 0` on every stationary state. The coin's own response already vanishes on stationary states (block 65 T3).

**(a) (PROVED; CHECKED exactly)** On the `6³` torus, the ties with `T†J = 0` on every stationary state are exactly the **relabelling ties** `B = d(Mθ)`: `B_a^j(x) = ξ_j(x + e_a) − ξ_j(x)` with `ξ = Mθ`, where `M` reads `θ` on the 7-point star. Their dimension is 21 per rotation component, 63 in all.
- A relabelling tie makes the tied rotation pure gauge: it is invisible to any field energy of the curls (block 64 T1).
- **So no genuine tie of bond rotations to coin rotations exists at this reach, and the nine-plus-three variables are forced.**
- The forward-bond tie of issue #8659 fails. The `4³` torus alone admits 6 more ties per component, which are artefacts of `2 ≡ −2` on that torus.

**(b) (PROVED; CHECKED)** The nine-plus-three field energies.
- The family is block 64's family with `c₀ = 0`: five numbers `c₁` to `c₅`.
- It sees bond rotations iff `(c₁, c₂, c₃)` is not along `(1, 2, −4)`, block 64's blind ratio.
- Its static equations are solvable for every source iff `(2c₁ − c₂)(2c₁ + c₂)(2c₁ + c₂ + c₃)(2c₁ + c₂ + 2c₃) ≠ 0`. The blind member has rank 3 and cannot balance a bond torque.
- Block 64's exponent is `β = c₄/(2(2c₁ + c₂ + 2c₃))`: **free**. `β = 1` is the hyperplane `c₄ = 2(2c₁ + c₂ + 2c₃)`; it is not forced.

## 2. Steps

### Step 1 — the current's symbol (PROVED; CHECKED 1.1)
- For plane waves `|k, u⟩`: `⟨k′, u′| σ_a (1/2){C_a[δ_x], S_j} |k, u⟩ = e^{iq·x}(e^{ik_a} + e^{−ik′_a})(sin k_j + sin k′_j)/4 · u′†σ_a u`, with `q = k − k′`.
- The proof uses `S_j|k⟩ = sin k_j |k⟩` and `C_a[δ_x] = (|x⟩⟨x + e_a| + h.c.)/2`. Checked exactly on the `4³` torus.
- It is block 63's `e^{iq_a/2} cos(k̄_a)` form.

### Step 2 — the linear system (PROVED; CHECKED 2.1–2.7)
- **The system.** `(T†J)_b(y) = Σ_{a,j,δ} t^{jb}_a(δ) J_a^j(y − δ)`. A stationary state lies in one eigenspace of `H`: a shell `Σ sin² k_j = const` with one branch `±|s|`, or, at the eight zeros, the whole coin space.
- **Reduction to the symbol.** `T†J` vanishes on every vector of an eigenspace iff `P̃_{k′} X_{k′k} P̃_k = 0` for every pair `(k′, k)` in it. Here `X_{k′k} = Σ t e^{−iq·δ}(e^{ik_a} + e^{−ik′_a})(sin k_j + sin k′_j) σ_a`, and `P̃_k = ±|s(k)| + σ·s(k)`, the unnormalised projector on the branch. At the zeros `P̃ = 1`.
- **The same system for each `b`.** It is linear in `t` and identical for each rotation component `b`: 108 unknowns (2.2).
- **Exactness.** The coefficients lie in `ℤ[1/2][i, √2, √3]`. On the `6³` torus the phases are powers of `ζ₆ = (1 + i√3)/2`, the sines are `0` or `±√3/2`, and `|s| ∈ {√3/2, √6/2, 3/2}`.
  - A ring homomorphism into `F_p`, with `p = 1048609 ≡ 1 (mod 24)`, sends `i, √2, √3` to square roots that exist there (2.1).
  - Every minor maps to a minor, so `rank_K ≥ rank_{F_p}`.
- **The numbers.**
  - The `6³` system (125184 rows) has rank 87 mod `p`, so over `K` the solution space has dimension at most 21 (2.5).
  - The relabelling ties are 21 linearly independent solutions (2.3). They are solutions by block 63: `T†J = −M†(div J)`, and `div J = 0` on stationary states. The mod-`p` check confirms it (2.4).
  - Hence exactly 21.
- **Real ties.** The solutions are spanned by real ties, so the real solution space is the same.
- **The `4³` torus alone** has rank 81 (2.6). Its extra ties use offsets `2` and `−2`, which that torus does not tell apart.
- **Issue #8659's tie.** The forward-bond tie `B_a^j = ε_{abj} θ_b(x)` violates about 70,000 of the `6³` rows (2.7).

### Step 3 — (b) (PROVED; CHECKED 3.1–3.4)
- **Which members see bond rotations (3.1).** Split the quadratic density `c₁T₁ + c₂T₂ + c₃T₃` of a plane wave by symmetric plus antisymmetric strain. It is independent of the antisymmetric part iff `(c₁, c₂, c₃) ∝ (1, 2, −4)`.
- **The static form (3.2).** With `k = κe₃`, the relabellings are `B₃^j`. On the six remaining components the form has eigenvalues `κ² × {2c₁ − c₂, 2c₁ + c₂ (twice), 2c₁ + c₂ + c₃ (twice), 2c₁ + c₂ + 2c₃}`.
- **Solvability.** The walk's source `J` is divergence-free on stationary states (block 63), so it is orthogonal to the relabellings. Solvable for every such source therefore means non-degenerate.
- **The blind member (3.3).** It has two vanishing factors and rank 3.
- **The exponent (3.4).** Block 64 T4: `β = c₄/(4c₁ + 2c₂ + 4c₃) = c₄/(2(2c₁ + c₂ + 2c₃))`. `c₄` is free, so `β` is free.
- **Count.** Five numbers, four ratios after the overall `K`. Imposing `β = 1` leaves three.
- **Comparator.** This is the teleparallel family of Hayashi and Shirafuji, where `γ = 1` is also an extra condition.

## 3. Where the route stops

Nothing claimed fails. Two limits:
1. **Reach.** The reach is one step from the bond's ends. A wider reach needs a torus larger than `6³` to avoid aliasing (the `4³` torus shows how aliasing admits spurious ties).
2. **(b)'s degree.** Part (b) is quadratic in the continuum symbols.

## 4. What would finish it

1. Repeat (a) at reach two from the bond's ends on an `8³` or larger torus. The method is unchanged; the system grows to about a million rows.
2. Place (b)'s family on the lattice. Decide which part of the four-ratio family the owner would state, and whether a principle (for example, no ghost in the antisymmetric sector) fixes `β`.
