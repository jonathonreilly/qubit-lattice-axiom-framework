#!/usr/bin/env python3
"""Mirror vs dense central-band head-to-head, read from registered caches.

This runner is a cache-reader: it opens the registered runner-cache files
for the cited one-hop authorities and prints the rows that those caches
already contain. It does not introduce any hard-coded row that is not
present in a cited authority cache.

Sources (one-hop registered dependencies):

* Central-band lane row:
  ``logs/runner-cache/central_band_dense_joint_highN.txt`` (authority:
  ``docs/CENTRAL_BAND_DENSE_JOINT_HIGHN_NOTE.md``). The reader extracts the
  ``N=80, npl=80, LN+|y|`` row.
* Mirror strict-default lane rows:
  ``logs/runner-cache/mirror_chokepoint_joint.txt`` (authority:
  ``docs/MIRROR_CHOKEPOINT_NOTE.md``). The reader extracts the
  ``N=15`` and ``N=25`` ``mirror p2=0`` rows and reports the
  ``N=40, 60, 80, 100`` FAIL markers on the same strict default card.
* Mirror dense boundary-card lane rows:
  ``logs/runner-cache/mirror_chokepoint_boundary_fit_certificate.txt``
  (authority: ``docs/MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md``). The reader
  extracts the four pre-fit retention rows at ``N=40, 60, 80, 100`` on the
  dense boundary card and the ``N=120`` gravity-wall marker.

The previous version of this script printed a hard-coded ``N=40,
NPL_HALF=50`` mirror row that is not present in any cited authority cache.
That row and the through-``N=60`` strict-pocket range claim are dropped.

Exit codes:

* ``0`` on PASS (all required rows recovered from their caches).
* ``1`` if any required cache file is missing or any required row cannot
  be parsed.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

CENTRAL_CACHE = REPO_ROOT / "logs/runner-cache/central_band_dense_joint_highN.txt"
MIRROR_STRICT_CACHE = REPO_ROOT / "logs/runner-cache/mirror_chokepoint_joint.txt"
MIRROR_DENSE_CACHE = REPO_ROOT / "logs/runner-cache/mirror_chokepoint_boundary_fit_certificate.txt"


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"required cache missing: {path}")
    return path.read_text()


def find_line_containing(text: str, *needles: str) -> str | None:
    """Return the first line of ``text`` containing every needle, else None."""
    for line in text.splitlines():
        if all(n in line for n in needles):
            return line
    return None


def parse_central_row(cache_text: str) -> str:
    """Locate the ``N=80, npl=80, LN+|y|`` retained row in the central cache."""
    # The cache prints a header line and per-row lines. The ``LN+|y|``
    # non-collapse row at npl=80 is the retained row cited by the note.
    in_n80_block = False
    for line in cache_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("N = 80"):
            in_n80_block = True
            continue
        if stripped.startswith("N = ") and in_n80_block:
            in_n80_block = False
            continue
        if in_n80_block and stripped.startswith("80 ") and "LN+|y|" in stripped and "collapse" not in stripped:
            return stripped
    raise ValueError("central-band N=80 npl=80 LN+|y| row not found in cache")


def parse_mirror_strict_rows(cache_text: str) -> tuple[str, str, list[str]]:
    """Return ``(n15_mirror, n25_mirror, fail_markers)`` from the strict cache."""
    n15 = find_line_containing(cache_text, "  15  mirror p2=0")
    n25 = find_line_containing(cache_text, "  25  mirror p2=0")
    if n15 is None or n25 is None:
        raise ValueError("strict default mirror p2=0 N=15/N=25 rows not found")
    fail_markers: list[str] = []
    for n in ("40", "60", "80", "100"):
        line = find_line_containing(cache_text, f"  {n}  mirror p2=0", "FAIL")
        if line is None:
            raise ValueError(f"strict default mirror p2=0 FAIL marker missing for N={n}")
        fail_markers.append(line.strip())
    return n15.strip(), n25.strip(), fail_markers


def parse_mirror_dense_rows(cache_text: str) -> tuple[list[str], str]:
    """Return ``(retention_rows, wall_row)`` from the dense boundary cache."""
    rows: list[str] = []
    for n in ("40", "60", "80", "100"):
        line = find_line_containing(cache_text, f"   {n}  mirror p2=0") or find_line_containing(
            cache_text, f"  {n}  mirror p2=0"
        )
        if line is None or "FAIL" in line:
            raise ValueError(f"dense boundary mirror p2=0 retention row missing for N={n}")
        rows.append(line.strip())
    wall = find_line_containing(cache_text, "120  mirror p2=0")
    if wall is None:
        raise ValueError("dense boundary mirror p2=0 N=120 wall row missing")
    return rows, wall.strip()


def main() -> int:
    try:
        central_text = read_text(CENTRAL_CACHE)
        mirror_strict_text = read_text(MIRROR_STRICT_CACHE)
        mirror_dense_text = read_text(MIRROR_DENSE_CACHE)
    except FileNotFoundError as exc:
        print(f"FAIL: {exc}")
        return 1

    try:
        central_row = parse_central_row(central_text)
        n15, n25, strict_fails = parse_mirror_strict_rows(mirror_strict_text)
        dense_rows, dense_wall = parse_mirror_dense_rows(mirror_dense_text)
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1

    print("MIRROR VS CENTRAL HEAD-TO-HEAD (cache-reader)")
    print("=" * 92)
    print()
    print("Lane 1: Dense central-band + layer norm")
    print(f"  source cache: {CENTRAL_CACHE.relative_to(REPO_ROOT)}")
    print(f"  authority   : docs/CENTRAL_BAND_DENSE_JOINT_HIGHN_NOTE.md")
    print(f"  purity      : pur_min")
    print("  retained row (verbatim cache line):")
    print(f"    npl mode    Born            pur_min          gravity")
    print(f"    {central_row}")
    print()

    print("Lane 2a: Mirror strict default card (NPL_HALF=25, connect_radius=4.0)")
    print(f"  source cache: {MIRROR_STRICT_CACHE.relative_to(REPO_ROOT)}")
    print(f"  authority   : docs/MIRROR_CHOKEPOINT_NOTE.md")
    print(f"  purity      : pur_cl")
    print("  retained mirror p2=0 rows (verbatim cache lines):")
    print(f"    {n15}")
    print(f"    {n25}")
    print("  same-card FAIL markers (also verbatim):")
    for line in strict_fails:
        print(f"    {line}")
    print()

    print("Lane 2b: Mirror dense boundary card (NPL_HALF=60, connect_radius=5.0)")
    print(f"  source cache: {MIRROR_DENSE_CACHE.relative_to(REPO_ROOT)}")
    print(f"  authority   : docs/MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md")
    print(f"  purity      : pur_cl")
    print("  pre-fit retention rows (verbatim cache lines):")
    for line in dense_rows:
        print(f"    {line}")
    print("  gravity-wall row (verbatim cache line, excluded from the fit):")
    print(f"    {dense_wall}")
    print()

    print("Ranking (structural reading of the cited registered rows above):")
    print("  1. Dense central-band + layer norm")
    print("  2. Mirror chokepoint (strict + dense-boundary bounded pockets)")
    print()
    print("Fairness note: the central lane reports pur_min and the mirror lane")
    print("reports pur_cl, so the ranking is a full-lane comparison, not a")
    print("raw purity-to-purity contest.")
    print()
    print("PASS: every printed row was read from a cited registered cache.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
