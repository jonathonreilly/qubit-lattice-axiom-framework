#!/usr/bin/env python3
"""B26 part 3: B20/B23 closure screen of the enlarged-palette words (skeleton classes from skeletons.py, i.e. words in
{S^+-1, S^+-2, R_L, Rt = A0 R_L A0^-1 (= every even-A2-half-letter word)} with on-site Clifford slots, length <= 5,
reduced class not screened in B20/B23).  Model: b26lib (B20_check/chklib on B18_check/chk_model).
Stage A: levels of W(k*): keep 2-fold levels (D+ or D-; L1 => isotropic Weyl at |n_S|sqrt2/3) and 4-fold levels equal
         to D+ (+) D- (exact isotropic Dirac point, B20_check caveat b).  G3/2-containing levels are counted, not screened.
Stage B: r(k) = prod_j (lambda_j(k) - e^{iE}) / (e^{6iE} sqrt det W(0)) is real; a sign change on a grid proves a band
         crossing E (Fermi surface).  8^3 grid first (any sign change is a proof), then the 16^3 grid of B20/B23.
Stage C: survivors: nodes = (pi/4)Z^3 points at E + Nelder-Mead from the 40 lowest 16^3 points; classified by DPT
         (pass only if every node is an untilted isotropic linear cone at v = |n_S| sqrt2/3).
Usage: b26_screen.py <tag> [nproc]   tag = one:<palette>:<i0>-<i1>  |  two:<i0>-<i1>   (skeleton index ranges)"""
import sys, time, pickle, collections
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from b26lib import *
from skeletons import generate
from scipy.optimize import minimize
from multiprocessing import Pool
TAG = sys.argv[1] if len(sys.argv) > 1 else "one:PC:0-2"; NP = int(sys.argv[2]) if len(sys.argv) > 2 else 3
OUT = os.path.join(HERE, f"screen_{TAG.replace(':', '_')}.pkl")
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
G = generate(); ONE = sorted([v for (no, c), v in G.items() if no == 1], key=lambda s: (len(s), s)); TWO = sorted([v for (no, c), v in G.items() if no == 2], key=lambda s: (len(s), s))
PHL = dict(PC); PHL.update({f"{h}*{l}": PC[h] @ PC[l] for h in PC if h[0] == 'H' for l in PC if l[0] == 'L'})
PAL = {'PC': PC, 'PHL': PHL}
g8 = np.linspace(-np.pi, np.pi, 8, endpoint=False) + 0.1931; GRID8 = np.array(list(itertools.product(g8, repeat=3)))
def jobs(tag):
    p = tag.split(':')
    if p[0] == 'one':
        i0, i1 = map(int, p[2].split('-'))
        for sk in ONE[i0:i1]:
            for n in PAL[p[1]]: yield sk, (n,)
    elif p[0] == 'onesample':         # seeded random sample of N fills per one-slot class
        i0, i1 = map(int, p[2].split('-')); N = int(p[3]); rg = np.random.default_rng(4052 + i0); names = list(PAL[p[1]])
        for sk in ONE[i0:i1]:
            for t in rg.choice(len(names), size=N, replace=False): yield sk, (names[t],)
    elif p[0] == 'two':
        i0, i1 = map(int, p[1].split('-'))
        for sk in TWO[i0:i1]:
            for n1 in PC:
                for n2 in PC: yield sk, (n1, n2)
    elif p[0] == 'twosample':          # seeded random sample of N fills per two-slot class
        i0, i1 = map(int, p[1].split('-')); N = int(p[2]); rg = np.random.default_rng(2026 + i0)
        names = list(PC)
        for sk in TWO[i0:i1]:
            for t in rg.choice(len(names) ** 2, size=N, replace=False): yield sk, (names[t // len(names)], names[t % len(names)])
def build(sk, names, pal):
    it = iter(names); return [pal[next(it)] if L == 'o' else L for L in sk]
def rsign(ev, E, c0):
    r = np.prod(ev - np.exp(1j * E), axis=-1) / (np.exp(6j * E) * np.sqrt(c0))
    return bool(r.real.max() > 0 and r.real.min() < 0), float(np.abs(r.imag).max() / max(np.abs(r).max(), 1e-300))
def stageAB(job):
    sk, names = job; w = build(sk, names, PHL); ns = nS(w)
    W0 = Wb(w, kst[None])[0]; e, V = np.linalg.eig(W0); st = collections.Counter(); cand = []
    for E, m in levels(W0):
        if m == 2: Vd = V[:, np.abs(wrap(np.angle(e) - E)) < 1e-6]; Q, _ = np.linalg.qr(Vd); kind = 'D+' if np.linalg.norm(Q.conj().T @ Dp) ** 2 > 1.999 else ('D-' if np.linalg.norm(Q.conj().T @ Dm) ** 2 > 1.999 else '2?')
        elif m == 4:
            Vd = V[:, np.abs(wrap(np.angle(e) - E)) < 1e-6]; Q, _ = np.linalg.qr(Vd)
            kind = 'D+D-' if abs(np.linalg.norm(Q.conj().T @ Dpm) ** 2 - 4) < 1e-6 else 'G'
        else: kind = f'{m}-fold'
        st[kind] += 1
        if kind in ('D+', 'D-', 'D+D-'): cand.append((E, kind))
    if not cand: return (dict(st), [])
    c0 = np.linalg.det(Wb(w, np.zeros((1, 3)))[0])
    ev8 = np.linalg.eigvals(Wb(w, GRID8)); out = []; ev16 = None
    for E, kind in cand:
        f8, ri8 = rsign(ev8, E, c0)
        if f8: out.append(dict(sk=sk, names=names, E=float(E), kind=kind, nS=ns, nR=nR(w), fermi=True, grid=8, rimag=ri8)); continue
        if ev16 is None: ev16 = np.linalg.eigvals(Wb(w, GRID))
        f16, ri16 = rsign(ev16, E, c0)
        out.append(dict(sk=sk, names=names, E=float(E), kind=kind, nS=ns, nR=nR(w), fermi=f16, grid=16, rimag=max(ri8, ri16)))
    return (dict(st), out)
def stageC(rec):
    w = build(rec['sk'], rec['names'], PHL); E = rec['E']; vs = abs(rec['nS']) * np.sqrt(2) / 3
    f = lambda k: float(dist_E(w, np.asarray(k)[None], E)[0])
    d = dist_E(w, GRID, E); ds = dist_E(w, SPEC, E)
    nodes = [k for k, x in zip(SPEC, ds) if x < 1e-7]
    # early reject: classify the (pi/4)Z^3 nodes first; if one is defective, the level fails (no Nelder-Mead search)
    pre = []
    for k in nodes:
        c = classify(w, k, E, vs)
        if c is not None: pre.append((tuple(np.round(k / np.pi, 5)), kclass(k), c[0], c[1], {a: round(b, 6) for a, b in c[2].items()}))
    if any(x[3] != 'ok' for x in pre):
        rec = dict(rec); rec['vs'] = vs; rec['gridmin'] = float(d.min()); rec['nodes'] = pre; rec['early'] = True
        rec['bad'] = [x for x in pre if x[3] != 'ok']; return rec
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
    _k = np.array([0.3, -0.7, 1.1]); _w = ['S', 'Rt', UH, 'S2i', UL, 'Si', 'R']
    W_, G_ = W_grad(_w, _k); h = 1e-6
    fd = [(Wb(_w, (_k + h * np.eye(3)[j])[None])[0] - Wb(_w, (_k - h * np.eye(3)[j])[None])[0]) / (2 * h) for j in range(3)]
    ref = Wword(['S'], _k) @ (A0 @ RLk(_k) @ A0i) @ UH @ Wword(['S2i'], _k) @ UL @ Wword(['Si', 'R'], _k)
    check("batched word (with Rt) == chklib-letter product, analytic gradient == finite difference", np.allclose(W_, ref) and max(np.abs(a - b).max() for a, b in zip(G_, fd)) < 1e-7)
    # reduction / duality sanity on a few words: Rt-word = -(reduced old-palette word); A0-dual has identical spectrum
    from skeletons import dual
    okr = okd = True
    for sk in (ONE[:3] + TWO[:2]):
        nm = tuple(list(PC)[5 + i] for i in range(sk.count('o'))); w = build(sk, nm, PHL)
        wr = []
        for L in w: wr += (['S', 'R', 'Si'] if (isinstance(L, str) and L == 'Rt') else [L])
        sgn = (-1) ** sum(1 for L in w if isinstance(L, str) and L == 'Rt')
        wd = [A0 @ L @ A0i if not isinstance(L, str) else L for L in build(dual(sk), nm, PHL)]
        for k in np.random.default_rng(5).uniform(-np.pi, np.pi, (3, 3)):
            okr &= np.allclose(Wb(w, k[None])[0], sgn * Wb(wr, k[None])[0])
            okd &= np.allclose(np.sort_complex(np.round(np.linalg.eigvals(Wb(w, k[None])[0]), 9)), np.sort_complex(np.round(np.linalg.eigvals(Wb(wd, k[None])[0]), 9)))
    check("Rt-words equal +-(old-palette word with Rt -> S R_L S^-1); A0-dual words (S<->Si, R<->Rt, o -> A0 o A0^-1) are isospectral", okr and okd)
    J = list(jobs(TAG)); print(f"{TAG}: {len(J)} words  ({len(ONE)} one-slot / {len(TWO)} two-slot classes in total)", flush=True)
    with Pool(NP) as p: res = p.map(stageAB, J, chunksize=16)
    stats = collections.Counter(); recs = []
    for st, out in res: stats.update(st); recs.extend(out)
    nf = [r for r in recs if not r['fermi']]
    print(f"  k* level statistics: {dict(stats)}", flush=True)
    print(f"  screened levels {len(recs)} (D+/D-: {sum(r['kind'] != 'D+D-' for r in recs)}, D+D-: {sum(r['kind'] == 'D+D-' for r in recs)}); "
          f"Fermi (8^3): {sum(r['fermi'] and r['grid'] == 8 for r in recs)}, Fermi (16^3 only): {sum(r['fermi'] and r['grid'] == 16 for r in recs)}, survivors: {len(nf)}  [{time.time() - t0:.0f}s]", flush=True)
    check("r(k) real on every grid (det W k-independent)", all(r['rimag'] < 1e-8 for r in recs), f"max {max([r['rimag'] for r in recs], default=0):.1e}")
    with Pool(NP) as p: cres = p.map(stageC, nf, chunksize=1)
    print(f"  stage C: {len(cres)} survivors, early-rejected at (pi/4)Z^3 nodes: {sum(bool(r.get('early')) for r in cres)}", flush=True)
    pickle.dump(dict(tag=TAG, stats=dict(stats), recs=[r for r in recs if r['fermi']] + cres), open(OUT, 'wb'))
    def kst_ok(r):
        want = 4 if r['kind'] == 'D+D-' else 2
        return any(x[1] == 'cube' and abs(np.array(x[0]) - kst / np.pi).max() < 1e-4 and x[3] == 'ok' and x[2] == want for x in r['nodes'])
    ko = [kst_ok(r) for r in cres]
    check("every survivor's k* node is classified an isotropic untilted cone at |n_S| sqrt2/3 (L1 / Dirac lemma sanity of DPT)", all(ko), f"{sum(ko)}/{len(ko)}")
    clean = [r for r in cres if not r['bad']]
    print(f"  {len(clean)} survivors with every found node an isotropic untilted cone at v (screen level)  [{time.time() - t0:.0f}s]")
    for r in clean[:30]: print("   CLEAN-AT-SCREEN:", r['sk'], r['names'], round(r['E'], 4), r['kind'], r['nS'], [(x[0], x[1], x[2]) for x in r['nodes']])
    pat = collections.Counter(); ex = {}
    for r in cres:
        if not r['bad']: continue
        key = (r['sk'], tuple(sorted(set((x[1], x[2], x[3]) for x in r['bad']))))
        pat[key] += 1; ex.setdefault(key, r)
    print("  obstruction pattern among survivors (skeleton, {(point class, multiplicity, defect)}):")
    for key, n in pat.most_common(40):
        r = ex[key]; b = r['bad'][0]
        print(f"   {n:5d} x {key[0]} {list(key[1])[:6]}  e.g. {r['names']} E={r['E']:+.4f} {r['kind']}  first bad: k/pi={b[0]} m={b[2]} {b[3]} {b[4]}")
    def score(r): return (len(r['bad']), min([x[4].get('smax', 9) - x[4].get('smin', 0) for x in r['bad']], default=0))
    print("  best (fewest defective nodes):")
    for r in sorted(cres, key=score)[:10]:
        print("   ", r['sk'], r['names'], f"E={r['E']:+.4f} {r['kind']} nS={r['nS']} nodes={len(r['nodes'])} bad={len(r['bad'])}", [(x[0], x[1], x[2], x[3], x[4].get('smin'), x[4].get('smax'), x[4].get('tilt')) for x in r['bad'][:3]])
    print(f"RESULT {TAG}: words={len(J)} levels={len(recs)} fermi={len(recs) - len(nf)} survivors={len(nf)} clean_at_screen={len(clean)}")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
