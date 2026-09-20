# J:derive:static-formation-singularity:a1 — w-macbookpro90c72-je8fe

Definitions are those of the census note on the PR branch named at claim time
(`docs/ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md`,
lines 112–150). Every finite claim below is verified as exact rationals by `check.py`
in this directory (28 `ok` lines, exit 0); the label `Cn` names the check.

## 0. Notation

`M = 6` states with an antipode `s ↦ s̄`; `φ(s,t) = p = 3` if `s = t`, `q = 1` if
`t = s̄`, `r = 2` otherwise; `Z_1 = p + q + 4r = 12`. Static law on a finite graph
`G = (V,E)`: `μ(v) = W(v)/Z_W`, `W(v) = ∏_{xy∈E} φ(v_x,v_y)`. Formation law for an
order `σ = (x_1,…,x_n)`: `ν_σ(v) = ∏_k r(v_{x_k} | v|A_k)`, `A_k = N(x_k) ∩ {x_1,…,x_{k−1}}`,
`r(s|A) = ∏_{y∈A} φ(s,v_y) / Z(v|A)`, `Z(v|A) = Σ_s ∏_{y∈A} φ(s,v_y)`. An *adapted*
law may choose `x_{k+1}` as a function of the values already placed; `H` is the closed
convex hull of all adapted laws (so it contains every mixture of orders as well).
`N(a,b) := Z(v|{a,b}) = 26 / 22 / 24` for `b` equal / antipodal / other (C1);
`Z_3` is the three-argument version, with values `{44,48,52,60}`.

## 1. Statement attempted

At `(p,q,r) = (3,1,2)`:
(a) an explicit `m` with `TV(μ_{mC_4}, H) ≥ 1/2` for `G = m` disjoint 4-cycles,
    together with a converse `m` below which no test can succeed;
(b) a positive lower bound on the relative-entropy density of `μ` with respect to the
    lexicographic formation law on `Z²` and on `Z³`;
(c) the observable that attains the separation on the `2×2` and `2×2×2` windows, and in
    particular whether the plaquette four-point function is such an observable.

Nothing outside the note's definitions is ASSUMED. The prior attempt `a3` is quoted only
for comparison; every one of its numbers used here (`Z_W(cube)`, the cube `TV`, the 600
constant-tilt boundaries, `986`) is re-derived independently below.

## 2. Steps

**S1 — the exact likelihood identity. PROVED; CHECKED C1, C1b, C2, C3.**
For every order `σ` on every graph,

    ν_σ(v) = W(v) / ( M^{a_0} Z_1^{a_1} ∏_{A ∈ K(σ)} Z(v|A) ),

where `a_i = #{k : |A_k| = i}` and `K(σ)` is the multiset `{A_k : |A_k| ≥ 2}`.
*Proof.* `ν_σ(v) = ∏_k ∏_{y∈A_k} φ(v_{x_k},v_y) / ∏_k Z(v|A_k)`. In the numerator the
pair `(x_k,y)`, `y ∈ A_k`, is an edge of `G`, and each edge is produced exactly once — at
the step of whichever endpoint is later in `σ`, the other endpoint then lying in
`N(x_k) ∩ predecessors`. As `φ` is symmetric the numerator is `W(v)`. `Z(v|∅) = M` and
`Z(v|{y}) = Σ_s φ(s,v_y) = Z_1 = 12` for every `v_y`, because every row of `φ` is a
permutation of the same six values (C1). ∎
Hence `dμ/dν_σ (v) = (M^{a_0} Z_1^{a_1}/Z_W) ∏_{A∈K(σ)} Z(v|A)`: the vector
`(Z(v|A))_{A∈K(σ)}` is a sufficient statistic and, by Neyman–Pearson, **every optimal
test between `μ` and `ν_σ` is a level set of `Σ_{A∈K(σ)} log Z(v|A)`.**
CHECKED C2: the identity holds as exact rationals for all 24 orders × 1296 configurations
on the 4-cycle. CHECKED C3: the 24 orders give exactly 4 distinct laws, with
`K ∈ {{d}, {d′}, {d,d}, {d′,d′}}` and multiplicities 8, 8, 4, 4, where `d = {0,3}` and
`d′ = {1,2}` are the two diagonals. CHECKED C1b: `Z_W(C_4) = 12⁴ + 3·2⁴ = 20784`.

**S2 — the lower bound must be an event bound. PROVED.**
For a fixed event `E` the map `ν ↦ ν(E)` is affine, so `sup_{ν∈H} ν(E)` equals the sup
over the extreme points, i.e. over adapted laws; therefore
`TV(μ,ν) ≥ μ(E) − sup_{ν∈H} ν(E)` holds *simultaneously for every* `ν ∈ H`. By contrast
the Hellinger affinity `ρ(μ,ν) = Σ_v √(μ(v)ν(v))` is **concave** in `ν` (a sum of concave
functions of `ν`), so a bound `TV ≥ 1 − ρ^m` proved at each extreme point does not
transfer to the hull. Hence the lower bound below is built from a single test statistic,
and Hellinger is used only for the converse (S6), where the alternative is one fixed order.

