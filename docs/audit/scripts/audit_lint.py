#!/usr/bin/env python3
"""Lint the audit ledger for consistency.

Checks (all hard rules from FRESH_LOOK_REQUIREMENTS.md and README.md):

  1. Schema:
     - Every row has the expected fields.
     - audit_status is one of the allowed enum values.
     - claim_type is one of the auditor-owned allowed enum values.
     - legacy source-status fields are absent from generated audit data.

  2. The hard rules:
     - audit_status = audited_clean requires auditor and auditor_family set.
     - audit_status = audited_clean promotes only through claim_type:
       positive_theorem -> retained, no_go -> retained_no_go, and
       bounded_theorem -> retained_bounded, provided the dependency chain is
       already retained-grade.
     - effective_status in a retained-grade bucket requires audit_status =
       audited_clean AND every dep's effective_status is retained-grade or a
       supplied axiom or approved primitive. Open obligations never satisfy
       the chain.
     - effective_status = retained_no_go requires claim_type = no_go,
       audit_status = audited_clean, and a current valid No-Go Discipline
       packet. Archived failures remain non-authoritative history.
     - independence = 'weak' cannot land audited_clean. Critical clean
       confirmations must be cross-family, strong/external, or same-family
       fresh_context from a distinct restricted-input session.
     - note_hash on row must equal current note hash on disk.
     - a registered derivation obligation must agree with the source note it
       registers (exact target, declared governance source, both sections
       present) and its ledger row must be typed open_gate. Divergence is
       reported, never repaired: which surface is right is not a mechanical
       call. Closure-condition grounding is a lexical comparison and is
       advisory only.

  3. Graph health:
     - No dangling deps.
     - Cycles reported (notice, not failure).
     - Orphaned ledger rows (no source note) reported.

Exit code 0 if clean, 1 if any error-level issue found. Lint warnings are
reserved for mechanically actionable metadata problems. Audit-backlog items
that require a real re-audit are reported as notices so strict lint stays
useful without implying those rows can be mechanically repaired.
"""
from __future__ import annotations

import hashlib
import json
import posixpath
import re
import sys
from collections import defaultdict
from fnmatch import fnmatchcase
from pathlib import Path
from urllib.parse import unquote, urlsplit

import premise_nodes
import ledger_io
import no_go_discipline_gate
import audit_contract
import runner_pin_gate

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = REPO_ROOT / "docs" / "audit" / "data"
LEDGER_PATH = DATA_DIR / "audit_ledger.json"
GRAPH_PATH = DATA_DIR / "citation_graph.json"
AUDIT_DISPATCH_QUEUE_PATH = DATA_DIR / "audit_dispatch_queue.json"
RETIRED_ADMISSIONS_PATH = DATA_DIR / "tier_a_admissions.json"
RETIRED_OWNER_GOVERNANCE_PATH = DATA_DIR / "owner_governed_premise_nodes.json"
DERIVATION_OBLIGATIONS_PATH = DATA_DIR / "derivation_obligations.json"
# Beside the scripts, not in DATA_DIR: docs/audit/data/ is restored wholesale
# from the branch merge-base before a science PR is committed, so a baseline
# there would have every drain silently reverted.
OBLIGATION_RECONCILIATION_BASELINE_PATH = (
    REPO_ROOT
    / "docs"
    / "audit"
    / "scripts"
    / "derivation_obligation_reconciliation_baseline.txt"
)

ALLOWED_AUDIT_STATUSES = {
    "unaudited",
    "audit_in_progress",
    "audited_clean",
    "audited_renaming",
    "audited_conditional",
    "audited_decoration",
    "audited_failed",
    "audited_numerical_match",
}
ALLOWED_CLAIM_TYPES = {
    "positive_theorem",
    "bounded_theorem",
    "no_go",
    "open_gate",
    "decoration",
    "meta",
    None,
}
RETAINED_GRADES = {"retained", "retained_no_go", "retained_bounded"}
AUDIT_TUPLE_AGREEMENT_SCHEMA = "audit_tuple_v2"


def normalized_claim_scope(audit_like: dict) -> str:
    """Normalize insignificant whitespace without weakening scoped agreement."""
    scope = audit_like.get("claim_scope")
    if not isinstance(scope, str):
        return ""
    return " ".join(scope.split())


def normalized_negative_assertion_classes(audit_like: dict) -> tuple[str, ...]:
    """Return the declared negative-assertion classes as a stable tuple."""
    declared = audit_like.get("negative_assertion_classes")
    if not isinstance(declared, list):
        return ()
    return tuple(sorted({item for item in declared if isinstance(item, str)}))


def audit_summary_tuples_match(first: dict, second: dict) -> bool:
    """Mirror apply_audit's full cross-confirmation agreement tuple."""
    if not isinstance(first, dict) or not isinstance(second, dict):
        return False
    return (
        first.get("verdict") == second.get("verdict")
        and first.get("claim_type") == second.get("claim_type")
        and normalized_claim_scope(first) == normalized_claim_scope(second)
        and first.get("load_bearing_step_class")
        == second.get("load_bearing_step_class")
        and normalized_negative_assertion_classes(first)
        == normalized_negative_assertion_classes(second)
        and audit_contract.decoration_parent_tuple_key(
            first.get("verdict"), first.get("decoration_parent_claim_id")
        )
        == audit_contract.decoration_parent_tuple_key(
            second.get("verdict"), second.get("decoration_parent_claim_id")
        )
    )


def live_row_audit_tuple(row: dict) -> dict:
    """Project the authoritative live row onto the v2 agreement tuple."""
    return {
        "verdict": row.get("audit_status"),
        "claim_type": row.get("claim_type"),
        "claim_scope": row.get("claim_scope"),
        "load_bearing_step_class": row.get("load_bearing_step_class"),
        "negative_assertion_classes": row.get("negative_assertion_classes"),
        "decoration_parent_claim_id": row.get("decoration_parent_claim_id"),
    }


def audit_summary_tuple_schema_error(summary: object) -> str | None:
    """Require a complete, typed v2 agreement tuple before comparison."""
    if not isinstance(summary, dict) or not summary:
        return "audit summary must be a non-empty object"
    required = {
        "verdict",
        "claim_type",
        "claim_scope",
        "load_bearing_step_class",
        "negative_assertion_classes",
    }
    missing = required - set(summary)
    if missing:
        return f"audit summary missing tuple fields: {sorted(missing)}"
    verdict = summary.get("verdict")
    if not isinstance(verdict, str) or verdict not in ALLOWED_AUDIT_STATUSES or verdict in {
        "unaudited", "audit_in_progress"
    }:
        return f"audit summary has non-terminal verdict {verdict!r}"
    claim_type = summary.get("claim_type")
    if (
        not isinstance(claim_type, str)
        or claim_type not in ALLOWED_CLAIM_TYPES
    ):
        return f"audit summary has invalid claim_type {claim_type!r}"
    tuple_error = audit_contract.verdict_claim_type_error(
        verdict,
        claim_type,
        summary.get("decoration_parent_claim_id"),
    )
    if tuple_error:
        return f"audit summary has incompatible verdict/claim_type: {tuple_error}"
    scope = summary.get("claim_scope")
    if not isinstance(scope, str) or not scope.strip():
        return "audit summary claim_scope must be a non-empty string"
    step_class = summary.get("load_bearing_step_class")
    if not isinstance(step_class, str) or not step_class.strip():
        return "audit summary load_bearing_step_class must be a non-empty string"
    declared = summary.get("negative_assertion_classes")
    if not isinstance(declared, list) or not all(
        isinstance(item, str) for item in declared
    ):
        return "audit summary negative_assertion_classes must be a list of strings"
    unknown = sorted(set(declared) - no_go_discipline_gate.POLICY_NEGATIVE_CLASSES)
    if unknown:
        return f"audit summary has unknown negative_assertion_classes: {unknown}"
    return None


def is_retained_grade(status):
    """Mirror compute_effective_status.is_retained_grade: literal retained-grade
    keywords plus `decoration_under_<parent>` (which is only assigned when the
    parent is itself retained-grade)."""
    if status in RETAINED_GRADES:
        return True
    if isinstance(status, str) and status.startswith("decoration_under_"):
        return True
    return False


def is_chain_satisfying_status(status):
    """Mirror compute_effective_status.is_chain_satisfying_status.

    Metadata rows can satisfy theorem/no-go dependency closure as stable audit
    context, but they are not retained-grade theorem support and do not satisfy
    decoration-parent retention.
    """
    return status == "meta" or is_retained_grade(status)


ALLOWED_EFFECTIVE_STATUSES = {
    "retained",
    "retained_no_go",
    "retained_bounded",
    "retained_pending_chain",
    "open_gate",
    "unaudited",
    "audit_in_progress",
    "meta",
    "audited_decoration",
    "audited_numerical_match",
    "audited_renaming",
    "audited_conditional",
    "audited_failed",
}
ALLOWED_INDEPENDENCE = {"weak", "fresh_context", "cross_family", "strong", "external", "judicial_review", None}
DEPRECATED_LEDGER_FIELDS = {"current_status", "current_status_raw"}

# Vocabulary-drift status, orthogonal to audit_status. See
# docs/repo/VOCABULARY_HYGIENE_DESIGN.md and
# docs/repo/controlled_vocabulary.yaml. prose_status records whether the
# source note's vocabulary is compliant; it does NOT factor into
# effective_status (physics ≠ prose orthogonality invariant).
ALLOWED_PROSE_STATUS = {
    "clean",
    "auto_corrected",
    "needs_human_vocab_decision",
    "not_evaluated_pre_vocab_lint",
    "queue_backpressure_exceeded",
    None,  # legacy rows pre-Cleanup-1 backfill
}

# Repair classes that audited_conditional / audited_renaming rows must prefix
# in notes_for_re_audit_if_any (per docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md).
ALLOWED_REPAIR_CLASSES = {
    "missing_dependency_edge",
    "dependency_not_retained",
    "missing_bridge_theorem",
    "scope_too_broad",
    "runner_artifact_issue",
    "compute_required",
    "other",
}

# Boilerplate scope written by seed_audit_ledger.backfill_scope when the
# auditor never supplied a real scope. Terminal verdicts must replace this
# with a real claim_scope; the lint flags rows that still carry it.
BACKFILL_SCOPE_PREFIX = (
    "Legacy audit row backfilled during scope-aware classification migration"
)

