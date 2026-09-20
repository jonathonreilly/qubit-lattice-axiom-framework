# plane-memory-loss-2, attempt 3 of 4 — the task's own GIVEN (2) is false

Worker `w-jonathonsmac4f50-jdb1c` (`claude-opus-5`), unit `J-derive-plane-memory-loss-2-a3`.

**Provenance, stated because it bears on independence.** Both prior attempts on this problem are
by the same model family, machine and running worker as this one: `a1`
(`w-jonathonsmac4f50-jd237`) and `a4` (`w-jonathonsmac4f50-j5926`). Nothing below is independent
confirmation of either. I do not re-run either route. What I do instead is take the task's stated
GIVEN (2) at face value and test it against the object `a1` and `a4` already put on the table,
because the three cannot all be true: GIVEN (2) says the minimum space-time twist cost tends to
`0`, `a4` says it tends to about `1.38`, and `a1` exhibits a flow whose energy is bounded. One of
them is wrong. It is GIVEN (2), and the closed form below settles it without extrapolation.

## 1. The statement attempted

Let the backward cone have apex at level `T` and base at level `0`; the sites at level `m` are the
triples `n ≥ 0` of non-negative integers with `|n| = m`, and each site's three successors are
`n + e_j`. The order-`β` cost of a site-wise twist field is the quadratic Dirichlet form on this
network with `θ = θ₀` at the apex and `θ = 0` on the base; by the Dirichlet principle its minimum
is `θ₀²·C_T` with `C_T` the effective conductance, and `C_T = 1/R_T`.

> **Theorem.** The Pólya-urn unit flow — at level `m`, move `n → n + e_j` with probability
> `(n_j+1)/(m+3)` — has level energy exactly `1/((m+1)(m+3))`, hence total energy
>
> ```
> E_T  =  Σ_{m<T} 1/((m+1)(m+3))  =  3/4 − (1/2)( 1/(T+1) + 1/(T+2) )  <  3/4   for every T.
> ```
>
> By Thomson's principle `R_T ≤ E_T < 3/4`, therefore
>
> ```
> C_T  >  4/3    for every T.
> ```
>
> **Corollary.** The task's GIVEN (2) is false as stated: the minimum space-time twist cost is not
> `1/Σ_{k<T}P_k` and does not tend to `0`. Route A is closed — by a proof, not by an
> extrapolation.

## 2. The steps

1. **CHECKED (`C1`).** The Pólya urn's law at level `m` is uniform on that level's
   `N(m) = (m+1)(m+2)/2` sites — verified exactly for `m = 0..8`. (This is the standard Pólya
   property; it is checked here rather than cited because everything else rests on it.)
2. **CHECKED (`C2`).** The induced edge flows form a unit flow: total outflow `1` at each level and
   inflow `=` outflow at every site, exactly, for levels `0..6`.
3. **PROVED (`C3`).** The level-`m` energy is
   `3·Σ_{|n|=m}(n₁+1)² / (N(m)(m+3))²`, and `Σ_{|n|=m}(n₁+1)² = Σ_{a≤m}(a+1)²(m+1−a)`, which in
   closed form reduces the whole expression to `1/((m+1)(m+3))`. `sympy` verifies the
   simplification identically in `m`; the flow's own energy is checked term-by-term at
   `m = 0,1,2,3,7,12,20`.
4. **PROVED (`C4`).** Partial fractions: `1/((m+1)(m+3)) = (1/2)[1/(m+1) − 1/(m+3)]`, so the sum
   telescopes to `3/4 − (1/2)(1/(T+1) + 1/(T+2))`, checked exactly at `T = 1, 5, 20, 40` and
   verified as a symbolic summation. `E_T ↑ 3/4`, so `3/4` is the best constant this flow gives.
5. **PROVED + CHECKED (`C5`).** Thomson's principle gives `R_T ≤ E_T`, hence `C_T > 4/3`. As a
   cross-check I recompute `C_T` directly and independently, by exact rational layer elimination
   (the cone is layered, so levels can be eliminated one at a time): `C_1..C_5 = 3, 9/4, 117/59,
   2595/1408, 369612/210437`. **These reproduce attempt `a4`'s table exactly**, and every one
   satisfies `R_T = 1/C_T ≤ E_T`.
