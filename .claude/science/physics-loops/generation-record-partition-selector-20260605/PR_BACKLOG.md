# PR Status

Opened and verified:
https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2703

## Title

[physics-loop] generation record partition selector bounded-support

## Body summary

Adds a bounded theorem for the generation partition gate. Given the supplied
C3 generation carrier and fixed K/CPT readout context, the native
Record-compatible central partition is uniquely `P0 | P1`.

Key checks:

- complex character projectors `P0,P+,P-` are central idempotents;
- K/CPT fixes `P0` and swaps `P+ <-> P-`;
- exact real central idempotent enumeration gives only `0,I,P0,P1`;
- K-real C3-invariant observables cannot split the faithful doublet;
- `J=i(C-C^2)` splits the doublet but is K-odd.

Runners:

- `python3 scripts/generation_record_partition_selector_2026_06_05.py`
  with PASS=25 FAIL=0.
- `python3 scripts/record_generation_readout_two_sectors_2026_06_05.py`
  with PASS=32 FAIL=0.

This selects the partition only. It does not select weights, probability,
dynamics, or a charged-lepton value.
