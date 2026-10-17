#!/usr/bin/env python3
"""One exact-rational interval evaluation; no dynamics, quadrature or sweep."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json

PREC = 512
SCALE = 1 << PREC


def floor_grid(x: F) -> F:
    return F((x.numerator * SCALE) // x.denominator, SCALE)


def ceil_grid(x: F) -> F:
    return -floor_grid(-x)


@dataclass(frozen=True)
class I:
    lo: F
    hi: F

    def __init__(self, lo, hi=None):
        lo = F(lo)
        hi = lo if hi is None else F(hi)
        if lo > hi:
            raise ValueError("reversed interval")
        object.__setattr__(self, "lo", floor_grid(lo))
        object.__setattr__(self, "hi", ceil_grid(hi))

    def __add__(self, other):
        o = box(other)
        return I(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-box(other))

    def __rsub__(self, other):
        return box(other) - self

    def __mul__(self, other):
        o = box(other)
        vals = [self.lo * o.lo, self.lo * o.hi,
                self.hi * o.lo, self.hi * o.hi]
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval includes zero")
        return I(1 / self.hi, 1 / self.lo)

    def __truediv__(self, other):
        return self * box(other).reciprocal()

    def __rtruediv__(self, other):
        return box(other) / self

    def __pow__(self, n):
        if not isinstance(n, int):
            raise TypeError("integer powers only")
        if n < 0:
            return (self ** (-n)).reciprocal()
        if n == 0:
            return I(1)
        if n % 2 == 0:
            lower = 0 if self.lo <= 0 <= self.hi else min(self.lo ** n, self.hi ** n)
            return I(lower, max(self.lo ** n, self.hi ** n))
        return I(self.lo ** n, self.hi ** n)

    def sqrt(self):
        if self.lo < 0:
            raise ValueError("negative square-root interval")
        lower = isqrt((self.lo.numerator * SCALE * SCALE) // self.lo.denominator)
        upper = isqrt((self.hi.numerator * SCALE * SCALE) // self.hi.denominator)
        if F(upper * upper, SCALE * SCALE) < self.hi:
            upper += 1
        assert F(lower * lower, SCALE * SCALE) <= self.lo
        assert F(upper * upper, SCALE * SCALE) >= self.hi
        return I(F(lower, SCALE), F(upper, SCALE))


def box(x) -> I:
    return x if isinstance(x, I) else I(x)


def imax(*xs) -> I:
    ys = [box(x) for x in xs]
    return I(max(y.lo for y in ys), max(y.hi for y in ys))


def imin(*xs) -> I:
    ys = [box(x) for x in xs]
    return I(min(y.lo for y in ys), min(y.hi for y in ys))


def log_unit_interval(x: F, terms: int = 96) -> I:
    """Exact positive series for 1 <= x <= 2, including its remainder."""
    assert 1 <= x <= 2
    z = I((x - 1) / (x + 1))
    z2, power, partial = z * z, z, I(0)
    for k in range(terms):
        partial = partial + 2 * power / (2 * k + 1)
        power = power * z2
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return I(partial.lo, (partial + tail).hi)


LOG2 = log_unit_interval(F(2))


def log_exact(x: F) -> I:
    assert x > 0
    if x < 1:
        return -log_exact(1 / x)
    k = max(0, x.numerator.bit_length() - x.denominator.bit_length())
    while F(1 << k) > x:
        k -= 1
    while F(1 << (k + 1)) <= x:
        k += 1
    y = x / (1 << k)
    assert 1 <= y < 2
    return log_unit_interval(y) + k * LOG2


def ilog(x) -> I:
    y = box(x)
    return I(log_exact(y.lo).lo, log_exact(y.hi).hi)


def atan_small(x: F, terms: int = 160) -> I:
    assert 0 < x < 1 and terms % 2 == 0
    partial = sum(((-1) ** k * x ** (2 * k + 1) / (2 * k + 1)
                   for k in range(terms)), F(0))
    # An even number of alternating terms ends with a negative term.
    return I(partial, partial + x ** (2 * terms + 1) / (2 * terms + 1))


PI = 16 * atan_small(F(1, 5)) - 4 * atan_small(F(1, 239))


def decimal_text(x: F, rounding: str) -> str:
    with localcontext() as ctx:
        ctx.prec = 22
        ctx.rounding = rounding
        return format(Decimal(x.numerator) / Decimal(x.denominator), ".14E")


def encode(x: I) -> dict:
    return {
        "lo": {"numerator": str(x.lo.numerator), "denominator": str(x.lo.denominator)},
        "hi": {"numerator": str(x.hi.numerator), "denominator": str(x.hi.denominator)},
        "decimal_lo": decimal_text(x.lo, "ROUND_FLOOR"),
        "decimal_hi": decimal_text(x.hi, "ROUND_CEILING"),
    }


VALUES = {}
GATES = []


def save(name, value):
    value = box(value)
    VALUES[name] = encode(value)
    return value


def lt(name, left, right):
    left, right = box(left), box(right)
    ok = left.hi < right.lo
    GATES.append({"name": name, "comparison": "upper(left)<lower(right)",
                  "left": encode(left), "right": encode(right), "passed": ok})
    if not ok:
        raise AssertionError(name)


def le(name, left, right):
    left, right = box(left), box(right)
    ok = left.hi <= right.lo
    GATES.append({"name": name, "comparison": "upper(left)<=lower(right)",
                  "left": encode(left), "right": encode(right), "passed": ok})
    if not ok:
        raise AssertionError(name)


def ceil_integer(x: F) -> int:
    return -((-x.numerator) // x.denominator)


def calculate() -> dict:
    j = save("j_original_checked_enclosure", I("0.0027", "0.003"))
    Jm, q, u = I("0.001"), I("0.0005"), I("1e-8")
    m, g, h = 12, I("5e-8"), I("4e-6")
    a, r = Jm - q, q / Jm
    dinf = 1 / (Jm ** 2 - q ** 2)
    Ctune = 3 * I(3).sqrt() * j * Jm * dinf
    A, B = 1 + u, 8 * u ** 2

    def v_of(w):
        return (B + (B ** 2 + 4 * A * B * (1 + box(w))).sqrt()) / (2 * A)

    def root_polynomial(w, jj):
        w = box(w)
        v = v_of(w)
        # Squared positive-side tuning equation; C^2=27 j^2 Jm^2 dinf^2.
        return w ** 4 * A * (A + v) - 27 * box(jj) ** 2 * Jm ** 2 * dinf ** 2 * u ** 2 * (1 + v + w) ** 2

    initial_lo, initial_hi = F("0.0004"), F("0.0005")
    lt("root_initial_left_negative_all_j", root_polynomial(initial_lo, j), 0)
    lt("root_initial_right_positive_all_j", 0, root_polynomial(initial_hi, j))
    endpoints = []
    for jj in (j.lo, j.hi):
        low, high = initial_lo, initial_hi
        for _ in range(100):
            mid = (low + high) / 2
            val = root_polynomial(mid, jj)
            if val.hi < 0:
                low = mid
            elif val.lo > 0:
                high = mid
            else:
                raise ArithmeticError("root-sign interval unresolved")
        endpoints.append((low, high))
    w = save("w_exact_root_enclosure", I(endpoints[0][0], endpoints[1][1]))
    v = save("v_exact_root_enclosure", v_of(w))
    lt("root_final_left_negative_all_j", root_polynomial(w.lo, j), 0)
    lt("root_final_right_positive_all_j", 0, root_polynomial(w.hi, j))
    vprime = B / (2 * A * v - B)
    # For h(w)=w^2 sqrt(A(A+v))-C u(1+v+w), omitted derivative term is positive.
    derivative_lower = 2 * I(w.lo) - Ctune * u * (1 + vprime)
    lt("root_unique_in_final_box", 0, derivative_lower)
    save("root_h_derivative_lower_enclosure", derivative_lower)

    gamma1, gamma2, gamma3 = (u / dinf).sqrt(), (v / dinf).sqrt(), (w / dinf).sqrt()
    gammamax = imax(gamma1, gamma2, gamma3)
    Z0, Z1, Z2 = 1 + u, 1 + u + v, 1 + v + w
    Lambda = I(3).sqrt() * gamma1 ** 2 / (Jm * (Z0 * Z1).sqrt())
    lam = Lambda * r ** (2 * m - 2)
    rho = (a * lam).sqrt()
    kappa = (3 * j * lam).sqrt()
    delta_m = (u + v + w) * r ** (2 * m)
    Gamma2 = gamma1 ** 2 + gamma2 ** 2 + gamma3 ** 2
    Delta = I("0.185")
    beta_gap, b_gap = Delta - 2 * j, Delta - (Jm + q)
    sin_h = I((h - h ** 3 / 6).lo, h.hi)
    cos_h = I((1 - h ** 2 / 2).lo, 1)
    dbg = 2 * j * sin_h
    for name, value in locals().copy().items():
        if name in ("Jm", "q", "u", "a", "r", "dinf", "Ctune", "gamma1", "gamma2", "gamma3", "gammamax", "Z0", "Z1", "Z2", "Lambda", "lam", "rho", "kappa", "delta_m", "Gamma2", "beta_gap", "b_gap", "g", "h", "dbg"):
            save(name, value)
    lt("q_positive", 0, q)
    lt("q_below_Jm", q, Jm)
    lt("Jm_plus_q_below_2j", Jm + q, 2 * j)
    for name, gam in (("gamma1", gamma1), ("gamma2", gamma2), ("gamma3", gamma3)):
        lt(name + "_positive", 0, gam)
        le(name + "_below_a_over_4", gam, a / 4)
        le(name + "_plus_Jm_below_2j", gam + Jm, 2 * j)
    le("gamma3_below_j", gamma3, j)
    le("gamma1_plus_gamma2_below_2j", gamma1 + gamma2, 2 * j)
    le("gamma2_plus_gamma3_below_2j", gamma2 + gamma3, 2 * j)
    lt("g_positive", 0, g)
    le("g_at_most_1e-6", g, I("1e-6"))
    # h is exactly the rational 4e-6; interval rounding cannot prove self equality.
    assert F("4e-6") == F(1, 250000)
    lt("rho_positive", 0, rho)
    le("rho_inside_original_background_band", rho, dbg)
    le("rho_below_half_mediator_gap", rho, a / 2)
    le("background_band_over_g_at_most_half", dbg / g, I(F(1, 2)))
    le("rho_over_g_at_most_half", rho / g, I(F(1, 2)))
    le("lambda_at_most_1e-8", lam, I("1e-8"))
    le("lambda_over_j_at_most_1_over_16", lam / j, I(F(1, 16)))
    lt("complementary_reference_gap_positive", 0, beta_gap)
    lt("complementary_mediator_gap_positive", 0, b_gap)

    a0 = I("8e-18")
    b0 = 46000 / I("0.0053") + 290 / g
    nu = gamma3 ** 2 / (a * (a - rho))
    tau = gamma3 ** 2 / b_gap
    sigma = imax(nu * rho, tau)
    erho = a0 + b0 * rho
    eta0 = imax(nu * rho / j, tau / beta_gap)
    eta = eta0 + sigma * erho
    lt("eta_strict_below_one", eta, 1)
    lt("selected_port_denominator_positive", nu * rho / j, 1)
    Btilde = (1 / j + erho) / (1 - eta)
    etilde = erho / ((1 - eta0) * (1 - eta))
    qC = Gamma2 / b_gap
    kC = Delta - qC - tau ** 2 * Btilde
    lt("kC_strict_positive", 0, kC)
    gerr = nu * rho / (j ** 2 * (1 - nu * rho / j)) + etilde + etilde ** 2 * tau ** 2 / kC
    y = rho ** 2 / a ** 2
    theta12 = (1 - y) ** (-(2 * m - 1)) - 1
    theta3 = (1 - y) ** (-m) - 1
    chi = delta_m + Gamma2 * rho ** 2 / (a ** 3 * (a - rho)) + I(3).sqrt() * theta12 + 3 * theta3 * (2 + theta3) + 3 * j * (1 + theta3) ** 2 * gerr
    s = (1 - 3 * lam / j).sqrt()
    zeta = 6 * chi / s
    lt("zeta_strict_below_one", zeta, 1)
    bmix = kappa * (1 + theta3) * etilde * tau
    for name in ("a0", "b0", "nu", "tau", "sigma", "erho", "eta0", "eta", "Btilde", "etilde", "qC", "kC", "gerr", "theta12", "theta3", "chi", "s", "zeta", "bmix"):
        save(name, locals()[name])

    # Numerator-resolved selected Stone bound. Three replacements are UPPER bounds:
    # atan(rho/lambda)<=pi/2; Q2<=2rho; rho^2-lambda^2 L<=rho^2.
    Aerr = 1 / ((1 - eta0) * (1 - eta))
    Berr = Aerr ** 2 * tau ** 2 / kC
    D3 = Gamma2 / (a ** 3 * (a - rho))
    H12 = (2 * m - 1) / a ** 2 * (1 - y) ** (-2 * m)
    H3 = m / a ** 2 * (1 - y) ** (-m - 1)
    Hhop = I(3).sqrt() * H12 + 3 * (2 + theta3) * H3
    Jfac = 3 * j * (1 + theta3) ** 2
    C0 = Aerr * a0 + Berr * a0 ** 2
    C1 = nu / (j ** 2 * (1 - nu * rho / j)) + Aerr * b0 + 2 * Berr * a0 * b0
    C2 = Berr * b0 ** 2
    Llog = ilog(1 + rho ** 2 / lam ** 2)
    LR = 2 * ilog(1 + 2 * rho / lam)  # asinh(x)<=log(1+2x), x>=0.
    Jint_upper = delta_m * Llog + D3 * rho ** 2 + 2 * lam * Hhop * rho + Jfac * (PI * C0 + lam * C1 * Llog + 2 * lam * C2 * rho)
    CF = 6 / (s * (1 - zeta))
    beta_mix = bmix / kC
    Dsel = 36 * Jint_upper / (PI * Z0.sqrt() * s ** 2 * (1 - zeta))
    Dout = CF * beta_mix * LR / (PI * Z0.sqrt())
    Dwrong = (2 * rho / kC + CF * LR * (beta_mix + beta_mix ** 2)) / PI
    rc = lam / j
    qc, Cc = 1 - 3 * rc, 6 * rc + 9 * rc ** 2
    E0 = (Cc + rc ** 2 / 12) / qc ** 2 + rc ** 5 / (30 * PI)
    E1 = (4 * I(3).sqrt() * Cc / (3 * PI) + I(3).sqrt() * rc ** 2 / (3 * PI)) / qc ** 2 + I(3).sqrt() * rc ** 4 / (12 * PI)
    E2 = (Cc / I(2).sqrt() + 5 * rc ** 2 / (12 * I(2).sqrt())) / qc ** 2 + rc ** 3 / (3 * PI * I(2).sqrt()) + rc ** 5 / (60 * PI * I(2).sqrt())
    EZ = (E0 ** 2 / Z0 + E1 ** 2 / Z1 + E2 ** 2 / Z2).sqrt() / Z0.sqrt()
    etaref = imin(1, (6 * lam ** 6 + F(16, 3) * j * lam ** 5).sqrt() / rho ** 3)
    Cs = 9 / Z0.sqrt()
    Ss = EZ + etaref / Z0.sqrt() + I(2).sqrt() * (Dsel + Dout) + 2 * Dwrong

    # Full physical nontraveling recovery, including complementary columns.
    UP, UC = CF * (1 + beta_mix), CF * beta_mix * (1 + beta_mix)
    tP = Z2.sqrt() * kappa * (1 + theta3)
    Dstar = tP * UP + tau * UC
    J1_upper = 2 * rho  # sqrt(rho^2+lambda^2)-lambda<=rho.
    W0 = Dstar * LR + 2 * rho * tau / kC
    P0 = Btilde * W0
    P1 = Btilde * (Dstar * J1_upper + rho ** 2 * tau / kC)
    Eint = 2 * gammamax / PI * ((I(2).sqrt() * UP * J1_upper + P1) / (a * (a - rho)) + (1 / a + 1 / b_gap) * (I(2).sqrt() * (UC * LR + 2 * rho / kC) + P0))
    Erec_background = 2 / PI * 14000 * W0 / (1 - eta)
    Erec_port = 2 * gammamax / (PI * a) * P0
    Erec = Erec_background + Erec_port + Eint
    cR = 1 + I(2).sqrt() * gammamax / a
    um = u * (1 - r ** (4 * m - 2))
    # sqrt(u) >= delta_p,m, avoiding a subtractive evaluation.
    epsout = imin(1, u.sqrt() + (F(2, 3) * Z0 * Z1).sqrt() * lam / (rho * (1 + um).sqrt()))

    # New energy-resolved RAW allowance; positive integral ceilings only.
    ds = [lam * Jfac * C0, delta_m + lam * Jfac * C1,
          lam * Hhop + lam * Jfac * C2, D3]
    Is = [PI / (2 * lam ** 3), PI / (2 * lam), 2 * rho, F(2, 3) * rho ** 3]
    Js = [3 * PI / (8 * lam ** 5), PI / (8 * lam ** 3), 3 * PI / (8 * lam)]
    Kint = PI / lam
    AF = 36 * (1 + theta3) / (s ** 2 * (1 - zeta))
    e0, e1 = sigma * a0, nu / j + sigma * b0
    CC = CF * (1 + theta3) * etilde * tau ** 2 / kC
    ca = 2 * I(2).sqrt() / 3
    raw_prefactor = 461 * (j / PI).sqrt() * kappa / (Z0.sqrt() * (1 - eta))
    raw_numerator_terms = [raw_prefactor * AF * d * integ.sqrt() for d, integ in zip(ds, Is)]
    raw_sharp_terms = [raw_prefactor * ca * lam ** 2 / s * e * integ.sqrt() for e, integ in zip((e0, e1, H3), Js)]
    raw_complement = raw_prefactor * CC * Kint.sqrt()
    Eload = sum(raw_numerator_terms, I(0)) + sum(raw_sharp_terms, I(0)) + raw_complement
    Erow = (I("2.1e-13") + (304 / (2 * j * cos_h) + I("0.302") / g) * lam / I(3).sqrt()) / Z0.sqrt()
    Uwrong = tau / (kC * (1 - eta))
    Vwrong = CF / (1 - eta) * beta_mix * (kappa * (1 + theta3) + tau * beta_mix)
    Ewrong_one = 461 * (j / PI).sqrt() * (Uwrong * (2 * rho).sqrt() + Vwrong * (PI / lam).sqrt())
    Eraw = I(2).sqrt() * (Eload + Erow) + 2 * Ewrong_one

    # Unit critical-reference measure only: tail<=mu2/rho^2 and reflected<=mu2/g^2.
    Xi_upper = lam ** 2 / (3 * rho ** 2) + lam ** 2 / (3 * g ** 2)
    p_lower = I((1 - Xi_upper).lo)
    lt("reference_transmitted_mass_lower_positive", 0, p_lower)
    le("reference_mass_lower_at_most_one", p_lower, 1)
    normalization_floor = 1 - (p_lower / Z0).sqrt()
    floor_upper = epsout + cR * Ss + Erec + 2 * Eraw + normalization_floor
    e_infinite, epscut = I(F(1, 200)), I(F(1, 1000))
    lt("complete_upper_allowance_below_requested_error", floor_upper, e_infinite)
    Delta_error = I((e_infinite - floor_upper).lo)

    # Exact-dispersion all-late scalar estimate at restricted cutoff rho.
    sin_hrho, sin_alpha = rho / (2 * j), rho / (2 * g)
    cos_hrho, cos_alpha = (1 - sin_hrho ** 2).sqrt(), (1 - sin_alpha ** 2).sqrt()
    vstar = 2 * g * cos_alpha
    Q1 = g / (j * cos_hrho)
    Pphi = I(F(1, 2)) + I("102.78") * Q1
    tan_hrho, tan_alpha = sin_hrho / cos_hrho, sin_alpha / cos_alpha
    # asin(x)<=x/sqrt(1-x^2); then tan(z)<=z/(1-z^2/2).
    half_angle_upper = (tan_hrho + tan_alpha) / 2
    lt("half_angle_upper_below_one", half_angle_upper, 1)
    tan_half_upper = half_angle_upper / (1 - half_angle_upper ** 2 / 2)
    PN = tan_hrho * Q1 + tan_alpha + F(1, 2) * tan_half_upper * (Q1 + 1)
    Aref = 3 + 9 * rc / (2 * cos_hrho)
    Kref = (2 * g).sqrt() * (8 * lam ** 5 / (3 * PI)).sqrt()
    I0ref = 2 * Kref / (s * vstar * lam ** 2)
    I1ref = (Pphi + PN) * I0ref + Kref * Aref * PI / (2 * s ** 2 * lam ** 3)
    Eedge = 2 * Kref / (s * ((rho ** 2 + lam ** 2) ** 3).sqrt())
    Bref = Eedge + I1ref + (rho / vstar) * I0ref
    onset_terms = {
        "positive_velocity": 1 / vstar,
        "local_decay": 2 / lam * imax(0, ilog(3 * cR * Cs / Delta_error)),
        "incoming_halfline": 9 * Bref ** 2 / (PI * vstar * Z0 * Delta_error ** 2),
        "target_nonzero": Bref ** 2 / (PI * vstar * p_lower),
        "normalization_tail": 3 * Bref ** 2 / (2 * PI * vstar * Z0.sqrt() * p_lower.sqrt() * Delta_error),
    }
    T_required = max(x.hi for x in onset_terms.values())
    T = 1
    while F(T) < T_required:
        T *= 10
    for name, val in onset_terms.items():
        save("onset_" + name, val)
        le("T_satisfies_" + name, val, T)
    # sinh(1)<6/5, proved by its first three terms plus geometric remainder.
    sinh_partial = F(1) + F(1, 6) + F(1, 120)
    sinh_tail = F(1, 5040) / (1 - F(1, 72))
    lt("sinh_one_below_six_fifths", I(sinh_partial + sinh_tail), F(6, 5))
    cut_log = ilog(I(F(6, 5)) / epscut)
    cut_required = 4 * g * T * F(6, 5) + cut_log
    M = ceil_integer(cut_required.hi)
    le("M_satisfies_entire_double_onset_window_cut", cut_required, M)
    lt("total_complete_error_below_one_percent", e_infinite + epscut, I("0.01"))
    # Check explicit incoming and norm terms at the selected T (local term via log gate).
    J_at_T = Bref / (2 * PI).sqrt() * ((vstar * T) ** -2 + (vstar * T) ** -1).sqrt()
    L2_at_T = Bref ** 2 / (2 * PI * vstar * T)
    le("outgoing_halfline_mass_positive_with_margin", L2_at_T, p_lower / 2)
    le("incoming_budget_at_selected_T", J_at_T / Z0.sqrt(), Delta_error / 3)
    le("normalization_tail_budget_at_selected_T", L2_at_T / (Z0.sqrt() * p_lower.sqrt()), Delta_error / 3)
    for name in ("Aerr", "Berr", "D3", "H12", "H3", "Hhop", "Jfac", "C0", "C1", "C2", "Llog", "LR", "Jint_upper", "CF", "beta_mix", "Dsel", "Dout", "Dwrong", "rc", "E0", "E1", "E2", "EZ", "etaref", "Cs", "Ss", "UP", "UC", "tP", "Dstar", "W0", "P0", "P1", "Eint", "Erec_background", "Erec_port", "Erec", "cR", "um", "epsout", "AF", "e0", "e1", "CC", "raw_prefactor", "raw_complement", "Eload", "Erow", "Uwrong", "Vwrong", "Ewrong_one", "Eraw", "Xi_upper", "p_lower", "normalization_floor", "floor_upper", "e_infinite", "epscut", "Delta_error", "vstar", "Q1", "Pphi", "PN", "Aref", "Kref", "I0ref", "I1ref", "Eedge", "Bref", "cut_log", "cut_required", "J_at_T", "L2_at_T"):
        save(name, locals()[name])
    for index, val in enumerate(raw_numerator_terms):
        save(f"raw_numerator_term_{index}", val)
    for index, val in enumerate(raw_sharp_terms):
        save(f"raw_sharp_term_{index}", val)
    save("pi", PI)
    save("log2", LOG2)
    return {
        "kind": "single_tuple_exact_rational_interval_author_certificate",
        "status": "all_programmed_finite_gates_passed_pending_distinct_check",
        "scope": "arithmetic/proof-adapter evaluation; no dynamics, calibration replay, parameter sweep or physical verification",
        "dyadic_fractional_bits": PREC,
        "tuple": {"J_m": "1/1000", "q": "1/2000", "u": "1/100000000", "m": m,
                  "g": "1/20000000", "h": "1/250000", "j": "unchanged exact old calibration, enclosed by [27/10000,3/1000]",
                  "v_w": "unique correlated positive implicit roots in certified box, not independent interval choices",
                  "rho": "sqrt((J_m-q)*lambda_m)", "n1": 2*m-1, "n2": 2*m-1, "n3": m},
        "selected_window": {"T": str(T), "T1": str(2*T), "M": str(M),
                            "infinite_error": "1/200", "cut_error": "1/1000", "complete_error": "3/500"},
        "counts": {"mediator_internal_heads": 10*m-4, "source_path_heads_including_existing_port": 10*m,
                   "head_qubits": str(M+10*m+234), "apparatus_qubits": str(M+10*m+239),
                   "head_edges": str(M+10*m+235), "positive_blocks_at_most": str(2*M+20*m+274)},
        "implicit_root": {"initial_w_box": [str(initial_lo), str(initial_hi)],
                          "root_endpoint_brackets": [[str(x), str(y)] for x, y in endpoints],
                          "bisections_per_extreme_j": 100, "uniform_derivative_argument": "h'(w)>=2w-Cu(1+v'(w))>0"},
        "gates": GATES,
        "intervals": VALUES,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    result = calculate()
    result["executed_source_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    summary = {key: result[key] for key in ("kind", "status", "scope", "tuple", "selected_window", "counts")}
    summary["gate_count"] = len(GATES)
    summary["all_gates_passed"] = all(row["passed"] for row in GATES)
    summary["interval_decimal_views"] = {name: [val["decimal_lo"], val["decimal_hi"]] for name, val in VALUES.items()}
    summary["exact_certificate"] = {"path": str(args.output.resolve()), "bytes": args.output.stat().st_size,
                                    "sha256": sha256(args.output.read_bytes()).hexdigest()}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
