"""w1: numerical sanity checks for HW.md (Lemma KS for SU(2), (KS-N) scalar case for SU(3), counts).
Criteria: checks/w1_criteria.md (written before this script). Informational; never a proof."""
import itertools
import math
import time

import numpy as np
from scipy import integrate, special

t0 = time.time()
results = {}


# ---------------- A. Lemma KS (SU(2)) ----------------
def g_bessel(b):
    if b == 0.0:
        return 0.0
    ratio = special.ive(2, b) / special.ive(1, b)
    return b * (1.0 - ratio)


def g_quad(b):
    cut = min(math.pi, 60.0 / math.sqrt(b)) if b > 1 else math.pi

    def num(a):
        return (1 - math.cos(a)) * math.exp(-b * (1 - math.cos(a))) * math.sin(a) ** 2

    def den(a):
        return math.exp(-b * (1 - math.cos(a))) * math.sin(a) ** 2

    n1 = integrate.quad(num, 0, cut, limit=400, epsabs=0, epsrel=1e-13)[0]
    d1 = integrate.quad(den, 0, cut, limit=400, epsabs=0, epsrel=1e-13)[0]
    if cut < math.pi:
        n1 += integrate.quad(num, cut, math.pi, limit=200)[0]
        d1 += integrate.quad(den, cut, math.pi, limit=200)[0]
    return b * n1 / d1


def norm_N(b):
    # N(b) = 2 e^{-b} I_1(b) / b  (N(0) = 1)
    if b == 0.0:
        return 1.0
    return 2.0 * special.ive(1, b) / b


bs = np.logspace(-4, 7, 400)
gb = np.array([g_bessel(b) for b in bs])
gq_idx = bs <= 1e4
gq = np.array([g_quad(b) for b in bs[gq_idx]])
a1_max_b = gb.max()
a1_max_q = gq.max()
a1_agree = np.max(np.abs(gq - gb[gq_idx]))
a1_top = g_bessel(1e7)
A1 = (a1_max_b <= 1.5 + 1e-9) and (a1_max_q <= 1.5 + 1e-9) and (a1_agree <= 1e-7) and (a1_top >= 1.4999)
results["A1"] = A1
print(f"A1: max g (Bessel) = {a1_max_b:.12f}, max g (quad, b<=1e4) = {a1_max_q:.12f}, "
      f"max |quad-Bessel| = {a1_agree:.2e}, g(1e7) = {a1_top:.9f} -> {'PASS' if A1 else 'FAIL'}")

lams = list(np.round(np.arange(0.05, 0.951, 0.05), 2)) + [0.99]
worst = -np.inf
neg_fail = False
neg_worst = -np.inf
for lam in lams:
    for b in bs:
        R = norm_N((1 - lam) * b) / norm_N(b)
        worst = max(worst, R / (1 - lam) ** (-1.5))
        nr = R / (1 - lam) ** (-1.0)
        neg_worst = max(neg_worst, nr)
        if nr > 1 + 1e-9:
            neg_fail = True
A2 = worst <= 1 + 1e-12
A3 = neg_fail
results["A2"] = A2
results["A3"] = A3
print(f"A2: max R/(1-lam)^(-3/2) = {worst:.12f} -> {'PASS' if A2 else 'FAIL'}")
print(f"A3 (negative control, false exponent 1): max R/(1-lam)^(-1) = {neg_worst:.4f}; "
      f"false claim fails = {neg_fail} -> {'PASS' if A3 else 'FAIL'}")

rng = np.random.default_rng(20261028)


def rand_su2(n):
    q = rng.normal(size=(n, 4))
    q /= np.linalg.norm(q, axis=1, keepdims=True)
    a, b_, c, d = q.T
    return np.stack([np.stack([a + 1j * d, c + 1j * b_], -1), np.stack([-c + 1j * b_, a - 1j * d], -1)], -2)


ok_a = True
ok_b = True
max_dev = 0.0
for _ in range(200):
    W = rand_su2(1)[0]
    r = rng.uniform(0.01, 1.0)
    M = r * W
    V = rand_su2(1000)
    Vinv = np.conj(np.transpose(V, (0, 2, 1)))
    retr_V = np.real(np.einsum('nij,ji->n', Vinv, M))
    retr_W0 = np.real(np.trace(np.conj(W.T) @ M))
    phi = 0.5 * (retr_W0 - retr_V)
    opn = np.linalg.norm(V - W[None], ord=2, axis=(1, 2))
    dev = np.max(np.abs(phi - r * opn ** 2 / 2))
    max_dev = max(max_dev, dev)
    if dev > 1e-12:
        ok_a = False
    Wr = rand_su2(10000)
    retr_r = np.real(np.einsum('nij,ji->n', np.conj(np.transpose(Wr, (0, 2, 1))), M))
    if retr_r.max() > retr_W0 + 1e-12:
        ok_b = False
ok_c = True
Vh = rand_su2(200000)
cosal = np.real(np.trace(Vh, axis1=1, axis2=2)) / 2.0
mc_lines = []
for b in [0.5, 2.0, 8.0, 32.0]:
    x = np.exp(-b * (1 - cosal))
    est, se = x.mean(), x.std(ddof=1) / math.sqrt(len(x))
    z = abs(est - norm_N(b)) / se
    mc_lines.append(f"b={b}: MC {est:.6f} +- {se:.1e}, Bessel {norm_N(b):.6f}, z={z:.2f}")
    if z > 4:
        ok_c = False
