"""R5-2 (A): per-realization Gaussian sums over WHOLE classes of L7 vectors, frame by frame.
Tests whether infinite-orbit 'scale-free' weights (f_m = 1, f_m = m on ALL timelike shells) cancel the
automorphic l^1 growth that R4-1 found for finite-orbit weights.
  T0  = sum_{v timelike future} phi_l(gv)               (f_m = 1, all m)
  T1  = sum_{v timelike future} m(v) phi_l(gv)          (f_m = m)
  Tfin= sum_{v timelike future, m<=7} phi_l(gv)         (finite-orbit reference, 'bad')
  S1  = sum_{v timelike future, m==1} phi_l(gv)         (single shell reference)
  F   = sum_{all v in L7} phi_l(gv)                     (full lattice: Poisson => frame-independent; truncation check)
phi_l(y) = exp(-|y|_E^2/(2 l^2)) in the observer frame;  g = B(eta) R.
"""
import numpy as np, sys, time
t0 = time.time()
Rlat = float(sys.argv[1]); NF = int(sys.argv[2]); eta_max = float(sys.argv[3]); seed = int(sys.argv[4])
ells = np.array([float(x) for x in sys.argv[5].split(',')])
assert 7.0*ells.max()*np.exp(eta_max) <= Rlat + 1e-9, "reach"
rng = np.random.default_rng(seed)
def boost(eta, nhat):
    nhat = nhat/np.linalg.norm(nhat); Bm = np.eye(4)
    Bm[0, 0] = np.cosh(eta); Bm[0, 1:] = Bm[1:, 0] = np.sinh(eta)*nhat
    Bm[1:, 1:] += (np.cosh(eta)-1)*np.outer(nhat, nhat); return Bm
def randrot(rng):
    q, r = np.linalg.qr(rng.normal(size=(3, 3))); q *= np.sign(np.diag(r))
    if np.linalg.det(q) < 0: q[:, 0] *= -1
    R4 = np.eye(4); R4[1:, 1:] = q; return R4
Ms = []; etas = []
for f in range(NF):
    while True:
        e = rng.uniform(0, eta_max)
        if rng.uniform() < (np.sinh(e)/np.sinh(eta_max))**2: break
    if f == 0: e = 0.0
    G = boost(e, np.array([0, 0, 1.0])) @ randrot(rng)
    Ms.append(G.T @ G); etas.append(e)
Ms = np.array(Ms)
K = int(np.floor(Rlat))
g = np.arange(-K, K+1)
X, Y, Z = np.meshgrid(g, g, g, indexing='ij'); X = X.ravel(); Y = Y.ravel(); Z = Z.ravel()
s = X*X + Y*Y + Z*Z; k = s <= Rlat**2; X = X[k].astype(float); Y = Y[k].astype(float); Z = Z[k].astype(float); s = s[k]
order = np.argsort(s); X = X[order]; Y = Y[order]; Z = Z[order]; s = s[order]
nL = len(ells); keys = ['T0', 'T1', 'Tfin', 'S1', 'F']
acc = {kk: np.zeros((NF, nL)) for kk in keys}
n0max = int(np.floor(Rlat/np.sqrt(7)))
npts = 0
for n0 in range(-n0max, n0max+1):
    lim = Rlat**2 - 7*n0*n0
    j = np.searchsorted(s, lim, side='right')
    x1, x2, x3, ss = X[:j], Y[:j], Z[:j], s[:j]
    x0 = np.sqrt(7.0)*n0*np.ones(j)
    m = 7*n0*n0 - ss                         # m = -Q(v) ; timelike iff m > 0
    tl = (m > 0) & (n0 > 0)
    P = np.stack([x0, x1, x2, x3], 1)
    npts += j
    for f in range(NF):
        q = np.einsum('ni,ij,nj->n', P, Ms[f], P)
        for jl, l in enumerate(ells):
            w = np.exp(-q/(2*l*l))
            acc['F'][f, jl] += w.sum()
            if tl.any():
                wt = w[tl]; mt = m[tl]
                acc['T0'][f, jl] += wt.sum()
                acc['T1'][f, jl] += (wt*mt).sum()
                acc['Tfin'][f, jl] += wt[mt <= 7].sum()
                acc['S1'][f, jl] += wt[mt == 1].sum()
print(f"Rlat={Rlat} NF={NF} eta_max={eta_max} seed={seed} points={npts} ({time.time()-t0:.0f}s)")
np.savez(f'r52_A_R{int(Rlat)}_NF{NF}_eta{eta_max}_s{seed}.npz', ells=ells, etas=np.array(etas), **acc)
for kk in keys:
    a = acc[kk]
    print(f"\n[{kk}]   l   mean_over_frames   sd_over_frames   sd/mean   (frame0 - mean)")
    for jl, l in enumerate(ells):
        mu = a[:, jl].mean(); sd = a[:, jl].std(ddof=1)
        print(f"  {l:5.2f}  {mu:18.10f}  {sd:14.6e}  {sd/abs(mu):10.3e}  {a[0, jl]-mu:+.3e}")
print(f"done {time.time()-t0:.0f}s")
