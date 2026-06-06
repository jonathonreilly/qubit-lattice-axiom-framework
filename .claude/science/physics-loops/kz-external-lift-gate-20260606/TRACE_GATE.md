trace_class: direct_blocker_closure
target_claim_id: "2026-05-03-pr484-kz-external-lift-gate"
target_blocker_text: "do not land the K-Z / SU(3) external-lift package as a bounded theorem or parent status promotion while the runner fails without optional CVXPY and the load-bearing W_lift = 0.05 is not extracted from an explicit SU(3), beta=6 primary-source bracket"
source_of_blocker_text: active_review_queue
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Use the available CVXPY path for a repo-owned SU(3), beta=6 SDP reproduction, or find an explicit primary-source bracket."

# Trace Gate

This artifact partially closes the execution side of the active blocker:
CVXPY is available and a small PSD/Hausdorff SDP probe solves. It does not
close the primary-bracket provenance blocker, so the route remains open.
