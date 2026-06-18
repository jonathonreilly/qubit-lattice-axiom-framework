# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Human Tier-A registry note | Source description of admitted-input governance | meta governance | `docs/ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md` | Yes | Yes | Existing source | Checked by runner |
| Machine Tier-A registry | Machine-readable two-target registry | meta governance | `docs/audit/data/tier_a_admissions.json` | Yes | Yes | Existing registry | Checked by runner |
| Axiom-premise registry | Separates axioms/primitives from Tier-A admissions | framework-derived registry surface | `docs/audit/data/axiom_premise_nodes.json` | Yes | Yes | Existing registry | Checked by runner |
| Admission count and target set | Ensures count remains two and only AC_phi_lambda/theta are target ids | governance boundary | source + JSON | Yes | Yes | Existing owner-approved sharpening | Checked by runner |
| Negative status boundary | Prevents source note from implying audit/status changes | governance boundary | source note | Yes | Yes | Source note already states it | Checked by runner |

No observed target value, fitted selector, new axiom, or admission retirement is used.
