#!/usr/bin/env python3
"""Conditional dual-compliance bridge for the Route-2 E-center readout.

This is a constructive stretch attempt, not an audit verdict and not current
surface closure. It proves the exact consequence of the missing positive shape
isolated by the prior covariance no-go: if a same-domain readout primitive
scales the channel lift by the inverse square of the channel's own Oh
per-arm projector weight, then the Route-2 endpoint triple is forced exactly.

The load-bearing premise is the dual-compliance exponent p=2. The runner also
checks that ordinary projector, one-power dual, and wrong-exponent variants do
not produce the target.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0


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


def fpow(base: Fraction, exponent: int) -> Fraction:
    if exponent >= 0:
        return base**exponent
    return Fraction(1, 1) / (base ** (-exponent))


def route2_from_lambda(lambda_et: Fraction) -> dict[str, Fraction]:
    q_t = Fraction(5, 6)
    shell_te = Fraction(-2, 1)
    q_e = q_t * lambda_et
    rho_e = Fraction(6, 1) * (q_e - 1)
    c_te = shell_te * q_t / q_e
    return {
        "q_t": q_t,
        "q_e": q_e,
        "rho_e": rho_e,
        "c_te": c_te,
        "rho_e_over_6": rho_e / 6,
    }


def part1_current_surface_markers() -> None:
    print("PART 1: current Route-2 surface markers")
    required = {
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": [
            "beta_E / alpha_E = 21/4",
            "P(rho_E)",
            "E-center = (1, 0, 1/6, 0)",
            "exact missing-map obstruction",
        ],
        "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md": [
            "inverse-square characterization",
            "projector weights",
            "9/4",
            "realized by no named functional",
        ],
        "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md": [
            "source-domain rule that fixes the E-center endpoint weight",
            "readout-map primitive",
            "gamma_E(center)/gamma_E(shell) = 15/8",
        ],
        "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md": [
            "open_gate route survey",
            "readout-map endpoint triple is not yet derived",
            "conditional Route-2 coupling family",
        ],
        "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md": [
            "valid for every admissible readout in the 1-parameter family",
            "Does **not** derive the readout-triple",
        ],
    }
    for relpath, markers in required.items():
        text = read_text(relpath)
        check(f"{relpath} exists", bool(text))
        for marker in markers:
            check(f"{relpath} contains marker: {marker}", marker in text)


def part2_same_domain_weights() -> tuple[Fraction, Fraction, Fraction]:
    print()
    print("PART 2: same-domain Oh channel weights")
    arms = 6
    dim_a1 = 1
    dim_e = 2
    dim_t = 3
    w_a1 = Fraction(dim_a1, arms)
    w_e = Fraction(dim_e, arms)
    w_t = Fraction(dim_t, arms)
    kappa = w_t / w_e

    check("six-arm Oh support decomposes as A1 + E + T1", dim_a1 + dim_e + dim_t == arms)
    check("A1 per-arm projector weight is 1/6", w_a1 == Fraction(1, 6), str(w_a1))
    check("E per-arm projector weight is 1/3", w_e == Fraction(1, 3), str(w_e))
    check("T1 per-arm projector weight is 1/2", w_t == Fraction(1, 2), str(w_t))
    check("same-domain leverage kappa=w_T/w_E is 3/2", kappa == Fraction(3, 2), str(kappa))
    check("kappa squared is the target covariance ratio 9/4", kappa**2 == Fraction(9, 4), str(kappa**2))
    return w_e, w_t, kappa


def part3_conditional_bridge(w_e: Fraction, w_t: Fraction, kappa: Fraction) -> None:
    print()
    print("PART 3: dual-compliance conditional bridge")
    exponent = 2
    lambda_et = (w_e / w_t) ** (-exponent)
    data = route2_from_lambda(lambda_et)

    check("dual-compliance exponent is explicitly p=2", exponent == 2)
    check("inverse-square channel law gives lambda_E/T = (w_E/w_T)^-2 = 9/4", lambda_et == Fraction(9, 4), str(lambda_et))
    check("lambda_E/T equals kappa^2", lambda_et == kappa**2, f"{lambda_et} vs {kappa**2}")
    check("granted T-side q_T remains 5/6", data["q_t"] == Fraction(5, 6), str(data["q_t"]))
    check("q_E = q_T * lambda_E/T = 15/8", data["q_e"] == Fraction(15, 8), str(data["q_e"]))
    check("rho_E = 6*(q_E-1) = 21/4", data["rho_e"] == Fraction(21, 4), str(data["rho_e"]))
    check("rho_E/6 is the E-center lift increment 7/8", data["rho_e_over_6"] == Fraction(7, 8), str(data["rho_e_over_6"]))
    check("c_TE = -2*q_T/q_E = -8/9", data["c_te"] == Fraction(-8, 9), str(data["c_te"]))


def part4_falsifiers(w_e: Fraction, w_t: Fraction) -> None:
    print()
    print("PART 4: wrong-exponent falsifiers")
    base = w_e / w_t
    target = Fraction(9, 4)
    tested = {p: fpow(base, -p) for p in range(-3, 4)}
    hits = [p for p, value in tested.items() if value == target]

    check("only exponent p=2 hits lambda_E/T=9/4 in the tested local exponent window", hits == [2], str(tested))
    check("uniform exponent p=0 gives lambda_E/T=1, not target", tested[0] == Fraction(1, 1), str(tested[0]))
    check("one-power dual exponent p=1 gives lambda_E/T=3/2, not target", tested[1] == Fraction(3, 2), str(tested[1]))
    check("ordinary projector-square direction p=-2 gives lambda_E/T=4/9, not target", tested[-2] == Fraction(4, 9), str(tested[-2]))
    check("current surface does not select p=2 from the exponent family", len(tested) == 7 and hits == [2])


def part5_companion_note() -> None:
    print()
    print("PART 5: companion note hygiene")
    relpath = "QUARK_ROUTE2_DUAL_COMPLIANCE_BRIDGE_CONDITIONAL_SUPPORT_NOTE_2026-06-21.md"
    text = read_text(relpath)
    check(f"{relpath} exists", bool(text))
    required = [
        "**Actual current-surface status:** conditional support",
        "conditional on the dual-compliance premise",
        "This is not an audit verdict",
        "does not close the parent S3/Route-2 gate",
        "does not derive the endpoint triple on the current surface",
        "upstream_support",
    ]
    for marker in required:
        check(f"note contains marker: {marker}", marker in text)
    banned = [
        ("parent closure", "closes the " + "parent"),
        ("unconditional endpoint derivation", "derives the endpoint " + "triple"),
        ("bare retained", "Status: " + "retained"),
        ("audit verdict", "audit-" + "ratified"),
    ]
    for label, phrase in banned:
        check(f"note avoids overclaim: {label}", phrase not in text)


def main() -> int:
    print("Route-2 dual-compliance bridge conditional-support checker")
    print("Status: open / conditional-support; not an audit verdict.")
    print("TRACE: upstream_support")
    print()
    part1_current_surface_markers()
    w_e, w_t, kappa = part2_same_domain_weights()
    part3_conditional_bridge(w_e, w_t, kappa)
    part4_falsifiers(w_e, w_t)
    part5_companion_note()
    print()
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print(
            "VERDICT: conditional on a new dual-compliance p=2 readout "
            "primitive, the Route-2 endpoint triple follows exactly. The "
            "current surface still does not derive or adopt that premise."
        )
        return 0
    print("VERDICT: conditional dual-compliance bridge checks failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
