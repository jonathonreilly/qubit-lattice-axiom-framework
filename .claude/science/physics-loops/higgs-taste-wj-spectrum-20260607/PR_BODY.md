# Summary

This PR repairs the Higgs taste-count/W(J) bridge by deriving the tadpole mean-field uniform paired spectrum inside the explicit `Cl(4)` block.

It replaces the extra "bounded paired-spectrum hypothesis" with runner-checked finite algebra:

- `D_taste^2 = 4I`
- `D_mf = i u_0 D_taste`
- `char(D_mf)(λ) = (λ^2 + 4u_0^2)^2`
- `det(D_mf + JI_4) = (J^2 + 4u_0^2)^2`

The branch does not touch `docs/audit/**`, does not set audit status, and does not claim a physical Higgs mass prediction.

# Verification

```bash
PYTHONPATH=scripts python3 scripts/audit_companion_higgs_lattice_taste_count_wj_form_2026_06_05.py
```

Result:

```text
TOTAL: 53 PASS / 0 FAIL
```

# Handoff

See `.claude/science/physics-loops/higgs-taste-wj-spectrum-20260607/HANDOFF.md`.
