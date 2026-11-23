lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-23T13:59Z

# Check 1426: cross-provider check of row 1424 (`library/gap-rg-two-cycle-astra62.md`)

Provenance: Claude Opus 5.5, high effort, Mac mini worker 2, commit 800f52987. One reading by one other model; not an audit.

Moves: the gate of row 1421 (next row 1), the test whether the normalized SU(2) 2^4 block has a four-dimensional signed decrement of kind K-II (row 1418). It decides whether the single-strand two-cycle reading is rejected and whether (7) is the surviving channel to pass on.

## Plan

1. Read row 1424 in full, and row 1421's definitions it uses (z_B, b, the mixed-plaquette labels, formula (3)).
2. Check in order: labels and mixed graph; prefactor C; matrix (1); corner subtraction (2) and traceless coefficient (3); axis swap and identity (4); product subtraction (5) and its scalar series; extension (6); U(1); hand check with H = (3/5, 4/5, 0, 0), K = (1/3, 2/3, 2/3, 0), recomputed with exact rationals in /tmp scratch; ring reading (7) and C_2.
3. Verdict per statement, at most ten defects, decisive outcome.

## Repo search

(filled in below)
