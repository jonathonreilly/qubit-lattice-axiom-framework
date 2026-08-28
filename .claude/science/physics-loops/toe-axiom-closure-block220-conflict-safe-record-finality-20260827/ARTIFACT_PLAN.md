# Artifact Plan

1. A preregistered representation-capacity runner that reconstructs the
   Block-218 code and exactly tests the proposed controller representation
   inside its rank-76 complement.
2. A primary protocol runner using only local transition tables.  It must
   enumerate event-seeded success and rollback, first commit, Record flood,
   critical peaks and first-commit histories on L=4 and L=6, then use the
   frozen rule on held-out L=8.
3. A structurally independent checker with a separately implemented graph and
   state encoding; it may consume a frozen sidecar but may not import the
   primary runner.
4. A mutation plan covering carrier leakage, broken rotation/complement
   transport, hidden size or coordinate data, incomplete coverage, false
   success at cross edges, failed cleanup, premature commit, Record overwrite,
   opposite-root conflict, history normalization and held-out overfit.
5. If tier 2 is tractable, a finite-state arbitration search with exact
   reachable fair-MEC and disjoint-opposite-commit queries.
6. A bounded theorem or scoped boundary note, fresh caches, trace gate,
   conformance receipt and one stacked draft PR.  No audit verdict or
   canonical axiom edit is part of this block.
