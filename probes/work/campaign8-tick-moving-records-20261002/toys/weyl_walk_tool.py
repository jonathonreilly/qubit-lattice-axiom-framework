#!/usr/bin/env python3
"""Verification tool for ticked single-particle steps U(k) (2x2) on the Brillouin 3-torus.

Computes, independently of any construction's own claims:
  * band touchings (nodes): points where the two eigenvalues of U(k) coincide, and their quasi-energy E* (lambda = e^{-iE});
  * the chirality of each node: Chern number of the band just ABOVE the touching (in quasi-energy, mod 2 pi) through a
    small cube around the node (Fukui-Hatsugai-Suzuki link variables, gauge invariant, outward orientation);
  * the 3D winding number W3 = (1/24 pi^2) Int eps^{ijk} Tr[(U^-1 d_i U)(U^-1 d_j U)(U^-1 d_k U)] d^3k (central differences).
usage: python3 weyl_walk_tool.py  (runs the self-tests)"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import itertools
import numpy as np
from scipy.optimize import minimize
from scipy.linalg import expm

s0 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
SIG = (sx, sy, sz)
TWO_PI = 2 * np.pi


def quasi(U):
    lam = np.linalg.eigvals(U)
    return np.mod(-np.angle(lam), TWO_PI)


def gap(U):
    lam = np.linalg.eigvals(U)
    return abs(lam[0] - lam[1])


def find_nodes(Uf, n=40, tol=1e-6):
    ks = np.arange(n) * TWO_PI / n
    G = np.empty((n, n, n))
    for i, j, l in itertools.product(range(n), repeat=3):
        G[i, j, l] = gap(Uf(np.array([ks[i], ks[j], ks[l]])))
    cands = []
    for i, j, l in itertools.product(range(n), repeat=3):
        g = G[i, j, l]
        nb = [G[(i + a) % n, (j + b) % n, (l + c) % n] for a, b, c in itertools.product((-1, 0, 1), repeat=3) if (a, b, c) != (0, 0, 0)]
        if g <= min(nb) and g < 0.5:
            cands.append(np.array([ks[i], ks[j], ks[l]]))
    nodes = []
    for k0 in cands:
        r = minimize(lambda k: gap(Uf(k)) ** 2, k0, method="Nelder-Mead", options={"xatol": 1e-11, "fatol": 1e-22, "maxiter": 20000})
        k = np.mod(r.x, TWO_PI)
        if gap(Uf(k)) < tol and not any(np.linalg.norm(np.mod(k - q + np.pi, TWO_PI) - np.pi) < 1e-4 for q in nodes):
            nodes.append(k)
    return nodes


def upper_vec(U, Estar):
    """eigenvector of the band whose quasi-energy lies just above Estar (smallest positive offset mod 2 pi)."""
    lam, V = np.linalg.eig(U)
    E = np.mod(-np.angle(lam), TWO_PI)
    off = np.mod(E - Estar, TWO_PI)
    idx = int(np.argmin(off))
    v = V[:, idx]
    return v / np.linalg.norm(v)


def chirality(Uf, k0, h=1e-3, m=8):
    Estar = float(np.mean(quasi(Uf(k0))))
    lam = np.exp(-1j * quasi(Uf(k0)))
    Estar = float(np.mod(-np.angle(lam.mean()), TWO_PI))
    total = 0.0
    # six faces of the cube [-h,h]^3 around k0, each with outward normal; parametrize (u,v) with u x v = outward normal
    faces = []
    for ax in range(3):
        for sgn in (+1, -1):
            a, b = [x for x in range(3) if x != ax]
            # orientation: e_a x e_b = +e_ax for (a,b) cyclic after ax
            if (ax, a, b) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
                ua, ub = a, b
            else:
                ua, ub = b, a
            if sgn < 0:
                ua, ub = ub, ua
            faces.append((ax, sgn, ua, ub))
    grid = np.linspace(-h, h, m + 1)
    for ax, sgn, ua, ub in faces:
        vecs = np.empty((m + 1, m + 1, 2), dtype=complex)
        for i, u in enumerate(grid):
            for j, v in enumerate(grid):
                k = np.array(k0, dtype=float)
                k[ax] += sgn * h
                k[ua] += u
                k[ub] += v
                vecs[i, j] = upper_vec(Uf(k), Estar)
        for i in range(m):
            for j in range(m):
                l1 = np.vdot(vecs[i, j], vecs[i + 1, j])
                l2 = np.vdot(vecs[i + 1, j], vecs[i + 1, j + 1])
                l3 = np.vdot(vecs[i + 1, j + 1], vecs[i, j + 1])
                l4 = np.vdot(vecs[i, j + 1], vecs[i, j])
                total += np.angle(l1 * l2 * l3 * l4)
    return total / TWO_PI, Estar


def winding(Uf, n=48):
    ks = np.arange(n) * TWO_PI / n
    d = TWO_PI / n
    tot = 0.0
    perms = [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]
    for i, j, l in itertools.product(range(n), repeat=3):
        k = np.array([ks[i], ks[j], ks[l]])
        U = Uf(k)
        Ui = U.conj().T
        A = []
        for ax in range(3):
            e = np.zeros(3)
            e[ax] = d / 2
            A.append(Ui @ (Uf(k + e) - Uf(k - e)) / d)
        acc = 0.0
        for (a, b, c), sg in perms:
            acc += sg * np.trace(A[a] @ A[b] @ A[c])
        tot += acc
    return (tot * d ** 3 / (24 * np.pi ** 2))


def report(name, Uf, n_nodes=40, n_w=40):
    nodes = find_nodes(Uf, n=n_nodes)
    print("== %s: %d nodes" % (name, len(nodes)))
    byE = {}
    for k in nodes:
        ch, E = chirality(Uf, k)
        key = round(float(np.mod(round(E / np.pi, 3), 2.0)), 3)
        byE.setdefault(key, []).append(ch)
        print("   node k/pi = %s  E*/pi = %.3f  chirality %+.3f" % (np.round(k / np.pi, 4), E / np.pi, ch))
    for key, chs in sorted(byE.items()):
        print("   net chirality at E*/pi = %.3f : %+.3f (%d nodes)" % (key, sum(chs), len(chs)))
    W = winding(Uf, n=n_w)
    print("   W3 = %+.4f (Re part; numerical, grid %d^3)" % (W.real, n_w))
    return nodes, byE, W


if __name__ == "__main__":
    # test 1: degree-one map (normalized; not finite range): expect |W3| = 1 and unpaired net chirality at each gap
    def U1(k, m=2.0):
        d0 = m - np.cos(k).sum()
        d = np.sin(k)
        nrm = np.sqrt(d0 ** 2 + (d ** 2).sum())
        return (d0 * s0 - 1j * (d[0] * sx + d[1] * sy + d[2] * sz)) / nrm
    report("degree-one normalized map (m=2)", U1)

    # test 2: Hamiltonian-generated step exp(-i t H) of a two-node Weyl semimetal: expect W3 = 0, net chirality 0
    def U2(k, t=0.4, k0=np.pi / 2):
        H = np.sin(k[0]) * sx + np.sin(k[1]) * sy + (np.cos(k[2]) - np.cos(k0) + 2 - np.cos(k[0]) - np.cos(k[1])) * sz
        return expm(-1j * t * H)
    report("exp(-i t H_Weyl), two nodes", U2)

    # test 3: content-set conveyors in a fixed order: U = exp(i kx sx) exp(i ky sy) exp(i kz sz) (finite range, nearest neighbour)
    def U3(k):
        return expm(1j * k[0] * sx) @ expm(1j * k[1] * sy) @ expm(1j * k[2] * sz)
    report("content-set conveyors exp(i kx sx) exp(i ky sy) exp(i kz sz)", U3)
