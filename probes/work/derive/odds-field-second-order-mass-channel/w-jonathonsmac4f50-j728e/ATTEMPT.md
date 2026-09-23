# odds-field-second-order-mass-channel, attempt 1 of 4

**The content-blind interaction is the normalizer's second order, exactly. Content couples at first order. No covariant clause makes mass first order.**

Worker `w-jonathonsmac4f50-j728e` (`claude-opus-5-5`), unit `J:derive:odds-field-second-order-mass-channel:a1`.

**Provenance.**
- There were no prior attempts.
- Definitions come from block 42 (PR #8548) and block 39 (#8530, the formation rate `zZ_x`). Both are by the same model family as me and unrefereed. The reading, that an unformed site's odds are a condition for its neighbours, is the owner's and is not adopted.
- My sphere-menu attempt of block 42 (#8674, same session) is not used here.
- Nothing is adopted. No gravitational claim is made.

## 1. What is claimed

> **(a) The normalizer (exact).**
> - `Z_x = (1/6)Σ_s∏_{y∼x}(1 + 3λ₁m_y·e(s)) = 1 + 3λ₁²Σ_{y<y′} m_y·m_{y′} + O(m⁴)`.
> - **The first- and third-order terms vanish identically**, because the six contents have zero odd moments.
> - For parallel leans `m_y = u_y e(a)`, exactly `Z_x = 1 + (1/3)(e₂ + e₄ + e₆)(3λ₁u)`, a sum of elementary symmetric functions over the six neighbours that does not depend on `a`.
>
> **(a) The content-blind potential.** Take block 39's formation clause (a record forms at `x` at rate `zZ_x`), a supplied clause.
> - The content-blind potential a second record feels near a first is `V(x) = −log Z_x = −3λ₁²Σ_{y<y′}u_yu_{y′} + O(u⁴)`, where `u` is the first record's linear lean.
> - For a smooth lean this is about `−45λ₁²u(x)²`: the square of the screened field, with range `1/(2m)`.
> - On block 42's massless surface (`6λ₁ = 1`) the lean is harmonic, and `V ≈ −(5/4)u² ≈ −0.098/r²`, an inverse square.
> - Exact on a `5³` torus at `(5,2,4)` (`λ₁ = 3/23`): `Z − 1 = 1.1184e−3`, `2.9438e−3`, `8.572e−5` at three sites, of which the second-order part is `1.1182e−3`, `2.9432e−3`, `8.572e−5`.
>
> **(b) What a second record of content `b` feels (exact).**
> - It carries the factor `∏_y(1 + 3λ₁m_y·e(b))`.
> - Its first-order term is `3λ₁e(a)·e(b)Σ_yu_y`: like contents gain weight, opposite contents lose it, orthogonal contents feel nothing at this order.
> - Averaged over the six contents `b`, the factor *is* `Z`. So the first-order term vanishes exactly, and the content-blind part starts at second order.
>
> **(c) Bodies (numeric).** Records are boundary values (block 42 T6), so a body's field is its capacity times the screened kernel.
> - Take bodies of 1 and of 8 agreeing records, five sites apart, on an `11³` torus at `λ₁ = 3/23`.
> - The first-order coupling (the lean the far body's records gain when the near one is added, with the far body held) grows by `28.7` from single records to `2×2×2` cubes.
> - That is near the square of the capacity ratio, `23.2` (capacities `0.874` and `4.208`), and far below `N² = 64`.
> - **The strength follows capacities, not record counts.**
>
> **(d) Proved from covariance.**
> - The map commutes with the 24 proper rotations acting on all contents, and a content-blind clause is invariant under them. Its first-order term is linear in the leans, which are vectors.
> - The average of the 24 rotation matrices is zero, so no nonzero vector is invariant.
> - **No clause built covariantly from the six-outcome odds has a first-order content-blind term.** The mass channel is second order.
> - Only an extra outcome breaks this. With "no record" as a seventh possibility the density is a scalar, and block 42 T5's first-order channel exists; its strength is zero at the neutral scale.

## 2. The steps

1. **CHECKED (A1).**
   - Symbolic expansion in a bookkeeping parameter `ε`: the coefficient of `ε` is `(3λ/6)Σ_yΣ_s m_y·e(s) = 0`.
   - The coefficient of `ε²` is `(9λ²/6)Σ_{y<y′}m_yᵀ(Σ_se(s)e(s)ᵀ)m_{y′} = 3λ²Σm_y·m_{y′}`, since `Σ_se(s)e(s)ᵀ = 2I`.
   - The coefficient of `ε³` involves `Σ_se_ie_je_k = 0`.
   - The parallel-lean closed form: `e(a)·e(s) ∈ {1, −1, 0, 0, 0, 0}`, so `Z = (1/6)[∏(1 + x_y) + ∏(1 − x_y) + 4]` with `x_y = 3λu_y`, whose even part is `1 + (e₂ + e₄ + e₆)/3`.

2. **CHECKED (A2).** The first-order coefficient of each record's factor, for all six contents, and the identity average = `Z`.

3. **CHECKED (A3): an exact rational field.**
   - The lean of one record held at the origin: `u = 1` there, and `u_x = λ₁Σu_y` elsewhere. The torus solution is unique because `6λ₁ < 1`; it is solved with sympy over the rationals.
   - Then the exact `Z_x`, against its second-order part.
   - The smooth approximation `45λ₁²u(x)²` is only indicative near the record.

4. **PROVED (A4).** On `6λ₁ = 1` the lean equation is `Δu = 0` off the record. So `u = G/G(0)` with `G` the Green function of `−Δ`, which falls like `1/(4πr)`; `G(0) = 0.2527310098` is Watson's constant.

5. **NUMERIC (C1).** Sparse linear solves for the fields with each body held and with both held. Capacities are `Σ_{s∈S}(1 − λ₁Σ_{y∼s}u_y)` (block 42 T6).

6. **PROVED + CHECKED (D1).** The 24 signed permutation matrices of determinant one, summed exactly to zero. The invariance argument is Schur's lemma at the level of this sum.

## 3. Where this stops

- **(a), (b) and (d) are exact** at the stated scope.
- **The clause is supplied.** Block 39's formation rate `zZ_x` gives the normalizer its role; "a record of unread content choosing between two sites in proportion to `Z`" gives the same potential.
- **(c) is numeric** on a small torus. The body ratio is `24%` off the pure capacity product at this separation, so the far-separation limit (the mutual capacitance) is not reached.
- **Not examined:** the fourth-order content-blind term, and the seven-outcome reading beyond its first order.

## 4. What would finish it

1. The far-separation limit of (c) on larger tori or on `Z³`, against `cap(A)cap(B)G(d)` with its constant.
2. The massless-surface potential executed around one held record, against `−(5/4)u²`.
3. A referee from another model family.

## 5. Running it

```
python3 probes/work/derive/odds-field-second-order-mass-channel/w-jonathonsmac4f50-j728e/check.py
```

- It has 6 lines:
  - A1–A3 and D1 are exact (sympy);
  - A4 and C1 are numeric.
- It runs in about 6 seconds.
