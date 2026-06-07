# Handoff

This is a stacked PR on top of PR #3029.

It updates the delta-sign theorem so the audit no longer has to accept a
single sampled sign propagation. The runner now proves:

```text
K_C3 = t^2 delta / (eps_gap (eps_gap + delta))
```

and restricts `K_C3 < 0` to:

```text
eps_gap > 0
eps_gap + delta > 0
```

The stacked periodic-kernel bridge supplies the generation-pair density
normalization and `delta_ij < 0` for the retained hw=1 corners. The remaining
open item is physical IR/gap closure, not algebraic sign propagation.

Verification:

```bash
PYTHONPATH=scripts python3 scripts/delta_sign_from_retained_mediator_runner.py
# TOTAL: PASS=20 FAIL=0
```
