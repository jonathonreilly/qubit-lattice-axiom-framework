#!/usr/bin/env python3
"""[POST HOC robustness check, written after seeing the declared analysis] chunk-mean errors for
<W^2> and P1 at beta=L: treat each 15-min chunk (after the declared 20% discard, applied to measurements)
as one sample; error = std(chunk means)/sqrt(nchunks). Compares with the declared 20-bin errors."""
import glob, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
for L, tags in ((4, ("L4_s3", "L4_s4")), (6, ("L6_s3", "L6_s4"))):
    allc = []
    for tag in tags:
        fs = sorted(glob.glob(os.path.join(HERE, "..", "data", "raw", tag + "_c*.npz")))
        ds = [np.load(f) for f in fs]
        k = list(ds[0]["keys"]); b = ds[0]["betas"]; i = int(np.argmin(np.abs(b - L)))
        n = [len(d["m"]) for d in ds]; cut = int(0.2 * sum(n))
        cm, w, acc = [], [], 0
        for d in ds:
            m = d["m"]; s = max(0, cut - acc); acc += len(m)
            if s >= len(m):
                continue
            W = m[s:, i, [k.index("Wx"), k.index("Wy"), k.index("Wz")]]
            cm.append(((W ** 2).mean(), (np.abs(W) == 1).mean()))
        cm = np.array(cm); allc.append(cm)
        print(f"L={L} {tag}: nchunks={len(cm)} W2 chunkmean={cm[:,0].mean():.4f}+-{cm[:,0].std(ddof=1)/np.sqrt(len(cm)):.4f}  P1={cm[:,1].mean():.4f}+-{cm[:,1].std(ddof=1)/np.sqrt(len(cm)):.4f}")
    a, c = allc
    ea, ec = (x[:, 0].std(ddof=1) / np.sqrt(len(x)) for x in (a, c))
    print(f"L={L}: start-diff z(W2, chunk errors) = {(a[:,0].mean()-c[:,0].mean())/np.hypot(ea, ec):+.2f}")
