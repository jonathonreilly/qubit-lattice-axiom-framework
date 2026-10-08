#!/usr/bin/env python3
"""Exact checks for the supplied three-level downward-jump model.

This is an input-free symbolic runner: no calibration, empirical holdout,
network request, repository data read, numerical optimizer, or Lean build.
The mathematical proof and the narrowly accepted external capacity import
are in the paired note. PASS records algebraic checks, not physical adequacy.
"""

from __future__ import annotations

from itertools import combinations, product
import sys

import sympy as sp


AUDIT_TIMEOUT_SEC = 120


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f": {detail}" if detail else ""))

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return int(self.failed != 0)


def unit(n: int, i: int, j: int) -> sp.Matrix:
    answer = sp.zeros(n)
    answer[i, j] = 1
    return answer


def equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(sp.simplify(x - y) == 0 for x, y in zip(left, right))


def dissipator(jump: sp.Matrix, rho: sp.Matrix) -> sp.Matrix:
    jj = jump.H * jump
    return jump * rho * jump.H - (jj * rho + rho * jj) / 2


def kraus_apply(operators: list[sp.Matrix], rho: sp.Matrix) -> sp.Matrix:
    return sum((k * rho * k.H for k in operators), sp.zeros(operators[0].rows))


def complete(operators: list[sp.Matrix]) -> bool:
    n = operators[0].cols
    return equal(sum((k.H * k for k in operators), sp.zeros(n)), sp.eye(n))


K02 = [sp.Matrix([[1, 0, 0], [0, 0, 1]]), sp.Matrix([[0, 1, 0], [0, 0, 0]])]
K12 = [sp.Matrix([[0, 1, 0], [0, 0, 1]]), sp.Matrix([[1, 0, 0], [0, 0, 0]])]
J02 = sp.Matrix([[1, 0], [0, 0], [0, 1]])
J12 = sp.Matrix([[0, 0], [1, 0], [0, 1]])
S12 = sp.eye(3)
X = sp.Matrix([[0, 1], [1, 0]])


def c02(rho: sp.Matrix) -> sp.Matrix:
    return kraus_apply(K02, rho)


def c12(rho: sp.Matrix) -> sp.Matrix:
    return kraus_apply(K12, rho)


def generator(rho: sp.Matrix, a, b, c, energies) -> sp.Matrix:
    h = sp.diag(*energies)
    return -sp.I * (h * rho - rho * h) + sum(
        (rate * dissipator(unit(3, dest, src), rho)
         for dest, src, rate in [(0, 1, a), (1, 2, b), (0, 2, c)]), sp.zeros(3)
    )


def wait_from_amplitudes(rho: sp.Matrix, u, v, d, energies, time) -> sp.Matrix:
    """Closed form with A=u^2, B=v^2, D=d, and explicit energy phases."""
    out = sp.zeros(3)
    out[0, 0] = rho[0, 0] + (1 - u**2) * rho[1, 1] + (1 - v**2 - d) * rho[2, 2]
    out[1, 1] = u**2 * rho[1, 1] + d * rho[2, 2]
    out[2, 2] = v**2 * rho[2, 2]
    amplitude = (1, u, v)
    for i, j in product(range(3), repeat=2):
        if i != j:
            out[i, j] = (amplitude[i] * amplitude[j]
                         * sp.exp(-sp.I * (energies[i] - energies[j]) * time) * rho[i, j])
    return out


