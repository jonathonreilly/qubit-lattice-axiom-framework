# Collapse/Merger Comparator Engine Software Validation

**Date:** 2026-07-08
**Type:** meta
**Primary runner:**
[`scripts/collapse_merger_toy_engine_2026_07_08.py`](../scripts/collapse_merger_toy_engine_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/collapse_merger_toy_engine_2026_07_08.txt`](../logs/runner-cache/collapse_merger_toy_engine_2026_07_08.txt)

## Purpose

This artifact validates software intended for later collapse/merger comparator
experiments. It is a meta-level engine check, not a physics theorem and not
evidence that the framework produces attraction, collapse, mergers, gravity,
or an energy-to-record coupling.

## Imposed Comparator

Every coupling used by the engine is supplied:

- a periodic one-dimensional ring with `L = 400`;
- 200 indistinguishable, unrestricted-multiplicity parcel counts;
- the availability table
  `A(0), A(1), A(2) = 2.1, 1.1, 0.1` and normalized probe field
  `N(r) = A(r)/A(0)`;
- the directional hop bias
  `D = clip(beta [N_left - N_right]/2, -0.45, 0.45)`, with
  `beta = 0.6`, `p_right = (1+D)/2`, and `p_left = (1-D)/2`;
- discrete deposition probability
  `p_deposit = kappa * parcels * A(r)/A(0) * dt`, with `dt = 1` and
  supplied `kappa` values `0.002` and `0.01`;
- zero deposition on recorded or parcel-free sites;
- blocked hops wait at their source;
- a newly recorded site's parcels are relocated to the nearest remaining open
  site, with seeded splitting of equal-distance ties; and
- a terminal refuge rule that prevents the relocation rule from closing the
  final open site.

The attraction-directed sign is therefore imposed in the hop bias. The
deposition coupling is likewise imposed; neither is inferred from another
claim.

## Software Checks

The fixed-seed runner checks:

- exact parcel conservation and monotone record bits;
- response of accepted hop flux to the imposed directional bias, with an
  unbiased no-record control;
- record deposition only in a parcel-bearing pinned region, with a parcel-free
  control;
- decreasing offered and empirical deposition rates as the supplied
  availability table is crowded;
- blocking, zero transmission, and boundary accumulation at a pre-recorded
  block; and
- byte-for-byte deterministic final state, probe field, and random-generator
  state for same-seed reruns.

These checks validate implementation behavior only. Names such as
`collapse`, `merger`, `husk`, and `attraction` are experiment labels,
not conclusions of this meta artifact.

## Dependencies

None. The comparator equations and couplings are declared in this note and
implemented directly in the paired runner.
