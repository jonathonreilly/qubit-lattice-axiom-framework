"""K2 (kill agent, F1a): the Delaunay version of F1a is not analytic in the strain, configuration by configuration.

Model = R1 check B, 2D liquid arm exactly: Poisson points (fixed N, periodic square), P1/cotan stiffness K
on the Delaunay complex of the strained points (= Delaunay in metric g), unit site masses,
E = 1/2 sum sqrt(lambda(K)).  Strain M = exp(t S), S = diag(1,-1)/sqrt(2) (tr S^2 = 1).
'glass' arm: same points, complex frozen at t = 0, weights recomputed from strained geometry.

Claims tested (pre-stated):
 (a) between flips E_liq(t) = E_glass(t) exactly (same complex), so the per-configuration Hessian at t = 0
     (infinitesimal amplitude, a.s. no flip at 0) is the GLASS Hessian, whose ensemble mean is >0 (R1: ~+1.7 e0).
     PASS if mean d2E/dt2 at t=0 (step 1e-6, flip-free windows) is > 5 SE above 0.
 (b) flips occur at a rate ~ N per unit strain, and each flip is a concave kink (Rippa): E_liq <= E_glass.
 (c) the random part of E_liq(t) - E_liq(0) - t E'(0) grows like t^(3/2) at small t (flip shot noise),
     not t^2 (a smooth random stiffness).  Reported: fitted exponent of sd vs t over the flip-rich range.
 (d) first-order TT stress dE/dt at t=0: sd * sqrt(N) at N = 400, 900, 1600 (white if constant).
"""
import numpy as np, sys, time
from scipy.spatial import Delaunay
from itertools import product
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 7)

def periodic_delaunay(Y, A):
    N, d = Y.shape
    shifts = np.array(list(product((-1, 0, 1), repeat=d)))
    P = np.concatenate([Y + s @ A for s in shifts])
    idx = np.tile(np.arange(N), len(shifts)); off = np.repeat(shifts, N, axis=0)
    tri = Delaunay(P, qhull_options="Qbb Qc Qz").simplices
    cen = P[tri].mean(axis=1); frac = cen @ np.linalg.inv(A)
    keep = np.all((frac >= 0) & (frac < 1), axis=1); tri = tri[keep]
    return idx[tri], off[tri]

def edgeset(vid, voff):
    s = set()
    for t in range(len(vid)):
        for a, b in ((0, 1), (1, 2), (0, 2)):
            i, j = int(vid[t, a]), int(vid[t, b]); o = tuple(int(x) for x in (voff[t, b] - voff[t, a]))
            mo = tuple(-x for x in o)
            if i > j or (i == j and o < mo):
                i, j, o = j, i, mo
            s.add((i, j, o))
    return s

def stiffness(Y, A, vid, voff):
    N, d = Y.shape
    pos = Y[vid] + np.einsum("tvk,kl->tvl", voff, A)
    D = pos[:, 1:, :] - pos[:, :1, :]
    vol = np.abs(np.linalg.det(D)) / 2
    Dinv = np.linalg.inv(D)
    G = np.concatenate([-Dinv.sum(axis=2, keepdims=True), Dinv], axis=2)
    Kloc = vol[:, None, None] * np.einsum("tka,tkb->tab", G, G)
    K = np.zeros((N, N))
    for a in range(3):
        for b in range(3):
            np.add.at(K, (vid[:, a], vid[:, b]), Kloc[:, a, b])
    return K

def E_vac(K):
    return 0.5*np.sqrt(np.clip(np.linalg.eigvalsh(K), 0, None)).sum()

S = np.diag([1.0, -1.0])/np.sqrt(2)
def expm2(t): return np.diag(np.exp(t*np.diag(S)))

def energies(X, A0, t, frozen):
    M = expm2(t); Y, A = X @ M.T, A0 @ M.T
    v, o = periodic_delaunay(Y, A)
    El = E_vac(stiffness(Y, A, v, o))
    Eg = E_vac(stiffness(Y, A, *frozen))
    return El, Eg, (v, o)

