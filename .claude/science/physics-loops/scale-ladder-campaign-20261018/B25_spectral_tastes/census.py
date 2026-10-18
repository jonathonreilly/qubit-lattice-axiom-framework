#!/usr/bin/env python3
"""B25 part 1b: word-level taste census.  For each word: spectral taste lattice Lambda_sp (rotation-type, w = 1) on (pi/8)Z^3,
Lambda_u (largest O-invariant lattice in Lambda_sp with k-independent unitary intertwiners), the kind of every coset of
Lambda_sp / Lambda_u (U, T = k-independent transpose intertwiner, '' = no k-independent intertwiner: k-dependent taste),
reflection-type tastes (spec W(k+t) = w conj spec W(k); level-preserving at E = arg(w)/2 mod pi) and their I/K kind,
and whether (Lambda_u, Lambda_sp) or (Lambda_u, Lambda_sp(E)) is a good pair.
Families: B20 skeletons with R_L (SKEL1, SKEL2) x Clifford; B24 skeletons (MIX2, PLSK, TSK) x Clifford+plane; SKPI6 x pi/6;
designed alignment words (S^a P S^b G S^a P' S^b G, plane P, P'); random 3-4 slot words (S^{+-1,2,4}, R_L, Clifford/plane).
Usage: census.py [nproc]"""
import sys, os, time, collections, random, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b25lib import *
from multiprocessing import Pool
NP = int(sys.argv[1]) if len(sys.argv) > 1 else 4
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
ALL.update(PLANE6)
def bld(sk, names):
    it = iter(names); return [ALL[next(it)] if L in ('o', 'p', 'q') else L for L in sk]
def jobs():
    rnd = random.Random(2025); J = []
    PCn = list(PC); PLn = list(PLANE) + list(PLANE6); CPn = PCn + PLn; P6n = list(P6)
    for sk in SKEL1 + SKEL2:
        for _ in range(30): J.append(('B20R', sk, tuple(rnd.choice(PCn) for L in sk if L == 'o')))
    for sk in MIX2 + PLSK + list(TSK.values()):
        for _ in range(30): J.append(('B24', sk, tuple(rnd.choice(PLn if L in ('p', 'q') else CPn) for L in sk if L in ('o', 'p', 'q'))))
    for sk in SKPI6:
        for _ in range(30): J.append(('PI6', sk, tuple(rnd.choice(P6n) for L in sk if L == 'o')))
    pw = ['S', 'Si', 'S2', 'S2i', 'S4', 'S4i']
    for _ in range(300):
        a, b = rnd.choice(pw), rnd.choice(pw)
        J.append(('ALIGN', (a, 'p', b, 'o', a, 'q', b, 'o'), (rnd.choice(PLn), rnd.choice(PCn), rnd.choice(PLn), rnd.choice(PCn))))
    for _ in range(100):
        a = rnd.choice(pw); g = rnd.choice(PCn)
        J.append(('ALIGN2', (a, 'p', a, 'o', a, 'q', a, 'o'), (rnd.choice(PLn), g, rnd.choice(PLn), g)))
    for _ in range(400):
        m = rnd.choice([3, 4]); sk = []
        for i in range(m):
            sk.append(rnd.choice(pw + ['R'] if i else pw)); sk.append('o')
        J.append(('RAND', tuple(sk), tuple(rnd.choice(CPn) for L in sk if L == 'o')))
    return J
def run(job):
    fam, sk, names = job; w = bld(sk, names)
    if nS(w) == 0: return (job, None)
    try: return (job, analyse_word(w))
    except Exception as e: return (job, dict(err=repr(e)))
if __name__ == '__main__':
    t0 = time.time(); good_table()
    J = jobs(); print(f"{len(J)} words", flush=True)
    with Pool(NP) as p: R = p.map(run, J, chunksize=4)
    R = [(j, r) for j, r in R if r is not None]
    pickle.dump(R, open(os.path.join(HERE, 'census.pkl'), 'wb'))
    errs = [r for j, r in R if 'err' in r]; print("errors:", len(errs), errs[:3])
    named = [(j, r) for j, r in R if 'err' not in r and r['Lu'] is not None]
    check("every word's Lambda_sp is a group of the sc/fcc/bcc list (rotation-invariant lattice)", len(named) == len(R) - len(errs), f"{len(named)}/{len(R)}")
    pairs = collections.Counter(); exm = {}
    for j, r in named:
        key = (j[0], r['Lu'], r['Lsp'], r['index'], tuple(sorted(r['kinds'].items())))
        pairs[key] += 1; exm.setdefault(key, (j[1], j[2]))
    for k in sorted(pairs, key=str): print("  ", k, pairs[k], exm[k])
    idx = collections.Counter(r['index'] for j, r in named)
    print("index [Lambda_sp : Lambda_u] distribution:", dict(idx))
    kd = [(j, r) for j, r in named if r['kdep'] > 0]
    print(f"words with k-dependent (no k-independent U/T intertwiner) rotation tastes: {len(kd)}")
    for j, r in kd[:15]: print("   kdep:", j, r['Lu'], r['Lsp'], dict(r['kinds']))
    check("index lemma, numerically: whenever every coset has a k-independent U/T intertwiner, [Lambda_sp : Lambda_u] <= 2",
          all(r['index'] <= 2 for j, r in named if r['kdep'] == 0), f"max index among such words {max([r['index'] for j, r in named if r['kdep'] == 0], default=0)}")
    gd = [(j, r) for j, r in named if r['good']]
    gE = [(j, r, x) for j, r in named for x in r['refl'] if x[2]]
    print(f"GOOD (Lambda_u, Lambda_sp) pairs: {len(gd)}; good with reflection tastes at their E: {len(gE)}")
    for j, r in gd[:20]: print("   GOOD:", j, r)
    for j, r, x in gE[:20]: print("   GOOD(E):", j, r['Lu'], x)
    refl = collections.Counter((j[0], x[3], x[1] == r['Lsp']) for j, r in named for x in r['refl'])
    print("reflection tastes (family, I/K kind found, Lambda_sp(E) == Lambda_sp):", dict(refl))
    pickle.dump(dict(R=R), open(os.path.join(HERE, 'census.pkl'), 'wb'))
    check("census ran on every word", len(R) > 0 and not errs)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
