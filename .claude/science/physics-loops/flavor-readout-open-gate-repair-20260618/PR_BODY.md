# Summary

This source-side PR repairs the fresh `audited_renaming` blocker for
`flavor_readout_gate_equals_carrier_identification_2026-05-31`.

The previous note advertised `bounded_theorem`, but the audit correctly found
that the row verifies finite algebra and gate bookkeeping, not a retained
derivation of the physical flavor observable. This PR narrows the source to
`open_gate` and hardens the runner to enforce that boundary.

# Changes

- Change the note claim type from `bounded_theorem` to `open_gate`.
- Add standard primary runner/cache links.
- Add a source-repair section for the next re-audit.
- Update the runner wording from theorem/derivation language to open-gate
  support language.
- Add source-boundary checks to the runner.
- Refresh the SHA-pinned cache.
- Add a branch-local physics-loop handoff packet.

# Verification

```bash
python3 scripts/flavor_readout_gate_equals_carrier_identification_2026_05_31.py
python3 scripts/cached_runner_output.py --check-only scripts/flavor_readout_gate_equals_carrier_identification_2026_05_31.py
python3 -m py_compile scripts/flavor_readout_gate_equals_carrier_identification_2026_05_31.py
git diff --check
```

Runner result: `SCORECARD PASS=11 FAIL=0`.

# Boundaries

This PR does not audit, retag, land, or edit ledger/status surfaces. It does
not derive the physical charged-lepton flavor observable. The single
carrier/basepoint premise remains open.
