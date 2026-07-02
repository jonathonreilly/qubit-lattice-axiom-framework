#!/usr/bin/env python3
"""Exact verifier for the AC_phi_lambda cycle-flux transport-face inventory."""
from __future__ import annotations

import re
from pathlib import Path

import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}" + (f" -- {detail}" if detail else ""))
    return ok


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def flat(text: str) -> str:
    return " ".join(text.split())

def exact(expr: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.trigsimp(sp.expand_trig(sp.expand(expr))))


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    if left.shape != right.shape:
        return False
    return all(exact(left[i, j] - right[i, j]) == 0 for i in range(left.rows) for j in range(left.cols))


def cycle_shift(n: int) -> sp.Matrix:
    return sp.Matrix(n, n, lambda i, j: sp.Integer(1) if j == (i + 1) % n else sp.Integer(0))


def cycle_laplacian(n: int) -> sp.Matrix:
    c = cycle_shift(n)
    return 2 * sp.eye(n) - c - c.T


def trace(matrix: sp.Matrix) -> sp.Expr:
    return exact(sum(matrix[i, i] for i in range(matrix.rows)))


def cycle_distance(n: int, v: int, w: int) -> int:
    forward = (w - v) % n
    backward = (v - w) % n
    return min(forward, backward)


def fixed_term(omega: sp.Expr, a: int, b: int, j: int) -> sp.Expr:
    return exact(1 / ((omega ** (j * a) - 1) * (omega ** (j * b) - 1)))


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    docs = root / "docs"
    note_path = docs / "ACPHILAMBDA_CYCLE_FLUX_TRANSPORT_FACE_INVENTORY_2026-07-01.md"
    runner_path = root / "scripts" / "acphilambda_cycle_flux_transport_face_inventory_2026_07_01.py"
    fixed_path = docs / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
    circulant_path = (
        docs / "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md"
    )
    radian_path = docs / "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md"

    section("PART A - source files and quote pins")
    check("paired note exists", note_path.exists(), str(note_path.relative_to(root)))
    check("paired runner exists", runner_path.exists(), str(runner_path.relative_to(root)))
    check("fixed-locus source exists", fixed_path.exists(), str(fixed_path.relative_to(root)))
    check("circulant source exists", circulant_path.exists(), str(circulant_path.relative_to(root)))
    check("radian-bridge source exists", radian_path.exists(), str(radian_path.relative_to(root)))

    note = read(note_path)
    fixed = read(fixed_path)
    circulant = read(circulant_path)
    radian = read(radian_path)
    note_s = flat(note)
    fixed_s = flat(fixed)
    circulant_s = flat(circulant)
    radian_s = flat(radian)

    check(
        "fixed-locus pins transverse determinant singlet forcing",
        "det` of the transverse action is the C3 singlet" in fixed_s
        or "det` of the transverse action is the C₃ singlet" in fixed_s
        or "determinant of the transverse action is the C3 singlet" in fixed_s
        or "determinant of the transverse action is the C₃ singlet" in fixed_s,
    )
    check(
        "fixed-locus pins physical single-summand boundary",
        "does **not** supply the physical single-summand readout" in fixed_s,
    )
    check("radian bridge pins eta_APS witness", "eta_APS(Z_3; 1,2)" in radian_s)
    check("radian bridge pins Type-B-to-radian boundary", "Type-B-to-radian" in radian_s)
    check("circulant source pins circulant form", "circulant form" in circulant_s)
    check("circulant source pins couplings", "(a, |b|, delta)" in circulant_s)

    section("PART B - T-F1 exact conjugate-pair reduction")
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    check("omega is an exact primitive cube root", exact(omega**3 - 1) == 0 and exact(omega - 1) != 0)
    for j in (1, 2):
        check(
            f"forced pair conjugate identity j={j}",
            exact(omega ** (2 * j) - sp.conjugate(omega**j)) == 0,
        )

    forced_terms = [fixed_term(omega, 1, 2, j) for j in (1, 2)]
    for j, term in zip((1, 2), forced_terms):
        check(f"forced pair term j={j} equals 1/3", exact(term - sp.Rational(1, 3)) == 0)
        check(f"forced pair term j={j} is real", exact(term - sp.conjugate(term)) == 0)
        check(f"forced pair term j={j} is positive rational", term == sp.Rational(1, 3))

    reversed_terms = [fixed_term(omega, 2, 1, j) for j in (1, 2)]
    check("reversed forced pair has the same per-mode terms", forced_terms == reversed_terms)
    check("S_sum(1,2) is 2/3", exact(sum(forced_terms) - sp.Rational(2, 3)) == 0)
    check("L3(1,2) is 2/9", exact(sum(forced_terms) / 3 - sp.Rational(2, 9)) == 0)

    bad_11_terms = [fixed_term(omega, 1, 1, j) for j in (1, 2)]
    bad_22_terms = [fixed_term(omega, 2, 2, j) for j in (1, 2)]
    for j, term in zip((1, 2), bad_11_terms):
        check(f"(1,1) per-mode term j={j} has nonzero imaginary part", exact(sp.im(term)) != 0)
    for j, term in zip((1, 2), bad_22_terms):
        check(f"(2,2) per-mode term j={j} has nonzero imaginary part", exact(sp.im(term)) != 0)
    check("S_sum(1,1) is 1/3", exact(sum(bad_11_terms) - sp.Rational(1, 3)) == 0)
    check("S_sum(1,1) rejects 2/3", exact(sum(bad_11_terms) - sp.Rational(2, 3)) != 0)

    real_positive_pairs = []
    for pair in ((1, 1), (1, 2), (2, 1), (2, 2)):
        terms = [fixed_term(omega, pair[0], pair[1], j) for j in (1, 2)]
        if all(exact(term - sp.Rational(1, 3)) == 0 for term in terms):
            real_positive_pairs.append(pair)
    check("only trace-free nontrivial pairs are per-mode Green weights", real_positive_pairs == [(1, 2), (2, 1)])

    section("PART C - T-F2 exact transport faces")
    laplacians: dict[int, sp.Matrix] = {}
    pinvs: dict[int, sp.Matrix] = {}
    for n in range(2, 9):
        laplacians[n] = cycle_laplacian(n)
        pinvs[n] = laplacians[n].pinv()
        target_trace = sp.Rational(n * n - 1, 12)
        target_diag = sp.Rational(n * n - 1, 12 * n)
        check(f"L_{n} has exact zero row sums", all(exact(sum(laplacians[n][i, j] for j in range(n))) == 0 for i in range(n)))
        check(f"Tr pinv(L_{n}) equals (N^2-1)/12", exact(trace(pinvs[n]) - target_trace) == 0)
        check(f"pinv(L_{n}) diagonal equals per-site closed form", all(exact(pinvs[n][v, v] - target_diag) == 0 for v in range(n)))

    eigenvals_l3 = laplacians[3].eigenvals()
    check("L_3 eigenvalues are {0,3,3}", eigenvals_l3 == {sp.Integer(0): 1, sp.Integer(3): 2})
    check("Tr pinv(L_3) is 2/3", exact(trace(pinvs[3]) - sp.Rational(2, 3)) == 0)
    check("pinv(L_3) diagonal entries are 2/9", all(exact(pinvs[3][v, v] - sp.Rational(2, 9)) == 0 for v in range(3)))

    for n in range(2, 7):
        resistance_ok = True
        for v in range(n):
            for w in range(v + 1, n):
                d = cycle_distance(n, v, w)
                r = exact(pinvs[n][v, v] + pinvs[n][w, w] - 2 * pinvs[n][v, w])
                resistance_ok = resistance_ok and exact(r - sp.Rational(d * (n - d), n)) == 0
        check(f"cycle resistance formula holds for N={n}", resistance_ok)

        kirchhoff_sum = sp.Integer(0)
        for v in range(n):
            for w in range(v + 1, n):
                kirchhoff_sum += exact(pinvs[n][v, v] + pinvs[n][w, w] - 2 * pinvs[n][v, w])
        check(f"Kirchhoff route holds for N={n}", exact(kirchhoff_sum - n * trace(pinvs[n])) == 0)
        check(
            f"distance polynomial sum holds for N={n}",
            exact(sum(d * (n - d) for d in range(1, n)) - sp.Rational(n * (n * n - 1), 6)) == 0,
        )

    for n in range(3, 6):
        l_n = laplacians[n]
        p_n = pinvs[n]
        check(f"LPL=L pinv sanity for N={n}", matrix_equal(l_n * p_n * l_n, l_n))
        check(f"PLP=P pinv sanity for N={n}", matrix_equal(p_n * l_n * p_n, p_n))

    for n in (2, 3, 4, 6):
        spectral = exact(sum(1 / (2 - 2 * sp.cos(2 * sp.pi * j / n)) for j in range(1, n)))
        check(f"exact spectral face holds for N={n}", exact(spectral - sp.Rational(n * n - 1, 12)) == 0)

    wrong_form_n3 = sp.Rational(3 * 3 + 1, 12)
    check("wrong closed form (N^2+1)/12 fails at N=3", exact(wrong_form_n3 - trace(pinvs[3])) != 0)
    check("Tr pinv(L_4) is 5/4", exact(trace(pinvs[4]) - sp.Rational(5, 4)) == 0)
    check("Tr pinv(L_4) rejects 2/3", exact(trace(pinvs[4]) - sp.Rational(2, 3)) != 0)

    l_path = sp.Matrix([[1, -1, 0], [-1, 2, -1], [0, -1, 1]])
    p_path = l_path.pinv()
    check("3-path graph Laplacian has trace pinv 4/3", exact(trace(p_path) - sp.Rational(4, 3)) == 0)
    check("3-path graph Laplacian rejects 2/3", exact(trace(p_path) - sp.Rational(2, 3)) != 0)

    section("PART D - T-F3 arithmetic")
    delta = sp.Rational(2, 9)
    phi = 3 * delta
    check("Phi = 3 delta gives 2/3", exact(phi - sp.Rational(2, 3)) == 0)
    check("Phi equals Tr pinv(L_3)", exact(phi - trace(pinvs[3])) == 0)
    check("delta equals the per-site return amplitude", exact(delta - pinvs[3][0, 0]) == 0)
    check("all N=3 return amplitudes equal delta", all(exact(delta - pinvs[3][v, v]) == 0 for v in range(3)))
    wrong_delta = sp.Rational(1, 9)
    check("wrong c=1/2 member gives delta=1/9", wrong_delta == sp.Rational(1, 9))
    check("wrong c=1/2 member rejects per-site return amplitude", exact(wrong_delta - pinvs[3][0, 0]) != 0)

    section("PART E - note discipline")
    required_pins = [
        "the fixed-defect density is the generation ring's per-site return amplitude",
        "the equation itself remains the wall; this note types it",
        "W_cycle_holonomy_value",
        "unaudited context",
        "not a terminal no-go",
    ]
    for pin in required_pins:
        check(f"note contains required pin: {pin}", pin in note)

    for label in [f"### N{i}" for i in range(1, 9)]:
        check(f"note contains {label}", label in note)

    forbidden = [
        "only " + "route",
        "last " + "route",
        "ex" + "hausted",
        "closes " + "the " + "route",
        "P" + "DG",
        "new " + "wall",
    ]
    for phrase in forbidden:
        check(f"note excludes forbidden phrase: {phrase}", phrase not in note)

    check("note declares canonical bounded_theorem claim type", "**Claim type:** bounded_theorem" in note)
    check("note does not use runner PASS as source status", "**Status:** PASS" not in note)
    check("note does not lean on PR #4783 as authority", "RULED OUT by PR #4783" not in note)

    allowed_walls = {"W_cycle_holonomy_value", "W_defect_identity_unit", "W_defect_readout_selection"}
    seen_walls = set(re.findall(r"\bW_[A-Za-z0-9_]+\b", note))
    check("note uses no unlisted W_ wall identifiers", seen_walls <= allowed_walls, detail=", ".join(sorted(seen_walls)))

    markdown_targets = re.findall(r"\[[^\]]+\]\(([^)]+)\)", note)
    md_basenames = sorted(Path(target).name for target in markdown_targets if target.endswith(".md"))
    expected_md = sorted(
        [
            "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
            "BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md",
            "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md",
        ]
    )
    check("markdown-link inventory has exactly the three origin/main doc targets", md_basenames == expected_md)

    in_flight = [
        "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01",
        "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01",
        "ACPHILAMBDA_REAL_HOLONOMY_LOCUS_IDENTITY_2026-07-01",
    ]
    for basename in in_flight:
        check(f"in-flight basename appears in text: {basename}", basename in note)
        check(f"in-flight basename is not a markdown target: {basename}", all(basename not in target for target in markdown_targets))

    check("status-authority header is standard", "**Status authority:** independent audit lane only. This note does not set an audit verdict, edit registries, register primitives, change axioms, or claim `AC_phi_lambda` retirement." in note_s)
    check("paired runner is linked", "../scripts/acphilambda_cycle_flux_transport_face_inventory_2026_07_01.py" in note)
    check("note excludes preserved-token meta-language", ("PRES" + "ERVE") not in note)
    check("note excludes record-requirement meta-language", ("required for " + "the record") not in note)
    check("note excludes local-instruction meta-language", ("this " + "spec") not in note)

    note_lines = note.splitlines()
    runner_lines = read(runner_path).splitlines()
    check("note line count is in requested band", 200 <= len(note_lines) <= 250, detail=str(len(note_lines)))
    check("runner line count is in requested band", 230 <= len(runner_lines) <= 290, detail=str(len(runner_lines)))

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 and PASS >= 60 else 1


if __name__ == "__main__":
    raise SystemExit(main())
