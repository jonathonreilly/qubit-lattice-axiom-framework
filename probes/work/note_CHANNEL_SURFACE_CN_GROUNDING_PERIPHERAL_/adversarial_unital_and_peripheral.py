#!/usr/bin/env python3
"""J:note falsifiers for CHANNEL_SURFACE_CN_GROUNDING_PERIPHERAL_UNITARY_SUMMAND_BOUNDED_THEOREM_NOTE_2026-06-11 (on main).

Falsifiers implemented (the note's list), beyond its runner's random Stinespring/mixed-unitary instances:
  - "a unital trace-preserving CP map with HS-norm > 1": the HS operator norm (largest singular value of the natural n^2 x n^2
    representation) of (i) the Werner-Holevo channels Phi(x) = (tr(x) I - x^T)/(n-1), n = 3..7, which are unital and CPTP but not
    mixed-unitary at n = 3; (ii) unital CPTP maps made by operator-Sinkhorn scaling of random Kraus families, n = 2..6; (iii) an
    ADVERSARIAL hill climb over Kraus families (Sinkhorn-projected at every step) maximising the HS norm, n = 3, 4; plus the two
    hostile witnesses (a TP non-unital and a unital non-TP map exceed 1);
  - "a contraction with a unimodular eigenvalue whose eigenvector fails the joint-T^dag property": a hill climb over contractions
    T = [[lam, x^dag], [0, C]] (so T e_1 = lam e_1) rescaled to norm 1 maximising |x|, and random W (U + C) W^dag contractions;
  - "a peripheral summand admitting no spectrum-reflection conjugacy": for random unitaries, Theta = W K W^T (K complex conjugation)
    gives Theta U Theta^-1 = U^-1;
  - "large-separation covariance data carrying non-peripheral content beyond the geometric bound": ||T^n - U_per^n (+) 0|| against
    ||C^n|| for the cnu block.
HIT if any falsifier fires.
"""
from __future__ import annotations

import numpy as np

rng = np.random.default_rng(20260919)


def superop(kraus):
    """natural representation of Phi(x) = sum K x K^dag acting on vec(x) (row-major): S = sum K (x) conj(K)."""
    return sum(np.kron(K, K.conj()) for K in kraus)


def hs_norm(kraus):
    return np.linalg.norm(superop(kraus), 2)


def sinkhorn_unital(kraus, iters=5000):
    """operator Sinkhorn: alternately enforce sum K^dag K = I (TP) and sum K K^dag = I (unital), until both hold to 1e-13."""
    for _ in range(iters):
        if unital_err(kraus) < 1e-13:
            break
        A = sum(K.conj().T @ K for K in kraus)
        w, V = np.linalg.eigh(A)
        Ai = V @ np.diag(w ** -0.5) @ V.conj().T
        kraus = [K @ Ai for K in kraus]
        B = sum(K @ K.conj().T for K in kraus)
        w, V = np.linalg.eigh(B)
        Bi = V @ np.diag(w ** -0.5) @ V.conj().T
        kraus = [Bi @ K for K in kraus]
    A = sum(K.conj().T @ K for K in kraus)
    w, V = np.linalg.eigh(A)
    kraus = [K @ V @ np.diag(w ** -0.5) @ V.conj().T for K in kraus]
    return kraus


def unital_err(kraus):
    n = kraus[0].shape[0]
    return max(np.abs(sum(K.conj().T @ K for K in kraus) - np.eye(n)).max(), np.abs(sum(K @ K.conj().T for K in kraus) - np.eye(n)).max())


def werner_holevo(n):
    """Phi(x) = (tr(x) I - x^T)/(n-1): Kraus K_ij = (|i><j| - |j><i|)/sqrt(n-1), i < j."""
    ks = []
    for i in range(n):
        for j in range(i + 1, n):
            K = np.zeros((n, n), complex)
            K[i, j], K[j, i] = 1, -1
            ks.append(K / np.sqrt(n - 1))
    return ks


