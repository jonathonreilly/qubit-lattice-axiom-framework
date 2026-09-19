# Referee report: J:derive:formation-order-independence:a3

- **Author:** w-macbookpro90c72-j08d0 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j6e70 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j08d0__bd4e0b98__20260919T014437Z`.

**Disclosure.** This referee's model family has already refereed two attempts of this problem:
- a1 (`referee_w-jonathonsmac4f50-j40d0`);
- a4 (`referee_w-jonathonsmac4f50-jacb3`).

Both of those used the undirected six-axis reading, where the three-site path is the smallest example. `check.py` is independent code, using
exact Fractions over full joint laws. Nothing is taken from the author's script.

## The claim

1. **The DAG statement.** On a finite DAG, every linear extension gives the law `∏ᵥ K_v(s_v | s_pa(v))`.
2. **The smallest example.** The smallest order that violates the hypothesis is the three-site V formed child-first:
   - `P(C=1)` is `1/3` child-first against `1/2` causally;
   - full-joint `TV = 5/24`.
3. **Z³.** Anti-causal parent/child orders change the law and same-level swaps do not. The campaign's undirected monotone sweeps are not
   linear extensions of the event DAG.

The HIT and SUMMARY lines both state "smallest".

## The reading the attempt uses

A record formed before one of its parents conditions only on the parents already formed. The attempt uses this directed reading in two
places:
- its child-first V uses `K_C(·|∅)`, and the sources `A`, `B` ignore the child;
- its own D1 forms the parent "empty" after the child.

## Step by step

**Step 1 (product formula): holds.**
- The chain-rule argument is correct under the stated hypothesis.
- R1 tests it on 40 random DAGs with 3–6 sites, 377 linear extensions in all, with random non-symmetric kernels on menus of 2–3 values. Each
  DAG has one joint law across its linear extensions.
- A non-extension changes the law on 40/40.

**Step 2 (V-shape): the arithmetic holds; the "smallest" claim fails.**
- R2 recomputes the numbers with the attempt's kernels:
  - both topological orders agree;
  - `P(C=1)` is `1/2` causally and `1/3` child-first;
  - `TV = 5/24` exactly.
- **Minimality is asserted in (1) and in the HIT and SUMMARY lines. No step proves it, and it is false in the attempt's own reading.**
  - With one site there is only one order.
  - The two-site edge `x → y`, formed child-first, already changes the law. R3 gives:
    - `TV = 1/6` with the attempt's own kernels (`K(1|x) = (1+x)/3`, `K(1|∅) = 1/3`), which is the attempt's own check D1;
    - `TV = 1/12` with the rule-consistent six-axis product kernel at `(3,1,2)`, whose kernel is uniform when nothing is recorded.
  - In the directed reading the edge changes the law exactly when `K_y(·|x)` depends on `x`. So two sites is the minimum.
- The V is the smallest example only in a different reading: undirected, where a record conditions on its already-formed neighbours, with the
  six-axis kernel (constant normaliser). There the edge has `TV = 0` and the three-site path has `TV = 1/72` (R3). That is the setting of
  a1 and a4, not this attempt.

**Step 3 (diamond): holds.** The two linear extensions agree; R1's class covers this.

**Step 4 (two incomparable sites): holds.** There is no edge, so the law is a product.

**Step 5 (Z³ fragment): holds.** It also contradicts step 2. D1 is a two-site anti-causal order with `TV = 1/6`.

R4 checks the Z³ comparison on a genuine window rather than a two-site toy:
- **Window.** The `2×2×2` cube with event-DAG parents `x − eᵢ` and the binary product kernel `W = [[2,1],[1,2]]`.
- **Linear extensions.** All 48 give one joint law.
- **The eight monotone sweeps read undirected.** They give 8 distinct laws. Only the `(1,1,1)` sweep equals the DAG law. The other seven are
  at least `TV = 1/150` away.
- **The reversed order read directed.** It differs (`TV = 832589/1944000`).

So the explanation of the campaign's sweep dependence holds: a sweep in another direction conditions a site on a successor.

**Scope.** The task also asks why the event-lattice reading removes, or does not remove, the order dependence that the formation-rate and
formation-unit clauses (blocks 14 and 15) were introduced to settle. ATTEMPT.md does not mention those clauses. That part of the statement is
not attempted.

## Verdict

**Fails at step 2.** The three-site V is not the smallest violating example. In the attempt's reading the two-site edge formed child-first
changes the law, and the attempt's own D1 shows `TV = 1/6`.

What survives:
- step 1;
- the V's numbers (`1/2`, `1/3`, `5/24`);
- the Z³ comparison (R4).

The blocks 14/15 comparison is missing.

`check.py` prints `SUMMARY: fails at step 2 - ...` with no HIT line.
