"""K2-T3 (pre-registered in ../PREREG.md, Amendment A1): gauge-invariant RP kernel of the gauged Dirac overlap, beta_g = 0
analogue with admissible (Fejer-triangle, primary; hard indicator, secondary) crossing-plaquette weight, all plaquettes admissible.
usage: python3 k2t3_gi_rp.py GEOM delta s nsets weight nlo nhi [nw_lo nw_hi]"""
import numpy as np, sys, time
from lat2d import *
geom_name, delta, s, nsets, weight, nlo, nhi = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5], int(sys.argv[6]), int(sys.argv[7])
nwlo = int(sys.argv[8]) if len(sys.argv) > 8 else None; nwhi = int(sys.argv[9]) if len(sys.argv) > 9 else None
G = {'G1': Geom(2, 4, False, -1), "G1p": Geom(2, 6, False, -1), 'G2': Geom(4, 4, False, -1), 'G3': Geom(2, 4, True, 1), 'G3p': Geom(2, 6, True, 1)}[geom_name]
k = 8
seed = {'G1': 101, 'G1p': 202, 'G2': 303, 'G3': 404, 'G3p': 505}[geom_name] + int(100 * delta)
rng = np.random.default_rng(seed)
print(f"# {geom_name}: Lx={G.Lx} Lt={G.Lt} torus={G.torus} xbc={G.xbc} delta={delta} s={s} weight={weight} n=({nlo},{nhi}) nw=({nwlo},{nwhi}) k={k} seed={seed}")
nc = G.Lx * (2 if G.torus else 1); Fs, Bs = G.crossing_mats()
for rep in range(nsets):
    t0 = time.time()
    U = [rand_half(rng, G, s, delta) for _ in range(k)]
    res = {}
    for op in ['W', 'O']:
        Zl, gl, il = kernel(G, U, delta, nlo, weight, op, nwlo)
        Zh, gh, ih = kernel(G, U, delta, nhi, weight, op, nwhi)
        q = np.abs(Zh - Zl).max()
        res[op] = (mineig(Zl), mineig(Zh), q, min(gl, gh), max(il, ih), int((np.abs(Zh) > 0).sum()), Zh)
    # diagnostic D-GF: gauge-fixed (crossing links = 1) kernel on the same configs
    gf = {}
    for op in ['W', 'O']:
        L = np.zeros((k, k), complex)
        for a in range(k):
            for b in range(k):
                L[a, b] = logdet_batch(G, G.D0(U[a], U[b]), Fs, Bs, np.zeros((1, nc)), op)[0][0]
        gf[op] = mineig(np.exp(L - 0.5 * (L.diagonal()[:, None] + L.diagonal()[None, :])))
    W, O = res['W'], res['O']
    clean = (O[2] < 1e-5) and (O[3] > 0.1) and (W[2] < 1e-5)
    print(f"set {rep}: OVERLAP min/max n_lo {O[0]:+.3e} n_hi {O[1]:+.3e} q {O[2]:.1e} min|H_W| {O[3]:.3f} imag {O[4]:.1e} nonzero {O[5]}/{k*k}"
          f" | WILSON min/max n_lo {W[0]:+.3e} n_hi {W[1]:+.3e} q {W[2]:.1e} | gauge-fixed diag: W {gf['W']:+.2e} O {gf['O']:+.2e}"
          f" | clean {clean} | {time.time()-t0:.0f}s")
    ev = np.linalg.eigvalsh(0.5 * (O[6] + O[6].conj().T)); print(f"   overlap eigenvalues (n_hi): {np.array2string(ev, precision=3)}")
    sys.stdout.flush()
print("done")
