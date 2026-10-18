import sys, os, time, collections, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b25lib import *
random.seed(1)
SKS = SKEL1 + SKEL2 + MIX2 + PLSK + list(TSK.values())
names = list(PC) + list(PLANE)
res = collections.Counter(); ex = {}
t0 = time.time()
for sk in SKS:
    for trial in range(12):
        n = [random.choice(names) for L in sk if L in ('o', 'p', 'q')]
        w = build24(sk, tuple(n))
        if nS(w) == 0: continue
        rot, ref = tastes25(w); Ls = lam_sp(rot); nu = lam_u(w, Ls)
        rotm, refm = tastes25(w, -1)
        key = (sk, nu, lname(Ls), len(ref) > 0, any(len(s) > 1 or abs(list(s)[0]) > 1e-4 for s in rot.values()), len(rotm), len(refm))
        res[key] += 1; ex.setdefault(key, n)
for k, v in sorted(res.items(), key=lambda x: str(x[0])): print(k, v, ex[k])
print(time.time() - t0)
