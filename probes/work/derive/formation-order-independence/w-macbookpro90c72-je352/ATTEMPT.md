# formation-order-independence, attempt 2 (worker w-macbookpro90c72-je352, model grok-4.6)

## (1) The statement attempted

**Hypothesis.** An event lattice is a countable DAG: each site `x` has a finite
predecessor set `pred(x)`, edges point from predecessors to `x`, and there are
no directed cycles. A formation order is *compatible* if it is a linear
extension of the DAG (every predecessor of `x` is recorded before `x`). Records
are not re-formed. The kernel `K(v_x | v_{pred(x)})` depends only on the
predecessors' values.

**Theorem.** Under that hypothesis the joint law of any finite set of records
is `P(v) = Π_x K(v_x | v_{pred(x)})`, independent of the compatible order.

**Smallest violating example.** The V-shape `A → C ← B` with binary records and
`P(C=1 | a,b) = (2a+b+1)/7` (not exchangeable in `A,B`). The two topological
orders `ABC` and `BAC` give the same joint law. Forming `C` first (then `A,B`
from the empty kernel) changes `P(C=1, A=1, B=0)` from `3/28` to `1/8`.

**Campaign comparison.** On `Z^3` in a monotone spatial order, neighbours of a
site are not its causal predecessors (the graph is undirected). Different
monotone orders are not topological orders of one DAG, so they can (and do)
give different laws. The event-lattice reading removes that order dependence
because it supplies a DAG.

## (2) Steps

**Step 1 — product formula (PROVED).** Along any topological order `x_1,…,x_n`
of a finite down-set, the chain rule and the kernel's dependence only on
`pred(x)` give `P(v_{x_1…x_n}) = Π_j K(v_{x_j} | v_{pred(x_j)})`. The right-hand
side does not mention the order. Any other topological order yields the same
product.

**Step 2 — two topological orders agree (CHECKED as E2a, E3a).** On the V-shape,
`ABC` and `BAC` produce identical 8-atom joints (total mass 1).

**Step 3 — violating order changes the law (CHECKED as E2b–E2e, E3b).** Of the
`3!=6` total orders, exactly the two topological ones agree; the four that place
`C` before both predecessors differ. Explicit: legal `P(1,0,1)=3/28`, `C`-first
`=1/8`.

**Step 4 — why `Z^3` is different (PROVED).** A neighbour on `Z^3` is not a
predecessor in a DAG. A monotone corner order is a total order of an undirected
graph, not a linear extension of `x ↦ {x−e_j}`. The hypothesis of Step 1 fails,
and blocks 05/08/09's order-dependence is the expected residue.

## (3) First failing step if the DAG hypothesis is dropped

Step 1: without "predecessors already recorded", the factor `K(v_x | v_{pred(x)})`
is not the conditional used at formation time (Step 3's numbers).

## (4) What would finish it

The same product formula on infinite DAGs as a Kolmogorov extension (finite
dimensional laws already match). Nothing further for the finite statement.

Nothing here edits notes or runners.
