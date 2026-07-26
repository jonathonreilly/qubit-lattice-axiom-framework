# A Note That Should Pass The Inference Audit

Negative control for the linter: a gate that fires on every input is worth as
little as one that fires on none. This note carries a complete claim ledger,
states hypotheses where it cites a named result, and records the converse of
its one directional claim.

## Answer

Every proper-cubic orbit on the content sphere has size 6, 8, 12 or 24. The
size-6 orbit is unique. This uses orbit-stabilizer for a finite group action,
whose hypotheses are that the group is finite and the group action is on a set.

## Claim ledger

| ID | Claim | Support | Hypotheses | Shown vs claimed | Falsifier |
|---|---|---|---|---|---|
| C1 | orbit sizes are 6, 8, 12, 24 | row A, exhaustive enumeration | [satisfied] finite group action, faithful on the sphere | shown: sizes over all scanned orbits; claimed: same | an orbit of another size |
| C2 | the size-6 orbit is unique | row A, orbit-stabilizer | [satisfied] finite group action | shown: uniqueness on the scan and by stabilizer order; claimed: same | two distinct size-6 orbits |
