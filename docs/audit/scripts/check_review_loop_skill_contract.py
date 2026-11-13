#!/usr/bin/env python3
"""Fail closed if review-loop loses a quality, safety, or landing invariant."""

from __future__ import annotations

import argparse
import ast
import re
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SKILL_REL = "docs/ai_methodology/skills/review-loop/SKILL.md"
# The entry point routes by operation. Validate every relocated procedure as
# part of the original contract, without forcing every runtime operation to
# load unrelated landing or salvage instructions. This order keeps each old
# section group (including executable shell recipes) intact for mutation tests.
SKILL_CONTRACT_REFERENCES = (
    "references/REVIEW_UNITS.md",
    "references/LANDING.md",
    "references/REVIEW_SETUP.md",
    "references/SCIENCE_LENSES.md",
    "references/SALVAGE.md",
    "references/FIXES_AND_REPORTING.md",
    "references/AUDIT_COMPATIBILITY.md",
    "references/COMBINED_VALIDATION.md",
)
REFERENCE_TRIGGER_RULES = {
    "references/REVIEW_SETUP.md": r"Every branch/PR review.*before review starts",
    "references/REVIEW_UNITS.md": r"Before defining, reviewing, confirming, or reusing any unit",
    "references/SCIENCE_LENSES.md": r"Every scientific, code, governance, or methodology review and affected-fix confirmation",
    "references/FIXES_AND_REPORTING.md": r"Before fixes, checks after fixes, re-review, or the final report",
    "references/AUDIT_COMPATIBILITY.md": r"Changed source notes, runners, claim tables, lane stubs, or publication/control-plane files.*scientific PASS gate",
    "references/COMBINED_VALIDATION.md": r"Whenever combined candidate validation is required.*named review-only or landing mode",
    "references/LANDING.md": r"Actual unspecified/focus-text-only invocation, a set of PRs, or any authorized landing",
    "references/SALVAGE.md": r"Before PR closure/rejection, non-landable disposition, discarded stretch/campaign packets, or salvage",
    "references/UNIT_RECEIPT.md": r"Creating a new canonical unit record, using supporting-proof relationships, or adapting an older record",
    "references/OPERATIONS.md": r"Historical payload consolidation, exclusive sequential checkout reuse, or dependent-PR head/base maintenance and recovery",
}
ROUTING_RULES = {
    "same_source": r"read the complete required reference from the same source revision",
    "cumulative_triggers": r"Triggers accumulate",
    "unread_holds_action": r"A missing or unread\s+required reference holds the dependent operation",
    "full_procedure_required": r"routing summaries are not substitutes for the detailed instructions",
}
REVIEW_ONLY_VALIDATION_RULES = (
    r"For a named review-only candidate, run the mutating validation recipe in a\s+disposable isolated copy",
    r"staged, unstaged and untracked reviewed content and all declared inputs",
    r"Verify\s+the copied source/input identities against the reviewed candidate, preserve\s+the caller's source and index",
    r"In that copy, use `--include-worktree`",
    r"Do not execute the landing commit, replay or push instructions for this mode",
    r"do not create an iteration commit under `--no-commit`",
    r"a matching `HEAD` alone is insufficient",
)
COMMAND_REL = ".claude/commands/review-loop.md"
# The landing loop is a script in the skill package. Its structure is checked
# in that file, and LANDING.md must run exactly that file.
LANDING_SCRIPT_PACKAGE_PATH = "scripts/land_train.sh"
LANDING_SCRIPT_REL = (
    "docs/ai_methodology/skills/review-loop/" + LANDING_SCRIPT_PACKAGE_PATH
)
LANDING_RUN_COMMAND = 'bash "$SKILL_DIR/scripts/land_train.sh" "$TRAIN_FILE"'
LANDING_SCRIPT_ENTRY = "land_train() {"
LANDING_SCRIPT_READS_INPUT = 'read_train_file "$@"'
LANDING_SCRIPT_CALL = 'land_train "$@"; exit'
GENERATOR_REL = "docs/audit/scripts/generate_skill_axiom_baselines.py"
PIPELINE_REL = "docs/audit/scripts/run_pipeline.sh"
PLACEMENT_REFERENCES = {
    "preflight": "docs/ai_methodology/skills/review-loop/PREFLIGHT.md",
    "conformance": "docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md",
    "workflow": "docs/ai_methodology/SCIENCE_WORKFLOW.md",
}
FENCE_OPEN_RE = re.compile(r"^ {0,3}(?P<fence>`{3,}|~{3,})(?P<info>.*)$")
REFERENCE_START_RE = re.compile(r"^ {0,3}\[[^\]\n]+\]:")
PIPELINE_CONTRACT_LINE = (
    "python3 docs/audit/scripts/check_review_loop_skill_contract.py"
)
CONTAINMENT_CONTEXT = """   if ! git fetch -q origin \\
          +refs/heads/main:refs/remotes/origin/main; then
     echo "FAILED: could not refresh origin/main for containment verification" >&2
     exit 1
   fi
   if ! git merge-base --is-ancestor "$landed" origin/main; then"""
PIPELINE_CONTRACT_CONTEXT = """echo "==> 18b/18 check_review_loop_skill_contract.py (review quality/safety guard)"
python3 docs/audit/scripts/check_review_loop_skill_contract.py

if [[ "${PIPELINE_MODE}" == "full" ]]; then"""
TRAIN_VALIDATION_CONTEXT = """   TRAIN_COMBINED_VALIDATION_SCOPE=integrated-candidate
   if ! { bash docs/audit/scripts/run_pipeline.sh \\
          && python3 docs/audit/scripts/audit_lint.py --strict \\
          && python3 docs/audit/scripts/check_changed_audit_evidence.py --base origin/main; }; then
     echo "FAILED: combined validation; preserve log and do not land" >&2
     exit 1
   fi"""
TRAIN_CLEAN_CONTEXT = """   TRAIN_COMBINED_CLEAN_SCOPE=integrated-candidate
   if ! { review_base=$(git merge-base origin/main HEAD) \\
          && git diff --check "$review_base"..HEAD \\
          && git diff --check \\
          && git diff --cached --check; }; then
     echo "FAILED: candidate diff checks; do not land" >&2
     exit 1
   fi"""
TRAIN_HEAD_FUNCTION_CONTEXT = """   verify_pr_head() {
     local pr="$1" expected="$2" live_ref actual
     case "$pr" in
       ''|*[!0-9]*) return 1 ;;
     esac
     live_ref="refs/tmp/review-loop-train-pr-$pr"
     if ! git fetch -q origin "+pull/$pr/head:$live_ref"; then
       return 1
     fi
     actual="$(git rev-parse --verify "$live_ref")" || return 1
     [ "$actual" = "$expected" ]
   }"""
# The lander moves each PR head so that GitHub marks the PR merged. Every
# guard below must run, in this order, before `main` is pushed: frozen heads,
# GitHub state, recovery refs, the leased head push, and the wait for
# refs/pull/<N>/head.
TRAIN_PRE_PUSH_HEAD_CONTEXT = """     if ! verify_frozen_pr_heads; then
       echo "FAILED: PR head moved; dissolve the train without pushing" >&2
       exit 1
     fi
     if ! verify_pr_github_state; then
       echo "FAILED: a carried PR is not open on main from its recorded branch, or an open PR is based on a carried head; nothing was pushed" >&2
       exit 1
     fi
     if ! record_recovery_refs; then
       echo "FAILED: could not record every recovery ref; no head was moved" >&2
       exit 1
     fi
     if ! move_pr_heads; then
       echo "FAILED: leased head push refused; no head was moved" >&2
       exit 1
     fi
     if ! wait_for_landed_pr_heads; then
       echo "FAILED: a PR does not show the pushed head; main was not pushed" >&2
       restore_frozen_pr_heads
       exit 1
     fi
     if git push -q origin HEAD:main; then"""
TRAIN_HEAD_MOVE_CONTEXT = """   move_pr_heads() {
     local index
     local -a leases specs
     leases=()
     specs=()
     for index in "${!PR_NUMBERS[@]}"; do
       leases+=("--force-with-lease=refs/heads/${PR_HEAD_REFS[$index]}:${PR_HEADS[$index]}")
       specs+=("${PR_LANDED[$index]}:refs/heads/${PR_HEAD_REFS[$index]}")
     done
     git push -q --atomic "${leases[@]}" origin "${specs[@]}"
   }"""
