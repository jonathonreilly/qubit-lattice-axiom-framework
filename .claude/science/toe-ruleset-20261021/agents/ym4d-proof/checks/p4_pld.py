#!/usr/bin/env python3
"""p4 (lane E, session 4): checks of PLD.md section 16 against checks/p4_criteria.md (written first).
Elementary statements and arithmetic only. Prints a SUMMARY line. Keep stdout short."""
import itertools
import numpy as np
import mpmath as mp

rng = np.random.default_rng(20261028)
results = {}

# ---------- SU(2) helpers ----------
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def opn(A):
    return np.linalg.norm(A, 2)


def haar_su2(n):
    q = rng.normal(size=(n, 4))
    q /= np.linalg.norm(q, axis=1, keepdims=True)
    a = q[:, 0] + 1j * q[:, 3]
    b = q[:, 2] + 1j * q[:, 1]
    U = np.zeros((n, 2, 2), dtype=complex)
    U[:, 0, 0] = a
    U[:, 0, 1] = -np.conj(b)
    U[:, 1, 0] = b
    U[:, 1, 1] = np.conj(a)
    return U


def expsu2(alpha, nvec):
    # exp(i alpha n.sigma) for unit n
    H = nvec[0] * sx + nvec[1] * sy + nvec[2] * sz
    return np.cos(alpha) * I2 + 1j * np.sin(alpha) * H


def near_one(n, scale):
    out = []
    for _ in range(n):
        v = rng.normal(size=3)
        v /= np.linalg.norm(v)
        out.append(expsu2(scale * rng.random(), v))
    return np.array(out)


def unit3():
    v = rng.normal(size=3)
    return v / np.linalg.norm(v)


# ---------- A1 / A1n: kernel tail vs bound (quadrature) ----------
mp.mp.dps = 30


def tail(b, s):
    f = lambda w: mp.e ** (-b * w) * mp.sqrt(w * (2 - w))
    pts0 = sorted(set([mp.mpf(0)] + [mp.mpf(x) for x in (1.0 / b, 10.0 / b, 100.0 / b) if x < 2] + [mp.mpf(2)]))
    Z = mp.quad(f, pts0)
    pts1 = sorted(set([mp.mpf(s)] + [mp.mpf(x) for x in (s + 1.0 / b, s + 10.0 / b, s + 100.0 / b) if x < 2] + [mp.mpf(2)]))
    T = mp.quad(f, pts1)
    return T / Z


A1_ok, A1n_fail_found = True, False
worst = mp.mpf(0)
for b in (1, 10, 100, 1000, 10000):
    for s in (0.01, 0.1, 0.5, 1.0, 1.5):
        T = tail(mp.mpf(b), mp.mpf(s))
        for lam in (0.25, 0.5, 0.75, 0.9):
            B = (1 - mp.mpf(lam)) ** mp.mpf(-1.5) * mp.e ** (-mp.mpf(lam) * b * s)
            if B < T * (1 - mp.mpf('1e-20')):
                A1_ok = False
            if T > 0:
                worst = max(worst, T / B)
            if mp.e ** (-mp.mpf(lam) * b * s) < T:
                A1n_fail_found = True
results['A1'] = A1_ok
results['A1n'] = A1n_fail_found
print(f"A1 kernel tail <= (1-l)^-1.5 e^(-l b s): {A1_ok} (max exact/bound {mp.nstr(worst, 5)}); A1n prefactor-free bound fails somewhere: {A1n_fail_found}")

# ---------- A2 ----------
V = haar_su2(20000)
Wh = haar_su2(20000)
r = rng.random(20000) * 0.999 + 0.001
err_phi = 0.0
for i in range(20000):
    M = r[i] * Wh[i]
    phi = r[i] - 0.5 * np.real(np.trace(np.linalg.inv(V[i]) @ M))
    rhs = r[i] * opn(V[i] - Wh[i]) ** 2 / 2
    err_phi = max(err_phi, abs(phi - rhs))
err_lin = 0.0
for i in range(5000):
    n = rng.integers(1, 13)
    Us = haar_su2(n) if rng.random() < 0.5 else near_one(n, 0.5)
    M = Us.mean(axis=0)
    err_lin = max(err_lin, opn(M.conj().T @ M - opn(M) ** 2 * I2))
results['A2'] = err_phi < 1e-12 and err_lin < 1e-12
print(f"A2 phi identity err {err_phi:.1e}; real-combination err {err_lin:.1e}: {results['A2']}")

