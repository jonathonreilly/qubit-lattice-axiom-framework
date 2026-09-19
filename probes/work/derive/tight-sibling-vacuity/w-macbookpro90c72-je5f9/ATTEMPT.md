# J:derive:tight-sibling-vacuity:a4 — independent attempt

Worker `w-macbookpro90c72-je5f9`, model `claude-opus-5`.
Check: `probes/work/derive/tight-sibling-vacuity/w-macbookpro90c72-je5f9/check.py`
(44 exact checks, exit 0, `SUMMARY: COUNTEREXAMPLE`).

## 1. The exact statement attempted

> A processed site with at least two processed 1-predecessors cannot have all of
> them tight (rooted value 0).

If it held, the open lemma of block 33 (PR #8177) would be vacuously true and the
unit budget `c* = 1` would follow.

**Result: the statement is false.** An explicit realization has a processed site
whose three 1-predecessors are all processed and all tight. So the conjecture is
refuted, the open lemma is *not* vacuous, and — worse for the route — the lemma
itself and the rooted inequality (H) are both false at that site.

This is an independent attempt: I built my own plan and my own machinery before
reading the prior attempt, and I reproduce every value by a method that uses
neither `probes/lib` nor an MILP. Where I land on the same witness as attempt a2
I say so in §7 and separate out what is new.

## 2. Definitions used (block 33 note, PR #8177 branch)

Sites `z` in `Z^3`; `level(z) = z0+z1+z2`; `preds(z) = {z - e_j}`; fork offsets
`e_i - e_j`, `i != j`. The automaton sweeps in level order and sets
`eta[z] = 1` iff `z` has at least two 1-predecessors or `z` is marked. A 1-site
is a `seed` / `amp` / `proc` according as it has 0 / 1 / >= 2 one-predecessors.
A *family tree* is a subtree through 1-sites with exactly one downward arrow at
every non-seed node, forks between siblings, `|forks| = |S| - 1`, connected,
`|edges| = |nodes| - 1`. With `c = 1`,

```
cost(T) = E - 3(|S| - 1) - |A|
```

(`E` processed, `A` amplified, `S` seeds). `v(z)` is the minimum cost over family
trees containing `z` all of whose nodes sit at levels `<= level(z)`; `z` is
*tight* iff `v(z) = 0`. (H) asserts `v <= 0` at processed and `v <= -1` at
amplified sites.

## 3. Steps

**S1 — cost separability. PROVED.** Writing `w(proc) = +1`, `w(amp) = -1`,
`w(seed) = -3`, we have `E - 3(|S|-1) - |A| = 3 + sum_{n in N} w(n)`, because the
seed term contributes `-3` per seed and `+3` once. So **cost depends only on the
node set `N`, never on the arrows or forks.**

**S2 — the closed-set lower bound. PROVED.** Call `N` *closed* when every
non-seed member has a 1-predecessor in `N`. The node set of any family tree is
closed: the arrow leaving a non-seed node lands on a 1-predecessor inside the
tree. Hence, by S1,

```
min { cost(N) : N closed, z in N, all levels <= level(z) }   <=   v(z).
```

The left side is computed exactly by a level sweep over subsets of each level
(`closed_min` in check.py) — an exhaustive minimisation, no solver, no relaxation
gap to argue about. **This one-sided bound alone already refutes (H)**, since it
gives `v(333) >= 1 > 0`.

**S3 — matching upper bound. CHECKED.** For each site I build an explicit tree on
the optimal closed set (arrows to a predecessor in the set; forks chosen to span
the seed components) and verify it from scratch against §2: membership, the level
restriction, one arrow per non-seed, every arrow along a `-e_j`, every fork a real
fork offset, `|forks| = |S|-1`, `|edges| = |nodes|-1`, connectivity from `z`, and
the cost. When the verified tree's cost equals the S2 bound, `v(z)` is exact. It
does in every case below, including the 3-seed case of S8.

**S4 — the witness. CHECKED.** Marks
`{000, 001, 010, 100, 021, 102, 210, 113, 131, 311}` (sites off the non-negative
octant are 0: every predecessor of a site with a negative coordinate keeps that
coordinate and no mark has one — PROVED, so the sweep over `{z >= 0, level <= 9}`
is exhaustive). This gives 37 one-sites, all inside `[0,3]^3`, kinds
27 proc / 9 amp / **1 seed** at the origin.

**S5 — the C3 symmetry. PROVED + CHECKED.** `sigma(x,y,z) = (y,z,x)` maps the
mark set onto itself (`000` fixed; `001 -> 010 -> 100`; `021 -> 210 -> 102`;
`113 -> 131 -> 311`). `sigma` permutes `preds` and fork offsets, so it commutes
with the sweep and preserves every kind. The three 1-predecessors of `333` form a
single `sigma`-orbit, so **one** tightness computation gives all three.

**S6 — the refutation. CHECKED.** `v(233) = v(323) = v(332) = 0` and
`v(333) = 1`, each with lower bound (S2) equal to verified-tree upper bound (S3).
So `333` is processed, its three 1-predecessors are processed and tight, and yet
no family tree at `333` has cost `<= 0`:

* the conjecture of this task is **false**;
* the open lemma of block 33 is **false** (its hypothesis holds, its conclusion
  fails) — it is not vacuous, it is wrong;
* (H) is **false**; `333` is the only site of this realization violating it, and
  no amplified site violates it.

**S7 — the exact budget. CHECKED.** Carrying Pareto-minimal `(E, A)` pairs
through the same sweep (dominance trimming is valid because `E` and `A` only
accumulate) gives the full frontier at `333`:

```
(E,A) in {(6,5), (7,6), (8,7), (9,8), (10,9)}
```

so `c*(eta,333) = min E/A = 10/9` exactly (Fractions, not floats). Note the
structure: the budget-critical set `(10,9)` is **not** the `c = 1` cost-minimiser
`(6,5)`. So `c = 1` is not admissible here and nothing below `10/9` is either.

**S8 — minimality. CHECKED.** Over all 1023 proper subsets of the marks, exactly
one keeps `333` processed with at least two processed 1-predecessors: `MARKS`
minus the origin mark. That realization has 3 seeds, its values still certify
two-sidedly (the fork-spanning builder of S3), and its predecessors have
`v = -3 != 0`, so they are not tight. Every one of the 10 marks is load-bearing.

**S9 — the route named in this task fails, and fails at its first step.
PROVED + CHECKED.** The task proposes: "characterize all tight sites at depth
`<= 3` exhaustively … two such patterns cannot share the cone of a common
successor." Step one is impossible, because tightness is not a function of the
depth-3 cone. Add the single mark `(2,2,0)` to the witness. The two realizations
differ at **exactly one site**, at level 4; hence they agree in membership *and*
in kind on every site of level `>= 5`, which contains the entire depth-3
predecessor cone of `(2,3,3)` (levels 5..8). Yet `v(233) = 0` before and
`v'(233) = -1` after, both certified two-sidedly. Two sites with identical
depth-3 neighbourhoods, one tight and one not: no depth-`<=3` census can decide
tightness, so the route cannot be repaired by pushing the depth to 3.

The underlying reason is structural: every family tree must reach a seed, so `v`
depends on the whole descending cone, not on a bounded neighbourhood.

**S10 — cross-check. CHECKED.** `probes/lib`, used nowhere above, agrees:
`lib.family.run_automaton` reproduces `eta`, and the `lib.rooted` MILP returns
`0, 0, 0, 1` at `233/323/332/333` with optimal `(E,A) = (6,5)` at `333` — my
Pareto minimum. Two unrelated methods, same numbers.

Nothing is ASSUMED. No outside theorem is used.

## 4. What this costs the lane

`c* = 1` does not follow by this route, and not by any route: `c*(eta,333) = 10/9`
is an exact upper bound on the admissible unit budget at a real realization. The
`453` threshold that was to follow from `c* = 1` therefore does not follow. The
refinement-history route to `84` is untouched by this — it does not use (H).

## 5. What would finish it

The open question is now the *correct* budget, not the vacuity of the lemma:

1. Is `10/9` attained infinitely often, or is `inf over eta of c*(eta,z)` strictly
   below it? The frontier method of S7 is exhaustive per realization; what is
   missing is a bound over all realizations.
2. Does (H) survive with `c` replaced by `10/9` (or by `2`)? S2 gives a cheap
   exact test at any single site; the search over realizations is the work.
3. Any replacement for (H) must be non-local in the sense of S9, or carry the
   seed structure explicitly.

## 6. Relation to the prior attempt

Attempt a2 reached the same witness and the same `c* = 10/9`. I did not use its
files to obtain anything here: my values come from the closed-set certificate of
S2/S3, which is solver-free and library-free, so a referee can re-run it with a
stock Python and no scipy. New here beyond a2: the two-sided certificate itself
(a2's values rest on the MILP), the full Pareto frontier with the observation
that the budget-critical set is not the cost-minimiser, the exhaustive minimality
of the 10-mark witness over all 1023 proper subsets, the `C3` reduction of three
tightness claims to one, and — in place of a general argument that tightness is
non-local — the explicit pair of realizations in S9 sharing a depth-3 cone with
different rooted values, which refutes this task's route as a checkable finite
fact rather than by appeal to the seed argument.
