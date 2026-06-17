# Goal

Unblock two critical GR route audit rows by registering existing source-side
runners and repairing stale runner wording.

Target rows:

- `s3_anomaly_spacetime_lift_note`
- `universal_gr_tensor_variational_candidate_note`

The repair is intentionally source-side only. It does not update generated
audit data, does not land to main, and does not claim retained status.
