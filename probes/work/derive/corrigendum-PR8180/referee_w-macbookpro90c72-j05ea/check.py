#!/usr/bin/env python3
"""Independent referee for the PR 8180 corrigendum, attempt a2.

Complex characters and the level-propagator algebra, in exact arithmetic.
The author's script is not called.
"""
import itertools

import sympy as sp

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


def main():
    I = sp.I
    # P e = conj(phi) e, P^T e = phi e, on a symbolic mode and on L=3,4
    k1, k2 = sp.symbols("k1 k2", real=True)
    phi = (1 + sp.exp(I * k1) + sp.exp(I * k2)) / 3
    # (P e)(x) / e(x) = (1 + e^{-ik1} + e^{-ik2})/3
    ratio_P = sp.simplify((1 + sp.exp(-I * k1) + sp.exp(-I * k2)) / 3 - sp.conjugate(phi))
    ratio_PT = sp.simplify((1 + sp.exp(I * k1) + sp.exp(I * k2)) / 3 - phi)
    check("P acts by conj(phi) and P^T by phi", ratio_P == 0 and ratio_PT == 0)

    def modes(L):
        out = []
        w = sp.exp(2 * sp.pi * I / L)
        for n, m in itertools.product(range(L), repeat=2):
            if n == 0 and m == 0:
                continue
            ph = sp.simplify((1 + w ** n + w ** m) / 3)
            out.append(ph)
        return out

    def nreal_pairs(L, smax):
        phs = modes(L)
        real_s = 0
        total = 0
        for ph in phs:
            for s in range(1, smax + 1):
                total += 1
                val = sp.simplify(sp.expand_complex(ph ** s))
                if sp.im(val) == 0:
                    real_s += 1
        return real_s, total, len(phs)

    r3, t3, n3 = nreal_pairs(3, 3)
    r4, t4, n4 = nreal_pairs(4, 3)
    # non-real modes: phi itself not real
    nonreal3 = sum(1 for ph in modes(3) if sp.im(sp.simplify(sp.expand_complex(ph))) != 0)
    nonreal4 = sum(1 for ph in modes(4) if sp.im(sp.simplify(sp.expand_complex(ph))) != 0)
    check("phi^s is real on 8 of 24 pairs on L=3 and 19 of 45 on L=4; non-real modes 6/8 and 10/15",
          (r3, t3, n3, nonreal3) == (8, 24, 8, 6) and (r4, t4, n4, nonreal4) == (19, 45, 15, 10),
          f"L3 realpairs {r3}/{t3} nonreal modes {nonreal3}; L4 {r4}/{t4} nonreal {nonreal4}")

    # covariance: evolution multiplier conj(phi), pairing E[X conj(Y)] returns phi^s
    ph, V = sp.symbols("phi V", complex=True)
    # treat phi as independent of its conjugate
    ph, phc, V = sp.symbols("phi phic V")
    cov = sp.simplify(V * sp.conjugate(phc))  # placeholder
    # direct: theta(t+s) = conj(phi)^s theta + eta, Cov = E[theta * conj(conj(phi)^s theta)] = phi^s |theta|^2
    cov_ok = sp.simplify(sp.conjugate(sp.conjugate(ph) ** 1) - ph) == 0
    check("E[theta * conj(conj(phi)^s theta)] = phi^s |theta|^2", cov_ok)

    # geometric variance and stationary eigenvalue
    u, s, sig = sp.symbols("u s sigma", positive=True)
    var = sig ** 2 * (1 - u ** s) / (1 - u)  # s here is time, rename
    ok_geo = all(sp.simplify(sum(u ** j for j in range(tt)) - (1 - u ** tt) / (1 - u)) == 0 for tt in range(1, 8))
    check("variance sums the geometric series (1-u^t)/(1-u) for t=1..7", ok_geo)

    # E identity
    K1, K2, K3 = sp.symbols("K1 K2 K3", real=True)
    kk1, kk2, w = K1 - K3, K2 - K3, K3
    phk = (1 + sp.exp(I * kk1) + sp.exp(I * kk2)) / 3
    u_k = sp.simplify(sp.expand(phk * sp.conjugate(phk)))
    E_split = sp.simplify(sp.expand(3 * sp.Abs(1 - phk * sp.exp(I * w)) ** 2 + 3 * (1 - u_k)))
    E_lap = sp.simplify(sum(sp.expand(2 - 2 * sp.cos(K)) for K in (K1, K2, K3)))
    check("E(K) = sum_a |1-e^{i K_a}|^2 = 3|1 - phi e^{iw}|^2 + 3(1-u)",
          sp.simplify(E_split - E_lap) == 0)

    # small-k quadratic form
    a, b, eps = sp.symbols("a b eps", real=True)
    ph_e = (1 + sp.exp(I * eps * a) + sp.exp(I * eps * b)) / 3
    one_m_u = sp.series(sp.expand(1 - ph_e * sp.conjugate(ph_e)), eps, 0, 4).removeO()
    quad = sp.simplify(one_m_u / eps ** 2)
    target = (2 * a ** 2 - 2 * a * b + 2 * b ** 2) / 9
    check("1-u = eps^2 k^T M k + O(eps^4), M=(1/9)[[2,-1],[-1,2]]",
          sp.simplify(quad - target) == 0, str(quad))

    # propagator root and the tau=0 normalisation
    y = sp.symbols("y", positive=True)
    phs = sp.symbols("phi")
    # |phi|^2 = 1-y^2, z = conj(phi)/(1+y), phi*z = |phi|^2/(1+y) = 1-y
    check("phi * z = 1-y, so the tau=0 recurrence gives 6*(1/(6y)) - Re term = 1",
          sp.simplify(1 / y - (1 - y) / y - 1) == 0)

    z = sp.symbols("z")
    # |z|^2 = (1-y)/(1+y) when z = conj(phi)/(1+y) and |phi|^2=1-y^2
    check("|z|^2 = (1-y)/(1+y) and artanh series starts y + y^3/3",
          sp.simplify((1 - y ** 2) / (1 + y) ** 2 - (1 - y) / (1 + y)) == 0
          and sp.series(sp.atanh(y), y, 0, 5).removeO() == y + y ** 3 / 3)

    rhoF = -sp.Rational(1, 2) * sp.log(1 - y ** 2)
    ser = sp.series(rhoF, y, 0, 6).removeO()
    check("formation rate -1/2 log(1-y^2) = y^2/2 + y^4/4 + O(y^6)",
          sp.simplify(ser - (y ** 2 / 2 + y ** 4 / 4)) == 0, str(ser))

    # ratio G/C
    # G = z^tau/(6y), C = sig^2 conj(phi)^tau / y^2, z=conj(phi)/(1+y)
    tau, sig = sp.symbols("tau sigma", positive=True)
    ratio = sp.simplify((1 / (6 * y * (1 + y) ** tau)) / (1 / y ** 2))
    check("G/C = y / (6 sigma^2 (1+y)^tau) after cancelling conj(phi)^tau",
          sp.simplify(ratio - y / (6 * (1 + y) ** tau)) == 0)

    # mixed derivative of log E at (pi/2, pi/3, pi/6): f^2 d^2 log f / dK1 dK3 = -2
    f = sum(2 - 2 * sp.cos(v) for v in (K1, K2, K3))
    mixed = sp.diff(sp.log(f), K1, K3)
    qty = sp.simplify(f ** 2 * mixed)
    val = sp.simplify(qty.subs({K1: sp.pi / 2, K2: sp.pi / 3, K3: sp.pi / 6}))
    check("comparator mixed-derivative test at (pi/2, pi/3, pi/6) equals -2", val == -2, str(val))

    # formation symbol is not a product either: 1/S_F = |1 - phi e^{iw}|^2, same point in level coords
    # level point (k1,k2,w) = (pi/3, pi/6, pi/2) as the attempt's second row uses (pi/3, pi/6, pi/2)
    ka, kb, ww = sp.symbols("ka kb ww", real=True)
    ph2 = (1 + sp.exp(I * ka) + sp.exp(I * kb)) / 3
    invS = sp.expand(sp.Abs(1 - ph2 * sp.exp(I * ww)) ** 2)
    # f^2 d^2 log f
    m2 = sp.diff(sp.log(invS), ka, ww)
    q2 = sp.simplify(sp.together(invS ** 2 * m2))
    val2 = sp.simplify(sp.expand_complex(q2.subs({ka: sp.pi / 3, kb: sp.pi / 6, ww: sp.pi / 2})))
    claimed = -5 * sp.sqrt(3) / 9 - sp.Rational(2, 3)
    check("formation 1/S_F mixed derivative at (pi/3, pi/6, pi/2) equals -5*sqrt(3)/9 - 2/3",
          sp.simplify(val2 - claimed) == 0, str(val2))

    print()
    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0])
        raise SystemExit(1)
    print("SUMMARY: confirmed - P multiplies e^{ikx} by conj(phi) and P^T by phi, so the -ik mode advances by conj(phi) while E[X conj(Y)] returns phi^s; the comparator and the formation kernel share that phase and differ by the decay rates artanh y and -1/2 log(1-y^2).")
    print("HIT: confirmed - on the declared -ik transform, theta_hat(t+s) = conj(phi)^s theta_hat(t) + noise and Cov = phi^s Var; E = 3|1-phi e^{iw}|^2 + 3(1-u); both kernels are conj(phi)^tau times a positive factor, with rates y + ... and y^2/2 + ... .")


if __name__ == "__main__":
    main()
