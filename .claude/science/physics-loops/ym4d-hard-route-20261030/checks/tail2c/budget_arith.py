"""tail-two-step-c: exact arithmetic behind Sections 3, 4 and 8 of library/tail-two-step-c.md.

Registered before the first run.
PASS-BUDGET: 1/16 + 1/12 + 1/4 < 1/2, and with a source rate of 1/16 added, still < 1/2.
PASS-WALL: for L in LS and 1 <= n <= NMAX, with m := floor(16 + 64 (n - 1) / L): (MARGIN) for L >= 128,
  and (1/2)(n - 160)_+ >= (m - 160)_+ for L >= 512.
PASS-RATE: the labelled library's rate r_l(kappa) = kappa/4 - a_1/2 - 4 - log 2 is below kappa for every
  kappa > 0 and a_1 >= 0, which is the mismatch of defect D3. With a_0, a_1 >= 0 the sharpened rate
  (A - a_1) - a_0 - 3 - log 2 at A = 5 kappa / 4 exceeds kappa once kappa >= 4 (a_0 + a_1 + 4).
PASS-MODEL: sinh(1) / 4 < 1/3, the size of the counter-model of defect D1, from a rational bound.
FAIL: any of these false. This checks arithmetic only. It proves nothing about Yang-Mills.
"""
from fractions import Fraction as Fr
from math import floor
import resource, sys

LS = [128, 129, 511, 512, 513, 1025, 4097]
NMAX = 60000


def pos(x):
    return x if x > 0 else 0


def budget():
    base = Fr(1, 16) + Fr(1, 12) + Fr(1, 4)
    src = base + Fr(1, 16)
    print("budget", base, "left", Fr(1, 2) - base, "| with source", src, "left", Fr(1, 2) - src)
    return base < Fr(1, 2) and src < Fr(1, 2)


def wall():
    ok = True
    for L in LS:
        for n in range(1, NMAX + 1):
            m = floor(16 + Fr(64 * (n - 1), L))
            if L >= 128:
                if n <= 169 and m > 100:
                    ok = False; print("MARGIN small", L, n, m)
                if n >= 170 and pos(n - 160) - pos(m - 160) < 10 + Fr(n - 170, 2):
                    ok = False; print("MARGIN large", L, n, m)
            if L >= 512 and Fr(pos(n - 160), 2) < pos(m - 160):
                ok = False; print("HALF", L, n, m)
    print("wall", ok)
    return ok


def rate():
    # r_l(kappa) - kappa = -3 kappa / 4 - a_1 / 2 - 4 - log 2 < 0 for kappa > 0, a_1 >= 0: all terms negative.
    a = -Fr(3, 4)
    # sharpened: 5 kappa / 4 - a_1 - a_0 - 3 - log 2 - kappa = kappa / 4 - a_0 - a_1 - 3 - log 2,
    # and log 2 < 1, so kappa >= 4 (a_0 + a_1 + 4) suffices.
    b = Fr(5, 4) - 1
    print("rate slopes: r_l - kappa", a, "; sharpened - kappa", b)
    return a < 0 and b > 0


def model():
    # sinh(1) = sum 1/(2j+1)!, tail after j = 4 below 2 / 11!
    s = Fr(0)
    f = 1
    for j in range(0, 5):
        if j > 0:
            f *= (2 * j) * (2 * j + 1)
        s += Fr(1, f)
    ub = s + Fr(2, 39916800)
    print("sinh(1) <=", float(ub), " /4 =", float(ub / 4))
    return ub / 4 < Fr(1, 3)


def main():
    r = [budget(), wall(), rate(), model()]
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print("maxrss (bytes on darwin)", rss)
    if rss > 2 * 1024 ** 3:
        sys.exit("over 2 GB")
    print("PASS" if all(r) else "FAIL", r)


if __name__ == "__main__":
    main()
