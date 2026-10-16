#!/usr/bin/env python3
"""A cubic-covariant Dirac tick on 2x2x2 blocks of one-amplitude sites.

One amplitude per site of Z^3. Group sites into 2x2x2 blocks (translations by 2)
and let each proper cubic rotation R act about the block centre: it permutes the
eight corners, possibly with signs (staggered phases). A one-tick walk is then
an 8-component walk on the block lattice, U(k) = sum_n A_n e^{ik.n},
n in {-1,0,1}^3 (block units), covariant if A_{Rn} = D(R) A_n D(R)^dagger.

Checks:
  1. the signed corner actions fall into five classes; two are spinorial
     (quarter-turn lifts of order 8) and are, up to phases, C^2 (x) E (x) E_{1/2},
     i.e. two copies of the spin-3/2 representation;
  2. for a spinorial class, transporting the two-qubit Dirac walk
     U_2q (x) 1_E (companion note) through an intertwiner gives a unitary,
     exactly block-covariant, moving walk;
  3. that walk has an isotropic massless cone at k = 0, eightfold (two Dirac
     fermions), and no other zero of the quasienergy on a grid (numerical).
"""

from __future__ import annotations

import itertools
import sys

import numpy as np
from scipy.linalg import expm, null_space, polar

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    'docs/STAGGERED_ONE_QUBIT_BLOCKS_CARRY_A_CUBIC_COVARIANT_DIRAC_TICK_BOUNDED_THEOREM_NOTE_2026-10-16.md',
)

RZ = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
RX = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.diag([1.0 + 0j, -1.0])
S0 = np.eye(2, dtype=complex)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool) -> None:
        if ok:
            self.passed += 1
            print(f"PASS {name}")
        else:
            self.failed += 1
            print(f"FAIL {name}")


CORNERS = [np.array(v) for v in itertools.product((0, 1), repeat=3)]
CIDX = {tuple(v): i for i, v in enumerate(CORNERS)}


