# Valley-Linear Wide Tail Note

**Date:** 2026-04-04  
**Verifier repair:** 2026-06-07
**Status:** bounded wide-lattice replay on the 3D ordered-lattice `1/L^2` family

## One-line read

On the widened `h = 0.25`, `W = 12` replay for the 3D valley-linear branch,
the no-barrier distance tail is better resolved and the far-tail fit on the
tested `z >= 5` window is `b^(-1.17)` with high `R^2`.

That is a strong finite-lattice replay, not a universal theorem by itself.

## Primary artifact

- Script: [scripts/valley_linear_wide_tail_replay.py](../scripts/valley_linear_wide_tail_replay.py)
- Frozen replay log: [logs/2026-04-04-valley-linear-wide-tail-replay.txt](../logs/2026-04-04-valley-linear-wide-tail-replay.txt)
- Registered runner cache: [logs/runner-cache/valley_linear_wide_tail_replay.txt](../logs/runner-cache/valley_linear_wide_tail_replay.txt)

The registered runner defaults to a verifier for the frozen replay log above;
use `--recompute` to run the original slow wide-tail replay.

## 2026-06-07 verifier repair

The audit blocker asked for either a SHA-pinned completed recompute output or
frozen raw distance rows plus a verifier that recomputes the peak-tail and
far-tail fits from those rows rather than accepting prose strings. This note
takes the frozen-row verifier route:

- frozen raw replay log SHA-256:
  `2047f12a5143ac9501bacac31cc895fc278e47cf61372c8504d1ef1059a3d409`;
- the registered verifier parses the nine raw `z, delta, direction` rows;
- it recomputes the peak row (`z = 4`) from the parsed deltas;
- it recomputes the peak-tail fit from the parsed rows with `z >= 4`;
- it recomputes the far-tail fit from the parsed rows with `z >= 5`;
- current verifier scorecard: `SCORECARD PASS=9 FAIL=0`.

This replay keeps fixed:

- the 3D ordered-lattice family
- the valley-linear action `S = L(1-f)`
- the `1/L^2` kernel with `h^2` measure
- `h = 0.25`

It changes only the lattice width to improve the post-peak tail resolution.

## Frozen replay result

- barrier sanity:
  - Born remains machine-clean
  - `k = 0` remains exactly zero
- no-barrier distance rows:
  - `9/9` tested `z` rows remain TOWARD
  - peak remains near `z = 4`
- tail fits:
  - peak-tail fit from `z >= 4`: `b^(-1.07)`, `R^2 = 0.990`
  - far-tail fit from `z >= 5`: `b^(-1.17)`, `R^2 = 0.997`

## Safe interpretation

- The widened replay strengthens the 3D valley-linear distance-law story.
- On this tested finite-lattice window, the far tail is near-Newtonian and
  clearly resolved, but it is somewhat steeper than exact `1/b`.
- This is stronger than the earlier narrower-width replay because it has more
  post-peak support.

## What this is not

- A proof that every finer lattice will continue to fit the same exponent.
- A universal theorem for all dimensions.
- A replacement for the broader continuum / kernel-selection reconciliation.

The review-safe read is:

- the finite-lattice 3D valley-linear replay now has a stronger wide-tail
  confirmation
- that materially improves confidence in the bounded 3D distance-law claim
- the broader asymptotic and dimensional story still needs separate artifact
  chains
