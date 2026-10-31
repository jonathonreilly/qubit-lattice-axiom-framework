#!/usr/bin/env python3
"""h5: (A) real-space inequalities of Lemma E-loc (HIST.md section 15); (B) d(M) of HIST.md section 14.2 (c1).
Criteria: checks/h5_criteria.md (written before this script). Reads no files. Prints < 6000 chars."""
import time, resource, sys
import numpy as np
from scipy.linalg import expm

t0 = time.time()
rng = np.random.default_rng(20261028)
L = 3
KAPPA = 1.0
C_LOC = ((2 * L - 1) / (L - 1)) * max(2.0, 16.0 / KAPPA)
out = []
def say(s):
    out.append(s); print(s); sys.stdout.flush()

# ---------------- Part A: abelian linear fields on a 4D periodic lattice ----------------
def leg_sum(Amu, mu, n):
    s = np.zeros_like(Amu)
    for j in range(n):
        s += np.roll(Amu, -j, axis=mu)
    return s

def block_mean(f, n):
    S = f.shape[0]; c = S // n
    return f.reshape(c, n, c, n, c, n, c, n).mean(axis=(1, 3, 5, 7))

def Qstr(A, n):
    return np.stack([block_mean(leg_sum(A[mu], mu, n), n) for mu in range(4)])

def dplaq(A, mu, nu):
    return A[mu] + np.roll(A[nu], -1, axis=mu) - np.roll(A[mu], -1, axis=nu) - A[nu]

def box_sum(f, ext):
    s = f
    for ax, e in enumerate(ext):
        t = np.zeros_like(s)
        for a in range(e):
            t += np.roll(s, -a, axis=ax)
        s = t
    return s

def sample(f, n):
    return f[::n, ::n, ::n, ::n]

PLANES = [(m, v) for m in range(4) for v in range(m + 1, 4)]

# A1
T = 3
A = rng.standard_normal((4,) + (27,) * 4)
q33 = Qstr(Qstr(A, 3), 3); q9 = Qstr(A, 9)
a1i = np.max(np.abs(q33 - q9)) / np.max(np.abs(A))
a1ii = 0.0
for n in (3, 9):
    S = n * T
    An = A if S == 27 else rng.standard_normal((4,) + (S,) * 4)
    Q = Qstr(An, n)
    for (m, v) in PLANES:
        lhs = dplaq(Q, m, v)
        dA = dplaq(An, m, v)
        ext = [1, 1, 1, 1]; ext[m] = n; ext[v] = n
        phi = box_sum(dA, ext)              # flux of the n x n square with corner y
        rhs = block_mean(phi, n)
        a1ii = max(a1ii, np.max(np.abs(lhs - rhs)) / np.max(np.abs(dA)))
A1 = a1i <= 1e-10 and a1ii <= 1e-10
say(f"A1 composite Q3.Q3 = Q9: rel err {a1i:.2e}; d(Q^n A) = block-avg square flux (n=3,9): rel err {a1ii:.2e} -> {'PASS' if A1 else 'FAIL'}")

# A2 counting (in-plane; transverse coordinates fixed)
a2 = True; rep = []
for n in (3, 9):
    cp = np.zeros((2 * n, 2 * n), int); cmu = np.zeros((2 * n, 2 * n + 1), int)
    for y0 in range(n):
        for y1 in range(n):
            cp[y0:y0 + n, y1:y1 + n] += 1
            for a in range(n):
                cmu[y0 + a, y1] += 1; cmu[y0 + a, y1 + n] += 1
    rep.append(f"n={n}: max plaq count {cp.max()} (bound {n*n}), max link count {cmu.max()} (bound {2*n})")
    a2 &= (cp.max() <= n * n) and (cmu.max() <= 2 * n)
say("A2 " + "; ".join(rep) + f" -> {'PASS' if a2 else 'FAIL'}")

