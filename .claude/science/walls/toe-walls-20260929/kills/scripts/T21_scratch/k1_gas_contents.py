"""K1 (kill check, own code): the block-81/117 record gas WITH six-axis contents, heat-bath Monte Carlo.

Weight of a configuration a_x in {0 (empty), 1..6 (axes +x,-x,+y,-y,+z,-z)}:
    prod_x z^[a_x>0]  prod_bonds W(a_x,a_y),   W = 1 if an end is empty, else g*M(a_x,a_y),
    M = 6*omega/(p+q+4r),  omega = p (equal), q (opposite), r (orthogonal),  z = zeta/6 = g^-3 H / 6.
(p=q=r gives M=1 and the contentless gas = 3D Ising AF at H=1.)
Order parameter: staggered occupancy  m = (1/N) sum_x eps_x (2 n_x - 1).
Independent of the attacker's code (heat bath on 7 states, checkerboard sweeps, own neighbour tables).
"""
import sys, numpy as np
from numba import njit


@njit(cache=True)
def build_nb(L):
    N = L * L * L
    nb = np.empty((N, 6), np.int64)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = (x * L + y) * L + z
                nb[i, 0] = (((x + 1) % L) * L + y) * L + z
                nb[i, 1] = (((x - 1) % L) * L + y) * L + z
                nb[i, 2] = (x * L + (y + 1) % L) * L + z
                nb[i, 3] = (x * L + (y - 1) % L) * L + z
                nb[i, 4] = (x * L + y) * L + (z + 1) % L
                nb[i, 5] = (x * L + y) * L + (z - 1) % L
    return nb


@njit(cache=True)
def build_eps(L):
    N = L * L * L
    e = np.empty(N, np.int64)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                e[(x * L + y) * L + z] = 1 if (x + y + z) % 2 == 0 else -1
    return e


def Wmatrix(g, p, q, r):
    W = np.ones((7, 7))
    for a in range(1, 7):
        for b in range(1, 7):
            if a == b:
                om = p
            elif (a - 1) // 2 == (b - 1) // 2:
                om = q
            else:
                om = r
            W[a, b] = g * 6.0 * om / (p + q + 4 * r)
    return W


@njit(cache=True)
def run(L, W, z, ntherm, nmeas, seed, start_ordered):
    np.random.seed(seed)
    nb = build_nb(L)
    eps = build_eps(L)
    N = L * L * L
    a = np.zeros(N, np.int64)
    if start_ordered:
        for i in range(N):
            if eps[i] == 1:
                a[i] = 1 + np.random.randint(0, 6)
    else:
        for i in range(N):
            if np.random.random() < 0.5:
                a[i] = 1 + np.random.randint(0, 6)
    w = np.empty(7)
    m1 = 0.0
    m2 = 0.0
    m4 = 0.0
    rho = 0.0
    for sweep in range(ntherm + nmeas):
        for par in range(2):
            for i in range(N):
                if (1 if eps[i] == 1 else 0) != par:
                    continue
                tot = 0.0
                for s in range(7):
                    val = 1.0 if s == 0 else z
                    for k in range(6):
                        val *= W[s, a[nb[i, k]]]
                    w[s] = val
                    tot += val
                u = np.random.random() * tot
                acc = 0.0
                ch = 6
                for s in range(7):
                    acc += w[s]
                    if u < acc:
                        ch = s
                        break
                a[i] = ch
        if sweep >= ntherm:
            m = 0.0
            n = 0
            for i in range(N):
                o = 1 if a[i] > 0 else 0
                m += eps[i] * (2 * o - 1)
                n += o
            m /= N
            m1 += abs(m)
            m2 += m * m
            m4 += m ** 4
            rho += n / N
    return m1 / nmeas, m2 / nmeas, m4 / nmeas, rho / nmeas


if __name__ == "__main__":
    pass
