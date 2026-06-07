#!/usr/bin/env python3
"""Companion diagnostic for the Koide selected-eigenline ambient-eta split.

This runner does not edit or re-ratify the audited witness. It records the
repair target: the ambient eta proxy is diagnostic-only; the selected-eigenline
and endpoint-lift residuals are the load-bearing no-go.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from frontier_koide_delta_lattice_wilson_selected_eigenline_no_go import (  # noqa: E402
    build_wilson_lattice,
    eta_per_fixed_site,
)


RESULTS: list[tuple[str, bool, str]] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((label, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if detail:
        print(f"       {detail}")


def main() -> int:
    print("Koide selected-eigenline ambient-eta repair target")
    print("=" * 72)

    d_op, z3_action, fixed_sites = build_wilson_lattice(1.0)
    eta = eta_per_fixed_site(d_op, z3_action, len(fixed_sites))
    check(
        "current frozen finite Wilson eta diagnostic equals APS comparator 2/9",
        abs(eta - 2 / 9) <= 1e-10,
        f"|eta|/fixed_site={eta:.12f}; 2/9={2/9:.12f}",
    )

    alpha, c, eta_proxy = sp.symbols("alpha c eta_proxy", real=True)
    eta_aps = sp.Rational(2, 9)
    residual = sp.simplify(sp.cos(alpha) ** 2 + c / eta_aps - 1)
    selected_eigenline_form = sp.simplify(residual - (-sp.sin(alpha) ** 2 + c / eta_aps))
    check(
        "selected/spectator residual is independent of ambient eta proxy",
        selected_eigenline_form == 0 and sp.diff(residual, eta_proxy) == 0,
        f"delta/eta_APS - 1 = {residual}",
    )

    check(
        "closure still requires selected line alpha=0 and endpoint offset c=0",
        sp.simplify(residual.subs({alpha: 0, c: 0})) == 0
        and sp.simplify(residual.subs({alpha: sp.pi / 2, c: 0})) == -1
        and sp.simplify(residual.subs({alpha: 0, c: eta_aps})) == 1,
        "ambient eta matching does not choose the rank-one line or endpoint lift",
    )

    root = Path(__file__).resolve().parent.parent
    witness_note = root / "docs" / "KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24.md"
    witness_script = root / "scripts" / "frontier_koide_delta_lattice_wilson_selected_eigenline_no_go.py"
    note_text = witness_note.read_text()
    script_text = witness_script.read_text()
    check(
        "live witness still exposes ambient-residual wording, so this is a real repair target",
        "RESIDUAL_AMBIENT" in note_text and "finite Wilson eta proxy is not the exact APS value" in script_text,
        "companion leaves the audited witness untouched",
    )

    companion_note = root / "docs" / "KOIDE_SELECTED_EIGENLINE_AMBIENT_ETA_REPAIR_TARGET_NOTE_2026-06-07.md"
    companion_text = companion_note.read_text()
    required = [
        "**Claim type:** open_gate",
        "does not modify",
        "audit-bound",
        "diagnostic-only",
        "No-promotion statement",
    ]
    check(
        "companion note keeps audit-bound diagnostic status",
        all(token in companion_text for token in required),
        "independent audit lane owns any witness re-ratification",
    )

    passed = sum(1 for _, ok, _ in RESULTS if ok)
    failed = len(RESULTS) - passed
    print("=" * 72)
    print(f"TOTAL: {passed} PASS / {failed} FAIL")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
