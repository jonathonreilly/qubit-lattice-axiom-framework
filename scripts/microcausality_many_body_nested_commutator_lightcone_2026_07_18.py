#!/usr/bin/env python3
"""Exact checks for the many-body nested-commutator lightcone note."""

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TARGET_NOTE = ROOT / "docs/MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md"
CT_NOTE = ROOT / "docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md"
AXIOM_NOTE = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"


def normalized_whitespace(text):
    return " ".join(text.split())


class CheckRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, label, condition):
        ok = bool(condition)
        if ok:
            self.passed += 1
            print(f"PASS: {label}")
        else:
            self.failed += 1
            print(f"FAIL: {label}")

    def needle(self, label, path, needles):
        haystack = normalized_whitespace(path.read_text(encoding="utf-8"))
        if isinstance(needles, str):
            needles = (needles,)
        self.check(
            label,
            all(normalized_whitespace(n) in haystack for n in needles),
        )

    def finish(self):
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])


def kron(*mats):
    out = mats[0]
    for m in mats[1:]:
        out = sp.Matrix(sp.kronecker_product(out, m))
    return out


def com(a, b):
    return a * b - b * a


def is_zero(m):
    return sp.simplify(m) == sp.zeros(*m.shape)


def main():
    checks = CheckRunner()

    site_a = kron(SZ, I2, I2)
    probe_x3 = kron(I2, I2, SX)
    probe_z3 = kron(I2, I2, SZ)
    bond_12_xx = kron(SX, SX, I2)
    bond_23_xx = kron(I2, SX, SX)
    bond_23_zz = kron(I2, SZ, SZ)

    # Group L1 -- support growth.
    checks.check(
        "L1a a bond not touching the support commutes exactly",
        is_zero(com(bond_23_zz, site_a)) and is_zero(com(bond_23_xx, site_a)),
    )
    generic_h = bond_12_xx + bond_23_zz
    ad1 = com(generic_h, site_a)
    checks.check(
        "L1b the first adjoint step stays inside the one-neighborhood",
        is_zero(com(ad1, probe_x3)) and is_zero(com(ad1, probe_z3)),
    )
    checks.check(
        "L1c the first adjoint step is itself nonzero",
        not is_zero(ad1),
    )

    # Group T1 -- below-cone vanishing and cone arrival (generic chain).
    ad2 = com(generic_h, ad1)
    checks.check(
        "T1a k=0 commutator vanishes below the cone",
        is_zero(com(site_a, probe_x3)),
    )
    checks.check(
        "T1b k=1 commutator vanishes below the cone",
        is_zero(com(ad1, probe_x3)),
    )
    checks.check(
        "T1c k=2 commutator is nonzero at the cone distance",
        not is_zero(com(ad2, probe_x3)),
    )

    # Group T2 -- commuting-chain stall exhibit.
    commuting_h = bond_12_xx + bond_23_xx
    cad1 = com(commuting_h, site_a)
    cad2 = com(commuting_h, cad1)
    cad3 = com(commuting_h, cad2)
    checks.check(
        "T2a commuting chain first step is nonzero",
        not is_zero(cad1),
    )
    checks.check(
        "T2b commuting chain never reaches the cone at k=2 (any site-3 probe)",
        is_zero(com(cad2, probe_z3)) and is_zero(com(cad2, probe_x3)),
    )
    checks.check(
        "T2c commuting chain never reaches the cone at k=3 (any site-3 probe)",
        is_zero(com(cad3, probe_z3)) and is_zero(com(cad3, probe_x3)),
    )
    checks.check(
        "T2d the stall mechanism: the two bonds commute exactly",
        is_zero(com(bond_12_xx, bond_23_xx))
        and not is_zero(com(bond_12_xx, bond_23_zz)),
    )

    # Group T3 -- series-bound ingredients.
    k_val, d_val = 5, 2
    checks.check(
        "T3a factorial tail domination d!/k! <= 1/(k-d)! via binomial >= 1",
        sp.binomial(k_val, d_val) >= 1
        and sp.Rational(sp.factorial(d_val), sp.factorial(k_val))
        <= sp.Rational(1, sp.factorial(k_val - d_val)),
    )
    x = sp.Rational(3, 2)
    lhs_tail = sum(x**k / sp.factorial(k) for k in range(d_val, 12))
    rhs_tail = (x**d_val / sp.factorial(d_val)) * sp.exp(x)
    checks.check(
        "T3b exact partial-tail instance is dominated by the closed form",
        sp.simplify(rhs_tail - lhs_tail).is_positive is True,
    )
    two_by_two = sp.Matrix([[0, 2], [1, 0]])
    other = sp.Matrix([[1, 1], [0, -1]])
    comm_norm_sq = max(
        (com(two_by_two, other).H * com(two_by_two, other)).eigenvals()
    )
    prod_bound_sq = 4 * max((two_by_two.H * two_by_two).eigenvals()) * max(
        (other.H * other).eigenvals()
    )
    checks.check(
        "T3c commutator norm-bound instance ||[P,Q]||^2 <= 4||P||^2||Q||^2",
        sp.simplify(prod_bound_sq - comm_norm_sq).is_nonnegative is True,
    )
    pq_norm_sq = max((
        (two_by_two * other).H * (two_by_two * other)
    ).eigenvals())
    qp_norm_sq = max((
        (other * two_by_two).H * (other * two_by_two)
    ).eigenvals())
    p_norm_sq = max((two_by_two.H * two_by_two).eigenvals())
    q_norm_sq = max((other.H * other).eigenvals())
    checks.check(
        "T3d rebuilt chain: triangle plus submultiplicativity on the instance",
        sp.simplify(p_norm_sq * q_norm_sq - pq_norm_sq).is_nonnegative is True
        and sp.simplify(p_norm_sq * q_norm_sq - qp_norm_sq).is_nonnegative
        is True
        and sp.simplify(
            (sp.sqrt(pq_norm_sq) + sp.sqrt(qp_norm_sq)) ** 2 - comm_norm_sq
        ).is_nonnegative
        is True,
    )

    # Group N -- source needles.  __TOTAL__ deliberately not matched.
    checks.needle(
        "N1 cited note names the many-body slice as a separate open task",
        CT_NOTE,
        "The `U`-integrated, many-body, and\n  sharp-rate problems are "
        "separate open tasks, not walls claimed here.",
    )
    checks.needle(
        "N2 axiom memo supplies no dynamics",
        AXIOM_NOTE,
        (
            "Admissibility is not a dynamics axiom.",
            "choose a Hamiltonian or transfer operator",
        ),
    )
    checks.needle(
        "N3 target identifier and labels",
        TARGET_NOTE,
        (
            "microcausality_many_body_nested_commutator_lightcone_bounded_theorem_note_2026-07-18",
            "**L1 (one-neighborhood support growth, exact).**",
            "commuting exhibit, exact, all orders).**",
            "zero of order **at least** `d(X, Y)` at `t = 0`",
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
