# Temporary source-identity controls

RECORD.json maps every archived gzip file to its exact uncompressed bytes.
Four baselines exit 0. Two incorrect source-diff conventions and four byte
corruptions exit 1 for their exact expected reasons. Full stdout, stderr,
argv, interpreter, timeouts, timings, return codes and modified source diffs
are preserved. The temporary fixture was restored, then removed; original
inputs stayed unchanged. This is source-identity evidence, not mathematical
mutation testing or canonical prepare/verify evidence.
