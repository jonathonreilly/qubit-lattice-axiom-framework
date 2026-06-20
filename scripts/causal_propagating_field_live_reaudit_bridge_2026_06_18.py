#!/usr/bin/env python3
"""Verifier for the causal propagating-field live re-audit bridge.

This runner does not replace the primary finite replay
``scripts/causal_propagating_field.py``.  It checks that the archived failed
row is explicitly retired as evidence and that the current live packet exposes
the executable runner/cache/manifest surface needed for an independent
re-audit of the narrowed bounded claim.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

ARCHIVED_NOTE = ROOT / "archive_unlanded/causal-field-stale-runners-2026-04-30/CAUSAL_PROPAGATING_FIELD_NOTE.md"
LIVE_NOTE = ROOT / "docs/CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md"
BRIDGE_NOTE = ROOT / "docs/CAUSAL_PROPAGATING_FIELD_LIVE_REAUDIT_BRIDGE_NOTE_2026-06-18.md"
PRIMARY_RUNNER = ROOT / "scripts/causal_propagating_field.py"
PRIMARY_CACHE = ROOT / "logs/runner-cache/causal_propagating_field.txt"
MANIFEST_RUNNER = ROOT / "scripts/causal_propagating_field_source_packet_manifest_2026_06_05.py"
MANIFEST_CACHE = ROOT / "logs/runner-cache/causal_propagating_field_source_packet_manifest_2026_06_05.txt"
MANIFEST_JSON = ROOT / "outputs/causal_propagating_field_source_packet_manifest_2026_06_05.json"
DISPATCH_SIDECAR = ROOT / "docs/audit/data/causal_field_live_reaudit_queue_2026-06-18.json"


results: list[tuple[str, bool, str]] = []


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def record(name: str, condition: bool, detail: str) -> None:
    results.append((name, bool(condition), detail))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def parse_cache_header(path: Path) -> dict[str, str]:
    text = read(path)
    header, _, _stdout = text.partition("----- stdout -----")
    parsed = {"_text": text}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        parsed[key.strip()] = value.strip()
    return parsed


def main() -> int:
    for path in [
        ARCHIVED_NOTE,
        LIVE_NOTE,
        BRIDGE_NOTE,
        PRIMARY_RUNNER,
        PRIMARY_CACHE,
        MANIFEST_RUNNER,
        MANIFEST_CACHE,
        MANIFEST_JSON,
        DISPATCH_SIDECAR,
    ]:
        record(f"path exists: {rel(path)}", path.exists(), rel(path))

    archived = read(ARCHIVED_NOTE)
    live = read(LIVE_NOTE)
    bridge = read(BRIDGE_NOTE)
    runner = read(PRIMARY_RUNNER)
    primary_cache = parse_cache_header(PRIMARY_CACHE)
    manifest_cache = read(MANIFEST_CACHE)
    manifest_json = json.loads(read(MANIFEST_JSON))
    dispatch_sidecar = json.loads(read(DISPATCH_SIDECAR))

    record("archived note is explicitly retracted", "RETRACTED 2026-04-30" in archived, "archive note carries retraction status")
    record("archived note carries do-not-cite warning", "Do NOT cite" in archived, "old 0.63/0.45 table is not live evidence")
    record("archived note points to live packet", rel(LIVE_NOTE) in archived, "archive links current live packet")
    record("archived note does not restore old positive claim", "not a live authority" in archived, "archive remains historical only")

    record("live note has bounded-support status", "bounded-support live packet" in live, "live packet is not bare retained")
    record("live note names primary runner", rel(PRIMARY_RUNNER) in live, "primary runner is source-visible")
    record("live note names primary cache", rel(PRIMARY_CACHE) in live, "primary cache is source-visible")
    record("live note names manifest runner", rel(MANIFEST_RUNNER) in live, "manifest runner is source-visible")
    record("live note excludes stale 0.63/0.45 table", "does not reproduce that table" in live, "old table is not restored")
    record("live note excludes physical wave-speed claim", "physical wave speed" in live, "physical-speed promotion is excluded")

    for marker in [
        "def _instantaneous_field",
        "def _forward_only_field",
        "def _dynamic_field",
        "ASSERTIONS:",
        "archived 0.63/0.45 positive table is not reproduced",
    ]:
        record(f"primary runner marker: {marker}", marker in runner, marker)
    record("primary runner is substantive", len(runner) > 8000, f"bytes={len(runner)}")

    record("primary cache runner path matches", primary_cache.get("runner") == rel(PRIMARY_RUNNER), primary_cache.get("runner", ""))
    record("primary cache sha is fresh", primary_cache.get("runner_sha256") == sha256(PRIMARY_RUNNER), primary_cache.get("runner_sha256", ""))
    record("primary cache exits cleanly", primary_cache.get("exit_code") == "0" and primary_cache.get("status") == "ok", str(primary_cache))
    for snippet in [
        "ASSERTIONS: PASS",
        "current live c=1 ratio: 1.456",
        "current live c=0.5 ratio: 0.938",
        "current live forward ratio: 0.668",
        "archived 0.63/0.45 positive table is not reproduced",
    ]:
        record(f"primary cache snippet: {snippet}", snippet in primary_cache["_text"], snippet)

    record("manifest cache passes", "SUMMARY: CAUSAL PROPAGATING FIELD SOURCE PACKET PASS=30 FAIL=0" in manifest_cache, "manifest cache fail count is zero")
    record("manifest json fail count is zero", manifest_json["summary"]["fail"] == 0, str(manifest_json["summary"]))
    record("manifest json points at live note", manifest_json["note"] == rel(LIVE_NOTE), manifest_json["note"])

    for phrase in [
        "re-audit target",
        "does not edit audit results",
        "does not restore the archived",
        "bounded finite configured replay",
    ]:
        record(f"bridge note boundary phrase: {phrase}", phrase in bridge, phrase)
    record("bridge note is meta, not a bounded theorem row", "**Claim type:** meta" in bridge, "bridge is dispatch/readiness metadata")
    record("bridge note names dispatch sidecar", rel(DISPATCH_SIDECAR) in bridge, rel(DISPATCH_SIDECAR))

    targets = [
        target
        for group in dispatch_sidecar.get("groups", [])
        for target in group.get("targets", [])
    ]
    record("dispatch sidecar uses supported schema", dispatch_sidecar.get("schema") == "promotion_reaudit_queue.v1", dispatch_sidecar.get("schema", ""))
    record("dispatch sidecar is not an audit verdict", dispatch_sidecar.get("status") == "dispatcher_only_not_audit_verdict", dispatch_sidecar.get("status", ""))
    record("dispatch sidecar forbids use as evidence", dispatch_sidecar.get("must_not_apply_ledger_changes_from_this_file") is True, str(dispatch_sidecar.get("must_not_apply_ledger_changes_from_this_file")))
    record("dispatch sidecar has exactly one target", len(targets) == 1, f"targets={len(targets)}")
    if targets:
        target = targets[0]
        record("dispatch sidecar targets live packet row", target.get("claim_id") == "causal_propagating_field_live_packet_note_2026-06-05", target.get("claim_id", ""))
        record("dispatch sidecar expects current retained-bounded row", target.get("current_claim_type") == "bounded_theorem" and target.get("current_audit_status") == "audited_clean" and target.get("current_effective_status") == "retained_bounded", str(target))
        record("dispatch sidecar excludes archived table as evidence", any("0.63 / 0.45" in item for item in dispatch_sidecar.get("forbidden_context", [])), "archived table forbidden")

    passed = sum(1 for _, ok, _ in results if ok)
    failed = len(results) - passed
    print("=" * 96)
    print("CAUSAL PROPAGATING FIELD LIVE RE-AUDIT BRIDGE")
    print("=" * 96)
    for name, ok, detail in results:
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: {detail}")
    print("=" * 96)
    print(f"SUMMARY: CAUSAL FIELD LIVE REAUDIT BRIDGE PASS={passed} FAIL={failed}")
    print("=" * 96)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
