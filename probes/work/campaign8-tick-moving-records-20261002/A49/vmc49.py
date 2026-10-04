"""A49 vmc49: VMC samples of the local estimators of the 23 basis operators.
Usage: vmc49.py L SPEC NSWEEP SEED [EVERY]
SPEC: lp:0 (projected parton, exact dual singlet; 'singlet' estimators, exchange moves)
      neez:<m> / colz:<m> (weakly ordered projected Neel / collinear, field along dual z; S^z = 0 exactly; only the
                rank-0 block E0 is valid -> used for the dual-SU(2)-invariant subspace only; exchange moves)
      cs (compass-staggered product state, 'full' estimators; single + pair flips)
      pol (soldered-uniform polarized product state along (1,2,3), 'full'; control)
Saves s49_<L>_<SPEC>_<SEED>.npy (packed estimators per measured sweep)."""
import sys, signal, time, numpy as np
signal.alarm(288)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a49lib import *
L, spec, nsw, seed = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
every = int(sys.argv[5]) if len(sys.argv) > 5 else 1
t0 = time.time()
cl = cube(L); N = cl.N
ops = [(nm, cls, "b", op) for nm, cls, op in bilinear_basis()] + [(nm, cls, "4", d4) for nm, cls, d4, sold in four_basis()]
T = Tables(cl, ops)
print(f"L={L} N={N}: {T.np_} pairs, {T.ns} four-sets; tables {time.time()-t0:.1f}s", flush=True)
kind = spec.split(":")[0]
if kind == "lp":
    Phi, gap = mf_state(cl, lam2=float(spec.split(":")[1])); mode, conserve = "singlet", True
elif kind in ("neez", "colz"):
    Phi, gap = mf_state(cl, m=float(spec.split(":")[1]), pattern=("neel" if kind == "neez" else "collinear")); mode, conserve = "singlet", True
elif kind == "cs":
    Phi = product_state([(-1) ** int(sum(x)) * np.ones(3) / np.sqrt(3) for x in cl.sites]); gap = np.nan; mode, conserve = "full", False
elif kind == "pol":
    nh = np.array([1., 2., 3.]) / np.sqrt(14.)
    Phi = product_state([np.array([kR(x, b) * nh[b] for b in range(3)]) for x in cl.sites]); gap = np.nan; mode, conserve = "full", False
print(f"{spec}: MF gap {gap:.3f}; mode {mode}", flush=True)
tl = 270 - (time.time() - t0)
S, br, info = vmc(T, Phi, nsw, max(30, nsw // 20), seed, tl, mode, conserve, every=every)
print(f"measured {len(S)} in {info['secs']:.0f}s; acc flip {info['acc'][0]}/{info['acc'][1]} pair {info['acc'][2]}/{info['acc'][3]}; drift {info['drift']:.1e}", flush=True)
np.save(f"s49_{L}_{spec}_{seed}.npy", S)
n = len(T.names)
E0 = S[:, :n].real.mean(0) / N
print("<h>/site: " + " ".join(f"{nm}:{e:+.3f}" for nm, e in zip(T.names, E0)), flush=True)
