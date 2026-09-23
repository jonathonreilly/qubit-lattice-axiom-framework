# Referee: tight-sibling-vacuity a3

Author: `w-jonathonsmac4f50-j041c` (claude-opus-5). Referee: `w-macbookpro90c72-j5571` (grok-4.6).

Statement attempted: (Vac) — a processed site with at least two processed 1-predecessors cannot have all of them tight. The attempt claims a PARTIAL reduction, not a proof.

## Step verdicts

- **S1 / L1 — holds.** Independent count: `cost = 3 + Σ w` and joining two disjoint trees by one fork subtracts 3, on all small `(E, A, |S|)` pairs.
- **S2 — holds as bookkeeping.** The intersecting-tree consequences follow from L1 plus the definition of `v`. No finite counterexample is claimed.
- **S3 — holds as a bound scheme.** O0/O1/O2 are upper bounds on `v`, not a classification.
- **S4 / C1 — holds.** Independent enumeration of the depth-2 cone (different tree search: one bottom open end of value 0, subsets of the upper window) reproduces **10272** configurations, **1844** permutation classes, **6196** / **1107** certified under (H) only.
- **S5 / C2 — not re-enumerated.** The 66 + 6 of 267 small-class counts are the author's. They are not needed for the qualitative claim: 737 classes remain uncertified by (H) alone, so the route does not prove (Vac).
- **S6 — consistent.** An open remainder is exhibited; the attempt does not call it a counterexample.

## Verdict

The first place a *proof* fails is the open remainder after the depth-2 census, which the author already marks as the stop. The new exact partial (the 10272/1844/6196/1107 split) survives.

`HIT: confirmed` — the PARTIAL census stands; (Vac) is not proved.
