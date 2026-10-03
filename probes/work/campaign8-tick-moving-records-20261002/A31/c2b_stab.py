"""A31 c2b: which 24 space-group cosets stabilize the most symmetric period-2 pi-flux sign pattern?"""
import signal, itertools, numpy as np
signal.alarm(55)
exec(open('c2_patterns.py').read().split('# (3) largest exact stabilizer')[0].split('# annealing over all')[0])
cos = [(M, t) for M in rots for t in itertools.product([0,1], repeat=3)]
perms = [np.array([bond_image(M,t,b) for b in bonds]) for M,t in cos]
res = []
for e in p2:
    st = [c for c,pm in enumerate(perms) if np.array_equal(e[np.argsort(pm)], e)]
    res.append((len(st), st, e))
res.sort(key=lambda r: -r[0])
n, st, e = res[0]
print("best stabilizer size:", n)
# describe: for each coset, the rotation (as signed permutation), the offset t, and whether it fixes some site/point
for c in st:
    M, t = cos[c]
    # fixed point p of x -> Mx + t (mod 2): solve (1-M)p = t mod 2 over half-integers
    fp = None
    for p in itertools.product([0,0.5,1,1.5], repeat=3):
        q = M @ np.array(p) + np.array(t) - np.array(p)
        if np.allclose(np.mod(q, 2), 0): fp = p; break
    print(f"  M={M.tolist()} t={t} fixed point mod 2: {fp}")
print("site sums of this pattern:", sorted(set(site_sums(e).tolist())))
print("KS site sums:", sorted(set(site_sums(eta_ks).tolist())))
# how many cosets keep the pattern up to a global sign flip (eta -> -eta keeps every flux)?
st2 = [c for c,pm in enumerate(perms) if np.array_equal(-e[np.argsort(pm)], e)]
print("cosets mapping it to minus itself:", len(st2))
