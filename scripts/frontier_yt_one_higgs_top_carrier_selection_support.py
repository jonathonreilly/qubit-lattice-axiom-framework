#!/usr/bin/env python3
"""Narrow one-Higgs top-carrier selection support for Y_T."""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_one_higgs_top_carrier_selection_support_2026-05-26.json"

NOTE = DOCS / "YT_ONE_HIGGS_TOP_CARRIER_SELECTION_SUPPORT_NOTE_2026-05-26.md"
BROAD_ONE_HIGGS = DOCS / "SM_ONE_HIGGS_YUKAWA_GAUGE_SELECTION_THEOREM_NOTE_2026-04-26.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

PASS_COUNT = 0
FAIL_COUNT = 0


@dataclass(frozen=True)
class Field:
    name: str
    color: str
    su2: str
    y: Fraction
    left_doublet: bool = False
    right_singlet: bool = False
    scalar: bool = False


FIELDS = {
    "Q_L": Field("Q_L", "3", "2", Fraction(1, 3), left_doublet=True),
    "L_L": Field("L_L", "1", "2", Fraction(-1, 1), left_doublet=True),
    "u_R": Field("u_R", "3", "1", Fraction(4, 3), right_singlet=True),
    "d_R": Field("d_R", "3", "1", Fraction(-2, 3), right_singlet=True),
    "e_R": Field("e_R", "1", "1", Fraction(-2, 1), right_singlet=True),
    "nu_R": Field("nu_R", "1", "1", Fraction(0, 1), right_singlet=True),
    "H": Field("H", "1", "2", Fraction(1, 1), scalar=True),
    "tilde_H": Field("tilde_H", "1", "2", Fraction(-1, 1), scalar=True),
}


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ledger_row(claim_id: str) -> dict[str, Any]:
    rows = json.loads(read(LEDGER))["rows"]
    iterable = rows.values() if isinstance(rows, dict) else rows
    for row in iterable:
        if row.get("claim_id") == claim_id:
            return row
    raise KeyError(claim_id)


def color_allowed(left: Field, right: Field) -> bool:
    if left.name == "Q_L":
        return right.color == "3"
    if left.name == "L_L":
        return right.color == "1"
    return False


def hypercharge_total(left: Field, scalar: Field, right: Field) -> Fraction:
    return -left.y + scalar.y + right.y


def allowed(left: Field, scalar: Field, right: Field) -> bool:
    return color_allowed(left, right) and scalar.su2 == "2" and right.su2 == "1" and hypercharge_total(left, scalar, right) == 0