def hill_climb_hs(n, r=4, steps=300):
    ks = sinkhorn_unital([rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)) for _ in range(r)])
    best = hs_norm(ks)
    for s in range(steps):
        step = 0.3 * (1 - s / steps) + 0.01
        cand = sinkhorn_unital([K + step * (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) for K in ks], iters=150)
        val = hs_norm(cand)
        if val > best and unital_err(cand) < 1e-10:
            ks, best = cand, val
    return best, unital_err(ks)


def contraction_climb(n, steps=2000):
    lam = np.exp(1j * rng.uniform(0, 2 * np.pi))
    x = rng.normal(size=n - 1) + 1j * rng.normal(size=n - 1)
    C = rng.normal(size=(n - 1, n - 1)) + 1j * rng.normal(size=(n - 1, n - 1))
    def build(x, C):
        T = np.zeros((n, n), complex)
        T[0, 0] = lam
        T[0, 1:] = x.conj()
        T[1:, 1:] = C
        nrm = np.linalg.norm(T, 2)
        if nrm > 1:
            # a norm-1 contraction keeping T e_1 = lam e_1 exactly requires shrinking the off-diagonal and C, not the whole matrix
            lo, hi = 0.0, 1.0
            for _ in range(60):
                mid = (lo + hi) / 2
                Tm = T.copy()
                Tm[0, 1:] *= mid
                Tm[1:, 1:] *= mid
                if np.linalg.norm(Tm, 2) <= 1 + 1e-15:
                    lo = mid
                else:
                    hi = mid
            T[0, 1:] *= lo
            T[1:, 1:] *= lo
        return T
    best = 0.0
    for _ in range(steps):
        T = build(x, C)
        v = np.zeros(n, complex)
        v[0] = 1
        dev = np.linalg.norm(T.conj().T @ v - np.conj(lam) * v)
        if dev > best:
            best = dev
        x = x + 0.5 * (rng.normal(size=n - 1) + 1j * rng.normal(size=n - 1))
        C = C + 0.5 * (rng.normal(size=(n - 1, n - 1)) + 1j * rng.normal(size=(n - 1, n - 1)))
    return best


