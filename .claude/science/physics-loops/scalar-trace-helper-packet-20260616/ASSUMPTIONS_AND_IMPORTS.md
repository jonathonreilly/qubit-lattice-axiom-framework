# Assumptions And Imports

Allowed inputs:

- the three helper source modules named in the audit blocker;
- their SHA-pinned runner caches under `logs/runner-cache/`;
- finite numerical tensor/probe checks already performed by the helper runners.

Forbidden hidden inputs:

- no new axiom;
- no audit verdict edit;
- no claim that the helper constructions are axiom-derived beyond their source
  and cached outputs;
- no positive tensor-valued gravity completion claim.

Import movement:

- dynamic `_frontier_loader` use is removed from the primary no-go runner;
- the helper source/cache packet makes the restricted-packet evidence explicit.
