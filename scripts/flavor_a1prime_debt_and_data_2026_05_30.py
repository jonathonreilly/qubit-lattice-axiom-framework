#!/usr/bin/env python3
"""Finite algebra and comparator boundary for the A1prime flavor packet."""

from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def koide_q(masses):
    masses = np.array(masses, float)
    return masses.sum() / np.sqrt(masses).sum() ** 2


def main():
    passed = []

    eye = sp.eye(3)
    g = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    g2 = g * g
    basis = [eye, g, g2]
    gram = sp.Matrix(3, 3, lambda i, j: sp.trace(basis[i].T * basis[j]) / 3)
    passed.append(
        check(
            "A1 real R[Z3] tracial group-element basis has Gram=I",
            gram == sp.eye(3),
            "This is a finite basis calculation, not a physical measure ranking.",
        )
    )

    coeffs = sp.Matrix([sp.trace(b.T * (g + g2)) / 3 for b in basis])
    support_count = sum(1 for c in coeffs if c != 0)
    passed.append(
        check(
            "A2 J-I=g+g^2 occupies two real group-element directions",
            coeffs == sp.Matrix([0, 1, 1])
            and sp.simplify((coeffs.T * coeffs)[0]) == 2
            and support_count == 2,
            f"coeffs={list(coeffs)}; support_count={support_count}",
        )
    )

    theta = sp.symbols("theta", real=True)

    def rotation(th):
        return sp.Matrix([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])

    allowed = [0, 2 * sp.pi / 3, 4 * sp.pi / 3]
    allowed_ok = all(sp.simplify(rotation(t) ** 3 - sp.eye(2)) == sp.zeros(2) for t in allowed)
    continuous_counterexample = sp.simplify(rotation(sp.pi / 6) ** 3 - sp.eye(2)) != sp.zeros(2)
    z = sp.symbols("z")
    passed.append(
        check(
            "A3 fixed C^3=I carrier has only cube-root phases in this finite model",
            allowed_ok
            and continuous_counterexample
            and sp.factor(z**3 - 1) == (z - 1) * (z**2 + z + 1),
            "A continuous U(1) doublet phase is extra to this finite carrier model.",
        )
    )

    a_sym, b_sym, delta = sp.symbols("a_sym b_sym delta", positive=True, real=True)
    lambdas = [a_sym + 2 * b_sym * sp.cos(delta + 2 * sp.pi * k / 3) for k in range(3)]
    q_signed = sp.trigsimp(
        sp.simplify(sum(x**2 for x in lambdas) / sp.simplify(sum(lambdas)) ** 2)
    )
    q_expected = sp.Rational(1, 3) + sp.Rational(2, 3) * b_sym**2 / a_sym**2
    passed.append(
        check(
            "A4 signed Hermitian Q is delta-independent in the supplied model",
            sp.trigsimp(sp.simplify(q_signed - q_expected)) == 0
            and sp.diff(q_signed, delta) == 0,
            f"Q_signed={q_expected}",
        )
    )

    c2 = lambda masses: 6 * koide_q(masses) - 2
    lep = [0.51099895e-3, 0.1056583755, 1.77686]
    up = [2.16e-3, 1.27, 172.69]
    down = [4.67e-3, 93.4e-3, 4.18]
    cbt = [1.27, 4.18, 172.69]
    passed.append(
        check(
            "B1 supplied mass comparators put leptons near c^2=2 and quarks above",
            abs(c2(lep) - 2) < 3e-3 and c2(up) > 3 and 2.3 < c2(down) < 2.5,
            f"lep={c2(lep):.3f}, up={c2(up):.3f}, down={c2(down):.3f}",
        )
    )
    passed.append(
        check(
            "B2 supplied (c,b,t) comparator is cross-sector, not a within-sector C3 closure",
            abs(c2(cbt) - 2) < 0.05,
            f"(c,b,t) c^2={c2(cbt):.3f}",
        )
    )

    d21, d31 = 7.5e-5, 2.5e-3

    def qnu(m1):
        masses = np.array([m1, np.sqrt(m1**2 + d21), np.sqrt(m1**2 + d31)])
        return koide_q(masses)

    qmax = max(qnu(x) for x in np.linspace(0, 0.05, 200))
    passed.append(
        check(
            "B3 supplied normal-ordering neutrino sweep stays below Q=2/3",
            qmax < 0.6,
            f"max Q_nu(NO)={qmax:.3f}",
        )
    )

    required = (17.0, 37.0)
    cabibbo = 13.0
    ratios = (required[0] / cabibbo, required[1] / cabibbo)
    passed.append(
        check(
            "B4 supplied CKM angle inventory is 1.31-2.85x Cabibbo",
            1.30 < ratios[0] < 1.31 and 2.84 < ratios[1] < 2.85,
            f"required={required[0]:.0f}-{required[1]:.0f} deg; ratios={ratios[0]:.2f}-{ratios[1]:.2f}x",
        )
    )

    note = (ROOT / "docs/FLAVOR_A1PRIME_DEBT_AND_DATA_NOTE_2026-05-30.md").read_text()
    compact_note = " ".join(note.split())
    guard_ok = (
        "does not introduce, accept, or reject a revised Axiom 1" in compact_note
        and "does not prove a native `r/Q` normalization law" in compact_note
        and "class-D comparator checks" in compact_note
        and "does not add an axiom" in compact_note
    )
    passed.append(
        check(
            "source guards keep axiom status, normalization, and comparator bridges open",
            guard_ok,
        )
    )

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed) - sum(passed)}")
    print("VERDICT: bounded support for finite R[Z3] support-count algebra and")
    print("external comparator stress tests only. The packet does not prove a")
    print("native r/Q normalization law, does not globally forbid every complex")
    print("order-three representation, and does not certify the embedded mass or")
    print("angle data as framework-derived inputs.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
