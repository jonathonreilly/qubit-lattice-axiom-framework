# GOAL — block 16: the static law is not a mixture of formation laws on any window with a cycle (2026-09-15)

**Owner directive (2026-09-15):** don't stop; assess the next lane at each conclusion; no subagents; derivations over computation.

**Why this block.** Blocks 14 and 15 (PRs #8148, #8149) showed on the plaquette, through its symmetries, that the static law is unreachable by rate and unit clauses. The normalizer lemma of block 15 gives a symmetry-free mechanism: flipping one record from `b` to `−b` raises every order's weight ratio monotonically. That yields a general theorem in a few lines: for every finite window and every probability law on orders, the mixture of sequential laws equals the static law iff the law charges only orders in which every site records at most one neighbour; on any window with a cycle no such order exists. It closes the "randomized formation" route to the static reading completely (value-blind randomization of any kind: random orders, random priorities, set-dependent clocks), unifies block 01's Theorem B, the census note's Theorem 3 and block 14's plaquette hull statement, and extends to units in an environment with block 15's criterion.

**Object.** A finite window `Λ ⊂ Z³` (or a unit `U` with outside records `v_O`); the six-axis menu with the product rule `(p,q,r)`, executed at `(3,1,2)`; the sequential laws `μ_σ`; a probability `P` on orders ("a mixture"); the static law `Π_edges φ/Z` (or the joint law of the unit).

**Contract.**
- X1 (the flip lemma): with `w_σ(v) = μ_σ(v)/Π_edges K(v_e)`, `v = all b`, and `v^z` the pattern with site `z` flipped to `−b` (or to `c ⊥ b` when `p = q`): `w_σ(v^z) ≥ w_σ(v)` for every order, with strict inequality iff `z` lies in some recorded set of size at least two. Proved; executed on every (order, site) pair of the plaquette, `2×3` and the cube.
- X2 (the mixture theorem): `Σ_σ P(σ) μ_σ = static` iff `P` charges only orders in which every site records at most one neighbour. On a window with a cycle no order qualifies, so no mixture is the static law. Proved for every non-constant rule.
- X3 (units in an environment): the same with block 15's criterion and the joint law; proved.
- X4 (what is left): value-dependent order laws are outside X2 (block 14 covers the plaquette); recorded as the open boundary.
- N-gate for the negatives.

**Lens pass (self-run panel).**
- *"This is block 01 plus the census note."* Those treat one order and one mixture; X2 treats every mixture on every window with one proof; the flip lemma is the new mechanism.
- *"The order law could depend on the values."* Then `P(σ|v)` changes with the flip and the argument breaks; block 14 handled that on the plaquette by symmetry; X4 names it as the boundary.
- *"Small block."* Yes: a short theorem with a wide scope; the executions are exhaustive on three windows.

**Forbidden phrases (beyond the lane's standing list):** "the static law is derived", "the formation reading is refuted", "converge", "emergent", "certified".

**Prior-art search at `origin/main`.** `git grep -n -iE "mixture over (all )?orders|convex (hull|combination) of (the )?(order|sequential|formation) laws|random(ized)? formation"` → the census note (the uniform mixture; Theorem 3), nothing on general mixtures. Open PRs: #8148, #8149 (this lane; plaquette-specific).
