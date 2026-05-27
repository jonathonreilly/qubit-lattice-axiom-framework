# Handoff

This branch repairs the beta-gbare product-invariance conditional row by
accepting the audit blocker's conditional-rescope route.

Key movement:

- Removed the Ward-route coupling closure as a Wilson-matching authority.
- Declared `WM: beta = 2 N_c / g_bare^2` as an explicit premise.
- Cited the retained abstract beta-gbare polynomial identity for the algebraic
  product invariance.
- Kept the generator-basis rescaling dependency only for its scoped
  rescaling-map role.
- Updated the runner to enforce those scope firewalls.
- Cache result: `TOTAL: PASS=151, FAIL=0`.
- Pipeline reset the target row to `audit_status=unaudited`,
  `effective_status=unaudited`, `ready=true`.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2059

Remaining science blocker: derive Wilson matching from the framework, or keep
this row bounded/conditional when used downstream.
