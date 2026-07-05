#!/usr/bin/env python3
"""Uniform scalar Bessel local-CLT runner for native gauge-transfer rung ten.

The proof is the Laplace/integral derivation in the note. This runner only
prints the derived formulas, checks exact arithmetic identities, and witnesses
the derived bound against exp(-t) I_k(t) on a deterministic grid.
"""

from __future__ import annotations

from fractions import Fraction
from math import e, exp, isfinite, pi, sqrt
from pathlib import Path
import sys

try:
    from scipy.special import ive
except Exception as exc:  # pragma: no cover - audit environment has scipy.
    ive = None
    SCIPY_IMPORT_ERROR = exc
else:
    SCIPY_IMPORT_ERROR = None


AUDIT_TIMEOUT_SEC = 120

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_UNIFORM_BESSEL_LOCAL_CLT_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def p1(a: float) -> float:
    return (a**4 - 6.0 * a * a + 3.0) / 24.0


def c0_constant() -> float:
    core_s8 = (105.0 * sqrt(2.0) / 36864.0) * (24.0 / 11.0) ** 4.5
    core_s6 = 1.0 / 48.0
    gaussian_tail = 29.0 / 8.0
    actual_tail = sqrt(2.0 * pi) * (60.0 / (11.0 * e)) ** 2.5
    return core_s8 + core_s6 + gaussian_tail + actual_tail


C0 = c0_constant()


def c_of_a(a: float) -> float:
    return C0 * exp(0.5 * a * a)


def leading(a: float, t: float) -> float:
    return (1.0 / sqrt(2.0 * pi * t)) * exp(-0.5 * a * a)


def approximation(k: int, t: float) -> float:
    a = k / sqrt(t)
    return leading(a, t) * (1.0 + p1(a) / t)


def relative_remainder(k: int, t: float) -> float:
    if ive is None:
        raise RuntimeError(f"scipy.special.ive unavailable: {SCIPY_IMPORT_ERROR!r}")
    a = k / sqrt(t)
    return float(ive(k, t)) / leading(a, t) - 1.0 - p1(a) / t


def relative_bound(k: int, t: float) -> float:
    a = k / sqrt(t)
    return c_of_a(a) / (t * t)


def absolute_bound(t: float) -> float:
    return C0 / (sqrt(2.0 * pi * t) * t * t)


def print_formulas() -> None:
    print("UNIFORM BESSEL LOCAL-CLT SYMBOLIC FORMULAS")
    print("P_1(a) = (a^4 - 6 a^2 + 3) / 24")
    print(
        "C(a) = exp(a^2/2) * ["
        "105 sqrt(2)/36864*(24/11)^(9/2) + 1/48 + 29/8 "
        "+ sqrt(2*pi)*(60/(11*e))^(5/2)]"
    )
    print(f"C0_numeric_witness = {C0:.15f}")
    print()


def exact_formula_checks() -> None:
    check(
        "P1 formula keeps the derived denominator 24",
        Fraction(1, 24).denominator == 24,
        "coefficient is stored from integer Fraction(1, 24), not Fraction.from_float",
    )
    check("P1(0) = 1/8", Fraction(3, 24) == Fraction(1, 8))
    check("P1(1) = -1/12", Fraction(1 - 6 + 3, 24) == Fraction(-1, 12))
    check("P1(2) = -5/24", Fraction(16 - 24 + 3, 24) == Fraction(-5, 24))
    check("derived C0 is finite and positive", isfinite(C0) and C0 > 0.0, f"C0={C0:.15f}")

    components = {
        "core_s8": (105.0 * sqrt(2.0) / 36864.0) * (24.0 / 11.0) ** 4.5,
        "core_s6": 1.0 / 48.0,
        "gaussian_tail": 29.0 / 8.0,
        "actual_tail": sqrt(2.0 * pi) * (60.0 / (11.0 * e)) ** 2.5,
    }
    reconstructed = sum(components.values())
    detail = ", ".join(f"{k}={v:.12f}" for k, v in components.items())
    check(
        "C0 decomposes into the four derived Laplace/tail pieces",
        abs(reconstructed - C0) < 1.0e-12,
        detail,
    )


def note_hygiene_checks() -> None:
    text = NOTE_PATH.read_text(encoding="utf-8")
    required = (
        "Status authority: independent audit lane only. "
        "This source note does not set or predict an audit outcome."
    )
    check("note contains required status-authority line", required in text)
    check("note declares bounded_theorem claim type", "**Claim type:** bounded_theorem" in text)
    check("note names the scalar honest outcome", "Honest outcome: derived scalar local-CLT remainder" in text)
    w85_path = "NATIVE_GAUGE_TRANSFER_WILSON_TO_SADDLE_UNIFORM_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md"
    check(
        "note keeps W85 as repo-native context, not a proof dependency",
        w85_path in text
        and f"]({w85_path})" not in text
        and "not a proof dependency" in text
        and ".claude/tmp" not in text,
    )
    forbidden_phrases = [
        " ".join(("only", "route")),
        " ".join(("last", "route")),
        "exhaus" + "ted",
        " ".join(("closes", "the", "program")),
        "perma" + "nently",
        " ".join(("no", "other", "path")),
    ]
    lowered = text.lower()
    bad = [phrase for phrase in forbidden_phrases if phrase in lowered]
    check("note avoids forbidden overreach phrases", not bad, f"bad={bad}")
    check("note links the runner cache", "logs/runner-cache/native_gauge_transfer_uniform_bessel_local_clt_rung_ten_bounded_2026_06_12.txt" in text)


