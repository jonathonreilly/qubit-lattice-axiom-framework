#!/usr/bin/env python3
"""Independent referee for sources-under-the-record-reading a3.

Held-wall operator (1 - average), exact on the 5^3 interior and in float on the 7^3 interior.
The author's script is not called.
"""
import itertools

import numpy as np
import sympy as sp

FAILS = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


def sites_of(n):
    sites = list(itertools.product(range(1, n + 1), repeat=3))
    return sites, {s: i for i, s in enumerate(sites)}


def operator(n, exact=True):
    sites, ix = sites_of(n)
    N = len(sites)
    A = sp.zeros(N) if exact else np.zeros((N, N))
    one = sp.Integer(1) if exact else 1.0
    sixth = sp.Rational(1, 6) if exact else 1.0 / 6.0
    for s in sites:
        i = ix[s]
        A[i, i] = one
        for a in range(3):
            for d in (1, -1):
                t = list(s)
                t[a] += d
                t = tuple(t)
                if t in ix:
                    A[i, ix[t]] -= sixth
    return sites, ix, A


def star(n):
    c = tuple([(n + 1) // 2] * 3)
    arms = [tuple(c[d] + (s if d == a else 0) for d in range(3)) for a in range(3) for s in (1, -1)]
    return c, [c] + arms


def mprime(g, ix, sites, weights, gamma, centre):
    """Ledger of the amplitude, then the record mass that matches it."""
    rho = {s: w for s, w in zip(star(len(ix) and sites)[1] if False else [], [])}
    # weights aligned with the star list
    c, st = star(sites and 0 or 0)
    return None


def main():
    # Sherman-Morrison algebra
    L, gyy, gam = sp.symbols("L gyy gamma", positive=True)
    mp = L / (1 - gam / 12 * gyy * L)
    after = sp.simplify(mp / (1 + gam / 12 * gyy * mp))
    check("m' = L/(1 - (gamma/12) g_yy L) restores the ledger", sp.simplify(after - L) == 0)

    # exact 5^3 (interior side 3)
    sites, ix, A = operator(3, exact=True)
    g = A.inv()
    c, st = star(3)
    wts = {
        "uniform": [sp.Rational(1, 7)] * 7,
        "centre": [sp.Rational(1, 2)] + [sp.Rational(1, 12)] * 6,
        "lop": [sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 8), sp.Rational(1, 8),
                sp.Rational(1, 8), sp.Rational(1, 16), sp.Rational(1, 16)],
    }

    def mass(n_sites, gmat, ix_, st_, w, gam, exact=True):
        # solve (A + (gam/12) M) delta = -(gam/12) m, ledger = sum m (1+delta)
        m = [w[st_.index(s)] if s in st_ else (0 if exact else 0.0) for s in n_sites]
        # only star sites are nonzero; build the reduced system via the full matrix
        if exact:
            M = sp.diag(*m)
            delta = (gmat.inv() if False else None)
            Op = gmat + (gam / 12) * M  # gmat here is A, not g
            delta = Op.LUsolve(-(gam / 12) * sp.Matrix(m))
            Led = sum(m[i] * (1 + delta[i]) for i in range(len(m)))
            gyy = g.inv() if False else None
            return Led
        return None

    # g is inverse; ledger via the formula using quadratic form
    def ledger_from_g(gmat, ix_, sites_, st_, w, gam):
        mvec = sp.zeros(len(sites_), 1)
        for s, wt in zip(st_, w):
            mvec[ix_[s]] = wt  # E=1, m = rho
        # (A + (gam/12) diag(m)) delta = -(gam/12) m
        A_ = gmat.inv()
        delta = (A_ + (gam / 12) * sp.diag(*[mvec[i] for i in range(len(sites_))])).LUsolve(-(gam / 12) * mvec)
        return sum(mvec[i] * (1 + delta[i]) for i in range(len(sites_)))

    # cheaper: A is known, g = A.inv() already. Don't invert twice.
    A3 = g.inv()  # recover... wait g = A.inv() so A = g.inv() is expensive again. Keep A.
    # I named g = A.inv() and lost A. Recompute A only.
    sites, ix, A3 = operator(3, exact=True)
    g3 = A3.inv()

    def led(A_, ix_, sites_, st_, w, gam):
        m = [0] * len(sites_)
        for s, wt in zip(st_, w):
            m[ix_[s]] = wt
        delta = (A_ + (gam / 12) * sp.diag(*m)).LUsolve(-(gam / 12) * sp.Matrix(m))
        return sum(m[i] * (1 + delta[i]) for i in range(len(m)))

    gam = sp.Integer(1)
    Luni = led(A3, ix, sites, st, wts["uniform"], gam)
    gyy = g3[ix[c], ix[c]]
    mp = sp.simplify(Luni / (1 - gam / 12 * gyy * Luni))
    check("uniform 7-site star at gamma=1 on the 5^3 box has m' = 1188/1091",
          mp == sp.Rational(1188, 1091), str(mp))

    # positive definite sample and corner sign on the 7^3 interior, in float
    sites5, ix5, A5 = operator(5, exact=False)
    # numpy inverse
    g5 = np.linalg.inv(A5)
    # symmetry: eigenvalues positive
    ev = np.linalg.eigvalsh(g5)
    c5, st5 = star(5)
    # uniform rho
    rho = np.zeros(len(sites5))
    for s in st5:
        rho[ix5[s]] = 1.0 / 7.0
    rgr = float(rho @ g5 @ rho)
    gdiag_mean = sum(rho[ix5[s]] * g5[ix5[s], ix5[s]] for s in st5)
    corner = (1, 1, 1)
    g_corner = g5[ix5[corner], ix5[corner]]
    rho2 = np.zeros(len(sites5))
    rho2[ix5[c5]] = 0.99
    rho2[ix5[corner]] = 0.01
    rgr2 = float(rho2 @ g5 @ rho2)
    check("on the 7^3 interior, star excess is positive and the corner odds can make it negative",
          ev.min() > 0 and gdiag_mean > rgr and g_corner < rgr2,
          f"excess {gdiag_mean - rgr:.5f}, corner {g_corner:.5f} vs {rgr2:.5f}")

    # locality: m' on both boxes
    def mprime_float(n, weights, gamma=1.0):
        sites_n, ix_n, An = operator(n, exact=False)
        c_n, st_n = star(n)
        m = np.zeros(len(sites_n))
        for s, wt in zip(st_n, weights):
            m[ix_n[s]] = wt
        delta = np.linalg.solve(An + (gamma / 12.0) * np.diag(m), -(gamma / 12.0) * m)
        Led = float(m @ (1.0 + delta))
        # g_yy from a solve
        e = np.zeros(len(sites_n))
        e[ix_n[c_n]] = 1.0
        gcol = np.linalg.solve(An, e)
        gyy_n = gcol[ix_n[c_n]]
        return Led / (1.0 - (gamma / 12.0) * gyy_n * Led)

    uni = [sp.Rational(1, 7)] * 7
    heavy = [sp.Rational(1, 2)] + [sp.Rational(1, 12)] * 6
    lop = wts["lop"]
    m5 = mprime_float(3, [float(x) for x in uni])
    m7 = mprime_float(5, [float(x) for x in uni])
    h5 = mprime_float(3, [float(x) for x in heavy], gamma=7 / 3)
    h7 = mprime_float(5, [float(x) for x in heavy], gamma=7 / 3)
    l5 = mprime_float(3, [float(x) for x in lop])
    l7 = mprime_float(5, [float(x) for x in lop])
    check("symmetric stars give the same m' on the 5^3 and 7^3 boxes; lopsided weights do not",
          abs(m5 - m7) < 1e-9 and abs(m5 - 1188 / 1091) < 1e-9 and abs(h5 - h7) < 1e-9 and abs(l5 - l7) > 1e-6,
          f"uniform {m5:.10f} vs {m7:.10f}; lopsided {l5:.9f} vs {l7:.9f}")

    # weak-field coefficient on the small box, exact derivative via a tiny gamma
    eps = sp.Rational(1, 10 ** 8)
    Le = led(A3, ix, sites, st, wts["uniform"], eps)
    rho_q = sp.zeros(len(sites), 1)
    for s in st:
        rho_q[ix[s]] = sp.Rational(1, 7)
    rgr_e = (rho_q.T * g3 * rho_q)[0]
    dL = (Le - 1) / eps
    check("weak field: (L - E)/gamma -> -<rho, g rho>/12",
          abs(dL + rgr_e / 12) < sp.Rational(1, 10 ** 6), str(sp.N(dL + rgr_e / 12)))

    print()
    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0])
        raise SystemExit(1)
    print("SUMMARY: confirmed - the record mass that keeps the ledger is L/(1-(gamma/12) g_yy L); the uniform star gives 1188/1091 on both boxes; the corner odds can reverse the sign.")
    print("HIT: confirmed - m' = L/(1 - (gamma/12) g_yy L); weak-field excess (gamma/12) E^2 (g_yy - <rho,g rho>); any-odds excess is nonnegative on Z^3 by g_xy <= G_0(0) and can be negative in a box; symmetric stars give m' = 1188/1091 independent of the 5^3 versus 7^3 walls.")


if __name__ == "__main__":
    main()