TRAIN_HEAD_RESTORE_CONTEXT = """     if ! restore_frozen_pr_heads; then
       echo "FAILED: main was not updated and a PR head could not be restored" >&2
       exit 1
     fi
     sleep 3"""
TRAIN_POST_PUSH_HEAD_CONTEXT = """     if ! verify_pr_head "$pr" "$expected"; then
       echo "LEAVE_OPEN $pr: PR head moved after landing" >&2
     elif pr_shows_merged "$pr"; then
       printf 'MERGED %s %s %s\\n' "$pr" "${PR_HEADS[$index]}" "$expected"
     else
       echo "NOT_MERGED $pr: main holds $expected but GitHub does not show the PR merged" >&2
     fi"""

REVIEWER_BODY_RULES: dict[str, str] = {
    "CodeRunnerReviewer": r"^\s+Review changed Python/scripts/log-producing code\.",
    "PhysicsClaimReviewer": (
        r"^\s+Attack theorem notes, claims tables, publication surfaces, and prose\."
    ),
    "ProofObligationReviewer": (
        r"^\s+Trigger when changed content claims a theorem, proof, derivation, "
        r"reduction,"
    ),
    "ImportSupportReviewer": (
        r"^\s+Inventory every measured, fitted, literature, PDG, cosmological,"
    ),
    "NatureRetentionReviewer": r"^\s+Apply the hostile external-review bar\.",
    "NoGoDisciplineReviewer": (
        r"^\s+Scrutinize negative claims with the same rigor as positive ones\."
    ),
    "LabelingConventionReviewer": (
        r"^\s+Detect labeling/naming/convention content masquerading as a bounded"
    ),
    "RepoGovernanceReviewer": r"^\s+Check placement and authority surfaces\.",
}
METHODOLOGY_BODY_RULE = (
    r"^Run `MethodologySkillReviewer` when files under "
    r"`docs/ai_methodology/skills/`,\s+`docs/ai_methodology/`, or "
    r"`\.claude/commands/` changed\."
)
REVIEWER_DISABLE_RE = re.compile(
    r"(?:"
    r"\b(?:do\s+not|don't|never|must\s+not|should\s+not|shall\s+not|"
    r"need\s+not|cannot|can't)\b[^\n]*"
    r"\b(?:run|invoke|use|apply|execute|perform|review|required|enable)\w*\b"
    r"|\b(?:skip|disable|omit|bypass)\w*\b"
    r"|\b(?:is|are|be|remain)\s+(?:not\s+required|optional|disabled|omitted|skipped)\b"
    r"|\bno\s+need\s+to\b"
    r")",
    re.IGNORECASE,
)


# These are structural tripwires, not a substitute for methodology review.
# Exact positive clauses protect load-bearing commands from commented-out,
# negated, or inert-token mutations while allowing ordinary prose wrapping.
SKILL_RULES: dict[str, tuple[str, ...]] = {
    "freshness": (
        r"^## Skill Freshness\s*$",
        r"^Before using this workflow, inspect its applicability and correctness and use\s+"
        r"`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK\.md` to select one consistent\s+"
        r"source revision, including references\.",
        r"a user-requested prompt review/test uses the identified candidate under review",
    ),
    "mandatory_authority_reads": (
        r"^## Premise Authority\s*$",
        r"^\*\*Mandatory authority read:\*\* before any premise, import, wall, "
        r"or dependency\s+judgment, read the current axiom memo, primitive "
        r"registry check, registry data,\s+and every relevant primitive source "
        r"listed below\.",
        r"PRIMITIVE_REGISTRY_CHECK\.md",
        r"axiom_premise_nodes\.json",
        r"premise_decision_history\.json",
    ),
    "reviewer_model_and_effort": (
        r"^Review-loop is a text/code/math review path\. For ordinary pre-landing science\s+"
        r"review, use the \*\*fast reviewer\*\* named in the owner's landing-review setting\s+"
        r"\(`docs/ai_methodology/SCIENCE_WORKFLOW\.md` section 4; owner direction\s+"
        r"2026-09-08\), from a different model family than the author when one is\s+"
        r"available\.",
        r"\.\s+Escalate a material mathematical or\s+"
        r"premise question, reviewer disagreement or failed decisive control that the\s+"
        r"unit review cannot resolve through a narrow correction to the \*\*strongest\s+"
        r"configured reviewer\*\* in that setting;",
        r"\.\s+Respect a later explicit owner choice\.",
        r"\.\s+If a requested model is unavailable, report that fact and use an available\s+"
        r"reviewer only with its actual configuration stated\. Do not silently substitute\s+"
        r"a model\.",
        r"\.\s+If no different-family reviewer is available, use a distinct\s+"
        r"restricted-input reviewer context and label it same-family/fresh-context\.",
        r"^Independence here requires separation from authorship and independent checks;\s+"
        r"model-family diversity alone does not establish it\. Never label same-family\s+"
        r"work cross-family\. If context separation cannot be established, hold the\s+"
        r"independent confirmation gate\. Keep the original reviewer for affected fixes\.",
    ),
    "reviewer_lenses": (
        r"^- `CodeRunnerReviewer`\s*$",
        r"^\s+Review changed Python/scripts/log-producing code\.",
        r"^- `PhysicsClaimReviewer`\s*$",
        r"^\s+Attack theorem notes, claims tables, publication surfaces, and prose\.",
        r"^- `ProofObligationReviewer`\s*$",
        r"^\s+Trigger when changed content claims a theorem, proof, derivation, "
        r"reduction,",
        r"^- `ImportSupportReviewer`\s*$",
        r"^\s+Inventory every measured, fitted, literature, PDG, cosmological,",
        r"^- `NatureRetentionReviewer`\s*$",
        r"^\s+Apply the hostile external-review bar\.",
        r"^- `NoGoDisciplineReviewer`\s*$",
        r"^\s+Scrutinize negative claims with the same rigor as positive ones\.",
        r"^- `LabelingConventionReviewer`\s*$",
        r"^\s+Detect labeling/naming/convention content masquerading as a bounded",
        r"^- `RepoGovernanceReviewer`\s*$",
        r"^\s+Check placement and authority surfaces\.",
        r"^Run `MethodologySkillReviewer` when files under "
        r"`docs/ai_methodology/skills/`,\s+`docs/ai_methodology/`, or "
        r"`\.claude/commands/` changed\.",
    ),
    "independent_math_and_mutations": (
        r"independent route",
        r"mutation tests?",
        r"self-confirming tests",
    ),
    "proof_import_governance": (
        r"proof-search-governance\.md",
        r"Inventory every measured, fitted, literature",
        r"RepoGovernanceReviewer",
        r"EQUIVALENT-GAP",
    ),
    "no_go_discipline": (
        r"N1-N8",
        r"NoGoDisciplineReviewer.*blocks PASS|FAIL.*NoGoDisciplineReviewer blocks PASS",
        r"obstruction questions",
        r"missing or short packet is never a",
    ),
    "audit_compatibility_boundary": (
        r"## Audit-System Compatibility Gate",
        r"must not run `docs/audit/scripts/apply_audit\.py`",
        r"must not.*apply audit verdicts",
    ),
    "same_session_confirmation": (
        r"same reviewer thread/session",
        r"do not launch a\s+new reviewer process",
        r"FINAL VERDICT: PASS",
        r"fail closed and do not land",
    ),
    "landing_train_scheduler": (
        r"Land confirmed units in continuously collected trains of at most eight",
        r"depart with the useful ready batch as soon as the coordinator is available",
        r"do not wait for an arbitrary collection deadline or an unfinished reviewer",
        r"open the next empty\s+collecting train immediately",
        r"one-component trains",
    ),
    "landing_train_combined_gate": (
        r"combined gate is mechanical",
        r"check_changed_audit_evidence\.py --base origin/main",
        r'git diff --check "\$review_base"\.\.HEAD',
        r"git diff --cached --check",
        r"^\s*VALIDATED_BASE=<origin-main-sha-used-by-the-combined-gate>$",
        r"^\s*VALIDATED_TREE=<combined-candidate-tree-sha>$",
    ),
    "landing_train_head_guard": (
        r"^\s*PR_NUMBERS=<pr-a-number> <pr-b-number> \.\.\.$",
        r"^\s*PR_HEADS=<pr-a-frozen-head-sha> <pr-b-frozen-head-sha> \.\.\.$",
        r"^\s*PR_HEAD_REFS=<pr-a-head-branch> <pr-b-head-branch> \.\.\.$",
        r"^\s*PR_TIPS=<pr-a-newest> <pr-b-newest> \.\.\.$",
        r"refs/review-loop/recovery/pr-",
        r"post-push head check",
        r"force-with-lease=refs/heads/<head>:<frozen-head-sha>",
    ),
    "landing_script_entry": (
        r"The train's fail-closed landing loop is the script\s+"
        r"\[`scripts/land_train\.sh`\]\(\.\./scripts/land_train\.sh\)\.",
        r"Never paste or edit a copy of\s+it\.",
        r"^\s*COMMITS=<pr-a-oldest> \.\.\. <pr-a-newest> <pr-b-oldest> \.\.\.$",
        r"The script parses the train file and never executes it\.",
    ),
    "landed_pr_shows_merged": (
        r"A landed PR shows as merged \(owner decision 2026-11-10\)\. Review-loop never\s+"
        r"closes a landed PR and never merges one through GitHub's button or API",
        r"Close a PR only when nothing from it reaches `main`",
        r"The lander\s+merges nothing through GitHub and closes no landed PR\.",
        r"A `NOT_MERGED` line means the mechanism failed for\s+that PR",
        r"do not close it by hand, and report it to the owner",
    ),
    "dependent_pr_base_preservation": (
        r"So protect dependents before the landing push, not\s+after it\.",
        r"list open PRs that\s+use it as their base, including drafts",
        r"Freeze each dependent PR's number, head SHA, original base and original delta",
        r"retarget those dependent PR bases to `main` without changing their heads",
        r"re-list open PRs targeting the old base immediately before the\s+landing push",
        r"preserve the parent branch for recovery",
        r"After the push, verify the expected dependent PRs remain open",
        r"restore the exact deleted parent ref with an absent-ref lease",
    ),
    "live_surface_routing": (
        r"docs/KEY_SCIENCE\.md",
        r"relevant sharded rows under `docs/audit/data/ledger/`",
        r"archive/publication/ci3_z3/` is record-only",
        r"docs/repo/FRONT_DOOR_STATUS\.md",
        r"docs/repo/RETAINED_BACKBONE\.md",
    ),
    "pipeline_strict_and_evidence": (
        r"run_pipeline\.sh",
        r"audit_lint\.py --strict",
        r"check_changed_audit_evidence\.py",
    ),
    "manifest_landing": (
        r"acknowledged by the nightly\s+refresh",
        r"before EVERY push attempt",
        r"write_citation_graph_manifest\.py",
        r"citation_graph_manifest\.json",
    ),
    "disk_and_worktree_guards": (
        r"5242880",
        r"mktemp -d",
        r"trap cleanup_review_wt EXIT",
        r"retained worktree for recovery",
        r"from science_fix_loop import cleanup_worktree",
    ),
}

