# growth-and-drag-against-attraction, attempt a3: the orbit spirals in self-similarly

**Provenance.** Written by Claude Opus 5.5 (`claude-opus-5-5`), worker `w-jonathonsmac4f50-j6227`, task
`J:derive:growth-and-drag-against-attraction:a3`.

The prior attempt a4 (`w-macbookpro90c72-j9059`, issue #8655) is by the **same model** on another machine, and it is
unrefereed. So this attempt is not independent of it. Blocks 44–48 were supervisor-run in the same family.

**Plan before and after reading a4.** a4 derived the model (a) and the timescale conditions (b)–(d). Its first "what would
finish it" item was open: the two-body motion with drag, growth and the `1/r²` wind together, which answers how many orbits
survive. This attempt solves that motion. It re-derives the pieces of a4's model it uses.

## 1. What is claimed

**The model** (a4's (a), restated):
- A transparent capturing body with momentum per record `p` drifts at `v = p/√3`, and `dp/dt = q₁(⟨s⟩_wind − p)`.
- The wind of body 1 drifts at `u_w = −Q₁/(4πρ(1−ρ)r²) r̂`, with `Q₁ = q₁N₁`.
- Body 1 grows, `N₁ = N₁₀e^{q₁t}`.

Hence, exactly within the model,

```
x'' = −q₁ x' − μ(t) x/|x|³,     μ(t) = q₁²N₁(t)/(4πρ(1−ρ)) = μ₀ e^{q₁t}.
```

This is a Kepler problem with linear drag at rate `q₁` and a central mass growing at the same rate `q₁`.

**The results.**
1. **Angular momentum.** For every orbit, the angular momentum per record is `L₀e^{−q₁t}`, exactly. The growth of body 1
   does not enter, and no orbit is stationary.
2. **The spiral.** In the adiabatic regime `ε = q₁T₀ ≪ 1`:
   - a near-circular orbit spirals in as `r = r₀e^{−3q₁t}`. Two thirds of the rate come from the drag on `L`, one third
     from the growth of the centre;
   - its period falls as `T₀e^{−5q₁t}`;
   - it completes `((r₀/r)^{5/3} − 1)/(5ε)` turns on its way to radius `r`, which is **`0.435/ε` turns per halving of its
     radius**.
   - `ε² = 16π³ρ(1−ρ)r₀³/N₁`, so `ε ≪ 1` is exactly a4's orbit condition.
3. **Eccentricity is kept.**
   - The eccentricity vector obeys `de/dt = −3q₁(e + r̂)` exactly.
   - Its secular change vanishes, because the Kepler time average of `r̂` is `−e`.
   - So eccentric orbits shrink **self-similarly**, as `a₀e^{−3q₁t}` with `e` unchanged.
4. **The carried regime** (`ε ≫ 1`, the body moving with the wind): `r³ = r₀³ − (3μ₀/q₁²)(e^{q₁t} − 1)`, exactly. The body
   reaches the centre at `t_c = ln(1 + q₁²r₀³/(3μ₀))/q₁`, radially, with no orbit.
5. **Integrations agree.** For `ε = 0.01` and `0.03`:
   - the turns to half radius are 43.49 and 14.49, against the adiabatic 43.50 and 14.50;
   - the radius tracks `e^{−3q₁t}` to 0.01%;
   - eccentric orbits (`e₀ = 0.2, 0.5`) keep `e` to 0.0001 and `a·e^{3q₁t}` to 0.0001 after one e-fold;
   - at `ε = 1` not one turn is completed.

**What this does to the unit's (b)–(d).**
- "A bound orbit survives many periods" is true only as a spiral. The orbit is always bound, and increasingly so. It keeps
  its shape, completes `0.435/ε` turns per halving of its radius, and never settles.
- The pull on a circling test body grows as `N₁N₂/r² ∝ e^{q₁t}e^{q₁t}e^{6q₁t} = e^{8q₁t}`.

## 2. Steps

1. **ASSUMED — the model.** a4's (a), as restated above, re-derived at the level used:
   - the drift `s/√3` of a record;
   - the capture weighting;
   - the wind law and `q₁` established in the unit;
   - the free-streaming regime;
   - a heavy central body. The test body's pull on body 1 is not included.

2. **PROVED / CHECKED (E1).** `d(x × v)/dt = x × a`, and the central term drops, leaving `−q₁ x × v` (sympy, symbolic).

3. **PROVED / CHECKED (E2).**
   - The adiabatic circular orbit at the current `L` and `μ` has `r = L²/μ`. With `L = L₀e^{−q₁t}` and `μ = μ₀e^{q₁t}`,
     that gives `r₀e^{−3q₁t}`.
   - Then `T = 2πr^{3/2}μ^{−1/2} = T₀e^{−5q₁t}`, and `∫dt/T = (e^{5q₁t} − 1)/(5q₁T₀)`.
   - In the unit's variables, `(q₁T₀)² = 16π³ρ(1−ρ)r₀³/N₁`.

   All of this is sympy.

4. **PROVED / CHECKED (E3).** The carried regime has `v = u_w`, so `dr/dt = −μ₀e^{q₁t}/(q₁r²)`. Integrate `d(r³)/dt` directly
   (sympy `dsolve`).

5. **PROVED / CHECKED (E4).**
   - With `A = v × L − μr̂`, the Kepler identity `−(μ/r³) r × L = μ dr̂/dt` gives `dA/dt = −2q₁A − 3q₁μr̂` (the extra `μ̇r̂`
     term enters here). Hence `de/dt = −3q₁(e + r̂)` for `e = A/μ` (sympy, component by component).
   - `⟨cos f⟩_t = −e` over a Kepler ellipse (checked numerically to `10⁻¹⁶` at three values of `e`). So the orbit average of
     `de/dt` is zero to first order in `ε`.

6. **NUMERICAL (N1).**
   - The runs use `solve_ivp` with `rtol = 10⁻¹⁰`, in units `a₀ = μ₀ = 1`.
   - They start at pericentre with the adiabatic radial drift `−3q₁r` added, which removes the forced epicycle. Without it,
     the radius oscillates about the spiral with relative amplitude about `3ε/(2π)`.
   - `L` follows `L₀e^{−q₁t}` to `10⁻⁷` in every run.

## 3. Where the route stops

- **What the model includes.** It is a4's free-streaming, heavy-centre model. The test body's own wind and its pull on body 1
  are not included, and neither is depletion of the gas around a growing body. With depletion, `q₁` falls, and so does the
  common rate that makes the spiral self-similar.
- **The adiabatic results are first order in `ε`.** The integrations show the corrections: 2% in the turn count at
  `ε = 0.3`, and 13% at `ε = 1`.
- **No simulator run.** None of this is checked against `inertial_bodies.py`.

## 4. What would finish it

1. **Different rates.** Let the capture rate of the test body differ from the growth rate of the centre (a body in balance,
   block 49). The exponents become `r ∝ e^{−(2γ + g)t}` for drag `γ` and growth `g`, which should be checked the same way.
2. **Depletion.** A growing body's `q₁` should fall as the gas around it thins, so derive the rate from the gas. The spiral
   then need not be self-similar.
3. **A simulator run.** Put a free test body on a near-circular orbit with block 48's simulator and measure the turns per
   halving against `0.435/ε`.
4. **A referee from another model family.**

## 5. Running it

```
python3 probes/work/derive/growth-and-drag-against-attraction/w-jonathonsmac4f50-j6227/check.py
```

It needs `numpy`, `scipy` and `sympy`. It runs 5 checks (E1–E4, N1) in about 5 seconds.
