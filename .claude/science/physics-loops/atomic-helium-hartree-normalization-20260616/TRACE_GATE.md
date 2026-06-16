trace_class: direct_blocker_closure
target_claim_id: work_history.atomic.hydrogen_helium_atomic_companion_note_2026-04-18
target_blocker_text: "Correct the helium Hartree Coulomb-integral normalization, rerun the Hartree and Jastrow baselines, and have a second auditor re-check the non-load-bearing finite-Rydberg/d=3-selection prose is quarantined outside the scoped claim."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Reviewer/auditor checks whether the repaired runner/cache/note packet clears the failed row."

The Hartree runner now distinguishes one-electron density rho=|phi|^2 from
total density n=2rho. It certifies by brute-force small-grid summation that
sum rho V_H[rho] equals the one electron-pair integral, and that the total
density half-form counts twice this pair on the two-electron product-state
surface. Hartree and Jastrow caches were rerun after the repair.
