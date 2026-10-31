#!/usr/bin/env python3
"""f2: E^2 channel with the soft block kernel as IR regulator (scalar toy). Criteria: checks/f2_criteria.md."""
import itertools, sys, time
import numpy as np

t0 = time.time(); OUT = []; fails = []
def say(*a):
    s = " ".join(str(x) for x in a); OUT.append(s); print(s, flush=True)
def crit(name, ok, detail):
    say(f"[{name}] {'PASS' if ok else 'FAIL'} :: {detail}")
    if not ok: fails.append(name)

def dirichlet(theta, l):
    """u(theta) = l^-1 sum_{j=0}^{l-1} e^{i theta (j-o)}, o=(l-1)/2: real."""
    th = np.asarray(theta, float)
    out = np.empty_like(th)
    small = np.abs(np.sin(th / 2)) < 1e-14
    out[~small] = np.sin(l * th[~small] / 2) / (l * np.sin(th[~small] / 2))
    out[small] = np.cos(np.pi * np.round(th[small] / (2 * np.pi)) * (l - 1))  # limit (+-1)
    return out

def per_P_sums(P, l, d=4):
    """For one coarse momentum P (len d): alias arrays d_K=1/omega, w_K=|u_K|^2 flattened."""
    K = np.arange(l)
    cs, us = [], []
    for a in range(d):
        q = (P[a] + 2 * np.pi * K) / l
        cs.append(2 - 2 * np.cos(q)); us.append(dirichlet(q, l) ** 2)
    om = cs[0]; w = us[0]
    for a in range(1, d):
        om = om[..., None] + cs[a]; w = w[..., None] * us[a]
    return om.ravel(), w.ravel()

def trG2_SM(om, w, c):
    dd = 1.0 / om
    S1 = np.dot(dd, w); S2 = np.dot(dd * dd, w); S3 = np.dot(dd ** 3, w); S0 = np.dot(dd, dd)
    if np.isinf(c):
        return S0 - 2 * S3 / S1 + (S2 / S1) ** 2
    den = 1 + c * S1
    return S0 - 2 * c * S3 / den + (c * S2 / den) ** 2

def tau(l, kc, nP):
    kap = kc * l ** 2; c = kap / l ** 4
    g = (np.arange(nP) + 0.5) / nP * 2 * np.pi - np.pi
    tot = 0.0
    for P in itertools.product(g, repeat=4):
        om, w = per_P_sums(np.array(P), l)
        tot += trG2_SM(om, w, c)
    return tot / nP ** 4 / l ** 4

# ---------- (A) validation on a small torus ----------
def lap_torus(n, d):
    N = n ** d; idx = np.arange(N).reshape((n,) * d)
    D = np.zeros((N, N))
    for a in range(d):
        nb = np.roll(idx, -1, axis=a).ravel()
        for i, j in zip(idx.ravel(), nb):
            D[i, i] += 1; D[j, j] += 1; D[i, j] -= 1; D[j, i] -= 1
    return D

def block_avg(n, l, d):
    """Q: (n/l)^d x n^d straight block average, blocks l*X + {0..l-1}^d."""
    nc = n // l; N = n ** d
    Q = np.zeros((nc ** d, N))
    coords = np.array(list(itertools.product(range(n), repeat=d)))
    X = coords // l
    rows = np.ravel_multi_index(X.T, (nc,) * d)
    Q[rows, np.arange(N)] = 1.0 / l ** d
    return Q

l, Tc, kc = 3, 2, 1.0
n = l * Tc; D = lap_torus(n, 4); Q = block_avg(n, l, 4)
kap = kc * l ** 2
G = np.linalg.inv(D + kap * Q.T @ Q)
tau_bf = np.sum(G * G) / n ** 4
# per-P alias formula on the torus momenta (direct per-P inversion; P = 0 allowed)
tot = 0.0; smerr = 0.0
for P in itertools.product(2 * np.pi * np.arange(Tc) / Tc, repeat=4):
    P = np.array(P)
    om, w = per_P_sums(P, l)
    # phases: v_K = u_K e^{-i q_K o}; |v|^2 = w; build the rank-one term with phases
    Ks = np.array(list(itertools.product(range(l), repeat=4)))
    qK = (P[None, :] + 2 * np.pi * Ks) / l
    uK = np.prod(dirichlet(qK, l), axis=1)
    v = uK * np.exp(-1j * qK.sum(axis=1) * (l - 1) / 2)
    M = np.diag(om).astype(complex) + (kap / l ** 4) * np.outer(v.conj(), v)
    Gp = np.linalg.inv(M)
    tot += np.real(np.trace(Gp @ Gp))
