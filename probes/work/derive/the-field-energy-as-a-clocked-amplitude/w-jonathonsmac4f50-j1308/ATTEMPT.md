# the-field-energy-as-a-clocked-amplitude, attempt 1 of 3: an exact rewriting, a background that cannot hold the energy, and a sea that can on a line

Worker `w-jonathonsmac4f50-j1308` (`claude-opus-5-5`), unit `J-derive-the-field-energy-as-a-clocked-amplitude:a1`.

**Provenance.** There were no prior attempts. Blocks 53–56 and 76 (open PRs; same model family as me) supply the objects. Part
(c) is the one-dimensional counterpart of block 76's three-dimensional sea computation, done with my own code.

## 1. What is claimed

**Setting.**
- `Λ` is the lattice Laplacian: `(Λv)_x = Σ_{y∼x}(v_x − v_y)`, so `⟨v, Λv⟩ = Σ_bonds(v_x − v_y)²`.
- Rates are `w = φ²`. Block 56's simplest member is `F = c Σ_bonds(φ_x − φ_y)²`.

> **(a) (exact).** `c Σ_bonds(φ_x − φ_y)² = ⟨ξ| φ(cΛ)φ |ξ⟩` with `ξ ≡ 1`. The field's energy is the clocked energy of a uniform
> background under the rate-independent, positive semidefinite generator `cΛ`.
>
> **(b) (exact): not a structure unless a clause pins the background.**
> - `φΛφ(1/φ) = φΛ1 = 0`, and `⟨ξ|φΛφ|ξ⟩ = Σ_bonds(φ_xξ_x − φ_yξ_y)² ≥ 0`, with equality exactly when `φξ` is constant.
> - So the clocked background's stationary state near uniform, the only kind a static law can use, is `ξ ∝ 1/φ`, and it carries
>   **zero** energy.
> - Started uniform, `ξ` does not stay uniform (`dξ/dt = −icφΛφ1 ≠ 0`). It keeps the energy `F` only as the conserved value of a
>   non-stationary state.
> - With `ξ` free (real, small deviations), the field term depends on `θ = φξ − 1` alone. Stationarity in `ξ` makes `θ`
>   constant, so the field term vanishes and the rates' static law keeps only the source: there is no static solution for a
>   nonzero source.
> - **Block 56's static results are exactly the limit in which `ξ` is held uniform.** A supplied pinning `μΣ(ξ − 1)²` gives the
>   rates the stiffness `cμs/(cs + μ)` per mode (`s = |q|²_lat`). That is block 56's `cs` at long wavelength and a mass `μ` at
>   short wavelength.
>
> **(c) (numeric, on a ring): the filled-sea reading, with what is filled stated.**
> - **A chiral sea**, the walk `σ_x ⊗ S` with every negative mode filled. The volume term is `c₀ = −2/π`. Beyond it, the rates'
>   second variation is `g(q)(1 − cos q)` with `g = (1/(6π))(1 − 1/m²)` at `q = 2πm/N`.
>   - This holds to `2·10⁻³` for `m = 2..6` at `N = 512`, and to `5·10⁻⁴` at `N = 256–1024` in the control. `m = 1` gives zero,
>     within rounding.
>   - At long wavelength on an infinite line this is `c Σ_bonds(u_x − u_y)²` with **`c = 1/(6π) > 0`**. That is the conformal
>     anomaly coefficient `c_CFT/(12π)` for the walk's two Dirac species (`c_CFT = 2`). The `(1 − 1/m²)` factor is the
>     finite-size Virasoro `m³ − m` structure; it is why `m = 1` vanishes.
>   - It is **not** a nearest-neighbour form: `g` grows to `0.0795` at `q = π`.
>   - So `c` is a computed number: `γ = 1/c = 6π` on a line, and block 76's `κ = 0.095`, `γ = 10.5` in three dimensions. That
>     holds only after the volume term is removed by normal ordering, which issue #8625 found to be a supplied clause, and only at
>     long wavelength.
> - **A non-chiral sea**, the ring Laplacian with its lower half filled. The Fermi level lies inside a band, so as `q → 0` the
>   second variation beyond the volume term tends to **`−1/(2π)`**: a mass term for the rates (a compressibility), not a gradient
>   term. Clause A forbids it. **So A itself restricts what may be filled:** only a sea at a chiral point avoids a mass term.
>
> **(d) What it adds.**
> - (a) is a rewriting.
> - (b) shows that reading the background as an amplitude with its own clocked motion *removes* the field energy, unless a
>   pinning clause is supplied, and a pinning clause is as much a supply as `F` itself.
> - Only the filled-sea reading adds content: a computed `γ`, at the price of supplied choices. Those are:
>   - which modes are filled (a chiral generator, filled to its chiral point, as A requires);
>   - the exchange sign;
>   - normal ordering.
>
>   Even then it gives block 56's member only at long wavelength.

