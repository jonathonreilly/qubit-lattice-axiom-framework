#!/usr/bin/env python3
"""Fail closed if review-loop loses a quality, safety, or landing invariant."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SKILL_REL = "docs/ai_methodology/skills/review-loop/SKILL.md"
GENERATOR_REL = "docs/audit/scripts/generate_skill_axiom_baselines.py"
PIPELINE_REL = "docs/audit/scripts/run_pipeline.sh"
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
REVIEWER_NEGATION_RE = re.compile(
    r"^\s*(?:do not|don't|never|skip|disable)\b[^\n]*\breviewer\b",
    re.IGNORECASE | re.MULTILINE,
)


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


def _active_shell(text: str) -> str:
    """Blank shell comments, multiline strings, and here-document payloads."""
    lines: list[str] = []
    quote: str | None = None
    backtick = False
    command_substitution = False
    heredoc: str | None = None
    heredoc_re = re.compile(
        r"(?<!<)<<-?(?!<)[ \t]*"
        r"(?P<word>'[^'\n]*'|\"[^\"\n]*\"|[^\s;|&()<>]+)"
    )
    for raw in text.splitlines():
        if heredoc is not None:
            lines.append("")
            if raw.strip() == heredoc:
                heredoc = None
            continue

        if command_substitution:
            lines.append("")
            close = re.match(r"^\s*\)(?P<quote>['\"]?)\s*$", raw)
            if close:
                command_substitution = False
                if close.group("quote") and close.group("quote") == quote:
                    quote = None
            continue

        started_in_inert_text = quote is not None or backtick
        opens_command_substitution = bool(re.search(r"\$\(\s*$", raw))
        escaped = False
        comment_at: int | None = None
        for index, char in enumerate(raw):
            if quote == "'":
                if char == "'":
                    quote = None
                continue
            if escaped:
                escaped = False
                continue
            if char == "\\":
                escaped = True
                continue
            if backtick:
                if char == "`":
                    backtick = False
                continue
            if quote == '"':
                if char == "`":
                    backtick = True
                    continue
                if char == '"':
                    quote = None
                continue
            if char == "`":
                backtick = True
                continue
            if char in {"'", '"'}:
                quote = char
                continue
            if char == "#" and (index == 0 or raw[index - 1].isspace()):
                comment_at = index
                break

        active = raw[:comment_at].rstrip() if comment_at is not None else raw
        # A line entered while a multiline quote was open is string payload,
        # even if it also carries the closing quote.
        lines.append("" if started_in_inert_text else active)
        if opens_command_substitution:
            command_substitution = True
            continue
        if not started_in_inert_text and quote is None and not backtick:
            match = heredoc_re.search(active)
            if match:
                word = match.group("word")
                if len(word) >= 2 and word[0] == word[-1] and word[0] in {'"', "'"}:
                    word = word[1:-1]
                heredoc = re.sub(r"\\(.)", r"\1", word)
    return "\n".join(lines)


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
        named_negation = re.compile(
            r"^\s*(?:do not|don't|never|skip|disable)\b[^\n]*"
            + rf"(?:`{re.escape(reviewer)}`|\b{re.escape(reviewer)}\b)",
            re.IGNORECASE | re.MULTILINE,
        )
        if REVIEWER_NEGATION_RE.search(body) or named_negation.search(body):
            return False
        if re.match(REVIEWER_BODY_RULES[reviewer], first_instruction, flags) is None:
            return False

    methodology = "\n".join(lines[optional + 1 : prompt])
    methodology_first = from_first_nonblank(optional + 1, prompt)
    methodology_negation = re.compile(
        r"^\s*(?:do not|don't|never|skip|disable)\b[^\n]*"
        r"(?:`MethodologySkillReviewer`|\bMethodologySkillReviewer\b)",
        re.IGNORECASE | re.MULTILINE,
    )
    return (
        REVIEWER_NEGATION_RE.search(methodology) is None
        and methodology_negation.search(methodology) is None
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
    shell = _active_shell(shell)
    lines = shell.splitlines()
    wanted = context.splitlines()
    starts = [
        i
        for i in range(0, len(lines) - len(wanted) + 1)
        if lines[i : i + len(wanted)] == wanted
    ]
    depths, balanced = _shell_depths(shell)
    return balanced and len(starts) == 1 and depths[starts[0]] == 0


def _landing_context_is_top_level(scan: MarkdownScan) -> bool:
    candidates = [
        body
        for info, body in scan.fenced_blocks
        if info.split(maxsplit=1)[0] in {"bash", "sh", "shell", "zsh"}
        and CONTAINMENT_CONTEXT in body
    ]
    return len(candidates) == 1 and _context_is_top_level(
        candidates[0], CONTAINMENT_CONTEXT
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
    scan = _markdown_scan(skill)
    active_skill = scan.visible
    active_pipeline = _active_shell(pipeline)
    missing = (
        _missing(active_skill, SKILL_RULES)
        + _missing(generator, GENERATOR_RULES)
        + _missing(active_pipeline, PIPELINE_RULES)
    )
    if scan.errors:
        _append_once(missing, "markdown_structure")
    if not _reviewer_structure_ok(scan.prose):
        _append_once(missing, "reviewer_lenses")
    if not _landing_context_is_top_level(scan):
        _append_once(missing, "fail_closed_landing")
    if not _context_is_top_level(pipeline, PIPELINE_CONTRACT_CONTEXT):
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
