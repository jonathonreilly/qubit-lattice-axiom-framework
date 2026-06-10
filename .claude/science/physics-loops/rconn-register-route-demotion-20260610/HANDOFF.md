# Rconn Register-Not-Read Route-Demotion Handoff

## Target

`rconn_kappa_ew_register_not_read_color_trace_open_gate_note_2026-06-08`

Prior audit blocker:

```text
missing_bridge_theorem: retain a theorem that register-not-read governs this color operator-trace split and treats the trace channel as unregistered reference.
```

## Repair Summary

This branch does not try to prove `kappa_EW = 0`. It repairs the Rconn source
surface by demoting the specific route that attempted to get `kappa_EW = 0`
from register-not-read on the color trace.

The runner now verifies the decisive obstruction:

- the singlet map is the SU(3) depolarizing twirl target, not a finite
  central-sector partition map;
- the exact `8/9` value is a channel-count fraction, not a physical singlet
  weight selector;
- the current Record/Quantum axiom memo does not supply the missing readout
  context or physical observable bridge.

## Verification

```text
python3 scripts/frontier_rconn_kappa_ew_register_not_read.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_rconn_kappa_ew_register_not_read.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_rconn_kappa_ew_register_not_read.py
python3 -m py_compile scripts/frontier_rconn_kappa_ew_register_not_read.py
git diff --check
git diff --name-only -- docs/audit
```

Latest runner result: `TOTAL: PASS=18 FAIL=0`.

## Remaining Blocker

The wider `kappa_EW` gate remains open. A future physical EW readout/weighting
theorem, explicit convention, or owner-approved admission would be a different
route and is not foreclosed by this repair.
