#!/usr/bin/env python3
"""ABJ P-HY retained-bounded supplier wiring checker.

This runner verifies that the ABJ B1 left-handed anomaly arithmetic can cite
the existing retained-bounded hypercharge-identification surface instead of
treating P-HY as an unsupported local premise. It does not edit or apply audit
verdicts.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"
ABJ_NOTE_NAME = (
    "ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_"
    "BOUNDED_NOTE_2026-05-26.md"
)
ABJ_NOTE = ROOT / "docs" / ABJ_NOTE_NAME
SUPPLIER_NOTE = ROOT / "docs/ABJ_P_HY_RETAINED_BOUNDED_SUPPLIER_WIRING_NOTE_2026-06-18.md"
HYPERCHARGE_NOTE = ROOT / "docs/HYPERCHARGE_IDENTIFICATION_NOTE.md"
RETAINED_POSITIVE_GRADES = {"retained", "retained_bounded"}
LH_SCOPE_NEEDLES = (
    "Bounded LH-doublet chain assembly",
    "commutant U(1) gives Y(Q_L)=+1/3, Y(L_L)=-1",
)
EXCLUSION_SCOPE_NEEDLES = (
    "no full-spectrum anomaly",
    "GUT-normalization",
    "sin^2(theta_W) claim is included",
)

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  -- {detail}" if detail else ""
    print(f"[{status}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def one_line(text: str) -> str:
    return " ".join(text.split())


def ledger_row(claim_id: str) -> dict:
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    return rows[claim_id]


def test_current_supplier_status() -> None:
    print("== T1: current supplier status and scope ==")
    row = ledger_row("hypercharge_identification_note")
    effective_status = row.get("effective_status")
    check(
        "hypercharge_identification_note is retained-grade on this branch base",
        effective_status in RETAINED_POSITIVE_GRADES,
        str(effective_status),
    )
    check(
        "hypercharge_identification_note remains a theorem supplier",
        row.get("claim_type") in {"bounded_theorem", "positive_theorem"},
        str(row.get("claim_type")),
    )
    scope = row.get("claim_scope") or ""
    expected_scope = (
        "Bounded LH-doublet chain assembly: from the retained-grade ratio, "
        "matter-assignment, alpha=1/3 normalization, and GMN readout "
        "authorities, the commutant U(1) gives Y(Q_L)=+1/3, Y(L_L)=-1 and "
        "the derived LH charge table; no full-spectrum anomaly, "
        "GUT-normalization, or sin^2(theta_W) claim is included."
    )
    check(
        "ledger scope matches the note-quoted scope exactly",
        " ".join(scope.split()) == " ".join(expected_scope.split()),
        "exact claim_scope comparison (whitespace-folded)",
    )
    check(
        "ledger scope carries the derived LH charge-table clause",
        "the derived LH charge table" in scope,
    )
    check(
        "ledger scope includes current LH-doublet surface needles",
        all(needle in scope for needle in LH_SCOPE_NEEDLES),
    )
    check(
        "ledger scope includes current exclusion needles",
        all(needle in scope for needle in EXCLUSION_SCOPE_NEEDLES),
    )


def test_source_notes() -> None:
    print("== T2: source-note wiring and guardrails ==")
    abj = read(ABJ_NOTE)
    supplier = read(SUPPLIER_NOTE)
    hyper = read(HYPERCHARGE_NOTE)

    check(
        "ABJ note cites the new P-HY supplier wiring note",
        "ABJ_P_HY_RETAINED_BOUNDED_SUPPLIER_WIRING_NOTE_2026-06-18.md" in abj,
    )
    check(
        "ABJ note routes B1 through retained-bounded P-HY supplier",
        "retained-bounded P-HY LH-surface supplier" in abj
        and "retained-bounded P-HY supplier surface" in abj,
    )
    check(
        "ABJ note keeps P-COMP and P-REC open",
        "does not derive P-COMP or P-REC" in abj
        and "P-COMP/P-REC premise edges" in abj,
    )
    check(
        "ABJ note refuses to widen P-HY to full physical hypercharge",
        "does not widen P-HY beyond the bounded left-handed "
        "hypercharge-identification surface" in abj
        and "derivation of full physical hypercharge" in abj,
    )
    check(
        "supplier note names the exact target blocker",
        "Target blocker" in supplier
        and "anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_"
        "bounded_note_2026-05-26" in supplier,
    )
    check(
        "supplier note forbids new axioms or admissions",
        "No new axiom, primitive, Tier-A admission" in supplier,
    )
    check(
        "supplier note keeps remaining ABJ blockers explicit",
        "P-ABJ remains" in supplier
        and "P-COMP remains" in supplier
        and "P-REC remains" in supplier,
    )
    check(
        "hypercharge note supplies the bounded LH identification surface",
        "Y_\u03b1 = \u03b1(P_sym" in hyper
        and "\u03b1 = +1/3" in hyper
        and "(2, 3)" in hyper
        and "(2, 1)" in hyper,
    )
    check(
        "hypercharge note declares normalization and full-spectrum boundaries",
        "full anomaly-canceling Standard Model spectrum" in hyper
        and "absolute normalization" in hyper,
    )


def test_exact_b1_arithmetic() -> None:
    print("== T3: exact B1 anomaly arithmetic from supplied LH Y values ==")
    y_q = Fraction(1, 3)
    y_l = Fraction(-1, 1)
    t_f = Fraction(1, 2)

    tr_y = 6 * y_q + 2 * y_l
    tr_y3 = 6 * y_q**3 + 2 * y_l**3
    tr_su3sq_y = 2 * t_f * y_q
    tr_su2sq_y = 3 * t_f * y_q + t_f * y_l
    # computed from rep content: LH color-triplet doublet components, A(fund)=1
    color_triplet_lh_components = [rep for rep in ("Q_L_up", "Q_L_down") ]
    tr_su3cube = sum(Fraction(1) for _ in color_triplet_lh_components)

    check("Tr[Y] LH = 0", tr_y == 0, str(tr_y))
    check("Tr[Y^3] LH = -16/9", tr_y3 == Fraction(-16, 9), str(tr_y3))
    check(
        "Tr[SU(3)^2 Y] LH = 1/3",
        tr_su3sq_y == Fraction(1, 3),
        str(tr_su3sq_y),
    )
    check("Tr[SU(2)^2 Y] LH = 0", tr_su2sq_y == 0, str(tr_su2sq_y))
    check("Tr[SU(3)^3] LH = 2", tr_su3cube == 2, str(tr_su3cube))
    nonzero = [tr_y3, tr_su3sq_y, tr_su3cube]
    check(
        "B1 still has exactly three nonzero ABJ-relevant traces",
        sum(v != 0 for v in nonzero) == 3,
    )


def test_path_firewall() -> None:
    print("== T4: path and status firewall ==")
    touched_authority_paths = [
        "docs/audit/",
        "docs/publication/ci3_z3/",
        "docs/repo/FRONT_DOOR_STATUS.md",
        "docs/repo/LANE_REGISTRY.yaml",
        "docs/repo/ACTIVE_REVIEW_QUEUE.md",
        "docs/work_history/repo/LANE_STATUS_BOARD.md",
    ]
    source_paths = [
        str(ABJ_NOTE.relative_to(ROOT)),
        str(SUPPLIER_NOTE.relative_to(ROOT)),
        "scripts/frontier_abj_phy_retained_bounded_supplier_wiring_2026_06_18.py",
    ]
    for banned in touched_authority_paths:
        check(
            f"new source paths avoid authority surface {banned}",
            all(not path.startswith(banned) for path in source_paths),
        )
    supplier = read(SUPPLIER_NOTE)
    supplier_one_line = one_line(supplier)
    check(
        "supplier note uses bounded-support status rather than bare retained",
        "bounded-support source theorem" in supplier_one_line
        and "independent review/audit owns any effective status movement"
        in supplier_one_line,
    )


def main() -> int:
    test_current_supplier_status()
    test_source_notes()
    test_exact_b1_arithmetic()
    test_path_firewall()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
