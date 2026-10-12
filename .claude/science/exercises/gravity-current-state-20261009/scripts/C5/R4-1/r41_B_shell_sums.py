"""R4-1 (B): per-realization shell sums of a smooth test function, frame by frame, vs the exact ensemble mean.
S_m(g, l) = sum_{n in Z^4, n0>0, 7n0^2-|n|^2 = m} phi(g D n),  phi(y) = exp(-|y|_E^2/(2 l^2))  (observer frame),
mean      = C_m * I_m(l),  I_m(l) = int theta(x0) delta(x^2+m) phi(x) d^4x = 2 pi int r^2/sqrt(r^2+m) exp(-(2r^2+m)/(2l^2)) dr.
g = B(eta) R : random rotation of the lattice, then a boost; eta drawn with density ~ sinh^2(eta) on [0, eta_max].
Output: npz with S[frame, l, m], I[l, m].
"""
import numpy as np, sys, time
from scipy.integrate import quad
t0 = time.time()
M = int(sys.argv[1]) if len(sys.argv) > 1 else 96
Rmax = float(sys.argv[2]) if len(sys.argv) > 2 else 440.0
NF = int(sys.argv[3]) if len(sys.argv) > 3 else 40
eta_max = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
seed = int(sys.argv[5]) if len(sys.argv) > 5 else 7
ells = np.array([float(x) for x in (sys.argv[6].split(",") if len(sys.argv) > 6 else "2,3,4,6,8,11,15,19".split(","))])
assert 8.0*ells.max()*np.exp(eta_max) <= Rmax + 1e-9, "reach too small"

# enumerate shell vectors with 1 <= m <= M, |Dn|_E^2 = 14 n0^2 - m <= Rmax^2
rows = []; ms = []
n0max = int(np.sqrt((Rmax**2 + M)/14.0))
for a in range(1, n0max+1):
    hi = 7*a*a - 1; lo = 7*a*a - M
    R = int(np.floor(np.sqrt(hi)))
    g = np.arange(-R, R+1)
    X, Y = np.meshgrid(g, g, indexing='ij'); X = X.ravel(); Y = Y.ravel()
    s = X*X + Y*Y
    k = s <= hi; X = X[k]; Y = Y[k]; s = s[k]
    zlo = np.ceil(np.sqrt(np.maximum(lo - s, 0))).astype(np.int64)
    zhi = np.floor(np.sqrt(hi - s)).astype(np.int64)
    # fix float rounding
    zhi = np.where((zhi+1)**2 <= hi - s, zhi+1, zhi); zhi = np.where(zhi**2 > hi - s, zhi-1, zhi)
    zlo = np.where((zlo-1) >= 0, np.where((zlo-1)**2 >= lo - s, zlo-1, zlo), zlo)
    zlo = np.where(zlo**2 < lo - s, zlo+1, zlo)
    cnt = np.maximum(zhi - zlo + 1, 0)
    if cnt.sum() == 0: continue
    rep = np.repeat(np.arange(len(X)), cnt)
    off = np.arange(cnt.sum()) - np.repeat(np.cumsum(cnt) - cnt, cnt)
    Z = zlo[rep] + off
    Xr = X[rep]; Yr = Y[rep]
    # both signs of z (z=0 once)
    nz = Z != 0
    Xa = np.concatenate([Xr, Xr[nz]]); Ya = np.concatenate([Yr, Yr[nz]]); Za = np.concatenate([Z, -Z[nz]])
    m = 7*a*a - (Xa*Xa + Ya*Ya + Za*Za)
    assert m.min() >= 1 and m.max() <= M
    rows.append(np.stack([np.full(len(Xa), a), Xa, Ya, Za], 1).astype(np.int16)); ms.append(m.astype(np.int16))
V = np.concatenate(rows); mm = np.concatenate(ms).astype(np.int64)
P = np.stack([np.sqrt(7.0)*V[:, 0], V[:, 1], V[:, 2], V[:, 3]], 1)
print(f"M={M} Rmax={Rmax} n0max={n0max}: {len(V)} shell vectors ({time.time()-t0:.1f}s)", flush=True)

def I_m(m, l):
    f = lambda r: r*r/np.sqrt(r*r+m)*np.exp(-(2*r*r+m)/(2*l*l))
    v, e = quad(f, 0, np.inf, epsabs=0, epsrel=1e-13, limit=400)
    return 2*np.pi*v
I = np.array([[I_m(m, l) for m in range(1, M+1)] for l in ells])

def boost(eta, nhat):
    nhat = nhat/np.linalg.norm(nhat); Bm = np.eye(4)
    Bm[0, 0] = np.cosh(eta); Bm[0, 1:] = Bm[1:, 0] = np.sinh(eta)*nhat
    Bm[1:, 1:] += (np.cosh(eta)-1)*np.outer(nhat, nhat)
    return Bm
def randrot(rng):
    q, r = np.linalg.qr(rng.normal(size=(3, 3))); q *= np.sign(np.diag(r))
    if np.linalg.det(q) < 0: q[:, 0] *= -1
    R4 = np.eye(4); R4[1:, 1:] = q; return R4
rng = np.random.default_rng(seed)
S = np.zeros((NF, len(ells), M))
etas = []
for f in range(NF):
    # eta with density ~ sinh^2 on [0, eta_max] (rejection)
    while True:
        e = rng.uniform(0, eta_max)
        if rng.uniform() < (np.sinh(e)/np.sinh(eta_max))**2: break
    if f == 0: e = 0.0
    etas.append(e)
    G = boost(e, np.array([0, 0, 1.0])) @ randrot(rng)
    Y = P @ G.T
    r2 = (Y*Y).sum(1)
    for j, l in enumerate(ells):
        w = np.exp(-r2/(2*l*l))
        S[f, j] = np.bincount(mm - 1, weights=w, minlength=M)
    print(f"frame {f:3d} eta={e:.3f} ({time.time()-t0:.0f}s)", flush=True)
C = np.load('C_siegel.npy')[:M+1]
np.savez(f'r41_B_M{M}_seed{seed}_eta{eta_max}.npz', S=S, I=I, ells=ells, etas=np.array(etas), C=C)
# quick single-shell summary
print("\nsingle-shell relative deviation  (S_m - C_m I_m)/(C_m I_m): frame mean / frame sd")
for j, l in enumerate(ells):
    rel = (S[:, j, :] - C[1:]*I[j])/(C[1:]*I[j])
    print(f"l={l:5.1f}  " + "  ".join(f"m={m}:{rel[:, m-1].mean():+.4f}/{rel[:, m-1].std():.4f}" for m in (1, 2, 3, 4, 7, 16, 31, 64)))
print(f"done {time.time()-t0:.0f}s")
