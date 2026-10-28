#!/usr/bin/env python3
"""x7 (session 8): leading-order (g^4) cross-plane covariance of plaquettes in every toron sector (A, exact) and a
Monte Carlo of SU(2) Wilson lattice gauge theory on a fixed small periodic torus (B). Criteria: checks/x7_criteria.md.
Reads no external files. Prints well under 6000 characters."""
import itertools, math, resource, sys, time
import numpy as np

T0 = time.time()
ORI = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
SPATIAL = [3, 4, 5]                       # indices of (1,2), (1,3), (2,3) in ORI

# ----------------------------------------------------------------------------------------------------------- A
def dsym(k):
    """6x4 symbol of d on 1-forms: (dA)_{mu nu}(x) = A_nu(x+mu) - A_nu(x) - A_mu(x+nu) + A_mu(x)."""
    e = np.exp(1j * np.asarray(k)) - 1.0
    D = np.zeros((6, 4), complex)
    for r, (m, n) in enumerate(ORI):
        D[r, n] += e[m]
        D[r, m] -= e[n]
    return D

def pi_k(k):
    D = dsym(k)
    M = D.conj().T @ D
    w, v = np.linalg.eigh(M)
    inv = np.where(w > 1e-12, 1.0 / np.where(w > 1e-12, w, 1.0), 0.0)
    return D @ (v * inv) @ v.conj().T @ D.conj().T

def pi_position(shape, phi):
    """Pi^phi(y)_{o,o'} = (1/V) sum_k e^{iky} Pi(k), k_mu = (2 pi n_mu + phi_mu)/T_mu; returns |.|-relevant array
    P[y0,y1,y2,y3,o,o'] up to the phase e^{i phi.y/T} (which is returned separately applied)."""
    V = int(np.prod(shape))
    P = np.zeros(tuple(shape) + (6, 6), complex)
    for n in itertools.product(*[range(T) for T in shape]):
        k = [(2 * math.pi * n[m] + phi[m]) / shape[m] for m in range(4)]
        P[n] = pi_k(k)
    # sum_k e^{i k y} P(k) = e^{i phi y / T} * sum_n e^{2 pi i n y / T} P(n)  -> ifft * V
    Py = np.fft.ifftn(P, axes=(0, 1, 2, 3))     # (1/V) sum_n e^{+2 pi i n y/T}
    ph = np.ones(tuple(shape))
    grids = np.meshgrid(*[np.arange(T) for T in shape], indexing='ij')
    ph = np.exp(1j * sum(phi[m] * grids[m] / shape[m] for m in range(4)))
    return Py * ph[..., None, None]

def dense_pi(shape, phi):
    V = int(np.prod(shape))
    idx = lambda x: np.ravel_multi_index(tuple(x), shape)
    D = np.zeros((6 * V, 4 * V), complex)
    for x in itertools.product(*[range(T) for T in shape]):
        for r, (m, n) in enumerate(ORI):
            row = 6 * idx(x) + r
            def add(mu, shift, comp, c):
                y = list(x); ph = 1.0
                if shift is not None:
                    y[shift] += 1
                    if y[shift] == shape[shift]:
                        y[shift] = 0; ph = np.exp(1j * phi[shift])
                D[row, 4 * idx(y) + comp] += c * ph
            add(None, m, n, 1.0); add(None, None, n, -1.0); add(None, n, m, -1.0); add(None, None, m, 1.0)
    M = D.conj().T @ D
    w, v = np.linalg.eigh(M)
    inv = np.where(w > 1e-9, 1.0 / np.where(w > 1e-9, w, 1.0), 0.0)
    return D @ (v * inv) @ v.conj().T @ D.conj().T, idx

out = []
pr = lambda s: (out.append(s), print(s), sys.stdout.flush())
pr("x7 A (exact)")
# A1
small = (4, 4, 4, 4)
a1 = 0.0
for phi in [(0.0, 0.0, 0.0, 0.0), (0.7, 1.3, 0.0, 2.1)]:
    Pd, idx = dense_pi(small, phi)
    Py = pi_position(small, phi)
    rng = np.random.default_rng(7)
    for _ in range(400):
        x = rng.integers(0, 4, 4); xp = rng.integers(0, 4, 4)
        o, op = rng.integers(0, 6, 2)
        y = (x - xp) % 4
        # momentum formula for x - x' with wrap: e^{ik(x-x')} with x, x' in the fundamental domain
        k_sum = 0.0
        val = Py[tuple(y)][o, op]
        # correct wrapped phase: y computed mod T loses e^{i phi_mu} when x_mu - x'_mu < 0
        for m in range(4):
            if x[m] - xp[m] < 0:
                val = val * np.exp(-1j * phi[m])
        a1 = max(a1, abs(val - Pd[6 * idx(x) + o, 6 * idx(xp) + op]))
pr(f"A1 max|formula - dense| = {a1:.2e}  ({'PASS' if a1 < 1e-10 else 'FAIL'})")

