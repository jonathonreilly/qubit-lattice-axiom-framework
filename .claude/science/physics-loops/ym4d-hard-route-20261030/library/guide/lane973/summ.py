#!/usr/bin/env python3
"""row 973: one line per JSON log: name, beta, L, colour raw moments of X_a (lag 0) with errors, means, lambda_star,
lambda_max_k with its k, seconds. Usage: python3 -I summ.py logs/*.json"""
import json, sys, os
for p in sys.argv[1:]:
    try:
        r = json.load(open(p))
    except Exception as e:
        print(os.path.basename(p), "unreadable", e); continue
    if "X0_raw2" not in r or not isinstance(r["X0_raw2"][0], list):
        continue
    a = r["args"]
    x2 = "/".join("%.2f(%.2f)" % tuple(v) for v in r["X0_raw2"])
    mn = "/".join("%.2f" % (v[0] / v[1] if v[1] > 0 else 0) for v in r["X0_mean"])
    print("%-24s b=%s L=%2d X^2[c1/c2/c3]=%s mean/err=%s lam*=%.2f(%.2f) lmaxk=%.2f@%s %.0fs" % (
        os.path.basename(p)[:-5], a["beta"], a["L"], x2, mn, r["lambda_star"][0], r["lambda_star"][1],
        r["lambda_max_k"], r["k_of_max"], r["seconds"]))
