#!/usr/bin/env python3
"""Verify an abstract supplied-functional obstruction in Herm_circ(3).

This runner contains no charged-lepton data and assigns no physical meaning
to the matrix coordinates.  It checks only exact finite algebra.
"""

from __future__ import annotations

import argparse

import sympy as sp


def exact(label: str, residual: sp.Expr) -> tuple[int, int]:
    simplified = sp.simplify(residual)
    if isinstance(simplified, sp.MatrixBase):
        ok = simplified == sp.zeros(*simplified.shape)
    else:
        ok = simplified == 0
    print(f"{'PASS' if ok else 'FAIL'}: {label}")
    return (1, 0) if ok else (0, 1)


def killed(label: str, mutant_residual: sp.Expr) -> tuple[int, int]:
    ok = sp.simplify(mutant_residual) != 0
    print(f"{'PASS' if ok else 'FAIL'}: hostile mutation killed: {label}")
    return (1, 0) if ok else (0, 1)


def finish(results: list[tuple[int, int]]) -> int:
    passes = sum(item[0] for item in results)
    failures = sum(item[1] for item in results)
    print(f"PASS={passes} FAIL={failures}")
    return 0 if failures == 0 else 1


def normal() -> int:
    a, x, y, mu, nu, total = sp.symbols(
        "a x y mu nu total", real=True, positive=True
    )
    b = x + sp.I * y
    bbar = x - sp.I * y
    identity = sp.eye(3)
    shift = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    h = a * identity + b * shift + bbar * shift**2
    h_plus = a * identity
    h_perp = h - h_plus
    e_plus = sp.trace(h_plus.conjugate().T * h_plus)
    e_perp = sp.trace(h_perp.conjugate().T * h_perp)
    radius2 = x**2 + y**2
    p_star = mu * total / (mu + nu)
    q_star = total - p_star

    results = [
        exact("cyclic shift has order three", shift**3 - identity),
        exact("trivial-isotype energy is 3 a^2", e_plus - 3 * a**2),
        exact("nontrivial-isotype energy is 6 |b|^2", e_perp - 6 * radius2),
        exact("stationary E+ fraction", p_star - mu * total / (mu + nu)),
        exact("stationary Eperp fraction", q_star - nu * total / (mu + nu)),
        exact("coordinate ratio equals twice energy ratio", a**2 / radius2 - 2 * (3 * a**2) / (6 * radius2)),
        exact("stationary kappa is 2 mu/nu", 2 * p_star / q_star - 2 * mu / nu),
        exact("supplied weights (1,2) give kappa 1", (2 * mu / nu).subs({mu: 1, nu: 2}) - 1),
        exact("equal weights give kappa 2", (2 * mu / nu).subs({mu: 1, nu: 1}) - 2),
        exact("polynomial zero locus equals equal energies", (3 * a**2 - 6 * radius2) - 3 * (a**2 - 2 * radius2)),
        exact("zero locus at b=0 forces a=0", (a**2 - 2 * radius2).subs({x: 0, y: 0, a: 0})),
    ]
    return finish(results)


def independent() -> int:
    t, mu, nu = sp.symbols("t mu nu", real=True, positive=True)
    reduced = mu * sp.log(t) + nu * sp.log(1 - t)
    derivative = sp.diff(reduced, t)
    t_star = mu / (mu + nu)
    curvature = sp.diff(reduced, t, 2)
    a2, radius2 = sp.symbols("a2 radius2", positive=True)
    energy_fraction = 3 * a2 / (3 * a2 + 6 * radius2)

    results = [
        exact("one-variable derivative vanishes at reconstructed fraction", derivative.subs(t, t_star)),
        exact("stationary odds are mu/nu", t_star / (1 - t_star) - mu / nu),
        exact("coordinate ratio reconstructed from energy fraction", sp.solve(sp.Eq(t, energy_fraction), a2, dict=True)[0][a2] / radius2 - 2 * t / (1 - t)),
        exact("(1,2) fraction is one third", t_star.subs({mu: 1, nu: 2}) - sp.Rational(1, 3)),
        exact("equal-weight fraction is one half", t_star.subs({mu: 1, nu: 1}) - sp.Rational(1, 2)),
        exact("curvature is strictly negative up to a positive factor", curvature * t**2 * (1 - t) ** 2 + mu * (1 - t) ** 2 + nu * t**2),
    ]
    return finish(results)


def hostile() -> int:
    # Every entry is the residual of a deliberately wrong conclusion.
    mutations = [
        ("swap the (1,2) weights", sp.Rational(4) - 1),
        ("drop the factor two in kappa", sp.Rational(1, 2) - 1),
        ("replace Eperp=6|b|^2 by 3|b|^2", sp.Rational(2) - 1),
        ("put the (1,2) point on the equal-energy locus", sp.Rational(1, 3) - sp.Rational(1, 2)),
        ("claim equal weights give kappa one", sp.Rational(2) - 1),
        ("pretend the ratio denominator is nonzero at b=0", sp.Integer(0) - 1),
        ("reverse the global zero-locus coefficient", sp.Symbol("a2") + 2 * sp.Symbol("r2") - (sp.Symbol("a2") - 2 * sp.Symbol("r2"))),
    ]
    return finish([killed(label, residual) for label, residual in mutations])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("normal", "independent", "hostile"), default="normal")
    args = parser.parse_args()
    return {"normal": normal, "independent": independent, "hostile": hostile}[args.mode]()


if __name__ == "__main__":
    raise SystemExit(main())
