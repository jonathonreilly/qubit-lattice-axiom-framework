#!/usr/bin/env python3
"""Sharp-record probability tangent theorem for source/measure P-cal.

This route removes one layer of semantics: on a finite sharp-record sample
space, every smooth supplied record-probability intervention has a
Radon-Nikodym score tangent.  The retained finite Fisher theorem now supplies
the canonical pairing.  A primitive signed record is therefore a unit tangent
vector; scaling it by lambda changes the tangent norm to lambda^2.  Physical
source semantics and strict same-source top/W response remain out of scope.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = ROOT / "outputs" / "source_measure_sharp_record_tangent_space_2026-05-30.json"

NOTE = DOCS / "SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"
RN_NOTE = DOCS / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
CUMULANT_NOTE = DOCS / "SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS_THEOREM_NOTE_2026-05-30.md"
FISHER_NOTE = DOCS / "SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06.md"
ONB_NOTE = DOCS / "SOURCE_MEASURE_SHARP_RECORD_ORTHONORMAL_RESPONSE_BASIS_NARROW_THEOREM_NOTE_2026-06-05.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-05.md"
LSP = DOCS / "LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md"

PASS_COUNT = 0
FAIL_COUNT = 0


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


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def ledger_row(claim_id: str) -> dict[str, Any]:
    ledger = json.loads(read(LEDGER))
    rows = ledger.get("rows", ledger)
    if isinstance(rows, dict):
        return rows.get(claim_id, {})
    for row in rows:
        if row.get("claim_id") == claim_id:
            return row
    return {}


def part1_boundary() -> dict[str, Any]:
    print("\nPart 1: document/status boundary")
    for path in (NOTE, LEDGER, RN_NOTE, CUMULANT_NOTE, FISHER_NOTE, ONB_NOTE, AXIOMS, LSP):
        check(f"{path.relative_to(ROOT)} exists", path.exists())
    note = read(NOTE)
    for phrase in (
        "Theorem",
        "Tangent-space proof",
        "Exponential chart",
        "Conditional corollary: supplied Y_T source unit",
        "Status boundary",
        "Non-claims",
        "2026-06-08 finite-boundary repair",
        "2026-06-07 authority split",
        "SHARP_RECORD_FISHER_TANGENT_SPACE_NARROW_THEOREM_NOTE_2026-06-06",
        "SOURCE_MEASURE_SHARP_RECORD_ORTHONORMAL_RESPONSE_BASIS_NARROW_THEOREM_NOTE_2026-06-05",
    ):
        check(f"note contains required phrase: {phrase}", phrase in note)
    check("note marks bounded-support status", "actual_current_surface_status: bounded-support" in note)
    check(
        "note names finite load-bearing claim",
        'load_bearing_claim: "finite Fisher tangent plus six diagonal E_ii basis algebra only"' in note,
    )
    check(
        "note marks Y_T interpretation as conditional corollary only",
        'conditional_corollary_only: "Y_T/source interpretation after a separate physical-source bridge"' in note,
    )
    check("note forbids bare retained", "bare_retained_allowed: false" in note)
    flat_note = " ".join(note.split())
    for phrase in (
        "does not supply those bridges",
        "does not prove that this basis is the physical top source basis",
        "strict same-source top/W response",
        "unbounded retained Y_T closure",
    ):
        check(f"boundary phrase present: {phrase}", phrase in flat_note)

    fisher = ledger_row("sharp_record_fisher_tangent_space_narrow_theorem_note_2026-06-06")
    onb = ledger_row("source_measure_sharp_record_orthonormal_response_basis_narrow_theorem_note_2026-06-05")
    check("retained Fisher tangent dependency present in ledger", bool(fisher))
    check("six-diagonal basis dependency present in ledger", bool(onb))
    check("Fisher tangent dependency is audited clean", fisher.get("audit_status") == "audited_clean", fisher.get("audit_status"))
    check("Fisher tangent dependency is retained", fisher.get("effective_status") == "retained", fisher.get("effective_status"))
    check(
        "six-diagonal basis dependency is audited clean",
        onb.get("audit_status") == "audited_clean",
        onb.get("audit_status"),
    )
    check(
        "six-diagonal basis dependency is retained_bounded",
        onb.get("effective_status") == "retained_bounded",
        onb.get("effective_status"),
    )
    check("dependency rows have no open dependency paths", not fisher.get("open_dependency_paths") and not onb.get("open_dependency_paths"))
    return {
        "actual_status": "bounded-support",
        "load_bearing_claim": "finite Fisher tangent plus six diagonal E_ii basis algebra only",
        "conditional_corollary_only": "Y_T/source interpretation after a separate physical-source bridge",
        "dependencies": {
            "fisher_tangent": fisher.get("effective_status"),
            "six_diagonal_basis": onb.get("effective_status"),
        },
    }


def part2_probability_tangent_space() -> dict[str, Any]:
    print("\nPart 2: finite probability tangent space")
    # Two-outcome sharp record with reference p0=(1/2,1/2).  A tangent dp has
    # sum zero.  The score s=dp/p0 is the RN tangent.
    a = sp.symbols("a", real=True)
    p0 = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)])
    dp = sp.Matrix([a, -a])
    score = sp.Matrix([sp.simplify(dp[i] / p0[i]) for i in range(2)])
    check("probability tangent sums to zero", is_zero(sum(dp)), sum(dp))
    check("RN score has zero reference mean", is_zero(sum(p0[i] * score[i] for i in range(2))), score)
    fisher = sp.simplify(sum(p0[i] * score[i] ** 2 for i in range(2)))
    check("Fisher norm of generic two-outcome tangent is 4a^2", is_zero(fisher - 4 * a**2), fisher)

    # Primitive signed record epsilon=(+1,-1) corresponds to dp=(1/2,-1/2).
    score_prim = sp.Matrix([1, -1])
    dp_prim = sp.Matrix([p0[i] * score_prim[i] for i in range(2)])
    fisher_prim = sp.simplify(sum(p0[i] * score_prim[i] ** 2 for i in range(2)))
    check("primitive score tangent is signed record", list(score_prim) == [1, -1], score_prim)
    check("primitive dp sums to zero", is_zero(sum(dp_prim)), dp_prim)
    check("primitive signed-record tangent has Fisher norm one", is_zero(fisher_prim - 1), fisher_prim)
    return {"primitive_score": "(+1,-1)", "primitive_fisher_norm": "1"}


def part3_scaled_tangent_and_exponential_chart() -> dict[str, Any]:
    print("\nPart 3: scaled tangent and exponential chart")
    lam, h = sp.symbols("lambda h", positive=True, real=True)
    eps = {1: 1, -1: -1}
    p0 = {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}
    fisher_lam = sp.simplify(sum(p0[e] * (lam * eps[e]) ** 2 for e in (1, -1)))
    check("lambda-scaled signed tangent has Fisher norm lambda^2", is_zero(fisher_lam - lam**2), fisher_lam)
    check("unit tangent condition selects lambda=1", sp.solve(sp.Eq(fisher_lam, 1), lam) == [1])

    # Exponential chart realizes any score s as a normalized positive path with
    # that score at the origin; W is forced by normalization.
    W = sp.log(sum(p0[e] * sp.exp(h * eps[e]) for e in (1, -1)))
    R = {e: sp.exp(h * eps[e] - W) for e in (1, -1)}
    score = {e: sp.diff(sp.log(R[e]), h).subs(h, 0) for e in (1, -1)}
    norm = sp.simplify(sum(p0[e] * R[e] for e in (1, -1)))
    check("exponential chart normalizes the path", is_zero(norm - 1), norm)
    check("exponential chart has requested score", score[1] == 1 and score[-1] == -1, score)
    check("chart normalizer is log moment generator", is_zero(W - sp.log(sp.cosh(h))), W)
    return {"exponential_chart": "R_h=exp(h epsilon - log E exp(h epsilon))"}


def part4_supplied_basis_unit() -> dict[str, Any]:
    print("\nPart 4: supplied six-diagonal basis unit")
    lam = sp.symbols("lambda", positive=True)
    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    fisher = sp.simplify(u.dot(u))
    fisher_lam = sp.simplify((lam * u).dot(lam * u))
    check("supplied six-component democratic tangent has unit norm", is_zero(fisher - 1), fisher)
    check("lambda-scaled supplied tangent has norm lambda^2", is_zero(fisher_lam - lam**2), fisher_lam)
    check("unit tangent selects lambda=1", sp.solve(sp.Eq(fisher_lam, 1), lam) == [1])
    check("supplied-basis component coefficient is 1/sqrt(6)", is_zero(u[0] - 1 / sp.sqrt(6)), u[0])
    return {"supplied_basis_component": "1/sqrt(6)", "yt_interpretation": "conditional_bridge_only"}


def part5_firewall() -> None:
    print("\nPart 5: firewall")
    note = read(NOTE)
    flat = " ".join(note.split())
    for phrase in ("H_unit", "yt_ward_identity", "y_t_bare", "PDG", "alpha_LM", "plaquette", "fitted selector"):
        check(f"forbidden import named in firewall: {phrase}", phrase in flat)
    for phrase in ("Status: retained", "unbounded retained Y_T closure is claimed", "audit-clean retained"):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("SOURCE/MEASURE SHARP-RECORD TANGENT-SPACE THEOREM")
    print("=" * 88)
    result = {
        "boundary": part1_boundary(),
        "tangent_space": part2_probability_tangent_space(),
        "exponential_chart": part3_scaled_tangent_and_exponential_chart(),
        "supplied_basis_unit": part4_supplied_basis_unit(),
    }
    part5_firewall()
    result["summary"] = {
        "pass": PASS_COUNT,
        "fail": FAIL_COUNT,
        "actual_current_surface_status": "bounded-support",
        "trace_class": "direct_blocker_closure",
        "reachability_to_target": "partially_closes",
        "proposal_allowed": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
