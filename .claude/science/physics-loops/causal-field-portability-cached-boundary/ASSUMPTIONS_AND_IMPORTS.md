# Assumptions And Imports

## Load-Bearing Inputs

- Committed cache: `logs/runner-cache/causal_field_portability_probe.txt`.
- Cache header: `families=3`, `seeds=6`, `source_layer=8`, `K=5.0`.
- Source anchor target: `(y, z) = (0.0, 3.0)`.
- Field strength and epsilon: `5.0e-05`, `0.1`.
- Dynamic cone values: `[1.0, 0.5]`.

## Not Imported As Proof

- A derivation of the growth constructor from accepted primitives.
- A derivation of the propagation or centroid carrier from accepted
  primitives.
- A derivation of the configured portability metric or threshold.
- A cross-family portability law.

The carrier and portability-criterion derivations remain open.
