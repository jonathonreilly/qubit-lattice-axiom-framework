# J:derive:discrete-step-walk-under-the-clock-clause:a3 — worker w-macbookpro90c72-jf02d

Model: claude-opus-5-5. Check: `python3 probes/work/derive/discrete-step-walk-under-the-clock-clause/w-macbookpro90c72-jf02d/check.py`
(sympy + numpy, about one second; P1–P6 exact, P7 floating point).

**Provenance.**
- I formed the plan (a split-step walk whose rotation angle is the bond clock, plus a spectral no-go for exact
  clocks) before reading attempt a1 (`w-jonathonsmac4f50-j0f4f`).
- a1 tabulates three formulations: a coin angle that acts as a mass, a fraction of ticks that is not unitary, and
  `U^w` that is not local. Under "what would finish it" it lists (2) a theorem replacing its symbol argument for
  `U^w`, and (3) the split-step walk, "which might separate the mass from the rate".
- This attempt supplies (3) in S1–S4 and a general theorem in the direction of (2) in S5–S6. It builds on a1's open
  items, not on a refereed result.
- S1(ii) also narrows a1's (a)-i: the coin angle is a mass near `θ = 0` but a rate near `θ = π/2`, read every
  second tick.
- Overlap with my own earlier unit: #8760 (ray-limit-of-the-clocked-walk a4) worked on block 54's continuous-time
  walk. No step here reuses it.
- Blocks 53/54, a1 and this attempt are all from the Claude family. S1–S6 want a referee of another family.

