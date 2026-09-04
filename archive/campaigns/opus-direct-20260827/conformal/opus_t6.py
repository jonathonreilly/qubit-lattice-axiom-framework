"""T5 — THE CURVATURE COUPLING, extracted by linearisation.
Continuum fact: for the Kahler-Dirac operator D = d + delta, D^2 is the Hodge
Laplacian, and Weitzenbock says  D^2 = nabla*nabla + W  with W = 0 on
0-forms and W = Ric on 1-forms.  So if this framework's rule really is that
operator, then ITS OWN SQUARE MUST CONTAIN THE RICCI CURVATURE on the
degree-1 sector, with no extra postulate.
TEST: 2D conformal lam = 1 + eps*s(x), work to FIRST ORDER in eps (exact).
Predicted linearised Ricci for g = lam^2 delta in 2D:  Ric_ab = -(Lap s) delta_ab * eps.
Compare with the measured  L1 - L0 (x) I  from K^2."""
import sympy as sp
B2 = [(), (0,), (1,), (0, 1)]; IDX = {b: i for i, b in enumerate(B2)}
eps_ = sp.Symbol("epsilon")
def lin(e): return sp.expand(sp.series(sp.expand(e), eps_, 0, 2).removeO())
def epsm(a):
    M = sp.zeros(4, 4)
    for Sx in B2:
        if a in Sx: continue
        T = tuple(sorted(Sx + (a,)))
        M[IDX[T], IDX[Sx]] = (-1) ** sum(1 for i in Sx if i < a)
    return M
def iota(a, gi):
    M = sp.zeros(4, 4)
    for Sx in B2:
        for pos, i in enumerate(Sx):
            T = tuple(x for x in Sx if x != i)
            M[IDX[T], IDX[Sx]] += (-1) ** pos * gi[a, i]
    return M
L = 6; N = L * L
sites = [(x, y) for x in range(L) for y in range(L)]
sid = {s: i for i, s in enumerate(sites)}
def wrap(s): return (s[0] % L, s[1] % L)
# a non-trivial rational profile with zero mean, varying in BOTH directions
prof = {}
for (x, y) in sites:
    prof[(x, y)] = sp.Rational(((x * x + 2 * y) % 5) - 2, 3)
lam = {s: 1 + eps_ * prof[s] for s in sites}
def Gam(s, a):
    gi = sp.eye(2) * lin(1 / lam[s] ** 2)
    return sp.Matrix(4, 4, lambda p, q: lin((epsm(a) + iota(a, gi))[p, q]))
def U(s, r):
    q = lin(lam[r] / lam[s]); qi = lin(lam[s] / lam[r])
    return sp.diag(q, sp.Integer(1), sp.Integer(1), qi)
def Lam(s, r, a):
    Us = U(s, r)
    return sp.Matrix(4, 4, lambda p, q: lin((sp.Rational(1,2)*(Gam(s,a)*Us + Us*Gam(r,a)))[p, q]))
K = sp.zeros(4*N, 4*N)
for s in sites:
    for a in range(2):
        for sgn, r in ((+1, wrap((s[0]+(a==0), s[1]+(a==1)))), (-1, wrap((s[0]-(a==0), s[1]-(a==1))))):
            blk = Lam(s, r, a); i, j = sid[s]*4, sid[r]*4
            for p in range(4):
                for q in range(4): K[i+p, j+q] += sgn * sp.Rational(1,2) * blk[p, q]
K = sp.Matrix(4*N, 4*N, lambda i, j: lin(K[i, j]))

# ---- T6: DO RECORD WEIGHTS RESPOND TO CURVATURE?
# Q = m + K on the variable-metric carrier.  W9-style weights at a site are the
# normalised diagonal of the hermitian part of the ON-SITE block of Q^-1 --
# a probability over the exterior degrees, which is the record's possibility
# space here.  Linearise in eps and ask what the shift tracks.
m = sp.Rational(1, 2)
Q = sp.Matrix(4*N, 4*N, lambda i, j: sp.expand((m if i == j else 0) + K[i, j]))
Q0 = sp.Matrix(4*N, 4*N, lambda i, j: sp.expand(Q[i, j].subs(eps_, 0)))
Q1 = sp.Matrix(4*N, 4*N, lambda i, j: sp.expand(sp.diff(Q[i, j], eps_)))
print("inverting the flat operator ...", flush=True)
Q0i = Q0.inv()
print("first-order inverse ...", flush=True)
Qi1 = sp.expand(-Q0i * Q1 * Q0i)
def lap(s):
    nb = [wrap((s[0]+1,s[1])), wrap((s[0]-1,s[1])), wrap((s[0],s[1]+1)), wrap((s[0],s[1]-1))]
    return sum(prof[n] for n in nb) - 4*prof[s]
rows = []
for s in sites:
    i = sid[s]*4
    d0 = [sp.expand(sp.Rational(1,2)*(Q0i[i+k, i+k] + Q0i[i+k, i+k])) for k in range(4)]
    d1 = [sp.expand(sp.Rational(1,2)*(Qi1[i+k, i+k] + Qi1[i+k, i+k])) for k in range(4)]
    t0 = sum(d0); t1 = sum(d1)
    # W9_k = d_k / t  ;  first order shift
    shift = [sp.cancel(d1[k]/t0 - d0[k]*t1/t0**2) for k in range(4)]
    rows.append((s, shift))
print("first-order record-weight shifts computed", flush=True)
import itertools
# candidate explanatory variables
def col(f): return [f(s) for s, _ in rows]
cands = {"prof (the conformal factor itself)": col(lambda s: prof[s]),
         "Lap prof (the curvature)": col(lambda s: lap(s))}
for k in range(4):
    y = [sh[k] for _, sh in rows]
    print(f"\n degree-{k} weight shift:", flush=True)
    for nm, x in cands.items():
        num = [sp.cancel(yy/xx) for yy, xx in zip(y, x) if xx != 0]
        const = len(set(map(sp.simplify, num))) == 1 if num else False
        print(f"    proportional to {nm}? {const}"
              + (f"   ratio = {sp.simplify(num[0])}" if const and num else ""), flush=True)
    nz = [str(sp.simplify(v)) for v in y[:4]]
    print(f"    sample values: {nz}", flush=True)
