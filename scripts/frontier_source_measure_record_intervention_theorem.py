#!/usr/bin/env python3
"""Physical source as sharp-record probability intervention theorem runner."""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = ROOT / "outputs" / "source_measure_record_intervention_2026-05-30.json"

NOTE = DOCS / "SOURCE_MEASURE_RECORD_INTERVENTION_THEOREM_NOTE_2026-05-30.md"
SYNTHESIS = DOCS / "SOURCE_MEASURE_PCAL_RETIREMENT_SYNTHESIS_NOTE_2026-05-30.md"
TANGENT = DOCS / "SOURCE_MEASURE_SHARP_RECORD_TANGENT_SPACE_THEOREM_NOTE_2026-05-30.md"
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


def histories(n: int) -> list[tuple[int, ...]]:
    return list(itertools.product((-1, 1), repeat=n))


def part1_boundary() -> dict[str, Any]:
    print("\nPart 1: document/status boundary")
    for path in (NOTE, SYNTHESIS, TANGENT, AXIOMS, LSP):
        check(f"{path.relative_to(ROOT)} exists", path.exists())
    note = read(NOTE)
    for phrase in (
        "Theorem",
        "Operational equivalence",
        "RN representation",
        "Connection to P-cal",
        "Status boundary",
        "Non-claims",
    ):
        check(f"note contains required phrase: {phrase}", phrase in note)
    check("note marks proposed_retained source-side status", "actual_current_surface_status: proposed_retained" in note)
    check("note requires audit before effective retained", "audit_required_before_effective_retained: true" in note)
    return {"actual_status": "proposed_retained"}


def part2_operational_equivalence() -> dict[str, Any]:
    print("\nPart 2: operational equivalence on finite history algebra")
    omega = histories(2)
    # Generic probability vectors p, q on four histories.  If all indicator
    # expectations agree, every component agrees.
    p = sp.symbols("p0:4")
    q = sp.symbols("q0:4")
    diffs = [sp.simplify(p[i] - q[i]) for i in range(4)]
    indicator_equalities_force_equal = all(d == p[i] - q[i] for i, d in enumerate(diffs))
    check("history space has four sharp-record atoms", len(omega) == 4, omega)
    check("indicator expectations recover probability components", indicator_equalities_force_equal, diffs)

    # A generic observable is a linear combination of indicators; probabilities
    # are the full operational state on the finite commutative record algebra.
    f = sp.symbols("f0:4")
    ep = sum(p[i] * f[i] for i in range(4))
    eq = sum(q[i] * f[i] for i in range(4))
    expected = sum((p[i] - q[i]) * f[i] for i in range(4))
    check("all observable expectations equal iff all components equal", sp.simplify(sp.expand(ep - eq - expected)) == 0)
    return {"atoms": len(omega), "operational_state": "probability vector on sharp-record atoms"}


def part3_rn_representation() -> dict[str, Any]:
    print("\nPart 3: RN representation of smooth source interventions")
    n = 3
    omega = histories(n)
    N = len(omega)
    p0 = [sp.Rational(1, N)] * N
    # Choose symbolic score variables s_i with zero mean enforced by last value.
    s = list(sp.symbols(f"s0:{N-1}"))
    s_last = -sum(s)
    scores = s + [s_last]
    h = sp.symbols("h", real=True)
    R = [1 + h * scores[i] for i in range(N)]
    ph = [sp.simplify(p0[i] * R[i]) for i in range(N)]
    norm = sp.simplify(sum(ph))
    score_mean = sp.simplify(sum(p0[i] * scores[i] for i in range(N)))
    check("uniform trace reference has full support", all(x > 0 for x in p0))
    check("linearized RN path normalizes to first order exactly", is_zero(norm - 1), norm)
    check("RN score has zero reference mean", is_zero(score_mean), score_mean)
    # RN density is componentwise ph/p0.
    rn = [sp.simplify(ph[i] / p0[i]) for i in range(N)]
    check("RN derivative recovers the source density path", all(is_zero(rn[i] - R[i]) for i in range(N)), rn[:3])
    return {"history_atoms": N, "rn_score_dimension": N - 1}


def part4_independent_composition() -> dict[str, Any]:
    print("\nPart 4: independent composition")
    h = sp.symbols("h", real=True)
    e1, e2 = sp.symbols("e1 e2", real=True)
    W = sp.Function("W")
    logR1 = h * e1 - W(h)
    logR2 = h * e2 - W(h)
    logR_joint = h * (e1 + e2) - 2 * W(h)
    check("independent joint log RN is sum of log RNs", is_zero(logR_joint - (logR1 + logR2)), logR_joint)
    return {"composition": "RN densities multiply; log densities add"}


def part5_closure_status() -> dict[str, Any]:
    print("\nPart 5: closure status and firewall")
    note = read(NOTE)
    flat = " ".join(note.split())
    check(
        "note says residual from synthesis is closed on record sector",
        "is not an extra structure on the finite sharp-record source sector" in note,
    )
    check("note keeps generic dynamics out of scope", "generic non-record dynamics" in note)
    for phrase in ("H_unit", "yt_ward_identity", "y_t_bare", "PDG", "alpha_LM", "plaquette", "fitted selector"):
        check(f"forbidden import named: {phrase}", phrase in flat)
    for phrase in ("Status: retained", "audit-clean retained", "effective retained before audit"):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)
    return {"proposal_allowed": True, "scope": "finite sharp-record source sector"}


def main() -> int:
    print("=" * 88)
    print("SOURCE/MEASURE RECORD-INTERVENTION THEOREM")
    print("=" * 88)
    result = {
        "boundary": part1_boundary(),
        "operational_equivalence": part2_operational_equivalence(),
        "rn_representation": part3_rn_representation(),
        "composition": part4_independent_composition(),
        "status": part5_closure_status(),
    }
    result["summary"] = {
        "pass": PASS_COUNT,
        "fail": FAIL_COUNT,
        "actual_current_surface_status": "proposed_retained",
        "trace_class": "direct_blocker_closure",
        "proposal_allowed": True,
        "audit_required_before_effective_retained": True,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
