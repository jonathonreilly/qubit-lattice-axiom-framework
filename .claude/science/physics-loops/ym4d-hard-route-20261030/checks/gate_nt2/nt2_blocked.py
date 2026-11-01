#!/usr/bin/env python3
"""C4 of CRITERIA.md: K_vert(n, S) for the block B-1, Feynman prescription, formula (B-6).

Periodic fine lattice of side N = n S. E_i = (-Delta)^-1 J_i^fine, zero mode removed.
K_vert = 12 sum_p sum_(s<t) eps_s eps_t det[((dE_i)_p, E_i(b_s), E_i(b_t))].
"""
import json
import resource
import sys

import numpy as np

RSS_LIMIT_BYTES = 2 * 10**9


def check_rss():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > RSS_LIMIT_BYTES:
        sys.exit("RSS limit reached")


def block_weight_1d(N, n, mu_dir):
    """1D factors of the fine current of one coarse link in direction mu located at coarse origin.

    (Q_n A)_mu(0) = n^-4 sum_(x in B_n) sum_(s=0..n-1) A_mu(x + s e_mu).
    Along mu: convolution of box(n) centred with box(n) one-sided. Transverse: box(n) centred.
    """
    tr = np.zeros(N)
    for x in range(-(n - 1) // 2, (n - 1) // 2 + 1):
        tr[x % N] += 1.0 / n
    al = np.zeros(N)
    for x in range(-(n - 1) // 2, (n - 1) // 2 + 1):
        for s in range(n):
            al[(x + s) % N] += 1.0 / n
    return tr, al


def fine_current(N, n, coarse_path):
    """coarse_path: list of (y, mu, eps), y coarse site tuple. Returns array J[mu, x...]."""
    J = np.zeros((4, N, N, N, N))
    tr, al = block_weight_1d(N, n, 0)
    for y, mu, eps in coarse_path:
        fac = []
        for nu in range(4):
            v = al if nu == mu else tr
            fac.append(np.roll(v, n * y[nu]))
        J[mu] += eps * np.einsum("i,j,k,l->ijkl", *fac, optimize=True)
    return J


def corner(mu, nu):
    e = lambda m: tuple(1 if i == m else 0 for i in range(4))
    o = (0, 0, 0, 0)
    return [(o, mu, 1), (e(mu), nu, 1), (e(nu), mu, -1), (o, nu, -1)]


def inv_laplace(J, N):
    k = 2 * np.pi * np.fft.fftfreq(N)
    s2 = 4 * np.sin(k / 2) ** 2
    rk = 2 * np.pi * np.fft.rfftfreq(N)
    rs2 = 4 * np.sin(rk / 2) ** 2
    lam = s2[:, None, None, None] + s2[None, :, None, None] + s2[None, None, :, None] + rs2[None, None, None, :]
    lam[0, 0, 0, 0] = 1.0
    E = np.zeros_like(J)
    for mu in range(4):
        h = np.fft.rfftn(J[mu])
        h /= lam
        h[0, 0, 0, 0] = 0.0
        E[mu] = np.fft.irfftn(h, s=(N, N, N, N))
    return E


def kvert(Es):
    """Sum over all plaquettes of V_p with links b1=(x,m), b2=(x+m,n), b3=(x+n,m) rev, b4=(x,n) rev."""
    tot = 0.0
    for m in range(4):
        for nn in range(m + 1, 4):
            e = []
            pm = []
            for E in Es:
                em = E[m]
                en = E[nn]
                b1 = em
                b2 = np.roll(en, -1, axis=m)
                b3 = np.roll(em, -1, axis=nn)
                b4 = en
                P = b1 + b2 - b3 - b4
                # signed edge values eps_s E(b_s)
                e.append([b1, b2, -b3, -b4])
                pm.append(P)
            del P
            for s in range(4):
                for t in range(s + 1, 4):
                    # det of 3x3 with rows i, columns (P_i, E_i(s), E_i(t)), signs included
                    a = [pm[i] for i in range(3)]
                    b = [e[i][s] for i in range(3)]
                    c = [e[i][t] for i in range(3)]
                    det = (a[0] * (b[1] * c[2] - b[2] * c[1])
                           - a[1] * (b[0] * c[2] - b[2] * c[0])
                           + a[2] * (b[0] * c[1] - b[1] * c[0]))
                    tot += det.sum()
            check_rss()
    return 12 * tot


def run(n, S):
    N = n * S
    Js = [fine_current(N, n, corner(0, 1)), fine_current(N, n, corner(1, 2)), fine_current(N, n, corner(2, 0))]
    Es = [inv_laplace(J, N) for J in Js]
    P11 = float(np.sum(Js[0] * Es[0]))
    P12 = float(np.sum(Js[0] * Es[1]))
    kv = kvert(Es)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9
    return {"n": n, "S": S, "N": N, "P11": P11, "P12": P12, "K_vert": kv, "rss_gb": round(rss, 3)}


if __name__ == "__main__":
    out = []
    plan = [(1, 8), (1, 16), (1, 24), (3, 8), (3, 12), (3, 16), (5, 8), (5, 10), (5, 12)]
    for n, S in plan:
        r = run(n, S)
        print(r, flush=True)
        out.append(r)
        with open(__file__.replace("nt2_blocked.py", "nt2_blocked.json"), "w") as f:
            json.dump(out, f, indent=1)
