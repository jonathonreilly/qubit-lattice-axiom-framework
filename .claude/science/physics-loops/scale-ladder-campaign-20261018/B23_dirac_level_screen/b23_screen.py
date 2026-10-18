#!/usr/bin/env python3
"""B23: screen the Dirac (4-fold D+ (+) D-) k* levels of B20's cliff2, pi6 and taste-pi6 word families
(rebuilt in the B20 checker's model, chklib; independent of b20lib).
Stage A: levels of W(k*); keep 4-fold levels whose eigenspace is D+ (+) D- (= H_on = 2 space), n_S != 0.
Stage B: r(k) = det(W - e^{iE}) / (e^{6iE} sqrt(det W(0))) on the 16^3 grid; a sign change proves a band crossing E.
Stage C (survivors): candidate nodes = (pi/4)Z^3 points at E  +  Nelder-Mead from the 40 lowest grid points;
         every node classified by degenerate perturbation theory (DPT): pass only if every node is an untilted
         isotropic linear cone set with speed v_D = |n_S| sqrt2/3 (directional DPT spectra all +-v_D).
Usage: b23_screen.py <tag> [nproc]    tag in cliff2:i,j,..  pi6  taste_pi6"""
import sys, time, pickle, collections
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from b23lib import *
from multiprocessing import Pool
TAG = sys.argv[1] if len(sys.argv) > 1 else "test"; NP = int(sys.argv[2]) if len(sys.argv) > 2 else 4
OUT = os.path.join(HERE, f"screen_{TAG.replace(':', '_').replace(',', '-')}.pkl")
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

def stageAB(job):
    sk, names = job; w = build(sk, names); ns = nS(w); out = []
    if ns == 0: return ('nS0', [])
    W0 = Wb(w, kst[None])[0]; e, V = np.linalg.eig(W0); st = collections.Counter()
    for E, m in levels(W0):
        if m != 4: continue
        Vd = V[:, np.abs(wrap(np.angle(e) - E)) < 1e-6]; Q, _ = np.linalg.qr(Vd)
        if abs(np.linalg.norm(Q.conj().T @ Dpm) ** 2 - 4) > 1e-6: st['G3/2'] += 1; continue
        st['D+D-'] += 1
        Ws = Wb(w, GRID); c0 = np.linalg.det(Wb(w, np.zeros((1, 3)))[0])
        r = np.linalg.det(Ws - np.exp(1j * E) * np.eye(12)) / (np.exp(6j * E) * np.sqrt(c0))
        rim = float(np.abs(r.imag).max() / max(np.abs(r).max(), 1e-300))
        fermi = bool(r.real.max() > 0 and r.real.min() < 0)
        out.append(dict(sk=sk, names=names, E=float(E), nS=ns, nR=nR(w), fermi=fermi, rimag=rim))
    return (dict(st), out)

def stageC(rec):
    w = build(rec['sk'], rec['names']); E = rec['E']; vs = abs(rec['nS']) * np.sqrt(2) / 3
    f = lambda k: float(dist_E(w, np.asarray(k)[None], E)[0])
    d = dist_E(w, GRID, E); ds = dist_E(w, SPEC, E)
    nodes = [k for k, x in zip(SPEC, ds) if x < 1e-7]
    for i in np.argsort(d)[:40]:
        r_ = minimize(f, GRID[i], method='Nelder-Mead', options={'xatol': 1e-11, 'fatol': 1e-13, 'maxiter': 3000})
        if r_.fun < 1e-7: nodes.append(r_.x)
    uniq = []
    for k in nodes:
        k = wrap(k)
        if not any(np.linalg.norm(wrap(k - u)) < 1e-4 for u in uniq): uniq.append(k)
    res = []
    for k in uniq:
        c = classify(w, k, E, vs)
        if c is None: continue
        res.append((tuple(np.round(k / np.pi, 5)), kclass(k), c[0], c[1], {a: round(b, 6) for a, b in c[2].items()}))
    rec = dict(rec); rec['vs'] = vs; rec['gridmin'] = float(d.min()); rec['nodes'] = res
    rec['bad'] = [x for x in res if x[3] != 'ok']
    return rec

