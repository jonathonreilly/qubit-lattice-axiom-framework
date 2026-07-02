"""Shared downstream occupancy-boundary checks for flavor open-gate rows."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Callable

import sympy as sp


OCCUPANCY_ROW = "koide_orbit_occupancy_independence_and_premise_candidate_note_2026-06-09"


def run_occupancy_boundary_checks(root: Path, check: Callable[[str, bool, str], bool], prefix: str) -> list[bool]:
    """Check that the shared flavor residual is the explicit occupancy atom."""

    passed: list[bool] = []

    def c(label: str, cond: bool, detail: str = "") -> None:
        passed.append(check(f"{prefix}: {label}", cond, detail))

    rows = json.loads((root / "docs" / "audit" / "data" / "audit_ledger.json").read_text())["rows"]
    occupancy_row = rows.get(OCCUPANCY_ROW, {})
    c(
        "downstream occupancy theorem is ledger-registered as a bounded_theorem source",
        occupancy_row.get("claim_type") == "bounded_theorem"
        and occupancy_row.get("note_path") == "docs/KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md",
        (
            f"{OCCUPANCY_ROW}: claim_type={occupancy_row.get('claim_type')}, "
            f"note_path={occupancy_row.get('note_path')}"
        ),
    )

    minimal_axioms = (root / "docs" / "MINIMAL_AXIOMS_2026-06-05.md").read_text(encoding="utf-8")
    c(
        "Record axiom declines weighting and occupancy supply",
        bool(re.search(r"weighting,\s*normalization,\s*probability", minimal_axioms))
        and "occupancy rule" in minimal_axioms,
        "checked live Minimal Axioms text",
    )

    occupancy_note = (
        root / "docs" / "KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md"
    ).read_text(encoding="utf-8")
    c(
        "occupancy note records independence without adopting the premise",
        "**Claim type:** bounded_theorem" in occupancy_note
        and re.search(r"the occupancy rule is\s+not supplied by the current checked premise surface", occupancy_note)
        and "The premise candidate: orbit-occupancy (proposal; NOT adopted)" in occupancy_note
        and "adoption of any premise" in occupancy_note,
    )

    x, y, rr, g = sp.symbols("x y rr g", positive=True, real=True)
    z_sector = sp.integrate(sp.exp(-g * x**2 / 2), (x, -sp.oo, sp.oo)) * sp.integrate(
        sp.exp(-g * y**2 / 2), (y, -sp.oo, sp.oo)
    )
    z_orbit = sp.integrate(2 * sp.pi * rr * sp.exp(-g * rr**2), (rr, 0, sp.oo))
    c(
        "sector and orbit occupancy weights differ by exactly two",
        sp.simplify(z_sector - 2 * sp.pi / g) == 0
        and sp.simplify(z_orbit - sp.pi / g) == 0
        and sp.simplify(z_sector / z_orbit - 2) == 0,
        f"sector={sp.simplify(z_sector)}, orbit={sp.simplify(z_orbit)}",
    )

    rho_sector = sp.simplify((sp.pi / g) / z_sector)
    rho_orbit = sp.simplify((sp.pi / g) / z_orbit)
    r_sector = sp.simplify(1 / (2 * rho_sector))
    r_orbit = sp.simplify(1 / (2 * rho_orbit))
    c(
        "orientation maps sector occupancy to r=1 and orbit occupancy to r=1/2",
        (r_sector, r_orbit) == (1, sp.Rational(1, 2)),
        f"sector={r_sector}, orbit={r_orbit}",
    )

    return passed
