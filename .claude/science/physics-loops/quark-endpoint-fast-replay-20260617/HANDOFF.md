# Quark Endpoint Fast Replay Handoff

## Target

The current audit runner breakage inventory lists the critical quark endpoint
law runners as timeout-limited:

- `scripts/frontier_quark_e_channel_endpoint_quotient_law.py`
- `scripts/frontier_quark_endpoint_ratio_chain_law.py`

Both runners passed in the existing cache, but the old replay path spent about
219 seconds because it repeatedly imported and recomputed the slow tensor
endpoint readout plus non-load-bearing refit diagnostics.

## Change

- Adds a fast endpoint certificate replay path to
  `scripts/frontier_quark_endpoint_readout_constraints.py`.
- Keeps the full tensor recomputation available with
  `QUARK_ENDPOINT_FULL_TENSOR_REPLAY=1`.
- Makes the two endpoint law runners skip non-load-bearing refit diagnostics
  while preserving the bounded law, chain, anchored-branch, and traceability
  checks.
- Refreshes the affected runner caches.
- Adds explicit runner-cache metadata and replay-boundary notes to the source
  notes.

## Honest Boundary

This does not derive the missing E-center primitive, does not repair the
audited numerical-match verdict into retained status, and does not claim
quark endpoint closure. The retained Route-2 no-go boundary still says the
restricted carrier/readout class leaves `rho_E` free until an additional
E-center primitive or stronger readout-map theorem is supplied.

## Verification

```bash
python3 scripts/frontier_quark_endpoint_readout_constraints.py
QUARK_ENDPOINT_FULL_TENSOR_REPLAY=1 python3 scripts/frontier_quark_endpoint_readout_constraints.py
python3 scripts/frontier_quark_e_channel_endpoint_quotient_law.py
python3 scripts/frontier_quark_endpoint_ratio_chain_law.py
python3 scripts/frontier_quark_route2_exact_readout_map.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_quark_endpoint_readout_constraints.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_quark_e_channel_endpoint_quotient_law.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_quark_endpoint_ratio_chain_law.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_quark_route2_exact_readout_map.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_quark_up_amplitude_candidate_scan.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_quark_endpoint_readout_constraints.py,scripts/frontier_quark_e_channel_endpoint_quotient_law.py,scripts/frontier_quark_endpoint_ratio_chain_law.py,scripts/frontier_quark_route2_exact_readout_map.py,scripts/frontier_quark_up_amplitude_candidate_scan.py --check-only
python3 -m py_compile scripts/frontier_quark_endpoint_readout_constraints.py scripts/frontier_quark_e_channel_endpoint_quotient_law.py scripts/frontier_quark_endpoint_ratio_chain_law.py scripts/frontier_quark_route2_exact_readout_map.py scripts/frontier_quark_up_amplitude_candidate_scan.py
git diff --check
git diff -- docs/audit docs/publication docs/repo/FRONT_DOOR_STATUS.md --stat
```
