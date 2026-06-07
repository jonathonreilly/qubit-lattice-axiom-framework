# Handoff

This branch repairs the audited `scope_too_broad` complaint by adding the exact
formula:

```text
K_eff = t^2 * U / (eps * (eps + U)).
```

The sign law is now stated only for `eps>0` and `eps+U>0`. The runner also
checks an `eps+U<0` control where the sign flips, so the narrower statement is
substantive rather than cosmetic.

Verification:

```bash
PYTHONPATH=scripts python3 scripts/interaction_asymmetry_delta_occupation_curvature_runner.py
python3 -m py_compile scripts/interaction_asymmetry_delta_occupation_curvature_runner.py
git diff --check
```
