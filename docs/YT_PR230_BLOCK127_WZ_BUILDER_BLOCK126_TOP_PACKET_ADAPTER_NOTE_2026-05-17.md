# PR230 Block127 W/Z Builder Block126 Top-Packet Adapter

**Status:** bounded support / W/Z builder now recognizes the Block126 top-side
packet; W/Z rows, matched top-W/Z covariance, strict `g2`, and accepted action
remain absent

**Runner:** `scripts/frontier_yt_pr230_block127_wz_builder_block126_top_packet_adapter.py`

**Certificate:** `outputs/yt_pr230_block127_wz_builder_block126_top_packet_adapter_2026-05-17.json`

## Result

Block127 wires the Block126 matched top-side additive-subtraction packet into
`scripts/frontier_yt_wz_mass_fit_response_row_builder.py` as the default
top-side support input.

The adapter verifies:

- the Block126 packet is present and complete with 1008 same-configuration
  tau1 rows;
- the packet carries 23 complete tau slices;
- the selected mass is the middle mass, `0.75`;
- the `numba_gauge_seed_v1` seed-control metadata is preserved;
- the W/Z builder consumes the Block126 packet and recognizes it as top-side
  production support;
- the builder still refuses strict W/Z output because genuine W/Z rows,
  matched top-W/Z covariance, strict non-observed `g2`, accepted same-source
  EW/Higgs action, and canonical-Higgs/source-overlap authority remain absent;
- no strict measurement rows are written.

This prevents future W/Z route work from redoing the top-side packet discovery
or treating the old missing top-response certificate as the current blocker.
The current blocker is now explicitly the absent W/Z side and its strict
authority roots.

## Claim Boundary

Block127 is not W/Z closure and not `y_t` closure.  It does not:

- provide same-source W/Z mass-fit response rows;
- provide matched top-W/Z covariance;
- provide strict non-observed `g2`;
- provide accepted same-source EW/Higgs action authority;
- provide canonical-Higgs/source-overlap normalization;
- treat `dE_top/dm_bare` as `dE_top/dh`;
- assume top-W/Z factorization or covariance;
- use `H_unit`, `yt_ward_identity`, observed targets, observed W/Z values,
  `alpha_LM`, plaquette, or `u0`;
- set `kappa_s`, `c2`, `Z_match`, or `g2` to one;
- claim retained or `proposed_retained` closure.

## Exact Next Action

Supply genuine same-source W/Z mass-fit rows with configuration keys matchable
to the Block126 top-side packet, plus strict non-observed `g2` and accepted
same-source EW/Higgs action authority.  Then rerun the W/Z builder in strict
mode and rerun the same-source W/Z gates.
