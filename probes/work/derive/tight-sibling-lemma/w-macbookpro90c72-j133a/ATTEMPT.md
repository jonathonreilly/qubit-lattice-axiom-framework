# tight-sibling-lemma, attempt 1 (worker w-macbookpro90c72-j133a, model grok-4.6)

Independent of a3 (isolated depth-2 cone, 1024) and a5 (2×2×2 cube, 256). Route (i) on a larger local box: `3×2×2`.

## (1) The statement attempted

Lemma (block 33): a processed site all of whose 1-predecessors are tight processed sites has a rooted tree of cost `≤ 0` (`c*=1`). Equivalent local test: if two processed 1-predecessors of a processed `z` are fork-siblings, then `v(z)<0` on finite cones, so they cannot both be tight (`v=0`) while feeding `z`.

**Statement.** On the `3×2×2` box, all `4096` noise patterns: among `4544` (pattern, processed `z`, fork-related processed 1-predecessor pair) cases, `brute_min(η,z,c*=1) ∈ {-8,-7,-6,-5,-4,-3,-2,-1}`, never `0`. No local tight-sibling counterexample in this box. The lemma remains open on `Z^3`.

## (2) Steps

**Step 1 — definitions (from `probes/lib/family.py`, restated).** Automaton, kinds (seed/amp/proc), forks, `brute_min` enumerating the counted family on the finite `1`-set.

**Step 2 — census (CHECKED).** `3×2×2` has 12 sites. For each of `2^{12}` marks, run the automaton, collect processed sites with at least two processed 1-predecessors that form a fork, compute `brute_min`. Histogram as above; `n_tight=0`.

**Step 3 — what this does not prove.** A tight pair on `Z^3` could use marks outside any `3×2×2`. This is a local no-go for a counterexample of that size, not the lemma.

## (3) First failing step, if any

The lemma's induction gap is not closed. The local statement "two tight processed siblings cannot share a processed successor" is verified on this box and not proved in general.

## (4) What would finish it

A potential on marks implying `v≤-1` whenever two processed fork-siblings feed a processed site, for arbitrary cones; or a counterexample larger than `3×2×2`.