# The loop's own clauses. They must be active shell text of the landing
# script: a comment, a multiline string or a heredoc that only mentions one
# does not count. A family that also has prose clauses keeps them above.
LANDING_SCRIPT_RULES: dict[str, tuple[str, ...]] = {
    "landing_train_combined_gate": (
        r'VALIDATED_BASE\) VALIDATED_BASE="\$\{entries\[0\]\}" ;;',
        r'VALIDATED_TREE\) VALIDATED_TREE="\$\{entries\[0\]\}" ;;',
        r'if \[ "\$\(git rev-parse origin/main\)" != "\$VALIDATED_BASE" \]; then',
        r'if \[ "\$\(git rev-parse \'HEAD\^\{tree\}\'\)" '
        r'!= "\$VALIDATED_TREE" \]; then',
    ),
    "landing_train_head_guard": (
        r"PR_NUMBERS=\(",
        r"PR_HEADS=\(",
        r"PR_HEAD_REFS=\(",
        r"PR_TIPS=\(",
        r"verify_frozen_pr_heads\(\)",
        r"verify_pr_github_state\(\)",
        r"record_recovery_refs\(\)",
        r"refs/review-loop/recovery/pr-",
        r"move_pr_heads\(\)",
        r"restore_frozen_pr_heads\(\)",
        r"PR head moved; dissolve the train without pushing",
    ),
    "landing_script_entry": (
        r"COMMITS=\(",
        r"^read_train_file\(\) \{$",
    ),
    "manifest_landing": (
        r"run_citation_graph_build\.py",
        r"write_citation_graph_manifest\.py",
        r"citation_graph_manifest\.json",
    ),
    "manifest_sequencer_progress": (
        r'while \[ -z "\$cherry_pick_complete" \]; do',
        r'if ! conflicts="\$\(git diff --name-only --diff-filter=U\)"; then',
        r'if ! conflicted_commit="\$\(git rev-parse --verify CHERRY_PICK_HEAD\)"; then',
        r'if \[ "\$conflicted_commit" = "\$last_conflicted_commit" \]; then',
        r"FAILED: manifest repair made no sequencer progress",
        r"FAILED: source conflict or sequencer failure",
        r"FAILED: manifest generation or staging during cherry-pick",
    ),
    "fail_closed_landing": (
        r"for attempt in 1 2 3 4",
        r"landed=",
        r"refs/heads/main:refs/remotes/origin/main",
        r'^\s*if ! git merge-base --is-ancestor "\$landed" origin/main; then\s*$',
        r"landing did not complete after 4 attempts",
    ),
}

