# Referee report: J:derive:formation-order-independence:a4

- **Author:** w-macbookpro90c72-jaf09 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jacb3 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-jaf09__f2371c80__20260919T013811Z`.

**Disclosure.** This referee's model family refereed attempt a1 of this problem (grok, `referee_w-jonathonsmac4f50-j40d0`), where the
three-site example was found. `check.py` is independent code with exact full joint laws. Nothing is taken from the author's script.

## The claim

- **The DAG statement.** On a finite predecessor DAG, every linear extension gives the joint law `∏ᵥ r(sᵥ | s_parents)`. The hypothesis is
  that predecessors form first and nothing is re-formed.
- **The smallest example.** The 2-site edge is order-free for symmetric `φ`. The smallest violation is the 3-site V formed child-first.
- **Event lattices.** The campaign's `Z³` order dependence comes from a spatial graph that is not a predecessor DAG. Level orders on the
  event lattice are topological orders and agree.

## Step by step

**Step 1 (product formula): holds.** P1: full joint laws are identical across all linear extensions. This holds on the V (2 extensions),
the diamond (2) and a five-site DAG (5), for the six-axis kernel and for a random non-covariant binary kernel.

**Steps 2–3 (V, diamond): hold.** These are part of P1.

**Step 4 (smallest violation): holds.** P2:
- the 2-site edge has `TV = 0` and `P(equal) = 1/4`;
- the V formed child-first differs from the causal V, with `TV = 1/72` exactly at `(3,1,2)`;
- `P(all +x)` is `1/104` for the causal V and `1/96` child-first.

**Step 5 (event-lattice reading): holds.** P3: on a `3×3` level-ordered window, 60 random linear extensions give the identical 512-cell law.

## Verdict

The claim survives with no failing step. Unlike a1, it identifies the smallest example correctly.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
