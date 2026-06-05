# Claim Status Certificate - Generation Record Partition Selector

**Loop slug:** `generation-record-partition-selector-20260605`  
**Date:** 2026-06-05  
**Branch:** `physics-loop/generation-record-partition-selector-20260605`  
**Review PR:** https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2703  
**Runner:** `scripts/generation_record_partition_selector_2026_06_05.py` -> PASS=25 FAIL=0  
**Cross-check:** `scripts/record_generation_readout_two_sectors_2026_06_05.py` -> PASS=32 FAIL=0

## Status fields

```yaml
actual_current_surface_status: open
target_claim_type: bounded_theorem
conditional_surface_status: bounded-support
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Claim

Given the supplied C3 generation carrier and fixed K/CPT readout context,
the native Record-compatible central partition is uniquely:

```text
P0 | P1
```

where `P0` is the singlet projector and `P1=P++P-` is the faithful doublet
orbit projector. Splitting `P1` requires the K-odd orientation operator
`i(C-C^2)`.

## What remains open

- Weighting of `P0` versus `P1`.
- Probability/Born normalization.
- Time-arrow/source/action.
- Charged-lepton value selection.
