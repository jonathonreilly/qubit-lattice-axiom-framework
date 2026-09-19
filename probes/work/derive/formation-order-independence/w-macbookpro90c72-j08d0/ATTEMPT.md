# formation-order-independence, attempt 3 (worker w-macbookpro90c72-j08d0, model grok-4.6)

Plan, locked from the task: the joint law on a causal DAG is the product of
kernels along any topological order; the smallest violating order is a 3-site
V with the child first; Z^3 monotone orders that condition on undirected
neighbours are not topological orders of the event DAG.

## (1) The statement attempted

**Hypothesis.** Finite directed acyclic graph `G = (V, E)` of records; each
`v` has a kernel `K_v(· | s_{pa(v)})` on a finite menu; formation order `π` is
a linear extension of `G` (every predecessor of `v` appears before `v` in `π`);
no record is re-formed.

**Theorem.** Under that hypothesis the joint law is
```
P_π(s) = ∏_{v ∈ V} K_v(s_v | s_{pa(v)})
```
independent of the linear extension `π`.

**Smallest counterexample when the hypothesis is dropped.** Three-site V:
sources `A, B` with empty parent sets, child `C` with `pa(C) = {A, B}`. Any
order with `C` last is topological and gives the same joint. The order
`C, A, B` (child first) uses `K_C(· | ∅)` in place of `K_C(· | A, B)` and
changes the law. Binary menus, sources `Bern(1/2)`, child
`K(1|x,y) = (1+x+y)/4`, empty-conditional `K(1|∅) = 1/3`:
`P_topo(C=1) = 1/2` and `P_{C-first}(C=1) = 1/3`; full-joint TV `= 5/24`
(CHECKED: exact 8-atom joints).

**Z^3.** Two sites at the same level are incomparable in the event DAG, so
either order of them is topological and the joint is unchanged. A monotone
sweep that treats a *spatial neighbour* as a parent (the undirected lattice of
blocks 05/08/09) is not a linear extension of the event DAG: that neighbour is
not a predecessor. That is why those sweeps can change the law while
event-lattice topological orders cannot.

## (2) Steps

**Step 1: product formula (PROVED).**
Let `π = (v_1, …, v_n)` be a linear extension. The chain rule along `π` is
`P(s) = ∏_i P(s_{v_i} | s_{v_1}, …, s_{v_{i-1}})`. By the hypothesis, every
parent of `v_i` is among `v_1, …, v_{i-1}`, and the formation kernel depends
only on those parent values, not on any other already-formed record, so
`P(s_{v_i} | s_{v_1}, …, s_{v_{i-1}}) = K_{v_i}(s_{v_i} | s_{pa(v_i)})`.
The right-hand side does not mention `π`. ∎

**Step 2: V-shape (CHECKED as A1, A2).**
Sources independent `Bern(1/2)`. Child kernel `(1+a+b)/4` for `P(C=1|A,B)`.
Both topo orders `A,B,C` and `B,A,C` give the same 8-atom joint (Fractions).
Child-first uses `K(C=1|∅) = 1/3`; the two joints differ; `P(C=1)` is `1/3`
versus `1/2`; full-joint TV `= 5/24`.

**Step 3: diamond (CHECKED as B1).**
Nodes `A → B, A → C, B → D, C → D`. All topological orders (there are 2:
`A,B,C,D` and `A,C,B,D`) give the same 16-atom joint.

**Step 4: two incomparable sites (CHECKED as C1).**
Two sources, no edge. Both orders give the product `K(A)K(B)`, TV `= 0`.

**Step 5: Z^3 fragment (CHECKED as D1).**
Sites `x` at level 0 and `y = x+e_1` at level 1, so `x ∈ pa(y)` in the event
DAG. The order `y` then `x` is not topological. With the same kernels, the
joints differ (TV `> 0`). Two same-level sites `x` and `x+e_1−e_2` are
incomparable; swapping them leaves the joint unchanged.

## (3) Where the route stops

No step fails for the theorem and the V-shaped counterexample. The campaign's
Z^3 order-dependence is not a counterexample to the theorem: those orders are
not linear extensions of the event DAG.

## (4) What would finish it

The same statement for infinite DAGs as a projective limit of finite down-sets
(Kolmogorov extension under uniformly bounded menus); a full census of
minimal undirected order-changing graphs vs minimal anti-causal DAG orders.

Imports: none beyond finite probability (chain rule).
