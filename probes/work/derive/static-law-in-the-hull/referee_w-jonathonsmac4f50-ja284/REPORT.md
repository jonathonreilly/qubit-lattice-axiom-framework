# Referee report: J:derive:static-law-in-the-hull:a2

- **Author:** w-macbookpro90c72-j67ba (grok-4.6).
- **Referee:** w-jonathonsmac4f50-ja284 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j67ba__1c43a808__20260919T015059Z`.

**Provenance.** The constant-pattern separator on every cyclic window is attempt a1's. a1 was written by this referee's model family and
confirmed by a grok referee. a2 applies it to C4. `check.py` is new code, using Python integers and brute force.

## The claim

On C4, at `(3,1,2)`, `(5,2,4)` and `(7,3,5)`, the static law is not in the convex hull of adapted formation laws. Three facts are behind
this:
- `Z < D_σ` for all 24 orders;
- along the all-+x pattern, an adapted scheme runs a fixed order, or a mixture of orders if randomized;
- so the all-+x mass under any adapted scheme stays below `p⁴/Z`.

The path of 3 sites is a control, with `Z = D`.

## Step by step

**Step 1 (`D_σ = ∏ N_{kₓ}`): holds.** P2: the chain rule from the rule gives `p⁴/D_σ` for every order.

**Step 2 (census): holds.** P1 and P2:

| `(p,q,r)` | `Z` | `D_min` | margin |
|---|---|---|---|
| (3,1,2) | 20784 | 22464 | 1680 |
| (5,2,4) | 280086 | 295182 | 15096 |
| (7,3,5) | 810768 | 853200 | 42432 |

- `Z` agrees three ways: brute force, `tr W⁴`, and the eigenvalue sum.
- `D_min = 6N₁²N₂`, attained by the 16 orders whose first two sites are adjacent.

**Step 3 (adapted schemes): holds.** On the all-+x atom, every recorded neighbourhood is all-+x. A deterministic scheme's choices are
therefore a fixed order, and a randomized scheme gives a mixture of orders.

**Step 4 (control): holds.** P3: the path of 3 has `Z = D = 864`.

## Scope

C4 is the plaquette. The task calls value-dependent orders open *beyond* the plaquette, and names the 2×3 rectangle and the cube. a2 does
not treat those windows; a1 and a3 do. The result is correct as the plaquette case of a1's separator.

## Verdict

The partial claim survives with no failing step on C4.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
