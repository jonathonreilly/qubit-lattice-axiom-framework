#!/usr/bin/env python3
"""p3: lane E session 3 checks (criteria: checks/p3_criteria.md). Elementary statements only."""
import math
import numpy as np
from math import erfc, sqrt, pi, exp, log, sin, asin

rng = np.random.default_rng(20261028)
out = []
def rep(s):
    out.append(s); print(s)

# ---------------- A. Lemma TL ----------------
def haar_su(N):
    Z = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) / sqrt(2)
    Q, R = np.linalg.qr(Z)
    d = np.diag(R); Q = Q * (d / abs(d))
    Q = Q / np.linalg.det(Q) ** (1.0 / N)
    return Q

def expm_herm_i(X):
    # X anti-Hermitian: X = i H; exp via eigen-decomposition of H = -iX
    H = -1j * X; H = (H + H.conj().T) / 2
    w, V = np.linalg.eigh(H)
    return (V * np.exp(1j * w)) @ V.conj().T

def principal_log(U):
    # U unitary: diagonalise the commuting Hermitian combination Im U + c Re U (orthonormal eigenbasis)
    Hr = (U + U.conj().T) / 2; Ki = (U - U.conj().T) / 2j
    _, Q = np.linalg.eigh(Ki + 0.3719 * Hr)
    D = Q.conj().T @ U @ Q
    th = np.angle(np.diag(D))
    th = np.where(th < -pi + 1e-9, th + 2 * pi, th)   # principal branch (-pi, pi]
    return Q, th

def TL(U):
    N = U.shape[0]
    Q, th = principal_log(U)
    m = int(round(th.sum() / (2 * pi)))
    thp = th.copy()
    order = np.argsort(th)
    if m > 0:
        for j in order[::-1][:m]:
            thp[j] -= 2 * pi
    elif m < 0:
        for j in order[:(-m)]:
            thp[j] += 2 * pi
    X = (Q * (1j * thp)) @ Q.conj().T
    Xp = (Q * (1j * th)) @ Q.conj().T
    return X, Xp, m

def opn(A): return np.linalg.norm(A, 2)
def hsn(A): return np.linalg.norm(A, 'fro')

A_ok = {k: True for k in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']}
worst = {k: 0.0 for k in ['A1', 'A2', 'A3']}
counts = {}
for N in (2, 3, 4):
    samples = [haar_su(N) for _ in range(2000)]
    cents = [np.exp(2j * pi * j / N) * np.eye(N) for j in range(N)]
    near = []
    for _ in range(200):
        j = rng.integers(N)
        H = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N)); H = (H + H.conj().T) / 2
        H -= np.trace(H) / N * np.eye(N)
        near.append(np.exp(2j * pi * j / N) * expm_herm_i(1j * 1e-6 * H / opn(H)))
    allS = samples + cents + near + ([-np.eye(2)] if N == 2 else [])
    nprin = 0
    for U in allS:
        X, Xp, m = TL(U)
        e1 = opn(expm_herm_i(X) - U); worst['A1'] = max(worst['A1'], e1)
        if e1 > 1e-10: A_ok['A1'] = False
        e2 = abs(np.trace(X)); worst['A2'] = max(worst['A2'], e2)
        if e2 > 1e-10: A_ok['A2'] = False
        I = np.eye(N)
        r3 = hsn(I - U) - hsn(X) * (1 + 1e-12) - 1e-14
        worst['A3'] = max(worst['A3'], hsn(I - U) / max(hsn(X), 1e-300) if hsn(X) > 0 else 0)
        if r3 > 0 or opn(I - U) > hsn(I - U) + 1e-14: A_ok['A3'] = False
        if opn(X) > 3 * pi + 1e-10: A_ok['A4'] = False
        if opn(I - U) < 2 * sin(pi / N):
            nprin += 1
            if opn(X - Xp) > 1e-10: A_ok['A5'] = False
    for j in range(1, N):
        U = cents[j]
        _, Xp, m = TL(U)
        if abs(np.trace(Xp)) < 1.0: A_ok['A6'] = False
    counts[N] = (len(allS), nprin)
