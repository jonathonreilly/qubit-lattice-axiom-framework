#!/usr/bin/env python3
"""Read-only pull-request review queue and landing history.

Default mode makes one ``gh pr list --state open`` call and prints every open
PR with its age, size, review counts, mergeable state and a computed next
action.  ``--history N`` makes one ``gh pr list --state closed`` call and
prints, for each PR, the hours from open to merged or closed and the cost
fields its comments carry in a ``landing-record`` block.  ``--check-record
FILE`` checks the block of a drafted landing comment and calls nothing.

The command writes nothing to GitHub and creates no file.  A next action is a
reading of GitHub fields and comment text.  It is not a review result, and it
replaces no review-loop lens, gate or landing check.  The block format and the
comment text this command reads are defined in
``docs/ai_methodology/skills/review-loop/references/FIXES_AND_REPORTING.md``.
"""
from __future__ import annotations

import argparse
import functools
import json
import math
import re
import statistics
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import review_loop_backlog_inventory as inventory


REPO_ROOT = Path(__file__).resolve().parents[1]
QUEUE_FIELDS = inventory.GH_FIELDS + (
    ",createdAt,additions,deletions,changedFiles,mergeable,mergeStateStatus,"
    "reviewDecision,reviews,comments"
)
HISTORY_FIELDS = (
    "number,title,state,baseRefName,headRefOid,createdAt,closedAt,mergedAt,"
    "additions,changedFiles,comments,url"
)
# Comment bodies make these calls slower than the inventory's: 60 closed PRs
# took 7 seconds when this was written.
GH_TIMEOUT_SECONDS = 300
DEFAULT_TITLE_WIDTH = 48

DRAFT = "draft"
BASE_NOT_MAIN = "base is not main"
CONFLICTS = "conflicts with main"
FIRST_REVIEW = "needs first review"
NO_VERDICT = "comments, no verdict"
RE_REVIEW = "needs re-review"
READY = "ready to land"
FINDINGS = "findings posted"
# Display order: who can act now comes first.
NEXT_ACTIONS = (
    READY,
    RE_REVIEW,
    FIRST_REVIEW,
    FINDINGS,
    NO_VERDICT,
    CONFLICTS,
    BASE_NOT_MAIN,
    DRAFT,
)

VERDICT_PASS = "pass"
VERDICT_FINDINGS = "findings"
_VERDICT_WORD_RE = re.compile(
    r"\b(?P<findings>HOLD|NEEDS MANUAL SCIENCE)\b|\b(?P<pass>PASS)\b"
)
_HEX_TOKEN_RE = re.compile(r"\b[0-9a-f]{12,40}\b")

COST_BLOCK_NAME = "landing-record"
COST_FIELDS = (
    "review_start_utc",
    "review_end_utc",
    "rounds",
    "reviewer_provider",
    "reviewer_model",
    "reviewer_effort",
    "gate_seconds",
    "train",
    "frozen_head",
    "landed_head",
    "recovery_ref",
)
NOT_RECORDED = "none"
_COST_BLOCK_RE = re.compile(
    r"^```" + COST_BLOCK_NAME + r"[ \t]*\n(?P<body>.*?)^```[ \t]*$",
    re.MULTILINE | re.DOTALL,
)
_UTC_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
_TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/-]*")
_SHA_RE = re.compile(r"[0-9a-f]{40}")
_REF_RE = re.compile(r"refs/[A-Za-z0-9._/-]+")


def parse_utc(text: str) -> datetime:
    """Parse the one UTC form GitHub prints, ``2026-11-10T21:45:18Z``."""
    return datetime.strptime(text, _UTC_FORMAT).replace(tzinfo=timezone.utc)


def _hours(start: datetime, end: datetime) -> float:
    return round((end - start).total_seconds() / 3600, 2)


def _days(start: datetime, end: datetime) -> float:
    return round((end - start).total_seconds() / 86400, 1)


# ---------------------------------------------------------------------------
# Open queue
# ---------------------------------------------------------------------------


def read_verdict(body: str) -> str | None:
    """Return the verdict the first paragraph of a comment or review states.

    The first of ``PASS``, ``HOLD`` or ``NEEDS MANUAL SCIENCE`` in the first
    paragraph decides; the words are upper case and whole.  Text without one
    of them carries no verdict for this command.
    """
    first_paragraph = re.split(
        r"\n\s*\n", body.replace("\r\n", "\n").strip(), maxsplit=1
    )[0]
    match = _VERDICT_WORD_RE.search(first_paragraph)
    if match is None:
        return None
    return VERDICT_FINDINGS if match.group("findings") else VERDICT_PASS


