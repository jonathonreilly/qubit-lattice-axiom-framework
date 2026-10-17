# Exact coverage and evidence limits

This is an exposed same-model review of the emitted-word fixture, following the already completed sparse-proof review. Neither source blindness nor complete independent simulation is claimed.

## Read coverage

Complete new fixture review, scientific source, original launcher, source manifest, exposure/checkpoint, launch context, execution receipt, stdout/stderr, RESULT.json, segments and seal source were read. The source/launcher bytes equal the actual source/launcher-at-launch captures. A combined output initially truncated part of the metadata; affected files and full execution streams were subsequently read untruncated. The initial output-directory existence probe returned nonexistent, as expected for a new packet; it was not a failed science launch.

The previously reviewed sparse derivation and local-control source are unchanged at their declared identities. Relevant proofs and primary Bai–Marvian coverage from the preceding reviews are reused. The primary paper was not newly read or downloaded. The author's copied parent sources were verified against both their recorded identities and their current original files. The prior exposed sparse REVIEW.md and FREEZE.json were checked and copied as exposure/identity records; their whole prior closure is not copied here or newly revalidated.

Every one of the fixture's 22 freeze members and its seal was captured exactly in `fixture_source/`. `SOURCE_MANIFEST.json` records each original, capture, byte count and SHA256. This includes all complete gate lists and all saved matrices, not selected excerpts. Full JSON records were processed by the independent inspector; the model did not manually read several megabytes of individual gate records. Every saved matrix was loaded with pickle disabled, checked for expected shape/type/finite values, and subjected to the specifically listed artifact checks. These are distinct coverage mechanisms, not claims that every matrix entry was visually inspected.

## Actual independent artifact inspection

The named risk was divergence between saved emitted routes/counts/targets and their reported interpretation. `inspect_artifacts.py` was written independently for this review, imports no fixture source and performs no gate emission or propagation. It checks all route groups through exact integer wire permutations, inverse return order, adjacency, operand order, preserved onsite values, full counts, distance histograms, segment coverage and exact determinant-segment deletion. It rebuilds the declared target from fixed basis indices and V, checks saved arrays, and recomputes their numerical residuals.

This execution therefore contains exact structural verification and floating saved-data reanalysis. It is not merely metadata, but it is not independent execution of the circuit, a new physical simulation, or an interval certificate. `ARTIFACT_INSPECTION.json` and its complete stdout give the actual outcomes. Its source SHA256 is `676aa072d4053421f910370f368ff88d5d6b38c96e894d46e2058f7ff32a5422`; launcher SHA256 is `09c9c70e174fa2b4185ac4ffda28291bd787bfae31ddadfaffb1d7ae86c64fde`. Actual source/launcher captures, argv/cwd, environment, timeout, timestamps, exit zero and full streams are retained under `runs/artifact_inspection/`. Stdout SHA256 is `82a674252dcb9f2120bca87e64f37034046175ede01a33e878402403b6db8c77`; stderr is empty. Both streams were read completely. No attempt was hidden or replaced.

## Author execution and negative control

The actual author source-at-launch SHA256 is `e7dc44e6493fb9d847390161e109d3fe58d5124fb1ce8e308eeec4dfd93bb7c8`; launcher is `fd9229b989b33e4a3959dc42fcbadcc016b82dc0ef56cccd6436b672cf03deb5`; receipt is `fb0fa13bec56ba4560fd7bd3a59671a0a0e4cc3f293cd3f4834f7b9d6895f145`. Its actual stdout is `4e279574f87ea9dfabf4f98de5db201801892f93f6f1258fcbc098f7277a9ba9`; stderr is empty. Exact source, launcher and stream hash bindings were checked. Original argv lacks `-B` and is preserved. There is one recorded successful launch in this fixture. The deliberate determinant-omission mutant is retained completely and is a negative control, not a launch failure.

The earlier sparse parent had a preserved preexec launcher failure and successful retry. That history remains in the unchanged parent and prior review; this packet neither removes it nor presents it as an execution of the new fixture.

## Analytical checking and untested claims

Independent calculations cover the three complete prefix blocks, target determinant, Givens order, phase-pair orientation, chronological product convention, XYX signs, controlled-word count, full spectator cancellation, exact SWAP route interpretation, nominal/mutant counts, exact 24/13 mutant prediction, positive-pulse scalar identities and actual-time endpoint ordering. The complete tensor-action routine was inspected analytically; its circuit propagation was not replayed.

The numerical tolerances are observational. No rigorous roundoff certificate, efficient general compiler, finite-grid search implementation, q>1 block test, greater-than-two logical routing test, preparation cost, actual waveform integration, calibration validation, native clock/driver closure, laboratory energy identification or indefinite reservoir reuse is established. Existing source/theorem qualifications remain in force. Root owns acceptance; editable prompt files changed: none.
