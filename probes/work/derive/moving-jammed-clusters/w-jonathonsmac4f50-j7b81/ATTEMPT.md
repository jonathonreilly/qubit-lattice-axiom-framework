# moving-jammed-clusters, attempt a1 — the surface decides, and the critical size runs the wrong way

**Provenance.** This attempt was written by Claude Opus 5 (`claude-opus-5`), worker
`w-jonathonsmac4f50-j7b81`, on task `J:derive:moving-jammed-clusters:a1`. There were no prior
attempts on this problem at claim time, so nothing here is a check of another worker's route; it
is a first pass. Several results in this campaign's block-39 lane were produced by the same model
family, including the neighbourhood-independence of the formation rate at `c_0` that I use in §2.4
— that is same-family input, not independent confirmation, and it should be re-derived by a
different family before it is leaned on.

## 1. What is claimed

The setting is block 39's, as the unit states it: a site is empty or carries one permanent record
whose content is one of six axes; two neighbouring records weigh `c·ω` with `ω = p, q, r` for equal,
opposite and orthogonal contents; a bond with an empty end weighs 1; the neutral scale is
`c₀ = 6/(p+q+4r)`. A record with `k` agreeing neighbours leaves with probability `1/(1 + (cp)^k)`,
and **a record with no empty neighbour cannot move at all**. Formation happens at an empty site `x`
at rate `z·Z_x`. Write `A_j = p^j + q^j + 4r^j`, so `Z_x = c^j A_j` at an empty site with `j`
aligned occupied neighbours, and `c₀ A_1 = 6`.

For a solid `L×L×L` box of aligned records in empty space:

**(a) Who moves, and how much is reachable.** The movable records are exactly the surface,
`6(L−2)² + 12(L−2) + 8`; the `(L−2)³` interior records can never move. The number of arrangements
reachable in **one** move is exactly `6L²` — the surface area — and is blind to the volume. Over
`T` sweeps, `log|reachable(T)| ≤ S·T·log(6S) = O(L² log L)` against
`log|configurations| ≥ V·log 7 = O(L³)`, so the fraction of its own configuration space that a
cluster can reach tends to 0.

**(b) Growth, evaporation, and the critical size.** On the six-neighbour stencil **every** empty
site touching a box has exactly **one** occupied neighbour — the sites diagonally outside an edge
or a corner are at distance √2 or √3 and are not neighbours at all — so growth is a pure quadratic
with no subleading terms, and all size dependence sits in evaporation:

```
G(L) = 6 z c A_1 L²
E(L) = 8/(1+(cp)³) + 12(L−2)/(1+(cp)⁴) + 6(L−2)²/(1+(cp)⁵)
```

Hence `G/E → z c A_1 (1+(cp)⁵)` and the survival criterion is a **critical coupling, free of any
size**:

```
z_c = 1 / ( c A_1 (1 + (cp)⁵) ) ,   which at the neutral scale is  1/(6(1 + (c₀p)⁵)).
```

The coefficient of `L` in `E` has numerator `12((cp)⁵ − 2(cp)⁴ − 1)`, so **the sign of the
finite-size correction flips exactly at the positive root `x*` of `x⁵ = 2x⁴ + 1`, `x* = 2.05597…`,
in the variable `x = cp`**, and the answer to the unit's question is opposite on the two sides:

| | `cp < x*` (weak alignment) | `cp > x*` (strong alignment) |
|---|---|---|
| `z > z_c` | grows at **every** size; no critical size | critical size `L*`, **repelling**: below it shrinks, above it grows — ordinary nucleation |
| `z < z_c` | critical size `L*`, **attracting**: below it grows, above it shrinks — a *maximum stable size* | shrinks at every size |

So "a size above which a cluster only grows" exists only for `cp > x*` and `z > z_c`. For
`cp < x*` the cluster does not run away: below `z_c` it settles at a finite size `L*(z)`, which
diverges as `z ↑ z_c`.

**(c) The interior.** The interior is frozen in three independent senses — its records cannot move
(no empty neighbour), their contents cannot change (records are permanent, one per site), and no
formation can occur there (no empty site). Combined with (a), every arrangement reachable in time
`T` has the *same* interior, so no reading of records in that time distinguishes two clusters with
equal surfaces and different interiors. The interior is readable only as the surface erodes down to
it — in principle recoverable, but only by destroying the cluster.

## 2. The steps

1. **PROVED / CHECKED — the census.** `L³ − (L−2)³ = 6(L−2)² + 12(L−2) + 8` symbolically, and the
   occupied-neighbour counts (face 5, edge 4, corner 3, interior 6) enumerated on the lattice at
   `L = 3,4,5,6`. The movable count matches `L³ − (L−2)³` at each.
2. **PROVED / CHECKED — the one-move count is the surface area.** A move carries a record across an
   occupied–empty bond; distinct bonds give distinct arrangements, so the reachable set after one
   move is in bijection with the boundary bonds. Brute-force enumeration of the distinct resulting
   configurations gives `24, 54, 96, 150` at `L = 2,3,4,5`, i.e. exactly `6L²`.
3. **PROVED — the reachable fraction vanishes.** The bound `log|reachable(T)| ≤ S T log(6S)` is the
   trivial one (at most `S` movers, `T` attempts, 6 targets); the ratio to `V log 7` tends to 0 by
   `sympy.limit`. This is an upper bound on reachability, not an estimate of it.
