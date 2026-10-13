"""R19-7 s3: compact table from s2 pickles: per (bU, v): gap w1-w0, and per k-point the main pole (>=10% weight)
of TT1, TT2, V1, S1 ('-' = channel has zero weight at that k), plus S of TT2."""
import pickle, sys, numpy as np
tag = sys.argv[1]; res = pickle.load(open("../data/s2_%s.pkl" % tag, "rb"))
keys = sorted({(k[0], k[1]) for k in res if len(k) == 3})
kp = sorted({(k[2], k[3]) for k in res if len(k) == 5}, key=lambda x: (x[0] != "axis", x[0], x[1]))
chs = ["TT1", "TT2", "V1", "S1"]
print("tag", tag, "k-points", kp)
print("columns per k: main pole TT1/TT2/V1/S1 ; [S_TT2]")
for (bU, v) in keys:
    w = res[(bU, v, "w")]; cells = []
    for (nm, m) in kp:
        c = []
        for ch in chs:
            dg = res.get((bU, v, nm, m, ch))
            c.append("-" if (dg is None or dg["S"] < 1e-8) else ("%.3g" % dg["main"]))
        s2 = res.get((bU, v, nm, m, "TT2")); c.append("[%.3g]" % (s2["S"] if s2 else 0))
        cells.append("%s%s:%s" % (nm[0:2], "" if m < 0 else m, "/".join(c)))
    print("bU=%.1f v=%5.2f gap=%-9.4g %s" % (bU, v, w[1] - w[0], "  ".join(cells)))
