import sympy as sp, itertools, time, sys
# Flatness through order N-1 with top-order (order N) coefficients eliminated linearly (numeric matrix), then Groebner.
A0, A1, U0, U1, N = map(int, sys.argv[1:6]); mode = sys.argv[6]
cont1 = "cont1" in sys.argv
d = {1: sp.Rational(1, 2), -1: -sp.Rational(1, 2)}
span = (A1-A0)*2 + (U1-U0) + 6 + max(abs(A0), abs(A1), abs(U0), abs(U1))
L = 2*span + 3
def Dl(i, j):
    r = (j-i) % L
    if r > L//2: r -= L
    return d.get(r, 0)
a = sp.symbols(f"a0:{L}"); w = sp.symbols(f"w0:{L}")
pairs = [(r, s) for r in range(A0, A1+1) for s in range(r, A1+1)]
ts = list(range(U0, U1+1))
mons = [c for k in range(N+1) for c in itertools.combinations_with_replacement(ts, k)]
kap = {(r, s, c): sp.Symbol("k_%d_%d_" % (r, s) + "_".join(map(str, c)) + "_%d" % len(c)) for (r, s) in pairs for c in mons}
top = [v for (r, s, c), v in kap.items() if len(c) == N]
low = [v for (r, s, c), v in kap.items() if len(c) < N]
tt = sp.Symbol("tt")
def h(x): return sp.expand(sum(v*sp.prod([w[(x+t) % L] for t in c])*a[(x+r) % L]*a[(x+s) % L] for (r, s, c), v in kap.items()))
def pba(F, G): return sp.expand(sum(2*Dl(i, j)*sp.diff(F, a[i])*sp.diff(G, a[j]) for i in range(L) for j in range(L) if Dl(i, j) != 0))
def du(F, y):
    if mode == "g": return sp.expand(sum(Dl(z, y)*sp.diff(F, w[z]) for z in range(L) if Dl(z, y) != 0))
    return sp.expand(sp.diff(F, w[y]))
def trunc(F, n):
    if F == 0: return F
    p = sp.Poly(F, *w)
    return sp.expand(sum(cf*sp.prod([v**k for v, k in zip(w, mon)]) for mon, cf in p.terms() if sum(mon) <= n))
eqs = []; h0 = h(0); t0 = time.time()
for y in range(1, span+1):
    F = trunc(du(h0, y) - du(h(y), 0) + pba(h0, h(y)), N-1)
    if F == 0: continue
    eqs += sp.Poly(F, *[v for v in list(a)+list(w) if F.has(v)]).coeffs()
if mode == "shift":
    sh = sp.expand(sum(sp.diff(h0, w[t % L]) for t in ts))
    if sh != 0: eqs += sp.Poly(sh, *[v for v in list(a)+list(w) if sh.has(v)]).coeffs()
print("built", len(eqs), "eqs", time.time()-t0); sys.stdout.flush()
# split: eqs containing top unknowns (linear in them, numeric coefficients)
withtop = [e for e in eqs if any(e.has(v) for v in top)]
notop = [e for e in eqs if not any(e.has(v) for v in top)]
M = sp.Matrix([[sp.diff(e, v) for v in top] for e in withtop])
assert all(x.is_number for x in M)
b = [sp.expand(e - sum(M[i, j]*top[j] for j in range(len(top)))) for i, e in enumerate(withtop)]
Nl = M.T.nullspace()
conds = [sp.expand(sum(n[i]*b[i] for i in range(len(b)))) for n in Nl]
conds = [c for c in conds if c != 0]
S0 = sum(v for (r, s, c), v in kap.items() if len(c) == 0)
norms = [tt*S0 - 1]
if cont1: norms.append(sum(t*v for (r, s, c), v in kap.items() if len(c) == 1 for t in c) + S0)
allc = notop + conds + norms
used = sorted(set().union(*[c.free_symbols for c in allc]), key=str)
print("top", len(top), "rank", M.rank(), "conditions", len(conds), "low unknowns used", len(used), time.time()-t0); sys.stdout.flush()
G = sp.groebner(allc, *used, order="grevlex")
print(f"a-win [{A0},{A1}] u-win [{U0},{U1}] flat through order {N-1} {mode} {'cont1' if cont1 else ''}:",
      "[1] OBSTRUCTION" if list(G) == [1] else f"consistent ({len(G)} elems)", f"{time.time()-t0:.0f}s")