# Canonical auditor families. Anything outside this set is a lint warning;
# legacy strings (codex-current, codex-fresh, codex-fresh-agent, codex-fresh-context)
# are accepted as known-legacy and produce a migration warning rather than a hard
# error so the queue stays open while a one-time migration script normalises them.
CANONICAL_AUDITOR_FAMILIES = {
    # Codex GPT models (current and future): codex-gpt-<version>
    "codex-gpt-5",
    "codex-gpt-5.5",
    "codex-gpt-5.6",
    "codex-gpt-5.7",
    "codex-gpt-6",
    # Other model families
    "claude-opus",
    "claude-sonnet",
    "human",
    "external",
    # Legacy archival summary rows produced by apply_audit's
    # legacy_clean_consensus_summary (collapsed pre-PR291 cross-confirmations).
    "legacy-confirmed-clean",
}
LEGACY_AUDITOR_FAMILIES = {
    "codex-current",
    "codex-fresh",
    "codex-fresh-agent",
    "codex-fresh-context",
}

# audit_status values that are terminal verdicts (not pending/in-progress).
TERMINAL_VERDICTS = {
    "audited_clean",
    "audited_renaming",
    "audited_conditional",
    "audited_decoration",
    "audited_failed",
    "audited_numerical_match",
}

SUPPORTED_DISPATCH_SCHEMAS = {"promotion_reaudit_queue.v1"}

_CODEX_FAMILY_RE = re.compile(r"^codex-gpt-(\d+(?:\.\d+)*)$")
_INLINE_MARKDOWN_LINK_RE = re.compile(
    r"(?<!!)\[[^\]\n]*\]\(\s*"
    r"(?P<destination><[^>\n]+>|[^)\s]+)"
    r"(?:\s+(?:\"[^\"\n]*\"|'[^'\n]*'|\([^\)\n]*\)))?\s*\)"
)


def codex_family_meets_minimum(family: str, minimum: str = "gpt-5.5") -> bool:
    """True iff a codex-gpt family label meets the audit-lane model floor."""
    if not isinstance(family, str) or not family.startswith("codex-gpt-"):
        return True
    fam_match = _CODEX_FAMILY_RE.match(family)
    if not fam_match:
        return True
    min_match = re.match(r"gpt-(\d+(?:\.\d+)*)", minimum)
    if not min_match:
        return True
    fam_rank = tuple(int(part) for part in fam_match.group(1).split("."))
    min_rank = tuple(int(part) for part in min_match.group(1).split("."))
    width = max(len(fam_rank), len(min_rank))
    fam_padded = fam_rank + (0,) * (width - len(fam_rank))
    min_padded = min_rank + (0,) * (width - len(min_rank))
    return fam_padded >= min_padded


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def mask_nonrendered_markdown(text: str) -> str:
    """Mask code and comments before extracting rendered Markdown links."""
    masked_lines: list[str] = []
    fence_char: str | None = None
    fence_len = 0
    paragraph_open = False
    indented_code = False
    list_content_indent: int | None = None
    prior_quote_depth = 0
    for line in text.splitlines(keepends=True):
        content = line
        container_offset = 0
        quote_depth = 0
        while True:
            container = re.match(r"[ \t]{0,3}>[ \t]?", content)
            if not container:
                break
            container_offset += container.end()
            quote_depth += 1
            content = content[container.end():]
        if quote_depth != prior_quote_depth:
            # A list item cannot continue across a block-quote boundary. The
            # new container also starts its own paragraph/code-block context.
            list_content_indent = None
            paragraph_open = False
            indented_code = False
        prior_quote_depth = quote_depth
        stripped = content.lstrip(" \t")
        indent = len(content) - len(stripped)
        list_opener = re.match(
            r"(?P<leading>[ ]{0,3})(?P<marker>[*+-]|\d{1,9}[.)])"
            r"(?P<spacing>[ \t]+|(?=\r?$))",
            content,
        )
        list_item_code_on_marker_line = False
        if list_opener:
            spacing = list_opener.group("spacing") or ""
            # CommonMark accepts one to four spaces after a list marker. With
            # five or more, only the first is marker padding and the remaining
            # four spaces start an indented code block inside the item.
            padding = len(spacing) if 1 <= len(spacing) <= 4 else min(len(spacing), 1)
            list_content_indent = (
                len(list_opener.group("leading"))
                + len(list_opener.group("marker"))
                + padding
            )
            list_item_code_on_marker_line = len(spacing) >= 5
        elif stripped.strip() and list_content_indent is not None and indent < list_content_indent:
            list_content_indent = None
        container_indent = (
            indent - list_content_indent
            if list_content_indent is not None and indent >= list_content_indent
            else indent
        )
        if fence_char is not None:
            closing = re.match(
                rf"{re.escape(fence_char)}{{{fence_len},}}[ \t]*(?:\r?\n)?$",
                stripped,
            )
            masked_lines.append("".join("\n" if ch == "\n" else " " for ch in line))
            if container_indent <= 3 and closing:
                fence_char = None
                fence_len = 0
                paragraph_open = False
            continue
        opener = (
            re.match(r"(`{3,}|~{3,})", stripped)
            if container_indent <= 3
            else None
        )
        if opener:
            fence_char = opener.group(1)[0]
            fence_len = len(opener.group(1))
            masked_lines.append("".join("\n" if ch == "\n" else " " for ch in line))
            paragraph_open = False
            indented_code = False
            continue
        if not stripped.strip():
            masked_lines.append(line)
            paragraph_open = False
            indented_code = False
            continue
        if list_item_code_on_marker_line:
            masked_lines.append("".join("\n" if ch == "\n" else " " for ch in line))
            paragraph_open = False
            indented_code = True
            continue
        if container_indent >= 4 and (
            indented_code or not paragraph_open
        ):
            masked_lines.append("".join("\n" if ch == "\n" else " " for ch in line))
            indented_code = True
            continue
        masked_lines.append(line)
        paragraph_open = True
        indented_code = False

    visible = list("".join(masked_lines))
    source = "".join(masked_lines)
    i = 0
    while i < len(source):
        if source.startswith("<!--", i):
            end = source.find("-->", i + 4)
            end = len(source) if end < 0 else end + 3
            for j in range(i, end):
                if visible[j] != "\n":
                    visible[j] = " "
            i = end
            continue
        if source[i] == "`":
            backslashes = 0
            escape_index = i - 1
            while escape_index >= 0 and source[escape_index] == "\\":
                backslashes += 1
                escape_index -= 1
            if backslashes % 2:
                i += 1
                continue
            run_end = i + 1
            while run_end < len(source) and source[run_end] == "`":
                run_end += 1
            delimiter = source[i:run_end]
            close = source.find(delimiter, run_end)
            while close >= 0:
                exact_run = not (
                    (close > 0 and source[close - 1] == "`")
                    or (
                        close + len(delimiter) < len(source)
                        and source[close + len(delimiter)] == "`"
                    )
                )
                # Backslashes have no escaping role inside a CommonMark code
                # span, so an exact matching run closes even after "\\".
                if exact_run:
                    break
                close = source.find(delimiter, close + len(delimiter))
            if close >= 0:
                end = close + len(delimiter)
                for j in range(i, end):
                    if visible[j] != "\n":
                        visible[j] = " "
                i = end
                continue
            i = run_end
            continue
        i += 1
    return "".join(visible)


def markdown_link_targets(surface: str, text: str) -> set[str]:
    """Return normalized repo-relative targets of inline Markdown links.

    Plain prose and code spans intentionally do not count: front-door axiom
    currency is a navigation guarantee, so only an actual Markdown link can
    satisfy it. Fragments and query strings do not affect target identity.
    """
    surface_parent = Path(surface).parent.as_posix()
    targets: set[str] = set()
    rendered_text = mask_nonrendered_markdown(text)
    for match in _INLINE_MARKDOWN_LINK_RE.finditer(rendered_text):
        backslashes = 0
        escape_index = match.start() - 1
        while escape_index >= 0 and rendered_text[escape_index] == "\\":
            backslashes += 1
            escape_index -= 1
        if backslashes % 2:
            continue
        destination = match.group("destination")
        if destination.startswith("<") and destination.endswith(">"):
            destination = destination[1:-1]
        parsed = urlsplit(destination)
        if parsed.scheme or parsed.netloc or destination.startswith(("#", "/")):
            continue
        path = unquote(parsed.path)
        if not path:
            continue
        targets.add(posixpath.normpath(posixpath.join(surface_parent, path)))
    return targets


def front_door_axiom_pointer_errors(
    surface: str,
    text: str,
    current_path: str | None,
    superseded: list[str],
) -> list[str]:
    targets = markdown_link_targets(surface, text)
    errors: list[str] = []
    if current_path and current_path not in targets:
        errors.append(
            "[front_door_axiom_pointer] "
            f"{surface}: does not cite the current axiom memo {current_path}"
        )
    for old in superseded:
        if old in targets:
            errors.append(
                "[front_door_axiom_pointer] "
                f"{surface}: cites superseded axiom memo {old} "
                f"(current: {current_path})"
            )
    return errors


def obligation_text_normalize(text: object) -> str:
    """Registry/note text comparison form: backticks and whitespace dropped."""
    if not isinstance(text, str):
        return ""
    return re.sub(r"\s+", " ", text.replace("`", "")).strip()


