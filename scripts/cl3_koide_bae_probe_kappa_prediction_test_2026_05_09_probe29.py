#!/usr/bin/env python3
"""Verify an abstract supplied-functional obstruction in Herm_circ(3).

This runner contains no load-bearing charged-lepton data and assigns no
physical meaning to the matrix coordinates. Its counted checks use only exact
finite algebra; a charged-lepton snapshot appears only in an explicitly
uncounted conditional comparator.
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


def predicate(label: str, condition: bool) -> tuple[int, int]:
    print(f"{'PASS' if condition else 'FAIL'}: {label}")
    return (1, 0) if condition else (0, 1)


def finish(results: list[tuple[int, int]]) -> tuple[int, int]:
    passes = sum(item[0] for item in results)
    failures = sum(item[1] for item in results)
    print(f"PASS={passes} FAIL={failures}")
    return passes, failures


def normal() -> tuple[int, int]:
    a, x, y = sp.symbols("a x y", real=True)
    mu, nu, total = sp.symbols("mu nu total", real=True, positive=True)
    p = sp.symbols("p", real=True)
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
    reduced = mu * sp.log(p) + nu * sp.log(total - p)
    derivative = sp.diff(reduced, p)
    derivative_numerator = sp.factor(sp.together(derivative).as_numer_denom()[0])
    stationary_solutions = sp.solve(derivative_numerator, p)
    p_star = stationary_solutions[0]
    q_star = total - p_star
    curvature = sp.diff(reduced, p, 2)
    b_zero_solutions = sp.solve((a**2 - 2 * radius2).subs({x: 0, y: 0}), a)

    results = [
        exact("cyclic shift has order three", shift**3 - identity),
        exact("cyclic shift adjoint is its square", shift.conjugate().T - shift**2),
        exact("trivial-isotype energy is 3 a^2", e_plus - 3 * a**2),
        exact("nontrivial-isotype energy is 6 |b|^2", e_perp - 6 * radius2),
        exact(
            "stationarity equation is linear with the claimed numerator",
            derivative_numerator - (mu * total - (mu + nu) * p),
        ),
        predicate("stationarity equation has one algebraic solution", len(stationary_solutions) == 1),
        exact("derived stationary E+ fraction", p_star - mu * total / (mu + nu)),
        exact("derived stationary Eperp fraction", q_star - nu * total / (mu + nu)),
        exact(
            "curvature is negative on 0<p<total after clearing its positive denominator",
            curvature * p**2 * (total - p) ** 2
            + mu * (total - p) ** 2
            + nu * p**2,
        ),
        exact("coordinate ratio equals twice energy ratio", a**2 / radius2 - 2 * (3 * a**2) / (6 * radius2)),
        exact("stationary kappa is 2 mu/nu", 2 * p_star / q_star - 2 * mu / nu),
        exact("supplied weights (1,2) give kappa 1", (2 * mu / nu).subs({mu: 1, nu: 2}) - 1),
        exact("equal weights give kappa 2", (2 * mu / nu).subs({mu: 1, nu: 1}) - 2),
        exact("polynomial zero locus equals equal energies", (3 * a**2 - 6 * radius2) - 3 * (a**2 - 2 * radius2)),
        predicate("global zero locus at b=0 has only a=0", b_zero_solutions == [0]),
        predicate(
            "kappa denominator vanishes at b=0",
            sp.simplify(radius2.subs({x: 0, y: 0})) == 0,
        ),
    ]
    return finish(results)


def independent() -> tuple[int, int]:
    t, mu, nu = sp.symbols("t mu nu", real=True, positive=True)
    reduced = mu * sp.log(t) + nu * sp.log(1 - t)
    q = mu / (mu + nu)
    kl = q * sp.log(q / t) + (1 - q) * sp.log((1 - q) / (1 - t))
    kl_identity = sp.expand_log(
        reduced - reduced.subs(t, q) + (mu + nu) * kl,
        force=True,
    )
    weighted_mean = sp.simplify(q * (t / q) + (1 - q) * ((1 - t) / (1 - q)))
    equality_solutions = sp.solve(sp.Eq(t / q, (1 - t) / (1 - q)), t)
    a2, radius2 = sp.symbols("a2 radius2", positive=True)
    energy_fraction = 3 * a2 / (3 * a2 + 6 * radius2)

    results = [
        exact("Bernoulli KL identity reconstructs the functional gap", kl_identity),
        exact("weighted AM-GM comparison has arithmetic mean one", weighted_mean - 1),
        predicate("weighted AM-GM equality has the unique solution t=q", equality_solutions == [q]),
        exact("coordinate ratio reconstructed from energy fraction", sp.solve(sp.Eq(t, energy_fraction), a2, dict=True)[0][a2] / radius2 - 2 * t / (1 - t)),
        exact("(1,2) fraction is one third", q.subs({mu: 1, nu: 2}) - sp.Rational(1, 3)),
        exact("equal-weight fraction is one half", q.subs({mu: 1, nu: 1}) - sp.Rational(1, 2)),
    ]
    return finish(results)


def hostile() -> tuple[int, int]:
    a, x, y = sp.symbols("a x y", real=True)
    mu, nu, total = sp.symbols("mu nu total", real=True, positive=True)
    p = sp.symbols("p", real=True)
    radius2 = x**2 + y**2
    b = x + sp.I * y
    shift = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    h = a * sp.eye(3) + b * shift + sp.conjugate(b) * shift**2
    h_perp = h - a * sp.eye(3)
    e_perp = sp.simplify(sp.trace(h_perp.conjugate().T * h_perp))

    correct_functional = mu * sp.log(p) + nu * sp.log(total - p)
    correct_equation = sp.together(sp.diff(correct_functional, p)).as_numer_denom()[0]
    p_star = sp.solve(correct_equation, p)[0]
    q_star = total - p_star

    swapped_functional = nu * sp.log(p) + mu * sp.log(total - p)
    swapped_equation = sp.together(sp.diff(swapped_functional, p)).as_numer_denom()[0]
    swapped_p_star = sp.solve(swapped_equation, p)[0]

    results = [
        killed("swap the supplied weights", swapped_p_star - p_star),
        killed("drop the factor two in kappa", p_star / q_star - 2 * p_star / q_star),
        killed("replace Eperp=6|b|^2 by 3|b|^2", e_perp - 3 * radius2),
        killed(
            "put the supplied (1,2) stationary point on the equal-energy locus",
            (p_star - total / 2).subs({mu: 1, nu: 2}),
        ),
        killed(
            "claim equal weights give kappa one",
            (2 * p_star / q_star - 1).subs({mu: 1, nu: 1}),
        ),
        predicate(
            "hostile ratio extension is killed because its denominator is zero at b=0",
            sp.denom(a**2 / radius2).subs({x: 0, y: 0}) == 0,
        ),
        killed(
            "reverse the global zero-locus coefficient",
            (a**2 + 2 * radius2) - (a**2 - 2 * radius2),
        ),
    ]
    return finish(results)


def print_conditional_empirical_comparator() -> None:
    """Recompute a support-only comparator; do not count it as theorem evidence."""
    masses = [
        sp.Rational("0.51099895"),
        sp.Rational("105.6583755"),
        sp.Rational("1776.86"),
    ]
    lambdas = [sp.sqrt(mass) for mass in masses]
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    a0 = sum(lambdas) / sp.sqrt(3)
    z = (lambdas[0] + omega**-1 * lambdas[1] + omega * lambdas[2]) / sp.sqrt(3)
    a = a0 / sp.sqrt(3)
    b = z / sp.sqrt(3)
    kappa = sp.N(a**2 / (sp.re(b) ** 2 + sp.im(b) ** 2), 14)
    print("CONDITIONAL SUPPORT (uncounted): supplied charged-lepton mass snapshot")
    print(f"  recomputed square-root Fourier comparator kappa={kappa}")
    print("  this comparison requires P1, a charged-lepton carrier/readout, and")
    print("  the supplied (1,2) functional as a physical law; none is derived here")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("all", "normal", "independent", "hostile"),
        default="all",
    )
    args = parser.parse_args()
    modes = {"normal": normal, "independent": independent, "hostile": hostile}
    selected = tuple(modes) if args.mode == "all" else (args.mode,)
    total_pass = 0
    total_fail = 0
    for mode in selected:
        print(f"MODE={mode}")
        passes, failures = modes[mode]()
        print(f"TOTAL mode={mode} PASS={passes} FAIL={failures}")
        total_pass += passes
        total_fail += failures
    if args.mode == "all":
        print(f"TOTAL mode=all PASS={total_pass} FAIL={total_fail}")
    print_conditional_empirical_comparator()
    return int(total_fail != 0)


if __name__ == "__main__":
    raise SystemExit(main())
