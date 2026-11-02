"""w5: informational check for HW session 5 (Theorem CRC-2T, Lemma SH-att, two-level toy gas).
Criteria: checks/w5_criteria.md (written before this script). Never a proof."""
import itertools
import math
import random
import time

import mpmath as mp
import numpy as np

mp.mp.dps = 50
t0 = time.time()
res = {}

# ---------------- Part A: arithmetic of (S1), (S2), (T) ----------------
a = mp.mpf('1.0e-86'); beta = mp.mpf('0.186'); L = 3; a_ret = mp.mpf('2.0e-91')
rho = 8; c_att = 1 + 153664 * rho; Delta = (2 * rho + 1) ** 4 - 1
assert 6561 == 9 ** 4 and 531441 == 6561 * 81
cU = 1
A_ok = {k: True for k in ['A1', 'A2', 'A3', 'A4', 'A5']}
lines = []
for cA in [0, 1, 100]:
    cp = cA + cU
    b_n = 531441 * 38418 * cp + 38417 * cU
    b_D = 38416 * (531441 * cp + cU)
    for Cl in [1, 10 ** 6]:
        CA = Cl
        for R in [0, 10]:
            g2 = a / (b_n + a * R + mp.log(12800 * Cl))
            if not (mp.mpf('4.0e-97') <= g2 * cp <= mp.mpf('5.5e-97')):
                A_ok['A1'] = False
            nT = b_D / (a * beta * mp.log(L))
            if not (mp.mpf('5e96') <= nT / cp <= mp.mpf('2e97')):
                A_ok['A4'] = False
            nsh = max(mp.ceil(nT) - 1, mp.mpf('2e87'))

            def log_eps2(gk2):
                return nsh * mp.log(6400) + (nsh + 1) * (mp.log(2 * Cl) + b_n + a * R - a / gk2)

            def log_S1(gk2, rate):
                return mp.log(Delta ** 2 * CA) + rate * R + cp * c_att - rate / gk2
            gA2 = g2 / 2
            if not (log_eps2(gA2) <= mp.log(0.5) and log_S1(gA2, a) <= mp.log(0.5)):
                A_ok['A2'] = False
            if not (log_eps2(mp.mpf('1e-94')) > 0):
                A_ok['A3'] = False
            g2ret = a_ret / (cp * c_att + mp.log(2 * Delta ** 2 * CA))
            if cA >= 1 and not (mp.mpf('1.0e-97') <= g2ret * cp <= mp.mpf('2.0e-97')):
                A_ok['A5'] = False
            lines.append(f"cA={cA} Cl={Cl} R={R}: g2_CRC*c+={mp.nstr(g2*cp,4)} nT/c+={mp.nstr(nT/cp,4)} "
                         f"log_eps2(g2/2)={mp.nstr(log_eps2(gA2),3)} log_eps2(1e-94)={mp.nstr(log_eps2(mp.mpf('1e-94')),3)} "
                         f"g2_ret*c+={mp.nstr(g2ret*cp,4)}")
res.update(A_ok)
print("Part A")
for s in lines[::4]:
    print("  " + s)
print("  b_n(cA=0)=%d b_D(cA=0)=%d c_att=%d Delta_rho^2=%.4e" % (531441 * 38418 + 38417, 38416 * (531441 + 1), c_att, Delta ** 2))

# ---------------- Part B: Lemma SH-att on Z^4 ----------------
M = 10
OFF1 = list(itertools.product((-1, 0, 1), repeat=4))


def N1(X):
    return {tuple(x[i] + o[i] for i in range(4)) for x in X for o in OFF1}


