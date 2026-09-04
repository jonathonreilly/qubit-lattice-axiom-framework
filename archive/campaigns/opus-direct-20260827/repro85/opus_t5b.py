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
K2 = sp.Matrix(4*N, 4*N, lambda i, j: lin(sum(K[i, k]*K[k, j] for k in range(4*N))))
print("K^2 built to O(eps)", flush=True)
def blk(i0, j0): return sp.Matrix(N, N, lambda p, q: K2[sid[sites[p]]*4+i0, sid[sites[q]]*4+j0])
L0 = blk(0, 0)
L1 = [[blk(1+a, 1+b) for b in range(2)] for a in range(2)]
def lap(s):
    nb = [wrap((s[0]+1,s[1])), wrap((s[0]-1,s[1])), wrap((s[0],s[1]+1)), wrap((s[0],s[1]-1))]
    return sum(prof[n] for n in nb) - 4*prof[s]
prop = True
for p in range(N):
    for q in range(N):
        d00 = sp.expand(L1[0][0][p,q] - L0[p,q]); d11 = sp.expand(L1[1][1][p,q] - L0[p,q])
        if sp.expand(d00-d11) != 0 or sp.expand(L1[0][1][p,q]) != 0 or sp.expand(L1[1][0][p,q]) != 0:
            prop = False
print(f"1. defect (L1 - L0 x I) proportional to delta_ab everywhere : {prop}", flush=True)
print("2. ROW SUMS of the defect vs the discrete curvature -Lap(prof):", flush=True)
ok = True; shown = 0
for p, s in enumerate(sites):
    rs = sp.expand(sum(L1[0][0][p,q] - L0[p,q] for q in range(N)))
    pred = sp.expand(-eps_ * lap(s))
    if sp.expand(rs - pred) != 0: ok = False
    if shown < 5:
        print(f"   s={s}: rowsum={rs}   -eps*Lap={pred}   match={sp.expand(rs-pred)==0}", flush=True); shown += 1
print(f"   ALL {N} SITES match: {ok}", flush=True)
zz = all(sp.expand(sum(L0[p,q] for q in range(N))) == 0 for p in range(N))
print(f"3. control: row sums of the degree-0 (function) operator vanish: {zz}", flush=True)
nz = sum(1 for q in range(N) if sp.expand(L1[0][0][0,q]-L0[0,q]) != 0)
print(f"4. defect row 0 nonzero entries: {nz} (of {N})", flush=True)
