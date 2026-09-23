# lightcone-uniqueness-region: derivation attempt 3 of 3

Worker `w-jonathonsmac4f50-je99d` (claude-opus-5-5), unit `J-derive-lightcone-uniqueness-region-a3`.

**Provenance, stated because it bears on independence.** The two prior attempts, a1
(`w-jonathonsmac4f50-j715c`) and a2 (`w-jonathonsmac4f50-j246a`), are claude-opus-5. That is my
model family (Claude Opus) in a different version, on the same machine.

I formed the route below before reading them: harmonic extension into the ball, Cauchy–Schwarz,
and a Dirichlet energy that is a quadratic form in the direction. It is not in a1 or a2. From them
I take only three things:
- the statement of the open step (a2's "directional lemma", a1's "once the directional lemma is complete");
- the fact that the perpendicular case `A(κ)/κ` and the value `1/3` at `V = 0` were already settled;
- their numbers, used once as a cross-check.

Where my S1 and S10 repeat a2's S1 and its TV ceiling, I prove them again here in my own words. A
referee should treat agreement with a1/a2 on those two points as same-family agreement.

**The object** (block 90, PR #8692, note
`ADMISSIBILITY_RULE_LIGHT_CONE_FORMATION_KEEPS_MEMORY_IN_3PLUS1_…_2026-09-23.md`, "The light-cone
clause"). Levels `t = 0, 1, …` are configurations of unit vectors `s_t(x)`, `x ∈ (Z/L)³`. The
record at `(t+1, x)` forms with density proportional to `e^{β s'·h}`, where
`h = Σ_{d∈N7} s_t(x+d)` and `N7 = {0, ±e_j}`. Records form independently over `x` given level `t`.
So each record is drawn from `μ_V`, `V = βh`. `μ_V` has density `p_V(s) = e^{V·s}/Z(|V|)` with
respect to area on `S²`. Write `κ = |V|`, `A(κ) = coth κ − 1/κ`, `m_V = E_V s = A(κ) V/κ`.

**Metric and influence.** `S²` carries the chordal metric `|s − s'|`, and "Lip" means 1-Lipschitz
for it. For a unit vector `u`, the influence in direction `u` at `V` is

  `‖D_u(V)‖ := sup_{f Lip} Cov_V(f, u·s)`,

which is the derivative of `V ↦ E_V f` in direction `u`, maximised over Lip `f`. The round-1
referee's point (the GIVEN) is that the Dobrushin/W1 influence of a predecessor is this quantity,
and that the covariance bound `‖Cov_V(s)‖ ≤ 1/3` does not control it.

## 1. Statement attempted

**(a) The directional lemma.** For every `V ∈ R³`, every unit `u` and every Lip `f`:

  `Cov_V(f, u·s) ≤ 1/3`,

with equality at `V = 0`, `f = u·s`. So the true influence constant of the vMF kernel is
`L := sup_{V,u} ‖D_u(V)‖ = 1/3` exactly. For `κ > 0` the bound is strict in every direction.

**(b) The regions for 7 predecessors.**
- **W1.** The light-cone chain contracts at rate `7β/3` and forgets its initial level for every
  `β < 3/7 = 0.428571…`. Its invariant law on each torus is unique. Since `L = 1/3` is attained,
  `3/7` is exactly where this method stops.
- **TV.** No total-variation Dobrushin argument reaches past `β = ln(4/3) = 0.287682…`, and block
  27's constant gives `√3/7 = 0.247436…`. The W1 region is the larger. It also contains a2's
  unconditional `β ≤ 3/10`.

**(c) Against the executed onset.** Block 90 brackets the onset of memory at `(0.55, 0.60)`. This
unit's statement quotes an earlier bracket, `(0.6, 0.75)`. The proved no-memory region ends at
`3/7 ≈ 0.4286`. The window `[3/7, 0.55]` is open on both sides.

## 2. Steps

**S1 (PROVED). Contraction in Lipschitz form.** This is the standard Dobrushin argument, written
out so the constant is visible.

Let `F` depend on finitely many records of one level. Define:
- `δ_x(F) := sup |F(τ) − F(τ')| / |τ_x − τ'_x|` over `τ, τ'` that differ only at `x`;
- `Δ(F) := Σ_x δ_x(F)`;
- the one-level operator `PF(σ) := ∫ F(τ) Π_x μ_{βh_x(σ)}(dτ_x)`.

Suppose that for Lip `g` and all `V, V'`,

  `|E_V g − E_{V'} g| ≤ L |V − V'|`. (★)

If `σ, σ'` differ only at `y`, then `h_x` changes only at the 7 sites `x` with `y ∈ x + N7`, and
there `|βh_x − βh'_x| = β|σ_y − σ'_y|`. Replace the product measure one affected factor at a time.
At each replacement the integrand, as a function of `τ_x` with the other coordinates frozen, has
Lipschitz constant `δ_x(F)`, so (★) applied to `g = τ_x ↦ F(…)/δ_x(F)` bounds the change by
`δ_x(F) L β|σ_y − σ'_y|`. Hence

  `δ_y(PF) ≤ βL Σ_{x: y ∈ x+N7} δ_x(F)`, and `Δ(PF) ≤ 7βL Δ(F)`.

Iterating, `Δ(P^t F) ≤ (7βL)^t Δ(F)`. Two conclusions follow.
- **Forgetting.** For any two initial levels `σ, σ'`, `|P^tF(σ) − P^tF(σ')| ≤ 2(7βL)^t Δ(F)`,
  since `P^tF` depends on finitely many initial records, changed one at a time, each by chord at
  most 2. In particular the memory from the aligned start, `m_t = E[s_t(x)·e]`, compared with its
  reflection, satisfies `m_t ≤ (7βL)^t`.
- **Uniqueness.** For invariant laws `π, π'` on the torus,
  `|π(F) − π'(F)| = |π(P^tF) − π'(P^tF)| → 0` whenever `7βL < 1`. The cylinder functions `F`
  determine the law.

**S2 (PROVED). (★) with `L = sup_{V,u} ‖D_u(V)‖`.** Let `V_t = V + t(V' − V)`. Then
`d/dt E_{V_t} g = Cov_{V_t}(g, (V' − V)·s) ≤ ‖D_{u}(V_t)‖ |V' − V|` with `u = (V' − V)/|V' − V|`.
Integrate over `t ∈ [0, 1]`. Differentiation under the integral is fine: `p_V` is smooth in `V` and
`S²` is compact.

**S3 (PROVED; ASSUMED: Green's first identity for a Lipschitz function against a smooth one on
the ball). The ball bound.** Fix `V` and `u`, and let

  `g(s) := p_V(s)(u·s − u·m_V)` on `S²`.

Then `∫_{S²} g dS = 0`, and for any `f`, `Cov_V(f, u·s) = ∫_{S²} f g dS`. Let `φ` be harmonic in
the open unit ball `B` with Neumann data `∂_nφ = g` on `S²`. It exists because `∫g = 0`, and it is
smooth on the closed ball because `g` is real-analytic (ASSUMED, standard).

For Lip `f`, set `F(x) := inf_{y∈S²} (f(y) + |x − y|)` for `x ∈ R³`. This is McShane's extension.
It is 1-Lipschitz on `R³` as an infimum of 1-Lipschitz functions, and it equals `f` on `S²`
because `f` is Lip. So `|∇F| ≤ 1` a.e. and

  `Cov_V(f, u·s) = ∫_{S²} F ∂_nφ dS = ∫_B ∇F·∇φ dx + ∫_B F Δφ dx = ∫_B ∇F·∇φ dx ≤ ∫_B |∇φ| dx.`

This is where the chordal metric matters: chord equals Euclidean distance in `R³`, so the extension
lives on the ball and mass may be moved through the interior. (The geodesic metric would give
`π/8 > 1/3` at `V = 0`.)

**S4 (PROVED; ASSUMED: the spherical-harmonic solution of the Neumann problem). Cauchy–Schwarz and
the energy.**

  `∫_B |∇φ| ≤ |B|^{1/2} (∫_B |∇φ|²)^{1/2}`, with `|B| = 4π/3`.

Write `g = Σ_{l≥1} g_l` in spherical harmonics (`g_0 = 0`). Then `φ = Σ_{l≥1} r^l g_l / l` up to a
constant, and the energy is

  `D := ∫_B |∇φ|² = ∫_{S²} φ g dS = Σ_{l≥1} ‖g_l‖²/l`

by orthogonality, with `‖·‖` the `L²(S², dS)` norm. So `Cov_V(f, u·s) ≤ (4πD/3)^{1/2}`, and it
suffices to show `D ≤ D₀ := 1/(12π)`, since `(4π/3 · 1/(12π))^{1/2} = 1/3` (CHECKED `E5.2`).

**S5 (PROVED; CHECKED `E2.3`). The mixed direction reduces to the two principal ones.** Take
`V = κe₃`, `κ > 0`. By rotation about `e₃`, write `u = cos α e₃ + sin α e` with `e ⊥ e₃`. Then:
- `g_u = cos α g_∥ + sin α g_⊥`, with `g_∥ = p_V(z)(z − A)` (a function of `z` alone, since
  `u·m_V = A cos α`) and `g_⊥ = p_V(z)(e·s) ∝ cos(azimuth − azimuth_e)`;
- the harmonic solutions are linear in the data: `φ_u = cos α φ_∥ + sin α φ_⊥`;
- `φ_∥` is axisymmetric and `φ_⊥` is a pure `cos` azimuthal mode, so `∫ φ_∥ g_⊥ = ∫ φ_⊥ g_∥ = 0`
  (the azimuthal integral of `cos` vanishes).

Hence

  `D(u) = cos²α D_∥ + sin²α D_⊥ ≤ max(D_∥, D_⊥)`.

Here the Hilbert structure of the energy does what the triangle inequality cannot. a2's bound
`|cos α|R + |sin α|A/κ` loses a factor `√2` at `κ → 0`. The quadratic form loses nothing.

**S6 (PROVED; CHECKED `E1`, `E2`, `E3.1`, `E3.2`). One harmonic is enough.** Since `1/l ≤ 1/2`
for `l ≥ 2`,

  `D ≤ ‖g_1‖² + (‖g‖² − ‖g_1‖²)/2 = (‖g‖² + ‖g_1‖²)/2 =: B`.

In closed form, with `c = κ/(4π sinh κ)` (so `p_V = c e^{κz}`), `I(a) := ∫_{−1}^{1} e^{az}(1−z²) dz = 4(a cosh a − sinh a)/a³`,
`J₂ := ∫ e^{2κz}(z−A)² dz`, and `J₁ := ∫ e^{κz}(z−A)z dz = 2 sinh κ/κ³ − 2/(κ sinh κ)`:
- `‖g_⊥‖² = πc² I(2κ)`, and the `l = 1` part of `g_⊥` is `(3cI(κ)/4)(e·s)`, so
  `B_⊥ = (πc²/2)(I(2κ) + (3/4) I(κ)²)`;
- `‖g_∥‖² = 2πc² J₂`, and the `l = 1` part of `g_∥` is `(3cJ₁/2) z`, so
  `B_∥ = πc²(J₂ + (3/2)J₁²)`.

Exact identities (`E3.1`, `E3.2`):

  `D₀ − B_⊥ = F_⊥/(96π sinh²κ)`, where `F_⊥ = 8 sinh²κ − 3κ²(I(2κ) + (3/4)I(κ)²)`;
  `D₀ − B_∥ = F_∥/(48π sinh²κ)`, where `F_∥ = 4 sinh²κ − 3κ²(J₂ + (3/2)J₁²)`.

**S7 (PROVED; CHECKED `E3.3`, `E3.4`, `E4`). `F_⊥ ≥ 0` and `F_∥ ≥ 0` for every `κ`.**
`κ⁴F_⊥ = G_⊥` and `κ⁴ sinh²κ F_∥ = G_∥` exactly, where

  `G_⊥ = κ⁴ cosh 2κ − 4κ⁴ + (3/2)κ³ sinh 2κ − 18κ² cosh 2κ − 18κ² + 36κ sinh 2κ − 18 cosh 2κ + 18`

and `G_∥` is the exponential polynomial (exponents `e^{nκ}`, `|n| ≤ 4`, powers `κ^m`, `m ≤ 7`)
assembled in `check.py` from `A = (κ cosh κ − sinh κ)/(κ sinh κ)`.

Both are even in `κ`. Every Taylor coefficient of both is `≥ 0`:
- exactly for all degrees `< 90`;
- for every even degree `j ≥ 60`, by a dominance argument. `c_j·j!/M^j` equals the polynomial
  `P_M(j) + P_{−M}(j)` plus terms of size `≤ ((M−2)/M)^j U(j)`. The shifted polynomial
  `P_M(J₀ + y) + P_{−M}(J₀ + y)` has nonnegative coefficients and is positive at `y = 0`. The
  geometric remainder decreases for `j ≥ J₀ = 60` and is already smaller at `J₀`. For `G_⊥` the
  remainder is empty.

The first nonzero terms are `(4/15)κ⁸` and `(16/15)κ¹⁰`. Hence `G_⊥, G_∥ > 0` for `κ ≠ 0`, and so
`B_⊥, B_∥ < D₀` for `κ > 0`. As `κ → 0` both tend to `D₀` (`E5.3`). The margin is thin near 0:
`(D₀ − B_⊥)/D₀ = κ²/30 + O(κ⁴)`, which matches the Legendre-series energies in `N1`.

**S8 (PROVED). The directional lemma.**
- For `κ > 0`, S3–S7 give `Cov_V(f, u·s) ≤ (4π/3 · max(B_∥, B_⊥))^{1/2} < 1/3` for every Lip `f`
  and unit `u`.
- At `V = 0`: `g = (u·s)/(4π)` is pure `l = 1`, so `φ = (u·x)/(4π)` and
  `∫_B|∇φ| = (4π/3)/(4π) = 1/3`.
- The linear `f = u·s` attains it: `E₀[(u·s)²] = 1/3` (`E5.1`).

So `L = 1/3` exactly.

**S9 (PROVED). The W1 region.** By S1, S2 and S8, `7βL = 7β/3`. For `β < 3/7` the light-cone chain
forgets its initial level at geometric rate `(7β/3)^t`, and its invariant law on every torus is
unique. Because `L` is attained, no choice of `f` or `V` sharpens this Dobrushin/W1 bound. `3/7` is
the method's exact edge.

**S10 (PROVED; CHECKED `E6`, `E7`). TV cannot reach as far.** The TV-Dobrushin influence of a
predecessor is `c_TV(β) := sup TV(μ_{βh}, μ_{βh'})` over `h, h'` differing in one of the seven
records.
- Six unit vectors can sum to 0 (three opposite pairs). With `s_y ∈ {e, −e}` this gives
  `c_TV(β) ≥ TV(μ_{βe}, μ_{−βe}) = tanh(β/2)` (`E6.1`).
- The Dobrushin sum `7c_TV(β) ≥ 7 tanh(β/2)` reaches 1 at `β = ln(4/3)` (`E6.2`: `tanh(ln(4/3)/2) = 1/7`).

Order of the constants (`E7`):

  `√3/7 (block 27's TV sensitivity) < ln(4/3) (TV ceiling) < 3/10 (a2, unconditional W1) < 3/7 (this attempt) < 0.55 (onset bracket).`

**S11 (c). Against the onset.**
- Executed onset: block 90 (W3 and the probes' scans) puts it in `(0.55, 0.60)`. The plateau
  halves from plane 32 to 48 at `0.55` and holds at `0.60`: `0.418, 0.411`.
- Proved no-memory region: `β < 3/7 = 0.4286`, which is `0.78` of the lower edge of the bracket.
  The earlier bracket in this unit's statement, `(0.6, 0.75)`, is consistent.
- Nothing proved here, and nothing executed, covers `[3/7, 0.55]`.

## 3. What is new, and what would finish the programme

- **New and exact.** The directional lemma (S3–S8) closes the step a1 and a2 left open. Their
  `3/7` "once the lemma holds" becomes unconditional. a1's antitone parallel plan and a2's
  `R(κ)` are no longer needed for the region; they remain as sharper descriptions of `‖D_∥‖`.
- **Beyond `3/7`.** Needs a tool other than single-site Dobrushin, because `L = 1/3` is attained at
  `V = 0` and so the constant cannot be improved. Candidates:
  - block Dobrushin over a level-plane patch;
  - T1 of block 90: the chain is reversible with respect to one layer of a bilayer Gibbs law. So
    uniqueness for the bilayer O(3) model (high-temperature or cluster expansion on the graph
    `Γ_L`) gives no-memory wherever it holds. On `Γ_L`, each vertex has 7 neighbours, the same `7`.
- **Checked vs assumed.** Every finite claim above is exact in `check.py`: sympy identities in
  `(κ, e^κ)`, and Fraction arithmetic for the Taylor coefficients and the constants. The ASSUMED
  analytic facts are:
  - Green's first identity for a Lipschitz function against a smooth harmonic one on the ball;
  - existence and smoothness of the Neumann solution, and its spherical-harmonic form.

  Sections `N1`, `N2` are numerical cross-checks only: Legendre-series energies, and a discretised
  optimal-transport LP in mixed directions, which gives `0.326`, `0.298` and `0.232`, all below `1/3`.

`SUMMARY: PROVED` (see `check.py`).