**Definitions used** (block 54 note on the branch of PR #8570, theorems T2–T4, read for this unit):
- `(T_e ψ)(x) = ψ(x − e)`, with symbol `e^{−ik·e}`.
- `D = (i/2)(T − T†)`, with symbol `sin k`.
- The line walk is `σ D`.
- The clause gives `H_w = W^{1/2} H W^{1/2}`: every bond carries `√(w_x w_y)`, and any bond timing homogeneous of
  degree one is allowed (T2, T3).
- The translation identity (T3): if `w(x + a) = λ_a w(x)`, then `H_w T_a = λ_a T_a H_w` and
  `U_w(t) T_a = T_a U_w(λ_a t)`, meaning "a packet moved up the gradient by `a` does everything `λ_a` times
  faster".
- The ray law for `E = w(x) ε(k)` (T4) is `dv/dt = −w² (ε²/2)'' ∂_x u + 2 v² ∂_x u` on a line, with `u = log w`.
  For the walk, `ε = |sin k|`, which gives `−w² cos 2k`.

## 1. Statement attempted

The **partial-swap walk** on `ℓ²(ℤ; ℂ²)`, with components (up, down) per site:
- `U[w] = B[w] A[w]`.
- `A[w]` is the product over bonds `b = (x, x+1)` of `exp(−i ε_b X_b^A)`, where `X_b^A` swaps `(up, x)` and
  `(down, x+1)`.
- `B[w]` is the same with `X_b^B` swapping `(down, x)` and `(up, x+1)`.
- The bond angle is the bond clock, `ε_b = ε0 √(w_x w_{x+1})`.

Claims:

- **(a)** `U[w]` is unitary for every positive field `w` and has range 2. It equals, up to conjugation and a sign,
  two ticks of the coined walk `S R(θ_x)` at `θ_x = π/2 − ε_{(x,x+1)}`. Its first-order generator is, after the
  gauge `ψ_x → i^x ψ_x`, exactly `2ε0` times block 54's clocked line walk.
- **(b)** At a uniform angle, `sin(ω/2) = sin ε |cos k|`. The rays of this dispersion, with `ε = ε0 e^{u}`, obey
  `dv/dt = (2v² + Ψ) ∂_x u`, where `Ψ = 4 sin ε (ε cos ε − 2 sin ε sin²k)/(1 − sin²ε cos²k)`. This is block 54's
  law for `E = 2ε|sin k'|` (with `k' = k + π/2`) plus `O(ε⁴)`.
- **(c)** The translation identity splits into two halves:
  - *Covariance:* the translate of the step is the step at all clocks multiplied by `λ_a`. This holds exactly.
  - *Clock:* that step equals `λ_a` steps. This fails, and it fails for **every** local unitary rule that moves
    packets. The general statement is the flat-band theorem S5: a finite-range unitary whose powers up to
    `N(2R+2)` stay within range `R`, or whose eigenphases scale exactly with a clock over an interval, has flat
    bands and never moves a walker more than `(N−1)R` sites.

## 2. Steps

**S1 (a): unitarity, locality, and two relations.**
- (i) PROVED + CHECKED (P1). Each layer is a product of commuting rotations `cos ε_b − i sin ε_b X_b` on disjoint
  pairs, because each layer's pairs form a perfect matching of the basis. So `A` and `B` are unitary for every
  assignment of angles.
  - An `(up, x)` amplitude reaches `(up, x)`, `(down, x±1)` and `(up, x+2)`. A `(down, x)` amplitude reaches
    `(down, x)`, `(up, x±1)` and `(down, x−2)`. So the range is 2.
  - P1 checks `U†U = 1` and the range exactly on a ring of 6, with six different rational `(cos, sin)` pairs.
- (ii) PROVED + CHECKED (P1). Let `S` move up by +1 and down by −1, `R(θ) = [[cos θ, −sin θ], [sin θ, cos θ]]` (a1's
  coin), and `Y = ⊕σ_y`. Then:
  - `R(π/2 − ε) = (−iσ_y) exp(iεσ_y)`.
  - `Y S Y = S^{−1}`, and `Y` commutes with every on-site `exp(iε_xσ_y)`.
  - Hence `(S R(θ))² = −S R'(−ε) S^{−1} R'(−ε)`, where `R'(φ) = ⊕_x exp(−iφ_x σ_y)`, i.e. `R'(−ε)` is the on-site
    coin `exp(+iε_xσ_y)`.
  - Conjugating by the half-shift of the down component and the phase `diag(1, −i)` turns the right side into
    `−U[ε]`, with `ε_x` on the bond `(x, x+1)`.
  - P1 checks `(S R(θ))² = −G U G^{−1}` exactly on a ring of 6, where `G` shifts the down component by −1 and then
    multiplies it by −i.
  - Reading: the coin angle is a mass near `θ = 0` (a1's `cos ω = cos θ cos k` has gap `θ`), and a rate near
    `θ = π/2`, read every second tick. At `ε = 0` the two ticks cancel (`S S^{−1}`) and the walker is at rest.
- (iii) PROVED + CHECKED (P4, symbol part). Write `σ_± = |up⟩⟨down|, |down⟩⟨up|`.
  - The layer generators are `σ_− ⊗ T + σ_+ ⊗ T†` and `σ_+ ⊗ T + σ_− ⊗ T†`. They sum to `H' = σ_x ⊗ (T + T†)`, with
    symbol `2 cos k σ_x`.
  - With bond angles `ε0 √(w_x w_{x+1})`: `U[w] = 1 − iε0 W^{1/2} H' W^{1/2} + O(ε0²)`.
  - The gauge `(Gψ)(x) = i^x ψ(x)` gives `G T G^{−1} = iT`, so `G H' G^{−1} = σ_x ⊗ i(T − T†) = 2σ_x D`.
  - `G` commutes with `W`. So the first-order generator is `2ε0 (σ_x D)_w`, block 54's clocked line walk with time
    measured in units of `1/(2ε0)` ticks.
  - A plane wave of wave number `k` becomes one of `k' = k + π/2`.
- (iv) Remark, PROVED: the `O(ε²)` term of the product formula is `−(ε²/2)[H'_B, H'_A]`, with symbol
  `i ε² sin 2k σ_z`. It changes the Bloch eigenvectors at relative `O(ε)`, not the bands.
  - The symmetric step `A_{1/2} B A_{1/2} = A_{1/2} (BA) A_{1/2}^{−1}` has no `ε²` term (it is second-order
    accurate) and the same spectrum.
  - So that deviation is a fixed local change of basis.

**S2 (b): dispersion.** PROVED + CHECKED (P2).
- The pair operators have symbols `M_A = [[0, e^{ik}], [e^{−ik}, 0]]` and `M_B = M_A*`. Both are hermitian
  involutions, so each layer is `cos ε − i sin ε M`.
- Multiplying out gives `tr Û/2 = 1 − 2 sin²ε cos²k` and `det Û = 1`.
- So the eigenvalues are `e^{∓iω}` with `cos ω = 1 − 2 sin²ε cos²k`, that is `sin(ω/2) = sin ε |cos k|`.

**S3 (b): a clock to relative `O(ε²)`.** CHECKED (P3), an exact series.
- `ω = 2ε|cos k|(1 − (ε²/6) sin²k) + O(ε⁵)`.
- `ε ∂_ε ω / ω = 1 − (ε²/3) sin²k + O(ε⁴)`.
- With `ε = ε0 w`, every frequency scales with the local clock up to a relative `O(ε²)` that reshapes the band.
- The force `−∂_x ω = −(ε ∂_ε ω) ∂_x u = −ω ∂_x u (1 − (ε²/3) sin²k + …)`: block 54's "force = energy × gradient"
  (T3) to that order.

**S4 (b): the ray law.** PROVED + CHECKED (P4, P5).
- (i) For any separable `ω = w(x) f(k)`, Hamilton's equations `ẋ = ∂_k ω` and `k̇ = −∂_x ω` give exactly
  `dv/dt = −w² (f²/2)'' ∂_x u + 2v² ∂_x u` (P4, symbolic in `w` and `f`). This is block 54's T4 on a line.
- (ii) For the walk, `ω = Ω(ε(x), k)` with `ε = ε0 e^{u}`:
  - `dv/dt = Ω_kk k̇ + Ω_kε ε ∂_x u ẋ = ε ∂_x u (Ω_kε Ω_k − Ω_kk Ω_ε)`.
  - P5 verifies exactly that this equals `(2v² + Ψ) ∂_x u`, with `Ψ` as in §1, on both branches `cos k ≷ 0`.
  - The expansion is `Ψ = 4ε² cos 2k + (ε⁴/3)(2 cos 2k + 3 cos 4k − 1) + O(ε⁶)`.
- (iii) Comparison with block 54.
  - Since `cos 2k = −cos 2k'`, the leading term is `−(2ε)² cos 2k'`. That is block 54's `−w² cos 2k` for the
    dispersion `E = 2ε|sin k'|` of S1(iii), with `2ε = 2ε0 w` as the clock.
  - The discrete step adds exactly the `O(ε⁴)` term above, and nothing at `O(ε²)`.
  - a1 found block 54's law "does not apply" to its coin-angle walk. That is consistent: a1's walk is read at
    `θ` near 0, where `θ` is a mass.
- (iv) CHECKED, floating point (P7). The line has `ε = 0.6 e^{0.001(x−500)}`, and a packet of width 30 starts at
  `k = π/3` on the upper band. It runs 400 steps of the exact vectorized `U[w]`.
  - The centroid moved −326.59 sites.
  - The exact discrete rays of S2 give −326.80, off by 0.213.
  - The separable leading-order law gives −324.47, off by 2.118.
  - The packet follows the discrete rays and resolves the `O(ε²)` of S3.

**S5 (c): the flat-band theorem.** PROVED (a full argument, below). P6 checks exactly that the conclusion is
attained, so it is not vacuous.

- *Setting.* `V` is a unitary on `ℓ²(ℤ; ℂ^N)` that commutes with translations. Its Bloch matrix `V̂(k)` satisfies
  `(V^m)^ = V̂^m`. "Range `≤ R`" means every entry of the symbol lies in
  `T_R = span{e^{ijk} : |j| ≤ R}`, which has dimension `2R+1`.
- **Theorem S5a.** If `V, V², …, V^M` all have range `≤ R`, where `M = N(2R+2)`, then the spectrum of `V̂(k)`
  (with multiplicity) does not depend on `k`, and `V^n` has range `≤ (p−1)R ≤ (N−1)R` for every `n ∈ ℤ`. Here `p`
  is the number of distinct eigenvalues.
- **Theorem S5b.** Let `I` be an open interval and, for `c ∈ I`, let `V_c` have range `≤ R`. Suppose there are
  real functions `f_1, …, f_N` (no regularity assumed) such that, for all `c ∈ I` and all `k`, the eigenvalues of
  `V̂_c(k)` are `e^{−icf_b(k)}`; that is, the step at clock `c` runs one law for time `c`. Then the same conclusion
  holds for every `c ∈ I`.

*Proof.*

1. **Interpolation.** Take the nodes `k_i = 2πi/(2R+1)`, `i = 0..2R`.
   - If `p ∈ T_R` vanishes at every node, then `e^{iRk} p(k)` is a polynomial of degree `≤ 2R` in `e^{ik}` with
     `2R+1` distinct roots, so `p = 0`.
   - Evaluation at the nodes is therefore a bijection `T_R → ℂ^{2R+1}`. So there are `ℓ_i ∈ T_R` with
     `p(k) = Σ_i ℓ_i(k) p(k_i)` for every `p ∈ T_R`.
2. **The traces are in `T_R`.** For S5a, `t_m(k) = tr V̂(k)^m = Σ_b z_b(k)^m` lies in `T_R` for `m = 1..M`, where
   the `z_b` are the eigenvalues. So for every `k`:
   `Σ_b z_b(k)^m = Σ_i ℓ_i(k) Σ_b z_b(k_i)^m`, for `m = 1..M`.
3. **The eigenvalues lie in a finite set.** Fix `k`.
   - Let `Z` be the distinct values among `{z_b(k)} ∪ {z_b(k_i)}`. Then `|Z| ≤ N + N(2R+1) = M`.
   - Collecting terms gives `Σ_{ζ∈Z} a_ζ ζ^m = 0` for `m = 1..|Z|`, where
     `a_ζ = #{b : z_b(k) = ζ} − Σ_i ℓ_i(k) #{b : z_b(k_i) = ζ}`.
   - The matrix `(ζ^m)` has determinant `Π ζ · Π_{ζ<ζ'} (ζ' − ζ) ≠ 0`, so every `a_ζ = 0`.
   - A `z_b(k)` outside the node values would have `a_ζ` equal to its multiplicity, which is `≥ 1`. So every
     eigenvalue of every `V̂(k)` lies in the finite set `F = {z_b(k_i)}`.
   - For S5b the same identity holds with `e^{−icf_b}` for all `c ∈ I`. Fix `k` and let `Λ` be the distinct values
     among `{f_b(k)} ∪ {f_b(k_i)}`. Then `E(c) = Σ_{λ∈Λ} a_λ e^{−icλ}` vanishes on `I`, so all its derivatives
     vanish at some `c_0 ∈ I`.
   - Orders `0..|Λ|−1` give a Vandermonde system in the distinct numbers `−iλ`, so `a_λ = 0`. Hence
     `f_b(k) ∈ {f_b(k_i)}`, and for each `c` the eigenvalues lie in a finite set.
4. **The spectrum is constant in `k`.** `χ_k(z) = det(z − V̂(k))` has coefficients continuous in `k`, and its roots
   lie in the finite set.
   - So `χ_k` belongs to the finite set of polynomials `Π (z − ζ)^{n_ζ}` with `Σ n_ζ = N`. Distinct members have
     distinct coefficient vectors.
   - A continuous map from the connected circle into a finite set is constant.
5. **No transport.** `V̂(k)` is unitary, hence diagonalizable, with the constant distinct eigenvalues
   `s_1..s_p`.
   - So `P_q = Π_{r≠q} (V̂ − s_r)/(s_q − s_r)` is its spectral projection, with entries in `T_{(p−1)R}`.
   - Then `V̂^n = Σ_q s_q^n P_q` for all `n ∈ ℤ`. ∎

*Remarks.*
- In `d` dimensions, use `T_R` in each variable with range in the max-norm, product-grid nodes (unisolvent by
  induction on `d`), `M = N((2R+1)^d + 1)`, and the connected torus.
- S5b covers a1's `U^w`, in the form that matters: no finite-range family has exact clock scaling. It is not a
  theorem that "no finite-range `V` has `V² = U`". That statement is false in general: by S1(ii), the partial-swap
  walk is the square of a range-1 unitary. P1 checks exactly that `U = V²` with `V = i G^{−1} S R G` of range 1.
- The conclusion cannot be strengthened from "flat" to "trivial". P6 exhibits `H = [[0, e^{−ik}], [e^{ik}, 0]]`,
  which has `H² = 1`, so `e^{−icH} = cos c − i sin c H`. That is a group of range-1 steps with k-dependent
  eigenvectors, satisfying both hypotheses.

**S6 (c): the translation identity in discrete steps.** PROVED; the instance is CHECKED (P6).
- (i) **The covariance half is exact.**
  - The rule is translation covariant: with the note's `T_a`, `T_a^{−1} U[w] T_a = U[w(·+a)]`.
  - Its bond angles are homogeneous of degree one in the clocks.
  - So in a uniform gradient `T_a^{−1} U[w] T_a = U[λ_a w]`: the translate is the step with every bond angle
    multiplied by `λ_a`.
  - Unlike T3, this holds on all of `ℤ`, not only in a slab, because `U[w]` is a bounded product of rotations for
    every field.
- (ii) **The discrete form of "does everything `λ_a` times faster".** Block 54's `U_w(t) T_a = T_a U_w(λ_a t)`
  becomes `U[w] T_a = T_a U[w]^{λ_a}`. This is defined for integer `λ_a` without choosing a logarithm, and by (i)
  it is equivalent to `U[λ_a w] = U[w]^{λ_a}`.
  - For the partial-swap walk it fails for every field at `λ_a = 2`.
  - `⟨up, x+4| U[w]² |up, x⟩ = Π_{j=0}^{3} sin ε_{(x+j, x+j+1)}`. The only path is `(up, x) → (up, x+2) → (up, x+4)`,
    each leg contributing `(−i sin)(−i sin)`. This is nonzero, while `U[2w]` has range 2.
  - P6 checks both facts exactly on a ring of 10 with ten different angles. It also checks the uniform-clock trace
    mismatch: `tr Û(2ε)/2 − cos 2ω(ε) = 0.0162` at `ε = 1/3`, `k = 1/2`.
- (iii) **General.** Let a rule `w ↦ U[w]` on `ℓ²(ℤ; ℂ^N)` satisfy three conditions:
  - it has range `≤ R` for every field;
  - it is translation covariant;
  - each entry `⟨y|U[w]|x⟩` depends only on the clocks within a fixed distance of `x`, and continuously on them.

  Suppose that for every `c > 0`, every integer `a ≥ 1` and every `m = 2..M` (with `M = N(2R+2)`), the identity
  `U[w] T_a = T_a U[w]^m` holds for the field `w = c e^{gx}`, `g = (log m)/a`, on amplitudes supported near the
  origin. Then every uniform-clock step `U[c]` has flat bands and never moves a walker more than `(N−1)R` sites.

  *Proof.*
  - Taking matrix elements and using covariance gives `⟨y|U[m w]|x⟩ = ⟨y|U[w]^m|x⟩` for `x, y` near the origin.
  - As `a → ∞`, `w → c` and `m w → mc` uniformly on every bounded window.
  - The entries of `U[w]^m` near the origin are finite sums, over paths of length `m` and steps `≤ R`, of products
    of entries within `mR` of the origin. So both sides converge, and `U[mc] = U[c]^m` near the origin. By
    translation invariance this holds everywhere.
  - So `U[c]^m` has range `≤ R` for `m = 1..M`, and S5a applies. ∎

  **So:** a local, continuous unitary rule whose uniform-clock steps move packets (any non-flat band) violates the
  discrete identity at some integer ratio `m ≤ M` in some gradient. The partial-swap walk violates it already at
  `m = 2`, and satisfies it to relative `O(ε²)` (S3).

**ASSUMED:** nothing beyond the definitions quoted from block 54 and standard linear algebra: the Vandermonde
determinant, the diagonalizability of unitaries, and the continuity of polynomial coefficients.

## 3. Where the exact route stops

The first step that fails is the exact clock.
- No formulation of the clause as a local unitary rule, with a uniform range and continuous in the clocks, can make
  "the translate does `λ_a` steps per step" exact while moving packets (S5a, S6(iii)).
- For clocks given as a continuum, the same holds for eigenphase scaling (S5b).
- The positive result is the best one available of this kind. The partial-swap walk is unitary and local for every
  field, has the exact covariance half, and is a clock to relative `O(ε²)`. Its ray law is block 54's law plus an
  explicit `O(ε⁴)` term (S4).

What this attempt does **not** show:
- The 3D walk.
- The sideways drift `gT/(2k)` that block 54 measured and that no ray has.
- Any statement about fraction-of-ticks schedules beyond their unitarity. A tick schedule with bond angles in
  `{0, π/2}` is unitary tick by tick; S5a applies to its period-product only when the schedule is periodic.

## 4. What would finish it

1. **3D.** For each axis `j`, choose a basis `{a_j, b_j}` in which `σ_j = |a_j⟩⟨b_j| + |b_j⟩⟨a_j|`, and rotate on the
   pairs `{(a_j, x), (b_j, x+e_j)}` and `{(b_j, x), (a_j, x+e_j)}` with angle `ε0 √(w_x w_{x+e_j})`.
   - Each layer is unitary for every field, by S1(i).
   - The first-order generator is `Σ_j σ_j (T_j + T_j†)`. The gauge `ψ_x → i^{x_1+x_2+x_3} ψ_x` maps it to `2H`, block
     54's walk.
   - A palindromic order of the six layers is second-order accurate, so it is a clock to relative `O(ε²)`.
   - What is missing is its exact dispersion, its ray law, and a packet run in three dimensions.
2. **The sideways drift** in discrete steps. The `O(ε)` eigenvector term of S1(iv) is a natural place for a
   discrete correction to the drift.
3. **A referee of another model family** for S5 and S6(iii). They are general no-gos, so a hostile reading of the
   hypotheses (uniform range, continuity in the clocks, integer ratios) is the right test.

## 5. Running it

`python3 probes/work/derive/discrete-step-walk-under-the-clock-clause/w-macbookpro90c72-jf02d/check.py` prints
P1–P7, `TOTAL: PASS=7 FAIL=0`, the SUMMARY line and the HIT line. The output is 3.9 kB.
