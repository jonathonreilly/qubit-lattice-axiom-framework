# the-level-ordered-response-kernel: derivation attempt 1 of 2

Worker `w-jonathonsmac4f50-j40ae` (claude-opus-5-5), unit `J-derive-the-level-ordered-response-kernel-a1`.

**Provenance.** No earlier attempt at this problem is on `ai/probes`. The plan is my own: read the gain-one kernel as the Green function of a walk with steps `{0, e₁, e₂, e₃}`, and sum the zero steps in closed form.

**Sources.**
- **Block 90** (PR #8692, note `…LIGHT_CONE_FORMATION_KEEPS_MEMORY_IN_3PLUS1…`, "The level-ordered clause"): the record at `(t+1, x)` forms from the records of level `t` at `x + d`, `d ∈ {0, −e₁, −e₂, −e₃}`.
- **Block 91** (PR #8696): the light-cone law's window `R̂_⊥(k) ≤ 1/E(k)`, `E(k) = 6 − 2Σ_j cos k_j`; its T4 comparator `θ' = (1 − E/7)θ + (A(7β)/7)h`, `A(κ) = coth κ − 1/κ`; and the probes' level-ordered ratios `0.918 … 1.060`, one above the upper bound.

Nothing is adopted.

## 1. Statement attempted

**(a) The gain-one kernel, exactly.** The linear theory is `θ'(x) = ¼Σ_d θ(x + d) + (source at 0)`. Its stationary response is `G = Σ_{n≥0} Pⁿδ`, with `P(k) = (1 + Σ_j e^{−ik_j})/4`, and

  `G(a, b, c) = (4/3) · L!/(a! b! c!) · 3^{−L}`  on the forward octant `a, b, c ≥ 0`, `L = a + b + c`,

and `G = 0` everywhere else. So:
- **The source is felt only downstream.** The kernel is a wake along `(1,1,1)`. It vanishes behind the source and on every point with a negative coordinate: `G(1,0,0) = 4/9`, `G(−1,0,0) = 0`.
- **On each level plane `L`**, `G` is `4/3` times the trinomial law with equal cells. Every level carries total response exactly `4/3`.
- **At large distance**: on the axis `G ≈ 2/(πr)`. Across it, a Gaussian of variance `L/3` in each transverse direction: `G ≈ (2√3/(πL)) exp(−3ρ²/(2L))`, with `ρ` the distance from the axis. Off the axis at a fixed angle `θ`, `G` decays like `exp(−(√3/2) r sin²θ/cos θ)`.
- **Against the inverse Laplacian.** The light-cone gain-one kernel is `7/E(k)`, which is `7/(4πr)` at large `r` in every direction. The level-ordered wake is `8/7` of that on the axis and exponentially small off it.
- **In Fourier**, `R(k) = 4/(3 − Σ_j e^{−ik_j})`. At small `k` this is `≈ 4/(i k·(1,1,1) + |k|²/2)`, so the drift dominates the diffusion.

**(b) Against the light-cone bound.**
- In the drift-free directions, where `Σ_j sin k_j = 0` (for example `k = (q, −q, 0)`), `3 − Σe^{−ik_j} = E(k)/2`. So the gain-one kernel is `8/E(k)`, against the light-cone law's `7/E(k)`.
- With the rule's gain, block 91 T4's model carried over is `θ' = Pθ + (A(4β)/4)h`. It answers `A(4β)/(3 − Σe^{−ik})`, which in those directions is `2A(4β)/E(k)`. This **exceeds the light-cone upper bound `1/E(k)` exactly when `A(4β) > 1/2`**, i.e. for `β > κ*/4 ≈ 0.45`, where `κ* ∈ (1.79, 1.81)`.
- The level-ordered chain is not reversible (block 90 T1), so no covariance or infrared bound constrains it. The one executed ratio above the bound (block 91) is consistent with this.
- That the *nonlinear* level-ordered response exceeds `1/E(k)` is **not proved here**. Only the linear model is exact.

## 2. Steps

**S1 (PROVED; CHECKED `E1`, `E2`). The kernel.**
- `G = Σ_n Pⁿδ` is the expected number of visits to `x` by the walk with steps `{0, e₁, e₂, e₃}`, each of probability `1/4`, started at 0.
- To reach `(a, b, c)` the walk takes exactly `a`, `b`, `c` steps along `e₁`, `e₂`, `e₃` and some number `j ≥ 0` of zero steps, in any order. So

  `G(a, b, c) = Σ_j (L + j)!/(a! b! c! j!) · 4^{−(L+j)} = (L!/(a! b! c!)) 4^{−L} Σ_j C(L+j, j) 4^{−j}`.

- `Σ_j C(L+j, j) x^j = (1 − x)^{−(L+1)}`. At `x = 1/4` this is `(4/3)^{L+1}`, which gives the formula.
- Steps never decrease a coordinate, so `G = 0` off the octant.
- Equivalently, `G = (4/3)δ + (1/3)Σ_j G(· − e_j)`. `E1.1` checks that the closed form solves this recursion at every octant point with `L ≤ 24`.

**S2 (PROVED; CHECKED `E3`). Levels and Fourier.** By the multinomial theorem,

  `Σ_{a+b+c=L} G(a,b,c) e^{−ik·x} = (4/3)(Σ_j e^{−ik_j}/3)^L`.

At `k = 0` this is `4/3` for every `L`. Summed over `L` it is a geometric series, equal to `4/(3 − Σe^{−ik}) = 1/(1 − P(k))` for `k ≠ 0`.

**S3 (PROVED; CHECKED `N1`, `N2`). The large-distance form.** This is the local central limit theorem for the trinomial with equal cells.
- The steps projected on the plane `Σx = L` have covariance `1/3` per transverse direction per step.
- The plane's lattice has area `√3` per point.
- So the probability at a point is `(3√3/(2πL)) exp(−3ρ²/(2L))`. Multiplying by `4/3` and using `r = L/√3` on the axis gives `2/(πr)`.

The local CLT is standard (ASSUMED at this scope). `N1` and `N2` confirm it numerically: the on-axis ratio is `0.99998` at `n = 10⁴`, and the cross-section is within `10⁻⁴` at `L = 9000`.

**S4 (PROVED; CHECKED `E4`). The comparison.**
- `1/(1 − P_lc) = 7/E(k)` for the light-cone past (`E4.1`), and `3 − Σe^{−ik_j} = E/2` on `k = (q, −q, 0)` (`E4.2`).
- The rule-gain model's stationary mean is `θ = (A(4β)/4)h/(1 − P)`, as in block 91 T4 with four predecessors.
- `A` increases with `κ`, and `A(1.79) < 1/2 < A(1.81)` (`E4.3`).

**Relation to block 35.** Block 35's heat kernel in level time is `Pⁿ(a,b,c) = n!/(a! b! c! (n−L)!) 4^{−n}` (`n ≥ L`). S1 is its sum over `n`: the stationary kernel is the time integral of the drifted heat kernel.

## 3. What would finish the problem

- **The nonlinear law's own response.** The gain-one model is linear. For the nonlinear rule, the wake should survive where the linear theory is a valid guide (small sources, the disordered side and weak order). Across the ordered side, a proof would need an irreversible-chain replacement for block 91's covariance identity.
- **The probes' ratios.** The executed `0.918 … 1.060` against the symmetric kernel are shell averages. The exact kernel predicts:
  - a phase in `R̂(k)` (imaginary part `∝ Σ sin k_j`), odd under `k → −k`, from the forward-backward asymmetry;
  - in the drift-free directions, a modulus `8/7` of the light-cone kernel's at gain one.

  Comparing the measured complex `R̂(k)` direction by direction with `4/(3 − Σe^{−ik})`, scaled by the rule's gain, is the executable test.
- **Physically**, the level-ordered past carries influence one way, along the level diagonal. Under it a held source does not produce an inverse-Laplacian kernel. The light-cone past is the one that does (block 91).

`SUMMARY: PROVED` for (a) exactly and for (b) at the level of the linear model (see `check.py`).
