"""Test A (beam): contiguous windows of up to 36 sites, truncated exact Holevo; disjoint-window redundancy."""
import json, sys, time
import numpy as np
import beam_vs_sea as b
from gauss_trunc import holevo_trunc

LENS = [4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32, 36]

def run(L, NB, g, coup, T, sigma, spacing, first, K=4, maxpart=10):
    h = b.chain_h(L); j0 = 110
    Vu, Vd = (g, 0.0) if coup == "proj" else (g, -g)
    Phi0 = b.packets(L, j0, NB, sigma=sigma, spacing=spacing, first=first)
    Pu = b.evolve(h, j0, Vu, Phi0, T); Pd = b.evolve(h, j0, Vd, Phi0, T)
    Du, Dd = b.corr(Pu), b.corr(Pd)
    ov = float(np.prod(np.linalg.svd(Pu.conj().T @ Pd, compute_uv=False)))
    t0 = time.time(); tab = {}; lostmax = 0.0; nex = 0
    for i in range(1, L - 2):
        for m in LENS:
            if i + m > L - 1: break
            a, c = Du[i:i+m, i:i+m], Dd[i:i+m, i:i+m]
            if np.linalg.norm(a - c) < 1e-7: tab[(i, m)] = 0.0; continue
            chi, lost = holevo_trunc(a, c, K=K, maxpart=maxpart)
            if lost > 1e-6:
                nex += 1; continue      # truncation not trustworthy: window excluded (R is then a lower bound)
            tab[(i, m)] = chi
    out = dict(L=L, NB=NB, g=g, coup=coup, T=T, sigma=sigma, spacing=spacing, first=first, overlap=ov,
               excluded_windows=nex, secs=round(time.time() - t0, 1))
    for thr in (0.9, 0.5):
        ch = b.disjoint_count(tab, thr)
        out[f"R{thr}"] = len(ch); out[f"win{thr}"] = [(i - j0, m, round(c, 3)) for i, m, c in ch]
    contact = [v for (i, m), v in tab.items() if i <= j0 < i + m]
    out["max_chi"] = max(tab.values()); out["max_chi_short(<=12)"] = max(v for (i, m), v in tab.items() if m <= 12)
    return out

if __name__ == "__main__":
    NB = int(sys.argv[1]); g = float(sys.argv[2]); coup = sys.argv[3]
    T = float(sys.argv[4]) if len(sys.argv) > 4 else 44.0
    sigma = float(sys.argv[5]) if len(sys.argv) > 5 else 2.0
    o = run(300, NB, g, coup, T, sigma, 12, 8)
    line = json.dumps(o); print(line, flush=True)
    open("results_beam2.jsonl", "a").write(line + "\n")
