# Handoff

This branch registers the correct bounded runner packet for two
persistent-record rows.

The companion runs:

- side-bit slice:
  `--seeds 2 --gamma 1.0 --methods node,pr_trace,pr_soft,pr_side_trace,pr_side_soft`
- refinement slice:
  `--seeds 2 --gamma 1.0,1.5,2.0 --methods node,pr_side_packet_trace,pr_side_packet_soft,pr_side_packet_entry_trace,pr_side_packet_entry_soft`

It checks the frozen tables and the bounded conclusions:

- side-bit improves the soft persistent lane at N=12 and N=18 but remains
  behind node-label;
- side+packet+entry gives a tiny N=18 gamma=1.0 improvement over side+packet
  but remains behind node-label;
- gamma 1.5 and 2.0 worsen the N=18 side+packet+entry result relative to
  gamma 1.0.

Generated audit/publication outputs were restored after local pipeline
verification.
