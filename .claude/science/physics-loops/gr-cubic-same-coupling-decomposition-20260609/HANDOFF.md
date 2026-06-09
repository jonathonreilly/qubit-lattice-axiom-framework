# Handoff

## Result

This branch repairs the GR cubic conditional blocker by adding the requested
same-vielbein-coupled `dD/d2D/d3D` decomposition to
`scripts/frontier_universal_gr_cubic_graviton_seagull_vertex.py`.

The decomposition shows the old source claim was too broad. The same-coupling
`dD^3` triangle is nonzero in the trace channels, so the note now treats the
older conserved-vertex triangle as a separate comparator only. The durable
claim is narrowed to a finite W-native trace-channel/contact boundary.

## Verification

- `python3 scripts/frontier_universal_gr_cubic_graviton_seagull_vertex.py`
  - `TOTAL: PASS=7 FAIL=0`
- `python3 scripts/cached_runner_output.py scripts/frontier_universal_gr_cubic_graviton_seagull_vertex.py --refresh`

## Reviewer Focus

Please verify that this is the right source-side response to the audit blocker:

- It adds the missing same-coupling decomposition.
- It does not pretend the old separate triangle was the same-coupling
  paramagnetic term.
- It narrows rather than over-promotes.
- It keeps the GR-frontier boundaries explicit: no Einstein-Hilbert cubic
  closure, no cubic Ward identity, no pure-TT cubic vertex, no magnitude
  normalization.
