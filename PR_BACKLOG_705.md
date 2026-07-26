# Cycle 705 — BACKLOGGED

Branch: `physics-loop/confusability-floor-20260725`
Science commit: `6cf0dcf0eb` · loop pack: `918e6a0fd9`
Runner: 9 PASS / 0 FAIL, cold-run at `6cf0dcf0eb` in an isolated worktree,
receipt pinned to the committed blob (`ac7e3450...`, PIN MATCH).

Cluster-cap evaluator (codex `gpt-5.6-sol`, xhigh): **BACKLOG**. All three
objections accepted.

## What survived

The evaluator independently confirmed the load-bearing arithmetic:

> "The central orbit geometry is correct. For `R_x, R_y, R_z`, the dot products
> are exactly `x^2, y^2, z^2`, summing to `|v|^2`. For every non-face direction
> all three rotations produce distinct orbit points, so one overlap is at least
> `(1+1/3)/2 = 2/3`. The face exception is handled correctly."

So the exact content — face 1/2, corner 2/3, edge 3/4, every size-24 orbit
`>= 2/3`, the quarter-turn identity, and the uniqueness of the face orbit as
the only orbit below 2/3 — stands.

## Error 1 (flat, mine) — the chirality/distinguishability claim is false as restated

Theorem 5 was stated correctly in the theorem block, qualified to "a chiral
`A0` **built on a single unpaired free orbit**". But the "Why this bears on the
residual" section restated it without the qualifier:

> "a chiral alphabet ... contains no perfectly distinguishable pair whatsoever"

That is **false**. Take `A0` = (unpaired free orbit) ∪ (face orbit). Inversion
maps the free orbit to its disjoint twin and fixes the face orbit, so `A0` is
chiral — yet it contains the face orbit's antipodal pairs, which are perfectly
distinguishable. The evaluator constructed exactly this counterexample.

This is the same failure mode as cycles 701, 702 and 704: **the exact
arithmetic was right and the prose restatement of it overreached.** The
qualified theorem and the unqualified sentence were both in the same document.

## Error 2 (overclaim) — `conf` is not "a functional the framework already carries"

The overlap identity `Tr(P_v P_w) = (1 + v.w)/2` *is* forced by `Cl(3,0)`, and
that part of the defence holds. But `conf` = **max over pairs** adds two things
the framework does not supply:

1. the **aggregation** (worst pair, rather than mean, or spectrum, or count);
2. the **preference direction** (that less is better).

I named the minimization premise as unadopted but never named the aggregation
choice at all, and the note and value gate both called `conf` framework-carried.
Under the owner's standing bar — *"I don't want to accept a counting convention
unless it's so obvious it's stupid not to"* — that is exactly the move being
warned against, and the evaluator was right to call it.

## Error 3 (rigor gap) — finiteness was assumed silently

The parents do not make `A0` finite or closed, so "max over distinct pairs"
may not exist; the statement needs `sup`, or a named finiteness premise. The
floor itself survives the fix (any infinite invariant `A0` contains a non-face
point, so `sup >= 2/3` by the same quarter-turn argument), but the note as
written did not say so.

## The objection that actually matters, and the honest successor

The deepest objection is not any of the three above. It is this: **the
asymmetry I found is objective-dependent, and I chose the objective.**

Confusability prefers the achiral face orbit (1/2 vs `>= 2/3`). But alphabet
richness — a no less natural preference — prefers the 24-element chiral orbit.
So "the two sides of Residual 1 are no longer symmetric" is not established;
what is established is that *one particular optional objective* ranks them.

The honest successor is therefore a **no-go, not a positive claim**:

> Compute the complete pairwise-overlap spectrum of every proper-cubic content
> orbit — a complete invariant, so *every* objective is a function of it — and
> show that the orbit geometry does not break the Residual-1 symmetry, because
> monotone objectives of that data rank the two sides in opposite directions.

That closes off a route rather than claiming a result, which is the right shape
for this surface and matches the campaign's standing guidance to mine no-gos
for their escape conditions. Its own risk, named up front: "reasonable
objective" is undefined, so the no-go must quantify over an explicitly stated
class of objectives or it proves nothing.

**Not attempted tonight.** Starting a sixth cycle at 23:45 after five
consecutive gate rejections would be filling a quota, and the brief is explicit
that a thin PR is worse than none.

## Recovery

```
git fetch origin physics-loop/confusability-floor-20260725
git checkout physics-loop/confusability-floor-20260725   # 918e6a0fd9
python3 scripts/physical_first_alphabet_confusability_floor_cycle705_2026_07_25.py
```

To salvage rather than restart: drop every claim about Residual 1, drop `conf`
as a named functional, retitle to the overlap-geometry classification of
proper-cubic content orbits, state the finiteness premise, and fix the
Theorem 5 restatement. That is a bounded classification note of the same shape
as the landed cycle-697 salvage — but it should only be opened if a reviewer
judges the classification itself worth banking, since with the Residual-1
framing removed it is close to thin.
