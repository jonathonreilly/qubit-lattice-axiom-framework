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

# ---- T8: THE CORRECTED EXTRACTION.  Conjugate into the ORTHONORMAL frame,
# K_hat = D^(1/2) K D^(-1/2), where the operator is genuinely antisymmetric and
# an ON-SITE DIAGONAL is a frame-independent local quantity (the "potential").
# Then the Weitzenbock prediction is sharp:
#   [-K_hat^2]_(ss) on degree 1  minus  the same on degree 0  =  Ric  =  -eps*Lap(s)
Dh = sp.zeros(4*N, 4*N); Dhi = sp.zeros(4*N, 4*N)
for s in sites:
    l = lam[s]
    h = [lin(l), sp.Integer(1), sp.Integer(1), lin(1/l)]      # D^(1/2) per degree
    hi = [lin(1/l), sp.Integer(1), sp.Integer(1), lin(l)]
    for k in range(4):
        Dh[sid[s]*4+k, sid[s]*4+k] = h[k]; Dhi[sid[s]*4+k, sid[s]*4+k] = hi[k]
Kh = sp.Matrix(4*N, 4*N, lambda i, j: lin((Dh*K*Dhi)[i, j]))
anti = sp.Matrix(4*N, 4*N, lambda i, j: lin((Kh + Kh.T)[i, j]))
print(f"orthonormal frame: K_hat antisymmetric : {anti.is_zero_matrix}", flush=True)
M = sp.Matrix(4*N, 4*N, lambda i, j: lin(-sum(Kh[i, k]*Kh[k, j] for k in range(4*N))))
def lap(s):
    nb = [wrap((s[0]+1,s[1])), wrap((s[0]-1,s[1])), wrap((s[0],s[1]+1)), wrap((s[0],s[1]-1))]
    return sum(prof[n] for n in nb) - 4*prof[s]
print("on-site diagonals of -K_hat^2 (orthonormal frame), first order in eps:", flush=True)
ok_ric = True; shown = 0
for s in sites:
    i = sid[s]*4
    d = [sp.expand(M[i+k, i+k]) for k in range(4)]
    ric_meas = sp.expand(d[1] - d[0])          # degree1 - degree0  == Ric ?
    ric_pred = sp.expand(-eps_ * lap(s))
    if sp.expand(ric_meas - ric_pred) != 0: ok_ric = False
    if shown < 6:
        print(f"  s={s}: deg0={d[0]}  deg1={d[1]}  deg2={d[3]}", flush=True)
        print(f"        (deg1-deg0)={ric_meas}   -eps*Lap={ric_pred}   match={sp.expand(ric_meas-ric_pred)==0}", flush=True)
        shown += 1
print(f"ALL SITES  (deg1 - deg0) == -eps*Lap(prof) : {ok_ric}", flush=True)
# also: is the deg1 on-site diagonal isotropic (both 1-form components equal)?
iso = all(sp.expand(M[sid[s]*4+1, sid[s]*4+1] - M[sid[s]*4+2, sid[s]*4+2]) == 0 for s in sites)
print(f"the two 1-form components carry the SAME on-site term (Ric ~ delta_ab in 2D) : {iso}", flush=True)
