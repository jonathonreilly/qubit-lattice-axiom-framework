#!/usr/bin/env python3
"""Exact abelian minimal lift for the linearised block map (Bloch modes).

Criteria S1-S3, E1, E2, R1, P1, W1 in upper-chain_criteria.md.
Usage: upper-chain_lift_modulus.py [modes|decay|pos|ce|all]
"""
import resource
import sys

import numpy as np

PLANES = [(m, n) for m in range(4) for n in range(m + 1, 4)]
RSS_LIMIT = 2.0e9


def check_rss():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss > RSS_LIMIT:
        sys.exit(f"RSS {rss / 1e9:.2f} GB above limit")
    return rss


class Bloch:
    """Fine momenta k_B = (K + 2 pi B)/L for one coarse momentum K."""

    def __init__(self, L, K):
        self.L, self.K = L, np.asarray(K, float)
        q = [(self.K[m] + 2 * np.pi * np.arange(L)) / L for m in range(4)]
        s = np.arange(L)
        d = [np.exp(1j * np.outer(qm, s)).mean(axis=1) for qm in q]
        hat1 = [np.exp(1j * qm) - 1 for qm in q]
        shape = [(L, 1, 1, 1), (1, L, 1, 1), (1, 1, L, 1), (1, 1, 1, L)]
        self.D = [d[m].reshape(shape[m]) for m in range(4)]
        self.kh = [hat1[m].reshape(shape[m]) for m in range(4)]
        self.khsq = sum(np.abs(self.kh[m]) ** 2 for m in range(4))
        self.pi_D = self.D[0] * self.D[1] * self.D[2] * self.D[3]
        self.M = [L * self.D[m] * self.pi_D for m in range(4)]
        self.Kh = np.exp(1j * self.K) - 1

    def hplus_apply(self, v):
        """H^+ v for v a list of four arrays."""
        dot = sum(np.conj(self.kh[m]) * v[m] for m in range(4)) / self.khsq
        return [(v[m] - self.kh[m] * dot) / self.khsq for m in range(4)]

    def g0(self):
        G = np.zeros((4, 4), complex)
        for n in range(4):
            v = [np.zeros((1, 1, 1, 1), complex) for _ in range(4)]
            v[n] = np.conj(self.M[n])
            A = self.hplus_apply(v)
            for m in range(4):
                G[m, n] = (self.M[m] * A[m]).sum()
        return G

    def transverse(self):
        """Orthonormal basis of the complement of Kh in C^4; eigen data of G_perp."""
        u, _, _ = np.linalg.svd(self.Kh.reshape(4, 1), full_matrices=True)
        U = u[:, 1:]
        lam, vec = np.linalg.eigh(U.conj().T @ self.g0() @ U)
        return U, lam, U @ vec

    def lift(self, multiplier):
        """Fourier curvature of H^+ M^* multiplier, for the six planes."""
        v = [np.conj(self.M[m]) * multiplier[m] for m in range(4)]
        A = self.hplus_apply(v)
        return {(m, n): self.kh[m] * A[n] - self.kh[n] * A[m] for (m, n) in PLANES}

    def r4_average(self, Fh):
        out = {}
        for (m, n) in PLANES:
            weight = self.pi_D * self.L ** 2 * self.D[m] * self.D[n]
            out[(m, n)] = (weight * Fh[(m, n)]).sum()
        return out

    def position(self, Fhat_arr):
        """F(x) on x in {0..L-1}^4 from its Bloch coefficients."""
        L = self.L
        x = np.arange(L)
        phase = [np.exp(1j * self.K[m] * x / L) for m in range(4)]
        shape = [(L, 1, 1, 1), (1, L, 1, 1), (1, 1, L, 1), (1, 1, 1, L)]
        ph = 1
        for m in range(4):
            ph = ph * phase[m].reshape(shape[m])
        return ph * np.fft.ifftn(Fhat_arr) * L ** 4


def cube_weight(kb, r):
    """Mean over h in [-r,r]^4 of |exp(i k h) - 1|^2."""
    prod = 1.0
    for m in range(4):
        q = np.real(np.log(kb.kh[m] + 1) / 1j)
        s2 = np.sin(q / 2)
        small = np.abs(s2) < 1e-12
        safe = np.where(small, 1.0, s2)
        dirich = np.where(small, 1.0, np.sin((2 * r + 1) * q / 2) / ((2 * r + 1) * safe))
        prod = prod * dirich
    return 2 - 2 * prod


