#!/usr/bin/env python3
"""Compact table of lane952 JSON logs (row 952). Usage: python3 -I summarize.py <json> ..."""
import json, sys, os

def f(v, d=2):
    return ("%." + str(d) + "f") % v

for p in sys.argv[1:]:
    r = json.load(open(p))
    a = r["args"]
    name = os.path.basename(p).replace(".json", "")
    line = [name, "grp=" + a["group"], "b=" + str(a["beta"]), "L=" + str(a["L"]), "s=%.1fs" % r.get("seconds", 0)]
    if a["group"] == "su2":
        ls = r.get("lambda_star")
        if ls:
            line.append("lam*=%s+-%s" % (f(ls[0]), f(ls[1])))
        x2 = r.get("X0_raw2")
        if x2:
            line.append("X0^2=" + "/".join(f(v[0]) for v in x2))
        if "LB_split_Y1" in r:
            yx, eyx = r["Y1X3"]; y2 = r["Y1_raw2"][0]
            elb = 2 * abs(yx) * eyx / y2 if y2 else float("nan")
            line.append("LB=%s+-%s (full %s, Y1Y2 %s)" % (f(r["LB_split_Y1"]), f(elb), f(r["LB_full_Y1"]), f(r["LB_Y1Y2"])))
        for c in (3, 1):
            k = "lag_X%d" % c
            if k in r:
                d = r[k]
                line.append("lagX%d[0,8,16,32,64]=" % c + "/".join(f(d[n][0]) for n in ("0", "8", "16", "32", "64") if n in d)
                            + " (e64 %s)" % f(d["64"][1]))
        if "pca_split_top" in r:
            line.append("pca split=%s ins=%s C0=%s" % ("/".join(f(v) for v in r["pca_split_top"]),
                                                     "/".join(f(v) for v in r["pca_insample_top"]), f(r["pca_C0_top_insample"])))
        if "percomp_var" in r:
            line.append("var=%s lmax=%s@%s" % (f(r["percomp_var"][0], 4), f(r["lambda_max_k"]), r["k_of_max"]))
    else:
        line.append("X0^2=%s+-%s" % (f(r["X0_raw2"][0]), f(r["X0_raw2"][1])))
        yx, eyx = r["YX"]; y2 = r["Y_raw2"][0]
        line.append("LB=%s (+-%s)" % (f(r["LB_split_Y"]), f(2 * abs(yx) * eyx / y2)))
        if "lag_X" in r:
            d = r["lag_X"]
            line.append("lagX[0,8,16,32,64]=" + "/".join(f(d[n][0]) for n in ("0", "8", "16", "32", "64")) + " (e64 %s)" % f(d["64"][1]))
    print(" | ".join(line))
