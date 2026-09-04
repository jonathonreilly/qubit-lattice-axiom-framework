"""T14 — ON-LOCUS vs OFF-LOCUS with an INHOMOGENEOUS carrier.
T13 showed a UNIFORM bench gives a flat record distribution (1/4 each) whether
on or off the propagation locus, so all the landed record structure must come
from the carrier's INHOMOGENEITY.  Test that directly.
Note: at rational shear the locus v^2 = 1 - c^2 is exactly the PYTHAGOREAN
locus - and the lane's own committed shears, 3/5 and 5/13, are Pythagorean
legs, so the matching on-locus volumes 4/5 and 12/13 are rational."""
import sympy as sp
R = sp.Rational
BAS = [(), (0,), (1,), (0,1)]; IDX = {b:i for i,b in enumerate(BAS)}
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
L = 4; N = L*L
sites = [(x,y) for x in range(L) for y in range(L)]
sid = {s:i for i,s in enumerate(sites)}
def wrap(s): return (s[0]%L, s[1]%L)
PYTH = {R(3,5): R(4,5), R(5,13): R(12,13), R(8,17): R(15,17), R(7,25): R(24,25)}
legs = list(PYTH.keys())
def shear(s): return legs[(3*s[0] + 2*s[1]) % len(legs)]
def vol_on(s):  return PYTH[shear(s)]                                  # ON  locus
def vol_off(s): return R(1 + ((3*s[0] + 2*s[1]) % 5), 3) + R(1,2)      # lane-style, OFF locus
def build(volf, m=R(1,2)):
    def Dof(s):
        cc, vv = shear(s), volf(s)
        g = sp.Matrix([[1, cc],[cc, 1]]); gi = g.inv()
        D = sp.zeros(4,4); D[0,0] = vv; D[3,3] = vv*gi.det()
        D[1,1] = vv*gi[0,0]; D[2,2] = vv*gi[1,1]; D[1,2] = vv*gi[0,1]; D[2,1] = vv*gi[1,0]
        return D, gi
    def Gam(s, a):
        _, gi = Dof(s); return sp.Matrix(sp.expand(epsm(a) + iota(a, gi)))
    def Utr(s, r):
        Ds, _ = Dof(s); Dr, _ = Dof(r)
        # transport must satisfy U^T D_s U = D_r ; use the symmetric positive solution
        Ds12 = Ds.pow(R(1,2)) if False else None
        # diagonalise numerically-exactly: both are symmetric 4x4, use Cholesky-like route
        Ls = Ds.cholesky(hermitian=False); Lr = Dr.cholesky(hermitian=False)
        return sp.Matrix(sp.expand(Ls.inv().T * Lr.T))
    K = sp.zeros(4*N, 4*N)
    for s in sites:
        for a in range(2):
            for sgn, r in ((+1, wrap((s[0]+(a==0), s[1]+(a==1)))), (-1, wrap((s[0]-(a==0), s[1]-(a==1))))):
                U = Utr(s, r)
                blk = R(1,2)*(Gam(s,a)*U + U*Gam(r,a))
                i, j = sid[s]*4, sid[r]*4
                for p in range(4):
                    for q in range(4): K[i+p, j+q] += sgn*R(1,2)*blk[p,q]
    Q = sp.Matrix(4*N,4*N, lambda i,j: (m if i==j else 0) + K[i,j])
    Qi = Q.inv()
    out = []
    for s in sites:
        i = sid[s]*4
        blk = sp.Matrix(4,4, lambda p,q: R(1,2)*(Qi[i+p,i+q] + Qi[i+q,i+p]))
        tot = sum(blk[k,k] for k in range(4))
        out.append((s, [sp.cancel(blk[k,k]/tot) for k in range(4)]))
    return out
for nm, volf in (("ON  locus (v = sqrt(1-c^2), Pythagorean)", vol_on),
                 ("OFF locus (lane-style graded volumes)", vol_off)):
    w = build(volf)
    spreads = [sp.nsimplify(max(x)-min(x)) for _, x in w]
    mx = max(spreads, key=lambda z: abs(float(z)))
    print(f"{nm}:", flush=True)
    print(f"   max within-site spread over degrees = {mx}  ({float(mx):.6f})", flush=True)
    print(f"   site (0,0) weights = {[str(x) for x in w[0][1]]}", flush=True)
    allflat = all(sp.simplify(sprd) == 0 for sprd in spreads)
    print(f"   record distribution FLAT at every site: {allflat}", flush=True)