MODES = {
    "e1/64": (2 * np.pi / 64, 0, 0, 0),
    "pi": (np.pi, 0, 0, 0),
    "pi,pi": (np.pi, np.pi, 0, 0),
    "pi^3": (np.pi, np.pi, np.pi, 0),
    "pi^4": (np.pi, np.pi, np.pi, np.pi),
    "2pi/3(1,1)": (2 * np.pi / 3, 2 * np.pi / 3, 0, 0),
    "d/64": (2 * np.pi / 64,) * 4,
}


def run_modes(Ls=(3, 5, 7, 9, 15, 21, 27)):
    radii = {3: [1], 5: [1], 7: [1], 9: [1, 3], 15: [1, 5], 21: [1, 7], 27: [1, 3, 9]}
    worst_s1 = worst_s2 = 0.0
    CE, R, phi = {}, {}, {}
    for L in Ls:
        CE[L] = 0.0
        R[L] = {r: 0.0 for r in radii[L]}
        phi[L] = {}
        for name, K in MODES.items():
            kb = Bloch(L, K)
            U, lam, vec = kb.transverse()
            Khsq = np.sum(np.abs(kb.Kh) ** 2)
            phi[L][name] = 0.0
            for i in range(3):
                # A' = G_perp lam-multiplier, normalised to |A'| = 1
                mult = vec[:, i] / lam[i]
                Aprime = vec[:, i]
                Fh = kb.lift(mult)
                energy = L ** 4 * sum(np.sum(np.abs(Fh[p]) ** 2) for p in PLANES)
                Fprime2 = Khsq  # |K^ wedge A'|^2 for transverse unit A'
                # S1
                avg = kb.r4_average(Fh)
                for (m, n) in PLANES:
                    target = kb.Kh[m] * Aprime[n] - kb.Kh[n] * Aprime[m]
                    worst_s1 = max(worst_s1, abs(avg[(m, n)] - target) / np.sqrt(Fprime2))
                # S2
                worst_s2 = max(worst_s2, abs(energy - L ** 4 / lam[i]) / (L ** 4 / lam[i]))
                CE[L] = max(CE[L], energy / Fprime2)
                for r in radii[L]:
                    w = cube_weight(kb, r)
                    osc = L ** 4 * sum(np.sum(w * np.abs(Fh[p]) ** 2) for p in PLANES)
                    R[L][r] = max(R[L][r], osc / energy)
                sup = 0.0
                for p in PLANES:
                    sup = max(sup, np.abs(kb.position(Fh[p])).max())
                phi[L][name] = max(phi[L][name], sup * L ** 2 / np.sqrt(Fprime2))
            check_rss()
        print(f"L={L:2d} C_E={CE[L]:.4f} R={ {r: round(R[L][r], 5) for r in R[L]} } rss={check_rss() / 1e9:.2f}GB", flush=True)
    print(f"S1 worst {worst_s1:.2e}  S2 worst {worst_s2:.2e}")
    print("alpha at K small, L=3,9,27:", end=" ")
    for L in (3, 9, 27):
        kb = Bloch(L, MODES["e1/64"])
        U, lam, vec = kb.transverse()
        print(f"{L ** 4 / lam.max() / np.sum(np.abs(kb.Kh) ** 2):.4f}/{L ** 4 / lam.min() / np.sum(np.abs(kb.Kh) ** 2):.4f}", end="  ")
    print()
    print("E1:", CE[27] <= 1.25 * CE[9] and CE[9] <= 1.25 * CE[3], {L: round(CE[L], 4) for L in CE})
    a_eff = 0.5 * np.log(R[9][1] / R[27][1]) / np.log(3)
    c1, c2 = R[27][3] / R[9][1], R[27][9] / R[9][3]
    print(f"R1: alpha_eff {a_eff:.3f} collapse {c1:.3f} {c2:.3f} pass {a_eff >= 0.25 and 2 / 3 <= c1 <= 1.5 and 2 / 3 <= c2 <= 1.5}")
    for name in MODES:
        s = np.log(phi[27][name] / phi[9][name]) / np.log(3)
        print(f"W1 {name:12s} phi(3,9,27)= {phi[3][name]:.3f} {phi[9][name]:.3f} {phi[27][name]:.3f} slope {s:.3f}")


