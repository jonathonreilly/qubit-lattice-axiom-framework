# J:derive:composite-bodies-rest-energy-without-a-larger-site-algebra:a4: binding gives a rest energy inside M₂(ℂ); in 3D a contact pair falls like everything else only when its coin triplet points across the gradient, and only as the binding grows; the exchange sign decides which pairs exist

**Provenance.**
- Worker `w-macbookpro90c72-j16c3`, model `claude-opus-5-5`, one session. Attempt 4 of 4.
- **The prior attempt.** The claim printed one: a3 (`w-jonathonsmac4f50-j8f94`, the **same model**, another machine, unrefereed).
  - a3 found the exact 1D contact dispersions, the 1D nearest-neighbour pairs, a numerical 3D ground pair with an inverted band, the timed translation identity, and executed falls.
- **My own plan, formed before reading a3:**
  - the 1D contact bound state from the two-body Green function;
  - the untimed case via Hellmann–Feynman (at rest all the energy is interaction energy).
- **After reading a3** I took a different route and do not build on it, since it is unrefereed:
  - the 3D channel structure exactly (singlet against triplet at `K = 0`);
  - exact moments `⟨A²⟩`, `⟨A⁴⟩` at every `K`, and the strong-binding series for each channel's rest energy and limiting speed;
  - which pairs exist for each exchange sign.
- The task's mandated checks (ring diagonalisation, a pair falling in a gradient) are redone independently.
- Definitions come from the task text, which restates blocks 53 and 54 (open PRs ail53 and ail54). Nothing is adopted. Parked entry 4 of `docs/repo/DEFERRED_DECISIONS.md` is neither touched nor raised.

## 1. The statement attempted

**Setting.**
- One walker: `H₁ = Σ_j σ_j D_j` on `Z³`, or `σ_z D` on `Z`, with `D = (i/2)(T − T†)`, `(Tψ)(x) = ψ(x − 1)` (symbol `sin k`).
- Two walkers: `H = H₁⊗1 + 1⊗H₁ + V δ_{x₁x₂}` (contact; `V < 0` binds).
- With total wave vector `K` and relative wave vector `q`, the kinetic term is `A(q; K) = h(K/2 + q)·σ¹ + h(K/2 − q)·σ²`, with `h = (sin k_j)`.
- Rate field: the timed generator is `Σ_i √w H_i √w + V w δ`; untimed, `V δ` is left bare.

**Claims.**

**(a) Bound states and energy functions.**
1. **1D.** Executed on a ring of 64, matching to `9·10⁻¹⁵`:
   - equal coins: `E = −√(V² + 4sin²(K/2))`, so `M = |V|` and `c = 1`, the walker's speed;
   - opposite coins: `E = −√(V² + 4cos²(K/2))`, inverted at rest.
2. **3D at rest, exactly (CHECKED C.chan).** The contact condition splits into:
   - a **singlet** channel, `1 = V I(E)`;
   - a **triplet** channel of three states, `1 = V(2/(3E) + I(E)/3)`;
   - with `I(E) = ⟨E/(E² − 4|h|²)⟩`.
3. **3D near rest, exactly to `O(V⁻²)` (CHECKED C.mom).** `⟨A⟩ = ⟨A³⟩ = 0` and `⟨A²⟩ = 3 − Σ_i cos K_i σ¹_iσ²_i` at every `K`. With `⟨A⁴⟩`:
   - **singlet:** `E² = V² + 12 − 24/V² − (1 − 8/V²)K²`, inverted, `c² = −1 + 8/V²`;
   - **triplet with its direction across the motion:** `E² = V² + 4 + 16/V² + (1 − 2/V²)K²`, so `c² = 1 − 2/V²`;
   - **triplet with its direction along the motion:** `E² = V² + 4 + 16/V² − (1 + 4/V²)K²`, inverted, `c² = −1 − 4/V²`.

   Here a triplet state's "direction" is the axis along which its coin pair has zero total spin component.
4. **Executed (32³ grid secular equation):**

   | `V` | singlet `c²` | triplet across | triplet along |
   |---|---|---|---|
   | −4 | −0.766 | +0.740 | −1.168 |
   | −6 | −0.852 | +0.916 | −1.096 |
   | −10 | −0.932 | +0.976 | −1.038 |
   | −20 | −0.981 | +0.995 | −1.010 |

   The series values are `(−0.980, +0.995, −1.010)` at `V = −20`.

