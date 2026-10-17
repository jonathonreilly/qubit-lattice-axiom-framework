# Portability review of the combined two-body halt runner

**No blocking adaptation defect found in the pinned scripts.** They preserve
the checked mathematical computations and assertions, route their data through
repository-local declared inputs, and write only the two new output artifacts.
This is a static portability disposition. The canonical note was absent at
inspection, as expected from the integration handoff; installing that declared
input and performing the root-owned canonical execution remain pending.

| Reviewed source | SHA256 |
|---|---|
| Portable primary | `6111c95e2add4eb92fbc3f46d49f45085c3e95dc73431a68da7dcd602c912618` |
| Directly imported helper | `ee4b71de1d1ab3f92dd1c812974a9dac1b740bea2b8fa3c442890b1854881b92` |
| prepare_code.py | `2a1b88c3d5b8feccb6aa318d7717a48c2dcacbae7c5ef8eaddfc79b958d4f9f3` |
| CODE_ADAPTATION.json | `e5ac66e653ff066a56e64f0d358cd0cc8888333a28eb42403f5d1efa398dd545` |
| Frozen author original | `06b71bb656d17289d0f1759f9dd385bf9a49e07d58e6c840f4741eca6ae1e07f` |
| Frozen reviewer original | `3f25ff5b24829d8876246c99bec01a66bc049295b424e4ed95f057800e9b5460` |

The complete builder and complete changed execution logic were read. The
[complete diff](COMPLETE_CHANGED_LOGIC.diff) includes every changed execution
section, with the long input tuple represented separately and fully preserved
in [STATIC_EVIDENCE.json](STATIC_EVIDENCE.json). The previous mathematical
review was reused within its pinned scope; no scientific argument was reopened.

The author calculation from exact coefficient loading through report creation
is byte-identical, apart from the separately inspected runtime metadata.
All **60 author assertions** and **66 independent-check assertions** are
identical as ordered Python AST expressions. The helper body is exactly the
original body after the three declared transformations: use the supplied
`input_root`, record the shared limits, and return its result instead of
writing/printing it. Wrapping the body in a function does not alter the
captured numerical definitions. The two implementations have separate local
state; the primary invokes the imported helper explicitly.

The **45 literal `AUDIT_INPUT_PATHS` entries** exactly cover the note, helper,
both input manifests and every data file reachable through their frozen
records. All 41 manifest-directed file identities match the copied snapshots.
The author's six historical absolute snapshot paths are routed by unique
basenames into its local `inputs/`; their hashes are still checked. The
helper's 35 snapshot suffixes are relative, contain no parent traversal, and
resolve under its supplied root. Every direct helper `read(...)` literal is
also declared. Historical `original_path` strings are evidence metadata;
neither adapted computation follows them. Current declared-input identities
and the note's absence are recorded in the evidence.

The helper has no file-writing calls. The primary's only file writes are
`outputs/two_body_autonomous_halt_2026_10_17_point_witnesses.json` and
`outputs/two_body_autonomous_halt_2026_10_17.json`, both outside the frozen
input tree. The primary hashes itself as execution provenance and hashes all
declared inputs into the result. The unchanged historical evidence is read,
not rewritten or relabeled as a new execution.

The **120-second CPU ceiling is shared by the whole process**: the primary
sets `RLIMIT_CPU=(120,120)` before numerical imports; the helper does not
reset or add a separate allowance. The primary also requests one thread in
the numerical-library environment before importing those libraries.
`AUDIT_TIMEOUT_SEC=120` declares the intended common wall allowance. It does
not itself enforce a wall timeout: the canonical harness must do so, and its
actual receipt must establish that enforcement. This review did not execute
that harness or claim that its future wall limit has already been observed.
The helper is an imported calculation, not a standalone bounded runner.

The primary explicitly preserves the important scope distinction: the helper
rechecks physical point matrices, square-root and inverse certificates plus
interval, Schur, phase and resource calculations. Prior independent
point-state/reflection certificates are inherited by immutable identity and
are **not** recomputed by the helper. The original author point replay remains
in the primary. The helper's `author_program_imported_or_executed=False`
field describes the helper's own method, not the combined process. The
combined execution-scope field makes that distinction explicit.

The only executed program in this pass was the bounded static inspector:
exit zero in **0.14296479197219014 seconds**, under a 15 CPU-second and
30 wall-second cap. It parsed and compared source, checked paths and hashes,
and saved evidence. It did not import or execute the primary, helper, builder
or either historical scientific calculation. Complete command/output evidence
is in [INSPECTION_RECEIPT.json](INSPECTION_RECEIPT.json),
[inspection.stdout](inspection.stdout) and [inspection.stderr](inspection.stderr).
No failed inspection occurred. The old frozen review and all its original
manifest-listed files remain unchanged. All new writes are confined to this
`portability/` subdirectory; no prompt, axiom, checkpoint, audit, Git or PR
change was made.
