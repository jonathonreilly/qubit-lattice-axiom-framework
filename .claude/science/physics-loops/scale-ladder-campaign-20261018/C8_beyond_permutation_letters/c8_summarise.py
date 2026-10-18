#!/usr/bin/env python3
"""C8: aggregate the class-3 screen pickles (screen_*.pkl from c8_screen.py)."""
import glob, pickle, collections, os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
tot = collections.Counter(); pat = collections.Counter(); pc = collections.Counter(); best = []; kst_minus = collections.Counter()
files = sorted(glob.glob(os.path.join(HERE, 'screen_*.pkl')))
for f in files:
    d = pickle.load(open(f, 'rb')); recs = d['recs']
    for r in recs:
        tot['levels'] += 1; tot[r['kind']] += 1
        if r['fermi']: tot['fermi'] += 1; continue
        tot['survivors'] += 1
        if not r['bad']: tot['clean'] += 1
        if r.get('early'): tot['early'] += 1
        pat[tuple(sorted(set((x[1], x[2], x[3]) for x in r['bad'])))] += 1
        for x in r['bad']: pc[(x[1], x[3])] += 1
        mk = [x for x in r['nodes'] if x[1] == 'cube' and np.allclose(np.array(x[0]), -np.array([0.5, -0.5, 0.5]), atol=1e-4)]
        kst_minus[(mk[0][2], mk[0][3]) if mk else 'not at E'] += 1
        best.append((len(r['bad']), r['sk'], r['names'], round(r['E'], 4), r['kind'], [(x[0], x[1], x[2], x[3]) for x in r['bad'][:3]], bool(r.get('early'))))
    print(f"  {os.path.basename(f)}: {len(recs)} levels")
print("totals:", dict(tot))
print("defective-node (point class, defect) counts among survivors:", dict(pc.most_common(20)))
print("-k* status among survivors (multiplicity, verdict):", dict(kst_minus))
print("most common obstruction sets:")
for k, n in pat.most_common(12): print(f"  {n:5d}  {list(k)[:6]}")
print("fewest defective nodes (early = rejected at the first defective (pi/4)Z^3 node, so counts are lower bounds):")
for b in sorted(best, key=lambda x: x[0])[:10]: print("  ", b)
check("aggregate: no level passes the closure criterion", tot['clean'] == 0, f"clean = {tot['clean']}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
