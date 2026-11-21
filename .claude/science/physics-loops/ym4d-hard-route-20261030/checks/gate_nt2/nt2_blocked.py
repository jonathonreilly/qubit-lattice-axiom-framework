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
        E[mu] = np.fft.irfftn(h, s=(N, N, N, N), axes=(0, 1, 2, 3))
    return E


def kvert(Es):
    """Sum over all plaquettes of V_p, b1=(x,m), b2=(x+m,n), b3=(x+n,m) reversed, b4=(x,n) reversed."""
    tot = 0.0
    signs = [1, 1, -1, -1]
    for m in range(4):
        for nn in range(m + 1, 4):
            e = []
            pm = []
            for E in Es:
                em = E[m]
                en = E[nn]
                b2 = np.roll(en, -1, axis=m)
                b3 = np.roll(em, -1, axis=nn)
                pm.append(em + b2 - b3 - en)
                e.append([em, b2, b3, en])
            for s in range(4):
                for t in range(s + 1, 4):
                    sg = signs[s] * signs[t]
                    b = [e[i][s] for i in range(3)]
                    c = [e[i][t] for i in range(3)]
                    v0 = float(np.vdot(pm[0], b[1] * c[2] - b[2] * c[1]))
                    v1 = float(np.vdot(pm[1], b[0] * c[2] - b[2] * c[0]))
                    v2 = float(np.vdot(pm[2], b[0] * c[1] - b[1] * c[0]))
                    tot += sg * (v0 - v1 + v2)
            del e, pm
            check_rss()
    return 12 * tot


def run(n, S):
    N = n * S
    Es = []
    P11 = P12 = None
    J0 = None
    for k, (mu, nu) in enumerate([(0, 1), (1, 2), (2, 0)]):
        J = fine_current(N, n, corner(mu, nu))
        E = inv_laplace(J, N)
        Es.append(E)
        if k == 0:
            P11 = float(np.vdot(J, E))
            J0 = J
        if k == 1:
            P12 = float(np.vdot(J0, E))
            J0 = None
        del J
        check_rss()
    kv = float(kvert(Es))
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9
    return {"n": n, "S": S, "N": N, "P11": P11, "P12": P12, "K_vert": kv, "rss_gb": round(rss, 3)}


if __name__ == "__main__":
    n, S = int(sys.argv[1]), int(sys.argv[2])
    r = run(n, S)
    print(json.dumps(r), flush=True)
    with open(__file__.replace("nt2_blocked.py", "nt2_blocked.jsonl"), "a") as f:
        f.write(json.dumps(r) + "\n")
