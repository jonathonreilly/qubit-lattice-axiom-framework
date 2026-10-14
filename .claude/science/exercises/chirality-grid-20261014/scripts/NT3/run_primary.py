"""NT-3 primary runs (PREREG.md): H_Q alone (W = infinity), mirror Fock space.
usage: python3 run_primary.py <tag> <Ls comma> <filters comma> [cube]"""
import sys, json, time
import numpy as np
from ed_core import Model, ring, cube2
from analyze import analyze, summarize
from filters import ring_fvals, cube_fvals

tag = sys.argv[1]
Ls = [int(x) for x in sys.argv[2].split(",")] if sys.argv[2] != "-" else []
names = sys.argv[3].split(",") if sys.argv[3] != "-" else []
do_cube = len(sys.argv) > 4 and sys.argv[4] == "cube"
out = []; summ = {}
def P(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s)

for name in names:
    for L in Ls:
        m = Model(ring(L), ring_fvals(name, L), include_light=(name == "C0"))
        P(f"# {name} L={L}: f on included momenta = {np.round(m.f, 6).tolist()}  quads = {len(m.quads)}")
        r = analyze(m, near_light=(1, L - 1)); r["Vs"] = L
        summarize(r, f"{name} L={L}", P)
        summ[f"{name}|{L}"] = {k: (float(v) if isinstance(v, (float, np.floating, int)) else None)
                               for k, v in r.items() if not isinstance(v, (list, np.ndarray, tuple, dict))}
        summ[f"{name}|{L}"]["gap_nl_row"] = str(r["gap_nl_row"])
if do_cube:
    for name in ("f_NN", "f_F1"):
        G = cube2(); fv = cube_fvals(name)
        m = Model(G, fv, include_light=False)
        P(f"# cube {name}: f at corners (label: bits x,y,z) = { {i: round(fv[i], 6) for i in range(8)} }  quads = {len(m.quads)}")
        r = analyze(m, near_light=()); r["Vs"] = 8
        summarize(r, f"cube {name}", P)
        summ[f"cube|{name}"] = {k: (float(v) if isinstance(v, (float, np.floating, int)) else None)
                                for k, v in r.items() if not isinstance(v, (list, np.ndarray, tuple, dict))}
open(f"primary_{tag}.out", "w").write("\n".join(out) + "\n")
json.dump(summ, open(f"primary_{tag}.json", "w"), indent=1)
