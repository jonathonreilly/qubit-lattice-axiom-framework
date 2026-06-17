# Goal

Repair the stale primary runner for the critical
`s3_anomaly_spacetime_lift_note` audit lane so it checks the current honest
open-gate boundary instead of failing on old exact/closed wording.

No audit data, ledger verdict, queue row, publication status, or front-door
status is edited.
