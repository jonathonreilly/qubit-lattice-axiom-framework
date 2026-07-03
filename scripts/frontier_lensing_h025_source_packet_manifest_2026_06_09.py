#!/usr/bin/env python3
"""Source-packet manifest for the H=0.25 lensing edge-kernel certificate.

This runner does not recompute the 150s edge-kernel certificate. It makes the
audit packet explicit: the fine-H runner, its local helper scripts, its fresh
cache, and its structured JSON output must all be present and mutually pinned.
"""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

import runner_cache as rc


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
NOTE = ROOT / "docs" / "LENSING_EXPONENT_IS_A_DIPOLE_CROSSOVER_RESOLUTION_BOUNDED_THEOREM_NOTE_2026-06-07.md"
TARGET_RUNNER = "scripts/frontier_lensing_h025_edge_kernel_certificate_2026_06_08.py"
TARGET_OUTPUT = ROOT / "outputs/lensing_h025_edge_kernel_certificate_2026_06_08.json"
SOURCE_CERT = ROOT / "outputs/lensing_deflection_h025_slope_fit_certificate.json"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(ok)
    FAIL += int(not ok)
    return ok


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_imports(path: Path) -> set[Path]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    deps: set[Path] = set()
    for node in ast.walk(tree):
        module = None
        if isinstance(node, ast.Import):
            for alias in node.names:
                module = alias.name.split(".")[0]
                candidate = SCRIPTS / f"{module}.py"
                if candidate.exists():
                    deps.add(candidate)
        elif isinstance(node, ast.ImportFrom) and node.module:
            module = node.module.split(".")[0]
            candidate = SCRIPTS / f"{module}.py"
            if candidate.exists():
                deps.add(candidate)
    return deps


def transitive_local_deps(root: Path) -> list[Path]:
    seen: set[Path] = set()
    stack = [root]
    while stack:
        path = stack.pop()
        if path in seen:
            continue
        seen.add(path)
        for dep in sorted(local_imports(path)):
            if dep not in seen:
                stack.append(dep)
    return sorted(seen)


def cache_guard() -> bool:
    status = rc.cache_status(TARGET_RUNNER)
    cache_path, header, text = rc.load_cache(TARGET_RUNNER)
    runner_path = ROOT / TARGET_RUNNER
    live_sha = sha256(runner_path)
    header_sha = header.get("runner_sha256") if header else None
    ok = (
        status == "fresh"
        and header is not None
        and header.get("status") == "ok"
        and str(header.get("exit_code")) == "0"
        and header_sha == live_sha
        and text is not None
        and "TOTAL: PASS=12 FAIL=0" in text
    )
    return check(
        "H=0.25 edge-kernel cache is fresh and source-pinned",
        ok,
        f"cache={cache_path.relative_to(ROOT)}, status={status}, live_sha={live_sha}, cache_sha={header_sha}",
    )


def output_guard() -> bool:
    data = json.loads(TARGET_OUTPUT.read_text(encoding="utf-8"))
    summary = data.get("summary", {})
    setup = data.get("setup", {})
    ok = (
        summary.get("pass") == 12
        and summary.get("fail") == 0
        and setup.get("H") == 0.25
        and setup.get("NL") == 60
        and setup.get("n_edges_streamed", 0) > 60_000_000
        and abs(data.get("small_fit", {}).get("slope", 0.0) + 1.4335) < 1.0e-3
        and data.get("monopole_ratio", 1.0) < 0.01
    )
    return check(
        "structured H=0.25 JSON output matches certificate summary",
        ok,
        (
            f"summary={summary}; H={setup.get('H')}; NL={setup.get('NL')}; "
            f"edges={setup.get('n_edges_streamed')}; slope={data.get('small_fit', {}).get('slope')}"
        ),
    )


def source_cert_guard() -> bool:
    data = json.loads(SOURCE_CERT.read_text(encoding="utf-8"))
    fit = data.get("fit_results", {})
    ok = (
        data.get("certificate_id") == "lensing_deflection_h025_slope_fit"
        and abs(fit.get("kubo_slope", 0.0) + 1.4335) < 1.0e-3
        and fit.get("kubo_r_squared", 0.0) > 0.998
    )
    return check(
        "source fine-H slope certificate is present",
        ok,
        f"id={data.get('certificate_id')}; slope={fit.get('kubo_slope')}; r2={fit.get('kubo_r_squared')}",
    )


def note_guard() -> bool:
    note = NOTE.read_text(encoding="utf-8")
    required = [
        "frontier_lensing_h025_source_packet_manifest_2026_06_09.py",
        "frontier_lensing_h025_source_packet_manifest_2026_06_09.txt",
        "frontier_lensing_h025_edge_kernel_certificate_2026_06_08.py",
        "lensing_h025_edge_kernel_certificate_2026_06_08.json",
    ]
    missing = [phrase for phrase in required if phrase not in note]
    return check("source note names fine-H manifest packet", not missing, f"missing={missing}")


def main() -> int:
    print("Lensing H=0.25 source-packet manifest")
    print("=" * 78)
    target_path = ROOT / TARGET_RUNNER
    deps = transitive_local_deps(target_path)
    print("LOCAL SOURCE PACKET")
    for path in deps:
        print(f"  {path.relative_to(ROOT)}  sha256={sha256(path)}")
    print()
    expected = {
        ROOT / TARGET_RUNNER,
        SCRIPTS / "kubo_continuum_limit.py",
        SCRIPTS / "lensing_adjoint_kernel_probe.py",
    }
    check(
        "transitive local helper scripts are present",
        expected.issubset(set(deps)),
        f"deps={[path.relative_to(ROOT).as_posix() for path in deps]}",
    )
    cache_guard()
    source_cert_guard()
    output_guard()
    note_guard()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
