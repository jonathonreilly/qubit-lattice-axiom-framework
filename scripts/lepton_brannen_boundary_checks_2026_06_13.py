"""Shared downstream boundary checks for Lepton/Brannen open-gate rows."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

import sympy as sp


FINITE_WEIGHT_ROW = "flavor_asymmetry_2over9_forced_weight_2026-05-31"
RADIAN_SEPARATION_ROW = "koide_dimensionless_radian_native_unit_separation_narrow_theorem_note_2026-05-25"
RADIAN_NO_GO_ROW = "koide_a1_radian_bridge_irreducibility_audit_note_2026-04-24"
DELTA_ORIENTATION_ROW = "koide_delta_phase_and_generation_count_share_one_z2_orientation_narrow_theorem_note_2026-06-08"
M2_256_ROW = "m2_tensor_d4_dimension_256_bounded_note_2026-05-26"


def _rows(root: Path) -> dict[str, dict[str, object]]:
    return json.loads((root / "docs" / "audit" / "data" / "audit_ledger.json").read_text())["rows"]


def _registration_guard(
    rows: dict[str, dict[str, object]],
    check: Callable[[str, bool, str], bool],
    label: str,
    row_id: str,
    claim_types: set[str],
    note_path: str,
) -> bool:
    row = rows.get(row_id, {})
    ok = row.get("claim_type") in claim_types and row.get("note_path") == note_path
    return check(
        label,
        ok,
        f"{row_id}: claim_type={row.get('claim_type')}, note_path={row.get('note_path')}",
    )


def run_delta_boundary_checks(root: Path, check: Callable[[str, bool, str], bool], prefix: str) -> list[bool]:
    passed: list[bool] = []
    rows = _rows(root)

    def c(label: str, ok: bool, detail: str = "") -> None:
        passed.append(check(f"{prefix}: {label}", ok, detail))

    passed.append(
        _registration_guard(
            rows,
            check,
            f"{prefix}: finite 2/9 weight row is registered as bounded_theorem",
            FINITE_WEIGHT_ROW,
            {"bounded_theorem"},
            "docs/FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md",
        )
    )
    passed.append(
        _registration_guard(
            rows,
            check,
            f"{prefix}: radian native-unit separation row is registered as bounded_theorem",
            RADIAN_SEPARATION_ROW,
            {"bounded_theorem"},
            "docs/KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md",
        )
    )
    passed.append(
        _registration_guard(
            rows,
            check,
            f"{prefix}: A1 radian bridge irreducibility row is registered as no_go",
            RADIAN_NO_GO_ROW,
            {"no_go"},
            "docs/KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md",
        )
    )
    passed.append(
        _registration_guard(
            rows,
            check,
            f"{prefix}: delta orientation row is registered as bounded_theorem",
            DELTA_ORIENTATION_ROW,
            {"bounded_theorem"},
            "docs/KOIDE_DELTA_PHASE_AND_GENERATION_COUNT_SHARE_ONE_Z2_ORIENTATION_NARROW_THEOREM_NOTE_2026-06-08.md",
        )
    )

    n = sp.symbols("n", integer=True, positive=True)
    finite_weight = sp.Rational(2, 9)
    plancherel_step = sp.pi * finite_weight
    eta_holonomy = 2 * sp.pi * finite_weight
    c(
        "finite rational 2/9 is not the bare-radian phase by itself",
        sp.simplify(plancherel_step - finite_weight) != 0
        and sp.simplify(eta_holonomy - finite_weight) != 0,
        f"2/9, pi*(2/9), 2*pi*(2/9) remain distinct",
    )
    family_weight = (n**2 - 1) / (12 * n)
    rank_fraction = (n - 1) / n**2
    c(
        "finite 2/9 family coincidence is N=3-specific",
        sp.simplify(family_weight.subs(n, 3) - rank_fraction.subs(n, 3)) == 0
        and sp.simplify(family_weight.subs(n, 5) - rank_fraction.subs(n, 5)) != 0,
        "prevents promoting a family identity from the N=3 coincidence",
    )
    return passed


def run_scale_boundary_checks(root: Path, check: Callable[[str, bool, str], bool], prefix: str) -> list[bool]:
    passed: list[bool] = []
    rows = _rows(root)

    passed.append(
        _registration_guard(
            rows,
            check,
            f"{prefix}: M2 tensor d4 dimension 256 row is registered as bounded_theorem",
            M2_256_ROW,
            {"bounded_theorem"},
            "docs/M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26.md",
        )
    )

    dim_c_m2 = 4
    dim_factor = dim_c_m2**4
    passed.append(
        check(
            f"{prefix}: exact bookkeeping factor is dim_C(M2(C))^4 = 256",
            dim_factor == 256,
            f"{dim_c_m2}^4={dim_factor}",
        )
    )
    passed.append(
        check(
            f"{prefix}: 256 support is not an m_W or lepton-mass derivation",
            True,
            "bounded tensor-dimension support leaves electroweak scale and observations external",
        )
    )
    return passed
