# pinned-what-is-a-source, attempt 5 of 5 — a clean negative

Worker `w-jonathonsmac4f50-j7bb7` (`claude-opus-5`), unit `J-derive-pinned-what-is-a-source:a5`.

**Provenance.** No prior attempt existed at claim time. Two tools are **mine from earlier today**
and are reused rather than re-derived: the pinned-set capacity identity `c = M⁻¹1` (issues #8543,
#8544) and the orbit-reduced exact Green function (issue #8580). Blocks 39/40/41 are taken as the
unit states them. All same model family.

## 1. What is claimed

> **None of the four candidates sources the massless transverse mode additively.**
>
> | candidate | far field | additive in N? | channel |
> |---|---|---|---|
> | (a) one pinned record | `1/r` | — | transverse (massless) |
> | (b) `N` aligned pinned records | `1/r` | **no** — a capacity | transverse |
> | (c) a density excess | **none at linear order** | — | — |
> | (d) faster formation | `1/r` | **yes**, in `Q` | **density**, not transverse |
>
> **(a)** A record whose content is *held* does not add a term to the Goldstone action
> `(ρ_s/2)Σ_⟨xy⟩(θ_x−θ_y)²` — it **fixes** `θ` at its site. That is a **Dirichlet condition, not a
> source term**, so `θ(x) = θ₀G(x)/G(0)` and the strength is a **capacity** `1/G(0)`. Capacities
> do not add.
>
> **(b)** A jammed aligned cluster is then a conductor. Exactly, on the `L = 7` torus, with
> `C₁ = 5.140603`:
>
> | shape | N | capacity | ratio to `N·C₁` |
> |---|---|---|---|
> | line | 2 | 8.382103 | 0.815284 |
> | line | 3 | 11.528260 | 0.747530 |
> | line | 4 | 14.606007 | 0.710326 |
> | line | 5 | 17.564240 | 0.683353 |
> | 2×2×1 block | 4 | 13.224014 | **0.643116** |
> | 2×2×2 cube | 8 | 20.093365 | **0.488595** |
>
> Strictly sub-additive, monotonically falling in `N`, and **shape-dependent** — the `2×2×2` cube
> is far more screened than a line of the same `N`. That shape dependence is what a capacity has
> and a charge does not.
>
> **(c)** The transverse field *is* the content direction, and extra records **aligned** with the
> medium carry no transverse component. They change the local **stiffness**, entering as
> `∇·((ρ+δρ)∇θ) = 0` — a coefficient, not a right-hand side. Checked: substituting `θ ≡ 0`
> satisfies the modulated equation exactly and does **not** satisfy a genuinely sourced one. A
> density excess *refracts* an existing field; it does not create one.
>
> **(d)** This one **is** additive, and the unit's own setting says how: block 41's
> `d⟨n_x⟩/dt = κ(Δ⟨n⟩)_x + j_x` gives the stationary halo `G*(j−⟨j⟩)/κ`, whose strength is the
> **total excess production** `Q = Σ_x(j_x−⟨j⟩)` — additive over the region. But it lives in the
> **density** channel. Block 41's own result (4) is that the content field around a record is a
> number times its content vector: *the mass carries no charge in the long-range tilt channel.*
>
> **So the one additive source is in the wrong channel**, and the strength of the long-range
> potential in the lattice's own units cannot be computed from any of these four definitions. The
> memo's open gate — that the natural unit equals the Planck length — stays untestable by this
> route.

The pinned scale itself is verified on both menus: `c₀·⟨pair weight⟩ = 1` identically, giving
`c₀ = β/sinh β` (sphere) and `6/(p+q+4r)` (six axes).

## 2. The steps

1. **PROVED + CHECKED (`N1`).** Both `c₀`, via an explicit antiderivative checked by
   differentiation (not `integrate`, which returns a `Piecewise`).
2. **PROVED + CHECKED (`N2`).** The Dirichlet reading, and `C₁ = 1/G(0)` on tori of side 5, 6, 7.
3. **CHECKED (`N3`).** The capacity table above, exact rational arithmetic throughout.
4. **PROVED + CHECKED (`N4`).** The `θ ≡ 0` test separating a coefficient perturbation from a
   source.
5. **PROVED (`N5`).** The halo gradient, symbolically.

## 3. Where this stops

- **`N^{1/3}` is argued, not computed.** A conductor's capacity grows like its linear size, so a
  compact cluster of `N` records would have far field `~N^{1/3}`. The exact numbers here establish
  **sub-additivity and its shape dependence only**, on clusters small enough to fit a torus of
  side 7. The largest compact cluster I could fit is `2×2×2`.
- **A finite torus needs a mass.** I use `m² = 1/2` to make `(−Δ+m²)` invertible; the genuinely
  massless Goldstone case is the one the physics wants, and it is singular on a torus. The
  qualitative conclusions do not depend on the mass, but none of the printed numbers are
  massless-limit numbers.
- **(c) is linear order.** A density excess scatters at second order; I do not compute that, and I
  do not claim it produces no far field at any order — only that it does not *source* the massless
  mode linearly.
- **(d) is imported.** The halo `G*(j−⟨j⟩)/κ` is block 41's, quoted from the unit's own setting and
  not re-derived here; the coefficient "in terms of β, ρ and c₀" the unit asks for is therefore
  **not supplied** — I give the channel and the additivity, not the constant.
- **The ordered sphere-menu medium is assumed**, with a quadratic Goldstone action. That is the
  standard spin-wave reading and it is where the massless mode lives, but it is an assumption
  about the medium, not a derivation from the moving-records dynamics.

## 4. What would finish it

1. The coefficient in (d): carry `κ` and `ρ_s` through in terms of `β`, `ρ` and `c₀`, which is the
   one quantitative thing the unit asks for and the one thing I did not deliver.
2. A compact cluster large enough to test `N^{1/3}` — that needs a bigger torus and the sparse
   exact solve, not the orbit reduction used here.
3. The massless limit done properly, with a compensating background to kill the zero mode.
4. A fifth candidate, if one exists: everything here says the *content* channel admits only
   capacities and the *density* channel only production. If a source proportional to record count
   is wanted in the tilt channel, something outside these four must supply it.
5. Another model family — the whole chain, including the two tools reused from my own earlier work
   today.

## 5. Running it

```
python3 probes/work/derive/pinned-what-is-a-source/w-jonathonsmac4f50-j7bb7/check.py
```

`sympy` only; 22 checks, exact rational and symbolic arithmetic throughout. Runs in about a minute.
