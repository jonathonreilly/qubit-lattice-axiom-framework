# Handoff

This PR retires the avoidable textbook-math import for the BBN analytic
Planck factor. The note now includes the series proof for
`integral_0^infty x^2/(exp(x)-1) dx = 2 zeta(3)`, and the runner certifies
the `zeta(3)` reference by a partial p-series sum through `N=20000` with the
tail bound `1/(2N^2)`.

What remains open: P1 proton mass, P2 CMB temperature, P3 critical-density
unit inputs, photon polarization count, and P4 Cyburt residual are still
admitted physical/comparator inputs. The row should not be treated as a
framework derivation of the BBN coefficient.

Checks run:

```text
PYTHONPATH=scripts python3 scripts/bbn_eta10_to_omega_b_h2_coefficient_admission_bridge_runner.py
```

Result: `TOTAL: PASS=39 FAIL=0`.