def check_generator_and_wait(q: Checks) -> None:
    a, b, c, t = sp.symbols("a b c t", nonnegative=True)
    h0, h1, h2 = sp.symbols("h0 h1 h2", real=True)
    energies = (h0, h1, h2)
    r = b + c
    hq = sp.diag(h0, h2)

    def l2(rho: sp.Matrix) -> sp.Matrix:
        return -sp.I * (hq * rho - rho * hq) + r * dissipator(unit(2, 0, 1), rho)

    q.check("C02_Kraus_complete", complete(K02))
    q.check("C12_Kraus_complete", complete(K12))
    q.check("J02_J12_isometric", equal(J02.H * J02, sp.eye(2)) and equal(J12.H * J12, sp.eye(2)))
    q.check("S12_X_unitary", equal(S12.H * S12, sp.eye(3)) and equal(X.H * X, sp.eye(2)))

    expected_c = {
        (0, 0): unit(2, 0, 0), (1, 1): unit(2, 0, 0), (2, 2): unit(2, 1, 1),
        (0, 2): unit(2, 0, 1), (2, 0): unit(2, 1, 0),
    }
    loss = (0, a, r)
    for i, j in product(range(3), repeat=2):
        e = unit(3, i, j)
        q.check(f"C02_basis_E{i}{j}", equal(c02(e), expected_c.get((i, j), sp.zeros(2))))
        q.check(f"GKLS_intertwining_E{i}{j}", equal(c02(generator(e, a, b, c, energies)), l2(c02(e))))
        if i != j:
            expected = (-sp.I * (energies[i] - energies[j]) - (loss[i] + loss[j]) / 2) * e
            q.check(f"offdiagonal_generator_E{i}{j}", equal(generator(e, a, b, c, energies), expected))

    u, v = sp.exp(-a * t / 2), sp.exp(-r * t / 2)
    d = b * (sp.exp(-a * t) - sp.exp(-r * t)) / (r - a)
    for i, j in product(range(3), repeat=2):
        e = unit(3, i, j)
        ft = wait_from_amplitudes(e, u, v, d, energies, t)
        q.check(f"free_wait_ODE_distinct_E{i}{j}", equal(ft.diff(t), generator(ft, a, b, c, energies)))
        q.check(f"free_wait_initial_distinct_E{i}{j}", equal(ft.subs(t, 0), e))
        # Physical coincident-rate branch has a=b+c and 0<=b<=a.
        ft_equal = wait_from_amplitudes(e, u, u, b * t * sp.exp(-a * t), energies, t)
        q.check(f"free_wait_ODE_coincident_E{i}{j}", equal(ft_equal.diff(t), generator(ft_equal, a, b, a - b, energies)))
        q.check(f"free_wait_initial_coincident_E{i}{j}", equal(ft_equal.subs(t, 0), e))

    rr = sp.symbols("r", nonnegative=True)
    expr = b * (sp.exp(-a * t) - sp.exp(-rr * t)) / (rr - a)
    q.check("D_coincident_continuous_limit", sp.simplify(sp.limit(expr, rr, a) - b * t * sp.exp(-a * t)) == 0)
    for i, j in product(range(2), repeat=2):
        e = unit(2, i, j)
        ft = wait_from_amplitudes(J02 * e * J02.H, u, v, d, energies, t)
        w = sp.diag(sp.exp(-sp.I * h0 * t), sp.exp(-sp.I * h2 * t))
        # AD at eta=exp(-r*t), written without square-root branch ambiguity.
        ad = sp.Matrix([[e[0, 0] + (1 - v**2) * e[1, 1], v * e[0, 1]],
                        [v * e[1, 0], v**2 * e[1, 1]]])
        q.check(f"encoded_free_AD_with_phase_e{i}{j}", equal(c02(ft), w * ad * w.H))

    q.check("C02_S12_same_before", equal(c02(unit(3, 0, 0)), c02(unit(3, 1, 1))))
    witness = c02(S12 * unit(3, 0, 0) * S12.H) - c02(S12 * unit(3, 1, 1) * S12.H)
    q.check("C02_S12_different_after", equal(witness, sp.diag(1, -1)), "witness = diag(1,-1)")

    # All three deterministic two-cell population partitions.
    pop = sp.Matrix([[0, a, c], [0, -a, b], [0, 0, -b - c]])
    expected_obstruction = {0: sp.Matrix([a - c, c - a]),
                            1: sp.Matrix([-b, b]), 2: sp.zeros(2, 1)}
    for singleton in range(3):
        merged = [i for i in range(3) if i != singleton]
        partition = sp.Matrix([[int(i == singleton) for i in range(3)],
                               [int(i != singleton) for i in range(3)]])
        obstruction = partition * (pop[:, merged[0]] - pop[:, merged[1]])
        q.check(f"population_partition_singleton_{singleton}", equal(obstruction, expected_obstruction[singleton]), str(list(obstruction)))
    expected_escape = {(0, 1): [0, 0], (0, 2): [0, b], (1, 2): [a, c]}
    for pair in combinations(range(3), 2):
        outside = next(i for i in range(3) if i not in pair)
        escaped = [generator(unit(3, i, i), a, b, c, energies)[outside, outside] for i in pair]
        q.check(f"coordinate_escape_{pair}", escaped == expected_escape[pair], str(escaped))


