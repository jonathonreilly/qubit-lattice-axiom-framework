#!/usr/bin/env python3
"""Fail closed if review-loop loses a quality, safety, or landing invariant."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SKILL_REL = "docs/ai_methodology/skills/review-loop/SKILL.md"
GENERATOR_REL = "docs/audit/scripts/generate_skill_axiom_baselines.py"
PIPELINE_REL = "docs/audit/scripts/run_pipeline.sh"
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
COMMONMARK_COMMENT_RE = re.compile(r"^[ \t]*\[//\]:[ \t]*#.*(?:\n|$)", re.MULTILINE)
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


# These are structural tripwires, not a substitute for methodology review.
# Exact positive clauses protect load-bearing commands from commented-out,
# negated, or inert-token mutations while allowing ordinary prose wrapping.
SKILL_RULES: dict[str, tuple[str, ...]] = {
    "freshness": (
        r"^## Skill Freshness\s*$",
        r"^Before applying this skill, perform the repo skill freshness check "
        r"described in\s+`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK\.md`\. "
        r"If a newer version of\s+this `SKILL\.md` exists on `origin/main`, "
        r"follow that version for the current\s+task\.$",
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
        r"^Review-loop is a text/code/math review path\. Run it with the user's "
        r"configured\s+highest-tier Codex reviewer model "
        r"and maximum available reasoning for this\s+repo \(currently "
        r"GPT-5\.6-Sol; use the maximum available reasoning tier unless\s+the "
        r"owner directs a specific tier for the episode\)\.",
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
        r"no_go_discipline_gate\.py",
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
    "pipeline_strict_and_evidence": (
        r"run_pipeline\.sh",
        r"audit_lint\.py --strict",
        r"check_changed_audit_evidence\.py",
    ),
    "manifest_landing": (
        r"PROACTIVE rule",
        r"before EVERY push attempt",
        r"run_citation_graph_build\.py",
        r"write_citation_graph_manifest\.py",
        r"citation_graph_manifest\.json",
    ),
    "disk_and_worktree_guards": (
        r"5242880",
        r"mktemp -d",
        r"trap cleanup_review_wt EXIT",
        r"retained dirty worktree for recovery",
    ),
    "fail_closed_landing": (
        r"for attempt in 1 2 3 4",
        r"landed=",
        r"refs/heads/main:refs/remotes/origin/main",
        r'^\s*if ! git merge-base --is-ancestor "\$landed" origin/main; then\s*$',
        r"landing did not complete after 4 attempts",
    ),
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


def _active_markdown(text: str) -> str:
    """Remove non-rendered Markdown material; comments never satisfy a contract."""
    return COMMONMARK_COMMENT_RE.sub("", HTML_COMMENT_RE.sub("", text))


def _active_shell(text: str) -> str:
    """Remove full-line shell comments; only active commands count."""
    return "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("#")
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


def validate_texts(skill: str, generator: str, pipeline: str) -> list[str]:
    """Return invariant-family names that are absent from the supplied texts."""
    active_skill = _active_markdown(skill)
    active_pipeline = _active_shell(pipeline)
    missing = (
        _missing(active_skill, SKILL_RULES)
        + _missing(generator, GENERATOR_RULES)
        + _missing(active_pipeline, PIPELINE_RULES)
    )
    if CONTAINMENT_CONTEXT not in active_skill:
        _append_once(missing, "fail_closed_landing")
    if PIPELINE_CONTRACT_CONTEXT not in active_pipeline:
        _append_once(missing, "pipeline_contract_registration")
    return missing


def validate_repo(repo_root: Path) -> list[str]:
    return validate_texts(
        (repo_root / SKILL_REL).read_text(encoding="utf-8"),
        (repo_root / GENERATOR_REL).read_text(encoding="utf-8"),
        (repo_root / PIPELINE_REL).read_text(encoding="utf-8"),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=str(REPO_ROOT))
    args = parser.parse_args(argv)
    root = Path(args.repo_root).resolve()
    missing = validate_repo(root)
    if missing:
        print("check_review_loop_skill_contract: FAIL")
        for name in missing:
            print(f"  missing invariant family: {name}")
        return 1
    print(
        "check_review_loop_skill_contract: OK "
        f"({len(SKILL_RULES) + len(GENERATOR_RULES) + len(PIPELINE_RULES)} families)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