**S3 — exponential-moment bound against an adaptive adversary. PROVED; CHECKED C4.**
Let `G` be `m` disjoint 4-cycles; `μ_G = μ^{⊗m}` because `W` factors over components and
`Z_W` is multiplicative. For `h > 0` on `Σ⁴` put `U = E_μ[1/h]` and
`V = sup{ E_ν[h] : ν adapted on one 4-cycle }`.
*(i) Product lemma.* For every adapted `ν` on `G`, `E_ν[∏_{i≤m} h(v^{(i)})] ≤ V^m`.
Let `f(state)` be the sup over adapted continuations of `E[∏_i h_i | state]`. Claim:
`f(state) = ∏_i f_i(state_i)`, `state_i` the restriction to component `i`. Induction on
the number of unfilled sites. If none, both sides are `∏_i h_i`. Otherwise
`f(state) = max_x Σ_s r(s | v|A_x) f(state + (x,s))`; the components are disconnected, so
for `x` in component `j` the kernel depends only on `state_j`, and by the inductive
hypothesis `f(state+(x,s)) = (∏_{i≠j} f_i(state_i))·f_j(state_j+(x,s))`. The constant
`∏_{i≠j} f_i ≥ 0` pulls out of the inner sum and out of the max over `x ∈ j`, so
`f(state) = max_j ∏_i f_i(state_i) = ∏_i f_i(state_i)`. At the empty state this is `V^m`.
A mixture of adapted laws gives a convex combination, hence no more. ∎
*(ii)* With `T = Σ_i log h(v^{(i)})` and any `τ`: `μ(T ≤ τ) ≤ e^{τ} E_μ[e^{−T}] = e^{τ}U^m`
and `ν(T > τ) ≤ e^{−τ} E_ν[e^{T}] ≤ e^{−τ}V^m` by (i) — Markov's inequality both times.
So for every `ν ∈ H`, `TV ≥ μ(T>τ) − ν(T>τ) ≥ 1 − e^{τ}U^m − e^{−τ}V^m`, and
`e^{τ} = (V/U)^{m/2}` gives `TV ≥ 1 − 2(UV)^{m/2}`. Thus `TV ≥ 1/2` once `UV < 1` and
`m ≥ 4 log 2 / log(1/(UV))`.
`V` is computed by exactly this backward induction over partially filled configurations;
CHECKED C4 that it dominates all 24 pure orders.

**S4 — the price sheet. CHECKED C5, C5b, C5c.**
By S1 it suffices to take `h` a function of the unordered pair of diagonal values, indexed
by `(i,j)`, `i = (N−22)/2 ∈ {0,1,2}`. An exact descent on a `1/1000` grid gives

    G(0,0)=1, G(0,1)=511/500, G(0,2)=1041/1000, G(1,1)=209/200, G(1,2)=533/500, G(2,2)=136/125,

`U = 13339090843683247/13958280479086944`, `V = 1009751/965250` (the DP sup of S3),

    U·V = 13469160318500002341497/13473230232438672696000 < 1,   1 − UV ≈ 3.02·10⁻⁴.

**S5 — a rational threshold: `m = 9268`. PROVED; CHECKED C6, C7, C12b.**
`log(1/x) ≥ 2(1−x)/(1+x)` on `(0,1]`: both sides vanish at `x = 1` and the derivative of
the difference is `−(1−x)²/(x(1+x)²) ≤ 0` (CHECKED symbolically, C12b), so the difference
decreases to `0` at `x = 1` and is `≥ 0` to its left. Hence
`4log2/log(1/UV) ≤ 2log2·(1+UV)/(1−UV) ≤ (7/5)(1+UV)/(1−UV)` using `log 2 < 7/10`, which is
certified rationally by `e > Σ_{k≤13} 1/k! > 2718/1000` and `2718⁷ > 1024·1000⁷`, i.e.
`e⁷ > 2¹⁰` (C6). The right-hand side is `< 9268` (C7). **So `m = 9268` disjoint plaquettes
give `TV(μ,H) ≥ 1/2` against every adapted formation law and every mixture of them**,
against `80237` for the same quantity in `a3` — a factor `> 8.65` (C7).

