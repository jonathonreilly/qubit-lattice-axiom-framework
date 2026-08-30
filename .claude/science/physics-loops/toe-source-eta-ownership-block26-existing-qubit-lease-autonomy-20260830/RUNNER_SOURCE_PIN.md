# Block26 runner source pin

source_sha256: c728895b949f2e4db7adc3d810fe6d026fdb53431db354282faf52b3fbd6e72f
source_commit: 82e940b22742112f606049756f37a7debc29c42a
declared_input_count: 43
input_fingerprint_sha256: d11cbc8773aa727a21b2011b3c3d4d7792816880e22a1d80a1cfa3b551a297a7
canonical_cache: logs/runner-cache/admissibility_d4_existing_qubit_lease_autonomy_gate_2026_08_30.txt
state: content_pinned_unexecuted

The pin is deliberately outside `AUDIT_INPUT_PATHS` to avoid a
self-referential input fingerprint. The runner verifies its source SHA against
this file before emitting a terminal.
