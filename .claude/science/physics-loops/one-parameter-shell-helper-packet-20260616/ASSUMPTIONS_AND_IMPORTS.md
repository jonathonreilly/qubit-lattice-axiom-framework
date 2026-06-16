# Assumptions And Imports

Allowed inputs:

- the five helper source modules named by the audit blocker;
- their SHA-pinned runner caches under `logs/runner-cache/`;
- finite reduced-shell arithmetic already performed by the helper and primary
  runners.

Forbidden hidden inputs:

- no new axiom;
- no audit verdict edit;
- no claim that the helper constructions are axiom-derived beyond their source
  and cached outputs;
- no full nonlinear gravity closure claim.

Import movement:

- dynamic `_frontier_loader` use is removed from the primary reduced-shell
  runner;
- the helper source/cache packet makes the restricted-packet evidence explicit.
