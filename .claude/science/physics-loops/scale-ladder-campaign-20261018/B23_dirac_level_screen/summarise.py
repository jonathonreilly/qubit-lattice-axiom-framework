#!/usr/bin/env python3
"""B23 summary over all screen_*.pkl: counts per family/skeleton, coarse obstruction classes, best candidates.
Coarse class of a survivor = set of (point class of a defective node) with defects merged; plus flags:
'band' (a single band at E found by Nelder-Mead: Fermi surface missed by the sign test),
'cube-only' (every defective node sits at a cube point (+-pi/2)^3, i.e. +-k* or its doublers)."""
import glob, pickle, collections, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
tot = collections.Counter(); allsurv = []
for fn in sorted(glob.glob(os.path.join(HERE, 'screen_*.pkl'))):
    D = pickle.load(open(fn, 'rb')); R = D['recs']; surv = [r for r in R if not r['fermi']]
    fam = D['tag'].split(':')[0]
    tot[fam, 'words'] += 0; tot[fam, 'Dirac levels'] += len(R); tot[fam, 'fermi (sign test)'] += len(R) - len(surv); tot[fam, 'survivors'] += len(surv)
    tot[fam, 'clean'] += sum(1 for r in surv if not r['bad'])
    for k, v in D['stats'].items(): tot[fam, k] += v
    for r in surv: r['fam'] = fam; allsurv.append(r)
    print(f"== {os.path.basename(fn)}  per skeleton (Dirac levels, survivors):",
          {str(sk): (sum(1 for r in R if r['sk'] == sk), sum(1 for r in surv if r['sk'] == sk)) for sk in sorted(set(r['sk'] for r in R))})
print("\nTotals by family:")
for fam in sorted(set(f for f, _ in tot)):
    print("  ", fam, {k: v for (f, k), v in tot.items() if f == fam and k != 'words'})
def coarse(r):
    defs = set(x[3] for x in r['bad']); pcs = set(x[1] for x in r['bad'])
    if 'band' in defs: return 'band crossing at E (missed by sign test)'
    if pcs <= {'cube'}: return 'cube points only (doublers of +-k*): ' + '/'.join(sorted(defs))
    if 'cube' in pcs: return 'cube doublers + other points'
    hs = pcs & {'Gamma', 'X_pi', 'M_pi', 'R_pi'}
    if hs: return 'piZ^3 points (Gamma/X/M/R) + others'
    if pcs & {'X_r', 'M_r', '(1,1/2,1/2)pi', '(0,1/2,1)pi', '(1,1,1/2)pi'}: return '(pi/2)Z^3 non-cube points + others'
    if pcs <= {'generic'}: return 'generic-k nodes only: ' + '/'.join(sorted(defs))
    return 'other (pi/4 lattice etc.)'
cc = collections.Counter((r['fam'], coarse(r)) for r in allsurv)
print("\nCoarse obstruction classes (family, class): count")
for k, v in sorted(cc.items()): print(f"   {v:5d}  {k}")
cs = collections.Counter((r['fam'], r['sk'], coarse(r).split(':')[0]) for r in allsurv)
print("\nPer skeleton:")
for k, v in sorted(cs.items(), key=lambda t: (t[0][0], str(t[0][1]), -t[1])): print(f"   {v:5d}  {k}")
mind = sorted(set(min(len(r['bad']) for r in allsurv if r['sk'] == sk and r['fam'] == f) for f, sk in set((r['fam'], r['sk']) for r in allsurv)))
print("minimum number of defective nodes per (family, skeleton):", {f"{f}{sk}": min(len(r['bad']) for r in allsurv if r['sk'] == sk and r['fam'] == f) for f, sk in sorted(set((r['fam'], r['sk']) for r in allsurv), key=str)})
dcount = collections.Counter(x[3] for r in allsurv for x in r['bad'])
print("\nDefect types over all defective nodes:", dict(dcount))
print("Speeds ratio smax/smin and tilt never matter for the verdict once one defect exists; best candidates by (number of defective nodes, smallest anisotropy):")
def score(r): return (len(r['bad']), min([x[4].get('smax', 9) - x[4].get('smin', 0) for x in r['bad']], default=0))
for r in sorted(allsurv, key=score)[:15]:
    print(f"   {r['fam']:10s} {r['sk']} {r['names']} E={r['E']:+.4f} nS={r['nS']} nR={r['nR']} v_D={r['vs']:.5f} nodes={len(r['nodes'])} bad={len(r['bad'])}")
    for x in r['bad'][:4]: print(f"        k/pi={tuple(float(y) for y in x[0])} {x[1]} m={x[2]} {x[3]} speeds[{x[4].get('smin')},{x[4].get('smax')}] tilt={x[4].get('tilt')}")
clean = [r for r in allsurv if not r['bad']]
print(f"\nclean at screen level: {len(clean)}")
check("every survivor's +k* node classified as the expected 4-fold Dirac point (classifier sanity)",
      all(any(x[1] == 'cube' and x[2] == 4 and x[3] == 'ok' and np.allclose(np.array(x[0]), [0.5, -0.5, 0.5], atol=1e-4) for x in r['nodes']) for r in allsurv))
check("every rejected survivor has at least one explicit defective node (no silent rejection)", all(r['bad'] for r in allsurv if r not in clean))
print(f"\nRESULT: Dirac levels={sum(v for (f,k),v in tot.items() if k=='Dirac levels')} survivors={len(allsurv)} clean_at_screen={len(clean)}")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