rep("A Lemma TL: samples (total, in principal domain) per N: %s" % counts)
rep("A worst: ||e^TL-U||=%.2e |trTL|=%.2e max||1-U||_HS/|TL|_HS=%.6f" % (worst['A1'], worst['A2'], worst['A3']))
for k in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']:
    rep("  %s %s" % (k, 'PASS' if A_ok[k] else 'FAIL'))

# ---------------- B. HS-net / HS vs exact ----------------
def chi3_sf(x):
    return erfc(x / sqrt(2)) + sqrt(2 / pi) * x * exp(-x * x / 2)

B1 = B2 = True; B4_found = False; minr1 = minr2 = float('inf')
for sig in (1.0, 2.0):
    for g in (0.05, 0.1, 0.2):
        for x in (0.5, 1, 2, 3, 5, 8):
            tau = x * sig * g
            for nA in (1, 3, 10):
                ex = chi3_sf(x) ** nA
                b1 = (125 * exp(-(49 / 128) * tau ** 2 / (sig ** 2 * g ** 2))) ** nA
                b2 = ((2 * sqrt(2)) ** 3 * exp(-tau ** 2 / (4 * sig ** 2 * g ** 2))) ** nA
                b4 = exp(-tau ** 2 / (2 * sig ** 2 * g ** 2)) ** nA
                if ex > 0:
                    minr1 = min(minr1, b1 / ex); minr2 = min(minr2, b2 / ex)
                if b1 < ex: B1 = False
                if b2 < ex: B2 = False
                if b4 < ex: B4_found = True
rep("B1 HS-net bound >= exact: %s (min bound/exact = %.3g)" % ('PASS' if B1 else 'FAIL', minr1))
rep("B2 HS (Gaussian-xi) bound >= exact: %s (min bound/exact = %.3g)" % ('PASS' if B2 else 'FAIL', minr2))
# B3 net on S^2
P = rng.standard_normal((20000, 3)); P /= np.linalg.norm(P, axis=1)[:, None]
net = []
for v in P:
    if not net or np.min(np.linalg.norm(np.array(net) - v, axis=1)) > 0.5:   # greedy delta-separated, delta = 1/2
        net.append(v)
net = np.array(net)
Vt = rng.standard_normal((100000, 3)); Vt /= np.linalg.norm(Vt, axis=1)[:, None]
cov = np.max(Vt @ net.T, axis=1)
B3 = (len(net) <= 125) and (cov.min() >= 0.875 - 1e-3)
rep("B3 net: %d points (<=125), min_v max_u <u,v> = %.5f (>= 0.875; tol 1e-3): %s" % (len(net), cov.min(), 'PASS' if B3 else 'FAIL'))
rep("B4 negative control (prefactor-1 bound violated somewhere): %s" % ('PASS (violated, discriminating)' if B4_found else 'FAIL'))
# B5 Gaussian CGF and threshold algebra
nA = 5; rho = 0.4; v_diag = 1.0
C = (1 - rho) * np.eye(nA) + rho * np.ones((nA, nA))   # scalar component along u, per plaquette
Ls = np.linalg.cholesky(C)
Xs = rng.standard_normal((100000, nA)) @ Ls.T
t = 0.7
Y = np.exp(t * Xs.sum(axis=1))
mc = Y.mean(); se = Y.std() / sqrt(len(Y))
v = C.sum() / nA
theo = exp(0.5 * t * t * v * nA)
B5a = abs(mc - theo) <= 3 * se
sig, g, m, e1 = 1.3, 0.1, 0.7, 0.05
tt = e1 / (sig ** 2 * g ** 2)
vstar = sig ** 2 * g ** 2 + 2 * m * sig ** 2 * g ** 3 / e1
lhs = 0.5 * tt ** 2 * vstar; rhs = 0.5 * sig ** 2 * g ** 2 * tt ** 2 + m * g * tt
B5b = abs(lhs - rhs) <= 1e-12 * max(1, abs(rhs))
rep("B5 Gaussian CGF MC %.5f vs exact %.5f (3se = %.5f): %s; threshold crossing |lhs-rhs| = %.1e: %s" % (
    mc, theo, 3 * se, 'ok' if B5a else 'bad', abs(lhs - rhs), 'ok' if B5b else 'bad'))
rep("  B5 %s" % ('PASS' if (B5a and B5b) else 'FAIL'))

