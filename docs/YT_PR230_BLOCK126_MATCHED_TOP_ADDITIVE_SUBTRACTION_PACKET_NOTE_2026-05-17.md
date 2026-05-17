# PR230 Block126 Matched Top Additive-Subtraction Packet

**Status:** bounded support / matched top-side rows constructed; W/Z response,
matched top-W/Z covariance, strict `g2`, and accepted action remain absent

**Runner:** `scripts/frontier_yt_pr230_block126_matched_top_additive_subtraction_packet.py`

**Certificate:** `outputs/yt_pr230_block126_matched_top_additive_subtraction_packet_2026-05-17.json`

## Result

Block126 consumes the completed higher-shell production files and joins the
same-configuration source-response and top mass-scan rows into the top-side
part of the additive-subtraction contract:

`T_total = dE_top/ds`, `A_top = dE_top/dm_bare`, and
`T_minus_A = T_total - A_top`.

The runner finds:

- 63/63 raw production files;
- `numba_gauge_seed_v1` seed control across all files;
- selected-mass-only scalar FH/LSZ policy across all files;
- preserved 3-mass top correlator scans across all files;
- selected mass parameter `0.75`;
- 1008 same-configuration matched tau1 rows;
- 23 tau slices with complete same-configuration matching;
- tau1 mean `T_total = 1.245693776284446`;
- tau1 mean `A_top = 1.2732143441892123`;
- tau1 mean `T_minus_A = -0.02752056790476608`;
- tau1 `corr(T_total, A_top) = 0.9905564447030847`;
- exact variance identity check for `T-A` with absolute error
  `1.1858461261560205e-19`.

This is a real same-configuration top-side covariance packet.  It retires the
coarse-row limitation of the older additive-top Jacobian support, but only for
the top-side source and bare-mass responses already present in the completed
chunk files.

## Claim Boundary

Block126 is not W/Z closure and not `y_t` closure.  It does not:

- treat `dE/dm_bare` as `dE/dh`;
- provide W/Z response rows under the same source;
- provide matched top-W/Z covariance;
- provide strict non-observed `g2`;
- provide an accepted same-source EW/Higgs action;
- provide canonical-Higgs/source-overlap normalization;
- use `H_unit`, `yt_ward_identity`, observed targets, `alpha_LM`, plaquette,
  or `u0`;
- set `kappa_s`, `c2`, `Z_match`, `g2`, or `delta_perp` by convention;
- claim retained or `proposed_retained` closure.

The additive-subtraction contract still requires genuine same-source W/Z
response production rows, matched top-W/Z covariance, strict non-observed `g2`,
and accepted same-source EW/Higgs action authority.  Without those rows, this
packet is bounded support only.

## Exact Next Action

Run genuine same-source W/Z response production under the same scalar source,
join those rows with this top-side packet into matched top-W/Z covariance, and
supply strict non-observed `g2` plus accepted same-source EW/Higgs action
authority.