def pi(X):
    return {tuple(c // 3 for c in x) for x in X}


def norm_sh(X, Mlev):
    tot = len(X); cur = set(X)
    for _ in range(Mlev):
        cur = N1(pi(cur)); tot += len(cur)
    return tot


rng = random.Random(20261028)
B1v = B2v = 0; nB = 0; maxratio = 0.0
for s in range(160):
    P = [(0, 0, 0, 0)]
    for _ in range(rng.randint(0, 5)):
        b = rng.choice(P)
        P.append(tuple(b[i] + rng.choice((-1, 0, 1)) for i in range(4)))
    P = list(set(P))
    Y = []
    for _ in range(rng.randint(1, 8)):
        while True:
            b = rng.choice(P + Y)
            dist = rng.randint(1, rho)
            o = [rng.randint(-dist, dist) for _ in range(4)]
            o[rng.randrange(4)] = rng.choice((-dist, dist))
            y = tuple(b[i] + o[i] for i in range(4))
            if y not in P and y not in Y:
                break
        Y.append(y)
    nP = norm_sh(P, M); nPY = norm_sh(set(P) | set(Y), M)
    if nPY > 6561 * nP + c_att * len(Y):
        B1v += 1
    exc = nPY - nP
    if exc > c_att * len(Y):
        B2v += 1
    maxratio = max(maxratio, exc / len(Y))
    nB += 1
P0 = {(0, 0, 0, 0)}
y_far = (3 ** (M + 2), 0, 0, 0)
exc10 = norm_sh(P0 | {y_far}, 10) - norm_sh(P0, 10)
exc5 = norm_sh(P0 | {y_far}, 5) - norm_sh(P0, 5)
res['B1'] = (B1v == 0 and nB >= 150)
res['B2'] = (B2v == 0)
res['B3'] = (exc10 >= 81 * 9 and exc10 - exc5 >= 81 * 4)
print("Part B: samples=%d B1 violations=%d B2 violations=%d max excess per Y-cube=%.1f (c_att=%d); detached excess M=5: %d, M=10: %d"
      % (nB, B1v, B2v, maxratio, c_att, exc5, exc10))

# ---------------- Part C: two-level monotone toy ----------------
n0, n1 = 12, 4
cfg0 = np.array(list(itertools.product((0, 1), repeat=n0)), dtype=np.int8)       # 4096 x 12
k0 = cfg0.sum(1)
ok0 = np.all(~((cfg0 == 1) & (np.roll(cfg0, -1, axis=1) == 1)), axis=1)          # no adjacent level-0 pair (ring)
dirty = np.stack([cfg0[:, 3 * X:3 * X + 3].max(1) for X in range(n1)], axis=1)   # 4096 x 4
xis = np.array(list(itertools.product((0, 1, 2), repeat=n1)), dtype=np.int8)      # 81 x 4 ; 0=low,1=mid,2=high
D1 = (xis[None, :, :] == 0) | ((xis[None, :, :] == 1) & (dirty[:, None, :] == 1))  # 4096 x 81 x 4
adj = [(X, (X + 1) % n1) for X in range(n1)]
viol_full = np.zeros(D1.shape[:2], bool); viol_relB = np.zeros(D1.shape[:2], bool)
for (X, Z) in adj:
    pair = D1[:, :, X] & D1[:, :, Z]
    viol_full |= pair
    if X != 0 and Z != 0:
        viol_relB |= pair
inR = ok0[:, None] & ~viol_full
inRB = ok0[:, None] & ~viol_relB
diff = inRB & ~inR
through0 = (D1[:, :, 3] & D1[:, :, 0]) | (D1[:, :, 0] & D1[:, :, 1])
C1exc = int(np.sum(diff & ~through0))
C2v = 0; C3v = 0; npts = 0; worst = None
for p in [0.02, 0.1, 0.3]:
    w0 = p ** k0 * (1 - p) ** (n0 - k0)
    for q in [0.001, 0.02, 0.1]:
        for qp in sorted({q, 0.3, 0.9}):
            if qp < q:
                continue
            pr = np.array([q, qp - q, 1 - qp])
            w1 = np.prod(pr[xis], axis=1)
            W = w0[:, None] * w1[None, :]
            ratio = float((W * inRB).sum() / (W * inR).sum())
            z = q + (1 - (1 - p) ** 3) * (qp - q)
            npts += 1
            if 2 * z * z < 1 and ratio > 1 / (1 - 2 * z * z) * (1 + 1e-12):
                C2v += 1
            if ratio > 1 / (1 - 2 * q * q) * (1 + 1e-12):
                C3v += 1
            if worst is None or ratio * (1 - 2 * z * z) > worst[0]:
                worst = (ratio * (1 - 2 * z * z), p, q, qp, ratio)
res['C1'] = (C1exc == 0)
res['C2'] = (C2v == 0)
res['C3'] = (C3v >= 1)
print("Part C: configs in R^-B minus R: %d, not through site 0: %d; grid points %d; C2 violations %d; "
      "C3 (z0=q) violations %d; max ratio/bound %.4f at p=%g q=%g q'=%g (ratio %.4f)"
      % (int(diff.sum()), C1exc, npts, C2v, C3v, worst[0], worst[1], worst[2], worst[3], worst[4]))

print("RESULTS: " + " ".join(f"{k}:{'PASS' if v else 'FAIL'}" for k, v in sorted(res.items())))
print("OVERALL " + ("PASS" if all(res.values()) else "FAIL"))
print("secs %.1f" % (time.time() - t0))
