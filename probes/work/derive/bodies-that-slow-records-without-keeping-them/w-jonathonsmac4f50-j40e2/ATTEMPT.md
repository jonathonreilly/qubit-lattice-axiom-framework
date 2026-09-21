# bodies-that-slow-records-without-keeping-them, attempt 2 of 4 — the slowing strength cancels

Worker `w-jonathonsmac4f50-j40e2` (`claude-opus-5`), unit
`J-derive-bodies-that-slow-records-without-keeping-them:a2`.

**Provenance.** No prior attempt existed at claim time. Blocks 48/49/51/52 are taken as the unit
states them and are same-family campaign work; I re-derive none of them, but I do check block 48's
shell constant.

## 1. What is claimed

> **(a) A slowing site casts a shadow in momentum flux and in nothing else.** With `h = h(x,s)`
> the fraction of the flux at `x` that came through the origin, the slowed population is denser by
> `1/κ` and carries `κ` times the content, and:
>
> | quantity | value | |
> |---|---|---|
> | density | `ρ(1 + h(1/κ − 1))` | **denser** |
> | number current | `ρv` | **unchanged** |
> | momentum density | `ρv` | **unchanged** |
> | momentum **current** | `ρv²(1 − h(1−κ))` | **short by `ρv²h(1−κ)`** |
>
> *(The number current and momentum density are the same sum here, because velocity is
> proportional to content in this model — one fact read twice, not two checks.)*
>
> That is exactly why such a body can pull without growing: block 49 ties attraction to growth
> through the **number** flux, and this clause leaves the number flux alone.
>
> **(b)** The push on a second slowing site is
> `F₂ = (1−κ₁)(1−κ₂) ρ ⟨m²⟩ h ×` block 48's geometric factor. It is **symmetric under exchanging
> the bodies** (checked by a simultaneous swap) and block 48's factor depends only on the
> separation, so **action and reaction are equal and opposite**. Neither body grows — a slowing
> site keeps no record by definition, so the capture rate is identically zero. The weight is
> `⟨m²⟩`, not `⟨m⟩`: the momentum current is quadratic in the content.
>
> **(c) And here is the result.** The run-down of the gas is **linear** in `u = 1−κ`
> (`τ = 1/(n_b σ ⟨m⟩ u)`) while the pull is **quadratic** (`F = u²ρ⟨m²⟩/r²`). But the approach
> time goes as the inverse *first* power, `t = √(Mr³/(ρ⟨m²⟩))/u`, so in the ratio
>
> ```
> (t/τ)²  =  M r³ n_b² σ² ⟨m⟩² / (ρ ⟨m²⟩)
> ```
>
> **`κ` has cancelled exactly.** The attraction is usable iff
>
> ```
> M r³ n_b² σ² ⟨m⟩²  <  ρ ⟨m²⟩        i.e.   r³ < ρ⟨m²⟩ / (M n_b² σ² ⟨m⟩²)
> ```
>
> — a bound set by the **density** of slowing sites and by the gas's `⟨m²⟩/⟨m⟩²`, and **not by how
> hard any one site slows**. Making the slowers gentler buys exactly as much life for the gas as
> it costs in pull.

**On block 48's shell constant.** The integral of the hitting probability over the simplex is
confirmed **the same at every site of a shell** — the substantive claim — at `n = 2, 3, 4`. On the
*value*: with the uniform **probability** measure on the simplex it is `2/((n+1)(n+2))`; with plain
**Lebesgue** measure it is `1/((n+1)(n+2))`, the form the unit quotes. Both are right; the
statement needs the measure named.

## 2. The steps

1. **CHECKED (`B1`).** Shell-constancy at `n = 2, 3, 4`, exact rational integration, and the
   measure convention pinned.
2. **PROVED + CHECKED (`B2`).** The four bookkeeping identities, symbolically.
3. **PROVED + CHECKED (`B3`).** The pair force and its exchange symmetry.
4. **PROVED + CHECKED (`B4`).** The run-down, the approach time, and `∂(t/τ)²/∂u = 0`.

## 3. Where this stops

- **The pair force is assembled, not derived from a kinetic calculation.** I take block 48's
  geometric factor as given and compute how the slowing clause rescales it (`(1−κ₁)(1−κ₂)⟨m²⟩`).
  A first-principles derivation of the angular integral for the *slowed* gas is not done, so the
  geometric factor's `|r|₁²/r²` structure and its large `1/r` corrections are inherited.
- **Independent records throughout** — no exchange, no scattering, as in block 48's collisionless
  regime. The whole shadow picture assumes records do not re-randomise between the two bodies,
  which is exactly what block 51's `γ` scattering would do.
- **(c) is a scaling argument.** `σ` (the slowing cross-section) is not derived, the approach time
  uses a free-fall estimate `t ~ √(rM/F)` rather than an integrated trajectory, and `M` is the
  body's inertia, which this clause does not say how to compute. The **cancellation of `κ` is
  exact given those scalings** and is the part I would defend; the prefactors are not.
- **The `1/κ` density law assumes a single passage.** A record crossing several slowing sites is
  denser by `1/κ^j`; the multi-passage bookkeeping is what (c)'s run-down uses, but I do not verify
  the stationary state of a gas that has passed many.

## 4. What would finish it

1. Derive the angular integral for the slowed gas directly, instead of rescaling block 48's — that
   would turn (b) from an assembly into a computation and would test the `⟨m²⟩` weight.
2. Put `σ` and `M` on a footing: a slowing site's cross-section and a body's inertia are both
   undefined in the clause as stated, and (c)'s inequality cannot be evaluated numerically without
   them.
3. Re-do (a) with scattering at rate `γ` switched on and see how far the shadow survives — block 51
   says the wind of a capturing body is not isotropic, and the same question applies here.
4. Another model family on the `κ` cancellation, which is the claim worth checking: it is a
   statement about how two exponents combine, and a slip in either would destroy it.

## 5. Running it

```
python3 probes/work/derive/bodies-that-slow-records-without-keeping-them/w-jonathonsmac4f50-j40e2/check.py
```

`sympy` only; 10 checks, exact symbolic and rational arithmetic. Runs in about half a minute.
