# Handoff

Changed source packet:

- `docs/KOIDE_DIRAC_MASS_FORCES_R_ONE_LR_COUPLING_BERRY_FLAT_BOUNDED_NO_GO_NOTE_2026-06-05.md`
- `scripts/audit_companion_koide_dirac_mass_forces_r_one_exact.py`

Science move:

- Adds a conditional-row source firewall that explicitly chooses the algebraic
  narrowing route from the audit blocker.
- Strengthens the runner from 6 source/algebra checks to 11 checks.
- Verifies the determinant sign, open branch-selection bridge, r=1/r=1/2
  firewalls, and non-load-bearing staggered-gate pointer.

Verification:

```bash
python3 -m py_compile scripts/audit_companion_koide_dirac_mass_forces_r_one_exact.py
python3 scripts/audit_companion_koide_dirac_mass_forces_r_one_exact.py
python3 scripts/cached_runner_output.py scripts/audit_companion_koide_dirac_mass_forces_r_one_exact.py --refresh --timeout-sec 120
python3 scripts/cached_runner_output.py scripts/audit_companion_koide_dirac_mass_forces_r_one_exact.py --check --timeout-sec 120
```

Expected runner result:

```text
11 PASS, 0 FAIL
```

No audit ledger or publication-status file is edited.