# These clauses are prose obligations, not an automated scheduler or a proof
# that a real unit's dispositions/receipts are complete. Keep positive clauses
# visible and anchored; adversarial methodology review still checks behavior.
UNIT_PROSE_RULES: dict[str, tuple[str, ...]] = {
    # Two read depths. These clauses keep the full read as the default, keep
    # the depth out of anyone's hands, and keep a scope read from being taken
    # for a check. `review_depth_paths` binds the path table to the script.
    "review_depth": (
        r"^`scripts/review_depth\.py` reads the depth from the unit's delta: a scope read\s+"
        r"when the unit only adds working material, and the full read for every other\s+"
        r"change\. The depth may be raised with a recorded reason and is never lowered\.",
        r"^## Review depth\s*$",
        r"^It prints `DEPTH scope` only when every changed path is working material:",
        r"^Every other change gets the full read and prints `DEPTH full`\.",
        r"^One such path gives the whole unit the full read\. If the script prints no\s+"
        r"`DEPTH` line, the unit gets the full read\.",
        r"^The reviewer or the lander may raise a unit to the full read and records the\s+"
        r"reason\. Nobody lowers a depth\.",
        r"^Where a lens, a gate or another passage of this skill asks for more than this\s+"
        r"list, it describes the full read\.",
        r"^A scope read files no check record and moves no standing\.",
    ),
    "versioned_mechanical_receipt": (
        r"For new units, use the versioned schema in \[`references/UNIT_RECEIPT\.md`\]\(UNIT_RECEIPT\.md\) and\s+"
        r"\[`scripts/review_receipt\.py`\]\(\.\./scripts/review_receipt\.py\) for shared preflight against actual repository APIs\.",
        r"never infer a scientific verdict or restamp an old execution",
        r"Mechanical success\s+does not establish proof closure, reviewer authenticity or landing PASS",
    ),
    "exact_history_and_exclusive_reuse": (
        r"exact archive\s+mapping and externally pinned manifest checks in \[`references/OPERATIONS\.md`\]\(OPERATIONS\.md\)",
        r"Keep all active proof/runtime/link targets accessible, preserve every original\s+path/mode/disposition",
        r"guarded release preserves the exact HEAD,\s+rejects tracked/untracked/ignored residue and unfinished Git operations, and\s+retains ownership on failure",
        r"never concurrently share a slot or force cleanup",
    ),
    "coherent_unit_coverage": (
        r"^A review unit is one frozen, reviewable source argument\. It may be one PR or\s+"
        r"several cumulative/dependent PRs",
        r"^For every constituent, freeze its PR number, original head SHA, declared base,",
        r"Record every source path and claim\s+in a complete disposition map: accepted unchanged, narrowed, superseded,\s+rejected, or deferred",
        r"Unmapped content\s+blocks unit confirmation\.",
        r"^Run every applicable reviewer lens on the complete final unit and its\s+interactions\.",
    ),
    "unit_provenance_and_recheck": (
        r"^Freeze the disposition map hash, source/dependency/input blob hashes, original",
        r"A changed PR head fails the provenance\s+gate even if source bytes look identical\.",
        r"A changed premise, input, source byte,\s+or semantic interaction reopens the affected conclusion",
        r"Both require renewed frozen provenance and same-session confirmation\.",
        r"^The lander's own push in the \[landing loop\]\(LANDING\.md\) is not a changed head in\s+this sense\.",
        r"under an exact lease on that frozen SHA",
        r"only after\s+the frozen head is recorded under a recovery ref",
        r"Any other movement of a head,\s+before or after that push, still fails the gate\.",
    ),
    "shared_validation_placement": (
        r"^Perform focused source, runner, premise, vocabulary, and all three diff checks\s+per unit before freezing it\.",
        r"^The full pipeline, strict lint, and changed-evidence gates run once on the exact\s+integrated current-main candidate, covering all units\.",
        r"They are not required\s+again on each constituent or unit before enrollment\.",
        r"^Reuse successful validation only for an identical frozen base and candidate\s+tree, command/options, tool/runtime versions, declared inputs, and evidence\s+scope, with accessible successful logs and their hashes\.",
        r"already validated unit whose raw tree equals the whole integrated candidate",
        r"A missing receipt, failed\s+command, changed base/tree/input, or changed validation scope invalidates reuse\.",
        r"verify all non-generated bytes stayed identical\.",
    ),
    "unit_scope_and_close": (
        r"^Exclude drafts by default\. Explicit owner-directed draft triage may review a",
        r"mark-ready is not PASS, and a still-draft PR cannot land\.",
        r"Exclude owner-reserved\s+PRs from units and their inherited content unless that reservation is explicitly\s+lifted\.",
        r"^   After the loop, verify each constituent's accepted/narrowed/superseding\s+source and evidence on current `origin/main` against the disposition map;",
        r"never delete the recovery ref of such a PR\.",
        r"review-loop must\s+not invoke an auditor or apply a scientific verdict/status\.",
    ),
}

# Bind each family to the source an agent actually loads for that operation.
# Pooled validation alone could find displaced science obligations in a landing
# file that a named review never reads. Multi-file families retain explicit
# shared boundaries (entry authority, unit scope, or the common gate).
SKILL_RULE_LOCATIONS = {
    "freshness": ("SKILL.md",),
    "mandatory_authority_reads": ("SKILL.md",),
    "reviewer_model_and_effort": ("SKILL.md",),
    "reviewer_lenses": ("references/SCIENCE_LENSES.md",),
    "independent_math_and_mutations": ("references/SCIENCE_LENSES.md",),
    "proof_import_governance": ("references/SCIENCE_LENSES.md",),
    "no_go_discipline": ("references/AUDIT_COMPATIBILITY.md",),
    "audit_compatibility_boundary": ("SKILL.md", "references/AUDIT_COMPATIBILITY.md"),
    "same_session_confirmation": ("references/LANDING.md",),
    "landing_train_scheduler": ("references/LANDING.md",),
    "landing_train_combined_gate": ("references/LANDING.md", "references/COMBINED_VALIDATION.md"),
    "landing_train_head_guard": ("SKILL.md", "references/LANDING.md"),
    "landing_script_entry": ("references/LANDING.md",),
    "landed_pr_shows_merged": ("SKILL.md", "references/LANDING.md"),
    "dependent_pr_base_preservation": ("SKILL.md",),
    "live_surface_routing": ("references/REVIEW_SETUP.md", "references/SCIENCE_LENSES.md", "references/AUDIT_COMPATIBILITY.md"),
    "pipeline_strict_and_evidence": ("references/COMBINED_VALIDATION.md",),
    "manifest_landing": ("references/LANDING.md",),
    "disk_and_worktree_guards": ("references/LANDING.md",),
}
UNIT_RULE_LOCATIONS = {
    "review_depth": ("SKILL.md", "references/SCIENCE_LENSES.md"),
    "versioned_mechanical_receipt": ("references/REVIEW_UNITS.md",),
    "exact_history_and_exclusive_reuse": ("references/REVIEW_UNITS.md", "references/LANDING.md"),
    "coherent_unit_coverage": ("references/REVIEW_UNITS.md",),
    "unit_provenance_and_recheck": ("references/REVIEW_UNITS.md",),
    "shared_validation_placement": ("references/REVIEW_UNITS.md",),
    "unit_scope_and_close": ("references/REVIEW_UNITS.md", "references/LANDING.md"),
}

GENERATOR_RULES: dict[str, tuple[str, ...]] = {
    "generated_authority_router": (
        r"SPAN_AUTHORITY_ROUTER",
        r'key="review-loop"[\s\S]{0,220}spans=\(SPAN_AUTHORITY_ROUTER,\)',
        r"missing_authority_router_coverage",
    ),
}

PIPELINE_RULES: dict[str, tuple[str, ...]] = {
    "pipeline_contract_registration": (
        rf"^{re.escape(PIPELINE_CONTRACT_LINE)}$",
    ),
}

COMMAND_RULES: dict[str, tuple[str, ...]] = {
    "command_landing_train": (
        r"continuously collected trains of at most eight",
        r"double-buffered landing train",
        r"next empty train\s+opens as soon as the old membership freezes",
        r"verifies every frozen PR head\s+immediately before push",
        r"records each frozen head under a recovery ref",
        r"force-with-lease=<ref>:<frozen-head-sha>",
        r"rechecks each landed head after the push",
        r"the loop closes no landed PR",
        r"The landing loop is the skill's `scripts/land_train\.sh`: run that file",
        r"never paste or edit a\s+copy of it",
    ),
    "command_dependent_base_preservation": (
        r"inventory open PRs using this branch as their base",
        r"drafts and out-of-unit dependents",
        r"retarget dependent bases to `main`",
        r"preserve the parent branch if any remain or a head changed",
        r"Verify dependent PRs remain open after deletion",
    ),
    "command_unit_validation": (
        r"complete constituent\s+claim/content disposition map",
        r"perform one full `docs/audit/scripts/run_pipeline\.sh`",
        r"do not require duplicate per-PR or per-unit full runs",
        r"no fixed\s+collection wait",
        r"Mark-ready is not PASS and still-draft PRs cannot\s+land",
    ),
    "command_review_depth": (
        r"Take the depth of the read from the skill's `scripts/review_depth\.py`: a\s+"
        r"scope read when the unit only adds working material, the full read for\s+"
        r"every other change\.",
        r"Raise a depth with a recorded reason; never lower one\.",
    ),
}


@dataclass(frozen=True)
class MarkdownScan:
    """Visible Markdown prose plus fenced command blocks and syntax defects."""

    visible: str
    prose: str
    fenced_blocks: tuple[tuple[str, str], ...]
    errors: tuple[str, ...]


def _strip_html_from_line(line: str, in_comment: bool) -> tuple[str, bool]:
    """Remove HTML comments from one non-fenced line, preserving visible text."""
    visible: list[str] = []
    rest = line
    while True:
        if in_comment:
            end = rest.find("-->")
            if end < 0:
                return "".join(visible), True
            rest = rest[end + 3 :]
            in_comment = False
        start = rest.find("<!--")
        if start < 0:
            visible.append(rest)
            return "".join(visible), False
        visible.append(rest[:start])
        rest = rest[start + 4 :]
        in_comment = True


