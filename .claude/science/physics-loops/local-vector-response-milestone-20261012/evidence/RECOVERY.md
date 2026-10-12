# Archival byte recovery

Three original reviewer-linked files carry significant diff-context or terminal
whitespace. Their exact bytes and hashes are stored in ARCHIVAL_BYTES_v1.json;
the originals remain untouched locally. This prevents ordinary source-whitespace
checks from rewriting historical evidence. Original reviewer reports/manifests
are immutable and keep their original paths. Recover any named file by decoding
its base64 entry to that original_path in a separate checkout; verify its SHA-256
before use. No proof, numerical output or failed attempt was discarded. All
other original snapshots are committed directly.
