# No-Go Ledger

## Do Not Treat Null Runner Paths As Missing Files

Observation: `canonical_runner_path(None)` previously returned `"None"`.
`audit_packet_script_deps.py` then counted null runner rows as missing runner
files.

Status: blocked by this PR's null-to-empty canonicalization rule.

## Do Not Run Audits From This Map

The refreshed packet-deps map is an audit packet assembly support surface only.
It is not itself an audit verdict source.
