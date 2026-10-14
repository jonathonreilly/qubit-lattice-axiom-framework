"""NT-3 secondary / follow-up runs (PREREG.md S1, S2 and dated follow-up A1: D1, D2).
usage: python3 run_secondary.py D1|S1|S2 <Ls comma> <filters comma> [W list comma]"""
import sys, json
import numpy as np
from ed_core import Model, ring, lowest
from analyze import analyze, summarize, chain
from filters import ring_fvals

mode = sys.argv[1]
Ls = [int(x) for x in sys.argv[2].split(",")]
names = sys.argv[3].split(",")
Ws = [float(x) for x in sys.argv[4].split(",")] if len(sys.argv) > 4 else [1.0]
out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s)

for name in names:
    for L in Ls:
        fv = ring_fvals(name, L)
        fnear = fv[1]
        if mode == "D1":
            G = ring(L); G.light = {0, 1, L - 1}
            m = Model(G, fv, include_light=False)
            P(f"# D1 {name} L={L}: near-light f = {fnear:.6f} set to 0 (dropped); kept f = {np.round(m.f, 6).tolist()}")
            r = analyze(m, near_light=()); r["Vs"] = L
            summarize(r, f"D1 {name} L={L}", P)
        elif mode == "S1":
            for v in Ws:
                m = Model(ring(L), fv)
                r = analyze(m, v=v, near_light=(1, L - 1)); r["Vs"] = L
                summarize(r, f"S1 {name} L={L} v={v}", P)
        elif mode == "S2":
            for W in Ws:
                kin = {k: float(np.sin(2 * np.pi * k / L)) for k in range(L)}
                m = Model(ring(L), fv, kin=kin)
                eK = []
                for K in range(L):
                    b = chain(m, (0, 0, 0, 0), K)
                    e, _ = lowest(m.build_H(b, W=W), k=1)
                    eK.append(e[0])
                Kgs = int(np.argmin(eK))
                P(f"# S2 {name} L={L} W={W}: weight-0 lowest per K = {np.round(eK, 6).tolist()} -> Kgs = {Kgs}")
                r = analyze(m, W=W, near_light=(1, L - 1), Kgs=Kgs); r["Vs"] = L
                summarize(r, f"S2 {name} L={L} W={W}", P)
        P(f"   D2: f_near = {fnear:.6f}, f_near^2 = {fnear**2:.6f}, f_near^4 = {fnear**4:.6f}, "
          f"gap/f_near^2 = {r['gap']/fnear**2:.4f}, gap/f_near^4 = {r['gap']/fnear**4:.4f}")
open(f"secondary_{mode}_{'_'.join(sys.argv[2:]).replace(',', '-')}.out", "w").write("\n".join(out) + "\n")
