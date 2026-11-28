#!/usr/bin/env python3
"""GUIDE (row 918): twist ratio rho = Z^v/Z^0 on the torus t x b^3 by interpolation of the twist-stack coupling.
Usage: twist.py t b beta nsgrid nth nmeas seed ndir [spin(0/1)] [n_or] [outnpz]
The stack of direction i (i = 1..ndir) is the set of (0, i) plaquettes with x_0 = t-1, x_i = b-1 (all other
coordinates): b^2 plaquettes. All stacks get coefficient s; s runs over nsgrid equally spaced values from 1 to -1.
s = 1 is Z^0, s = -1 is the twisted Z^(e) with e = (1,..,1,0,..) (ndir twists).
log rho = log Z(-1) - log Z(1) = -beta int_{-1}^{1} <X>_s ds, X = sum of x_p over the stacks.
Estimators: trapezoid and Simpson on the grid, and Bennett acceptance ratio (BAR) between neighbours.
spin=1: at s = +1 and s = -1 also measure the row-860 spin-weight estimator on all temporal plaquettes of the time
steps x_0 = 0..t-2 (the stack step x_0 = t-1 is excluded), per time step, for EXC (family 4).
"""
import sys, json, time
import numpy as np
from scipy.optimize import brentq
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from su2lat import Lattice, binned_err, pl_index, improved_plaq

t, b = int(sys.argv[1]), int(sys.argv[2]); beta = float(sys.argv[3])
ns, nth, nme, seed, ndir = (int(x) for x in sys.argv[4:9])
spin = len(sys.argv) > 9 and sys.argv[9] == '1'
n_or = int(sys.argv[10]) if len(sys.argv) > 10 else 3
outnpz = sys.argv[11] if len(sys.argv) > 11 else None
lat = Lattice((t, b, b, b), beta, seed)
stacks = []
for i in range(1, ndir+1):
    k = pl_index(0, i)
    sites = np.nonzero((lat.coords[0] == t-1) & (lat.coords[i] == b-1))[0]
    stacks.append((k, sites))
nst = sum(s.size for _, s in stacks)
sgrid = np.linspace(1.0, -1.0, ns)
tsites = np.nonzero(lat.coords[0] < t-1)[0]
tstep = lat.coords[0][tsites]
X = []; Y = []; spin_out = {}
T0 = time.time()
for si, s in enumerate(sgrid):
    for k, sites in stacks: lat.C[k, sites] = s
    lat.refresh()
    for _ in range(nth if si > 0 else 3*nth): lat.sweep(n_or)
    xs = []; ys = []; sw = []
    for m in range(nme):
        lat.sweep(n_or)
        x = lat.plaquettes()
        xs.append(sum(x[k, sites].sum() for k, sites in stacks))
        ys.append(sum(improved_plaq(lat, k, sites).sum() for k, sites in stacks))
        if spin and si in (0, ns-1) and m % 2 == 0:
            w = sum(lat.spin_weights(k, tsites) for k in (0, 1, 2))   # (nmax+1, len) summed over 3 planes
            per = np.stack([np.bincount(tstep, weights=w[n], minlength=t-1)[:t-1] for n in range(w.shape[0])])
            sw.append(per.mean(axis=1))   # per time step average count, each spin
    X.append(np.array(xs)); Y.append(np.array(ys))
    if spin and si in (0, ns-1):
        spin_out['plus' if si == 0 else 'minus'] = np.array(sw)
    print(json.dumps(dict(s=float(s), X=float(np.mean(xs)), dX=float(binned_err(xs)), Y=float(np.mean(ys)), dY=float(binned_err(ys)), sec=round(time.time()-T0, 1))), flush=True)

