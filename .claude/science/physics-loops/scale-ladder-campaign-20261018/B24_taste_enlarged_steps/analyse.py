#!/usr/bin/env python3
"""B24 aggregation + pinning analysis over all screen_*.pkl.
For every survivor (no Fermi sign change) and every defective node (verdict != ok) at a point of (pi/16)Z^3:
  * whether every level of W at that point is even-degenerate (operator-level even-level point, observed);
  * the quasi-energy symmetry group of the full spectrum at that point: maps E -> E + c and E -> -E + c (c in (pi/12)Z)
    leaving the 12-point multiset invariant; and whether the node level E is a fixed point of a reflection E -> c - E
    (a 'special' value) -- the counting mechanism: 6 doublets in orbits of a group of order 4 force a special orbit.
Prints aggregate tables, PASS/FAIL and TOTAL."""
import sys, os, glob, pickle, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b24lib import *
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
files = sorted(glob.glob(os.path.join(HERE, 'screen_*.pkl')))
tot = collections.Counter(); surv = []
for f in files:
    d = pickle.load(open(f, 'rb'))
    for r in d['recs']:
        tot[(r['kind'], 'fermi' if r['fermi'] else 'survivor')] += 1
        if not r['fermi']: surv.append(r)
    print(f"  {os.path.basename(f)}: stats {d['stats']}")
print("  totals (kind, outcome):", dict(tot))
clean = [r for r in surv if not r['bad']]
print(f"  survivors {len(surv)}, clean {len(clean)}")
def qsym(e):
    z = np.exp(1j * np.asarray(e)); out = []
    for s in (1, -1):
        for j in range(24):
            c = j * np.pi / 12
            z2 = np.exp(1j * (s * np.asarray(e) + c)); D = np.abs(z[:, None] - z2[None, :])
            if D.min(0).max() < 1e-7 and D.min(1).max() < 1e-7 and not (s == 1 and j == 0): out.append((s, j))
    return out
pat = collections.Counter(); evenlv = collections.Counter(); special = collections.Counter(); grp = collections.Counter()
for r in surv:
    w = build(r['sk'], r['names']); E = r['E']
    for x in r['bad']:
        k = np.array(x[0]) * np.pi; pt = x[1]
        pat[(pt, x[3])] += 1
        if pt == 'gen': continue
        W = Wb(w, k[None])[0]; lv = levels(W); e = np.angle(np.linalg.eigvals(W))
        evenlv[(pt, all(m % 2 == 0 for _, m in lv))] += 1
        sy = qsym(e); order = 1 + len(sy); grp[(pt, order)] += 1
        refl = [(s, j) for s, j in sy if s == -1 and abs(wrap(j * np.pi / 12 - 2 * E)) < 1e-6]
        special[(pt, bool(refl))] += 1
print("  defective nodes in survivors by (type mod Lambda_0, verdict):", dict(pat.most_common()))
print("  operator-level: all levels even at the defect point? (type, all-even):", dict(evenlv))
print("  order of the quasi-energy symmetry group of the spectrum at the defect point (type, order):", dict(grp))
print("  node level E fixed by a spectral reflection E -> c - E at the defect point (type, yes):", dict(special))
for r in sorted(surv, key=lambda r: len(r['bad']))[:15]:
    print(f"   best: {r['sk']} {r['names']} E={r['E']:+.4f} {r['kind']} L0={r['L0']} nbad={len(r['bad'])} "
          f"{[(x[0], x[1], x[2], x[3], x[4].get('smin'), x[4].get('smax')) for x in r['bad'][:3]]}")
check("aggregation read every screen pickle", len(files) > 0, f"{len(files)} files")
print(f"  RESULT: {len(clean)} screen-level clean candidates (outcome, not a test)")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
