"""Exact: the law with vacancies at the neutral scale c0 = 6/(p+q+4r) (pair weight = the rule's one-neighbour probability over the uniform
probability).  Claim: on a window WITHOUT a cycle the occupancy is independent from site to site (Bernoulli 6z/(1+6z)) — records do not
attract; on a window WITH a cycle they do; away from c0 they attract or repel even on a tree, with an effective bond attraction c/c0."""
from fractions import Fraction
from itertools import product
M6 = range(6)
def law(sites, edges, p, q, r, c, z):
    W = [[Fraction(c) * (Fraction(p) if a == b else Fraction(q) if a == (b ^ 1) else Fraction(r)) for b in M6] for a in M6]
    out = {}
    for cfg in product([None] + list(M6), repeat=len(sites)):
        w = Fraction(1)
        for v in cfg:
            if v is not None: w *= z
        for a, b in edges:
            if cfg[a] is not None and cfg[b] is not None: w *= W[cfg[a]][cfg[b]]
        occ = tuple(v is not None for v in cfg); out[occ] = out.get(occ, 0) + w
    Z = sum(out.values()); return {k: v / Z for k, v in out.items()}
def report(name, sites, edges, p, q, r, c, z):
    L = law(sites, edges, p, q, r, c, z); n = len(sites)
    dens = [sum(v for k, v in L.items() if k[i]) for i in range(n)]
    indep = all(L[k] == _prod(dens[i] if k[i] else 1 - dens[i] for i in range(n)) for k in L)
    a, b = edges[0]; cov = sum(v for k, v in L.items() if k[a] and k[b]) - dens[a] * dens[b]
    print(f"{name:<10} c = {str(c):<5} density at site 0 = {dens[0]} (6z/(1+6z) = {6*z/(1+6*z)}); occupancy independent: {indep}; covariance of neighbouring occupancies = {cov} = {float(cov):+.6f}")
def _prod(it):
    o = Fraction(1)
    for t in it: o *= t
    return o
p, q, r = 3, 1, 2; c0 = Fraction(6, p + q + 4 * r); z = Fraction(1, 12)
path = ([0, 1, 2], [(0, 1), (1, 2)]); star = ([0, 1, 2, 3], [(0, 1), (0, 2), (0, 3)]); plaq = ([0, 1, 2, 3], [(0, 1), (1, 2), (2, 3), (3, 0)])
for c in (c0, Fraction(1), Fraction(1, 4)):
    report("path of 3", *path, p, q, r, c, z); report("star of 4", *star, p, q, r, c, z); report("plaquette", *plaq, p, q, r, c, z)
W0 = [[c0 * (p if a == b else q if a == (b ^ 1) else r) for b in M6] for a in M6]
print("at c0 the pair weight is 6 x the rule's one-neighbour probability:", all(W0[a][b] == 6 * Fraction(p if a == b else q if a == (b ^ 1) else r, p + q + 4 * r) for a in M6 for b in M6), "; rows sum to 6:", all(sum(W0[a]) == 6 for a in M6))
