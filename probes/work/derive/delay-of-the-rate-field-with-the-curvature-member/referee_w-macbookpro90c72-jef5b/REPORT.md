# Referee report: J:derive:delay-of-the-rate-field-with-the-curvature-member:a2

- **Author:** `w-macbookpro9927a-j6a3f` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-jef5b` (`grok-4.6`). Different model family.
- **Target:** the clock law of block 62's curvature member has no retarded part, and a ledger-kept formation event still moves a distant packet at once and leaves a `1/r` memory.
- **Checks:** the `7×7` pencil rebuilt from `R₁`, `R₂` and the kinetic term, and the continuum kernels. The author's script is not called. The `96³` box was not rebuilt.

## The statement that survives

For `p ≠ 0`, `α ≠ 0` and `α + β ≠ 0`,

`u/e = −1/(4K w̄ p²) + C s²/p⁴`, `C = α(α + 3β)/(K² w̄³ (α + β))`.

The right-hand side is a polynomial in `s`. The clock at label time `t` is a combination of `e(t)` and `ë(t)`, with no retarded piece.

A ledger-kept event keeps the monopole and jumps the dipole by `D`. At large `r` the Poisson part of the clock changes by `−(D·r̂)/(16π K w̄ r²)`, a force of order `r⁻³`. The `C` term leaves every slow packet permanently displaced by

`Δx = −(E C/m*)(ΔD − (ΔD·r̂) r̂)/(8π r)`,

transverse to `r̂` and falling as `1/r`. That displacement is linear in the energy carried by `D`, and it is carried by `u` at the same label time, before any transverse traceless wave.

## Steps

**1.** The variables are the six strains and `u`. The kinetic term has no `u̇`, so `M` has a zero `u` row. The potential is `F₂ = −K w̄ (u R₁ + R₂)` with the quoted quadratic members. The Euler–Lagrange pencil `(s² M + V) x = −e ê_u` was solved over `Q(s)` at four rational `(p, α, β, K, w̄)` points and with every parameter symbolic on the axis `p = P ẑ`. The `u` component matches the stated transfer function, and the denominator does not depend on `s`.

**2.** A Cayley rotation built from a rational antisymmetric matrix is a rotation (`QᵀQ = I`, `det Q = 1`). `R₁`, `R₂` and both kinetic invariants are unchanged when `p → Qp` and `h → Q h Qᵀ`. The axis computation therefore covers every `p`.

**3.** Away from the origin, `G = 1/(4π r)` is harmonic and `Δ(−r/(8π)) = −G`. A pure dipole convolves to `−D·∇` of the kernel: `(D·r̂)/(4π r²)` for `G` and `(D·r̂)/(8π)` for `B`. The Hessian of `B` is `−(I − r̂ r̂)/(8π r)`. Multiplying the Poisson kernel by `−1/(4 K w̄)` produces the stated clock jump `−(D·r̂)/(16π K w̄ r²)`. The gradient of the `B` dipole is the stated transverse `1/r` memory.

**4.** The `96³` periodic control (values `0.840`, `0.768`, `0.698`, intercept `0.981`) was not rebuilt. The continuum identities above do not use it.

## Verdict

The partial result survives for ledger-kept events at first order. The clock is not retarded. The instantaneous dipole force and the `1/r` memory are the continuum kernels of that transfer function. Second order, moving bodies, and the singular branch `α + β = 0` stay outside the claim.
