# Product-seed emitter execution evidence

Root accepted the source portability changes. The first canonical attempt emitted the complete result JSON but the runner-cache filesystem-generation guard rejected the run because creating the missing output slot changed its ancestor outputs directory. Source/input content hashes were unchanged. The complete outer failure and emitted JSON are preserved; the removed merged child log is unavailable, so this attempt has no successful canonical cache or reconstructed execution receipt.

The corrected launcher creates missing output slots before identity capture.
The [second execution](evidence/canonical_02/EXECUTION.json) completed in
14.675397 seconds under one shared CPU120/wall120 envelope. Its real
[prelaunch record](evidence/canonical_02/PRELAUNCH.json) binds the primary and
168 declared inputs. Their content and filesystem generations stayed stable,
and the canonical cache is fresh. The merged stdout/stderr stream is preserved;
the empty protocol stderr file is not a separately observed child stderr.
All six scientific payloads match the qualified historical reports after the
explicit execution-metadata transformations, as recorded in
[REPORT_COMPARISON.json](REPORT_COMPARISON.json).

All twelve planned copied-source mutations reached the intended scientific
assertion on their sole attempts, totaling 29.179188 seconds of child wall time
under CPU60/wall60 per case. The [root mutation review](ROOT_MUTATION_REVIEW.json)
and [complete evidence map](evidence/MUTATION_EVIDENCE_MAP.json) distinguish
these fault-sensitivity checks from independent theorem evidence. No failed
checksum, import, path or harness check was counted as a scientific rejection.
The generic resolver's canonical wall-enforcement string is preserved in the
mutation output; the actual mutation launcher enforced subprocess timeout60.

The initial cache rejection, missing first merged stream, and old preparation
records remain explicit. SOURCE_MANIFEST.json, PORTABILITY_FREEZE.json,
PORTABILITY_REVIEW.md and PRE_RUN_PLAN.md record the earlier preparation stage.
The final note/map/manifest transition is bound by
[ROOT_WRAPPER_FINALIZATION.json](ROOT_WRAPPER_FINALIZATION.json), and the old
PUBLISH_CHECKS is preserved in
[evidence/prepared_PUBLISH_CHECKS.json](evidence/prepared_PUBLISH_CHECKS.json).
Current focused checks are in [PUBLISH_CHECKS.json](PUBLISH_CHECKS.json).
Six exact unified diffs and one historical stdout are stored as lossless gzip
files to preserve whitespace in the evidence. The
[portability archive map](evidence/PORTABILITY_ARCHIVE_MAP.json) resolves the
original raw-path identities retained in historical records. No scientific
input changed during this packaging step.

The graph adds exactly one theorem node and one edge to parent PR9661.
Source qualifications remain conditional and separate from reproducibility,
publication and retained audit. Full pipeline, strict lint and changed-evidence
checks on the actual integrated current-main delta remain later shared landing
gates. No science merge, main push, audit verdict, editable prompt change or
new physical implementation claim is authorized by this packet.
