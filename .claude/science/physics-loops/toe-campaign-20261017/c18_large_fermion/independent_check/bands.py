"""Item 1: global minimum of the lowest band.  Dense grid + many local minimizations.
usage: python3 bands.py note | scan | other"""
import itertools, sys
import numpy as np
from scipy.optimize import minimize
from multiprocessing import Pool
from model import *

FD = dict(square=1, triangle=0, plaquette=1, tube=1)
U = {0: solve_gauge(FD), 1: solve_gauge(dict(FD, triangle=1))}
KSTAR = {}  # fixed momenta for each gauge (from affine.py: default gauge -> (1,3,1),(3,1,3) in pi/2)
KP = np.array([1, -1, 1]) * np.pi / 2

def wrap(k): return (np.asarray(k) + np.pi) % (2 * np.pi) - np.pi

def analyse(args):
    t1, t2, lam, tri, N, nrand, seed = args
    u = U[tri]
    e0 = lambda k: np.linalg.eigvalsh(bloch(u, k, t1, t2, lam))[0]
    g = np.linspace(-np.pi, np.pi, N, endpoint=False) + np.pi / N * 0.37   # offset grid (avoids sitting on k*)
    ks = np.array(list(itertools.product(g, repeat=3)))
    E = np.concatenate([np.linalg.eigvalsh(bloch_batch(u, ks[i:i+8000], t1, t2, lam))[:, 0] for i in range(0, len(ks), 8000)])
    rng = np.random.default_rng(seed)
    starts = list(ks[np.argsort(E)[:24]]) + list(rng.uniform(-np.pi, np.pi, (nrand, 3)))
    mins = []
    for k0 in starts:
        r = minimize(e0, k0, method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-13, maxiter=20000))
        r2 = minimize(e0, r.x, method='BFGS', options=dict(gtol=1e-10))
        x, f = (r2.x, r2.fun) if r2.fun < r.fun else (r.x, r.fun)
        mins.append((f, wrap(x)))
    mins.sort(key=lambda t: t[0])
    # cluster distinct minima
    dist = []
    for f, x in mins:
        if all(np.linalg.norm(wrap(x - y)) > 1e-3 for _, y in dist): dist.append((f, x))
    fmin, xmin = dist[0]
    Ep = np.linalg.eigvalsh(bloch(u, KP, t1, t2, lam)); Em = np.linalg.eigvalsh(bloch(u, -KP, t1, t2, lam))
    at = None
    if np.linalg.norm(wrap(xmin - KP)) < 1e-3: at = '+k*'
    elif np.linalg.norm(wrap(xmin + KP)) < 1e-3: at = '-k*'
    Eat = Ep if at == '+k*' else Em
    deg = int(np.sum(np.abs(Eat - Eat[0]) < 1e-8)) if at else int(np.sum(np.abs(np.linalg.eigvalsh(bloch(u, xmin, t1, t2, lam)) - fmin) < 1e-8))
    second = dist[1][0] - fmin if len(dist) > 1 else np.inf
    # number of distinct degenerate global minima (within 1e-7)
    ndeg = sum(1 for f, x in dist if f - fmin < 1e-7)
    return dict(t1=t1, t2=t2, lam=lam, tri=tri, Emin=fmin, kmin=xmin / (np.pi / 2), at=at, deg=deg,
                gap_kstar=(Eat[deg] - Eat[0]) if at else None, dE_other=abs(Ep[0] - Em[0]),
                next_min=second, n_global=ndeg, grid_min=E.min(), nloc=len(dist))

def fmt(r):
    return (f"t1={r['t1']:+.0f} tri={r['tri']} t2={r['t2']:+.3f} lam={r['lam']:+.3f}: Emin={r['Emin']:.6f} at {r['at'] or np.round(r['kmin'],3)}"
            f" deg={r['deg']} #globalmin={r['n_global']} gap@k*={r['gap_kstar'] if r['gap_kstar'] is None else round(r['gap_kstar'],4)}"
            f" |E(k*)-E(-k*)|={r['dE_other']:.4f} (/|t2|={r['dE_other']/abs(r['t2']):.3f}) next local min +{r['next_min']:.4g} (#loc {r['nloc']})")

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'note':
        sets = [(-1.0, 0.1, -0.5), (-1.0, -0.1, -0.5), (-1.0, 0.3, -0.5), (-1.0, 0.1, 0.5), (-1.0, 0.2, -0.3)]
        jobs = [(t1, t2, lam, 0, 48, 200, i) for i, (t1, t2, lam) in enumerate(sets)]
        jobs += [(1.0, t2, lam, 1, 48, 200, 9 + i) for i, (_, t2, lam) in enumerate(sets)]
    elif mode == 'scan':
        t2s = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
        lams = [-1.0, -0.75, -0.5, -0.3, -0.1, -0.03, 0.03, 0.1, 0.3, 0.5, 0.75, 1.0]
        jobs = [(-1.0, s * t2, lam, 0, 28, 30, 100 + i) for i, (t2, s, lam) in enumerate(itertools.product(t2s, (1, -1), lams))]
    elif mode == 'other':
        jobs = []
        for i, (t2, lam) in enumerate(itertools.product((0.1, 0.3, 0.6), (-0.5, 0.5))):
            jobs.append((1.0, t2, lam, 1, 28, 30, 500 + i))   # t1=+1, triangle pi
            jobs.append((1.0, t2, lam, 0, 28, 30, 600 + i))   # t1=+1, triangle 0
            jobs.append((-1.0, t2, lam, 1, 28, 30, 700 + i))  # t1=-1, triangle pi
        for i, t2 in enumerate((0.1, 0.3)):
            jobs.append((-1.0, t2, 0.0, 0, 28, 30, 800 + i))  # lam = 0
        for i, (t2, lam) in enumerate(((0.8, -0.5), (1.0, -0.5), (1.5, -0.5), (0.8, -1.0), (1.0, -1.5), (2.0, -1.0))):
            jobs.append((-1.0, t2, lam, 0, 28, 30, 900 + i))  # beyond the stated range
    with Pool(4) as p:
        for r in p.imap(analyse, jobs):
            print(fmt(r), flush=True)
