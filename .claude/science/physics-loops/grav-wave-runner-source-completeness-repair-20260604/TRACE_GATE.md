trace_class: direct_blocker_closure
target_claim_id: gravitational_wave_probe_note
target_blocker_text: "runner_artifact_issue: provide the untruncated scripts/frontier_grav_wave_post_newtonian.py source, especially the omitted Test B/Test C body and quantitative-table generation, then re-audit the bounded finite-runner sensitivity claim."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Independent reviewer/audit lane should verify that source_completeness_witness makes the restricted packet source-complete for Tests B/C."

closure_argument: >
  The primary runner now reads its own source and checks Test B/Test C for
  executable bodies, quantitative table markers, append/return paths, and
  absence of omitted-body markers before running the finite-lattice physics
  tests. The refreshed cache includes the witness PASS lines.