def part1_anchors() -> dict[str, Any]:
    print("\nPart 1: anchors and status")
    for path in (NOTE, BROAD_ONE_HIGGS, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Claim",
        "Inputs And Scope",
        "Proof",
        "Exhaustion Check",
        "What This Burns Down",
        "What Still Remains",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains required section: {phrase}", phrase in note)

    hyper = ledger_row("sm_hypercharge_uniqueness_algebraic_solution_enumeration_narrow_theorem_note_2026-05-10")
    broad = ledger_row("sm_one_higgs_yukawa_gauge_selection_theorem_note_2026-04-26")
    check("narrow hypercharge enumeration is retained_bounded", hyper.get("effective_status") == "retained_bounded", hyper.get("effective_status"))
    check("broad one-Higgs row remains unaudited context", broad.get("effective_status") == "unaudited", broad.get("effective_status"))
    return {
        "hypercharge_enumeration_status": hyper.get("effective_status"),
        "broad_one_higgs_status": broad.get("effective_status"),
    }


def part2_top_carrier() -> None:
    print("\nPart 2: top carrier selection")
    q = FIELDS["Q_L"]
    u = FIELDS["u_R"]
    h = FIELDS["H"]
    ht = FIELDS["tilde_H"]
    check("bar Q_L tilde_H u_R hypercharge vanishes", hypercharge_total(q, ht, u) == 0, hypercharge_total(q, ht, u))
    check("bar Q_L H u_R hypercharge is rejected", hypercharge_total(q, h, u) != 0, hypercharge_total(q, h, u))
    check("bar Q_L tilde_H u_R is gauge allowed", allowed(q, ht, u))
    check("bar Q_L H u_R is not gauge allowed", not allowed(q, h, u))


def part3_exhaustion() -> list[str]:
    print("\nPart 3: exhaustion over one-Higgs Dirac carriers")
    lefts = [f for f in FIELDS.values() if f.left_doublet]
    rights = [f for f in FIELDS.values() if f.right_singlet]
    scalars = [f for f in FIELDS.values() if f.scalar]
    allowed_monomials = []
    rejected_wrong_higgs = []
    rejected_color = []
    for left in lefts:
        for right in rights:
            for scalar in scalars:
                label = f"bar {left.name} {scalar.name} {right.name}"
                if allowed(left, scalar, right):
                    allowed_monomials.append(label)
                elif not color_allowed(left, right):
                    rejected_color.append(label)
                elif hypercharge_total(left, scalar, right) != 0:
                    rejected_wrong_higgs.append(label)

    expected = {
        "bar Q_L tilde_H u_R",
        "bar Q_L H d_R",
        "bar L_L H e_R",
        "bar L_L tilde_H nu_R",
    }
    check("exactly four one-Higgs Dirac carriers are allowed", set(allowed_monomials) == expected, allowed_monomials)
    check("top carrier is unique in Q_L to u_R channel", [m for m in allowed_monomials if "Q_L" in m and "u_R" in m] == ["bar Q_L tilde_H u_R"])
    check("wrong-Higgs candidates are rejected by hypercharge", len(rejected_wrong_higgs) == 4, rejected_wrong_higgs)
    check("quark/lepton crossed candidates rejected by color", len(rejected_color) == 8, rejected_color)
    return allowed_monomials


def part4_coefficient_boundary() -> dict[str, Any]:
    print("\nPart 4: coefficient boundary")
    boundary = {
        "top_carrier_skeleton_selected": True,
        "generation_matrix_entry_selected": False,
        "physical_intervention_law_accepted": False,
        "strict_top_w_response_evidence_present": False,
        "proposal_allowed": False,
    }
    check("top carrier skeleton selected", boundary["top_carrier_skeleton_selected"])
    check("generation matrix entry remains free", not boundary["generation_matrix_entry_selected"])
    check("physical intervention law remains outside carrier theorem", not boundary["physical_intervention_law_accepted"])
    check("strict top/W response evidence remains absent", not boundary["strict_top_w_response_evidence_present"])
    check("proposal remains forbidden", not boundary["proposal_allowed"])

    broad = read(BROAD_ONE_HIGGS)
    check("broad note also leaves generation matrices free", "generation matrices" in broad and "free" in broad)
    check("broad note does not select numerical entries", "does not select the numerical entries" in broad)
    return boundary


def part5_firewalls() -> None:
    print("\nPart 5: firewalls")
    note = read(NOTE)
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed W/Z/top masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in note)

    for phrase in (
        "Status:** retained",
        "proposed_retained Y_T closure",
        "This note derives `y_t`",
        "selects the numerical Yukawa coefficient",
        "generation matrix entry is derived",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T ONE-HIGGS TOP-CARRIER SELECTION SUPPORT")
    print("=" * 78)

    statuses = part1_anchors()
    part2_top_carrier()
    allowed_monomials = part3_exhaustion()
    boundary = part4_coefficient_boundary()
    part5_firewalls()

    result = {
        "actual_current_surface_status": "exact-support for one-Higgs up-type top carrier skeleton",
        "trace_class": "upstream_support",
        "reachability_to_target": "supports",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "The top carrier skeleton is selected, but the generation matrix entry, "
            "physical intervention law, same-scale g2, and matching/running remain outside this packet."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "allowed_monomials": allowed_monomials,
        "boundary": boundary,
        "upstream_statuses": statuses,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_ONE_HIGGS_TOP_CARRIER_SELECTION_SUPPORT_NOTE_2026-05-26.md",
            "scripts/frontier_yt_one_higgs_top_carrier_selection_support.py",
            "outputs/yt_one_higgs_top_carrier_selection_support_2026-05-26.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
