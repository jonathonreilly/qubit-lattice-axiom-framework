#!/usr/bin/env python3
"""Recompute the block's L=2 validation tables from the raw validation files that the author moved to the
session scratchpad (path given as argv[1]), using the block's own analysis (analyze.estimate) with its data
directory redirected, and compare line by line with logs/validate_L2_val2.log and validate_L2_val3.log.
This checks provenance (log <-> data), not the method."""
import os, sys, re, json
sys.dont_write_bytecode = True
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
import analyze
analyze.D = sys.argv[1]
ex = json.load(open(os.path.join(HERE, "..", "data", "exact_L2.json")))["0.0"]["beta"]
npass = nfail = 0
for tags, logf in ((["val2_s1", "val2_s2"], "validate_L2_val2.log"), (["val3_s1", "val3_s2"], "validate_L2_val3.log")):
    per, comb = analyze.estimate(tags)
    betas = per[0]["betas"]
    logged = {}
    for line in open(os.path.join(HERE, "..", "logs", logf)):
        m = re.match(r"\[(PASS|FAIL)\] V=0.0 beta=(\S+) (\S+): QMC (\S+) \+- (\S+)\s+exact (\S+)\s+z=(\S+)", line)
        if m: logged[(float(m.group(2)), m.group(3))] = (float(m.group(4)), float(m.group(5)), float(m.group(7)))
    ok_all = True; nrow = 0; fails = 0
    for i, b in enumerate(betas):
        if str(float(b)) not in ex: continue
        for q, eq in (("E", "E"), ("W2", "W2"), ("P0", "P0"), ("Nc", "Nc"), ("S1", "Sq")):
            mu, se = comb[q][0][i], comb[q][1][i]
            z = (mu - ex[str(float(b))][eq]) / se
            lm, ls, lz = logged[(float(b), q)]
            nrow += 1; fails += abs(z) > 3
            if not (abs(mu - lm) < 1e-5 + 1e-5 * abs(lm) and abs(se - ls) < 1e-5 and abs(z - lz) < 0.01):
                ok_all = False
    ok = ok_all and nrow == len(logged)
    print(f"[{'PASS' if ok else 'FAIL'}] {logf}: {nrow} rows recomputed from raw files match the log (recomputed FAIL count {fails})")
    npass += ok; nfail += (not ok)
print(f"TOTAL: PASS={npass} FAIL={nfail}")
