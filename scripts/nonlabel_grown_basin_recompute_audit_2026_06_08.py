#!/usr/bin/env python3
"""Live recompute audit artifact for the non-label grown basin row.

This runner intentionally does not read the frozen log.  It reruns the
geometry-sector grown-row measurement for the three restore values named in
``docs/NONLABEL_GROWN_BASIN_NOTE.md`` and checks the same gates used by the
frozen verifier.
"""

from __future__ import annotations

from dataclasses import dataclass
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts import NONLABEL_GROWN_BASIN_TARGETED as basin
from scripts.gate_b_grown_joint_package import grow


@dataclass(frozen=True)
class Row:
    restore: float
    zero: float
    plus: float
    minus: float
    neutral: float
    double: float
    exponent: float
    ok: bool


def recompute_row(restore: float) -> Row:
    pos, _adj, layers = grow(basin.DRIFT, restore, basin.SEED)
    sector_adj = basin._build_geometry_sector_grown(pos, layers)
    zero, plus, minus, neutral, double, exponent, ok = basin._measure(
        pos,
        sector_adj,
        layers,
    )
    return Row(
        restore=restore,
        zero=zero,
        plus=plus,
        minus=minus,
        neutral=neutral,
        double=double,
        exponent=exponent,
        ok=ok,
    )


def main() -> int:
    rows = [recompute_row(restore) for restore in basin.RESTORES]
    failures: list[str] = []

    print("=" * 90)
    print("NON-LABEL GROWN BASIN LIVE RECOMPUTE AUDIT")
    print(
        f"drift={basin.DRIFT:.2f} restores={basin.RESTORES} seed={basin.SEED} "
        f"NL={basin.NL} source_strength={basin.SOURCE_STRENGTH:.1e}"
    )
    print("=" * 90)
    for row in rows:
        print(
            f"restore={row.restore:.2f} "
            f"zero={row.zero:+.12e} "
            f"plus={row.plus:+.12e} "
            f"minus={row.minus:+.12e} "
            f"neutral={row.neutral:+.12e} "
            f"double={row.double:+.12e} "
            f"exp={row.exponent:.12f} "
            f"{'PASS' if row.ok else 'FAIL'}"
        )

        if not row.ok:
            failures.append(f"restore={row.restore:.2f} original basin gate failed")
        if abs(row.zero) > 1e-12:
            failures.append(f"restore={row.restore:.2f} zero-source gate failed")
        if abs(row.neutral) > 1e-12:
            failures.append(f"restore={row.restore:.2f} neutral-pair gate failed")
        if not (row.plus < 0.0 < row.minus):
            failures.append(f"restore={row.restore:.2f} sign orientation failed")
        if row.double >= 0.0:
            failures.append(f"restore={row.restore:.2f} double-charge sign failed")
        if abs(row.exponent - 1.0) > 0.05:
            failures.append(
                f"restore={row.restore:.2f} charge exponent outside basin tolerance",
            )

    print()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"SCORECARD PASS=0 FAIL={len(failures)}")
        return 1

    print("SAFE READ: live recompute confirms the three-row bounded basin gates.")
    print(f"SCORECARD PASS={len(rows)} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
