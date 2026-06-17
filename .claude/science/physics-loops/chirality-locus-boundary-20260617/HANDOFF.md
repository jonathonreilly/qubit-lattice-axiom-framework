# Handoff

## What changed

The carrier-locus note and runner now make the physical-locus boundary exact:

- `hw=1` shell labels are finite and `S_3`-invariant, with no axis anisotropy.
- The parity label used to distinguish `hw=1` from `hw=2` is complement-odd.
- Exhaustive enumeration proves there is no `C_3`-invariant, complement-even
  three-corner projector.
- Therefore the physical choice of `hw=1` over Hodge-dual `hw=2` is still the
  Hodge-orientation bit, not a no-import consequence of the shell labels.

## Checks

```bash
python3 scripts/frontier_koide_carrier_locus_decomposition.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_koide_carrier_locus_decomposition.py
```

## Remaining blocker

The next science target is the records-pointer/sign(beta) bridge, or the larger
matter-operator `M` supply line. This PR does not close either.

## Integration note

Reviewer should extract the source repair if useful. Do not land audit verdicts
or publication status changes from this branch.