tau_mom = tot / n ** 4
for _ in range(5):
    P = np.random.default_rng(7).uniform(-np.pi, np.pi, 4) + _ * 0.1
    om, w = per_P_sums(P, l)
    Ks = np.array(list(itertools.product(range(l), repeat=4)))
    qK = (P[None, :] + 2 * np.pi * Ks) / l
    v = np.prod(dirichlet(qK, l), axis=1) * np.exp(-1j * qK.sum(axis=1) * (l - 1) / 2)
    M = np.diag(om).astype(complex) + (kap / l ** 4) * np.outer(v.conj(), v)
    Gp = np.linalg.inv(M); direct = np.real(np.trace(Gp @ Gp))
    smerr = max(smerr, abs(direct - trG2_SM(om, w, kap / l ** 4)) / direct)
rel = abs(tau_bf - tau_mom) / tau_bf
crit("A", rel <= 1e-10 and smerr <= 1e-10, f"dense tau={tau_bf:.12f}, alias tau={tau_mom:.12f}, rel={rel:.1e}; SM rel={smerr:.1e}")
del G, D

# ---------- (E) two-step chain = one big step (d = 2) ----------
d2 = 2; Lb = 3; nf = 18
D2 = lap_torus(nf, d2); Q1 = block_avg(nf, Lb, d2); Q2 = block_avg(nf // Lb, Lb, d2)
k0, k1 = 1.7, 0.6
N0, N1 = nf ** 2, (nf // Lb) ** 2
# joint precision in (phi0, phi1), phi2 = 0: 1/2 phi0 D phi0 + k0/2 |Q1 phi0 - phi1|^2 + k1/2 |Q2 phi1|^2
J = np.zeros((N0 + N1, N0 + N1))
J[:N0, :N0] = D2 + k0 * Q1.T @ Q1
J[:N0, N0:] = -k0 * Q1.T; J[N0:, :N0] = -k0 * Q1
J[N0:, N0:] = k0 * np.eye(N1) + k1 * Q2.T @ Q2
C0 = np.linalg.inv(J)[:N0, :N0]
keff = k0 * k1 / (k0 + k1 * Lb ** -d2)
QQ = Q2 @ Q1
C1 = np.linalg.inv(D2 + keff * QQ.T @ QQ)
eE = np.abs(C0 - C1).max()
crit("E", eE <= 1e-12, f"two-step marginal vs one-step(kappa_eff={keff:.6f}): max diff {eE:.1e}")

# ---------- (B) quadrature ----------
t8 = tau(7, 1.0, 8); t12 = tau(7, 1.0, 12)
crit("B", abs(t8 - t12) <= 2e-4, f"tau(7,1): nP=8 {t8:.7f}, nP=12 {t12:.7f}, diff {abs(t8-t12):.1e}")
say(f"   (t={time.time()-t0:.0f}s)")

# ---------- (C), (D) ----------
ls = [3, 5, 7, 9, 11, 13, 15]
kcs = [0.25, 1.0, 4.0, np.inf]
c0 = 1 / (8 * np.pi ** 2)
taus = {}
for kc_ in kcs:
    for l_ in ls:
        taus[(kc_, l_)] = tau(l_, kc_, 8)
    sl = [(taus[(kc_, b)] - taus[(kc_, a)]) / np.log(b / a) / c0 for a, b in zip(ls[:-1], ls[1:])]
    say(f"   kappa_c={kc_}: slope/(1/8pi^2) along (3,5),...,(13,15): " + ", ".join(f"{x:.4f}" for x in sl)
        + f"   [t={time.time()-t0:.0f}s]")
last = {kc_: (taus[(kc_, 15)] - taus[(kc_, 13)]) / np.log(15 / 13) for kc_ in kcs}
okC = all(abs(v / c0 - 1) <= 0.03 for v in last.values())
crit("C", okC, "slope at (13,15) / (1/8pi^2): " + ", ".join(f"k_c={k}: {v/c0:.4f}" for k, v in last.items()))
spread = max(last.values()) - min(last.values())
crit("D", spread <= 0.03 * c0, f"kappa spread of the (13,15) slope = {spread/c0:.4f} x 1/(8pi^2)")
say("   constants tau(15,k_c) - log(15)/(8pi^2): " + ", ".join(f"k_c={k}: {taus[(k,15)] - c0*np.log(15):.5f}" for k in kcs))
say(f"f2 done: {'ALL PASS' if not fails else 'FAIL: ' + ','.join(fails)}; wall {time.time()-t0:.1f}s")
with open(sys.argv[1] if len(sys.argv) > 1 else "f2_out.txt", "w") as f:
    f.write("\n".join(OUT) + "\n")
