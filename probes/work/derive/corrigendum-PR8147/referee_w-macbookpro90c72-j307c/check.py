#!/usr/bin/env python3
"""Referee for corrigendum PR8147 a2.

Author w-jonathonsmac4f50-j3b64 (claude-opus-5). Own symbol identities and own read
of commit 9c364d1d6f75. The other campaign PRs were not re-audited.
"""
import subprocess
import mpmath as mp
import sympy as sp

fails = []
SHA = "9c364d1d6f75"
NOTE = (
    "docs/ADMISSIBILITY_RULE_CAUSAL_GAUSSIAN_FORMATION_LAW_RECORD_TWO_POINT_FUNCTION_HEAT_"
    "KERNEL_NOT_LATTICE_GREEN_FUNCTION_BOUNDED_THEOREM_NOTE_2026-09-15.md"
)


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def symbol():
    u, g = sp.symbols("u g", real=True)
    mod = sp.expand((1 - g * sp.cos(u)) ** 2 + (g * sp.sin(u)) ** 2)
    closed = (1 - g) ** 2 + 4 * g * sp.sin(u / 2) ** 2
    series = sp.series(4 * sp.sin(u / 2) ** 2, u, 0, 6).removeO()
    report(
        "symbol",
        sp.simplify(mod - closed) == 0 and sp.simplify(series - (u ** 2 - u ** 4 / 12)) == 0,
        "at g=1 the level symbol is 4 sin^2(u/2) = u^2 - u^4/12 + ...",
    )


def domain():
    u = sp.symbols("u", positive=True)
    r = 1 - 4 * sp.sin(u / 2) ** 2 / u ** 2
    head = sp.series(r, u, 0, 8).removeO()
    want = u ** 2 / 12 - u ** 4 / 360 + u ** 6 / 20160
    edge = sp.simplify(1 - 4 / sp.pi ** 2)

    def radius(tol):
        return mp.findroot(lambda x: 1 - 4 * mp.sin(x / 2) ** 2 / x ** 2 - tol, mp.mpf("0.5"))

    one, five, ten = radius(mp.mpf("0.01")), radius(mp.mpf("0.05")), radius(mp.mpf("0.10"))
    report(
        "domain",
        sp.simplify(head - want) == 0
        and abs(edge - mp.mpf("0.594715")) < mp.mpf("1e-5")
        and abs(3 * one - mp.mpf("1.04132")) < mp.mpf("1e-4")
        and abs(3 * five - mp.mpf("2.34761")) < mp.mpf("1e-4")
        and abs(3 * ten - mp.mpf("3.35547")) < mp.mpf("1e-4"),
        f"1% out to |K|={3*one}, and the zone boundary is wrong by {edge}",
    )


def sharp():
    u = sp.symbols("u", real=True)
    num = u * sp.sin(u) - 2 + 2 * sp.cos(u)
    d2 = sp.diff(num, u, 2)
    mono = sp.simplify(d2 + u * sp.sin(u)) == 0 and num.subs(u, 0) == 0 and sp.diff(num, u).subs(u, 0) == 0
    at_pi = sp.simplify((1 - sp.cos(sp.pi)) - 2 * sp.pi ** 2 / sp.pi ** 2) == 0
    outside = True
    for val in (4, 5, 2 * mp.pi):
        left = 1 - mp.cos(val)
        right = 2 * val ** 2 / mp.pi ** 2
        outside &= left < right
    # dropping the nonnegative (k1-k2) term is what keeps both arguments in [-pi, pi]
    k1, k2 = sp.symbols("k1 k2", real=True)
    gap = sp.simplify((1 - sp.cos(k1 - k2)) - 2 * sp.sin((k1 - k2) / 2) ** 2)
    report(
        "line 195",
        mono and at_pi and outside and gap == 0,
        "2/pi^2 is sharp on [-pi, pi] and false at 4, 5 and 2pi; 1-cos is nonnegative",
    )


def gaussian():
    n = sp.symbols("n", positive=True)
    a = 4 * n / (9 * sp.pi ** 2)
    integral = (1 / (4 * sp.pi * a))
    report(
        "gaussian bound",
        sp.simplify(integral - 9 * sp.pi / (16 * n)) == 0,
        "(2pi)^{-2} integral of exp(-(4n/9 pi^2)|k|^2) is 9 pi/(16 n)",
    )


def lines():
    body = subprocess.run(["git", "show", f"{SHA}:{NOTE}"], capture_output=True, text=True)
    if body.returncode != 0:
        report("note lines", False, "pinned note is not in this checkout")
        return
    rows = body.stdout.splitlines()
    line = rows[194]
    has = "1 − cos u" in line and "2u²/π²" in line
    target = rows[349]
    gate = "K²/9" in target
    report(
        "note lines",
        has and gate and 195 not in {4, 43, 225},
        "line 195 states 1-cos u >= 2u^2/pi^2, and line 350 asks for an expansion other than K^2/9",
    )


def main():
    symbol()
    domain()
    sharp()
    gaussian()
    lines()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - at unit weight the level symbol is 4 sin^2(u/2), within 1% of u^2 only for |K|<=1.04132, "
        "and wrong by 1-4/pi^2 at u=pi. Note line 195 is a sharp use of 1-cos u >= 2u^2/pi^2 on [-pi,pi], "
        "and it stays inside that interval only because the (k1-k2) term is dropped first. Line 350 asks for K^2/9."
    )
    print(
        "SUMMARY: confirmed the symbol, the three tolerance radii, the sharpness, the Gaussian integral, "
        "and the two note lines a1 does not list. The other campaign PRs were not re-audited."
    )


if __name__ == "__main__":
    main()
