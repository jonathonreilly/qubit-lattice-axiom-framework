# Handoff

This branch repairs the critical `gravity_clean_derivation_note` row by making
the bounded IF-chain the only binding claim.

Key movement:

- Removed the live source framing as a complete single-axiom,
  zero-free-parameter Newton derivation.
- Preserved the conditional chain: if `L^{-1}=G_0`, `rho=|psi|^2`,
  `S=L(1-phi)`, and the `Z^3` Green-function normalization are supplied,
  then a `1/r` potential and inverse-square force follow in lattice units.
- Preserved the four direct dependency edges already used by the audit lane.
- Pipeline reset the target row to `audit_status=unaudited`,
  `effective_status=unaudited`, `ready=true`.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2062

Remaining science blocker: prove the missing closure/source/response/Green
bridges if we want an unconditional gravity derivation.
