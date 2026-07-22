# Cycle 509 A/B science-train attempt-1 failure receipt

Date: 2026-07-20
Authority: **none**
Audit: **unset**
Disposition: **implementation-invalid; no scientific verdict**

## Scope

The first authorized execution of the frozen 34-row Cycle-509 Route-A/B train
completed and sealed every row, then failed before any result, artifact index,
receipt, transcript, or final output directory was written.  This note records
only technical provenance and identity/cardinality evidence.  It contains no
science values and creates no physics, minimum-content, no-go, or axiom-pressure
claim.

## Frozen evidence

| item | exact value |
|---|---|
| repository commit at attempt | `3ca3ec03e22410b3fbd97d6cb7c96ae89219f986` |
| science runner SHA-256 | `a42a993a9eeb4c9c6b419ac7627e436eea1cf2ad219e8ef33983899201a2df65` |
| dependency-bundle SHA-256 | `1cf6e552ad9d60352bd14e0d2c316be5660bd1934f07491370b775813b308252` |
| sealed row artifacts | `34` (`0..33`; 17 Route A and 17 Route B) |
| sealed row artifact bytes | `454759` |
| ordered row-identity SHA-256 | `9dbdd66166e329aa3b3f3f36ca1926a77fb73349fa4b3c69d39fdf6b4d4591a4` |
| canonical compact-JSON inventory SHA-256 | `d3ddb1b61bfa9c366df4c2b25b7198528b847b7877062a422ea372336946a3e4` |
| sorted-text ledger SHA-256 | `45fb921425b776a6db545baecc8fc07afb92a6afb11cf3c7a97a0cd57b05ff4b` |
| exact time/traceback log SHA-256 | `ef03c150c70564f2116c805573f41b0ce90a76f9b5a3d4f779f0bcecc90047e6` |
| captured stdout SHA-256 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty) |
| final output directory | absent |
| result/index/receipt/transcript | absent |

The exact captured time and traceback stream is preserved verbatim at
[`outputs/physical_local_bond_character_ab_science_train_attempt1_failure_cycle509_2026_07_20.log`](../../../../outputs/physical_local_bond_character_ab_science_train_attempt1_failure_cycle509_2026_07_20.log).
Its committed bytes are identical to the transient capture and reproduce the
SHA-256 above.

The compact-JSON inventory digest is reproducible without reading any science
array.  Sort `row-*.npz` lexicographically; for each file record exactly
`name`, `bytes`, full-file `sha256`, filename-prefix `prefix_ok`, and the
`index`, `row_sha256`, `route`, `role`, `source_beta`, `probe_beta`, `geometry`,
and `deletion` fields decoded from `artifact_metadata_utf8.row_identity`.
Serialize the 34-entry array with
`json.dumps(inventory, sort_keys=True, separators=(",", ":"),
ensure_ascii=True).encode()` and no newline or BOM.  The preimage is exactly
13,678 bytes and hashes to `d3ddb1b6…a3e4` above.

The failed staging directory was moved without modification to the local
quarantine path `outputs/.cycle509_attempt1_failed_a42a993a`.  It is not an
accepted result packet and will not be reused by the replay.

## Failure classification

`row_identity` correctly stored the full contract geometry name
`train-canonical-3D-L25`.  The downstream deletion-baseline selector compared
that field to the construction alias `train-canonical`, found no baseline, and
raised:

```text
RuntimeError: intact middle-mass deletion baselines missing
```

The failure is therefore a host-side post-processing identity-schema defect.
It occurred after row sealing and before result packaging.  It does not
falsify either retained route and cannot support a shared-substrate
obstruction.

Pre-replay review found a second outcome-independent host defect that the
first failure had masked: the Route-B mirror comparison produced a NumPy
Boolean for its `pass` field, which the final JSON encoder would reject.  The
technical repair converts that gate explicitly to a built-in Python Boolean.
No response value was inspected or used to select either repair.

## Technical replay boundary

Any replay must retain the original frozen train authorization and additionally
require a distinct attempt-2 replay authorization plus the exact repaired
runner-integrity hash.  The repair may change only identity validation,
full-name geometry resolution, JSON-native mirror typing, authorization
separation, and outcome-free host fixtures.  Thresholds, manifests, route
physics, observables, gates, and artifact science members remain frozen.

Attempt-1 artifacts must not be reused as attempt-2 outputs.  A replay is a
technical recovery, not an independent blind replication.  The old staging
artifacts remain quarantined until a successful replay can compare nonmetadata
logical-array hashes without inspecting or tuning against science values.
