#!/usr/bin/env python3
"""row 973: pooled tie-mode values and per-step factors g = (lambda(16)/lambda(8))^(1/4) by the rules of
library/gap-tiesearch-opus.md Sections 2 and 5.1 (replica rule): pooled value = plain mean of the chains, error = max(propagated
block error sqrt(sum e^2)/n, chain-to-chain standard error of the mean); sigma_g = g (r_8 + r_16)/4, r = relative errors.
Screen runs (S_*) are not pooled. Value: lambda_star for xy, colour 3 (index 2) for twists. Usage: python3 -I analyze.py"""
import json, glob, os, math, re
def val(r, slc):
    return tuple(r["lambda_star"]) if slc == "xy" else tuple(r["X0_raw2"][2])
rows = {}
for p in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs", "*.json"))):
    n = os.path.basename(p)[:-5]
    m = re.match(r"(F|R|K3)_(xy|zt90|zt45)_b([\d.]+)_L(\d+)", n)
    if not m:
        continue
    r = json.load(open(p))
    rows.setdefault((m.group(3), m.group(2), int(m.group(4))), []).append((n, *val(r, m.group(2))))
def pool(ch):
    v = [c[1] for c in ch]; e = [c[2] for c in ch]; k = len(v); mu = sum(v) / k
    eb = math.sqrt(sum(x * x for x in e)) / k
    es = (math.sqrt(sum((x - mu) ** 2 for x in v) / (k - 1)) / math.sqrt(k)) if k > 1 else 0.0
    return mu, max(eb, es), k
for b in ("2.4", "2.3"):
    for s in ("xy", "zt90", "zt45"):
        line = []; P = {}
        for L in (8, 10, 12, 14, 16):
            ch = rows.get((b, s, L))
            if ch:
                P[L] = pool(ch); line.append("L%d %.2f+-%.2f (n=%d: %s)" % (L, *P[L], ", ".join("%.2f" % c[1] for c in ch)))
        if 8 in P and 16 in P:
            g = (P[16][0] / P[8][0]) ** 0.25
            sg = g * (P[8][1] / P[8][0] + P[16][1] / P[16][0]) / 4
            verdict = "REFUTES" if g - 2 * sg > 1.25 else ("not refuted" if g + 2 * sg <= 1.25 else "INCONCLUSIVE")
            line.append("g=%.3f+-%.3f g+2s=%.3f g-2s=%.3f -> %s" % (g, sg, g + 2 * sg, g - 2 * sg, verdict))
        print("beta %s %s: " % (b, s) + "; ".join(line))
