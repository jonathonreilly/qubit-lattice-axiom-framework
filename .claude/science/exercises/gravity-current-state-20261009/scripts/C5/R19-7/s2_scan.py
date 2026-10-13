"""R19-7 s2: v/t x bU scan of H(v,bU) on one torus. For each k (axis k_z = 2 pi m/Lz, plus the cluster's off-axis
points) and channel (TT1, TT2, V1, V2, S w.r.t. khat; at k=0 khat=z is a label only) report S, SMA (first moment),
main pole (lowest pole with >= 10% weight), lowest pole (>= 1e-6 weight), imaginary-time decay rates.
usage: s2_scan.py h1 h2 h3 r p q  vlist  bUlist  M  tag  [channels]"""
import numpy as np, sys, time, pickle
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from ed import *
h = [int(a) for a in sys.argv[1:7]]; vs = [float(a) for a in sys.argv[7].split(',')]; bUs = [float(a) for a in sys.argv[8].split(',')]
M = int(sys.argv[9]); tag = sys.argv[10]; chans = sys.argv[11].split(',') if len(sys.argv) > 11 else ["TT1", "TT2", "V1", "V2", "S1"]
T = Torus(*h); t0 = time.time(); mod = Model(T)
print("torus HNF %s V=%d d=%d N=%d nonzero moves=%d (identity dropped %d) max|dE|=%g build %.1fs" % (h, T.V, mod.d, mod.N, len(mod.masks), mod.n_identity, mod.maxabsdE, time.time() - t0))
Lz = T.h[2]
kpts = [("axis", m, np.array([0, 0, 2*np.pi*m/Lz])) for m in range(0, Lz//2 + 1)]
# off-axis points allowed by the period lattice: k.a_i in 2piZ
A = T.A
for name, kv in [("face", np.array([np.pi, np.pi, 0])), ("body", np.array([np.pi, np.pi, np.pi])), ("face_xz", np.array([np.pi, 0, np.pi]))]:
    if np.allclose(np.mod(kv @ A/(2*np.pi) + 1e-9, 1), 0, atol=1e-6): kpts.append((name, -1, kv))
res = {}
for bU in bUs:
    for v in vs:
        t1 = time.time()
        E0, g, w, dense = ground(mod, v, bU)
        line = "bU=%.2f v=%.3f E0=%.6f gaps(w1..w3-w0)=%s ground amp min/max=%.2e/%.2e" % (bU, v, E0, np.round(np.array(w[1:4]) - w[0], 6), g.min(), g.max())
        print(line)
        for (name, m, kv) in kpts:
            khat = kv/np.linalg.norm(kv) if np.linalg.norm(kv) > 0 else np.array([0, 0, 1.0])
            pols = channel_pols(khat)
            pl = {"TT1": pols["TT"][0], "TT2": pols["TT"][1], "V1": pols["V"][0], "V2": pols["V"][1], "S1": pols["S"][0]}
            row = []
            for ch in chans:
                om, wt = spectral(mod, v, bU, kv, pl[ch], E0, g, dense=dense, M=M)
                dg = diagnose(om, wt); res[(bU, v, name, m, ch)] = dg
                if dg["S"] == 0: row.append("%s: S=0" % ch); continue
                row.append("%s: S=%.4f sma=%.4f main=%.4f low=%.4f r20=%.4f" % (ch, dg["S"], dg["sma"], dg["main"], dg["low"], dg["r20"]))
            print("   %-7s m=%2d k=(%.3f,%.3f,%.3f) | %s" % (name, m, kv[0], kv[1], kv[2], " | ".join(row)))
        res[(bU, v, "E0")] = E0; res[(bU, v, "w")] = np.array(w[:4]); sys.stdout.flush()
        print("   [%.1fs]" % (time.time() - t1))
        pickle.dump(res, open("../data/s2_%s.pkl" % tag, "wb"))
pickle.dump(res, open("../data/s2_%s.pkl" % tag, "wb"))
print("total %.1fs" % (time.time() - t0))