# ---------------- C. arithmetic ----------------
target = log(24 * 3 ** 4) / log(3)
N = 2
while not (11 * N * N / (6 * pi * pi * (N - 1)) > target): N += 1
rep("C1 smallest N with 11N^2/(6pi^2(N-1)) > %.4f: N = %d: %s" % (target, N, 'PASS' if N == 37 else 'FAIL'))
def smallestN(alpha, t):
    N = 2
    while not (alpha(N) * t * t * 11 * N * N / (12 * pi * pi) > target): N += 1
    return N
res = {}
for an, al in (('1/(2N)', lambda N: 1 / (2 * N)), ('1/(2(N-1))', lambda N: 1 / (2 * (N - 1)))):
    for t in (0.5, 2 / 117):
        res[(an, t)] = smallestN(al, t)
okC2 = all(550 <= res[(a, 0.5)] <= 650 for a in ('1/(2N)', '1/(2(N-1))')) and all(4e5 <= res[(a, 2 / 117)] <= 6e5 for a in ('1/(2N)', '1/(2(N-1))'))
rep("C2 smallest N (alpha, t): %s: %s" % ({'%s,t=%.4g' % k: v for k, v in res.items()}, 'PASS' if okC2 else 'FAIL'))
okC3 = True; worst3 = 0
for p in (3, 24, 192):
    for da in (0.01, 0.1, 1.0):
        xs = np.exp(np.linspace(log(1e-6), log(1e7), 200001))
        f = (p / 2) * np.log(xs) - da * xs
        i = np.argmax(f)
        # refine by golden section on log scale
        lo, hi = xs[max(i - 1, 0)], xs[min(i + 1, len(xs) - 1)]
        for _ in range(200):
            a1 = lo + (hi - lo) * 0.382; a2 = lo + (hi - lo) * 0.618
            if (p / 2) * log(a1) - da * a1 > (p / 2) * log(a2) - da * a2: hi = a2
            else: lo = a1
        xm = (lo + hi) / 2
        num = (p / 2) * log(xm) - da * xm
        cl = (p / 2) * log(p / (2 * math.e * da))
        rel = abs(num - cl) / max(1, abs(cl))
        worst3 = max(worst3, rel)
        if rel > 1e-9: okC3 = False
rep("C3 sup x^{p/2}e^{-(a-a')x} closed form (log, rel err %.1e): %s" % (worst3, 'PASS' if okC3 else 'FAIL'))
okC4 = True; minmargin = float('inf')
for L in (3, 5):
    Ad = 1.5 * L * (L - 1)
    c1 = 1 / (2 * (L * L + 5.5 * Ad))
    for e1 in np.linspace(0.517 / 200, 0.517, 200):
        lo = 1.001 * L * L * c1 * e1
        for eps in np.linspace(lo, e1, 200, endpoint=False):
            th = 2 * asin(eps / 2)
            val = 2 * sin(th / (2 * L * L))
            if not (th < pi / 6 and val > c1 * e1): okC4 = False
            minmargin = min(minmargin, val / (c1 * e1))
rep("C4 INH: theta<pi/6 and 2sin(theta/(2L^2)) > c_1 eps_1 on grids (L=3,5); min ratio %.6f: %s" % (minmargin, 'PASS' if okC4 else 'FAIL'))
L = 3; c1 = 1 / 117
mt = {}
for CI in (1.0, 1.5, 2.0):
    m = 0
    while not ((L * L / (2 * CI)) ** m * c1 >= 2 * CI / (L * L)): m += 1
    mt[CI] = m
rep("C5 descent depth m_tau (L=3) for C_I=1,1.5,2: %s (informational)" % mt)
nc = 1e13; a = 1e-40
lhs = log(2 * nc + 1) * 4 + log(a); rhs = log(3 * 10 * 0.007)
rep("C6 log((2n_c+1)^4 a) = %.2f > log(3 kappa eps) = %.2f: %s" % (lhs, rhs, 'PASS' if lhs > rhs else 'FAIL'))

allpass = all(A_ok.values()) and B1 and B2 and B3 and B4_found and B5a and B5b and N == 37 and okC2 and okC3 and okC4 and lhs > rhs
rep("SUMMARY: %s" % ('ALL PASS' if allpass else 'SOME FAIL'))