def run_ce(Ls=(33, 45)):
    """C_E only, for criterion E1'."""
    for L in Ls:
        best = 0.0
        for name, K in MODES.items():
            kb = Bloch(L, K)
            U, lam, vec = kb.transverse()
            best = max(best, L ** 4 / lam.min() / np.sum(np.abs(kb.Kh) ** 2))
            del kb
            check_rss()
        print(f"L={L} C_E={best:.4f} rss={check_rss() / 1e9:.2f}GB", flush=True)


def run_decay(cases=((3, 12), (5, 8), (9, 6))):
    for L, n in cases:
        N = n * L
        Fh = {p: np.zeros((N, N, N, N), complex) for p in PLANES}
        src = np.zeros(4, complex)
        src[0] = 1.0
        idx = np.indices((L, L, L, L))
        for K_idx in np.ndindex(n, n, n, n):
            if K_idx == (0, 0, 0, 0):
                continue
            kb = Bloch(L, 2 * np.pi * np.array(K_idx) / n)
            U, lam, vec = kb.transverse()
            coef = vec.conj().T @ src
            mult = vec @ (coef / lam)
            F = kb.lift(mult)
            m_idx = tuple(K_idx[a] + n * idx[a] for a in range(4))
            for p in PLANES:
                Fh[p][m_idx] = F[p]
        check_rss()
        energy = np.zeros((n, n, n, n))
        for p in PLANES:
            Fx = np.fft.ifftn(Fh[p]) * N ** 4 / n ** 4
            e = np.abs(Fx) ** 2
            del Fx
            for a in range(4):
                sh = [n if b == a else None for b in range(4)]
            blocked = e.reshape(n, L, n, L, n, L, n, L).sum(axis=(1, 3, 5, 7))
            energy += blocked
            del e
        check_rss()
        ax = [energy[(d, 0, 0, 0)] for d in range(n // 2)]
        tr = [energy[(0, d, 0, 0)] for d in range(n // 2)]
        rates = [0.5 * np.log(tr[d] / tr[d + 1]) for d in range(1, n // 2 - 1)]
        print(f"L={L} n={n} E(0)={energy[0, 0, 0, 0]:.4f} trans E(d)={[f'{v:.2e}' for v in tr]} amp rates={[round(float(r), 3) for r in rates]} along={[f'{v:.2e}' for v in ax]} rss={check_rss() / 1e9:.2f}GB", flush=True)


def run_pos(Ls=(5, 9, 15, 21), n=4):
    res = {}
    for L in Ls:
        V = (n * L) ** 4
        red = {p: np.zeros((L, L, L, L)) for p in PLANES}
        free = {p: 0.0 for p in PLANES}
        for K_idx in np.ndindex(n, n, n, n):
            if K_idx == (0, 0, 0, 0):
                continue
            kb = Bloch(L, 2 * np.pi * np.array(K_idx) / n)
            U, lam, vec = kb.transverse()
            for p in PLANES:
                m, k = p
                free[p] += np.sum((np.abs(kb.kh[m]) ** 2 + np.abs(kb.kh[k]) ** 2) / kb.khsq * np.ones((L, L, L, L))) / V
            for i in range(3):
                F = kb.lift(vec[:, i])
                for p in PLANES:
                    red[p] += np.abs(kb.position(F[p])) ** 2 / lam[i] / V
            check_rss()
        total = sum(red[p].sum() for p in PLANES)
        s3 = abs(total - 3 * (n ** 4 - 1) / n ** 4)
        rel = max((red[p] / free[p]).max() for p in PLANES)
        mean = np.mean([(red[p] / free[p]).mean() for p in PLANES])
        res[L] = rel
        print(f"L={L:2d} S3 err {s3:.2e} free(0,1)={free[(0, 1)]:.5f} rel mean*L^4={mean * L ** 4:.3f} rel max={rel:.3e} rel max*L^4={rel * L ** 4:.3f} rss={check_rss() / 1e9:.2f}GB", flush=True)
    print(f"P1: rel(21)/rel(9) = {res[21] / res[9]:.4f}, pass if <= {9 / 21:.4f}: {res[21] / res[9] <= 9 / 21}")


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("modes", "all"):
        run_modes()
    if what == "ce":
        run_ce()
    if what in ("pos", "all"):
        run_pos()
    if what in ("decay", "all"):
        run_decay()