def markdown_sections(text: str) -> dict[str, str]:
    """Map each `## Heading` in a source note to its body text.

    Fenced code blocks are skipped rather than scanned: a ``## ...`` line inside
    a fence is sample text, not a section. Without that, a fenced ``## Exact
    target`` silently replaces the real section body and the reconciliation
    below reports a target divergence that does not exist. A repeated heading
    keeps its FIRST body for the same reason -- the later occurrence must not
    be able to displace the section the note actually opened with.

    Because every finding downstream of this parse can be a hard error, the
    fence and heading rules follow CommonMark rather than approximating it: a
    fence closes only on the same character, at least as long as the opener and
    with nothing after it (so ```` ```python ```` inside a block is content, not
    a closer), a backtick opener may not carry a backtick in its info string, an
    ATX heading may be indented up to three spaces and closed by a trailing run
    of ``#`` (``## Exact target ##`` names the section ``Exact target``), an
    indented heading inside an open list item belongs to that item and is not a
    section, and fenced lines are blanked rather than folded into the enclosing
    section -- a fence may interrupt a paragraph with no blank line, and the
    target comparison reads a section's opening paragraph. Getting any of those
    wrong turns valid Markdown into a missing-section or target-mismatch error.
    """
    sections: dict[str, list[str]] = {}
    order: list[str] = []
    current: str | None = None
    fence_char: str | None = None
    fence_len = 0
    list_open = False
    for line in text.splitlines():
        fence_match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        delimiter = False
        if fence_match:
            run, rest = fence_match.group(1), fence_match.group(2)
            char = run[0]
            if fence_char is None:
                if not (char == "`" and "`" in rest):
                    fence_char, fence_len = char, len(run)
                    delimiter = True
            elif char == fence_char and len(run) >= fence_len and not rest.strip():
                fence_char, fence_len = None, 0
                delimiter = True
        if delimiter or fence_char is not None:
            # Fenced content is sample text: it neither opens a section nor
            # belongs to one. This matters because a fence may interrupt a
            # paragraph with no blank line, and the target comparison reads the
            # section's opening paragraph. Each fenced line becomes a blank so
            # the content is gone but the paragraph break the fence created
            # survives -- dropping the lines outright would splice the
            # paragraphs on either side of the fence into one.
            if current is not None:
                sections[current].append("")
            continue
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        is_marker = bool(
            stripped
            and indent <= 3
            and re.match(r"^([-*+]|\d{1,9}[.)])(\s|$)", stripped)
        )
        heading = re.match(r"^ {0,3}##(?!#)\s+(.*?)(?:\s+#+)?\s*$", line)
        # An indented heading inside an open list item is a heading of that
        # item, not a section of the note. Accepting it would let
        # ``- item`` / ``  ## Exact target`` claim the name first and leave the
        # real top-level heading ignored as a repeat -- a false hard
        # target_mismatch. Only an unindented heading can open a section while a
        # list is open. The list state is read before it is updated, so the
        # marker line itself does not close the list it opens.
        if heading and heading.group(1).strip() and not (indent and list_open):
            list_open = False
            current = heading.group(1).strip()
            if current not in sections:
                sections[current] = []
                order.append(current)
            else:
                # Repeated heading: keep the first body, ignore the rest.
                current = None
            continue
        if is_marker:
            list_open = True
        elif stripped and indent == 0:
            list_open = False
        if current is not None:
            sections[current].append(line)
    return {name: "\n".join(sections[name]).strip() for name in order}


# Comparison stopwords for obligation grounding. Deliberately small, fixed and
# purely grammatical: the check is comparative (which section of the note is a
# registry sentence drawn from), so the list only has to stop function words
# from swamping the signal. It carries no framework vocabulary.
OBLIGATION_STOPWORDS = frozenset(
    """a an and any are as at be been both but by each every for from have if in
    into is it its must no not of on one or other per rather shall so such than
    that the their then there these this those to until use used uses was when
    which while with without all""".split()
)


def obligation_content_words(text: object) -> set[str]:
    stripped = re.sub(r"[^a-z0-9/_^|.-]+", " ", obligation_text_normalize(text).lower())
    return {
        word
        for word in (token.strip(".") for token in stripped.split())
        if len(word) >= 3 and word not in OBLIGATION_STOPWORDS
    }


OBLIGATION_RECONCILIATION_KINDS = frozenset(
    {
        "exact_target_section_missing",
        "target_mismatch",
        "closure_criterion_section_missing",
        "self_liquidation_condition_missing",
        "closure_condition_not_grounded",
        "governance_source_not_cited",
        "ledger_row_not_open_gate",
    }
)

# Not grandfatherable. This one is not a wording divergence between two
# records of the same obligation: it is the registry's own preamble promise
# that an obligation "never satisfies dependency closure", carried solely by
# claim_type == open_gate. Allowing a baseline line to suppress it would let a
# retyped-and-cleared obligation launder into a retained-grade premise, which
# is the failure the promise exists to prevent.
OBLIGATION_RECONCILIATION_NON_GRANDFATHERABLE_KINDS = frozenset(
    {"ledger_row_not_open_gate"}
)

# Advisory, never an error, baseline or no baseline. Every other kind is an
# exact mechanical comparison -- a section is present or absent, two normalized
# strings are equal or not, a basename occurs in the note or does not -- so it
# can only fire on a real divergence. Closure grounding is instead a lexical
# content-word comparison with no threshold, and the live margins are one to
# two words (measured: 0.36/0.18, 0.45/0.27, 0.50/0.40). A faithful but
# differently-worded condition on a NEW obligation can lose that comparison, and
# audit_lint is a stop-work gate in run_pipeline.sh and pre_commit_audit_check.sh
# with no honest drain except rewording correct prose to win a word count.
# It is a real and useful diagnostic -- it is what surfaced that all three
# entries paraphrase '## Running-program relation' -- so it is reported every
# run, and arming it needs a structured closure field or a validated threshold,
# not a baseline.
OBLIGATION_RECONCILIATION_ADVISORY_KINDS = frozenset({"closure_condition_not_grounded"})


def obligation_reconciliation_findings(
    dep_id: str,
    entry: dict,
    note_text: str,
) -> list[tuple[str, str]]:
    """Reconcile one derivation-obligation registry entry against its own note.

    Returns ``(kind, message)`` pairs. The registry preamble binds each entry to
    the exact open target stated by its ``current_path`` note, but nothing
    reconciled the two: ``target`` was checked for truthiness only and no rule
    validated ``self_liquidation_condition`` against its note at all (the no-go
    discipline gate reads the field, but only to pick an evidence excerpt), so a
    registry record could state a weaker target or a different closure condition
    than the obligation it registers and no gate would notice.

    No check decides which surface is right. What an obligation demands is
    owner/audit-lane content, so the caller reports and never repairs: today's
    exact-comparison divergences are grandfathered and only a new one errors,
    while ``closure_condition_not_grounded`` -- the one lexical, thresholdless
    comparison here -- is advisory at every run.
    """
    findings: list[tuple[str, str]] = []
    source_path = entry.get("current_path") or "<no current_path>"
    sections = markdown_sections(note_text)

    target_section = sections.get("Exact target")
    if target_section is None:
        findings.append(
            (
                "exact_target_section_missing",
                f"{dep_id}: {source_path} has no '## Exact target' section, so the "
                "registry target cannot be reconciled with the obligation it registers",
            )
        )
    else:
        registry_target = obligation_text_normalize(entry.get("target"))
        note_target = obligation_text_normalize(target_section.split("\n\n")[0])
        if registry_target != note_target:
            findings.append(
                (
                    "target_mismatch",
                    f"{dep_id}: registry target does not match '## Exact target' in "
                    f"{source_path}.\n        registry: {registry_target}\n"
                    f"        note:     {note_target}",
                )
            )

    closure_section = sections.get("Closure criterion")
    if closure_section is None:
        findings.append(
            (
                "closure_criterion_section_missing",
                f"{dep_id}: {source_path} has no '## Closure criterion' section, so "
                "self_liquidation_condition has nothing to be grounded in",
            )
        )
    condition = obligation_text_normalize(entry.get("self_liquidation_condition"))
    if not condition:
        findings.append(
            (
                "self_liquidation_condition_missing",
                f"{dep_id}: registry entry has no self_liquidation_condition, so the "
                "registry records nothing about what would close the obligation",
            )
        )
    elif closure_section is not None:
        condition_words = obligation_content_words(condition)
        if condition_words:
            def grounding(body: str) -> float:
                shared = condition_words & obligation_content_words(body)
                return len(shared) / len(condition_words)

            closure_grounding = grounding(closure_section)
            better = sorted(
                (
                    (grounding(body), name)
                    for name, body in sections.items()
                    if name != "Closure criterion" and grounding(body) > closure_grounding
                ),
                reverse=True,
            )
            if better:
                score, name = better[0]
                findings.append(
                    (
                        "closure_condition_not_grounded",
                        f"{dep_id}: self_liquidation_condition is drawn from "
                        f"'## {name}' rather than '## Closure criterion' in {source_path} "
                        f"(content-word grounding {score:.2f} vs {closure_grounding:.2f}); "
                        "the registry therefore records a different closure condition "
                        "than the obligation states",
                    )
                )

    governance_source = entry.get("historical_governance_source")
    if governance_source and posixpath.basename(str(governance_source)) not in note_text:
        findings.append(
            (
                "governance_source_not_cited",
                f"{dep_id}: registry asserts historical_governance_source "
                f"{governance_source} but {source_path} never cites it",
            )
        )

    return findings


def obligation_row_typing_findings(
    dep_id: str, row: dict | None
) -> list[tuple[str, str]]:
    """Registry membership implies ``claim_type == open_gate`` on the ledger row.

    The registry preamble promises these entries "never satisfy dependency
    closure, never bound or promote downstream rows". That invariant is carried
    solely by ``compute_effective_status.clean_status`` returning ``open_gate``
    for ``claim_type == open_gate``: retype the row to ``bounded_theorem`` and
    audit it clean and ``CLAIM_TYPE_TO_RETAINED`` yields ``retained_bounded``,
    which ``is_chain_satisfying_status`` accepts -- an open obligation laundered
    into a premise. ``meta`` is the same hole one step shorter, because
    ``is_chain_satisfying_status`` accepts ``meta`` directly. Requiring exactly
    ``open_gate`` closes both. Nothing checked the typing.

    Kept out of ``obligation_reconciliation_findings`` deliberately: this is a
    row-only invariant and must not inherit that function's precondition that
    the note file exists on disk.
    """
    if row is None or row.get("claim_type") == "open_gate":
        return []
    return [
        (
            "ledger_row_not_open_gate",
            f"{dep_id}: registered derivation obligation has ledger "
            f"claim_type={row.get('claim_type')!r}, but only 'open_gate' keeps the "
            "registry's promise that an obligation never satisfies dependency "
            "closure; report the typing to the audit lane rather than editing "
            "the row",
        )
    ]


def hash_note_on_disk(note_path_str: str) -> str | None:
    p = REPO_ROOT / note_path_str
    if not p.exists():
        return None
    return hashlib.sha256(p.read_text(encoding="utf-8", errors="replace").encode("utf-8")).hexdigest()


def dispatch_sidecars() -> list[Path]:
    """Machine-readable dispatcher manifests that must feed audit_dispatch_queue."""
    candidates: list[Path] = []
    for pattern in ("*reaudit_queue*.json", "*dispatch_queue*.json"):
        candidates.extend(DATA_DIR.glob(pattern))
    excluded = {"audit_dispatch_queue.json", "audit_queue.json", "reaudit_candidates.json"}
    return sorted({p for p in candidates if p.name not in excluded})


def dispatch_target_live(target: dict, rows: dict[str, dict]) -> bool:
    row = rows.get(target.get("claim_id"))
    if row is None:
        return False
    expected = {
        "claim_type": target.get("current_claim_type"),
        "audit_status": target.get("current_audit_status"),
        "effective_status": target.get("current_effective_status"),
    }
    return all(expected[k] in {None, row.get(k)} for k in expected)


