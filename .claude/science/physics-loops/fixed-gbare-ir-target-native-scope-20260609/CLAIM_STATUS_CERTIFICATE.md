# Claim Status Certificate

- Audit authority remains the independent audit lane.
- This PR does not edit `docs/audit/**`.
- This PR does not retag the ledger.
- This PR does not add axioms.
- The retained candidate surface is narrowed to the fixed-`g_bare=1`,
  `beta=6` target clarification plus the named open IR-gap target.
- Standard RG, two-loop, asymptotic-scaling, and dimensional-transmutation
  diagnostics are not load-bearing in the restricted packet.

Verification commands:

```bash
python3 scripts/fixed_gbare_interacting_existence_ir_target_reframing_2026_06_08.py
python3 scripts/cached_runner_output.py scripts/fixed_gbare_interacting_existence_ir_target_reframing_2026_06_08.py
python3 -m py_compile scripts/fixed_gbare_interacting_existence_ir_target_reframing_2026_06_08.py
git diff --check
git diff --name-only -- docs/audit
```
