# Exact recovery and finite closure

EVIDENCE_MAP.json maps 187 original-path aliases to 134 deterministic gzip objects. The archive contains all 175 original assembly files, four immediate root/branch records, three original root source-check streams/receipt, two actual parent publication identity records and three canonical parent snapshots. Every original assembly byte is preserved, including the wrapper defect and historical correction records.

The seven selected immediate source closures have extents 32, 14, 57, 14, 29, 23 and 7. Their copied receipts and source-owned members are checked. Nested historical receipts, including parent-publication execution references, remain opaque provenance; this is not a recursive audit or complete reconstruction of all earlier runtime.

PUBLICATION_EDITS.json records three pieces, exact byte/line boundaries, the unchanged 464-line core, a normalization-only diff and complete publication/wrapper diffs. One convention is used: difflib.diff_bytes(unified_diff), three context lines, preserved LF endings, literal labels, no timestamps. Gzip uses mtime=0 and has distinct compressed/decompressed hashes. Original preseal draft bytes not supplied by the source are not assigned an invented identity.

The archive is recoverable without the author's source directories. Live scientific inputs of the proposed canonical tool are only the three pinned canonical parent paths. Root owns recovery after partial installation; the driver never cleans, restores or retries automatically.
