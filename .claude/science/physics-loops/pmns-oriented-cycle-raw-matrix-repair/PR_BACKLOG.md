# PR Backlog

## This PR

Title:

`[physics-loop] PMNS oriented-cycle raw matrix repair (bounded-support)`

Body points:

- narrows the row to raw finite matrix identities only;
- removes carrier/value-law, physical identity-block, and graph-first bridge
  readings from the claim;
- removes the dependency edge to the channel-value-law row;
- resets the row for audit as `unaudited`, `deps=[]`, queue position 1;
- runner passes with `PASS=29 FAIL=0`;
- no new axioms and no audit verdict applied.

## Later PRs

- physical identity-block bridge, if it can be derived;
- graph-first to swap-conjugation bridge, if it can be derived;
- downstream PMNS cleanup once audit lands this repair.
