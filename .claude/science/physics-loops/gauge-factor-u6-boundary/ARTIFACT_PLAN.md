# Artifact Plan

## Source Repair

- Patch the source note to call the result the factor-preserving algebra of the
  supplied carrier, not the full carrier symmetry algebra.
- Patch the carrier runner to check full `u(6)` and the 24-dimensional
  cross-factor complement.
- Patch the discriminator runner wording so it inherits the same supplied
  factor-locality boundary.

## Verification

- `python3 -m py_compile` on changed runners.
- Run all three paired runners named by the source note.
- Refresh only the changed runner-cache transcripts.
- Check that no audit ledger/queue/effective-status/publication/front-door
  generated files are included.
