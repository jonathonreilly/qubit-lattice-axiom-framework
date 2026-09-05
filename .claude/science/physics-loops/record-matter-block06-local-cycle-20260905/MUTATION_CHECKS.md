# Mutation checks

These are small integrity checks for the already completed finite probe. They
do not add a scientific result. Each temporary mutation is expected to make a
runner exit nonzero by crossing an existing declared gate.

The final record is filled after canonical source-bound runs:

| Mutation | Expected guard | Result |
|---|---|---|
| Replace one edge in the primary EDGE_ORDER | L0 endpoint-star scheduler | pending final validation |
| Replace one dwell with a negative value in a temporary primary copy | L4/L6 dynamics or ledger guard | pending final validation |
| Replace the independent checker EXPECTED_ORDER | C0 independent front | pending final validation |
| Flip the independent checker ledger sign | C3 persistent ledger | pending final validation |

Temporary mutation copies are outside the repository and are not PR
artifacts. A mutation is counted only when it exits nonzero; no mutation result
is used as a physics input.

