# formation-order-independence, attempt 1 (worker w-macbookpro90c72-j482b, model grok-4.6)

## (1) The statement attempted

**Causal DAG.** Let records sit on a finite poset with a finite predecessor set; each site `x` is drawn from `K(· | values of predecessors of x)` after those predecessors are recorded, and is never re-formed. Then the joint law is
\[
\mu(s)=\prod_x K(s_x\mid s_{\mathrm{pred}(x)}),
\]
independent of the linear extension. Hypothesis: every predecessor is recorded before its successor; no re-form.

**Smallest undirected counterexample.** On C4, a Hamiltonian path has k-sequence `(0,1,1,2)` and `P(all +x)=3/832` at `(3,1,2)`; opposite-first has `(0,0,2,2)` and `9/2704`. Forming a child before its parents on the V-graph (undirected) changes k from `(0,0,2)` to `(0,1,1)` and changes `P(all +x)`.

**Why event lattices drop the Z^3 order dependence.** An event lattice is ranked by causal time; same-level sites are an antichain (no predecessor relation between them). Every level-compatible order is a linear extension of that DAG, hence agrees. The campaign's Z^3 formation uses the *undirected* neighbour graph (not a DAG), which is why different monotone orders (blocks 05, 08, 09) gave different laws and why rate/unit clauses were introduced.

## (2) Steps

**Step 1 — product formula (PROVED).** Induction along any linear extension: the next site's kernel depends only on already-recorded predecessors, whose values are already sampled from the unique prefix law.

**Step 2 — V-poset (CHECKED as E1).** Binary menu, both extensions `(a,b,c)` and `(b,a,c)` give the same 8-cell joint, normalised. Six-axis all-+x equal.

**Step 3 — C4 (CHECKED as E2).** Path vs opposite-first, distinct k-multisets and masses.

**Step 4 — violating the hypothesis (CHECKED as E4).** Child-first on the undirected V.

**Step 5 — event lattice (PROVED).** In-level sites are causally unrelated (independent set of the predecessor graph). Linear extensions differ only by permuting antichains, which does not change any k.

## (3) First failing step, if any

None for the DAG statement. Not proved: infinite posets (needs Kolmogorov extension); kernels that depend on *unrecorded* neighbours (a different reading).

## (4) What would finish it

Kolmogorov consistency for infinite event lattices; the same product formula when the predecessor set is the light-cone of 3+1.
