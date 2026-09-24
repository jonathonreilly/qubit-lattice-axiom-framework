# the-level-ordered-response-kernel, attempt 2

Worker `w-macbookpro90c72-jf747` (grok-4.6). The route is uniqueness for the causal recursion, not a path count.

## 1. Statement

On the level-ordered past, a site reads itself and the three parents `x-e_j`. At gain one the stationary response `G` of a source at the origin is the unique function with `G=0` off the forward octant, `G(0)=4/3`, and

`G(x) = (1/3) Σ_{j=1}^3 G(x-e_j)` for `x ≠ 0`.

It is `G(a,b,c) = (4/3) L!/(a!b!c!) 3^{-L}` for `a,b,c ≥ 0`, `L=a+b+c`. Every level sums to `4/3`. On the drift-free modes `k=(q,-q,0)` the symbol is `8/E(k)`.

## 2. Steps

**S1 (PROVED).** Steps are `{0,e_1,e_2,e_3}`, each with probability `1/4`. Only the all-stay paths remain at the origin, so `G(0) = Σ_j (1/4)^j = 4/3`. A coordinate never decreases, so `G=0` off the octant. Away from the origin the stay can be eliminated and `G(x) = (1/3) Σ_j G(x-e_j)`.

**S2 (PROVED).** Order the octant by `L`. Each value is fixed by values at level `L-1`. The solution is unique.

**S3 (CHECKED).** The displayed formula has `G(0)=4/3` and satisfies the recursion through level 8, including the faces where a coordinate vanishes. The algebraic step is `a+b+c=L`: the three parents contribute factors `a`, `b` and `c` and rebuild `L!`.

**S4 (PROVED).** On level `L` the formula is `(4/3)` times the equal trinomial. The trinomial sums to 1, so the level sums to `4/3`.

**S5 (CHECKED).** `G(1,0,0)=4/9` and `G(-1,0,0)=0`. The wake points along `(1,1,1)` and is silent upstream.

**S6 (CHECKED).** `E(k)=6-2Σ cos k_j`. On `k=(q,-q,0)`, `3-Σ e^{-ik_j}=E/2`. The symbol `4/(3-Σ e^{-ik_j})` is therefore `8/E`, against the light-cone gain-one kernel `7/E`.

**S7 (not proved).** Whether the nonlinear level-ordered response exceeds `1/E(k)` is not settled. The linear symbol already exceeds the light-cone gain-one kernel on drift-free modes. That is not a theorem about the nonlinear rule.

## 3. Where it stops

The large-distance Gaussian cross-section is not proved here. The nonlinear comparison is not proved here.

## 4. What would finish it

An exact nonlinear source on a finite window whose measured `R̂(k)` exceeds `1/E(k)` in a drift-free direction, or a proof that it cannot.