# A3 cone inequality
def chain_ratio(B0, rs, k):
    """B0 level-0 field; rs[i] level-(i+1) residual; returns max ratio, sum|dBk|^2, total energy."""
    B = B0
    for i in range(k):
        B = Qstr(B, 3) - rs[i]
    S0 = B0.shape[1]; n = 3 ** k
    worst = 0.0; num = 0.0
    Etot = 0.5 * sum(np.sum(dplaq(B0, m, v) ** 2) for (m, v) in PLANES) + sum(0.5 * KAPPA * np.sum(r ** 2) for r in rs)
    for (m, v) in PLANES:
        dBk = dplaq(B, m, v)
        ext = [n, n, n, n]; ext[m] = 2 * n - 1; ext[v] = 2 * n - 1
        E = 0.5 * sample(box_sum(dplaq(B0, m, v) ** 2, ext), n)
        for i in range(k):
            mm = 3 ** (k - 1 - i)
            e_mu = [mm] * 4; e_mu[m] = 2 * mm - 1; e_mu[v] = 2 * mm
            e_nu = [mm] * 4; e_nu[m] = 2 * mm; e_nu[v] = 2 * mm - 1
            E = E + 0.5 * KAPPA * (sample(box_sum(rs[i][m] ** 2, e_mu), mm) + sample(box_sum(rs[i][v] ** 2, e_nu), mm))
        ratio = dBk ** 2 / np.maximum(E, 1e-300)
        worst = max(worst, float(ratio.max())); num += float(np.sum(dBk ** 2))
    return worst, num / Etot