def names_head(body: str, head_oid: str) -> bool:
    """True when the text names the given head by 12 or more hex characters."""
    if not head_oid:
        return False
    return any(head_oid.startswith(token) for token in _HEX_TOKEN_RE.findall(body))


def latest_verdict(pr: dict) -> dict:
    """Read review and comment records; the newest one with a verdict wins."""
    head_oid = str(pr.get("headRefOid") or "")
    records: list[dict] = []
    for review in pr.get("reviews") or []:
        state = review.get("state")
        if state in {"DISMISSED", "PENDING"}:
            continue
        body = review.get("body") or ""
        if state == "APPROVED":
            verdict = VERDICT_PASS
        elif state == "CHANGES_REQUESTED":
            verdict = VERDICT_FINDINGS
        else:
            verdict = read_verdict(body)
        reviewed = str((review.get("commit") or {}).get("oid") or "")
        records.append(
            {
                "at": review.get("submittedAt") or "",
                "source": "review",
                "verdict": verdict,
                "names_head": bool(reviewed and reviewed == head_oid)
                or names_head(body, head_oid),
            }
        )
    for comment in pr.get("comments") or []:
        body = comment.get("body") or ""
        records.append(
            {
                "at": comment.get("createdAt") or "",
                "source": "comment",
                "verdict": read_verdict(body),
                "names_head": names_head(body, head_oid),
            }
        )
    with_verdict = [record for record in records if record["verdict"]]
    if not with_verdict:
        return {
            "record_count": len(records),
            "verdict": None,
            "verdict_at": None,
            "verdict_source": None,
            "verdict_names_head": None,
        }
    newest = max(with_verdict, key=lambda record: record["at"])
    return {
        "record_count": len(records),
        "verdict": newest["verdict"],
        "verdict_at": newest["at"] or None,
        "verdict_source": newest["source"],
        "verdict_names_head": newest["names_head"],
    }


def next_action(
    *,
    draft: bool,
    base: str,
    mergeable: str,
    record_count: int,
    verdict: str | None,
    verdict_names_head: bool | None,
) -> str:
    """Map one PR to the fixed vocabulary.  The first matching line decides."""
    if draft:
        return DRAFT
    if base != "main":
        return BASE_NOT_MAIN
    if mergeable == "CONFLICTING":
        return CONFLICTS
    if record_count == 0:
        return FIRST_REVIEW
    if verdict is None:
        return NO_VERDICT
    if not verdict_names_head:
        return RE_REVIEW
    return READY if verdict == VERDICT_PASS else FINDINGS


def _median(values: list[float]) -> float | None:
    return round(statistics.median(values), 2) if values else None


def _percentile(values: list[float], percent: int) -> float | None:
    """Nearest-rank percentile: the smallest value with ``percent`` at or below."""
    if not values:
        return None
    ordered = sorted(values)
    return ordered[max(0, math.ceil(percent / 100 * len(ordered)) - 1)]


