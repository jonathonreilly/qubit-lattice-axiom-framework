#!/usr/bin/env python3
"""s3: lane F session 3 checks (criteria: checks/s3_criteria.md, written before this script)."""
import itertools
import math
import numpy as np
import scipy.linalg as sla

RES = []


def rec(name, ok, msg):
    ok = bool(ok)
    RES.append((name, ok))
    print(f"{name}: {'PASS' if ok else 'FAIL'}  {msg}")


# ---------------- A: LOC-s' at the edge ----------------
def part_A():
    rng = np.random.default_rng(3)
    n = 12
    Z = rng.uniform(-1, 1, n)
    dist = np.array([min(y, n - y) for y in range(n)], dtype=float)
    b = 0.6 * np.exp(-0.5 * dist) * Z
    Xp = [0, 1]
    Fs = list(range(2, 12))
    c0 = b[0] + b[1]

    def g(svec):
        return 1.0 / (1.0 - (c0 + sum(b[y] * svec[y] for y in Fs)))

    # g at indicator 1_T, T subset of F
    gval = {}
    for k in range(len(Fs) + 1):
        for T in itertools.combinations(Fs, k):
            s = {y: 0.0 for y in Fs}
            for y in T:
                s[y] = 1.0
            gval[frozenset(T)] = g(s)
    viol, kept, skipped = 0, 0, 0
    maxratio = 0.0
    a3 = False
    for k in range(len(Fs) + 1):
        for S in itertools.combinations(Fs, k):
            FS = 0.0
            for j in range(len(S) + 1):
                for T in itertools.combinations(S, j):
                    FS += (-1) ** (len(S) - len(T)) * gval[frozenset(T)]
            sumb = sum(abs(b[y]) for y in S)
            sumbw = sum(abs(b[y]) * math.exp(0.5 * dist[y]) for y in S)
            if k == 0:
                m = abs(c0)
                B = 1.0 / (1.0 - m)
                kept += 1
                if abs(FS) > B * (1 + 1e-12):
                    viol += 1
                continue
            rho = (1 - 1e-3 - abs(c0) - sumb) / sumbw
            if rho <= 0:
                skipped += 1
                continue
            kept += 1
            r = {y: math.exp(0.5 * dist[y]) * rho for y in Fs}
            m = abs(c0) + sum(abs(b[y]) * (1 + r[y]) for y in S)
            B = (1.0 / (1.0 - m)) * np.prod([1.0 / r[y] for y in S])
            if abs(FS) > B * (1 + 1e-12):
                viol += 1
            maxratio = max(maxratio, abs(FS) / B)
            munref = abs(c0) + sum(abs(b[y]) * (1 + r[y]) for y in Fs)
            if munref >= 1:
                a3 = True
    rec("A1", viol == 0, f"violations {viol} of {kept} kept sets (skipped {skipped})")
    rec("A2", maxratio >= 1e-4 and kept >= 500, f"max |F_S|/B_S (|S|>=1) = {maxratio:.3e}; kept {kept}")
    rec("A3", a3, "unrefined domain contains the pole for some S" if a3 else "unrefined domain never reaches the pole")


# ---------------- B: Lemma QC ----------------
def kernel(nl, scale, rng):
    idx = np.arange(nl)
    dd = np.abs(idx[:, None] - idx[None, :])
    dd = np.minimum(dd, nl - dd)
    u = rng.standard_normal((nl, nl))
    u = (u + u.T) / 2
    return u * np.exp(-0.3 * np.round(dd / scale))


def part_B():
    rng = np.random.default_rng(5)
    # scalar
    ns = 300
    K = kernel(ns, 1, rng)
    A = np.abs(K)
    N0 = A.sum(axis=1).max()
    ok1 = True
    r1max, r3max = 0.0, 0.0
    for _ in range(200):
        dens = rng.uniform(0.05, 0.5)
        Q = rng.random(ns) < dens
        t = np.where(Q, 2.0 ** (rng.integers(0, 7, ns) + 1), 0.0)
        sig = A @ t
        for k in (1, 2, 3):
            lhs = (sig ** k).sum()
            rhs = N0 ** k * (t ** k).sum()
            if lhs > rhs * (1 + 1e-12):
                ok1 = False
        r1max = max(r1max, sig.sum() / (N0 * t.sum()))
        r3max = max(r3max, (sig ** 3).sum() / (N0 ** 3 * (t ** 3).sum()))
    rec("B1", ok1, f"scalar Hölder bounds hold in 200 trials (N_0 = {N0:.3f})")
    # block: 150 sites x 4 links
    nsite = 150
    nl = 4 * nsite
    Kl = kernel(nl, 4, rng)
    Al = np.abs(Kl)
    N0l = Al.sum(axis=1).max()
    Ablk = Al.reshape(nl, nsite, 4).sum(axis=2)  # |K(b, y)| := sum over links at y
    ok2 = True
    for _ in range(200):
        dens = rng.uniform(0.05, 0.5)
        Q = rng.random(nsite) < dens
        t = np.where(Q, 2.0 ** (rng.integers(0, 7, nsite) + 1), 0.0)
        sig = Ablk @ t
        for k in (1, 2, 3):
            lhs = (sig ** k).sum()
            rhs = 4 * N0l ** k * (t ** k).sum()
            if lhs > rhs * (1 + 1e-12):
                ok2 = False
    rec("B2", ok2, f"block Hölder bounds (factor 4) hold in 200 trials (N_0 = {N0l:.3f})")
    rec("B3", r1max >= 0.3 and r3max >= 1e-3, f"max linear ratio {r1max:.3f}, max cubic ratio {r3max:.3e}")


