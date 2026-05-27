#!/usr/bin/env python3
"""First-principles transfer-response boundary theorem for Y_T."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_first_principles_transfer_response_boundary_2026-05-27.json"

NOTE = DOCS / "YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md"
FULL_STACK = DOCS / "YT_FULL_CLOSURE_STACK_AND_STRICT_POLE_RESPONSE_CONTRACT_NOTE_2026-05-26.md"
FH_GATE = DOCS / "YT_FH_TOP_W_RESPONSE_RATIO_GATE_NOTE_2026-05-25.md"
TRANSFER_OBSTRUCTION = DOCS / "YT_STRICT_SAME_SOURCE_TOP_W_RESPONSE_COEFFICIENT_OBSTRUCTION_NOTE_2026-05-27.md"
C3_REAL_SOURCE = DOCS / "YT_C3_REAL_RECORD_REFLECTION_EVEN_SOURCE_THEOREM_NOTE_2026-05-27.md"
C3_TOP_LINE = DOCS / "YT_C3_TOP_LINE_MASS_ORDERING_OBSTRUCTION_NOTE_2026-05-27.md"

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


def part1_anchors() -> None:
    print("\nPart 1: note anchors and scope")
    for path in (NOTE, FULL_STACK, FH_GATE, TRANSFER_OBSTRUCTION, C3_REAL_SOURCE, C3_TOP_LINE):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    for section in (
        "Question",
        "Answer",
        "Theorem 1: Transfer Pole Response",
        "Theorem 2: Same-Source Top/W Readout",
        "Conditional Closure Row",
        "Formal-Transfer No-Go",
        "Relation To The C3 Source Work",
        "What This Burns Down",
        "What Remains Open",
        "Non-Claims",
        "Claim-Status Certificate",
    ):
        check(f"note contains section: {section}", f"## {section}" in note)

    for phrase in (
        "actual_current_surface_status: exact-support / formal-transfer no-go",
        "proposal_allowed: false",
        "bare_retained_allowed: false",
        "formal transfer theorem alone cannot force `1/sqrt(6)`",
        "first_open_gate_after_this_note",
    ):
        check(f"claim firewall/status phrase present: {phrase}", phrase in note)


def part2_transfer_derivative_identity() -> dict[str, str]:
    print("\nPart 2: transfer derivative identity")
    ell, a_t = sp.symbols("ell a_t", positive=True)
    l0, lx = sp.symbols("Lambda_0 Lambda_X", positive=True)
    g0, gx = sp.symbols("g_0 g_X", real=True)
    lambda_0 = l0 * sp.exp(-a_t * g0 * ell)
    lambda_x = lx * sp.exp(-a_t * gx * ell)

    mass = -sp.log(lambda_x / lambda_0) / a_t
    derivative = sp.simplify(sp.diff(mass, ell))
    expected = sp.simplify(gx - g0)
    formula = sp.simplify(
        -(
            sp.diff(lambda_x, ell) / lambda_x
            - sp.diff(lambda_0, ell) / lambda_0
        )
        / a_t
    )

    check("log-eigenvalue derivative equals sector generator difference", is_zero(derivative - expected), derivative)
    check("explicit transfer derivative formula matches", is_zero(formula - expected), formula)
    check("vacuum subtraction is load-bearing", derivative.has(g0), derivative)

    return {
        "dM_X_dell": "g_X - g_0",
        "transfer_formula": "-a_t^-1[(Lambda_X'/Lambda_X)-(Lambda_0'/Lambda_0)]",
    }


def part3_same_source_ratio() -> dict[str, str]:
    print("\nPart 3: same-source top/W response ratio")
    g2, y, A, c = sp.symbols("g_2 y_t A c", positive=True)
    dmt = y * A / sp.sqrt(2)
    dmw = g2 * A / 2
    recovered = sp.simplify(g2 / sp.sqrt(2) * dmt / dmw)
    check("same-source readout recovers y_t", is_zero(recovered - y), recovered)

    recovered_reparam = sp.simplify(g2 / sp.sqrt(2) * (dmt / c) / (dmw / c))
    check("common source reparameterization cancels", is_zero(recovered_reparam - y), recovered_reparam)

    target_dmt = A / sp.sqrt(12)
    target_recovered = sp.simplify(g2 / sp.sqrt(2) * target_dmt / dmw)
    check("target top row A/sqrt(12) gives 1/sqrt(6)", is_zero(target_recovered - 1 / sp.sqrt(6)), target_recovered)

    return {
        "same_source_readout": "y_t",
        "target_dM_t_dell": "A/sqrt(12)",
        "target_readout": "1/sqrt(6)",
    }


def part4_formal_transfer_counterfamily() -> dict[str, Any]:
    print("\nPart 4: finite formal-transfer counterfamily")
    ell, a_t, g2, A, mw0, mt0, kappa = sp.symbols(
        "ell a_t g_2 A M_W0 M_t0 kappa", positive=True
    )
    e0 = sp.Integer(0)
    ew = mw0 + ell * g2 * A / 2
    et = mt0 + ell * kappa * A / sp.sqrt(2)

    dmw = sp.simplify(sp.diff(ew - e0, ell))
    dmt = sp.simplify(sp.diff(et - e0, ell))
    readout = sp.simplify(g2 / sp.sqrt(2) * dmt / dmw)

    check("W response row is fixed in the counterfamily", is_zero(dmw - g2 * A / 2), dmw)
    check("top response row contains free kappa", is_zero(dmt - kappa * A / sp.sqrt(2)), dmt)
    check("top/W readout returns kappa", is_zero(readout - kappa), readout)

    k1 = 1 / sp.sqrt(6)
    k2 = 2 / sp.sqrt(6)
    readout_1 = sp.simplify(readout.subs(kappa, k1))
    readout_2 = sp.simplify(readout.subs(kappa, k2))
    check("two kappa choices differ", sp.simplify(readout_1 - readout_2) != 0, (readout_1, readout_2))
    check("W row is unchanged by kappa variation", not dmw.has(kappa), dmw)

    # Finite numerical witness for isolated eigenvalues and positivity of T = exp(-a H).
    vals = {a_t: 1, g2: sp.Rational(3, 5), A: sp.Rational(7, 4), mw0: 2, mt0: 5, ell: 0}
    eigenvalues_k1 = [
        sp.exp(-vals[a_t] * e0.subs(vals) if hasattr(e0, "subs") else 0),
        sp.exp(-vals[a_t] * ew.subs({**vals, kappa: k1})),
        sp.exp(-vals[a_t] * et.subs({**vals, kappa: k1})),
    ]
    check("representative transfer eigenvalues are positive", all(v > 0 for v in eigenvalues_k1), eigenvalues_k1)
    check("representative W/top eigenvalues are isolated", len(set(map(sp.simplify, eigenvalues_k1))) == 3, eigenvalues_k1)

    return {
        "counterfamily_status": "formal transfer axioms satisfied while kappa varies",
        "dM_W_dell": "g_2*A/2",
        "dM_t_dell": "kappa*A/sqrt(2)",
        "readout": "kappa",
        "witness_readouts": ["1/sqrt(6)", "2/sqrt(6)"],
    }


def c3_cycle() -> sp.Matrix:
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def part5_c3_boundary() -> dict[str, str]:
    print("\nPart 5: C3 source boundary")
    C = c3_cycle()
    I = sp.eye(3)
    Bx = (C + C**2) / sp.sqrt(6)
    omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    projectors = {
        "P_0": (I + C + C**2) / 3,
        "P_omega": (I + omega**-1 * C + omega**-2 * C**2) / 3,
        "P_omega2": (I + omega**-2 * C + omega**-4 * C**2) / 3,
    }
    responses = {
        name: sp.simplify(sp.expand_complex(sp.trace(P * Bx)))
        for name, P in projectors.items()
    }

    check("C3 singlet response is 2/sqrt(6)", is_zero(responses["P_0"] - 2 / sp.sqrt(6)), responses["P_0"])
    check("first nontrivial response is -1/sqrt(6)", is_zero(responses["P_omega"] + 1 / sp.sqrt(6)), responses["P_omega"])
    check("second nontrivial response is -1/sqrt(6)", is_zero(responses["P_omega2"] + 1 / sp.sqrt(6)), responses["P_omega2"])

    magnitudes = {
        name: sp.sqrt(sp.simplify(value * sp.conjugate(value)))
        for name, value in responses.items()
    }
    check("mass-ordering by response magnitude selects singlet", magnitudes["P_0"] > magnitudes["P_omega"], magnitudes)
    check("nontrivial line supplies target magnitude only with extra line law", is_zero(abs(responses["P_omega"]) - 1 / sp.sqrt(6)), responses["P_omega"])

    return {
        "B_x": "(C+C^2)/sqrt(6)",
        "P_0_response": "2/sqrt(6)",
        "P_nontrivial_response": "-1/sqrt(6)",
        "boundary": "nontrivial top-line law remains load-bearing",
    }


def part6_firewalls() -> None:
    print("\nPart 6: firewalls and non-claims")
    note = read(NOTE)
    one_line = " ".join(note.split())
    for phrase in (
        "`H_unit`",
        "`yt_ward_identity`",
        "`y_t_bare`",
        "observed W/Z/top masses",
        "PDG",
        "`alpha_LM`",
        "plaquette/u0",
        "Planck",
        "alpha_s",
        "fitted selector",
    ):
        check(f"firewall phrase present: {phrase}", phrase in one_line)

    for phrase in (
        "Status:** retained",
        "Status:** proposed_retained",
        "This note derives `y_t`",
        "This note proves retained `Y_T` closure",
        "the physical top pole projector is derived",
        "strict top/W pole-response evidence exists",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def main() -> int:
    print("=" * 78)
    print("Y_T FIRST-PRINCIPLES TRANSFER-RESPONSE BOUNDARY THEOREM")
    print("=" * 78)

    part1_anchors()
    transfer = part2_transfer_derivative_identity()
    ratio = part3_same_source_ratio()
    counterfamily = part4_formal_transfer_counterfamily()
    c3 = part5_c3_boundary()
    part6_firewalls()

    result = {
        "actual_current_surface_status": "exact-support / formal-transfer no-go",
        "trace_class": "negative_route_pruning",
        "reachability_to_target": "partially_closes",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Transfer/Feynman-Hellmann first principles prove the exact response "
            "formula and same-source ratio, but a finite positive transfer "
            "counterfamily leaves the top sector matrix element free."
        ),
        "bare_retained_allowed": False,
        "audit_required_before_effective_retained": True,
        "route_pruned": "formal transfer-matrix first principles alone force kappa",
        "first_open_gate_after_this_note": (
            "coefficient-certified same-surface top sector response row, or "
            "non-mass-ordering C3 top-line law"
        ),
        "transfer_derivative": transfer,
        "same_source_ratio": ratio,
        "formal_transfer_counterfamily": counterfamily,
        "c3_boundary": c3,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
        "review_surface": [
            "docs/YT_FIRST_PRINCIPLES_TRANSFER_RESPONSE_BOUNDARY_THEOREM_NOTE_2026-05-27.md",
            "scripts/frontier_yt_first_principles_transfer_response_boundary.py",
            "outputs/yt_first_principles_transfer_response_boundary_2026-05-27.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
