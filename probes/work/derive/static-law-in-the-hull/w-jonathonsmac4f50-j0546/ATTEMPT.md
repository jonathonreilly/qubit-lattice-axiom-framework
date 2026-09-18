# static-law-in-the-hull, attempt 1 (worker w-jonathonsmac4f50-j0546, model claude-opus-5)

## (1) The statement attempted

Definitions are those of blocks 01, 14 and 16 (PRs #8148 and #8150 restate them; block 01 is on `main`):
a window `Λ` is a finite set of sites of `Z³` with its nearest-neighbour edges `E` (`n = |Λ|`); the menu is
`M = {±e₁, ±e₂, ±e₃}`; the rule is `φ(a, b) = p` if `a = b`, `q` if `a = −b`, `r` if `a ⊥ b`, with `p, q, r > 0`;
`Z₁ = p + q + 4r`, `K(b, a) = φ(a, b)/Z₁`, `K_k(v_A) = Σ_s Π_{y∈A} K(v_y, s)`; the one-site formation conditional is
`r(a | ∅) = 1/6`, `r(a | A) = Π_{y∈A} K(v_y, a) / K_{|A|}(v_A)`. The static law is `μ_stat(v) = Π_{⟨xy⟩∈E} φ(v_x, v_y) / Z_Λ`.
Formation along an order `σ` of `Λ`: `μ_σ(v) = Π_x r(v_x | v_{A_x(σ)})`, `A_x(σ)` the neighbours of `x` formed before `x`.

**Adapted scheme.** A family `π(· | F, v_F)` of probability distributions on `Λ ∖ F`, one for every formed set
`F ⊊ Λ` and every record pattern `v_F ∈ M^F`. The scheme forms sites one at a time: in state `(F, v_F)` it picks
`x ~ π(· | F, v_F)`, draws `v_x ~ r(· | v_{N(x)∩F})`, and continues until `F = Λ`; `μ_S` is the law of the finished
pattern. Deterministic schemes are those with point-mass `π`; block 14's clock laws are the case
`π(x | F, v_F) = λ_x(F, v_F)/Σ_y λ_y(F, v_F)`; block 16's value-blind order laws are the case where `π` ignores `v_F`.

**Statement.** Let the graph `(Λ, E)` contain a cycle and let `(p, q, r)` be positive and not all equal. Put
`N_0 = 6`, `N_k = p^k + q^k + 4r^k` (`k ≥ 1`), and for an order `σ` let `k_x(σ) = |A_x(σ)|` and
`D_σ = Π_x N_{k_x(σ)}`; let `D_Λ = min_σ D_σ`. Then `Z_Λ < D_Λ`, and for every adapted scheme `S` and every constant
pattern `v^b` (all records equal to `b`)

    μ_S(v^b) ≤ p^{|E|} / D_Λ = (Z_Λ / D_Λ) · μ_stat(v^b) < μ_stat(v^b).

Consequently the functional `f(v) = 1[v is constant]` satisfies `E_μ f ≤ 6p^{|E|}/D_Λ < 6p^{|E|}/Z_Λ = E_stat f` for
every `μ` in the convex hull of the adapted formation laws: **the static law is not a mixture of adapted
(value-dependent) formation laws on any window with a cycle, for every non-constant positive rule**, with the explicit
separating functional `f` and the exact margin `6p^{|E|}(1/Z_Λ − 1/D_Λ)`. This answers the problem for the 2×3
rectangle and the cube at `(3,1,2)`, `(5,2,4)`, `(7,3,5)` (exact numbers in step 8) and for every other window with a
cycle and every weight; the finite linear program is not needed.

## (2) Steps

**Step 1 — representation (PROVED).** For every adapted scheme `S` and every pattern `v`,
`μ_S(v) = Σ_σ ρ_S(σ | v) μ_σ(v)` with `ρ_S(σ | v) = Π_{j=1}^{n} π(σ_j | {σ_1,…,σ_{j−1}}, v_{σ_1…σ_{j−1}})` and
`Σ_σ ρ_S(σ | v) = 1` for every `v`.
*Argument.* The event "the finished pattern is `v`" is the disjoint union over orders `σ` of the events "the sites
form in the order `σ` and receive the records `v`". Along such a run the scheme is in state
`({σ_1,…,σ_{j−1}}, v_{σ_1…σ_{j−1}})` before step `j`, chooses `σ_j` with probability `π(σ_j | ·)`, and draws
`v_{σ_j}` with probability `r(v_{σ_j} | v_{A_{σ_j}(σ)})` (the formed neighbours of `σ_j` are exactly `A_{σ_j}(σ)`).
Multiplying, the event has probability `ρ_S(σ | v) μ_σ(v)`. For fixed `v`, `ρ_S(· | v)` is a product of conditional
probabilities of a sequential choice (each `π(· | F, v_F)` sums to one over `Λ ∖ F`), so summing over `σ_n`, then
`σ_{n−1}`, … gives `Σ_σ ρ_S(σ | v) = 1`.

**Step 2 — the constant patterns (PROVED).** `μ_σ(v^b) = p^{|E|} / D_σ` and `μ_stat(v^b) = p^{|E|} / Z_Λ`.
*Argument.* `r(b | ∅) = 1/6 = 1/N_0`. For `k ≥ 1` and `A` with all records `b`:
`r(b | A) = (p/Z₁)^k / Σ_s (φ(s, b)/Z₁)^k = p^k / N_k`, because as `s` runs over `M`, `φ(s, b)` takes the value `p`
once (`s = b`), `q` once (`s = −b`) and `r` four times. Every edge is counted exactly once, at its later endpoint,
so `Σ_x k_x(σ) = |E|`; multiply. The static value is immediate.

**Step 3 — Hölder at the scope used (PROVED; CHECKED as C1).** For `a_1,…,a_k ∈ M` (`k ≥ 1`):
`Σ_s Π_{i=1}^k φ(s, a_i) ≤ N_k`, with equality iff the functions `φ(·, a_i)` coincide; for a non-constant rule this
holds iff all `a_i` are equal, or (only when `p = q`) all `a_i` lie in one antipodal pair; in particular two
orthogonal `a_i` give strict inequality.
*Argument.* For non-negative `x_1,…,x_k`, `Π x_i ≤ (1/k) Σ x_i^k` (AM–GM applied to `x_i^k`), with equality iff all
`x_i` are equal. Put `x_i = φ(s, a_i) / N_k^{1/k}` (note `Σ_s φ(s, a_i)^k = N_k` for every `a_i`, as in step 2) and sum
over `s`: `Σ_s Π_i φ(s, a_i) / N_k ≤ (1/k) Σ_i Σ_s φ(s, a_i)^k / N_k = 1`. Equality forces `φ(s, a_i)` to be independent
of `i` for every `s`. If `a ⊥ a'`, then `φ(a, a) = p`, `φ(a, a') = r`, `φ(−a, a) = q`, `φ(−a, a') = r`, so equal functions
would need `p = q = r`; if `a' = −a`, the functions are `φ(·, a)` and its swap of the values at `±a`, equal iff `p = q`.

**Step 4 — `Z_Λ ≤ D_σ` for every order, strictly when some `k_x(σ) ≥ 2` (PROVED).**
*Argument.* Write `Π_edges φ(v) = Π_{j=1}^n F_j(v)` with `F_j = Π_{y ∈ A_{σ_j}(σ)} φ(v_{σ_j}, v_y)` (empty product `1`), and
`G_j = Σ_{v_{σ_1},…,v_{σ_j}} Π_{i ≤ j} F_i`, so `G_n = Z_Λ`, `G_0 = 1`. The factors `F_i`, `i < j`, do not involve
`v_{σ_j}`, so `G_j = Σ_{v_{σ_1…σ_{j−1}}} (Π_{i<j} F_i) · S_j`, `S_j = Σ_{v_{σ_j}} F_j`. Here `S_j = 6` if `k = 0`, `S_j = Z₁ = N_1`
if `k = 1`, and `S_j ≤ N_k` by step 3 if `k ≥ 2`. Hence `G_j ≤ N_{k_{σ_j}} G_{j−1}` and `Z_Λ ≤ D_σ`. If `k_{σ_j} ≥ 2`, then
`S_j < N_k` on every pattern of the earlier sites in which two of the recorded neighbours of `σ_j` carry orthogonal
records; such patterns exist and every `Π_{i<j} F_i` is positive, so `G_j < N_{k_{σ_j}} G_{j−1}` and the final inequality
is strict.

**Step 5 — every order of a cyclic window has a site recording two neighbours (PROVED).** Take a cycle in `(Λ, E)`; the
site of the cycle that forms last has its two cycle-neighbours formed before it, so its `k_x ≥ 2`.

**Step 6 — the main inequality (PROVED).** By steps 1, 2: `μ_S(v^b) = Σ_σ ρ_S(σ | v^b) p^{|E|}/D_σ ≤ p^{|E|}/D_Λ`. By steps 4, 5
`Z_Λ < D_σ` for every order, and there are finitely many orders, so `Z_Λ < D_Λ` and
`μ_S(v^b) ≤ (Z_Λ/D_Λ) μ_stat(v^b) < μ_stat(v^b)`.

**Step 7 — the hull and the separating functional (PROVED).** A finite mixture `Σ_i λ_i μ_{S_i}` obeys the bound of step 6 at
every `v^b`, hence `E f ≤ 6p^{|E|}/D_Λ`; the static law has `E_stat f = 6p^{|E|}/Z_Λ`, larger by the fixed amount
`6p^{|E|}(1/Z_Λ − 1/D_Λ) > 0`. So `μ_stat` is not in the convex hull of adapted formation laws (nor in its closure). The
separating functional `f = 1[constant]` is the same for every non-constant positive weight. The bound of step 6 is
attained: the value-blind order minimizing `D_σ` achieves `μ_σ(v^b) = p^{|E|}/D_Λ`, so value-dependence gains nothing on
this functional.

**Step 8 — exact numbers (CHECKED by `check.py`).**
- C1: step 3 for every `v_A ∈ M^k`, `k ≤ 6`, at `(3,1,2)`, `(5,2,4)`, `(7,3,5)`, `(1,3,2)` (q > p), `(2,2,1)` (p = q): bound,
  equality set exactly as stated, strictness for every `k ≥ 2`.
- C2–C4 (`Z_Λ`, `D_Λ` by dynamic programming over formed sets and, up to `n = 8`, by enumerating every order):

| window | `(p,q,r)` | `Z_Λ` | `D_Λ` | `Z_Λ/D_Λ` |
|---|---|---|---|---|
| plaquette | (3,1,2) | 20784 | 22464 | 0.925214 |
| 2×3 rectangle | (3,1,2) | 6000000 | 7008768 | 0.856071 |
| 2×3 rectangle | (5,2,4) | 568472046 | 631394298 | 0.900344 |
| 2×3 rectangle | (7,3,5) | 3651973440 | 4044168000 | 0.903022 |
| cube | (3,1,2) | 6982520832 | 10933678080 | 0.638625 |
| cube | (5,2,4) | 17002040556294 | 22841951518746 | 0.744334 |
| cube | (7,3,5) | 412507735200000 | 555911333280000 | 0.742039 |
| 3×3 square | (3,1,2) | 41671876608 | 56855126016 | 0.732948 |

  (all rows of `check.py`'s output, including `(1,3,2)` and `(2,2,1)`, have `Z_Λ < D_Λ`).
- C5: two explicit value-dependent deterministic schemes ("form next the site with most formed neighbours agreeing with
  the latest record"; "while all records agree, form a site with fewest formed neighbours, else most") on the plaquette
  and the 2×3 rectangle: exact full laws of total mass `1`, constant-pattern probabilities `≤ p^{|E|}/D_Λ < μ_stat(v^b)`
  (the first scheme attains the bound), total-variation distances from the static law `0.009`–`0.038`.

## (3) Where the route could fail

No step fails. The steps a referee should press: step 1 (the formed neighbours of `σ_j` at its formation are exactly
`A_{σ_j}(σ)`, so a value-dependent scheme's law is a `v`-dependent mixture of the fixed-order laws evaluated at the same
`v`), and the strictness in step 4 (orthogonal records on two recorded neighbours of a site with `k ≥ 2` occur with
positive weight; step 3's equality set excludes them for non-constant rules).

## (4) What would finish it, and what it does not cover

The statement above is complete as a finite-window theorem, pending the referee. Not covered: windows with fixed
outside records (environments), where the constant pattern of the window is not privileged in the same way; rules
other than the six-axis product rule (the proof uses only `Σ_s φ(s, a)^k` independent of `a` and the existence of two
values with different `φ(·, a)`, so it extends to any finite menu with a transitive covariance group and a non-constant
positive rule, but that extension is not checked here); continuous menus. The result is consistent with block 16's flip
lemma (the constant pattern minimizes every order's weight ratio) and with block 01's Theorem B (on forests an order with
every `k_x ≤ 1` has `D_σ = Z_Λ`).