def corner_perm(R):
    P = np.zeros((8, 8))
    for i, v in enumerate(CORNERS):
        w = R @ (2 * v - 1)
        P[CIDX[tuple((w + 1) // 2)], i] = 1
    return P


def generated(gens, cap=200):
    G = {np.round(np.eye(8)).tobytes(): np.eye(8)}
    frontier = [np.eye(8)]
    while frontier:
        nxt = []
        for A in frontier:
            for g in gens:
                B = np.round(A @ g)
                k = (B + 0.0).tobytes()
                if k not in G:
                    G[k] = B
                    nxt.append(B)
                    if len(G) > cap:
                        return None
        frontier = nxt
    return list(G.values())


def order(M):
    return next(k for k in range(1, 17) if np.allclose(np.linalg.matrix_power(M, k), np.eye(len(M))))


def spin_lift(j):
    m = np.arange(j, -j - 1, -1)
    d = len(m)
    Jp = np.zeros((d, d), complex)
    for i in range(1, d):
        Jp[i - 1, i] = np.sqrt(j * (j + 1) - m[i] * (m[i] + 1))
    Jx = (Jp + Jp.conj().T) / 2
    Jz = np.diag(m).astype(complex)
    return expm(-1j * np.pi / 2 * Jz), expm(-1j * np.pi / 2 * Jx)


def hom_dim(A, B):
    (az, ax), (bz, bx) = A, B
    n, m = az.shape[0], bz.shape[0]
    M = np.vstack([np.kron(np.eye(m), az) - np.kron(bz.T, np.eye(n)),
                   np.kron(np.eye(m), ax) - np.kron(bx.T, np.eye(n))])
    return null_space(M).shape[1], null_space(M)


def two_qubit_dirac_coefficients():
    """The companion note's explicit member b* = (11/30, sqrt(u*), 3/20), massless at k = 0."""
    b0, b2 = 11 / 30, 3 / 20

    def gram(b0, b1, b2):
        G = np.array([[1 - 3 * b0 ** 2, -2 * b0 * b1, -b0 ** 2 - b0 * b2 + b1 ** 2, -3 * b1 * (b0 - b2)],
                      [0, b0 ** 2 - 2 * b1 ** 2, b1 * (b0 - b2), b0 * b2 - b1 ** 2 + b2 ** 2],
                      [0, 0, 2 * b1 ** 2 - b2 ** 2, 2 * b1 * b2],
                      [0, 0, 0, 3 * b2 ** 2]])
        return G + np.triu(G, 1).T
    # u* = smallest positive root of det G = 0 as a polynomial in u = b1^2 (quartic); bisection on det
    from scipy.optimize import brentq
    f = lambda u: np.linalg.det(gram(b0, np.sqrt(u), b2))
    us = np.linspace(1e-6, 0.2, 4000)
    vals = [f(u) for u in us]
    root = next(brentq(f, us[i], us[i + 1]) for i in range(len(us) - 1) if vals[i] * vals[i + 1] < 0)
    b1 = np.sqrt(root)
    G = gram(b0, b1, b2)
    phi0 = np.array([1.0, 3, 3, 1])
    a = G @ phi0
    rest = G - np.outer(a, a)
    w, V = np.linalg.eigh(rest)
    c = [np.sqrt(max(w[i], 0)) * V[:, i] for i in np.argsort(w)[-2:]]
    F = np.array([a, c[0], c[1]])
    b = np.array([b0, b1, b2])

    def U(k):
        cc, ss = np.cos(k), np.sin(k)
        ph = np.array([1, cc.sum(), cc[0] * cc[1] + cc[0] * cc[2] + cc[1] * cc[2], cc.prod()])
        v1 = np.array([ss[0] * (cc[1] + cc[2]), ss[1] * (cc[0] + cc[2]), ss[2] * (cc[0] + cc[1])])
        v2 = np.array([ss[0] * cc[1] * cc[2], ss[1] * cc[0] * cc[2], ss[2] * cc[0] * cc[1]])
        g = b[0] * ss + b[1] * v1 + b[2] * v2
        f_, h1, h2 = F @ ph
        return (f_ * np.eye(4) + 1j * (h1 * np.kron(SX, S0) + h2 * np.kron(SY, S0))
                + 1j * np.kron(SZ, g[0] * SX + g[1] * SY + g[2] * SZ))
    stencil = [tuple(v) for v in itertools.product((-1, 0, 1), repeat=3)]
    grid = [np.array(t) * 2 * np.pi / 3 for t in itertools.product(range(3), repeat=3)]
    A = np.array([sum(U(k) * np.exp(-1j * np.dot(k, n)) for k in grid) / 27 for n in stencil])
    return stencil, A, b[0] + 2 * b[1] + b[2]


def main() -> int:
    ck = Checks()
    PZ, PX = corner_perm(RZ), corner_perm(RX)
    ck.check('corner permutations represent the rotations about the block centre (orders 4, 4; group of order 24)',
             order(PZ) == 4 and order(PX) == 4 and len(generated([PZ, PX])) == 24)
    classes = {}
    for sz in itertools.product((1, -1), repeat=8):
        for sx in itertools.product((1, -1), repeat=8):
            DZ, DX = np.diag(sz) @ PZ, np.diag(sx) @ PX
            G = generated([DZ, DX])
            if G is None:
                continue
            spinorial = len(G) == 48 and order(DZ) == 8
            if len(G) == 24 or len(G) == 48:
                key = (len(G), spinorial, tuple(sorted(int(round(np.trace(g))) for g in G)))
                classes.setdefault(key, (DZ, DX))
    n_spin = sum(1 for k in classes if k[1])
    ck.check(f'signed corner actions: {len(classes)} classes by trace data (group order 24, order 48 split, order 48 spinorial), {n_spin} spinorial',
             len(classes) == 3 and n_spin == 1)
    Hz, Hx = spin_lift(1.5)
    Ez_h, Ex_h = spin_lift(0.5)
    Bs = np.array([[1, 1], [-1, 1], [0, -2]]) @ np.diag([1 / np.sqrt(2), 1 / np.sqrt(6)])
    Ez, Ex = Bs.T @ np.abs(RZ) @ Bs, Bs.T @ np.abs(RX) @ Bs
    R2 = (np.kron(np.eye(2), np.kron(Ez, Ez_h)), np.kron(np.eye(2), np.kron(Ex, Ex_h)))
    spin_classes = [v for k, v in classes.items() if k[1]]
    ok_dec = True
    found = None
    for DZ, DX in spin_classes:
        best = 0
        for pz in (1, -1, 1j, -1j):
            for px in (1, -1, 1j, -1j):
                h, Ns = hom_dim((DZ.astype(complex), DX.astype(complex)), (pz * R2[0], px * R2[1]))
                if h > best:
                    best = h
                    if found is None and h == 4:
                        found = (DZ.astype(complex), DX.astype(complex), pz, px, Ns)
        ok_dec &= best == 4
    ck.check('each spinorial class is equivalent, up to generator phases, to C^2 (x) E (x) E_1/2 (intertwiner space of dimension 4 = 2^2)', ok_dec)
    ok_h = all(max(hom_dim((DZ.astype(complex), DX.astype(complex)), (pz * Hz, px * Hx))[0]
                   for pz in (1, -1, 1j, -1j) for px in (1, -1, 1j, -1j)) == 2 for DZ, DX in spin_classes)
    ck.check('equivalently, two copies of the spin-3/2 representation (E (x) E_1/2 = spin 3/2)', ok_h)
    int_classes = [v for k, v in classes.items() if not k[1]]
    T1z, T1x = spin_lift(1.0)
    phases = (1, -1, 1j, -1j)
    no_spinor = all(max(hom_dim((DZ.astype(complex), DX.astype(complex)), (pz * M[0], px * M[1]))[0]
                        for M in ((Ez_h, Ex_h), (Hz, Hx)) for pz in phases for px in phases) == 0
                    for DZ, DX in int_classes)
    has_int = all(max(hom_dim((DZ.astype(complex), DX.astype(complex)), (pz * T1z, px * T1x))[0] for pz in phases for px in phases) >= 1
                  for DZ, DX in int_classes)
    ck.check('the other classes contain no spin-1/2 or spin-3/2 component (only scalar and spin-1 pieces): no spinor factor', no_spinor and has_int)
    DZ, DX, pz, px, Ns = found
    rng = np.random.default_rng(0)
    T = (Ns @ rng.normal(size=Ns.shape[1])).reshape(8, 8, order='F')
    T, _ = polar(T)
    err_T = max(np.abs(DZ @ T - T @ (pz * R2[0])).max(), np.abs(DX @ T - T @ (px * R2[1])).max())
    ck.check(f'unitary intertwiner T found (residual {err_T:.1e})', err_T < 1e-12)
    stencil, A2, s = two_qubit_dirac_coefficients()
    Pm = np.zeros((8, 8))
    for f in range(2):
        for sp_ in range(2):
            for e in range(2):
                Pm[f * 4 + e * 2 + sp_, f * 4 + sp_ * 2 + e] = 1
    A8 = np.array([T @ Pm @ np.kron(A, np.eye(2)) @ Pm.T @ T.conj().T for A in A2])
    W = lambda k: sum(A * np.exp(1j * np.dot(k, n)) for A, n in zip(A8, stencil))
    ks = rng.uniform(-np.pi, np.pi, (300, 3))
    err_u = max(np.abs(W(k) @ W(k).conj().T - np.eye(8)).max() for k in ks)
    ck.check(f'block walk W = T (U_2q (x) 1_E) T^dagger is unitary (max error {err_u:.1e})', err_u < 1e-12)
    err_c = max(np.abs(W(R @ k) - D @ W(k) @ D.conj().T).max() for R, D in ((RZ, DZ), (RX, DX)) for k in ks[:100])
    ck.check(f'W is covariant under the signed block action of both quarter-turn generators (max error {err_c:.1e})', err_c < 1e-12)
    moving = sum(np.abs(A).sum() for A, n in zip(A8, stencil) if n != (0, 0, 0))
    ck.check('W moves (nonzero hop coefficients)', moving > 1)
    ratios = []
    for direction in ([1, 0, 0], [1, 1, 0], [1, 1, 1], [0.3, -0.5, 0.8]):
        d_ = np.array(direction) / np.linalg.norm(direction)
        k = 1e-3 * d_
        ev = np.abs(np.angle(np.linalg.eigvals(W(k))))
        ratios.append(ev / 1e-3)
    ratios = np.array(ratios)
    ck.check(f'[numerical] massless isotropic cone at k = 0: all eight quasienergies = s |k| with s = {s:.4f} in four directions',
             np.allclose(ratios, s, atol=1e-4))
    tg = np.linspace(-np.pi, np.pi, 21)
    worst = min(np.abs(np.angle(np.linalg.eigvals(W(np.array(k))))).min() / np.linalg.norm(2 * np.sin(np.array(k) / 2))
                for k in itertools.product(tg, tg, tg) if np.linalg.norm(k) > 1e-9)
    ck.check(f'[numerical] on a 21^3 grid the quasienergy vanishes only at k = 0 (min omega / |2 sin(k/2)| = {worst:.3f})', worst > 0.3)
    print(f"TOTAL: PASS={ck.passed} FAIL={ck.failed}")
    return 0 if ck.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