def main() -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--strict", action="store_true", help="Accepted for compatibility; lint is strict by default.")
    args, _ = p.parse_known_args()

    ledger_io.ensure_cache()
    if not LEDGER_PATH.exists():
        print("FAIL: audit_ledger.json missing", file=sys.stderr)
        return 1
    ledger = load_json(LEDGER_PATH)
    graph = load_json(GRAPH_PATH) if GRAPH_PATH.exists() else None
    rows = ledger.get("rows", {})

    errors: list[str] = []
    warnings: dict[str, list[str]] = defaultdict(list)
    notices: dict[str, list[str]] = defaultdict(list)

    def add_warning(category: str, message: str) -> None:
        warnings[category].append(message)

    def add_notice(category: str, message: str) -> None:
        notices[category].append(message)

    def check_no_go_packet(
        *,
        cid: str,
        label: str,
        audit_like: dict,
        row: dict,
        source_required: bool,
    ) -> None:
        verdict = audit_like.get("verdict") or audit_like.get("audit_status")
        if verdict in {None, "unaudited"}:
            return
        packet = audit_like.get("no_go_discipline")
        forensic_tier = bool(
            source_required
            or audit_like.get("claim_type") == "no_go"
            or row.get("claim_type") == "no_go"
            or no_go_discipline_gate.forensic_mode()
        )
        required = source_required or no_go_discipline_gate.output_requires_no_go_discipline(
            audit_like
        ) or bool(audit_like.get("negative_assertion_classes"))
        binds = no_go_discipline_gate.packet_requirement_binds(
            {**audit_like, "verdict": verdict},
            source_required=source_required,
        )
        if required and binds and packet is None:
            message = (
                f"{cid}: {label} lacks structured No-Go Discipline and "
                "cannot be authoritative until fresh re-audit"
            )
            if label == "live audit" and verdict == "audited_clean":
                errors.append(message)
            else:
                add_notice("legacy_no_go_packet_absent", message)
            return
        if packet is None:
            return

        def report_invalid(detail: str) -> None:
            message = f"{cid}: {label} invalid no_go_discipline packet: {detail}"
            if verdict == "audited_clean":
                errors.append(message)
            else:
                add_notice("non_authoritative_invalid_no_go_packet", message)

        normalized = {
            **audit_like,
            "verdict": verdict,
            "chain_closes": audit_like.get(
                "chain_closes", verdict == "audited_clean"
            ),
        }
        evidence_manifest = None
        if forensic_tier:
            evidence_manifest = no_go_discipline_gate.evidence_manifest_from_snapshot(
                packet
            )
            current_manifest = no_go_discipline_gate.build_evidence_manifest(
                row, rows, REPO_ROOT
            )
            if evidence_manifest is None:
                report_invalid("authenticated evidence_snapshot is required")
                return
            snapshot_error = no_go_discipline_gate.evidence_snapshot_current_error(
                packet, current_manifest
            )
            if snapshot_error:
                report_invalid(snapshot_error)
                return
        error = no_go_discipline_gate.validate_no_go_discipline(
            normalized,
            source_required=source_required,
            evidence_manifest=evidence_manifest,
            structural_only=not forensic_tier,
        )
        if error:
            report_invalid(error)

    def _load_pattern_file(name: str) -> tuple[str, ...]:
        path = DATA_DIR / name
        if not path.exists():
            return ()
        return tuple(
            line.strip()
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")
        )

    # Typing-policy surfaces (see seed_audit_ledger.default_claim_type_for):
    # rows still under the silent positive_theorem default are warned below,
    # and rows grandfathered under excluded source patterns are noticed so
    # the exclusion-registry / ledger divergence stays visible.
    excluded_source_patterns = _load_pattern_file("excluded_source_patterns.txt")
    never_gate_source_paths = frozenset(_load_pattern_file("never_gate_source_paths.txt"))

    if RETIRED_ADMISSIONS_PATH.exists():
        errors.append(
            "tier_a_admissions.json must not exist; the only supplied premise "
            "registry is axiom_premise_nodes.json"
        )
    if RETIRED_OWNER_GOVERNANCE_PATH.exists():
        errors.append(
            "owner_governed_premise_nodes.json must not exist; the only "
            "supplied premise registry is axiom_premise_nodes.json"
        )

    if DERIVATION_OBLIGATIONS_PATH.exists():
        try:
            obligations = load_json(DERIVATION_OBLIGATIONS_PATH)
        except Exception as exc:
            errors.append(f"derivation_obligations.json could not be parsed: {exc}")
            obligations = {}
        nodes = obligations.get("nodes") or {}
        listed_ids = set(obligations.get("canonical_ids") or [])
        if listed_ids != set(nodes):
            errors.append(
                "derivation_obligations.json canonical_ids must equal nodes"
            )
        overlap = listed_ids & premise_nodes.accepted_premise_ids()
        if overlap:
            errors.append(
                "derivation_obligations.json overlaps the axiom/primitive foundation: "
                + ", ".join(sorted(overlap))
            )
        # Registry <-> source-note reconciliation.
        #
        # The registry entry and the note it registers are two records of the
        # same obligation, and nothing reconciled them: `target` was checked for
        # truthiness only, no rule validated `self_liquidation_condition`
        # against its note, and the source note was never opened. A registry
        # that states a weaker target, or a closure condition copied from a
        # different section of the note, is invisible to the audit lane
        # because no ledger row hashes docs/audit/data/.
        #
        # This is a ratchet, not a rewrite. What an obligation demands is
        # owner/audit-lane content, so a divergence is never repaired here and
        # never picked a side on: today's exact-comparison population is
        # grandfathered verbatim in
        # derivation_obligation_reconciliation_baseline.txt and reported as a
        # drainable notice, and only a NEW divergence is an error. Draining an
        # entry is the owner's adjudication of which surface was right.
        # Shrink-only is a reviewed convention, not a mechanical guarantee:
        # nothing here can tell a drained line from a newly added suppression,
        # so growth of this file is a review question. That is why only exact
        # mechanical comparisons are error-eligible at all
        # (OBLIGATION_RECONCILIATION_ADVISORY_KINDS carries the lexical one,
        # which is never suppressed and never an error).
        # The baseline lives beside the scripts rather than in
        # docs/audit/data/ because that directory is restored wholesale from
        # origin/main before a science PR lands, which would silently revert
        # every drain.
        reconciliation_baseline: set[str] = set()
        if OBLIGATION_RECONCILIATION_BASELINE_PATH.exists():
            reconciliation_baseline = {
                line.strip()
                for line in OBLIGATION_RECONCILIATION_BASELINE_PATH.read_text(
                    encoding="utf-8"
                ).splitlines()
                if line.strip() and not line.strip().startswith("#")
            }
        live_reconciliation_keys: set[str] = set()

        for dep_id, entry in sorted(nodes.items()):
            if dep_id not in rows:
                errors.append(f"derivation obligation {dep_id!r} has no ledger row")
            if premise_nodes.is_accepted_premise_dep(dep_id):
                errors.append(f"derivation obligation {dep_id!r} is incorrectly accepted")
            if not entry.get("target"):
                errors.append(f"derivation obligation {dep_id!r} lacks target")
            source_path = entry.get("current_path")
            obligation_findings: list[tuple[str, str]] = []
            if not source_path:
                errors.append(f"derivation obligation {dep_id!r} lacks current_path")
            elif not (REPO_ROOT / source_path).exists():
                errors.append(
                    f"derivation obligation {dep_id!r} current_path missing on disk: "
                    f"{source_path}"
                )
            else:
                note_text = (REPO_ROOT / source_path).read_text(
                    encoding="utf-8", errors="replace"
                )
                obligation_findings = obligation_reconciliation_findings(
                    dep_id, entry, note_text
                )
            # Row-only invariant: runs whether or not the note is on disk.
            obligation_findings += obligation_row_typing_findings(
                dep_id, rows.get(dep_id)
            )
            for kind, message in obligation_findings:
                key = f"{dep_id}:{kind}"
                live_reconciliation_keys.add(key)
                if kind in OBLIGATION_RECONCILIATION_NON_GRANDFATHERABLE_KINDS:
                    errors.append(
                        f"[derivation_obligation_registry_note_divergence] {message}"
                    )
                elif kind in OBLIGATION_RECONCILIATION_ADVISORY_KINDS:
                    add_notice(
                        "derivation_obligation_registry_note_divergence_advisory",
                        f"{message} [advisory: lexical content-word comparison, "
                        "reported every run and never an error]",
                    )
                elif key in reconciliation_baseline:
                    add_notice(
                        "derivation_obligation_registry_note_divergence",
                        f"{message} [grandfathered as {key} in "
                        "derivation_obligation_reconciliation_baseline.txt; "
                        "drain by owner adjudication of which surface is right]",
                    )
                else:
                    errors.append(
                        f"[derivation_obligation_registry_note_divergence] {message}"
                    )

        for stale in sorted(reconciliation_baseline - live_reconciliation_keys):
            add_notice(
                "derivation_obligation_registry_note_divergence_baseline_stale",
                f"{stale}: listed in derivation_obligation_reconciliation_baseline.txt "
                "but the divergence no longer reproduces; prune the baseline entry",
            )

    for cid, row in rows.items():
        if row.get("claim_type") == "meta":
            continue
        for dep_id in row.get("deps") or []:
            if premise_nodes.is_non_evidence_context_dep(dep_id):
                errors.append(
                    f"{cid}: scientific row depends on non-evidence context "
                    f"{dep_id!r}; cite the actual derivation/obligation instead"
                )

    # Front-door axiom-pointer currency. The ledger side of an axiom change
    # is guarded by the premise hash; the narrative front door is not in the
    # citation graph, so without this check it silently drifts (the 2026-06-29
    # reset left the root README on the superseded memo for five days). Every
    # surface listed in data/front_door_surfaces.txt must cite the registry's
    # current minimal_axioms path and must not cite a superseded alias.
    # Error-level: every registered front door is current, so strict lint must
    # fail closed if a later axiom reset leaves one behind.
    front_door_surfaces = _load_pattern_file("front_door_surfaces.txt")
    axiom_registry_path = DATA_DIR / "axiom_premise_nodes.json"
    if front_door_surfaces and axiom_registry_path.exists():
        registry = load_json(axiom_registry_path)
        minimal = (registry.get("nodes") or {}).get("minimal_axioms") or {}
        current_path = minimal.get("current_path")
        superseded = [
            p for p in (minimal.get("aliased_paths") or []) if p != current_path
        ]
        for surface in front_door_surfaces:
            spath = REPO_ROOT / surface
            if not spath.exists():
                errors.append(
                    "[front_door_axiom_pointer] "
                    f"{surface}: listed in front_door_surfaces.txt but missing on disk"
                )
                continue
            text = spath.read_text(encoding="utf-8", errors="replace")
            errors.extend(
                front_door_axiom_pointer_errors(
                    surface, text, current_path, superseded
                )
            )

    # Top-level stale timestamp keys cause PR drift-gate noise and were
    # removed by f383ded3d. compute_effective_status now drops them
    # defensively on every run; this lint check guards against regression.
    STALE_TIMESTAMP_KEYS = {
        "generated_at",
        "effective_status_computed_at",
        "invalidation_run_at",
        "load_bearing_computed_at",
    }
    for k in STALE_TIMESTAMP_KEYS & set(ledger):
        errors.append(
            f"audit_ledger.json top-level: stale timestamp key {k!r} present "
            "(should be removed by compute_effective_status; rerun the pipeline)"
        )

    # Schema and hard-rule checks.
    for cid, row in rows.items():
        a = row.get("audit_status")
        e = row.get("effective_status")
        ct = row.get("claim_type")
        ind = row.get("independence")

        note_body = ""
        note_path = row.get("note_path") or ""
        if note_path:
            try:
                note_body = (REPO_ROOT / note_path).read_text(
                    encoding="utf-8", errors="replace"
                )
            except OSError:
                pass
        source_requires_no_go = no_go_discipline_gate.source_requires_no_go_discipline(
            note_path, note_body, row.get("claim_type")
        )
        check_no_go_packet(
            cid=cid,
            label="live audit",
            audit_like={**row, "verdict": row.get("audit_status")},
            row=row,
            source_required=source_requires_no_go,
        )
        cross = row.get("cross_confirmation") or {}
        if isinstance(cross, dict):
            for audit_key in ("first_audit", "second_audit", "third_audit"):
                summary = cross.get(audit_key)
                if isinstance(summary, dict) and summary:
                    check_no_go_packet(
                        cid=cid,
                        label=f"cross_confirmation.{audit_key}",
                        audit_like=summary,
                        row=row,
                        source_required=source_requires_no_go,
                    )
        for index, archived in enumerate(row.get("previous_audits") or []):
            if not isinstance(archived, dict) or archived.get("no_go_discipline") is None:
                continue
            archived_verdict = archived.get("verdict") or archived.get("audit_status")
            archived_blob = {
                **archived,
                "verdict": archived_verdict,
                "chain_closes": archived.get(
                    "chain_closes", archived_verdict == "audited_clean"
                ),
            }
            # Historical source text is not archived, so validate the complete
            # structure and controlled enums without pretending current note
            # bytes can authenticate an old locator. Restoration performs the
            # stronger current-packet locator check before making it live.
            archived_error = no_go_discipline_gate.validate_no_go_discipline(
                archived_blob,
                evidence_manifest=None,
                structural_only=True,
            )
            if archived_error:
                message = (
                    f"{cid}: previous_audits[{index}] invalid no_go_discipline "
                    f"packet: {archived_error}"
                )
                # Archived packets are non-authoritative history. Schema
                # evolution may make them invalid under the current live gate;
                # restoration revalidates against current evidence before any
                # archived audit can become live again.
                add_notice("archived_invalid_no_go_packet", message)

        for field in DEPRECATED_LEDGER_FIELDS & set(row):
            errors.append(f"{cid}: deprecated ledger field {field!r} must not be present")
        if a not in ALLOWED_AUDIT_STATUSES:
            errors.append(f"{cid}: audit_status={a!r} not in allowed set")
        if ct not in ALLOWED_CLAIM_TYPES:
            errors.append(f"{cid}: claim_type={ct!r} not in allowed set")
        if e not in ALLOWED_EFFECTIVE_STATUSES and not (isinstance(e, str) and e.startswith("decoration_under_")):
            errors.append(f"{cid}: effective_status={e!r} not in allowed set")
        if a not in {None, "unaudited", "audit_in_progress"}:
            if ct is None:
                errors.append(f"{cid}: audited row requires claim_type")
            if not row.get("claim_scope"):
                errors.append(f"{cid}: audited row requires claim_scope")
            scope = row.get("claim_scope") or ""
            if scope.startswith(BACKFILL_SCOPE_PREFIX):
                add_notice(
                    "legacy_backfill_scope",
                    f"{cid}: terminal verdict {a!r} carries seeder backfill scope; "
                    "re-audit required to record a real claim_scope"
                )
        if row.get("claim_type_provenance") == "backfilled_pending_reaudit":
            add_notice(
                "legacy_claim_type_backfill",
                f"{cid}: claim_type was backfilled for a critical legacy audit; queue for re-audit"
            )
        if row.get("claim_type_provenance") == "default_positive_theorem":
            add_warning(
                "claim_type_defaulted",
                f"{cid}: claim_type silently defaulted to positive_theorem; add an "
                f"explicit 'Type:' header to {row.get('note_path')}, or register the "
                "path in docs/audit/data/meta_source_patterns.txt (catalog/index) or "
                "docs/audit/data/excluded_source_patterns.txt (non-claim infra)"
            )
        row_note_path = row.get("note_path") or ""
        if (
            excluded_source_patterns
            and row_note_path
            and row_note_path not in never_gate_source_paths
            and any(fnmatchcase(row_note_path, pat) for pat in excluded_source_patterns)
        ):
            row_has_audit_history = (
                row.get("audit_status") not in (None, "unaudited")
            ) or bool(row.get("previous_audits"))
            if row_has_audit_history:
                add_notice(
                    "excluded_path_row_grandfathered",
                    f"{cid}: {row_note_path} matches data/excluded_source_patterns.txt "
                    "but carries audit history, so history-preserving exclusion keeps "
                    "it (should_gate_node); retiring it is an owner/audit-lane decision"
                )
            else:
                add_notice(
                    "excluded_path_row_pending_drop",
                    f"{cid}: {row_note_path} matches data/excluded_source_patterns.txt "
                    "with no audit history; the next seeding run drops the row and "
                    "strips its inbound dep edges"
                )
        if ind not in ALLOWED_INDEPENDENCE:
            errors.append(f"{cid}: independence={ind!r} not in allowed set")

        # Vocabulary-drift status (orthogonal to audit_status). Pre-Cleanup-1
        # rows may lack the field entirely; backfill_prose_status.py sets
        # them to not_evaluated_pre_vocab_lint. After backfill, every row
        # carries a value.
        if "prose_status" in row:
            ps = row["prose_status"]
            if ps not in ALLOWED_PROSE_STATUS:
                errors.append(
                    f"{cid}: prose_status={ps!r} not in {sorted(s for s in ALLOWED_PROSE_STATUS if s is not None)}"
                )
            pc = row.get("prose_corrections")
            if pc is not None and not isinstance(pc, list):
                errors.append(
                    f"{cid}: prose_corrections must be a list of "
                    "{rule_id, before, after} dicts (got "
                    f"{type(pc).__name__})"
                )
        else:
            add_notice(
                "prose_status_backfill_pending",
                f"{cid}: prose_status missing; run backfill_prose_status.py"
            )

        # Repair-class enforcement on audited_conditional / audited_renaming
        # rows (per docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md and README.md).
        # These terminal repairable verdicts must prefix
        # notes_for_re_audit_if_any with one of the seven allowed repair
        # classes so the repair lane is machine-sortable. Legacy rows lacking
        # the prefix queue for re-audit.
        if a in ("audited_conditional", "audited_renaming"):
            notes = row.get("notes_for_re_audit_if_any") or ""
            prefix_tokens = notes.strip().split(":", 1)[0].strip().split()
            first_token = prefix_tokens[0].lower() if prefix_tokens else ""
            if first_token not in ALLOWED_REPAIR_CLASSES:
                add_warning(
                    "conditional_repair_prefix",
                    f"{cid}: {a} notes_for_re_audit_if_any must start with one of "
                    f"{sorted(ALLOWED_REPAIR_CLASSES)} (got {first_token!r}); re-audit required"
                )

        # Auditor-family canonicalization. Hard-error on unknown strings.
        # Legacy strings produce a migration warning.
        fam = row.get("auditor_family")
        if a in TERMINAL_VERDICTS and fam is not None:
            if fam not in CANONICAL_AUDITOR_FAMILIES and fam not in LEGACY_AUDITOR_FAMILIES:
                # Tolerate codex-gpt-X.Y for any X.Y (forward-compat)
                if not (isinstance(fam, str) and fam.startswith("codex-gpt-")):
                    errors.append(
                        f"{cid}: auditor_family={fam!r} not in canonical set "
                        f"{sorted(CANONICAL_AUDITOR_FAMILIES)} or known-legacy "
                        f"{sorted(LEGACY_AUDITOR_FAMILIES)}"
                    )
            elif fam in LEGACY_AUDITOR_FAMILIES:
                add_warning(
                    "legacy_auditor_family",
                    f"{cid}: auditor_family={fam!r} is legacy; run "
                    "scripts/canonicalize_auditor_family.py migration"
                )
            elif (
                isinstance(fam, str)
                and fam.startswith("codex-gpt-")
                and not codex_family_meets_minimum(fam)
                and not row.get("previous_auditor_family")
            ):
                add_warning(
                    "codex_model_floor",
                    f"{cid}: auditor_family={fam!r} is below the audit-lane "
                    "minimum (gpt-5.5); model provenance is unverified, so "
                    "relabel with explicit operator confirmation or queue for re-audit"
                )

        # Claude-authored note rule (per FRESH_LOOK_REQUIREMENTS.md §1).
        # A note audited only by Claude — at any criticality — records
        # independence='weak' regardless of session restriction. Cross-family
        # confirmation by Codex/human/external is required for retained-grade
        # promotion.
        #
        # We surface this as a WARNING for now (not an error) because a
        # handful of legacy claude-only fresh_context audits exist on
        # leaf/medium rows. Per current lint these are already prevented
        # from landing as retained-grade on critical/high; the warning
        # surfaces them for migration. After all such legacy rows are
        # migrated to independence='weak' or re-audited by a non-Claude
        # auditor, this notice can be promoted to errors.append.
        if a == "audited_clean" and isinstance(fam, str) and fam.startswith("claude-"):
            if ind != "weak":
                xc = row.get("cross_confirmation") or {}
                xc_status = xc.get("status") if isinstance(xc, dict) else None
                other_side_non_claude = False
                if xc_status in {"confirmed", "third_confirmed_first", "third_confirmed_second", "third_confirmed_hybrid"}:
                    for key in ("first_audit", "second_audit", "third_audit"):
                        side_value = xc.get(key) if isinstance(xc, dict) else None
                        side = side_value if isinstance(side_value, dict) else {}
                        side_fam = side.get("auditor_family") or ""
                        if side_fam and not side_fam.startswith("claude-"):
                            other_side_non_claude = True
                            break
                if not other_side_non_claude:
                    add_warning(
                        "claude_independence",
                        f"{cid}: claude-only audited_clean should record independence='weak' "
                        "per FRESH_LOOK_REQUIREMENTS.md §1, or carry a non-Claude "
                        f"cross-confirmation; got independence={ind!r}, "
                        f"cross_confirmation_status={xc_status!r}"
                    )

        xc = row.get("cross_confirmation") or {}
        xc_status = xc.get("status") if isinstance(xc, dict) else None
        agreement_schema_present = (
            isinstance(xc, dict) and "agreement_schema" in xc
        )
        agreement_schema = xc.get("agreement_schema") if agreement_schema_present else None
        if (
            agreement_schema_present
            and agreement_schema != AUDIT_TUPLE_AGREEMENT_SCHEMA
        ):
            errors.append(
                f"{cid}: unsupported cross_confirmation.agreement_schema "
                f"{agreement_schema!r}"
            )
        exact_tuple_schema = (
            isinstance(xc, dict)
            and agreement_schema == AUDIT_TUPLE_AGREEMENT_SCHEMA
        )
        summary_access_allowed = not agreement_schema_present
        if isinstance(xc, dict) and xc_status == "confirmed":
            first = xc.get("first_audit") or {}
            second = xc.get("second_audit") or {}
            tuple_schema_valid = True
            if exact_tuple_schema:
                for label, summary in (("first_audit", first), ("second_audit", second)):
                    schema_error = audit_summary_tuple_schema_error(summary)
                    if schema_error:
                        tuple_schema_valid = False
                        errors.append(
                            f"{cid}: versioned cross_confirmation.{label} {schema_error}"
                        )
            tuples_match = (
                audit_summary_tuples_match(first, second)
                if not agreement_schema_present
                or (exact_tuple_schema and tuple_schema_valid)
                else None
            )
            summary_access_allowed = (
                not agreement_schema_present
                or (exact_tuple_schema and tuple_schema_valid)
            )
            if exact_tuple_schema and tuple_schema_valid and tuples_match is False:
                errors.append(
                    f"{cid}: confirmed cross-confirmation full audit tuple mismatch "
                    "(verdict, claim_type, normalized claim_scope, "
                    "load_bearing_step_class, decoration_parent_claim_id, "
                    "negative_assertion_classes)"
                )
            elif not agreement_schema_present and tuples_match is False:
                message = (
                    f"{cid}: confirmed cross-confirmation full audit tuple mismatch "
                    "(verdict, claim_type, normalized claim_scope, "
                    "load_bearing_step_class, decoration_parent_claim_id, "
                    "negative_assertion_classes)"
                )
                add_notice(
                    "legacy_cross_confirmation_tuple_mismatch",
                    message + "; legacy confirmation requires fresh re-audit",
                )
            if (
                exact_tuple_schema
                and tuple_schema_valid
                and tuples_match is True
                and not audit_summary_tuples_match(live_row_audit_tuple(row), second)
            ):
                errors.append(
                    f"{cid}: authoritative live row full audit tuple does not "
                    "match the confirmed consensus"
                )
        if isinstance(xc, dict) and xc_status in {"third_confirmed_first", "third_confirmed_second", "third_confirmed_hybrid"}:
            expected_side = {
                "third_confirmed_first": "first",
                "third_confirmed_second": "second",
                "third_confirmed_hybrid": "hybrid",
            }[xc_status]
            first = xc.get("first_audit") or {}
            second = xc.get("second_audit") or {}
            winning = first if expected_side == "first" else second
            third_value = xc.get("third_audit")
            third = third_value if isinstance(third_value, dict) else third_value or {}
            if not third:
                errors.append(f"{cid}: {xc_status} requires third_audit")
            else:
                tuple_schema_valid = True
                if exact_tuple_schema:
                    for label, summary in (
                        ("first_audit", first),
                        ("second_audit", second),
                        ("third_audit", third),
                    ):
                        schema_error = audit_summary_tuple_schema_error(summary)
                        if schema_error:
                            tuple_schema_valid = False
                            errors.append(
                                f"{cid}: versioned cross_confirmation.{label} "
                                f"{schema_error}"
                            )
                third_dict = third if isinstance(third, dict) else {}
                summary_access_allowed = (
                    not agreement_schema_present
                    or (exact_tuple_schema and tuple_schema_valid)
                )
                if summary_access_allowed:
                    side = third_dict.get("sided_with")
                    if side is not None and side != expected_side:
                        errors.append(
                            f"{cid}: {xc_status} conflicts with "
                            f"third_audit.sided_with={side!r}"
                        )
                tuples_match = (
                    audit_summary_tuples_match(third, winning)
                    if not agreement_schema_present
                    or (exact_tuple_schema and tuple_schema_valid)
                    else None
                )
                if (
                    expected_side != "hybrid"
                    and exact_tuple_schema
                    and tuple_schema_valid
                    and tuples_match is False
                ):
                    errors.append(
                        f"{cid}: {xc_status} third_audit full audit tuple does not "
                        "match the winning audit"
                    )
                elif (
                    expected_side != "hybrid"
                    and not agreement_schema_present
                    and tuples_match is False
                ):
                    message = (
                        f"{cid}: {xc_status} third_audit full audit tuple does not "
                        "match the winning audit"
                    )
                    add_notice(
                        "legacy_cross_confirmation_tuple_mismatch",
                        message + "; legacy confirmation requires fresh re-audit",
                    )
                if (
                    exact_tuple_schema
                    and tuple_schema_valid
                    and not audit_summary_tuples_match(
                        live_row_audit_tuple(row), third_dict
                    )
                ):
                    errors.append(
                        f"{cid}: authoritative live row full audit tuple does not "
                        f"match {xc_status} consensus"
                    )
                if (
                    summary_access_allowed
                    and row.get("claim_type_provenance") == "judicial_review"
                ):
                    for key in ("verdict", "claim_type", "load_bearing_step_class"):
                        row_key = "audit_status" if key == "verdict" else key
                        if third_dict.get(key) is not None and row.get(row_key) != third_dict.get(key):
                            errors.append(
                                f"{cid}: judicial_review row {row_key}={row.get(row_key)!r} "
                                f"does not match third_audit {key}={third_dict.get(key)!r}"
                            )

        if a == "audited_clean":
            if not row.get("auditor"):
                errors.append(f"{cid}: audited_clean requires non-empty auditor")
            if not row.get("auditor_family"):
                errors.append(f"{cid}: audited_clean requires auditor_family")
            family = str(row.get("auditor_family") or "")
            if family.startswith("codex-gpt-"):
                model = str(row.get("auditor_model") or "")
                match = (
                    re.fullmatch(r"gpt-(\d+(?:\.\d+)*)(?:-sol)?", model)
                    if model else None
                )
                expected_family = f"codex-gpt-{match.group(1)}" if match else family
                effort = row.get("auditor_reasoning_effort")
                if (
                    expected_family != family
                    or (effort is not None and effort != "xhigh")
                ):
                    errors.append(
                        f"{cid}: Codex audited_clean has inconsistent legacy "
                        "family/model/effort or weak independence"
                    )
            elif family in LEGACY_AUDITOR_FAMILIES:
                pass
            elif row.get("independence") not in {"strong", "external", "judicial_review"}:
                errors.append(
                    f"{cid}: non-Codex audited_clean requires strong, external, "
                    "or judicial_review independence"
                )
            expected = {
                "positive_theorem": "retained",
                "no_go": "retained_no_go",
                "bounded_theorem": "retained_bounded",
                "open_gate": "open_gate",
            }.get(ct)
            if expected is None:
                errors.append(
                    f"{cid}: audited_clean claim_type={ct!r} cannot become a retained-grade theorem"
                )
            elif e != expected:
                if e == "retained_pending_chain":
                    add_notice(
                        "pending_dependency_chain",
                        f"{cid}: audited_clean claim_type={ct!r} waiting on upstream retained-grade closure"
                    )
                else:
                    errors.append(
                        f"{cid}: audited_clean claim_type={ct!r} expected effective_status={expected!r} "
                        f"or 'retained_pending_chain', got {e!r}"
                    )
            # Criticality-aware independence rules.
            criticality = row.get("criticality") or "leaf"
            if criticality in {"critical", "high"} and ind == "weak":
                errors.append(
                    f"{cid}: criticality={criticality} requires independence != 'weak' for audited_clean"
                )
            if criticality == "critical":
                xc_value = row.get("cross_confirmation")
                xc = xc_value if isinstance(xc_value, dict) else {}
                xc_status = xc.get("status")
                if xc_status not in {"confirmed", "third_confirmed_first", "third_confirmed_second", "third_confirmed_hybrid"}:
                    errors.append(
                        f"{cid}: critical claim requires confirmed cross-confirmation; "
                        f"got {xc_status!r}"
                    )
                elif summary_access_allowed:
                    first_value = xc.get("first_audit")
                    second_value = xc.get("second_audit")
                    first = first_value if isinstance(first_value, dict) else {}
                    second = second_value if isinstance(second_value, dict) else {}
                    if first.get("auditor") and first.get("auditor") == second.get("auditor"):
                        errors.append(
                            f"{cid}: critical cross-confirmation reused auditor identity/session "
                            f"{second.get('auditor')!r}"
                        )
                    if (
                        first.get("auditor_family")
                        and first.get("auditor_family") == second.get("auditor_family")
                        and second.get("independence") != "fresh_context"
                    ):
                        errors.append(
                            f"{cid}: same-family critical cross-confirmation requires "
                            "second_audit.independence='fresh_context'"
                        )
                    if xc_status in {"third_confirmed_first", "third_confirmed_second", "third_confirmed_hybrid"}:
                        third_value = xc.get("third_audit")
                        third = third_value if isinstance(third_value, dict) else {}
                        if not third:
                            errors.append(f"{cid}: {xc_status} requires third_audit")
                        elif third.get("auditor") in {first.get("auditor"), second.get("auditor")}:
                            errors.append(
                                f"{cid}: third audit reused auditor identity/session "
                                f"{third.get('auditor')!r}"
                            )
                        elif (
                            third.get("auditor_family")
                            and third.get("auditor_family")
                            in {first.get("auditor_family"), second.get("auditor_family")}
                            and third.get("independence") not in {"fresh_context", "judicial_review"}
                        ):
                            errors.append(
                                f"{cid}: same-family third audit requires "
                                "fresh_context or judicial_review independence"
                            )
                        else:
                            if xc_status == "third_confirmed_hybrid":
                                if third.get("sided_with") != "hybrid":
                                    errors.append(
                                        f"{cid}: third_confirmed_hybrid requires "
                                        f"third_audit.sided_with='hybrid'"
                                    )

        if a == "audited_decoration":
            parent = row.get("decoration_parent_claim_id")
            if ct != "decoration":
                errors.append(f"{cid}: audited_decoration requires claim_type='decoration'")
            if not parent:
                msg = f"{cid}: audited_decoration requires decoration_parent_claim_id"
                if row.get("claim_type_provenance") == "backfilled_pending_reaudit":
                    add_notice(
                        "legacy_decoration_parent",
                        msg + "; legacy row queued for re-audit",
                    )
                else:
                    errors.append(msg)
            else:
                parent_eff = rows.get(parent, {}).get("effective_status")
                if not is_retained_grade(parent_eff):
                    add_notice(
                        "decoration_parent_not_retained",
                        f"{cid}: decoration parent {parent!r} is not retained-grade "
                        f"(effective_status={parent_eff!r})"
                    )

        # Criticality bump after audit (warn that re-audit may be needed).
        # Skip rows already at unaudited / audit_in_progress: the warning is
        # only meaningful for an ACTIVE audit verdict whose snapshot might be
        # stale relative to current criticality. Once the row has been reset
        # (e.g. via invalidate_stale_audits.py or note-hash drift), the
        # snapshot is just historical noise and shouldn't generate a warning.
        snap = row.get("audit_state_snapshot")
        if snap is not None and a not in {None, "unaudited", "audit_in_progress"}:
            crit_now = row.get("criticality") or "leaf"
            crit_at_audit = snap.get("criticality") or "leaf"
            crit_rank = {"leaf": 0, "medium": 1, "high": 2, "critical": 3}
            if crit_rank.get(crit_now, 0) > crit_rank.get(crit_at_audit, 0):
                # Mirror invalidate_stale_audits._categorize_criticality_bump
                # so lint and invalidate stay in sync. Three outcomes per
                # FRESH_LOOK_REQUIREMENTS §4:
                #   - meets:      no notice, no warning.
                #   - soft_reset: invalidate.py will move audited_clean ->
                #                 audit_in_progress + awaiting_cross_confirmation
                #                 on the next run. Notice (informational).
                #   - invalidate: audit fundamentally fails the new tier
                #                 (e.g. weak independence at high+). Warning.
                indep = row.get("independence")
                cc = row.get("cross_confirmation") or {}
                cc_status = cc.get("status") if isinstance(cc, dict) else None
                action = "noop"
                if a != "audited_clean":
                    action = "noop"  # terminal verdict, cross-conf doesn't apply
                elif indep is None or indep == "weak":
                    action = "invalidate"  # below independence floor at high+
                elif crit_now == "high":
                    action = "noop"
                elif crit_now == "critical":
                    if cc_status in {"confirmed", "third_confirmed_first", "third_confirmed_second", "third_confirmed_hybrid"}:
                        action = "noop"
                    else:
                        action = "soft_reset"
                if action == "invalidate":
                    add_warning(
                        "criticality_bumped",
                        f"{cid}: criticality bumped {crit_at_audit}->{crit_now} since audit; "
                        "audit fails new-tier independence floor — invalidate_stale_audits.py "
                        "will hard-reset"
                    )
                elif action == "soft_reset":
                    add_notice(
                        "criticality_bumped_to_critical_awaits_cc",
                        f"{cid}: criticality bumped {crit_at_audit}->{crit_now} since audit; "
                        "first-pass clean stays live, awaiting independent second auditor"
                    )

        # Hash drift.
        on_disk = hash_note_on_disk(row.get("note_path", ""))
        if on_disk is None:
            add_warning(
                "source_note_missing",
                f"{cid}: source note missing on disk: {row.get('note_path')}",
            )
        elif on_disk != row.get("note_hash"):
            # note_hash is a source-content hash, not a verdict. A mismatch means the
            # note was edited since the audit lane last seeded. For a RETAINED-grade row
            # this is a real integrity violation — current text laundered past a stale
            # ratification — so it stays a hard error and must be re-audited before
            # landing. For a NON-retained row (unaudited / audited_conditional / pending)
            # it only means re-audit is pending; per this lint's design (re-audit-required
            # items are notices so strict lint stays useful) and because the nightly
            # audit-lane re-seed refreshes the hash, it is a non-blocking notice — review
            # loops that edit such notes (e.g. formal-carrier repairs on conditional rows)
            # must not be forced to commit audit-lane ledger churn just to clear strict lint.
            msg = f"{cid}: note_hash mismatch — note edited since seeding; re-run seed_audit_ledger.py"
            if is_retained_grade(row.get("effective_status")):
                errors.append(
                    msg + " (RETAINED-grade row: an edited retained note must be re-audited, "
                    "not landed with a stale ratification)"
                )
            else:
                add_notice(
                    "note_hash_drift_reaudit_pending",
                    msg + " (non-retained row: re-audit pending; the audit-lane re-seed "
                    "refreshes the hash — not a strict-lint blocker)",
                )

        # Dangling deps.
        for d in row.get("deps", []):
            if d not in rows:
                add_warning(
                    "dangling_dependency",
                    f"{cid}: dangling dep {d!r} (no ledger row)",
                )

    # Runner-pin integrity. A verdict is bound to the runner it names only
    # through audit_state_snapshot.runner_hash / .helper_runner_hashes; those
    # are the only fields invalidate_stale_audits can compare. A terminal
    # verdict whose snapshot leaves a named runner unbound stands even if the
    # runner is rewritten. Severity follows the note_hash-drift precedent
    # above: on a retained-grade row an undetectable source change is a real
    # integrity violation; on a non-retained row it is re-audit-pending and
    # must not block strict lint.
    pin_baseline = runner_pin_gate.load_baseline()
    for cid, row in rows.items():
        classified = runner_pin_gate.classify_row({**row, "claim_id": cid}, pin_baseline)
        if classified is None:
            continue
        label, detail = classified
        retained = is_retained_grade(row.get("effective_status"))
        message = f"{cid}: {detail}"
        if label == runner_pin_gate.PIN_WRITER_REGRESSION:
            # The snapshot writer had the field and emitted nothing. Only
            # apply_audit writes snapshots, and its runner-pin gate refuses
            # this shape, so a hit here is a regression or a hand-edited row.
            if retained:
                errors.append(
                    message + " (RETAINED-grade row: a verdict that binds no runner "
                    "source cannot be detected as stale)"
                )
            else:
                add_warning("runner_pin_writer_regression", message)
        elif label == runner_pin_gate.PIN_BASELINE_MISSING:
            # Pre-pin snapshot shape on a row the recorded debt does not
            # cover. The baseline is shrink-only; nothing may enter it. The
            # retained-grade split is the same one the note_hash rule above
            # uses, and for the same reason: a non-retained row in this shape
            # is re-audit-pending, and erroring on it would make an ordinary
            # ledger reshard or a newly resolved import closure a repo-wide
            # stop-work with no drain path.
            detail_msg = (
                message + " (runner_pin_baseline.json is shrink-only; a new "
                "unpinned terminal verdict must be pinned, not grandfathered)"
            )
            if retained:
                errors.append(detail_msg)
            else:
                add_warning("runner_pin_baseline_missing", detail_msg)
        elif label == runner_pin_gate.PIN_BASELINE_SOURCE_DRIFTED:
            add_warning("runner_pin_absent_and_source_drifted", message)
        elif label == runner_pin_gate.PIN_BASELINE_NEW_DRIFT:
            if retained:
                errors.append(
                    message + " (RETAINED-grade row: do not move a runner that a "
                    "live unpinned verdict cites — the audit lane must re-look first. "
                    "If the move is intended and already made, record it on this "
                    "row's runner_pin_baseline.json entry as "
                    "source_drifted_since_verdict with drift_evidence; that states "
                    "the debt without asserting a verdict and drops the row to the "
                    "recorded-drift warning class)"
                )
            else:
                add_warning("runner_pin_baseline_new_drift", message)
        else:
            add_notice("runner_pin_grandfathered", message)
    pin_stale = runner_pin_gate.stale_baseline_entries(rows, pin_baseline)
    for cid in pin_stale["drained"]:
        add_notice(
            "runner_pin_baseline_stale",
            f"{cid}: runner_pin_baseline.json entry has drained (row is now pinned "
            "or reset); drop it so the recorded debt keeps shrinking",
        )
    if pin_stale["absent"]:
        add_notice(
            "runner_pin_baseline_stale",
            f"{len(pin_stale['absent'])} runner_pin_baseline.json entries name no "
            f"ledger row (first: {', '.join(pin_stale['absent'][:3])}); drop them "
            "so the recorded debt keeps shrinking",
        )

    # Effective-status propagation sanity. A retained-grade row's deps must
    # themselves be retained-grade, metadata context, axioms, or approved
    # primitives.
    # Open gates, obligations, and retained_pending_chain are explicit blockers,
    # not support for downstream theorem retention. Axioms and approved
    # primitives can satisfy a dep without bounding the row.
    # Metadata deps are chain-satisfying context, not retained-grade theorem
    # support. `decoration_under_<parent>` deps count as retained-grade because
    # decoration_status() only assigns that status when the parent is itself
    # retained-grade.
    # Must stay in sync with compute_effective_status.py's clean_status.
    for cid, row in rows.items():
        if row.get("effective_status") in RETAINED_GRADES:
            for d in row.get("deps", []):
                if premise_nodes.is_accepted_premise_dep(d):
                    continue
                d_eff = rows.get(d, {}).get("effective_status")
                if not is_chain_satisfying_status(d_eff):
                    errors.append(
                        f"{cid}: effective_status={row.get('effective_status')!r} but dep {d!r} "
                        f"has effective_status={d_eff!r}"
                    )

    # Dispatcher manifests are not evidence, but they must be visible to the
    # audit loop. If a sidecar contains live targets and the generated dispatch
    # queue omits them, the process has silently dropped a re-audit request.
    sidecars = dispatch_sidecars()
    if sidecars:
        dispatch_known_ids: set[str] = set()
        if AUDIT_DISPATCH_QUEUE_PATH.exists():
            try:
                dispatch = load_json(AUDIT_DISPATCH_QUEUE_PATH)
                # A target is "known to the dispatch queue" if it appears in
                # live OR resolved_targets OR retired OR resolved_or_invalid.
                # All four buckets represent the dispatch producer having seen
                # and classified the target; only targets that don't appear in
                # any bucket are silently dropped.
                for bucket in ("live", "resolved_targets", "retired", "resolved_or_invalid"):
                    for entry in dispatch.get(bucket, []):
                        cid = entry.get("claim_id")
                        if cid:
                            dispatch_known_ids.add(cid)
            except Exception as exc:  # pragma: no cover - defensive lint path
                add_warning(
                    "audit_dispatch_queue_invalid",
                    f"{AUDIT_DISPATCH_QUEUE_PATH.relative_to(REPO_ROOT)} could not be parsed: {exc}",
                )
        else:
            add_warning(
                "audit_dispatch_queue_missing",
                "dispatcher sidecar exists but docs/audit/data/audit_dispatch_queue.json is missing; "
                "run compute_audit_dispatch_queue.py or the full pipeline"
            )
        for path in sidecars:
            try:
                manifest = load_json(path)
            except Exception as exc:  # pragma: no cover - defensive lint path
                add_warning(
                    "audit_dispatch_sidecar_invalid",
                    f"{path.relative_to(REPO_ROOT)} could not be parsed: {exc}",
                )
                continue
            schema = manifest.get("schema")
            if schema not in SUPPORTED_DISPATCH_SCHEMAS:
                add_warning(
                    "audit_dispatch_sidecar_unsupported",
                    f"{path.relative_to(REPO_ROOT)} schema={schema!r} is not supported by "
                    "compute_audit_dispatch_queue.py"
                )
                continue
            for group in manifest.get("groups") or []:
                for target in group.get("targets") or []:
                    cid = target.get("claim_id")
                    if dispatch_target_live(target, rows) and cid not in dispatch_known_ids:
                        add_warning(
                            "audit_dispatch_queue_stale",
                            f"{path.relative_to(REPO_ROOT)} live target {cid!r} is missing from "
                            "audit_dispatch_queue.json (not present in live, resolved_targets, "
                            "retired, or resolved_or_invalid); rerun the full pipeline before "
                            "relying on audit-loop selection"
                        )

    # A runner-bearing note under an excluded source pattern can never acquire
    # a claim id, note hash, runner pin, queue entry, or verdict:
    # seed_audit_ledger.should_gate_node drops the node before claim typing
    # runs, so no amount of author diligence registers the result. That makes
    # an excluded directory a write-only sink for runner-gated science.
    #
    # REPORTING ONLY -- deliberately not an error, and that is the reviewed
    # disposition, not an oversight. Measured on the landing commit, the
    # detector finds 398 notes, of which 369 sit under
    # docs/work_history/repo/review_feedback/ and were ALL added in the
    # seventeen days from 2026-07-10 to 2026-07-26 by a lane still producing
    # them. An error would therefore be red on arrival and red again within
    # hours of every drain, and audit_lint is a hard gate in two places
    # (run_pipeline.sh stage 13 under `set -e`, and pre_commit_audit_check.sh),
    # so that is a repo-wide stop-work condition with no drain path -- the same
    # objection that already ruled out erroring on the whole population.
    # Arming the error needs the prior decision about what
    # docs/work_history/ is for and where a runner-bearing result belongs;
    # that decision is the owner's and is not made here. Until then the
    # baseline split below is the measurement that decision needs: entries in
    # unregistered_runner_bearing_note_baseline.txt are the population as
    # measured when the detector was written, and anything the detector finds
    # outside that list is what the class has grown by since.
    #
    # The baseline lives beside the scripts rather than in docs/audit/data/
    # because that directory is restored wholesale from origin/main before a
    # science PR lands, which would silently revert every drain.
    if graph and excluded_source_patterns:
        baseline_path = (
            REPO_ROOT
            / "docs"
            / "audit"
            / "scripts"
            / "unregistered_runner_bearing_note_baseline.txt"
        )
        baseline: set[str] = set()
        if baseline_path.exists():
            baseline = {
                line.strip()
                for line in baseline_path.read_text(encoding="utf-8").splitlines()
                if line.strip() and not line.strip().startswith("#")
            }
        live_unregistered: set[str] = set()
        for cid, node in sorted(graph.get("nodes", {}).items()):
            if cid in rows:
                continue
            node_path = node.get("path") or ""
            if not node_path or node_path in never_gate_source_paths:
                continue
            if not any(fnmatchcase(node_path, pat) for pat in excluded_source_patterns):
                continue
            node_runners = [
                r
                for r in [node.get("runner_path"), *(node.get("helper_runner_paths") or [])]
                if r and (REPO_ROOT / r).exists()
            ]
            if not node_runners:
                continue
            live_unregistered.add(node_path)
            if node_path in baseline:
                add_notice(
                    "unregistered_runner_bearing_note",
                    f"{node_path}: names runner(s) {sorted(set(node_runners))} but matches "
                    "data/excluded_source_patterns.txt, so seeding creates no ledger row; "
                    "grandfathered in unregistered_runner_bearing_note_baseline.txt and "
                    "drainable by moving the note onto an auditable path"
                )
            else:
                add_notice(
                    "unregistered_runner_bearing_note_unbaselined",
                    f"{node_path}: names runner(s) {sorted(set(node_runners))} but matches "
                    "data/excluded_source_patterns.txt, so seed_audit_ledger.should_gate_node "
                    "drops it and the result can never acquire a claim id, note hash, runner "
                    "pin, queue entry, or verdict. Not in "
                    "unregistered_runner_bearing_note_baseline.txt, so it postdates the rule. "
                    "Move the note onto an auditable docs/ path, or register the exact path in "
                    "docs/audit/data/never_gate_source_paths.txt, or drop the runner reference "
                    "if the note is narrative only."
                )
        for stale in sorted(baseline - live_unregistered):
            add_notice(
                "unregistered_runner_bearing_note_baseline_stale",
                f"{stale}: listed in unregistered_runner_bearing_note_baseline.txt but no "
                "longer an unregistered runner-bearing note; prune the baseline entry"
            )

    # Graph health: cycles (informational).
    cycle_count = 0
    if graph:
        # Quick reachability-based cycle detection on the graph adjacency.
        adj = {c: list(n["deps"]) for c, n in graph["nodes"].items()}
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {c: WHITE for c in adj}
        for start in adj:
            if color[start] != WHITE:
                continue
            stack = [(start, iter(adj[start]))]
            color[start] = GRAY
            while stack:
                node, it = stack[-1]
                try:
                    nxt = next(it)
                except StopIteration:
                    color[node] = BLACK
                    stack.pop()
                    continue
                if nxt not in color:
                    continue
                if color[nxt] == GRAY:
                    cycle_count += 1
                    continue
                if color[nxt] == BLACK:
                    continue
                color[nxt] = GRAY
                stack.append((nxt, iter(adj[nxt])))
        if cycle_count:
            add_notice("graph_cycles", f"graph contains {cycle_count} back-edges (cycles)")

    # No-go grade-path health. `retained_no_go` is a named retained grade and
    # the framework leans on foreclosures constantly, but nothing reported
    # whether the grade was ever actually reached. It was not: the population
    # sat at zero for months while clean forensic verdicts were minted and
    # then reset, and no surface said so. These notices make the grade path
    # observable without asserting anything about any row's verdict.
    no_go_rows = [r for r in rows.values() if r.get("claim_type") == "no_go"]
    if no_go_rows:
        retained_no_go = sum(
            1 for r in no_go_rows if r.get("effective_status") == "retained_no_go"
        )
        reset_after_clean = 0
        legacy_snapshot_rows = 0
        for row in no_go_rows:
            archived = row.get("previous_audits") or []
            if row.get("audit_status") in {None, "unaudited"} and any(
                a.get("audit_status") == "audited_clean"
                and str(a.get("invalidation_reason") or "").startswith(
                    "no_go_discipline_packet_"
                )
                for a in archived
            ):
                reset_after_clean += 1
            if any(
                isinstance(a.get("no_go_discipline"), dict)
                and no_go_discipline_gate.evidence_snapshot_schema_defect(
                    a["no_go_discipline"]
                )
                is not None
                and isinstance(
                    (a.get("no_go_discipline") or {}).get("evidence_snapshot"), dict
                )
                for a in archived
            ):
                legacy_snapshot_rows += 1
        if retained_no_go == 0:
            add_notice(
                "no_go_grade_path_unreached",
                f"{len(no_go_rows)} rows carry claim_type no_go and none "
                "currently reaches effective_status retained_no_go",
            )
        if reset_after_clean:
            add_notice(
                "no_go_clean_verdict_reset_by_packet_gate",
                f"{reset_after_clean} no_go rows are unaudited today but hold an "
                "archived audited_clean reset by a no_go_discipline_packet_* "
                "reason; these are re-audit targets, not fresh rows",
            )
        if legacy_snapshot_rows:
            add_notice(
                "no_go_legacy_evidence_snapshot",
                f"{legacy_snapshot_rows} no_go rows carry an archived evidence "
                "snapshot the current reader cannot authenticate; run "
                "no_go_discipline_gate.evidence_snapshot_schema_defect on the "
                "archived packet for the specific reason. Their forensic "
                "evidence is not restorable in place",
            )

    # Output.
    def issue_count(groups: dict[str, list[str]]) -> int:
        return sum(len(items) for items in groups.values())

    def print_issue_groups(
        label: str,
        prefix: str,
        groups: dict[str, list[str]],
        max_items_per_group: int = 3,
    ) -> None:
        total = issue_count(groups)
        if not total:
            return
        print(f"  {total} {label}:")
        for category in sorted(groups):
            items = groups[category]
            print(f"    {category}: {len(items)}")
            for item in items[:max_items_per_group]:
                print(f"      {prefix}: {item}")
            if len(items) > max_items_per_group:
                print(f"      ... and {len(items) - max_items_per_group} more")

    print(f"audit_lint: {len(rows)} rows checked")
    print_issue_groups("warnings", "WARN", warnings)
    print_issue_groups("notices", "NOTICE", notices)
    if errors:
        print(f"  {len(errors)} errors:")
        for e in errors[:30]:
            print(f"    ERROR: {e}")
        if len(errors) > 30:
            print(f"    ... and {len(errors) - 30} more")
        return 1
    print("  OK: no errors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
