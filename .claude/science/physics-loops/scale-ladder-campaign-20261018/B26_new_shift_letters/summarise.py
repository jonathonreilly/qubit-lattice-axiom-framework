#!/usr/bin/env python3
"""B26: aggregate all screen pickles; obstruction pattern by defect point class; best candidates; then a FULL node census
(no early reject: (pi/4)Z^3 nodes + 60 Nelder-Mead starts) of the best survivors.  A candidate with no defect after the
full census would go to certify (Lipschitz / Bauer-Fike); none is expected to reach it unless printed below."""
import sys, os, glob, pickle, collections, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
t0 = time.time()
from b26lib import *
from scipy.optimize import minimize
PHL = dict(PC); PHL.update({f"{h}*{l}": PC[h] @ PC[l] for h in PC if h[0] == 'H' for l in PC if l[0] == 'L'})
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
files = sorted(glob.glob(os.path.join(HERE, 'screen_*.pkl')))
tot = collections.Counter(); allsurv = []; lvlstats = collections.Counter(); words = 0; SEEN = set()
for f in files:
    d = pickle.load(open(f, 'rb')); lvlstats.update(d['stats'])
    # de-duplicate (sk, fill, E) across runs (PC fills of classes 0-21 also occur in the full-PHL run)
    recs = []
    for r in d['recs']:
        key = (r['sk'], r['names'], round(r['E'], 6))
        if key not in SEEN: SEEN.add(key); recs.append(r)
    surv = [r for r in recs if not r['fermi']]; allsurv += surv
    tot['levels'] += len(recs); tot['fermi'] += len(recs) - len(surv); tot['survivors'] += len(surv)
    tot['clean'] += sum(1 for r in surv if not r['bad'])
    tot['D+D- levels'] += sum(r['kind'] == 'D+D-' for r in recs); tot['D+/D- levels'] += sum(r['kind'] != 'D+D-' for r in recs)
    print(f"  {os.path.basename(f)}: levels {len(recs)}, survivors {len(surv)}, clean {sum(1 for r in surv if not r['bad'])}")
print("TOTALS (distinct (word, level) pairs):", dict(tot)); print("k* level types (all runs, before de-duplication):", dict(lvlstats))
check("no screened survivor is clean at screen level", tot['clean'] == 0, f"{tot['clean']} clean")
# obstruction pattern: point class of defects (any node with verdict != ok), per survivor
pc = collections.Counter(); kinds = collections.Counter(); first = collections.Counter()
for r in allsurv:
    cls = sorted(set((x[1], x[3]) for x in r['bad']))
    for c in cls: pc[c] += 1
    kinds[r['kind']] += 1
    # which little-group class carries a defect: D4 points (X_r, M_r-type), cube doublers, etc.
print("defect (point class, verdict) occurrence over survivors:")
for c, n in pc.most_common(25): print(f"   {n:6d}  {c}")
def nbad_noncube(r): return sum(1 for x in r['bad'] if not (x[1] == 'cube'))
only_cube = [r for r in allsurv if r['bad'] and all(x[1] == 'cube' for x in r['bad'])]
print(f"survivors whose (pi/4)Z^3 defects are ALL at cube points (+-k*-type and the 6 cube doublers): {len(only_cube)}")
def score(r): return (len(r['bad']), min([x[4].get('smax', 9) - x[4].get('smin', 0) for x in r['bad']], default=0))
best = sorted(allsurv, key=score)
seen = set(); top = []
for r in best:
    key = (r['sk'], r['names'], round(r['E'], 6))
    if key in seen: continue
    seen.add(key); top.append(r)
    if len(top) == 8: break
g12 = np.linspace(-np.pi, np.pi, 12, endpoint=False) + 0.0417; G12 = np.array(list(itertools.product(g12, repeat=3)))
print("\nFULL census of the 8 best survivors (no early reject):")
for r in top:
    w = [PHL[n] for n in r['names']]; it = iter(w); w = [next(it) if L == 'o' else L for L in r['sk']]; E = r['E']; vs = abs(r['nS']) * np.sqrt(2) / 3
    f = lambda k: float(dist_E(w, np.asarray(k)[None], E)[0])
    d = np.concatenate([dist_E(w, GRID, E), dist_E(w, G12, E)]); pts = np.vstack([GRID, G12]); ds = dist_E(w, SPEC, E)
    nodes = [k for k, x in zip(SPEC, ds) if x < 1e-7]
    for i in np.argsort(d)[:60]:
        r_ = minimize(f, pts[i], method='Nelder-Mead', options={'xatol': 1e-11, 'fatol': 1e-13, 'maxiter': 4000})
        if r_.fun < 1e-7: nodes.append(r_.x)
    uniq = []
    for k in nodes:
        k = wrap(k)
        if not any(np.linalg.norm(wrap(k - u)) < 1e-4 for u in uniq): uniq.append(k)
    res = collections.Counter(); ex = {}
    for k in uniq:
        c = classify(w, k, E, vs)
        if c is None: continue
        key = (kclass(k), c[0], c[1]); res[key] += 1; ex.setdefault(key, (np.round(k / np.pi, 4), {a: round(b, 4) for a, b in c[2].items() if a in ('smin', 'smax', 'tilt')}))
    nb = sum(n for k_, n in res.items() if k_[2] != 'ok')
    print(f"  {r['sk']} {r['names']} E={E:+.4f} {r['kind']} n_S={r['nS']} v={vs:.4f}: nodes {len(uniq)}, defective {nb}")
    for k_, n in sorted(res.items(), key=lambda t: -t[1]): print(f"      {n:3d} x {k_}  e.g. k/pi={ex[k_][0]} {ex[k_][1]}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