# A2, A3 on 8 x 4^3
shape = (8, 4, 4, 4); V = int(np.prod(shape)); Vs = V // 8
def stats(phi):
    Py = pi_position(shape, phi)
    # projector: sum_{p'} |Pi(p,p')|^2 = Pi(p,p): sum over y and o'
    proj = np.abs(np.sum(np.abs(Py) ** 2, axis=(0, 1, 2, 3, 5)) - np.real(np.diagonal(Py[0, 0, 0, 0]))).max()
    meanpp = np.real(np.trace(Py[0, 0, 0, 0])) / 6.0
    lam = sum(np.sum(np.abs(Py[1, :, :, :, o, op]) ** 2) for o in SPATIAL for op in SPATIAL) / (9.0 * Vs)
    lam2 = sum(np.sum(np.abs(Py[2, :, :, :, o, op]) ** 2) for o in SPATIAL for op in SPATIAL) / (9.0 * Vs)
    hpp = np.mean([np.real(Py[0, 0, 0, 0][o, o]) for o in SPATIAL])
    return proj, meanpp, lam, lam2, hpp

p0, m0, L0, L0_2, h0 = stats((0.0, 0.0, 0.0, 0.0))
pg, mg, _, _, _ = stats((0.7, 1.3, 0.4, 2.1))
a2 = max(p0, pg, abs(m0 - (3 * V - 3) / (6 * V)), abs(mg - 0.5))
pr(f"A2 projector err {max(p0, pg):.1e}; mean Pi_pp {m0:.12f} vs {(3*V-3)/(6*V):.12f}, twisted {mg:.12f} vs 0.5 "
   f"({'PASS' if a2 < 1e-10 else 'FAIL'})")
grid = [0.0, math.pi / 2, math.pi, 3 * math.pi / 2]
lams, lams2, hs = [], [], []
for phi in itertools.product(grid, repeat=4):
    if phi == (0.0, 0.0, 0.0, 0.0):
        lams.append(L0); lams2.append(L0_2); hs.append(h0); continue
    _, _, l, l2, h = stats(phi)
    lams.append(l); lams2.append(l2); hs.append(h)
lams = np.array(lams); hs = np.array(hs); lams2 = np.array(lams2)
LB = L0 / 32.0
tot = (L0 + 2 * lams) / 32.0
hh = h0 + 2 * hs
UB = tot.max() + (hh.max() - hh.min()) ** 2 / 256.0
pr(f"A3 Lambda_0 = {L0:.6e}; Lambda_ch(phi) in [{lams.min():.4e}, {lams.max():.4e}] (untwisted {L0:.4e})")
pr(f"   leading g^-4 C_LO(phi) in [{tot.min():.4e}, {tot.max():.4e}]; untwisted 3*Lambda_0/32 = {3*L0/32:.4e}")
pr(f"   LB = {LB:.4e}  UB = {UB:.4e}  (h range {hh.min():.4f}..{hh.max():.4f})  A3 {'PASS' if LB > 0 else 'FAIL'}")
pr(f"   d = 2 (info): Lambda_0 = {L0_2:.4e}, untwisted g^-4 C_LO = {3*L0_2/32:.4e}")
tA = time.time() - T0

# ----------------------------------------------------------------------------------------------------------- B
def qmul(a, b):
    a0, av = a[..., :1], a[..., 1:]
    b0, bv = b[..., :1], b[..., 1:]
    s = a0 * b0 - np.sum(av * bv, axis=-1, keepdims=True)
    v = a0 * bv + b0 * av - np.cross(av, bv)
    return np.concatenate([s, v], axis=-1)

def qdag(a):
    return np.concatenate([a[..., :1], -a[..., 1:]], axis=-1)

sh = lambda X, mu, s: np.roll(X, -s, axis=mu)   # X(x + s e_mu)

def staple(U, mu):
    S = np.zeros_like(U[0])
    for nu in range(4):
        if nu == mu:
            continue
        up = qmul(qmul(sh(U[nu], mu, 1), qdag(sh(U[mu], nu, 1))), qdag(U[nu]))
        Um = sh(U[nu], nu, -1)                     # U_nu(x - nu)
        dn = qmul(qmul(qdag(sh(Um, mu, 1)), qdag(sh(U[mu], nu, -1))), Um)
        S += up + dn
    return S

def plaq_s(U, mu, nu):
    P = qmul(qmul(U[mu], sh(U[nu], mu, 1)), qmul(qdag(sh(U[mu], nu, 1)), qdag(U[nu])))
    return 1.0 - P[..., 0]

