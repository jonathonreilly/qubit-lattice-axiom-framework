#!/usr/bin/env python3
"""Exact algebra and scale-covariance checks for the CKM down-type boundary.

The proof layer contains no observed mass, fitted exponent, or selected scale.
The final numerical block is explicitly comparator-only and illustrates why
the historical +0.20% cross-surface match is not RG-covariant.
"""

from __future__ import annotations

from fractions import Fraction
from math import isclose, sqrt

import sympy as sp


EXACT_PASS = 0
COMPARATOR_PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "", *, comparator: bool = False) -> None:
    global EXACT_PASS, COMPARATOR_PASS, FAIL
    if condition:
        if comparator:
            COMPARATOR_PASS += 1
            status = "COMPARATOR_PASS"
        else:
            EXACT_PASS += 1
            status = "EXACT_PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"[{status}] {label}")
    if detail:
        print(f"             {detail}")


def normalized_determinant_core() -> None:
    print("\n1. EXACT NORMALIZED-DETERMINANT CORE")
    r = sp.symbols("R", positive=True)
    q = sp.diag(1, 0, 0, 0, 0, 0)
    identity = sp.eye(6)
    p = identity - q
    x_r = q + r * p

    check("Q is a projector", q * q == q)
    check("P is a projector", p * p == p)
    check("Q and P are complementary", q * p == sp.zeros(6) and q + p == identity)
    check("rank(Q)=1", q.rank() == 1)
    check("rank(P)=5", p.rank() == 5)
    check("det(Q+R P)=R^5", sp.factor(x_r.det()) == r**5)
    check("normalized log determinant has weight 5/6", sp.expand_log(sp.log(x_r.det()), force=True) / 6 == sp.Rational(5, 6) * sp.log(r))

    n = sp.symbols("N", integer=True, positive=True)
    p_det = sp.Rational(1, 1) - sp.Rational(1, 2) / n
    c_f = (n**2 - 1) / (2 * n)
    # Standard fundamental-generator normalization:
    # tr_F(T^a T^b) = T_F delta^(ab), T_F = 1/2.
    t_f = sp.Rational(1, 2)
    casimir_power = sp.factor(c_f - t_f)
    equality_numerator = sp.factor(sp.together(p_det - casimir_power) * 2 * n)

    check("2N rank-one complement gives (2N-1)/(2N)", sp.simplify(p_det - (2 * n - 1) / (2 * n)) == 0)
    check("C_F-T_F general form", sp.simplify(casimir_power - (n**2 - n - 1) / (2 * n)) == 0)
    check(
        "power equality reduces to N(3-N)=0",
        sp.simplify(equality_numerator - n * (3 - n)) == 0,
    )
    positive_solutions = [k for k in range(1, 20) if sp.simplify(p_det.subs(n, k) - casimir_power.subs(n, k)) == 0]
    check("N_c=3 is unique in positive scan", positive_solutions == [3], f"solutions={positive_solutions}")
    check("p_det(3)=5/6", p_det.subs(n, 3) == sp.Rational(5, 6))
    check("C_F-T_F at N_c=3 is 5/6", casimir_power.subs(n, 3) == sp.Rational(5, 6))


def orientation_countermodel() -> None:
    print("\n2. EXACT MASS-SPECTRUM / MIXING COUNTERMODEL")
    theta = sp.symbols("theta", real=True)
    u, c, t = sp.symbols("u c t", positive=True)
    d, s, b = sp.symbols("d s b", positive=True)
    rot = sp.Matrix([
        [1, 0, 0],
        [0, sp.cos(theta), sp.sin(theta)],
        [0, -sp.sin(theta), sp.cos(theta)],
    ])
    m_u = sp.diag(u, c, t)
    d_diag = sp.diag(d, s, b)
    m_d = sp.simplify(rot * d_diag * rot.T)

    check("down trace is orientation-invariant", sp.simplify(sp.trace(m_d) - (d + s + b)) == 0)
    check("down determinant is orientation-invariant", sp.simplify(m_d.det() - d * s * b) == 0)
    check("down quadratic trace is orientation-invariant", sp.simplify(sp.trace(m_d * m_d) - (d**2 + s**2 + b**2)) == 0)
    check("up spectrum stays fixed", m_u.det() == u * c * t)
    check("relative 2-3 mixing varies as sin(theta)", rot[1, 2] == sp.sin(theta))
    check("two fixed-spectrum models have different mixing", rot[1, 2].subs(theta, 0) == 0 and rot[1, 2].subs(theta, sp.pi / 6) == sp.Rational(1, 2))


