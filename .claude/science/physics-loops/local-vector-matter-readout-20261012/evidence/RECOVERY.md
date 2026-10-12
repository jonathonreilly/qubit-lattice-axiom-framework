# Exact historical recovery

ARCHIVAL_BYTES_v1.json stores exact old diff bytes with original whitespace.
Decode data using base64, verify bytes and SHA256, restore to the stated
repository-relative path. Original local copies are unchanged and untracked.
EXECUTED_RUNNER_v1.json preserves the initial canonical runner before a
one-space hygiene correction; its AST is unchanged. v1 JSON/cache returns
still refer to those old bytes. The new canonical cache uses a fresh run.
