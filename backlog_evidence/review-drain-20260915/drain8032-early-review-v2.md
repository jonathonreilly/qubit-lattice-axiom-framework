# PR8032 early affected-source review v2

**8032-IO1 resolved. Source accepted for staging and final cold freeze.** Actual capture clearance remains pending registry integration, final source/input/API identities and capture-wrapper confirmation.

Both emitters now leave the filesystem untouched in default and `--json` modes. An optional `AUDIT_RESULT_SIDECAR` exclusively writes only the caller’s unique absolute external destination. Existing canonical JSON can no longer break later live/auditor reproduction. Eighteen author synthetic IO cases cover repetition, unique sidecars and preserved duplicate/invalid-path failures; their exact outputs and errors were verified.

All82 source hashes match the v2 freeze. Exactly two emitters changed; every non-emitter AST node, all40/22 scientific predicates, the complete proofs, three note inputs and84-path recovery remain unchanged. Original68 independent math controls and the v1 scientific/premise conclusions remain valid without rerun.

Base remains `3dca18ddd0082dc23bb12c7ca38939b901c28736`. Root can apply the two accepted narrow helper-map proposals, freeze actual API discovery and prepare the bounded capture. Limits remain180s wall,180MiB self guard and256MiB aggregate external cap. Preserve same-run external sidecar and stdout; no duplicate JSON run, implicit retry or cap increase.

No primary/helper, simulation, gate, staging, source edit or PR action was performed by the reviewer. This is source confirmation, not landing PASS or an audit verdict.
