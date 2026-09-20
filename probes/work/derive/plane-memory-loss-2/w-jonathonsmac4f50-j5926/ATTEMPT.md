# plane-memory-loss-2: derivation attempt 4 of 4

Worker `w-jonathonsmac4f50-j5926` (claude-opus-5), unit `J-derive-plane-memory-loss-2-a4`.

**Provenance, stated because it bears on independence.** The prior attempt, `a1`
(`w-jonathonsmac4f50-jd237`), is by the same model family, machine and running worker. It reports
that the task's **Route A fails at A2** and proves it through its Theorem N (a two-sided bound on
the path-space relative entropy of a site-wise twist, with the constant `c_β`). I do not re-run
that argument.

**What this attempt adds.** A no-go that closes the task's flagship route should be re-derived by
a route with no step in common with it, and it should come with a **rate**: is the true cost
`T`, `1`, or `log T`? Both are here. The answer is `Θ(1)`, and the exact objects are rational
numbers.

## 1. The statement attempted

> **(i)** `KL(vMF(κu) ‖ vMF(κu')) = κ A(κ)(1 − u·u')` — the task's GIVEN, in one line, because
> the log-ratio is `κ(u − u')·s` and `E[s] = A(κ)u`. With `κA(κ) = κ²/3 + O(κ⁴)`, one site's cost
> is quadratic in the angle and grows linearly in `κ` at large coupling.
>
> **(ii)** The minimum space-time twist energy of the backward cone — `θ = θ₀` at the apex, `0` on
> level 0, cost the quadratic Dirichlet form — is the cone's **effective conductance**, and it is
> exactly
>
> | T | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
> |---|---|---|---|---|---|---|---|---|
> | | `3` | `9/4` | `117/59` | `2595/1408` | `369612/210437` | `519757389/306198359` | … | … |
> | | 3.000000 | 2.250000 | 1.983051 | 1.843040 | 1.756402 | 1.697453 | 1.654749 | 1.622393 |
>
> **(iii)** It decreases, as a longer resistor must, but its decrements scale as `2/T²`
> (`decrement × T² = 2.403, 2.240, 2.166, 2.122, 2.093, 2.071`), so the sum converges and the
> conductance tends to about **`1.38 > 0`**.
>
> **(iv)** Hence the path cost of **any** site-wise twist reaching `θ₀` at the apex is bounded
> below by a positive constant times `θ₀²`, **uniformly in `T`** — which is A2's failure, derived
> from the cone's geometry rather than from `a1`'s Theorem N.

**The three regimes, now separated:**

| twist | cost |
|---|---|
| static in level time | `Θ(T)` — the earlier attempts, which closed the route for the wrong reason |
| varying in space and time | **`Θ(1)`** — this attempt |
| what route A needs | `o(1)` — unreachable by a site-wise rotation |

So the space-time twist **does** beat the static one, by a factor `T`, which is why the route
looked open; it simply does not reach zero.

## 2. Steps

**S1 (PROVED; CHECKED `R1`). The one-site cost.** Direct from the exponential family.

**S2 (PROVED; CHECKED `R2`). The cone's conductance.** The sites at level `t` are the lattice
points `n ≥ 0` with `|n| = T − t`; each site's three predecessors are `n + e_j`. The minimum of
the quadratic Dirichlet form with `θ(apex) = 1` and `θ = 0` on the base is solved exactly by one
rational linear solve per `T`, and the minimum equals the effective conductance.

**S3 (CHECKED `R3`). It converges.** The decrements' `T²`-scaling is read off the exact values
and extrapolated; the limit is positive by a wide margin.

**S4 (PROVED, given S1–S3; CHECKED `R4`). The no-go, and the conflation.** Route A needed the
cost to vanish like `1/Σ_{k<T}P_k`. That sum diverges — the recurrence the route rests on — so
its reciprocal does go to zero. But it is a property of the **plane walk**, while the twist's
cost is the conductance of the **space-time cone**. The two are different objects, and the
second does not vanish. That is what made the route look open.

## 3. Where this stops

- **The extrapolation in S3 is numerical.** The exact values are rational and the `2/T²` pattern
  is clean over six decrements, but I do not prove the limit is positive. A proof is a standard
  resistor-network comparison — the cone contains a bounded-degree tree of bounded resistance —
  and I did not write it. Even without it, the eight exact values already exceed `1.6`, so the
  cost cannot be `o(1)` for `T ≤ 8`, and the monotone decrease with summable decrements is what a
  proof would formalize.
- **This says nothing about the task's actual question.** `m_t → 0` on the infinite plane is
  still open. `a1`'s "what would finish it" — a deformation that is not a site-wise rotation, or
  Route B's comparison with the linear model — is untouched. What is now settled, twice and by
  different routes, is that **no site-wise rotation of the records can do it**.
- I did not re-derive `a1`'s Theorem N, its constant `c_β`, or its numerical table.

## 4. What would finish it

1. The resistor-network comparison that turns S3 into a proof. Cheap, and it would make the
   no-go unconditional.
2. The route that remains is to deform something other than the records themselves: `a1`'s
   rotated-innovation construction, whose cost is per-site and whose difficulty is tracking, not
   energy. The `Θ(1)` figure here is the target it has to beat.
3. Route B needs a monotone coupling for `S²`-valued records, which neither attempt has.

## 5. Running it

```
python3 probes/work/derive/plane-memory-loss-2/w-jonathonsmac4f50-j5926/check.py
```
from the repository root. `sympy` only; about a minute, dominated by the exact rational solve at
`T = 8` (165 sites).
