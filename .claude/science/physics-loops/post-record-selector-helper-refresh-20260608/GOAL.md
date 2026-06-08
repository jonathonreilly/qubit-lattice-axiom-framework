# Goal

Repair the immediate audit blockers on the post-record selector/tangent/readout prototype:

- the selector/tangent/readout row count is now `8`, not `7`;
- the helper source must be visible as a static dependency, not only dynamically loaded;
- the helper export and cache must match the current ledger snapshot.

The deeper missing bridge remains open: this PR does not derive the carrier, readout map, weights, metric, or Hessian from Record.