def _markdown_scan(text: str) -> MarkdownScan:
    """Parse the CommonMark constructs that can make contract prose non-rendered.

    This intentionally is not a Markdown renderer. It recognizes the block forms
    that can hide requirements in this skill: HTML comments, fenced code blocks,
    and link-reference definitions (including multiline titles). Unterminated
    forms are syntax defects and make the contract fail closed.
    """
    visible_lines: list[str] = []
    prose_lines: list[str] = []
    fenced_blocks: list[tuple[str, str]] = []
    errors: list[str] = []
    fence_marker: str | None = None
    fence_width = 0
    fence_info = ""
    fence_body: list[str] = []
    in_comment = False
    in_reference_definition = False

    for raw in text.splitlines():
        if fence_marker is not None:
            indent = len(raw) - len(raw.lstrip(" "))
            candidate = raw[indent:] if indent <= 3 else ""
            run = len(candidate) - len(candidate.lstrip(fence_marker))
            if run >= fence_width and not candidate[run:].strip():
                fenced_blocks.append((fence_info, "\n".join(fence_body)))
                fence_marker = None
                fence_width = 0
                fence_info = ""
                fence_body = []
                visible_lines.append("")
                prose_lines.append("")
            else:
                fence_body.append(raw)
                visible_lines.append(raw)
                prose_lines.append("")
            continue

        line, in_comment = _strip_html_from_line(raw, in_comment)
        if in_comment:
            visible_lines.append(line)
            prose_lines.append(line)
            continue

        if in_reference_definition:
            visible_lines.append("")
            prose_lines.append("")
            if not line.strip():
                in_reference_definition = False
            continue

        fence = FENCE_OPEN_RE.match(line)
        if fence:
            token = fence.group("fence")
            info = fence.group("info")
            if token[0] != "`" or "`" not in info:
                fence_marker = token[0]
                fence_width = len(token)
                fence_info = info.strip().lower()
                visible_lines.append("")
                prose_lines.append("")
                continue

        # Four-space/tab indentation is a CommonMark code block. Keep its text
        # available to command-oriented tripwires, but never treat it as prose.
        if line.startswith("    ") or line.startswith("\t"):
            visible_lines.append(line)
            prose_lines.append("")
            continue

        if REFERENCE_START_RE.match(line):
            # A CommonMark definition may put its destination and multiline
            # title on following lines. Definitions are absent from the live
            # skill, so conservatively blank the whole block through its first
            # blank line rather than risk treating hidden title text as policy.
            in_reference_definition = True
            visible_lines.append("")
            prose_lines.append("")
            continue

        visible_lines.append(line)
        prose_lines.append(line)

    if fence_marker is not None:
        errors.append("unterminated fenced code block")
    if in_comment:
        errors.append("unterminated HTML comment")
    return MarkdownScan(
        visible="\n".join(visible_lines),
        prose="\n".join(prose_lines),
        fenced_blocks=tuple(fenced_blocks),
        errors=tuple(errors),
    )


# The review depth is read by a script. Its path list and the table in the
# lens reference are one rule in two places, so they are compared exactly.
REVIEW_DEPTH_REL = "docs/ai_methodology/skills/review-loop/scripts/review_depth.py"
REVIEW_DEPTH_LENSES_REL = "references/SCIENCE_LENSES.md"
REVIEW_DEPTH_HEADING = "## Review depth"
REVIEW_DEPTH_ROW_RE = re.compile(r"^\| `(?P<path>[^`|]+)` \| (?P<change>any|added) \|$")
REPO_BOUND_FAMILIES = ("review_depth_paths",)


def review_depth_table(lenses: str) -> tuple[tuple[str, str], ...] | None:
    """Return the working-material rows of the one active Review depth section."""
    prose = _markdown_scan(lenses).prose
    if sum(line.strip() == REVIEW_DEPTH_HEADING for line in prose.splitlines()) != 1:
        return None
    section = prose.split(REVIEW_DEPTH_HEADING, 1)[1]
    section = re.split(r"^## ", section, maxsplit=1, flags=re.MULTILINE)[0]
    rows = (REVIEW_DEPTH_ROW_RE.match(line) for line in section.splitlines())
    return tuple((row["path"], row["change"]) for row in rows if row)


def review_depth_script_paths(script: str) -> tuple[tuple[str, str], ...] | None:
    """Read WORKING_MATERIAL from the script source without running it."""
    try:
        tree = ast.parse(script)
    except SyntaxError:
        return None
    assigned = [
        node.value for node in tree.body
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "WORKING_MATERIAL"
                for target in node.targets)
    ]
    if len(assigned) != 1:
        return None
    try:
        value = ast.literal_eval(assigned[0])
    except (ValueError, SyntaxError):
        return None
    if not isinstance(value, tuple) or not all(
        isinstance(item, tuple) and len(item) == 2
        and all(isinstance(part, str) for part in item)
        for item in value
    ):
        return None
    return value


def review_depth_paths_ok(lenses: str, script: str) -> bool:
    """The prose table and the script must list the same paths in the same order."""
    table = review_depth_table(lenses)
    return bool(table) and table == review_depth_script_paths(script)


def review_depth_failures(repo_root: Path) -> list[str]:
    """Name the families that fail when the table and the script disagree."""
    try:
        lenses = ((repo_root / SKILL_REL).parent / REVIEW_DEPTH_LENSES_REL).read_text(
            encoding="utf-8"
        )
        script = (repo_root / REVIEW_DEPTH_REL).read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return list(REPO_BOUND_FAMILIES)
    return [] if review_depth_paths_ok(lenses, script) else list(REPO_BOUND_FAMILIES)


@dataclass
class _ShellFrame:
    """One multiline shell lexical context."""

    kind: str
    paren_depth: int = 0


@dataclass(frozen=True)
class ShellScan:
    """Top-level shell text after inert lexical regions are blanked."""

    active: str
    errors: tuple[str, ...]


def _heredoc_word(line: str, start: int) -> tuple[str, int] | None:
    """Parse one shell heredoc delimiter with quote removal."""
    index = start
    while index < len(line) and line[index] in " \t":
        index += 1
    if index == len(line) or line[index] in ";|&()<>":
        return None

    value: list[str] = []
    quote: str | None = None
    while index < len(line):
        char = line[index]
        if quote is not None:
            if char == quote:
                quote = None
            elif char == "\\" and quote == '"' and index + 1 < len(line):
                index += 1
                value.append(line[index])
            else:
                value.append(char)
            index += 1
            continue
        if char in " \t;|&()<>":
            break
        if char in {"'", '"'}:
            quote = char
            index += 1
            continue
        if char == "\\" and index + 1 < len(line):
            index += 1
            value.append(line[index])
            index += 1
            continue
        value.append(char)
        index += 1
    if quote is not None:
        return None
    return "".join(value), index


def _continued_shell_unit(
    physical_lines: list[str], start: int
) -> tuple[list[str], str, int]:
    """Fold Bash physical continuations into one lexical command unit."""
    unit = [physical_lines[start]]
    folded = physical_lines[start]
    cursor = start + 1
    while cursor < len(physical_lines):
        trailing = len(folded) - len(folded.rstrip("\\"))
        escaped_newline = trailing % 2 == 1
        grammar_continuation = bool(
            re.search(r"(?:\|\||&&|\|&|\|)\s*$", folded)
        )
        if not escaped_newline and not grammar_continuation:
            break
        if escaped_newline:
            folded = folded[:-1] + physical_lines[cursor]
        else:
            folded = folded + " " + physical_lines[cursor]
        unit.append(physical_lines[cursor])
        cursor += 1
    return unit, folded, cursor


