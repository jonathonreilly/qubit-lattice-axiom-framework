# Assumptions And Imports

| Item | Role | Status |
|---|---|---|
| `dimension_selection_finite_k_centroid_sign_bridge_note_2026-05-25` | Finite-k sign certificate used by the parent lower-bound row. | `audited_clean`, `retained_bounded` on current ledger |
| `dimension_selection_lower_bound_bridge_v2_2026-05-20` | Already-clean V2 lower-bound sign row. | `audited_clean`, `retained_bounded` on current ledger |
| `scripts/frontier_dimension_selection.py` | Original runner surface containing displayed beta, alpha, and `I_3` evidence. | Source/cache verified in this branch |
| `scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py` | Dynamically imported finite-k derivative machinery. | Source/cache verified in this branch |
| Source-packet manifest JSON/cache | Artifact-completeness verifier. | Zero-fail runner output verified in this branch |

Forbidden imports for this block:

- observed physical dimension as a proof input;
- textbook upper-bound mathematics as a closure input;
- a new axiom or baseline rewrite;
- an audit-lane status change.
