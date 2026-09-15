# Focused behavioral follow-up: manifest staging order

VERDICT: FINDING — material instruction-ordering omission; narrow correction required.

This is new observed evidence following the immutable initial skill PASS in `skill-review.md`; it does not rewrite that report or reopen unaffected science reviews. Independent Astra-low reviewer `/root/skill_review`; read-only source inspection, report-only write. No implementation, commit, push, pipeline rerun, or GitHub action.

## Finding F1 (P2): prepare the indexed topology acknowledgment before the combined pipeline

At main `5deabeb698a27c2c3f68c5df685af2521ef15307`, `docs/ai_methodology/skills/review-loop/SKILL.md:522–537` directs the combined full pipeline first and manifest regeneration afterward. Its proactive rule at lines 566–584 requires the refreshed manifest in the landing set and regeneration before every push, but does not explicitly place generation/inspection/staging before the combined pipeline. That ordering is operationally significant for source-only units and for independent manifests whose textual integration does not represent their union.

Evidence:

- `docs/audit/scripts/run_pipeline.sh:97–101` builds the graph then writes the manifest at stage 1b.
- `docs/audit/scripts/write_citation_graph_manifest.py:43–49` writes working-copy bytes; it never stages them.
- `docs/audit/scripts/repo_invariants_check.py:782–811` compares computed topology to the manifest read with `git show :docs/audit/data/citation_graph_manifest.json`, i.e. the index.
- `/private/tmp/review-drain-20260915/train01-pipeline.log:17` records stage 1b; lines 194–195 show stage 18 failed solely with two unacknowledged added nodes and `graph_delta=delta-unacknowledged`, alongside zero link/class-F violations. The train's manifest status was ` M` (working copy changed; index unchanged). Observed candidate HEAD was `4635cb32e9`, following `d99cd3d5ff` on reviewed main.

Thus completing the literal displayed combined-gate sequence cannot acknowledge fresh topology before its own stage-18 check. The prose requires a manifest eventually, but is insufficiently explicit about this necessary earlier step. The failure wastes a full validation and invokes the mandatory failed-train fallback. It supplies no adverse scientific verdict on either constituent.

## Minimal correction proposed

Immediately before the combined-validation example, add an explicit integration-preparation step: after source/disposition/interaction checks, build the citation graph and generate its manifest from the exact integrated candidate, inspect that every topology delta is intended, and stage **only** `docs/audit/data/citation_graph_manifest.json`. State that pipeline stage 1b writes working-copy bytes but stage 18 checks the index, so preparation must precede the full pipeline. Use the existing commands:

```bash
python3 docs/audit/scripts/run_citation_graph_build.py
python3 docs/audit/scripts/write_citation_graph_manifest.py
# Inspect intended topology against reviewed source before acknowledgment.
git add docs/audit/data/citation_graph_manifest.json
```

Keep these commands fail-closed when incorporated into an executable example. Preserve the single full pipeline/lint/evidence pass. Graph preparation is not a second full pipeline or a scientific confirmation. After generated-output cleanup, retain the intended manifest, commit/finalize its generated-only acknowledgment into the exact integration commit sequence, and bind the final landing tree/receipt; the push-loop replay must reconstruct the validated tree and its entry still requires no tracked residue. Do not drop the acknowledgment during generated cleanup or leave a staging-only manifest outside the final commit inventory.

Add a short ordering reminder to PREFLIGHT validation placement or graph-topology guidance, since PREFLIGHT item 6 currently describes acknowledging a delta during the shared pass and could invite the same late correction. Test the instruction ordering with a focused contract mutation after implementation, rather than rerunning unaffected source reviews or weakening the graph invariant. No change to source acceptance, reviewer identity, full-gate failure handling, or audit authority is proposed.

## Current run disposition

The coordinator's stated no-push, preserve-log, dissolve-and-single-unit fallback follows the current skill. This report grants no retrospective success receipt and does not waive that failure disposition. Each fallback candidate needs the pre-pipeline indexed acknowledgment and its own valid combined gate; prior successful science confirmations remain subject to their unchanged-source/input/interaction provenance rules.
