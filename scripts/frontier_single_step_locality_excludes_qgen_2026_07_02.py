#!/usr/bin/env python3
"""Exact bounded checks for Block10 single-step locality versus Q-gen."""

from __future__ import annotations

import sympy as sp


PASS = 0
FAIL = 0


def check(name: str, condition: bool) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
    else:
        FAIL += 1
        print(f"FAIL {name}")


def sym_rep(n: int, N: int) -> int:
    return n if 2 * n <= N else n - N


def qgen_full_step_weights(N: int) -> list[sp.Expr]:
    weights: list[sp.Expr] = []
    for k in range(1, N // 2 + 1):
        total = sum(
            sym_rep(n, N) ** 2 * sp.cos(2 * sp.pi * k * n / N)
            for n in range(N)
        )
        factor = sp.Rational(1, N) if (N % 2 == 0 and k == N // 2) else sp.Rational(2, N)
        weights.append(-factor * total)
    return weights


def sign_string(weights: list[sp.Expr]) -> str:
    signs = []
    for weight in weights:
        value = sp.N(weight, 80)
        if value > 0:
            signs.append("+")
        elif value < 0:
            signs.append("-")
        else:
            signs.append("0")
    return "".join(signs)


def verify_full_step_match(N: int, weights: list[sp.Expr]) -> None:
    for n in range(1, N // 2 + 1):
        lhs = sum(
            weights[k - 1] * (1 - sp.cos(2 * sp.pi * k * n / N))
            for k in range(1, N // 2 + 1)
        )
        rhs = sym_rep(n, N) ** 2
        residual = sp.N(lhs - rhs, 80)
        check(f"T2_Z{N}_mode_{n}_match", abs(residual) < sp.Float("1e-60"))


def main() -> None:
    # T1: finite U(1) jump generators obey psi(n) <= 2W, while Q-gen s*n^2 grows.
    W = sp.Rational(7, 3)
    for n in (3, 4, 8, 16):
        check(f"T1_U1_Qgen_exceeds_finite_bound_n{n}", sp.Rational(n * n, 1) > 2 * W)

    # T2: finite Z_N full-step cosine inversion matches q_N as a linear span.
    sign_records = {}
    positive_cases = []
    for N in (5, 7, 8, 9, 12):
        weights = qgen_full_step_weights(N)
        verify_full_step_match(N, weights)
        signs = sign_string(weights)
        sign_records[N] = signs
        check(f"T2_Z{N}_has_reported_negative_weight", "-" in signs)
        if "-" not in signs and "0" not in signs:
            positive_cases.append(N)

    # Exact N=5 closed forms.
    w5 = qgen_full_step_weights(5)
    check("T2_Z5_w1_exact", sp.simplify(w5[0] - (1 + 3 * sp.sqrt(5) / 5)) == 0)
    check("T2_Z5_w2_exact", sp.simplify(w5[1] - (1 - 3 * sp.sqrt(5) / 5)) == 0)

    # T3: nearest-step ratio and finite-N deficit.
    x = sp.symbols("x")
    ratio_identity = sp.trigsimp(
        (1 - sp.cos(2 * x)) / (1 - sp.cos(x)) - 4 * sp.cos(x / 2) ** 2
    )
    deficit_identity = sp.trigsimp(4 - 4 * sp.cos(x) ** 2 - 4 * sp.sin(x) ** 2)
    check("T3_ratio_identity", ratio_identity == 0)
    check("T3_deficit_identity", deficit_identity == 0)
    for N in range(3, 13):
        deficit = 4 * sp.sin(sp.pi / N) ** 2
        ratio = 4 * sp.cos(sp.pi / N) ** 2
        check(f"T3_Z{N}_deficit_positive", sp.N(deficit, 80) > 0)
        check(f"T3_Z{N}_ratio_below_4", sp.N(4 - ratio, 80) > 0)

    total = PASS + FAIL
    status = "PASS" if FAIL == 0 else "FAIL"
    signs = ";".join(f"N{N}:{sign_records[N]}" for N in (5, 7, 8, 9, 12))
    positive_text = ",".join(str(N) for N in positive_cases) if positive_cases else "none"
    print(f"SUMMARY PASS={PASS} FAIL={FAIL} TOTAL={total}")
    print(f"SUMMARY T2_full_ZN_signs={signs}; positive_full_step_cases={positive_text}")
    print(
        "SUMMARY status="
        f"{status} T1_U1_bound_witnesses=n=3,4,8,16 "
        "T3_deficit=4*sin(pi/N)^2 for N=3..12"
    )


if __name__ == "__main__":
    main()
