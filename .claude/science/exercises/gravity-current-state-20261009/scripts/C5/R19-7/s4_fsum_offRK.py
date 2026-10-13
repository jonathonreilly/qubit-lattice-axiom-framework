"""R19-7 s4: Lemma B check. Off the RK point, f(k) = (1/2)<[O^dag,[H,O]]> = (t/2) sum_m sum_C psi(C) psi(C xor p_m) |O(C xor p_m) - O(C)|^2
(psi = positive ground state of the stoquastic H(v,bU)). Compare with sum_n (E_n - E_0)|<n|O|0>|^2 from dense ED.
Also report f0 (k = 0) for TT2 and TT1 (positivity) and the Perron-Frobenius sign check (min psi > 0)."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from ed import *
for h in [(2, 2, 2, 0, 0, 0)]:   # identity check; dense ED only (tilted tori exceed the dense limit)
    mod = Model(Torus(*h)); idx = np.arange(mod.N)
    print("torus", h, "N", mod.N)
    for bU in [1.0, 2.0, 3.0]:
        for v in [-1.0, 0.0, 0.5, 1.0, 2.0, 4.0]:
            E0, g, w, dense = ground(mod, v, bU); W, U = dense
            out = []
            for kv in [np.array([0, 0, 0.0]), np.array([0, 0, 2*np.pi/mod.T.h[2]])]:
                pols = channel_pols(np.array([0, 0, 1.0]))
                for nm, eps in [("TT1", pols["TT"][0]), ("TT2", pols["TT"][1])]:
                    O = mod.Ovec(kv, eps)
                    fform = 0.0
                    for m in mod.masks:
                        fform += (g*g[idx ^ m]*np.abs(O[idx ^ m] - O)**2).sum()
                    fform *= 0.5   # (t/2) sum_m sum_C, t = 1
                    amp = U.T @ (O*g); fsp = ((W - E0)*np.abs(amp)**2).sum()
                    out.append("%s k=%.2f f_formula=%.6f f_spectral=%.6f" % (nm, kv[2], fform, fsp))
            print("  bU=%.0f v=%5.2f min psi=%.2e | %s" % (bU, v, g.min(), " | ".join(out)))
