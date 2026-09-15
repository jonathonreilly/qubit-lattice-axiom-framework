# Independent review-loop efficiency recommendations

Read-only recommendations; no skill/source changes or scientific verdict. Reviewed installed SKILL.md coherent-unit/overlap/mechanical reuse/receipt sections (lines220–348), scope discovery (900–935), evidence preflight (1460–1500). Existing canonical-unit records, immutable mechanical reuse, safe cleanup, same-tree combined-gate reuse, early dependency checks and priority final confirmation already cover those principles; do not add duplicate prose.

## 1. A versioned execution-receipt data contract and example

**Observed friction:** each final confirmation has to rediscover author JSON shapes, field names, output locations, and whether hashes describe preexecution source or postexecution output. This session repeatedly wrote one-off adapters for preexecution/final-execution/final-freeze files. The canonical-record instruction specifies content but no interoperable shape.

**Proposed addition:** “Store execution evidence using one versioned receipt schema. Required fields: schema_version; unit_id; original_heads; base_commit; source_tree_before_execution; cwd; argv (array); relevant environment and runtime identity; started_at; elapsed_seconds; timeout_seconds; status (success/failure/timeout/interrupted); exit_code or termination_signal; source_inputs (path→SHA256); stdout/stderr (artifact path, SHA256, byte_count); generated_outputs (path→SHA256); final_candidate_tree; reviewer_confirmation reference. Use null for genuinely unavailable values with a reason. Preserve failed receipts. A schema-valid receipt is mechanical metadata, not authenticated execution or scientific PASS.”

Supply one small template and a validating reader with fixture tests for missing field, timeout/partial output and source-drift rejection; do not silently migrate old receipts or retroactively invent timestamps. Reviewer still authenticates source/output relationships.

**Measure:** adapter scripts and manual schema clarification messages per unit; final-receipt-to-confirmation latency. No claimed measured savings yet.

## 2. Fresh constituent identity check immediately before delta freeze

**Observed friction:** a queued child can be retargeted or change head after an inventory was frozen. The skill rejects changed heads at landing but does not prescribe the closest early fetch/check before starting an expensive review. This lane manually fresh-verified every new child.

**Proposed addition:** “Immediately before freezing a new constituent's original delta, retrieve its current PR head/base metadata, fetch that exact head into an isolated ref, and require equality with the owner/inventory frozen head. Record observed metadata and fetched object. On mismatch, preserve the inventory and resolve the changed scope before reviewing the new delta; do not silently substitute the new head. Compute actual ancestry from Git objects independently of the declared base. This early check does not replace the existing prelanding head check.”

This is a cheap placement rule, not permission to absorb new arrivals or reserve exclusions.

**Measure:** mismatches caught before science reads/runs; wasted execution time caused by stale original identity.

## 3. One cheap preexecution preflight report, using real APIs

**Observed friction:** noncanonical TOTAL footers (8117/8130/8132/8134), duplicate archive Markdown basenames (8018), dynamic helper resolver misses (8036/8049/8051), and declared-ID versus filename-ID mismatch (8122) surfaced at different stages. Existing prose already says to check early; a single report makes completion observable and reusable on exact bytes.

**Proposed implementation:** a bounded preflight command emits path/hash-bound results from actual Type extraction, extract_citations and graph claim_id_from_path for each exact linked source; both actual helper resolvers; declared input existence/readability; archive basename/link invariants; staged/worktree equality; all three diff checks; vocabulary. Record declared alias and resolved graph ID together, checking the linked file's own frontmatter rather than accepting a missing edge. Classify historical links separately. Self-contained arguments may have no mathematical repository dependencies when independently justified. Inspect footer/count/certificate text as a source check; do not execute science merely to preflight. Run once after complete findings are reconciled and before final source freeze/execution; rerun only affected checks after edits.

No mechanical preflight PASS is scientific acceptance or a substitute for the complete cold diff, authentic receipt, whole integrated base/tree pipeline, strict lint or changed-evidence gates.

**Measure:** final executions invalidated by deterministic packaging defects and preflight runtime, recorded prospectively.

## Not recommended now: gzip or automatic historical-payload substitution

Blob-verified mechanical reuse is already authorized. Gzip changes artifact access and may break links, evidence readers and basename/input conventions; an encoded hash alone does not identify decoded source content or prove full recoverability. Current session evidence does not justify introducing that format change as a low-risk efficiency fix. First measure archive storage/IO pressure. If material, propose a separate decoded-byte identity/mapping/recovery contract and test every consumer. Never reuse an old semantic review solely because a historical blob repeats.