**(b) The fall.**
- **Timed (CHECKED C.fall).** `H_w T = λ T H_w` holds exactly for the joint translation, so force = −(energy) × grad u for the pair, binding energy included. At ray level (ASSUMED, as in block 54) a pair at rest accelerates at `a = −g w² Hess_K(ε²/2) ĝ`.
- **The 3D triplet.** The Cartesian triplet states `T_j` are the eigen-channels at every `K` at leading order: `⟨A²⟩` is diagonal in them. Their direction is the lattice axis `e_j`. With a gradient along a lattice axis, `a = −g[c_⊥² ĝ + (c_∥² − c_⊥²)(e_j·ĝ)e_j]`, and at strong binding `a = −g(ĝ − 2(e_j·ĝ)e_j)` for any gradient direction.
  - It falls at `−c_⊥² g` when its direction is across the gradient. That tends to `−g` only as `|V|` grows (`c_⊥² = 1 − 2/V²`).
  - It falls up when its direction is along the gradient.
  - It is pushed sideways otherwise.
- **The singlet** falls up at every `V`.
- **Untimed.** The identity fails. The 1D equal-coin pair at rest has no kinetic energy (all its energy is `V`), so it does not fall.
- **Executed on a 90-site chain:**

  | pair | `a/g` |
  |---|---|
  | equal coins, timed | −0.99 |
  | equal coins, untimed | +0.00 |
  | opposite coins, timed | +1.00 (falls up) |

**(c) "Rest energy needs a larger site algebra".**
- **Binding supplies a rest energy inside `M₂(ℂ)`.** The single-walker obstruction does not reach pairs.
- **But the exchange sign decides which pairs exist (CHECKED C.stat):**
  - A contact term acts only on the amplitude at coincidence, where exchange acts on the coins alone.
  - **Antisymmetric walkers** bind only in the coin singlet (in 1D, opposite coins). That band is inverted at rest, so the pair **falls up**.
  - **Symmetric walkers** bind only in the triplet: in 1D, equal coins with `c = 1`, and the inverted opposite-coin combination.
  - Under the Record axiom's one record per site (block 78's reading), the contact term acts on nothing.
- So a composite that falls like everything else needs all of the following:
  1. an interaction clause;
  2. that interaction timed by the local clock;
  3. symmetric composition;
  4. in 3D, a triplet across the gradient and strong binding.

  Items 1 and 2 are not in the axioms. For item 3 the axioms fix no exchange sign (block 78, the fork probe).

## 2. Steps

**S1 (ASSUMED: the setting).**
- **Supplied pieces.** Block 54's walk and clause, the contact interaction, and the ray limit for accelerations at rest.
- **The walkers.** Distinguishable unless an exchange sign is stated.
- **Timing.** A timed contact term is weighted by `w(x)` at its site.

**S2 (PROVED; floating check). 1D K blocks.**
- Write `Ψ(x₁, x₂) = e^{iKx₂}φ(x₁ − x₂)`. Then the block is `(H_Kφ)(r) = s₁(i/2)(φ(r−1) − φ(r+1)) + s₂(i/2)(e^{−iK}φ(r+1) − e^{iK}φ(r−1)) + Vδ_{r0}φ(0)`.
- **The contact bound state.** `φ(q) ∝ 1/(E − ε(q))` with `ε = 2 sin(K/2)cos q` (equal coins) or `2cos(K/2) sin q` (opposite). The condition is `1 = V(1/2π)∫dq/(E − ε)`.
- **The integral.** Residues give `(1/2π)∫dq/(a − 2b cos q) = sign(a)/√(a² − 4b²)` for `|a| > 2|b|`. Hence `E² = V² + 4b²`.
- **Exchange.** For equal coins, exchange is `(Xφ)(r) = e^{iKr}φ(−r)`.
- **Executed on a ring of 64:**
  - every `K` block's lowest level matches the closed forms to `9·10⁻¹⁵`;
  - the blocks are Hermitian and `X` commutes with the equal-coin block to `4·10⁻¹⁴`;
  - on the antisymmetric subspace `(1 − X)/2` no level leaves the continuum.

**S3 (PROVED; CHECKED C.chan). 3D at `K = 0`.**
- **The kinetic operator.** `h(−q) = −h(q)`, so `A = h·(σ¹ − σ²)`. Its eigenvalues on the two coins are `±2|h|` (the combinations `(|S⟩ ± |T_n⟩)/√2`) and `0` twice (the two Cartesian triplet states whose direction is perpendicular to `n = h/|h|`; `T_n` is the one whose direction is `n`).
- **The resolvent in the singlet/triplet basis** (sympy, symbolic `h`):
  - `⟨S|(E − A)⁻¹|S⟩ = E/(E² − 4|h|²)`;
  - the triplet block is `(1 − nnᵀ)/E + nnᵀ E/(E² − 4|h|²)`;
  - `⟨S|(E − A)⁻¹|T⟩` is odd in `h`, so it averages to zero under `q → −q`.
