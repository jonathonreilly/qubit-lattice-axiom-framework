#!/usr/bin/env python3
"""Exact beta^9 environment-cluster identification check.

This runner recomputes the source-sector pullback local-packet series
coefficient with exact
rational arithmetic, then checks the d9 census decomposition:

    H_Dloc[9] - Delta[9]
      = (H_Dloc[9] - cube_shell_9) - two_cube_9.

The signed residual is therefore not the raw two-cube weight alone. The
nonlocal irreducible content is the radius-2 two-cube class, with the local
beta^9 shell surplus subtracted in the stripped-environment bookkeeping.
"""

from __future__ import annotations

from math import factorial
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

SERIES_ORDER = 10
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


def build_h_dloc_series() -> list[sp.Rational]:
    """Recompute the rho=1 local packet H_Dloc series exactly."""
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
    return [sp.simplify(h_total[n] - h_mark[n]) for n in range(SERIES_ORDER + 1)]


def no_float_atoms(values: list[sp.Expr]) -> bool:
    return all(not value.has(sp.Float) for value in values)


def note_text() -> str:
    root = Path(__file__).resolve().parent.parent
    note = root / "docs" / "PLAQUETTE_BETA9_ENVIRONMENT_CLUSTER_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-06-12.md"
    return note.read_text(encoding="utf-8")


def main() -> int:
    print("Plaquette beta^9 environment-cluster identification narrow theorem runner")
    print("Status authority: independent audit lane only. This source runner does not set or predict an audit outcome.")
    print("No new imports: exact repo-internal d9 census constants plus exact source-sector local-packet series arithmetic.")

    h_dloc = build_h_dloc_series()
    delta = {
        5: sp.Rational(1, 472392),
        6: sp.Rational(7, 5668704),
        7: sp.Rational(5, 17006112),
        8: sp.Rational(5, 272097792),
        9: sp.Rational(-2035, 264479053824),
    }

    cube_shell_9 = sp.Rational(-235, 29386561536)
    support_count = sp.Integer(60)
    per_support = sp.Rational(1, 198359290368)
    two_cube_9 = support_count * per_support
    w60_signed_residual = sp.simplify(h_dloc[9] - delta[9])
    local_shell_surplus = sp.simplify(h_dloc[9] - cube_shell_9)
    stripped_env_9 = sp.simplify(delta[9] - h_dloc[9])

    section("Part 1: source-sector local-packet recomputation")
    check(
        "H_Dloc matches declared Delta through beta^8",
        all(h_dloc[n] == delta[n] for n in range(5, 9)),
        "; ".join(f"n={n}: {sp.factor(h_dloc[n])}" for n in range(5, 9)),
    )
    check(
        "H_Dloc beta^9 coefficient is exact and recomputed",
        h_dloc[9] == sp.Rational(-6313, 793437161472),
        f"H_Dloc[9] = {sp.factor(h_dloc[9])}",
    )
    check(
        "signed residual is reproduced",
        w60_signed_residual == sp.Rational(-13, 49589822592),
        f"H_Dloc[9] - Delta[9] = {sp.factor(w60_signed_residual)}",
    )

    section("Part 2: d9 census arithmetic")
    check(
        "d9 census assembly is exact: cube shell plus radius-2 two-cube class",
        cube_shell_9 + two_cube_9 == delta[9],
        f"{cube_shell_9} + {two_cube_9} = {delta[9]}",
    )
    check(
        "two-cube class weight is the 60-support census sum",
        two_cube_9 == sp.Rational(5, 16529940864),
        f"60 * {per_support} = {two_cube_9}",
    )
    check(
        "the raw two-cube weight is not equal to the stripped repair coefficient",
        two_cube_9 != stripped_env_9,
        f"two_cube_9 - (Delta[9]-H_Dloc[9]) = {sp.factor(two_cube_9 - stripped_env_9)}",
    )

    section("Part 3: exact residual decomposition")
    check(
        "H_Dloc has a beta^9 local shell surplus over the cube-shell census part",
        local_shell_surplus == sp.Rational(1, 24794911296),
        f"H_Dloc[9] - cube_shell_9 = {sp.factor(local_shell_surplus)}",
    )
    check(
        "signed residual equals local shell surplus minus the two-cube class",
        sp.simplify(local_shell_surplus - two_cube_9) == w60_signed_residual,
        f"{local_shell_surplus} - {two_cube_9} = {w60_signed_residual}",
    )
    check(
        "stripped environment coefficient equals two-cube class minus local surplus",
        stripped_env_9 == sp.Rational(13, 49589822592)
        and stripped_env_9 == sp.simplify(two_cube_9 - local_shell_surplus),
        f"H_env[9] in isolated P1 + H_Dloc bookkeeping = {sp.factor(stripped_env_9)}",
    )
    exact_values = [
        *[h_dloc[n] for n in range(5, 10)],
        *delta.values(),
        cube_shell_9,
        per_support,
        two_cube_9,
        w60_signed_residual,
        local_shell_surplus,
        stripped_env_9,
    ]
    check(
        "all load-bearing arithmetic is exact rational arithmetic",
        all(getattr(value, "is_Rational", False) for value in exact_values)
        and no_float_atoms(exact_values),
        "no Float atoms appear in the checked expressions",
    )

    section("Part 4: note hygiene checks")
    text = note_text()
    lower = text.lower()
    check(
        "note preserves the required status-authority block",
        "Status authority:** independent audit lane only." in text,
    )
    forbidden = ["only route", "last route", "exhausted", "closes the program"]
    check(
        "note avoids listed overreach phrases",
        not any(phrase in lower for phrase in forbidden),
        ", ".join(phrase for phrase in forbidden if phrase in lower),
    )
    check(
        "note states the exact decomposition rather than the naive equality",
        "local_shell_surplus - two_cube_9 = -13/49589822592" in text
        and "two_cube_9 - local_shell_surplus = 13/49589822592" in text,
    )

    print()
    print("FINDING: through beta^8, the local marked-link derivative absorbs the declared connected coefficient packet.")
    print("FINDING: at beta^9, the nonlocal radius-2 two-cube class is the new irreducible census content.")
    print("FINDING: the source-sector residual is the exact signed decomposition local_shell_surplus - two_cube_9.")
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
