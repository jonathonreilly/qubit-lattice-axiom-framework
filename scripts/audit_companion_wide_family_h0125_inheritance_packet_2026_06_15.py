#!/usr/bin/env python3
"""Audit companion for the wide-family h=0.125 reopen-audit row.

This row is not a fresh heavy-compute theorem. Its narrowed binding scope is
the fixed/reduced-family h=0.125 bounded negative inherited from retained
one-hop dependencies. The companion checks that inheritance packet and the
out-of-scope firewall for the wider phys_w=4 continuation.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import runner_cache as rc

if TYPE_CHECKING:
    # Packet-visible helper references for build_citation_graph.py.
    import lattice_3d_l2_numpy_h0125_audit as _lattice_3d_l2_numpy_h0125_audit
    import lattice_3d_l2_numpy_h0125_bridge as _lattice_3d_l2_numpy_h0125_bridge


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "WIDE_FAMILY_H0125_BRIDGE_REOPEN_AUDIT.md"
BRIDGE_NOTE = ROOT / "docs" / "LATTICE_3D_L2_NUMPY_H0125_BRIDGE_NOTE.md"
H2T_NOTE = ROOT / "docs" / "H2T_H0125_NARROW_BRIDGE_NOTE.md"

DEPENDENCY_RUNNERS = [
    "scripts/lattice_3d_l2_numpy_h0125_bridge.py",
    "scripts/lattice_3d_l2_numpy_h0125_audit.py",
]

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def cache_text(runner: str) -> tuple[dict | None, str]:
    path, header, text = rc.load_cache(runner)
    check(f"{runner} cache exists", path.exists(), path.relative_to(ROOT).as_posix())
    check(f"{runner} cache is SHA-fresh", rc.cache_status(runner) == "fresh", rc.cache_status(runner))
    check(f"{runner} cache header parses", header is not None)
    if header is not None:
        check(f"{runner} cache exits ok", header.get("status") == "ok" and header.get("exit_code") == "0", str(header))
        check(f"{runner} cache header names runner", header.get("runner_path") == runner, str(header.get("runner_path")))
    return header, text or ""


def check_note_boundaries() -> None:
    section("Source-note boundaries")
    text = NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    required = [
        "**Claim type:** bounded_theorem",
        "fixed/reduced-family `h = 0.125` bounded negatives",
        "does not add a new fixed/reduced-family result",
        "wider `phys_w = 4` family continuation",
        "out-of-binding-scope",
        "Promoting that wider-family reopen requires a separately registered retained note/log/runner",
        "scripts/audit_companion_wide_family_h0125_inheritance_packet_2026_06_15.py",
        "LATTICE_3D_L2_NUMPY_H0125_BRIDGE_NOTE.md",
        "H2T_H0125_NARROW_BRIDGE_NOTE.md",
    ]
    for marker in required:
        check(f"note marker: {marker[:62]}", marker in text or marker in flat)
    forbidden = [
        "wider `phys_w = 4` continuation is load-bearing",
        "clean Newtonian mass-law closure",
        "continuum-limit theorem",
    ]
    for marker in forbidden:
        check(f"forbidden overclaim absent: {marker}", marker not in text)


def check_dependency_notes() -> None:
    section("Dependency notes")
    for note in (BRIDGE_NOTE, H2T_NOTE):
        text = note.read_text(encoding="utf-8")
        check(f"{note.name} exists", note.exists(), note.relative_to(ROOT).as_posix())
        check(f"{note.name} records h=0.125", "h = 0.125" in text or "h=0.125" in text)
        check(f"{note.name} keeps F~M near 0.50 negative", "F~M" in text and "0.50" in text)
        check(f"{note.name} forbids promotion", "does **not** promote" in text or "does not currently survive" in text or "not a Newtonian bridge closure" in text)


def check_dependency_caches() -> None:
    section("Dependency runner caches")
    for runner in DEPENDENCY_RUNNERS:
        _, text = cache_text(runner)
        check(f"{runner} cache contains h=0.125 row", "h=0.125" in text or "h = 0.125" in text)
        check(f"{runner} cache contains TOWARD h=0.125 signal", "TOWARD" in text)
        check(f"{runner} cache contains F~M alpha about 0.50", "F~M alpha = 0.50" in text or "F~M alpha = 0.49" in text)
        check(f"{runner} cache contains machine-clean Born scale", "e-15" in text)


def main() -> int:
    print("WIDE-FAMILY H=0.125 INHERITANCE AUDIT PACKET")
    check_note_boundaries()
    check_dependency_notes()
    check_dependency_caches()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
