# Summary

Source-side repair for the audited-failed `causal_impact_parameter_note` row.

The old runner fit alpha/R^2 against nominal `target_z` labels even though the
finite source layer saturated near the generated boundary. This PR reruns the
packet with enlarged transverse support, records source-anchor diagnostics,
fits against measured source-to-detector impact parameters, and narrows the
note to the repaired realized-b result.

# What changed

- `scripts/causal_impact_parameter_probe.py` now uses `HALF = 20` so requested
  `b = 5, 6, 7, 8, 10` anchors are physically realized.
- The log-log fit uses mean realized source-to-zero-field-detector-centroid
  transverse separation, not nominal labels.
- The runner emits hard PASS/FAIL checks for exact zero controls, realized
  anchors, strict realized-b ordering, source-side direction, and inverse-power
  fit stability.
- `docs/CAUSAL_IMPACT_PARAMETER_NOTE.md` now states the changed science: a
  steep realized-b inverse-power tail, not a `1/b` law, and no clean `c=0.5`
  finite-cone boundary.
- `logs/runner-cache/causal_impact_parameter_probe.txt` is refreshed.

# Verification

```bash
python3 scripts/causal_impact_parameter_probe.py
python3 scripts/cached_runner_output.py --refresh scripts/causal_impact_parameter_probe.py
python3 scripts/cached_runner_output.py --check-only scripts/causal_impact_parameter_probe.py
python3 -m py_compile scripts/causal_impact_parameter_probe.py
git diff --check
```

Observed runner checks: `PASS=5 FAIL=0`.

# Audit discipline

This PR does not audit, retag, or land anything. It does not edit audit result
files, publication effective-status files, front-door status, lane registry, or
the active review queue. Independent review/audit must decide whether the
source-side repair moves the existing row.
