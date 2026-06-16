# Handoff

This PR repairs the audited conditional row
`staggered_dirac_bz_corner_forcing_theorem_note_2026-05-07` by narrowing the
source to the part the audit said closes: finite BZ-corner Hamming-count
algebra and hw=1 `M_3(C)` support.

It does not add axioms, audit the row, retag the ledger, or claim retained
status. The unsupported parity-to-chirality identification is removed and
recorded as a separate future bridge, not silently assumed.

Reviewer should check:
- The finite `1+3+3+1` Hamming-count and hw=1 algebra remain intact.
- The note no longer says Hamming parity is K-S sublattice/chirality parity.
- The runner cache matches the updated runner and prints the no-derivation
  firewall.
