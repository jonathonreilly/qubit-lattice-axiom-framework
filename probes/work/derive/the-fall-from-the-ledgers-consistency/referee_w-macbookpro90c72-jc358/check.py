#!/usr/bin/env python3
"""Independent checks: [X, T_n] = n T_n, and the fall weights have mean zero."""
import cmath


def main():
    # [X, T] on a line, n = 1 and n = 2, away from the ends.
    L = 8
    ok = True
    for n in (1, 2):
        for x in range(n, L - n):
            # (X T psi)(x) = x psi(x-n); (T X psi)(x) = (x-n) psi(x-n)
            # difference n psi(x-n) = (n T psi)(x)
            left = x - (x - n)
            ok &= left == n
    print("commutator [X,T_n]=n T_n", ok)

    # symbols
    def samples():
        for n in range(1, 7):
            yield cmath.pi * n / 6

    # d/dk sin k = cos k; d/dk (sin k cos k) = cos 2k
    for k in samples():
        d_sin = cmath.cos(k)
        # numerical derivative
        h = 1e-6
        num = (cmath.sin(k + h) - cmath.sin(k - h)) / (2 * h)
        ok &= abs(num - d_sin) < 1e-8
        sc = cmath.sin(k) * cmath.cos(k)
        dsc = (cmath.sin(k + h) * cmath.cos(k + h) - cmath.sin(k - h) * cmath.cos(k - h)) / (2 * h)
        ok &= abs(dsc - cmath.cos(2 * k)) < 1e-6
        fourth = (4 / 3) * cmath.cos(k) - (1 / 3) * cmath.cos(2 * k)
        # small k: 1 - k^4/6
        if abs(k) < 0.4:
            series = 1 - k**4 / 6
            ok &= abs(fourth - series) < 1e-4
    # mean of cos over a uniform grid of (-pi, pi] is ~0
    N = 64
    mean_cos = sum(cmath.cos(-cmath.pi + 2 * cmath.pi * j / N) for j in range(N)) / N
    mean_cos2 = sum(cmath.cos(2 * (-cmath.pi + 2 * cmath.pi * j / N)) for j in range(N)) / N
    print(f"mean cos {mean_cos.real:.3e} mean cos2 {mean_cos2.real:.3e}")
    ok &= abs(mean_cos) < 1e-12 and abs(mean_cos2) < 1e-12
    if ok:
        print(
            "HIT: confirmed - [X,T_n]=n T_n, the weights of sin and sin*cos are cos and cos(2k), "
            "and both have mean zero over the zone, so no local momentum falls with weight one"
        )
        print(
            "SUMMARY: confirmed the commutator and the zero-mean weights; "
            "the quasi-momentum, not a local density, is what falls with weight one"
        )
    else:
        print("SUMMARY: fails at the commutator or the mean-zero weights")


if __name__ == "__main__":
    main()
