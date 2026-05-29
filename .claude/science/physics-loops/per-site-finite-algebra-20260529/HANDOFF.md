# Handoff

This block repairs the per-site finite-algebra cluster that was conditional
because it leaned on the older per-site uniqueness note for physical
`H_x = C^2`. The repaired source notes are A1-local:

- A1 supplies `A_x = M_2(C) = End(C^2)`.
- retained Pauli-irrep uniqueness is used only for Pauli generator
  uniqueness, not for physical Hilbert identification.
- the runners include source firewalls checking this boundary.

Verification run:

```text
python3 -m py_compile scripts/no_per_site_bosonic_ccr_check.py scripts/q_integer_spectrum_check.py scripts/per_site_su2_spin_half_check.py scripts/no_per_site_chirality_check.py
python3 scripts/no_per_site_bosonic_ccr_check.py
python3 scripts/q_integer_spectrum_check.py
python3 scripts/per_site_su2_spin_half_check.py
python3 scripts/no_per_site_chirality_check.py
bash docs/audit/scripts/run_pipeline.sh
```

All passed. The pipeline reported `re-audit required (hash changed): 4`
and audit lint ended with notices only.

The reviewer should extract the source-note/runners science and rerun the
pipeline from current main before landing. This loop does not merge the PR.
