## Science block

This closes the executable chain for the finite native-parity factorization obstruction in dimensions 1–3 and sides 2 and 4. The primary runner now verifies the exact `sigma_s Z_logical` environment blocks and balanced spectator-sign counts before applying its expected classification rules.

- [Target note](docs/TELEPORTATION_TASTE_READOUT_OPERATOR_MODEL_NOTE.md)
- [Primary runner](scripts/frontier_teleportation_taste_readout_operator_model.py)
- [Handoff](.claude/science/physics-loops/teleportation-taste-readout-factorization-20260711/HANDOFF.md)
- [Trace gate](.claude/science/physics-loops/teleportation-taste-readout-factorization-20260711/TRACE_GATE.md)
- [Claim-status certificate](.claude/science/physics-loops/teleportation-taste-readout-factorization-20260711/CLAIM_STATUS_CERTIFICATE.md)
- [Assumptions and imports](.claude/science/physics-loops/teleportation-taste-readout-factorization-20260711/ASSUMPTIONS_AND_IMPORTS.md)
- [Review history](.claude/science/physics-loops/teleportation-taste-readout-factorization-20260711/REVIEW_HISTORY.md)
- [No-go discipline](.claude/science/physics-loops/teleportation-taste-readout-factorization-20260711/NO_GO_DISCIPLINE_CHECKLIST.md)

Trace classification: `direct_blocker_closure`. No measured, fitted, observational, literature, selector, normalization, or physical-apparatus input is load-bearing.

Verification:

```text
python3 -m py_compile scripts/frontier_teleportation_taste_readout_operator_model.py
local certificate import check: PASS, 6/6 cases
independent itertools.product enumeration: PASS, 6/6 cases
python3 scripts/vocab_lint.py --fix <changed files>: 0 violations
bash docs/audit/scripts/run_pipeline.sh: complete
python3 docs/audit/scripts/audit_lint.py --strict: no errors
git diff --check: PASS
```

The full primary runner currently exits nonzero only at its separate downstream status guard because several downstream audit-controlled rows are `unaudited`; all local operator and no-record checks complete first. No generated audit/status surface is included in this branch.

Review-loop disposition: PASS. The overall claim remains an `open_gate`: apparatus dynamics, noisy readout, preparation, and heralded protocols remain open. Independent audit is required after landing before the repository may derive any effective status from this change.
