#!/usr/bin/env python3
"""Independent check of the block 34 multiplier convention."""
import cmath
import itertools


def phi(k1, k2):
    return (1 + cmath.exp(1j * k1) + cmath.exp(1j * k2)) / 3


def phi_c(k1, k2):
    return (1 + cmath.exp(-1j * k1) + cmath.exp(-1j * k2)) / 3


def apply_P(theta, L):
    out = [0j] * (L * L)
    for x1, x2 in itertools.product(range(L), repeat=2):
        acc = theta[x1 * L + x2]
        acc += theta[((x1 - 1) % L) * L + x2]
        acc += theta[x1 * L + ((x2 - 1) % L)]
        out[x1 * L + x2] = acc / 3
    return out


def hat(theta, L, k1, k2, sign):
    s = 0j
    for x1, x2 in itertools.product(range(L), repeat=2):
        s += cmath.exp(sign * 1j * (k1 * x1 + k2 * x2)) * theta[x1 * L + x2]
    return s / L


def main():
    ok = True
    # algebraic difference
    for n1, n2, L in itertools.product(range(6), range(6), (3, 4, 5)):
        k1, k2 = 2 * cmath.pi * n1 / L, 2 * cmath.pi * n2 / L
        diff = phi(k1, k2) - phi_c(k1, k2)
        pred = (2j / 3) * (cmath.sin(k1) + cmath.sin(k2))
        ok &= abs(diff - pred) < 1e-12
        ok &= abs(abs(phi(k1, k2)) - abs(phi_c(k1, k2))) < 1e-12
    # |phi|^2 identity
    for n1, n2 in itertools.product(range(5), repeat=2):
        k1, k2 = 2 * cmath.pi * n1 / 5, 2 * cmath.pi * n2 / 5
        u = (3 + 2 * cmath.cos(k1) + 2 * cmath.cos(k2) + 2 * cmath.cos(k1 - k2)) / 9
        ok &= abs(abs(phi(k1, k2)) ** 2 - u) < 1e-12
    # direct transform on L=3: P-hat = phi_c * hat for the minus convention
    L = 3
    theta = [complex(x1 + 2 * x2, x1 * x2) for x1, x2 in itertools.product(range(L), repeat=2)]
    Pth = apply_P(theta, L)
    agree = 0
    for n1, n2 in itertools.product(range(L), repeat=2):
        k1, k2 = 2 * cmath.pi * n1 / L, 2 * cmath.pi * n2 / L
        h = hat(theta, L, k1, k2, -1)
        hp = hat(Pth, L, k1, k2, -1)
        ok &= abs(hp - phi_c(k1, k2) * h) < 1e-9
        if abs(cmath.sin(k1) + cmath.sin(k2)) < 1e-12:
            agree += 1
            ok &= abs(hp - phi(k1, k2) * h) < 1e-9
    # L=3: modes with sin k1+sin k2=0 are n1+n2 ≡ 0 mod 3: (0,0),(1,2),(2,1) = 3 of 9
    ok &= agree == 3
    # L=2: every mode agrees
    L = 2
    bad = 0
    for n1, n2 in itertools.product(range(L), repeat=2):
        k1, k2 = 2 * cmath.pi * n1 / L, 2 * cmath.pi * n2 / L
        if abs(phi(k1, k2) - phi_c(k1, k2)) > 1e-12:
            bad += 1
    ok &= bad == 0
    print(f"L=3 agreeing modes {agree}/9; L=2 disagreements {bad}")
    if ok:
        print(
            "HIT: confirmed - with theta-hat using e^{-ikx}, P multiplies by "
            "(1+e^{-ik1}+e^{-ik2})/3; the note's phi is the conjugate and agrees only when sin k1+sin k2=0"
        )
        print(
            "SUMMARY: confirmed the corrigendum: phi and phi_c differ by (2i/3)(sin k1+sin k2), "
            "have equal modulus, and the stated formula holds for every field only for L<=2"
        )
    else:
        print("SUMMARY: fails at the multiplier identity")


if __name__ == "__main__":
    main()