# ---------------- C: Lemma SF-N natural ----------------
def rand_su(N, rng, norm):
    M = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    X = (M - M.conj().T) / 2
    X -= np.trace(X) / N * np.eye(N)
    return X * (norm / np.linalg.norm(X))


def rand_sl(N, rng, norm):
    M = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    M -= np.trace(M) / N * np.eye(N)
    return M * (norm / np.linalg.norm(M))


def part_C():
    rng = np.random.default_rng(7)
    pL = 11
    ell = 2 * pL
    cy = 2.2 * pL
    ok1, ok2 = True, True
    worst1 = -1.0
    al_ratios = []
    for N in (2, 3):
        for alpha in (1e-4, 3e-4):
            for a in (1e-4, 5e-4):
                for trial in range(301):
                    aligned = trial == 300
                    eps = rng.choice([1, -1], ell)
                    U = [sla.expm(rand_su(N, rng, alpha)) for _ in range(ell)]
                    L = np.eye(N, dtype=complex)
                    partial = []
                    for i in range(ell):
                        L = L @ (U[i] if eps[i] == 1 else np.linalg.inv(U[i]))
                        partial.append(L.copy())
                    Y = sla.logm(L)
                    ybg = np.linalg.norm(Y)
                    if ybg > cy * alpha * (1 + 1e-12):
                        ok2 = False
                    if aligned:
                        What = Y / np.linalg.norm(Y)
                        What = (What - What.conj().T) / 2
                        What /= np.linalg.norm(What)
                        As = []
                        Pprev = np.eye(N, dtype=complex)
                        for i in range(ell):
                            if eps[i] == 1:
                                Ai = np.linalg.inv(Pprev) @ (a * What) @ Pprev
                            else:
                                Pi = partial[i]
                                Ai = -np.linalg.inv(Pi) @ (a * What) @ Pi
                            As.append(Ai)
                            Pprev = partial[i]
                    else:
                        As = [rand_sl(N, rng, a) for _ in range(ell)]
                    P = np.eye(N, dtype=complex)
                    for i in range(ell):
                        F = sla.expm(As[i]) @ U[i]
                        P = P @ (F if eps[i] == 1 else np.linalg.inv(F))
                    y = np.linalg.norm(sla.logm(P))
                    if y > ybg + cy * a + 1e-14:
                        ok1 = False
                    worst1 = max(worst1, (y - ybg) / (cy * a))
                    if aligned:
                        al_ratios.append((y - ybg) / (ell * a))
    rec("C1", ok1, f"max (y - y_bg)/(c_y a) = {worst1:.4f}")
    rec("C2", ok2, "y_bg <= 2.2 p_L alpha in every sample")
    rec("C3", max(al_ratios) >= 0.5 and max(al_ratios) <= 1.04,
        f"aligned (y - y_bg)/(l a): min {min(al_ratios):.4f}, max {max(al_ratios):.4f}")


# ---------------- D: arithmetic ----------------
def part_D():
    k0 = 16 * math.log(12800)
    kt = 16 * math.log(2 * 624 ** 2)
    rec("D1", 151.31 <= k0 <= 151.32 and 217.0 <= kt <= 217.1 and 588 <= k0 + 2 * kt + 3 <= 589,
        f"kappa_0 = {k0:.4f}, tilde kappa_0 = {kt:.4f}, kappa_0 + 2 tilde + 3 = {k0 + 2 * kt + 3:.3f}")
    w8 = sum((2 * n + 1) ** 4 * math.exp(-8 * n) for n in range(1, 200))
    l2 = 16 * math.log(2)

    def closes(kc):
        return 3 * (kc - k0 - 2 * kt - 3 - l2 - k0) - 1 >= kc + l2 + 1296 * w8
    lo, hi = 0.0, 1e6
    for _ in range(200):
        mid = (lo + hi) / 2
        if closes(mid):
            hi = mid
        else:
            lo = mid
    rec("D2", 1100 <= hi <= 1200, f"kappa_c^* = {hi:.3f} (w_8 = {w8:.5f})")
    grid = np.exp(np.linspace(math.log(3 * k0 + 3), math.log(1e8), 10000))
    fails = all(3 * (kc - 3 * k0 - 3 - k0) - 1 < 273 * (kc + l2) + 1296 * w8 for kc in grid)
    rec("D3", fails, "273 route never reproduces the rate on the grid")
    ok = True
    for N in (2, 3):
        n = 4 * (N * N - 1)
        for p in (10, 30, 100):
            s = sum(2 ** (n / 2) * math.exp(-4 ** j * p * p / 4 + 3 / 16 * 4 ** j * p * p) for j in range(0, 31))
            if s > 2 * 2 ** (n / 2) * math.exp(-p * p / 16):
                ok = False
    rec("D4", ok, "CE-Q per-site shell sums bounded")


if __name__ == "__main__":
    part_A()
    part_B()
    part_C()
    part_D()
    npass = sum(ok for _, ok in RES)
    print(f"OVERALL: {'PASS' if npass == len(RES) else 'FAIL'} {npass}/{len(RES)}")
