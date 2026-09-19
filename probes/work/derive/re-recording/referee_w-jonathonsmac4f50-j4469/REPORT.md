# Referee report: J:derive:re-recording:a3

- **Author:** w-macbookpro90c72-j3a06 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j4469 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j3a06__d082ab2d__20260919T012532Z`.

**Disclosure.** This referee's model family refereed attempts a1 and a2 of this problem (both grok). `check.py` is independent exact code in
Fractions. Nothing is taken from the author's script.

## The claim

The setting is one bond at `(3,1,2)`, with exact 36 × 36 matrices.
- **(a)** Asynchronous heat-bath has the static law `μ ∝ W` as its reversible stationary law.
- **(b)** The synchronous chain is reversible with respect to `π ∝ Z(s₀)Z(s₁)`. `TV(μ, π) = 1/12`, and both one-site marginals are uniform.
- **(c)** The static results transfer to (a) and not to (b).

## Step by step

**Step 1 (async): holds.** T1:
- rows sum to 1;
- `μP = μ`;
- detailed balance holds on all 1296 pairs;
- `P² > 0`, so `μ` is the unique stationary law.

**Step 2 (sync): holds.** T2:
- rows sum to 1;
- `πP = π`;
- detailed balance holds;
- `P > 0`, so `π` is unique.

**Step 3 (distinct): holds.** T3: `TV(μ, π) = 1/12`, and the one-site marginals are `1/6`.

**Step 4 (transfer): holds**, and more strongly than stated (T4).
- On the six-axis menu, `Z(a) = p + q + 4r` for every `a`, by cube symmetry.
- So `π` is exactly the uniform product law on the 36 states, at every positive `(p, q, r)`. The synchronous law carries no correlation
  across the bond.
- Hence `TV(μ, π) = (1/144) Σ |W − 2| = 1/12` at `(3,1,2)`.
- At other weights, `Z` is again constant and `π` uniform:

  | weights | `Z` | `TV(μ, π)` |
  |---|---|---|
  | `(5,2,4)` | 23 | `11/138` |
  | `(1,3,2)` | 12 | `1/12` |
  | `(7,1,1)` | 12 | `5/12` |

This is the one-bond case of the sublattice factorization of the synchronous law. On a bipartite window with a neighbour-only rule, `π`
factorizes over the two sublattices (`referee_w-jonathonsmac4f50-j50b9`, a2).

## Verdict

The partial claim survives with no failing step. The synchronous one-bond law is uniform, which makes (c)'s non-transfer immediate.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
