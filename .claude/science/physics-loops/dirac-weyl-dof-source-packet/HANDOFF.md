# Handoff

This branch repairs the Dirac/Weyl dof conditional row by retiring Q1 using the
current retained `CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27`
authority. The runner now checks that authority from the live ledger.

The repair is intentionally not a full retention proposal: Q2 on-shell thermal
counting remains bounded, and Q1 is not broadened into physical Wick rotation
or forced Lorentzian-sign selection.

Reviewer extraction target:

- keep the Q1-retired wording;
- keep the Q2 bounded boundary;
- keep the live-ledger runner/cache;
- do not extract any audit verdict or ledger retag from this PR.
