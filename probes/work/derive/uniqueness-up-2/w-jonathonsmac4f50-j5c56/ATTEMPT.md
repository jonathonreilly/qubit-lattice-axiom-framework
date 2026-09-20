# uniqueness-up-2: derivation attempt 4 of 4

Worker `w-jonathonsmac4f50-j5c56` (claude-opus-5), unit `J-derive-uniqueness-up-2-a4`.

**Provenance, stated because it bears on independence.** The one prior attempt, `a3`
(`w-jonathonsmac4f50-j96fc`), is by the same model family, machine and running worker. It took the
task's route (i) in its one-site form to `p = 5.26` and concluded "the one-site constant cannot
see" the alignment. I do not re-derive it and I do not try to beat `5.26`.

**What this attempt is.** The task lists three routes above `5.11`. Route (ii) —
disagreement percolation — is a substantial build: a domination argument, an exact enumeration
over two levels, and a percolation estimate. **Before a unit is spent building it, it is worth
knowing what it can deliver.** That is a cheap calculation, and the answer is: about `p = 5.9`,
which is `0.6` above `a3` and a long way below the located `10.5`. The route's own ingredient
rules it out at `10.5`, by 50 per cent.

## 1. The statement attempted

Route (ii)'s ingredient is the **site-wise maximal-coupling failure rate**: with one parent
disagreeing and the others equal, the two children can be coupled except on a set of probability
`α₃(p)`, the largest total variation between two three-parent kernels differing in one parent.
Under that coupling the disagreement set is dominated by **oriented site percolation with
parameter `α₃` on the level-ordered `Z³` DAG** (each site has the three parents `x − e_i`; a level
is the 2D triangular lattice). Memory is lost whenever the cluster dies out, i.e. whenever
`α₃(p) < q_c` of that percolation.

> **(i)** `α₃` exactly on `(p,1,2)`: `0.38791` at `p = 5`, `0.42081` at `p = 23/4`, `0.43370` at
> `p = 6`, `0.48649` at `p = 7`, **`0.65303` at `p = 21/2`**.
>
> **(ii)** `q_c` of that percolation, measured: **between `0.425` and `0.43`** (survival `0.000`
> at `0.425` over 600 levels and 200 runs, `0.015` at `0.43`, `0.367` at `0.45`).
>
> **(iii)** So **route (ii)'s ceiling is `p ≈ 5.9`** — the crossing lies between `23/4` and `6`.
>
> **(iv)** Reaching the located `10.5` would need `q_c ≥ 0.653`, half again the DAG's actual
> threshold. **The route does not fail narrowly there; it fails in its own ingredient**, and no
> sharpening of the percolation estimate can close it, because `q_c` is a property of the DAG and
> `α₃` a property of the rule.

## 2. Steps

**S1 (PROVED; CHECKED `N1`). The ingredient.** `α₃` is computed exactly over all `6³` parent
configurations and all `3 × 5` single-parent changes, in rationals. It increases along the line:
the coupling gets harder as `p` grows, which is the whole difficulty.

**S2 (PROVED). The domination.** Couple the two processes site by site with the maximal coupling,
independently across a level given the level below. A site whose parents all agree is coupled
with probability one. A site with at least one disagreeing parent fails to couple with
probability at most `α₃` per disagreeing parent, and at most `α₃` by the one-parent bound if we
ask only "does this site disagree at all". So the disagreement set at level `t+1` is contained in
`{x : some parent of x disagrees} ∩ {x open}` with the open sites independent of parameter `α₃` —
oriented site percolation. This is the standard disagreement-percolation domination; the only
input is the per-site bound.

**S3 (CHECKED `N2`, numerical and labelled). The threshold.** Starting from one disagreeing site,
survival to level `T` is `0.000` at `q = 0.40, 0.42, 0.425`, `0.015` at `0.43`, `0.367` at `0.45`
and `0.683` at `0.50` (fixed seed, `T = 400`–`600`, `120`–`200` runs, `L = 210`–`260`). So
`q_c ∈ (0.425, 0.45)`, and the `0.43` run puts it just below `0.43`.

**S4 (CHECKED `N3`). The ceiling.** `α₃(23/4) = 0.42081 < q_c < 0.43370 = α₃(6)`, so route (ii)
certifies to about `p = 5.9`.

**S5 (CHECKED `N4`). The no-go at the located value.** `α₃(21/2) = 0.65303`. For a percolation
criterion with this ingredient to certify `p = 10.5` the DAG would have to percolate only above
`0.653`; it percolates above about `0.428`.

**S6 (CHECKED `N5`). The four criteria.**

| criterion | reaches | source |
|---|---|---|
| branching / Dobrushin, `3α₃ < 1` | `p < 3.7564` | exact; my `causal-clauses` a3 |
| one-site averaged Wasserstein | `p ≤ 5.26` | attempt `a3` of this task |
| disagreement percolation, `α₃ < q_c` | `p ≈ 5.9` | this attempt, measured |
| executed, located | `p ∈ (10.5, 11)` | block 28, PR #8172 |

Every criterion whose ingredient is the **one-site** coupling failure rate sits in `[3.76, 5.9]`.
The three differ only in how cleverly they combine the same number, and the combination is worth
at most a factor `1.6`. The located value is a further factor `1.8` away.

## 3. Where the route stops

- **`q_c` is measured, not bounded.** A certificate needs a rigorous lower bound on `q_c`, and the
  only easy one is the branching bound `1/3`, which gives back `p < 3.7564`. So as it stands this
  attempt is a **feasibility calculation for route (ii), not a certificate**: it says what the
  route would deliver if the percolation estimate were made rigorous, and that this is not worth
  much. That is its purpose.
- **S2's per-site bound is the crude one.** A site with two or three disagreeing parents fails
  with more than `α₃`, and one with one disagreeing parent often less; a sharper domination would
  use the whole profile. That refines the constant, not the conclusion, because even `q_c = 0.5`
  would only reach `p ≈ 6.7`.
- **The alignment is still invisible.** `a3`'s diagnosis stands: the ingredient is a worst-case
  single-site quantity and the large-`p` law is ferromagnetically aligned, so the worst case is
  never typical. Routes (i)-with-blocks and (iii) are the ones that can see it; route (ii) cannot,
  whatever constants it is given.

## 4. What would finish it

1. **Do not build route (ii) for its own sake.** Its ceiling is `5.9`.
2. Route (i) with real blocks and an exact LP over the block metric is the remaining cheap route;
   the block metric can charge a disagreement differently according to its neighbours, which is
   the first thing in this family that can see alignment.
3. If a percolation route is wanted anyway, the object to bound is not `α₃` but the *conditional*
   failure rate given an aligned environment — which is a different quantity and much smaller at
   large `p`.

## 5. Running it

```
python3 probes/work/derive/uniqueness-up-2/w-jonathonsmac4f50-j5c56/check.py
```
from the repository root. `numpy` for the percolation runs; the rest is the standard library.
About three minutes, almost all of it in the six percolation ensembles.
