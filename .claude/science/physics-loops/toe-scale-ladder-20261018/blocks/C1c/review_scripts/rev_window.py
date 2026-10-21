#!/usr/bin/env python3
"""Reviewer POST HOC sensitivity: per-chunk P1(beta=L) means from logs/drift_L{4,6}.log, retained series split in halves.
Unweighted chunk means (chunks have ~equal measurement counts). Not a criterion evaluation."""
import re, numpy as np
for L in (4, 6):
    P = {}
    for l in open(f"logs/drift_L{L}.log"):
        m = re.match(rf"(L{L}_s\d)_c(\d+).*?b={L} P0=(\S+) P1=(\S+)", l)
        if m: P.setdefault(m[1], []).append((float(m[3]), float(m[4])))
    for half in ("all", "first", "second"):
        p1s = []
        for t, v in P.items():
            v = np.array(v); r = v[int(0.2*len(v)+0.5):]; h = len(r)//2
            r = r if half == "all" else (r[:h] if half == "first" else r[h:])
            p1s.append(r.mean(0))
        P0, P1 = np.mean(p1s, 0)
        dF1 = -np.log(P1/(2*P0))/L
        print(f"L={L} {half:6s}: P1={P1:.4f} (per start {[round(x[1],4) for x in p1s]}) dF1={dF1:.3f} a={L*dF1:.3f}")