# ---------- A3 ----------
viol = 0
for i in range(20000):
    if i % 2 == 0:
        Vs = haar_su2(4)
        Ws = haar_su2(4)
    else:
        Ws = near_one(4, 0.3)
        Vs = np.array([Ws[j] @ near_one(1, 0.2)[0] for j in range(4)])
    hol = lambda X: X[0] @ X[1] @ np.linalg.inv(X[2]) @ np.linalg.inv(X[3])
    lhs = opn(I2 - hol(Vs))
    rhs = opn(I2 - hol(Ws)) + sum(opn(Vs[j] - Ws[j]) for j in range(4))
    if lhs > rhs + 1e-12:
        viol += 1
results['A3'] = viol == 0
print(f"A3 plaquette telescoping violations: {viol}")

# ---------- B1 / B1n ----------
viol1, viol_f1 = 0, 0
for i in range(20000):
    n = rng.integers(1, 9)
    Us = haar_su2(n) if i % 2 == 0 else near_one(n, 1.0)
    M0 = Us.mean(axis=0)
    k = rng.integers(0, n)
    Us2 = Us.copy()
    Us2[k] = Us2[k] @ near_one(1, rng.random() * 2.0)[0]
    M = Us2.mean(axis=0)
    r0, r1 = opn(M0), opn(M)
    if r0 < 1e-6 or r1 < 1e-12:
        continue
    lhs = opn(M / r1 - M0 / r0)
    if lhs > 2 * opn(M - M0) / r0 + 1e-12:
        viol1 += 1
    if lhs > opn(M - M0) / r0 + 1e-12:
        viol_f1 += 1
# explicit pair: r0 = 1, r = 1/2, opposite directions
M0 = I2.copy()
M = 0.5 * expsu2(np.pi / 2, np.array([0, 0, 1.0]))  # i sigma_z, eigenvalues +-i ; use -1 for opposite
M = 0.5 * (-I2)
lhs = opn(M / 0.5 - M0 / 1.0)
explicit_fail = lhs > opn(M - M0) / 1.0 + 1e-12
results['B1'] = viol1 == 0
results['B1n'] = (viol_f1 > 0) or explicit_fail
print(f"B1 polar Lipschitz (factor 2) violations: {viol1}; B1n factor-1 violations: {viol_f1} (explicit pair fails: {explicit_fail})")

# ---------- B2 ----------
viol2 = 0
for t in range(2000):
    npool = 30
    pool = near_one(npool, 1.0) if t % 2 else haar_su2(npool)
    nc = rng.integers(2, 15)
    ell = rng.integers(1, 7)
    contours = [rng.choice(npool, size=ell, replace=False) for _ in range(nc)]
    E = set(rng.choice(npool, size=rng.integers(1, 6), replace=False).tolist())
    delta = rng.random() * 0.5
    pool2 = pool.copy()
    for e in E:
        pool2[e] = pool[e] @ expsu2(rng.random() * 0.25 * delta, unit3())  # ||U-U'|| <= 2 sin(.) <= delta/2
    dmax = max(opn(pool2[e] - pool[e]) for e in E)

    def T(pl, c):
        X = I2.copy()
        for e in c:
            X = X @ pl[e]
        return X
    M1 = np.mean([T(pool, c) for c in contours], axis=0)
    M2 = np.mean([T(pool2, c) for c in contours], axis=0)
    meet = [len(E.intersection(set(c.tolist()))) for c in contours]
    f = sum(1 for m in meet if m > 0) / nc
    ellE = max(meet)
    if opn(M1 - M2) > f * ellE * dmax + 1e-12:
        viol2 += 1
results['B2'] = viol2 == 0
print(f"B2 contour-average dilution bound violations: {viol2}")

# ---------- C: toy Proposition CC ----------
eps1, g, kappa = 0.02, 1e-3, 1.0
b = kappa / g ** 2
delta = g


def sample_kernel(W, n):
    # V with V^{-1} W = exp(i alpha n.sigma), w = 1 - cos alpha ~ density prop. e^{-b w} sqrt(w(2-w))
    out = np.zeros((n, 2, 2), dtype=complex)
    k = 0
    while k < n:
        w = rng.gamma(1.5, 1.0 / b, size=2 * (n - k))
        acc = (w < 2) & (rng.random(w.size) < np.sqrt(np.clip(2 - w, 0, 2) / 2))
        for wv in w[acc]:
            if k >= n:
                break
            al = np.arccos(1 - wv)
            out[k] = W @ np.linalg.inv(expsu2(al, unit3()))
            k += 1
    return out


