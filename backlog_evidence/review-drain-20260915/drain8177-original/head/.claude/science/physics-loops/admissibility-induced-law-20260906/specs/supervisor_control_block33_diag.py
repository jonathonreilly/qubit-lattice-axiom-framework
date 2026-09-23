import sys, os, numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import supervisor_control_block33_restricted_count as rc
from supervisor_control_block33_kind_certs import KEYS, image
p, q, r, c, variant, t = 4165, 1, 2, 2, "none", Fr(99, 1000)
d1, d2, d3 = rc.devs(p, q, r); e1, e2 = d1, max(d2, d3)
xP, xA, eS, yF = Fr(t), e2 / Fr(t) ** c, e1, 1 / Fr(t) ** 3
xf = dict(xP=float(xP), xA=float(xA), eS=float(eS), yF=float(yF))
G = {key: 0.0 for key in KEYS}
for it in range(50000):
    Gn = image(G, xf["xP"], xf["xA"], xf["eS"], xf["yF"], variant)
    diff = max(abs(Gn[k] - G[k]) / max(1e-300, abs(Gn[k])) for k in KEYS)
    G = Gn
    if diff < 1e-13: break
print("iterations", it, "rel diff", diff)
print({f"{e}{k}": f"{v:.6g}" for (e, k), v in G.items()})
im = image(G, xf["xP"], xf["xA"], xf["eS"], xf["yF"], variant, root=True)
print("root R =", im[("R","P")] + im[("R","A")] + im[("R","S")], " eps1*R =", float(e1) * (im[("R","P")] + im[("R","A")] + im[("R","S")]))
# uniform inflation test with exact rationals
for delta in (Fr(1, 10000), Fr(1, 1000), Fr(1, 100), Fr(1, 20), Fr(1, 10), Fr(1, 4), Fr(1, 2), Fr(1)):
    Gq = {k: Fr(v) * (1 + delta) for k, v in G.items()}
    imq = image(Gq, xP, xA, eS, yF, variant)
    ok = all(Gq[k] >= imq[k] for k in KEYS)
    bad = [f"{e}{k}" for (e, k) in KEYS if Gq[(e, k)] < imq[(e, k)]]
    print(f"delta={delta}: super-solution {ok}; violating {bad[:4]}")
