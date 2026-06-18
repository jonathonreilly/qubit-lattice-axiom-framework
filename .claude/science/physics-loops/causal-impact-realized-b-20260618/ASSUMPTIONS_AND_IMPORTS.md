# Assumptions And Imports

- No new axiom is introduced.
- The center growth-rule parameters remain `drift = 0.20`, `restore = 0.70`,
  `h = 0.5`, `n_layers = 13`, and seeds `0..5`.
- The transverse support is enlarged to `HALF = 20` so the requested
  `b = 5, 6, 7, 8, 10` source anchors are physically realized.
- The fitted coordinate is the measured transverse separation between the
  selected source anchor and the zero-field detector centroid.
- `scripts/evolving_network_prototype_v6.py` is used as an executable bounded
  harness source. This PR does not claim that its growth constructor,
  propagator, field carrier, detector-centroid metric, or thresholds are
  derived from accepted primitives.
- Literature supplies no load-bearing proof input in this block.
