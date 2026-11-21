#!/usr/bin/env python3
"""GUIDE run for FINISH row 899, Step 8 (the thickness ladder for wall W1).

It decides nothing. A run can refute or guide, never discharge.

Object. 4D Wilson SU(2), weight exp(beta * sum_p (1/2) tr U_p), in a slab of
T layers of time-like links between two FLAT slices (all wall links = 1),
periodic in the three space directions with side L.
s(x) = H_0(x) H_1(x) ... H_{T-1}(x), the wall-to-wall line, a unit quaternion.
G(r) = < s(x) . s(x + r e_i) >  (the wall-to-wall Wilson rectangle T x r).
m2   = < |sum_x s(x)|^2 > / L^6  (volume mean of G).

Criteria, written before any run.
 C0 (code check). T = 1 is the 3D O(4) model at coupling beta. At beta = 0.5
    m2 must be O(1/L^3) (disordered); at beta = 2.3 the infrared bound of
    Proposition TB2 demands m2 >= 1 - 4*G_3/beta - o(1) = 0.56 (G_3 = 0.2527).
    If either fails, the code is wrong and nothing below is read.
 C1 (the ladder). For T = 1, 2, 3, 4 at beta = 2.3 and 2.6: compare m2 at
    L = 8 and L = 12. "Ordered" if m2(12) >= 0.7 * m2(8) and m2(12) >= 0.05.
    "Disordered" if m2(12) * 12^3 <= 1.6 * m2(8) * 8^3 (susceptibility flat).
    Otherwise "undecided".
 The ARGUED guess of Step 8.2 (stiffness in series) is: ordered for
 T <= beta/0.94, disordered above. The run can contradict that guess.

Usage: python3 -I slab_ladder_guide.py [quick]
Single thread, numpy only, memory far below 300 MB.
"""
import sys
import time
import numpy as np


def qmul(a, b):
    """Quaternion product; a0 + i a.sigma convention."""
    a0, av = a[..., :1], a[..., 1:]
    b0, bv = b[..., :1], b[..., 1:]
    c0 = a0 * b0 - np.sum(av * bv, axis=-1, keepdims=True)
    cv = a0 * bv + b0 * av - np.cross(av, bv)
    return np.concatenate([c0, cv], axis=-1)


def qconj(a):
    return a * np.array([1.0, -1.0, -1.0, -1.0])


def sh(a, mu, d):
    """Field at site x + d * e_mu (periodic)."""
    return np.roll(a, -d, axis=mu)


def identity(L):
    q = np.zeros((L, L, L, 4))
    q[..., 0] = 1.0
    return q


def heatbath(staple, beta, rng):
    """New link U with density prop. to exp(beta * (1/2) tr(U A)), A = staple sum."""
    k = np.sqrt(np.sum(staple * staple, axis=-1))
    k = np.maximum(k, 1e-12)
    V = staple / k[..., None]
    bk = beta * k
    a0 = np.empty_like(bk)
    todo = np.ones(bk.shape, dtype=bool)
    while todo.any():
        n = int(todo.sum())
        b = bk[todo]
        x = np.exp(-2.0 * b) + (1.0 - np.exp(-2.0 * b)) * rng.random(n)
        cand = 1.0 + np.log(x) / b
        cand = np.clip(cand, -1.0, 1.0)
        acc = rng.random(n) ** 2 <= 1.0 - cand * cand
        idx = np.flatnonzero(todo)
        a0.flat[idx[acc]] = cand[acc]
        todo.flat[idx[acc]] = False
    r = np.sqrt(np.maximum(0.0, 1.0 - a0 * a0))
    ct = 2.0 * rng.random(bk.shape) - 1.0
    st = np.sqrt(1.0 - ct * ct)
    ph = 2.0 * np.pi * rng.random(bk.shape)
    W = np.stack([a0, r * st * np.cos(ph), r * st * np.sin(ph), r * ct], axis=-1)
    return qmul(W, qconj(V))


