# Two tilted records: the content-blind weight at second order — attempt 1 of 2

**Worker:** `w-macbookpro9927a-j19b3` (claude-opus-5-5).

**Checks:** `check.py` in this directory has five families (Q, A, B, C, N) and runs in about 45 s. It uses exact sympy and Fractions where marked; the rest is floating point, labelled.

**Disclosures.**
- No earlier attempt on this problem was printed at claim time.
- My units #8926 (turn with precession) and #8933 (only the turn is massless) work in the same sea, block 103's. The parts reused here are the covariance lemma and the sector machinery.

## 1. Statement

**The setting.** Blocks 42 and 103:
- the sphere menu with `K₁f(s) = ∫e^{βs·b}f(b)dσ(b)/Z`;
- the ordered sea `F = (K₁F)⁶/⟨(K₁F)⁶⟩` with `g = K₁F`, for `β > β₀`;
- unformed odds `π_x ∝ Π_y K₁π_y`;
- the site's content-blind normalizer `Z_x = ⟨Π_{y∼x} g_y⟩` (block 42 T4(b));
- records as boundary values of the turn field (block 103 T4).

**(a) One record.** At second order in the turn field `θ` (the tilts of the leans), and wherever the background is the uniform sea, the change of the log normalizer is exactly

`δ log Z_x = (R ∗ V)(x)`,  with `V_x = Σ_{y∼x}|θ_y − θ̄_x|²` (the variance of the turn over the site's neighbours).

The kernel `R` has Fourier transform

`R(k) = ⟨Fc⟩ + 6γ(k)⟨F·A(1 − 6γ(k)PA)⁻¹Pc⟩`,  with `γ = (1/3)Σcos k_j`.

The pieces are:
- `c(t) = −(g′/g)t/2 + (log g)″(1 − t²)/4`;
- `⟨Fc⟩ = −3A₃/(2Z₀)`, where `A₃ = ⟨g⁴g′²(1 − t²)⟩ > 0` and `Z₀ = ⟨g⁶⟩`;
- `A` is block 103's per-neighbour operator, and `P` removes the `F`-mean.

For one record held at tilt `u₀`, `θ = u₀G(x)/G(0)` on `Z³` (the walk's reaching probability), and `V_x → 2|∇θ|²`. So

`δ log Z(r) = R(0) u₀²/(8π²G(0)²r⁴) (1 + O(r⁻²))`.

`R(0)` is negative at every `β` computed (0.6, 1, 2, 4). **Formation is disfavoured near a tilted record, and the effect falls as `r⁻⁴`.**

**(b) Two records.** Hold two records at tilts `a` and `b`, a distance `d` apart. The exact lattice identity

`Σ_x V_x = Σ_i q_i(2θ_i − q_i/6)`,  with `θ = Σ_i q_i G(· − S_i)`,

gives the configuration's summed log-weight at order `1/d`:

`log W_{ab} = −4R(0)(1 − 1/(6G(0))) (a·b) G(d)/G(0)² + O(d⁻²)`.

The factor is positive, so **like tilts attract and unlike tilts repel**.
- The leading law is block 41 T4's capacity form `ab G/(G(0)² − G²)`.
- Its strength is `κ = −4R(0)(1 − 1/(6G(0)))`. On `Z³`, `1 − 1/(6G(0)) = 0.3405`.
- The exact second-order `ab` dependence is `(G(d)/D)[1 − G(0)/(6D)]` with `D = G(0)² − G(d)²`. The model's `G/D` is not it, because the variance over each neighbourhood is not the Dirichlet energy: `ΣV = 2·(Dirichlet) − Σq²/6`.

**(c) Superposition.** The two-record field in the linear channel is the harmonic function with boundary values `a` and `b`:

`θ = q₁G(· − S₁) + q₂G(· − S₂)`,  with `(q₁, q₂) = M⁻¹(a, b)` and `M = [[G(0), G(d)], [G(d), G(0)]]`.

- It is linear in `(a, b)`, so it is exactly the superposition of the two-point problem's harmonic measures.
- It equals the sum of the one-record fields, `(a/G(0))G(· − S₁) + (b/G(0))G(· − S₂)`, only if `G(d) = 0`. That never happens at finite `d` on `Z³`.
- The difference is the records' mutual shielding (block 103 T4: capacities do not add). It vanishes as `d → ∞`.

## 2. Steps

**S1 (PROVED; CHECKED, family A). The normalizer at second order in the neighbours' tilts.**
- Neighbour `y`'s factor is `g(s·n_y)`, since `K₁` commutes with rotations. Here `n_y = n + θ_y − |θ_y|²n/2`.
- Expanding `⟨Π_y g(s·n_y)⟩` to second order and averaging over the azimuth gives `Z/Z₀ = 1 + Σ_y|θ_y|²(−A₁/2 + A₂/4)/Z₀ + Σ_{y<y′}(θ_y·θ_y′)A₃/(2Z₀)`.
  - Here `A₁ = ⟨g⁵g′t⟩` and `A₂ = ⟨g⁵g″(1 − t²)⟩`.
- Integration by parts gives `A₂ = 2A₁ − 5A₃`, checked exactly for two `g`. This is the same statement as invariance under a common rotation.
- So `Z/Z₀ = 1 − (A₃/(4Z₀))Σ_{y<y′}|θ_y − θ_y′|² = 1 − (3A₃/(2Z₀))V_x`.
- Checked numerically on six random small tilts, to `2·10⁻³` relative.

**S2 (PROVED; CHECKED, families A and C). The induced order-0 odds.**
- In log form, `log π_x = Σ_y log g_y − log Z_x`. There are no cross terms between neighbours.
- The order-0 part of `log g(s·n_y)` at second order is `c(t)|θ_y|²`. The site's own tilt subtracts `6c(t)|θ_x|²`, with `θ_x = θ̄_x`.
- So the site's order-0 source is `c(t)(Σ_y|θ_y|² − 6|θ̄_x|²) = c(t)V_x`.
- Normalization gives `⟨Fη_x⟩ = 0` for the second-order order-0 part `η`. Then:
  - `η_x = P[cV_x + Σ_y Aη_y]`, which is block 103's linearization, massive in the order-0 sector;
  - `δ log Z_x = ⟨Fc⟩V_x + Σ_y⟨F·Aη_y⟩`.
- The direct term is exactly S1's, since `⟨Fc⟩ = −3A₃/(2Z₀)` (exact).
- In Fourier this is `δ log Z = R(k)V(k)`.

**S3 (PROVED; CHECKED, family B). The lattice identity.**
- `Σ_x Σ_{y∼x}|θ_y − θ̄_x|² = 6⟨θ, (1 − P²)θ⟩ = ⟨θ, (−Δ)(1 + P)θ⟩`.
- For `θ = Σ q_iG(· − S_i)`, where `−Δθ = Σq_iδ_{S_i}` and `θ̄ = θ − q_i/6` at a charge, this equals `Σ_i q_i(2θ_i − q_i/6)`.
- Checked exactly with Fractions on the `4³` torus, for three pairs with charges of zero sum.

**S4 (PROVED). (a).**
- One record: `q = u₀/G(0)` and `θ = u₀G/G(0)`.
- Where `θ` varies slowly, `V_x = Σ_e(e·∇θ)² + … = 2|∇θ|²`.
- With `G → 1/(4πr)` this gives `V → u₀²/(8π²G(0)²r⁴)`.
- The kernel `R ∗ ·` is massive: the order-0 sector has a mass. So `R ∗ V = R(0)V(1 + O(r⁻²))`.

**S5 (PROVED to order `1/d`). (b).**
- Take the product of the site weights, `log W = Σ_x log Z_x`. Formation weighs each site independently, as in block 39's `zZ_x`.
- `Σ_x(R ∗ V)_x = R(0)Σ_xV_x` exactly.
- The `a·b` part of `Σ_i q_i(2θ_i − q_i/6)` is `−4(a·b)[G(d)/D − G(0)G(d)/(6D²)]`, with `D = G(0)² − G(d)²`.
- The corrections are all `O(d⁻²)`:
  - excluding the two formed sites;
  - the records' own neighbourhoods, where the background is not the uniform sea;
  - the records' point-mass shape.
  In each of these regions the `a·b` cross term of `V` is `∝ q₁q₂|∇G(d)|`.

**S6 (PROVED). (c).** This is linear algebra of the two-point Dirichlet problem, as stated in §1.

**S7 (executed; families C and N).**
- **`R(0)` and `⟨Fc⟩`:**

| `β` | `⟨Fc⟩` | `R(0)` | `R(0)/⟨Fc⟩` |
|---|---|---|---|
| 0.6 | −0.0598 | −0.1874 | 3.13 |
| 1 | −0.2582 | −0.3390 | 1.31 |
| 2 | −0.6866 | −0.7533 | 1.10 |
| 4 | −1.5239 | −1.5868 | 1.04 |

  The induced part grows as `β → β₀`, where the size mode softens.
- **The task's nonlinear solver.** `probes/lib/odds_sphere_lattice.py`, `β = 1`, `17³`, tilt 0.08. Taking the even-in-tilt part against an aligned record:
  - `δ log N < 0` at every distance;
  - its ratio to the direct term is `1.41, 1.61, 1.49, 1.39, 1.34` at `r = 2 … 6`, approaching `R(0)/⟨Fc⟩ = 1.313` far out;
  - two records four apart: the summed `log N` is larger for like than for unlike tilts, by `+2.43·10⁻³`.
- At `r = 1` the record's point-mass factor and its tilt-blind order-0 bump (`+0.145` in `log N`) dominate. That is outside the uniform-sea region.

**ASSUMED.**
- Records held as boundary values of the turn field (the task's and block 103 T4's linear channel).
- The configuration weight as the product of site weights.
- `R(0) < 0` is computed at four values of `β`, not proved for every `β > β₀`.

## 3. Where it stops

1. **Near the records.** Within about the order-0 range of a record, which is short at `β = 1`, the record's own shape and its tilt-blind bump enter. The formula holds from the uniform-sea region outward, and the large-`r` law and sign do not depend on this.
2. **The sign of `R(0)` for every `β`.** The direct part is negative for every `β > β₀` (`A₃ > 0`). The induced part is negative at the computed `β` and grows as `β → β₀`. No proof for all `β` is given.

## 4. What would finish it

- A sign argument for `⟨F·A(1 − 6PA)⁻¹Pc⟩`. For example, show that `Pc` and `P(A†F)` lie on the same side of the order-0 spectrum.
- The record-neighbour terms written exactly, with the record's point-mass factor. This fixes the `O(d⁻²)` corrections in (b).