6. **CHECKED (`C6`).** The uniform-splitting flow (split equally three ways at each site — the
   simple random walk on the cone) is also a unit flow, and its energy is exactly
   `(1/3)Σ_{m<T}P_m`, with `P_m` the walk's collision probability at level `m` — verified as an
   identity at `T = 1, 3, 10, 30`. Since `P_m ~ c/m`, this energy diverges like `log T`, and at
   `T = 30` it is already larger than the Pólya flow's. So `1/Σ_k P_k` is the reciprocal of a
   *divergent upper bound* on `R_T`: it is a **lower bound on the conductance that tends to zero**
   — true, and vacuous. GIVEN (2) reads that vacuous lower bound as the value of the minimum.

### What this does to the two prior attempts

- `a1`'s Pólya flow is the right object; its stated bound `E_T ≤ 2T/(T+1)` is valid but loose by a
  factor of about `2.6` (`E_40 = 625/861 = 0.7259` against `1.951`). The closed form `E_T < 3/4`
  replaces it and is sharp for this flow.
- `a4`'s conductance table is confirmed exactly at `T = 1..5` by an independent elimination. Its
  conclusion was correct; its *justification* — reading a `2/T²` decrement scaling off six
  decrements and extrapolating — was not a proof, and could not have excluded a slow decay to
  zero. `C_T > 4/3` excludes it outright, and `a4`'s extrapolated `≈1.38` sits just above `4/3`.

## 3. Where the route stops

**The task's actual target is not proved.** Closing Route A does not show `m_t → 0` on the plane
for any `β`, let alone every `β`. All that is established is that no site-wise space-time twist
can have vanishing cost, so the entropy-inequality argument cannot be the mechanism. Route B (a
lower bound on the growth of the nonlinear law's transverse variance by comparison with the linear
one) is untouched here and is now the only live route in the task as written.

Three further limits:

- The cost is computed to order `β` — the quadratic Dirichlet form, with `KL(vMF(κu)‖vMF(κu')) =
  κA(κ)(1−u·u')` giving the one-site quadratic. A twist that is *not* a site-wise rotation is
  outside this analysis entirely, and nothing here forbids one.
- `C_T > 4/3` is proved on the cone with the base held at `0`. A different boundary condition (for
  instance a twist imposed at infinity rather than on level `0`) is a different variational
  problem, and it is possible that GIVEN (2)'s formula is the answer to *that* one; I have not
  identified a problem it does solve.
- The layer elimination is exact but expensive; I ran it to `T = 5` only. It is a cross-check of
  `a4`, not the basis of any claim — the theorem needs no value of `C_T` at all.

## 4. What would finish it

1. **Route B**, which now carries the whole task: bound below the transverse-variance growth of the
   nonlinear law by the linear one's `(3√3/(4π))σ² log t`. The GIVEN already grants that the linear
   model forgets; what is missing is a comparison that survives the nonlinearity.
2. Identify which variational problem `1/Σ_{k<T}P_k` *does* solve, if any, and correct the referee
   report that states it as the space-time twist minimum — it is currently the stated justification
   for keeping Route A open, and four attempts have now been spent against it.
3. If a vanishing-cost deformation exists at all, it is not a site-wise rotation; the natural next
   object is a twist acting on the *law* rather than on each record, for which the cone geometry
   gives no lower bound.
4. Re-derive step 3's closed form and step 5's elimination with a different model family before
   `C_T > 4/3` is used downstream. Everything here is same-family with what it corrects.

## 5. Running it

```
python3 probes/work/derive/plane-memory-loss-2/w-jonathonsmac4f50-jdb1c/check.py
```

Standard library plus `sympy`; 40 checks, exact rational and symbolic arithmetic throughout (only
printed decimals are floats). Runs in about half a minute, the layer elimination at `T = 5` being
the slow part.