**S6 — converse: 495 plaquettes are not enough. PROVED; CHECKED C11, C11b.**
For the fixed order with `K(σ) = {d′}`, S1 gives `dν/dμ = Z_W/(M Z_1² N) = 433/(18N)`, so
`ρ(μ,ν) = Σ_j μ(N = 22+2j) √(433/(18(22+2j)))`. Replacing each square root by a certified
rational lower bound gives `ρ ≥ 432875307883/433000000000 = 1 − δ`, `δ < 2.88·10⁻⁴` (C11).
`TV ≤ √(1−ρ²)`: `TV = ½Σ|p−q| = ½Σ|√p−√q|(√p+√q) ≤ ½(Σ(√p−√q)²)^{1/2}(Σ(√p+√q)²)^{1/2}
= ½√(2−2ρ)√(2+2ρ) = √(1−ρ²)` by Cauchy–Schwarz; and `ρ` for `m`-fold products is `ρ^m`.
So `TV_m < 1/2` whenever `ρ^{2m} > 3/4`, i.e. `2m log(1/ρ) < log(4/3)`. Since
`log(1/(1−δ)) = ∫_0^δ dt/(1−t) ≤ δ/(1−δ)` and `log(4/3) > 2/7` — certified by
`e < 2719/1000` (the series plus the geometric tail `(15/14)/14!`) and
`e² < 7392961/10⁶ < 16384/2187 = (4/3)⁷` (C11b) — it suffices that `m ≤ (1−δ)/(7δ)`, and
that exceeds 495 (C11).
**The plaquette threshold therefore lies in `[496, 9268]`:** S5 is within a factor 18.7 of
optimal, where `a3`'s bound was within 161.8.

**S7 — the optimal `2×2` observable; the four-point function is not one. CHECKED C8–C10b.**
By S1 the statistic is the pair of diagonal `N`-values, so exactly 64 events are
measurable with respect to it. Exhaustively (C8) the best is
`E = {(1,2),(2,2)} = {one diagonal has N = 26 and the other N ≥ 24} = {N_1N_2 ≥ 624}`, with
`μ(E) − sup_{ν∈H} ν(E) = 30457/2431728` (the sup over `H` by the S3 DP). Against a single
fixed order, `min_σ TV(μ,ν_σ) = 455/31176` and `max_σ = 37/1299` (C9), so
`TV(μ,H) ∈ [30457/2431728, 455/31176]`. The plaquette four-point function "all four sites
equal" has `μ = 81/3464`, `ν = 9/416`, gap `315/180128` — `8.34×` below `455/31176` and
`7.16×` below the hull-valid event (C10, C10b). **The four-point function is not an optimal
observable**, and no test built on it alone reaches the single-plaquette separation.

**S8 — the `2×2×2` window. CHECKED C15, C15b.**
Summing out the two antipodal corners `000` and `111` reduces the `6⁸` sum to `6³ × 6³`:
the weight is `Z_3(t) Z_3(s) · cross(t,s)` with `t = (v_{100},v_{010},v_{001})`,
`s = (v_{110},v_{101},v_{011})`. Then `Z_W = 6982520832`, `M^{a_0}Z_1^{a_1} = 6·12³ = 10368`,
and the likelihood ratio is the **single scalar** `Q = N(t_0,t_1)N(t_0,t_2)N(t_1,t_2)·Z_3(s)`
with 17 distinct values; `Σ_v ν(v) = 1` re-confirms S1 independently.
`TV(μ,ν) = 1182193085/23402354976`, attained on `{Q > Z_W/10368 = 6061216/9}`, where
`μ(E) = 5071505/12122432` and `ν(E) = 90895/247104`. This reproduces `a3`'s `Z_W` and `TV`
by a different route and identifies the optimal statistic.

**S9 — the per-site rate on `Z²` and `Z³`. PROVED; CHECKED C12–C14d, C16, C16b.**
*(i) Sharp rational divergence bound.* With `h(r) = r log r − r + 1`: `h(r) ≥ (r−1)²/2` on
`(0,1]` and `h(r) ≥ (r−1)²/(2r)` on `[1,∞)`, since in each case the difference vanishes to
second order at `r = 1` and has second derivative `1/r − 1 ≥ 0` resp. `(r²−1)/r³ ≥ 0` on
that interval (CHECKED symbolically, C12). Summing `D(P‖Q) = Σ_s Q_s h(P_s/Q_s)`:

    D(P‖Q) ≥ Σ_s (P_s − Q_s)² / (2 max(P_s,Q_s)) =: D̂(P,Q).

