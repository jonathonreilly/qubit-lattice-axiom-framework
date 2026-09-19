# Referee report: J:derive:formation-order-independence:a1

- **Author:** w-macbookpro90c72-j482b (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j40d0 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j482b__ecad10d3__20260919T013637Z`.

`check.py` is independent code: exact Fractions over full joint laws. Nothing is taken from the author's script.

## The claim

- **On a causal DAG.** The law is `∏ₓ K(sₓ | s_pred(x))`. It is the same for every linear extension, under the hypothesis that
  predecessors form first and nothing is re-formed.
- **On C4 formed from recorded neighbours.** The path order and the opposite-first order give different laws: `3/832` against `9/2704`.
  The attempt calls this the "smallest undirected counterexample".
- **The V.** Forming the child before its parents changes the law.
- **Event lattices.** Levels are antichains, so level orders are linear extensions and agree. The campaign's `Z³` law uses the undirected
  neighbour graph, which explains the order dependence seen in blocks 05/08/09.

## Step by step

**Step 1 (product formula): holds.** O1: every linear extension gives the same full joint law. This holds on the V, the diamond and a
five-site DAG, for the covariant six-axis kernel and for a random non-covariant binary kernel.

**Step 2 (V as a DAG): holds.** This is part of O1.

**Step 3 (C4): holds, with a correction.** O2:
- the path order gives `k = (0,1,1,2)` and `P(all +x) = 3/832`;
- the opposite-first order gives `k = (0,0,2,2)` and `9/2704`.

The HIT line writes the opposite-first sequence as `(0,0,1,1)`. That cannot occur, because the `k` values sum to `|E| = 4`. The attempt's
own check prints `(0,0,2,2)`.

**Step 4 (violating the hypothesis): holds, and it shows C4 is not the smallest example.** O3:
- **Two sites.** The two orders give the same law, because `W` is symmetric and `Z₁ = p + q + 4r` is constant. Checked at `(3,1,2)` and
  `(5,2,4)`.
- **Three sites.** On the path, which is the attempt's V read undirected, ends-first and middle-first give different laws: `P(all +x)` is
  `1/104` against `1/96`.

So the smallest undirected counterexample has three sites, and the attempt's own V is it. C4 is not the smallest, contrary to the statement
and the SUMMARY.

**Step 5 (event lattices): holds.** O4: on a `3×3` level-ordered window, 60 random linear extensions give the identical 512-cell joint
law.

## Verdict

The DAG statement and its consequence for event lattices survive. Two corrections:
- the opposite-first `k`-sequence is `(0,0,2,2)`;
- the smallest counterexample has three sites, not C4's four.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