def build_queue(raw_prs: list[dict], now: datetime, limit: int) -> dict:
    """Turn one ``gh pr list --state open`` payload into the queue."""
    topology = inventory.analyze_topology(raw_prs, limit=limit)
    parents = {row["number"]: row.get("parent_pr") for row in topology["prs"]}
    rows: list[dict] = []
    for raw in raw_prs:
        missing = [
            field
            for field in ("number", "baseRefName", "createdAt", "updatedAt")
            if field not in raw
        ]
        if missing:
            raise inventory.InventoryError(
                f"PR row missing fields: {', '.join(missing)}"
            )
        number = int(raw["number"])
        draft = bool(raw.get("isDraft"))
        base = str(raw["baseRefName"])
        mergeable = str(raw.get("mergeable") or "UNKNOWN")
        verdict = latest_verdict(raw)
        rows.append(
            {
                "number": number,
                "title": str(raw.get("title") or ""),
                "draft": draft,
                "base": base,
                "parent_pr": parents.get(number),
                "head": str(raw.get("headRefName") or ""),
                "head_oid": str(raw.get("headRefOid") or ""),
                "created_at": raw["createdAt"],
                "updated_at": raw["updatedAt"],
                "age_days": _days(parse_utc(raw["createdAt"]), now),
                "idle_days": _days(parse_utc(raw["updatedAt"]), now),
                "additions": raw.get("additions"),
                "deletions": raw.get("deletions"),
                "changed_files": raw.get("changedFiles"),
                "reviews": len(raw.get("reviews") or []),
                "comments": len(raw.get("comments") or []),
                "mergeable": mergeable,
                "merge_state": str(raw.get("mergeStateStatus") or "UNKNOWN"),
                "review_decision": raw.get("reviewDecision") or None,
                "verdict": verdict["verdict"],
                "verdict_at": verdict["verdict_at"],
                "verdict_source": verdict["verdict_source"],
                "verdict_names_head": verdict["verdict_names_head"],
                "next_action": next_action(
                    draft=draft,
                    base=base,
                    mergeable=mergeable,
                    record_count=verdict["record_count"],
                    verdict=verdict["verdict"],
                    verdict_names_head=verdict["verdict_names_head"],
                ),
                "url": raw.get("url"),
            }
        )
    rows.sort(
        key=lambda row: (
            NEXT_ACTIONS.index(row["next_action"]),
            row["created_at"],
            row["number"],
        )
    )
    non_draft = [row for row in rows if not row["draft"]]
    ages = [row["age_days"] for row in non_draft]
    counts = Counter(row["next_action"] for row in rows)
    return {
        "schema_version": 1,
        "generated_at": now.strftime(_UTC_FORMAT),
        "read_only": True,
        "source": "gh pr list --state open",
        "query_limit": limit,
        "limit_reached": len(raw_prs) >= limit,
        "next_action_vocabulary": list(NEXT_ACTIONS),
        "summary": {
            "open": len(rows),
            "non_draft": len(non_draft),
            "draft": len(rows) - len(non_draft),
            "non_draft_without_review_or_comment": sum(
                row["reviews"] == 0 and row["comments"] == 0 for row in non_draft
            ),
            "non_draft_age_days_median": _median(ages),
            "non_draft_age_days_max": max(ages) if ages else None,
            "non_draft_additions": sum(row["additions"] or 0 for row in non_draft),
            "non_draft_changed_files": sum(
                row["changed_files"] or 0 for row in non_draft
            ),
            "mergeable_unknown": sum(row["mergeable"] == "UNKNOWN" for row in rows),
            "by_next_action": {
                action: counts[action] for action in NEXT_ACTIONS if counts[action]
            },
        },
        "prs": rows,
    }


def _cell(text: str) -> str:
    return " ".join(str(text).split()).replace("|", "\\|")


def _number(value: object) -> str:
    if value is None:
        return "-"
    if isinstance(value, int):
        return f"{value:,}"
    return str(value)


