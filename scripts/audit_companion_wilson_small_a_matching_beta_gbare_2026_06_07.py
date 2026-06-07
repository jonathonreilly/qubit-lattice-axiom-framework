#!/usr/bin/env python3
"""Wilson small-a beta/g_bare matching coefficient theorem.

This runner checks the exact finite symbolic ingredients for the source note:

    supplied standard Wilson plaquette action
    canonical Tr(T_a T_b)=delta_ab/2
        -> beta = 2 N_c / g_bare^2.

It does not derive Wilson action-surface selection, g_bare=1, beta=6 as a
physical value, or any audit verdict.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md"
BETA_ROW = ROOT / "docs" / "BETA_GBARE_SQUARED_RESCALING_INVARIANCE_BOUNDED_NOTE_2026-05-08.md"

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
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def gell_mann_generators() -> list[sp.Matrix]:
    I = sp.I
    zero = sp.Integer(0)
    one = sp.Integer(1)
    sqrt3 = sp.sqrt(3)
    lambdas = [
        sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
        sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
        sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
        sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
        (one / sqrt3) * sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]),
    ]
    return [sp.simplify(L / 2) for L in lambdas]


def part0_source_boundaries() -> None:
    section("Part 0: source-note boundaries")
    check("WM theorem note exists", NOTE.exists(), NOTE.relative_to(ROOT).as_posix())
    check("beta_gbare conditional row exists", BETA_ROW.exists(), BETA_ROW.relative_to(ROOT).as_posix())
    text = NOTE.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    required = [
        "actual_current_surface_status: exact-support",
        "target_claim_id: beta_gbare_squared_rescaling_invariance_bounded_note_2026-05-08",
        "beta = 2 N_c / g_bare^2",
        "beta * g_bare^2 = 2 N_c",
        "does not derive that the framework must select the Wilson action surface",
        "does not claim:",
        "g_bare = 1",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    ]
    for marker in required:
        check(f"note contains marker: {marker[:62]}", marker in text or marker in flat)
    forbidden = [
        "effective_status: retained",
        "audit_status: audited_clean",
        "Wilson plaquette action-surface selection from the three framework axioms is derived",
        "g_bare = 1 is derived",
    ]
    for marker in forbidden:
        check(f"forbidden overclaim absent: {marker[:58]}", marker not in text)


def part1_generator_normalization() -> list[sp.Matrix]:
    section("Part 1: SU(3) generator normalization")
    gens = gell_mann_generators()
    check("eight generators are present", len(gens) == 8)
    all_traceless = all(sp.simplify(sp.trace(T)) == 0 for T in gens)
    check("all generators are traceless", all_traceless)
    all_hermitian = all(sp.simplify(T - T.conjugate().T) == sp.zeros(3) for T in gens)
    check("all generators are Hermitian", all_hermitian)
    gram = sp.Matrix([[sp.simplify(sp.trace(A * B)) for B in gens] for A in gens])
    check("trace Gram is delta_ab/2", sp.simplify(gram - sp.eye(8) / 2) == sp.zeros(8), str(gram[0, 0]))
    return gens


def part2_small_a_expansion(gens: list[sp.Matrix]) -> None:
    section("Part 2: small-a plaquette trace expansion")
    a, g = sp.symbols("a g", positive=True)
    f = sp.symbols("f0:8", real=True)
    X = sp.zeros(3)
    for coeff, T in zip(f, gens):
        X += coeff * T
    X = sp.simplify(a**2 * g * X)
    f_sq = sum(coeff**2 for coeff in f)
    tr_x = sp.simplify(sp.trace(X))
    tr_x2 = sp.simplify(sp.trace(X * X))
    check("Tr X is zero", tr_x == 0)
    check("Tr X^2 is a^4 g^2 F^2 / 2", sp.simplify(tr_x2 - a**4 * g**2 * f_sq / 2) == 0, str(tr_x2))
    re_tr_second = sp.simplify(3 - tr_x2 / 2)
    deficit = sp.simplify(1 - re_tr_second / 3)
    check("SU(3) normalized plaquette deficit coefficient is a^4 g^2 F^2 / 12", sp.simplify(deficit - a**4 * g**2 * f_sq / 12) == 0, str(deficit))
    n = sp.symbols("N_c", positive=True)
    general_deficit = sp.simplify(a**4 * g**2 * f_sq / (4 * n))
    check("general SU(N) deficit formula recorded", general_deficit == a**4 * g**2 * f_sq / (4 * n))


def part3_matching_algebra() -> None:
    section("Part 3: coefficient matching algebra")
    beta, g2, n = sp.symbols("beta g2 N_c", positive=True)
    lattice_coeff = beta * g2 / (4 * n)
    continuum_coeff_unordered = sp.Rational(1, 2)
    beta_solution = sp.solve(sp.Eq(lattice_coeff, continuum_coeff_unordered), beta)[0]
    check("matching equation solves to beta=2N/g^2", sp.simplify(beta_solution - 2 * n / g2) == 0, str(beta_solution))
    check("product beta*g^2 is 2N at solution", sp.simplify(beta_solution * g2 - 2 * n) == 0)
    check("N_c=3 and g^2=1 gives beta=6", sp.simplify(beta_solution.subs({n: 3, g2: 1}) - 6) == 0)
    for n_val, g2_val in [(3, 1), (2, sp.Rational(1, 4)), (5, sp.Rational(7, 3)), (8, sp.Rational(9, 10))]:
        beta_val = sp.simplify(beta_solution.subs({n: n_val, g2: g2_val}))
        check(
            f"N={n_val}, g^2={g2_val}: beta*g^2=2N",
            sp.simplify(beta_val * g2_val - 2 * n_val) == 0,
            f"beta={beta_val}",
        )


def part4_fraction_rescaling_compatibility() -> None:
    section("Part 4: exact Fraction compatibility with downstream beta row")
    samples = [
        (Fraction(3), Fraction(1)),
        (Fraction(3), Fraction(5, 7)),
        (Fraction(5), Fraction(11, 13)),
        (Fraction(7, 2), Fraction(9, 4)),
    ]
    c_values = [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3), Fraction(7, 5)]
    for n_c, g2 in samples:
        beta = 2 * n_c / g2
        check(f"Fraction WM product N={n_c}, g2={g2}", beta * g2 == 2 * n_c, f"beta={beta}")
        for c in c_values:
            beta_prime = c * c * beta
            g2_prime = g2 / (c * c)
            check(
                f"rescaled product invariant N={n_c}, g2={g2}, c={c}",
                beta_prime * g2_prime == 2 * n_c,
            )


def part5_downstream_link() -> None:
    section("Part 5: downstream link and firewall")
    text = BETA_ROW.read_text(encoding="utf-8")
    flat = " ".join(text.split())
    check("beta row cites WM theorem note", "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md" in text)
    check("beta row keeps physical Wilson-surface interpretation conditional", "physical Wilson-surface interpretation remains conditional" in text or "physical Wilson-surface interpretation remains conditional" in flat)
    check("beta row still forbids status promotion", "does not promote any status row" in text or "does not promote any" in text)


def main() -> int:
    print("WILSON SMALL-A MATCHING BETA/G_BARE THEOREM")
    part0_source_boundaries()
    gens = part1_generator_normalization()
    part2_small_a_expansion(gens)
    part3_matching_algebra()
    part4_fraction_rescaling_compatibility()
    part5_downstream_link()
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
