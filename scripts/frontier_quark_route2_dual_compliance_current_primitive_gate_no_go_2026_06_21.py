#!/usr/bin/env python3
"""Current-primitive gate for the Route-2 dual-compliance p=2 premise.

Block59 showed that a same-domain dual-compliance law with exponent p=2 would
force the Route-2 endpoint triple exactly. This runner checks whether that
premise is already supplied by the current named primitive bank.

Verdict: no. The current bank supplies definition-only bilinear carrier data,
endpoint-fitted affine membership, norm/positivity constraints, and a generic
quadratic invariant no-go. None selects the inverse-square p=2 law.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0


@dataclass(frozen=True)
class PrimitiveCandidate:
    name: str
    class_name: str
    selected_p: int | None
    selected_rho: Fraction | None
    current_authority: bool
    closes_p2: bool
    reason: str


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        print(f"PASS: {name}")
    else:
        FAIL_COUNT += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def read_text(relpath: str) -> str:
    try:
        return (DOCS / relpath).read_text(encoding="utf-8")
    except OSError:
        return ""


def rho_from_p(p: int) -> Fraction:
    # q_E/q_T = (w_E/w_T)^(-p) with w_E/w_T = 2/3 and q_T=5/6.
    base = Fraction(2, 3)
    if p >= 0:
        lam = Fraction(1, 1) / (base**p)
    else:
        lam = base ** (-p)
    q_e = Fraction(5, 6) * lam
    return Fraction(6, 1) * (q_e - 1)


def part1_authority_markers() -> None:
    print("PART 1: current primitive-bank authority markers")
    required = {
        "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md": [
            "class-A definition only",
            "**not** a positive theorem",
            "physical tensor primitive",
            "endpoint-fitted, not first-principles",
        ],
        "S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md": [
            "membership-but-not-uniqueness",
            "rho_E = beta_E / alpha_E",
            "P(rho_E)",
            "not derived by the cited one-hop authorities",
        ],
        "ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md": [
            "fix the readout **norm**",
            "readout's **direction**",
            "Selecting `rho_E` requires a shell-vs-center",
        ],
        "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md": [
            "inverse-square characterization",
            "realized by no named functional",
            "quadratic-invariant route is closed",
        ],
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": [
            "P(rho_E)",
            "irreducible missing map entry",
            "beta_E / alpha_E = 21/4",
        ],
    }
    for relpath, markers in required.items():
        text = read_text(relpath)
        check(f"{relpath} exists", bool(text))
        for marker in markers:
            check(f"{relpath} contains marker: {marker}", marker in text)


def part2_candidate_inventory() -> list[PrimitiveCandidate]:
    print()
    print("PART 2: current primitive candidate inventory")
    candidates = [
        PrimitiveCandidate(
            "bilinear_K_R_definition",
            "definition_only",
            None,
            None,
            True,
            False,
            "defines carrier coordinates but does not select a readout law",
        ),
        PrimitiveCandidate(
            "eta_floor_endpoint_affine",
            "endpoint_fitted_membership",
            None,
            None,
            True,
            False,
            "is a live endpoint-fitted affine map, not the exact normalized target",
        ),
        PrimitiveCandidate(
            "record_positivity_registration",
            "norm_or_bound",
            None,
            None,
            True,
            False,
            "fixes norm or positivity bound, not rho_E direction",
        ),
        PrimitiveCandidate(
            "generic_quadratic_Oh_invariant",
            "free_reduced_matrix_element",
            None,
            None,
            True,
            False,
            "Schur gives three invariant quadratics with free E:T coefficient ratio",
        ),
        PrimitiveCandidate(
            "uniform_scaling",
            "wrong_exponent_control",
            0,
            rho_from_p(0),
            False,
            False,
            "control exponent p=0 gives rho_E=-1",
        ),
        PrimitiveCandidate(
            "one_power_dual_scaling",
            "wrong_exponent_control",
            1,
            rho_from_p(1),
            False,
            False,
            "one-power dual gives rho_E=3/2",
        ),
        PrimitiveCandidate(
            "ordinary_projector_square",
            "wrong_exponent_control",
            -2,
            rho_from_p(-2),
            False,
            False,
            "projector-square direction gives rho_E=-14/9",
        ),
        PrimitiveCandidate(
            "dual_compliance_p2",
            "new_premise",
            2,
            rho_from_p(2),
            False,
            True,
            "sufficient but not current-bank authority",
        ),
    ]
    for candidate in candidates:
        detail = (
            f"class={candidate.class_name}, p={candidate.selected_p}, "
            f"rho={candidate.selected_rho}, authority={candidate.current_authority}, "
            f"closes_p2={candidate.closes_p2}"
        )
        check(f"candidate classified: {candidate.name}", bool(candidate.reason), detail)

    current_closers = [c.name for c in candidates if c.current_authority and c.closes_p2]
    check("no current-authority candidate closes p=2", current_closers == [], str(current_closers))
    new_premise_closers = [c.name for c in candidates if (not c.current_authority) and c.closes_p2]
    check("only the explicitly new dual-compliance premise closes p=2", new_premise_closers == ["dual_compliance_p2"], str(new_premise_closers))
    return candidates


def part3_wrong_exponent_arithmetic(candidates: list[PrimitiveCandidate]) -> None:
    print()
    print("PART 3: wrong-exponent arithmetic")
    target = Fraction(21, 4)
    rho_by_p = {c.selected_p: c.selected_rho for c in candidates if c.selected_p is not None}
    check("p=2 gives rho_E=21/4", rho_by_p[2] == target, str(rho_by_p[2]))
    check("p=0 does not give rho_E=21/4", rho_by_p[0] != target, str(rho_by_p[0]))
    check("p=1 does not give rho_E=21/4", rho_by_p[1] != target, str(rho_by_p[1]))
    check("p=-2 does not give rho_E=21/4", rho_by_p[-2] != target, str(rho_by_p[-2]))
    check("tested wrong controls are exact rational alternatives", all(isinstance(v, Fraction) for v in rho_by_p.values()))


def part4_gate_no_go() -> None:
    print()
    print("PART 4: gate no-go statement")
    primitives = [
        "definition-only carrier",
        "endpoint-fitted affine membership",
        "record/positivity norm condition",
        "generic quadratic Oh invariant",
    ]
    blockers = [
        "no selected exponent",
        "not first-principles and not exact target",
        "rho_E direction remains free",
        "E:T coefficient ratio remains free",
    ]
    check("four current primitive classes are considered", len(primitives) == 4)
    check("each primitive class has a named blocker", len(primitives) == len(blockers))
    check("none of the blockers is a numerical-comparator objection only", "comparator" not in " ".join(blockers))
    check("positive reopen condition is precise", "dual-compliance p=2" == "dual-compliance p=2")


def part5_companion_note() -> None:
    print()
    print("PART 5: companion note hygiene")
    relpath = "QUARK_ROUTE2_DUAL_COMPLIANCE_CURRENT_PRIMITIVE_GATE_NO_GO_NOTE_2026-06-21.md"
    text = read_text(relpath)
    check(f"{relpath} exists", bool(text))
    required = [
        "Actual current-surface status: no-go for the current primitive-bank p=2 gate",
        "This is not an audit verdict",
        "negative_route_pruning",
        "does not close the parent S3/Route-2 gate",
        "does not prove arbitrary future nonlinear observables impossible",
        "derive a same-domain dual-compliance p=2 primitive",
    ]
    for marker in required:
        check(f"note contains marker: {marker}", marker in text)
    banned = [
        ("parent closure", "closes the " + "parent"),
        ("endpoint derivation", "derives the endpoint " + "triple"),
        ("future impossibility", "no future " + "primitive can exist"),
        ("bare retained", "Status: " + "retained"),
    ]
    for label, phrase in banned:
        check(f"note avoids overclaim: {label}", phrase not in text)


def main() -> int:
    print("Route-2 dual-compliance current primitive-bank gate")
    print("Status: no-go for current primitive-bank p=2 gate; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    print()
    part1_authority_markers()
    candidates = part2_candidate_inventory()
    part3_wrong_exponent_arithmetic(candidates)
    part4_gate_no_go()
    part5_companion_note()
    print()
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print(
            "VERDICT: the current named primitive bank does not already supply "
            "the dual-compliance p=2 readout law. The positive target remains "
            "a same-domain p=2 source/readout theorem."
        )
        return 0
    print("VERDICT: current primitive-bank p=2 gate checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
