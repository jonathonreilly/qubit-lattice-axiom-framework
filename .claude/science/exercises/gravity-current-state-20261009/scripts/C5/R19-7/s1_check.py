"""R19-7 s1: engine checks at the L=2 cube: (i) v=t reproduces R19-1 s1 gaps and the TT2 main pole at k=(0,0,pi), bU=1;
(ii) H psi0 = 0 at v = t with psi0 ~ exp(-bU E/2); (iii) Lanczos poles agree with dense ED; (iv) bU=0 v-independence."""
import numpy as np, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from ed import *
t0 = time.time()
mod = Model(Torus(2, 2, 2)); print("L=2: d=%d N=%d moves(nonzero)=%d identity moves dropped=%d max|dE|=%g" % (mod.d, mod.N, len(mod.masks), mod.n_identity, mod.maxabsdE))
for bU in [1.0, 2.0]:
    E0, g, w, dense = ground(mod, 1.0, bU)
    psi = np.exp(-bU*mod.E/2); psi /= np.linalg.norm(psi)
    H = dense_H(mod, 1.0, bU)
    print("bU=%g v=t: E0=%.3e |H psi_RK|=%.2e overlap(g,psi_RK)=%.12f gap=%.6f (R19-1: 0.840445 / 0.087565)" % (bU, E0, np.linalg.norm(H @ psi), abs(g @ psi), w[1] - w[0]))
    pols = channel_pols(np.array([0, 0, 1.0]))
    om, wt = spectral(mod, 1.0, bU, np.array([0, 0, np.pi]), pols["TT"][1], E0, g, dense=dense)
    dg = diagnose(om, wt); print("   TT2 k=(0,0,pi): S=%.5f SMA=%.4f main=%.4f  (R19-1 bU=1: S=1.57407 f/S=8.2636 main 8.2159)" % (dg["S"], dg["sma"], dg["main"]))
    om2, wt2 = spectral(mod, 1.0, bU, np.array([0, 0, np.pi]), pols["TT"][1], E0, g, dense=None, M=80)
    dg2 = diagnose(om2, wt2); print("   Lanczos(80): S=%.5f SMA=%.4f main=%.4f low=%.4f vs dense low=%.4f" % (dg2["S"], dg2["sma"], dg2["main"], dg2["low"], dg["low"]))
for v in [0.0, 0.5, 2.0]:
    E0, g, w, dense = ground(mod, v, 0.0)
    print("bU=0 v=%g: spectrum - E0 (first 6) = %s" % (v, np.round(w[:6] - w[0], 6)))
print("time %.1fs" % (time.time() - t0))