def scale_covariance() -> None:
    print("\n3. EXACT SCALE-COVARIANCE OBSTRUCTION")
    pred, common, transport = sp.symbols("R_pred R_common T", positive=True)
    dev_common = pred / common - 1
    dev_mixed = transport * pred / (transport * common) - 1
    dev_cross = pred / (transport * common) - 1

    check("shared transport preserves relative deviation", sp.simplify(dev_mixed - dev_common) == 0)
    check("crossed comparison depends on transport", sp.diff(dev_cross, transport) == -pred / (common * transport**2))
    check("crossed comparison can be tuned to zero", sp.simplify(dev_cross.subs(transport, pred / common)) == 0)

    gamma = sp.symbols("gamma", positive=True)
    dlog_same = -gamma - (-gamma)
    p_power = sp.Rational(5, 6)
    dlog_mixed_bridge = p_power * (-gamma)
    check("flavor-universal common-scale mass ratio has zero RG derivative", dlog_same == 0)
    check("fixed-power mixed bridge has nonzero numerator-scale derivative", dlog_mixed_bridge != 0)

    c_f = sp.Rational(4, 3)
    gamma0 = 6 * c_f
    beta0_nf4 = sp.Rational(11) - sp.Rational(8, 3)
    one_loop_mass_power = gamma0 / (2 * beta0_nf4)
    check("one-loop n_f=4 mass-transport power is 12/25", one_loop_mass_power == sp.Rational(12, 25))
    check("one-loop mass-transport power is not 5/6", one_loop_mass_power != sp.Rational(5, 6))


def comparator_only_illustration() -> None:
    # All constants below are comparators only (comparator=True), never proof
    # inputs. Conditional provenance:
    #   alpha_s_v          -- reused strong coupling; rides on the supplied
    #                         plaquette <P>=0.5934 (comparator-only license,
    #                         ALPHA_S_DERIVED_NOTE.md). The alpha_s(v)/sqrt(6)
    #                         prediction rests on the supplied CKM-atlas
    #                         identifications |V_us|^2=alpha_s(v)/2,
    #                         A^2=N_pair/N_color=2/3, |V_cb|=A|V_us|^2 and the
    #                         open 5/6 bridge; none is derived here.
    #   81.0, 93.4, 4180.0 -- observational/PDG-style running masses (MeV).
    #   0.3026, 0.2211     -- observational/PDG-style alpha_s literature values.
    print("\n4. COMPARATOR-ONLY NUMERICAL ILLUSTRATION")
    alpha_s_v = 0.103303816122
    r_pred = (alpha_s_v / sqrt(6.0)) ** (6.0 / 5.0)
    r_common = 81.0 / 4180.0
    transport = 93.4 / 81.0
    r_mixed = 93.4 / 4180.0
    transported_pred = transport * r_pred
    cross_dev = r_pred / r_mixed - 1.0
    common_dev = r_pred / r_common - 1.0
    covariant_mixed_dev = transported_pred / r_mixed - 1.0
    one_loop_from_old_runner_couplings = (0.3026 / 0.2211) ** (12.0 / 25.0)

    check("R_mixed=T R_common", isclose(r_mixed, transport * r_common, rel_tol=0, abs_tol=1e-15), comparator=True)
    check("historical crossed deviation is +0.202%", isclose(cross_dev * 100, 0.2024391375, rel_tol=0, abs_tol=1e-9), comparator=True)
    check("covariant mixed deviation equals common deviation", isclose(covariant_mixed_dev, common_dev, rel_tol=0, abs_tol=1e-14), f"deviation={common_dev * 100:+.9f}%", comparator=True)
    check("covariant deviation remains +15.542%", isclose(covariant_mixed_dev * 100, 15.5420717956, rel_tol=0, abs_tol=1e-9), comparator=True)
    check(
        "old runner couplings imply 1.162557619574",
        isclose(
            one_loop_from_old_runner_couplings,
            1.1625576195735408,
            rel_tol=0,
            abs_tol=1e-14,
        ),
        f"one_loop={one_loop_from_old_runner_couplings:.12f}",
        comparator=True,
    )
    check(
        "one-loop factor differs from observed-mass transport",
        not isclose(
            one_loop_from_old_runner_couplings,
            transport,
            rel_tol=0,
            abs_tol=1e-3,
        ),
        f"one_loop={one_loop_from_old_runner_couplings:.9f}, "
        f"observed={transport:.9f}",
        comparator=True,
    )


def main() -> int:
    print("CKM DOWN-TYPE FIVE-SIXTHS ALGEBRA AND SCALE-COVARIANCE BOUNDARY")
    normalized_determinant_core()
    orientation_countermodel()
    scale_covariance()
    comparator_only_illustration()
    print(f"\nSUMMARY: EXACT_PASS={EXACT_PASS} COMPARATOR_PASS={COMPARATOR_PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
