"""PREREG follow-up A2, D3: pair-momentum attribution of the soft 6-sector state (W = infinity, primary model)."""
import numpy as np
from ed_core import Model, ring, lowest
from analyze import chain
from filters import ring_fvals

out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s)

runs = [("F_lo", L) for L in (5, 6, 7)] + [("F_star", L) for L in (5, 6, 7)] + [("F_hi", L) for L in (5, 6, 7)] + [("C1", 6)]
for name, L in runs:
    m = Model(ring(L), ring_fvals(name, L))
    b0 = chain(m, (0, 0, 0, 0), 0); e0, v0 = lowest(m.build_H(b0), k=2); g0 = v0[:, 0]
    b6 = chain(m, (1, 1, 0, 0), 0); e6, v6 = lowest(m.build_H(b6), k=2); s6 = v6[:, 0]
    w = {}
    Pd = np.zeros(len(b6))
    for j, k in enumerate(m.moms):
        j2 = m.jof[m.G.neg[k]]
        # c_2^dag(-k) c_1^dag(k): c_1^dag acts first
        vec = m.apply_op_sum([(1.0, [(True, m.p(0, j)), (True, m.p(1, j2))])], b0, g0, b6)
        w[k] = float((s6 @ vec) ** 2)
        Pd += vec
    tot = sum(w.values())
    nl = (w.get(1, 0) + w.get(L - 1, 0)) / tot if tot > 1e-30 else float("nan")
    ov = float((s6 @ Pd) ** 2 / (Pd @ Pd)) if Pd @ Pd > 0 else float("nan")
    P(f"{name} L={L}: gap6 = {e6[0]-e0[0]:.6f}; pair weights w(k) (k label: weight) = "
      f"{ {k: round(v / tot, 4) for k, v in w.items()} }; near-light share = {nl:.4f}; "
      f"|<6|P_M^dag GS>|^2/||P_M^dag GS||^2 = {ov:.4f}; f = {np.round(m.f, 4).tolist()}")
open(__file__.replace(".py", ".out"), "w").write("\n".join(out) + "\n")
