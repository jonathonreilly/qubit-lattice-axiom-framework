#!/usr/bin/env python3
"""Exact two-dimensional analogue of the interior estimate (criteria I1-I3)."""
import mpmath as mp

mp.mp.dps = 700


def osc(n, tau):
    beta = mp.mpf(n) / mp.mpf(tau)
    # truncation must beat Z_n(pi) ~ exp(-pi^2/(2 tau)), so l^2 tau/2 >= pi^2/(2 tau) + margin
    lmax = int(mp.ceil(mp.sqrt(mp.pi**2 / mp.mpf(tau)**2 + 200 / mp.mpf(tau)))) + 8
    I = [mp.besseli(l, beta) for l in range(0, lmax + 2)]
    # l = 2j+1 ; b_l proportional to I_l(beta); use ratios to l = 1
    rho = {}
    dlog = {}
    for l in range(1, lmax + 1):
        ratio = I[l] / I[1]
        rho[l] = ratio ** n
        # d/dbeta log(I_l) = I_{l-1}/I_l - l/beta
        dlog[l] = (I[l - 1] / I[l] - l / beta) - (I[0] / I[1] - 1 / beta)

    def chi(l, theta):
        # chi_j(theta) with l = 2j+1: sin(l theta)/sin(theta); at theta -> 0 equals l; at pi (-1)^(l-1) l
        if theta == 0:
            return mp.mpf(l)
        if theta == mp.pi:
            return (-1) ** (l - 1) * mp.mpf(l)
        return mp.sin(l * theta) / mp.sin(theta)

    def excess(theta):
        # E[s_p|theta] up to a theta independent constant: -(1/n) d/dbeta log Z_n(theta)
        # = -sum_l weight_l(theta) dlog_l (with the common -d/dbeta log b_1 removed)
        num = sum(l * rho[l] * chi(l, theta) * dlog[l] for l in range(1, lmax + 1))
        den = sum(l * rho[l] * chi(l, theta) for l in range(1, lmax + 1))
        return -num / den

    base = excess(mp.mpf(0))
    best = mp.mpf(0)
    for k in range(1, 41):
        theta = mp.pi * k / 40
        val = excess(theta) - base
        if abs(val) > abs(best):
            best = val
    return best


def main():
    taus = [0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
    ns = [10**2, 10**3, 10**4, 10**5]
    print("n^2 * osc, rows tau, columns n =", ns)
    for tau in taus:
        row = []
        for n in ns:
            row.append(float(n * n * osc(n, tau)))
        print(f"tau={tau:<5} " + " ".join(f"{x:12.6f}" for x in row))
    print("pi^2/2 =", float(mp.pi**2 / 2))


if __name__ == "__main__":
    main()
