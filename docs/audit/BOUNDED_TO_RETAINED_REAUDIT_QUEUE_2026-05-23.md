# Bounded-to-Retained Re-audit Queue (2026-05-23)

**Purpose:** rank high-leverage `retained_bounded` rows that look eligible
for claim-type / scope re-audit as `positive_theorem` without adding any new
framework axiom.

**Operating rule:** this queue does not retag the ledger. It only identifies
rows that should be opened for direct review. The reviewer/audit lane owns any
claim-type change.

**Baseline:** current `origin/main` at `8e33d17fd` after
`bash docs/audit/scripts/run_pipeline.sh`.

**Selection rule:** prefer already-audited clean `bounded_theorem` rows with
large downstream reach where the safe positive scope is exact local algebra,
finite representation theory, onset coefficients, or operator realization.
Longer descendant chains are ranked first. Rows whose bounded status protects
a still-open physical closure are only listed with a narrowed safe scope.

## Highest-Impact Queue

| Rank | Claim id | Downstream | Current status | Proposed re-audit scope | Why this can help |
|---:|---|---:|---|---|---|
| 1 | `native_gauge_closure_note` | 1126 | `retained_bounded` | Split/narrow to exact native cubic `Cl(3)` / `SU(2)` plus retained graph-first structural `SU(3)` closure; keep abelian/hypercharge-like surface bounded. | Highest reach. The bounded part is the abelian surface, not the exact nonabelian graph-first closure. |
| 2 | `gauge_vacuum_plaquette_transfer_operator_character_recurrence_note` | 1101 | `retained_bounded` | Exact transfer-operator / character-recurrence realization of the finite Wilson plaquette generating object. | The beta=6 transfer-state identification remains open, but the operator realization itself is exact. |
| 3 | `gauge_scalar_temporal_completion_theorem_note` | 1095 | `retained_bounded` | Exact universal temporal completion law for the accepted Wilson nearest-neighbor local bosonic scalar gauge-source class. | No new axiom required; source note already frames this as an exact theorem on the accepted source class. |
| 4 | `gauge_vacuum_plaquette_mixed_cumulant_audit_note` | 1094 | `retained_bounded` | Exact first nonlinear coefficient / onset theorem for the Wilson plaquette reduction law. | Does not claim full beta=6 closure; the scoped coefficient theorem looks positive. |
| 5 | `gauge_vacuum_plaquette_reduction_existence_theorem_note` | 1081 | `retained_bounded` | Exact existence and uniqueness of the implicit finite Wilson reduction law. | Source says explicit nonperturbative beta=6 characterization remains open; the implicit-law theorem is narrower and exact. |
| 6 | `scalar_3plus1_temporal_ratio_note` | 1079 | `retained_bounded` | Exact scalar bridge endpoint ratio `A_inf / A_2 = 2 / sqrt(3)` on the minimal APBC `3+1` block. | The dimension-4 observable insertion stays support-only; the endpoint ratio itself is exact. |
| 7 | `gauge_vacuum_plaquette_connected_hierarchy_theorem_note` | 1078 | `retained_bounded` | Exact connected plaquette cumulant hierarchy on the finite Wilson source surface. | The full beta=6 reduction law remains open, but the hierarchy identity is exact. |
| 8 | `gauge_vacuum_plaquette_spectral_measure_theorem_note` | 1078 | `retained_bounded` | Exact compact positive spectral-measure equivalence for the finite Wilson connected plaquette hierarchy. | Explicit beta=6 spectral-measure identification remains open; existence/uniqueness is exact. |
| 9 | `gauge_vacuum_plaquette_distinct_shell_theorem_note` | 1078 | `retained_bounded` | Exact minimal distinct-shell geometry around a marked plaquette on the accepted Wilson `3+1` surface. | Strong candidate after or alongside the mixed-cumulant onset row; full reduction law remains out of scope. |
| 10 | `su3_wigner_intertwiner_block2_theorem_note_2026-05-03` | 1090 | `retained_bounded` | Exact finite-rank `SU(3)` projector construction for `(1,1)^4` / `C^4096`. | Finite representation-theoretic construction can be retained as a scoped theorem without promoting the cube-closure campaign. |
| 11 | `s3_taste_cube_decomposition_note` | 1033 | `retained_bounded` | Abstract `S_3` representation theorem on `C^8 = (C^2)^3`; no physical taste-cube carrier promotion. | The framework-carrier interpretation remains gated, but the abstract finite-group theorem is closed. |

## Explicit Non-Automatic Cases

- `higgs_from_lattice_note` has high downstream reach but is explicitly
  bounded quantitative support only. Do not target it for promotion without a
  separate Higgs authority-boundary rewrite.
- `gauge_vacuum_plaquette_rho_pq6_wilson_environment_bounded_note_2026-05-09`
  is useful but intentionally finite-box coefficient support. It can be
  reconsidered later if the audit lane wants finite coefficient tables to land
  as scoped positive theorems.
- Rows blocked by the source-coupled local-action admission candidate are not
  included here. No new axiom or convention is assumed by this queue.

## Review Notes

- Re-audit each row independently; do not bulk-retag.
- Keep stronger physical closures out of the positive scope.
- If a row needs source-note surgery first, land that as a separate review
  packet before requesting audit.
- Use the JSON companion at
  `docs/audit/data/bounded_to_retained_reaudit_queue_2026-05-23.json` for
  dispatcher tooling.