class Slab:
    def __init__(self, L, T, beta, seed):
        self.L, self.T, self.beta = L, T, beta
        self.rng = np.random.default_rng(seed)
        # U[s][mu]: space-like links of slice s = 0..T; slices 0 and T are walls.
        self.U = [[identity(L) for _ in range(3)] for _ in range(T + 1)]
        # H[s]: time-like links from slice s to s + 1, s = 0..T-1.
        self.H = [identity(L) for _ in range(T)]
        x = np.indices((L, L, L)).sum(axis=0) % 2
        self.par = [x == 0, x == 1]

    def staple_space(self, s, mu):
        U, H = self.U, self.H
        A = np.zeros((self.L,) * 3 + (4,))
        for nu in range(3):
            if nu == mu:
                continue
            A += qmul(qmul(sh(U[s][nu], mu, 1), qconj(sh(U[s][mu], nu, 1))), qconj(U[s][nu]))
            dn = sh(U[s][nu], nu, -1)
            A += qmul(qmul(qconj(sh(dn, mu, 1)), qconj(sh(U[s][mu], nu, -1))), dn)
        A += qmul(qmul(sh(H[s], mu, 1), qconj(U[s + 1][mu])), qconj(H[s]))
        A += qmul(qmul(qconj(sh(H[s - 1], mu, 1)), qconj(U[s - 1][mu])), H[s - 1])
        return A

    def staple_time(self, s):
        U, H = self.U, self.H
        A = np.zeros((self.L,) * 3 + (4,))
        for mu in range(3):
            A += qmul(qmul(U[s + 1][mu], qconj(sh(H[s], mu, 1))), qconj(U[s][mu]))
            A += qmul(qmul(qconj(sh(U[s + 1][mu], mu, -1)), qconj(sh(H[s], mu, -1))),
                      sh(U[s][mu], mu, -1))
        return A

    def sweep(self):
        for s in range(self.T):
            for p in (0, 1):
                new = heatbath(self.staple_time(s), self.beta, self.rng)
                self.H[s] = np.where(self.par[p][..., None], new, self.H[s])
        for s in range(1, self.T):
            for mu in range(3):
                for p in (0, 1):
                    new = heatbath(self.staple_space(s, mu), self.beta, self.rng)
                    self.U[s][mu] = np.where(self.par[p][..., None], new, self.U[s][mu])

    def line(self):
        s = self.H[0]
        for k in range(1, self.T):
            s = qmul(s, self.H[k])
        return s

    def measure(self):
        s = self.line()
        L = self.L
        tot = s.reshape(-1, 4).sum(axis=0)
        m2 = float(tot @ tot) / L ** 6
        g = [float(np.mean([np.sum(s * sh(s, i, r), axis=-1).mean() for i in range(3)]))
             for r in range(L // 2 + 1)]
        return m2, g


def run(L, T, beta, ntherm, nmeas, seed):
    sl = Slab(L, T, beta, seed)
    for _ in range(ntherm):
        sl.sweep()
    m2s, gs = [], []
    for _ in range(nmeas):
        sl.sweep()
        m2, g = sl.measure()
        m2s.append(m2)
        gs.append(g)
    m2s = np.array(m2s)
    nb = 10
    blocks = m2s[: (len(m2s) // nb) * nb].reshape(nb, -1).mean(axis=1)
    return m2s.mean(), blocks.std(ddof=1) / np.sqrt(nb), np.mean(gs, axis=0)


def main():
    quick = len(sys.argv) > 1 and sys.argv[1] == "quick"
    nth, nme = (60, 120) if quick else (300, 800)
    t0 = time.time()
    print("C0 code check, T = 1 (3D O(4) model)")
    for beta in (0.5, 2.3):
        for L in (8,) if quick else (8, 12):
            m2, err, g = run(L, 1, beta, nth, nme, seed=1)
            print(f"  beta={beta} L={L}: m2={m2:.4f} +- {err:.4f}  m2*L^3={m2 * L ** 3:.2f}  "
                  f"G(L/2)={g[-1]:.4f}  [bound at 2.3: m2 >= {1 - 4 * 0.252731 / 2.3:.3f}]")
    print("C1 ladder")
    for beta in (2.3,) if quick else (2.3, 2.6):
        for T in (1, 2, 3, 4):
            row = []
            for L in (8,) if quick else (8, 12):
                m2, err, g = run(L, T, beta, nth, nme, seed=10 * T + L)
                row.append((L, m2, err, g[-1]))
            txt = "  ".join(f"L={L}: m2={m2:.4f}+-{err:.4f} chi={m2 * L ** 3:.1f} G(L/2)={gh:.4f}"
                            for (L, m2, err, gh) in row)
            print(f"  beta={beta} T={T}: {txt}")
    print(f"elapsed {time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