*(ii) Conditionals.* In the lexicographic order `A_x = {x − e_j}_j`, so
`ν(v) = W(v)/∏_x Z(v|A_x)`. Given everything but `v_x`, the `μ`-conditional is
`P_s ∝ w_x(s) = ∏_{y∈NN(x)} φ(s,v_y)` and the `ν`-conditional is `Q_s ∝ w_x(s)/g_x(s)`,
`g_x(s) = ∏_{z : x∈A_z} Z(v|A_z)|_{v_x = s}`. In `Z²`, `z ∈ {x+e_1, x+e_2}` and
`g_x(s) = N(s, v_{x+e_1−e_2}) N(s, v_{x+e_2−e_1})`; in `Z³`, `z ∈ {x+e_j}` and
`g_x(s) = ∏_j Z_3(s, v_{x+e_j−e_k}, v_{x+e_j−e_l})`.
*(iii) Chain rule.* Let `Γ` be the graph `x ∼ y ⟺ y − x ∈ {±e_j} ∪ {±(e_j−e_k)}` — exactly
the pairs sharing an edge of `W` or a factor `Z(v|A_z)`. For `S` independent in `Γ`, both
conditional laws of `{v_x}_{x∈S}` given `v_{S^c}` factor over `S`, and dropping the `S^c`
term of the chain rule gives `D(μ_Λ‖ν_Λ) ≥ Σ_{x∈S} E_μ[D_x]`. Maximal densities in `Γ`:
`1/3` in `Z²` (attained by `x_1 + 2x_2 ≡ 0 mod 3`) and `1/4` in `Z³` (attained both by
`x_1 + 2x_2 + 3x_3 ≡ 0 mod 4` and by the bcc class `x_1 ≡ x_2 ≡ x_3 mod 2`); both are
maximal because `{x, x+e_1, x+e_2}` is a triangle and `{x, x+e_1, x+e_2, x+e_3}` a 4-clique
in `Γ` (C16, C16b).
*(iv) `Z²`.* `D_x` depends on the boundary only through the NN multiset (126 of them) and
the anti-diagonal pair (21 distinct tilt vectors), so `126 × 21 = 2646` exact evaluations
cover all `6⁶` boundaries. **The tilt is never constant** (C13), so no finite-energy factor
is needed, and `min D̂ = 537719/129443808050` (C13b): `1.0067×` `a3`'s
`c_2 = 19/4604256`, reached by a different inequality — an independent confirmation rather
than a gain. Rate `≥ (1/3)·537719/129443808050`.
*(v) `Z³`.* The tilt is constant on exactly 600 of the `6⁶` face-diagonal boundaries (there
`D_x = 0`), and on none of those is `v_{x+e_1−e_2} = v_{x+e_1−e_3}` (C14b, confirming
`a3`'s S8 by enumeration). *Finite energy:* condition on everything except `a = x+e_1−e_2`,
whose nearest neighbours exclude `b = x+e_1−e_3` (they differ by `e_3−e_2`); then
`μ(v_a = v_b | F) = ∏_y φ(v_b,v_y)/Σ_s ∏_y φ(s,v_y) ≥ 1/986`, because `φ ≥ 1` and the
maximum of `Σ_s ∏_{i≤6} φ(s,b_i)` over boundary multisets is `986 = 3⁶ + 1 + 4·2⁶` (C14,
attained at an all-equal boundary). So

    E_μ[D_x] ≥ (1/986) · min_{v_a = v_b} D̂ = (1/986)·29405471333306771/9669810101542139423160,

which is **`21.41×`** `a3`'s `c_3 = (1/986)²(4/28561)` (C14d). The gain is exactly one
factor of `986`: `a3` bounded `γ_min` separately *inside* the divergence, while (i) needs it
only once, for the event. Rate `≥ (1/4)` times the display.

## 3. Where the route stops

No step above fails, but the route closes neither end:
1. `m = 9268` against the converse `496`: the residual factor 18.7 is the gap between a
   product-form exponential test and the true Chernoff exponent of `μ` against `H`, which
   need not be a product over plaquettes because the adversary's optimum need not be.
2. The price sheet `G` is a numerically located point of a 6-dimensional exact
   optimisation, *reported* as an exact rational; nothing here shows it is optimal.
3. The scope of (a) is **disjoint** plaquettes — `a3`'s scope too. For plaquettes embedded
   in a connected lattice neither law factorises over them, so the product lemma of S3(i)
   does not apply and `V^m` is not available.
4. The `Z²` minimum is a relaxation: the NN multiset and the tilt pair are minimised
   independently, so some argmin combinations may not be simultaneously realisable and the
   true minimum can only be larger. The same caveat applies to `Z³`.

## 4. What would finish it

- An exact optimisation of the six price values (an exact-rational Chernoff problem), which
  would replace "`UV < 1` at this point" by "`inf UV` over the class".
- For embedded plaquettes, a block/spacing argument: a positive-density family of plaquettes
  far enough apart that S3(i) applies up to a controlled error.
- A matching converse over the hull: an adapted `ν` whose `TV` stays below `1/2` up to `m`
  of order `10³`, which would bracket the threshold to within a small factor.
- For `Z³`, computing `E_μ[D_x]` as a full average over all `6⁶` boundaries (rather than
  restricting to the event) would remove the `1/986` entirely.
