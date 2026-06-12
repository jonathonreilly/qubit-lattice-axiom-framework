#!/usr/bin/env python3
"""Exact finite-series pullback falsifier for the plaquette source sector.

This runner uses only repo-internal character-recurrence algebra and the
already-declared connected-coefficient packet for Delta(beta) = P_full - P_1plaq.
It checks the source-sector HF combinations as formal beta-series. A mismatch is
reported as the expected bounded finding, not as a runner failure.
"""

from __future__ import annotations

from math import factorial

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

SERIES_ORDER = 10
COMPARE_ORDER = 9
NMAX = SERIES_ORDER

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {label}")
    else:
        FAIL += 1
        print(f"FAIL: {label}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print()
    print("=" * 96)
    print(title)
    print("=" * 96)


def weights_box(nmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def recurrence_neighbors(p: int, q: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for a, b in (
        (p + 1, q),
        (p - 1, q + 1),
        (p, q - 1),
        (p, q + 1),
        (p + 1, q - 1),
        (p - 1, q),
    ):
        if a >= 0 and b >= 0:
            out.append((a, b))
    return out


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def series_mul(a: list[sp.Rational], b: list[sp.Rational]) -> list[sp.Rational]:
    out = [sp.Integer(0)] * (SERIES_ORDER + 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b[: SERIES_ORDER + 1 - i]):
            if bj != 0:
                out[i + j] += ai * bj
    return [sp.simplify(x) for x in out]


def series_inv(a: list[sp.Rational]) -> list[sp.Rational]:
    assert a[0] != 0
    out = [1 / a[0]] + [sp.Integer(0)] * SERIES_ORDER
    for n in range(1, SERIES_ORDER + 1):
        out[n] = sp.simplify(-sum(a[k] * out[n - k] for k in range(1, n + 1)) / a[0])
    return out


def series_div(a: list[sp.Rational], b: list[sp.Rational]) -> list[sp.Rational]:
    return series_mul(a, series_inv(b))


def series_pow(a: list[sp.Rational], power: int) -> list[sp.Rational]:
    out = [sp.Integer(1)] + [sp.Integer(0)] * SERIES_ORDER
    for _ in range(power):
        out = series_mul(out, a)
    return out


def series_derivative_log(a: list[sp.Rational]) -> list[sp.Rational]:
    deriv = [
        (n + 1) * a[n + 1] if n + 1 <= SERIES_ORDER else sp.Integer(0)
        for n in range(SERIES_ORDER + 1)
    ]
    return series_mul(deriv, series_inv(a))


def build_recurrence() -> tuple[sp.Matrix, list[tuple[int, int]], dict[tuple[int, int], int]]:
    weights = weights_box(NMAX)
    index = {w: i for i, w in enumerate(weights)}
    jmat = sp.zeros(len(weights))
    for p, q in weights:
        col = index[(p, q)]
        for neighbor in recurrence_neighbors(p, q):
            if neighbor in index:
                jmat[index[neighbor], col] += sp.Rational(1, 6)
    return jmat, weights, index


def build_source_series() -> dict[str, object]:
    jmat, weights, index = build_recurrence()
    dim = len(weights)
    vacuum = index[(0, 0)]

    jpowers = [sp.eye(dim)]
    for _ in range(1, SERIES_ORDER + 1):
        jpowers.append(jpowers[-1] * jmat)

    multiplier = [
        jpowers[n] * sp.Rational(1, (2**n) * factorial(n))
        for n in range(SERIES_ORDER + 1)
    ]

    coeffs = [
        [jpowers[n][i, vacuum] / sp.factorial(n) for n in range(SERIES_ORDER + 1)]
        for i in range(dim)
    ]
    c00 = [coeffs[vacuum][n] for n in range(SERIES_ORDER + 1)]

    dloc_coeffs = [[sp.Integer(0)] * dim for _ in range(SERIES_ORDER + 1)]
    for i, (p, q) in enumerate(weights):
        denom = [dim_su3(p, q) * x for x in c00]
        a_link = series_div(coeffs[i], denom)
        a_link_fourth = series_pow(a_link, 4)
        for n, coeff in enumerate(a_link_fourth):
            dloc_coeffs[n][i] = coeff

    transfer = [sp.zeros(dim) for _ in range(SERIES_ORDER + 1)]
    for i in range(SERIES_ORDER + 1):
        for j in range(SERIES_ORDER + 1 - i):
            dloc_diag = sp.diag(*dloc_coeffs[j])
            for k in range(SERIES_ORDER + 1 - i - j):
                transfer[i + j + k] += multiplier[i] * dloc_diag * multiplier[k]

    e0 = sp.zeros(dim, 1)
    e0[vacuum, 0] = 1
    psi = [e0]
    lambda_coeffs = [sp.Integer(1)]

    for n in range(1, SERIES_ORDER + 1):
        accum = sp.zeros(dim, 1)
        for k in range(1, n + 1):
            accum += transfer[k] * psi[n - k]
        for k in range(1, n):
            accum -= lambda_coeffs[k] * psi[n - k]

        lambda_n = sp.simplify(accum[vacuum, 0])
        lambda_coeffs.append(lambda_n)
        residual = accum - lambda_n * e0

        psi_n = sp.zeros(dim, 1)
        for i in range(dim):
            if i != vacuum:
                psi_n[i, 0] = sp.simplify(residual[i, 0])
        psi.append(psi_n)

    def inner_series(operator: sp.Matrix | None = None) -> list[sp.Rational]:
        out = [sp.Integer(0)] * (SERIES_ORDER + 1)
        for i in range(SERIES_ORDER + 1):
            for j in range(SERIES_ORDER + 1 - i):
                if operator is None:
                    out[i + j] += (psi[i].T * psi[j])[0]
                else:
                    out[i + j] += (psi[i].T * operator * psi[j])[0]
        return [sp.simplify(x) for x in out]

    norm = inner_series()
    h_mark = series_mul(inner_series(jmat), series_inv(norm))
    h_total = series_derivative_log(lambda_coeffs)
    h_dloc = [sp.simplify(h_total[n] - h_mark[n]) for n in range(SERIES_ORDER + 1)]
    p_one_plaquette = series_derivative_log(c00)

    return {
        "jmat": jmat,
        "weights": weights,
        "index": index,
        "c00": c00,
        "p1": p_one_plaquette,
        "h_mark": h_mark,
        "h_dloc": h_dloc,
        "h_total": h_total,
        "lambda_coeffs": lambda_coeffs,
    }


def fmt_series_terms(series: list[sp.Rational], start: int, stop: int) -> str:
    terms = []
    for n in range(start, stop + 1):
        coeff = sp.factor(series[n])
        if coeff != 0:
            terms.append(f"beta^{n}: {coeff}")
    return "; ".join(terms) if terms else "all zero"


def main() -> int:
    print("Plaquette source-sector pullback identity narrow theorem runner")
    print("Status authority: independent audit lane only. This source runner does not set or predict an audit outcome.")
    print("No new imports: exact character recurrence plus repo-declared Delta coefficients only.")

    data = build_source_series()
    jmat = data["jmat"]
    c00 = data["c00"]
    p1 = data["p1"]
    h_mark = data["h_mark"]
    h_dloc = data["h_dloc"]
    h_total = data["h_total"]

    delta = {
        5: sp.Rational(1, 472392),
        6: sp.Rational(7, 5668704),
        7: sp.Rational(5, 17006112),
        8: sp.Rational(5, 272097792),
        9: sp.Rational(-2035, 264479053824),
    }
    p_full = list(p1)
    for n, coeff in delta.items():
        p_full[n] += coeff

    section("Part 1: recurrence and one-plaquette series")
    check(
        "source recurrence J is exactly symmetric on the finite box",
        jmat == jmat.T,
        f"box NMAX={NMAX}, dim={jmat.shape[0]}",
    )
    check(
        "finite box contains every recurrence path needed through beta^10",
        NMAX == SERIES_ORDER,
        "a path from the vacuum needs at least n steps to reach p+q=n",
    )
    check(
        "vacuum coefficient seeds are exact",
        c00[0] == 1 and c00[1] == 0 and c00[2] == sp.Rational(1, 36),
        f"c00[0..2]={[c00[i] for i in range(3)]}",
    )
    check(
        "rho=delta rank-one source gives the isolated one-plaquette derivative",
        p1[1] == sp.Rational(1, 18)
        and p1[2] == sp.Rational(1, 216)
        and p1[5] == sp.Rational(-1, 186624),
        fmt_series_terms(p1, 1, 8),
    )

    section("Part 2: local-packet HF combination")
    check(
        "D_loc prime term matches the declared connected Delta through beta^8",
        all(h_dloc[n] == delta[n] for n in range(5, 9)),
        fmt_series_terms(h_dloc, 5, 9),
    )
    dloc_d9_residual = sp.simplify(h_dloc[9] - delta[9])
    check(
        "D_loc prime term has a named beta^9 residual against full Delta",
        dloc_d9_residual == sp.Rational(-13, 49589822592),
        f"H_Dloc[9] - Delta[9] = {sp.factor(dloc_d9_residual)}",
    )
    hmark_shift_5 = sp.simplify(h_mark[5] - p1[5])
    check(
        "dressed multiplier H_mark is not the isolated one-plaquette derivative",
        hmark_shift_5 == sp.Rational(1, 944784),
        f"H_mark[5] - P_1plaq[5] = {sp.factor(hmark_shift_5)}",
    )

    section("Part 3: raw candidate falsifier")
    raw_diff = [sp.simplify(h_total[n] - p_full[n]) for n in range(SERIES_ORDER + 1)]
    check(
        "raw local-packet candidate H_mark + H_Dloc differs from P_full at beta^5",
        raw_diff[5] == sp.Rational(1, 944784),
        f"(H_mark+H_Dloc-P_full)[5] = {sp.factor(raw_diff[5])}",
    )
    check(
        "the candidate mismatch is exact rational arithmetic, not float-derived",
        all(getattr(raw_diff[n], "is_Rational", False) for n in range(COMPARE_ORDER + 1)),
        fmt_series_terms(raw_diff, 5, 9),
    )
    partial_combo = [sp.simplify(p1[n] + h_dloc[n] - p_full[n]) for n in range(SERIES_ORDER + 1)]
    check(
        "isolated P_1plaq plus H_Dloc is only a partial match: beta^5..8 pass, beta^9 fails",
        all(partial_combo[n] == 0 for n in range(5, 9))
        and partial_combo[9] == sp.Rational(-13, 49589822592),
        f"(P_1plaq+H_Dloc-P_full)[9] = {sp.factor(partial_combo[9])}",
    )

    print()
    print("FINDING: direct dressed local-packet pullback is refuted at beta^5.")
    print("FINDING: the D_loc prime term tracks Delta through beta^8 but leaves a beta^9 residual target.")
    print("Named residual: physical residual-environment pullback and dressed-multiplier state-shift separation.")
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
