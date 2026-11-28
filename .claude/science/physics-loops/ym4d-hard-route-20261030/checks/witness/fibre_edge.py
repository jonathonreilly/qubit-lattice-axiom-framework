#!/usr/bin/env python3
"""W3 extras: L^4 delta_pp at block-edge plaquettes, the W-measurable test (b), and L = 1 at a fine grid."""
import json, os
import numpy as np
import fibre_split as fs


def run(L, Gg):
    h = (L - 1) // 2
    conf = {"cen": (0, 0, 0, 0), "edge12": (h, h, 0, 0), "edge3": (0, 0, h, 0), "edge123": (h, h, h, h)}
    xs = sorted({c for v in conf.values() for c in v} | {c + 1 for v in conf.values() for c in v})
    T = fs.Tables(L, Gg, xs, max(30, 8 * L))
    M = fs.mats(T)
    S = {k: fs.cross(T, v, 0, 1) for k, v in conf.items()}
    out = {"L": L}
    for k in conf:
        d, _ = fs.delta(T, M, S[k], S[k])
        out[k] = d
        out[k + "_L4"] = d * L**4
    # W-measurable test current: a coarse plaquette, S = conj(J') M
    th = T.theta
    J0 = (1 - np.exp(-1j * L * th)).reshape(1, Gg, 1, 1)
    J1 = (np.exp(-1j * L * th) - 1).reshape(Gg, 1, 1, 1)
    St = np.zeros_like(M, dtype=complex)
    St[0] = np.conj(J0) * M[0]
    St[1] = np.conj(J1) * M[1]
    dt, _ = fs.delta(T, M, St, St)
    var = float(((np.abs(J0) ** 2 * M[0] + np.abs(J1) ** 2 * M[1]).sum() * T.h**4 / (2 * np.pi) ** 4))
    out["test_delta"] = dt
    out["test_var"] = var
    out["test_fibre_rel"] = abs(var - dt) / var
    return out


here = os.path.dirname(os.path.abspath(__file__))
res = []
for L, G in [(3, 8), (9, 8), (15, 8), (21, 8), (33, 8)]:
    r = run(L, G)
    res.append(r)
    print({k: float(f"{v:.6g}") for k, v in r.items()}, flush=True)
with open(os.path.join(here, "fibre_edge.json"), "w") as f:
    json.dump(res, f, indent=1)
