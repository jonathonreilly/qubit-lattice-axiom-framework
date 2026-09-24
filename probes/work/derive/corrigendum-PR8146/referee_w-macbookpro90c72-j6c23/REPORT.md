# Referee report: corrigendum PR8146, attempt 2

- **Author:** `w-jonathonsmac4f50-jd9fc` (`claude-opus-5`).
- **Referee:** `w-macbookpro90c72-j6c23` (`grok-4.6`). Different model family.
- **Checks:** the 2:1 weights recomputed from equal, opposite and orthogonal pair factors, and block 12's pack file read at `3acd27d2fca8`. The author's script is not called.

## The statement that survives

For a 2:1 triple the output `v` is the unique heaviest value in both the antipodal pattern and an orthogonal pattern if and only if

`p > max(q, √(r³/q))`.

That is stricter than `p > max(q, r)` exactly on the band `q < r < p ≤ √(r³/q)`, which is nonempty precisely when `q < r`. On `(p, 1, 2)` the band is `2 < p ≤ 2√2`. `(5, 2, 4)` and `(5/2, 1, 2)` lie in it; `(3, 1, 2)` and `(5, 2, 3)` do not.

At `(5, 2, 4)` the antipodal weights are `50` for `v`, `20` for `−v` and `64` for each other value, so the majority loses. The old selector `q ≥ p or r ≥ p` is false there.

Block 12's `ASSUMPTIONS_AND_IMPORTS.md`, line 78 at that commit, chooses its counterfactual menu by `q ≥ p or r ≥ p`. That is the negation of the defective condition, so the pass cannot enter the band. Attempt a1 lists the note, the runner, `RESULTS_block12.md`, `HANDOFF.md`, `STATE.yaml` and `GOAL_block12.md`, and does not name this file.

## Steps

**1.** Antipodal weights are `p²q`, `q²p` and `r³`. Orthogonal weights are `p²r`, `r²p`, `q²r`, `r²q` and `r³`. The eight margins factor as `pq(p−q)`, `p²q−r³`, `pr(p−r)`, `r(p−q)(p+q)`, `r(p²−qr)` and `r(p−r)(p+r)`.

**2.** `√(r³/q) − r = r(√(r/q) − 1)`, so the square root exceeds `r` exactly when `r` exceeds `q`. On 512 positive rational triples, both patterns have a unique majority at `v` exactly when `p > q` and `p²q > r³`.

**3.** On the same grid, `p > max(q, r)` and not the corrected inequality is exactly the band, and no triple with `q ≥ r` lands in it.

**4.** The pack file at `3acd27d2fca8` has six "Counterfactual pass" lines. The one that says the majority is not the most likely output is line 78, and it selects by `q ≥ p` or `r ≥ p`.

## Verdict

The corrected threshold and the missed pack line both survive. The counterfactual pass inherits the defect it was meant to catch.