X = [np.asarray(a) for a in X]
means = np.array([a.mean() for a in X]); errs = np.array([binned_err(a) for a in X])
ds = sgrid[1] - sgrid[0]   # negative
# integral from s=1 down to s=-1 of beta <X> ds (ds negative) gives log Z(-1) - log Z(1)
trap = beta * ds * (means.sum() - 0.5*(means[0] + means[-1]))
trap_err = beta * abs(ds) * np.sqrt((errs[1:-1]**2).sum() + 0.25*(errs[0]**2 + errs[-1]**2))
simp = None
if (ns - 1) % 2 == 0:
    wts = np.ones(ns); wts[1:-1:2] = 4; wts[2:-1:2] = 2
    simp = beta * ds / 3 * (wts * means).sum()
    simp_err = beta * abs(ds) / 3 * np.sqrt(((wts*errs)**2).sum())

def bar(wf, wr):
    # wf: work beta*(s1-s0)*X sampled at s0 (log weight ratio of s1 over s0); wr: same work sampled at s1.
    # Solve sum f(wf - dF) = sum f(-(wr - dF))... standard form with dF = log Z1/Z0.
    nf, nr = len(wf), len(wr); M = np.log(nf/nr)
    def g(dF):
        a = 1.0/(1.0 + np.exp(M - (wf - dF))) ; c = 1.0/(1.0 + np.exp((wr - dF) - M))
        return a.sum() - c.sum()
    lo = min(wf.min(), wr.min()) - 50; hi = max(wf.max(), wr.max()) + 50
    return brentq(g, lo, hi)

barsum = 0.0; barvar = 0.0
for k in range(ns-1):
    s0, s1 = sgrid[k], sgrid[k+1]
    wf = beta*(s1-s0)*X[k]; wr = beta*(s1-s0)*X[k+1]
    d = bar(wf, wr); barsum += d
    # crude error: blocks
    nb = 8; dd = []
    m0 = len(wf)//nb; m1 = len(wr)//nb
    for j in range(nb):
        dd.append(bar(wf[j*m0:(j+1)*m0], wr[j*m1:(j+1)*m1]))
    barvar += np.var(dd, ddof=1)/nb
ym = np.array([a.mean() for a in Y]); ye = np.array([binned_err(a) for a in Y])
if (ns - 1) % 2 == 0:
    simpY = beta * ds / 3 * (wts * ym).sum(); simpY_err = beta * abs(ds) / 3 * np.sqrt(((wts*ye)**2).sum())
else:
    simpY = beta * ds * (ym.sum() - 0.5*(ym[0] + ym[-1])); simpY_err = beta*abs(ds)*np.sqrt((ye**2).sum())
res = dict(logrho_simp_improved=float(simpY), err_simp_improved=float(simpY_err), t=t, b=b, beta=beta, ndir=ndir, ns=ns, nth=nth, nmeas=nme, seed=seed, nstack=int(nst),
           logrho_trap=float(trap), err_trap=float(trap_err),
           logrho_simp=None if simp is None else float(simp), err_simp=None if simp is None else float(simp_err),
           logrho_bar=float(barsum), err_bar=float(np.sqrt(barvar)), sec=round(time.time()-T0, 1))
res['rho_bar'] = float(np.exp(barsum))
if spin:
    for key in ('plus', 'minus'):
        a = spin_out[key]
        res['spin_'+key] = [float(v) for v in a.mean(axis=0)]
        res['spin_'+key+'_err'] = [float(v) for v in binned_err(a)]
        res['spin_'+key+'_hi'] = float(a[:, 5::2].sum(axis=1).mean()); res['spin_'+key+'_hi_err'] = float(binned_err(a[:, 5::2].sum(axis=1)))
        res['spin_'+key+'_half'] = float(a[:, 1::2].sum(axis=1).mean()); res['spin_'+key+'_half_err'] = float(binned_err(a[:, 1::2].sum(axis=1)))
        res['spin_'+key+'_3h'] = float(a[:, 3]. mean()); res['spin_'+key+'_3h_err'] = float(binned_err(a[:, 3]))
print(json.dumps(res), flush=True)
if outnpz:
    np.savez(outnpz, sgrid=sgrid, **{f'X{k}': X[k] for k in range(ns)}, **{f'Y{k}': Y[k] for k in range(ns)})
