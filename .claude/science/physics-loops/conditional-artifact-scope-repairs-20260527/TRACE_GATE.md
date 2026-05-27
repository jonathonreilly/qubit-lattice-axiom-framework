trace_class: direct_blocker_closure
target_claim_id:
  - gate_b_grown_joint_package_note
  - gravity_clean_derivation_note
source_of_blocker_text: audit_ledger
target_blocker_text:
  gate_b_grown_joint_package_note: "runner_artifact_issue — update docs/GATE_B_GROWN_JOINT_PACKAGE_NOTE.md so the frozen Born values match the current cached runner output, or add an explicit SHA-pinned explanation reconciling logs/2026-04-05-gate-b-grown-joint-package.txt with the current cache; then re-audit the same bounded scope."
  gravity_clean_derivation_note: "scope_too_broad: rewrite the source note so every binding claim is the bounded IF-chain only, remove or explicitly supersede the single-axiom/zero-free-parameter/clean-chain prose, and add retained bridge theorems if any future audit is meant to derive L^{-1}=G_0, rho=|psi|^2, S=L(1-phi), or the lattice Green-function normalization rather than assume them."
reachability_to_target: closes
artifact_role: source_repair
next_trace_action: "Independent audit re-runs the now-ready unaudited rows."