def _active_shell(text: str) -> ShellScan:
    """Structurally blank non-top-level shell text.

    The lexer tracks nested quotes, backticks, command/process substitutions,
    and the ordered payload queue for every heredoc attached to a command. A
    line that begins or ends in one of those contexts is inert for contract
    matching. Unterminated contexts fail closed through ``errors``.
    """
    lines: list[str] = []
    frames: list[_ShellFrame] = []
    heredocs: list[tuple[str, bool]] = []
    physical_lines = text.splitlines()
    cursor = 0

    while cursor < len(physical_lines):
        if heredocs:
            raw = physical_lines[cursor]
            cursor += 1
            delimiter, strip_tabs = heredocs[0]
            candidate = raw.lstrip("\t") if strip_tabs else raw
            lines.append("")
            if candidate == delimiter:
                heredocs.pop(0)
            continue

        unit, raw, cursor = _continued_shell_unit(physical_lines, cursor)
        started_in_inert_text = bool(frames)
        comment_at: int | None = None
        index = 0
        while index < len(raw):
            char = raw[index]
            frame = frames[-1] if frames else None

            if frame is not None and frame.kind == "single":
                if char == "'":
                    frames.pop()
                index += 1
                continue

            if char == "\\":
                index += 2
                continue

            if frame is not None and frame.kind == "double":
                if char == '"':
                    frames.pop()
                    index += 1
                    continue
                if char == "`":
                    frames.append(_ShellFrame("backtick"))
                    index += 1
                    continue
                if raw.startswith("$(", index):
                    frames.append(_ShellFrame("substitution", 1))
                    index += 2
                    continue
                index += 1
                continue

            if frame is not None and frame.kind == "backtick" and char == "`":
                frames.pop()
                index += 1
                continue

            if char == "'":
                frames.append(_ShellFrame("single"))
                index += 1
                continue
            if char == '"':
                frames.append(_ShellFrame("double"))
                index += 1
                continue
            if char == "`":
                frames.append(_ShellFrame("backtick"))
                index += 1
                continue

            if raw.startswith("$(", index) or (
                char in "<>" and index + 1 < len(raw) and raw[index + 1] == "("
            ):
                frames.append(_ShellFrame("substitution", 1))
                index += 2
                continue

            if frame is not None and frame.kind in {"substitution", "subshell"}:
                if char == "(":
                    frame.paren_depth += 1
                    index += 1
                    continue
                if char == ")":
                    frame.paren_depth -= 1
                    if frame.paren_depth == 0:
                        frames.pop()
                    index += 1
                    continue

            if char == "(":
                frames.append(_ShellFrame("subshell", 1))
                index += 1
                continue

            if raw.startswith("<<", index) and not raw.startswith("<<<", index):
                strip_tabs = raw.startswith("<<-", index)
                word_start = index + (3 if strip_tabs else 2)
                parsed = _heredoc_word(raw, word_start)
                if parsed is not None:
                    delimiter, index = parsed
                    heredocs.append((delimiter, strip_tabs))
                    continue

            if char == "#" and (index == 0 or raw[index - 1].isspace()):
                comment_at = index
                break
            index += 1

        active = raw[:comment_at].rstrip() if comment_at is not None else raw
        if started_in_inert_text or frames:
            lines.extend("" for _ in unit)
        elif len(unit) == 1:
            lines.append(active)
        else:
            # Preserve physical lines for exact multiline contract matching;
            # ``raw`` was used only for lexical parsing after continuation fold.
            lines.extend(unit)

    errors: list[str] = []
    if frames:
        errors.append("unterminated shell lexical context")
    if heredocs:
        errors.append("unterminated shell heredoc")
    return ShellScan(active="\n".join(lines), errors=tuple(errors))


def _section_disables_reviewer(body: str, reviewer: str) -> bool:
    """Reject any active instruction that disables its bound reviewer."""
    escaped_name = re.escape(reviewer)
    exact_name = re.compile(rf"(?:`{escaped_name}`|\b{escaped_name}\b)", re.I)
    for line in body.splitlines():
        if not REVIEWER_DISABLE_RE.search(line):
            continue
        if exact_name.search(line) or re.search(
            r"\b(?:this\s+)?reviewer\b", line, re.I
        ):
            return True
    return False


def _reviewer_structure_ok(prose: str) -> bool:
    """Bind every reviewer label to its own active, affirmative section body."""
    lines = prose.splitlines()

    def unique_index(needle: str) -> int | None:
        found = [i for i, line in enumerate(lines) if line.strip() == needle]
        return found[0] if len(found) == 1 else None

    def from_first_nonblank(start: int, end: int) -> str:
        first = next((i for i in range(start, end) if lines[i].strip()), end)
        return "\n".join(lines[first:end])

    fanout = unique_index("## Reviewer Fanout")
    required = unique_index("### Required Reviewers")
    optional = unique_index("### Optional Reviewer")
    prompt = unique_index("## Reviewer Prompt")
    if None in (fanout, required, optional, prompt):
        return False
    assert fanout is not None and required is not None
    assert optional is not None and prompt is not None
    if not fanout < required < optional < prompt:
        return False

    positions: list[tuple[str, int]] = []
    for reviewer in REVIEWER_BODY_RULES:
        label = f"- `{reviewer}`"
        found = [
            i
            for i in range(required + 1, optional)
            if lines[i].strip() == label
        ]
        if len(found) != 1:
            return False
        positions.append((reviewer, found[0]))
    if [position for _, position in positions] != sorted(
        position for _, position in positions
    ):
        return False

    flags = re.IGNORECASE | re.DOTALL | re.MULTILINE
    for index, (reviewer, start) in enumerate(positions):
        end = positions[index + 1][1] if index + 1 < len(positions) else optional
        body = "\n".join(lines[start + 1 : end])
        first_instruction = from_first_nonblank(start + 1, end)
        if _section_disables_reviewer(body, reviewer):
            return False
        if re.match(REVIEWER_BODY_RULES[reviewer], first_instruction, flags) is None:
            return False

    methodology = "\n".join(lines[optional + 1 : prompt])
    methodology_first = from_first_nonblank(optional + 1, prompt)
    return (
        not _section_disables_reviewer(methodology, "MethodologySkillReviewer")
        and re.match(METHODOLOGY_BODY_RULE, methodology_first, flags) is not None
    )


def _shell_depths(text: str) -> tuple[list[int], bool]:
    """Return shell compound-command depth before each line.

    The checked snippets use ordinary multiline Bash compound commands. Tracking
    their opening/closing tokens is enough to distinguish executable top-level
    gates from unchanged text nested under `if false`, a loop, case, function,
    brace group, or standalone subshell. Any imbalance fails closed.
    """
    depths: list[int] = []
    depth = 0
    valid = True
    for raw in text.splitlines():
        line = raw.strip()
        close_count = int(bool(re.match(r"^(?:fi|done|esac)\b", line)))
        close_count += len(re.findall(r"(?<![$\w])\}(?=(?:[;\s]|$))", line))
        close_count += int(line == ")")
        depth -= close_count
        if depth < 0:
            valid = False
            depth = 0
        depths.append(depth)

        open_count = int(
            bool(re.match(r"^(?:if|for|while|until|case|select)\b", line))
        )
        open_count += len(re.findall(r"(?<![$\w])\{(?=(?:[;\s]|$))", line))
        open_count += int(line == "(")
        depth += open_count
    return depths, valid and depth == 0


def _context_is_top_level(shell: str, context: str) -> bool:
    """Require one exact context whose first command is at shell depth zero."""
    scan = _active_shell(shell)
    lines = scan.active.splitlines()
    wanted = context.splitlines()
    starts = [
        i
        for i in range(0, len(lines) - len(wanted) + 1)
        if lines[i : i + len(wanted)] == wanted
    ]
    depths, balanced = _shell_depths(scan.active)
    return not scan.errors and balanced and len(starts) == 1 and depths[starts[0]] == 0


def _landing_script_body(script: str) -> tuple[str, list[int]] | None:
    """Return the active body of ``land_train`` and its command depths.

    The loop runs only if the script defines ``land_train`` once at the top
    level and calls it as its last command, and it sees validated inputs only
    if reading the train file is the first command of that body. Depths are
    relative to the body: a command the loop always runs has depth zero. Any
    lexical error, imbalance or other layout fails closed.
    """
    shell_scan = _active_shell(script)
    lines = shell_scan.active.splitlines()
    depths, balanced = _shell_depths(shell_scan.active)
    if shell_scan.errors or not balanced:
        return None
    entries = [
        index
        for index, line in enumerate(lines)
        if line == LANDING_SCRIPT_ENTRY and depths[index] == 0
    ]
    if len(entries) != 1:
        return None
    start = entries[0]
    end = next(
        (index for index in range(start + 1, len(lines)) if depths[index] == 0),
        None,
    )
    if end is None or lines[end] != "}":
        return None
    if [line for line in lines[end + 1 :] if line.strip()] != [LANDING_SCRIPT_CALL]:
        return None
    body = lines[start + 1 : end]
    first = next((line.strip() for line in body if line.strip()), "")
    if first != LANDING_SCRIPT_READS_INPUT:
        return None
    return "\n".join(body), [depth - 1 for depth in depths[start + 1 : end]]


