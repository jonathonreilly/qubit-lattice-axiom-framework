#!/usr/bin/env python3
"""Read-only review-loop backlog, recovery, and capacity inventory.

The command performs one GitHub PR enumeration and local read-only probes.  It
does not fetch refs, prune/remove worktrees, launch reviewers, edit files,
review claims, apply audit verdicts, or land anything.  Its ``ready`` language
means only that GitHub declares the PR's base as ``main``; every review-loop
lens, preflight, confirmation, and landing gate remains mandatory.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
GH_FIELDS = (
    "number,title,isDraft,isCrossRepository,baseRefName,headRefName,headRefOid,"
    "updatedAt,url"
)
DEFAULT_LIMIT = 1000
MAX_SHARED_PROCESSES = 10
# Use the conservative end of the skill's shared 8-10 process ceiling.  An
# operator can raise this to 10 after coordinating with the other lanes.
DEFAULT_MAX_PROCESSES = 8
MIN_FREE_KIB = 5 * 1024 * 1024
# Slightly conservative against the 343.6 MiB measured full-worktree cost in
# the review-loop skill.  This is planning headroom; every spawn still reruns
# the skill's authoritative 5 GiB admission guard.
ESTIMATED_WORKTREE_KIB = 384 * 1024
AUDIT_BUSY_SEATS = 4
AUDIT_BUSY_REVIEW_CAP = 3

Run = Callable[[list[str], Path], str]


class InventoryError(RuntimeError):
    """A required read-only probe failed."""


def run(cmd: list[str], cwd: Path) -> str:
    try:
        proc = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, timeout=60
        )
    except subprocess.TimeoutExpired as exc:
        raise InventoryError(f"{' '.join(cmd[:4])} timed out after 60 seconds") from exc
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "no diagnostic").strip()
        raise InventoryError(f"{' '.join(cmd[:4])} failed: {detail}")
    return proc.stdout


def fetch_open_prs(
    repo_root: Path,
    limit: int = DEFAULT_LIMIT,
    runner: Run = run,
) -> list[dict]:
    """Enumerate open PRs exactly once; fail closed on malformed output."""
    text = runner(
        [
            "gh",
            "pr",
            "list",
            "--state",
            "open",
            "--limit",
            str(limit),
            "--json",
            GH_FIELDS,
        ],
        repo_root,
    )
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        raise InventoryError(f"gh returned invalid JSON: {exc}") from exc
    if not isinstance(payload, list):
        raise InventoryError("gh PR inventory was not a JSON list")
    return payload


def _pr_copy(raw: dict) -> dict:
    required = ("number", "baseRefName", "headRefName")
    missing = [field for field in required if field not in raw]
    if missing:
        raise InventoryError(f"PR row missing fields: {', '.join(missing)}")
    row = dict(raw)
    row["number"] = int(row["number"])
    row["baseRefName"] = str(row["baseRefName"])
    row["headRefName"] = str(row["headRefName"])
    return row


def analyze_topology(raw_prs: Iterable[dict], limit: int = DEFAULT_LIMIT) -> dict:
    """Resolve declared GitHub base edges without guessing hidden dependencies."""
    raw = [_pr_copy(item) for item in raw_prs]
    drafts = [row for row in raw if bool(row.get("isDraft"))]
    prs = sorted(
        (row for row in raw if not bool(row.get("isDraft"))),
        key=lambda row: row["number"],
    )
    by_number = {row["number"]: row for row in prs}
    heads: dict[str, list[int]] = defaultdict(list)
    for row in prs:
        # A PR base lives in the base repository.  A same-named fork head is
        # not that base branch and must not create a false stack edge.
        if not bool(row.get("isCrossRepository")):
            heads[row["headRefName"]].append(row["number"])
    duplicate_heads = {
        head: sorted(numbers) for head, numbers in heads.items() if len(numbers) > 1
    }

    for row in prs:
        base = row["baseRefName"]
        if base == "main":
            row["parent_pr"] = None
            row["topology_state"] = "declared_main_root"
        elif len(heads.get(base, [])) == 1:
            row["parent_pr"] = heads[base][0]
            row["topology_state"] = "waiting_on_open_parent"
        elif len(heads.get(base, [])) > 1:
            row["parent_pr"] = None
            row["topology_state"] = "ambiguous_open_parent"
        else:
            row["parent_pr"] = None
            row["topology_state"] = "unresolved_non_main_base"

    cycle_numbers: set[int] = set()
    for start in by_number:
        order: list[int] = []
        positions: dict[int, int] = {}
        cursor: int | None = start
        while cursor is not None and cursor in by_number:
            if cursor in positions:
                cycle_numbers.update(order[positions[cursor] :])
                break
            positions[cursor] = len(order)
            order.append(cursor)
            cursor = by_number[cursor].get("parent_pr")
    for number in cycle_numbers:
        by_number[number]["topology_state"] = "declared_base_cycle"

    children: dict[int, list[int]] = defaultdict(list)
    for row in prs:
        parent = row.get("parent_pr")
        if parent in by_number:
            children[parent].append(row["number"])
    for number in children:
        children[number].sort()

    def depth(number: int, trail: frozenset[int] = frozenset()) -> int | None:
        row = by_number[number]
        if row["topology_state"] == "declared_main_root":
            return 0
        parent = row.get("parent_pr")
        if (
            parent is None
            or number in trail
            or row["topology_state"] == "declared_base_cycle"
        ):
            return None
        parent_depth = depth(parent, trail | {number})
        return None if parent_depth is None else parent_depth + 1

    for row in prs:
        row["stack_depth"] = depth(row["number"])
        row["child_prs"] = children.get(row["number"], [])

    stack_paths: list[dict] = []

    def add_paths(root: int, prefix: list[int]) -> None:
        path = prefix + [root]
        child_numbers = [n for n in children.get(root, []) if n not in path]
        if not child_numbers:
            first = by_number[path[0]]
            if len(path) > 1 or first["baseRefName"] != "main":
                stack_paths.append({"base": first["baseRefName"], "prs": path})
            return
        for child in child_numbers:
            add_paths(child, path)

    for row in prs:
        if row.get("parent_pr") is None and row["number"] not in cycle_numbers:
            add_paths(row["number"], [])

    ready_roots = [
        row["number"]
        for row in prs
        if row["topology_state"] == "declared_main_root"
        and (
            bool(row.get("isCrossRepository"))
            or row["headRefName"] not in duplicate_heads
        )
    ]
    return {
        "query_limit": limit,
        "limit_reached": len(raw) >= limit,
        "open_count": len(raw),
        "draft_count": len(drafts),
        "non_draft_count": len(prs),
        "main_based_count": sum(row["baseRefName"] == "main" for row in prs),
        "non_main_based_count": sum(row["baseRefName"] != "main" for row in prs),
        "open_parent_edge_count": sum(
            row.get("parent_pr") is not None for row in prs
        ),
        "unresolved_non_main_base_count": sum(
            row["topology_state"] == "unresolved_non_main_base" for row in prs
        ),
        "duplicate_head_branches": duplicate_heads,
        "declared_base_cycles": sorted(cycle_numbers),
        "declared_main_ready_prs": ready_roots,
        "stack_paths": sorted(stack_paths, key=lambda item: item["prs"]),
        "prs": prs,
    }


def parse_worktree_porcelain(text: str) -> list[dict]:
    records: list[dict] = []
    for block in text.split("\0\0"):
        fields = [field for field in block.split("\0") if field]
        if not fields:
            continue
        record: dict = {"detached": False, "locked": False, "prunable": False}
        for field in fields:
            key, _, value = field.partition(" ")
            if key in {"detached", "locked", "prunable"}:
                record[key] = True
                if value:
                    record[f"{key}_reason"] = value
            elif key == "worktree":
                record["path"] = value
            elif key == "HEAD":
                record["head"] = value
            elif key == "branch":
                record["branch"] = value.removeprefix("refs/heads/")
        if record.get("path"):
            records.append(record)
    return records


def _status_path(line: str) -> str:
    value = line[3:] if len(line) >= 4 else line
    return value.rsplit(" -> ", 1)[-1].strip('"')


def collect_worktrees(repo_root: Path, runner: Run = run) -> list[dict]:
    records = parse_worktree_porcelain(
        runner(["git", "worktree", "list", "--porcelain", "-z"], repo_root)
    )
    for record in records:
        path = Path(record["path"])
        record["exists"] = path.exists()
        record["verifiable"] = False
        record["dirty"] = None
        record["status_entry_count"] = None
        record["status_preview"] = []
        record["scratch_entries"] = []
        if not record["exists"]:
            record["recovery_state"] = "missing_registered_path"
            continue
        try:
            status = runner(
                [
                    "git",
                    "--no-optional-locks",
                    "status",
                    "--porcelain=v1",
                    "--untracked-files=all",
                ],
                path,
            )
        except InventoryError as exc:
            record["recovery_state"] = "unverifiable_existing_worktree"
            record["status_error"] = str(exc)
            continue
        lines = [line for line in status.splitlines() if line]
        record["verifiable"] = True
        record["dirty"] = bool(lines)
        record["status_entry_count"] = len(lines)
        record["status_preview"] = lines[:20]
        record["scratch_entries"] = [
            status_path
            for status_path in (_status_path(line) for line in lines)
            if Path(status_path).name.startswith(("RL_", "review-findings-pr"))
        ]
        record["recovery_state"] = "dirty_recovery" if lines else "clean_checkout"
    return records


_REVIEW_WORKTREE_RE = re.compile(r"^rev-(\d+)(?:[.-]|$)")
_FINDINGS_RE = re.compile(r"^review-findings-pr(\d+)(?:[.-]|$)")


def match_worktrees_to_prs(topology: dict, worktrees: list[dict]) -> None:
    prs = {row["number"]: row for row in topology["prs"]}
    by_branch: dict[str, set[int]] = defaultdict(set)
    by_oid: dict[str, set[int]] = defaultdict(set)
    for row in topology["prs"]:
        if not bool(row.get("isCrossRepository")):
            by_branch[row["headRefName"]].add(row["number"])
        if row.get("headRefOid"):
            by_oid[str(row["headRefOid"])].add(row["number"])
    for worktree in worktrees:
        matches: set[int] = set()
        matches.update(by_branch.get(str(worktree.get("branch", "")), set()))
        matches.update(by_oid.get(str(worktree.get("head", "")), set()))
        name_match = _REVIEW_WORKTREE_RE.match(Path(worktree["path"]).name)
        if name_match and int(name_match.group(1)) in prs:
            matches.add(int(name_match.group(1)))
        worktree["matched_open_prs"] = sorted(matches)


def scan_tmp_root(tmp_root: Path, registered_paths: set[Path]) -> dict:
    findings: list[dict] = []
    unregistered_worktrees: list[dict] = []
    scratch: list[dict] = []
    try:
        entries = list(tmp_root.iterdir())
    except OSError as exc:
        return {
            "scan_error": str(exc),
            "findings_files": [],
            "unregistered_review_paths": [],
            "scratch_paths": [],
        }
    registered = {path.resolve() for path in registered_paths}
    for entry in entries:
        name = entry.name
        finding_match = _FINDINGS_RE.match(name)
        if finding_match:
            try:
                size = entry.stat(follow_symlinks=False).st_size
            except OSError:
                size = None
            findings.append(
                {"path": str(entry), "pr": int(finding_match.group(1)), "bytes": size}
            )
            continue
        worktree_match = _REVIEW_WORKTREE_RE.match(name)
        if worktree_match and entry.resolve() not in registered:
            unregistered_worktrees.append(
                {
                    "path": str(entry),
                    "pr": int(worktree_match.group(1)),
                    "has_git_marker": (entry / ".git").exists() if entry.is_dir() else False,
                }
            )
            continue
        if name.startswith("RL_"):
            scratch.append({"path": str(entry), "is_dir": entry.is_dir()})
    return {
        "scan_error": None,
        "findings_files": sorted(findings, key=lambda item: (item["pr"], item["path"])),
        "unregistered_review_paths": sorted(
            unregistered_worktrees, key=lambda item: item["path"]
        ),
        "scratch_paths": sorted(scratch, key=lambda item: item["path"]),
    }


def parse_worker_processes(text: str) -> dict:
    all_processes: dict[int, dict] = {}
    for line in text.splitlines():
        match = re.match(r"\s*(\d+)\s+(\d+)\s+(.*)", line)
        if not match:
            continue
        pid, ppid, command = int(match.group(1)), int(match.group(2)), match.group(3)
        try:
            argv = shlex.split(command)
        except ValueError:
            argv = command.split()
        all_processes[pid] = {"pid": pid, "ppid": ppid, "argv": argv, "raw": command}

    workers: list[dict] = []
    for proc in all_processes.values():
        argv = proc["argv"]
        if not argv:
            continue
        executable = Path(argv[0]).name.lower()
        if executable == "codex" and ({"exec", "resume"} & set(argv[1:])):
            kind = "codex_cli_worker"
        elif (
            executable == "claude"
            and "--model" in argv
            and "--output-format" in argv
        ):
            kind = "claude_cli_worker"
        else:
            continue
        ancestry: list[str] = []
        cursor = proc
        seen: set[int] = set()
        while cursor and cursor["pid"] not in seen:
            seen.add(cursor["pid"])
            ancestry.append(cursor["raw"].lower())
            cursor = all_processes.get(cursor["ppid"])
        audit_hint = any(
            marker in command
            for command in ancestry
            for marker in (
                "orchestrate_audit",
                "codex_audit_runner",
                "audit-loop",
                "audit_loop",
            )
        )
        workers.append(
            {
                "pid": proc["pid"],
                "ppid": proc["ppid"],
                "kind": kind,
                "lane_hint": "audit" if audit_hint else "unknown",
            }
        )
    workers.sort(key=lambda item: item["pid"])
    return {
        "observed_worker_count": len(workers),
        "observed_audit_worker_count": sum(
            item["lane_hint"] == "audit" for item in workers
        ),
        "workers": workers,
    }


def collect_processes(repo_root: Path, runner: Run = run) -> dict:
    return parse_worker_processes(
        runner(["ps", "-axo", "pid=,ppid=,args="], repo_root)
    )


def compute_capacity(
    free_kib: int,
    observed_workers: int,
    observed_audit_workers: int,
    max_processes: int = DEFAULT_MAX_PROCESSES,
    min_free_kib: int = MIN_FREE_KIB,
    estimated_worktree_kib: int = ESTIMATED_WORKTREE_KIB,
) -> dict:
    if not 1 <= max_processes <= MAX_SHARED_PROCESSES:
        raise ValueError(
            f"max_processes must be between 1 and {MAX_SHARED_PROCESSES}"
        )
    process_slots = max(0, max_processes - observed_workers)
    if observed_audit_workers >= AUDIT_BUSY_SEATS:
        process_slots = min(process_slots, AUDIT_BUSY_REVIEW_CAP)
    disk_slots = max(0, (free_kib - min_free_kib) // estimated_worktree_kib)
    return {
        "free_kib": free_kib,
        "free_gib": round(free_kib / 1024 / 1024, 2),
        "minimum_free_kib": min_free_kib,
        "estimated_worktree_kib": estimated_worktree_kib,
        "disk_guard_pass": free_kib >= min_free_kib,
        "conservative_new_worktree_slots": disk_slots,
        "max_shared_worker_processes": max_processes,
        "observed_worker_processes": observed_workers,
        "observed_audit_worker_processes": observed_audit_workers,
        "review_process_slots": process_slots,
    }


def plan_slots(
    topology: dict,
    worktrees: list[dict],
    tmp_scan: dict,
    capacity: dict,
) -> dict:
    by_pr = {row["number"]: row for row in topology["prs"]}
    trees_by_pr: dict[int, list[dict]] = defaultdict(list)
    for worktree in worktrees:
        for number in worktree.get("matched_open_prs", []):
            trees_by_pr[number].append(worktree)
    findings_by_pr: dict[int, list[str]] = defaultdict(list)
    for item in tmp_scan.get("findings_files", []):
        findings_by_pr[item["pr"]].append(item["path"])
    unregistered_by_pr: dict[int, list[dict]] = defaultdict(list)
    for item in tmp_scan.get("unregistered_review_paths", []):
        unregistered_by_pr[item["pr"]].append(item)

    recovery_actions: list[dict] = []
    new_candidates: list[dict] = []
    for number in topology["declared_main_ready_prs"]:
        row = by_pr[number]
        trees = trees_by_pr.get(number, [])
        findings = findings_by_pr.get(number, [])
        unregistered = unregistered_by_pr.get(number, [])
        if trees or findings or unregistered:
            recovery_actions.append(
                {
                    "pr": number,
                    "head": row["headRefName"],
                    "worktrees": [tree["path"] for tree in trees],
                    "unregistered_review_paths": [
                        item["path"] for item in unregistered
                    ],
                    "external_findings": findings,
                    "states": (
                        [tree["recovery_state"] for tree in trees]
                        + ["unregistered_review_path"] * len(unregistered)
                        + ["external_findings_file"] * len(findings)
                    ),
                    "action": "inspect_recovery_artifacts_before_dispatch",
                }
            )
            continue
        new_candidates.append(
            {
                "pr": number,
                "head": row["headRefName"],
                "title": row.get("title", ""),
                "external_findings": findings_by_pr.get(number, []),
            }
        )

    new_candidates.sort(key=lambda item: item["pr"])
    suppression_reasons = []
    if topology["limit_reached"]:
        suppression_reasons.append(
            "GitHub query limit reached; topology may be incomplete"
        )
    if tmp_scan.get("scan_error"):
        suppression_reasons.append(
            "temporary-root recovery scan failed; recovery state is unknown"
        )
    if suppression_reasons:
        slot_count = 0
        suppression = "; ".join(suppression_reasons)
    else:
        slot_count = min(
            len(new_candidates),
            capacity["review_process_slots"],
            capacity["conservative_new_worktree_slots"],
        )
        suppression = None
    ready_slots = []
    for slot, candidate in enumerate(new_candidates[:slot_count], 1):
        ready_slots.append(
            {
                "slot": slot,
                "action": "candidate_for_new_isolated_worktree",
                "required_before_dispatch": [
                    "cumulative_history_check",
                    "merge_base_delta_check",
                ],
                **candidate,
            }
        )
    return {
        "readiness_definition": (
            "declared main base + no detected registered/unregistered checkout or "
            "external findings artifact; scheduling only, not review, science, "
            "merge, audit, or landing readiness"
        ),
        "ordering": "deterministic ascending PR number; no scientific priority implied",
        "recovery_actions": recovery_actions,
        "new_candidate_count": len(new_candidates),
        "ready_new_worktree_slot_count": len(ready_slots),
        "ready_slots": ready_slots,
        "slot_suppression_reason": suppression,
    }


def collect_snapshot(
    repo_root: Path,
    tmp_root: Path,
    limit: int,
    max_processes: int,
    runner: Run = run,
) -> dict:
    raw_prs = fetch_open_prs(repo_root, limit=limit, runner=runner)
    topology = analyze_topology(raw_prs, limit=limit)
    worktrees = collect_worktrees(repo_root, runner=runner)
    match_worktrees_to_prs(topology, worktrees)
    tmp_scan = scan_tmp_root(tmp_root, {Path(item["path"]) for item in worktrees})
    processes = collect_processes(repo_root, runner=runner)
    try:
        free_kib = shutil.disk_usage(tmp_root).free // 1024
    except OSError as exc:
        raise InventoryError(f"cannot read disk capacity for {tmp_root}: {exc}") from exc
    capacity = compute_capacity(
        free_kib,
        processes["observed_worker_count"],
        processes["observed_audit_worker_count"],
        max_processes=max_processes,
    )
    schedule = plan_slots(topology, worktrees, tmp_scan, capacity)
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "read_only": True,
        "repo_root": str(repo_root),
        "tmp_root": str(tmp_root),
        "topology_scope": (
            "declared GitHub baseRefName edges only; cumulative-history and hidden "
            "science dependencies remain worker preflight obligations"
        ),
        "topology": topology,
        "recovery": {
            "registered_worktrees": worktrees,
            **tmp_scan,
        },
        "processes": processes,
        "capacity": capacity,
        "schedule": schedule,
    }


def _short(text: str, width: int = 78) -> str:
    text = " ".join(text.split())
    return text if len(text) <= width else text[: width - 1] + "…"


def render(snapshot: dict, max_items: int) -> str:
    topology = snapshot["topology"]
    recovery = snapshot["recovery"]
    capacity = snapshot["capacity"]
    schedule = snapshot["schedule"]
    matched_trees = [
        item for item in recovery["registered_worktrees"] if item["matched_open_prs"]
    ]
    lines = [
        "Review-loop backlog inventory (READ ONLY)",
        (
            f"PRs: {topology['non_draft_count']} non-draft open "
            f"({topology['main_based_count']} main-based, "
            f"{topology['non_main_based_count']} non-main-based; "
            f"{topology['draft_count']} drafts excluded)"
        ),
        (
            f"Declared topology: {topology['open_parent_edge_count']} open-parent "
            f"edges, {topology['unresolved_non_main_base_count']} unresolved bases, "
            f"{len(topology['declared_base_cycles'])} cycle nodes"
        ),
        (
            f"Resources: {capacity['free_gib']:.2f} GiB free; 5 GiB guard "
            f"{'PASS' if capacity['disk_guard_pass'] else 'BLOCKED'}; "
            f"{capacity['conservative_new_worktree_slots']} conservative disk slots; "
            f"{capacity['observed_worker_processes']}/"
            f"{capacity['max_shared_worker_processes']} worker CLIs observed; "
            f"{capacity['review_process_slots']} process slots"
        ),
        (
            f"Recovery: {len(recovery['registered_worktrees'])} registered worktrees "
            f"({len(matched_trees)} matched to open PRs); "
            f"{len(recovery['unregistered_review_paths'])} unregistered rev-* paths; "
            f"{len(recovery['findings_files'])} external findings files; "
            f"{len(recovery['scratch_paths'])} top-level RL_* paths"
        ),
        (
            f"Ready new-worktree slots: {schedule['ready_new_worktree_slot_count']} "
            f"of {schedule['new_candidate_count']} declared-main candidates"
        ),
        (
            "  Each candidate still requires cumulative-history and merge-base delta "
            "checks; scheduling readiness replaces no lens or gate."
        ),
    ]
    if topology["limit_reached"]:
        lines.append("  BLOCKED: GitHub query limit reached; rerun with a higher --limit.")
    if recovery.get("scan_error"):
        lines.append(
            "  BLOCKED: temporary-root recovery scan failed; no new worktree "
            f"slots scheduled ({_short(recovery['scan_error'])})."
        )
    if topology["duplicate_head_branches"]:
        lines.append(
            f"  AMBIGUOUS: {len(topology['duplicate_head_branches'])} duplicate head branches."
        )
    if matched_trees:
        lines.append("Existing open-PR worktrees (inspect ownership and recover first):")
        for item in matched_trees[:max_items]:
            prs = ", ".join(f"#{number}" for number in item["matched_open_prs"])
            lines.append(f"  {prs} {item['recovery_state']} — {item['path']}")
    if schedule["recovery_actions"]:
        lines.append("Recovery actions (inspect ownership; never launch a duplicate):")
        for item in schedule["recovery_actions"][:max_items]:
            paths = (
                item["worktrees"]
                + item["unregistered_review_paths"]
                + item["external_findings"]
            )
            lines.append(
                f"  #{item['pr']} {item['head']} — {', '.join(item['states'])} — "
                f"{', '.join(paths)}"
            )
    if schedule["ready_slots"]:
        lines.append("Candidate slots (ascending PR number only):")
        for item in schedule["ready_slots"]:
            suffix = " [findings recovery]" if item["external_findings"] else ""
            lines.append(
                f"  slot {item['slot']}: #{item['pr']} {item['head']}{suffix} — "
                f"{_short(item['title'])}"
            )
    unresolved = [
        row
        for row in topology["prs"]
        if row["topology_state"] == "unresolved_non_main_base"
    ]
    if unresolved:
        lines.append("Unresolved non-main bases (not schedulable):")
        for item in unresolved[:max_items]:
            lines.append(
                f"  #{item['number']} {item['headRefName']} — base {item['baseRefName']}"
            )
    if topology["stack_paths"]:
        lines.append("Declared stack order (bottom-up; truncated display):")
        for item in topology["stack_paths"][:max_items]:
            chain = " -> ".join(f"#{number}" for number in item["prs"])
            lines.append(f"  base {item['base']}: {chain}")
        hidden = len(topology["stack_paths"]) - max_items
        if hidden > 0:
            lines.append(f"  … {hidden} additional paths; use --json for the full inventory")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print the full JSON snapshot")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    parser.add_argument("--max-items", type=int, default=20)
    parser.add_argument("--max-processes", type=int, default=DEFAULT_MAX_PROCESSES)
    parser.add_argument(
        "--tmp-root",
        type=Path,
        default=Path(os.environ.get("TMPDIR") or "/tmp"),
        help="filesystem/root used by review worktrees (default: TMPDIR or /tmp)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if (
        args.limit <= 0
        or args.max_items <= 0
        or not 1 <= args.max_processes <= MAX_SHARED_PROCESSES
    ):
        print(
            f"limit/max-items must be positive and max-processes must be 1-"
            f"{MAX_SHARED_PROCESSES}",
            file=sys.stderr,
        )
        return 2
    try:
        snapshot = collect_snapshot(
            REPO_ROOT,
            args.tmp_root.resolve(),
            limit=args.limit,
            max_processes=args.max_processes,
        )
    except InventoryError as exc:
        print(f"review-loop inventory failed closed: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(snapshot, indent=2, sort_keys=True))
    else:
        print(render(snapshot, args.max_items))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
