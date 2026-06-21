# Goal

Refresh the audit packet helper-dependency map after the latest ledger/main
updates and the runner-path canonicalization repairs.

Also fix a null-runner canonicalization bug found during the refresh:
`runner_path: null` was becoming the literal string `"None"`, which made the
packet-deps resolver report false missing runner files. Null runner paths now
remain empty/no-runner rows.
