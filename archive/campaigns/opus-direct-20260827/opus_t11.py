"""T11 — IS IT REALLY CURVATURE?  The decisive non-conformal test.
A CONFORMAL perturbation cannot distinguish a genuine curvature coupling from
a trace-of-the-perturbation artefact, because for lam = 1+eps*s both equal
Lap(s) up to a constant.  So perturb ANISOTROPICALLY:
       g = diag( (1+eps*a)^2 , 1 )     h_11 = 2a, h_22 = 0
Linearised curvature in 2D:  R = d_a d_b h_ab - Lap(tr h) = -2 * d_y^2 a.
   CURVATURE prediction :  potential = R/8      = -(1/4) d_y^2 a
   TRACE-ARTEFACT       :  potential = -(1/4) Lap a = -(1/4)(d_x^2 + d_y^2) a
They differ by -(1/4) d_x^2 a, so a profile with nonzero d_x^2 separates them."""
import sympy as sp
BAS = [(), (0,), (1,), (0,1)]; IDX = {b:i for i,b in enumerate(BAS)}
eps_ = sp.Symbol("epsilon")
def lin(e): return sp.expand(sp.series(sp.expand(e), eps_, 0, 2).removeO())
def epsm(a):
    M = sp.zeros(4,4)
    for Sx in BAS:
        if a in Sx: continue
        T = tuple(sorted(Sx+(a,))); M[IDX[T], IDX[Sx]] = (-1)**sum(1 for i in Sx if i < a)
    return M
def iota(a, gi):
    M = sp.zeros(4,4)
    for Sx in BAS:
        for pos,i in enumerate(Sx):
            T = tuple(x for x in Sx if x != i); M[IDX[T], IDX[Sx]] += (-1)**pos * gi[a,i]
    return M
L = 5; N = L*L
sites = [(x,y) for x in range(L) for y in range(L)]
sid = {s:i for i,s in enumerate(sites)}
def wrap(s): return (s[0]%L, s[1]%L)
# profile with BOTH second derivatives nonzero
prof = {(x,y): sp.Rational(((x*x + 3*y*y) % 7) - 3, 4) for (x,y) in sites}
al = {s: 1 + eps_*prof[s] for s in sites}; be = {s: sp.Integer(1) for s in sites}
def Ddiag(s):
    a_, b_ = al[s], be[s]
    return [lin(a_*b_), lin(b_/a_), lin(a_/b_), lin(1/(a_*b_))]
def Gam(s, a):
    gi = sp.diag(lin(1/al[s]**2), lin(1/be[s]**2))
    return sp.Matrix(4,4, lambda p,q: lin((epsm(a)+iota(a,gi))[p,q]))
def Utrans(s, r):
    ds, dr = Ddiag(s), Ddiag(r)
    return sp.diag(*[lin(sp.sqrt(sp.cancel(dr[k]/ds[k]))) for k in range(4)])
def Lam(s, r, a):
    Us = Utrans(s, r)
    return sp.Matrix(4,4, lambda p,q: lin((sp.Rational(1,2)*(Gam(s,a)*Us + Us*Gam(r,a)))[p,q]))
K = sp.zeros(4*N, 4*N)
for s in sites:
    for a in range(2):
        rp = wrap((s[0]+(a==0), s[1]+(a==1))); rm = wrap((s[0]-(a==0), s[1]-(a==1)))
        for sgn, r in ((+1, rp), (-1, rm)):
            blk = Lam(s, r, a); i, j = sid[s]*4, sid[r]*4
            for p in range(4):
                for q in range(4): K[i+p, j+q] += sgn*sp.Rational(1,2)*blk[p,q]
K = sp.Matrix(4*N, 4*N, lambda i,j: lin(K[i,j]))
Dh = sp.zeros(4*N,4*N); Dhi = sp.zeros(4*N,4*N)
for s in sites:
    dd = Ddiag(s)
    for k in range(4):
        h = lin(sp.sqrt(dd[k])); Dh[sid[s]*4+k, sid[s]*4+k] = h; Dhi[sid[s]*4+k, sid[s]*4+k] = lin(1/h)
Kh = sp.Matrix(4*N,4*N, lambda i,j: lin((Dh*K*Dhi)[i,j]))
print(f"anisotropic: K_hat antisymmetric: {sp.Matrix(4*N,4*N, lambda i,j: lin((Kh+Kh.T)[i,j])).is_zero_matrix}", flush=True)
M = sp.Matrix(4*N,4*N, lambda i,j: lin(-sum(Kh[i,k]*Kh[k,j] for k in range(4*N))))
def d2(s, ax):
    e = (1,0) if ax==0 else (0,1)
    return prof[wrap((s[0]+e[0], s[1]+e[1]))] + prof[wrap((s[0]-e[0], s[1]-e[1]))] - 2*prof[s]
degind = all(sp.expand(M[sid[s]*4+k, sid[s]*4+k] - M[sid[s]*4, sid[s]*4]) == 0 for s in sites for k in range(4))
print(f"anisotropic: on-site term still degree-independent: {degind}", flush=True)
print("site  measured-1st-order   R/8 = -(1/4)dyy   trace = -(1/4)(dxx+dyy)", flush=True)
cur_ok = tr_ok = True
for s in sites:
    c = sp.expand(sp.diff(M[sid[s]*4, sid[s]*4], eps_))
    curv = sp.expand(-sp.Rational(1,4)*d2(s,1))
    trac = sp.expand(-sp.Rational(1,4)*(d2(s,0)+d2(s,1)))
    if sp.expand(c-curv) != 0: cur_ok = False
    if sp.expand(c-trac) != 0: tr_ok = False
for s in sites[:6]:
    c = sp.expand(sp.diff(M[sid[s]*4, sid[s]*4], eps_))
    print(f" {s}  {c}    {sp.expand(-sp.Rational(1,4)*d2(s,1))}    {sp.expand(-sp.Rational(1,4)*(d2(s,0)+d2(s,1)))}", flush=True)
print(f"MATCHES CURVATURE R/8 at every site: {cur_ok}", flush=True)
print(f"MATCHES trace artefact at every site: {tr_ok}", flush=True)
# if neither, fit the general local 2nd-order form  p*dxx + q*dyy + r*prof
p_, q_, r_ = sp.symbols("p_ q_ r_")
rows = [(s, sp.expand(sp.diff(M[sid[s]*4, sid[s]*4], eps_))) for s in sites]
eqs = [sp.Eq(p_*d2(s,0)+q_*d2(s,1)+r_*prof[s], c) for s,c in rows[:3]]
sol = sp.solve(eqs, [p_,q_,r_], dict=True)
if sol:
    P,Q,R_ = sol[0][p_], sol[0][q_], sol[0][r_]
    ok = all(sp.expand(c-(P*d2(s,0)+Q*d2(s,1)+R_*prof[s])) == 0 for s,c in rows)
    print(f"general local fit: {P}*dxx + {Q}*dyy + {R_}*prof ; holds everywhere: {ok}", flush=True)
