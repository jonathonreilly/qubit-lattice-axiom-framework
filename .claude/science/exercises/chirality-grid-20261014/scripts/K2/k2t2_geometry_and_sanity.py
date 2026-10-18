"""K2-T2 (pre-registered in ../PREREG.md): free min|H_W| in X3's open-time geometry vs alternatives; plus sanity checks
of the K2 lattice code (hermiticity, gauge invariance, Wilson gauge-fixed RP calibration, kernel symmetry)."""
import numpy as np, sys
from lat2d import *
np.set_printoptions(precision=4)
M = 1.0
def free_gap(geom):
    T, Lx = geom.T, geom.Lx
    u0 = {'x': np.zeros((T, Lx)), 't': np.zeros((T - 1, Lx))}
    nc = Lx * (2 if geom.torus else 1)
    D = geom.full_D(u0, u0, np.zeros(nc))
    H = geom.g5d[:, None] * (D - M * np.eye(geom.N))
    assert np.abs(H - H.conj().T).max() < 1e-13
    w = np.linalg.eigvalsh(H); return np.abs(w).min()
print("== K2-T2: free min|eig H_W| (M = 1) ==")
for (Lx, T, torus, xbc, label) in [(4, 4, False, +1, "X3 geometry: Lx=4 PERIODIC x, open t in -3..4"),
                                    (4, 4, False, -1, "Lx=4 ANTIPERIODIC x, open t (K2 G2)"),
                                    (2, 4, False, +1, "Lx=2 periodic x, open t"),
                                    (2, 4, False, -1, "Lx=2 antiperiodic x, open t (K2 G1)"),
                                    (2, 6, False, -1, "Lx=2 antiperiodic x, open t in -5..6 (K2 G1')"),
                                    (8, 4, False, +1, "Lx=8 periodic x, open t"),
                                    (2, 4, True, +1, "torus Lx=2 periodic x, antiperiodic t (K2 G3)"),
                                    (4, 4, True, +1, "torus Lx=4 periodic x, antiperiodic t"),
                                    (8, 4, True, +1, "torus Lx=8 periodic x (X3 T-X3b/c geometry)")]:
    g = Geom(Lx, T, torus, xbc); print(f"  {label:60s} min|H_W| = {free_gap(g):.3e}")
# edge-mode localisation in X3 geometry
g = Geom(4, 4, False, +1); u0 = {'x': np.zeros((4, 4)), 't': np.zeros((3, 4))}
D = g.full_D(u0, u0, np.zeros(4)); H = g.g5d[:, None] * (D - M * np.eye(g.N)); w, V = np.linalg.eigh(H)
i0 = np.argsort(np.abs(w))[:2]
for i in i0:
    prob = np.abs(V[:, i]) ** 2; pt = prob.reshape(g.Lt, g.Lx, 2).sum(axis=(1, 2))
    print(f"  X3-geometry near-zero mode E = {w[i]:+.2e}; weight per time slice t=-3..4: {np.round(pt, 3)}")
# with a small boundary Wilson line the edge mode moves only by ~sin(W/Lx)
for W in [0.01, 0.05, 0.2]:
    ux = np.zeros((4, 4)); ux[3, :] = W / 4
    ua = {'x': ux, 't': np.zeros((3, 4))}
    D = g.full_D(ua, u0, np.zeros(4)); H = g.g5d[:, None] * (D - M * np.eye(g.N))
    print(f"  X3 geometry, Wilson line {W} on the t=4 slice only (all plaquettes in the bulk ~0): min|H_W| = {np.abs(np.linalg.eigvalsh(H)).min():.3e}")
sys.stdout.flush()

print("== sanity ==")
rng = np.random.default_rng(7)
for (Lx, T, torus, xbc) in [(2, 4, False, -1), (4, 4, False, -1), (2, 4, True, 1)]:
    g = Geom(Lx, T, torus, xbc); nc = Lx * (2 if torus else 1)
    ua = rand_half(rng, g, 0.12, 0.3); ub = rand_half(rng, g, 0.12, 0.3); ph = rng.normal(0, 0.1, nc)
    Fs, Bs = g.crossing_mats(); D0 = g.D0(ua, ub)
    l1, gp = logdet_batch(g, D0, Fs, Bs, ph[None], 'O')
    # constant gauge transformation on Lambda+: plane A phases -alpha, plane B phases +alpha
    alpha = 0.7; ph2 = ph.copy(); ph2[:Lx] -= alpha
    if torus: ph2[Lx:] += alpha
    l2, _ = logdet_batch(g, D0, Fs, Bs, ph2[None], 'O')
    lw1, _ = logdet_batch(g, D0, Fs, Bs, ph[None], 'W'); lw2, _ = logdet_batch(g, D0, Fs, Bs, ph2[None], 'W')
    # local gauge transformation at one Lambda+ boundary site (x=0,t=1): crossing phi_0 -> phi_0 - b, spatial links at t=1 touching x=0
    b = 0.4; ua3 = {'x': ua['x'].copy(), 't': ua['t'].copy()}; ph3 = ph.copy(); ph3[0] -= b
    ua3['x'][0, 0] += b; ua3['x'][0, Lx - 1] -= b; ua3['t'][0, 0] += b
    l3, _ = logdet_batch(g, g.D0(ua3, ub), Fs, Bs, ph3[None], 'O')
    print(f"  Lx={Lx} T={T} torus={torus}: logdet overlap {l1[0]:.10f}; const-gauge shift diff {abs(l1[0]-l2[0]):.1e};"
          f" local gauge diff {abs(l1[0]-l3[0]):.1e}; Wilson diff {abs(lw1[0]-lw2[0]):.1e}; min|H_W| {gp[0]:.3f}")
# Wilson gauge-fixed (crossing links = 1) kernel must be PSD (Osterwalder-Seiler) -> calibrates theta conventions
for (Lx, T, torus, xbc) in [(2, 4, False, -1), (4, 4, False, -1), (2, 4, True, 1), (4, 4, False, 1)]:
    g = Geom(Lx, T, torus, xbc); nc = Lx * (2 if torus else 1); Fs, Bs = g.crossing_mats()
    worstW = 1; worstO = 1
    for rep in range(4):
        U = [rand_half(rng, g, 0.3, 1.5) for _ in range(8)]
        for op in ['W', 'O']:
            L = np.zeros((8, 8), complex)
            for a in range(8):
                for bb in range(8):
                    L[a, bb] = logdet_batch(g, g.D0(U[a], U[bb]), Fs, Bs, np.zeros((1, nc)), op)[0][0]
            Z = np.exp(L - 0.5 * (L.diagonal()[:, None] + L.diagonal()[None, :]))
            r = mineig(Z); herm = np.abs(Z - Z.conj().T).max()
            if op == 'W': worstW = min(worstW, r)
            else: worstO = min(worstO, r)
    print(f"  gauge-FIXED kernel Lx={Lx} T={T} torus={torus} xbc={xbc}: Wilson min/max {worstW:+.2e} | overlap min/max {worstO:+.2e} (herm last {herm:.1e})")
print("done")
