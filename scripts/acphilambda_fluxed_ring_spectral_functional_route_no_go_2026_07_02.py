#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[PASS] {label}")
    else:
        FAIL += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"[FAIL] {label}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


Phi = sp.symbols("Phi", real=True)
lam = sp.symbols("lambda", real=True)


def simp(expr: sp.Expr) -> sp.Expr:
    expanded = sp.expand_trig(expr.rewrite(sp.cos))
    return sp.trigsimp(sp.simplify(expanded))


def exact_zero(expr: sp.Expr) -> bool:
    return simp(expr) == 0


def cycle_shift(n: int) -> sp.Matrix:
    matrix = sp.zeros(n)
    for col in range(n):
        matrix[(col + 1) % n, col] = 1
    return matrix


def hopping(n: int) -> sp.Matrix:
    c = cycle_shift(n)
    phase = sp.exp(sp.I * Phi / n)
    return phase * c + phase ** -1 * c.T


def weighted_hopping(weights: list[int]) -> sp.Matrix:
    n = len(weights)
    matrix = sp.zeros(n)
    phase = sp.exp(sp.I * Phi / n)
    for col, weight in enumerate(weights):
        row = (col + 1) % n
        matrix[row, col] = weight * phase
        matrix[col, row] = weight * phase ** -1
    return matrix


def laplacian(n: int) -> sp.Matrix:
    return 2 * sp.eye(n) - hopping(n)


def char_coeffs(matrix: sp.Matrix) -> list[sp.Expr]:
    n = matrix.rows
    poly = sp.Poly(sp.expand((lam * sp.eye(n) - matrix).det()), lam)
    return poly.all_coeffs()