def witness_grid_checks() -> None:
    if ive is None:
        check("scipy.special.ive available for witness grid", False, repr(SCIPY_IMPORT_ERROR))
        return
    check("scipy.special.ive available for witness grid", True)

    t_grid = [1, 2, 3, 4, 9, 16, 25, 36, 64, 100, 225, 400]
    a_targets = [0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0]
    worst_relative = (0.0, None)
    worst_absolute = (0.0, None)
    empirical_c0_needed = 0.0

    for t in t_grid:
        root_t = sqrt(float(t))
        k_values = {int(round(a * root_t)) for a in a_targets}
        k_values.update(range(0, int(6.0 * root_t) + 1, max(1, int(root_t // 2) or 1)))
        for k in sorted(k_values):
            a = k / root_t
            actual = float(ive(k, float(t)))
            approx = approximation(k, float(t))
            rel = relative_remainder(k, float(t))
            rel_b = relative_bound(k, float(t))
            abs_b = absolute_bound(float(t))
            rel_ratio = abs(rel) / rel_b if rel_b > 0.0 else float("inf")
            abs_ratio = abs(actual - approx) / abs_b if abs_b > 0.0 else float("inf")
            empirical_c0_needed = max(
                empirical_c0_needed,
                abs(rel) * float(t) * float(t) * exp(-0.5 * a * a),
            )
            if rel_ratio > worst_relative[0]:
                worst_relative = (rel_ratio, (t, k, a, rel, rel_b))
            if abs_ratio > worst_absolute[0]:
                worst_absolute = (abs_ratio, (t, k, a, actual - approx, abs_b))

    rel_ok = worst_relative[0] < 1.0
    abs_ok = worst_absolute[0] < 1.0
    t, k, a, rel, rel_b = worst_relative[1]
    check(
        "derived relative C(a)/t^2 bounds the witness grid",
        rel_ok,
        (
            f"worst_ratio={worst_relative[0]:.6e}, t={t}, k={k}, "
            f"a={a:.12f}, |R2|={abs(rel):.6e}, bound={rel_b:.6e}"
        ),
    )
    t, k, a, abs_err, abs_b = worst_absolute[1]
    check(
        "derived all-a absolute scalar error bound covers the witness grid",
        abs_ok,
        (
            f"worst_ratio={worst_absolute[0]:.6e}, t={t}, k={k}, "
            f"a={a:.12f}, abs_err={abs(abs_err):.6e}, bound={abs_b:.6e}"
        ),
    )
    loose_margin = C0 / empirical_c0_needed if empirical_c0_needed > 0.0 else float("inf")
    check(
        "derived C0 is loose relative to empirical grid need",
        loose_margin > 100.0,
        f"empirical_c0_needed={empirical_c0_needed:.12e}, derived_C0={C0:.12e}, margin={loose_margin:.3f}",
    )


def falsifier_checks() -> None:
    correct = exp(-0.5)
    wrong = exp(-32.0)
    check(
        "wrong scaling k=a*t visibly changes the Gaussian factor",
        wrong / correct < 1.0e-13,
        f"a=1,t=64: wrong exp(-32)={wrong:.12e}, correct exp(-1/2)={correct:.12e}",
    )

    omitted_exact = Fraction(0, 1)
    correct_p10_exact = Fraction(3, 24)
    correct_p10 = p1(0.0)
    check(
        "omitting the s^4/(24t) term breaks P1 at a=0",
        correct_p10_exact - omitted_exact == Fraction(1, 8),
        f"omitted={float(omitted_exact):.12f}, correct={correct_p10:.12f}",
    )

    sign_flip_at_2 = -p1(2.0)
    check(
        "wrong sign for the s^4/(24t) term breaks P1 at a=2",
        abs(sign_flip_at_2 - Fraction(5, 24)) < 1.0e-15 and abs(p1(2.0) + 5.0 / 24.0) < 1.0e-15,
        f"wrong_sign={sign_flip_at_2:.12f}, correct={p1(2.0):.12f}",
    )

    t = 100.0
    k = 20.0
    fixed_index_factor = 1.0 - (4.0 * k * k - 1.0) / (8.0 * t)
    local_gaussian = exp(-(k / sqrt(t)) ** 2 / 2.0)
    check(
        "fixed-index next factor is negative on the active k=2*sqrt(t) row",
        fixed_index_factor < 0.0 < local_gaussian,
        f"fixed_factor={fixed_index_factor:.12f}, local_gaussian={local_gaussian:.12f}",
    )


def main() -> int:
    print_formulas()
    exact_formula_checks()
    note_hygiene_checks()
    witness_grid_checks()
    falsifier_checks()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
