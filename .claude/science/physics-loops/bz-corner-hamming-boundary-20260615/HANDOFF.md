# Handoff

This PR repairs the BZ-corner conditional row by taking the narrow option named
in the blocker: closed Hamming-count plus hw=1 `M_3(C)` algebraic support.

Important boundary:

- The branch does not prove a Hamming-parity-to-position-space
  sublattice/chirality theorem.
- The runner no longer counts that unsupported bridge as a pass condition.
- The source note explicitly says that bridge remains separate.

Suggested reviewer focus:

- Confirm the remaining support chain is exactly the supplied `{0,1}^3`
  Hamming arithmetic plus existing hw=1 `M_3(C)`/no-proper-quotient surfaces.
- Confirm no audit ledger/result/status files were edited.
- Decide whether this is sufficient to re-audit the row under the narrowed
  claim.
