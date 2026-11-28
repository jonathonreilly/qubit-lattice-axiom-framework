#!/usr/bin/env python3
"""VERIFY: the positive-control fields recomputed by the attempt's pure-Python map at L = 5, and the best rule fields at L = 3, 5, and the exact maximum over all search records."""
import importlib.util, json, pathlib
import numpy as np, torch
import fi_map as fm
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("old", HERE.parent / "hard-core--independent_field_ineq.py")
old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)
def oldf(U, L):
    o = (L - 1) // 2
    def get(s, mu):
        idx = list(c + o for c in s); t = U[mu]
        if any(i < 0 or i >= t.shape[k] for k, i in enumerate(idx)):
            return old.ONE
        return tuple(float(c) for c in t[tuple(idx)])
    return old.Field(get)
for fn, L, eps, sr, base in (("best_PC_L5_sparse.npz", 5, 0.02 / 25, 0.02, "fixed"), ("best_R1_L3.npz", 3, 0.02 / 9, 0.02, "rule"), ("best_R1_L5.npz", 5, 0.02 / 25, 0.02, "rule")):
    d = np.load(HERE / fn); U = [torch.from_numpy(d[f"U{i}"]) for i in range(4)]
    U = [u / u.norm(dim=-1, keepdim=True) for u in U]
    e = fm.evaluate(U, L, eps, sr, base)
    old.EPS_RULE = eps; old.S_RULE = sr
    w, m = old.plaquette_W(oldf(U, L), L, base)
    print(fn, base, "new w1", round(e["w1"], 10), "old w1", round(w, 10), "ratio_c", round(e["ratio_c"], 6), "min|m|", e["min_m"], "old m", m)
rows = [json.loads(l) for fn in ("runs.jsonl", "runs2.jsonl") for l in open(HERE / fn)]
for reg in ("R1", "R2", "PC"):
    v = [r for r in rows if r["regime"] == reg]
    print(reg, "runs", len(v), "max Ratio_C", max(r["ratio_c"] for r in v), "by L", {L: round(max(r["ratio_c"] for r in v if r["L"] == L), 6) for L in sorted({r["L"] for r in v})})
