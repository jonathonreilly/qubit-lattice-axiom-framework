#!/usr/bin/env python3
"""Source-packet manifest verifier for the live staggered Green packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
NOTE = "docs/STAGGERED_BACKREACTION_LIVE_GREEN_PACKET_NOTE_2026-05-29.md"

MANIFEST = {
    "packet_checker": "scripts/staggered_backreaction_live_green_packet_check.py",
    "green_closure_source": "scripts/frontier_staggered_backreaction_green_closure.py",
    "prototype_helper_source": "scripts/frontier_staggered_backreaction_prototype.py",
    "packet_cache": "logs/runner-cache/staggered_backreaction_live_green_packet_check.txt",
    "green_closure_cache": "logs/runner-cache/frontier_staggered_backreaction_green_closure.txt",
    "prototype_helper_cache": "logs/runner-cache/frontier_staggered_backreaction_prototype.txt",
}

REQUIRED_SOURCE_FRAGMENTS = {
    "packet_checker": [
        "import frontier_staggered_backreaction_green_closure as green",
        "def _compute",
        "ASSERTIONS:",
    ],
    "green_closure_source": [
        "import frontier_staggered_backreaction_prototype as base",
        "def _make_mappings",
        "def _measure_family",
        "def _fit_gain",
        "class MapSummary",
    ],
    "prototype_helper_source": [
        "class GraphFamily",
        "def _make_graphs",
        "def _solve_phi",
        "def _build_hamiltonian",
        "def _evolve_cn",
    ],
}

EXPECTED_CACHE_SNIPPETS = {
    "packet_cache": "ASSERTIONS: PASS",
    "green_closure_cache": "raw improvement factor: 2.81x",
    "prototype_helper_cache": "STAGGERED SOURCE-GENERATED BACKREACTION PROTOTYPE",
}


def repo_path(rel_path: str) -> Path:
    return REPO_ROOT / rel_path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_cache(cache_path: Path) -> dict[str, str]:
    text = cache_path.read_text(encoding="utf-8", errors="replace")
    header, _, _stdout = text.partition("----- stdout -----")
    out = {"_text": text}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip()
    return out


def check(condition: bool, name: str, detail: str, results: list[dict]) -> None:
    results.append({"name": name, "pass": bool(condition), "detail": detail})


def main() -> int:
    results: list[dict] = []
    note_text = repo_path(NOTE).read_text(encoding="utf-8")

    for label, rel_path in MANIFEST.items():
        check(repo_path(rel_path).exists(), f"manifest_path_exists:{label}", rel_path, results)
        check(rel_path in note_text, f"note_links_manifest_path:{label}", rel_path, results)

    for label, fragments in REQUIRED_SOURCE_FRAGMENTS.items():
        rel_path = MANIFEST[label]
        source = repo_path(rel_path).read_text(encoding="utf-8")
        check(len(source) > 3000, f"source_full_length:{label}", f"{rel_path} has {len(source)} bytes", results)
        for fragment in fragments:
            check(fragment in source, f"source_contains:{label}:{fragment}", f"{fragment} present", results)

    cache_to_runner = {
        "packet_cache": "packet_checker",
        "green_closure_cache": "green_closure_source",
        "prototype_helper_cache": "prototype_helper_source",
    }
    for cache_label, source_label in cache_to_runner.items():
        cache_rel = MANIFEST[cache_label]
        source_rel = MANIFEST[source_label]
        header = parse_cache(repo_path(cache_rel))
        current_sha = sha256_file(repo_path(source_rel))
        check(header.get("runner") == source_rel, f"cache_runner_matches:{cache_label}", f"{header.get('runner')} == {source_rel}", results)
        check(header.get("runner_sha256") == current_sha, f"cache_sha_fresh:{cache_label}", f"{header.get('runner_sha256')} == {current_sha}", results)
        check(header.get("exit_code") == "0" and header.get("status") == "ok", f"cache_exit_ok:{cache_label}", f"exit_code={header.get('exit_code')} status={header.get('status')}", results)
        check(EXPECTED_CACHE_SNIPPETS[cache_label] in header["_text"], f"cache_snippet_present:{cache_label}", EXPECTED_CACHE_SNIPPETS[cache_label], results)

    pass_count = sum(1 for item in results if item["pass"])
    fail_count = len(results) - pass_count

    print("=" * 88)
    print("STAGGERED BACKREACTION LIVE GREEN: SOURCE PACKET MANIFEST")
    print("=" * 88)
    for item in results:
        status = "PASS" if item["pass"] else "FAIL"
        print(f"[{status}] {item['name']}: {item['detail']}")
    print("=" * 88)
    print(f"SUMMARY: STAGGERED GREEN SOURCE PACKET PASS={pass_count} FAIL={fail_count}")
    print("=" * 88)

    out_dir = repo_path("outputs")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "staggered_backreaction_live_green_source_packet_manifest_2026_06_04.json"
    out_path.write_text(
        json.dumps(
            {
                "claim_id": "staggered_backreaction_live_green_packet_note_2026-05-29",
                "note": NOTE,
                "manifest": MANIFEST,
                "summary": {"pass": pass_count, "fail": fail_count},
                "results": results,
                "audit_status_authority": "independent audit lane only",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Output written: {out_path.relative_to(REPO_ROOT)}")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
