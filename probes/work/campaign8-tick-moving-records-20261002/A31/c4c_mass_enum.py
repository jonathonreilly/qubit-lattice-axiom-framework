"""A31 c4c: exhaustive check. Every pi-flux sign pattern whose axis-a sign does not depend on the
coordinate along a is period-2 in the transverse coordinates (ratio argument in the report), so
enumerating the 2^12 period-2 tables is complete. Count those with pi flux everywhere, and among them
those with |site sum| constant (so that bond dimerization moves no site sum)."""
import itertools, numpy as np
E = [(1,0,0),(0,1,0),(0,0,1)]
par = list(itertools.product([0,1], repeat=3))
def eta(T, s, a):
    o = [s[i] % 2 for i in range(3) if i != a]; return T[a][o[0]*2 + o[1]]
npi = 0; good = 0; sumsets = set()
for bits in itertools.product([1,-1], repeat=12):
    T = [bits[0:4], bits[4:8], bits[8:12]]
    ok = True
    for s in par:
        for a,b in [(0,1),(1,2),(0,2)]:
            sa = tuple(s[i] + E[a][i] for i in range(3)); sb = tuple(s[i] + E[b][i] for i in range(3))
            if eta(T,s,a)*eta(T,sa,b)*eta(T,sb,a)*eta(T,s,b) != -1: ok = False; break
        if not ok: break
    if not ok: continue
    npi += 1
    sums = tuple(sorted(set(sum(eta(T,s,a) + eta(T,tuple(s[i]-E[a][i] for i in range(3)),a) for a in range(3)) for s in par)))
    sumsets.add(sums)
    if len(sums) == 1: good += 1
print(f"pi-flux patterns with axis-independent signs (period 2): {npi}; site-sum sets: {sorted(sumsets)}; constant: {good}")