def toy_freq(centre_eps, nsamp):
    # centres: x1 = exp(i th sz /2)... choose x1 with plaquette e^{i th sz}, others identity
    th = 2 * np.arcsin(centre_eps / 2)  # ||1 - e^{i th sz}|| = 2 sin(th/2)
    X1 = expsu2(th, np.array([0, 0, 1.0]))
    cen = [X1, I2, I2, I2]
    S = [sample_kernel(cen[j], nsamp) for j in range(4)]
    hits = 0
    for i in range(nsamp):
        P = S[0][i] @ S[1][i] @ np.linalg.inv(S[2][i]) @ np.linalg.inv(S[3][i])
        if opn(I2 - P) >= eps1:
            hits += 1
    return hits / nsamp


fC = toy_freq(eps1 - delta / 8, 100000)
fCn = toy_freq(eps1 / 2, 100000)
# exact Haar measure of op-ball radius r in SU(2): class angle psi, ||1-U|| = 2 sin(psi/2), density (2/pi) sin^2 psi
mp.mp.dps = 30
rad = mp.mpf(delta) / 16
psi_r = 2 * mp.asin(rad / 2)
m_r = (2 / mp.pi) * mp.quad(lambda p: mp.sin(p) ** 2, [0, psi_r])
lbC = m_r ** 4 * mp.e ** (-2 * b * delta ** 2)
results['C1'] = fC >= 0.05
results['C2'] = mp.mpf(fC) >= lbC
results['C1n'] = fCn < 1e-3
print(f"C toy: P(bad | centre eps1-delta/8) = {fC:.4f} (C1 >= 0.05: {results['C1']}); proven toy lower bound {mp.nstr(lbC, 4)} (C2: {results['C2']}); C1n centre eps1/2: {fCn:.1e} ({results['C1n']})")

# ---------- D1 recursion ----------
a, R = mp.mpf('1e-86'), mp.mpf(10)
D1 = {}
for eta in (mp.mpf(1) / 243, mp.mpf('0.5') / 243, mp.mpf(1), mp.mpf(1) / 81):
    C = mp.mpf(1)
    for k in range(400):
        C = max(mp.mpf(1), 243 * eta * mp.e ** (a * R) * C)
    D1[mp.nstr(eta, 4)] = C
ok_D1 = (D1[mp.nstr(mp.mpf(1) / 243, 4)] <= 1 + mp.mpf('1e-60') and D1[mp.nstr(mp.mpf('0.5') / 243, 4)] <= 1
         and D1[mp.nstr(mp.mpf(1), 4)] >= mp.mpf(10) ** 100 and D1[mp.nstr(mp.mpf(1) / 81, 4)] >= mp.mpf(10) ** 100)
results['D1'] = bool(ok_D1)
print("D1 C(400) by eta: " + ", ".join(f"{k}: {mp.nstr(v, 4)}" for k, v in D1.items()) + f" -> {ok_D1}")

# ---------- D2 shadows ----------
OFF = list(itertools.product((-1, 0, 1), repeat=4))


def N1(A):
    return {tuple(z[i] + o[i] for i in range(4)) for z in A for o in OFF}


