# Gate B No-Restore Joint Package Note

**Date:** 2026-04-05  
**Status:** bounded single-seed no-restore Born / interference / decoherence
replay on the same grown-geometry family

## Artifact chain

- [`scripts/gate_b_no_restore_joint_package.py`](../scripts/gate_b_no_restore_joint_package.py)
- [`logs/2026-04-05-gate-b-no-restore-joint-package.txt`](../logs/2026-04-05-gate-b-no-restore-joint-package.txt)
- [`outputs/gate_b_no_restore_recompute_certificate_2026_06_07.json`](../outputs/gate_b_no_restore_recompute_certificate_2026_06_07.json)
- [`logs/runner-cache/gate_b_no_restore_joint_package.txt`](../logs/runner-cache/gate_b_no_restore_joint_package.txt)

Runner behavior for audit replay:

- default: verify the frozen log rows against the completed 2026-06-07
  recompute certificate, the exact-grid/no-restore-zero identity, bounded
  metric ranges, safe interpretation text, and live replay time marker
- `--recompute --write-certificate`: run the live one-seed package replay and
  write the recompute certificate used by the default verifier

## 2026-06-07 recompute repair

The 2026-06-07 audit marked this row conditional for a runner-artifact issue:

```text
runner_artifact_issue: add a completed --recompute output or a cached
recompute certificate and have the verifier compare each frozen row against
those computed values.
```

This repair runs:

```text
python3 scripts/gate_b_no_restore_joint_package.py --recompute --write-certificate
```

and records the completed live replay in
`outputs/gate_b_no_restore_recompute_certificate_2026_06_07.json`. The default
verifier compares every frozen row against the certificate and exits:

```text
SCORECARD PASS=8 FAIL=0
```

## Question

What survives on the same grown-geometry family if the restoring force is
removed entirely?

This note freezes a single-seed bounded replay of:

- Born
- `d_TV`
- `MI`
- CL-bath decoherence

on:

- exact grid
- no-restore grown rows at a few drift values

## Safe read

This note is intentionally narrow.

- It does not claim a full generated-geometry closure.
- It isolates the no-restore lane only.
- It should be read as a companion to the retained restore-based grown-geometry
  notes, not as a replacement.

The bounded read answers a single question:

- how much of the non-gravity joint package survives when `restore = 0`?

## Frozen result

The one-seed replay reports:

- exact grid: Born `2.12e-15`, `d_TV = 0.787`, `MI = 0.568`,
  decoherence `49.4%`
- no restore drift `0.0`: Born `2.12e-15`, `d_TV = 0.787`, `MI = 0.568`,
  decoherence `49.4%`
- no restore drift `0.2`: Born `2.01e-15`, `d_TV = 0.596`, `MI = 0.314`,
  decoherence `1.0%`
- no restore drift `0.5`: Born `1.31e-15`, `d_TV = 0.971`, `MI = 0.811`,
  decoherence `4.3%`

## Safe read

- `restore = 0` with zero drift reproduces the exact-grid package on this seed.
- once drift is turned on, the joint package becomes highly drift-sensitive.
- the no-restore lane is therefore a bounded probe, not a stability claim.

This is the cleanest honest read from the frozen replay.
