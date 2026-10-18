import sympy as sp, itertools, time, sys
# Jet version: h_x = sum_{r<=s} c_rs(e) a_{x+r} a_{x+s}, c_rs = Taylor polynomial of order N in e_t = g_{x+t}-1, t in window
# impose flatness through order N-1 in e, uniform-background normalisation through order N.
Ra, Rg, N = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
dkind = sys.argv[4] if len(sys.argv) > 4 else "cen"
refl = len(sys.argv) > 5 and sys.argv[5] == "refl"
d = {"cen": {1: sp.Rational(1, 2), -1: -sp.Rational(1, 2)},
     "fwd": {1: 1, 0: -1},
     "c2": {1: sp.Rational(2, 3), -1: -sp.Rational(2, 3), 2: -sp.Rational(1, 12), -2: sp.Rational(1, 12)}}[dkind]
rd = max(abs(k) for k in d)
L = 2*(2*Ra+2*Rg+2*rd+2)+3
def Dl(x, y):
    r = (y-x) % L
    if r > L//2: r -= L
    return d.get(r, 0)
a = sp.symbols(f"a0:{L}"); e = sp.symbols(f"e0:{L}")
pairs = [(r, s) for r in range(-Ra, Ra+1) for s in range(r, Ra+1)]
ts = list(range(-Rg, Rg+1))
mons = []
for k in range(N+1):
    for c in itertools.combinations_with_replacement(ts, k):
        mons.append(c)
kap = {}
for (r, s) in pairs:
    for c in mons:
        kap[(r, s, c)] = sp.Symbol("k_%d_%d_" % (r, s) + "_".join(map(str, c)) + "_%d" % len(c))
unk = list(kap.values())
# reflection covariance (x -> -x): a -> ? for chiral a = pi + Delta phi, reflection maps a to b (other chirality); so
# reflection is NOT a symmetry of a single chiral sector; option 'refl' imposes c_rs(e_t) = c_{-s,-r}(e_{-t}) as a test only.
def h(x):
    tot = 0
    for (r, s) in pairs:
        for c in mons:
            m = 1
            for t in c: m *= e[(x+t) % L]
            tot += kap[(r, s, c)]*m*a[(x+r) % L]*a[(x+s) % L]
    return sp.expand(tot)
def pba(f, gg):
    return sp.expand(sum(2*Dl(x, y)*sp.diff(f, a[x])*sp.diff(gg, a[y]) for x in range(L) for y in range(L) if Dl(x, y) != 0))
def du(f, y):
    return sp.expand(sp.diff(f, e[y]))
def trunc(f, n):
    p = sp.Poly(f, *e)
    return sum(cf*sp.prod([v**k for v, k in zip(e, mon)]) for mon, cf in p.terms() if sum(mon) <= n)
eqs = set()
h0 = h(0)
rng = 2*Ra+2*Rg+2*rd+2
t0 = time.time()
for y in range(1, rng+1):
    hy = h(y)
    F = du(h0, y) - du(hy, 0) + pba(h0, hy)
    if F == 0: continue
    F = sp.expand(trunc(sp.expand(F), N-1))
    if F == 0: continue
    gens = [v for v in list(a)+list(e) if F.has(v)]
    for cf in sp.Poly(F, *gens).coeffs():
        eqs.add(sp.expand(cf))
# normalisation along uniform background: sum_rs c_rs(e..e) = 1/(4(1+e)) through order N
norms = []
for k in range(int(__import__("os").environ.get("NK", N))+1):
    norms.append(sp.Symbol("tt")*sum(v for (r, s, c), v in kap.items() if len(c) == k) - 1)
extra = []
if refl:
    for (r, s, c), v in kap.items():
        c2 = tuple(sorted(-t for t in c))
        extra.append(v - kap[(-s, -r, c2)])
eqs = list(eqs)
print("Ra Rg N", Ra, Rg, N, dkind, "refl" if refl else "", "L", L, "unknowns", len(unk), "eqs", len(eqs), "build", round(time.time()-t0, 1))
sys.stdout.flush()
t0 = time.time()
G = sp.groebner(eqs+norms+extra, *(unk+[sp.Symbol("tt")]), order="grevlex")
print("groebner with normalisation:", "[1]" if list(G) == [1] else f"{len(G)} elems", round(time.time()-t0, 1))
if list(G) != [1]:
    sol = sp.solve(list(G), unk, dict=True)
    print("sol", sol[:2])
