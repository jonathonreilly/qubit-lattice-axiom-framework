"""B13 production: forward-walking DMC magnetic-source curvatures of the supplied ring model on L^3 tori.

usage: python b13_scan.py L V N nblocks block_t seed
Sources (unit vectors): harmonic q=0 per orientation (3) and the single coexact direction at
q_min = 2 pi / L along each axis (cos and sin parts -> 2 per axis, 6 total).
Initial state: the 2-periodic tiling of the most-flippable 2^3 vacuum-component state (W = 0).
Writes results/L{L}_V{V}_N{N}_s{seed}.json.  Exploratory worker code; no claim.
"""
import os
os.environ.setdefault("NUMBA_NUM_THREADS", "1")
import sys, json, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B6_maxwell_winding"))
sys.path.insert(0, HERE)
import ringlib as R
import pqmclib as Q
import dmclib as D

L, V, N, nblocks, block_t, sd = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6])
t0 = time.time()
lat = Q.Lattice((L, L, L))
T2 = R.Torus((2, 2, 2))
codes = R.sector_states(T2, (0, 0, 0))
inv, sizes, _ = R.split_components(T2, codes)
vc = codes[inv == np.argmax(sizes)]
s2 = T2.sigma_of(int(vc[np.argmax(R.count_moves(vc, T2.plaq))]))
sig = np.zeros(lat.nl, np.int64)
for (x, y, z) in lat.verts:
    for a in range(3):
        sig[lat.link((x, y, z), a)] = s2[T2.link((x % 2, y % 2, z % 2), a)]
assert np.abs(lat.div @ sig).max() == 0 and lat.winding(sig) == (0, 0, 0)
src, labels = [], []
for o in range(3):
    src.append(lat.fourier_dirs((0, 0, 0), o)[0]); labels.append(f"harm_o{o}")
for ax in range(3):
    q = [0.0, 0.0, 0.0]; q[ax] = 2 * np.pi / L
    cd = lat.coexact_dirs(tuple(q))
    assert len(cd) == 2, len(cd)
    for k, v in enumerate(cd):
        src.append(v); labels.append(f"coex_ax{ax}_{k}")
Csrc = np.array(src)
res = D.run(lat, sig, V, N=N, dt=0.1, ntherm_t=max(20.0, block_t), nblocks=nblocks, block_t=block_t, Csrc=Csrc, seed_=sd)
Em = D.binned(res["Emix"])
Eg = D.binned(res["Egrowth"])
ch = D.chi_fit(res)
chi_h = np.mean([c[0] for c in ch[:3]]); chi_h_e = np.sqrt(sum(c[1] ** 2 for c in ch[:3])) / 3
kt = np.mean([c[0] for c in ch[3:]]); kt_e = np.sqrt(sum(c[1] ** 2 for c in ch[3:])) / 6
out = dict(L=L, V=V, N=N, nblocks=nblocks, block_t=block_t, seed=sd, nplaq=lat.np_, Emix=Em, Egrowth=Eg,
           E_per_plaq=(Em[0] / lat.np_, Em[1] / lat.np_), labels=labels, chi=ch, chi_harm=(chi_h, chi_h_e),
           KT_qmin=(kt, kt_e), M2_curve={lab: res["M2"][:, :, s].mean(0)[::10].tolist() for s, lab in enumerate(labels)},
           tau=res["tau"][::10].tolist(), seconds=time.time() - t0)
os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
fn = os.path.join(HERE, "results", f"L{L}_V{V:+.2f}_N{N}_s{sd}.json")
json.dump(out, open(fn, "w"), indent=1, default=float)
print(f"L={L} V={V:+.2f} N={N}: E/plaq={Em[0]/lat.np_:.5f}+-{Em[1]/lat.np_:.5f} chi_harm={chi_h:.4f}+-{chi_h_e:.4f} "
      f"K_T(qmin)={kt:.4f}+-{kt_e:.4f} per-source={[(round(a, 3), round(b, 3)) for a, b in ch]} ({out['seconds']:.0f}s)", flush=True)
