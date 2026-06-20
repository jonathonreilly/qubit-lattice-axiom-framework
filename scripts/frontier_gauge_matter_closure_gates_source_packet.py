#!/usr/bin/env python3
"""Gauge/matter closure gates source-packet verifier.

Authority note:
    docs/GAUGE_MATTER_CLOSURE_GATES_2026-04-12.md

This runner checks that the old closure-gates memo is packaged as a
superseded route memo, not as a live retained/positive-theorem authority.  It
verifies that the canonical replacement notes are named and that their own
guardrails remain explicit.

Exit code: 0 on full PASS, 1 on any FAIL.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, passed: bool, detail: str) -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if passed else "FAIL"
    if passed:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"[{status}] {name}: {detail}")
    return passed


def read_text(rel_path: str) -> str:
    return (REPO_ROOT / rel_path).read_text(encoding="utf-8")


def sha256_file(rel_path: str) -> str:
    return hashlib.sha256((REPO_ROOT / rel_path).read_bytes()).hexdigest()


def require_fragment(label: str, text: str, needle: str) -> None:
    check(label, needle in text, needle)


def cache_header(cache_text: str) -> dict[str, str]:
    header: dict[str, str] = {}
    for line in cache_text.splitlines():
        if line == "----- stdout -----":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            header[key.strip()] = value.strip()
    return header


def check_cache(*, runner: str, cache: str, fragments: list[str]) -> None:
    runner_path = REPO_ROOT / runner
    cache_path = REPO_ROOT / cache
    runner_exists = runner_path.exists()
    cache_exists = cache_path.exists()
    check(f"{runner} exists", runner_exists, runner)
    check(f"{cache} exists", cache_exists, cache)
    if not (runner_exists and cache_exists):
        return
    text = cache_path.read_text(encoding="utf-8", errors="replace")
    header = cache_header(text)
    check(f"{runner} cache names same runner", header.get("runner") == runner, header.get("runner", "<missing>"))
    check(f"{runner} cache status ok", header.get("status") == "ok", header.get("status", "<missing>"))
    check(f"{runner} cache exit code zero", header.get("exit_code") == "0", header.get("exit_code", "<missing>"))
    check(
        f"{runner} cache sha is fresh",
        header.get("runner_sha256") == sha256_file(runner),
        f"cache={header.get('runner_sha256', '<missing>')}",
    )
    for fragment in fragments:
        require_fragment(f"{runner} cache contains required fragment", text, fragment)


def main() -> int:
    print("=" * 78)
    print("GAUGE/MATTER CLOSURE GATES SOURCE PACKET")
    print("=" * 78)
    print()
    print("Question: is the old gates memo auditable as a superseded route")
    print("memo, with canonical replacement authorities and guardrails named?")
    print()

    gates = read_text("docs/GAUGE_MATTER_CLOSURE_GATES_2026-04-12.md")
    lh = read_text("docs/LEFT_HANDED_CHARGE_MATCHING_NOTE.md")
    one = read_text("docs/ONE_GENERATION_MATTER_CLOSURE_NOTE.md")
    three = read_text("docs/THREE_GENERATION_STRUCTURE_NOTE.md")

    require_fragment("gates note title is present", gates, "# Gauge/Matter Closure Gates")
    require_fragment("gates note is explicitly superseded", gates, "superseded route memo")
    require_fragment("gates note is not canonical authority", gates, "no longer the canonical main-branch authority")
    require_fragment("primary runner metadata names this verifier", gates, "Primary runner: `scripts/frontier_gauge_matter_closure_gates_source_packet.py`")
    require_fragment("primary cache metadata names this verifier output", gates, "logs/runner-cache/frontier_gauge_matter_closure_gates_source_packet.txt")
    require_fragment("historical closed-language firewall is present", gates, "historical route-memo language")
    require_fragment("closed/paper-ready/retained-core terms are historical only", gates, "not current\naudit-status claims")
    require_fragment("audit authority firewall is present", gates, "independent audit lane")

    canonical_notes = [
        "LEFT_HANDED_CHARGE_MATCHING_NOTE.md",
        "ONE_GENERATION_MATTER_CLOSURE_NOTE.md",
        "THREE_GENERATION_STRUCTURE_NOTE.md",
    ]
    for note in canonical_notes:
        check(f"{note} exists", (REPO_ROOT / "docs" / note).exists(), f"docs/{note}")
        require_fragment(f"{note} named by gates memo", gates, note)

    require_fragment("left-handed note refuses retained promotion", lh, "does not\npropose a retained / positive_theorem promotion")
    require_fragment("left-handed note names scale-free scope", lh, "structural eigenvalue ratio")
    require_fragment("left-handed note keeps convention boundary", lh, "Normalization-convention boundary")
    require_fragment("one-generation note is bounded theorem typed", one, "**Type:** bounded_theorem")
    require_fragment("one-generation note is bounded conditional", one, "bounded conditional one-generation completion")
    require_fragment("one-generation note keeps branch convention boundary", one, "Neutral-singlet branch-selection boundary")
    require_fragment("three-generation note is bounded theorem typed", three, "**Type:** bounded_theorem")
    require_fragment("three-generation note has narrowed claim scope", three, "No-rooting,\nphysical-species interpretation")
    require_fragment("three-generation note has explicit non-claims", three, "## Explicit Non-Claims")

    check_cache(
        runner="scripts/frontier_graph_first_su3_integration.py",
        cache="logs/runner-cache/frontier_graph_first_su3_integration.txt",
        fragments=["PASS=111 FAIL=0", "graph-first route to the color lane"],
    )
    check_cache(
        runner="scripts/frontier_anomaly_forces_time.py",
        cache="logs/runner-cache/frontier_anomaly_forces_time.txt",
        fragments=["TOTAL: PASS=90 FAIL=0", "Declared imports (never computed here)"],
    )
    check_cache(
        runner="scripts/frontier_right_handed_sector.py",
        cache="logs/runner-cache/frontier_right_handed_sector.txt",
        fragments=["Passed: 61", "Failed: 0", "neutral-singlet\n     branch convention"],
    )
    check_cache(
        runner="scripts/frontier_three_generation_structure_narrow_spectrum.py",
        cache="logs/runner-cache/frontier_three_generation_structure_narrow_spectrum.txt",
        fragments=["PASS=15 FAIL=0", "This row does not claim physical-lattice necessity"],
    )
    check_cache(
        runner="scripts/audit_companion_one_generation_anomaly_singlet_completion_exact_2026_05_10.py",
        cache="logs/runner-cache/audit_companion_one_generation_anomaly_singlet_completion_exact_2026_05_10.txt",
        fragments=["TOTAL: PASS=26, FAIL=0", "Discrete e_R <-> nu_R relabelling branch is anomaly-consistent"],
    )

    print()
    print("=" * 78)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 78)
    print()
    if FAIL_COUNT:
        print("Verdict: FAIL; gauge/matter gates packet is not audit-ready.")
        return 1
    print("Verdict: bounded source-packet support. The old gates memo is")
    print("runner-backed as a superseded route memo pointing to canonical")
    print("bounded/conditional replacement authorities. No audit verdict or")
    print("retained status is assigned.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
