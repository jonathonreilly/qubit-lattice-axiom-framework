# Handoff

This branch targets the audited conditional free-Dirac Poincare generator row.
It adds a bridge packet for the explicit mass-shell/Wigner action and wires the
parent runner to verify that bridge.

Verification:

```bash
python3 scripts/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.py
python3 scripts/free_dirac_poincare_generators_selfadjointness_2026-05-30.py
python3 -m py_compile scripts/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.py scripts/free_dirac_poincare_generators_selfadjointness_2026-05-30.py
git diff --check
```

Expected review outcome, if accepted: the missing dependency edge on the direct
unitary Wigner-action route is re-auditable. No audit result is changed here.
