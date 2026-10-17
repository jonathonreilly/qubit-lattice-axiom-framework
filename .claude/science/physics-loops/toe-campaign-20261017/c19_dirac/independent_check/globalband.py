"""Item 5: is the Dirac point the global low-energy feature?  Runner's H, then a search over
(t1 sign, t2, delta, X in the 9-dim space) for a clean Weyl semimetal (bands lev and lev+1 touch only at
+-k*, band lev <= E_d <= band lev+1 everywhere), then the mass and the global gap."""
import pickle, sys
import numpy as np
from scipy.optimize import minimize
from core import *
from bases import get

rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 3)
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4
Xb = get('X_r1'); Mb = get('Q_onsite_im_A2')
N = 16
g = np.arange(N) * 2 * np.pi / N
KG = np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T

def bands_on(H, ks): return np.linalg.eigvalsh(bloch_batch(H, ks))
def refine(H, k0, band, sign):
    f = lambda k: sign * np.linalg.eigvalsh(bloch(H, k))[band]
    r = minimize(f, k0, method='Nelder-Mead', options=dict(xatol=1e-7, fatol=1e-10, maxiter=4000))
    return sign * r.fun, r.x
def doublets_at_kstar(H):
    e = np.linalg.eigvalsh(bloch(H, KS)); out = []; i = 0
    while i < 12:
        j = i
        while j + 1 < 12 and abs(e[j+1] - e[i]) < 1e-8: j += 1
        if j - i + 1 == 2: out.append((i, e[i]))
        i = j + 1
    return out
def badness(H, refine_top=3):
    """for each doublet (lev, E_d): over-the-node amount max(band lev) - E_d and E_d - min(band lev+1)."""
    E = bands_on(H, KG); res = []
    for lev, Ed in doublets_at_kstar(H):
        a = E[:, lev] - Ed; b = Ed - E[:, lev + 1]
        top = np.argsort(-a)[:refine_top]; bot = np.argsort(-b)[:refine_top]
        amax = max(refine(H, KG[i], lev, -1)[0] - Ed for i in top)
        bmax = max(Ed - refine(H, KG[i], lev + 1, +1)[0] for i in bot)
        res.append((lev, Ed, amax, bmax))
    return res

# ---- runner H
R = pickle.load(open('runner_blocks.pkl', 'rb'))
bl, blM, kst = R['bl'], R['blM'], R['kst']
# convert runner blocks (e^{+ik.sh}) to mine (e^{-ik.sh'}): sh' = -sh
Hrun = {tuple(-x for x in sh): M for sh, M in bl.items()}
Mrun = {tuple(-x for x in sh): M for sh, M in blM.items()}
e = np.linalg.eigvalsh(bloch(Hrun, KS)); print("runner H in my convention: levels at my k*:", np.round(e[:4], 6))
print("runner H: doublets at k*:", doublets_at_kstar(Hrun))
for lev, Ed, a, b in badness(Hrun):
    print(f"  doublet at level {lev} (E_d = {Ed:.6f}): max band {lev} - E_d = {a:+.5f};  E_d - min band {lev+1} = {b:+.5f}")
E = bands_on(Hrun, KG)
print(f"  band 0 range [{E[:,0].min():.4f}, {E[:,0].max():.4f}], band 1 range [{E[:,1].min():.4f}, {E[:,1].max():.4f}] (grid)")
# where is band 0 above E_N?
EN = e[0]; over = KG[E[:, 0] > EN + 1e-9]
print(f"  fraction of BZ (grid) where band 0 > E_N: {len(over)/len(KG):.3f}; max at k/pi = {np.round(KG[np.argmax(E[:,0])]/np.pi, 3)}")
for m in (0.05,):
    Ef = np.linalg.eigvalsh(fold_batch(Hrun, {k: m * v for k, v in Mrun.items()}, KG))
    gap = Ef[:, 2].min() - Ef[:, 1].max()
    print(f"  massive (runner m = {m}, m_D = 0.0702): folded min(band 2) - max(band 1) = {gap:+.4f}  (vs 2 m_D = 0.1404)")

# ---- search
print("\n== search for a clean Weyl semimetal: params (t1=+-1, t2, delta, X in 9-dim)")
def build(t1, t2, dl, c):
    X = addm(*Xb, coeffs=list(c / np.linalg.norm(c)))
    nrm = max(np.abs(M).max() for M in X.values())
    return addm(hop(t1, t2), X, coeffs=[1, dl / nrm])
best = []
def score(t1, t2, dl, c):
    H = build(t1, t2, dl, c); E = bands_on(H, KG); out = []
    for lev, Ed in doublets_at_kstar(H):
        a = (E[:, lev] - Ed).max(); b = (Ed - E[:, lev + 1]).max(); out.append((max(a, b), lev, Ed, a, b))
    return min(out) if out else (np.inf,)
for trial in range(300):
    t1 = rng.choice([-1.0, 1.0]); t2 = rng.uniform(-1.5, 1.5); dl = 10 ** rng.uniform(-1.5, 0.7); c = rng.normal(size=9)
    s = score(t1, t2, dl, c); best.append((s[0], t1, t2, dl, c, s))
best.sort(key=lambda x: x[0])
print("  best 8 random (badness = max over grid of overshoot, 0 means clean):")
for b in best[:8]: print(f"   bad={b[0]:+.4f} t1={b[1]:+.0f} t2={b[2]:+.3f} delta={b[3]:.3f} lev={b[5][1]} E_d={b[5][2]:.4f} (a={b[5][3]:+.4f}, b={b[5][4]:+.4f})")
# local optimization from the best few
def obj(x, t1):
    t2, ldl = x[0], x[1]; c = x[2:]
    return score(t1, t2, 10 ** ldl, c)[0]
results = []
for b in best[:6]:
    x0 = np.concatenate([[b[2], np.log10(b[3])], b[4]])
    r = minimize(obj, x0, args=(b[1],), method='Nelder-Mead', options=dict(maxiter=1500, xatol=1e-5, fatol=1e-7))
    results.append((r.fun, b[1], r.x)); print(f"   optimized from bad={b[0]:+.4f}: bad={r.fun:+.5f}  t1={b[1]:+.0f} t2={r.x[0]:+.4f} delta={10**r.x[1]:.4f}")
results.sort(key=lambda x: x[0])
pickle.dump(results, open(f'global_search_{rng.bit_generator.seed_seq.entropy}.pkl', 'wb'))
f, t1, x = results[0]
H = build(t1, x[0], 10 ** x[1], x[2:])
print("\n  best: refined badness:", badness(H))