def _landing_containment_is_unconditional(script: str) -> bool:
    """Require the one containment check as a command the loop always runs."""
    shell = _landing_script_body(script)
    return shell is not None and _active_context_is_at_depth(
        shell[0], CONTAINMENT_CONTEXT, 0
    )


def _landing_run_command_ok(scan: MarkdownScan) -> bool:
    """Require one shell block that runs the package script and nothing else."""
    candidates = [
        body
        for info, body in scan.fenced_blocks
        if info.split(maxsplit=1)[:1] in (["bash"], ["sh"], ["shell"], ["zsh"])
        and "land_train.sh" in body
    ]
    if len(candidates) != 1:
        return False
    shell_scan = _active_shell(candidates[0])
    commands = [
        line.strip() for line in shell_scan.active.splitlines() if line.strip()
    ]
    return not shell_scan.errors and commands == [LANDING_RUN_COMMAND]


def _ordered_lines_at_depth(
    active: str, depths: list[int], expected: tuple[tuple[str, int], ...]
) -> bool:
    """Require unique active shell lines in the stated order and command depth."""
    lines = active.splitlines()
    positions: list[int] = []
    for wanted, depth in expected:
        matches = [
            index
            for index, line in enumerate(lines)
            if line.strip() == wanted and depths[index] == depth
        ]
        if len(matches) != 1:
            return False
        positions.append(matches[0])
    return positions == sorted(positions)


def _active_context_is_at_depth(
    active: str, context: str, expected_depth: int
) -> bool:
    """Require one exact active-shell context beginning at the requested depth."""
    lines = active.splitlines()
    wanted = context.splitlines()
    starts = [
        index
        for index in range(0, len(lines) - len(wanted) + 1)
        if lines[index : index + len(wanted)] == wanted
    ]
    depths, balanced = _shell_depths(active)
    return balanced and len(starts) == 1 and depths[starts[0]] == expected_depth


def _marked_train_shell(scan: MarkdownScan, marker: str) -> str | None:
    """Return one balanced active shell block carrying an executable marker."""
    candidates = [
        body
        for info, body in scan.fenced_blocks
        if info.split(maxsplit=1)[0] in {"bash", "sh", "shell", "zsh"}
        and marker in body
    ]
    if len(candidates) != 1:
        return None
    shell_scan = _active_shell(candidates[0])
    _, balanced = _shell_depths(shell_scan.active)
    if shell_scan.errors or not balanced:
        return None
    return shell_scan.active


def _combined_validation_recipe_ok(scan: MarkdownScan) -> bool:
    validation = _marked_train_shell(scan, "TRAIN_COMBINED_VALIDATION_SCOPE=")
    clean = _marked_train_shell(scan, "TRAIN_COMBINED_CLEAN_SCOPE=")
    if validation is None or clean is None:
        return False
    if not _active_context_is_at_depth(validation, TRAIN_VALIDATION_CONTEXT, 0):
        return False
    if not _active_context_is_at_depth(clean, TRAIN_CLEAN_CONTEXT, 0):
        return False
    return True


def _train_combined_gate_structure_ok(scan: MarkdownScan, script: str) -> bool:
    if not _combined_validation_recipe_ok(scan):
        return False
    shell = _landing_script_body(script)
    if shell is None:
        return False
    active, depths = shell
    return _ordered_lines_at_depth(
        active,
        depths,
        (
            (LANDING_SCRIPT_READS_INPUT, 0),
            ('if [ "$(git rev-parse origin/main)" != "$VALIDATED_BASE" ]; then', 1),
            (
                'if [ "$(git rev-parse \'HEAD^{tree}\')" '
                '!= "$VALIDATED_TREE" ]; then',
                1,
            ),
            ("if git push -q origin HEAD:main; then", 1),
        ),
    )


def _train_head_guard_structure_ok(script: str) -> bool:
    shell = _landing_script_body(script)
    if shell is None:
        return False
    active, depths = shell
    for context, depth in (
        (TRAIN_HEAD_FUNCTION_CONTEXT, 0),
        (TRAIN_HEAD_MOVE_CONTEXT, 0),
        (TRAIN_PRE_PUSH_HEAD_CONTEXT, 1),
        (TRAIN_HEAD_RESTORE_CONTEXT, 1),
        (TRAIN_POST_PUSH_HEAD_CONTEXT, 1),
    ):
        if not _active_context_is_at_depth(active, context, depth):
            return False
    return _ordered_lines_at_depth(
        active,
        depths,
        (
            ("verify_pr_head() {", 0),
            ("verify_frozen_pr_heads() {", 0),
            ("verify_pr_github_state() {", 0),
            ("record_recovery_refs() {", 0),
            ("move_pr_heads() {", 0),
            ("wait_for_landed_pr_heads() {", 0),
            ("restore_frozen_pr_heads() {", 0),
            ("if ! verify_frozen_pr_heads; then", 1),
            ("if ! verify_pr_github_state; then", 1),
            ("if ! record_recovery_refs; then", 1),
            ("if ! move_pr_heads; then", 1),
            ("if ! wait_for_landed_pr_heads; then", 1),
            ("if git push -q origin HEAD:main; then", 1),
            ("if ! restore_frozen_pr_heads; then", 1),
            ('if ! git merge-base --is-ancestor "$landed" origin/main; then', 0),
            ('if ! verify_pr_head "$pr" "$expected"; then', 1),
            (
                "printf 'MERGED %s %s %s\\n' \"$pr\" "
                "\"${PR_HEADS[$index]}\" \"$expected\"",
                2,
            ),
        ),
    )


def _landing_script_entry_ok(scan: MarkdownScan, script: str) -> bool:
    """Bind the documented command to a script that checks and sets all inputs."""
    if not _landing_run_command_ok(scan) or _landing_script_body(script) is None:
        return False
    active = _active_shell(script).active
    depths, _ = _shell_depths(active)
    return _ordered_lines_at_depth(
        active,
        depths,
        (
            ('if [ -z "${BASH_VERSION:-}" ]; then', 0),
            ("read_train_file() {", 0),
            (
                '*[!0123456789]*) train_file_error '
                '"$name entry is not a PR number: $entry" ;;',
                5,
            ),
            ('if ! git check-ref-format "refs/heads/$entry"; then', 4),
            ('if ! is_object_name "$entry"; then', 4),
            ('if [ "${#entries[@]}" -ne 1 ]; then', 3),
            ('VALIDATED_BASE) VALIDATED_BASE="${entries[0]}" ;;', 3),
            ('VALIDATED_TREE) VALIDATED_TREE="${entries[0]}" ;;', 3),
            ('COMMITS) COMMITS=("${entries[@]}") ;;', 3),
            ('PR_NUMBERS) PR_NUMBERS=("${entries[@]}") ;;', 3),
            ('PR_HEADS) PR_HEADS=("${entries[@]}") ;;', 3),
            ('PR_HEAD_REFS) PR_HEAD_REFS=("${entries[@]}") ;;', 3),
            ('PR_TIPS) PR_TIPS=("${entries[@]}") ;;', 3),
            (LANDING_SCRIPT_ENTRY, 0),
            (LANDING_SCRIPT_CALL, 0),
        ),
    )


def _missing(text: str, rules: dict[str, tuple[str, ...]]) -> list[str]:
    return [
        name
        for name, patterns in rules.items()
        if any(
            re.search(pattern, text, re.IGNORECASE | re.DOTALL | re.MULTILINE) is None
            for pattern in patterns
        )
    ]


def _append_once(items: list[str], name: str) -> None:
    if name not in items:
        items.append(name)


