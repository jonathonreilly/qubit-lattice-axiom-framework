trace_class: direct_blocker_closure
target_claim_id: "record-iid-typicality-firewall"
target_blocker_text: "Does a one-shot record-production probability vector supply IID frequencies or typicality?"
source_of_blocker_text: "record prerecord instrument kernel gate / campaign queue"
reachability_to_target: prunes
artifact_role: no_go
next_trace_action: "Require an explicit IID/sequence-law premise before frequency or typicality claims."

# Trace Gate

This artifact prunes the shortcut from one-shot probabilities to IID/frequency
typicality. It preserves future routes that explicitly supply a sequence law.
