# Goal

Repair one high-fan-in source-side dependency edge in
`anomaly_forces_time_theorem`.

The parent theorem needs the HY-surface calculation: a selected-axis cube
surface with a residual complementary-axis swap, a `3 + 1` base split, and a
traceless `u(1)` direction with spectrum `{+1/3 x6, -1 x2}` after weak-fiber
doubling. That content is in `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md` and is
recomputed by `scripts/frontier_anomaly_forces_time.py`.

The source repair makes that parent theorem cite the graph-first selected-axis
parent directly, while leaving the separate abelian-surface packaging as
non-load-bearing provenance context. It does not derive P-HY or change the
bounded anomaly/B-AXIS scope.
