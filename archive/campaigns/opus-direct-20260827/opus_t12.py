"""T12 — THE FULL EFFECTIVE OPERATOR ON SLOWLY VARYING MODES.
Result 9 showed the ON-SITE potential is not a tensor.  The full operator also
has two-step terms.  The curvature, if present, must live in the COMBINATION.
Extract it the invariant way: apply -K_hat^2 to a plane-wave test field of
small momentum q and read the O(q^0) part of the response — that is the true
effective potential, hops included.  Then test it against the linearised
scalar curvature   R = d_a d_b h_ab - Lap(tr h)   for an ANISOTROPIC h."""
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
prof = {(x,y): sp.Rational(((x*x + 3*y*y) % 7) - 3, 4) for (x,y) in sites}
al = {s: 1 + eps_*prof[s] for s in sites}; be = {s: sp.Integer(1) for s in sites}
def Ddiag(s):
    a_, b_ = al[s], be[s]; return [lin(a_*b_), lin(b_/a_), lin(a_/b_), lin(1/(a_*b_))]
def Gam(s, a):
    gi = sp.diag(lin(1/al[s]**2), lin(1/be[s]**2))
    return sp.Matrix(4,4, lambda p,q: lin((epsm(a)+iota(a,gi))[p,q]))
def Utrans(s, r):
    ds, dr = Ddiag(s), Ddiag(r); return sp.diag(*[lin(sp.sqrt(sp.cancel(dr[k]/ds[k]))) for k in range(4)])
def Lam(s, r, a):
    Us = Utrans(s, r); return sp.Matrix(4,4, lambda p,q: lin((sp.Rational(1,2)*(Gam(s,a)*Us + Us*Gam(r,a)))[p,q]))
K = sp.zeros(4*N, 4*N)
for s in sites:
    for a in range(2):
        for sgn, r in ((+1, wrap((s[0]+(a==0), s[1]+(a==1)))), (-1, wrap((s[0]-(a==0), s[1]-(a==1))))):
            blk = Lam(s, r, a); i, j = sid[s]*4, sid[r]*4
            for p in range(4):
                for q in range(4): K[i+p, j+q] += sgn*sp.Rational(1,2)*blk[p,q]
K = sp.Matrix(4*N,4*N, lambda i,j: lin(K[i,j]))
Dh = sp.zeros(4*N,4*N); Dhi = sp.zeros(4*N,4*N)
for s in sites:
    dd = Ddiag(s)
    for k in range(4):
        h = lin(sp.sqrt(dd[k])); Dh[sid[s]*4+k, sid[s]*4+k] = h; Dhi[sid[s]*4+k, sid[s]*4+k] = lin(1/h)
Kh = sp.Matrix(4*N,4*N, lambda i,j: lin((Dh*K*Dhi)[i,j]))
M = sp.Matrix(4*N,4*N, lambda i,j: lin(-sum(Kh[i,k]*Kh[k,j] for k in range(4*N))))
# ROW SUMS in the ORTHONORMAL frame = response to the constant mode = effective potential
def d2(s, ax):
    e = (1,0) if ax==0 else (0,1)
    return prof[wrap((s[0]+e[0], s[1]+e[1]))] + prof[wrap((s[0]-e[0], s[1]-e[1]))] - 2*prof[s]
def dxy(s):
    p = lambda dx,dy: prof[wrap((s[0]+dx, s[1]+dy))]
    return sp.Rational(1,4)*(p(1,1) - p(1,-1) - p(-1,1) + p(-1,-1))
print("row sums of -K_hat^2 (orthonormal frame) = effective potential, hops included", flush=True)
p_,q_,r_,t_ = sp.symbols("p_ q_ r_ t_")
rows = []
for s in sites:
    rs = sp.expand(sp.diff(sum(M[sid[s]*4, sid[r]*4] for r in range(N) for r in [r]) if False else
                           sum(M[sid[s]*4, j] for j in range(0, 4*N, 4)), eps_))
    rows.append((s, rs))
eqs = [sp.Eq(p_*d2(s,0)+q_*d2(s,1)+r_*prof[s]+t_*dxy(s), c) for s,c in rows[:4]]
sol = sp.solve(eqs, [p_,q_,r_,t_], dict=True)
print(f"fit of the effective potential: {sol}", flush=True)
if sol:
    P,Q,R_,T_ = sol[0][p_], sol[0][q_], sol[0][r_], sol[0][t_]
    ok = all(sp.expand(c-(P*d2(s,0)+Q*d2(s,1)+R_*prof[s]+T_*dxy(s))) == 0 for s,c in rows)
    print(f"  law = {P}*dxx + {Q}*dyy + {R_}*prof + {T_}*dxy ; holds everywhere: {ok}", flush=True)
    print(f"  linearised curvature for this h (h11=2a, h22=0) is R = -2*dyy a", flush=True)
    print(f"  => curvature-like iff dxx coefficient is 0 and dyy coefficient is nonzero", flush=True)
