#!/usr/bin/env python3
"""Conditional Route-2 p=2 source/readout theorem attempt.

This runner tests a constructive same-domain premise for the open Route-2
readout endpoint: two-sided canonical-dual Schur compliance. The premise says
that both source preparation and readout registration use the canonical dual
of the same O_h projector-weight frame. On the six-arm star this makes the
channel lift scale as q_X proportional to w_X^-2.

Status:
  conditional-support only. The runner proves the consequence of the stated
  same-domain premise and checks controls. It does not assert that the premise
  is already present on the current surface and does not apply an audit verdict.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0

Matrix = list[list[Fraction]]


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def eye(n: int) -> Matrix:
    return [[Fraction(int(i == j), 1) for j in range(n)] for i in range(n)]


def zeros(n: int) -> Matrix:
    return [[Fraction(0, 1) for _ in range(n)] for _ in range(n)]


def scalar_mul(a: Fraction, m: Matrix) -> Matrix:
    return [[a * value for value in row] for row in m]


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[x - y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def trace(m: Matrix) -> Fraction:
    return sum(m[i][i] for i in range(len(m)))


def antipodal_matrix() -> Matrix:
    neg = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}
    out = zeros(6)
    for i, j in neg.items():
        out[j][i] = Fraction(1, 1)
    return out


def all_ones_projector() -> Matrix:
    return [[Fraction(1, 6) for _ in range(6)] for _ in range(6)]


@dataclass(frozen=True)
class SchurWeights:
    w_a1: Fraction
    w_e: Fraction
    w_t: Fraction
    rank_a1: Fraction
    rank_e: Fraction
    rank_t: Fraction


def schur_weights() -> SchurWeights:
    identity = eye(6)
    antipodal = antipodal_matrix()
    p_a1 = all_ones_projector()
    p_even = scalar_mul(Fraction(1, 2), add(identity, antipodal))
    p_odd = scalar_mul(Fraction(1, 2), sub(identity, antipodal))
    p_e = sub(p_even, p_a1)
    p_t = p_odd
    return SchurWeights(
        w_a1=p_a1[0][0],
        w_e=p_e[0][0],
        w_t=p_t[0][0],
        rank_a1=trace(p_a1),
        rank_e=trace(p_e),
        rank_t=trace(p_t),
    )


def pow_fraction(x: Fraction, exponent: int) -> Fraction:
    if exponent >= 0:
        return x**exponent
    return Fraction(1, 1) / (x ** (-exponent))


def lift_ratio_from_exponent(w_e: Fraction, w_t: Fraction, p: int) -> Fraction:
    # q_X proportional to w_X^-p.
    return pow_fraction(w_e / w_t, -p)


def endpoint_from_lambda(lambda_et: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_t = Fraction(5, 6)
    q_e = q_t * lambda_et
    rho_e = Fraction(6, 1) * (q_e - 1)
    center_te = Fraction(-2, 1) * q_t / q_e
    return q_e, rho_e, center_te


@dataclass(frozen=True)
class Control:
    name: str
    exponent: int
    explanation: str


CONTROLS = (
    Control("channel-neutral", 0, "no dual factor"),
    Control("one-sided-dual", 1, "source or readout dualized, but not both"),
    Control("two-sided-dual", 2, "source and readout both canonical-dual"),
    Control("primal-square", -2, "ordinary projector-square scaling"),
)


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def phrase(*parts: str) -> str:
    return "".join(parts)


def main() -> int:
    print("Route-2 two-sided canonical-dual compliance conditional theorem")
    print("Status: conditional-support; not an audit verdict.")
    print("TRACE: upstream_support")

    print("\nPART 1: six-arm O_h Schur projector weights")
    weights = schur_weights()
    check(
        "projector ranks are A1=1, E=2, T=3",
        (weights.rank_a1, weights.rank_e, weights.rank_t)
        == (Fraction(1), Fraction(2), Fraction(3)),
        f"ranks={(weights.rank_a1, weights.rank_e, weights.rank_t)}",
    )
    check(
        "per-arm weights are w_A1=1/6, w_E=1/3, w_T=1/2",
        (weights.w_a1, weights.w_e, weights.w_t)
        == (Fraction(1, 6), Fraction(1, 3), Fraction(1, 2)),
        f"weights={(weights.w_a1, weights.w_e, weights.w_t)}",
    )
    kappa = weights.w_t / weights.w_e
    check("same-domain leverage kappa=w_T/w_E=3/2", kappa == Fraction(3, 2), f"kappa={kappa}")

    print("\nPART 2: two-sided canonical-dual compliance")
    lambda_dual = lift_ratio_from_exponent(weights.w_e, weights.w_t, 2)
    q_e, rho_e, center_te = endpoint_from_lambda(lambda_dual)
    check(
        "two-sided dual law gives lambda=q_E/q_T=(w_E/w_T)^-2=9/4",
        lambda_dual == Fraction(9, 4),
        f"lambda={lambda_dual}",
    )
    check(
        "with q_T=5/6, the law gives q_E=15/8 and rho_E=21/4",
        (q_e, rho_e) == (Fraction(15, 8), Fraction(21, 4)),
        f"q_E={q_e}, rho_E={rho_e}",
    )
    check(
        "with shell T/E=-2, the same law gives center T/E=-8/9",
        center_te == Fraction(-8, 9),
        f"center T/E={center_te}",
    )

    print("\nPART 3: wrong-exponent controls")
    control_results: dict[str, tuple[Fraction, Fraction, Fraction, Fraction]] = {}
    for control in CONTROLS:
        lam = lift_ratio_from_exponent(weights.w_e, weights.w_t, control.exponent)
        qe, rho, cte = endpoint_from_lambda(lam)
        control_results[control.name] = (lam, qe, rho, cte)
        print(
            f"  {control.name:>16s}: p={control.exponent:+d}, "
            f"lambda={lam}, q_E={qe}, rho_E={rho}, center T/E={cte}"
        )
    check(
        "only the two-sided-dual control lands rho_E=21/4",
        [
            name
            for name, (_, _, rho, _) in control_results.items()
            if rho == Fraction(21, 4)
        ]
        == ["two-sided-dual"],
    )
    check(
        "one-sided dual gives p=1 and misses the endpoint",
        control_results["one-sided-dual"][2] == Fraction(3, 2),
        f"rho_E={control_results['one-sided-dual'][2]}",
    )
    check(
        "ordinary projector-square scaling gives the wrong channel direction",
        control_results["primal-square"][2] == Fraction(-34, 9),
        f"rho_E={control_results['primal-square'][2]}",
    )

    print("\nPART 4: note and status firewall")
    note = note_text("QUARK_ROUTE2_DUAL_FRAME_COMPLIANCE_CONDITIONAL_SUPPORT_NOTE_2026-06-21.md")
    required_markers = (
        "**Actual current-surface status:** conditional support",
        "two-sided canonical-dual Schur compliance",
        "new source/readout premise",
        "This is not an audit verdict",
        "does not close the parent",
        "does not derive the T-side candidates",
    )
    for marker in required_markers:
        check(f"note contains marker: {marker}", marker in note)
    banned_markers = (
        ("legacy source-status certificate", "actual_current_surface_status:"),
        ("parent-closure phrase", phrase("closes ", "the parent")),
        (
            "current-surface endpoint-derivation phrase",
            phrase("derives ", "the endpoint triple", " on the current surface"),
        ),
        ("audit-ratification phrase", phrase("audit", "-ratified")),
        ("branch-local status-promotion phrase", phrase("retained ", "branch-local")),
        ("future-retention phrase", phrase("would ", "become retained")),
        ("promotion-to-retention phrase", phrase("promoted ", "to retained")),
    )
    for label, marker in banned_markers:
        check(f"note avoids overclaim marker: {label}", marker not in note)

    print("\nTOTAL: PASS=%d, FAIL=%d" % (PASS, FAIL))
    if FAIL:
        return 1
    print(
        "VERDICT: conditional-support. A two-sided canonical-dual Schur "
        "compliance premise gives p=2 and therefore rho_E=21/4 exactly, "
        "but that premise is new and remains the open source/readout theorem."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
