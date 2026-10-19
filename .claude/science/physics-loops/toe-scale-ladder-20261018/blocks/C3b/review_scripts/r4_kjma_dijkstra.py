"""Reviewer r4: nucleation-growth (candidate a) by an independent method: formation times as SITE first-passage times
tau_x = min(N_x, min_{y~x} tau_y + E_x) computed by scipy Dijkstra from a super-source (N ~ Exp(eps), E ~ Exp(1)),
then colours by majority of strictly-earlier nbrs (tie/none -> uniform).  2D torus.
Checks: (1) xi(1/e) exponent vs eps within 0.05 of -1/3 (and report vs author's -0.326);
(2) Corollary J-KJMA tail: P(tau_0 > t) <= exp(-eps|B_r| t/2) + P(Gamma(r,1) > t/2), r = floor(t/4).
"""
import math, time
import numpy as np
import numba as nb
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from scipy.stats import gamma as Gam
from rv_common import check, total

rng = np.random.default_rng(5150)


def nbrs(L):
    idx = np.arange(L * L).reshape(L, L)
    return np.stack([np.roll(idx, s, a).ravel() for a in (0, 1) for s in (1, -1)], 1)


@nb.njit(cache=True)
def colour(tau, nbr, u):
    order = np.argsort(tau)
    sig = np.zeros(tau.shape[0], np.int8)
    for x in order:
        s = 0
        for j in range(4):
            y = nbr[x, j]
            if tau[y] < tau[x]:
                s += sig[y]
        sig[x] = (1 if u[x] < 0.5 else -1) if s == 0 else (1 if s > 0 else -1)
    return sig


def sample(L, eps, nbr):
    Nn = L * L
    E = rng.exponential(1.0, Nn); N0 = rng.exponential(1 / eps, Nn)
    rows = np.r_[np.full(Nn, Nn), nbr.ravel()]
    cols = np.r_[np.arange(Nn), np.repeat(np.arange(Nn), 4)]
    # edge y -> x weight E_x  (row = from, col = to); nbr[x, j] = y
    w = np.r_[N0, np.repeat(E, 4)]
    rr = np.r_[np.full(Nn, Nn), nbr.ravel()]
    cc = np.r_[np.arange(Nn), np.repeat(np.arange(Nn), 4)]
    G = csr_matrix((w, (rr, cc)), shape=(Nn + 1, Nn + 1))
    tau = dijkstra(G, directed=True, indices=Nn)[:Nn]
    return tau, colour(tau, nbr, rng.random(Nn))


def corr(F, rmax):
    m = F.mean()
    return np.array([0.5 * ((F * np.roll(F, -r, 0)).mean() + (F * np.roll(F, -r, 1)).mean()) - m * m for r in range(rmax + 1)])


def xi_of(C):
    thr = C[0] / math.e
    for r in range(1, len(C)):
        if C[r] < thr:
            return r - 1 + (C[r - 1] - thr) / (C[r - 1] - C[r])
    return np.nan


t0 = time.time()
cfg = [(1e-2, 128, 60), (1e-3, 256, 16), (1e-4, 512, 6)]
xis = []; taus_by = {}
for eps, L, ns in cfg:
    nbr = nbrs(L)
    Cs = []; tt = []
    for _ in range(ns):
        tau, sig = sample(L, eps, nbr)
        Cs.append(corr(sig.reshape(L, L).astype(float), 60)); tt.append(tau)
    Cs = np.array(Cs)
    xi = xi_of(Cs.mean(0)); xb = np.nanstd([xi_of(Cs[rng.integers(0, ns, ns)].mean(0)) for _ in range(200)])
    xis.append((xi, xb)); taus_by[eps] = np.concatenate(tt)
    print(f"eps={eps:.0e} L={L} ns={ns}: xi(1/e)={xi:.3f}+-{xb:.3f}  (author: 4.154, 8.552, 18.854)  t={time.time()-t0:.0f}s", flush=True)
x = np.log([c[0] for c in cfg]); y = np.log([v[0] for v in xis])
slope = np.polyfit(x, y, 1)[0]
check("k1 xi(eps) exponent within 0.05 of -1/3 (independent Dijkstra implementation)", abs(slope + 1 / 3) < 0.05, f"slope {slope:.3f}")
auth = {1e-2: 4.154, 1e-3: 8.552, 1e-4: 18.854}
okm = all(abs(xis[i][0] - auth[c[0]]) < 4 * math.hypot(xis[i][1], 0.2) for i, c in enumerate(cfg))
check("k2 xi values agree with author's s2 table within 4 SE (author SE <= 0.2)", okm,
      " ".join(f"{v[0]:.2f}" for v in xis))
ok = True; rep = []
for eps, tt in taus_by.items():
    for t in np.linspace(4, 120, 59):
        r = int(t // 4)
        if r < 1:
            continue
        Br = 2 * r * r + 2 * r + 1
        b = math.exp(-eps * Br * t / 2) + Gam.sf(t / 2, r, scale=1.0)
        p = (tt > t).mean()
        ok &= p <= b + 4 * math.sqrt(max(p, 1e-6) / len(tt))
    rep.append(f"eps={eps:.0e}: P(tau>40)={(tt>40).mean():.2e}")
check("k3 Corollary J-KJMA tail bound P(tau>t) <= exp(-eps|B_r|t/2)+P(Gamma(r,1)>t/2) on a t-grid", ok, "; ".join(rep))
total()
