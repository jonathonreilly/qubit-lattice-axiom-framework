## Summary

Repairs the Picard-Fuchs rank-bound citation row without narrowing to a
finite coefficient window.

The row now uses the existing all-order certificate as its primary support:

- `scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py`
- `logs/runner-cache/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.txt`
- `outputs/su3_v1_picard_fuchs_all_order_certificate_2026_05_09.json`

The note now states the `[T1]`-`[T5]` certificate chain: D-finiteness,
effective order-3 degree-2 minimal-annihilator certificate,
Bostan-Salvy-Schost threshold, Frobenius branch identification, and
depth-200 regression.

## Checks

- `python3 -m py_compile scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py`
- `bash docs/audit/scripts/run_pipeline.sh`
  - target row reset to `unaudited`
  - queue ready: `true`
  - open dependency paths: `[]`
  - runner classification dominant class: `C`

## Status

Branch-local status: bounded-support, re-audit ready.

This PR does not apply an audit verdict and does not claim effective
retained status. Independent audit remains required.
