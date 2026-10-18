#!/usr/bin/env python3
"""B25 part 2b: B20/B23 criterion screen of the k-dependent-taste family ALIGN2 (no word realises a good pair; this is the
closest unscreened family where Lambda_sp strictly exceeds Lambda_u):
    W = S^a P S^a G S^a P' S^a G,  a in {1, 2, 4},  P = PL(m pi/6), P' = PL(-m pi/6) (m != 0, 6),  G a Clifford letter (PC minus identities).
Stage A/B/C exactly as B24's b24_screen.py (copied library b25lib24.py): k* level exactly 2-fold (D2) or 4-fold D+ (+) D-;
r(k) sign test on 16^3 (24^3 for S^4 words); survivors: nodes at E from (pi/8)Z^3 + Nelder-Mead (B24_NM starts), DPT cone
classification, pass iff every node is an untilted isotropic cone at |n_S| sqrt2/3.  Each node is typed (T / C2 / low / gen)
relative to Lambda_u and to Lambda_sp(E) (rotation tastes w=1 plus level-E reflection tastes).
Usage: screen25.py <power: S|S2|S4|all> [nproc]   (one log/pkl per power; runs fit the 25-min limit on a shared machine)"""
import sys, os, time, pickle, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b25lib import *
from multiprocessing import Pool
ALL.update(PLANE6)
TAG = sys.argv[1] if len(sys.argv) > 1 else 'all'; NP = int(sys.argv[2]) if len(sys.argv) > 2 else 4
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
def jobs():
    G = [n for n in PC if n not in ('H00', 'L000')]
    for a in (('S', 'S2', 'S4') if TAG == 'all' else (TAG,)):
        for m in [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]:
            for g in G: yield (a, 'p', a, 'o', a, 'q', a, 'o'), (f"P{m}", g, f"P{12 - m}", g)
SPEC16 = np.array(list(itertools.product(np.arange(-16, 16) * np.pi / 16, repeat=3)))      # (pi/16)Z^3: 32768 points
def stageC25(rec):
    """early reject: nodes at E on (pi/16)Z^3 classified first (DPT); one defective node rejects the word ('early').
    Otherwise the full B24 stage C (Nelder-Mead node search) is run."""
    w = build24(rec['sk'], rec['names']); E = rec['E']; vs = abs(rec['nS']) * np.sqrt(2) / 3
    A = analyse_word(w); rot, ref = tastes25(w); LsE = lam_sp(rot, ref, E); Lu = LATS[A['Lu']]
    ds = np.concatenate([dist_E(w, SPEC16[i:i + 8192], E) for i in range(0, len(SPEC16), 8192)])
    nodes = []
    cand = SPEC16[ds < 1e-7]; rec = dict(rec); rec['n_grid_nodes'] = len(cand)
    pri = np.array([min(np.abs(wrap(k - kst)).max(), np.abs(wrap(k + kst)).max()) < 1e-9 for k in cand], bool)
    cand = np.concatenate([cand[pri], cand[~pri]])                                     # +-k* classified first
    for k in cand:
        if len(nodes) >= 40 and any(x[3] != 'ok' for x in nodes): break          # enough to reject and to sample the pattern
        c = classify(w, k, E, vs)
        if c is not None: nodes.append((tuple(np.round(k / np.pi, 5)), point_type(k, LATS[A['Lsp']]), c[0], c[1], {a: round(b, 6) for a, b in c[2].items()}))
    bad = [x for x in nodes if x[3] != 'ok']
    if bad:
        r = dict(rec); r.update(vs=vs, nodes=nodes, bad=bad, stage='early')
    else:
        r = stageC(rec); r['stage'] = 'full'
    r['Lu'] = A['Lu']; r['Lsp'] = A['Lsp']; r['LspE'] = lname(LsE); r['kdep'] = A['kdep']
    r['types'] = [(point_type(np.array(x[0]) * np.pi, Lu), point_type(np.array(x[0]) * np.pi, LsE)) for x in r['nodes']]
    r['badtypes'] = [t for t, x in zip(r['types'], r['nodes']) if x[3] != 'ok']
    return r
if __name__ == '__main__':
    t0 = time.time(); good_table()
    J = list(jobs()); print(f"ALIGN2 [{TAG}]: {len(J)} words", flush=True)
    with Pool(NP) as p: res = p.map(stageAB, J, chunksize=16)
    stats = collections.Counter(); recs = []
    for st, out in res:
        if st == 'nS0': stats['nS0'] += 1; continue
        stats.update(st); recs.extend(out)
    nf = [r for r in recs if not r['fermi']]
    print(f"  k* level stats: {dict(stats)}; screened (kind, fermi): {dict(collections.Counter((r['kind'], r['fermi']) for r in recs))}  [{time.time() - t0:.0f}s]", flush=True)
    check("r(k) real on every grid (det W k-independent)", all(r['rimag'] < 1e-8 for r in recs), f"max {max([r['rimag'] for r in recs], default=0):.1e}")
    with Pool(NP) as p: cres = list(p.imap_unordered(stageC25, nf, chunksize=1))
    print('  stage C stages:', dict(collections.Counter(r['stage'] for r in cres)), flush=True)
    pickle.dump(dict(stats=dict(stats), recs=[r for r in recs if r['fermi']] + cres), open(os.path.join(HERE, f'screen25_{TAG}.pkl'), 'wb'))
    kst_ok = [any(abs(wrap(np.array(x[0]) * np.pi - kst)).max() < 1e-4 and x[3] == 'ok' for x in r['nodes']) for r in cres]
    check("DPT sanity: every survivor's k* node is an isotropic untilted cone set at |n_S| sqrt2/3", all(kst_ok), f"{sum(kst_ok)}/{len(cres)}")
    clean = [r for r in cres if not r['bad']]
    print(f"  survivors {len(cres)}; CLEAN: {len(clean)}  [{time.time() - t0:.0f}s]")
    for r in clean: print("   CLEAN:", r['sk'], r['names'], r['E'], r['kind'], r['Lu'], r['LspE'], [(x[0], x[2]) for x in r['nodes']])
    print("  survivors by (Lambda_u, Lambda_sp, Lambda_sp(E), kdep):", dict(collections.Counter((r['Lu'], r['Lsp'], r['LspE'], r['kdep'] > 0) for r in cres)))
    pat = collections.Counter()
    for r in cres:
        for x, t in zip(r['nodes'], r['types']):
            if x[3] != 'ok': pat[(t[0], t[1], x[3], x[2])] += 1
    print("  defective nodes by (type mod Lambda_u, type mod Lambda_sp(E), verdict, multiplicity):", dict(pat.most_common(16)))
    best = sorted(cres, key=lambda r: (len(r['bad']), sum(1 for x in r['bad'] if x[1] == 'gen')))[:10]
    for r in best:
        print(f"   best: {r['sk']} {r['names']} E={r['E']:+.4f} {r['kind']} Lu={r['Lu']} LspE={r['LspE']} nbad={len(r['bad'])} "
              f"bad={[(x[0], tt, x[2], x[3], x[4].get('smin'), x[4].get('smax')) for x, tt in list(zip(r['bad'], r['badtypes']))[:4]]}")
    check("screen ran on every word (A/B) and every survivor (C)", len(cres) == len(nf))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