if __name__ == '__main__':
    mode = sys.argv[2] if len(sys.argv) > 2 else 'all'
    if mode in ('all', 'abc'):
        N = 400; L = np.sqrt(N); A0 = L*np.eye(2); nconf = 40
        ts = np.concatenate([[0.0], np.geomspace(2e-4, 0.04, 16)])
        R_l, R_g, H0, NF, E0s = [], [], [], [], []
        t0 = time.time()
        for c in range(nconf):
            X = rng.uniform(0, L, (N, 2)); fr = periodic_delaunay(X, A0); es0 = edgeset(*fr)
            h = 1e-4   # K2b: 1e-6 is roundoff-dominated (spread ~ 1/h^2); 1e-4 is clean
            Ep, Egp, frp = energies(X, A0, h, fr); Em, Egm, frm = energies(X, A0, -h, fr); E0 = E_vac(stiffness(X, A0, *fr))
            d1 = (Egp - Egm)/(2*h); E0s.append(E0/N)
            if edgeset(*frp) == es0 and edgeset(*frm) == es0: H0.append((Ep + Em - 2*E0)/h**2/N)
            rl, rg, nf = [], [], []
            for t in ts[1:]:
                El, Eg, frt = energies(X, A0, t, fr)
                rl.append((El - E0 - d1*t)/N); rg.append((Eg - E0 - d1*t)/N)
                nf.append(len(es0 - edgeset(*frt)))
            R_l.append(rl); R_g.append(rg); NF.append(nf)
        R_l, R_g, NF, H0 = map(np.array, (R_l, R_g, NF, H0)); e0 = np.mean(E0s)
        print(f"2D N={N} nconf={nconf} e0/site={e0:.4f}  [{time.time()-t0:.0f}s]")
        print(f"(a) per-config Hessian at t=0 (flip-free windows only, n={len(H0)} of {nconf}, step 1e-4): mean {H0.mean():+.4f} +- {H0.std(ddof=1)/np.sqrt(len(H0)):.4f}"
              f"  (/e0 = {H0.mean()/e0:+.3f}); sd {H0.std(ddof=1):.4f}, sd*sqrtN {H0.std(ddof=1)*np.sqrt(N):.3f}")
        print("(b,c)  t        flips/N/t   <E_liq-E_glass>/N   mean R_liq/t^2      sd R_liq          sd R_glass        sd R_liq / t^1.5   sd R_liq / t^2")
        for k, t in enumerate(ts[1:]):
            dl = R_l[:, k] - R_g[:, k]
            print(f"     {t:.2e}  {NF[:, k].mean()/N/t:8.3f}   {dl.mean():+.3e} (max {dl.max():+.1e})   {R_l[:, k].mean()/t**2:+8.4f}   {R_l[:, k].std(ddof=1):.3e}   {R_g[:, k].std(ddof=1):.3e}   {R_l[:, k].std(ddof=1)/t**1.5:.3e}   {R_l[:, k].std(ddof=1)/t**2:.3e}")
        # exponent fit of sd R_liq over the flip-rich window (mean flips per config >= 3)
        sel = NF.mean(0) >= 3
        if sel.sum() >= 3:
            p = np.polyfit(np.log(ts[1:][sel]), np.log(R_l.std(0, ddof=1)[sel]), 1)[0]
            pg = np.polyfit(np.log(ts[1:][sel]), np.log(R_g.std(0, ddof=1)[sel]), 1)[0]
            print(f"(c) exponent of sd[R_liq] vs t where >=3 flips/config: {p:.3f}   (glass arm, smooth: {pg:.3f}; t^1.5 = flip shot noise, t^2 = smooth)")
    if mode in ('all', 'd'):
        for N, nconf in [(400, 60), (900, 40), (1600, 24)]:
            L = np.sqrt(N); A0 = L*np.eye(2); d1s = []; t0 = time.time()
            for c in range(nconf):
                X = rng.uniform(0, L, (N, 2)); fr = periodic_delaunay(X, A0); h = 1e-5
                _, Ep, _ = energies(X, A0, h, fr); _, Em, _ = energies(X, A0, -h, fr)   # glass branch: smooth, = liquid between flips
                d1s.append((Ep - Em)/(2*h)/N)
            d1s = np.array(d1s); sd = d1s.std(ddof=1)
            print(f"(d) N={N}: TT stress per site mean {d1s.mean():+.4f} sd {sd:.4f}  sd*sqrtN {sd*np.sqrt(N):.3f} +- {sd*np.sqrt(N)/np.sqrt(2*(nconf-1)):.3f}  [{time.time()-t0:.0f}s]", flush=True)
