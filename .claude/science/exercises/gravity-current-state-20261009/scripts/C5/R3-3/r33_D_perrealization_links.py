"""R3-3 (a) per-realization check: link sum of a smooth source seen from one L7-LRL point, frame by frame, vs the ensemble mean.
phi_g = sum_{v in link set of L7} J(-g v)   (y = x - g v ranges over the realization's link past of x)
mean  = sum_m C^link_m int theta delta(x^2+m) J(-x) d^4x  (C^link from r33_A, R=300)
J = Gaussian of Euclidean width W centred on the past light cone at null distance D (observer frame)."""
import numpy as np, sys, time
exec(open('r33_A_L7_layers.py').read().split('# ---------- (3) counting')[0].replace('print(','(lambda *a,**k: None)('))
t0 = time.time()
Clink = {1: 0.5035, 2: 0.7444, 3: 0.2496, 4: 0.2493, 5: 0.3111, 6: 0.1267, 7: 0.0199}   # r33_A_R300.out
Rbig = float(sys.argv[1]) if len(sys.argv) > 1 else 500.0
links = []
n0max = int(Rbig/np.sqrt(14)) + 2
for a in range(1, n0max+1):
    rr = int(np.floor(np.sqrt(7)*a)); g = np.arange(-rr, rr+1)
    X, Y = np.meshgrid(g, g, indexing='ij'); X = X.ravel(); Y = Y.ravel()
    lo = 7*a*a - 7 - X**2 - Y**2; hi = 7*a*a - 1 - X**2 - Y**2
    rows = []
    for z in range(0, rr+1):
        k = (z*z >= lo) & (z*z <= hi)
        if not k.any(): continue
        for zz in ([z] if z == 0 else [z, -z]):
            rows.append(np.stack([np.full(k.sum(), a), X[k], Y[k], np.full(k.sum(), zz)], 1))
    if not rows: continue
    V = np.concatenate(rows)
    V = V[7*V[:, 0]**2 + (V[:, 1:]**2).sum(1) <= Rbig**2]
    if len(V) == 0: continue
    RV = reduce(V)
    isl = np.array([direct.get(keyof(r)) == 0 for r in RV])
    links.append(V[isl])
Lk = np.concatenate(links).astype(float)
X = np.stack([np.sqrt(7)*Lk[:, 0], Lk[:, 1], Lk[:, 2], Lk[:, 3]], 1)     # physical link vectors (future)
print(f"link vectors with |x|_E <= {Rbig}: {len(X)}  ({time.time()-t0:.1f}s)")
def boost(eta, nhat):
    nhat = nhat/np.linalg.norm(nhat); Bm = np.eye(4)
    Bm[0, 0] = np.cosh(eta); Bm[0, 1:] = Bm[1:, 0] = np.sinh(eta)*nhat
    Bm[1:, 1:] += (np.cosh(eta)-1)*np.outer(nhat, nhat)
    return Bm
def randrot(rng):
    q, r = np.linalg.qr(rng.normal(size=(3, 3))); q *= np.sign(np.diag(r))
    if np.linalg.det(q) < 0: q[:, 0] *= -1
    R4 = np.eye(4); R4[1:, 1:] = q; return R4
def mean_val(D, W):
    # int theta delta(x^2+m) J(-x) d^4x = int d^3x /(2t) J(-t,-x), t = sqrt(r^2+m); J centred at yc = (-D, -D,0,0)
    tot = 0.0
    # cylindrical coords around the x1 axis
    x1 = np.linspace(D - 6*W, D + 6*W, 601); rho = np.linspace(0, 6*W, 301)
    X1, RHO = np.meshgrid(x1, rho, indexing='ij')
    for m, cm in Clink.items():
        t = np.sqrt(X1**2 + RHO**2 + m)
        J = np.exp(-((t - D)**2 + (X1 - D)**2 + RHO**2)/(2*W*W))
        f = 2*np.pi*RHO*J/(2*t)
        tot += cm*np.trapezoid(np.trapezoid(f, rho, axis=1), x1)
    return tot
rng = np.random.default_rng(1)
for D in (10.0, 20.0, 40.0, 80.0, 120.0):
    W = D/5
    mv = mean_val(D, W)
    vals = []
    for s in range(60):
        eta = rng.uniform(0, 1.0)
        Gm = randrot(rng) @ boost(eta, rng.normal(size=3)) @ randrot(rng)
        Y = X @ Gm.T                      # g v
        yc = np.array([D, D, 0, 0])       # -y_c (future-pointing)
        d2 = ((Y - yc)**2).sum(1)
        vals.append(np.exp(-d2/(2*W*W)).sum())
    vals = np.array(vals)
    # reach check: need e^eta * (|yc|+6W) < Rbig
    reach = np.exp(1.0)*(np.sqrt(2)*D + 6*W)
    print(f"D={D:5.1f} W={W:5.1f}: mean {mv:10.3f}; per-frame phi: avg {vals.mean():10.3f}, sd/mean {vals.std()/mv:.4f}, "
          f"min/max {(vals.min()/mv):.4f}/{(vals.max()/mv):.4f}  (reach {reach:.0f} vs Rbig {Rbig:.0f}); Poisson sqrt(3/mean) {np.sqrt(3/mv):.4f}")
print(f"time {time.time()-t0:.1f}s")
