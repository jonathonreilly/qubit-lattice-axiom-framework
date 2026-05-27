# Handoff

This branch repairs the Koide MRU reduced-carrier row by taking the audit
blocker's formal rescope path.

Key movement:

- Removed the physical SO(2)-quotient/reduced-carrier bridge from the binding
  claim.
- Kept only the formal two-variable corollary of retained bounded
  reduced-log-volume and block-total Frobenius algebra.
- Updated the runner prose to match the formal scope.
- Cache result: `TOTAL: PASS=35, FAIL=0`.
- Pipeline reset the target row to `audit_status=unaudited`,
  `effective_status=unaudited`, `ready=true`.

Remaining science blocker: derive the actual physical SO(2)-quotient on the
charged-lepton scalar lane if we want to close the physical parent lane.