## 2. The steps

1. **PROVED + CHECKED (A1).** `⟨1|φΛφ|1⟩ = ⟨φ, Λφ⟩ = Σ_bonds(φ_x − φ_y)²`. Checked exactly on the `3×3×3` torus with random
   positive rational rates. Also checked: the Gram identity for `Λ`, and `Λ1 = 0`.
2. **PROVED + CHECKED (B1): the zero mode.** `φΛφ(1/φ) = φΛ(1) = 0`, and the Gram form gives zero energy exactly when `φξ` is
   constant (connected graph). Checked exactly: the zero mode, its zero energy, and `dξ/dt(0) ≠ 0` for non-uniform rates.
   Energy conservation at fixed `φ` is the unitarity of `e^{−itφcΛφ}` (Hermitian generator).
3. **PROVED + CHECKED (B2, B3): the free and pinned backgrounds.**
   - `⟨ξ|φΛφ|ξ⟩ = c Σ(θ_x − θ_y)²` with `θ = φξ − 1 = ε + η + εη`. Stationarity in `η` gives `Λθ = 0`: a norm multiplier sums
     to zero against `Λ`'s constant null vector, so it must vanish.
   - The rates' equation is then the source alone.
   - Pinned: minimising `cs(ε + η)² + μη²` over `η` gives `cμs/(cs + μ)` (symbolic).
4. **NUMERIC (C1): the chiral sea.**
   - `E_sea[φ] = −Σ|eig(φSφ)|`, which covers both coin sectors of `σ_x ⊗ S`, with `φ = e^{u/2}` and `u = ε cos(qx)`, `ε = 10⁻⁴`.
   - `c₀ → −2/π` (`−0.636612` at `N = 512`).
   - `g·6π/(1 − 1/m²) = 0.9996, 1.0003, 1.0001, 1.0002` at `m = 2, 3, 4, 6`. At `m = 1` it is below 1 % of `m = 2`, which is
     rounding. `g(π) = 0.0796`.
   - The identification with `c_CFT/(12π)` is by the value and by the `m³ − m` structure. It is not proved.
5. **NUMERIC (C2): the non-chiral sea.** The half-filled ring Laplacian gives `(Π − c₀/4)·2π = −0.99999` at `m = 2`, `N = 512`.
   This is consistent with the Thomas–Fermi value `−ν E_F²/4` at `ν = 1/(2π)`, `E_F = 2`.
6. **Argued: (d).** Collects steps 1–5. The statement that clause A excludes non-chiral fillings follows from step 5 and the
   lane's reading of A as forbidding a mass term (row 1 of the decision record).

## 3. Where this stops

- **(c) is numeric and on a line.** The value `1/(6π)` and its conformal-anomaly reading are identified numerically (4 digits
  and the exact `m³ − m` pattern). Proving it would need the lattice polarisation in closed form.
- **Three dimensions** is block 76's executed `κ`. There is no closed form, and no conformal argument applies.
- **The background in (b) is one real amplitude with small deviations.** A complex `ξ`, or several backgrounds, would not
  change the zero mode `1/φ`, which is exact, but the dynamics were not worked out.
- **The sea readings carry block 76's imports:** the exchange sign, and a filled branch.

## 4. What would finish it

1. Closed forms for the chiral sea's polarisation on the line, proving `c = 1/(6π)` and the `(1 − 1/m²)` factor, and in three
   dimensions for `κ`.
2. The owner's decision whether the background is pinned (then (a) is only notation and `F` stays supplied) or is a filled chiral
   sea (then `γ` is computed, with normal ordering and the exchange sign supplied).
3. A referee from another model family.

## 5. Running it

```
python3 probes/work/derive/the-field-energy-as-a-clocked-amplitude/w-jonathonsmac4f50-j1308/check.py
```

It uses sympy and numpy, has 6 checks, and runs in about a second. A1–B3 are exact (fractions, sympy); C1 and C2 are labelled
`NUMERIC`.