def validate_texts(
    skill: str,
    landing_script: str,
    generator: str,
    pipeline: str,
    command: str | None = None,
    placement_references: dict[str, str] | None = None,
) -> list[str]:
    """Return invariant-family names that are absent from the supplied texts."""
    scan = _markdown_scan(skill)
    active_skill = scan.visible
    command_scan = _markdown_scan(command) if command is not None else None
    active_command = command_scan.visible if command_scan is not None else ""
    pipeline_scan = _active_shell(pipeline)
    active_pipeline = pipeline_scan.active
    missing = (
        _missing(active_skill, SKILL_RULES)
        + _missing(scan.prose, UNIT_PROSE_RULES)
        + _missing(generator, GENERATOR_RULES)
        + _missing(active_pipeline, PIPELINE_RULES)
        + (_missing(active_command, COMMAND_RULES) if command_scan is not None else [])
    )
    for name in _missing(_active_shell(landing_script).active, LANDING_SCRIPT_RULES):
        _append_once(missing, name)
    if scan.errors:
        _append_once(missing, "markdown_structure")
    if "docs/publication/ci3_z3" in active_skill:
        _append_once(missing, "live_surface_routing")
    if command_scan is not None and command_scan.errors:
        _append_once(missing, "command_landing_train")
    if pipeline_scan.errors:
        _append_once(missing, "pipeline_contract_registration")
    if not _reviewer_structure_ok(scan.prose):
        _append_once(missing, "reviewer_lenses")
    if not _landing_script_entry_ok(scan, landing_script):
        _append_once(missing, "landing_script_entry")
    if not _landing_containment_is_unconditional(landing_script):
        _append_once(missing, "fail_closed_landing")
    if not _train_combined_gate_structure_ok(scan, landing_script):
        _append_once(missing, "landing_train_combined_gate")
    if not _train_head_guard_structure_ok(landing_script):
        _append_once(missing, "landing_train_head_guard")
    if not _context_is_top_level(pipeline, PIPELINE_CONTRACT_CONTEXT):
        _append_once(missing, "pipeline_contract_registration")
    if placement_references is not None:
        placement_clauses = {
            "preflight": r"refer to one shared pass on the exact integrated\s+"
            r"current-main candidate, not a separate full run per constituent or unit",
            "conformance": r"Full pipeline, strict lint, and changed-evidence checks below are one\s+"
            r"shared pass on the exact integrated current-main candidate; they are not\s+"
            r"additional per-PR or per-unit pre-review runs",
            "workflow": r"then one full mechanical\s+pipeline, strict lint, and changed-evidence validation on the exact integrated\s+"
            r"current-main candidate",
        }
        for name, clause in placement_clauses.items():
            reference_scan = _markdown_scan(placement_references.get(name, ""))
            if reference_scan.errors or not re.search(clause, reference_scan.prose):
                _append_once(missing, f"shared_validation_reference_{name}")
    return missing


def load_skill_contract(repo_root: Path) -> tuple[str, list[str]]:
    """Read the routed contract, rejecting absent, hidden or optional routes.

    Read each file separately before joining: an unterminated comment/fence in
    one source must not be repaired by a delimiter in a different source. The
    existing prose, shell, and mutation guards then see all operative content.
    Fixed package-relative paths avoid silently accepting an unrelated file.
    """
    skill_path = repo_root / SKILL_REL
    package = skill_path.parent.resolve()
    missing: list[str] = []
    try:
        entry = skill_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return "", ["skill_entry_unreadable"]
    entry_scan = _markdown_scan(entry)
    if entry_scan.errors:
        missing.append("skill_entry_markdown_structure")
    heading = "## Required reference routing"
    if entry_scan.prose.count(heading) != 1:
        missing.append("reference_routing_section")
        routing = ""
    else:
        routing = entry_scan.prose.split(heading, 1)[1]
        routing = re.split(r"^## ", routing, maxsplit=1, flags=re.MULTILINE)[0]
    for name, pattern in ROUTING_RULES.items():
        if not re.search(pattern, routing):
            missing.append(f"reference_routing_{name}")
    sources: dict[str, str] = {"SKILL.md": entry}
    for relative, trigger in REFERENCE_TRIGGER_RULES.items():
        # The requirement must be an active table row in the routing section;
        # prose in a code sample, HTML comment or link definition cannot route
        # an agent to a procedure. Every link is coupled to its actual trigger.
        row = re.compile(
            r"^\| " + trigger + r"[^|]* \| .*\]\("
            + re.escape(relative) + r"\) \|$", re.MULTILINE,
        )
        stem = Path(relative).stem.lower()
        route = row.search(routing)
        trigger_cell = route[0].split("|")[1] if route else ""
        if (route is None or REVIEWER_DISABLE_RE.search(trigger_cell)
                or re.search(r"\boptional\b", trigger_cell, re.IGNORECASE)):
            missing.append(f"reference_route_{stem}")
        path = skill_path.parent / relative
        if not path.resolve().is_relative_to(package):
            missing.append(f"reference_outside_package_{stem}")
            continue
        try:
            source = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            missing.append(f"reference_unreadable_{stem}")
            continue
        source_scan = _markdown_scan(source)
        if source_scan.errors:
            missing.append(f"reference_markdown_structure_{stem}")
        if relative == "references/COMBINED_VALIDATION.md" and any(
            not re.search(pattern, source_scan.prose)
            for pattern in REVIEW_ONLY_VALIDATION_RULES
        ):
            missing.append("review_only_validation_isolation")
        if relative in SKILL_CONTRACT_REFERENCES:
            sources[relative] = source
    for rules, locations, prose_only in (
        (SKILL_RULES, SKILL_RULE_LOCATIONS, False),
        (UNIT_PROSE_RULES, UNIT_RULE_LOCATIONS, True),
    ):
        for family, patterns in rules.items():
            local = _markdown_scan("\n\n".join(
                sources.get(name, "") for name in locations.get(family, ())
            ))
            text = local.prose if prose_only else local.visible
            if _missing(text, {family: patterns}):
                missing.append(f"routed_{family}")
    lenses = _markdown_scan(sources.get("references/SCIENCE_LENSES.md", ""))
    if not _reviewer_structure_ok(lenses.prose):
        _append_once(missing, "routed_reviewer_lenses")
    combined = _markdown_scan(sources.get("references/COMBINED_VALIDATION.md", ""))
    if not _combined_validation_recipe_ok(combined):
        _append_once(missing, "routed_landing_train_combined_gate")
    landing = _markdown_scan(sources.get("references/LANDING.md", ""))
    if not _landing_run_command_ok(landing):
        _append_once(missing, "routed_landing_script_entry")
    parts = [entry] + [sources.get(name, "") for name in SKILL_CONTRACT_REFERENCES]
    return "\n\n".join(parts), missing


def load_landing_script(repo_root: Path) -> tuple[str, list[str]]:
    """Read the landing loop from its fixed place inside the skill package."""
    package = (repo_root / SKILL_REL).parent
    path = package / LANDING_SCRIPT_PACKAGE_PATH
    if not path.resolve().is_relative_to(package.resolve()):
        return "", ["landing_script_outside_package"]
    try:
        return path.read_text(encoding="utf-8"), []
    except (OSError, UnicodeError):
        return "", ["landing_script_unreadable"]


def validate_repo(repo_root: Path) -> list[str]:
    skill, routing_failures = load_skill_contract(repo_root)
    landing_script, script_failures = load_landing_script(repo_root)
    return routing_failures + script_failures + validate_texts(
        skill,
        landing_script,
        (repo_root / GENERATOR_REL).read_text(encoding="utf-8"),
        (repo_root / PIPELINE_REL).read_text(encoding="utf-8"),
        (repo_root / COMMAND_REL).read_text(encoding="utf-8"),
        {name: (repo_root / path).read_text(encoding="utf-8")
         for name, path in PLACEMENT_REFERENCES.items()},
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(REPO_ROOT))
    args = parser.parse_args(argv)
    root = Path(args.repo_root).resolve()
    missing = validate_repo(root)
    missing += review_depth_failures(root)
    if missing:
        print("check_review_loop_skill_contract: FAIL")
        for name in missing:
            print(f"  missing invariant family: {name}")
        return 1
    family_count = (
        len(set(SKILL_RULES) | set(LANDING_SCRIPT_RULES))
        + len(UNIT_PROSE_RULES)
        + len(GENERATOR_RULES)
        + len(PIPELINE_RULES)
        + len(COMMAND_RULES)
        + len(PLACEMENT_REFERENCES)
        + len(REPO_BOUND_FAMILIES)
    )
    print(
        "check_review_loop_skill_contract: OK "
        f"({family_count} families)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
