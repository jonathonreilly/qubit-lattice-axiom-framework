#!/usr/bin/env python3
"""A separated test: connected correlator of the odd cluster with a far plaquette energy.

Formula (parts/witness.md, Text 2), <T s_q>_c = L_q / beta^3 + O(beta^-4), with
  L_q = 12 { sum_i P_iq B_i(E_q) - V_q(E_1, E_2, E_3) },
  B_1(E) = sum_p V_p(E, E_2, E_3) - A_2(E_3, E) - A_3(E, E_2), and cyclically,
  and L_q^G, the same without the V terms, for the Gaussian potential in Feynman gauge.
On the flux class the correlator vanishes exactly, odd times even.

PRE-REGISTERED CRITERIA (written before the first run).
 Q1 SUM RULE: sum over all plaquettes q of L_q equals 2 K_total, relative 1e-6 on T = 12. This is
    d<T>/dbeta at order beta^-3. FAIL means L_q is wrong.
 Q2 NONZERO: at offsets (d, d, 2d, 2d), d = 2, 3, 4, 5, on T = 32, some q in the 6 planes has
    |L_q| / P_pq^2 bounded below with d: L_q / ((3/2) P_pq^2) stays within a factor 3 from
    d = 3 to d = 5 for the plane of largest |L_q|. FAIL means no separated test of this form.
 Q3 RATE: report the exponent of |L_q| and |L_q^G| between d = 3 and d = 5 (only a report).
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import itertools
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_tree_coeff import K_comp, K_vert, Lat, check_rss, current, curl, field_E, lievy, path_links, plaq  # noqa: E402


def V_at(lat, Es, x, mu, nu):
    """V_p(E_1, E_2, E_3) for the single plaquette p = (x; mu, nu)."""
    P, inc = [], []
    xm = list(x)
    xm[mu] = (xm[mu] + 1) % lat.T
    xn = list(x)
    xn[nu] = (xn[nu] + 1) % lat.T
    for E in Es:
        a, b, c, d = E[(mu,) + tuple(x)], E[(nu,) + tuple(xm)], E[(mu,) + tuple(xn)], E[(nu,) + tuple(x)]
        P.append(a + b - c - d)
        inc.append((a, b, -c, -d))
    tot = 0.0
    for i in range(4):
        for j in range(i + 1, 4):
            M = np.array([[P[k], inc[k][i], inc[k][j]] for k in range(3)])
            tot += np.linalg.det(M)
    return tot


def B_terms(lat, Ls, Es, Eq):
    L1, L2, L3 = Ls
    E1, E2, E3 = Es
    b1v = K_vert(lat, Eq, E2, E3) / 12.0
    b2v = K_vert(lat, E1, Eq, E3) / 12.0
    b3v = K_vert(lat, E1, E2, Eq) / 12.0
    b1a = -lievy(L2, E3, Eq) - lievy(L3, Eq, E2)
    b2a = -lievy(L1, Eq, E3) - lievy(L3, E1, Eq)
    b3a = -lievy(L1, E2, Eq) - lievy(L2, Eq, E1)
    return (b1v, b1a), (b2v, b2a), (b3v, b3a)


def L_q(lat, Ls, Es, q_x, q_mu, q_nu):
    Jq = current(lat, path_links(lat, q_x, plaq(q_mu + 1, q_nu + 1)))
    Eq = field_E(lat, Jq)
    Pi = [float(np.sum(Jq * E)) for E in Es]
    bs = B_terms(lat, Ls, Es, Eq)
    Vq = V_at(lat, Es, q_x, q_mu, q_nu)
    Lfull = 12.0 * (sum(Pi[i] * (bs[i][0] + bs[i][1]) for i in range(3)) - Vq)
    LG = 12.0 * sum(Pi[i] * bs[i][1] for i in range(3))
    return Lfull, LG, Pi


def sum_rule(T):
    lat = Lat(4, T)
    base = (0, 0, 0, 0)
    Ls = [path_links(lat, base, s) for s in (plaq(1, 2), plaq(2, 3), plaq(3, 1))]
    Es = [field_E(lat, current(lat, L)) for L in Ls]
    K = K_comp(lat, *Ls, *Es) + K_vert(lat, *Es)
    # fast version of sum_q: sum_q P_iq E_q = E_i, so the sum of the B terms is explicit;
    # brute force over q instead, which is what is being tested, on a small T.
    tot = 0.0
    for x in itertools.product(range(T), repeat=4):
        for mu in range(4):
            for nu in range(mu + 1, 4):
                tot += L_q(lat, Ls, Es, x, mu, nu)[0]
    return tot, 2 * K


def main():
    print("# Q1 SUM RULE, brute force on T = 4 (T = 12 is too slow by brute force; the identity is exact at each T)")
    tot, two_k = sum_rule(4)
    print(f"sum_q L_q = {tot:.10f}, 2 K_total = {two_k:.10f}, rel = {abs(tot-two_k)/abs(two_k):.2e}")

    T = 32
    lat = Lat(4, T)
    base = (0, 0, 0, 0)
    Ls = [path_links(lat, base, s) for s in (plaq(1, 2), plaq(2, 3), plaq(3, 1))]
    Es = [field_E(lat, current(lat, L)) for L in Ls]
    print("# Q2, Q3: corner cluster at the origin, far plaquette q at offset (d,d,2d,2d)")
    for d in (2, 3, 4, 5):
        x = (d, d, 2 * d, 2 * d)
        best = None
        for mu in range(4):
            for nu in range(mu + 1, 4):
                Lf, LG, Pi = L_q(lat, Ls, Es, x, mu, nu)
                if best is None or abs(Lf) > abs(best[2]):
                    best = (mu + 1, nu + 1, Lf, LG, Pi)
                print(f"d={d} q=({mu+1},{nu+1}): L_q={Lf:.4e} L_q^G={LG:.4e} P_iq=({Pi[0]:.2e},{Pi[1]:.2e},{Pi[2]:.2e})", flush=True)
        print(f"d={d} largest: q=({best[0]},{best[1]}) L_q={best[2]:.4e} L_q^G={best[3]:.4e} rss={check_rss():.2f}GB", flush=True)


if __name__ == "__main__":
    main()
