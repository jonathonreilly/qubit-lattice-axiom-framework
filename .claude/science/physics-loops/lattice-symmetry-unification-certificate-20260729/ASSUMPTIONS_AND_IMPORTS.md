# Assumptions and Imports

## Supplied finite contract

- `max_dy` is exactly `3, 4, 5, 6`.
- The aperture families are exactly `narrow_center`, `wide_center`, and
  `wide_outer`.
- The mass offsets are exactly `-1, 0, +1`.
- The helper's standard field strength is exactly `0.1`.
- Retention thresholds are the literals printed and cross-checked by the
  certificate.

## Dependency classification

The certificate has no external literature or observational import. It
declares the primary decision runner and lattice helper as mutable repository
inputs so the cache fingerprint binds both. None of the approved framework
primitives in `docs/audit/data/axiom_premise_nodes.json` is load-bearing for
this finite software certificate.

## Counterfactual pass

Changing field strength, lattice family, aperture family, offsets, observable,
or retention thresholds defines a different computation. In particular, the
later weak-field positive pocket is real counterevidence to any blanket no-go,
but it does not alter the enumerated standard-strength result.
