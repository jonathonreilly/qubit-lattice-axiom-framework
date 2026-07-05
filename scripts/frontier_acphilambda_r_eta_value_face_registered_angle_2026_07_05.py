#!/usr/bin/env python3
"""Checks for the AC_phi_lambda delta-side value-face note.

The runner is intentionally self-contained: it constructs the circulant object,
derives the elementary symmetric functions from the registered signed-root
triple, and then exercises the registered-angle functional numerically.
"""

from __future__ import annotations

import math
import random
import sys
from dataclasses import dataclass

import sympy as sp


@dataclass
class CheckLog:
    passed: int = 0
    failed: int = 0

    def check(self, tag: str, condition: bool, detail: str) -> None:
        if condition:
            self.passed += 1
            print(f"[PASS] {tag}: {detail}")
        else:
            self.failed += 1
            print(f"[FAIL] {tag}: {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


def elementary_from_spectrum(values: list[float]) -> tuple[float, float, float]:
    e1 = math.fsum(values)
    e2 = math.fsum(
        values[i] * values[j] for i in range(3) for j in range(i + 1, 3)
    )
    e3 = values[0] * values[1] * values[2]
    return e1, e2, e3


def recover_registered_angle(
    values: list[float], *, boundary_tol: float = 1.0e-14
) -> tuple[float, float, float, float]:
    e1, e2, e3 = elementary_from_spectrum(values)
    a = e1 / 3.0
    discriminant = e1 * e1 - 3.0 * e2
    if discriminant <= boundary_tol:
        raise ValueError("B=0 boundary: registered-angle functional undefined")
    B = math.sqrt(max(0.0, discriminant)) / 3.0
    cos3 = (e3 - a**3 + 3.0 * a * B * B) / (2.0 * B**3)
    if cos3 < -1.0 - 1.0e-10 or cos3 > 1.0 + 1.0e-10:
        raise ValueError(f"cos(3 delta) out of range: {cos3!r}")
    cos3_clamped = max(-1.0, min(1.0, cos3))
    Phi = math.acos(cos3_clamped) / 3.0
    return a, B, Phi, cos3


def spectrum(a: float, B: float, delta: float) -> list[float]:
    return [a + 2.0 * B * math.cos(delta + 2.0 * math.pi * k / 3.0) for k in range(3)]


def has_degenerate_pair(values: list[float], *, tol: float = 1.0e-12) -> bool:
    return any(
        abs(values[i] - values[j]) <= tol for i in range(3) for j in range(i + 1, 3)
    )


def hermitian_circulant_numeric(a: float, B: float, delta: float) -> list[list[complex]]:
    C = ((0, 1, 0), (0, 0, 1), (1, 0, 0))
    CT = tuple(zip(*C))
    phase = complex(math.cos(delta), math.sin(delta))
    phase_inv = phase.conjugate()
    H: list[list[complex]] = []
    for i in range(3):
        row: list[complex] = []
        for j in range(3):
            value = (a if i == j else 0.0) + B * phase * C[i][j] + B * phase_inv * CT[i][j]
            row.append(value)
        H.append(row)
    return H


def is_hermitian_numeric(H: list[list[complex]], *, tol: float = 1.0e-12) -> bool:
    return all(abs(H[i][j] - H[j][i].conjugate()) <= tol for i in range(3) for j in range(3))


def symbolic_checks(log: CheckLog) -> None:
    a = sp.symbols("a", real=True)
    B = sp.symbols("B", positive=True, real=True)
    delta = sp.symbols("delta", real=True)

    C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    H = a * sp.eye(3) + B * sp.exp(sp.I * delta) * C + B * sp.exp(-sp.I * delta) * C.T
    H_adjoint_gap = H - H.conjugate().T
    log.check(
        "S1.0",
        all(sp.simplify(entry) == 0 for entry in H_adjoint_gap),
        "constructed H(delta) is Hermitian for real a, positive B, real delta",
    )

    lambdas = [a + 2 * B * sp.cos(delta + 2 * sp.pi * k / 3) for k in range(3)]
    e1 = sp.trigsimp(sum(lambdas))
    e2 = sp.trigsimp(sum(lambdas[i] * lambdas[j] for i in range(3) for j in range(i + 1, 3)))
    e3_raw = sp.prod(lambdas)
    e3_expected = a**3 - 3 * a * B**2 + 2 * B**3 * sp.cos(3 * delta)

    det_gap = sp.simplify(sp.expand_complex(H.det()) - e3_expected)
    product_gap = sp.simplify(sp.expand_trig(e3_raw - e3_expected))
    log.check(
        "S1.1",
        det_gap == 0 and product_gap == 0,
        "det H(delta) and the product of the three constructed eigenvalues give the same e3",
    )
    log.check("S1.2", sp.simplify(e1 - 3 * a) == 0, "e1 derived exactly as 3a")
    log.check(
        "S1.3",
        sp.simplify(e2 - (3 * a**2 - 3 * B**2)) == 0,
        "e2 derived exactly as 3a^2 - 3B^2",
    )
    log.check(
        "S1.4",
        product_gap == 0,
        "e3 derived exactly as a^3 - 3aB^2 + 2B^3 cos(3 delta)",
    )

    # Matching all three invariants (tr H, the second elementary invariant via
    # tr H^2, det H) against the lambda-derived e1, e2, e3 is the
    # characteristic-polynomial identity: the constructed lambda_k ARE the
    # spectrum of H, not an assumed form.
    tr_H = sp.simplify(sp.expand_complex(H.trace()))
    tr_H2 = sp.simplify(sp.expand_complex((H * H).trace()))
    e2_H = sp.simplify((tr_H**2 - tr_H2) / 2)
    det_H = sp.simplify(sp.expand_complex(H.det()))
    gap1 = sp.simplify(sp.expand_trig(tr_H - e1))
    gap2 = sp.simplify(sp.expand_trig(e2_H - e2))
    gap3 = sp.simplify(sp.expand_trig(det_H - sp.expand_trig(e3_raw)))
    log.check(
        "S1.1b",
        gap1 == 0 and gap2 == 0 and gap3 == 0,
        "all three invariants of H(delta) (trace, second invariant from tr H^2, det) "
        "equal the lambda-derived e1, e2, e3: the constructed lambda_k ARE the "
        "spectrum of H, not an assumed form",
    )

    a_recovered = sp.simplify(e1 / 3)
    B_recovered = sp.simplify(sp.sqrt(e1**2 - 3 * e2) / 3)
    log.check("S1.5", sp.simplify(a_recovered - a) == 0, "a inversion from e1 is exact")
    log.check(
        "S1.6",
        sp.simplify(B_recovered - B) == 0,
        "B inversion from e1,e2 is exact on B > 0",
    )
    cos3_recovered = sp.simplify(
        (e3_expected - a_recovered**3 + 3 * a_recovered * B_recovered**2)
        / (2 * B_recovered**3)
    )
    cos3_gap = sp.simplify(sp.expand_trig(cos3_recovered - sp.cos(3 * delta)))
    log.check(
        "S1.7",
        cos3_gap == 0,
        "cos(3 delta) inversion is exact on the nondegenerate stratum",
    )

    e1_delta_blind = sp.diff(e1, delta) == 0
    e2_delta_blind = sp.diff(e2, delta) == 0
    log.check(
        "S1.12",
        e1_delta_blind and e2_delta_blind,
        "e1 and e2 have zero symbolic delta derivative",
    )

    E1, E2, E3 = sp.symbols("E1 E2 E3", real=True)
    r_from_registered_pair = (E1**2 - 3 * E2) / E1**2
    log.check(
        "S1.13",
        sp.diff(r_from_registered_pair, E3) == 0,
        "r is a function of e1,e2 only and is blind to the e3/Phi coordinate",
    )

    de3 = sp.diff(e3_expected, delta)
    derivative_gap = sp.simplify(de3 + 6 * B**3 * sp.sin(3 * delta))
    log.check(
        "S3.1",
        derivative_gap == 0,
        "d(e3)/d(delta) derives exactly as -6 B^3 sin(3 delta)",
    )
    log.check(
        "S3.2",
        sp.factor(de3) == -6 * B**3 * sp.sin(3 * delta),
        "for B > 0 the stationary condition is exactly sin(3 delta)=0",
    )

    stationary_degeneracies = []
    for k in range(6):
        vals = [sp.trigsimp(lam.subs(delta, k * sp.pi / 3)) for lam in lambdas]
        pair_equal = any(
            sp.simplify(vals[i] - vals[j]) == 0 for i in range(3) for j in range(i + 1, 3)
        )
        stationary_degeneracies.append(pair_equal)
    log.check(
        "S3.3",
        all(stationary_degeneracies),
        "each stationary point delta=k*pi/3 has a degenerate eigenvalue pair",
    )

    x = sp.symbols("x", real=True)
    Phi_expr = sp.acos(x) / 3
    log.check(
        "S4.1",
        Phi_expr.free_symbols == {x},
        "Phi=(1/3) arccos(x) contains only a pure numeric argument and no conversion symbol",
    )
    log.check(
        "S4.2",
        bool(0 < sp.Rational(2, 9) < sp.pi / 3),
        "the pure number 2/9 lies strictly inside the dimensionless fold domain [0, pi/3]",
    )


def numerical_checks(log: CheckLog) -> float:
    rng = random.Random(20260705)
    max_a_err = 0.0
    max_B_err = 0.0
    max_Phi_err = 0.0
    max_cos_err = 0.0
    phis_seen: list[float] = []

    for _ in range(200):
        a = rng.uniform(-3.0, 3.0)
        if abs(a) < 0.1:
            a += 0.25 if a >= 0.0 else -0.25
        B = rng.uniform(0.25, 2.5)
        delta = rng.uniform(-math.pi, math.pi)
        values = spectrum(a, B, delta)
        rng.shuffle(values)
        a_rec, B_rec, Phi_rec, cos3_rec = recover_registered_angle(values)
        Phi_target = math.acos(max(-1.0, min(1.0, math.cos(3.0 * delta)))) / 3.0
        max_a_err = max(max_a_err, abs(a_rec - a))
        max_B_err = max(max_B_err, abs(B_rec - B))
        max_Phi_err = max(max_Phi_err, abs(Phi_rec - Phi_target))
        max_cos_err = max(max_cos_err, abs(cos3_rec - math.cos(3.0 * delta)))
        phis_seen.append(Phi_rec)

    log.check(
        "S1.8",
        max(max_a_err, max_B_err, max_Phi_err, max_cos_err) < 1.0e-12,
        "200 shuffled-spectrum round trips recover a, B, Phi, and cos(3 delta) to 1e-12",
    )
    print(
        "ROUNDTRIP S1.8 "
        f"max_a_err={max_a_err:.3e} max_B_err={max_B_err:.3e} "
        f"max_Phi_err={max_Phi_err:.3e} max_cos_err={max_cos_err:.3e}"
    )

    uniform_values = spectrum(1.7, 0.0, 0.41)
    boundary_rejected = False
    try:
        recover_registered_angle(uniform_values)
    except ValueError:
        boundary_rejected = True
    log.check(
        "S1.9",
        boundary_rejected and max(uniform_values) == min(uniform_values),
        "B=0 gives a uniform spectrum and the Phi functional is rejected as undefined",
    )

    plus_values = spectrum(1.3, 0.8, 0.0)
    _, _, plus_Phi, plus_cos = recover_registered_angle(plus_values)
    log.check(
        "S1.10",
        has_degenerate_pair(plus_values)
        and abs(plus_cos - 1.0) < 1.0e-12
        and abs(plus_Phi - 0.0) < 1.0e-12,
        "cos(3 delta)=+1 gives a degenerate pair and Phi=0",
    )

    minus_values = spectrum(1.3, 0.8, math.pi / 3.0)
    _, _, minus_Phi, minus_cos = recover_registered_angle(minus_values)
    log.check(
        "S1.11",
        has_degenerate_pair(minus_values)
        and abs(minus_cos + 1.0) < 1.0e-12
        and abs(minus_Phi - math.pi / 3.0) < 1.0e-8,
        "cos(3 delta)=-1 gives a degenerate pair and Phi=pi/3",
    )

    a_fixed = 2.4
    B_fixed = 0.9
    delta_1 = 0.11
    delta_2 = 0.61
    vals_1 = spectrum(a_fixed, B_fixed, delta_1)
    vals_2 = spectrum(a_fixed, B_fixed, delta_2)
    e1_1, e2_1, _ = elementary_from_spectrum(vals_1)
    e1_2, e2_2, _ = elementary_from_spectrum(vals_2)
    _, _, Phi_1, _ = recover_registered_angle(vals_1)
    _, _, Phi_2, _ = recover_registered_angle(vals_2)
    r_1 = B_fixed * B_fixed / (a_fixed * a_fixed)
    r_2 = B_fixed * B_fixed / (a_fixed * a_fixed)
    log.check(
        "S1.14",
        abs(e1_1 - e1_2) < 1.0e-12
        and abs(e2_1 - e2_2) < 1.0e-12
        and abs(r_1 - r_2) < 1.0e-12
        and abs(Phi_1 - Phi_2) > 1.0e-2,
        "same a,B keep e1,e2 and r fixed while changing Phi through e3",
    )

    requested_phis = [0.05, 2.0 / 9.0, 0.5, math.pi / 3.0 - 0.05]
    explicit_ok = True
    recovered_requested: list[float] = []
    for target in requested_phis:
        a_state = 2.0
        B_state = 0.7
        delta_state = target
        H = hermitian_circulant_numeric(a_state, B_state, delta_state)
        values = spectrum(a_state, B_state, delta_state)
        _, B_rec, Phi_rec, cos3_rec = recover_registered_angle(values)
        ok = (
            B_state > 0.0
            and B_rec > 0.0
            and is_hermitian_numeric(H)
            and -1.0 - 1.0e-12 <= cos3_rec <= 1.0 + 1.0e-12
            and abs(Phi_rec - target) < 1.0e-12
        )
        explicit_ok = explicit_ok and ok
        recovered_requested.append(Phi_rec)
        print(
            "STATE S2.1 "
            f"target_Phi={target:.15f} recovered_Phi={Phi_rec:.15f} "
            f"B={B_state:.6f} hermitian={is_hermitian_numeric(H)}"
        )
    log.check(
        "S2.1",
        explicit_ok,
        "four explicitly constructed law-admissible B>0 states recover the requested Phi values",
    )
    log.check(
        "S2.2",
        len({round(value, 12) for value in recovered_requested}) == len(recovered_requested)
        and max(phis_seen) - min(phis_seen) > 0.9,
        "admissible checks span multiple Phi values; no unique interior Phi is output",
    )

    masses = [0.51099895, 105.6583755, 1776.86]
    positive_roots = [math.sqrt(mass) for mass in masses]
    _, pdg_B, Phi_PDG, pdg_cos3 = recover_registered_angle(positive_roots)
    pdg_gap = abs(Phi_PDG - 2.0 / 9.0)
    print(
        "COMPARATOR S2.PDG "
        f"positive_roots={[round(x, 15) for x in positive_roots]} "
        f"Phi_PDG={Phi_PDG:.15f} abs(Phi_PDG-2/9)={pdg_gap:.15e}"
    )
    log.check(
        "S2.3",
        pdg_B > 0.0 and 0.0 <= Phi_PDG <= math.pi / 3.0 and -1.0 <= pdg_cos3 <= 1.0,
        "PDG labeled comparator runs and lands in the fold domain without a closeness assertion",
    )
    log.check(
        "S5.1",
        math.isfinite(pdg_gap) and pdg_gap >= 0.0,
        "delta-side exactness residual is computed as a comparator gap, not thresholded as a theorem",
    )
    return pdg_gap


def textual_checks(log: CheckLog) -> None:
    from pathlib import Path

    repo = Path(__file__).resolve().parents[1]
    prim = " ".join(
        (repo / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
        .read_text(encoding="utf-8")
        .split()
    )
    q_laws = "The laws do not pick the state; the world does, among the states the laws permit."
    q_point = "Derivations may evaluate at the realized state, pointwise."
    q_cft = (
        "A value that would change under a different law-admissible realized state "
        "is registered data, not derivation output."
    )
    log.check(
        "S2.0",
        q_laws in prim and q_point in prim and q_cft in prim,
        "realized-state primitive sentences quoted in the note are present verbatim "
        "in REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    )

    memo = " ".join(
        (repo / "docs/MINIMAL_AXIOMS_2026-06-29.md").read_text(encoding="utf-8").split()
    )
    q1 = (
        "These axioms state only their named primitive content. Further physical "
        "structure requires derivation, bridge, explicit admission, or approved "
        "primitive registration before use as a premise."
    )
    q3 = (
        "A law privileges no states. Its domain is a supplied condition, and at every "
        "state where the condition holds it gives exactly one answer."
    )
    log.check(
        "S7.0",
        q1 in memo and q3 in memo,
        "2026-06-29 memo Qualification sentences quoted in the note are present "
        "verbatim in MINIMAL_AXIOMS_2026-06-29.md",
    )


def main() -> int:
    log = CheckLog()
    symbolic_checks(log)
    numerical_checks(log)
    textual_checks(log)
    return log.finish()


if __name__ == "__main__":
    sys.exit(main())
