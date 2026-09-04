"""T4 — THE FIELD-EQUATION PROBE.  For CONSTANT g the rule's square is exactly
a scalar Laplacian times the identity on the fiber (verified in T2): the
Clifford structure cancels.  For a VARIABLE metric it does not.  DEMAND that it
still does — that the propagator's square stay fiber-scalar, i.e. that the rule
propagate without mixing exterior degrees — and read off what that demands of
the metric field.  If the answer is a nontrivial local equation, it is a
candidate FIELD EQUATION derived from the rule's own consistency.
Test bed: 2D conformal g = lam^2 I, lam depending on x only, L = 4 periodic,
symbolic lam.  Rational throughout."""
import sympy as sp
B2 = [(), (0,), (1,), (0, 1)]; IDX = {b: i for i, b in enumerate(B2)}
def eps(a):
    M = sp.zeros(4, 4)
    for Sx in B2:
        if a in Sx: continue
        T = tuple(sorted(Sx + (a,)))
        M[IDX[T], IDX[Sx]] = (-1) ** sum(1 for i in Sx if i < a)
    return M
def iota(a, ginv):
    M = sp.zeros(4, 4)
    for Sx in B2:
        for pos, i in enumerate(Sx):
            T = tuple(x for x in Sx if x != i)
            M[IDX[T], IDX[Sx]] += (-1) ** pos * ginv[a, i]
    return M
L = 4; N = L * L
sites = [(x, y) for x in range(L) for y in range(L)]
sid = {s: i for i, s in enumerate(sites)}
def wrap(s): return (s[0] % L, s[1] % L)
mu = sp.symbols("m0:4", positive=True)
lam = {s: mu[s[0]] for s in sites}          # lam depends on x only
def Ds(s):
    l = lam[s]; return sp.diag(l**2, sp.Integer(1), sp.Integer(1), l**-2)
def Gam(s, a): return sp.Matrix(sp.expand(eps(a) + iota(a, sp.eye(2) / lam[s]**2)))
def U(s, r):
    q = lam[r] / lam[s]; return sp.diag(q, sp.Integer(1), sp.Integer(1), 1/q)
def Lam(s, r, a):
    Us = U(s, r); return sp.Rational(1,2) * (Gam(s, a) * Us + Us * Gam(r, a))
K = sp.zeros(4*N, 4*N)
def put(blk, s, r, sgn):
    i, j = sid[s]*4, sid[r]*4
    for p in range(4):
        for q in range(4): K[i+p, j+q] += sgn * blk[p, q]
for s in sites:
    for a in range(2):
        rp = wrap((s[0]+(a==0), s[1]+(a==1))); rm = wrap((s[0]-(a==0), s[1]-(a==1)))
        put(sp.Rational(1,2)*Lam(s, rp, a), s, rp, +1)
        put(sp.Rational(1,2)*Lam(s, rm, a), s, rm, -1)
K2 = sp.expand(K*K)
polys = set()
for s in sites:
    for r in sites:
        blk = sp.Matrix(4,4, lambda p,q: sp.cancel(K2[sid[s]*4+p, sid[r]*4+q]))
        if blk.is_zero_matrix: continue
        dev = sp.expand(blk - blk[0,0]*sp.eye(4))
        for p in range(4):
            for q in range(4):
                e = sp.cancel(sp.together(dev[p,q]))
                if e != 0:
                    polys.add(sp.expand(sp.numer(e)))
polys = {p for p in polys if p.free_symbols & set(mu)}
print(f"distinct numerator conditions: {len(polys)}", flush=True)
# scale fixing: overall conformal scale
polys1 = {sp.expand(p.subs(mu[0], 1)) for p in polys}
polys1 = {p for p in polys1 if p != 0}
print(f"after fixing m0 = 1: {len(polys1)} conditions in {sorted({str(s) for p in polys1 for s in p.free_symbols})}", flush=True)
const_ok = all(sp.simplify(p.subs({m: 1 for m in mu})) == 0 for p in polys)
print(f"SANITY — the constant metric satisfies every condition: {const_ok}", flush=True)
G = sp.groebner(sorted(polys1, key=str), mu[1], mu[2], mu[3], order="lex")
print(f"\nGROEBNER BASIS (lex) of the fiber-scalarity ideal, m0 = 1:", flush=True)
for g_ in G.exprs:
    print(f"   {sp.factor(g_)}", flush=True)
sol = sp.solve(list(G.exprs), [mu[1], mu[2], mu[3]], dict=True)
print(f"\nsolutions: {sol}", flush=True)
pos = [s for s in sol if all(sp.simplify(v).is_real is not False for v in s.values())]
print(f"real solutions: {pos}", flush=True)
