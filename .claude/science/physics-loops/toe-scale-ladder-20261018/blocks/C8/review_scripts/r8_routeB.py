#!/usr/bin/env python3
"""Route B (reviewer): q^2 coefficient of the TT bubble by
  * the reviewer's matrix-route walk/generator/vertex/band sums (r8_walk.py),
  * pointwise t^2 coefficient from an exact 5-point even-polynomial interpolation in t (not Richardson),
  * BZ integral by tensor tanh-sinh (double-exponential) quadrature on the 8 octant cubes, whose corners
    are the 8 TRIMs (all possible singular points); no partition of unity, no spherical rule.
Checkpointed to logs/r8_routeB.json.  Usage: r8_routeB.py <walk> <n> [theta] [hhat_angle] [kind]
"""
import sys, os, json, time, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r8_walk as rw
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', 'r8_routeB.json')

def eps_author(qn, pol):
    """TT bases (geometry only; same orientation conventions as the NOTE's table)."""
    if qn == 'z':
        qh = np.array([0, 0, 1.0]); u1 = np.array([1.0, 0, 0]); u2 = np.array([0, 1.0, 0])
    elif qn == 'f':
        qh = np.array([1.0, 1, 0])/np.sqrt(2); u1 = np.array([1.0, -1, 0])/np.sqrt(2); u2 = np.array([0, 0, 1.0])
    elif qn == 'd':
        qh = np.ones(3)/np.sqrt(3); u1 = np.array([1.0, -1, 0])/np.sqrt(2); u2 = np.array([1.0, 1, -2])/np.sqrt(6)
    elif qn == 'w':   # (2,3,6)/7: a generic direction NOT used by the author (fit-prediction test)
        qh = np.array([2.0, 3, 6])/7; u1 = np.array([3.0, -2, 0])/np.sqrt(13); u2 = np.cross(qh, u1)
    e = (np.outer(u1, u1) - np.outer(u2, u2))/np.sqrt(2) if pol == 'A' else (np.outer(u1, u2) + np.outer(u2, u1))/np.sqrt(2)
    return qh, e

def ts_nodes(n, T=3.0):
    tau = -T + (np.arange(n) + 0.5)*(2*T/n); ht = 2*T/n
    sh = (np.pi/2)*np.sinh(tau)
    x = 0.5*(1 + np.tanh(sh))                     # in (0,1)
    w = 0.5*(np.pi/2)*np.cosh(tau)/np.cosh(sh)**2*ht
    return x, w

# 5-point even interpolation: F(j h) = sum_m c_m (j h)^(2m), j = 0..4  -> c_1
J = np.arange(5.0); VAND = np.array([[j**(2*m) for m in range(5)] for j in J])
ROW1 = np.linalg.inv(VAND)[1]                     # c_1 h^2 = ROW1 . F(j h)

def F2_points(W, k, dirs, kind, rel=0.02):
    """returns dict (dir,pol) -> F2 at points k."""
    om0, V0 = W.bands(k)
    xabs = np.abs(np.sin(om0[:, 0]))              # |x| = sqrt(1-f^2)
    h = rel*np.minimum(1.0, xabs)
    out = {}
    H0 = np.einsum('nij,nj,nkj->nik', V0, om0, np.conj(V0))
    if kind in ('M1',):
        P = np.stack([-np.real(np.einsum('nij,ji->n', H0, rw.T3S[j]))/4 for j in range(3)], 1)
    for qn in dirs:
        qh, _ = eps_author(qn, 'A')
        bands = []
        for j in range(1, 5):
            d = (j*h)[:, None]*qh[None, :]
            bands.append((W.bands(k + d), W.bands(k - d)))
        for pol in 'AB':
            _, eps = eps_author(qn, pol)
            if kind == 'M1':
                w = P @ eps.T
                Vm = 0.5*sum(w[:, b, None, None]*rw.T3S[b] for b in range(3))
            else:   # 'L1' lapse: vertex = H at the midpoint
                Vm = H0
            Fv = [rw.bubble(W, Vm, k, k, (om0, V0), (om0, V0))]
            for (ba, bb) in bands:
                Fv.append(rw.bubble(W, Vm, None, None, ba, bb))
            Fv = np.array(Fv)
            out[(qn, pol)] = (ROW1 @ Fv)/h**2, Fv[0]
    return out

def run(walkname, n, theta=0.0, hang=np.pi/2, kind='M1', dirs=('z', 'f', 'd', 'w'), T=3.0, Fh=None):
    res = json.load(open(OUT)) if os.path.exists(OUT) else {}
    b = {'bstar': rw.bstar(), 'iso': rw.B_ISO, 'gold': rw.B_GOLD}[walkname]
    W = rw.Walk(b, theta=theta, hhat=(np.cos(hang), np.sin(hang)))
    if Fh is not None:
        W.Fh = np.asarray(Fh)
    x, w = ts_nodes(n, T)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij'); WW = (w[:, None, None]*w[None, :, None]*w[None, None, :]).ravel()
    base = np.stack([X.ravel(), Y.ravel(), Z.ravel()], 1)*np.pi
    for oc in itertools.product((1, -1), repeat=3):
        key = f"{walkname}|th={theta}|hang={hang:.4f}|{kind}|n={n}|T={T}|Fh={'own' if Fh is None else 'author'}|oct={oc}"
        if key in res:
            continue
        t0 = time.time()
        k_all = base*np.array(oc)[None, :]
        acc = {}; acc0 = {}
        for i in range(0, len(k_all), 20000):
            kk = k_all[i:i+20000]; ww = WW[i:i+20000]*np.pi**3
            o = F2_points(W, kk, dirs, kind)
            for key2, (f2, f0) in o.items():
                acc[f"{key2[0]}{key2[1]}"] = acc.get(f"{key2[0]}{key2[1]}", 0.0) + float(np.sum(ww*f2))
                acc0[f"{key2[0]}{key2[1]}"] = acc0.get(f"{key2[0]}{key2[1]}", 0.0) + float(np.sum(ww*f0))
        res[key] = dict(I2=acc, I0=acc0, s=W.s, sec=time.time() - t0)
        json.dump(res, open(OUT, 'w'), indent=0)
        print(key, f"{time.time()-t0:.0f}s", flush=True)
    tot = {}
    for oc in itertools.product((1, -1), repeat=3):
        key = f"{walkname}|th={theta}|hang={hang:.4f}|{kind}|n={n}|T={T}|Fh={'own' if Fh is None else 'author'}|oct={oc}"
        for c, v in res[key]['I2'].items():
            tot[c] = tot.get(c, 0.0) + v
    cG = {c: 2*(-0.25*v/(2*np.pi)**3)/W.s for c, v in tot.items()}
    return cG

if __name__ == '__main__':
    wn = sys.argv[1]; n = int(sys.argv[2])
    th = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
    hang = float(sys.argv[4]) if len(sys.argv) > 4 else np.pi/2
    kind = sys.argv[5] if len(sys.argv) > 5 else 'M1'
    cG = run(wn, n, th, hang, kind)
    print(wn, n, th, kind, {c: f"{v:.9e}" for c, v in sorted(cG.items())})
