# Exact source recovery

EVIDENCE_MAP.json maps409 original-path aliases to317 compressed content-addressed objects, including the entire405-file accepted assembly and four immediate root/parent records. Gzip uses mtime0. Decompression recovers exact bytes identified by SHA256; absolute origin paths are historical aliases and are never opened by the canonical identity tool.

The accepted assembly supplies its source-owned one-hop receipt closure, exact read/exposure history and prior failures. PUBLICATION_EDITS.json provides all literal wrapper pieces and byte/line boundaries. The only diff convention is full UTF-8 unified_diff, splitlines(keepends=True), n=3, exact per-record filenames; compressed copies have separate stored and decompressed hashes. All five core byte sequences remain exact and in their accepted order.

The new archive can be independently reconstructed without the author's workspace. Live scientific imports are only the four canonical parent paths in PARENT_BINDINGS.json. The published pair map is historical provenance, not an extra direct mathematical edge. Root owns recovery after any partial integration failure; the driver never restores or retries automatically.
