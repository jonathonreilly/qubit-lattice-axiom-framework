# Handoff

This PR refreshes three runner caches that became stale after the latest main
landing:

- `logs/runner-cache/frontier_pmns_graph_first_axis_alignment.txt`
- `logs/runner-cache/frontier_registrable_readout_additive_even_phase_free_2026_06_10.txt`
- `logs/runner-cache/frontier_yt_p1_bz_quadrature_full_staggered_pt.txt`

It does not edit audit data or claim any audit outcome. The runners all
completed successfully during the targeted refresh.

Expected remaining full-ledger cache blockers after this PR alone:

- `toy_event_physics.py`, covered by PR #4005.
- `scripts/kinetic_isotropy_3d_simultaneous_tick_2026_06_10.py`, covered by
  PR #3991.