def check_kraus_and_echo(q: Checks) -> None:
    u, v = sp.symbols("u v", nonnegative=True)
    d, time = sp.symbols("D tau", real=True)
    energies = sp.symbols("h0 h1 h2", real=True)
    phase = sp.diag(*(sp.exp(-sp.I * h * time) for h in energies))
    m0 = phase * sp.diag(1, u, v)
    weights = [(1 - u**2, unit(3, 0, 1)), (d, unit(3, 1, 2)),
               (1 - v**2 - d, unit(3, 0, 2))]
    # These weighted terms are Kraus terms when the note's integral bounds hold.
    normalization = m0.H * m0 + sum((weight * k.H * k for weight, k in weights), sp.zeros(3))
    q.check("free_weighted_Kraus_complete", equal(normalization, sp.eye(3)))
    for i, j in product(range(3), repeat=2):
        e = unit(3, i, j)
        formula = wait_from_amplitudes(e, u, v, d, energies, time)
        ks = m0 * e * m0.H + sum((weight * k * e * k.H for weight, k in weights), sp.zeros(3))
        q.check(f"free_weighted_Kraus_E{i}{j}", equal(formula, ks))

    def echo(rho: sp.Matrix) -> sp.Matrix:
        first = wait_from_amplitudes(rho, u, v, d, energies, time)
        return wait_from_amplitudes(S12 * first * S12.H, u, v, d, energies, time)

    slope02 = v**2 * d
    intercept12, slope12, coherence12 = 1 - u**2 * v**2, v**2 * (u**2 - d), u**2 * v**2
    for i, j in product(range(2), repeat=2):
        e = unit(2, i, j)
        out02 = c02(echo(J02 * e * J02.H))
        expected02 = sp.diag(sp.trace(e) - slope02 * e[1, 1], slope02 * e[1, 1])
        q.check(f"complete_Echo_J02_C02_e{i}{j}", equal(out02, expected02))
        out12 = X * c12(echo(J12 * e * J12.H)) * X
        excited12 = intercept12 * sp.trace(e) + slope12 * e[1, 1]
        expected12 = sp.Matrix([[sp.trace(e) - excited12, coherence12 * e[0, 1]],
                                [coherence12 * e[1, 0], excited12]])
        q.check(f"complete_Echo_J12_C12_X_e{i}{j}", equal(out12, expected12))

    # Exact physical point: a=b=c=1, half-wait tau=log(2).
    point_a = sp.exp(-sp.log(2))
    point_b = sp.exp(-2 * sp.log(2))
    point_d = (point_a - point_b) / (2 - 1)
    q.check("rational_point_from_rate_solution", (point_a, point_b, point_d) ==
            (sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 4)))
    rational = {u: sp.sqrt(sp.Rational(1, 2)), v: sp.Rational(1, 2), d: sp.Rational(1, 4)}
    values = tuple(sp.simplify(x.subs(rational)) for x in (slope02, intercept12, slope12, coherence12))
    q.check("rational_Echo_parameters", values == (sp.Rational(1, 16), sp.Rational(7, 8), sp.Rational(1, 16), sp.Rational(1, 8)), str(values))
    residual = sp.simplify((coherence12**2 - slope12).subs(rational))
    q.check("rational_GAD_square_mismatch", residual == -sp.Rational(3, 64), str(residual))
    q.check("first_Echo_nonconstant_Z_not_GAD", values[0] > 0 and values[0] != 0**2)

    # Independently compose exact finite Kraus matrices at that point.
    ms = [sp.diag(1, sp.sqrt(sp.Rational(1, 2)), sp.Rational(1, 2)),
          sp.sqrt(sp.Rational(1, 2)) * unit(3, 0, 1),
          sp.Rational(1, 2) * unit(3, 1, 2),
          sp.sqrt(sp.Rational(1, 2)) * unit(3, 0, 2)]
    q.check("rational_free_Kraus_complete", complete(ms))
    ks02 = [k * m2 * S12 * m1 * J02 for k, m2, m1 in product(K02, ms, ms)]
    ks12 = [X * k * m2 * S12 * m1 * J12 for k, m2, m1 in product(K12, ms, ms)]
    for label, operators in [("02", ks02), ("12", ks12)]:
        q.check(f"rational_composite_{label}_Kraus_complete", complete(operators))
        choi = sp.zeros(4)
        for i, j in product(range(2), repeat=2):
            e = unit(2, i, j)
            out = kraus_apply(operators, e)
            if label == "02":
                ex = sp.diag(sp.trace(e) - e[1, 1] / 16, e[1, 1] / 16)
            else:
                pop = sp.Rational(7, 8) * sp.trace(e) + e[1, 1] / 16
                ex = sp.Matrix([[sp.trace(e) - pop, e[0, 1] / 8], [e[1, 0] / 8, pop]])
            q.check(f"rational_composite_{label}_matrix_unit_{i}{j}", equal(out, ex))
            choi += sp.kronecker_product(e, out)
        minors = [sp.simplify(choi.extract(ix, ix).det())
                  for size in range(1, 5) for ix in combinations(range(4), size)]
        q.check(f"rational_composite_{label}_Choi_PSD", equal(choi, choi.H) and all(m >= 0 for m in minors), "all 15 principal minors nonnegative")

    # Degenerate branches are legitimate channels, not blanket exclusions.
    for i, j in product(range(2), repeat=2):
        e = unit(2, i, j)
        no_decay_echo = S12 * J12 * e * J12.H * S12.H
        q.check(f"zero_wait_second_Echo_identity_{i}{j}", equal(X * c12(no_decay_echo) * X, e))
        no_decay02 = c02(S12 * J02 * e * J02.H * S12.H)
        q.check(f"zero_wait_first_Echo_ground_{i}{j}", equal(no_decay02, sp.trace(e) * unit(2, 0, 0)))
    q.check("b_zero_first_Echo_ground", sp.simplify(slope02.subs(d, 0)) == 0)
    # A nontrivial coincident-rate point: a=b=1,c=0,tau=1.
    coincident = {u: sp.exp(-sp.Rational(1, 2)), v: sp.exp(-sp.Rational(1, 2)), d: sp.exp(-1)}
    q.check("coincident_second_Echo_population_slope_zero", sp.simplify(slope12.subs(coincident)) == 0)
    q.check("coincident_second_Echo_coherence_nonzero", sp.simplify(coherence12.subs(coincident) - sp.exp(-2)) == 0)
    # Positive exception: a=c=0 gives A=1 and D=1-B. The second
    # selected Echo channel is then GAD(gamma=1-B^2, nu=1/(1+B)).
    sequential_only = {u: 1, d: 1 - v**2}
    q.check("a_c_zero_second_Echo_GAD_slope", sp.simplify((slope12 - coherence12**2).subs(sequential_only)) == 0)
    q.check("a_c_zero_second_Echo_GAD_offset", sp.simplify(intercept12.subs(u, 1) - (1 - v**4) / (1 + v**2)) == 0)


