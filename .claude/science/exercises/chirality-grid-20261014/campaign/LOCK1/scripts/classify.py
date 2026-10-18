"""Apply PREREG's classification to runs/*.jsonl; also the chessboard folding check."""
import json, sys, itertools, collections
import numpy as np

D = sys.argv[1]


def load(t):
    try:
        return [json.loads(l) for l in open(f"{D}/{t}.jsonl")]
    except FileNotFoundError:
        return []


def corner(k, L):
    return all(c in (0, L // 2) for c in k) and any(c for c in k)


def classify(a, b):
    """a: smaller L run, b: larger L run (same g, rho, pqr)."""
    L = b["L"]
    rmax = b["Smax_over_V"] / max(a["Smax_over_V"], 1e-12)
    rmin = b["Smin_over_V"] / max(a["Smin_over_V"], 1e-12)
    kk = sorted(min(c, L - c) for c in b["kmax"])
    smallk = kk == [0, 0, 1]
    if (rmin > 0.7 and b["Smin_over_V"] > 0.01) or (smallk and rmax > 0.7 and b["Smax_over_V"] > 0.002):
        return "clumped(period1)", rmax, rmin
    if rmax > 0.7 and b["Smax_over_V"] > 0.005:
        if corner(b["kmax"], L):
            return ("period-2" if b["U"] > 0.5 else "period-2?"), rmax, rmin
        return f"other@{b['kmax']}", rmax, rmin
    if rmax < 0.5 and b["U"] < 0.3:
        return "liquid", rmax, rmin
    return "boundary", rmax, rmin


def table(runs, Lpair, label):
    idx = {}
    for r in runs:
        key = (tuple(r["pqr"]) if r["pqr"] else None, r["rho"], r["g"], r.get("start", "rand"))
        idx[(key, r["L"])] = r
    keys = sorted({k for (k, L) in idx}, key=lambda k: (str(k[0]), k[1], k[2], k[3]))
    print(f"\n## {label}: L {Lpair[0]} -> {Lpair[1]}")
    print("pqr | rho | g | start | class | U(L2)+-se | SQ/V(L2)+-se | Smax/V(L2)@k | ratio_max | Smin/V(L2) | ratio_min | bonds/rec | cont uni/stag")
    out = []
    for k in keys:
        if (k, Lpair[0]) in idx and (k, Lpair[1]) in idx:
            a, b = idx[(k, Lpair[0])], idx[(k, Lpair[1])]
            c, rmax, rmin = classify(a, b)
            out.append((k, c))
            print(f"{k[0]} | {k[1]} | {k[2]} | {k[3]} | {c} | {b['U']:.3f}+-{b['U_se']:.3f} | {b['SQ_over_V']:.4f}+-{b['SQ_over_V_se']:.4f} | "
                  f"{b['Smax_over_V']:.4f}@{b['kmax']} | {rmax:.2f} | {b['Smin_over_V']:.4f} | {rmin:.2f} | {b['bonds_per_rec']:.3f} | "
                  f"{b['cont_uni']:.3f}/{b['cont_stag']:.3f}")
    return out


for t, Lp in (("C1", (16, 24)), ("C1", (12, 16)), ("C3", (16, 24)), ("C2", (12, 16)), ("H", (16, 16))):
    runs = load(t)
    if not runs:
        continue
    if t == "H":
        print("\n## H: hysteresis, L=16, random vs board start")
        idx = collections.defaultdict(dict)
        for r in runs:
            idx[(r["rho"], r["g"])][r["start"].split("(")[0]] = r
        for k, v in sorted(idx.items()):
            if "rand" in v and "board" in v:
                print(f"rho={k[0]} g={k[1]}: SQ/V rand {v['rand']['SQ_over_V']:.4f} board {v['board']['SQ_over_V']:.4f} | "
                      f"U rand {v['rand']['U']:.3f} board {v['board']['U']:.3f} | Smin/V rand {v['rand']['Smin_over_V']:.4f} board {v['board']['Smin_over_V']:.4f}")
        continue
    table(runs, Lp, t)

# Chessboard residual translations (FCC sublattice) and the 8 corners
gens = [(1, 1, 0), (1, 0, 1), (0, 1, 1)]
fold = [n for n in itertools.product([0, 1], repeat=3) if all(sum(ni * ti for ni, ti in zip(n, t)) % 2 == 0 for t in gens)]
print("\nchessboard (FCC residual translations): corners folded onto Gamma:", fold)
pairs = sorted({tuple(sorted([n, tuple((ni + 1) % 2 for ni in n)])) for n in itertools.product([0, 1], repeat=3)})
print("corner classes under k -> k + (pi,pi,pi):", pairs)