- **The average.** `|h(q)|` is invariant under `q_i → −q_i` and under permutations, so `⟨h_ih_j f(|h|)⟩ = δ_ij⟨|h|²f⟩/3`. Hence `G = I(E)|S⟩⟨S| + (2/(3E) + I(E)/3)·1_T`.

**S4 (PROVED; CHECKED C.mom). Moments and the strong-binding series.**
- **The moments.** `G(E, K) = Σ_n M_n/E^{n+1}`, with `M_n = ⟨A(q; K)^n⟩_q`. These are computed exactly as constant terms of Laurent polynomials in `e^{iq_j}` and `e^{iK_j/2}`.
- **Odd moments vanish.** Every factor of `A` carries frequency `±1` in exactly one `q_j`, so an odd product cannot have zero total frequency: `M₁ = M₃ = 0`.
- **The second moment.** `M₂ = 3 − Σ_i cos K_i σ¹_iσ²_i`. On the singlet `σ¹_iσ²_i = −1`. On the Cartesian triplet state `T_j` it is `−1` for `i = j` and `+1` otherwise.
- **Decoupling.** For motion along `z`, `M₂` and `M₄` are diagonal in `{S, T_x, T_y, T_z}`. So up to `O(V⁻³)` each channel obeys the scalar condition `E = V Σ m_n/E^n`, giving `E = V + m₂/V + (m₄ − 2m₂²)/V³ + …` and `E² = V² + 2m₂ + (2m₄ − 3m₂²)/V² + …`.
- **The coefficients** of §1(a)3 follow by expanding in `κ`. Mixing enters through off-diagonal `M₄` elements only at higher order; for motion along an axis those elements vanish exactly.
- **Executed.** The grid secular equation `det(1 − V G) = 0` (4×4 `G` over a 32³ grid, which converges exponentially off the continuum) gives §1(a)4. It approaches the series as `|V|` grows.

**S5 (PROVED; CHECKED C.fall). The timed identity.**
- `√w_x = λ^x` makes each timed hop's amplitude pick up `λ²` under the joint translation, and the timed contact term picks up the same `λ²`. So `H_w T = λ² T H_w` on the interior. It is checked exactly with `w = 4^x` on a 7-site chain, both coin sectors.
- Untimed, the contact term breaks it.
- **The consequence** (block 54's argument, ASSUMED): `d⟨K⟩/dt = −g⟨H_w⟩`. At ray level, `E(X, K) = w(X)ε(K)` gives `a = −g w² Hess(ε²/2)ĝ` at a band extremum.

**S6 (PROVED; CHECKED C.stat). The exchange sign.**
- A contact term multiplies the amplitude at `x₁ = x₂`. There, exchange of the two walkers acts on the coins alone: the swap has eigenvalue `−1` on the singlet and `+1` on the triplet.
- So antisymmetric walkers have a nonzero amplitude at coincidence only in the coin singlet, and symmetric walkers only in the triplet. A channel with zero amplitude at coincidence does not feel `V`.
- **In 1D** (coins conserved):
  - the singlet is the opposite-coin antisymmetric combination;
  - the triplet contains the equal-coin states and the opposite-coin symmetric combination.
- **Under one record per site** no amplitude sits at coincidence, so `Vδ` is identically zero on that space.

**S7 (EXECUTED, floating point). A pair falling in a gradient.**
- **Setup.** A 90-site chain in `w = e^{0.004x}`. The pair starts at rest: the `K = 0` bound profile in `r` times a Gaussian of width 7 in the centre. It is evolved by `expm_multiply`, and `⟨X⟩(t)` is fitted to a quadratic over `t ≤ 24`.
- **Results, `a/g`:**
  - equal coins, timed: `−0.987`;
  - equal coins, untimed: `+0.002`;
  - opposite coins, timed: `+1.000`.

## 3. The first failing step

None for the claims made. The limits:
1. **The ray limit is assumed.**
2. **The 3D series** stops at `O(V⁻²)`, with the finite-`V` values executed on a grid.
3. **Nearest-neighbour binding** is not treated in 3D. Under one record per site it is the only binding left.

## 4. What would finish it

1. **Nearest-neighbour binding under exclusion, in 3D:** the channel split and the limiting speeds.
2. **An exact finite-`V` expression for `c²`**, from the `K²` term of `det(1 − V G(E, K))`, in lattice integrals.
3. **The fall of a triplet pair**, executed in 3D. Direction-dependent falls and sideways pushes are predicted.

## 5. Running it

```
python3 probes/work/derive/composite-bodies-rest-energy-without-a-larger-site-algebra/w-macbookpro90c72-j16c3/check.py
```

The run takes about 15 s. It prints four exact checks, then three floating-point notes, then the SUMMARY and HIT lines.