if __name__ == '__main__':
    t0 = time.time()
    check("H_on = 2 eigenspace is 4-dim and equals D+ + D- (Lambda = -+2sqrt2 on it)", Dpm.shape[1] == 4 and np.allclose(np.sort(np.linalg.eigvalsh(Dpm.conj().T @ Lam @ Dpm)), [-2 * np.sqrt(2)] * 2 + [2 * np.sqrt(2)] * 2))
    _k = np.array([0.3, -0.7, 1.1]); _w = ['S', 'R', UH, 'S2i', UL, 'Si', 'R']
    W_, G_ = W_grad(_w, _k); h = 1e-6
    fd = [(Wword(_w, _k + h * np.eye(3)[j]) - Wword(_w, _k - h * np.eye(3)[j])) / (2 * h) for j in range(3)]
    check("batched word == chklib Wword, analytic gradient == finite difference", np.allclose(Wb(_w, _k[None])[0], Wword(_w, _k)) and max(np.abs(a - b).max() for a, b in zip(G_, fd)) < 1e-7)
    J = list(jobs(TAG)); print(f"{TAG}: {len(J)} words", flush=True)
    with Pool(NP) as p: res = p.map(stageAB, J, chunksize=32)
    stats = collections.Counter(); recs = []
    for st, out in res:
        if st == 'nS0': stats['words n_S=0'] += 1; continue
        stats.update(st); recs.extend(out)
    nf = [r for r in recs if not r['fermi']]
    print(f"  4-fold k* level statistics: {dict(stats)}; Dirac levels with r sign change (Fermi surface): {len(recs) - len(nf)}; without: {len(nf)}  [{time.time() - t0:.0f}s]", flush=True)
    check("r(k) real on every grid (det W k-independent)", all(r['rimag'] < 1e-8 for r in recs), f"max {max([r['rimag'] for r in recs], default=0):.1e}")
    with Pool(NP) as p: cres = p.map(stageC, nf, chunksize=2)
    allrecs = [r for r in recs if r['fermi']] + cres
    pickle.dump(dict(tag=TAG, stats=dict(stats), recs=allrecs), open(OUT, 'wb'))
    # k* node itself must be classified ok (L1 caveat (b)): sanity of the DPT classifier on every survivor
    kst_ok = [any(x[1].startswith('cube') and abs(np.array(x[0]) - kst / np.pi).max() < 1e-4 and x[3] == 'ok' and x[2] == 4 for x in r['nodes']) for r in cres]
    check("every survivor's k* node is a 4-fold isotropic untilted Dirac point at |n_S| sqrt2/3 (DPT)", all(kst_ok), f"{sum(kst_ok)}/{len(cres)}")
    clean = [r for r in cres if not r['bad']]
    print(f"  {len(clean)} survivors with every found node an isotropic untilted cone at v_D (screen level)  [{time.time() - t0:.0f}s]")
    for r in clean[:30]: print("   CLEAN-AT-SCREEN:", r['sk'], r['names'], round(r['E'], 4), r['nS'], [(x[0], x[1], x[2]) for x in r['nodes']])
    pat = collections.Counter(); ex = {}
    for r in cres:
        if not r['bad']: continue
        key = (r['sk'], tuple(sorted(set((x[1], x[2], x[3]) for x in r['bad']))))
        pat[key] += 1; ex.setdefault(key, r)
    print("  obstruction pattern among survivors (skeleton, {(point class, multiplicity, defect)}):")
    for key, n in pat.most_common(60):
        r = ex[key]; b = r['bad'][0]
        print(f"   {n:5d} x {key[0]} {list(key[1])}  e.g. {r['names']} E={r['E']:+.4f}  first bad: k/pi={b[0]} m={b[2]} {b[3]} {b[4]}")
    # nearest-to-passing: survivors with the fewest bad nodes, then smallest anisotropy
    def score(r): return (len(r['bad']), min([x[4].get('smax', 9) - x[4].get('smin', 0) for x in r['bad']], default=0))
    print("  best (fewest defective nodes):")
    for r in sorted(cres, key=score)[:10]:
        print("   ", r['sk'], r['names'], f"E={r['E']:+.4f} nS={r['nS']} nodes={len(r['nodes'])} bad={len(r['bad'])}", [(x[0], x[1], x[2], x[3], x[4].get('smin'), x[4].get('smax'), x[4].get('tilt')) for x in r['bad'][:3]])
    print(f"RESULT {TAG}: words={len(J)} Dirac_levels={len(recs)} fermi={len(recs) - len(nf)} survivors={len(nf)} clean_at_screen={len(clean)}")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