def render_queue(queue: dict, title_width: int = DEFAULT_TITLE_WIDTH) -> str:
    summary = queue["summary"]
    lines = [
        "# Review queue (read only)",
        "",
        (
            f"Generated {queue['generated_at']} from one `{queue['source']}` call. "
            f"{summary['open']} open PRs: {summary['non_draft']} non-draft, "
            f"{summary['draft']} draft."
        ),
        (
            f"Non-draft: {summary['non_draft_without_review_or_comment']} with no "
            f"review and no comment; median age "
            f"{_number(summary['non_draft_age_days_median'])} d, oldest "
            f"{_number(summary['non_draft_age_days_max'])} d; "
            f"{summary['non_draft_additions']:,} added lines in "
            f"{summary['non_draft_changed_files']:,} files."
        ),
        (
            "By next action: "
            + "; ".join(
                f"{action} {count}"
                for action, count in summary["by_next_action"].items()
            )
            + "."
        ),
        "",
        (
            "| PR | title | draft | base | age d | idle d | +lines | files | "
            "reviews | comments | mergeable | next action |"
        ),
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for row in queue["prs"]:
        base = row["base"]
        if row["parent_pr"] is not None:
            base = f"{base} (#{row['parent_pr']})"
        lines.append(
            "| "
            + " | ".join(
                [
                    f"#{row['number']}",
                    _cell(inventory._short(row["title"], title_width)),
                    "yes" if row["draft"] else "no",
                    _cell(base),
                    f"{row['age_days']:.1f}",
                    f"{row['idle_days']:.1f}",
                    _number(row["additions"]),
                    _number(row["changed_files"]),
                    str(row["reviews"]),
                    str(row["comments"]),
                    row["mergeable"],
                    row["next_action"],
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append(
        "A next action is read from GitHub fields and comment text. It grants "
        "no review, audit or landing status."
    )
    if summary["mergeable_unknown"]:
        lines.append(
            f"{summary['mergeable_unknown']} PRs show mergeable UNKNOWN: GitHub "
            "computes that field after a request. Run the command again in a "
            "minute."
        )
    if queue["limit_reached"]:
        lines.append(
            f"The query limit of {queue['query_limit']} was reached, so the list "
            "may be incomplete. Run again with a higher --limit."
        )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Landing record: the cost fields of a landing comment
# ---------------------------------------------------------------------------


def find_cost_blocks(body: str) -> list[str]:
    """Return the text of every ``landing-record`` fenced block in a comment."""
    return [
        match.group("body")
        for match in _COST_BLOCK_RE.finditer(body.replace("\r\n", "\n"))
    ]


def _cost_value(key: str, value: str) -> object:
    """Convert one field value; raise ValueError with the reason if it is bad."""
    if key in {"review_start_utc", "review_end_utc"}:
        try:
            parse_utc(value)
        except ValueError:
            raise ValueError("not a UTC time like 2026-11-10T21:45:18Z") from None
        return value
    if key == "rounds":
        if not value.isdigit() or int(value) < 1:
            raise ValueError("not a whole number of 1 or more")
        return int(value)
    if key == "gate_seconds":
        try:
            seconds = float(value)
        except ValueError:
            raise ValueError("not a number of seconds") from None
        if not math.isfinite(seconds) or seconds < 0:
            raise ValueError("not a number of seconds")
        return seconds
    if key in {"frozen_head", "landed_head"}:
        if not _SHA_RE.fullmatch(value):
            raise ValueError("not a full 40-character commit SHA")
        return value
    if key == "recovery_ref":
        if not _REF_RE.fullmatch(value):
            raise ValueError("not a full ref name that starts with refs/")
        return value
    if not _TOKEN_RE.fullmatch(value):
        raise ValueError("not one word of letters, digits and . _ / -")
    return value


def parse_cost_block(text: str) -> tuple[dict, list[str]]:
    """Parse one block into ``{field: value or None}`` and a list of problems.

    Every field of ``COST_FIELDS`` is present in the result.  ``None`` means
    the block says ``none``, omits the field or gives a value that is not
    valid; the last two are also listed as problems.
    """
    fields: dict = {key: None for key in COST_FIELDS}
    problems: list[str] = []
    seen: set[str] = set()
    for line in text.splitlines():
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if not separator:
            problems.append(f"not a `field: value` line: {line.strip()[:60]}")
            continue
        if key not in fields:
            problems.append(f"unknown field: {key[:60]}")
            continue
        if key in seen:
            problems.append(f"repeated field: {key}")
            continue
        seen.add(key)
        if value == NOT_RECORDED:
            continue
        try:
            fields[key] = _cost_value(key, value)
        except ValueError as exc:
            problems.append(f"{key}: {exc}")
    problems.extend(f"missing field: {key}" for key in COST_FIELDS if key not in seen)
    if (
        fields["review_start_utc"]
        and fields["review_end_utc"]
        and fields["review_end_utc"] < fields["review_start_utc"]
    ):
        problems.append("review_end_utc is before review_start_utc")
    return fields, problems


def format_cost_block(fields: dict) -> str:
    """Render the block a landing comment carries; ``None`` prints as none."""
    lines = ["```" + COST_BLOCK_NAME]
    for key in COST_FIELDS:
        value = fields.get(key)
        lines.append(f"{key}: {NOT_RECORDED if value is None else value}")
    lines.append("```")
    return "\n".join(lines)


def check_record_text(text: str) -> list[str]:
    """Return the problems of a drafted landing comment; empty means usable."""
    blocks = find_cost_blocks(text)
    if len(blocks) != 1:
        return [f"expected one {COST_BLOCK_NAME} block, found {len(blocks)}"]
    return parse_cost_block(blocks[0])[1]


# ---------------------------------------------------------------------------
# History
# ---------------------------------------------------------------------------


def _stat(values: list[float]) -> dict:
    return {
        "n": len(values),
        "median": _median(values),
        "p90": _percentile(values, 90),
    }


def build_history(raw_prs: list[dict], requested: int, now: datetime) -> dict:
    """Turn one ``gh pr list --state closed`` payload into the history."""
    rows: list[dict] = []
    for raw in raw_prs:
        state = str(raw.get("state") or "")
        ended_at = raw.get("mergedAt") or raw.get("closedAt")
        if "number" not in raw or not raw.get("createdAt") or not ended_at:
            raise inventory.InventoryError(
                "closed PR row lacks number, createdAt or an end time"
            )
        created, ended = parse_utc(raw["createdAt"]), parse_utc(ended_at)
        blocks = [
            parse_cost_block(block)
            for comment in raw.get("comments") or []
            for block in find_cost_blocks(comment.get("body") or "")
        ]
        # A PR can land once under the merged-state loop, so the last block is
        # the landing; earlier blocks are counted, not read.
        cost, problems = blocks[-1] if blocks else (None, [])
        row = {
            "number": int(raw["number"]),
            "title": str(raw.get("title") or ""),
            "state": state,
            "created_at": raw["createdAt"],
            "ended_at": ended_at,
            "open_hours": _hours(created, ended),
            "comments": len(raw.get("comments") or []),
            "cost_blocks": len(blocks),
            "cost": cost,
            "cost_problems": problems,
            "wait_hours": None,
            "review_hours": None,
            "url": raw.get("url"),
        }
        if cost and cost["review_start_utc"]:
            start = parse_utc(cost["review_start_utc"])
            row["wait_hours"] = _hours(created, start)
            if cost["review_end_utc"]:
                row["review_hours"] = _hours(start, parse_utc(cost["review_end_utc"]))
        rows.append(row)
    rows.sort(key=lambda row: (row["ended_at"], row["number"]), reverse=True)
    with_cost = [row for row in rows if row["cost"] is not None]
    gate_by_landing = {
        row["cost"]["landed_head"] or f"pr-{row['number']}": row["cost"]["gate_seconds"]
        for row in with_cost
        if row["cost"]["gate_seconds"] is not None
    }
    return {
        "schema_version": 1,
        "generated_at": now.strftime(_UTC_FORMAT),
        "read_only": True,
        "source": "gh pr list --state closed",
        "requested": requested,
        "returned": len(rows),
        "cost_block": COST_BLOCK_NAME,
        "cost_fields": list(COST_FIELDS),
        "summary": {
            "merged": sum(row["state"] == "MERGED" for row in rows),
            "closed_not_merged": sum(row["state"] != "MERGED" for row in rows),
            "with_cost_fields": len(with_cost),
            "without_cost_fields": len(rows) - len(with_cost),
            "with_cost_problems": sum(bool(row["cost_problems"]) for row in rows),
            "open_to_merged_hours": _stat(
                [row["open_hours"] for row in rows if row["state"] == "MERGED"]
            ),
            "open_to_closed_hours": _stat(
                [row["open_hours"] for row in rows if row["state"] != "MERGED"]
            ),
            "open_to_review_start_hours": _stat(
                [row["wait_hours"] for row in rows if row["wait_hours"] is not None]
            ),
            "review_hours": _stat(
                [row["review_hours"] for row in rows if row["review_hours"] is not None]
            ),
            "rounds": _stat(
                [row["cost"]["rounds"] for row in with_cost if row["cost"]["rounds"]]
            ),
            # One gate serves a whole train: count it once per landed head.
            "gate_seconds": _stat(list(gate_by_landing.values())),
        },
        "prs": rows,
    }


def render_history(history: dict, title_width: int = DEFAULT_TITLE_WIDTH) -> str:
    summary = history["summary"]
    lines = [
        "# Landing history (read only)",
        "",
        (
            f"Generated {history['generated_at']} from one `{history['source']}` "
            f"call: the {history['returned']} most recently opened PRs that are "
            f"merged or closed ({history['requested']} requested), newest end "
            "first."
        ),
        "",
        (
            "| PR | title | state | open h | comments | rounds | reviewer | "
            "wait h | review h | gate s | train | landed head |"
        ),
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for row in history["prs"]:
        cost = row["cost"] or {}
        reviewer = "/".join(
            str(cost.get(key) or "-")
            for key in ("reviewer_provider", "reviewer_model", "reviewer_effort")
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    f"#{row['number']}",
                    _cell(inventory._short(row["title"], title_width)),
                    row["state"],
                    f"{row['open_hours']:.2f}",
                    str(row["comments"]),
                    _number(cost.get("rounds")),
                    reviewer if row["cost"] else "-",
                    _number(row["wait_hours"]),
                    _number(row["review_hours"]),
                    _number(cost.get("gate_seconds")),
                    _number(cost.get("train")),
                    (cost.get("landed_head") or "-")[:12],
                ]
            )
            + " |"
        )
    lines += [
        "",
        "| measure | n | median | p90 |",
        "|---|---|---|---|",
    ]
    for label, key in (
        ("open to merged, hours", "open_to_merged_hours"),
        ("open to closed without merge, hours", "open_to_closed_hours"),
        ("open to review start, hours", "open_to_review_start_hours"),
        ("review start to review end, hours", "review_hours"),
        ("review rounds", "rounds"),
        ("gate seconds, one per landed head", "gate_seconds"),
    ):
        stat = summary[key]
        lines.append(
            f"| {label} | {stat['n']} | {_number(stat['median'])} | "
            f"{_number(stat['p90'])} |"
        )
    lines += [
        "",
        (
            f"{summary['without_cost_fields']} of {history['returned']} PRs carry "
            f"no cost fields (no `{COST_BLOCK_NAME}` block in a comment). "
            f"{summary['with_cost_problems']} carry a block with a problem."
        ),
        (
            "p90 is the nearest-rank value. CLOSED does not say whether a PR "
            "landed: a landing loop that pushes the reviewed commits to main "
            "and then closes the PR leaves it CLOSED. A landed head says it "
            "landed."
        ),
    ]
    for row in history["prs"]:
        for problem in row["cost_problems"]:
            lines.append(f"#{row['number']} {COST_BLOCK_NAME}: {problem}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

_gh = functools.partial(inventory.run, timeout=GH_TIMEOUT_SECONDS)


def collect_queue(
    repo_root: Path,
    limit: int = inventory.DEFAULT_LIMIT,
    runner: inventory.Run = _gh,
    now: datetime | None = None,
) -> dict:
    raw = inventory.fetch_prs(
        repo_root, limit=limit, runner=runner, fields=QUEUE_FIELDS
    )
    return build_queue(raw, now or datetime.now(timezone.utc), limit)


def collect_history(
    repo_root: Path,
    count: int,
    runner: inventory.Run = _gh,
    now: datetime | None = None,
) -> dict:
    raw = inventory.fetch_prs(
        repo_root, limit=count, runner=runner, state="closed", fields=HISTORY_FIELDS
    )
    return build_history(raw, count, now or datetime.now(timezone.utc))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--json", action="store_true", help="print JSON, not Markdown")
    parser.add_argument(
        "--history",
        type=int,
        metavar="N",
        help="read the N most recently opened merged or closed PRs instead",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=inventory.DEFAULT_LIMIT,
        help="most open PRs to read (default %(default)s)",
    )
    parser.add_argument("--title-width", type=int, default=DEFAULT_TITLE_WIDTH)
    parser.add_argument(
        "--check-record",
        type=Path,
        metavar="FILE",
        help=(
            f"check the {COST_BLOCK_NAME} block of a drafted landing comment "
            "in FILE; no GitHub call"
        ),
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.limit <= 0 or args.title_width <= 0 or (
        args.history is not None and args.history <= 0
    ):
        print("--limit, --title-width and --history must be positive", file=sys.stderr)
        return 2
    if args.check_record is not None:
        try:
            problems = check_record_text(args.check_record.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as exc:
            print(f"cannot read {args.check_record}: {exc}", file=sys.stderr)
            return 2
        for problem in problems:
            print(f"{COST_BLOCK_NAME}: {problem}")
        if not problems:
            print(f"{COST_BLOCK_NAME}: OK")
        return 1 if problems else 0
    try:
        if args.history is not None:
            result = collect_history(REPO_ROOT, args.history)
            text = render_history(result, args.title_width)
        else:
            result = collect_queue(REPO_ROOT, args.limit)
            text = render_queue(result, args.title_width)
    except (inventory.InventoryError, ValueError) as exc:
        print(f"review queue failed closed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True) if args.json else text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
