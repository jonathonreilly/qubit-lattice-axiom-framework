#!/usr/bin/env python3
"""
frontier_d3_lower_bound_source_packet_gate_2026_06_06.py
--------------------------------------------------------

Audit-gate checker for the D3 dimension-selection lower-bound parent row.

This is not a dimension-selection theorem. It checks whether the current-main
source packet addresses the live runner-artifact issue recorded for
`dimension_selection_note`:

  runner_artifact_issue: include the finite-k bridge runner source, original
  dimension runner source/cache, and source-packet verifier output so the
  displayed beta, I_3, and sign computations can be independently inspected.

The runner verifies that the retained bounded finite-k sign bridge is already
audited clean, that the lower-bound V2 sign row is already audited clean, and
that the remaining parent-row packet artifacts are present, linked, SHA-fresh,
and cache-backed on current main. It does not update the audit ledger.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
ACTIVE_QUEUE = ROOT / "docs" / "repo" / "ACTIVE_REVIEW_QUEUE.md"
PARENT_NOTE = ROOT / "docs" / "DIMENSION_SELECTION_NOTE.md"
V2_NOTE = ROOT / "docs" / "DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_V2_2026-05-20.md"
FINITE_K_NOTE = ROOT / "docs" / "DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md"
SOURCE_PACKET_RUNNER = ROOT / "scripts" / "dimension_selection_parent_source_packet_manifest_2026_06_05.py"
SOURCE_PACKET_CACHE = ROOT / "logs" / "runner-cache" / "dimension_selection_parent_source_packet_manifest_2026_06_05.txt"
SOURCE_PACKET_JSON = ROOT / "outputs" / "dimension_selection_parent_source_packet_manifest_2026_06_05.json"
FINITE_K_PREMISE_QUOTES = (
    "This note takes the second route.  It does **not** use Fermat, WKB, or stationary phase as the load-bearing sign argument.  It differentiates the actual finite-k, finite-lattice, layer-normalized propagator used by `scripts/frontier_dimension_selection.py`.",
    "This supplies the finite-k sign bridge that the V2 lower-bound note was missing for the actual runner surface.",
)
LOWER_V2_PREMISE_QUOTES = (
    "is **positive (attractive)** for `d = 3, 4, 5` and **negative (repulsive)** for `d = 1, 2`, for the runner's fixed finite-k geometry and analytic potential family.",
    "The derivation admits the choice to use the runner's analytic potential family as the finite test surface, but the profile identities themselves are proved below on that surface rather than imported from a textbook.",
)
PARENT_PREMISE_QUOTES = (
    "Only the first statement is binding in this row. The second statement remains context for separate upper-bound work and is not a theorem of this packet.",
    "This is finite-runner lower-bound support only, not a unique-dimension theorem. This row does not authorize any framework-baseline rewrite.",
    "The current audit blocker is a packet/runner-artifact gap: the parent repair runner verifies the narrowed prose and finite-k sign replay, but the displayed `beta` and `I_3` entries come from the original dimension-selection runner, and the parent runner imports the bridge through a dynamic import.",
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" -- {detail}" if detail != "" else ""
    print(f"[{status}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def one_line(text: str) -> str:
    return " ".join(text.split())


def _norm(text: str) -> str:
    return " ".join(text.split())


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_cache(path: Path) -> dict[str, str]:
    text = read(path)
    header, _, _stdout = text.partition("----- stdout -----")
    out = {"_text": text}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip()
    return out


def ledger_rows() -> dict[str, dict[str, Any]]:
    raw = json.loads(read(LEDGER))["rows"]
    rows = raw.values() if isinstance(raw, dict) else raw
    return {
        row["claim_id"]: row
        for row in rows
        if isinstance(row, dict) and "claim_id" in row
    }


def require_row(rows: dict[str, dict[str, Any]], claim_id: str) -> dict[str, Any]:
    if claim_id not in rows:
        check(f"ledger row exists: {claim_id}", False, "missing")
        return {}
    check(f"ledger row exists: {claim_id}", True)
    return rows[claim_id]


def gate_dependency_note(label: str, row: dict[str, Any], note_path: Path, quotes: tuple[str, ...]) -> None:
    print(
        "  [info] "
        f"{label}: live claim_scope={row.get('claim_scope')!r} "
        f"effective_status={row.get('effective_status')!r} "
        f"audit_status={row.get('audit_status')!r} "
        "(audit-lane-owned; not gated)"
    )
    note_text = _norm(read(note_path)) if note_path.is_file() else ""
    check(f"{label} dependency note exists", note_path.is_file(), note_path.relative_to(ROOT))
    for quote in quotes:
        check(
            f"{label} note states premise verbatim: {quote[:60]}...",
            _norm(quote) in note_text,
            f"len={len(quote)}",
        )


def run_active_queue_and_status_checks(rows: dict[str, dict[str, Any]]) -> None:
    print("A. ledger and active-queue status")
    queue_text = read(ACTIVE_QUEUE)
    check(
        "active queue still carries the D3 lower-bound sign item",
        "2026-05-20-d3-lower-bound-bridge-sign" in queue_text,
    )

    finite_k = require_row(rows, "dimension_selection_finite_k_centroid_sign_bridge_note_2026-05-25")
    lower_v2 = require_row(rows, "dimension_selection_lower_bound_bridge_v2_2026-05-20")
    parent = require_row(rows, "dimension_selection_note")

    gate_dependency_note("finite-k sign bridge", finite_k, FINITE_K_NOTE, FINITE_K_PREMISE_QUOTES)
    gate_dependency_note("lower-bound V2 sign bridge", lower_v2, V2_NOTE, LOWER_V2_PREMISE_QUOTES)
    gate_dependency_note("parent dimension-selection row", parent, PARENT_NOTE, PARENT_PREMISE_QUOTES)


def run_source_packet_checks() -> None:
    print("B. source-packet artifact issue")
    parent_text = read(PARENT_NOTE)
    flat_parent = one_line(parent_text)
    source_packet_text = read(SOURCE_PACKET_RUNNER)
    cache = parse_cache(SOURCE_PACKET_CACHE)

    required_paths = [
        "scripts/frontier_dimension_selection_lower_bound_parent_repair.py",
        "logs/runner-cache/frontier_dimension_selection_lower_bound_parent_repair.txt",
        "scripts/frontier_dimension_selection.py",
        "logs/runner-cache/frontier_dimension_selection.txt",
        "docs/DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md",
        "scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py",
        "logs/runner-cache/frontier_dimension_selection_finite_k_centroid_sign_bridge.txt",
        "outputs/dimension_selection_finite_k_centroid_sign_bridge_2026-05-25.json",
        "scripts/dimension_selection_parent_source_packet_manifest_2026_06_05.py",
        "logs/runner-cache/dimension_selection_parent_source_packet_manifest_2026_06_05.txt",
        "outputs/dimension_selection_parent_source_packet_manifest_2026_06_05.json",
    ]
    for rel in required_paths:
        check(f"required packet path exists: {rel}", (ROOT / rel).exists())
        check(f"parent note links packet path: {rel}", rel in parent_text)

    manifest_labels = [
        "finite_k_bridge_runner",
        "original_cache",
        "cache_sha_fresh",
        "bridge_json_fail_count_zero",
        "source_full_length",
        "SUMMARY: DIMENSION SELECTION SOURCE PACKET PASS=",
    ]
    for label in manifest_labels:
        check(f"source-packet verifier contains label: {label}", label in source_packet_text)

    check(
        "source-packet cache belongs to current verifier",
        cache.get("runner") == "scripts/dimension_selection_parent_source_packet_manifest_2026_06_05.py",
        cache.get("runner"),
    )
    check(
        "source-packet cache SHA is fresh",
        cache.get("runner_sha256") == sha256_file(SOURCE_PACKET_RUNNER),
        f"{cache.get('runner_sha256')} == {sha256_file(SOURCE_PACKET_RUNNER)}",
    )
    check(
        "source-packet cache exits cleanly",
        cache.get("exit_code") == "0" and cache.get("status") == "ok",
        f"exit_code={cache.get('exit_code')} status={cache.get('status')}",
    )
    for snippet in (
        "SUMMARY: DIMENSION SELECTION SOURCE PACKET PASS=57 FAIL=0",
        "cache_sha_fresh:original_cache",
        "cache_snippet_present:original_cache:I_3/P = <1e-10",
        "cache_snippet_present:finite_k_bridge_cache:SUMMARY: PASS=56 FAIL=0",
    ):
        check(f"source-packet cache contains snippet: {snippet}", snippet in cache["_text"])

    if SOURCE_PACKET_JSON.exists():
        payload = json.loads(read(SOURCE_PACKET_JSON))
    else:
        payload = {}
    check(
        "source-packet verifier JSON exists",
        SOURCE_PACKET_JSON.exists(),
        SOURCE_PACKET_JSON.relative_to(ROOT),
    )
    check(
        "source-packet verifier JSON reports zero failures",
        payload.get("summary", {}).get("fail") == 0,
        payload.get("summary"),
    )

    boundaries = [
        "finite-runner lower-bound support only",
        "not a unique-dimension theorem",
        "does not authorize any framework-baseline rewrite",
        "This row does not claim:",
        "framework-internal upper-bound derivation",
    ]
    for phrase in boundaries:
        check(f"parent note keeps boundary phrase: {phrase}", phrase in flat_parent)


def run_note_gate_checks() -> None:
    print("C. supporting note boundaries")
    v2 = read(V2_NOTE)
    finite = read(FINITE_K_NOTE)
    combined_flat = one_line("\n".join((v2, finite, read(PARENT_NOTE))))
    for phrase in (
        "Retained finite-k sign bridge",
        "not a ledger retag",
        "not full retained dimension selection",
        "does not authorize changing the minimal axiom line",
    ):
        check(f"finite-k/V2 boundary phrase present: {phrase}", phrase in combined_flat)

    forbidden = [
        "full retained spatial d = 3 closure",
        "Z^3 has been derived from A1 alone",
        "repo-wide framework-baseline rewrite is authorized",
        "self-consistency uniquely selects d = 3",
    ]
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in combined_flat)


def main() -> int:
    print("D3 lower-bound source-packet audit gate")
    print("actual_current_surface_status: exact-support")
    print("trace_class: direct_blocker_closure")
    print("reachability_to_target: partially_closes")
    print("proposal_allowed: false")
    print("audit_required_before_effective_retained: true")
    print()
    rows = ledger_rows()
    run_active_queue_and_status_checks(rows)
    run_source_packet_checks()
    run_note_gate_checks()
    print()
    print(f"SCORECARD: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if PASS_COUNT > 0 and FAIL_COUNT == 0:
        print(
            "VERDICT: exact support that the current-main source packet exposes "
            "the artifacts named by the parent D3 lower-bound runner-artifact "
            "issue. This does not retag the audit ledger or prove full D=3 "
            "dimension selection."
        )
        return 0
    print("VERDICT: source-packet gate failed; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
