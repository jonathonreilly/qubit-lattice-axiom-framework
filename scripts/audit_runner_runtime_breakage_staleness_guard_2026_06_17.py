#!/usr/bin/env python3
"""Verify runtime-failure runner breakage entries against current caches.

This is a source-side audit-unblock guard. It does not edit audit results or
rerun heavy science runners. It checks whether entries currently labelled
`timeout` or `nonzero_exit` in `runner_breakage_inventory.json` still represent
live evidence blockers under the current SHA-pinned runner-cache policy.
"""
from __future__ import annotations

import json
from pathlib import Path

import runner_cache as rc

REPO_ROOT = Path(__file__).resolve().parent.parent
INVENTORY = REPO_ROOT / "docs/audit/data/runner_breakage_inventory.json"
TARGET_REASONS = ("nonzero_exit", "timeout")


def repo_relative_runner(raw: str) -> str:
    """Return a normalized repo-relative scripts/ path, or raise ValueError."""
    p = Path(raw)
    if p.is_absolute():
        try:
            p = p.resolve().relative_to(REPO_ROOT)
        except ValueError as exc:
            raise ValueError(f"outside repo: {raw}") from exc
    if not p.parts or p.parts[0] != "scripts" or p.suffix != ".py":
        raise ValueError(f"not a scripts/*.py runner: {raw}")
    return p.as_posix()


def cache_ok(runner: str) -> tuple[bool, str]:
    status = rc.cache_status(runner)
    cache_path, header, _body = rc.load_cache(runner)
    if status != "fresh":
        return False, f"cache_status={status} path={cache_path.relative_to(REPO_ROOT)}"
    if not header:
        return False, f"cache header missing path={cache_path.relative_to(REPO_ROOT)}"
    if header.get("status") != "ok":
        return False, f"header status={header.get('status')!r}"
    if str(header.get("exit_code")) != "0":
        return False, f"header exit_code={header.get('exit_code')!r}"
    return True, f"fresh ok {cache_path.relative_to(REPO_ROOT)}"


def main() -> int:
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    broken = inventory.get("broken_runners", [])

    examined: list[tuple[str, str, str]] = []
    failures: list[str] = []
    counts = {reason: 0 for reason in TARGET_REASONS}

    for entry in broken:
        reason = entry.get("reason")
        if reason not in TARGET_REASONS:
            continue
        counts[reason] += 1
        raw_runner = str(entry.get("runner_path", ""))
        try:
            runner = repo_relative_runner(raw_runner)
        except ValueError as exc:
            failures.append(f"{reason}: {raw_runner}: {exc}")
            continue
        ok, detail = cache_ok(runner)
        examined.append((reason, runner, detail))
        if not ok:
            failures.append(f"{reason}: {runner}: {detail}")

    print("runtime_breakage_staleness_guard_2026_06_17")
    print(f"inventory: {INVENTORY.relative_to(REPO_ROOT)}")
    print(f"inventory_runner_timeout_sec: {inventory.get('runner_timeout_sec')}")
    print(f"target_reasons: {', '.join(TARGET_REASONS)}")
    print(f"target_entries: {sum(counts.values())}")
    for reason in TARGET_REASONS:
        print(f"  {reason}: {counts[reason]}")
    print(f"fresh_ok_entries: {len(examined) - len(failures)}")

    if examined:
        print("checked_runners:")
        for reason, runner, detail in examined:
            print(f"  - {reason}: {runner}: {detail}")

    if failures:
        print("FAIL: live runtime-failure entries remain:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print(
        "PASS: all timeout/nonzero_exit inventory entries have fresh "
        "status=ok caches on the current source tree."
    )
    print(
        "Scope note: missing_runner_file entries are intentionally out of "
        "scope for this guard; they are path-resolution issues, not runtime "
        "timeout/nonzero evidence."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
