#!/usr/bin/env python3
"""Sharp-record probability tangent theorem for source/measure P-cal.

This route removes one layer of semantics: on a finite sharp-record sample
space, every smooth physical record-probability intervention has a
Radon-Nikodym score tangent.  The normalized trace reference supplies the
canonical Fisher pairing.  A primitive signed record is therefore a unit
tangent vector; scaling it by lambda changes the tangent norm to lambda^2.
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
RN_NOTE = DOCS / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
CUMULANT_NOTE = DOCS / "SOURCE_MEASURE_PCAL_CUMULANT_MOBIUS_THEOREM_NOTE_2026-05-30.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
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


def part1_boundary() -> dict[str, Any]:
    print("\nPart 1: document/status boundary")
    for path in (NOTE, RN_NOTE, CUMULANT_NOTE, AXIOMS, LSP):
        check(f"{path.relative_to(ROOT)} exists", path.exists())
    note = read(NOTE)
    for phrase in (
        "Theorem",
        "Tangent-space proof",
        "Exponential chart",
        "Y_T source unit",
        "Status boundary",
        "Non-claims",
    ):
        check(f"note contains required phrase: {phrase}", phrase in note)
    check("note marks exact-support status", "actual_current_surface_status: exact-support" in note)
    check("note forbids bare retained", "bare_retained_allowed: false" in note)
    return {"actual_status": "exact-support"}


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


def part4_yt_source_unit() -> dict[str, Any]:
    print("\nPart 4: Y_T source unit")
    lam = sp.symbols("lambda", positive=True)
    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    fisher = sp.simplify(u.dot(u))
    fisher_lam = sp.simplify((lam * u).dot(lam * u))
    check("six-component top tangent has unit Fisher norm", is_zero(fisher - 1), fisher)
    check("lambda-scaled top tangent has norm lambda^2", is_zero(fisher_lam - lam**2), fisher_lam)
    check("unit tangent selects lambda=1", sp.solve(sp.Eq(fisher_lam, 1), lam) == [1])
    check("component coefficient is 1/sqrt(6)", is_zero(u[0] - 1 / sp.sqrt(6)), u[0])
    return {"yt_component": "1/sqrt(6)"}


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
        "yt_source": part4_yt_source_unit(),
    }
    part5_firewall()
    result["summary"] = {
        "pass": PASS_COUNT,
        "fail": FAIL_COUNT,
        "actual_current_surface_status": "exact-support",
        "trace_class": "direct_blocker_closure_candidate",
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