def heat(U, mu, beta, mask, rng):
    V = staple(U, mu)
    k = np.sqrt(np.sum(V * V, axis=-1))
    Vh = V / k[..., None]
    alpha = beta * k
    a0 = np.empty(k.shape); todo = np.ones(k.shape, bool)
    while todo.any():
        n = todo.sum()
        r1, r2, r3, r4 = (1.0 - rng.random(n) for _ in range(4))
        lam2 = -(np.log(r1) + np.cos(2 * math.pi * r2) ** 2 * np.log(r3)) / (2 * alpha[todo])
        acc = r4 ** 2 <= 1 - lam2
        tmp = a0[todo]; tmp[acc] = 1 - 2 * lam2[acc]; a0[todo] = tmp
        t2 = todo.copy(); t2[todo] = ~acc; todo = t2
    nv = rng.normal(size=k.shape + (3,)); nv /= np.linalg.norm(nv, axis=-1, keepdims=True)
    W = np.concatenate([a0[..., None], np.sqrt(np.maximum(1 - a0 ** 2, 0))[..., None] * nv], axis=-1)
    new = qmul(W, qdag(Vh))
    U[mu] = np.where(mask[..., None], new, U[mu])

def over(U, mu, mask):
    V = staple(U, mu)
    Vh = V / np.sqrt(np.sum(V * V, axis=-1))[..., None]
    new = qdag(qmul(qmul(Vh, U[mu]), Vh))       # (Vh U Vh)^dag = Vh^dag U^dag Vh^dag
    U[mu] = np.where(mask[..., None], new, U[mu])

par = np.indices(shape).sum(axis=0) % 2
masks = [par == 0, par == 1]

def run(beta, seed, ntherm=1000, nmeas=8000):
    rng = np.random.default_rng(seed)
    U = np.zeros((4,) + shape + (4,)); U[..., 0] = 1.0
    phis = np.empty((nmeas, shape[0])); sall = np.empty(nmeas)
    for it in range(ntherm + nmeas):
        for mu in range(4):
            for m in masks:
                heat(U, mu, beta, m, rng)
        for _ in range(3):
            for mu in range(4):
                for m in masks:
                    over(U, mu, m)
        if it % 50 == 0:   # re-unitarise
            U /= np.linalg.norm(U, axis=-1, keepdims=True)
        if it >= ntherm:
            sp = [plaq_s(U, a, b) for (a, b) in [(1, 2), (1, 3), (2, 3)]]
            phis[it - ntherm] = np.mean(np.stack(sp), axis=(0, 2, 3, 4))
            st = [plaq_s(U, a, b) for (a, b) in [(0, 1), (0, 2), (0, 3)]]
            sall[it - ntherm] = (np.mean(np.stack(sp)) + np.mean(np.stack(st))) / 2
    return phis, sall

def cov_jk(phis, d, nb=40):
    n = phis.shape[0] // nb * nb; X = phis[:n]
    prod = np.mean(X * np.roll(X, -d, axis=1), axis=1)    # mean_t Phi(t)Phi(t+d) per sample
    mu = np.mean(X, axis=1)
    def est(sel):
        return np.mean(prod[sel]) - np.mean(mu[sel]) ** 2
    full = est(np.ones(n, bool))
    bs = n // nb; jk = []
    for b in range(nb):
        sel = np.ones(n, bool); sel[b * bs:(b + 1) * bs] = False
        jk.append(est(sel))
    jk = np.array(jk)
    return full, math.sqrt((nb - 1) * np.mean((jk - jk.mean()) ** 2))

pr("x7 B (MC, SU(2) Wilson, 8x4^3, HB + 3 OR, 1000 therm + 8000 meas, cold start)")
res = {}
for beta, seed in [(8.0, 801), (16.0, 1601), (32.0, 3201)]:
    t1 = time.time()
    phis, sall = run(beta, seed)
    g4 = (4.0 / beta) ** 2
    c1, e1 = cov_jk(phis, 1); c2, e2 = cov_jk(phis, 2)
    R, eR = c1 / g4, e1 / g4
    res[beta] = (c1, e1, R, eR, np.mean(sall))
    pr(f" beta={beta:4.0f}: <s>beta={np.mean(sall)*beta:.4f}; C(1)={c1:.4e}+-{e1:.1e} ({c1/e1:.1f} SE); "
       f"R=C(1)/g^4={R:.4e}+-{eR:.1e}; R/LB={R/LB:.2f}, R/UB={R/UB:.2f}; C(2)/g^4={c2/g4:.3e}+-{e2/g4:.1e} "
       f"[{time.time()-t1:.0f}s]")
b0 = abs(res[32.0][4] * 32 - 0.75) < 0.1
okp = all(res[b][0] > 5 * res[b][1] and 0.5 * LB <= res[b][2] <= 1.5 * UB for b in (16.0, 32.0))
c1, e1, R, eR, _ = res[32.0]
fail = (R < 0.5 * LB - 3 * eR) or (R > 1.5 * UB + 3 * eR) or (c1 < -3 * e1)
verdict = "PASS" if (b0 and okp) else ("FAIL" if fail else "INCONCLUSIVE")
pr(f"B0 {'PASS' if b0 else 'FAIL'}; B {verdict}")
ru = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20
pr(f"wall {time.time()-T0:.0f}s (A {tA:.0f}s); peak {ru:.0f} MB")