def proj(A):
    return {tuple(zi // 3 for zi in z) for z in A}


def Sig(A):
    return N1(proj(A))


def shadows(A, M):
    out, cur = [], set(A)
    for _ in range(M):
        cur = Sig(cur)
        out.append(cur)
    return out


Mlev = 10
D2a, D2b_ok, D2d_ok = True, True, True
max_excess = 0
DELTA = 81 + 2401 * 32 * 80 * mp.mpf(1) / 2  # sum_{m>=1} 3^{-m} = 1/2
for Q in [(0, 0, 0, 0), (1, 2, 0, 1), (2, 2, 2, 2), (-1, 4, 7, -3)]:
    shQ = shadows({Q}, Mlev)
    for m in range(Mlev):
        if len(shQ[m]) > 2401 * (16 + 0):
            D2d_ok = False
    for dx in itertools.product(range(3), repeat=4):
        x = tuple(3 * Q[i] + dx[i] for i in range(4))
        shx = shadows({x}, Mlev + 1)  # shx[0] = level k (N1(Q)), shx[m] = level k+m
        if not shx[0] >= {Q}:
            D2a = False
        exc = len(shx[0])
        for m in range(1, Mlev + 1):
            if not shx[m] >= shQ[m - 1]:
                D2a = False
            exc += len(shx[m]) - len(shQ[m - 1])
            if len(shx[m]) > 2401 * 16:
                D2d_ok = False
        max_excess = max(max_excess, exc)
        if exc > DELTA:
            D2b_ok = False
Q1, Q2 = (0, 0, 0, 0), (1, 0, 0, 0)
s1, s2, s12 = shadows({Q1}, Mlev), shadows({Q2}, Mlev), shadows({Q1, Q2}, Mlev)
D2c_ok, ratios = True, []
for m in range(Mlev):
    if len(s12[m]) > len(s1[m]) + len(s2[m]):
        D2c_ok = False
    ratio = len(s12[m]) / max(len(s1[m]), len(s2[m]))
    ratios.append(round(ratio, 3))
    if ratio > 2:
        D2c_ok = False
    if len(s12[m]) > 2401 * (16 + 32 * 1 * 3.0 ** (-(m + 1))):
        D2d_ok = False
results['D2a'], results['D2b'], results['D2c'], results['D2d'] = D2a, D2b_ok, D2c_ok, D2d_ok
print(f"D2a monotone {D2a}; D2b max excess {max_excess} <= {int(DELTA)}: {D2b_ok}; D2c pair/single ratios {ratios}: {D2c_ok}; D2d H-geo(iii): {D2d_ok}")
print(f"   |sh_m(Q)| m=1..{Mlev}: {[len(s) for s in s1]}")

# ---------- E arithmetic ----------
mp.mp.dps = 40
c_pr = mp.mpf(1) / (640 * 53 ** 2)
kmin = 256 * c_pr / (24 * mp.mpf('0.5'))
E1 = abs(c_pr / mp.mpf('5.5625e-7') - 1) < mp.mpf('1e-10') and kmin < mp.mpf('1.2e-5')
results['E1'] = bool(E1)
N, L, Ad = 2, 3, 9
etaq_over = min(mp.mpf(1) / (2 * L ** 2), mp.mpf(1) / (256 * N * Ad))
E2_ok = etaq_over == mp.mpf(1) / 4608
out_E2 = []
for lmin in (mp.mpf('3.17e-3'), mp.mpf('4.23e-3')):
    sig2 = 16 / lmin
    a_fl = 49 * etaq_over ** 2 / (1024 * sig2)
    a_J = mp.mpf(1) / 4096
    a_KN = (mp.mpf(35) / 256) ** 2 / 128
    a_ret = min(a_fl, a_J, a_KN)
    out_E2.append((lmin, sig2, a_fl, a_J, a_KN, a_ret, a_ret / c_pr))
lm, sig2, a_fl, a_J, a_KN, a_ret, rat = out_E2[0]
E2_ok = E2_ok and a_ret == a_fl and abs(rat / mp.mpf('8.0e-7') - 1) < mp.mpf('0.01') and abs(a_fl / mp.mpf('4.47e-13') - 1) < mp.mpf('0.01')
results['E2'] = bool(E2_ok)
print(f"E1 c_pr={mp.nstr(c_pr, 6)} kappa_min={mp.nstr(kmin, 5)}: {E1}")
for (lmin, s2, af, aj, ak, ar, rr) in out_E2:
    print(f"E2 lam_min={mp.nstr(lmin, 3)} sig_fl^2={mp.nstr(s2, 5)} a_fl/e1^2={mp.nstr(af, 4)} a_J/e1^2={mp.nstr(aj, 4)} a_KN/e1^2={mp.nstr(ak, 4)} a_ret/a_bad={mp.nstr(rr, 4)}")
print(f"E2 PASS: {E2_ok}")
e1 = mp.mpf('6.7e-40')
aret_abs = a_ret * e1 ** 2
sols = []
for p in (6, 12):
    for lnC in (0, 50):
        y = mp.mpf(1e90)
        for _ in range(200):
            y = ((12 + p) / mp.mpf(2) * mp.log(y) + lnC) / aret_abs
        sols.append(1 / y)
E3_ok = all(mp.mpf('1e-96') <= s <= mp.mpf('1e-93') for s in sols)
results['E3'] = bool(E3_ok)
print(f"E3 a_ret(eps1=6.7e-40)={mp.nstr(aret_abs, 4)}; ceilings g^2: {[mp.nstr(s, 3) for s in sols]}: {E3_ok}")
E4_ok = DELTA == 3073361
results['E4'] = bool(E4_ok)
print(f"E4 Delta_sh = {int(DELTA)}: {E4_ok}")
theta = mp.mpf(1) / 24 * (1 - mp.mpf('1e-12'))
entries = (mp.mpf(1) / 512, 6 * theta * c_pr)
E5_ok = min(entries) == entries[1]
results['E5'] = bool(E5_ok)
print(f"E5 a_A/a_bad = {mp.nstr(min(entries) / c_pr, 6)} (6theta entry binding: {E5_ok})")

allpass = all(results.values())
print("SUMMARY: " + ("ALL PASS" if allpass else "FAIL: " + ",".join(k for k, v in results.items() if not v)))
