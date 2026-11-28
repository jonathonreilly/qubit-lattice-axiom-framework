# GUIDE scan for row 903: R1 = b p(a)/g(a,b) and R2 = a delta_e(b)/g(a,b)
# on 3 <= a <= b/2, c, d >= b, for Neumann, Dirichlet, Proca (natural walls), Maxwell (m = 0).
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import sys
import numpy as np

def lam(th):
    return 2.0 - 2.0 * np.cos(th)

def omega(M2, th):
    x = (M2 + lam(th)) / 2.0
    return np.log1p(x + np.sqrt(x * (x + 2.0)))

def Fa(a, w):
    return -np.log1p(-np.exp(-a * w))

def g1(kind, n):
    if kind == "N":
        return np.pi * np.arange(n) / n
    if kind == "E":
        return np.pi * np.arange(1, n) / n
    if kind == "D":
        return np.pi * np.arange(1, n + 1) / (n + 1)

def towers(model, m, c, d):
    """list of (direction-1 type, transverse M2 array)"""
    m2 = m * m
    if model == "N":
        M2 = m2 + lam(g1("N", c))[:, None] + lam(g1("N", d))[None, :]
        return [("N", M2.ravel())]
    if model == "D":
        M2 = m2 + lam(g1("D", c))[:, None] + lam(g1("D", d))[None, :]
        return [("D", M2.ravel())]
    if model == "P":  # Proca: tower i has edge spectrum in direction i
        t1 = m2 + lam(g1("N", c))[:, None] + lam(g1("N", d))[None, :]
        t2 = m2 + lam(g1("E", c))[:, None] + lam(g1("N", d))[None, :]
        t3 = m2 + lam(g1("N", c))[:, None] + lam(g1("E", d))[None, :]
        return [("E", t1.ravel()), ("N", t2.ravel()), ("N", t3.ravel())]
    if model == "M":  # Maxwell photons, m = 0
        both = lam(g1("E", c))[:, None] + lam(g1("E", d))[None, :]
        one = np.concatenate([lam(g1("E", c)), lam(g1("E", d))])
        return [("N", both.ravel()), ("E", both.ravel()), ("E", one)]

def Nfor(mu):
    n = int(2 ** np.ceil(np.log2(max(256.0, 40.0 / mu))))
    return min(n, 1 << 17)

def hat0_groups(M2u, fun):
    """hat fun(0) for each unique M2 (fun(M2col, th))"""
    out = np.empty_like(M2u)
    mu = omega(M2u, 0.0)
    Ns = np.array([Nfor(x) for x in mu])
    for N in np.unique(Ns):
        sel = Ns == N
        th = 2 * np.pi * np.arange(N // 2 + 1) / N  # even function: half grid with weights
        wts = np.full(th.size, 2.0); wts[0] = 1.0; wts[-1] = 1.0
        vals = fun(M2u[sel][:, None], th[None, :])
        out[sel] = (vals * wts).sum(axis=1) / N
    return out

def analyse(model, m, b, c, d, alist):
    res = []
    tw = towers(model, m, c, d)
    pre = []
    delta = 0.0
    for kind, M2 in tw:
        M2u, cnt = np.unique(np.round(M2, 14), return_counts=True)
        B = b + 1 if kind == "D" else b
        thB = np.pi * np.arange(2 * B) / B
        SB = omega(M2u[:, None], thB[None, :]).mean(axis=1)
        w0 = hat0_groups(M2u, omega)
        delta += np.sum(cnt * (-(B / 2.0) * (SB - w0)))
        pre.append((kind, M2u, cnt))
    nT = sum(len(M2) for _, M2 in tw)
    reliable = delta > 1e3 * nT * (b + 1) * 1.5e-15
    for a in alist:
        g = 0.0; p = 0.0
        for kind, M2u, cnt in pre:
            th = g1(kind, b)
            g += np.sum(cnt[:, None] * Fa(a, omega(M2u[:, None], th[None, :])))
            p += np.sum(cnt * hat0_groups(M2u, lambda M, t: Fa(a, omega(M, t))))
        res.append((a, b * p / g, (a * delta / g) if reliable else 0.0, (a * delta / (b * p)) if reliable else 0.0, g, p, delta))
    return res

models = sys.argv[1:] if len(sys.argv) > 1 else ["N", "D", "P", "M"]
masses = {"N": [1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0],
          "D": [1e-3, 1e-2, 0.1, 0.3, 1.0],
          "P": [1e-3, 1e-2, 0.1, 0.3, 1.0],
          "M": [0.0]}
bs = [6, 8, 12, 16, 24, 32]
for model in models:
    best1 = (0, None); best2 = (0, None); worstk = (0, None)
    for m in masses[model]:
        for b in bs:
            for (c, d) in [(b, b), (2 * b, 2 * b), (b, 4 * b)]:
                if c * d > 9000:
                    continue
                alist = list(range(3, b // 2 + 1))
                for (a, R1, R2, R2p, g, p, de) in analyse(model, m, b, c, d, alist):
                    k = (2 * b) // a
                    if R1 > best1[0]:
                        best1 = (R1, (m, a, b, c, d, R2))
                    if R2 > best2[0]:
                        best2 = (R2, (m, a, b, c, d, R1))
                    if R2p * k > worstk[0]:
                        worstk = (R2p * k, (m, a, b, c, d))
        print(f"[{model}] m={m} done; running max R1={best1[0]:.4f} at {best1[1]}; max R2={best2[0]:.5f} at {best2[1]}", flush=True)
    print(f"RESULT {model}: sup R1 = b p/g = {best1[0]:.5f} at (m,a,b,c,d,R2)={best1[1]}")
    print(f"RESULT {model}: sup R2 = a delta_e/g = {best2[0]:.5f} at (m,a,b,c,d,R1)={best2[1]}")
    print(f"RESULT {model}: max of floor(2b/a) * a delta_e/(b p) = {worstk[0]:.5f} at {worstk[1]} (Theorem W2 says < 1)", flush=True)
