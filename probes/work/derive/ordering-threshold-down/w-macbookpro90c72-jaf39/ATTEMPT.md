# ordering-threshold-down: derivation attempt 1 of 5

Worker `w-macbookpro90c72-jaf39` (claude-opus-5), unit `J-derive-ordering-threshold-down-a1`.

Objects come from block 30 (PR #8174): the two-level automaton `η'` on the level
lattice, the deviations `d_1, d_2, d_3`, `ε₁ = d_1`, `ε₂ = max(d_2, d_3)`, and the
closed forms, on a general positive weight triple `(p, q, r)`

    d_1 = 1 − p³/(p³ + q³ + 4r³),
    d_2 = 1 − p²q/(pq(p+q) + 4r³),
    d_3 = 1 − p²r/(r(p² + q²) + r²(p+q) + 2r³),

which on the line `(p, 1, 2)` are

    d_1 = 33/(p³ + 33),   d_2 = (p + 32)/(p² + p + 32),   d_3 = (2p + 11)/(p² + 2p + 11).

`d_1 = 1 − K(a | a,a,a)`, `d_2 = 1 − K(a | a,a,−a)`, `d_3 = 1 − K(a | a,a,b)`: the
chance a site leaves the consensus axis `a` when all three, or two, of its
predecessors carry it. In the two-level domination a site is a *1-site* when it is off
`a`, so `ε₁ = d_1` is the flip rate with no 1-predecessor and `ε₂ = max(d_2, d_3)`
dominates the flip rate with exactly one, and two 1-predecessors make a 1-site
outright. That automaton is what `η'` means below.

The history construction, the move alphabet `d ∈ {1,2,3}³`, the bad-pair count
`b(d) = #{k : d_k = k}` and the potential constraint are round 1's refereed GIVEN,
`probes/work/derive/beyond-the-union-bound/w-jonathonsmac4f50-jae8a/ATTEMPT.md`.

**Provenance and independence.** The GIVEN I build on (`jae8a`) is claude-opus-5, as is
the only round-2 sibling on `origin/ai/probes` when I wrote this
(`w-jonathonsmac4f50-jc31e`, attempt 4). This attempt is *not* independent of either.
It is written after reading `jc31e`, deliberately: `jc31e` proves a no-go that rules
out the route I had planned before reading it (a recursion typed by pole
configuration), so re-walking it would have been waste. What is taken from `jc31e` is
cited at each use; nothing of `jc31e`'s is restated as mine.

## 1. The statement attempted

The task asks for a proved threshold below 58 on `(p, 1, 2)`. **None is proved here.**

The lever attempted is the second of the four gaps `jae8a` §4 names and nobody has
priced: *a processed pole's move is counted as one of two free choices, although that
pole needs a second 1-predecessor that is never charged.* This attempt turns that
sentence into a scalar and computes with it.

**(A) The refined criterion.** Let `w` be a price charged once for each move a pole
makes out of a site with two or more 1-predecessors. Summing the refinement histories
with this price in place of the free choice, the fork-free sum is *exactly*

    Σ_R  C(3R, R) · ε₂^R · (2ε₂ + 2w)^{2R},

which converges iff

    27 · ε₂ · (ε₂ + w)² < 1.                                            (★)

At `w = 1` — today's accounting, where the move is free — (★) is `27 ε₂ (1 + ε₂)² < 1`,
weaker than the `27 ε₂ < 1` of the current route, because the refined alphabet also
resolves the amplifying free moves that the current alphabet leaves implicit. The
refinement pays as soon as `w < 1 − ε₂`.

**(B) The price sheet.** (★) is an exact statement about one scalar, so the prize of
gap 2 can be read off. On `(p, 1, 2)`, writing `w*(p) = (27 ε₂)^{-1/2} − ε₂`:

| target | `ε₂` | `w` must be below |
|---|---|---|
| `p ≥ 58` (today's ceiling) | `127/3491` | `0.9726` |
| `p ≥ 40` | `91/1691` | `0.7757` |
| `p ≥ 20` | `52/452` | `0.4523` |
| `p ≥ 14` | `23/121` | `0.2513` |
| `p ≥ 13` | `45/214` | `0.2093` |
| `p ≥ 11` (located) | `43/164` | `0.1136` |

A price anywhere below `0.972` already beats 58. This is the quantitative content of
gap 2 and it is new: `jae8a` §4 names the gap, `jc31e` §4 names it again, neither
prices it.

**(C) The floor: `w ≥ ε₂`, so this scheme's own ceiling is `p ≥ 14`.**
No uniform price below `ε₂` is valid. The second predecessor `z` and the followed
predecessor `y` of a deterministic move are siblings and share exactly one
predecessor `c`; whenever the chain's next move is toward `c`, the chain's own content
forces `c ∈ S`, and then `P(z ∈ S | history) ≥ ε₂` by monotonicity, because the noise
variable at `z` is not used by the chain. Substituting `w = ε₂` in (★) gives

    108 ε₂³ < 1,

i.e. `ε₂ < 108^{-1/3}`, i.e. `p ≥ 14` on `(p, 1, 2)`: exactly, `108·45³ = 9841500 >
214³ = 9800344` (fails at 13) and `108·23³ = 1314036 < 121³ = 1771561` (holds at 14).
So gap 2, priced as tightly as it can be priced, is worth `58 → 14`, and no further.
It lands on the independently found pair-kernel threshold `(−2+√7)/3` of round 1's
attempt 2 (`p ≥ 13 or 14`), by a different route.

**(D) The naive bootstrap is refuted, twice.** Charging the unconditional density,
`w = θ ≈ ε₁`, is the obvious thing to try and it is wrong. (C) refutes it structurally
(`ε₁ < ε₂` on the whole line). It is also refuted numerically: `w = ε₁` makes (★) first
hold at `p = 10`, below the located strength `p ∈ (10.5, 11)`, so it would prove
stability where the law is not stable.

**(E) Monotonicity is exactly block 30's T1(a).** The local rule is nondecreasing in
its predecessor configuration for every value of the site's noise variable **iff**
`ε₁ ≤ ε₂`. So T1(a) is not bookkeeping: it is the attractiveness of `η'`, and it is
what makes Harris-FKG, the coupling, and the floor in (C) available. On `(p, 1, 2)` it
holds for every `p ≥ 1`; at `(1, 2, 1)` it fails, `d_1 = 12/13 > 9/10 = max(d_2, d_3)`,
and there `η'` is not attractive. This is the confirmed defect the task flags,
established on the lines used, with its reason.

**(F) Scope — what (A)-(E) are statements about.** (★) is an exact statement about the
*refinement sum* with the price `w` inserted; it is not yet a bound on the error
probability. The step that would make it one is S3's multiplication of the prices
along the chain, and §3 shows that step fails: the uncharged second predecessor shares
a predecessor with the one the chain follows, so its witness overlaps the chain's and
van den Berg-Kesten is denied, while Harris-FKG runs the wrong way. So (B), (C) and
(D) say what gap 2 is worth *if* the prices multiply, and what price a multiplying
argument would have to beat; (E) and the floor in (C) stand on their own. The task's
exhaustive small-cone check is carried out in S9 and is what exhibits the second,
independent limit of scope: at coincident poles the per-charge price counts one noise
variable three times.

## 2. Steps

**S1 (PROVED). `η'` is attractive iff `ε₁ ≤ ε₂`.**
Realise `η'` from i.i.d. uniforms `U_y`: a site `y` at level `t` is a 1-site iff

    f(n_y, U_y) = 1,   f(n, U) = 1{n ≥ 2} + 1{n = 1}·1{U < ε₂} + 1{n = 0}·1{U < ε₁},

`n_y` = number of 1-predecessors of `y`. `f(·, U)` is nondecreasing in `n` for every `U`
iff `f(0,U) ≤ f(1,U)` for every `U`, i.e. iff `1{U < ε₁} ≤ 1{U < ε₂}`, i.e. iff
`ε₁ ≤ ε₂`; the remaining comparison `f(1,U) ≤ f(2,U) = 1` is free. `n_y` is a
nondecreasing function of the predecessor configuration, so under `ε₁ ≤ ε₂` the level
map is monotone and `η'` started from the all-`a` level 0 is a monotone function of the
i.i.d. family `(U_y)`. Consequences used below: (i) Harris-FKG on `(U_y)`, (ii) for any
site `z` and any event `H` measurable with respect to noise variables other than `U_z`
and implying that some predecessor of `z` is a 1-site, `P(z is a 1-site | H) ≥ ε₂`,
because on `{U_z < ε₂}` the site `z` is a 1-site whenever `n_z ≥ 1`, and `U_z ⟂ H`.
This is exactly the hypothesis of block 30's T1(a); T1(a) is attractiveness.

**S2 (CHECKED, `D1`/`D2`). T1(a) on the lines used.**
On `(p, 1, 2)`, over positive denominators,

    num(d_2 − d_1) = p²(p − 1)(p + 33),
    num(d_3 − d_1) = p²(2p² + 11p − 33),
    num(d_2 − d_3) = p²(21 − p),

so `d_1 ≤ d_2 ≤ max(d_2, d_3)` for every `p ≥ 1`, with `d_3 ≥ d_1` only from `p ≥ 3`
and `ε₂ = d_2` for `p ≤ 21`, `ε₂ = d_3` for `p ≥ 21`. (The three numerators are
`jc31e`'s S1; `check.py` re-derives them from the closed forms rather than quoting
them.) T1(a) is not a general fact about positive weights: at `(1, 2, 1)`,
`d_1 = 12/13 > 9/10 = max(d_2, d_3)`, so there `η'` is *not* attractive and S1's
consequences — including everything block 30 and this attempt build on them — are
unavailable. This is the defect the task flags, with the reason it matters.

**S3 (PROVED given the GIVEN). The refined move alphabet.**
Take `jae8a`'s history construction as GIVEN: three charges, one refinement moves all
three, charge `k` moving in direction `d_k` is *bad* iff `d_k = k`, and a fork-free
chain satisfies `B = R` (`B` = total bad moves, `R` = refinements). Fix the choice rule
"charge `k` moves to a 1-predecessor in a direction `j ≠ k` whenever one exists".
Then each charge-move at a pole `P` is of exactly one type:

* **T1**, `P` has exactly one 1-predecessor, in direction `j`. Then `P` is a 1-site
  only through its own `ε₂`-noise, so this move carries the factor `ε₂`, for each of
  the three possible `j`; it is bad iff `j = k`.
* **T2**, `P` has two or more 1-predecessors. Then `P` is a 1-site with no noise at
  `P`, and the rule moves in one of the `2` directions `j ≠ k`; the move is never bad.
  The move consumes a *second* 1-predecessor `z ≠ P − e_{d_k}`, which the current
  accounting never charges. Let `w` be a price charged for it.

Marking bad moves with `r`, one charge-move contributes `g(r) = ε₂(r + 2) + 2w`, and
one refinement contributes `g(r)³`. Under the current accounting a free move carries
`1` and does not resolve T1 from T2, i.e. `g_old(r) = ε₂ r + 2`.

**S4 (PROVED + CHECKED, `G1`/`G2`). The exact sum and its rate.**
`[r^R] g(r)^{3R} = C(3R, R) · ε₂^R · (2ε₂ + 2w)^{2R}` — one term, because `g` is linear
in `r`. `check.py` verifies the identity symbolically for `R = 1..6`. The Chernoff
bound `C(3R,R) ≤ (1+z)^{3R} z^{-R}` at `z = 1/2` gives `C(3R,R) ≤ (27/4)^R`.  For the
matching lower bound, the `3R+1` terms of `Σ_k C(3R,k) 2^{-k} = (3/2)^{3R}` have ratio
`C(3R,k+1)2^{-(k+1)} / C(3R,k)2^{-k} = (3R−k)/(2(k+1))`, which is `≥ 1` exactly when
`k ≤ R − 2/3`; so the terms increase up to `k = R` and decrease after, the largest is
the one at `k = R`, and `(3/2)^{3R} ≤ (3R+1)·C(3R,R)2^{-R}`, i.e.
`C(3R,R) ≥ (27/4)^R/(3R+1)` (also checked exactly for `R ≤ 200`).  Hence

    ( Σ_R-term )^{1/R} → 27 · ε₂ · (ε₂ + w)²,

and the fork-free refined sum converges iff (★). The same extraction on `g_old` gives
`C(3R,R) ε₂^R 4^R → 27 ε₂`, reproducing the present ceiling exactly; so (★) is the one
scalar generalisation of `27 ε₂ < 1`, and the refinement pays iff `w < 1 − ε₂`.

**S5 (CHECKED, `G3`/`P1`). Price sheet.** §1(B), each row an exact rational witness
`w` with `27 ε₂ (ε₂ + w)² < 1` verified in exact arithmetic, and `27 ε₂ < 1` first at
`p = 58` (`d_3(57) = 125/3374 > 1/27 ≥ 127/3491 = d_3(58)`) reproduced as a control.

**S6 (PROVED). The floor `w ≥ ε₂`.**
Let a T2 move happen at pole `P` with 1-predecessors `P − e_i` and `P − e_j`, the rule
following `y = P − e_j` and leaving `z = P − e_i` uncharged. Then `z − y = e_j − e_i`,
so `y` and `z` are siblings, and they share exactly one predecessor,

    y − e_i = P − e_j − e_i = z − e_j =: c.

Whenever the chain's next move out of `y` is in direction `i`, the chain's own content
asserts `c` is a 1-site, and `c` is a predecessor of `z`. The noise variable `U_z` is
not used by the chain (`z` is not a pole and not a seed of it). By S1(ii),
`P(z is a 1-site | chain) ≥ ε₂`. So no uniform price below `ε₂` is valid, and the
direction `i` is one of the two the rule may take, so this is not a rare configuration.

**S7 (CHECKED, `F1`). The scheme's ceiling is `p ≥ 14`.**
`w = ε₂` in (★) is `108 ε₂³ < 1`. On `(p,1,2)`: at `p = 13`, `108·45³ = 9841500 >
9800344 = 214³`, so (★) fails; at `p = 14`, `108·23³ = 1314036 < 1771561 = 121³`, so
(★) holds. Gap 2 is worth `58 → 14` and no more. The coincidence with round 1 attempt
2's pair kernel `(−2 + √7)/3 = 0.21525` versus `108^{-1/3} = 0.20999` is not an
identity; two different routes bracket the same place.

**S8 (CHECKED, `F2`). The unconditional-density bootstrap is refuted.**
Charging `w = θ = ε₁` — "the second predecessor is a 1-site with the density we are
bounding" — makes (★) first hold at `p = 10` (`p = 9`: `27 d_2 (d_2+d_1)² > 1`;
`p = 10`: `< 1`), below the located strength `p ∈ (10.5, 11)`: it would prove the law
stable where it is not. S6 says why independently: the true conditional price is at
least `ε₂`, and `ε₁ < ε₂` on the whole line by S2. FKG (S1) is the mechanism — the
conditional density of a second 1-predecessor given the chain is larger than the
unconditional one, and Harris-FKG only ever pushes it the wrong way.

**S9 (CHECKED, `C1`/`C2`/`C3`). Exhaustive small cones, and the exact scope of (★).**
The backward cone of a site at level `T` has `C(m+2,2)` sites at depth `m`, so
`C(T+2,3)` noise variables above level 0. `check.py` resolves the exact law of the
whole cone level by level in rational arithmetic — every one of the `2^{C(T+2,3)}`
noise outcomes, `T = 1, 2, 3, 4` (`1, 4, 10, 20` variables) — and reports
`P_T = P(top site is a 1-site)` as an exact rational at `(p,1,2)`, `p ∈ {11,14,58,84}`.
Two facts come out, and they fix the scope of (★) rather than confirming a bound:

1. `P_2 = ε₁(1−ε₁)³ + 3ε₂ε₁(1−ε₁)² + 3ε₁²(1−ε₁) + ε₁³` exactly (closed form checked
   against the enumeration). Its `ε₁ε₂` term is `3ε₁ε₂`; the refined fork-free weight
   at `R = 1` is `12 ε₁ ε₂ (ε₂ + w)²`, which is *smaller* once `ε₂ + w < 1/2` — at the
   floor `w = ε₂` that reads `ε₂ < 1/4`, i.e. `4(p+32) < p² + p + 32`, i.e.
   `p² − 3p − 96 > 0`, i.e. `p ≥ 12` (`C2`: `−8` at 11, `+12` at 12). So the
   per-charge price is **not** valid where the three poles coincide: one refinement out
   of a single site consumes one noise variable, not three — `jae8a` §4's fourth gap.
   (★) is the **separated-pole** rate, which is where `jc31e` S6 locates the ceiling.
2. The `ε₁²` terms of `P_2` are two-seed terms. The fork-free sum does not contain
   them; a complete bound carries `jae8a`'s fork factor `c = 6ε₁/σ` on top of (★).

`check.py` also verifies `P_1 ≤ P_2 ≤ P_3 ≤ P_4` at each `p` (a consequence of S1 that
the enumeration could have falsified), and verifies S6 on real finite data: in the
`T = 4` cone it computes the exact conditional `P(z is a 1-site | c is a 1-site)` for
the sibling pair `y = x−(1,0,0)`, `z = x−(0,1,0)`, `c = x−(1,1,0)` of S6 and checks
`P(z | c) ≥ ε₂ > P(z)` at `p ∈ {13,14,58,84}` — the floor of S6 and, in the same two
inequalities, the fact that the correlation runs the wrong way for a product bound.

## 3. The first step that fails

**S3 fails, at the multiplication.** S3 assigns the price `w` to each T2 move and then
multiplies the prices along the chain, as if the events

    E_m = { the uncharged second predecessor z_m of the m-th T2 move is a 1-site }

occurred disjointly from one another and from the chain's own `ε₂`-noise. S6 proves
`P(E_m | chain) ≥ ε₂`, which is the bound in the wrong direction: it forbids a small
price, it does not license any price. For (★) to be a bound one needs the *upper*
factorisation

    P( chain ∧ E_1 ∧ … ∧ E_D )  ≤  P(chain) · w^D,

and the geometry of S6 is exactly what denies it. `z_m` is a sibling of the followed
predecessor `y_m` and shares the predecessor `c_m = P_m − e_i − e_j` with it. When the
chain's next move is toward `c_m`, the witness for `E_m` that S6 exhibits is the pair
`(c_m ∈ S, U_{z_m} < ε₂)` and `c_m` is a pole of the chain: the witness for `E_m` and
the witness for the chain *overlap in `c_m`*, so `E_m` and the chain do not occur
disjointly and van den Berg-Kesten gives nothing. S1 makes this worse rather than
better: both events are increasing in `(U_y)`, so Harris-FKG runs the wrong way,
`P(chain ∧ E) ≥ P(chain)P(E)`, and no product closure is available. The same collision
recurs between consecutive T2 moves when their poles are within two steps, which the
chain does not forbid.

So the price `w` is real — S6 shows the second predecessor costs at least `ε₂` — but
nothing here shows the costs *multiply*. (★) is a criterion for a sum that has not been
proved to dominate the error probability, and §1(B), §1(C), S7 and S8 are statements
about that sum, not about the law.

A second, independent failure of scope is S9.1: at coincident poles the per-charge
price triple-counts a single noise variable, and the exhaustive `T = 2` cone exhibits
the exact discrepancy (`3ε₁ε₂` against `12ε₁ε₂(ε₂+w)²`). This one is confined to a
finite prefix — `jc31e` S6 and `jae8a` §4 both locate the `1/27` ceiling at separated
poles — but it means (★) cannot be read as a bound on `P_T` for small `T`.

`SUMMARY: ROUTE FAILS AT S3 (the prices do not multiply: BK is denied by the shared
predecessor c, and FKG runs the wrong way).`

## 4. What would finish it

1. **A BK-legal witness for the second predecessor.** The price multiplies if `E_m` can
   be witnessed on a set of noise variables disjoint from the chain's and from the
   other `E_l`'s. S6's witness fails precisely because it reuses the pole `c_m`. What is
   needed is a bound of the form `P(E_m | F_m) ≤ w` for a filtration `F_m` generated by
   the chain's variables up to step `m` — a *conditional* upper bound, not the
   unconditional `θ`, which S8 refutes. Since S6 gives `P(E_m | F_m) ≥ ε₂` and S7 shows
   `w = ε₂` still reaches `p ≥ 14`, the whole prize of this lever survives if and only
   if such a conditional bound can be proved with `w = ε₂ + o(1)`. Note what is being
   asked for: the second predecessor is *typical*, not rare, so the bound must come
   from the chain carrying no information about `U_{z_m}` beyond one shared ancestor —
   a two-block decoupling, not an inclusion-exclusion.
2. **The tree-graph term for the shared ancestors.** `jc31e` §4 asks for exactly this
   under route (i): "BK for disjointly occurring pieces plus a tree-graph bound for
   shared ancestors, since positive correlations defeat product closures". The shared
   ancestor here is a single site `c_m` per T2 move, so the correction is one factor
   per move and is a candidate for absorption into `w`; the open part is the
   between-move collisions.
3. **A finite coincident-pole prefix.** S9.1 needs the first few refinements priced
   with one noise variable per coincident cluster (`jae8a`'s `3 + 3r` pattern count)
   and the separated-pole rate applied only past the cluster-breaking depth. This is
   bookkeeping, not a new idea, but it has to be written down for any statement about
   `P_T`.
4. **Then the fork factor.** S9.2: multiply the fork-free rate by `jae8a`'s
   `c = 6ε₁/σ`, or redo the `Z̄ ≥ 1 + μZ̄/(1 − cZ̄)³` fixed point with `μ` replaced by the
   refined `27 ε₂ (ε₂ + w)²`. At `w = ε₂` and `p = 14` there is no margin
   (`108 ε₂³ = 0.7417`), so the fork factor will move the threshold up; the honest
   reading of S7 is that this lever alone reaches the middle teens at best, and the
   located strength `p ∈ (10.5, 11)` needs a second lever — `jc31e`'s route (iii),
   a block renormalisation.
