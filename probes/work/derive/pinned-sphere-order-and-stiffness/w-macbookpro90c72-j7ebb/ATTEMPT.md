# The sphere menu with vacancies at the pinned scale: the kernel's positivity and the spin-wave stiffness

Attempt 3 of 5. Worker `w-macbookpro90c72-j7ebb`, model `claude-opus-5-5`. Script: `check.py` in this directory. It prints 5 checks, then a `SUMMARY` line and a `HIT` line.

**Provenance.**
- At claim time the tool printed the first sentence of attempt a4 (`w-jonathonsmac4f50-j7c7a`, claude-opus-5-5, same family, not refereed). In a previous unit I had also seen the first 25 lines of a4's `ATTEMPT.md`. So I knew its headline: the domination route (b)–(d) closes at `c₀` for the sphere menu.
- I did not re-attempt (b)–(d). This attempt takes the other parts: (a) exactly, and the stiffness (e) at leading order in `1/β`, with an exact first-order vacancy coefficient.
- **Overlap.** The `Z³` Green function code is reused from my `pinned-what-is-a-source:a3` (#8769).
- **Sources.** Blocks 39 and 40 (PRs #8530, #8546): the law with vacancies and the pinned scale. Block 19 (PR #8153): the full-lattice template.

## 1. Statement attempted

**(a)** On the one-site space "empty, or a unit vector" (any positive weights), the bond kernel

    B(∅, ·) = 1,    B(s, s') = c e^{βs·s'}

is positive semidefinite iff `c ≥ c₀ = β/sinh β`. At `c₀` it has rank one on the pair (empty, the constant function): an empty site is the uniform mixture of records. For two-valued contents (`±1`) the same holds with `c₀ = 1/cosh β`.

**(e)** Assume the spin-wave regime at large `β`: order along `n`, and Gaussian transverse fluctuations `π` weighted by `exp(−(β/2) Σ_{occupied bonds} |π_x − π_y|²)`. Then:
- The transverse structure factor of `σ_x = n_x s_x` has `1/E(k)` coefficient `ρ²/(β σ_eff) + O(1/β²)` per transverse component.
- `σ_eff` is the effective conductance of the occupied-bond network, relative to the full lattice.
- Near full occupancy, with vacancy density `ε = 1 − ρ`:

      σ_eff = 1 − a ε + O(ε²),    a = 2/(1 − G₀ + G(2,0,0)) = 2.5311,

  with `G` the `Z³` Green function of `−Δ`. So the coefficient is `(1/β)(1 + 0.5311 ε + O(ε²))`.

## 2. Steps

Each step is marked PROVED (argument given in full), CHECKED (verified by `check.py`, check named in brackets) or ASSUMED.

**S1 — PROVED and CHECKED [A1]. The sphere kernel.**
1. *Funk–Hecke.* `e^{βs·s'} = Σ_l (2l+1) i_l(β) P_l(s·s')`, with `i_l(β) = ½∫_{-1}^{1} e^{βt}P_l(t) dt`. Against `dΩ/4π`, the kernel acts on degree-`l` harmonics by the eigenvalue `i_l(β)`. Its series in `β` has non-negative coefficients (checked for `l = 1, 2, 3`) and it is positive for `β > 0`. Also `i_0 = sinh β/β`.
2. *Reduction to one block.* The empty state couples only to the constant function, so the kernel splits into:
   - the 2×2 block `[[1, 1], [1, c i_0]]` on (empty, constant), with determinant `c sinh β/β − 1`;
   - the multiplications by `c i_l > 0` for `l ≥ 1`.
3. *Positive weights.* A positive diagonal weighting (`z` on records, `1` on the empty state) conjugates the kernel and preserves semidefiniteness.
4. *Conclusion.* PSD iff `c ≥ c₀`. At `c₀` the block is `[[1,1],[1,1]]`, of rank one.

**S2 — CHECKED [A2]. Two-valued contents.** On (empty, +, −):
- the vector `(0, 1, −1)` has eigenvalue `2c sinh β`;
- the block on `span{e_∅, (e₊ + e₋)/√2}` has determinant `2c cosh β − 2`;
- at `c₀ = 1/cosh β` the determinant vanishes and a 2×2 minor does not, so the rank is 2.

**S3 — ASSUMED. The spin-wave regime.**
- `s = √(1 − π²) n + π`, so `s·s' = 1 − |π − π'|²/2 + O(π⁴)`.
- The measure is `dΩ = d²π (1 + O(π²))`.
- At leading order in `1/β` the transverse field is Gaussian on the occupied-bond network.
- The corrections from spin-wave interactions are `O(1/β²)` in the coefficient, and are not computed.
- The occupancies are taken homogeneous at density `ρ`.

**S4 — PROVED. The coefficient.**
1. Write `n_x π_x = ρ π̄_x + (n_x − ρ) π_x`, with `π̄` the long-wavelength field.
2. The second term has no `1/E(k)` singularity: it is a product of a short-range occupancy fluctuation and a field of variance `O(1/β)`.
3. At long wavelength the Gaussian weight on the random network is `(βσ_eff/2) Σ_bonds |∇π̄|²`. This is the definition of the effective conductance.
4. Hence `⟨|Σ_x π̄_x e^{ik·x}|²⟩ = N/(β σ_eff E(k))`, and the coefficient is `ρ²/(β σ_eff)`.
5. Check: for `ρ = 1`, `σ_eff = 1`, giving the full-lattice `1/β`.

**S5 — PROVED and CHECKED [V1, V2]. One vacancy.**
- *Setup.* Remove the site `0` and its six bonds `b`, with `a_b = δ₀ − δ_{y_b}`. Apply a unit field along `x₁` (`φ₀ = −x₁`).
- *Woodbury.* With `L = L₀ − AAᵀ`, the voltages across the removed bonds are `u = (I − AᵀGA)^{-1} u⁰`. Only the two bonds along `x₁` carry current. Their antisymmetric combination has `AᵀGA`-eigenvalue `G₀ − G(2,0,0)`, using `G₀ − G₁ = 1/6`, and the perpendicular bonds decouple by symmetry.
- *Power identity.* `ΔP = −Σ_b u⁰_b u_b = −2/(1 − G₀ + G(2,0,0))`.
- *Exact check on the 4³ torus* (twisted boundary, torus Green function with the zero mode removed, `G₀ − G₁ = (1 − 1/N)/6`): the dissipation falls from `64` to `7936/129`, which is exactly `64 − 2/(1 − (G₀ − G₂))` with `a_L = 320/129`.
- *On `Z³`.* `G₀ = 0.2527310099`, `G(2,0,0) = 0.0428893146`, so `a = 2.531138`. Six bonds removed independently would give `3`. The site's bonds are removed together, and only the two along the field carried current.

**S6 — PROVED. First order in the vacancy density.**
- At first order the vacancies are independent. `σ_eff = 1 − ε × (the power drop per vacancy per unit field, per site) = 1 − aε`.
- The per-site normalisation is right: every site has one bond along `x₁`, carrying power 1.
- *Annealed and quenched agree at this order.* In a homogeneous medium a single vacancy's free energy does not depend on its position, so its density is uniform, `ε`.

**S7 — CHECKED [V3]. The coefficient near full occupancy.** `ρ²/(β(1 − aε)) = (1/β)(1 + (a − 2)ε + O(ε²))`, and `a − 2 = 0.5311`. Vacancies thin the network faster than they thin the field.

## 3. Where the route stops

- **(b)–(d)** (twisted domination, the infrared bound, long-range order) are not attempted. a4 reports that the domination route closes at `c₀`. S1 shows why a naive split fails: the occupancy part `c^{n_x n_y}`, with `c₀ < 1`, is not PSD on its own, and the combined kernel is PSD only by its rank-one balance.
- **(e) beyond first order in `ε`.** At large `β`, records in the ordered medium bind: each aligned occupied bond is worth `c₀e^β ≈ 2β`. So a homogeneous ordered phase at moderate `ρ` may give way to clumping (blocks 39 and 40, executed). `σ_eff(ρ)` there needs the occupancy law's correlations.
- **Corrections in `1/β`** from spin-wave interactions are not computed.

## 4. What would finish it

1. `σ_eff` at second order in `ε`, from vacancy pair correlations at `c₀` (block 40's loop factors enter here).
2. The `O(1/β)` correction to the coefficient, from the quartic term of `s·s'` and the measure.
3. Long-range order by a route other than domination. The rank-one structure at `c₀` suggests treating the empty state as a record of unknown content, a "records-only" reformulation. Whether that yields a bound is open.
