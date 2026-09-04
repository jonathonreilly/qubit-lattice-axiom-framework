"""T3b — the CORRECTED variable-metric operator.
My first hop Gamma_d(s)U was NOT skew-adjoint; the algebra shows why, and what
is forced:  D_s M_(s<-r) = -(D_r M_(r<-s))^T  holds iff the hop is the
ENDPOINT-SYMMETRIC one
        Lam_(s<-r) = (1/2)[ Gamma_d(s) U_(s<-r) + U_(s<-r) Gamma_d(r) ].
(Proof used only Gamma D-self-adjoint and U a D-isometry.)  With that hop,
K = centred difference of Lam.  QUESTION: is K^2 still fiber-scalar for a
VARIABLE metric, and if not, is the defect the curvature?"""
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
lam = {}
vals = [1, sp.Rational(3,2), 2, sp.Rational(5,4), 1, sp.Rational(7,4), sp.Rational(3,2), 1,
        2, 1, sp.Rational(5,4), sp.Rational(3,2), 1, 1, 2, 1]
for i, s in enumerate(sites): lam[s] = sp.Integer(vals[i]) if isinstance(vals[i], int) else vals[i]
def Ds(s):
    l = lam[s]; return sp.diag(l**2, sp.Integer(1), sp.Integer(1), l**-2)
def Gam(s, a): return sp.Matrix(sp.expand(eps(a) + iota(a, sp.eye(2) / lam[s]**2)))
def U(s, r):
    q = lam[r] / lam[s]; return sp.diag(q, sp.Integer(1), sp.Integer(1), 1/q)
def Lam(s, r, a):
    Us = U(s, r)
    return sp.Rational(1,2) * (Gam(s, a) * Us + Us * Gam(r, a))
K = sp.zeros(4*N, 4*N)
def put(blk, s, r, sgn):
    i, j = sid[s]*4, sid[r]*4
    for p in range(4):
        for q in range(4): K[i+p, j+q] += sgn * blk[p, q]
for s in sites:
    for a in range(2):
        rp = wrap((s[0]+(a==0), s[1]+(a==1)))
        rm = wrap((s[0]-(a==0), s[1]-(a==1)))
        put(sp.Rational(1,2)*Lam(s, rp, a), s, rp, +1)
        put(sp.Rational(1,2)*Lam(s, rm, a), s, rm, -1)
Dg = sp.zeros(4*N, 4*N)
for s in sites:
    i = sid[s]*4; Db = Ds(s)
    for p in range(4):
        for q in range(4): Dg[i+p, i+q] = Db[p, q]
print(f"skew-adjoint  D K + K^T D = 0 : {sp.expand(Dg*K + K.T*Dg).is_zero_matrix}", flush=True)
K2 = sp.expand(K*K)
nons = []
for s in sites:
    for r in sites:
        blk = sp.Matrix(4,4, lambda p,q: K2[sid[s]*4+p, sid[r]*4+q])
        if blk.is_zero_matrix: continue
        if not sp.expand(blk - blk[0,0]*sp.eye(4)).is_zero_matrix: nons.append((s,r,blk))
print(f"K^2 fiber-scalar everywhere: {len(nons)==0}   (non-scalar blocks {len(nons)} of {N*N})", flush=True)
if nons:
    print("--- the DIAGONAL (on-site) part of K^2, which is where a curvature term would sit:", flush=True)
    for s in sites[:4]:
        blk = sp.Matrix(4,4, lambda p,q: K2[sid[s]*4+p, sid[s]*4+q])
        dev = sp.expand(blk - blk[0,0]*sp.eye(4))
        print(f"  s={s}: diag = {[sp.nsimplify(blk[i,i]) for i in range(4)]}  scalar={dev.is_zero_matrix}", flush=True)
    # compare the on-site deviation to a discrete curvature of log(lam)
    print("--- discrete curvature candidate  R ~ -2 lam^-2 * Laplacian(log lam):", flush=True)
    for s in sites[:4]:
        nb = [wrap((s[0]+1,s[1])), wrap((s[0]-1,s[1])), wrap((s[0],s[1]+1)), wrap((s[0],s[1]-1))]
        lapl = sum(sp.log(lam[n]) for n in nb) - 4*sp.log(lam[s])
        blk = sp.Matrix(4,4, lambda p,q: K2[sid[s]*4+p, sid[s]*4+q])
        d01 = sp.nsimplify(blk[0,0]-blk[1,1]); d12 = sp.nsimplify(blk[1,1]-blk[2,2]); d13 = sp.nsimplify(blk[1,1]-blk[3,3])
        print(f"  s={s}: lapl(log lam)={sp.simplify(lapl)}   deg0-deg1={d01}  deg1-deg2={d12}  deg1-deg3={d13}", flush=True)
