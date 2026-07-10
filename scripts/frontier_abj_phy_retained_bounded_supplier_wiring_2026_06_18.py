#!/usr/bin/env python3
"""ABJ P-HY retained-bounded supplier wiring checker.

This runner verifies that the ABJ B1 left-handed anomaly arithmetic can cite
the existing retained-bounded hypercharge-identification surface instead of
treating P-HY as an unsupported local premise. It does not edit or apply audit
verdicts.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
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
L2_MATTER_NOTE_NAME = "LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md"
L3_ALPHA_NOTE_NAME = "HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md"
L2_MATTER_CLAIM_ID = "lhcm_matter_assignment_from_su3_representation_note_2026-05-02"
L3_ALPHA_CLAIM_ID = "hypercharge_alpha_third_normalization_bridge_bounded_note_2026-05-25"
L2_MATTER_PARENT_CLAIM_ID = "graph_first_su3_integration_note"
DECORATION_PREFIX = "decoration_under_"
RETAINED_GRADES = {"retained", "retained_bounded", "retained_no_go"}
THEOREM_CLAIM_TYPES = {"bounded_theorem", "positive_theorem"}
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


def quoted_scope(text: str) -> str:
    lines = text.splitlines()
    start = next(
        (i for i, line in enumerate(lines) if line.startswith("> Bounded LH-doublet")),
        None,
    )
    if start is None:
        return ""
    quoted: list[str] = []
    for line in lines[start:]:
        if not line.startswith(">"):
            break
        quoted.append(line.removeprefix("> ").removeprefix(">"))
    return one_line(" ".join(quoted))


@dataclass(frozen=True)
class LeftHandedRep:
    name: str
    weak_multiplicity: int
    color_multiplicity: int
    hypercharge: Fraction
    color_quadratic_index: Fraction
    color_cubic_index: Fraction


LH_REPS = (
    LeftHandedRep("Q_L", 2, 3, Fraction(1, 3), Fraction(1, 2), Fraction(1)),
    LeftHandedRep("L_L", 2, 1, Fraction(-1), Fraction(0), Fraction(0)),
)


def ledger_row(claim_id: str) -> dict:
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    return rows.get(claim_id) or {}


def decoration_under_retained_parent(
    claim_id: str, expected_parent_id: str
) -> tuple[bool, str]:
    row = ledger_row(claim_id)
    status = str(row.get("effective_status") or "missing_row")
    parent = ledger_row(expected_parent_id)
    parent_status = parent.get("effective_status")
    expected_status = f"{DECORATION_PREFIX}{expected_parent_id}"
    return (
        row.get("claim_type") == "decoration"
        and status == expected_status
        and parent.get("claim_type") in THEOREM_CLAIM_TYPES
        and parent_status in RETAINED_GRADES,
        f"{status} (parent {expected_parent_id}: {parent_status})",
    )


def test_current_supplier_status() -> None:
    print("== T1: current supplier status and scope ==")
    row = ledger_row("hypercharge_identification_note")
    effective_status = row.get("effective_status")
    check(
        "hypercharge_identification_note is retained-grade in the current ledger",
        effective_status in RETAINED_GRADES,
        str(effective_status),
    )
    check(
        "hypercharge_identification_note remains a theorem supplier",
        row.get("claim_type") in {"bounded_theorem", "positive_theorem"},
        str(row.get("claim_type")),
    )
    scope = row.get("claim_scope") or ""
    check(
        "ledger scope matches the note-quoted scope exactly",
        " ".join(scope.split()) == quoted_scope(read(SUPPLIER_NOTE)),
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
    l2_ok, l2_detail = decoration_under_retained_parent(
        L2_MATTER_CLAIM_ID, L2_MATTER_PARENT_CLAIM_ID
    )
    check(
        "L2 matter-assignment authority satisfies current dependency-chain policy",
        l2_ok,
        l2_detail,
    )
    l3_row = ledger_row(L3_ALPHA_CLAIM_ID)
    l3_status = l3_row.get("effective_status")
    check(
        "L3 alpha=1/3 normalization authority satisfies current dependency-chain policy",
        l3_row.get("claim_type") in THEOREM_CLAIM_TYPES
        and l3_status in RETAINED_GRADES,
        str(l3_status),
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
        "supplier note carries a direct dependency edge to the L2 "
        "matter-assignment authority",
        f"]({L2_MATTER_NOTE_NAME})" in supplier
        and (ROOT / "docs" / L2_MATTER_NOTE_NAME).is_file(),
    )
    check(
        "supplier note carries a direct dependency edge to the L3 alpha=1/3 "
        "normalization authority",
        f"]({L3_ALPHA_NOTE_NAME})" in supplier
        and (ROOT / "docs" / L3_ALPHA_NOTE_NAME).is_file(),
    )
    check(
        "hypercharge note supplies the complete operator/eigenblock mapping",
        "Y_\u03b1 = \u03b1(P_sym \u2212 3 P_anti)" in hyper
        and "| (2, 3) = C² ⊗ Sym²(C²) | 6 | +1/3 |" in hyper
        and "| (2, 1) = C² ⊗ Anti²(C²) | 2 | −1 |" in hyper,
    )
    check(
        "hypercharge note declares normalization and full-spectrum boundaries",
        "full anomaly-canceling Standard Model spectrum" in hyper
        and "absolute normalization" in hyper,
    )


def test_exact_b1_arithmetic() -> None:
    print("== T3: exact B1 anomaly arithmetic from supplied LH Y values ==")
    tr_y = sum(
        rep.weak_multiplicity * rep.color_multiplicity * rep.hypercharge
        for rep in LH_REPS
    )
    tr_y3 = sum(
        rep.weak_multiplicity * rep.color_multiplicity * rep.hypercharge**3
        for rep in LH_REPS
    )
    tr_su3sq_y = sum(
        rep.weak_multiplicity * rep.color_quadratic_index * rep.hypercharge
        for rep in LH_REPS
    )
    su2_quadratic_index = Fraction(1, 2)
    tr_su2sq_y = sum(
        rep.color_multiplicity * su2_quadratic_index * rep.hypercharge
        for rep in LH_REPS
    )
    tr_su3cube = sum(
        rep.weak_multiplicity * rep.color_cubic_index for rep in LH_REPS
    )

    check("Tr[Y] LH = 0", tr_y == 0, str(tr_y))
    check("Tr[Y^3] LH = -16/9", tr_y3 == Fraction(-16, 9), str(tr_y3))
    check(
        "Tr[SU(3)^2 Y] LH = 1/3",
        tr_su3sq_y == Fraction(1, 3),
        str(tr_su3sq_y),
    )
    check("Tr[SU(2)^2 Y] LH = 0", tr_su2sq_y == 0, str(tr_su2sq_y))
    check("Tr[SU(3)^3] LH = 2", tr_su3cube == 2, str(tr_su3cube))
    anti_fundamental = LeftHandedRep(
        "anti-Q", 2, 3, Fraction(0), Fraction(1, 2), Fraction(-1)
    )
    check(
        "anti-fundamental edge case reverses the cubic-anomaly sign",
        anti_fundamental.weak_multiplicity * anti_fundamental.color_cubic_index
        == -2,
    )
    nonzero = [tr_y3, tr_su3sq_y, tr_su3cube]
    check(
        "B1 still has exactly three nonzero ABJ-relevant traces",
        sum(v != 0 for v in nonzero) == 3,
    )


def main() -> int:
    test_current_supplier_status()
    test_source_notes()
    test_exact_b1_arithmetic()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
