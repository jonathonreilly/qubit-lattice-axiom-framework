# Handoff

This branch adds a restricted-packet verifier for
`koide_q_reduced_observable_restriction_theorem_2026-04-22`.

It verifies three source-side facts:

- the parent reduced determinant theorem still has cached exact algebra;
- the physical charged-lepton carrier/readout bridge is explicitly open; and
- `D_red = I_2` is not derived by the split determinant algebra alone.

Verification commands:

```bash
python3 -m py_compile scripts/koide_q_reduced_reaudit_packet_verifier_2026_06_17.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py scripts/koide_q_reduced_reaudit_packet_verifier_2026_06_17.py --check-only
python3 scripts/koide_q_reduced_reaudit_packet_verifier_2026_06_17.py
git diff --check
git diff -- docs/audit docs/publication/ci3_z3 docs/repo/FRONT_DOOR_STATUS.md
```

No audit-owned files were edited. The result is not a positive retained
bridge; it is a clean source packet for reviewer/auditor handling.
