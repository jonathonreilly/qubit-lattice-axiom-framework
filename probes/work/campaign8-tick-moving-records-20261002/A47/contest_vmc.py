"""A47 contest_vmc: the U(1)-parton energy contest specified by A45 section 6 (supplied toys; nothing adopted).
Dual (pi-flux) frame of A44: H' = sum_NN s.s + j sum_fd s.s  <=>  original soldered-covariant rule
(J1, K1) = (-1, 2) plus j sum_fd (2 s^c s^c - s.s).  Per NN bond: E(j) = e_J' + 2 j c2 (3N NN bonds, 6N face
diagonals), e_J' = NN <s.s>, c2 = face-diagonal <s.s>, both in the dual frame.
States (A46 a46lib.mf_dual, soldered-frame hops then Klein-rotated):
  lp:<x>   projected U(1) parton: NN i lam s^a (lam = 1) + face-diagonal i x s.d/|d|  (A45 f2 form)
  neel:<m> / col:<m>  pi-flux + Neel / collinear (pi,pi,0) staggered field m (weakly ordered projected states)
Usage: contest_vmc.py L NSWEEP spec1,spec2,...   (per-sweep samples saved: [e_J', c2])"""
import sys, signal, numpy as np
signal.alarm(290)
sys.path.insert(0, __file__.rsplit('/', 2)[0] + "/A46")
from a46lib import *
L, nsw = sys.argv[1], int(sys.argv[2]); specs = sys.argv[3].split(",")
cl = Cluster([[2, 2, 0], [2, 0, 2], [0, 2, 2]]) if L == "fcc16" else cube(int(L))
pi_ = np.repeat(np.arange(cl.N), 6)
pj_ = np.array([cl.idx[tuple(cl.canon(np.array(x) + np.array(d))[0])] for x in cl.sites for d in FD])
budget = 270. / len(specs)
print(f"L={L}: N={cl.N}; specs {specs}; budget/state {budget:.0f}s", flush=True)
for sp_ in specs:
    kind, val = sp_.split(":"); val = float(val)
    if kind == "lp":
        Phi, gap = mf_dual(cl, 0., 1., lam2=val); conserve = (val == 0.)
    else:
        Phi, gap = mf_dual(cl, 0., 1., m=val, pattern=("neel" if kind == "neel" else "collinear")); conserve = True
    if gap < 1e-8:
        print(f"{sp_}: open shell (gap {gap:.1e}), skipped", flush=True); continue
    S, info = vmc_dual(cl, Phi, nsw, max(40, nsw // 10), 4900 + int(1000 * val) + len(kind), budget * 0.9, plaq=None, conserve=conserve, pairs2=(pi_, pj_))
    T = np.c_[S[:, 0].real, S[:, 4].real]
    mJ, eJ = binerr(T[:, 0]); mc, ec = binerr(T[:, 1]); E3, e3 = binerr(T[:, 0] + 0.6 * T[:, 1])
    n = len(T)
    print(f"{sp_}: MF gap {gap:.3f}; sweeps {n} in {info['secs']:.0f}s; acc flip {info['acc'][0]}/{info['acc'][1]} pair {info['acc'][2]}/{info['acc'][3]}; drift {info['drift']:.1e}", flush=True)
    print(f"   e_J' = {mJ:+.5f} +- {eJ:.5f}; c2 = {mc:+.5f} +- {ec:.5f}; E(j=0.3) = {E3:+.5f} +- {e3:.5f} (halves {np.mean(T[:n//2, 0] + 0.6*T[:n//2, 1]):+.4f}/{np.mean(T[n//2:, 0] + 0.6*T[n//2:, 1]):+.4f})", flush=True)
    np.save(f"c_{L}_{kind}{val}.npy", T)
