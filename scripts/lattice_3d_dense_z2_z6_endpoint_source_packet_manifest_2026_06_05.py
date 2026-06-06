#!/usr/bin/env python3
"""Source-packet manifest verifier for the dense z=2..6 endpoint packet."""

from __future__ import annotations

import hashlib
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
NOTE = "docs/LATTICE_3D_DENSE_SPENT_DELAY_Z2_Z6_ENDPOINT_NOTE_2026-05-29.md"

MANIFEST = {
    "endpoint_checker": "scripts/lattice_3d_dense_z2_z6_endpoint_check.py",
    "dense_helper_source": "scripts/lattice_3d_dense_10prop.py",
    "endpoint_cache": "logs/runner-cache/lattice_3d_dense_z2_z6_endpoint_check.txt",
    "dense_helper_cache": "logs/runner-cache/lattice_3d_dense_10prop.txt",
}

REQUIRED_SOURCE_MARKERS = {
    "endpoint_checker": [
        "import scripts.lattice_3d_dense_10prop as dense",
        "for z_mass in [2, 3, 4, 5, 6]",
        "dense.classify_sign",
        "ASSERTIONS:",
    ],
    "dense_helper_source": [
        "def generate(",
        "def propagate(",
        "def make_field(",
        "def classify_sign(",
        "def near_mass_window_gain(",
        "def mass_side_channel_bias(",
    ],
}

EXPECTED_CACHE_SNIPPETS = {
    "endpoint_cache": "ASSERTIONS: PASS",
    "dense_helper_cache": "3D DENSE LATTICE: CANONICAL 10-PROPERTY CARD",
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

    for label, markers in REQUIRED_SOURCE_MARKERS.items():
        rel_path = MANIFEST[label]
        source = repo_path(rel_path).read_text(encoding="utf-8")
        check(len(source) > 3000, f"source_untruncated:{label}", f"{rel_path} has {len(source)} bytes", results)
        for marker in markers:
            check(marker in source, f"source_marker:{label}:{marker}", f"{marker} present", results)

    cache_to_runner = {
        "endpoint_cache": "endpoint_checker",
        "dense_helper_cache": "dense_helper_source",
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
    print("3D DENSE z=2..6 ENDPOINT: SOURCE PACKET MANIFEST")
    print("=" * 88)
    for item in results:
        status = "PASS" if item["pass"] else "FAIL"
        print(f"[{status}] {item['name']}: {item['detail']}")
    print("=" * 88)
    print(f"SUMMARY: DENSE ENDPOINT SOURCE PACKET PASS={pass_count} FAIL={fail_count}")
    print("=" * 88)
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
