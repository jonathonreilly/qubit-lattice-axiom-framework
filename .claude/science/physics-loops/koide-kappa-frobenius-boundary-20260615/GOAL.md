# Goal

Repair the post-audit Koide kappa block-total Frobenius source artifact without
applying audit verdicts.

The audit blocker named two defects:

- the note elevated the block-total law to a canonical physical scalar-lane
  measure without deriving the required `SO(2)` quotient / canonical measure
  bridge;
- the prose parity formula for the sign real irrep used `d mod 2`, which is
  opposite to the runner/table for positive `d`.

This PR fixes both source-side issues that can be fixed honestly now. It keeps
the useful finite theorem as bounded algebraic support and names the remaining
bridge instead of closing it by convention.
