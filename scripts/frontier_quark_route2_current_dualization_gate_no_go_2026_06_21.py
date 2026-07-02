#!/usr/bin/env python3
"""Current-bank dualization gate for the Route-2 p=2 endpoint.

This runner tests whether the current Route-2 source/readout authority bank
already supplies the canonical-dual or inverse-square source/readout theorem
needed to turn the Schur weights w_E=1/3, w_T=1/2 into the p=2 lift.

Status:
  no-go for the current-bank canonical-dual shortcut.

Safe claim:
  The current authority bank gives exact carrier/readout algebra, exact
  conditional time coupling, source-domain and positivity no-gos, and a sharp
  E-center source/readout target. It does not supply source/readout
  adjointness, a canonical-dual frame, a Moore-Penrose/Riesz law, or two
  inverse Schur-weight factors. One-sided dualization would give p=1, not the
  target p=2. A future inverse-square source/readout theorem remains open.
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

AUTHORITY_BANK = (
    "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
    "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
    "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md",
    "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
    "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
    "QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md",
    "QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md",
    "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md",
    "ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md",
)

ABSENT_DUALIZATION_MARKERS = (
    "canonical dual",
    "canonical-dual",
    "dual frame",
    "dual-frame",
    "Moore-Penrose",
    "pseudoinverse",
    "Riesz",
    "adjoint readout",
    "source/readout adjoint",
    "two-sided dual",
    "two-sided canonical",
    "inverse-square dualization",
)

REQUIRED_SOURCE_MARKERS = {
    "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md": (
        "class-A definition only",
        "does not derive",
        "physical tensor primitive",
    ),
    "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md": (
        "any admissible bright-preserving linear readout",
        "irreducible missing map entry",
        "beta_E / alpha_E = 21/4",
    ),
    "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md": (
        "Given any admissible readout map `P_R`",
        "selects one unique `P_R`",
    ),
    "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md": (
        "structurally localized in the spatial prefactor",
        "time-channel structure is universal",
    ),
    "QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md": (
        "requested source bank does not contain an exact E-channel row",
        "typed E-channel source/readout theorem",
    ),
    "QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md": (
        "does not derive that row",
        "(alpha_E, alpha_T, beta_T) = (1, -2, 2)",
    ),
    "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md": (
        "There is no current typed edge",
        "extra source/readout rule",
    ),
    "ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md": (
        "fix the readout **norm**",
        "readout's **direction**",
    ),
}


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def eye(n: int) -> Matrix:
    return [[Fraction(int(i == j), 1) for j in range(n)] for i in range(n)]


def zeros(n: int) -> Matrix:
    return [[Fraction(0, 1) for _ in range(n)] for _ in range(n)]


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[x - y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def scalar_mul(k: Fraction, m: Matrix) -> Matrix:
    return [[k * value for value in row] for row in m]


def trace(m: Matrix) -> Fraction:
    return sum(m[i][i] for i in range(len(m)))


def antipodal_matrix() -> Matrix:
    antipodal = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}
    out = zeros(6)
    for i, j in antipodal.items():
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


def lift_ratio(w_e: Fraction, w_t: Fraction, dual_factor_count: int) -> Fraction:
    # q_X proportional to w_X^(-dual_factor_count).
    return pow_fraction(w_e / w_t, -dual_factor_count)


def endpoint_from_lambda(lambda_et: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_t = Fraction(5, 6)
    q_e = q_t * lambda_et
    rho_e = 6 * (q_e - 1)
    center_te = Fraction(-2) * q_t / q_e
    return q_e, rho_e, center_te


def lower_bank_text() -> str:
    return "\n".join(note_text(name) for name in AUTHORITY_BANK).lower()


def main() -> int:
    print("Route-2 current-bank canonical-dualization gate")
    print("Status: no-go for current-bank canonical-dual shortcut; not an audit verdict.")
    print("TRACE: negative_route_pruning")

    print("\nPART 1: exact Schur weights and dual-factor arithmetic")
    weights = schur_weights()
    check(
        "six-arm projector ranks are A1=1, E=2, T=3",
        (weights.rank_a1, weights.rank_e, weights.rank_t)
        == (Fraction(1), Fraction(2), Fraction(3)),
        f"ranks={(weights.rank_a1, weights.rank_e, weights.rank_t)}",
    )
    check(
        "per-arm Schur weights are w_A1=1/6, w_E=1/3, w_T=1/2",
        (weights.w_a1, weights.w_e, weights.w_t)
        == (Fraction(1, 6), Fraction(1, 3), Fraction(1, 2)),
        f"weights={(weights.w_a1, weights.w_e, weights.w_t)}",
    )
    check(
        "same-domain leverage is w_T/w_E=3/2",
        weights.w_t / weights.w_e == Fraction(3, 2),
        f"w_T/w_E={weights.w_t / weights.w_e}",
    )

    expected = {
        "zero-dual": (0, Fraction(1), Fraction(5, 6), Fraction(-1), Fraction(-2)),
        "source-only-dual": (1, Fraction(3, 2), Fraction(5, 4), Fraction(3, 2), Fraction(-4, 3)),
        "readout-only-dual": (1, Fraction(3, 2), Fraction(5, 4), Fraction(3, 2), Fraction(-4, 3)),
        "two-sided-dual": (2, Fraction(9, 4), Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)),
    }
    for label, (dual_count, lam_expected, q_expected, rho_expected, center_expected) in expected.items():
        lam = lift_ratio(weights.w_e, weights.w_t, dual_count)
        q_e, rho_e, center_te = endpoint_from_lambda(lam)
        print(
            f"  {label:>18s}: dual_factors={dual_count}, "
            f"lambda={lam}, q_E={q_e}, rho_E={rho_e}, center T/E={center_te}"
        )
        check(
            f"{label} exact endpoint arithmetic matches expected values",
            (lam, q_e, rho_e, center_te)
            == (lam_expected, q_expected, rho_expected, center_expected),
        )

    print("\nPART 2: current authority-bank marker checks")
    for name in AUTHORITY_BANK:
        check(f"authority file exists: {name}", (DOCS / name).is_file())
    for name, markers in REQUIRED_SOURCE_MARKERS.items():
        text = note_text(name)
        for marker in markers:
            check(f"{name} contains marker: {marker}", marker in text)

    print("\nPART 3: absence of current-bank dualization semantics")
    bank = lower_bank_text()
    for marker in ABSENT_DUALIZATION_MARKERS:
        check(
            f"authority bank does not supply marker: {marker}",
            marker.lower() not in bank,
        )
    check(
        "current bank has exact conditional P_R algebra but no canonical-dual selector",
        "given any admissible readout map `p_r`" in bank
        and "selects one unique `p_r`" in bank
        and "canonical-dual" not in bank,
    )
    check(
        "current bank names source/readout theorem target rather than deriving it",
        "typed e-channel source/readout theorem" in bank
        and "requested source bank does not contain an exact e-channel row" in bank,
    )

    print("\nPART 4: note and status firewall")
    note = note_text("QUARK_ROUTE2_CURRENT_DUALIZATION_GATE_NO_GO_NOTE_2026-06-21.md")
    required_note_markers = (
        "**Actual current-surface status:** no-go for current-bank canonical-dual dualization shortcut",
        "This is not an audit verdict",
        "does not resolve the parent",
        "does not rule out a future inverse-square dualization theorem",
        "one-sided source-only or readout-only dualization gives `p=1`",
        "the current authority bank does not supply a source/readout adjointness or canonical-dual law",
    )
    for marker in required_note_markers:
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
        ("no-future-theorem phrase", phrase("no future ", "primitive can exist")),
    )
    for label, marker in banned_markers:
        check(f"note avoids overclaim marker: {label}", marker not in note)

    print("\nTOTAL: PASS=%d, FAIL=%d" % (PASS, FAIL))
    if FAIL:
        return 1
    print(
        "VERDICT: no-go for the current-bank canonical-dual shortcut. "
        "The current Route-2 authority bank does not already supply the "
        "two-sided inverse-Schur source/readout law; deriving that law remains "
        "the next science target."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
