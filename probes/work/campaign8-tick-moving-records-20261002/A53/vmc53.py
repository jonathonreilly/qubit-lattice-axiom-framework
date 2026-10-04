"""A53 vmc53: projected pi-flux parton with block-modulated hopping (bonds crossing the boundaries of a block tiling
scaled by delta; delta = 1 is A51's parton, delta = 0 the projected product of block partons).  VMC with A51's sampler
and estimators (all dual class sums + A49 four-spin terms); energies under A51's B4_inner and B4_r4 rules of the same L.
Usage: vmc53.py L BLOCK DELTA NSWEEP SEED     (BLOCK e.g. 222 cube, 221 plaquette, 211 dimer)"""
import sys, signal, time, numpy as np
signal.alarm(288)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a53lib import *
from a51lib import _parton_h
t0 = time.time()
L, blk, delta, nsw, seed = int(sys.argv[1]), sys.argv[2], float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
B = [int(c) for c in blk]
cl = cube(L); N = cl.N
ks, K, m = class_matrix(cl, L); ncls = len(ks)
F4b, G4 = four_ops()
T4 = Tables(cl, [(nm, c, "4", d4) for nm, c, d4, so in F4b])
h = _parton_h(cl); nmod = 0
for (i, j, a, n) in cl.bonds:
    if cl.sites[i][a] % B[a] == B[a] - 1:
        h[2 * i:2 * i + 2, 2 * j:2 * j + 2] *= delta; h[2 * j:2 * j + 2, 2 * i:2 * i + 2] *= delta; nmod += 1
ev, W = np.linalg.eigh(h); Phi = W[:, :N].copy(); gap = ev[N] - ev[N - 1]
print(f"L={L} block {blk} delta {delta}: {nmod} of {len(cl.bonds)} bonds scaled; MF gap {gap:.4f}  [{time.time()-t0:.1f}s]", flush=True)
S, info = vmc51(cl, Phi, K.ravel(), ncls, T4, nsw, max(30, nsw // 20), seed, 266 - (time.time() - t0), "singlet", True)
np.save(f"s53_{L}_{blk}_{delta}_{seed}.npy", S)
print(f"measured {len(S)} in {info['secs']:.0f}s; acc pair {info['acc'][2]}/{info['acc'][3]}; drift {info['drift']:.1e}", flush=True)
cas = S[:, :ncls].sum(1); print(f"Casimir estimator max |dev| {np.abs(cas + 1.5 * N).max():.1e}")
R = np.load(f"{D53}/../A51/rules51_{L}.npz")
for key in ("B4_inner", "B4_r4"):
    v = R[key]; e = (S.real @ v) / N; mu, err = binerr(e)
    print(f"  E/N under {key}: {mu:+.5f} +- {err:.5f}")
e = S.real.mean(0) / N
print("  <O_c>/N first 4 classes: " + " ".join(f"{k}:{x:+.4f}" for k, x in zip(ks[:4], e[:4])) + "; four-spin: " +
      " ".join(f"{o[0]}:{x:+.4f}" for o, x in zip(F4b[:8], e[ncls:ncls + 8])))