def elementary(coeffs: list[sp.Expr], k: int) -> sp.Expr:
    return simp(((-1) ** k) * coeffs[k])


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    note_path = root / "docs" / "ACPHILAMBDA_FLUXED_RING_SPECTRAL_FUNCTIONAL_ROUTE_NO_GO_2026-07-02.md"
    runner_path = root / "scripts" / "acphilambda_fluxed_ring_spectral_functional_route_no_go_2026_07_02.py"
    brannen_path = root / "docs" / "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md"
    modulus_path = root / "docs" / "KOIDE_PHASE_DELTA_IS_ALSO_AN_ADMISSION_CLEAN_MODULUS_HAS_ONLY_DEGENERATE_STATIONARY_POINTS_NARROW_NO_GO_NOTE_2026-06-04.md"
    axioms_path = root / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

    check("PART A note exists", note_path.exists())
    check("PART A runner exists", runner_path.exists())
    check("PART A Brannen source exists", brannen_path.exists())
    check("PART A modulus source exists", modulus_path.exists())
    check("PART A minimal axioms source exists", axioms_path.exists())

    note = read(note_path) if note_path.exists() else ""
    brannen = read(brannen_path) if brannen_path.exists() else ""
    modulus = read(modulus_path) if modulus_path.exists() else ""

    check("PART A Brannen quote pin: circulant form", "circulant form" in brannen)
    check("PART A Brannen quote pin: (a, |b|, delta)", "(a, |b|, delta)" in brannen)
    check("PART A modulus quote pin: stationary only at delta=k60", "stationary **only** at `δ = k·60°`" in modulus)
    check("PART A modulus quote pin: candidates degenerate", "its stationary candidates are degenerate" in modulus)

    l_coeffs: dict[int, list[sp.Expr]] = {}
    for n in range(3, 7):
        coeffs = char_coeffs(laplacian(n))
        l_coeffs[n] = coeffs
        for idx, coeff in enumerate(coeffs[:-1]):
            power = n - idx
            check(f"PART B L N={n} lambda^{power} coefficient is flux-blind", exact_zero(sp.diff(coeff, Phi)), simp(sp.diff(coeff, Phi)))
        expected_constant = ((-1) ** n) * (2 - 2 * sp.cos(Phi))
        check(f"PART B L N={n} constant term is localized flux term", exact_zero(coeffs[-1] - expected_constant), simp(coeffs[-1] - expected_constant))

    h3 = hopping(3)
    h3_coeffs = char_coeffs(h3)
    for idx, coeff in enumerate(h3_coeffs[:-1]):
        power = 3 - idx
        check(f"PART B H N=3 lambda^{power} coefficient is flux-blind", exact_zero(sp.diff(coeff, Phi)), simp(sp.diff(coeff, Phi)))
    check("PART B H N=3 det H equals 2 cos Phi", exact_zero(h3.det() - 2 * sp.cos(Phi)), simp(h3.det() - 2 * sp.cos(Phi)))
    check("PART B H N=3 e1 equals 0", exact_zero(elementary(h3_coeffs, 1)), elementary(h3_coeffs, 1))
    check("PART B H N=3 e2 equals -3", exact_zero(elementary(h3_coeffs, 2) + 3), elementary(h3_coeffs, 2))

    l3 = laplacian(3)
    p1 = simp(sp.trace(l3))
    p2 = simp(sp.trace(l3 * l3))
    e1_l3 = p1
    e2_l3 = simp((p1 ** 2 - p2) / 2)
    det_l3 = simp(l3.det())
    check("PART B L N=3 power-sum e1 equals 6", exact_zero(e1_l3 - 6), e1_l3)
    check("PART B L N=3 power-sum e2 equals 9", exact_zero(e2_l3 - 9), e2_l3)
    check("PART B L N=3 det L equals 2 - 2 cos Phi", exact_zero(det_l3 - (2 - 2 * sp.cos(Phi))), det_l3)

    defect_l3 = 2 * sp.eye(3) - weighted_hopping([2, 1, 1])
    defect_coeffs = char_coeffs(defect_l3)
    check(
        "PART B robustness: defected ring keeps non-constant coefficients flux-blind",
        all(exact_zero(sp.diff(coeff, Phi)) for coeff in defect_coeffs[:-1]),
    )
    check(
        "PART B robustness: defected constant term is 2w^2 + 2w cos Phi - 4 at w=2",
        exact_zero(defect_coeffs[-1] - (2 * 4 + 2 * 2 * sp.cos(Phi) - 4)),
        simp(defect_coeffs[-1]),
    )
    check(
        "PART B robustness: defected constant term differs from the unit-modulus value",
        not exact_zero(defect_coeffs[-1] - (-1) ** 3 * (2 - 2 * sp.cos(Phi))),
    )
    check("PART B discriminator: N=3 lambda^1 coefficient is not flux-dependent", exact_zero(sp.diff(l_coeffs[3][-2], Phi)), simp(sp.diff(l_coeffs[3][-2], Phi)))

    # true structural rejector: a SECOND independent cycle breaks localization.
    # 4-ring 0-1-2-3 with a real chord 0-2; Peierls phase on ring edges only.
    chord_a = sp.zeros(4)
    ring_phase = sp.exp(sp.I * Phi / 4)
    for a_v, b_v in ((0, 1), (1, 2), (2, 3), (3, 0)):
        chord_a[b_v, a_v] += ring_phase
        chord_a[a_v, b_v] += sp.conjugate(ring_phase)
    chord_a[2, 0] += 1
    chord_a[0, 2] += 1
    chord_l = sp.diag(3, 2, 3, 2) - chord_a
    chord_coeffs = char_coeffs(chord_l)
    check(
        "PART B rejector: chorded 4-ring puts flux into the lambda^1 coefficient",
        not exact_zero(sp.diff(chord_coeffs[-2], Phi)),
        simp(sp.diff(chord_coeffs[-2], Phi)),
    )
    check(
        "PART B rejector: chorded 4-ring keeps lambda^2 and higher flux-blind",
        all(exact_zero(sp.diff(coeff, Phi)) for coeff in chord_coeffs[:-2]),
    )

    e2_over_e3 = simp(elementary(l_coeffs[3], 2) / elementary(l_coeffs[3], 3))
    trace_inverse_closed = 9 / (2 - 2 * sp.cos(Phi))
    check("PART C Tr L^{-1} at N=3 equals e2/e3 closed form", exact_zero(e2_over_e3 - trace_inverse_closed), e2_over_e3)

    samples = [sp.Rational(1, 2), sp.Rational(2, 3), sp.Rational(3, 2)]
    det_derivative = simp(sp.diff(2 - 2 * sp.cos(Phi), Phi))
    log_derivative = simp(sp.diff(sp.log(2 - 2 * sp.cos(Phi)), Phi))
    expected_log_derivative = sp.sin(Phi) / (1 - sp.cos(Phi))
    trace_inverse_derivative = simp(sp.diff(trace_inverse_closed, Phi))

    for value in samples:
        check(f"PART C det L derivative positive at Phi={value}", simp(det_derivative.subs(Phi, value)).is_positive)
    check("PART C log-det derivative equals sin Phi over 1-cos Phi", exact_zero(log_derivative - expected_log_derivative), log_derivative)
    for value in samples:
        check(f"PART C log-det derivative positive at Phi={value}", simp(expected_log_derivative.subs(Phi, value)).is_positive)
    for value in samples:
        check(f"PART C Tr L inverse derivative negative at Phi={value}", simp(trace_inverse_derivative.subs(Phi, value)).is_negative)

    x = sp.symbols("x")
    g = sp.Function("g")
    functional_derivative = sp.diff(g(sp.cos(Phi)), Phi)
    expected_functional_derivative = -sp.sin(Phi) * sp.Subs(sp.Derivative(g(x), x), x, sp.cos(Phi))
    check("PART C general spectral functional derivative factors through sin Phi", sp.simplify(functional_derivative - expected_functional_derivative) == 0)
    check("PART C stationarity endpoint Phi=0", sp.sin(0) == 0)
    check("PART C stationarity endpoint Phi=pi", sp.sin(sp.pi) == 0)

    tuned_derivative_at_target = simp(2 * (sp.cos(sp.Rational(2, 3)) - sp.cos(sp.Rational(2, 3))))
    wrong_value_derivative = simp(2 * (sp.cos(sp.Rational(1, 2)) - sp.cos(sp.Rational(2, 3))))
    check("PART C tuned selector demonstrates the circularity: the target appears in the functional", tuned_derivative_at_target == 0)
    check("PART C wrong-value rejector: tuned selector is not stationary at Phi=1/2", wrong_value_derivative.equals(0) is False, wrong_value_derivative)

    for n in range(3, 7):
        coeffs = l_coeffs[n]
        for k in range(1, n):
            e_k = elementary(coeffs, k)
            check(f"PART D L N={n} e_{k} is flux-blind", exact_zero(sp.diff(e_k, Phi)), simp(sp.diff(e_k, Phi)))
        check(f"PART D L N={n} e_{{N-1}} equals N^2", exact_zero(elementary(coeffs, n - 1) - n ** 2), elementary(coeffs, n - 1))

    c3 = cycle_shift(3)
    l0 = 2 * sp.eye(3) - c3 - c3.T
    for row in range(3):
        for col in range(3):
            cofactor = ((-1) ** (row + col)) * l0.minor_submatrix(row, col).det()
            check(f"PART D matrix-tree N=3 cofactor ({row},{col}) equals 3", cofactor == 3, cofactor)

    phi_target = 3 * sp.Rational(2, 9)
    check("PART E target arithmetic 3*(2/9)=2/3", phi_target == sp.Rational(2, 3), phi_target)
    check("PART E target lies above 0", phi_target > 0)
    check("PART E target lies below pi", phi_target < sp.pi)
    check("PART E cos target is not +1", sp.cos(phi_target).equals(1) is False)
    check("PART E cos target is not -1", sp.cos(phi_target).equals(-1) is False)
    check("PART E on-locus endpoints do not contain target", phi_target not in {sp.Integer(0), sp.pi})

    required_pins = [
        "the flux enters the fluxed-ring characteristic polynomial only through the constant term, as `2 cos Phi`",
        "selecting the off-locus member through a spectral functional requires tuning the outer function to the target",
        "W_cycle_holonomy_value",
        "not a terminal no-go",
        "next path",
    ]
    for pin in required_pins:
        check(f"PART F note required pin: {pin}", pin in note)

    for n in range(1, 9):
        check(f"PART F note has N{n} header", f"### N{n}" in note)

    forbidden = [
        "only " + "route",
        "last " + "route",
        "exh" + "austed",
        "closes " + "the route",
        "PD" + "G",
        "new " + "wall",
    ]
    note_flat = flat(note)
    for fragment in forbidden:
        check(f"PART F forbidden fragment absent: {fragment}", fragment not in note_flat)

    allowed_walls = {"W_cycle_holonomy_value", "W_defect_identity_unit", "W_defect_readout_selection"}
    found_walls = set(re.findall(r"\bW_[A-Za-z0-9_]+\b", note))
    check("PART F W identifier whitelist", found_walls <= allowed_walls, sorted(found_walls - allowed_walls))

    link_targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", note)
    md_link_basenames = sorted(Path(target.split("#", 1)[0]).name for target in link_targets if target.split("#", 1)[0].endswith(".md"))
    expected_md_links = sorted([brannen_path.name, modulus_path.name])
    check("PART F markdown .md link inventory has exactly the two origin docs", md_link_basenames == expected_md_links, md_link_basenames)
    check("PART F in-flight basenames are not markdown link targets", all("ACPHILAMBDA_" not in name for name in md_link_basenames), md_link_basenames)
    check("PART F paired runner is linked", any(Path(target.split("#", 1)[0]).name == runner_path.name for target in link_targets), link_targets)
    check("PART F status-authority header is standard", "**Status authority:** independent audit lane only." in note)

    leakage = [
        "required for " + "the record",
        "this " + "spec",
        "PRES" + "ERVE",
    ]
    for fragment in leakage:
        check(f"PART F spec-leakage detector absent: {fragment}", fragment not in note)

    check("PART F note does not claim AC_phi_lambda retirement", "claim `AC_phi_lambda` retirement" in note and "does not" in note)

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 and PASS >= 60 else 1


if __name__ == "__main__":
    raise SystemExit(main())