a3 = True; lines = []; glob = 0.0
for k in (1, 2):
    S0 = 3 ** k * T
    for sc in (0.0, 0.3, 1.0, 3.0, 10.0):
        B0 = rng.standard_normal((4,) + (S0,) * 4)
        rs = [sc * rng.standard_normal((4,) + (S0 // 3 ** (i + 1),) * 4) for i in range(k)]
        w, g = chain_ratio(B0, rs, k); glob = max(glob, g)
        lines.append(f"k={k} sc={sc}: {w:.3f}"); a3 &= w <= C_LOC
    # (a) constant flux in plane 12
    x = np.indices((S0,) * 4)
    F = 2 * np.pi / S0  # one flux quantum over the torus (periodic)
    B0 = np.zeros((4,) + (S0,) * 4); B0[1] = F * x[0]   # dB_{01} = F except on the periodic seam (any field is a valid instance)
    rs = [np.zeros((4,) + (S0 // 3 ** (i + 1),) * 4) for i in range(k)]
    w, _ = chain_ratio(B0, rs, k)
    lines.append(f"k={k} constflux: {w:.3f}"); a3 &= w <= C_LOC
    # (b) residual pattern +c lower half / -c upper half of each level-(i+1) block in the nu direction
    B0 = rng.standard_normal((4,) + (S0,) * 4) * 0.1
    rs = []
    for i in range(k):
        Si = S0 // 3 ** (i + 1); r = np.zeros((4,) + (Si,) * 4)
        mm = 3 ** (k - 1 - i); idx = np.indices((Si,) * 4)[1] % max(mm, 1)
        r[0] = np.where(idx < mm / 2, 1.0, -1.0); rs.append(r)
    w, _ = chain_ratio(B0, rs, k)
    lines.append(f"k={k} pattern: {w:.3f}"); a3 &= w <= C_LOC
# (c) random-search ascent at k = 1
S0 = 9; best = 0.0
for start in range(4):
    B0 = rng.standard_normal((4,) + (S0,) * 4); r0 = rng.standard_normal((4,) + (3,) * 4)
    cur, _ = chain_ratio(B0, [r0], 1)
    for step in range(50):
        B1 = B0 + 0.3 * rng.standard_normal(B0.shape); r1 = r0 + 0.3 * rng.standard_normal(r0.shape)
        wv, _ = chain_ratio(B1, [r1], 1)
        if wv > cur:
            cur, B0, r0 = wv, B1, r1
    best = max(best, cur)
lines.append(f"k=1 ascent(4x50): {best:.3f}"); a3 &= best <= C_LOC
say("A3 max ratio |dB_k(P)|^2/E_C(P) vs C_loc=%.0f: " % C_LOC + "; ".join(lines) + f" -> {'PASS' if a3 else 'FAIL'}")
say(f"A4 (info) max sum_P|dB_k|^2/E(chain) = {glob:.4f} vs 12*C_loc = {12*C_LOC:.0f}")

# ---------------- Part B: d(M) for SU(2), SU(3) ----------------
def rand_su(N, rng):
    H = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    Y = (H - H.conj().T) / 2; Y -= np.trace(Y) / N * np.eye(N)
    return Y / np.linalg.norm(Y)

def Pi(Z):
    N = Z.shape[0]; A = (Z - Z.conj().T) / 2
    return A - np.trace(A) / N * np.eye(N)

def haar_su(N, rng):
    Z = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) / np.sqrt(2)
    Q, R = np.linalg.qr(Z); Q = Q * (np.diag(R) / np.abs(np.diag(R)))
    return Q / np.linalg.det(Q) ** (1.0 / N)

def maximiser(M):
    N = M.shape[0]; X = np.zeros((N, N), complex)
    for it in range(400):
        G = Pi(expm(-X) @ M)
        X = X + G
        if np.linalg.norm(G) < 1e-15:
            break
    return expm(X), np.linalg.norm(G)

def dM(M):
    N = M.shape[0]
    W0, res = maximiser(M)
    trP = np.sum(np.linalg.svd(M, compute_uv=False))
    return (trP - np.real(np.trace(np.linalg.inv(W0) @ M))) / N, W0, res

def make_M(dirs, us, y):
    return sum(expm(y * u * D) for D, u in zip(dirs, us)) / len(dirs)

YS = [0.02, 0.04, 0.08, 0.16]; J = 8
b1max = 0.0; b2min = 1.0; worst_comp = -1.0; maxres = 0.0
for N, nsamp in ((2, 200), (3, 200)):
    for s in range(nsamp):
        dirs = [rand_su(N, rng) for _ in range(J)]; us = rng.uniform(0.2, 1.0, J)
        for y in YS:
            M = make_M(dirs, us, y)
            d, W0, res = dM(M); maxres = max(maxres, res)
            b2min = min(b2min, d)
            if N == 2:
                b1max = max(b1max, d)
            if s < 10 and y == YS[-1]:
                F0 = np.real(np.trace(np.linalg.inv(W0) @ M))
                for c in range(200):
                    if c < 100:
                        Wc = W0 @ expm(10 ** rng.uniform(-6, 0) * rand_su(N, rng))
                    else:
                        Wc = haar_su(N, rng)
                    worst_comp = max(worst_comp, np.real(np.trace(np.linalg.inv(Wc) @ M)) - F0)
B1 = b1max <= 1e-13; B2 = b2min >= -1e-13
say(f"B1 SU(2) max d(M) = {b1max:.2e} -> {'PASS' if B1 else 'FAIL'};  B2 min d(M) (both) = {b2min:.2e} -> {'PASS' if B2 else 'FAIL'}")
say(f"   maximiser check: max(F(competitor) - F(W0)) = {worst_comp:.2e} (<= 1e-14 means W0 global); max fixed-point residual {maxres:.1e}")

slopes = []; ratios = []
for s in range(50):
    dirs = [rand_su(3, rng) for _ in range(J)]; us = rng.uniform(0.2, 1.0, J)
    ds = []
    for y in YS:
        M = make_M(dirs, us, y); d, _, _ = dM(M); ds.append(d)
        trP = np.sum(np.linalg.svd(M, compute_uv=False)); al = np.angle(np.linalg.det(M))
        if y == 0.08:
            ratios.append(d / ((trP / 3) * al ** 2 / 18) if al != 0 else np.nan)
    ds = np.array(ds)
    if np.all(ds > 0):
        slopes.append(np.polyfit(np.log(YS), np.log(ds), 1)[0])
med = float(np.median(slopes)) if slopes else float('nan')
B3 = 5.5 <= med <= 6.5
say(f"B3 SU(3) median slope of log d vs log y = {med:.3f} (n={len(slopes)}/50; range {min(slopes):.2f}..{max(slopes):.2f}) -> {'PASS' if B3 else 'FAIL'}")

b4 = 0.0
for N in (2, 3):
    for s in range(20):
        dirs = [rand_su(N, rng) for _ in range(J)]; us = rng.uniform(0.2, 1.0, J)
        M = make_M(dirs, us, 0.16); d, W0, _ = dM(M)
        U, Sv, Vh = np.linalg.svd(M); W = U @ Vh; P = Vh.conj().T @ np.diag(Sv) @ Vh
        F0 = np.real(np.trace(np.linalg.inv(W0) @ M))
        for c in range(50):
            V = haar_su(N, rng); Vi = np.linalg.inv(V)
            kt = np.real(np.trace((np.eye(N) - Vi @ W) @ P)) / N
            ph = (F0 - np.real(np.trace(Vi @ M))) / N
            b4 = max(b4, abs(kt - ph - d))
B4 = b4 <= 1e-12
say(f"B4 |k~ - phi - d| max = {b4:.2e} -> {'PASS' if B4 else 'FAIL'}")
rat = np.array([r for r in ratios if np.isfinite(r)])
say(f"B5 (info) d / ((trP/N) alpha^2/(2N^2)) at y=0.08, SU(3): median {np.median(rat):.4f}, range {rat.min():.4f}..{rat.max():.4f}")

ok = A1 and a2 and a3 and B1 and B2 and B3 and B4
say(f"OVERALL: {'PASS' if ok else 'FAIL'}  (A1 {A1}, A2 {a2}, A3 {a3}, B1 {B1}, B2 {B2}, B3 {B3}, B4 {B4})")
say(f"time {time.time()-t0:.1f} s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576:.0f} MB")
