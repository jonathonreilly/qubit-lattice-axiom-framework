"""A51 vmc51: VMC samples of all dual Heisenberg class sums (folded components <= L/2) + A49's 10 four-spin terms.
Usage: vmc51.py L SPEC NSWEEP SEED [EVERY]     (SPEC as in a51lib.state)
Saves s51_<L>_<SPEC>_<SEED>.npy: (n_samples, ncls + 10) complex local estimators (classes unnormalized O_c; four-spin
normalized as in A49)."""
import sys, signal, time, numpy as np
signal.alarm(288)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a51lib import *
L, spec, nsw, seed = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
every = int(sys.argv[5]) if len(sys.argv) > 5 else 1
t0 = time.time()
cl = cube(L); N = cl.N
ks, K, m = class_matrix(cl, L); ncls = len(ks)
F4, G4 = four_ops()
T4 = Tables(cl, [(nm, c, "4", d4) for nm, c, d4, so in F4])
Phi, gap, mode, conserve = state(cl, spec)
print(f"L={L} N={N} {spec}: {ncls} classes, {len(F4)} four-spin ({T4.ns} four-sets); MF gap {gap:.3f}; mode {mode}; setup {time.time()-t0:.1f}s", flush=True)
s0 = np.array([x[0] % 2 for x in cl.sites]) if spec == "vbs" else None
S, info = vmc51(cl, Phi, K.ravel(), ncls, T4, nsw, max(30, nsw // 20), seed, 268 - (time.time() - t0), mode, conserve, every, s0=s0)
np.save(f"s51_{L}_{spec}_{seed}.npy", S)
print(f"measured {len(S)} in {info['secs']:.0f}s; acc flip {info['acc'][0]}/{info['acc'][1]} pair {info['acc'][2]}/{info['acc'][3]}; drift {info['drift']:.1e}", flush=True)
cas = S[:, :ncls].sum(1)
print(f"Casimir estimator: mean {cas.real.mean():.6f}, max |dev from -3N/2| {np.abs(cas + 1.5 * N).max():.2e} (zero iff exact singlet)")
e = S.real.mean(0) / N
print("<O_c>/site (first 8 classes): " + " ".join(f"{k}:{v:+.4f}" for k, v in zip(ks[:8], e[:8])))
print(f"NN s.s per bond {e[0]/3:+.4f}; four-spin: " + " ".join(f"{o[0]}:{v:+.4f}" for o, v in zip(F4, e[ncls:])))