4. **CHECKED — the growth census.** Enumerated at `L = 2,3,4,5`: the touching empty sites are
   `{1: 6L²}` and nothing else. This is the step where my first draft was **wrong** — I had assumed
   `j = 2` edge-adjacent and `j = 3` corner-adjacent growth sites by analogy with 2D pictures, and
   the enumeration refuted it. With one aligned neighbour, `Z_x = c A_1`, giving the pure `6zcA_1L²`.
   **ASSUMED** here: the aligned-neighbourhood normalizer `Z_x = c^j A_j`, which is block 39's
   formation weight with all neighbours aligned; and that the cluster's surrounding records are
   aligned with it, which is the unit's "cluster of aligned records".
5. **PROVED / CHECKED — `z_c`.** `G/E → z c A_1 (1+(cp)⁵)` by `sympy.limit`; `c₀A_1 = 6` exactly.
6. **PROVED / CHECKED — the sign flip.** `12/(1+x⁴) − 24/(1+x⁵)` has numerator `12(x⁵ − 2x⁴ − 1)`
   (verified by `factor`), whose positive root is bracketed exactly between `2` and `21/10`.
7. **CHECKED — both regimes, with exact integer brackets.** At `(3,1,2)` (`c₀ = 1/2`, `cp = 3/2`,
   `z_c = 16/825`): at `z = (9/10)z_c` the crossing is `L* = 10.768`, with `G−E > 0` at `L = 10`
   and `< 0` at `L = 11` (attracting); at `z = z_c` and `z = (11/10)z_c`, `G−E > 0` at every size
   tested. At `(20,1,1)` (`c₀ = 6/25`, `cp = 24/5 > x*`): at `z ≤ z_c`, `G−E < 0` everywhere; at
   `z = (3/2)z_c` the crossing is `L* = 13.445`, with `G−E < 0` at `L = 13` and `> 0` at `L = 14`
   (repelling). All arithmetic is exact rational; only the printed decimals are floats.
8. **CHECKED — the census is a property of the box, not of convexity.** The ramp
   `{(i,j,k) ∈ [0,2]³ : i+j ≤ 2}` — a box cut by a half-space, hence convex — has touching-site
   census `{1: 36, 2: 6}`: its sloped face carries `j = 2` sites, which grow at `c²A_2`. So §1(b)'s
   numbers are stated for boxes, not for every convex cluster.
9. **ASSUMED — the dynamics.** I read "evaporation rate" as one departure attempt per surface
   record per sweep at the unit's stated transit probability, with a departed record leaving the
   cluster, and "growth rate" as `z Z_x` summed over the touching empty sites. The unit states the
   transit probability and the formation rate but not the sweep convention; a different convention
   rescales `G` and `E` by constants and moves `z_c` accordingly, but does not touch the `L`
   dependence, so (a), (c), the `x*` dichotomy and the *shape* of the table survive it. The numeric
   `z_c` values do not.

## 3. Where the route stops

- Only the **box** is done. Step 8 shows a convex cluster with a slanted face has `j = 2` growth
  sites, so the general convex statement needs a growth term summed over the shape's faces — the
  `x*` dichotomy is then a statement per face orientation, and I have not done it.
- The evaporation side counts **one attempt per record**, i.e. a mean-field rate, not the actual
  stochastic process. `L*` is therefore the deterministic balance point, not a nucleation rate; the
  fluctuation problem (how long a cluster of size `L < L*` survives) is untouched.
- A departed record is treated as lost. Re-attachment, and the vapour density it would build up
  around the cluster, are not modelled — with them `z` becomes self-consistent rather than a
  parameter.
- (a)'s reachable count is exact for one move and only a bound for `T > 1`. The true growth rate of
  the reachable set with `T` is open; the bound is enough for the vanishing-fraction statement and
  nothing more.
- (c) is a statement about what is *invariant*, not an information-theoretic one. "No surface
  reading distinguishes the interiors" is proved in the strong sense that the interior never enters
  the dynamics; quantifying what an observer learns from the erosion sequence is not attempted.

## 4. What would finish it

1. Redo §1(b) for a general convex box-like cluster `L₁×L₂×L₃` and then for a faceted convex shape,
   with the growth term summed per face orientation with its own `j`. The prediction to test is
   that `x*` moves per orientation and the dichotomy becomes a per-face condition.
2. Replace the mean-field balance by the actual birth–death chain in `L` and compute the mean
   survival time below `L*` on each side of `x*`. The attracting case predicts a *stationary* size
   distribution peaked at `L*`; the repelling case predicts Arrhenius escape. That is a sharp,
   simulable difference — `probes/lib/moving_gas.py p q r scale rho L sweeps seed` is the obvious
   instrument, and neither prediction has been run.
3. Close the self-consistency: let `z` be set by the vapour the cluster itself emits, and ask
   whether the attracting `L*` survives it.
4. Re-derive step 4's normalizer and the `c₀` neutrality with a different model family before the
   numbers are used downstream.

## 5. Running it

```
python3 probes/work/derive/moving-jammed-clusters/w-jonathonsmac4f50-j7b81/check.py
```

Standard library plus `sympy`. 33 checks, all exact rational or integer arithmetic; runs in a few
seconds. It prints `ok`/`FAIL` per check and then a `SUMMARY:` and `HIT:` line.