def check_capacity_interface_and_bosonic_control(q: Checks) -> None:
    eta, p = sp.symbols("eta p", nonnegative=True)
    output = sp.Matrix([[1 - eta * p, sp.sqrt(eta) * sp.sqrt(p * (1 - p))],
                        [sp.sqrt(eta) * sp.sqrt(p * (1 - p)), eta * p]])
    q.check("phase_pair_output_determinant", sp.simplify(output.det() - eta * (1 - eta) * p**2) == 0)
    opposite = output.copy()
    opposite[0, 1] *= -1
    opposite[1, 0] *= -1
    q.check("phase_pair_average_diagonal", equal((output + opposite) / 2, sp.diag(1 - eta * p, eta * p)))
    # Exact matching of the nu=0 external Kraus convention, eta=1-gamma.
    w = sp.symbols("w", nonnegative=True)
    for i, j in product(range(2), repeat=2):
        e = unit(2, i, j)
        ad = sp.diag(1, w) * e * sp.diag(1, w) + (1 - w**2) * unit(2, 0, 1) * e * unit(2, 1, 0)
        expected = sp.Matrix([[e[0, 0] + (1 - w**2) * e[1, 1], w * e[0, 1]],
                              [w * e[1, 0], w**2 * e[1, 1]]])
        q.check(f"external_nu_zero_channel_interface_{i}{j}", equal(ad, expected))
        q.check(f"AD_eta_one_identity_{i}{j}", equal(ad.subs(w, 1), e))
        q.check(f"AD_eta_zero_ground_{i}{j}", equal(ad.subs(w, 0), sp.trace(e) * unit(2, 0, 0)))

    ladder = unit(3, 0, 1) + sp.sqrt(2) * unit(3, 1, 2)
    rho = unit(3, 1, 2)
    delta = dissipator(ladder, rho) - dissipator(unit(3, 0, 1), rho) - 2 * dissipator(unit(3, 1, 2), rho)
    q.check("bosonic_separate_jump_witness", equal(delta, sp.sqrt(2) * unit(3, 0, 1)), "D[ladder](E12)-D[E01](E12)-2D[E12](E12)=sqrt(2)E01")
    for i in range(3):
        e = unit(3, i, i)
        sep = dissipator(unit(3, 0, 1), e) + 2 * dissipator(unit(3, 1, 2), e)
        q.check(f"bosonic_population_agreement_E{i}{i}", equal(dissipator(ladder, e), sep))
    loss_kraus = [sp.diag(1, sp.sqrt(2) / 2, sp.Rational(1, 2)),
                  (unit(3, 0, 1) + unit(3, 1, 2)) / sp.sqrt(2), unit(3, 0, 2) / 2]
    q.check("bosonic_eta_half_Kraus_complete", complete(loss_kraus))
    q.check("bosonic_eta_half_mixed_output", equal(kraus_apply(loss_kraus, sp.eye(3) / 3), sp.diag(sp.Rational(7, 12), sp.Rational(1, 3), sp.Rational(1, 12))), "(7/12,1/3,1/12)")
    print("EXTERNAL_IMPORT: OAI.GAD.main at adc7f1241b42e322a6451854ab7e4b4c146bf78a; accepted import, not rebuilt by this runner")
    print("SCOPE: supplied GKLS/channel mathematics; no fitted rates, empirical transfer claim, or universal encoding exclusion")


def main() -> int:
    q = Checks()
    print("Exact qutrit free-wait and encoded-channel checks; SymPy " + sp.__version__)
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    try:
        check_generator_and_wait(q)
        check_kraus_and_echo(q)
        check_capacity_interface_and_bosonic_control(q)
    except Exception as exc:
        q.check("UNHANDLED_EXCEPTION", False, repr(exc))
        q.finish()
        raise
    return q.finish()


if __name__ == "__main__":
    sys.exit(main())
