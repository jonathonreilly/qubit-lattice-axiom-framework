"""A46 vmc_def: SU(2)->U(1) deformations of the soldered ansatz (Q2).  Soldered-frame covariant
same-sublattice hop on face diagonals, t2 + i lam2 s.d/|d|, added to the NN soldered hop (t=0, lam=1);
state transformed to the dual frame (no longer S^z-conserving there: single + pair flips).
Usage: vmc_def.py L NSWEEP spec1,spec2,...   spec = t2:<v> | lam2:<v> | none"""
import sys, signal, numpy as np
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a46lib import *
L, nsw = sys.argv[1], int(sys.argv[2]); specs = sys.argv[3].split(",")
cl = Cluster([[2, 2, 0], [2, 0, 2], [0, 2, 2]]) if L == "fcc16" else cube(int(L)); plaq = plaquettes(cl); budget = 265. / len(specs)
pi_ = np.repeat(np.arange(cl.N), 6)
pj_ = np.array([cl.idx[tuple(cl.canon(np.array(x) + np.array(d))[0])] for x in cl.sites for d in FD])
print(f"L={L}: N={cl.N}; specs {specs}; budget/state {budget:.0f}s", flush=True)
for sp_ in specs:
    t2 = float(sp_.split(":")[1]) if sp_.startswith("t2") else 0.
    l2 = float(sp_.split(":")[1]) if sp_.startswith("lam2") else 0.
    Phi, gap = mf_dual(cl, 0., 1., t2=t2, lam2=l2)
    if gap < 1e-8:
        print(f"{sp_}: open shell, skipped", flush=True); continue
    S, info = vmc_dual(cl, Phi, nsw, max(40, nsw // 10), 4700 + len(sp_), budget * 0.9, plaq=plaq, conserve=(t2 == 0 and l2 == 0), pairs2=(pi_, pj_))
    out = []
    for k, nm in ((0, "e_J'"), (1, "e_K'"), (2, "ring"), (4, "fd s.s")):
        mu, er = binerr(S[:, k].real); out.append(f"{nm} = {mu:+.5f} +- {er:.5f}")
    print(f"{sp_}: MF gap {gap:.3f}; sweeps {len(S)} in {info['secs']:.0f}s; acc flip {info['acc'][0]}/{info['acc'][1]} pair {info['acc'][2]}/{info['acc'][3]}; drift {info['drift']:.1e}")
    print("   " + "; ".join(out), flush=True)
    np.save(f"vmcd2_{L}_{sp_.replace(':', '')}.npy", S)
