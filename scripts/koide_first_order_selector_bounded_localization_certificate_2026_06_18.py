#!/usr/bin/env python3
"""Verify the Koide first-order selector bounded-localization certificate."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "KOIDE_FIRST_ORDER_SELECTOR_IS_THE_CHIRAL_LR_COUPLING_NOT_A_SYMMETRY_NARROW_NOTE_2026-06-05.md"
CERT = DOCS / "KOIDE_FIRST_ORDER_SELECTOR_BOUNDED_LOCALIZATION_CERTIFICATE_2026-06-18.md"
META = DOCS / "KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md"
Z3_NOGO = DOCS / "KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md"
BERRY = DOCS / "KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md"
STAGGERED = DOCS / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{tag}: {name}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def kron(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.kronecker_product(a, b)


def algebraic_surface_checks() -> None:
    section("1. finite algebraic localization surface")
    w = sp.exp(2 * sp.I * sp.pi / 3)
    c = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    ident3 = sp.eye(3)
    j = ident3 + c + c**2
    gamma = sp.Rational(2, 3) * j - ident3

    check("C is a three-cycle", sp.simplify(c**3 - ident3) == sp.zeros(3, 3))
    check("Gamma_chi is circulant", sp.simplify(gamma * c - c * gamma) == sp.zeros(3, 3))
    check("Gamma_chi has one singlet and two doublet eigenvalues", gamma.eigenvals() == {1: 1, -1: 2})

    a, p, q = sp.symbols("a p q")
    h = a * ident3 + p * c + q * c**2
    anti = sp.simplify(h * gamma + gamma * h)
    sol = sp.solve([anti[i, k] for i in range(3) for k in range(3)], [a, p, q], dict=True)
    check("native circulant anticomm(Gamma_chi) intersection is zero", sol == [{a: 0, p: 0, q: 0}])

    bmod, delta, r = sp.symbols("bmod delta r", positive=True)
    lam = [a + 2 * bmod * sp.cos(delta + 2 * sp.pi * k / 3) for k in range(3)]
    q_koide = sp.simplify(sum(x**2 for x in lam) / sum(lam) ** 2)
    check("Q is delta-independent", sp.simplify(sp.diff(q_koide, delta)) == 0)
    check("Q=(1+2r)/3 under bmod^2/a^2=r", sp.simplify(q_koide.subs(bmod, sp.sqrt(r) * a) - (1 + 2 * r) / 3) == 0)

    omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    omega_bar = sp.Rational(-1, 2) - sp.I * sp.sqrt(3) / 2
    chi_reg = [3, 0, 0]

    def inner(x: list[sp.Expr], y: list[sp.Expr]) -> sp.Expr:
        return sp.simplify(sum(u * sp.conjugate(v) for u, v in zip(x, y)) / 3)

    mult = (
        inner(chi_reg, [1, 1, 1]),
        inner(chi_reg, [1, omega, omega_bar]),
        inner(chi_reg, [1, omega_bar, omega]),
    )
    check("C3 clock character multiplicities are (1,1,1)", mult == (1, 1, 1))

    sx = sp.Matrix([[0, 1], [1, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    escape = kron(ident3, sx)
    c_ext = kron(c, sp.eye(2))
    gamma_ext = kron(ident3, sz)
    check("separate-factor escape commutes with C tensor I", sp.simplify(escape * c_ext - c_ext * escape) == sp.zeros(6, 6))
    check("separate-factor escape anticommutes with I tensor sigma_z", sp.simplify(escape * gamma_ext + gamma_ext * escape) == sp.zeros(6, 6))

    bre, bim = sp.symbols("bre bim", real=True)
    b = bre + sp.I * bim
    mass = a * ident3 + b * c + sp.conjugate(b) * c**2

    def fourier(k: int) -> sp.Matrix:
        return sp.Matrix([1, omega**k, omega ** (2 * k)])

    eigen_checks = [
        sp.simplify(mass * fourier(k) - (a + b * omega**k + sp.conjugate(b) * omega ** (2 * k)) * fourier(k))
        == sp.zeros(3, 1)
        for k in range(3)
    ]
    check("native circulant mass has b-independent Fourier eigenvectors", all(eigen_checks))


def textual_firewall_checks() -> None:
    section("2. note and certificate firewalls")
    note = NOTE.read_text(encoding="utf-8")
    cert = CERT.read_text(encoding="utf-8")
    flat = " ".join((note + "\n" + cert).split())

    for path in [NOTE, CERT, META, Z3_NOGO, BERRY, STAGGERED]:
        check(f"dependency/certificate exists: {path.name}", path.exists())

    required_markers = [
        "Status authority",
        "2026-06-18 bounded-localization re-audit packet",
        "Load-bearing theorem surface:",
        "Non-load-bearing open gates:",
        "bounded algebraic localization and route-pruning theorem",
        "explicit first-order escape isolated by the finite analysis",
        "physical `AC_phi_lambda -> M(b) tensor sigma_+` action term",
        "physical first-order/readout weighting rule",
        "not as a retained positive theorem deriving the physical",
        "not be consumed as a retained physical selector",
        "bounded-localization certificate",
        "source-side bounded-localization certificate",
        "not a claim that the framework already supplies that gate",
        "## No-Go Discipline Gate",
        "Status: PASS",
        "N1 alternative routes",
        "continuous `U(1)_b`",
        "discrete `C3` clock index",
        "native circulant anticommuting operator",
        "static grading or complex structure",
        "separate chiral factor",
        "N2 wall independence",
        "N3 hidden-wall scan",
        "N4 residual matching",
        "N5 rhetoric audit",
        "N6 partial-closure path scan",
        "N7 steelman",
        "N8 cross-cycle echo",
    ]
    for marker in required_markers:
        check(f"required firewall marker present: {marker[:58]}", marker in flat)

    forbidden_overclaims = [
        "is a retained physical selector",
        "derives the physical Koide `r=1/2` selector",
        "AC_phi_lambda supplies the physical",
        "framework supplies the physical coupling",
        "is a retained Koide `r=1/2` derivation",
        "asserts an effective-status change",
        "only surviving escape requires",
        "only surviving first-order escape",
        "only viable first-order escape",
    ]
    for marker in forbidden_overclaims:
        check(f"forbidden overclaim absent: {marker}", marker not in flat)

    numbered = ["1.", "2.", "3.", "4.", "5."]
    check("certificate enumerates five load-bearing statements", all(n in cert for n in numbered))
    check("verification stanza points at this runner", "koide_first_order_selector_bounded_localization_certificate_2026_06_18.py" in cert)


def main() -> int:
    print("KOIDE FIRST-ORDER SELECTOR BOUNDED-LOCALIZATION CERTIFICATE")
    algebraic_surface_checks()
    textual_firewall_checks()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: bounded localization certificate passes; physical L-R coupling/readout remains open.")
        return 0
    print("VERDICT: bounded localization certificate FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
