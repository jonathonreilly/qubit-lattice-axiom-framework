#!/usr/bin/env python3
"""B25 part 1c: independent route to Lambda_sp (exact characterisation).
tr W(k)^p = sum_K a_K^(p) e^{i k.K} with integer frequencies K, and tr W(k+t)^p = sum_K a_K^(p) e^{i t.K} e^{i k.K}; spec W(k+t) =
spec W(k) for all k iff tr W(k+t)^p = tr W(k)^p for p = 1..12 iff e^{i t.K} = 1 on every frequency K of every tr W^p.
So Lambda_sp = 2 pi M^*, M = Z-span of the Fourier supports (p <= 12).  Using p <= p_max (alias-free FFT on an N^3 grid) gives
the superlattice D = 2 pi M_{p<=pmax}^* of Lambda_sp, and [D : 2piZ^3] = [Z^3 : M] (Smith form) tells whether D lies on the
(pi/16)Z^3 grid.  Check on census words: D on the grid, D contains the detected Lambda_sp, and D == Lambda_sp in most words
(then the detector, which only scans (pi/8)Z^3, provably missed no finer taste).  Prints PASS/FAIL, TOTAL."""
import sys, os, time, pickle, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b25lib import *
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
ALL.update(PLANE6)
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
def bld(sk, names):
    it = iter(names); return [ALL[next(it)] if L in ('o', 'p', 'q') else L for L in sk]
def kmax(w): return sum(abs(PW[L]) if L != 'R' else 1 for L in w if isinstance(L, str))
def supports(w, pmax, N):
    g = 2 * np.pi * np.arange(N) / N; K = np.array(list(itertools.product(g, repeat=3))); tr = np.zeros((pmax, len(K)), complex)
    for s in range(0, len(K), 8192):
        Wk = Wb(w, K[s:s + 8192]); M = Wk.copy()
        for p in range(pmax):
            tr[p, s:s + 8192] = np.trace(M, axis1=1, axis2=2); M = M @ Wk
    sup = set()
    for p in range(pmax):
        F = np.fft.fftn(tr[p].reshape(N, N, N)) / N ** 3
        for idx in zip(*np.where(np.abs(F) > 1e-9)):
            sup.add(tuple(int(i) if i < N // 2 else int(i) - N for i in idx))
    return sup
def dual(sup):
    Ks = np.array(sorted(sup)); grid16 = np.array(list(itertools.product(range(32), repeat=3)))
    ok = np.all(np.mod(grid16 @ Ks.T, 32) == 0, axis=1)        # t = (pi/16) v:  t.K in 2pi Z  <=>  v.K = 0 mod 32
    D = {tuple(int(c) for c in v) for v in grid16[ok]}
    snf = smith_normal_form(Matrix(Ks.tolist()).T, domain=None) if len(Ks) else None
    d = [abs(snf[i, i]) for i in range(min(snf.shape))] if snf is not None else []
    index = int(np.prod([x for x in d])) if len(d) == 3 and all(x != 0 for x in d) else 0
    return D, index
R = pickle.load(open(os.path.join(HERE, 'census.pkl'), 'rb'))['R']
rnd = random.Random(7); sample = [(j, r) for j, r in R if r and r.get('Lu')]
sample = rnd.sample(sample, 60)
stat = collections.Counter(); bad = []
for j, r in sample:
    w = bld(j[1], j[2]); km = kmax(w)
    pmax = max(1, min(3, 31 // max(km, 1))); N = 64 if pmax * km > 15 else 32
    sup = supports(w, pmax, N); D, idx = dual(sup)
    Ls = LATS[r['Lsp']]
    on_grid = (idx == len(D)); contains = Ls <= D; eq = (D == Ls)
    stat[(on_grid, contains, eq)] += 1
    if not (on_grid and contains): bad.append((j, r['Lsp'], len(D), idx))
print("   (D on grid, D >= Lambda_sp, D == Lambda_sp) ->", dict(stat))
for b in bad[:5]: print("   problem:", b)
check("D = 2pi M*(p <= pmax) lies on the (pi/16)Z^3 grid ([Z^3 : M] = |D|) for every sampled word", all(k[0] for k in stat), f"{sum(v for k, v in stat.items() if k[0])}/{len(sample)}")
check("D contains the detected Lambda_sp for every sampled word (the exact characterisation is consistent with the detector)", all(k[1] for k in stat))
check("D == Lambda_sp (detector complete, no taste finer than (pi/8)Z^3) in at least 90% of sampled words", sum(v for k, v in stat.items() if k[2]) >= 0.9 * len(sample), f"{sum(v for k, v in stat.items() if k[2])}/{len(sample)}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
