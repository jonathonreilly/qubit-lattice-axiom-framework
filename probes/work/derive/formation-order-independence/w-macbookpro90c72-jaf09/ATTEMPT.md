# formation-order-independence, attempt 4 (worker w-macbookpro90c72-jaf09, model grok-4.6)

No prior attempt printed. Route: the joint law on a finite predecessor DAG is the product of kernels along the partial order, hence independent of the linear extension.

## (1) The statement attempted

On any finite event lattice whose predecessor relation is a DAG, and for any one-site kernel that depends only on the recorded parents, **every formation order compatible with the causal order** (every linear extension of the DAG) produces the same joint law

    P(s) = ∏_v r(s_v | s_{parents(v)}).

Hypotheses: (i) every predecessor is recorded before its successor; (ii) no record is re-formed. A 2-site edge is **not** a counterexample when `φ` is symmetric (the two orders agree, CHECKED TV=0). The smallest violation is a 3-site V-shape formed child-first: parents then see the child as a neighbour, so the joint is `U(c) r(a|{c}) r(b|{c})` rather than `U(a)U(b) r(c|{a,b})`; TV>0 at `(3,1,2)` (CHECKED). This is why the campaign's `Z^3` monotone orders disagree (blocks 05, 08, 09): a spatial neighbour is not a predecessor, so those orders are not topological orders of a predecessor DAG. On an event lattice, level order is one topological order among many, all equivalent. Formation-rate and formation-unit clauses (blocks 14, 15) settle order on a *non-causal* graph; they are not needed once the graph is a predecessor DAG.

## (2) Steps

**Step 1 — product formula (PROVED).** Enumerate vertices in any topological order `v_1,…,v_n`. Site `v_i` is formed from `parents(v_i) ⊆ {v_1,…,v_{i-1}}` by hypothesis (i), independently of which linear extension was chosen, by (ii). The chain rule gives `P=∏_i r(s_{v_i}|s_{parents(v_i)})`, a formula that does not mention the order.

**Step 2 — V-shape (CHECKED T).** Two independent roots and one child. The two topological orders (root-swap) give identical joints, summing to 1.

**Step 3 — diamond (CHECKED D).** Two roots, two children each depending only on the roots. Child-order swap is the same product, summing to 1.

**Step 4 — smallest violation (PROVED; CHECKED V).** For symmetric `φ`, a 2-site edge is order-independent (TV=0): `U(p) r(c|{p})=U(c) r(p|{c})`. The smallest violation is a V-shape (two parents, one child) formed child-first: `TV>0` at `(3,1,2)`, and `P(0,0,0)` differs. This is the smallest graph on which an order can violate (i) when `φ` is symmetric.

**Step 5 — Z^3 (PROVED as a reading).** Blocks 05, 08, 09 compare monotone *spatial* orders on `Z^3`, where an edge is not a causal predecessor. Different orders record different neighbour sets at formation time, so Step 1's hypothesis (i) fails for the spatial graph. Light-cone / level order on the event lattice `Z^{d+1}` *does* satisfy (i): the past of `(t+1,x)` lies at level `t`. Any two linear extensions of that causal order agree.

## (3) Where the route stops

Infinite event lattices: the same product formula defines the law of every finite down-set, consistently, so Kolmogorov extension applies when the kernels are regular. Not written as a measure-theoretic theorem. Re-recording (hypothesis (ii) dropped) is the other unit.

## (4) What would finish it

A named Kolmogorov-extension lemma for locally finite DAGs; the exact TV on the 2-site edge as a rational (printed by `check.py`).
