#!/usr/bin/env python3
"""Source/measure P-cal RN-cocycle theorem runner.

This runner checks the first source/measure retirement route:

  sharp projective record + RN source cocycle + primitive unit score
    -> W(h) = log E_0 exp(h O)
    -> primitive Fisher source unit
    -> lambda = 1 on the six-component Y_T top source.

The runner is deliberately status-aware.  It verifies exact algebraic support
for the RN-cocycle route, and it also verifies that the route is not presented
as unbounded retained Y_T closure while the physical-source-as-RN-cocycle
identification remains an audit decision.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = ROOT / "outputs" / "source_measure_pcal_rn_cocycle_2026-05-30.json"

NOTE = DOCS / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
LSP = DOCS / "LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md"
P1P2 = DOCS / "OBSERVABLE_PRINCIPLE_P1P2_TWO_STAGE_SYNTHESIS_NARROW_THEOREM_NOTE_2026-05-28.md"
SOURCE_ACTION = DOCS / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
YT_TIER_A = DOCS / "YT_TIER_A_SOURCE_ACTION_TOP_PREMISE_CLOSURE_NOTE_2026-05-29.md"
YT_NOGO = DOCS / "YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md"

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


def flat(text: str) -> str:
    return " ".join(text.split())


def part1_document_boundary() -> dict[str, Any]:
    print("\nPart 1: document and status boundary")
    for path in (NOTE, AXIOMS, LSP, P1P2, SOURCE_ACTION, YT_TIER_A, YT_NOGO):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for phrase in (
        "Theorem",
        "RN cocycle proof",
        "Connection to P-cal",
        "Application to Y_T",
        "Status boundary",
        "Non-claims",
    ):
        check(f"note contains required phrase: {phrase}", phrase in note)

    check("note marks actual status as exact-support", "actual_current_surface_status: exact-support" in note)
    check("note forbids bare retained", "bare_retained_allowed: false" in note)
    check("note names physical-source identification as residual", "physical source intervention is an RN cocycle" in note)

    p1p2 = read(P1P2)
    check("parent synthesis names P-cal as residual", "P-cal" in p1p2 and "single residual premise" in p1p2)
    check("parent synthesis records F_p wall", "F_p" in p1p2 and "Pattern-L wall" in p1p2)

    nogo = read(YT_NOGO)
    check("YT no-go exposes lambda family", "y_33(lambda)=lambda/sqrt(6)" in nogo)
    check("YT no-go leaves primitive source/action route live", "derive the primitive source/action premise" in nogo)

    return {
        "actual_status": "exact-support",
        "pcal_residual": "physical source intervention is an RN cocycle over sharp records",
    }


def part2_projective_record() -> dict[str, Any]:
    print("\nPart 2: sharp projective signed record")
    sigma_z = sp.Matrix([[1, 0], [0, -1]])
    ident = sp.eye(2)
    p_plus = (ident + sigma_z) / 2
    p_minus = (ident - sigma_z) / 2

    check("P_plus is a projector", p_plus * p_plus == p_plus)
    check("P_minus is a projector", p_minus * p_minus == p_minus)
    check("projectors resolve identity", p_plus + p_minus == ident)
    check("projectors are orthogonal", p_plus * p_minus == sp.zeros(2))
    signed = p_plus - p_minus
    check("signed readout is sigma_z", signed == sigma_z)
    check("signed readout squares to identity", signed * signed == ident)

    return {
        "outcomes": [-1, 1],
        "signed_operator": "sigma_z = P_+ - P_-",
    }


def part3_rn_cocycle_forces_log_normalizer() -> dict[str, Any]:
    print("\nPart 3: RN cocycle forces log normalizer")
    h, lam = sp.symbols("h lambda", real=True, positive=True)

    # Uniform sharp-record reference on epsilon = +/- 1.
    weights = {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}
    moment = sum(weights[e] * sp.exp(h * e) for e in (-1, 1))
    W = sp.log(moment)
    R = {e: sp.exp(h * e - W) for e in (-1, 1)}

    norm = sp.simplify(sum(weights[e] * R[e] for e in (-1, 1)))
    check("RN density normalizes exactly", is_zero(norm - 1), norm)
    check("normalizer is log cosh(h)", is_zero(W - sp.log(sp.cosh(h))), W)

    score = {e: sp.diff(sp.log(R[e]), h).subs(h, 0) for e in (-1, 1)}
    fisher = sp.simplify(sum(weights[e] * score[e] ** 2 for e in (-1, 1)))
    check("origin score for + record is +1", is_zero(score[1] - 1), score[1])
    check("origin score for - record is -1", is_zero(score[-1] + 1), score[-1])
    check("primitive Fisher norm is one", is_zero(fisher - 1), fisher)

    # Sequential independent records: RN densities multiply, log densities add.
    e1, e2 = sp.symbols("e1 e2")
    W2 = 2 * W
    log_R_total = h * e1 + h * e2 - W2
    log_R_sum = (h * e1 - W) + (h * e2 - W)
    check("sequential RN log-density is additive", is_zero(log_R_total - log_R_sum), log_R_total)

    # Scaled source families are normalized but not primitive unit coordinates.
    moment_lam = sum(weights[e] * sp.exp(h * lam * e) for e in (-1, 1))
    W_lam = sp.log(moment_lam)
    R_lam = {e: sp.exp(h * lam * e - W_lam) for e in (-1, 1)}
    score_lam = {e: sp.diff(sp.log(R_lam[e]), h).subs(h, 0) for e in (-1, 1)}
    fisher_lam = sp.simplify(sum(weights[e] * score_lam[e] ** 2 for e in (-1, 1)))
    check("scaled source normalizes exactly", is_zero(sum(weights[e] * R_lam[e] for e in (-1, 1)) - 1))
    check("scaled score is lambda epsilon", is_zero(score_lam[1] - lam) and is_zero(score_lam[-1] + lam))
    check("scaled Fisher norm is lambda^2", is_zero(fisher_lam - lam**2), fisher_lam)
    check("primitive Fisher-unit condition selects lambda=1", sp.solve(sp.Eq(fisher_lam, 1), lam) == [1])

    # Bare-gradient check against the F_p family: normalized logarithmic
    # derivatives can hide p, but the RN score/Fisher unit cannot.
    p = sp.symbols("p", positive=True)
    Fp = sp.exp(p * W)
    bare_grad = sp.diff(Fp, h).subs(h, 0)
    log_grad = sp.diff(sp.log(Fp), h).subs(h, 0)
    check("bare gradient of Z^p at origin is zero for centered record", is_zero(bare_grad), bare_grad)
    check("log-gradient scale of Z^p is p times primitive mean response", is_zero(log_grad), log_grad)
    second_log_grad = sp.diff(sp.log(Fp), h, 2).subs(h, 0)
    check("second log-gradient of Z^p carries scale p", is_zero(second_log_grad - p), second_log_grad)

    return {
        "W": "log E_0 exp(h epsilon)",
        "normalization": "E_0 R_h = 1",
        "fisher_unit": "I(0)=1",
        "scaled_family": "I_lambda(0)=lambda^2",
    }


def part4_top_source_application() -> dict[str, Any]:
    print("\nPart 4: Y_T six-component top source application")
    lam = sp.symbols("lambda", positive=True)
    u = sp.Matrix([1 / sp.sqrt(6)] * 6)
    norm = sp.simplify((u.T * u)[0])
    scaled_norm = sp.simplify((lam * u).dot(lam * u))
    check("democratic six-component vector has unit norm", is_zero(norm - 1), norm)
    check("each component is 1/sqrt(6)", all(is_zero(x - 1 / sp.sqrt(6)) for x in u), list(u))
    check("scaled top-source Fisher norm is lambda^2", is_zero(scaled_norm - lam**2), scaled_norm)
    check("unit Fisher source condition selects lambda=1", sp.solve(sp.Eq(scaled_norm, 1), lam) == [1])
    check("selected Y_T component is 1/sqrt(6)", is_zero(u[0] - 1 / sp.sqrt(6)), u[0])

    return {
        "top_source_vector": "(1,1,1,1,1,1)/sqrt(6)",
        "component": "1/sqrt(6)",
        "remaining_if_rn_cocycle_accepted": "none for lambda",
    }


def part5_firewall() -> None:
    print("\nPart 5: forbidden-import and overclaim firewall")
    note = read(NOTE)
    body = flat(note)
    for phrase in (
        "H_unit",
        "yt_ward_identity",
        "y_t_bare",
        "observed top",
        "PDG",
        "alpha_LM",
        "plaquette",
        "fitted selector",
    ):
        check(f"firewall names forbidden import: {phrase}", phrase in body)

    forbidden_status_phrases = (
        "Status: retained",
        "effective retained",
        "audit-clean retained",
        "unbounded retained Y_T closure is claimed",
    )
    for phrase in forbidden_status_phrases:
        check(f"forbidden status phrase absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 88)
    print("SOURCE/MEASURE P-CAL RN-COCYCLE THEOREM")
    print("=" * 88)

    result = {
        "document_boundary": part1_document_boundary(),
        "projective_record": part2_projective_record(),
        "rn_cocycle": part3_rn_cocycle_forces_log_normalizer(),
        "yt_application": part4_top_source_application(),
    }
    part5_firewall()

    result.update(
        {
            "summary": {
                "pass": PASS_COUNT,
                "fail": FAIL_COUNT,
                "actual_current_surface_status": "exact-support",
                "trace_class": "direct_blocker_closure_candidate",
                "target_blocker": "P-cal / primitive source-action unit",
                "proposal_allowed": False,
                "bare_retained_allowed": False,
            }
        }
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
