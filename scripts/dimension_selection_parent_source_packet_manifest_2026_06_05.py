#!/usr/bin/env python3
"""Source-packet manifest for DIMENSION_SELECTION_NOTE.md."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
NOTE = "docs/DIMENSION_SELECTION_NOTE.md"
OUTPUT_JSON = "outputs/dimension_selection_parent_source_packet_manifest_2026_06_05.json"

MANIFEST = {
    "parent_runner": "scripts/frontier_dimension_selection_lower_bound_parent_repair.py",
    "original_runner": "scripts/frontier_dimension_selection.py",
    "finite_k_bridge_note": "docs/DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md",
    "finite_k_bridge_runner": "scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py",
    "finite_k_bridge_json": "outputs/dimension_selection_finite_k_centroid_sign_bridge_2026-05-25.json",
    "parent_cache": "logs/runner-cache/frontier_dimension_selection_lower_bound_parent_repair.txt",
    "original_cache": "logs/runner-cache/frontier_dimension_selection.txt",
    "finite_k_bridge_cache": "logs/runner-cache/frontier_dimension_selection_finite_k_centroid_sign_bridge.txt",
}

REQUIRED_SOURCE_FRAGMENTS = {
    "parent_runner": [
        "import importlib.util",
        "BRIDGE_RUNNER",
        "def load_bridge_runner",
        "SUMMARY: PASS=",
    ],
    "original_runner": [
        "def measure_gravity_2d_with_d_potential",
        "def measure_I3",
        "SUMMARY TABLE",
        "beta",
        "I_3",
    ],
    "finite_k_bridge_runner": [
        "def finite_k_centroid_derivative",
        "def propagate_centroid_for_mass",
        "def part3_finite_difference",
        "SUMMARY: PASS=",
    ],
}

EXPECTED_CACHE_SNIPPETS = {
    "parent_cache": [
        "SUMMARY: PASS=27 FAIL=0",
        "COMPANION_PACKET: PASS",
        "finite-k lower-bound pass set is d=3,4,5",
        "finite-k lower-bound fail set is d=1,2",
    ],
    "original_cache": [
        "I_3/P = <1e-10",
        "d <= 2: EXCLUDED",
        "d >= 3: attractive gravity with beta ~ 1 and I_3 = 0",
        "  3 |       Yes |    Yes |     Yes |    1.01",
        "  4 |       Yes |    Yes |     Yes |    1.05",
        "  5 |       Yes |    Yes |     Yes |    1.03",
    ],
    "finite_k_bridge_cache": [
        "SUMMARY: PASS=56 FAIL=0",
        "d=1 derivative has expected sign",
        "d=5 parent raw_delta sign matches lower-bound sign",
    ],
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

    check(OUTPUT_JSON in note_text, "note_links_manifest_output", OUTPUT_JSON, results)

    for label, fragments in REQUIRED_SOURCE_FRAGMENTS.items():
        rel_path = MANIFEST[label]
        source = repo_path(rel_path).read_text(encoding="utf-8")
        check(len(source) > 3000, f"source_full_length:{label}", f"{rel_path} has {len(source)} bytes", results)
        for fragment in fragments:
            check(fragment in source, f"source_contains:{label}:{fragment}", f"{fragment} present", results)

    cache_to_runner = {
        "parent_cache": "parent_runner",
        "original_cache": "original_runner",
        "finite_k_bridge_cache": "finite_k_bridge_runner",
    }
    for cache_label, source_label in cache_to_runner.items():
        cache_rel = MANIFEST[cache_label]
        source_rel = MANIFEST[source_label]
        header = parse_cache(repo_path(cache_rel))
        current_sha = sha256_file(repo_path(source_rel))
        check(header.get("runner") == source_rel, f"cache_runner_matches:{cache_label}", f"{header.get('runner')} == {source_rel}", results)
        check(header.get("runner_sha256") == current_sha, f"cache_sha_fresh:{cache_label}", f"{header.get('runner_sha256')} == {current_sha}", results)
        check(header.get("exit_code") == "0" and header.get("status") == "ok", f"cache_exit_ok:{cache_label}", f"exit_code={header.get('exit_code')} status={header.get('status')}", results)
        for snippet in EXPECTED_CACHE_SNIPPETS[cache_label]:
            check(snippet in header["_text"], f"cache_snippet_present:{cache_label}:{snippet}", snippet, results)

    bridge_json = json.loads(repo_path(MANIFEST["finite_k_bridge_json"]).read_text(encoding="utf-8"))
    check(bridge_json.get("fail_count") == 0, "bridge_json_fail_count_zero", str(bridge_json.get("fail_count")), results)
    check(bridge_json.get("pass_count") == 56, "bridge_json_pass_count_56", str(bridge_json.get("pass_count")), results)

    pass_count = sum(1 for item in results if item["pass"])
    fail_count = len(results) - pass_count

    print("=" * 88)
    print("DIMENSION SELECTION PARENT: SOURCE PACKET MANIFEST")
    print("=" * 88)
    for item in results:
        status = "PASS" if item["pass"] else "FAIL"
        print(f"[{status}] {item['name']}: {item['detail']}")
    print("=" * 88)
    print(f"SUMMARY: DIMENSION SELECTION SOURCE PACKET PASS={pass_count} FAIL={fail_count}")
    print("=" * 88)

    out_dir = repo_path("outputs")
    out_dir.mkdir(exist_ok=True)
    out_path = repo_path(OUTPUT_JSON)
    out_path.write_text(
        json.dumps(
            {
                "claim_id": "dimension_selection_note",
                "note": NOTE,
                "manifest": MANIFEST,
                "summary": {"pass": pass_count, "fail": fail_count},
                "results": results,
                "audit_status_provenance": "independent audit handling only",
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