A4 = ok_a and ok_b and ok_c
results["A4"] = A4
print(f"A4: (a) max |phi - r||V-W0||^2/2| = {max_dev:.2e} ok={ok_a}; (b) maximiser ok={ok_b}; (c) "
      + "; ".join(mc_lines) + f" -> {'PASS' if A4 else 'FAIL'}")


# ---------------- B. (KS-N) scalar case, SU(3), Weyl integration (informational) ----------------
def g3(b):
    if b <= 200:
        n = 1024
        th = np.linspace(-np.pi, np.pi, n, endpoint=False)
        w = np.full(n, 2 * np.pi / n)
    else:
        h = min(np.pi, 14.0 / np.sqrt(b))
        n = 1201
        th = np.linspace(-h, h, n)
        w = np.full(n, (2 * h) / (n - 1))
        w[1:-1:2] *= 4 / 3
        w[2:-1:2] *= 2 / 3
        w[0] *= 1 / 3
        w[-1] *= 1 / 3
    T1, T2 = np.meshgrid(th, th, indexing='ij')
    T3 = -T1 - T2
    f = 1 - (np.cos(T1) + np.cos(T2) + np.cos(T3)) / 3
    vd = (4 * np.sin((T1 - T2) / 2) ** 2) * (4 * np.sin((T1 - T3) / 2) ** 2) * (4 * np.sin((T2 - T3) / 2) ** 2)
    ww = np.outer(w, w)
    e = np.exp(-b * f) * vd * ww
    return b * (f * e).sum() / e.sum()


b3 = np.logspace(-3, 4, 60)
g3v = np.array([g3(b) for b in b3])
g3_cross = (g3(199.0), None)
B_ok = g3v.max() <= 4 + 1e-3
print(f"B (informational): SU(3) scalar case: max_b b E_b[f] = {g3v.max():.6f} at b = {b3[g3v.argmax()]:.3g}; "
      f"value at b = 1e4: {g3v[-1]:.6f}; D/2 = 4 -> I-{'PASS' if B_ok else 'FAIL'}")
mid = [(round(float(b), 3), round(float(v), 4)) for b, v in zip(b3[::10], g3v[::10])]
print(f"   samples (b, g3): {mid}")

# ---------------- C. counts ----------------
L, d = 3, 4
sites = list(itertools.product(range(L), repeat=d))
siteset = set(sites)
links = [(x, mu) for x in sites for mu in range(d) if x[mu] + 1 < L]
plaqs = []
for x in sites:
    for mu, nu in itertools.combinations(range(d), 2):
        verts = [x, tuple(x[i] + (i == mu) for i in range(d)), tuple(x[i] + (i == nu) for i in range(d)),
                 tuple(x[i] + (i == mu) + (i == nu) for i in range(d))]
        if all(v in siteset for v in verts):
            plaqs.append((x, mu, nu))


def plaq_links(p):
    x, mu, nu = p
    xm = tuple(x[i] + (i == mu) for i in range(d))
    xn = tuple(x[i] + (i == nu) for i in range(d))
    return [(x, mu), (xn, mu), (x, nu), (xm, nu)]


cnt = {l: 0 for l in links}
for p in plaqs:
    for l in plaq_links(p):
        cnt[l] += 1
C1 = (len(links) == 216) and (max(cnt.values()) <= 6) and (max(cnt.values()) == 6)
results["C1"] = C1
print(f"C1: n_int = {len(links)}, max plaquettes per interior link = {max(cnt.values())}, "
      f"min = {min(cnt.values())} -> {'PASS' if C1 else 'FAIL'}")

corner = 0
origin = (0,) * d
for x in itertools.product((-2, -1, 0, 1), repeat=d):
    for mu, nu in itertools.combinations(range(d), 2):
        verts = {x, tuple(x[i] + (i == mu) for i in range(d)), tuple(x[i] + (i == nu) for i in range(d)),
                 tuple(x[i] + (i == mu) + (i == nu) for i in range(d))}
        if origin in verts:
            corner += 1
C2 = corner == 24
results["C2"] = C2
print(f"C2: plaquettes with a given corner = {corner} -> {'PASS' if C2 else 'FAIL'}")

Tn = 9
offs = list(itertools.product((-1, 0, 1), repeat=d))


def n1(A):
    out = set()
    for a in A:
        for o in offs:
            out.add(tuple((a[i] + o[i]) % Tn for i in range(d)))
    return out


y = (0, 0, 0, 0)
cntQ = sum(1 for Q in itertools.product(range(Tn), repeat=d) if y in n1([Q]))
ok3 = cntQ == 81
worst_ratio = 0.0
for _ in range(50):
    n = int(rng.integers(1, 61))
    A = {tuple(int(v) for v in rng.integers(0, Tn, size=d))}
    while len(A) < n:
        a = list(A)[int(rng.integers(len(A)))]
        o = offs[int(rng.integers(len(offs)))]
        A.add(tuple((a[i] + o[i]) % Tn for i in range(d)))
    r_ = len(n1(A)) / len(A)
    worst_ratio = max(worst_ratio, r_)
    if r_ > 81:
        ok3 = False
results["C3"] = ok3
print(f"C3: #Q with y in N_1(Q) = {cntQ}; max |N_1(A)|/|A| over 50 sets = {worst_ratio:.2f} -> {'PASS' if ok3 else 'FAIL'}")

overall = all(results[k] for k in ["A1", "A2", "A3", "A4", "C1", "C2", "C3"])
print(f"OVERALL: {'PASS' if overall else 'FAIL'}  ({', '.join(f'{k}={v}' for k, v in results.items())}); "
      f"wall {time.time() - t0:.1f} s")