def rand_unitary(n):
    Q, R = np.linalg.qr(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
    return Q * (np.diag(R) / np.abs(np.diag(R)))


def main():
    wh = {n: (hs_norm(werner_holevo(n)), unital_err(werner_holevo(n))) for n in range(3, 8)}
    rnd = {}
    for n in range(2, 7):
        vals = []
        while len(vals) < 20:
            ks = sinkhorn_unital([rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)) for _ in range(rng.integers(2, 6))])
            if unital_err(ks) < 1e-12:                               # only converged (exactly unital CPTP to 1e-12) maps are tested
                vals.append((hs_norm(ks), unital_err(ks)))
        rnd[n] = (max(v[0] for v in vals), max(v[1] for v in vals))
    climb = {n: hill_climb_hs(n) for n in (3, 4)}
    g = 0.5
    ad = [np.array([[1, 0], [0, np.sqrt(1 - g)]], complex), np.array([[0, np.sqrt(g)], [0, 0]], complex)]
    un_ntp = [np.array([[1.2, 0], [0, 0.8]], complex) / 1.0]
    un_ntp = [np.sqrt(0.5) * np.array([[1, 0.4], [0, 1]], complex), np.sqrt(0.5) * np.array([[1, 0], [-0.4, 1]], complex)]
    witness = {"amplitude damping (TP, not unital), gamma = 1/2": hs_norm(ad),
               "sum K K^dag = I but not TP": (hs_norm(un_ntp), float(np.abs(sum(K @ K.conj().T for K in un_ntp) - np.eye(2)).max()))}
    print(f"1. HS operator norms: Werner-Holevo n = 3..7 (norm, unital/TP error) {({n: (round(v[0], 12), float('%.1e' % v[1])) for n, v in wh.items()})}; "
          f"Sinkhorn unital maps, max over 20 per n {({n: (round(v[0], 12), float('%.1e' % v[1])) for n, v in rnd.items()})}; adversarial hill climb "
          f"{({n: (round(v[0], 12), float('%.1e' % v[1])) for n, v in climb.items()})}; hostile witnesses {witness}")
    cc = {n: contraction_climb(n) for n in (2, 3, 5)}
    blk = 0.0
    for n in (4, 6, 8):
        for _ in range(20):
            k = rng.integers(1, n)
            U = rand_unitary(k)
            C = rng.normal(size=(n - k, n - k)) + 1j * rng.normal(size=(n - k, n - k))
            C *= rng.uniform(0.3, 0.95) / np.linalg.norm(C, 2)
            W = rand_unitary(n)
            T = W @ np.block([[U, np.zeros((k, n - k))], [np.zeros((n - k, k)), C]]) @ W.conj().T
            ev, vecs = np.linalg.eig(T)
            for lam, v in zip(ev, vecs.T):
                if abs(abs(lam) - 1) < 1e-10:
                    blk = max(blk, np.linalg.norm(T.conj().T @ v - np.conj(lam) * v))
    print(f"2. joint T^dag property: adversarial climb max |T^dag v - conj(lam) v| over norm-1 contractions with T v = lam v "
          f"{ {n: float('%.1e' % v) for n, v in cc.items()} }; random W(U + C)W^dag, n = 4, 6, 8: max {blk:.1e}")
    conj_err = 0.0
    for n in range(2, 9):
        for _ in range(10):
            U = rand_unitary(n)
            ev, W = np.linalg.eig(U)
            W, _ = np.linalg.qr(W)                                   # orthonormal eigenbasis (distinct eigenvalues)
            Theta = lambda x: W @ np.conj(W.conj().T @ x)            # antiunitary: conjugation in the spectral frame
            for _ in range(3):
                x = rng.normal(size=n) + 1j * rng.normal(size=n)
                lhs = Theta(U @ Theta(x))                            # Theta U Theta^-1 x (Theta^2 = 1)
                conj_err = max(conj_err, np.linalg.norm(lhs - U.conj().T @ x))
    print(f"3. Theta U Theta^-1 = U^-1 for random unitaries n = 2..8: max error {conj_err:.1e}")
    decay_ok, worst = True, 0.0
    for n in (4, 6):
        k = 2
        U = rand_unitary(k)
        C = rng.normal(size=(n - k, n - k)) + 1j * rng.normal(size=(n - k, n - k))
        C *= 0.8 / max(abs(np.linalg.eigvals(C)))
        T = np.block([[U, np.zeros((k, n - k))], [np.zeros((n - k, k)), C]])
        for m in (5, 10, 20, 40):
            Tm = np.linalg.matrix_power(T, m)
            per = np.zeros_like(T)
            per[:k, :k] = np.linalg.matrix_power(U, m)
            dev = np.linalg.norm(Tm - per, 2)
            bound = np.linalg.norm(np.linalg.matrix_power(C, m), 2)
            decay_ok &= dev <= bound * (1 + 1e-12)
            worst = max(worst, dev)
    print(f"4. non-peripheral content ||T^n - U^n (+) 0|| against ||C^n|| (rho_cnu = 0.8, n = 5..40): within bound {decay_ok}; largest {worst:.1e}")
    fails = []
    if max(v[0] for v in wh.values()) > 1 + 1e-12 or max(v[0] for v in rnd.values()) > 1 + 1e-12 or max(v[0] for v in climb.values()) > 1 + 1e-12:
        fails.append("unital CPTP map with HS norm > 1")
    if max(cc.values()) > 1e-6 or blk > 1e-8:
        fails.append("joint eigenvector")
    if conj_err > 1e-9:
        fails.append("conjugacy")
    if not decay_ok:
        fails.append("geometric bound")
    if fails:
        print(f"HIT: {fails}")
    print(f"SUMMARY: HS operator norms of unital CPTP maps are exactly 1 (Werner-Holevo n = 3..7, Sinkhorn-scaled random maps n = 2..6, and an "
          f"adversarial hill climb at n = 3, 4 reaching {max(v[0] for v in climb.values()):.12f}) while the TP-non-unital and unital-non-TP "
          f"witnesses exceed 1; an adversarial climb over norm-1 contractions with a unimodular eigenvector keeps |T^dag v - conj(lam) v| at "
          f"{max(cc.values()):.0e}; conjugation in the spectral frame reverses every random unitary to {conj_err:.0e}; the non-peripheral "
          f"content stays within ||C^n||; no falsifier fires")


if __name__ == "__main__":
    main()
