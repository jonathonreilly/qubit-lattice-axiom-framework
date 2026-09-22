# J:derive:growth-and-drag-against-attraction:a4 — w-macbookpro90c72-j9059

Attempt 4 of 4, by claude-opus-5-5 (all of `check.py` and this file). At claim time no other attempt existed on
`ai/probes` for this problem. `python3 check.py` prints 4 `ok` lines, exits 0 with `FAIL` empty, and runs in about 1 s.

What is exact and what is floating point:
- **Exact** (sympy): the sphere moments, the drift, the solutions of the equations of motion, the fall time and the
  coefficients.
- **Floating point, labelled:** one integration.

Nothing is adopted and no gravitational claim is made.

**Setting.** This is the unit's supplied clause, blocks 44–47:
- a record's content is its direction `s`;
- it steps to `x + e` with probability `max(0, s·e)/√3` for each of the six unit vectors `e`;
- a capturing site takes up records in proportion to `|s|₁`, at `q₁ = (√3/2)ρ` per tick;
- a body capturing `Q` per tick draws the wind `⟨s⟩_wind = √3Q/(4πr²ρ(1−ρ))`.

## 1. Statement attempted

**(a) Equations of motion.** Take a free transparent body of `N` capturing sites and momentum `P`, and write `p = P/N`.
- Its equations are `dN/dt = q₁N` and `dP/dt = q₁N⟨s⟩_wind`, hence `dp/dt = q₁(⟨s⟩_wind − p)`.
- Captured records carry exactly the wind's mean momentum. Over the uniform sphere, `⟨|s|₁⟩ = 3/2` and
  `⟨|s|₁ s_i s_j⟩ = δ_ij/2`. In a first-harmonic wind `(1 + 3u·s)/(4π)`, the `|s|₁`-weighted mean content of captured
  records is therefore `u = ⟨s⟩_wind`.
- **Velocity.** A record of content `s` drifts at `Σ_e e·max(0, s·e)/√3 = s/√3`, which is linear in `s`. A body is a
  lump of records whose mean content is `p`, so it drifts at `p/√3`. This is its centre of mass, and it is block 48's
  "streams as a record whose content is `P/M`".

**(b) Fall, orbit and the condition.** In the ballistic regime (`t ≪ 1/q₁`) the pull is `GM/r²`, with
`GM = q₁²N₁/(4πρ(1−ρ))`.
- The radial fall from rest takes `(π/2)√(r³/(2GM))`. It beats the growth-and-drag time `1/q₁` iff
  **`(4π/3)ρr³ ≪ 8N₁/(3π²(1−ρ))`**, i.e. `0.270N₁` at low density.
  - The supervisor's estimate is `N₁/6 = 0.167N₁`. The derived coefficient is 1.62 times larger.
  - It agrees with the value `8N₁/(3π²(1−ρ))` quoted for block 48 in the sister unit's established text
    (`collisionless-force-between-extended-bodies`).
- One circular period beats `1/q₁` iff `(4π/3)ρr³ ≪ N₁/(12π²(1−ρ))`, which is 32 times stricter.
- `n` periods need `n²` times more.

**(c) Long times.** Beyond `1/q₁` the body is entrained by the wind.
- In a steady wind, `p → ⟨s⟩_wind`, and the body moves with the wind.
- But a free capturing source grows at the same `q₁`, so the wind at a fixed point grows as `e^{q₁t}`. Then, exactly,
  `p = (w₀/2)e^{q₁t} + (p₀ − w₀/2)e^{−q₁t}`, and **`p/⟨s⟩_wind → 1/2`**: the body moves at half the local wind.
- For two free bodies, each is carried at half the other's wind. Their terminal relative velocity is therefore half the
  sum of the two winds, not the full wind speed the unit anticipates. Full entrainment needs a source that does not
  grow, for example a body in balance (block 49).

**(d) Growth.** `N(t) = N₀e^{q₁t}` in an unbounded uniform gas, so the force `K q₁²N₁N₂/r²` grows as `e^{2q₁t}` at fixed
`r`. That holds until the gas near the bodies is depleted, which these equations do not model.

## 2. Steps
1. **CHECKED:** `⟨|s|₁⟩ = 3/2` and `⟨|s|₁ s₁²⟩ = 1/2`, integrated over the first octant with the reflection symmetry.
   The off-diagonal moments vanish by the reflection `s_i → −s_i`, so `3⟨|s|₁s_is_j⟩/⟨|s|₁⟩ = δ_ij`, and the captured
   momentum equals `u`. **PROVED** from these.
2. **CHECKED:** the drift `s/√3`, exactly on vectors of every sign pattern including zeros. **PROVED:** per axis,
   `e_k max(0, s_k) − e_k max(0, −s_k) = e_k s_k`.
3. **PROVED; CHECKED:** the equations of motion and their exact solution in a constant wind. The momentum bookkeeping is
   `d(Np)/dt = q₁N⟨s⟩` and `(Np)(0) = N₀p₀`.
4. **PROVED; CHECKED:** the solution in a wind growing at `q₁`, and its limit `1/2`.
5. **PROVED; CHECKED** (all symbolic):
   - the pull `q₁⟨s⟩/√3 = GM/r²`;
   - the radial fall time `∫₀^{r₀} dr/√(2GM(1/r − 1/r₀)) = (π/2)√(r₀³/(2GM))`;
   - the thresholds `N₁ = (π³/2)ρ(1−ρ)r³` (fall) and `16π³ρ(1−ρ)r³` (orbit), whose ratio is 32.
6. **Floating point:** one integration in the entrained regime (`ρ = 0.3`, a growing source `N₁ = 50` at `r₀ = 30`, a
   test body from rest, `t = 3.1/q₁`).
   - The body carries `0.496` of the local wind, against the exact 1/2 up to `e^{−2q₁t}`.
   - `N₁` grew by `e^{q₁t}`.
   - The captures are booked exactly, to rounding.

**ASSUMED.**
- The wind law `⟨s⟩_wind = √3Q/(4πr²ρ(1−ρ))` and the capture rate `q₁`, both ESTABLISHED in the unit.
- The first-harmonic form of the wind at the body.
- The free-streaming regime: no collisions between the body's records and the gas beyond capture.

## 3. Where the route stops
- **The conditions in (b) are timescale comparisons** (`t_fall` or `T_orbit` against `1/q₁`). The factor `≪` is not
  sharpened into a probability of survival. The full motion with drag and growth together would be needed, for example
  the orbit's decay rate at small `q₁T`.
- **(c)'s half-wind result assumes both bodies grow at `q₁` in an unbounded gas.** Depletion around a growing body
  would slow its growth, and move the ratio from 1/2 towards 1.

## 4. What would finish it
- Integrating the two-body equations with drag, growth and the `1/r²` wind together, over the boundary
  `(4π/3)ρr³ ~ N₁/(12π²)`. That would measure how many orbits survive as a function of `N₁/(ρr³)`.
- A run of `inertial_bodies.py` with a free test body (block 48's simulator) to measure `p/⟨s⟩_wind` against `1/2`
  for a growing source and against `1` for a body in balance.
- Depletion: the gas's density near a growing body, and its effect on `q₁`.
