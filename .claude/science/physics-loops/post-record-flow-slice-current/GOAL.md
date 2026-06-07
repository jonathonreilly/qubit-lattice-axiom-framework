# Goal

Repair the audit-blocked source packet for
`post_record_flow_thermal_stable_setting_certificate_2026-06-06`.

The concrete objective is not to retag the audit ledger. It is to make the
runner artifact exact on the current ledger snapshot by:

- checking the current flow/thermal stable-setting row map;
- printing the complete current ledger slice used by the runner;
- refreshing the SHA-pinned runner cache;
- leaving the claim at exact-support pending independent re-audit.
