# PR8146 unit original source recovery

This archive preserves all 116 original path occurrences across PR8138, PR8139,
PR8141, PR8142 and PR8146. `original-manifest.json` records the original head,
path and SHA256 plus the gzip archive path and archive SHA256. Decompress with
Python `gzip.decompress` or `gzip -dc`; the decompressed bytes must match the
original SHA256. Compression uses a zero timestamp. Repeated inherited versions
remain separate per PR so the complete branch history is recoverable.

The live notes retain the constructive proofs, exact algebra and finite
witnesses with repaired hypotheses. Original broad negative certificates,
unproved parameter-wide distinctness and phase claims remain historical,
unlanded material: the live narrowing is not a passing negative certificate.
Keep the original branches as recovery handles. No audit verdict is supplied.

Original cache bytes are provenance only. They are not freshness evidence for
repaired notes/runners. New captures require independent cold source confirmation
and the cheap source/input-bound unit preflight first.
