#!/usr/bin/env python3
"""B24 screen: taste-enlarged (no R_L) parameter-free words with mixed S powers (S^{+-1,+-2,+-4}), Clifford on-site
letters (PC: Clifford phases of the H_on / Lambda eigenprojectors) and plane letters (PP + e^{i phi}(1-PP)).
Stage A: k* levels that are exactly 2-fold (spin-1/2 doublet) or 4-fold D+ (+) D- (Dirac).
Stage B: r(k) = det(W - e^{iE}) / (e^{6iE} sqrt det W(0)) real; a sign change on the 16^3 (24^3 for S^4 words) grid proves a
         band crossing E (Fermi surface) -> reject.
Stage C (survivors): nodes at E from (pi/8)Z^3 points + Nelder-Mead from the 40 lowest grid points; each classified by
         degenerate perturbation theory (B23 classify); pass iff every node is an untilted isotropic cone set at
         v = |n_S| sqrt2/3.  Each node is typed relative to the word's own spectral level-preserving taste lattice Lambda_0:
         T (T-fixed mod Lambda_0), C2 (commuting-C2-pair fixed, not T), low, gen (off (pi/16)Z^3).
Usage: b24_screen.py <fam:i,j> [nproc]"""
import sys, os, time, pickle, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b24lib import *
from multiprocessing import Pool
TAG = sys.argv[1]; NP = int(sys.argv[2]) if len(sys.argv) > 2 else 4
OUT = os.path.join(HERE, f"screen_{TAG.replace(':', '_').replace(',', '-')}.pkl")
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
if __name__ == '__main__':
    t0 = time.time()
    _k = np.array([0.3, -0.7, 1.1]); _w = ['S4', UH, 'S2i', UL, 'S4i', 'S']
    W_, G_ = W_grad(_w, _k); h = 1e-6
    fd = [(Wb(_w, (_k + h * np.eye(3)[j])[None])[0] - Wb(_w, (_k - h * np.eye(3)[j])[None])[0]) / (2 * h) for j in range(3)]
    S4ok = np.allclose(Wb(['S4'], _k[None])[0], np.linalg.matrix_power(SKc(_k), 4))
    check("S^4 letter = S(k)^4; analytic word gradient = finite difference", S4ok and max(np.abs(a - b).max() for a, b in zip(G_, fd)) < 1e-6)
    check("plane letters commute with Z_x, Z_y, Z_z and are PSG-symmetric on-site unitaries",
          all(all(np.allclose(Z @ M, M @ Z) for Z in Zs) and np.allclose(M @ M.conj().T, np.eye(12)) and onsite_check(M) for M in list(PLANE.values()) + list(PLANE6.values())[:3]))
    J = list(jobs24(TAG)); print(f"{TAG}: {len(J)} words", flush=True)
    with Pool(NP) as p: res = p.map(stageAB, J, chunksize=16)
    stats = collections.Counter(); recs = []
    for st, out in res:
        if st == 'nS0': stats['words n_S=0'] += 1; continue
        stats.update(st); recs.extend(out)
    nf = [r for r in recs if not r['fermi']]
    byk = collections.Counter((r['kind'], r['fermi']) for r in recs)
    print(f"  k* level stats: {dict(stats)}; screened (kind, fermi): {dict(byk)}  [{time.time() - t0:.0f}s]", flush=True)
    check("r(k) real on every grid (det W k-independent)", all(r['rimag'] < 1e-8 for r in recs), f"max {max([r['rimag'] for r in recs], default=0):.1e}")
    with Pool(NP) as p: cres = p.map(stageC, nf, chunksize=2)
    allrecs = [r for r in recs if r['fermi']] + cres
    pickle.dump(dict(tag=TAG, stats=dict(stats), recs=allrecs), open(OUT, 'wb'))
    kst_ok = [any(abs(np.array(x[0]) - kst / np.pi).max() < 1e-4 and x[3] == 'ok' for x in r['nodes']) for r in cres]
    check("DPT classifier sanity: every survivor's k* node is classified an isotropic untilted cone set at |n_S| sqrt2/3 (L1 / Dirac lemma)", all(kst_ok), f"{sum(kst_ok)}/{len(cres)}")
    clean = [r for r in cres if not r['bad']]
    print(f"  survivors {len(cres)}; clean at screen level: {len(clean)}  [{time.time() - t0:.0f}s]")
    for r in clean: print("   CLEAN:", r['sk'], r['names'], r['E'], r['kind'], r['L0'], [(x[0], x[1], x[2]) for x in r['nodes']])
    pat = collections.Counter(); lat = collections.Counter()
    for r in cres:
        lat[r['L0']] += 1
        for x in r['bad']: pat[(x[1], x[3], x[2])] += 1
    print("  survivors by Lambda_0:", dict(lat))
    print("  defective nodes by (type mod Lambda_0, verdict, multiplicity):", dict(pat.most_common(20)))
    best = sorted(cres, key=lambda r: (len(r['bad']), sum(1 for x in r['bad'] if x[1] == 'gen')))[:12]
    for r in best:
        print(f"   best: {r['sk']} {r['names']} E={r['E']:+.4f} {r['kind']} L0={r['L0']} nbad={len(r['bad'])} "
              f"bad={[(x[0], x[1], x[2], x[3], x[4].get('smin'), x[4].get('smax')) for x in r['bad'][:4]]}")
    check("screen ran on every word (stage A/B) and every survivor (stage C)", len(cres) == len(nf))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
