"""QMC-1b L6 queue (PREREG section 5.2). Prints 'filt W seed' of the next L6 run, or 'none'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis_b import load_all, ratio
RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "runs")
res = load_all(RUNS)
order = [("fG", 4.0, 61004), ("f2", 4.0, 62004), ("fG", 2.0, 61002), ("f2", 2.0, 62002)]
for f, W, seed in order:
    r4 = res.get((f, 4, W))
    if r4 is None or not r4["complete"]:
        print(f"# {f} W{W}: L4 missing/incomplete -> skip", file=sys.stderr); continue
    if r4["E3w"] > 0.1:
        print(f"# {f} W{W}: L4 E3w {r4['E3w']:.4f} > 0.1 -> not a window, skip", file=sys.stderr); continue
    if os.path.exists(os.path.join(RUNS, f"L6_{f}_W{W:g}.npz")):
        continue                                       # done or attempted (no reruns)
    if f == "fG" and W == 2.0:
        a4, a6 = res.get(("fG", 4, 4.0)), res.get(("fG", 6, 4.0))
        if a4 and a6 and a6["complete"] and a4["E3w"] <= 0.1 and a6["E3w"] <= 0.1:
            R, Re = ratio(a4, a6)
            if R <= 0.75 and (1 - R) / Re >= 2:
                print("# fG W2 skipped: fG W4 already meets the FILTER-SENSITIVE fG clause", file=sys.stderr); continue
    print(f"{f} {W:g} {seed}"); sys.exit(0)
print("none")
