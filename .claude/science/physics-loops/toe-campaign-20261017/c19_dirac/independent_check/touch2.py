"""(a) survey: do bands 0,1 (t1=-1) touch away from +-k* for random (t2, delta, X)?  Scan the lines
(pi/2)(1, a, -a) found in touch.py and a full-BZ gap minimization; (b) Berry flux of the extra touchings
(runner H); (c) mass on the best candidate: global gap vs 2 m_D."""
import glob, pickle
import numpy as np
from scipy.optimize import minimize
from core import *
from bases import get
rng = np.random.default_rng(8)
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4
Xb = get('X_r1'); Mb = get('Q_onsite_im_A2')
def build(t1, t2, dl, c):
    X = addm(*Xb, coeffs=list(c / np.linalg.norm(c))); nrm = max(np.abs(M).max() for M in X.values())
    return addm(hop(t1, t2), X, coeffs=[1, dl / nrm])
def dist(k, k0): return np.linalg.norm((k - k0 + np.pi) % (2 * np.pi) - np.pi)
def touchings(H, lev=0, N=20, nst=30):
    g = (np.arange(N) + 0.37) * 2 * np.pi / N
    KG = np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T
    E = np.linalg.eigvalsh(bloch_batch(H, KG)); gap = E[:, lev + 1] - E[:, lev]
    found = []
    for i in np.argsort(gap)[:nst]:
        f = lambda k: np.diff(np.linalg.eigvalsh(bloch(H, k))[lev:lev + 2])[0]
        r = minimize(f, KG[i], method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-14, maxiter=6000))
        kk = r.x % (2 * np.pi)
        if r.fun < 1e-6 and dist(kk, KS) > 1e-2 and dist(kk, -KS) > 1e-2 and all(dist(kk, q) > 1e-3 for q, _ in found):
            found.append((kk, np.linalg.eigvalsh(bloch(H, kk))[lev]))
    return found, np.linalg.eigvalsh(bloch(H, KS))[lev]
print("(a) survey, t1 = -1, lowest doublet at k*")
nt = 0; nx = 0
for trial in range(14):
    t2 = rng.uniform(-0.6, 0.6); dl = 10 ** rng.uniform(-1.5, -0.3); H = build(-1.0, t2, dl, rng.normal(size=9))
    e = np.linalg.eigvalsh(bloch(H, KS))
    if abs(e[0] - e[1]) > 1e-8 or abs(e[1] - e[2]) < 1e-8: continue
    nt += 1; found, Ed = touchings(H)
    nx += bool(found)
    if found:
        Ex = sorted(set(np.round([x[1] for x in found], 6)))
        print(f"  t2={t2:+.3f} delta={dl:.3f}: {len(found)} extra touchings of bands 0/1; energies - E_d: {np.round(np.array(Ex) - Ed, 5)}; sample k/(pi/2) {np.round(found[0][0]/(np.pi/2), 4)}")
    else:
        print(f"  t2={t2:+.3f} delta={dl:.3f}: no extra touching found")
print(f"  -> extra touchings in {nx}/{nt} sets")

R = pickle.load(open('runner_blocks.pkl', 'rb'))
Hrun = {tuple(-x for x in sh): M for sh, M in R['bl'].items()}
found, Ed = touchings(Hrun)
def berry(H, k0, band, r=0.004, n=20):
    th = np.linspace(0, np.pi, n + 1); ph = np.linspace(0, 2*np.pi, 2*n, endpoint=False)
    U = [[np.linalg.eigh(bloch(H, k0 + r*np.array([np.sin(t)*np.cos(p), np.sin(t)*np.sin(p), np.cos(t)])))[1][:, band] for p in ph] for t in th]
    tot = 0
    for i in range(n):
        for j in range(2*n):
            a, b, c, d = U[i][j], U[i+1][j], U[i+1][(j+1) % (2*n)], U[i][(j+1) % (2*n)]
            tot += np.angle(np.vdot(a, b)*np.vdot(b, c)*np.vdot(c, d)*np.vdot(d, a))
    return tot / (2*np.pi)
fl = [round(berry(Hrun, k, 0), 3) for k, _ in found]
print(f"\n(b) runner H: {len(found)} extra touchings at E - E_d = {found[0][1]-Ed:+.5f}; Berry flux of band 0 around each: {fl}; sum {sum(fl)}")
Qs = [any(dist((k + Q) % (2*np.pi), q) < 1e-4 for q, _ in found) for k, _ in found]
print("    set closed under k -> k + Q:", all(Qs))
# (c) mass on candidates
print("\n(c) candidates with mass: global gap vs 2 m_D")
cs = []
for f in sorted(glob.glob('global_search_*.pkl')):
    for fun, t1, x in pickle.load(open(f, 'rb')):
        if fun < 1e-3 and 10 ** x[1] > 1e-3 and abs(x[0]) > 1e-3 and t1 < 0: cs.append(x)
M = addm(*Mb, coeffs=list(rng.normal(size=len(Mb)))); nr = max(np.abs(v).max() for v in M.values()); M = {k: v / nr for k, v in M.items()}
N = 20; g = (np.arange(N) + 0.37) * 2 * np.pi / N
KG = np.vstack([np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T, KS])
for x in cs[:3]:
    H = build(-1.0, x[0], 10 ** x[1], x[2:])
    for m in (3e-4, 1e-3, 3e-3, 1e-2):
        Mm = {k: m * v for k, v in M.items()}
        Ef = np.linalg.eigvalsh(fold_batch(H, Mm, KG)); e = np.linalg.eigvalsh(fold(H, Mm, KS)); mD = (e[2] - e[1]) / 2
        top_i = np.argsort(-Ef[:, 1])[:6]; bot_i = np.argsort(Ef[:, 2])[:6]
        top = max(-minimize(lambda k: -np.linalg.eigvalsh(fold(H, Mm, k))[1], KG[i], method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-13)).fun for i in top_i)
        bot = min(minimize(lambda k: np.linalg.eigvalsh(fold(H, Mm, k))[2], KG[i], method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-13)).fun for i in bot_i)
        top = max(top, Ef[:, 1].max()); bot = min(bot, Ef[:, 2].min())
        print(f"  t2={x[0]:+.4f} delta={10**x[1]:.4f} m={m:.0e}: m_D={mD:.2e}; global gap {bot-top:+.2e} (2 m_D = {2*mD:.2e})")
