#!/usr/bin/env python3
"""B25 part 2a: does level pinning follow the k-independent unitary lattice Lambda_u, or every spectral taste?
For words whose Lambda_sp exceeds Lambda_u (index 2, bcc extension) we list the classes (mod Lambda_sp) of points that are
fixed by a commuting C2 pair mod Lambda_sp but not T-fixed, split by whether they are also C2-pair fixed mod Lambda_u, and
record whether all 12 levels there are even (pinned degeneracies).  Extension kinds: 'T' (k-independent transpose
intertwiner, antiunitary-type) and 'kdep' (no k-independent intertwiner; k-dependent unitary, ALIGN2 words
S^a P S^a G S^a P^T S^a G).  Prints PASS/FAIL, TOTAL."""
import sys, os, time, collections, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b25lib import *
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
ALL.update(PLANE6)
def bld(sk, names):
    it = iter(names); return [ALL[next(it)] if L in ('o', 'p', 'q') else L for L in sk]
R = pickle.load(open(os.path.join(HERE, 'census.pkl'), 'rb'))['R']
sel = [(j, r) for j, r in R if r and 'index' in r and r['index'] == 2]
print(f"{len(sel)} census words with [Lambda_sp : Lambda_u] = 2")
grid = np.array(list(itertools.product(range(32), repeat=3)))
def fixers(L):
    memb = np.zeros((32,) * 3, bool)
    for v in L: memb[v] = True
    return np.array([memb[tuple(((grid @ R_.T + c - grid) % 32).T)] for R_, c in ACT])
def classes(mask, L):
    Lv = np.array(sorted(L)); cov = np.zeros((32,) * 3, bool); reps = []
    for q in grid[mask]:
        if cov[tuple(q)]: continue
        reps.append(q); cov[tuple(((q + Lv) % 32).T)] = True
    return reps
stat = collections.Counter(); ex = {}
for j, r in sel:
    w = bld(j[1], j[2]); Lu, Ls = LATS[r['Lu']], LATS[r['Lsp']]
    kind = 'kdep' if r['kdep'] else 'T'
    Fu, Fs = fixers(Lu), fixers(Ls)
    istT = np.array(IST)
    def c2(F):
        p = np.zeros(len(grid), bool)
        for a, b in C2PAIRS: p |= F[a] & F[b]
        return p
    pu, ps = c2(Fu), c2(Fs); tfs = np.all(Fs[istT], axis=0)
    for lab, mask in (('C2pair mod Lsp & mod Lu', ps & pu & ~tfs), ('C2pair mod Lsp only', ps & ~pu & ~tfs), ('C2pair mod Lu only', pu & ~ps & ~tfs)):
        for q in classes(mask, Ls):
            e = np.angle(np.linalg.eigvals(Wb(w, (np.pi / 16 * q)[None])[0]))
            mm = [m for _, m in levels(np.diag(np.exp(1j * e)))]
            ev = all(m % 2 == 0 for m in mm)
            stat[(kind, r['Lu'], r['Lsp'], lab, ev)] += 1; ex.setdefault((kind, lab, ev), (j[1], j[2], tuple(q), mm))
for k in sorted(stat, key=str): print("  ", k, stat[k])
for k, v in ex.items(): print("   example", k, v)
kd = {k: v for k, v in stat.items() if k[0] == 'kdep'}; tt = {k: v for k, v in stat.items() if k[0] == 'T'}
check("audit covered both extension kinds", len(kd) > 0 and len(tt) > 0)
both = [k for k in stat if k[3] == 'C2pair mod Lsp & mod Lu']
check("at points that are C2-pair fixed mod BOTH lattices, every level is even (pinned) for every word", all(k[4] for k in both), f"{sum(stat[k] for k in both)} classes")
only_s = {k: v for k, v in stat.items() if k[3] == 'C2pair mod Lsp only'}
print("   C2pair-mod-Lsp-only classes (kind, all-even) ->", {(k[0], k[4]): 0 for k in only_s} | {(k[0], k[4]): sum(v for kk, v in only_s.items() if (kk[0], kk[4]) == (k[0], k[4])) for k in only_s})
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
