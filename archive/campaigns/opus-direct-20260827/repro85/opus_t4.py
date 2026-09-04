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
eqs = set()
for s in sites:
    for r in sites:
        blk = sp.Matrix(4,4, lambda p,q: sp.cancel(K2[sid[s]*4+p, sid[r]*4+q]))
        if blk.is_zero_matrix: continue
        dev = sp.expand(blk - blk[0,0]*sp.eye(4))
        for p in range(4):
            for q in range(4):
                e = sp.cancel(sp.together(dev[p,q]))
                if e != 0:
                    for f, _ in sp.factor_list(sp.numer(e))[1]:
                        if f.free_symbols & set(mu): eqs.add(sp.expand(f))
print(f"FIBER-SCALARITY demands these irreducible factors vanish ({len(eqs)}):", flush=True)
for e in sorted(eqs, key=lambda z: (len(str(z)), str(z)))[:14]:
    print(f"   0 = {sp.factor(e)}", flush=True)
sol = sp.solve(list(eqs), list(mu), dict=True)
print(f"\nSOLUTIONS of the full system: {sol}", flush=True)
print("\n(interpretation guide: mu_i all equal  => the condition is FLATNESS;")
print(" a nontrivial relation among neighbours => a genuine field equation.)", flush=True)
