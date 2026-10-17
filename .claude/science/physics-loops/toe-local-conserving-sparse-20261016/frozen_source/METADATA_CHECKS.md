# Actual metadata checks

Two metadata-only invocations used the captured validator source. The controlling manifest, provenance, body map, evidence map and capture map were saved before launch. No source theorem, circuit propagation, matrix reanalysis or physical simulation was executed.

- `strict_default`: actual exit `2`, declared expected exit `2`; complete streams in `runs/metadata_checks/strict_default.stdout.txt` and `.stderr.txt`.
- `explicit_source_only`: actual exit `0`, declared expected exit `0`; complete streams in `runs/metadata_checks/explicit_source_only.stdout.txt` and `.stderr.txt`.

Default exit 2 is the deliberate UNBOUND primary outcome, not a hidden failed launch. An unexpected exit remains recorded and prevents sealing. Before the final seal, these invocations claim exact source/receipt closure only; their `exact_final_inventory_checked` value is false. The sealer subsequently constructs the exhaustive final inventory and performs a read-only final validation. Its final result is returned to the caller without adding an unhashed post-seal file.
