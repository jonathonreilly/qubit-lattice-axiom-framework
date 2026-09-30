"""With the staggered Dirac mass m != 0 the covariance group shrinks to elements preserving eps_v
(even translation sum).  Build every covariant pairing invariant of that reduced group, class by
class, and ask what it does to the 8 light modes (energy +-m)."""
import sys, itertools, numpy as np
src = open('verify_and_bdg.py').read().split('print("\\n== step 1')[0].replace('print(', '(lambda *a, **k: None)(')
sys.argv = ['x', sys.argv[1] if len(sys.argv) > 1 else '8']
exec(src)
tx, ty, tz = gens["tx"], gens["ty"], gens["tz"]
mg = {"c4z": gens["c4z"], "c4x": gens["c4x"], "c3": gens["c3"],
      "tx2": compose(tx, tx), "ty2": compose(ty, ty), "tz2": compose(tz, tz),
      "txty": compose(ty, tx), "tytz": compose(tz, ty)}
rots = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for r in range(3): M[r, perm[r]] = signs[r]
        if round(np.linalg.det(M)) == 1: rots.append(M)
def class_of(d):
    orb = set(tuple(int(t) for t in M @ np.array(d)) for M in rots)
    return orb | set(tuple(-t for t in o) for o in orb)
def all_invariants(d, kappa=-1):
    cls = class_of(d)
    nodes = set()
    for i in range(N):
        v = coords(i)
        for dd in cls:
            j = idx(v[0]+dd[0], v[1]+dd[1], v[2]+dd[2])
            if i < j: nodes.add((i, j))
    nodes = sorted(nodes)
    seen = {}
    comps = []
    for start in nodes:
        if start in seen: continue
        val = {start: 1}; stack = [start]; ok = True
        while stack:
            (i, j) = stack.pop()
            for kind, (perm, s) in mg.items():
                pi, pj = int(perm[i]), int(perm[j])
                x = s[i] * s[j] * val[(i, j)]
                key = (pi, pj) if pi < pj else (pj, pi)
                x = x if pi < pj else kappa * x
                if key in val:
                    if val[key] != x: ok = False
                else:
                    val[key] = x; stack.append(key)
        for k in val: seen[k] = True
        if ok: comps.append(val)
    return comps
h = np.zeros((N, N))
for (i, j), e in hop.items(): h[i, j] = e
eps = np.array([(-1) ** (sum(coords(i))) for i in range(N)], dtype=float)
m = 0.3
hm = h + m * np.diag(eps)
print(f"L={L}, m={m}: unperturbed lowest |E| = {np.round(np.sort(np.abs(np.linalg.eigvalsh(hm)))[:3],4)}")
RM = 2 if L == 8 else 3
for d in [(1,0,0),(1,1,1),(2,1,0),(2,2,1),(3,0,0),(3,1,0),(3,1,1),(3,2,0)]:
    comps = all_invariants(d)
    for ci, val in enumerate(comps):
        Delta = np.zeros((N, N))
        for (i, j), x in val.items(): Delta[i, j] = x; Delta[j, i] = -x
        res = []
        for lam in [0.05, 0.1]:
            H = np.block([[hm, lam * Delta], [-lam * Delta, -hm]])
            a = np.sort(np.abs(np.linalg.eigvalsh(H)))
            res.append((round(float(a[0]), 5), round(float(a[15]), 5)))
        print(f"d={d} invariant #{ci}: (lowest, 16th-lowest |E|) at lam=0.05,0.1: {res}   [m = {m}]", flush=True)
