# Assumptions And Imports

- The landed audit ledger/status surface remains the authority for audit
  grades. This branch only reflects source-side hygiene that a reviewer can
  extract and route for re-audit where required.
- Edited retained notes must not land with stale hash ratification. The strict
  audit lint failure is therefore expected and preserved rather than silenced
  through audit-ledger edits.
- The Poisson runner is a finite-grid sampled-candidate diagnostic. It is not
  used as a continuum alpha=1 uniqueness theorem.
