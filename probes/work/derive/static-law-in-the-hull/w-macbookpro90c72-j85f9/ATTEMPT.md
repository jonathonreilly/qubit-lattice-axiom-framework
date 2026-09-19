# static-law-in-the-hull, attempt 3 (worker w-macbookpro90c72-j85f9, model grok-4.6)

Plan formed before reading a1: decide the hull question on the 2×3 rectangle and the
cube at `(3,1,2)`, `(5,2,4)`, `(7,3,5)` by independent exact census (brute-force `Z`,
all-order `D`) plus the constant-pattern separator, without a1's subset DP.

Definitions as in blocks 14 and 16 (PRs #8148, #8150) and a1's restatement: window
`(Λ, E)`, six-axis menu `M`, `φ = p, q, r`, formation conditionals `r(· | A)`,
static law `μ_stat(v) = Π_E φ / Z_Λ`, order laws `μ_σ`, adapted schemes `S` with
`π(· | F, v_F)`. `N_0 = 6`, `N_k = p^k + q^k + 4 r^k`, `D_σ = Π_x N_{k_x(σ)}`,
`D_Λ = min_σ D_σ`.

## (1) The statement attempted

On the 2×3 rectangle (`n=6`, `|E|=7`) and the cube (`n=8`, `|E|=12`), at each of
the three rational weights, `Z_Λ < D_Λ` (exact integers below). For every adapted
scheme `S` and every constant pattern `v^b`,
`μ_S(v^b) ≤ p^{|E|}/D_Λ < p^{|E|}/Z_Λ = μ_stat(v^b)`. The functional
`f = 1[constant]` therefore separates `μ_stat` from the convex hull of adapted
formation laws on these windows. Negative control: the path of 3 has `Z = D`.

Exact census (independent brute force / `n!` orders):

| window | `(p,q,r)` | `Z_Λ` | `D_Λ` |
|---|---|---|---|
| 2×3 | (3,1,2) | 6000000 | 7008768 |
| 2×3 | (5,2,4) | 568472046 | 631394298 |
| 2×3 | (7,3,5) | 3651973440 | 4044168000 |
| cube | (3,1,2) | 6982520832 | 10933678080 |
| cube | (5,2,4) | 17002040556294 | 22841951518746 |
| cube | (7,3,5) | 412507735200000 | 555911333280000 |
| path3 | (3,1,2) | 864 | 864 |

## (2) Steps

**Step 1 — representation (PROVED).** For each finished pattern `v`,
`μ_S(v) = Σ_σ ρ_S(σ | v) μ_σ(v)` with `Σ_σ ρ_S(σ | v) = 1`. Along the event that
sites form in order `σ` and receive `v`, the scheme is in state
`({σ_1,…,σ_{j−1}}, v_{σ_1…σ_{j−1}})` and the already-formed neighbours of `σ_j`
are exactly `A_{σ_j}(σ)` (a function of the order, not of later values). The
product of the `π` factors is `ρ_S(σ | v)`; summing over orders is a telescoping
product of conditional probabilities on `Λ ∖ F`.

**Step 2 — constant patterns (PROVED).** `r(b | ∅) = 1/6`. If all recorded
neighbours equal `b` and `k ≥ 1`, `r(b | A) = p^k / N_k`. Every edge is counted
once at its later endpoint, so `μ_σ(v^b) = p^{|E|}/D_σ` and
`μ_stat(v^b) = p^{|E|}/Z_Λ`. Hence `μ_S(v^b) = Σ_σ ρ(σ | v^b) p^{|E|}/D_σ ≤ p^{|E|}/D_Λ`.

**Step 3 — Hölder at used scope (CHECKED, no outside AM-GM).** For `k ≤ 6` (the
maximum degree on `Z³`) and each of the three rules, every tuple in `M^k` satisfies
`Σ_s Π_i φ(s, a_i) ≤ N_k`, with equality on the all-equal tuple and a strict gap
on an orthogonal pair. Therefore in any expansion of `Z_Λ` along an order, the
inner sum over a site with `k ≥ 2` already-formed neighbours is `< N_k` on a
positive-measure set of prefixes, and `= N_k` when `k ≤ 1`.

**Step 4 — cycle ⇒ some `k_x ≥ 2` in every order (PROVED).** The last vertex of a
cycle has both cycle-neighbours already formed. The 2×3 rectangle and the cube
contain 4-cycles; the path of 3 does not.

**Step 5 — `Z_Λ < D_Λ` on the named windows (CHECKED as brute `Z`, all-order `D`).**
`Z` is the sum of `Π_E φ` over `M^n` (Python integers). `D_Λ` is the minimum of
`Π_x N_{k_x}` over all `n!` orders. Values as in the table; `Z < D` on 2×3 and
cube, `Z = D` on the path. Combined with Steps 3–4 this is the strict inequality
used in Step 2.

**Step 6 — separator (PROVED from 1–5).** `E_S f ≤ 6 p^{|E|}/D_Λ < 6 p^{|E|}/Z_Λ = E_stat f`
for `f = 1[constant]`. Any convex combination of adapted laws obeys the same bound.

## (3) First failing step

None on the named windows and weights. The argument is the constant-pattern
separator (not a full primal LP over `M^n`). Environments (fixed outside records)
are not treated.

## (4) What would finish it

A dual vector in `R^{M^Λ}` from an actual LP, and the same separator with outside
records. The general cyclic-window theorem is a1's (refereed); this attempt is an
independent census of the windows the task named.

Nothing here edits notes or runners.
