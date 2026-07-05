#!/usr/bin/env python3
"""Guard stale audit runner-path canonicalization.

This checks the source-side tooling behavior only. It does not edit audit
results, runner inventories, ledgers, or queues.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_module(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {rel}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check(label: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    print(f"{status}: {label}{(' -- ' + detail) if detail else ''}")
    if not ok:
        raise AssertionError(label)


def main() -> int:
    audit_runner = load_module("codex_audit_runner_under_test", "scripts/codex_audit_runner.py")
    deps = load_module("audit_packet_script_deps_under_test", "scripts/audit_packet_script_deps.py")

    cases = {
        "frontier_staggered_cycle_battery.py": "scripts/frontier_staggered_cycle_battery.py",
        "/Users/jonreilly/Projects/Physics/.claude/worktrees/sleepy-cerf/scripts/frontier_gravitational_time_dilation.py": "scripts/frontier_gravitational_time_dilation.py",
        "scripts/frontier_lorentz_derived.py": "scripts/frontier_lorentz_derived.py",
    }
    for raw, expected in cases.items():
        for module_name, module in [
            ("codex_audit_runner", audit_runner),
            ("audit_packet_script_deps", deps),
        ]:
            got = module.canonical_runner_path(raw)
            check(f"{module_name} canonicalizes {Path(raw).name}", got == expected, got)
            check(f"{module_name} canonical target exists", (ROOT / got).exists(), got)

    inventory_path = ROOT / "docs" / "audit" / "data" / "runner_breakage_inventory.json"
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    missing_entries = [
        entry for entry in inventory["broken_runners"]
        if entry.get("reason") == "missing_runner_file"
    ]
    unresolved = []
    for entry in missing_entries:
        raw = entry["runner_path"]
        canonical = audit_runner.canonical_runner_path(raw)
        if not (ROOT / canonical).exists():
            unresolved.append(raw)
    check(
        "current missing_runner_file inventory is basename-recoverable",
        not unresolved,
        f"checked={len(missing_entries)} unresolved={len(unresolved)}",
    )

    prompt = audit_runner.render_prompt(
        {
            "claim_id": "cycle_battery_note_2026-04-10",
            "note_path": "docs/CYCLE_BATTERY_NOTE_2026-04-10.md",
            "runner_path": "frontier_staggered_cycle_battery.py",
            "claim_type": "bounded_theorem",
        },
        {},
        "runner={{RUNNER_PATH}}\nsource={{RUNNER_SOURCE}}\nstdout={{RUNNER_STDOUT}}",
        runner_timeout_sec=0,
        use_cache=False,
        skip_runner_stdout=True,
    )
    check("render_prompt exposes canonical runner path", "runner=scripts/frontier_staggered_cycle_battery.py" in prompt)
    check("render_prompt reads runner source through canonical path", "[runner missing on disk" not in prompt)
    check("render_prompt preserves no-runner stdout suppression", "stdout=(stdout suppressed by --no-runner)" in prompt)

    print("SUMMARY: stale runner references resolve to checked-in scripts before audit prompt rendering.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
