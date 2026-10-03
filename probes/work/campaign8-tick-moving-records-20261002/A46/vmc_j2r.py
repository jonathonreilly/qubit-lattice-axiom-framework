"""A46 vmc_j2r: dual-frame VMC of the pi-flux singlet (m = 0) and the AF family, measuring e_J', ring and the
face-diagonal <s.s> (the dual J2 term; original frame: j sum_fd (2 s^c s^c - s.s), star-local).
Usage: vmc_j2r.py L NSWEEP m1,m2,..."""
import sys, signal, numpy as np
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a46lib import *
L, nsw = int(sys.argv[1]), int(sys.argv[2]); ms = [float(v) for v in sys.argv[3].split(",")]
pat = sys.argv[4] if len(sys.argv) > 4 else "neel"; tag = "" if pat == "neel" else "c"
cl = cube(L); plaq = plaquettes(cl); budget = 265. / len(ms)
pi_ = np.repeat(np.arange(cl.N), 6)
pj_ = np.array([cl.idx[tuple(cl.canon(np.array(x) + np.array(d))[0])] for x in cl.sites for d in FD])
print(f"L={L}: N={cl.N}; field pattern {pat}; m {ms}; budget/state {budget:.0f}s", flush=True)
for m in ms:
    Phi, gap = mf_dual(cl, 0., 1., m=m, pattern=pat)
    S, info = vmc_dual(cl, Phi, nsw, max(40, nsw // 10), 4800 + int(100 * m), budget * 0.9, plaq=plaq, conserve=True, pairs2=(pi_, pj_))
    out = []
    for k, nm in ((0, "e_J'"), (2, "ring"), (4, "fd s.s"), (3, "m_stag")):
        mu, er = binerr(S[:, k].real); out.append(f"{nm} = {mu:+.5f} +- {er:.5f}")
    print(f"m={m}: sweeps {len(S)} in {info['secs']:.0f}s; drift {info['drift']:.1e}; " + "; ".join(out), flush=True)
    np.save(f"vmcj{tag}_{L}_m{m}.npy", S)
