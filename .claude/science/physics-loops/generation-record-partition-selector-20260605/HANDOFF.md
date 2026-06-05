# Handoff - Generation Record Partition Selector

## Summary

This block attacks the partition gate for the dynamics program. It proves that
given the supplied C3 generation carrier and fixed K/CPT readout context, the
native Record-compatible central partition is uniquely:

```text
singlet P0 | faithful doublet P1.
```

The three complex character sectors are not three native Record letters because
K/CPT swaps the faithful pair. Splitting the doublet requires the K-odd
orientation operator `i(C-C^2)`.

## Files

- `docs/GENERATION_RECORD_PARTITION_SELECTOR_2026-06-05.md`
- `scripts/generation_record_partition_selector_2026_06_05.py`
- `logs/runner-cache/generation_record_partition_selector_2026_06_05.txt`
- `.claude/science/physics-loops/generation-record-partition-selector-20260605/`

## Verification

- `python3 scripts/generation_record_partition_selector_2026_06_05.py`
  -> PASS=25 FAIL=0.
- `python3 scripts/record_generation_readout_two_sectors_2026_06_05.py`
  -> PASS=32 FAIL=0.

Review PR:
https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2703

## Meaning

The partition half of the dynamics gate is now a positive bounded theorem
candidate. The remaining gate is arrow/measure selection on that partition.

## Next exact action

Open a review PR. If accepted, next attack should target why the charged-lepton
record dynamics uses two-sector block-counting entropy rather than
dimension/Born weighting, sharpening, or transit.
