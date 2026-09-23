# Review-loop efficiency proposal v1

Status: external proposal only. Independent methodology review and landing are pending.

Four existing reference files change: 47 inserted lines and one replaced line. No entry point, script, model setting, approval policy, audit boundary, once-only invariant or task scope changes. No PR was created.

The changed source files match remote main `64f53dd443cd02997394e1a8bef16e2baf9f9d39` byte for byte before this proposal. `manifest.json` binds each before/after SHA-256; `proposal.patch` uses skill-relative paths so the same change can be applied to local and repository copies. Do not apply while active receipts bind the old skill bytes.

## Frozen source and actual main

Proposed file: `references/REVIEW_UNITS.md`. The actual same-session confirmations preserve frozen base/tree, separately bind observed main, and require ancestry plus source/input disjointness before and after capture. The proposal retains that narrow exception while preserving fresh integration validation.

- [drain8174-capture-dual-binding-v2.json](/private/tmp/review-drain-20260915/drain8174-capture-dual-binding-v2.json) — SHA-256 `f1308b59571f515c97b37f54dfcc745331f3a2b40c778b1b5dd7f689ad34ba2a`
- [drain8174-adapter-review-v2.json](/private/tmp/review-drain-20260915/drain8174-adapter-review-v2.json) — SHA-256 `c789eeeee564f5118d3fdfd47706e850e9c805064099b17f4e5a1e1dfbde2444`
- [drain8176-capture-dual-binding-v2.json](/private/tmp/review-drain-20260915/drain8176-capture-dual-binding-v2.json) — SHA-256 `5b4615ff3b832f23006b2065e7064d1ceaa2951683f7096ff9815079456d5299`
- [drain8176-adapter-review-v2.json](/private/tmp/review-drain-20260915/drain8176-adapter-review-v2.json) — SHA-256 `357562e86290ee489ac250991734ec163179bea4eafdc3ffbbeaed4d22c057ec`

## Rerunnable outputs and same-run capture

Proposed file: `references/FIXES_AND_REPORTING.md`. The first IO design failed when its canonical JSON already existed. The corrected optional external destination passed 18 synthetic controls without science execution; capture v3 intercepts the raw execute_runner return before execute_and_write_cache performs later checks.

- [drain8032-early-review-v1.md](/private/tmp/review-drain-20260915/drain8032-early-review-v1.md) — SHA-256 `cf5838c5e262276956690b1a79494aa6cda99b627a5b9003649c20960291ecaa`
- [drain8032-early-review-v2.md](/private/tmp/review-drain-20260915/drain8032-early-review-v2.md) — SHA-256 `d0762f4b0cafb13091e2d4d89064eea9c93e4121797e7dc2a7f0588571404e43`
- [drain8032-io-control-receipt-v2.json](/private/tmp/review-drain-20260915/drain8032-io-control-receipt-v2.json) — SHA-256 `0366ea0ace10fe60f633f777f47ac2f67862bfdf456c8ddf41827f8b4af71c65`
- [drain8032-capture-v3.py](/private/tmp/review-drain-20260915/drain8032-capture-v3.py) — SHA-256 `df1b538f1c0c3bae759dea26e371850f9f1284f4376ddb3d6157da6577052ac6`

## Archival basename preparation

Proposed file: `references/OPERATIONS.md`. The existing repo invariant inventories all tracked docs Markdown, including history, and exempts README.md and SKILL.md. The demonstrated cheap check catches this before a source freeze; the proposal adds timing, not a new naming policy.

- [drain8174-basename-collision-check-v3.json](/private/tmp/review-drain-20260915/drain8174-basename-collision-check-v3.json) — SHA-256 `27589cbdba55d1142f40633caad5fa6ef21bbab6af96c01574dd00572f7f5824`

## Complete compact recovery packets

Proposed file: `references/REVIEW_UNITS.md`. The packet binds base/head/main identities for original paths and retains their complete delta and current-main loss findings. Compact transport can omit unrelated whole-main diff material without omitting original source, proofs, deleted content or interacting context.

- [drain8174-original/inventory.json](/private/tmp/review-drain-20260915/drain8174-original/inventory.json) — SHA-256 `247038ae72ce92f8a5b72a58f42ada6e2e752097656b7dac32056860dd434f0e`
- [drain8174-original/main-loss-guard.json](/private/tmp/review-drain-20260915/drain8174-original/main-loss-guard.json) — SHA-256 `f8849e04979296764a7e6844d12a94dd5aa4ccbb247c052ee3eddae7c78aece0`
- [drain8174-original/original.patch](/private/tmp/review-drain-20260915/drain8174-original/original.patch) — SHA-256 `9887b73aa5f1c89df2de5950c00f23cd9dbaaf2872062a9706e65f273b5ca9bd`

## Required tooling category

Proposed file: `references/UNIT_RECEIPT.md`. The actual checker rejected an omitted tooling category even though edited API source was already owned source. The existing tool list stays unchanged; one clarification avoids this category mistake and unnecessary discovery or science reruns.

- [drain8032-author-cheap-v1.json](/private/tmp/review-drain-20260915/drain8032-author-cheap-v1.json) — SHA-256 `30979b36068cccc08eb01ba7fcef963a12a989a9f22c7145a5a8bb8bff75bcc3`
- [drain8032-receipt-tooling-fix-v2.json](/private/tmp/review-drain-20260915/drain8032-receipt-tooling-fix-v2.json) — SHA-256 `35f49131f0d7aac299ab25ae5ac8360bb9a1971b06b5e8fe1d3c940236b14164`

## Validation

Forward and reverse `git apply --check` succeeded. The unchanged skill entry point passes `quick_validate.py`. Changed Markdown has valid UTF-8, balanced fences, final newlines, no trailing whitespace, and unchanged link targets. All 15 live skill files still match the parity receipt. Detailed results are in `validation.json`. No scientific execution or independent self-PASS was performed.

Existing inventory reuse, discovery memoization, model choice and combined-gate rules already cover the broader efficiency lessons; they are not duplicated here. The single-PR model comparison does not justify changing Astra low.
